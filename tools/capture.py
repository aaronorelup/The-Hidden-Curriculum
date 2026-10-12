"""capture.py: record real actions on a computer for a lesson to SHOW (K.demo, K.shot, K.termReplay).

usage:
  python tools/capture.py browser  <lesson> <name> [--steps steps.json] [--headed]
  python tools/capture.py terminal <lesson> <name> [--steps steps.json]
  python tools/capture.py desktop  <lesson> <name> --seconds 12 (--window "part of its title" | --region x,y,w,h)
                                   [--fps 30] [--width 1920] [--no-mouse] [--countdown 3] [--steps steps.json]
  python tools/capture.py again    <lesson> <name>     re-record from lessons/<lesson>/steps/<name>.json (the recipe
                                                       people edit), else from the copy kept in the capture folder
  python tools/capture.py check    <lesson> [<name>]   video spec, file sizes and a secrets scan of the captures
  python tools/capture.py show     <lesson> <name>     a readable summary of events.json

Every capture lands in lessons/<lesson>/assets/capture/<name>/:
  events.json   what happened, on the video's clock (seconds): kind move / click / type / key / scroll / shot / nav /
                mark, the cursor x / y and the target's box in VIDEO pixels, typed text with per-key times, the
                boxes a shot or mark step measured. For a terminal capture: each command, its real output lines and
                their real timings.
  video.mp4     browser / desktop: the recording, re-encoded to the course clip spec (tools/media_util.py check)
  shots/*.webp  browser: real screenshots taken by `shot` steps (K.shot animates them; "format": "png" keeps a PNG)
  steps.json    a copy of the recipe it was recorded from (the recipe itself lives in lessons/<lesson>/steps/)
A recording goes to a sibling folder <name>.new first and replaces the capture only when it finished and passed
`check`: a failed or refused re-record says which step failed and leaves the old capture as it was.

Modes
  browser   Playwright drives a clean, throw-away Chromium profile (a fresh context: no cookies, no logins) through
            the steps file and records it with the DevTools screencast at the device pixel ratio (1280x720 CSS at
            dpr 1.5 = a crisp 1920x1080 video, so the engine's zoom stays sharp). The pointer is NOT in the video:
            the engine draws it from events.json (smooth, crisp, with click ripples). Runs headless.
  terminal  runs real commands, one after another, in a throw-away folder, and records each command, its real
            output (stdout and stderr, line by line) and the timings. The folder's real path and your home folder
            are replaced in the output by `cwd_display` / C:\\Users\\you. Runs headless.
  desktop   records a screen region or a window with ffmpeg gdigrab (draw_mouse on) for N seconds while a person or a
            computer-use agent acts, and logs the cursor and mouse buttons at 30 Hz (GetCursorPos, GetAsyncKeyState
            for the mouse buttons only: the keyboard is never logged). Needs an interactive desktop session. With
            --window it brings the window to the front, refuses to start while another window covers it and throws
            the recording away if one comes in front while it runs; a --region is filmed as it is.
            --steps desktop.json may add {"redact": [{"box": [x, y, w, h], "from": s, "to": s}]} (pixels of the area).

Safety (hard rules, also in docs/showing-real-computer-actions.md): never record real keys, tokens, passwords, emails
or personal data. Use public pages and test accounts. capture.py refuses typed text and terminal output that looks
like a secret or a real email (or contains one of the keys stored in ~/.claude/secrets, the home folder's path,
this machine's account or computer name), refuses env-dumping commands, and blurs every `redact` box. Look at the result before committing it: the repo is public.

steps.json (browser):
  {"mode": "browser", "size": [1280, 720], "dpr": 1.5, "fps": 30, "crf": 20, "color_scheme": "dark",
   "start": [900, 560],                          cursor start (CSS px)
   "redact": [{"selector": ".account-email"},    blurred live in the page (follows scrolling)
              {"box": [x, y, w, h], "from": 0, "to": 4.5}],   blurred in the video and shots (CSS px, seconds)
   "steps": [
     {"do": "goto", "url": "https://aaronorelup.com/courses/the-hidden-curriculum/"},   a first goto runs before
                                                   the recording starts, so the video opens on a loaded page
     {"do": "wait", "ms": 800},
     {"do": "move", "text": "Browse the map", "ms": 900},          move the pointer onto a target (or "to": [x, y])
     {"do": "hover", "target": "a.lesson", "ms": 800},             move there and rest
     {"do": "scroll", "to": "text=Files are just bytes", "block": 0.45, "ms": 1600},   or "by": 600
     {"do": "click", "text": "Files are just bytes", "nav": true},  "nav": the click loads a new page
     {"do": "type", "target": "input[name=q]", "text": "hello", "delay": 95},   per-key delay (ms, +-35 %)
     {"do": "press", "key": "Enter"},
     {"do": "wait_for", "js": "window.__readyDone === true", "timeout": 30000},   or "selector": "..."
     {"do": "mark", "name": "playing", "boxes": {"stage": "#stage"}},   a named moment + element boxes (K.captureAt,
                                                   K.captureBox): scenes read times and positions, never type them in
     {"do": "shot", "name": "lesson-page", "boxes": {"card": ".hc-feature"}},   a real screenshot (WebP), with boxes
     {"do": "shot", "name": "next-page", "href": "a.hc-feature", "wait_for_js": "window.__readyDone === true"}]}
                                                   a side shot: where that link leads (or "url"), opened in a second
                                                   tab the video never shows: the "after" picture for K.shot's swap
  Targets: "target" (any Playwright selector: css, text=..., role=...), "text" (visible text, first match),
  "selector" (css). "at": [fx, fy] aims at that fraction of the target's box (default its centre).
steps.json (terminal):
  {"mode": "terminal", "shell": "cmd" | "powershell" | "bash", "cwd_display": "C:\\Users\\you\\demo",
   "prompt": optional (default from the shell: cmd "C:\\Users\\you\\demo>", powershell "PS ...>", bash "$ "),
   "env": {...}, "timeout": 60, "commands": ["python --version", "git --version", "git init", "git status"],
   "git_config": "neutral" (default: no system or global git config, so the output is what a fresh git prints on
                 any machine and no real name or email can show) | "machine" (this machine's config)}
  The output has the throw-away folder, the home folder, the account name (-> you) and the computer name
  (-> DEMO-PC) rewritten; commands that list the environment (set, env, printenv, cmd /c set, dir env:,
  Get-ChildItem env:, [Environment]::GetEnvironmentVariables()...) are refused.
"""
import argparse
import asyncio
import base64
import datetime
import json
import math
import os
import pathlib
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import media_util as mu  # noqa: E402
from common import lesson_dir  # noqa: E402

PAGES_LIMIT = 25 * 1000 * 1000
VERSION = 1


# ------------------------------------------------------------------ safety
SECRET_PATTERNS = [
    (r'sk-ant-[A-Za-z0-9_-]{10,}', 'an Anthropic API key'),
    (r'\bsk-[A-Za-z0-9_-]{16,}', 'an API key (sk-...)'),
    (r'\bgh[pousr]_[A-Za-z0-9]{20,}', 'a GitHub token'),
    (r'github_pat_[A-Za-z0-9_]{20,}', 'a GitHub token'),
    (r'\bAKIA[0-9A-Z]{16}\b', 'an AWS access key'),
    (r'\bxox[baprs]-[A-Za-z0-9-]{10,}', 'a Slack token'),
    (r'\bAIza[0-9A-Za-z_-]{30,}', 'a Google API key'),
    (r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.', 'a JWT'),
    (r'-----BEGIN [A-Z ]*PRIVATE KEY-----', 'a private key'),
    (r'(?i)\b(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*\S{6,}', 'a credential assignment'),
]
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}')
SAFE_EMAIL_DOMAINS = ('example.com', 'example.org', 'example.net', '.example', '.test', '.invalid', 'users.noreply.github.com')
# commands that print the whole environment (which holds keys, tokens, the account and the computer name): a bare
# set / env / printenv / export / declare anywhere in a command line (cmd /c set, `env | sort`), PowerShell's env:
# drive listed (dir env:, gci env:*, Get-Item env:*, Get-ChildItem -Path env:), .NET's GetEnvironmentVariables, and
# a single variable whose name says key / token / secret / pass. One named variable ($env:PATH, %PATH%) is allowed:
# the account and computer names in it are rewritten (clean_names) and anything secret-shaped is refused (scan).
ENV_DUMPS = re.compile(
    r'(^|[\s&|;(/])(set|env|printenv|export|declare)(\s+-p)?\s*($|[&|>;)])'
    r'|\b(gci|gi|ls|dir|get-item|get-childitem)\s+(-path\s+|-literalpath\s+)?env:'
    r'|(^|[\s"\'(])env:\s*\*?\s*($|[|;&)>"\'])'
    r'|GetEnvironmentVariables|\bos\.environ\b(?!\s*[\[.])|\bprocess\.env\b(?!\s*[\[.])'
    r'|\$env:\w*(key|token|secret|pass)|%\w*(key|token|secret|pass)\w*%', re.I)


