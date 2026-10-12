"""Does tools/render.py's MP4 show the right clip frame at the right time, with the sounds where the scenes put them?

usage: python lessons/_mediatest/tests/render_sync.py [--no-render] [--workers 4]

Renders lessons/_mediatest with tools/render.py (unless --no-render), then reads out/lesson.mp4 back with ffmpeg:
- Picture. Every 2nd frame of scene 02 (clip2 at native size, media time T - 12.95) and every 3rd of scene 05
  (clip2 scaled into 660x371 at (1170, 260), media time T - 47.0): the clip region is compared with ffmpeg's decode
  of clip frames n - 1, n, n + 1 (n = the frame the scene formula asks for at T = i / 30). Right frame = closest to n.
- Sound. The lesson clock (mix.mp3) ticks at 1 kHz on every whole second; the exhibit beeps.mp3 bursts at 2 kHz on
  every whole second of the sound, heard at (T - 25.2) - 0.5 in scene 03 and T - 47.0 in scene 05. Onsets of both are
  measured in the MP4's audio (complex demodulation, 2 ms window, half-peak crossing) and compared with where they
  belong; a 2 kHz burst anywhere else is a failure.
Writes out/tests/render_sync.json.
"""
import argparse
import json
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
L = HERE.parent
ROOT = L.parent.parent
CLIP = L / 'assets' / 'video' / 'clip.mp4'
MP4 = L / 'out' / 'lesson.mp4'
OUT = L / 'out' / 'tests'
FPS, CFPS, SR = 30, 24, 44100
W, H = 960, 540
# a frame is only scored when its neighbours differ from it by at least this much (mean abs difference, 0-255):
# the clip has near-duplicate frames (50 and 51 differ by 0.36), which two lossy encodes cannot tell apart
DISTINCT = 1.0


def ref_frames():
    vf = f'scale={W}:{H}:in_color_matrix=bt601:in_range=limited:out_range=full:flags=bilinear+accurate_rnd+full_chroma_int,format=rgb24'
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(CLIP), '-vf', vf, '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(np.int16)


def mp4_crops(frames, x, y, w, h):
    """the given output frames of the MP4 (an arithmetic run: first, first + step, ... last), cropped"""
    a, b, step = frames[0], frames[-1], frames[1] - frames[0]
    assert list(frames) == list(range(a, b + 1, step))
    sel = f'between(n\\,{a}\\,{b})*not(mod(n-{a}\\,{step}))'
    vf = f"select='{sel}',crop={w}:{h}:{x}:{y},scale=in_range=limited:out_range=full:in_color_matrix=bt601,format=rgb24"
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(MP4), '-vf', vf, '-fps_mode', 'passthrough', '-f', 'rawvideo', '-'],
                         capture_output=True, check=True).stdout
    arr = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.int16)
    assert len(arr) == len(frames), (len(arr), len(frames))
    return dict(zip(frames, arr))


def frame_n(m, frames=240):
    return int(min(max(np.floor(m * CFPS + 1e-6), 0), frames - 1))


def picture(ref):
    rows = []
    # scene 02: native size at (480, 270); drawn alone from 13.5 to 24.9
    f2 = [i for i in range(int(13.6 * FPS), int(24.8 * FPS)) if i % 2 == 0]
    crops = mp4_crops(f2, 480, 270, W, H)
    for i in f2:
        n = frame_n(i / FPS - 12.95)
        d = {k: float(np.abs(crops[i] - ref[k]).mean()) for k in (n - 1, n, n + 1) if 0 <= k < len(ref)}
        sep = min(float(np.abs(ref[k] - ref[n]).mean()) for k in d if k != n)
        rows.append({'scene': '02', 'frame': i, 'T': round(i / FPS, 4), 'n': n, 'mad': {str(k): round(v, 3) for k, v in d.items()},
                     'neighbour_sep': round(sep, 3), 'distinct': sep >= DISTINCT, 'right': min(d, key=d.get) == n})
    # scene 05: contain-fit into 660x371 at (1170, 260), r 14, outline: compare the inside, away from the corners
    s = min(660 / W, 371 / H)
    dw, dh = W * s, H * s
    ox, oy = 1170 + (660 - dw) / 2, 260 + (371 - dh) / 2
    cx, cy, cw, ch = 1190, 280, 620, 330
    f5 = [i for i in range(int(46.4 * FPS), int(57.0 * FPS)) if i % 3 == 0]
    crops = mp4_crops(f5, cx, cy, cw, ch)
    small = {}

    def scaled(k):   # reference frame k drawn the way the canvas places it, cropped like the MP4
        if k not in small:
            im = Image.fromarray(ref[k].astype(np.uint8)).resize((round(dw), round(dh)), Image.BILINEAR)
            a = np.asarray(im, np.int16)
            small[k] = a[cy - round(oy):cy - round(oy) + ch, cx - round(ox):cx - round(ox) + cw]
        return small[k]
    for i in f5:
        n = frame_n(i / FPS - 47.0)
        d = {k: float(np.abs(crops[i] - scaled(k)).mean()) for k in (n - 1, n, n + 1) if 0 <= k < len(ref)}
        sep = min(float(np.abs(scaled(k) - scaled(n)).mean()) for k in d if k != n)
        rows.append({'scene': '05', 'frame': i, 'T': round(i / FPS, 4), 'n': n, 'mad': {str(k): round(v, 3) for k, v in d.items()},
                     'neighbour_sep': round(sep, 3), 'distinct': sep >= DISTINCT, 'right': min(d, key=d.get) == n,
                     'held': (i / FPS - 47.0) < 0 or (i / FPS - 47.0) >= 10})
    return rows


