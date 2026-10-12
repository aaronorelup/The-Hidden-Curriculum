"""Rebuild the _mediatest test media (engine test for K.video / K.image / K.listen / K.sound / K.cursor).

usage: python lessons/_mediatest/make_assets.py [--clip-source <autoplay.mp4>] [--screen]

Everything here is synthetic or Aaron's own, and the timings are what the tests in tests/ expect:
- audio/mix.mp3      the lesson clock (gitignored like every mix.mp3, so rebuilt here): a 20 ms 1 kHz tick at
                     every whole lesson second over silence, as long as cues.json says
- assets/audio/beeps.mp3   the sound exhibit: a 60 ms 2 kHz burst at every whole second, 12 s, -16 LUFS
- assets/img/spec_beeps.webp   its K.listen spectrogram
- assets/video/clip.mp4    10 s of the Lamplighter game's autoplay (source 4.0-14.0 s), 960x540, 24 fps, to the clip
                     spec (tools/media_util.py encode). Only rebuilt when --clip-source is given (the source lives
                     outside the repo: _planning/opus-made-this/experiments/game/cpp-bare/autoplay.mp4)
- assets/img/screen.webp   with --screen: a real screenshot (a lesson page of this course in headless Chromium,
                     1600x900), the "screenshot in use" exhibit of scene 05
"""
import argparse
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import media_util as mu  # noqa: E402

BEEP_HZ, TICK_HZ = 2000, 1000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--clip-source')
    ap.add_argument('--screen', action='store_true')
    a = ap.parse_args()
    cues = json.loads((HERE / 'cues.json').read_text(encoding='utf-8'))
    dur = cues['duration']

    tick = f"0.25*sin(2*PI*{TICK_HZ}*t)*lt(mod(t\\,1)\\,0.02)"
    (HERE / 'audio').mkdir(exist_ok=True)
    subprocess.run([mu.ffmpeg(), '-v', 'error', '-y', '-f', 'lavfi', '-i', f'aevalsrc={tick}:s=44100:d={dur}', '-ac', '2',
                    '-c:a', 'libmp3lame', '-b:a', '128k', str(HERE / 'audio' / 'mix.mp3')], check=True)
    print('wrote audio/mix.mp3 (lesson clock ticks)')

    raw = HERE / 'assets' / 'audio' / 'beeps.raw.wav'
    raw.parent.mkdir(parents=True, exist_ok=True)
    beep = f"0.5*sin(2*PI*{BEEP_HZ}*t)*lt(mod(t\\,1)\\,0.06)"
    subprocess.run([mu.ffmpeg(), '-v', 'error', '-y', '-f', 'lavfi', '-i', f'aevalsrc={beep}:s=44100:d=12', '-ac', '2', str(raw)], check=True)
    try:
        mu.audio(raw, HERE / 'assets' / 'audio' / 'beeps.mp3')
    finally:
        raw.unlink(missing_ok=True)
    mu.spectrogram(HERE / 'assets' / 'audio' / 'beeps.mp3', HERE / 'assets' / 'img' / 'spec_beeps.webp')

    if a.clip_source:
        if mu.encode(a.clip_source, HERE / 'assets' / 'video' / 'clip.mp4', t0=4.0, t1=14.0, fps=24, width=960):
            raise SystemExit('clip.mp4 does not meet the spec')
    else:
        print('assets/video/clip.mp4 kept:', mu.check(HERE / 'assets' / 'video' / 'clip.mp4') or 'meets the spec')

    if a.screen:
        from playwright.sync_api import sync_playwright
        from common import Server
        srv = Server()
        png = HERE / 'assets' / 'img' / 'screen.tmp.png'
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={'width': 1600, 'height': 900})
            # a published lesson's own page, as a visitor sees it (srv.url is not used: it would re-sync that lesson's scenes.js)
            pg.goto(f'http://127.0.0.1:{srv.port}/lessons/01-03-folders-paths-the-working-directory/index.html')
            pg.wait_for_function('window.__readyDone === true', timeout=60000)
            pg.wait_for_timeout(500)
            pg.screenshot(path=str(png))
            b.close()
        srv.close()
        try:
            mu.still(png, HERE / 'assets' / 'img' / 'screen.webp', lossless=True)
        finally:
            png.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