_NAMES = None


def machine_names():
    """the names that identify this machine and account and must never reach a public repo: the Windows account
    (getpass.getuser), the computer name (socket.gethostname, %COMPUTERNAME%, %USERDOMAIN%) -> what replaces each"""
    global _NAMES
    if _NAMES is not None:
        return _NAMES
    import getpass
    import socket
    names = _NAMES = {}
    for v, rep in ((getpass.getuser(), 'you'), (os.environ.get('USERNAME'), 'you'), (socket.gethostname(), 'DEMO-PC'),
                   (os.environ.get('COMPUTERNAME'), 'DEMO-PC'), (os.environ.get('USERDOMAIN'), 'DEMO-PC')):
        v = (v or '').strip()
        # a name of one or two letters, or a word every page uses, would match everywhere: not a usable signal
        if len(v) >= 3 and v.lower() not in ('you', 'user', 'users', 'admin', 'administrator', 'demo', 'demo-pc', 'localhost'):
            names.setdefault(v.lower(), rep)
    return names


def _name_rx(name):
    """whole-word, case-insensitive: 'soulo' matches 'laptop\\soulo' and 'soulo.' but not 'soulmate'"""
    return re.compile(r'(?<![A-Za-z0-9_-])' + re.escape(name) + r'(?![A-Za-z0-9_-])', re.I)


def clean_names(text):
    """terminal output: the account name -> you, the computer name -> DEMO-PC (whoami, hostname, %USERNAME%...)"""
    for name, rep in sorted(machine_names().items(), key=lambda kv: -len(kv[0])):
        text = _name_rx(name).sub(rep, text)
    return text


def stored_secrets():
    """the values in ~/.claude/secrets/*.key (held in memory only, to make sure none of them is ever recorded)"""
    d = pathlib.Path.home() / '.claude' / 'secrets'
    vals = []
    for f in d.glob('*.key') if d.is_dir() else []:
        try:
            v = f.read_text(encoding='utf-8').strip()
            if len(v) >= 8:
                vals.append(v)
        except OSError:
            pass
    return vals


_SECRETS = None


def scan(text):
    """what in `text` looks like a secret or personal data: a list of reasons (empty = clean)"""
    global _SECRETS
    if _SECRETS is None:
        _SECRETS = stored_secrets()
    text = str(text or '')
    found = [why for rx, why in SECRET_PATTERNS if re.search(rx, text)]
    for m in EMAIL.finditer(text):
        dom = m.group(0).split('@', 1)[1].lower()
        if not any(dom == s.lstrip('.') or dom.endswith(s if s.startswith('.') else '.' + s) or dom == s for s in SAFE_EMAIL_DOMAINS):
            found.append(f'an email address ({m.group(0)[:2]}...@{dom}); use an @example.com test address')
    if any(s in text for s in _SECRETS):
        found.append('one of the keys stored in ~/.claude/secrets')
    home = str(pathlib.Path.home())
    if home.lower() in text.lower() or home.replace('\\', '/').lower() in text.lower():
        found.append(f'your home folder path (it names your account); it should read C:\\Users\\you')
    for name, rep in machine_names().items():
        if _name_rx(name).search(text):
            found.append(f'this machine\'s {"account" if rep == "you" else "computer"} name ({name[:2]}...); '
                         f'it should read {rep}')
    return sorted(set(found))


def refuse_if(text, where):
    bad = scan(text)
    if bad:
        raise SystemExit(f'capture.py refused: {where} contains {", ".join(bad)}.\n'
                         f'Never record real keys, tokens, emails or personal data: use public pages, test accounts and '
                         f'@example.com addresses.')


# ------------------------------------------------------------------ helpers
def cap_dir(lesson, name):
    if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', name):
        raise SystemExit(f'capture name {name!r}: use lowercase letters, digits, - and _')
    return lesson_dir(lesson) / 'assets' / 'capture' / name


def write_json(path, data):
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


def min_jerk(u):
    """the minimum-jerk profile of a human reach: quick start, long soft landing"""
    u = max(0.0, min(1.0, u))
    return u * u * u * (10 - 15 * u + 6 * u * u)


def today():
    return datetime.date.today().isoformat()


def r2(v):
    return round(float(v), 2)


def r3(v):
    return round(float(v), 3)


# ------------------------------------------------------------------ browser
CURSOR_JS = """([x, y]) => { let el = document.elementFromPoint(x, y);
  while (el && el.nodeType === 1) { const c = getComputedStyle(el).cursor; if (c && c !== 'auto') return c; el = el.parentElement; }
  return 'auto'; }"""
SCROLLER_JS = """([x, y]) => { document.querySelectorAll('[data-hc-scroller]').forEach((e) => e.removeAttribute('data-hc-scroller'));
  let el = document.elementFromPoint(x, y);
  while (el && el !== document.body && el !== document.documentElement) {
    const s = getComputedStyle(el);
    if (/(auto|scroll)/.test(s.overflowY) && el.scrollHeight > el.clientHeight + 2) { el.setAttribute('data-hc-scroller', '1'); return true; }
    el = el.parentElement; }
  return false; }"""


RAF_SCROLL_JS = """([sel, dy, ms]) => new Promise((res) => {
  const el = sel ? document.querySelector(sel) : null;
  const get = () => (el ? el.scrollTop : scrollY), set = (v) => (el ? (el.scrollTop = v) : scrollTo(0, v));
  const root = el || document.scrollingElement || document.documentElement;
  const from = get(), to = Math.max(0, Math.min(root.scrollHeight - root.clientHeight, from + dy)), t0 = performance.now();
  if (Math.abs(to - from) < 1) { res(0); return; }   // already at that end: nothing to animate, no time spent
  dy = to - from;
  const ease = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
  const step = (now) => { const u = Math.min(1, (now - t0) / ms); set(from + dy * ease(u));
    if (u < 1) requestAnimationFrame(step); else res(get() - from); };
  requestAnimationFrame(step); })"""


def shape_of(css):
    return 'hand' if css == 'pointer' else 'text' if css in ('text', 'vertical-text') else 'arrow'


class StepFailed(Exception):
    """a step of a recording failed: run_spec reports it in one line and keeps the old capture"""


def save_still(src, dst, lossless=False, quality=92):
    """a shot -> its file: WebP by default (quality 92 keeps UI text clean at a fifth of the PNG: course-page 518 ->
    about 130 KB, a lesson frame 1351 -> about 100 KB; "lossless": true is about 30 % under the PNG), or .png"""
    from PIL import Image
    dst = pathlib.Path(dst)
    im = Image.open(src).convert('RGB')
    if dst.suffix == '.png':
        im.save(dst, optimize=True)
    else:
        im.save(dst, 'WEBP', lossless=lossless, quality=100 if lossless else quality, method=6)


