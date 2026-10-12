"""Does the live lesson page (engine/player.js) keep clips and sounds in step with the narration clock, seek and pause?

usage: python lessons/_mediatest/tests/player_sync.py [--base http://127.0.0.1:8793]

Opens lessons/_mediatest/index.html as a visitor would (the real lesson page, no render=1), from the preview server
in .claude/launch.json ("missing-map", port 8793) when it answers, else from its own static server. Presses Play and
samples on every animation frame: the narration clock T (the player's own clock, audio/mix.mp3) and each clip's and
sound's currentTime, against the media time lesson.js asks for at T. The run: play 0-15 s (scenes 01 and 02), jump
to 26 s (03: the beeps sound), 37 s (04: the clip looping at 2x), 48 s (05: a clip and its sound together), switch to
1.5x speed, then pause and scrub to 20, 6, 40 and 50 s, checking the frame each paused clip holds.
Writes out/tests/player_sync.json.
"""
import argparse
import json
import pathlib
import sys
import time
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
L = HERE.parent
ROOT = L.parent.parent
OUT = L / 'out' / 'tests'
sys.path.insert(0, str(ROOT / 'tools'))
from playwright.sync_api import sync_playwright  # noqa: E402

PROBE = r"""
(() => {
  // what lesson.js asks for at narration time T (bounds: 12.9, 24.9, 35.3, 45.7 mid-gap; 0.6 s crossfades)
  // e[name] = media time; mv[name] = whether that time is moving (a clip held on its first or last frame is not)
  const LC = K.videoDur('clip'), FPS = 24, top = LC - 0.5 / FPS, hold = (m) => Math.min(Math.max(m, 0), top);
  const SD = K.soundDur('beeps');
  window.__mv = {};
  window.__expect = (T) => {
    const e = {}, mv = window.__mv = {};
    const held = (n, raw) => { e[n] = hold(raw); mv[n] = raw >= 0 && raw <= top; };
    if (T < 13.5) held('clip', T - 2.7);
    if (T >= 12.9 && T < 25.5) held('clip2', T - 12.95);
    if (T >= 35.3 && T < 46.3) { e.clip = ((2 * (T - 35.6)) % LC + LC) % LC; mv.clip = true; }
    if (T >= 45.7) held('clip2', T - 47.0);
    let b = null;
    if (T >= 24.9 && T < 35.9) b = T - 25.7;
    if (T >= 45.7) b = T - 47.0;
    if (b != null && b >= 0 && b < SD) { e.beeps = b; mv.beeps = true; }
    return e;
  };
  window.__log = [];
  (function tick() {
    const P = window.__player;
    if (P) {
      const T = P.now(), e = window.__expect(T), row = { at: performance.now(), T, playing: !!(P.audio ? !P.audio.paused : 0), rate: P.audio ? P.audio.playbackRate : 1 };
      Object.keys(K.vid).forEach((n) => {
        const v = K.vid[n];
        if (e[n] == null) { row[n] = { wanted: false, paused: v.paused }; return; }
        let d = v.currentTime - e[n];
        if (n === 'clip' && T >= 35.3) d = ((d + LC / 2) % LC + LC) % LC - LC / 2;   // looped: compare on the circle
        row[n] = { wanted: true, moving: !!window.__mv[n], cur: v.currentTime, exp: e[n], drift: d, paused: v.paused, rate: v.playbackRate, ready: v.readyState, seeking: v.seeking, hold: !!v.__hold };
      });
      const a = K.snd.beeps;
      row.beeps = e.beeps == null ? { wanted: false, paused: a.paused } : { wanted: true, moving: true, cur: a.currentTime, exp: e.beeps, drift: a.currentTime - e.beeps, paused: a.paused, rate: a.playbackRate };
      window.__log.push(row);
    }
    requestAnimationFrame(tick);
  })();
})()
"""

HELD = """(T) => { const e = window.__expect(T), o = {};
  Object.keys(K.vid).forEach((n) => { const v = K.vid[n]; if (e[n] == null) { o[n] = { wanted: false, paused: v.paused }; return; }
    const fps = K.vidInfo[n].fps, want = (Math.floor(e[n] * fps + 1e-6) + 0.5) / fps;
    o[n] = { cur: v.currentTime, frame_centre: want, on_frame: Math.abs(v.currentTime - want) < 0.5 / fps, paused: v.paused, seeking: v.seeking }; });
  o.beeps = { paused: K.snd.beeps.paused };
  o.T = window.__player.now();
  return o; }"""


