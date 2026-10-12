"""stills.py: render review frames and a contact sheet, without rendering the whole video.

usage:
  python tools/stills.py <lesson>                   every cue, every scene start/middle/end
  python tools/stills.py <lesson> --every 2         one frame every 2 seconds
  python tools/stills.py <lesson> --at 12.5 40      specific times
  python tools/stills.py <lesson> --scene 03        only frames inside scene 03
  python tools/stills.py <lesson> --from 41 --to 43 --every 0.25   only a short time window (seconds,
                                                    lesson time; combines with --every, --at and --scene)
  python tools/stills.py <lesson> --every 1.5 --captions --tag review   own folder, captions burned in

Writes out/stills/<time>.png and out/sheet.jpg (labelled grid) and prints any console
errors the page raised, because a JS error in one scene otherwise just shows a blank frame.
"""
import argparse
import base64
import io
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import Server, lesson_dir, open_lesson  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson')
    ap.add_argument('--every', type=float)
    ap.add_argument('--at', type=float, nargs='*')
    ap.add_argument('--scene')
    ap.add_argument('--cols', type=int, default=4)
    ap.add_argument('--captions', action='store_true', help='burn captions into the stills')
    ap.add_argument('--from', dest='t_from', type=float, help='only frames at or after this time (s)')
    ap.add_argument('--to', dest='t_to', type=float, help='only frames at or before this time (s)')
    ap.add_argument('--tag', help='output folder suffix, so parallel reviewers keep separate frames')
    a = ap.parse_args()
    L = lesson_dir(a.lesson)
    # per-scene folders so parallel scene builders never wipe each other's frames
    tag = f'-{a.tag}' if a.tag else f'-{a.scene}' if a.scene else ''
    outdir = L / 'out' / f'stills{tag}'
    outdir.mkdir(parents=True, exist_ok=True)
    for old in outdir.glob('*.png'):
        old.unlink()
    srv = Server()
    with sync_playwright() as p:
        browser, page, errors = open_lesson(p, srv.url(L, 'render=1' + ('&captions=1' if a.captions else '')))
        tl = page.evaluate('window.__timeline')
        dur = tl['dur']
        times, labels = [], {}
        secs = tl['sections']
        if a.at:
            times = a.at
        elif a.every:
            # with --from, the grid starts at the window's start so a short window gets its own beat
            t0 = max(0.0, a.t_from) if a.t_from is not None else 0.0
            times = [round(t0 + i * a.every, 2) for i in range(int((dur - t0) / a.every) + 1)]
        else:
            for s in secs:
                for t, lab in [(s['start'] + 0.3, 'start'), ((s['start'] + s['end']) / 2, 'mid'), (s['end'] - 0.2, 'end')]:
                    times.append(round(t, 2)); labels[round(t, 2)] = f"{s['n']} {lab}"
                for name, t in (s.get('cues') or {}).items():
                    times.append(round(t + 0.9, 2)); labels[round(t + 0.9, 2)] = f"{s['n']} [[{name}]]+0.9"
        if a.scene:
            s = next((x for x in secs if str(x['n']) == a.scene), None)
            if s is None:  # also accept '3' for '03'
                s = next((x for x in secs if str(x['n']).lstrip('0') == a.scene.lstrip('0')), None)
            if s is None:
                browser.close(); srv.close()
                sys.exit(f"stills.py: no such section '{a.scene}' in {a.lesson}. "
                         f"Sections: {', '.join(str(x['n']) for x in secs)}")
            lo = s['start'] - 1.0
            hi = secs[secs.index(s) + 1]['start'] if secs.index(s) + 1 < len(secs) else dur
            times = [t for t in times if lo <= t < hi] or [round(lo + (hi - lo) * k / 8, 2) for k in range(9)]
        if a.t_from is not None or a.t_to is not None:
            lo = a.t_from if a.t_from is not None else 0.0
            hi = min(a.t_to, dur) if a.t_to is not None else dur
            win = [t for t in times if lo <= t <= hi]
            # a window with no cue/section frames in it still gets 9 evenly spaced frames
            times = win or [round(lo + (hi - lo) * k / 8, 2) for k in range(9)]
        times = sorted(set(times))
        thumbs = []
        for t in times:
            data = page.evaluate('t => window.__png(t)', t)
            png = base64.b64decode(data.split(',', 1)[1])
            (outdir / f'{t:07.2f}.png').write_bytes(png)
            im = Image.open(io.BytesIO(png)).convert('RGB')
            im.thumbnail((480, 270))
            thumbs.append((t, im))
        browser.close()
    srv.close()

    cols = a.cols
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * 490 + 10, rows * 310 + 10), (8, 9, 18))
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype('arial.ttf', 16)
    except OSError:
        font = ImageFont.load_default()
    for i, (t, im) in enumerate(thumbs):
        x, y = 10 + (i % cols) * 490, 10 + (i // cols) * 310
        sheet.paste(im, (x, y))
        d.text((x, y + 276), f'{t:6.2f}s  {labels.get(t, "")}', fill=(240, 192, 106), font=font)
    sheet_path = L / 'out' / f'sheet{tag}.jpg'
    sheet.save(sheet_path, quality=88)
    print(f'{len(thumbs)} stills -> {outdir}\nsheet -> {sheet_path}')
    if errors:
        print('PAGE ERRORS / WARNINGS:')
        for e in dict.fromkeys(errors):
            print('  ', e)


if __name__ == '__main__':
    main()
