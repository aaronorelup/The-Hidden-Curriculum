"""Regression stills for the 2026-10-12 engine rework (map as data, real-computer media).

The 12 published lessons are LEGACY: after any engine change they must render exactly as they do today.
This script renders fixed frames of every published lesson (plus lessons/_sandbox) and hashes them, so a
later phase can be compared byte for byte with compare.py.

usage:
  python stills_hash.py <phase>                       render + hash every lesson listed in times.json
  python stills_hash.py <phase> --lessons 00-01-the-hidden-curriculum _sandbox
  python stills_hash.py <phase> --order reverse       seek order: sorted (default) | reverse | shuffle
  python stills_hash.py <phase> --driver tools        go through tools/stills.py instead of driving the page
  python stills_hash.py <phase> --root <course dir>   e.g. a git worktree of the course
  python stills_hash.py <phase> --no-png              hashes only, no PNG copies (~320 MB per full phase otherwise)
  python stills_hash.py <phase> --force               overwrite an existing phase (refused by default, so a
                                                      baseline such as "before" cannot be clobbered by accident)
  python stills_hash.py --plan [--force]              (re)compute times.json from cues.json + a map.draw probe

Frames per lesson (all fixed in times.json, never recomputed by a normal run):
  s1..s8  8 times spread evenly over the lesson: dur * (k + 0.5) / 8
  x1, x2  2 times inside scene crossfades: 0.3 s into the 0.6 s fade (runtime.js XFADE), i.e. both scenes at 50 %
  map     published lessons only: inside the "Where it lives" section (whose scene calls K.map.draw), the middle
          of the longest stretch where the map is drawn at full alpha with its reveal finished (--plan sweeps
          the section every 0.2 s with a probe on K.map.draw; runs, alpha and camera scale are kept in times.json)

Output: stills/<lesson>/<phase>/<role>_<time>.png and stills/<lesson>/<phase>.sha256.json, which also records
the inputs (git HEAD, dirty paths, a hash of every local file the page loaded, the font files and font faces
in use, the Chromium version) so compare.py can tell an engine change from a font or browser change.

The default driver is self-contained: its own static server rooted at the course folder and its own headless
Chromium calling the page contract (window.__readyDone, window.__timeline, window.__png), exactly as
tools/stills.py does, so the PNG bytes are the same, but it writes nothing into the course folder and does
not depend on tools/ (which other agents may be editing). --driver tools runs tools/stills.py itself, the
way the 2026-10-04 baseline did.
"""
import argparse
import base64
import functools
import hashlib
import http.server
import json
import pathlib
import platform
import random
import re
import shutil
import socketserver
import subprocess
import sys
import threading
import time
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
HC = HERE.parent.parent                 # the course repo (tests/legacy_freeze/ lives in it)
OUT = HERE / 'stills'                   # <lesson>/<phase>.sha256.json (+ PNGs); only 'before' is committed
TIMES = HERE / 'times.json'

PUBLISHED = ['00-01-the-hidden-curriculum', '00-02-the-map-of-everything', '00-03-how-old-is-all-this',
             '00-04-model-vs-app-vs-agent', '00-05-how-llms-work-just-enough', '00-06-how-to-learn-anything-technical',
             '01-01-files-are-just-bytes', '01-02-file-extensions-associations',
             '01-03-folders-paths-the-working-directory', '01-04-hidden-files-dotfiles',
             '01-05-environment-variables-path', '01-06-programs-processes-services']
EXTRA = ['_sandbox']
XFADE = 0.6                       # engine/runtime.js
MAP_CALL = re.compile(r'(?:K\.map|\bMAP)\.draw\(')
TEXT_EXT = {'.js', '.css', '.html', '.json', '.md', '.vtt', '.txt', '.svg'}
TAG = 'eb1012'                    # out/stills-<TAG> folder used by --driver tools
MAP_STEP = 0.2                    # --plan: sweep step through the "Where it lives" section (s)
MAP_OVERRIDE = {                  # --plan: map times picked by eye where the automatic middle is unsuitable
    '00-05-how-llms-work-just-enough': (53.0, 'auto middle 56.97 falls in [[tour]] 55.4-61.6, where the scene veils the '
                                              'map under the ghost desk; 53.0 is the plain full map with all six '
                                              'lanterns lit and labelled, after [[lanterns]] 48.8 and before [[tour]]'),
}
MAP_REVEAL = 2.6                  # map.js staggered reveal: 8 x 0.22 + 0.7 s (path 2.2 s), plus a margin


