"""render.py: lesson -> MP4 (1080p, the mixed narration, soft English subtitles).

usage: python tools/render.py <lesson> [--fps 30] [--workers 4] [--from 0 --to 20] [--captions]

Each worker is its own headless Chromium that seeks frames from time alone
(window.__frame), so the frame range is split across workers and the pieces are
joined losslessly at the end. Writes out/lesson.mp4, and out/lesson-720.mp4 when the
1080p file is too big for Cloudflare Pages (25 MB per file).

Media exhibits: a frame that shows video waits until every clip is on its exact frame (window.__frame
returns a promise then). A lesson with sounds:{} also records, after every frame, which sounds the
scenes asked for (window.__heard()); each stretch where a sound's time runs with the lesson clock
is cut from its file and mixed over audio/mix.mp3, sample-accurately (sound_stretches, sound_track).

3D shots: before rendering it warns about any blender/<shot>.py clip that no longer matches its script or the course
map it was built from (tools/blender_shot.py stale_shots; re-render that shot first).
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
    url, start, end, fps, seg, listen = job
    from playwright.sync_api import sync_playwright
    heard = {}
    with sync_playwright() as p:
        browser, page, errors = open_lesson(p, url)
        ff = subprocess.Popen([ffmpeg(), '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(fps),
                               '-g', str(fps * 4), str(seg)], stdin=subprocess.PIPE)
        for i in range(start, end):
            if listen:
                data, h = page.evaluate('async ([t, q]) => [await window.__frame(t, q), window.__heard()]', [i / fps, 0.93])
                if h:
                    heard[i] = h
            else:
                data = page.evaluate('([t, q]) => window.__frame(t, q)', [i / fps, 0.93])
            ff.stdin.write(base64.b64decode(data.split(',', 1)[1]))
        ff.stdin.close()
        ff.wait()
        browser.close()
    return seg, errors, heard


def sound_stretches(heard, fps, min_frames=2):
    """frames -> stretches: {frame: [[name, seconds into the sound, gain], ...]} becomes
    [(name, first frame, frame count, seconds into the sound at the first frame, gain)], one per run of frames
    where the sound's time advances by exactly one frame per frame (1x). Held or jumping times stay silent,
    as in the live player (player.js syncSounds)."""
    out, runs = [], {}
    for i in sorted(heard):
        now = {n: (m, g) for n, m, g in heard[i]}
        for n in list(runs):
            first, count, m0, g, last_m = runs[n]
            if n in now and first + count == i and abs(now[n][0] - last_m - 1 / fps) < 1e-3:
                runs[n] = (first, count + 1, m0, g, now[n][0])
                del now[n]
            else:
                if count >= min_frames:
                    out.append((n, first, count, m0, g))
                del runs[n]
        for n, (m, g) in now.items():
            runs[n] = (i, 1, m, g, m)
    for n, (first, count, m0, g, _) in runs.items():
        if count >= min_frames:
            out.append((n, first, count, m0, g))
    return sorted(out, key=lambda s: (s[1], s[0]))


def sound_track(stretches, srcs, f0, fps, base_input, n_frames, first_input):
    """ffmpeg inputs + filter graph that lay every stretch over the base audio (input number base_input, or
    silence when it is None), each at its frame's time, sample-accurate, with 10 ms fades against clicks.
    Returns (extra input args, filter_complex, output label)."""
    inputs, chains, labels = [], [], []
    sr = 44100
    for k, (name, first, count, m0, gain) in enumerate(stretches):
        inputs += ['-i', srcs[name]]
        d, at = count / fps, (first - f0) / fps
        fade = min(0.01, d / 4)
        chains.append(f'[{first_input + k}:a]atrim=start={m0:.6f}:duration={d:.6f},asetpts=PTS-STARTPTS,'
                      f'aformat=sample_rates={sr}:channel_layouts=stereo,afade=t=in:d={fade:.4f},'
                      f'afade=t=out:st={max(0.0, d - fade):.6f}:d={fade:.4f},volume={gain:.4f},'
                      f'adelay=delays={round(at * sr)}S:all=1[s{k}]')
        labels.append(f'[s{k}]')
    if base_input is None:
        chains.insert(0, f'anullsrc=r={sr}:cl=stereo,atrim=duration={n_frames / fps:.6f}[base]')
    else:
        chains.insert(0, f'[{base_input}:a]aformat=sample_rates={sr}:channel_layouts=stereo[base]')
    chains.append(f'[base]{"".join(labels)}amix=inputs={1 + len(labels)}:normalize=0:duration=first[aout]')
    return inputs, ';'.join(chains), '[aout]'


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
    # 3D shots (blender/<shot>.py) are clips rendered once: say so when one no longer matches its script or the course
    # data it was built from (a curriculum change would otherwise show the new 2D map next to the old 3D one)
    try:
        import blender_shot
        for x in blender_shot.stale_shots(L):
            print(f'WARNING: 3D shot {x["shot"]} is stale: {"; ".join(x["reasons"])}. Re-render it first (GPU, inside a '
                  f'gpu-queue lease): {x["cmd"]}', flush=True)
    except Exception as e:      # never stop a render over the check itself
        print(f'(could not check the 3D shots: {e})')

    srv = Server()
    url = srv.url(L, 'render=1' + ('&captions=1' if a.captions else ''))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser, page, errors = open_lesson(p, url)
        meta = page.evaluate('window.__meta')
        # the sounds:{} that loaded (src is relative to the lesson folder); failed ones stay silent, as on the page
        snd = page.evaluate("() => Object.entries((window.K && K.sndInfo) || {}).map(([n, i]) => [n, i.src, !!i.failed])")
        browser.close()
    sound_src = {n: str((L / src).resolve()) for n, src, failed in snd if not failed}
    listen = bool(sound_src)
    fps = a.fps
    t1 = a.t1 if a.t1 is not None else meta['DUR']
    f0, f1 = int(a.t0 * fps), int(t1 * fps)
    n = f1 - f0
    per = (n + a.workers - 1) // a.workers
    jobs = []
    for w in range(a.workers):
        s, e = f0 + w * per, min(f1, f0 + (w + 1) * per)
        if s < e:
            jobs.append((url, s, e, fps, str(out_dir / f'seg{w}.mp4'), listen))
    print(f'{L.name}: {n} frames ({n / fps:.1f}s) on {len(jobs)} workers', flush=True)
    with mp.get_context('spawn').Pool(len(jobs)) as pool:
        results = pool.map(work, jobs)
    srv.close()
    heard = {}
    for _, errs, h in results:
        heard.update(h)
        for e in dict.fromkeys(errs):
            print('  page:', e)
    stretches = sound_stretches(heard, fps) if listen else []
    for name, first, count, m0, gain in stretches:
        print(f'  sound {name}: lesson {first / fps:.3f}-{(first + count) / fps:.3f} s = its {m0:.3f}-{m0 + count / fps:.3f} s'
              + (f' (gain {gain})' if gain != 1 else ''))

    lst = out_dir / 'segments.txt'
    lst.write_text(''.join(f"file '{pathlib.Path(s).name}'\n" for s, _, _ in results), encoding='utf-8')
    final = pathlib.Path(a.out) if a.out else out_dir / ('lesson.mp4' if a.t0 == 0 and a.t1 is None else 'clip.mp4')
    cmd = [ffmpeg(), '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst)]
    has_audio = mix.exists()
    vtt = L / 'captions.vtt'
    if has_audio:
        cmd += ['-ss', str(a.t0), '-t', str(n / fps), '-i', str(mix)]
    if stretches:
        # sound exhibits over the mix (or over silence when the lesson has no mix yet); the subtitles stay
        # input 2, so the sound files come after them
        subs = has_audio and vtt.exists() and a.t0 == 0 and not a.captions
        first_input = (2 if has_audio else 1) + (1 if subs else 0)
        extra, graph, label = sound_track(stretches, sound_src, f0, fps, 1 if has_audio else None, n, first_input)
        if subs:
            cmd += ['-i', str(vtt)]
        cmd += extra + ['-filter_complex', graph, '-map', '0:v', '-map', label]
        if subs:
            cmd += ['-map', '2:s', '-c:s', 'mov_text', '-metadata:s:s:0', 'language=eng']
        has_audio = True
    elif has_audio and vtt.exists() and a.t0 == 0 and not a.captions:
        cmd += ['-i', str(vtt), '-map', '0:v', '-map', '1:a', '-map', '2:s', '-c:s', 'mov_text', '-metadata:s:s:0', 'language=eng']
    elif has_audio:
        cmd += ['-map', '0:v', '-map', '1:a']
    cmd += ['-c:v', 'copy']
    if has_audio:
        # no -shortest: the subtitle stream ends at the last caption and would cut the video
        cmd += ['-c:a', 'aac', '-b:a', '160k']
    cmd += ['-movflags', '+faststart', str(final)]
    subprocess.run(cmd, check=True)
    for s, _, _ in results:
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