class BrowserCapture:
    def __init__(self, spec, out, headed=False):
        self.spec, self.out, self.headed = spec, out, headed
        self.W, self.H = spec.get('size', [1280, 720])
        self.dpr = float(spec.get('dpr', 1.5))
        self.events, self.frames, self.shots = [], [], []
        self.shapes = []                 # [wall time, 'arrow' | 'hand' | 'text']
        self.cur = tuple(spec.get('start', [self.W * 0.66, self.H * 0.72]))
        self.rng = random.Random(spec.get('seed', 7))
        self.flip = 1
        self.t0 = None
        self.titles = {}                 # url -> page title (for the window title / address bar)
        self.frame_dir = None
        self.page = self.cdp = None

    # -- the recording
    async def on_frame(self, params):
        ts = params.get('metadata', {}).get('timestamp') or time.time()
        path = self.frame_dir / f'{len(self.frames):06d}.jpg'
        self.frames.append((ts, path))
        path.write_bytes(base64.b64decode(params['data']))
        try:                                     # ack at once: Chrome sends the next frame only after the ack
            await self.cdp.send('Page.screencastFrameAck', {'sessionId': params['sessionId']})
        except Exception:
            pass

    def ev(self, kind, wall, **kw):
        self.events.append({'wall': wall, 'kind': kind, **kw})

    async def on_load(self):
        try:
            self.titles[self.page.url] = await self.page.title()
        except Exception:
            pass

    # -- pointer and targets
    async def shape_at(self, x, y):
        try:
            return shape_of(await self.page.evaluate(CURSOR_JS, [x, y]))
        except Exception:
            return 'arrow'

    async def note_shape(self, x, y, wall=None):
        s = await self.shape_at(x, y)
        if not self.shapes or self.shapes[-1][1] != s:
            self.shapes.append((wall or time.time(), s))

    def locator(self, step):
        p = self.page
        if step.get('target'):
            return p.locator(step['target']).first
        if step.get('selector'):
            return p.locator(step['selector']).first
        if step.get('text'):
            return p.get_by_text(step['text'], exact=bool(step.get('exact'))).first
        if step.get('role'):
            return p.get_by_role(step['role'], name=step.get('name')).first
        return None

    def describe(self, step):
        for k in ('target', 'selector', 'text', 'role'):
            if step.get(k):
                return f'{k}={step[k]}'
        return ''

    async def box_of(self, step, visible=True):
        loc = self.locator(step)
        if loc is None:
            return None
        await loc.wait_for(state='attached', timeout=step.get('timeout', 15000))
        if visible:
            await self.ensure_visible(loc, step)
        b = await loc.bounding_box()
        if not b:
            raise SystemExit(f'step {step}: the target has no box (hidden?)')
        return [b['x'], b['y'], b['width'], b['height']]

    def aim(self, box, at=None):
        fx, fy = at or [0.5, 0.5]
        return box[0] + box[2] * fx, box[1] + box[3] * fy

    async def move_to(self, x, y, ms=None):
        x0, y0 = self.cur
        dist = math.hypot(x - x0, y - y0)
        if dist < 1:
            return
        ms = ms or max(380, min(1300, 330 + dist * 0.6))
        nx, ny = -(y - y0) / dist, (x - x0) / dist
        self.flip = -self.flip
        bow = min(70.0, dist * 0.1) * self.flip
        start = time.time()
        path = []
        k = 0
        while True:
            u = min(1.0, (time.time() - start) / (ms / 1000))
            e = min_jerk(u)
            arc = math.sin(math.pi * e) * bow
            px, py = x0 + (x - x0) * e + nx * arc, y0 + (y - y0) * e + ny * arc
            await self.page.mouse.move(px, py)
            now = time.time()
            path.append((now, px, py))
            if k % 3 == 2 or u >= 1:
                await self.note_shape(px, py, now)
            k += 1
            if u >= 1:
                break
            await asyncio.sleep(1 / 90)
        self.cur = (x, y)
        self.ev('move', start, t1=path[-1][0], x=x, y=y, path=path)

    async def scroll_by(self, dy, ms=None, wall_ev=True):
        """eased scroll of whatever scrolls under the pointer (a page or an inner panel), animated inside the page on
        requestAnimationFrame, so every rendered frame shows the position for its own moment (smooth in the video)"""
        if abs(dy) < 1:
            return
        ms = ms or max(900, min(3200, 700 + abs(dy) * 1.1))
        inner = await self.page.evaluate(SCROLLER_JS, list(self.cur))
        sel = '[data-hc-scroller]' if inner else None
        start = time.time()
        moved = await self.page.evaluate(RAF_SCROLL_JS, [sel, dy, ms])
        if abs(moved) < 1:           # nothing scrolled (already at that end): no event, so no camera break either
            return 0
        if wall_ev:
            self.ev('scroll', start, t1=time.time(), dy=moved * self.dpr, x=self.cur[0], y=self.cur[1])
        await self.note_shape(*self.cur)
        return moved

    async def ensure_visible(self, loc, step):
        b = await loc.bounding_box()
        if not b:
            return
        margin = 40
        if b['y'] >= margin and b['y'] + b['height'] <= self.H - margin:
            return
        target = self.H * step.get('block', 0.42)
        if await self.scroll_by(b['y'] + b['height'] / 2 - target, step.get('scroll_ms')):
            await asyncio.sleep(0.25)

    # -- steps
    async def step(self, s):
        p, do = self.page, s.get('do')
        if do == 'goto':
            await p.goto(s['url'], wait_until=s.get('wait_until', 'load'))
            await asyncio.sleep(s.get('settle', 400) / 1000)
        elif do == 'wait':
            await asyncio.sleep(s.get('ms', 500) / 1000)
        elif do == 'wait_for':
            if s.get('js'):
                await p.wait_for_function(s['js'], timeout=s.get('timeout', 30000))
            else:
                await self.locator(s).wait_for(state='visible', timeout=s.get('timeout', 30000))
            await asyncio.sleep(s.get('settle', 0) / 1000)
        elif do in ('move', 'hover'):
            if s.get('to'):
                x, y = s['to']
                box = None
            else:
                box = await self.box_of(s)
                x, y = self.aim(box, s.get('at'))
            await self.move_to(x, y, s.get('ms') if do == 'move' else None)
            if box:
                self.events[-1]['box'] = box
                self.events[-1]['target'] = self.describe(s)
            if do == 'hover':
                await asyncio.sleep(s.get('ms', 700) / 1000)
        elif do == 'scroll':
            if s.get('at'):
                await self.move_to(*s['at'])
            if s.get('by') is not None:
                await self.scroll_by(s['by'], s.get('ms'))
            else:
                loc = self.locator({**s, 'target': s.get('to')} if s.get('to') else s)
                await loc.wait_for(state='attached', timeout=s.get('timeout', 15000))
                b = await loc.bounding_box()
                await self.scroll_by(b['y'] + b['height'] / 2 - self.H * s.get('block', 0.42), s.get('ms'))
            await asyncio.sleep(s.get('settle', 250) / 1000)
        elif do == 'click':
            box = await self.box_of(s)
            x, y = self.aim(box, s.get('at'))
            await self.move_to(x, y, s.get('ms'))
            await asyncio.sleep(s.get('pause', 180) / 1000)
            shape = await self.shape_at(x, y)
            wall = time.time()
            if s.get('nav'):
                async with p.expect_navigation(wait_until=s.get('wait_until', 'load'), timeout=s.get('timeout', 30000)):
                    await p.mouse.down(button=s.get('button', 'left'))
                    await asyncio.sleep(0.085)
                    await p.mouse.up(button=s.get('button', 'left'))
            else:
                await p.mouse.down(button=s.get('button', 'left'))
                await asyncio.sleep(0.085)
                await p.mouse.up(button=s.get('button', 'left'))
            self.ev('click', wall, x=x, y=y, box=box, target=self.describe(s), cursor=shape, button=s.get('button', 'left'))
            await asyncio.sleep(s.get('after', 250) / 1000)
            await self.note_shape(*self.cur)
        elif do == 'type':
            text = str(s['text'])
            refuse_if(text, f'typed text {text[:12]!r}...')
            box = None
            if any(s.get(k) for k in ('target', 'selector', 'text_target', 'role')):
                box = await self.box_of({k: v for k, v in s.items() if k != 'text'} | ({'text': s['text_target']} if s.get('text_target') else {}))
                x, y = self.aim(box, s.get('at'))
                await self.move_to(x, y)
                await asyncio.sleep(0.15)
                shape = await self.shape_at(x, y)
                wall = time.time()               # stamped as the button goes down: the field takes focus on mousedown
                await p.mouse.down()
                await asyncio.sleep(0.07)
                await p.mouse.up()
                self.ev('click', wall, x=x, y=y, box=box, target='focus', cursor=shape)
                await asyncio.sleep(0.3)
            delay = s.get('delay', 95) / 1000
            keys, start = [], time.time()
            for ch in text:
                keys.append((time.time(), ch))  # stamped as the key goes down: the character shows a frame or two later
                await p.keyboard.type(ch)
                d = delay * (0.65 + 0.7 * self.rng.random()) + (delay * 0.8 if ch == ' ' else 0)
                await asyncio.sleep(d)
            if box is None:
                box = await p.evaluate("() => { const e = document.activeElement; if (!e || e === document.body) return null;"
                                       " const r = e.getBoundingClientRect(); return [r.x, r.y, r.width, r.height]; }")
            # the field's own text size, so K.demo shows a typing chip only while that text is too small to read
            font = await p.evaluate("() => { const e = document.activeElement; return e && e !== document.body ?"
                                    " parseFloat(getComputedStyle(e).fontSize) || null : null; }")
            self.ev('type', start, t1=keys[-1][0] if keys else start, text=text, keys=keys, box=box, x=self.cur[0], y=self.cur[1],
                    font=font)
        elif do == 'press':
            wall = time.time()
            if s.get('nav'):
                async with p.expect_navigation(wait_until=s.get('wait_until', 'load')):
                    await p.keyboard.press(s['key'])
            else:
                await p.keyboard.press(s['key'])
            self.ev('key', wall, key=s['key'], x=self.cur[0], y=self.cur[1])
            await asyncio.sleep(s.get('after', 250) / 1000)
        elif do == 'shot':
            name = s['name']
            if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', name):
                raise SystemExit(f'shot name {name!r}: use lowercase letters, digits, - and _')
            fmt = s.get('format', 'webp')
            if fmt not in ('webp', 'png'):
                raise SystemExit(f'shot {name}: "format" is webp (default) or png')
            wall = time.time()
            file = f'shots/{name}.{fmt}'
            shot = {'name': name, 'file': file, 'raw': self.frame_dir / f'shot-{name}.png', 'wall': wall, 'side': False,
                    'lossless': bool(s.get('lossless')), 'quality': s.get('quality', 92)}
            if s.get('url') or s.get('href'):
                # a side shot: a page the video never shows (where a link leads, or any url), the "after" picture for
                # K.shot's swap. The link is read now; the page is opened in a second tab of the same throw-away
                # profile at the same size AFTER the recording stops (side_shots), so loading it costs the video nothing
                url = s.get('url') or await self.locator({'target': s['href']}).evaluate('(e) => e.href')
                refuse_if(url, f'the url {url}')
                shot.update(side=True, url=url, step=s)
                self.ev('shot', wall, name=name, file=file, url=url, side=True)
                self.shots.append(shot)
                return
            await p.screenshot(path=str(shot['raw']))
            shot.update(boxes=await self.boxes_of(s.get('boxes'), p), url=p.url, title=await p.title())
            # a screenshot can stall the screencast until the next navigation (seen 2026-10-12): restart it
            await self.cdp.send('Page.stopScreencast')
            await self.cdp.send('Page.startScreencast', self.cast)
            self.ev('shot', wall, name=name, file=file, url=p.url)
            self.shots.append(shot)
        elif do == 'mark':
            # a named moment on the capture's clock (K.captureAt) with the boxes of some elements then (K.captureBox),
            # so scenes never hard-code times or positions that move when the capture is re-recorded
            name = s['name']
            if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', name):
                raise SystemExit(f'mark name {name!r}: use lowercase letters, digits, - and _')
            wall = time.time()
            self.ev('mark', wall, name=name, boxes=await self.boxes_of(s.get('boxes'), p))
        else:
            raise SystemExit(f'unknown step {s!r}')

    async def side_shots(self, ctx):
        """take the side shots (another page, not in the video) once the recording has stopped"""
        for sh in [x for x in self.shots if x['side']]:
            s = sh['step']
            side = await ctx.new_page()
            try:
                to = s.get('timeout', 30000)
                await side.goto(sh['url'], wait_until=s.get('wait_until', 'load'), timeout=to)
                if s.get('wait_for_js'):
                    await side.wait_for_function(s['wait_for_js'], timeout=to)
                if s.get('wait_for'):
                    await side.locator(s['wait_for']).first.wait_for(state='visible', timeout=to)
                await asyncio.sleep(s.get('settle', 600) / 1000)
                await side.screenshot(path=str(sh['raw']))
                sh.update(boxes=await self.boxes_of(s.get('boxes'), side), url=side.url, title=await side.title())
            except Exception as e:
                raise StepFailed(f'the side shot {sh["name"]} ({sh["url"]}): {str(e).strip().splitlines()[0]}') from None
            finally:
                await side.close()

    async def boxes_of(self, sels, pg):
        """{name: css selector} -> {name: [x, y, w, h] in CSS px of the viewport, or None when missing / hidden}"""
        out = {}
        for k, sel in (sels or {}).items():
            try:
                b = await pg.locator(sel).first.bounding_box(timeout=3000)
            except Exception:
                b = None
            out[k] = [b['x'], b['y'], b['width'], b['height']] if b else None
        return out

    async def run(self):
        from playwright.async_api import async_playwright
        spec = self.spec
        steps = list(spec.get('steps', []))
        redact_css = ''.join(f"{r['selector']}{{filter:blur(14px)!important}}" for r in spec.get('redact', []) if r.get('selector'))
        self.frame_dir = pathlib.Path(tempfile.mkdtemp(prefix='hc-cap-'))
        try:
            async with async_playwright() as pw:
                args = [f'--force-device-scale-factor={self.dpr:g}']
                if spec.get('scrollbars') is False:
                    args.append('--hide-scrollbars')
                browser = await pw.chromium.launch(headless=not self.headed, args=args)
                # a fresh context is a clean, throw-away profile: no cookies, storage, logins or extensions
                ctx = await browser.new_context(viewport={'width': self.W, 'height': self.H}, device_scale_factor=self.dpr,
                                                locale=spec.get('locale', 'en-US'), timezone_id=spec.get('timezone', 'UTC'),
                                                color_scheme=spec.get('color_scheme', 'dark'), service_workers='block',
                                                accept_downloads=False)
                if redact_css:
                    await ctx.add_init_script("document.addEventListener('DOMContentLoaded', () => { const s = document.createElement('style');"
                                              f" s.textContent = {json.dumps(redact_css)}; document.head.appendChild(s); }});")
                self.page = p = await ctx.new_page()
                p.on('framenavigated', lambda fr: fr == p.main_frame and self.ev('nav', time.time(), url=fr.url))
                p.on('load', lambda _=None: asyncio.ensure_future(self.on_load()))
                first_goto = 0
                if steps and steps[0].get('do') == 'goto':
                    first = steps.pop(0)
                    first_goto = 1
                    try:
                        await p.goto(first['url'], wait_until=first.get('wait_until', 'load'))
                    except Exception as e:
                        raise StepFailed(f'step 1 (goto {first["url"]}): {str(e).strip().splitlines()[0]}') from None
                    await asyncio.sleep(first.get('settle', 900) / 1000)
                    self.events = [e for e in self.events if e['kind'] != 'nav']
                await p.mouse.move(*self.cur)
                await self.note_shape(*self.cur)
                self.cdp = await ctx.new_cdp_session(p)
                self.cdp.on('Page.screencastFrame', lambda prm: asyncio.ensure_future(self.on_frame(prm)))
                self.cast = {'format': 'jpeg', 'quality': spec.get('jpeg', 92),
                             'maxWidth': round(self.W * self.dpr), 'maxHeight': round(self.H * self.dpr)}
                await self.cdp.send('Page.startScreencast', self.cast)
                rec_start = time.time()
                self.titles[p.url] = await p.title()
                self.ev('nav', rec_start, url=p.url)
                self.shapes = [(rec_start, self.shapes[-1][1] if self.shapes else 'arrow')]
                await asyncio.sleep(spec.get('lead', 600) / 1000)
                for i, s in enumerate(steps):
                    try:
                        await self.step(s)
                    except (Exception, SystemExit) as e:
                        # name the step that failed, not a traceback (the first line of a Playwright error says why)
                        msg = str(e).strip().splitlines()[0] if str(e).strip() else type(e).__name__
                        raise StepFailed(f'step {i + 1 + first_goto} of {len(steps) + first_goto} '
                                         f'({s.get("do")}{" " + self.describe(s) if self.describe(s) else ""}): {msg}') from None
                await asyncio.sleep(spec.get('tail', 900) / 1000)
                end = time.time()
                await self.cdp.send('Page.stopScreencast')
                await asyncio.sleep(0.2)
                await self.side_shots(ctx)
                await browser.close()
            if not self.frames:
                raise SystemExit('no frames were recorded')
            self.frames.sort(key=lambda f: f[0])
            self.t0 = self.frames[0][0]
            self.finish(end)
        finally:
            shutil.rmtree(self.frame_dir, ignore_errors=True)

    # -- output
    def finish(self, end):
        spec, out, dpr, t0 = self.spec, self.out, self.dpr, self.t0
        fps = int(spec.get('fps', 30))
        dur = end - t0
        # the screencast delivers frames when the page changes (about 50 a second while it moves, none while it rests).
        # Resample them here to a constant `fps`, piped to ffmpeg, by sample-and-hold: output frame i (it is on show
        # from i / fps, and the renderer seeks to its centre) takes the NEWEST screencast frame delivered at or before
        # its centre. Never the nearest one: after a quiet stretch the next frame can be a second away, and taking it
        # early would show a page reacting before the click that caused it (seen 2026-10-12: up to 0.63 s early).
        # (The ffmpeg concat demuxer would quantise the frame times to 1/25 s and drop every sixth frame.)
        W, H = round(self.W * dpr), round(self.H * dpr)
        W, H = W - W % 2, H - H % 2
        raw = self.frame_dir / 'raw.mkv'
        vf = [f'scale={W}:{H}:flags=lanczos', 'format=rgb24']
        boxes = [r for r in spec.get('redact', []) if r.get('box')]
        graph = ','.join(vf)
        src = ['-f', 'image2pipe', '-framerate', str(fps), '-c:v', 'mjpeg', '-i', '-']
        if boxes:
            graph = f'[0:v]{graph},split={len(boxes) + 1}[b0]' + ''.join(f'[c{i}]' for i in range(len(boxes)))
            for i, r in enumerate(boxes):
                x, y, w, h = (round(v * dpr) for v in r['box'])
                a, b = r.get('from', 0), r.get('to', 1e9)
                graph += f';[c{i}]crop={w}:{h}:{x}:{y},boxblur=24:3[k{i}];[b{i}][k{i}]overlay={x}:{y}:enable=\'between(t,{a},{b})\'[b{i + 1}]'
            cmd = [mu.ffmpeg(), '-v', 'error', '-y', *src, '-filter_complex', graph, '-map', f'[b{len(boxes)}]']
        else:
            cmd = [mu.ffmpeg(), '-v', 'error', '-y', *src, '-vf', graph]
        cmd += ['-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast', str(raw)]
        n_out = max(1, int(dur * fps))
        ff = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        j, cache = 0, (None, b'')
        for i in range(n_out):
            tick = t0 + i / fps
            while j + 1 < len(self.frames) and self.frames[j + 1][0] <= tick + 0.5 / fps:
                j += 1
            if cache[0] != j:
                cache = (j, self.frames[j][1].read_bytes())
            ff.stdin.write(cache[1])
        ff.stdin.close()
        err = ff.stderr.read().decode('utf-8', 'replace')
        if ff.wait():
            raise SystemExit(f'ffmpeg failed assembling the frames:\n{err[-1500:]}')
        print(f'  {len(self.frames)} screencast frames -> {n_out} frames at {fps} fps')
        problems = mu.encode(raw, out / 'video.mp4', fps=fps, crf=spec.get('crf', 20))
        if problems:
            raise SystemExit(f'video.mp4 breaks the clip spec: {problems}')
        vdur = mu.probe(out / 'video.mp4')['format'].get('duration')

        def T(w):
            return r3(max(0.0, w - t0))

        def P(v):
            return r2(v * dpr)

        events = []
        for e in sorted(self.events, key=lambda e: e['wall']):
            o = {'t': T(e['wall']), 'kind': e['kind']}
            if 't1' in e:
                o['t1'] = T(e['t1'])
            for k in ('x', 'y'):
                if k in e:
                    o[k] = P(e[k])
            if e.get('box'):
                o['box'] = [P(v) for v in e['box']]
            if e['kind'] == 'move':
                o['path'] = [[T(w), P(x), P(y)] for w, x, y in e['path']]
            if e['kind'] == 'type':
                o['text'] = e['text']
                o['keys'] = [[T(w), ch] for w, ch in e['keys']]
            if e['kind'] == 'scroll':
                o['dy'] = r2(e['dy'])
            if e['kind'] == 'nav':
                o['title'] = self.titles.get(e['url'], '')
            if e.get('font'):
                o['fontPx'] = P(e['font'])
            if e.get('boxes') is not None:
                o['boxes'] = {k: ([P(v) for v in b] if b else None) for k, b in e['boxes'].items()}
            for k in ('key', 'target', 'cursor', 'button', 'url', 'title', 'name', 'file', 'side'):
                if e.get(k) is not None:
                    o[k] = e[k]
            events.append(o)
        sx, sy = spec.get('start', [self.W * 0.66, self.H * 0.72])
        shots = []
        if self.shots:
            (out / 'shots').mkdir(exist_ok=True)
        for s in self.shots:
            # a side shot (another page) is not part of the video: no time-boxed video redaction applies to it
            self.redact_shot(s['raw'], None if s['side'] else T(s['wall']))
            save_still(s['raw'], out / s['file'], lossless=s['lossless'], quality=s['quality'])
            shots.append({'name': s['name'], 'file': s['file'], 't': T(s['wall']), 'url': s['url'], 'title': s.get('title', ''),
                          'size': [W, H], **({'side': True} if s['side'] else {}),
                          **({'boxes': {k: ([P(v) for v in b] if b else None) for k, b in s['boxes'].items()}} if s.get('boxes') else {})})
        data = {
            'version': VERSION, 'kind': 'browser', 'recorded': today(), 'tool': 'tools/capture.py browser',
            'video': 'video.mp4', 'size': [W, H], 'viewport': [self.W, self.H], 'dpr': dpr, 'fps': fps,
            'duration': r3(float(vdur) if vdur else dur),
            'start': {'x': P(sx), 'y': P(sy)},
            'events': events,
            'shapes': [[T(w), s] for w, s in self.shapes],
            'shots': shots,
            'redact': spec.get('redact', []),
        }
        write_json(out / 'events.json', data)
        size = (out / 'video.mp4').stat().st_size
        print(f'wrote {out / "video.mp4"} ({size / 1e6:.2f} MB, {W}x{H}, {data["duration"]:.1f} s), '
              f'{len(events)} events, {len(shots)} shots')

    def redact_shot(self, path, t):
        """blur the redact boxes that apply at capture time t (t None: a side shot of another page, which only the
        boxes without a time window apply to)"""
        boxes = [r for r in self.spec.get('redact', []) if r.get('box') and (
            r.get('from', 0) <= t <= r.get('to', 1e9) if t is not None else ('from' not in r and 'to' not in r))]
        if not boxes:
            return
        from PIL import Image, ImageFilter
        im = Image.open(path).convert('RGB')
        for r in boxes:
            x, y, w, h = (round(v * self.dpr) for v in r['box'])
            im.paste(im.crop((x, y, x + w, y + h)).filter(ImageFilter.GaussianBlur(18)), (x, y))
        im.save(path)