def reachable(url):
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return r.status == 200
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default='http://127.0.0.1:8793')
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    srv = None
    page_url = f'{a.base}/lessons/_mediatest/index.html'
    if not reachable(page_url):
        from common import Server
        srv = Server()
        page_url = f'http://127.0.0.1:{srv.port}/lessons/_mediatest/index.html'
    print('page', page_url)
    marks = {}
    with sync_playwright() as p:
        # default autoplay policy, as a visitor has it: page.click below is a trusted click, which is what lets media play
        b = p.chromium.launch()
        page = b.new_page(viewport={'width': 1400, 'height': 1000})
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('console', lambda m: errors.append(m.text) if m.type in ('error', 'warning') else None)
        page.goto(page_url)
        page.wait_for_function('window.__readyDone === true && window.__player && document.querySelector("#bigplay").textContent === "Play lesson"', timeout=60000)
        page.evaluate(PROBE)
        now = lambda: page.evaluate('performance.now()')  # noqa: E731
        page.click('#bigplay')
        marks['play_0'] = now()
        time.sleep(15.0)
        for T, secs in ((26, 4.0), (37, 4.0), (48, 4.0)):
            marks[f'seek_{T}'] = page.evaluate(f'(window.__player.setT({T}), performance.now())')
            time.sleep(secs)
        marks['speed_1.5'] = page.evaluate("(document.querySelector('#speed').click(), document.querySelector('#speed').click(), performance.now())")
        time.sleep(3.0)
        marks['pause'] = page.evaluate('(window.__player.pause(), performance.now())')
        time.sleep(0.6)
        page.screenshot(path=str(OUT / 'player_paused.png'))
        held = {}
        for T in (20.0, 6.0, 40.0, 50.0):
            page.evaluate(f'window.__player.setT({T})')
            time.sleep(1.0)
            held[str(T)] = page.evaluate(HELD, T)
        page.screenshot(path=str(OUT / 'player_paused_50s.png'))
        log = page.evaluate('window.__log')
        b.close()
    if srv:
        srv.close()

    # how long each clip / sound has been in its current state (wanted and moving, wanted and held, unwanted) without
    # a break: the player measures a clip's speed over its first 0.1 s, so the first GRACE seconds are not judged
    GRACE = 0.2
    since = {}
    for r in log:
        for n in ('clip', 'clip2', 'beeps'):
            x = r.get(n) or {}
            state = (x.get('wanted'), x.get('moving'), r['playing'])
            if n not in since or since[n][0] != state:
                since[n] = (state, r['at'])
            x['age'] = (r['at'] - since[n][1]) / 1000

    def stats(t0, t1, settle=0.6):
        rows = [r for r in log if t0 + settle * 1000 <= r['at'] < t1]
        out = {}
        for n in ('clip', 'clip2', 'beeps'):
            mov = [r for r in rows if r.get(n, {}).get('wanted') and r[n].get('moving') and r['playing'] and r[n]['age'] >= GRACE]
            held = [r for r in rows if r.get(n, {}).get('wanted') and not r[n].get('moving') and r['playing'] and r[n]['age'] >= GRACE]
            ds = sorted(abs(r[n]['drift']) for r in mov)
            if ds:
                out[n] = {'samples': len(ds), 'median': round(ds[len(ds) // 2], 4), 'p95': round(ds[int(0.95 * (len(ds) - 1))], 4),
                          'max': round(ds[-1], 4), 'paused_while_moving': sum(r[n]['paused'] for r in mov)}
            if held:
                o = out.setdefault(n, {})
                o['held_samples'] = len(held)
                o['held_wrong'] = sum(not r[n]['paused'] or abs(r[n]['cur'] - (int(r[n]['exp'] * 24 + 1e-6) + 0.5) / 24) > 0.5 / 24 for r in held)
            if n != 'beeps':
                blank = sum(1 for r in rows if r.get(n, {}).get('wanted') and r[n]['ready'] < 2 and not r[n]['hold'])
                if blank:
                    out.setdefault(n, {})['blank_frames'] = blank
            unwanted_playing = sum(1 for r in rows if r.get(n) and not r[n]['wanted'] and not r[n]['paused'] and r[n].get('age', 9) >= GRACE)
            if unwanted_playing:
                out.setdefault(n, {})['playing_while_unwanted'] = unwanted_playing
        T = [r['T'] for r in rows]
        if T:
            out['T'] = [round(T[0], 2), round(T[-1], 2)]
            out['wall_s'] = round((rows[-1]['at'] - rows[0]['at']) / 1000, 2)
            out['clock_rate'] = round((T[-1] - T[0]) / ((rows[-1]['at'] - rows[0]['at']) / 1000), 3)
        return out

    def lock(t0, t1, tol):
        """seconds after t0 until every moving clip / sound is within tol of where the scene wants it"""
        for r in log:
            if t0 <= r['at'] < t1 and r['playing']:
                live = [n for n in ('clip', 'clip2', 'beeps') if r.get(n, {}).get('wanted') and r[n].get('moving')]
                if live and all(abs(r[n]['drift']) <= tol and not r[n]['paused'] for n in live):
                    return round((r['at'] - t0) / 1000, 3)
        return None

    keys = list(marks)
    windows = {k: (marks[k], marks[keys[i + 1]] if i + 1 < len(keys) else marks[k] + 1e9) for i, k in enumerate(keys)}
    res = {'page': page_url, 'windows': {}, 'paused_scrubs': held, 'frames_logged': len(log), 'errors': list(dict.fromkeys(errors))}
    for k, (t0, t1) in windows.items():
        if k == 'pause':
            continue
        res['windows'][k] = {'stats_after_0.6s': stats(t0, t1), 'lock_within_0.15s_after': lock(t0, t1, 0.15),
                             'lock_within_1_frame_after': lock(t0, t1, 1 / 24)}
    (OUT / 'player_sync.json').write_text(json.dumps({'result': res, 'marks': marks, 'log': log}), encoding='utf-8')
    print(json.dumps(res, indent=1))

    ok = True
    for k, w in res['windows'].items():
        st = w['stats_after_0.6s']
        for n in ('clip', 'clip2', 'beeps'):
            if n in st:
                s = st[n]
                ok &= s.get('max', 0) <= 0.15 and s.get('paused_while_moving', 0) == 0 and s.get('held_wrong', 0) == 0 and s.get('blank_frames', 0) == 0
                ok &= not s.get('playing_while_unwanted')
    for T, h in held.items():
        for n, v in h.items():
            if isinstance(v, dict) and 'on_frame' in v:
                ok &= v['on_frame'] and v['paused']
        ok &= h['beeps']['paused']
    print('PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
