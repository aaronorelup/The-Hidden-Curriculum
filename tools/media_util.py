"""media_util.py: prepare and check the media exhibits a lesson shows (K.video, K.image, K.listen / K.sound).

usage:
  python tools/media_util.py encode  <src> <dst.mp4> [--from S] [--to S] [--fps 30] [--width 1280] [--crf 18]
  python tools/media_util.py audio   <src> <dst.mp3> [--from S] [--to S] [--lufs -16]
  python tools/media_util.py spectrogram <audio> <dst.webp>       (name it assets/img/spec_<sound>.webp)
  python tools/media_util.py still   <src image> <dst.webp> [--width 1600] [--quality 90 | --lossless]
  python tools/media_util.py record  <dst.mp4> --seconds 8 (--window "part of its title" | --region x,y,w,h) [--fps 30]
  python tools/media_util.py check   <file.mp4> [...]               (exit 1 when a clip breaks the spec)

The clip spec (lessons/10-16-what-opus-made-this-leaves-out/MEDIA.md, engine/KIT.md "Media exhibits"):
H.264 High, yuv420p limited range, GOP 12 (-g 12 -keyint_min 12 -sc_threshold 0), no B-frames, +faststart, even
dimensions, constant frame rate, no audio track (a clip's sound is a separate sounds:{} MP3 made by `audio`), under
Cloudflare Pages' 25 MB per file. Colour: converted with the BT.601 matrix and tagged smpte170m, because Chromium's
2D canvas (the renderer's path and the live player's) decodes BT.601 exactly (mean error 0.34 / 255 on colour bars,
2026-10-12) but a BT.709-matrix clip comes out off (2.4 when tagged, 6.1 untagged). Why GOP 12 and no B-frames:
the renderer seeks every frame, and a seek decodes from the previous keyframe, so a short GOP keeps a frame cheap;
without B-frames the decode order is the display order and the MP4 needs no edit list.
Sounds: 44.1 kHz stereo MP3 192 kbps, one linear gain to -16 LUFS (the narration mix's level).
"""
import argparse
import json
import pathlib
import re
import shutil
import struct
import subprocess
import sys

PAGES_LIMIT = 25 * 1000 * 1000          # Cloudflare Pages: 25 MiB per file; stay under 25 MB to be safe
GOP = 12
X264 = ['-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-g', str(GOP), '-keyint_min', str(GOP),
        '-sc_threshold', '0', '-bf', '0', '-movflags', '+faststart']
# BT.601 matrix, limited range, tagged (primaries and transfer as sRGB screens are: bt709)
COLOUR = 'out_color_matrix=bt601:out_range=tv'
TAGS = 'setparams=colorspace=smpte170m:color_primaries=bt709:color_trc=bt709:range=tv'
SPECTRUM = 'showspectrumpic=s=1600x400:legend=0:mode=combined:color=intensity:scale=log:fscale=lin:win_func=hann:stop=11025'


def ffmpeg():
    return shutil.which('ffmpeg') or 'ffmpeg'


def ffprobe():
    return shutil.which('ffprobe') or 'ffprobe'


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode:
        raise SystemExit(f'failed: {" ".join(map(str, cmd))}\n{r.stderr[-2000:]}')
    return r