# ------------------------------------------------------------------ static server + page (no tools/ import)
class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


class Server:
    def __init__(self, root):
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        self.httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(_Quiet, directory=str(root)))
        self.httpd.daemon_threads = True
        self.port = self.httpd.server_address[1]
        self.base = f'http://127.0.0.1:{self.port}/'
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()


class Page:
    """one headless Chromium per lesson, like tools/common.open_lesson (fresh profile, 1920x1080 viewport)"""

    def __init__(self, pw, srv, slug):
        self.srv, self.errors, self.requests, self.failed = srv, [], [], []
        self.browser = pw.chromium.launch()
        self.page = self.browser.new_page(viewport={'width': 1920, 'height': 1080})
        pg = self.page
        pg.on('pageerror', lambda e: self.errors.append(f'pageerror: {e}'))
        pg.on('console', lambda m: self.errors.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
        pg.on('request', lambda r: self.requests.append(r.url))
        pg.on('requestfailed', lambda r: self.failed.append(f'{r.url} {r.failure}'))
        pg.goto(f'{srv.base}lessons/{slug}/index.html?render=1')
        try:
            pg.wait_for_function('window.__readyDone === true', timeout=90_000)
        except Exception as exc:
            self.close()
            raise SystemExit(f'{slug}: page never became ready ({type(exc).__name__}): {self.errors}')

    def png(self, t):
        data = self.page.evaluate('t => window.__png(t)', t)
        return base64.b64decode(data.split(',', 1)[1])

    def faces(self):
        # 'loading' counts too: a glyph outside the loaded unicode-range subsets makes Chromium fetch another
        # subset while the frame is drawn with a fallback face, which is a first-draw nondeterminism
        return self.page.evaluate("""() => Array.from(document.fonts)
            .filter((f) => f.status !== 'unloaded')
            .map((f) => [f.family.replace(/"/g, ''), f.weight, f.style, f.unicodeRange].join(' | ')).sort()""")

    def close(self):
        try:
            self.browser.close()
        except Exception:
            pass


# ------------------------------------------------------------------ input fingerprints
def file_hash(p: pathlib.Path):
    b = p.read_bytes()
    if p.suffix.lower() in TEXT_EXT:      # .gitattributes forces eol=lf: a re-checkout must not look like a change
        b = b.replace(b'\r\n', b'\n')
    return hashlib.sha256(b).hexdigest()


def local_inputs(root, base, urls):
    files, external = {}, []
    for u in dict.fromkeys(urls):
        if u.startswith(base):
            rel = urllib.parse.unquote(urllib.parse.urlsplit(u).path).lstrip('/')
            p = root / rel
            files[rel] = file_hash(p) if p.is_file() else 'MISSING'
        elif not u.startswith('data:'):
            external.append(u)
    return dict(sorted(files.items())), sorted(external)


def git(root, *args):
    r = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else f'(git failed: {r.stderr.strip()[:200]})'


def scenes_js_in_sync(lesson: pathlib.Path):
    """what tools/common.py sync_scenes would write; the page loads scenes.js as committed"""
    d = lesson / 'scenes'
    names = sorted(p.name for p in d.glob('*.js')) if d.is_dir() else []
    tags = ''.join(f'<script src="scenes/{n}"></script>' for n in names)
    want = f'// generated by tools/common.py sync_scenes; do not edit\ndocument.write({json.dumps(tags)});\n'
    have = (lesson / 'scenes.js').read_text(encoding='utf-8').replace('\r\n', '\n') if (lesson / 'scenes.js').exists() else None
    return have == want


# ------------------------------------------------------------------ plan: fix the times once
PROBE = """(T) => {
  const calls = [], hit = [], sc = window.__lesson.scenes, orig = K.map.draw, keep = {};
  K.map.draw = function (t, o) {
    const g = K.ctx(), m = g.getTransform();
    calls.push({ alpha: +g.globalAlpha.toFixed(3), scale: +m.a.toFixed(3), tx: +m.e.toFixed(1), ty: +m.f.toFixed(1),
                 t: +(+t).toFixed(3), t0: o && o.t0 != null ? +(+o.t0).toFixed(3) : null });
    return orig.apply(this, arguments);
  };
  for (const n of Object.keys(sc)) { const f = sc[n]; keep[n] = f; sc[n] = function () { hit.push(n); return f.apply(this, arguments); }; }
  try { window.__seek(T); } finally { K.map.draw = orig; for (const n in keep) sc[n] = keep[n]; }
  return { calls, scenes: hit };
}"""


def plan(root, slugs):
    from playwright.sync_api import sync_playwright
    old = json.loads(TIMES.read_text(encoding='utf-8')) if TIMES.exists() else {}
    out = {'_about': 'fixed regression times (lesson seconds). Written by stills_hash.py --plan on '
                     f'{time.strftime("%Y-%m-%d")}; normal runs only read this file. Roles: s1..s8 spread, '
                     'x1/x2 mid-crossfade (0.3 s into the 0.6 s fade entering section `enters`), map = middle '
                     'of the "Where it lives" section (published lessons only).'}
    srv = Server(root)
    with sync_playwright() as pw:
        for slug in slugs:
            pg = Page(pw, srv, slug)
            tl = pg.page.evaluate('window.__timeline')
            trans = pg.page.evaluate('window.__lesson.transition || {}')
            secs, dur = tl['sections'], tl['dur']
            bounds = [0.0] + [(secs[i - 1]['end'] + secs[i]['start']) / 2 for i in range(1, len(secs))]
            roles = {f's{k + 1}': round(dur * (k + 0.5) / 8, 2) for k in range(8)}
            fades = [i for i in range(1, len(secs)) if trans.get(secs[i]['n'], 'fade') == 'fade']
            picks = []
            for want in (2, len(secs) - 2):                       # the old baseline's choice: i = 2 and len - 2
                i = min((f for f in fades if f not in picks), key=lambda f: abs(f - want), default=None)
                if i is not None:
                    picks.append(i)
            entry = {'duration': dur, 'sections': len(secs), 'times': roles, 'xfade': {}, 'map': None}
            for j, i in enumerate(sorted(picks)):
                t = round(bounds[i] + XFADE / 2, 2)
                pr = pg.page.evaluate(PROBE, t)
                entry['times'][f'x{j + 1}'] = t
                entry['xfade'][f'x{j + 1}'] = {'leaves': secs[i - 1]['n'], 'enters': secs[i]['n'], 'bound': round(bounds[i], 3),
                                               'scenes_drawn': pr['scenes']}
            if slug in PUBLISHED:
                sec = next((s for s in secs if re.search(r'where it lives', s.get('title') or '', re.I)), None)
                if sec is None:
                    raise SystemExit(f'{slug}: no "Where it lives" section')
                lesson = root / 'lessons' / slug
                files = [lesson / 'scenes' / f"{sec['n']}.js"]
                src = '\n'.join(f.read_text(encoding='utf-8') for f in files if f.exists())
                if not MAP_CALL.search(src):
                    raise SystemExit(f'{slug}: scene {sec["n"]} never calls K.map.draw')
                # the map is often on screen for only part of the scene (it fades for the metaphor): sweep the
                # section and take the middle of the longest run where the map is drawn at full alpha and its
                # staggered reveal (map.js: t0 + 8 x 0.22 + 0.7 s, path 2.2 s) has finished
                step, runs, cur = MAP_STEP, [], None
                n = int((sec['end'] - sec['start']) / step) + 1
                for k in range(n):
                    t = round(sec['start'] + k * step, 3)
                    c = pg.page.evaluate(PROBE, t)['calls']
                    ok = bool(c) and max(x['alpha'] for x in c) >= 0.99 and all(
                        x['t0'] is None or x['t'] - x['t0'] >= MAP_REVEAL for x in c)
                    if ok:
                        cur = [t, t] if cur is None else [cur[0], t]
                    elif cur is not None:
                        runs.append(cur); cur = None
                if cur is not None:
                    runs.append(cur)
                if not runs:
                    raise SystemExit(f'{slug}: K.map.draw never drawn fully revealed at full alpha in section {sec["n"]}')
                best = max(runs, key=lambda r: (r[1] - r[0], -r[0]))
                t = auto = round((best[0] + best[1]) / 2, 2)
                why = None
                if slug in MAP_OVERRIDE:          # chosen by eye: the probe cannot see a veil drawn over the map
                    t, why = MAP_OVERRIDE[slug]
                pr = pg.page.evaluate(PROBE, t)
                if not pr['calls'] or max(x['alpha'] for x in pr['calls']) < 0.99:
                    raise SystemExit(f'{slug}: map not drawn at full alpha at {t}')
                entry['times']['map'] = t
                entry['map'] = {'section': sec['n'], 'title': sec['title'], 'scene_file': f"scenes/{sec['n']}.js",
                                'section_span': [sec['start'], sec['end']], 'sweep_step': step,
                                'full_map_runs': [[round(r[0], 2), round(r[1], 2)] for r in runs],
                                'chosen_run': [round(best[0], 2), round(best[1], 2)], 'auto_time': auto,
                                'override': why, 'probe': pr}
            dup = [r for r, t in entry['times'].items() if list(entry['times'].values()).count(t) > 1]
            if dup:
                print(f'  note {slug}: roles share a time: {dup}')
            pg.close()
            out[slug] = entry
            print(slug, json.dumps(entry['times']), json.dumps(entry['map'] and entry['map']['probe']['calls'][:2]))
    srv.close()
    if old and {k: v for k, v in old.items() if k != '_about'} != {k: v for k, v in out.items() if k != '_about'}:
        print('times.json changed: earlier phases are no longer comparable with new ones')
    TIMES.write_text(json.dumps(out, indent=1), encoding='utf-8')
    print(f'wrote {TIMES}')


# ------------------------------------------------------------------ a phase
def order_items(items, how):
    items = sorted(items, key=lambda kv: (kv[1], kv[0]))
    if how == 'reverse':
        items.reverse()
    elif how == 'shuffle':
        random.Random(1012).shuffle(items)
    return items


def run_page(pw, srv, root, slug, roles, how):
    pg = Page(pw, srv, slug)
    faces_ready = pg.faces()
    shots = {}
    for role, t in order_items(roles.items(), how):
        shots[f'{role}_{t:07.2f}.png'] = pg.png(t)
    faces_end = pg.faces()
    ver = pg.browser.version
    tl = pg.page.evaluate('({ dur: window.__timeline.dur, n: window.__timeline.sections.length, narrated: window.__timeline.narrated })')
    files, external = local_inputs(root, srv.base, pg.requests)
    meta = {'chromium': ver, 'timeline': tl, 'faces_at_ready': faces_ready,
            'faces_lazy': sorted(set(faces_end) - set(faces_ready)),
            'page_errors': list(dict.fromkeys(pg.errors)), 'failed_requests': pg.failed,
            'inputs': files, 'external': external}
    pg.close()
    return shots, meta


def run_tools(root, slug, roles):
    """the 2026-10-04 way: tools/stills.py --at ... --tag, then pick its PNGs up by time"""
    ts = sorted(set(roles.values()))
    r = subprocess.run([sys.executable, 'tools/stills.py', slug, '--tag', TAG, '--at', *[str(t) for t in ts]],
                       cwd=str(root), capture_output=True, text=True)
    src = root / 'lessons' / slug / 'out' / f'stills-{TAG}'
    shots = {}
    for role, t in roles.items():
        p = src / f'{t:07.2f}.png'
        if p.exists():
            shots[f'{role}_{t:07.2f}.png'] = p.read_bytes()
    shutil.rmtree(src, ignore_errors=True)
    (root / 'lessons' / slug / 'out' / f'sheet-{TAG}.jpg').unlink(missing_ok=True)
    return shots, {'stills_py_stdout': r.stdout.strip(), 'stills_py_stderr': r.stderr.strip()[-2000:], 'returncode': r.returncode}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('phase', nargs='?')
    ap.add_argument('--plan', action='store_true')
    ap.add_argument('--lessons', nargs='*')
    ap.add_argument('--order', choices=['sorted', 'reverse', 'shuffle'], default='sorted')
    ap.add_argument('--driver', choices=['page', 'tools'], default='page')
    ap.add_argument('--root', default=str(HC))
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--no-png', action='store_true', help='record hashes only (a PNG is ~2 MB: the grain defeats compression)')
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()

    if a.plan:
        if TIMES.exists() and not a.force:
            sys.exit(f'{TIMES.name} exists: the times are fixed. Pass --force to recompute them (and re-run every phase).')
        plan(root, a.lessons or PUBLISHED + EXTRA)
        return
    if not a.phase or not re.fullmatch(r'[\w.-]+', a.phase):
        sys.exit('usage: python stills_hash.py <phase>   (letters, digits, - _ . only)')
    times = json.loads(TIMES.read_text(encoding='utf-8'))
    slugs = a.lessons or [k for k in times if not k.startswith('_about')]
    unknown = [s for s in slugs if s not in times]
    if unknown:
        sys.exit(f'not in times.json: {unknown}')
    clash = [s for s in slugs if (OUT / s / f'{a.phase}.sha256.json').exists()]
    if clash and not a.force:
        sys.exit(f'phase "{a.phase}" already exists for {clash}. Pick a new phase name, or --force to overwrite it.')

    head = git(root, 'rev-parse', 'HEAD')
    env = {'python': sys.version.split()[0], 'platform': platform.platform()}
    try:
        from importlib.metadata import version
        env['playwright'] = version('playwright')
    except Exception:
        pass
    summary, t_all = {}, time.time()
    srv = Server(root) if a.driver == 'page' else None
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        for slug in slugs:
            t0 = time.time()
            roles = times[slug]['times']
            if a.driver == 'page':
                shots, meta = run_page(pw, srv, root, slug, roles, a.order)
            else:
                shots, meta = run_tools(root, slug, roles)
            dst = OUT / slug / a.phase
            if dst.exists():
                shutil.rmtree(dst)
            if not a.no_png:
                dst.mkdir(parents=True)
            hashes = {}
            for name in sorted(shots):
                if not a.no_png:
                    (dst / name).write_bytes(shots[name])
                hashes[name] = hashlib.sha256(shots[name]).hexdigest()
            rec = {'phase': a.phase, 'lesson': slug, 'when': time.strftime('%Y-%m-%d %H:%M:%S'), 'driver': a.driver,
                   'order': a.order if a.driver == 'page' else 'sorted (tools/stills.py)', 'root': str(root),
                   'git_head': head, 'git_dirty': git(root, 'status', '--porcelain', '--', 'engine', 'tools', f'lessons/{slug}').splitlines(),
                   'scenes_js_in_sync': scenes_js_in_sync(root / 'lessons' / slug), 'env': env,
                   'times': roles, 'pngs_kept': not a.no_png, 'sha256': hashes, 'seconds': round(time.time() - t0, 1), **meta}
            (OUT / slug / f'{a.phase}.sha256.json').write_text(json.dumps(rec, indent=1), encoding='utf-8')
            missing = sorted(set(f'{r}_{t:07.2f}.png' for r, t in roles.items()) - set(hashes))
            warn = []
            if missing:
                warn.append(f'MISSING {missing}')
            if meta.get('page_errors'):
                warn.append(f'{len(meta["page_errors"])} page errors/warnings')
            if meta.get('faces_lazy'):
                warn.append(f'{len(meta["faces_lazy"])} font subsets loaded only while drawing')
            if meta.get('failed_requests'):
                warn.append(f'failed requests {meta["failed_requests"]}')
            print(f'{slug}: {len(hashes)} stills, {rec["seconds"]} s' + (f'  [{"; ".join(warn)}]' if warn else ''), flush=True)
            summary[slug] = len(hashes)
    if srv:
        srv.close()
    print(json.dumps({'phase': a.phase, 'stills': summary, 'seconds': round(time.time() - t_all, 1)}))


if __name__ == '__main__':
    main()
