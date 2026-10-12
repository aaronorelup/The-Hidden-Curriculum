"""lessons/_demo/tests/camera.py: checks of the capture camera, the typing chips and K.shot's swap, on the real _demo
captures (python lessons/_demo/tests/camera.py; no GPU, no network). Exit 1 on any failure.

  1. K.shot's camera is the same whatever order two scenes that share a shot are drawn in (render workers seek out of
     order): its memo is keyed on everything autoCam reads, zoom callouts included.
  2. Back-to-back scripted zooms pan from one to the next (no dip toward 1x): scene 03's zoom never drops between them.
  3. A click that loads a page at once does not get a zoom that cannot hold (minHold): the camera stays at 1x around
     the navigating click in the site capture, and still zooms for the #bigplay click.
  4. The zoom eases in log scale: halfway through a 1x -> z move it is at sqrt(z), not (1 + z) / 2.
  5. K.termReplay draws at the alpha it is given (a terminal window fading in never shows its text at full strength).
  6. K.captureAt / K.captureBox read the recipe's marks and shot boxes.
"""
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
from common import Server, open_lesson  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

L = ROOT / 'lessons' / '_demo'
fails = []


def check(ok, what):
    print(('ok    ' if ok else 'FAIL  ') + what)
    if not ok:
        fails.append(what)


srv = Server()
with sync_playwright() as p:
    browser, page, errors = open_lesson(p, srv.url(L))
    page.evaluate('window.__frame(0)')

    # 1. K.shot camera independent of draw order
    js = '''([order]) => {
      K.shot.memo = {};
      const base = { cursor: [{ at: 0, x: 1500, y: 950 }, { at: 1.6, x: 520, y: 780, click: true }] };
      const A = { ...base, callouts: [{ at: 0.5, until: 3, box: [100, 700, 870, 170], zoom: true }] };
      const B = { ...base, callouts: [{ at: 0.5, until: 3, box: [1030, 280, 810, 460], zoom: 1.7 }] };
      const r = {};
      for (const k of order) { const v = K.shot('site/course-page', 2.4, [260, 150, 1400], k === 'A' ? A : B); r[k] = [v.cam.x, v.cam.y, v.cam.z]; }
      return r; }'''
    ab, ba = page.evaluate(js, [['A', 'B']]), page.evaluate(js, [['B', 'A']])
    check(ab == ba and ab['A'] != ab['B'], f'K.shot camera independent of draw order (A {ab["A"]}, B {ab["B"]})')

    # 2. scene 03's two scripted zooms (stats 0.9-4.3, then the card from 4.6): the zoom never dips between them
    z = page.evaluate('''() => {
      const stats = K.captureBox('site', 'course-page', 'stats'), card = K.captureBox('site', 'course-page', 'card');
      const o = { zooms: [{ at: 0.9, until: 4.3, box: stats }, { at: 4.6, until: 7.0, box: card, z: 1.55 }] };
      const out = []; for (let t = 3.6; t <= 6.2; t += 0.05) out.push(+K.shot('site/course-page', t, [260, 150, 1400], o).cam.z.toFixed(3));
      return out; }''')
    check(min(z) >= min(z[0], z[-1]) - 0.02, f'no dip between back-to-back scripted zooms (zoom {z[0]} .. min {min(z)} .. {z[-1]})')

    # 3. minHold: the navigating click in the site capture gets no zoom; the #bigplay click does
    ev = page.evaluate("K.capture('site').clicks.map((c) => [c.t, c.target])")
    nav_click = next(t for t, tg in ev if 'Files are just bytes' in (tg or ''))
    play_click = next(t for t, tg in ev if '#bigplay' in (tg or ''))
    zn = page.evaluate('''([a, b]) => { const out = []; for (let t = a; t <= b; t += 0.05) out.push(K.demo('site', t, [260, 150, 1400], { zoom: 1.75 }).cam.z); return out; }''',
                       [nav_click - 1.5, nav_click + 0.5])
    zp = page.evaluate('''([t]) => K.demo('site', t, [260, 150, 1400], { zoom: 1.75 }).cam.z''', [play_click])
    check(max(zn) < 1.001, f'no zoom on the navigating click at {nav_click:.2f} s (max zoom {max(zn):.3f})')
    check(zp > 1.6, f'the #bigplay click at {play_click:.2f} s is zoomed ({zp:.2f}x)')

    # 4. log-scale zoom: halfway through a 1x -> 1.8x move (the eased k is 0.5 at the middle) the zoom is sqrt(1.8)
    zm = page.evaluate('''() => K.shot('site/course-page', 1.0 + 0.6, [260, 150, 1400], { zooms: [{ at: 1.0, d: 1.2, x: 960, y: 540, z: 1.8 }] }).cam.z''')
    check(abs(zm - math.sqrt(1.8)) < 0.01, f'zoom eased in log scale (mid-move {zm:.3f}, sqrt(1.8) = {math.sqrt(1.8):.3f})')

    # 5. K.termReplay alpha: the brightest pixel of the prompt row at alpha 0.3 vs 1
    lum = page.evaluate('''() => { const g = K.ctx(); g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1;
      const one = (a) => { g.fillStyle = '#000'; g.fillRect(0, 0, 1920, 1080); K.termReplay([100, 100, 900, 300], 5, 'term', { alpha: a });
        const d = g.getImageData(0, 0, 1920, 1080).data; let m = 0; for (let i = 0; i < d.length; i += 4) m = Math.max(m, d[i] + d[i + 1] + d[i + 2]); return m; };
      const r = [one(1), one(0.3)]; g.restore(); return r; }''')
    check(lum[1] < lum[0] * 0.45, f'K.termReplay draws at o.alpha (brightest prompt pixel {lum[0]} at 1, {lum[1]} at 0.3)')

    # 6. marks and boxes
    mk = page.evaluate("[K.captureAt('site', 'playing', -1), K.captureBox('site', 'course-page', 'stats'), K.captureAt('site', 'nope', -1)]")
    check(mk[0] > 0 and mk[1] and len(mk[1]) == 4 and mk[2] == -1, f'K.captureAt / K.captureBox ({mk[0]}, {mk[1]}, fallback {mk[2]})')
    browser.close()
srv.close()
print('ALL OK' if not fails else f'{len(fails)} FAILED')
sys.exit(1 if fails else 0)