def probe(path):
    """the first video and audio stream of a file, plus format info (ffprobe JSON)"""
    r = run([ffprobe(), '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)])
    d = json.loads(r.stdout)
    v = next((s for s in d['streams'] if s['codec_type'] == 'video'), None)
    a = next((s for s in d['streams'] if s['codec_type'] == 'audio'), None)
    return {'video': v, 'audio': a, 'format': d['format']}


def trim_args(t0, t1):
    out = []
    if t0 is not None:
        out += ['-ss', str(t0)]
    if t1 is not None:
        out += ['-t', str(t1 - (t0 or 0))]
    return out


# ------------------------------------------------------------------ video
def encode(src, dst, t0=None, t1=None, fps=None, width=None, height=None, crf=18, preset='slow'):
    """any video (screen recording, render, game capture) -> an exhibit clip that meets the spec"""
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    info = probe(src)['video']
    if not info:
        raise SystemExit(f'{src}: no video stream')
    w, h = int(info['width']), int(info['height'])
    if width and not height:
        height = round(h * width / w / 2) * 2
    elif height and not width:
        width = round(w * height / h / 2) * 2
    width, height = width or w - w % 2, height or h - h % 2
    vf = []
    if fps:
        vf.append(f'fps={fps}')
    vf += [f'scale={width}:{height}:flags=lanczos+accurate_rnd+full_chroma_int:{COLOUR}', 'format=yuv420p', TAGS]
    run([ffmpeg(), '-v', 'error', '-y', *trim_args(t0, t1), '-i', str(src), '-map', '0:v:0', '-an', '-sn', '-dn',
         '-vf', ','.join(vf), *X264, '-crf', str(crf), '-preset', preset, '-fps_mode', 'cfr', str(dst)])
    problems = check(dst)
    print(f'wrote {dst} ({dst.stat().st_size / 1e6:.2f} MB, {width}x{height})' + (f'; PROBLEMS: {problems}' if problems else ''))
    return problems


def top_boxes(path):
    """the top-level MP4 boxes in order (faststart puts moov before mdat)"""
    out = []
    with open(path, 'rb') as f:
        while True:
            hd = f.read(8)
            if len(hd) < 8:
                break
            size, kind = struct.unpack('>I4s', hd)
            if size == 1:
                size = struct.unpack('>Q', f.read(8))[0]
                f.seek(size - 16, 1)
            elif size == 0:
                out.append(kind.decode('latin-1'))
                break
            else:
                f.seek(size - 8, 1)
            out.append(kind.decode('latin-1'))
    return out


def check(path):
    """[] when the clip meets the spec, else a list of problems"""
    path = pathlib.Path(path)
    p = probe(path)
    v, problems = p['video'], []
    if not v:
        return ['no video stream']
    if v.get('codec_name') != 'h264':
        problems.append(f"codec {v.get('codec_name')} (want h264)")
    if v.get('profile') != 'High':
        problems.append(f"profile {v.get('profile')} (want High)")
    if v.get('pix_fmt') != 'yuv420p':
        problems.append(f"pix_fmt {v.get('pix_fmt')} (want yuv420p)")
    if v.get('color_range') not in (None, 'tv', 'unknown'):
        problems.append(f"color_range {v.get('color_range')} (want tv / limited)")
    if v.get('color_space') not in ('smpte170m', 'bt470bg'):
        cs = v.get('color_space') or 'untagged'
        problems.append(f"colour matrix {cs} (want BT.601, tagged smpte170m: the canvas decodes it exactly; `encode` converts and tags)")
    if int(v.get('has_b_frames') or 0):
        problems.append(f"has_b_frames {v.get('has_b_frames')} (want 0)")
    if int(v['width']) % 2 or int(v['height']) % 2:
        problems.append(f"odd size {v['width']}x{v['height']}")
    if v.get('r_frame_rate') != v.get('avg_frame_rate'):
        problems.append(f"variable frame rate? r {v.get('r_frame_rate')} avg {v.get('avg_frame_rate')}")
    if p['audio']:
        problems.append('has an audio track (clips are muted: put the sound in sounds:{} with `audio`)')
    boxes = top_boxes(path)
    if 'moov' in boxes and 'mdat' in boxes and boxes.index('moov') > boxes.index('mdat'):
        problems.append('moov after mdat (want +faststart)')
    # keyframes every GOP frames, exactly
    r = run([ffprobe(), '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'packet=flags', '-of', 'csv=p=0', str(path)])
    flags = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    keys = [i for i, f in enumerate(flags) if 'K' in f]
    gaps = sorted(set(b - a for a, b in zip(keys, keys[1:])))
    if not keys or keys[0] != 0 or (gaps and gaps != [GOP]):
        problems.append(f'keyframe gaps {gaps} (want every {GOP})')
    size = path.stat().st_size
    if size > PAGES_LIMIT:
        problems.append(f'{size / 1e6:.1f} MB (Cloudflare Pages takes at most 25 MB per file)')
    return problems


WINDOW_RECT_PS = r'''
Add-Type @"
using System; using System.Runtime.InteropServices;
public class HcWin {
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int size);
  public struct RECT { public int L, T, R, B; }
}
"@
[HcWin]::SetProcessDPIAware() | Out-Null
$p = Get-Process | Where-Object { $_.MainWindowHandle -ne 0 -and $_.MainWindowTitle -like $env:HC_TITLE } | Select-Object -First 1
if (-not $p) { exit 3 }
$r = New-Object HcWin+RECT
[HcWin]::DwmGetWindowAttribute($p.MainWindowHandle, 9, [ref]$r, 16) | Out-Null
"$($r.L),$($r.T),$($r.R - $r.L),$($r.B - $r.T),$($p.MainWindowTitle)"
'''


def window_rect(title):
    """the visible frame (DWM extended frame bounds, physical pixels) of the first window whose title contains
    `title`: (x, y, w, h, full title). Windows only."""
    import os
    r = subprocess.run(['powershell', '-NoProfile', '-Command', WINDOW_RECT_PS], capture_output=True, text=True,
                       env={**os.environ, 'HC_TITLE': f'*{title}*'})
    if r.returncode or not r.stdout.strip():
        raise SystemExit(f'no window with "{title}" in its title')
    x, y, w, h, full = r.stdout.strip().split(',', 4)
    return int(x), int(y), int(w), int(h), full


def record(dst, seconds, window=None, region=None, fps=30, crf=18):
    """screen recording on Windows: a desktop region x,y,w,h, or the region a window covers (found by part of its
    title; it must be on top, unobstructed), captured from the composited desktop with ffmpeg gdigrab (a window
    capture, gdigrab title=..., comes out black for GPU-drawn windows such as Chromium, tested 2026-10-12), then
    encoded to the clip spec. Make the window the size it will be shown (1280x720 for a full-screen exhibit)."""
    dst = pathlib.Path(dst)
    raw = dst.with_suffix('.raw.mkv')
    if window:
        x, y, w, h, full = window_rect(window)
        print(f'recording "{full}" at {x},{y} {w}x{h}')
    else:
        x, y, w, h = (int(n) for n in region.split(','))
    w, h = w - w % 2, h - h % 2
    grab = ['-f', 'gdigrab', '-framerate', str(fps), '-draw_mouse', '1',
            '-offset_x', str(x), '-offset_y', str(y), '-video_size', f'{w}x{h}', '-i', 'desktop']
    run([ffmpeg(), '-v', 'error', '-y', *grab, '-t', str(seconds), '-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast', str(raw)])
    try:
        return encode(raw, dst, fps=fps, crf=crf)
    finally:
        raw.unlink(missing_ok=True)


# ------------------------------------------------------------------ audio
def loudness(path):
    """integrated loudness (LUFS) and true peak (dBTP) of a file, measured by ffmpeg's ebur128"""
    r = subprocess.run([ffmpeg(), '-hide_banner', '-nostats', '-i', str(path), '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    tail = r.stderr[r.stderr.rfind('Summary:'):]
    i = re.search(r'I:\s+(-?[\d.]+|-inf) LUFS', tail)
    pk = re.search(r'Peak:\s+(-?[\d.]+|-inf) dBFS', tail)
    return (float(i.group(1)) if i else None), (float(pk.group(1)) if pk else None)


def audio(src, dst, t0=None, t1=None, lufs=-16.0):
    """a sound exhibit: 44.1 kHz stereo MP3 192 kbps at one linear gain to `lufs` (the narration mix's level)"""
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    wav = dst.with_suffix('.tmp.wav')
    run([ffmpeg(), '-v', 'error', '-y', *trim_args(t0, t1), '-i', str(src), '-map', '0:a:0', '-ac', '2', '-ar', '44100', str(wav)])
    try:
        i, _ = loudness(wav)
        gain = 0.0 if i is None or i == float('-inf') else lufs - i
        for _ in range(3):          # the MP3 encode moves the loudness a little: re-trim until within 0.05 LU
            run([ffmpeg(), '-v', 'error', '-y', '-i', str(wav), '-af', f'volume={gain:.3f}dB', '-c:a', 'libmp3lame', '-b:a', '192k',
                 '-ar', '44100', str(dst)])
            i2, peak = loudness(dst)
            if i2 is None or i2 == float('-inf') or abs(i2 - lufs) <= 0.05:
                break
            gain += lufs - i2
    finally:
        wav.unlink(missing_ok=True)
    note = f'; true peak {peak:+.1f} dBTP: lower --lufs or limit it first' if peak is not None and peak > -1.0 else ''
    print(f'wrote {dst} ({dst.stat().st_size / 1e6:.2f} MB, {i2} LUFS, gain {gain:+.2f} dB){note}')


def spectrogram(src, dst):
    """the K.listen strip picture: 1600x400, 0-11 kHz, the same settings for every sound (MEDIA.md)"""
    from PIL import Image
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    png = dst.with_suffix('.tmp.png')
    run([ffmpeg(), '-v', 'error', '-y', '-i', str(src), '-lavfi', SPECTRUM, str(png)])
    try:
        Image.open(png).convert('RGB').save(dst, quality=88, method=6)
    finally:
        png.unlink(missing_ok=True)
    print(f'wrote {dst} ({dst.stat().st_size / 1e3:.0f} KB)')


def still(src, dst, width=None, quality=90, lossless=False):
    """a screenshot or photo -> WebP at display size (lossless keeps UI text crisp)"""
    from PIL import Image
    dst = pathlib.Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src)
    im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
    if width and im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(dst, lossless=lossless, quality=100 if lossless else quality, method=6)
    print(f'wrote {dst} ({dst.stat().st_size / 1e3:.0f} KB, {im.width}x{im.height})')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    e = sub.add_parser('encode'); e.add_argument('src'); e.add_argument('dst')
    e.add_argument('--from', dest='t0', type=float); e.add_argument('--to', dest='t1', type=float)
    e.add_argument('--fps', type=float); e.add_argument('--width', type=int); e.add_argument('--height', type=int)
    e.add_argument('--crf', type=int, default=18); e.add_argument('--preset', default='slow')
    a = sub.add_parser('audio'); a.add_argument('src'); a.add_argument('dst')
    a.add_argument('--from', dest='t0', type=float); a.add_argument('--to', dest='t1', type=float)
    a.add_argument('--lufs', type=float, default=-16.0)
    s = sub.add_parser('spectrogram'); s.add_argument('src'); s.add_argument('dst')
    st = sub.add_parser('still'); st.add_argument('src'); st.add_argument('dst'); st.add_argument('--width', type=int)
    st.add_argument('--quality', type=int, default=90); st.add_argument('--lossless', action='store_true')
    r = sub.add_parser('record'); r.add_argument('dst'); r.add_argument('--seconds', type=float, required=True)
    r.add_argument('--window'); r.add_argument('--region'); r.add_argument('--fps', type=int, default=30)
    r.add_argument('--crf', type=int, default=18)
    c = sub.add_parser('check'); c.add_argument('files', nargs='+')
    o = ap.parse_args()
    if o.cmd == 'encode':
        sys.exit(1 if encode(o.src, o.dst, o.t0, o.t1, o.fps, o.width, o.height, o.crf, o.preset) else 0)
    elif o.cmd == 'audio':
        audio(o.src, o.dst, o.t0, o.t1, o.lufs)
    elif o.cmd == 'spectrogram':
        spectrogram(o.src, o.dst)
    elif o.cmd == 'still':
        still(o.src, o.dst, o.width, o.quality, o.lossless)
    elif o.cmd == 'record':
        if not (o.window or o.region):
            raise SystemExit('record: give --window "Title" or --region x,y,w,h')
        sys.exit(1 if record(o.dst, o.seconds, o.window, o.region, o.fps, o.crf) else 0)
    elif o.cmd == 'check':
        bad = 0
        for f in o.files:
            pr = check(f)
            bad += bool(pr)
            print(f'{f}: ' + ('OK' if not pr else 'PROBLEMS: ' + '; '.join(pr)))
        sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