def capture_browser(spec, out, headed=False):
    for s in spec.get('steps', []):
        if s.get('do') == 'type':
            refuse_if(s.get('text', ''), 'a type step')
        for k in ('url',):
            if s.get(k):
                refuse_if(s[k], f'the url {s[k]}')
    asyncio.run(BrowserCapture(spec, out, headed).run())


# ------------------------------------------------------------------ terminal
ANSI = re.compile(r'\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b\][^\x07]*\x07')
DEMO_ENV = {'GIT_AUTHOR_NAME': 'Demo Learner', 'GIT_AUTHOR_EMAIL': 'learner@example.com',
            'GIT_COMMITTER_NAME': 'Demo Learner', 'GIT_COMMITTER_EMAIL': 'learner@example.com',
            'NO_COLOR': '1', 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1', 'GIT_PAGER': 'cat', 'PAGER': 'cat'}


def shell_argv(shell, cmd):
    if shell == 'cmd':
        return ['cmd', '/d', '/s', '/c', cmd]
    if shell == 'powershell':
        return ['powershell', '-NoLogo', '-NoProfile', '-NonInteractive', '-Command', cmd]
    if shell == 'bash':
        return ['bash', '-c', cmd]
    raise SystemExit(f'unknown shell {shell!r} (cmd, powershell or bash)')


def default_prompt(shell, cwd_display):
    if shell == 'cmd':
        return f'{cwd_display}>'
    if shell == 'powershell':
        return f'PS {cwd_display}> '
    return '$ '


def decode(b):
    try:
        return b.decode('utf-8')
    except UnicodeDecodeError:
        return b.decode('cp437', errors='replace')


def capture_terminal(spec, out):
    shell = spec.get('shell', 'cmd')
    display = spec.get('cwd_display', r'C:\Users\you\demo')
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='hc-term-'))
    work = tmp / pathlib.PureWindowsPath(display).name
    work.mkdir()
    env = {**os.environ, **DEMO_ENV}
    if spec.get('git_config', 'neutral') != 'machine':
        # a neutral git: no system or global config, so the output is what a fresh install prints on any machine
        # (this machine's system gitconfig sets init.defaultBranch, which hides the 11-line `hint:` after git init,
        # and the global one holds a real name and email). "git_config": "machine" keeps this machine's config.
        empty = tmp / 'gitconfig-empty'
        empty.write_text('', encoding='utf-8')
        env.update({'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': str(empty)})
    env.update(spec.get('env', {}))
    home = str(pathlib.Path.home())
    # what the output shows instead of the real paths: the throw-away folder -> cwd_display, the home folder -> C:\Users\you
    subs = []
    for real in {str(work), str(work.resolve())}:
        subs += [(real, display), (real.replace('\\', '/'), display.replace('\\', '/'))]
        drive_less = real.replace('\\', '/')
        if re.match(r'^[A-Za-z]:/', drive_less):
            subs.append(('/' + drive_less[0].lower() + drive_less[2:], '/' + display[0].lower() + display[2:].replace('\\', '/')))
    subs += [(home, r'C:\Users\you'), (home.replace('\\', '/'), 'C:/Users/you')]
    subs.sort(key=lambda s: -len(s[0]))

    def clean(s):
        s = ANSI.sub('', s).rstrip('\r\n')
        if '\r' in s:
            s = s.split('\r')[-1]
        for a, b in subs:
            s = re.sub(re.escape(a), b.replace('\\', '\\\\'), s, flags=re.I)
        return clean_names(s).expandtabs(4)

    cwd, rel = work, pathlib.PureWindowsPath(display)
    commands = []
    try:
        for cmd in spec['commands']:
            if ENV_DUMPS.search(cmd) and not spec.get('allow_env'):
                raise SystemExit(f'capture.py refused {cmd!r}: it prints environment variables, which hold keys and tokens')
            refuse_if(cmd, f'the command {cmd!r}')
            prompt = spec.get('prompt') or default_prompt(shell, str(rel))
            m = re.match(r'^\s*cd(?:\s+/d)?\s+(.+?)\s*$', cmd, re.I)
            if m:
                dest = (cwd / m.group(1).strip('"\'')).resolve()
                if not str(dest).lower().startswith(str(work.resolve()).lower()):
                    raise SystemExit(f'capture.py refused {cmd!r}: a terminal capture stays inside its throw-away folder')
                if not dest.is_dir():
                    raise SystemExit(f'{cmd!r}: no such folder in the capture folder')
                cwd = dest
                rel = pathlib.PureWindowsPath(display) / dest.relative_to(work.resolve())
                commands.append({'cmd': cmd, 'prompt': prompt, 'exit': 0, 'dur': 0.0, 'out': []})
                continue
            lines, lock = [], threading.Lock()
            t_start = time.perf_counter()
            proc = subprocess.Popen(shell_argv(shell, cmd), cwd=str(cwd), env=env, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            def pump(stream, name):
                for raw in iter(stream.readline, b''):
                    with lock:
                        lines.append((time.perf_counter() - t_start, clean(decode(raw)), name))
                stream.close()
            th = [threading.Thread(target=pump, args=(proc.stdout, 'out')), threading.Thread(target=pump, args=(proc.stderr, 'err'))]
            for x in th:
                x.start()
            try:
                code = proc.wait(timeout=spec.get('timeout', 60))
            except subprocess.TimeoutExpired:
                proc.kill()
                raise SystemExit(f'{cmd!r} ran longer than {spec.get("timeout", 60)} s')
            for x in th:
                x.join()
            dur = time.perf_counter() - t_start
            lines.sort(key=lambda r: r[0])
            text = '\n'.join(s for _, s, _ in lines)
            refuse_if(text, f'the output of {cmd!r}')
            commands.append({'cmd': cmd, 'prompt': prompt, 'exit': code, 'dur': r3(dur),
                             'out': [[r3(t), s, n] for t, s, n in lines]})
            print(f'  {prompt}{cmd}  ({dur:.2f} s, exit {code}, {len(lines)} lines)')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    data = {'version': VERSION, 'kind': 'terminal', 'recorded': today(), 'tool': 'tools/capture.py terminal',
            'shell': shell, 'cwd_display': display, 'commands': commands}
    write_json(out / 'events.json', data)
    print(f'wrote {out / "events.json"} ({len(commands)} commands)')


# ------------------------------------------------------------------ desktop
def desktop_events(samples, t0, scale, vdur):
    """the 30 Hz log [(wall time, x, y, buttons)] (x, y relative to the recorded region) -> events on the video's
    clock: one move (with its path) per stretch of motion, a click per left / right press, a drag when the pointer
    moved more than 6 px while the left button was down"""
    pts = [(r3(t - t0), r2(px * scale), r2(py * scale), b) for t, px, py, b in samples if 0 <= t - t0 <= vdur]
    events, path, prev_b, down = [], [], 0, None
    for i, (t, px, py, b) in enumerate(pts):
        moved = i and (px, py) != pts[i - 1][1:3]
        if moved:
            if not path:
                path.append(list(pts[i - 1][:3]))
            path.append([t, px, py])
        elif path:
            events.append({'t': path[0][0], 't1': path[-1][0], 'kind': 'move', 'x': path[-1][1], 'y': path[-1][2], 'path': path})
            path = []
        if b & 1 and not prev_b & 1:
            down = (t, px, py)
        if prev_b & 1 and not b & 1 and down:
            dragged = math.hypot(px - down[1], py - down[2]) > 6
            events.append({'t': down[0], 'kind': 'drag' if dragged else 'click', 'x': down[1], 'y': down[2],
                           **({'t1': t, 'x1': px, 'y1': py} if dragged else {}), 'button': 'left'})
            down = None
        if b & 2 and not prev_b & 2:
            events.append({'t': t, 'kind': 'click', 'x': px, 'y': py, 'button': 'right'})
        prev_b = b
    if path:
        events.append({'t': path[0][0], 't1': path[-1][0], 'kind': 'move', 'x': path[-1][1], 'y': path[-1][2], 'path': path})
    events.sort(key=lambda e: e['t'])
    return events


def _user32():
    import ctypes
    return ctypes, ctypes.windll.user32


def find_window(part):
    """(hwnd, title) of the first visible top-level window whose title contains `part` (case-insensitive)"""
    ctypes, u = _user32()
    from ctypes import wintypes
    hits = []
    proto = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    def each(h, _):
        if u.IsWindowVisible(h):
            n = u.GetWindowTextLengthW(h)
            if n:
                buf = ctypes.create_unicode_buffer(n + 1)
                u.GetWindowTextW(h, buf, n + 1)
                if part.lower() in buf.value.lower():
                    hits.append((h, buf.value))
        return True
    u.EnumWindows(proto(each), 0)
    if not hits:
        raise SystemExit(f'no visible window with "{part}" in its title')
    return hits[0]


def bring_to_front(hwnd):
    ctypes, u = _user32()
    # no injected keys or clicks: if Windows refuses the focus change, covering() catches it and nothing is recorded
    u.ShowWindow(hwnd, 9)                 # SW_RESTORE
    u.SetForegroundWindow(hwnd)
    u.BringWindowToTop(hwnd)
    time.sleep(0.6)


def window_bounds(hwnd):
    """the window's visible frame (DWM extended frame bounds, physical pixels): x, y, w, h"""
    ctypes, u = _user32()
    from ctypes import wintypes
    r = wintypes.RECT()
    ctypes.windll.dwmapi.DwmGetWindowAttribute(wintypes.HWND(hwnd), 9, ctypes.byref(r), ctypes.sizeof(r))
    return r.left, r.top, r.right - r.left, r.bottom - r.top


def covering(hwnd, rect):
    """the title of a window on top of part of `rect` (sampled on a 5x5 grid), or None when hwnd is what shows there"""
    ctypes, u = _user32()
    from ctypes import wintypes
    u.WindowFromPoint.argtypes = [wintypes.POINT]
    u.WindowFromPoint.restype = wintypes.HWND
    u.GetAncestor.argtypes = [wintypes.HWND, ctypes.c_uint]
    u.GetAncestor.restype = wintypes.HWND
    x, y, w, h = rect
    for i in range(5):
        for j in range(5):
            pt = wintypes.POINT(int(x + w * (0.04 + 0.23 * i)), int(y + h * (0.04 + 0.23 * j)))
            top = u.GetAncestor(u.WindowFromPoint(pt), 2)          # GA_ROOT
            if top and top != hwnd:
                n = u.GetWindowTextLengthW(top)
                buf = ctypes.create_unicode_buffer(n + 1)
                u.GetWindowTextW(top, buf, n + 1)
                return buf.value or 'another window'
    return None


def capture_desktop(spec, out):
    import ctypes
    from ctypes import wintypes
    user32 = ctypes.windll.user32
    try:
        user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))      # per-monitor v2: physical pixels, like gdigrab
    except Exception:
        user32.SetProcessDPIAware()
    fps, seconds = int(spec.get('fps', 30)), float(spec['seconds'])
    hwnd = None
    if spec.get('window'):
        hwnd, full = find_window(spec['window'])
        bring_to_front(hwnd)
        x, y, w, h = window_bounds(hwnd)
        print(f'recording "{full}" at {x},{y} {w}x{h}')
    else:
        x, y, w, h = (int(v) for v in str(spec['region']).split(','))
        print('recording a screen region: everything visible in it is recorded, so clear it of anything private first')
    w, h = w - w % 2, h - h % 2
    for n in range(int(spec.get('countdown', 3)), 0, -1):
        print(f'recording in {n}...', flush=True)
        time.sleep(1)
    if hwnd:
        who = covering(hwnd, (x, y, w, h))
        if who:
            raise SystemExit(f'capture.py refused: "{who}" covers part of the window, and the recording would show it. '
                             f'Bring the window to the front (or close what covers it) and run again.')
    samples, stop, covered = [], threading.Event(), []

    def log():
        pt = wintypes.POINT()
        nxt = time.time()
        k = 0
        while not stop.is_set():
            k += 1
            if hwnd and k % 15 == 0 and not covered:     # twice a second: is anything else on top of the window now?
                who = covering(hwnd, (x, y, w, h))
                if who:
                    covered.append(who)
            user32.GetCursorPos(ctypes.byref(pt))
            btn = (1 if user32.GetAsyncKeyState(0x01) & 0x8000 else 0) | (2 if user32.GetAsyncKeyState(0x02) & 0x8000 else 0)
            samples.append((time.time(), pt.x - x, pt.y - y, btn))
            nxt += 1 / 30
            time.sleep(max(0.0, nxt - time.time()))
    th = threading.Thread(target=log, daemon=True)
    th.start()
    raw = pathlib.Path(tempfile.mkdtemp(prefix='hc-desk-')) / 'raw.mkv'
    mouse = '0' if spec.get('no_mouse') else '1'
    try:
        r = subprocess.run([mu.ffmpeg(), '-hide_banner', '-y', '-f', 'gdigrab', '-framerate', str(fps), '-draw_mouse', mouse,
                            '-offset_x', str(x), '-offset_y', str(y), '-video_size', f'{w}x{h}', '-i', 'desktop',
                            '-t', str(seconds), '-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast', str(raw)],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        stop.set()
        th.join()
        if r.returncode:
            raise SystemExit(f'ffmpeg gdigrab failed:\n{r.stderr[-1500:]}')
        if covered:
            raise SystemExit(f'capture.py discarded the recording: "{covered[0]}" came in front of the window while it '
                             f'was recording, so the video would show it. Run again with the window on top.')
        m = re.search(r'start: ([\d.]+)', r.stderr)
        t0 = float(m.group(1)) if m else samples[0][0]       # gdigrab stamps frames with the wall clock
        width = spec.get('width')
        scale = (width / w) if width else 1.0
        boxes = [rr for rr in spec.get('redact', []) if rr.get('box')]
        src = raw
        if boxes:
            src = raw.with_name('redacted.mkv')
            graph = f'[0:v]split={len(boxes) + 1}[b0]' + ''.join(f'[c{i}]' for i in range(len(boxes)))
            for i, rr in enumerate(boxes):
                bx, by, bw, bh = (int(v) for v in rr['box'])
                a, b = rr.get('from', 0), rr.get('to', 1e9)
                graph += f';[c{i}]crop={bw}:{bh}:{bx}:{by},boxblur=24:3[k{i}];[b{i}][k{i}]overlay={bx}:{by}:enable=\'between(t,{a},{b})\'[b{i + 1}]'
            mu.run([mu.ffmpeg(), '-v', 'error', '-y', '-i', str(raw), '-filter_complex', graph, '-map', f'[b{len(boxes)}]',
                    '-c:v', 'libx264rgb', '-crf', '0', '-preset', 'ultrafast', str(src)])
        problems = mu.encode(src, out / 'video.mp4', fps=fps, width=width, crf=spec.get('crf', 20))
        if problems:
            raise SystemExit(f'video.mp4 breaks the clip spec: {problems}')
    finally:
        stop.set()
        shutil.rmtree(raw.parent, ignore_errors=True)
    W, H = round(w * scale / 2) * 2, round(h * scale / 2) * 2
    vdur = float(mu.probe(out / 'video.mp4')['format'].get('duration') or seconds)
    events = desktop_events(samples, t0, scale, vdur)
    # clicks outside the recorded area are someone acting elsewhere on the screen: not part of this recording
    events = [e for e in events if e['kind'] == 'move' or (0 <= e['x'] <= w * scale and 0 <= e['y'] <= h * scale)]
    pts = [(r3(t - t0), r2(px * scale), r2(py * scale), b) for t, px, py, b in samples if 0 <= t - t0 <= vdur]
    data = {'version': VERSION, 'kind': 'desktop', 'recorded': today(), 'tool': 'tools/capture.py desktop',
            'video': 'video.mp4', 'size': [W, H], 'fps': fps, 'duration': r3(vdur),
            'cursorInVideo': mouse == '1', 'start': {'x': pts[0][1], 'y': pts[0][2]} if pts else {'x': W / 2, 'y': H / 2},
            'events': events, 'redact': spec.get('redact', [])}
    write_json(out / 'events.json', data)
    print(f'wrote {out / "video.mp4"} ({(out / "video.mp4").stat().st_size / 1e6:.2f} MB, {W}x{H}, {vdur:.1f} s), '
          f'{len(events)} events ({sum(e["kind"] == "click" for e in events)} clicks)')


# ------------------------------------------------------------------ check / show
def check_capture(d):
    problems = []
    ev = d / 'events.json'
    if not ev.exists():
        return ['no events.json']
    data = json.loads(ev.read_text(encoding='utf-8'))
    if not (d / 'steps.json').exists():
        problems.append('no steps.json (the capture cannot be re-recorded from the repo)')
    if data.get('video'):
        v = d / data['video']
        if not v.exists():
            problems.append(f'missing {data["video"]}')
        else:
            problems += [f'video: {p}' for p in mu.check(v)]
    for s in data.get('shots', []):
        if not (d / s['file']).exists():
            problems.append(f'missing {s["file"]}')
    for f in d.rglob('*'):
        if f.is_file() and f.stat().st_size > PAGES_LIMIT:
            problems.append(f'{f.name} is {f.stat().st_size / 1e6:.1f} MB (Cloudflare Pages: 25 MB per file)')
    def strings(v):
        if isinstance(v, str):
            yield v
        elif isinstance(v, dict):
            for x in v.values():
                yield from strings(x)
        elif isinstance(v, list):
            for x in v:
                yield from strings(x)
    problems += [f'events.json contains {why}' for why in scan('\n'.join(strings(data)))]
    return problems


def show(d):
    data = json.loads((d / 'events.json').read_text(encoding='utf-8'))
    print(f'{d.name}: {data["kind"]} capture, recorded {data.get("recorded")}')
    if data['kind'] == 'terminal':
        for c in data['commands']:
            print(f'  {c["prompt"]}{c["cmd"]}   ({c["dur"]} s, exit {c["exit"]})')
            for t, s, n in c['out']:
                print(f'      +{t:6.3f} {"!" if n == "err" else " "} {s}')
        return
    print(f'  {data["size"][0]}x{data["size"][1]}, {data["duration"]} s')
    for e in data['events']:
        bits = [f'{e["t"]:6.2f}', f'{e["kind"]:6}']
        if 't1' in e:
            bits.append(f'..{e["t1"]:.2f}')
        if 'x' in e:
            bits.append(f'at {e["x"]:.0f},{e["y"]:.0f}')
        for k in ('text', 'key', 'url', 'target', 'name', 'dy'):
            if e.get(k) is not None:
                bits.append(f'{k}={e[k]!r}')
        if e.get('side'):
            bits.append('(side page, taken after the recording; not in the video)')
        print('  ' + ' '.join(bits))
        boxes = e.get('boxes') or {}
        if e['kind'] == 'shot':
            boxes = next((sh.get('boxes') or {} for sh in data.get('shots', []) if sh['name'] == e.get('name')), {})
        for k, b in boxes.items():
            print(f'           box {k}: ' + (', '.join(f'{v:.0f}' for v in b) if b else 'not found'))


# ------------------------------------------------------------------ main
def run_spec(spec, out, headed=False):
    """record into a sibling folder <name>.new, check it, and only then swap it in for the old capture: a failed or
    refused re-record (a flaky network, a renamed selector, a secret on screen) leaves the old capture untouched, so
    the lesson never loses its clip and nothing half-written is ever committed. Returns the problems (empty = OK)."""
    mode = spec.get('mode')
    if mode not in ('browser', 'terminal', 'desktop'):
        raise SystemExit(f'steps.json mode {mode!r}: browser, terminal or desktop')
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp, old = out.with_name(out.name + '.new'), out.with_name(out.name + '.old')
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir()
    kept = 'the old capture is untouched' if (out / 'events.json').exists() else 'nothing was written'
    try:
        write_json(tmp / 'steps.json', spec)
        if mode == 'browser':
            capture_browser(spec, tmp, headed)
        elif mode == 'terminal':
            capture_terminal(spec, tmp)
        else:
            capture_desktop(spec, tmp)
        bad = check_capture(tmp)
    except (StepFailed, SystemExit, Exception) as e:
        shutil.rmtree(tmp, ignore_errors=True)
        why = str(e).strip() or type(e).__name__
        if not isinstance(e, (StepFailed, SystemExit)):
            why = f'{type(e).__name__}: {why.splitlines()[0]}'
        print(f'capture.py: recording {out.name} failed at {why}' if isinstance(e, StepFailed)
              else f'capture.py: recording {out.name} failed: {why}')
        print(f'  ({kept})')
        return [why]
    if bad:
        shutil.rmtree(tmp, ignore_errors=True)
        print(f'check: PROBLEMS: {"; ".join(bad)}')
        print(f'  the new recording was thrown away ({kept})')
        return bad
    shutil.rmtree(old, ignore_errors=True)
    if out.exists():
        out.rename(old)
    try:
        tmp.rename(out)
    except OSError as e:
        if old.exists() and not out.exists():
            old.rename(out)
        print(f'capture.py: could not swap the new recording in ({e}); {kept}; the new one is in {tmp}')
        return [str(e)]
    shutil.rmtree(old, ignore_errors=True)
    print('check: OK')
    return []


def lesson_steps(lesson, name):
    """the recipe kept in the lesson, lessons/<slug>/steps/<name>.json (the one people edit), or None"""
    p = lesson_dir(lesson) / 'steps' / f'{name}.json'
    return p if p.exists() else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    for m in ('browser', 'terminal'):
        s = sub.add_parser(m)
        s.add_argument('lesson'); s.add_argument('name')
        s.add_argument('--steps', help='the recipe (default: lessons/<lesson>/steps/<name>.json)')
        if m == 'browser':
            s.add_argument('--headed', action='store_true', help='show the browser window while recording')
    d = sub.add_parser('desktop')
    d.add_argument('lesson'); d.add_argument('name')
    d.add_argument('--seconds', type=float); d.add_argument('--window'); d.add_argument('--region')
    d.add_argument('--fps', type=int, default=30); d.add_argument('--width', type=int)
    d.add_argument('--no-mouse', action='store_true', help='leave the OS pointer out of the video (K.demo draws its own)')
    d.add_argument('--countdown', type=int, default=3); d.add_argument('--steps', help='a desktop steps.json (redact boxes)')
    ag = sub.add_parser('again'); ag.add_argument('lesson'); ag.add_argument('name'); ag.add_argument('--headed', action='store_true')
    ck = sub.add_parser('check'); ck.add_argument('lesson'); ck.add_argument('name', nargs='?')
    sh = sub.add_parser('show'); sh.add_argument('lesson'); sh.add_argument('name')
    a = ap.parse_args()

    if a.cmd in ('browser', 'terminal'):
        src = pathlib.Path(a.steps) if a.steps else lesson_steps(a.lesson, a.name)
        if not src:
            raise SystemExit(f'no --steps and no lessons/{a.lesson}/steps/{a.name}.json')
        spec = json.loads(src.read_text(encoding='utf-8'))
        if spec.get('mode') not in (None, a.cmd):
            raise SystemExit(f'{src} is a {spec["mode"]} recipe, not {a.cmd}')
        spec['mode'] = a.cmd
        sys.exit(1 if run_spec(spec, cap_dir(a.lesson, a.name), getattr(a, 'headed', False)) else 0)
    if a.cmd == 'desktop':
        spec = json.loads(pathlib.Path(a.steps).read_text(encoding='utf-8')) if a.steps else {}
        spec['mode'] = 'desktop'
        for k in ('seconds', 'window', 'region', 'fps', 'width', 'countdown'):
            if getattr(a, k) is not None:
                spec[k] = getattr(a, k)
        if a.no_mouse:
            spec['no_mouse'] = True
        if not spec.get('seconds') or not (spec.get('window') or spec.get('region')):
            raise SystemExit('desktop: give --seconds and --window "title" or --region x,y,w,h')
        sys.exit(1 if run_spec(spec, cap_dir(a.lesson, a.name)) else 0)
    if a.cmd == 'again':
        out = cap_dir(a.lesson, a.name)
        kept = out / 'steps.json'
        src = lesson_steps(a.lesson, a.name)
        if src:
            # the lesson's recipe is the one people edit; the capture's copy only records what was last recorded
            spec = json.loads(src.read_text(encoding='utf-8'))
            if kept.exists():
                prev = json.loads(kept.read_text(encoding='utf-8'))
                if {k: v for k, v in prev.items() if k != 'mode'} != {k: v for k, v in spec.items() if k != 'mode'}:
                    print(f'note: {src.relative_to(lesson_dir(a.lesson).parent.parent)} differs from the recipe this capture '
                          'was recorded from; re-recording from the lesson recipe')
            spec.setdefault('mode', json.loads(kept.read_text(encoding='utf-8')).get('mode') if kept.exists() else None)
        elif kept.exists():
            spec = json.loads(kept.read_text(encoding='utf-8'))
        else:
            raise SystemExit(f'nothing to re-record: no lessons/{a.lesson}/steps/{a.name}.json and no {kept}')
        sys.exit(1 if run_spec(spec, out, a.headed) else 0)
    if a.cmd == 'check':
        root = lesson_dir(a.lesson) / 'assets' / 'capture'
        dirs = [root / a.name] if a.name else sorted(p for p in root.iterdir() if p.is_dir() and '.' not in p.name) if root.is_dir() else []
        bad = 0
        for d in dirs:
            pr = check_capture(d)
            bad += bool(pr)
            print(f'{d.name}: ' + ('OK' if not pr else 'PROBLEMS: ' + '; '.join(pr)))
        # a recording killed mid-way leaves <name>.new (or .old after a failed swap): never commit or publish one
        for d in sorted(root.glob('*.new')) + sorted(root.glob('*.old')) if root.is_dir() and not a.name else []:
            bad += 1
            print(f'{d.name}: PROBLEMS: a leftover folder from an interrupted recording; delete it')
        sys.exit(1 if bad else 0)
    if a.cmd == 'show':
        show(cap_dir(a.lesson, a.name))


if __name__ == '__main__':
    main()
