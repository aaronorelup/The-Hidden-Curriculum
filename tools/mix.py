"""mix.py: score + narration -> audio/mix.mp3 (what the web player and the MP4 both use).

usage: python tools/mix.py <lesson> [--no-music] [--music-db -21]

The score comes from engine/music.js (rendered in a headless browser, deterministic).
It is ducked under the voice with a sidechain compressor, then the mix is normalised to
-16 LUFS so every lesson plays at the same loudness.
"""
import argparse
import base64
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import Server, ffmpeg, lesson_dir, open_lesson  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson')
    ap.add_argument('--no-music', action='store_true')
    ap.add_argument('--music-db', type=float, default=-21.0, help='score level before ducking')
    a = ap.parse_args()
    L = lesson_dir(a.lesson)
    audio = L / 'audio'
    narr = audio / 'narration.wav'
    if not narr.exists():
        raise SystemExit('run narrate.py first')
    out = audio / 'mix.mp3'
    if a.no_music:
        subprocess.run([ffmpeg(), '-v', 'error', '-y', '-i', str(narr), '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                        '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '128k', str(out)], check=True)
    else:
        srv = Server()
        with sync_playwright() as p:
            browser, page, errors = open_lesson(p, srv.url(L))
            n = page.evaluate('window.__music()')
            b64 = ''.join(page.evaluate('([a, b]) => window.__musicB64.slice(a, b)', [i, i + 4_000_000]) for i in range(0, n, 4_000_000))
            browser.close()
        srv.close()
        wav = audio / 'music.wav'
        wav.write_bytes(base64.b64decode(b64))
        g = 10 ** (a.music_db / 20)
        filt = (f'[1:a]volume={g:.4f},aformat=channel_layouts=stereo[m];'
                '[0:a]aformat=channel_layouts=stereo,asplit=2[v][sc];'
                '[m][sc]sidechaincompress=threshold=0.02:ratio=5:attack=30:release=600[duck];'
                '[v][duck]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11[out]')
        subprocess.run([ffmpeg(), '-v', 'error', '-y', '-i', str(narr), '-i', str(wav), '-filter_complex', filt,
                        '-map', '[out]', '-ar', '44100', '-c:a', 'libmp3lame', '-b:a', '128k', str(out)], check=True)
    print(f'wrote {out} ({out.stat().st_size / 1e6:.1f} MB)')


if __name__ == '__main__':
    main()
