"""render.py: lesson -> MP4 (1080p, the mixed narration, soft English subtitles).

usage: python tools/render.py <lesson> [--fps 30] [--workers 4] [--from 0 --to 20] [--captions]

Each worker is its own headless Chromium that seeks frames from time alone
(window.__frame), so the frame range is split across workers and the pieces are
joined losslessly at the end. Writes out/lesson.mp4, and out/lesson-720.mp4 when the
1080p file is too big for Cloudflare Pages (25 MB per file).
"""
import argparse
import base64
import multiprocessing as mp
import pathlib
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import Server, ffmpeg, lesson_dir, open_lesson  # noqa: E402

PAGES_LIMIT = 24 * 1024 * 1024


def work(job):
    url, start, end, fps, seg = job
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser, page, errors = open_lesson(p, url)
        ff = subprocess.Popen([ffmpeg(), '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(fps),
                               '-g', str(fps * 4), str(seg)], stdin=subprocess.PIPE)
        for i in range(start, end):
            data = page.evaluate('([t, q]) => window.__frame(t, q)', [i / fps, 0.93])
            ff.stdin.write(base64.b64decode(data.split(',', 1)[1]))
        ff.stdin.close()
        ff.wait()
        browser.close()
    return seg, errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson')
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--from', dest='t0', type=float, default=0)
    ap.add_argument('--to', dest='t1', type=float)
    ap.add_argument('--captions', action='store_true', help='burn captions into the picture')
    ap.add_argument('--out')
    a = ap.parse_args()
    L = lesson_dir(a.lesson)
    out_dir = L / 'out'
    out_dir.mkdir(exist_ok=True)
    mix = L / 'audio' / 'mix.mp3'
    started = time.time()

    srv = Server()
    url = srv.url(L, 'render=1' + ('&captions=1' if a.captions else ''))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser, page, errors = open_lesson(p, url)
        meta = page.evaluate('window.__meta')
        browser.close()
    fps = a.fps
    t1 = a.t1 if a.t1 is not None else meta['DUR']
    f0, f1 = int(a.t0 * fps), int(t1 * fps)
    n = f1 - f0
    per = (n + a.workers - 1) // a.workers
    jobs = []
    for w in range(a.workers):
        s, e = f0 + w * per, min(f1, f0 + (w + 1) * per)
        if s < e:
            jobs.append((url, s, e, fps, str(out_dir / f'seg{w}.mp4')))
    print(f'{L.name}: {n} frames ({n / fps:.1f}s) on {len(jobs)} workers', flush=True)
    with mp.get_context('spawn').Pool(len(jobs)) as pool:
        results = pool.map(work, jobs)
    srv.close()
    for _, errs in results:
        for e in dict.fromkeys(errs):
            print('  page:', e)

    lst = out_dir / 'segments.txt'
    lst.write_text(''.join(f"file '{pathlib.Path(s).name}'\n" for s, _ in results), encoding='utf-8')
    final = pathlib.Path(a.out) if a.out else out_dir / ('lesson.mp4' if a.t0 == 0 and a.t1 is None else 'clip.mp4')
    cmd = [ffmpeg(), '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst)]
    has_audio = mix.exists()
    vtt = L / 'captions.vtt'
    if has_audio:
        cmd += ['-ss', str(a.t0), '-t', str(n / fps), '-i', str(mix)]
    if has_audio and vtt.exists() and a.t0 == 0 and not a.captions:
        cmd += ['-i', str(vtt), '-map', '0:v', '-map', '1:a', '-map', '2:s', '-c:s', 'mov_text', '-metadata:s:s:0', 'language=eng']
    elif has_audio:
        cmd += ['-map', '0:v', '-map', '1:a']
    cmd += ['-c:v', 'copy']
    if has_audio:
        # no -shortest: the subtitle stream ends at the last caption and would cut the video
        cmd += ['-c:a', 'aac', '-b:a', '160k']
    cmd += ['-movflags', '+faststart', str(final)]
    subprocess.run(cmd, check=True)
    for s, _ in results:
        pathlib.Path(s).unlink(missing_ok=True)
    lst.unlink(missing_ok=True)
    size = final.stat().st_size
    print(f'wrote {final} ({size / 1e6:.1f} MB) in {time.time() - started:.0f}s')
    if final.name == 'lesson.mp4' and size > PAGES_LIMIT:
        web = out_dir / 'lesson-720.mp4'
        subprocess.run([ffmpeg(), '-v', 'error', '-y', '-i', str(final), '-map', '0', '-vf', 'scale=1280:720', '-c:v', 'libx264',
                        '-crf', '26', '-preset', 'slow', '-c:a', 'copy', '-c:s', 'copy', '-movflags', '+faststart', str(web)], check=True)
        if web.stat().st_size > PAGES_LIMIT:
            # long lessons (over ~10 min) overshoot at CRF 26: two-pass to a bitrate that fits (22 MiB: x264 overshoots ~5%)
            secs = (f1 - f0) / fps
            vk = int((22 * 1024 * 1024 * 8 / secs - 64_000) / 1000)
            log = out_dir / 'x264-2pass'
            base = [ffmpeg(), '-v', 'error', '-y', '-i', str(final), '-vf', 'scale=1280:720', '-c:v', 'libx264',
                    '-b:v', f'{vk}k', '-preset', 'slow', '-passlogfile', str(log)]
            subprocess.run(base + ['-pass', '1', '-an', '-f', 'mp4', 'NUL' if sys.platform == 'win32' else '/dev/null'], check=True)
            subprocess.run(base + ['-pass', '2', '-map', '0', '-c:a', 'aac', '-b:a', '64k', '-c:s', 'copy',
                                   '-movflags', '+faststart', str(web)], check=True)
            for f in out_dir.glob('x264-2pass*'):
                f.unlink(missing_ok=True)
        print(f'1080p is over the Pages limit; web copy {web} ({web.stat().st_size / 1e6:.1f} MB)')


if __name__ == '__main__':
    main()