def envelope(x, f, burst):
    """matched filter for a burst of `burst` seconds of an f Hz tone: demodulate, then average over exactly the
    burst length (that window nulls every multiple of 1 / burst Hz, so the other test tone cannot leak in)"""
    t = np.arange(len(x)) / SR
    z = x * np.exp(-2j * np.pi * f * t)
    k = int(round(burst * SR))
    return np.abs(np.convolve(z, np.ones(k) / k, mode='same'))


def onsets(env, thr, burst):
    """burst start times: each run above thr peaks when the window covers the whole burst, i.e. at its centre"""
    on = env > thr
    edges = np.flatnonzero(np.diff(on.astype(np.int8)) == 1) + 1
    ends = np.flatnonzero(np.diff(on.astype(np.int8)) == -1) + 1
    out = []
    for s0 in edges:
        e = ends[ends > s0]
        e0 = e[0] if len(e) else len(env)
        out.append((s0 + int(np.argmax(env[s0:e0]))) / SR - burst / 2)
    return out


def sound():
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(MP4), '-map', '0:a', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64)
    res = {'audio_seconds': round(len(x) / SR, 4)}
    for name, f, burst, expect in (('ticks (lesson clock, mix.mp3)', 1000, 0.02, [float(k) for k in range(0, 58)]),
                                   ('beeps (sound exhibit)', 2000, 0.06, [25.7 + k for k in range(11)] + [47.0 + k for k in range(11)])):
        env = envelope(x, f, burst)
        got = onsets(env, 0.5 * env.max(), burst)
        pairs, extra = [], []
        for g in got:
            e = min(expect, key=lambda v: abs(v - g))
            (pairs if abs(e - g) < 0.1 else extra).append((e, g))
        missing = [e for e in expect if all(abs(e - g) >= 0.1 for g in got)]
        errs = [1000 * (g - e) for e, g in pairs]
        res[name] = {'expected': len(expect), 'found': len(pairs), 'missing': missing, 'unexpected': [round(g, 4) for _, g in extra],
                     'error_ms': {'mean': round(float(np.mean(errs)), 2), 'max_abs': round(float(np.max(np.abs(errs))), 2)} if errs else None,
                     'per_onset_ms': {f'{e:.2f}': round(1000 * (g - e), 2) for e, g in pairs}}
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-render', action='store_true')
    ap.add_argument('--workers', type=int, default=4)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if not a.no_render:
        r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'render.py'), '_mediatest', '--workers', str(a.workers)],
                           capture_output=True, text=True, cwd=str(ROOT))
        print(r.stdout.strip(), r.stderr.strip()[-1500:])
        if r.returncode:
            raise SystemExit('render.py failed')
    v = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,duration,nb_frames', '-of', 'json', str(MP4)],
                                  capture_output=True, text=True, check=True).stdout)
    rows = picture(ref_frames())
    snd = sound()
    pic = {sc: {'checked': sum(r['scene'] == sc and r['distinct'] for r in rows),
                'right': sum(r['right'] for r in rows if r['scene'] == sc and r['distinct']),
                'indistinct_skipped': sum(r['scene'] == sc and not r['distinct'] for r in rows),
                'indistinct_right_anyway': sum(r['right'] for r in rows if r['scene'] == sc and not r['distinct']),
                'mean_mad_n': round(float(np.mean([r['mad'][str(r['n'])] for r in rows if r['scene'] == sc])), 3)} for sc in ('02', '05')}
    summary = {'mp4_streams': v['streams'], 'picture': pic, 'sound': {k: (dict((kk, vv) for kk, vv in s.items() if kk != 'per_onset_ms') if isinstance(s, dict) else s) for k, s in snd.items()}}
    (OUT / 'render_sync.json').write_text(json.dumps({'summary': summary, 'rows': rows, 'sound': snd}, indent=1), encoding='utf-8')
    print(json.dumps(summary, indent=1))
    ok = all(p['right'] == p['checked'] for p in pic.values())
    for k, s in snd.items():
        if isinstance(s, dict):
            ok &= not s['missing'] and not s['unexpected'] and s['error_ms'] is not None and s['error_ms']['max_abs'] <= 12
    print('PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
