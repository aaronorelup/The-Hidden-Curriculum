"""publish.py: put a lesson on aaronorelup.com/courses/the-hidden-curriculum/ and verify it is live.

usage:
  python tools/publish.py <lesson-slug>            stage, commit, push, verify
  python tools/publish.py --all                    re-stage every published lesson (after an engine/template change)
  python tools/publish.py --data-only              rebuild only the course data the site's course page reads
  python tools/publish.py ... --into <checkout>    stage into another blog checkout; no git, no push
  python tools/publish.py ... --no-push / --no-verify

What lands in the blog repo (and nothing else, ever):
  public/courses/the-hidden-curriculum/engine/          the shared player engine + painted plate
  public/courses/the-hidden-curriculum/lessons/<slug>/  each lesson: page, scripts, cues, mixed audio,
                                                       captions, MP4 (720p copy when 1080p is over 25 MB), poster
  src/data/courses/the-hidden-curriculum.json          course data: modules, lessons, which are published,
                                                       durations, the course map; the Astro course page and
                                                       the /courses list are built from it

The blog's own checkout is never touched (other sessions keep uncommitted work there): publishing uses
a dedicated git worktree at <course>/.publish/blog, reset to origin/main on every run.
Lesson pages are re-rendered from engine/lesson-template.html on every stage, so a template change
reaches every lesson with --all.
"""
import argparse
import datetime
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import ENGINE, LESSONS, ROOT, ffmpeg, lesson_dir, sync_scenes  # noqa: E402

BLOG = pathlib.Path(r'C:\Users\soulo\Organized\Personal\My Projects\My Blog\blog')
WT = ROOT / '.publish' / 'blog'
SITE = 'https://aaronorelup.com'
COURSE_SLUG = 'the-hidden-curriculum'
COURSE_TITLE = 'The Hidden Curriculum'
SITE_DIR = f'public/courses/{COURSE_SLUG}'
DATA_FILE = f'src/data/courses/{COURSE_SLUG}.json'
LIMIT = 24 * 1024 * 1024
ENGINE_FILES = ['kit.js', 'map.js', 'runtime.js', 'music.js', 'player.js', 'player.css']
REGISTRY = ROOT / 'course.json'
TRAILER = 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'

# The course map (Start, six districts, Finish) and the lantern (AI) lessons are read from curriculum.md's
# `# Start/District N/Finish · Name — question` headings and its `Lantern lessons:` line; engine/map.js mirrors them.


def git(*args, cwd=WT, check=True):
    r = subprocess.run(['git', *args], cwd=str(cwd), capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f'git {" ".join(args)} failed:\n{r.stdout}\n{r.stderr}')
    return r


def fresh_worktree():
    if not (WT / '.git').exists():
        WT.parent.mkdir(parents=True, exist_ok=True)
        git('fetch', 'origin', cwd=BLOG)
        git('worktree', 'add', '--detach', str(WT), 'origin/main', cwd=BLOG)
    git('fetch', 'origin')
    git('checkout', '--detach', '--force', 'origin/main')
    git('reset', '--hard', 'origin/main')
    git('clean', '-fdq', '--', SITE_DIR)


def registry():
    return json.loads(REGISTRY.read_text(encoding='utf-8')) if REGISTRY.exists() else {'lessons': {}}


def lesson_meta(L: pathlib.Path) -> dict:
    """id/title/module/summary/keep/poc out of lesson.js, without running it"""
    src = (L / 'lesson.js').read_text(encoding='utf-8')

    def grab(key):
        m = re.search(rf"\b{key}\s*:\s*(['\"])(.*?)(?<!\\)\1", src, re.S)
        return m.group(2).replace("\\'", "'") if m else ''
    cues = json.loads((L / 'cues.json').read_text(encoding='utf-8')) if (L / 'cues.json').exists() else {}
    voice = json.loads((L / 'voice.json').read_text(encoding='utf-8')) if (L / 'voice.json').exists() else {}
    return {'id': grab('id'), 'title': grab('title'), 'module': grab('module'), 'summary': grab('summary'),
            'poc': bool(re.search(r'\bpoc\s*:\s*true', src)), 'duration': cues.get('duration'),
            'narrator': re.split(r'\s[-–—]\s', voice.get('name', ''))[0] or None}


def render_page(L: pathlib.Path, meta: dict, prev_next=('', '')) -> str:
    page = (ENGINE / 'lesson-template.html').read_text(encoding='utf-8')
    return (page.replace('{{SLUG}}', L.name).replace('{{ID}}', html.escape(meta['id'])).replace('{{TITLE}}', html.escape(meta['title']))
                .replace('{{SUMMARY}}', html.escape(meta['summary'])).replace('{{DATE}}', meta.get('published') or datetime.date.today().isoformat())
                .replace('{{PREV}}', prev_next[0]).replace('{{NEXT}}', prev_next[1]))


def copy_lesson(L: pathlib.Path, dest: pathlib.Path, meta: dict, prev_next):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    sync_scenes(L)
    (dest / 'index.html').write_text(render_page(L, meta, prev_next), encoding='utf-8')
    for name in ['lesson.js', 'cues.js', 'scenes.js', 'captions.vtt']:
        if (L / name).exists():
            shutil.copy2(L / name, dest / name)
    for sub in ['scenes', 'assets']:
        if (L / sub).is_dir() and any((L / sub).iterdir()):
            shutil.copytree(L / sub, dest / sub)
    (dest / 'audio').mkdir()
    shutil.copy2(L / 'audio' / 'mix.mp3', dest / 'audio' / 'mix.mp3')
    mp4, web = L / 'out' / 'lesson.mp4', L / 'out' / 'lesson-720.mp4'
    chosen = mp4 if mp4.exists() and mp4.stat().st_size <= LIMIT else web if web.exists() else None
    if chosen:
        shutil.copy2(chosen, dest / 'lesson.mp4')
        # poster: the title card once it has fully built (end of section 01), never mid-animation
        cues = json.loads((L / 'cues.json').read_text(encoding='utf-8')) if (L / 'cues.json').exists() else {}
        secs = cues.get('sections') or []
        at = max(3.0, secs[0]['end'] - 0.4) if secs else 6.0
        subprocess.run([ffmpeg(), '-v', 'error', '-y', '-ss', f'{at:.2f}', '-i', str(chosen), '-frames:v', '1', '-vf', 'scale=1280:-2',
                        '-q:v', '3', str(dest / 'poster.jpg')], check=False)
    elif mp4.exists():
        print('note: MP4 exceeds the Pages limit and no 720p copy exists; publishing the interactive page only')
    big = [p for p in dest.rglob('*') if p.is_file() and p.stat().st_size > LIMIT]
    if big:
        raise SystemExit(f'files over the Pages limit: {big}')


def parse_curriculum():
    """modules (with lessons) in file order, each tagged with the map region it sits in"""
    text = (ROOT / 'curriculum.md').read_text(encoding='utf-8')
    modules, cur, region = [], None, None
    for line in text.splitlines():
        m = re.match(r'^# (Start|Finish|District (\d+)) · (.+?) — (.+)$', line)
        if m:
            region = m.group(3).strip()
            continue
        m = re.match(r'^## Module (\d+) — (.*)$', line)
        if m:
            cur = {'n': m.group(1), 'name': m.group(2), 'region': region, 'lessons': []}
            modules.append(cur)
            continue
        m = re.match(r'^\|\s*(\d{2}\.\d{2}[a-z]?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\w+)\s*\|$', line)
        if m and cur:
            cur['lessons'].append({'id': m.group(1), 'title': m.group(2), 'idea': m.group(3)})
    return modules


def parse_map():
    """the map's regions in order: {kind: start|district|finish, n, id, name, q, mods}, plus the lantern lesson ids"""
    text = (ROOT / 'curriculum.md').read_text(encoding='utf-8')
    regions, cur = [], None
    for line in text.splitlines():
        m = re.match(r'^# (Start|Finish|District (\d+)) · (.+?) — (.+)$', line)
        if m:
            kind = 'district' if m.group(2) else m.group(1).lower()
            name = m.group(3).strip()
            cur = {'kind': kind, 'n': int(m.group(2)) if m.group(2) else None,
                   'id': re.sub(r'[^a-z]+', '-', re.sub(r'^the ', '', name.lower())).strip('-'),
                   'name': name, 'q': m.group(4).strip(), 'mods': []}
            regions.append(cur)
            continue
        m = re.match(r'^## Module (\d+) — ', line)
        if m and cur:
            cur['mods'].append(m.group(1))
    lm = re.search(r'^Lantern lessons:\s*(.*)$', text, re.M)
    lanterns = set(re.findall(r'\d{2}\.\d{2}', lm.group(1))) if lm else set()
    return regions, lanterns


def course_data(reg) -> dict:
    """everything the site's course page needs, as plain data"""
    published = {m['id']: (slug, m) for slug, m in reg['lessons'].items() if not m.get('poc')}
    modules, total, filed, runtime = [], 0, 0, 0.0
    plain = lambda s: re.sub(r'`([^`]*)`', r'\1', s)
    regions, lanterns = parse_map()
    ids = {les['id'] for mod in parse_curriculum() for les in mod['lessons']}
    for x in sorted(lanterns - ids):
        print(f'warning: lantern lesson {x} is not in curriculum.md')
    for mod in parse_curriculum():
        lessons = []
        for les in mod['lessons']:
            total += 1
            hit = published.get(les['id'])
            row = {'id': les['id'], 'title': plain(les['title']), 'idea': plain(les['idea'])}
            if les['id'] in lanterns:
                row['lantern'] = True
            if hit:
                slug, m = hit
                filed += 1
                runtime += m.get('duration') or 0
                row.update({'status': 'published', 'slug': slug, 'url': f'/courses/{COURSE_SLUG}/lessons/{slug}/',
                            'duration': round(m.get('duration') or 0, 1), 'summary': m.get('summary', ''),
                            'published': m.get('published'), 'narrator': m.get('narrator'),
                            'poster': f'/courses/{COURSE_SLUG}/lessons/{slug}/poster.jpg' if m.get('mp4') else None})
            else:
                row['status'] = 'locked'
            lessons.append(row)
        name = mod['name']
        short = name.split(':')[0].strip()
        modules.append({'n': mod['n'], 'name': name, 'short': short, 'region': mod['region'], 'lessons': lessons,
                        'filed': sum(1 for x in lessons if x['status'] == 'published')})
    latest = max((m for _, m in published.values()), key=lambda m: (m.get('published') or '', m['id']), default=None)
    latest_row = next((x for mod in modules for x in mod['lessons'] if latest and x['id'] == latest['id']), None)
    first = next((x for mod in modules for x in mod['lessons'] if x['status'] == 'published'), None)
    return {
        'slug': COURSE_SLUG, 'title': COURSE_TITLE, 'updated': datetime.date.today().isoformat(),
        'totalLessons': total, 'publishedLessons': filed, 'runtimeSeconds': round(runtime),
        'moduleCount': len(modules), 'districtCount': sum(1 for r in regions if r['kind'] == 'district'),
        'regions': regions, 'lanternCount': len(lanterns & ids), 'modules': modules,
        'latest': latest_row, 'first': first,
    }


def foot_links(order, pub, lesson_id):
    """(left, right) footer links of a lesson page: back to the whole curriculum, and on to the next
    lesson in course order (a link when it is out; its title marked 'not released yet' while it is locked)"""
    ids = [x['id'] for x in order]
    left = f'<a href="../../#curriculum">← All {len(ids)} lessons</a>'
    i = ids.index(lesson_id) if lesson_id in ids else -1
    if i < 0 or i + 1 >= len(ids):
        return left, ''
    nxt = order[i + 1]
    if nxt['id'] in pub:
        return left, f'<a href="../{pub[nxt["id"]]}/">Next: {html.escape(nxt["id"])} {html.escape(nxt["title"])} →</a>'
    return left, f'<a href="../../#module-{nxt["id"].split(".")[0]}">Next: {html.escape(nxt["id"])} {html.escape(nxt["title"])} <span class="soon">(not released yet)</span></a>'


def stage(repo: pathlib.Path, slugs, reg):
    """copy engine + the given lessons into a blog checkout and write the course data file"""
    site = repo / SITE_DIR
    (site / 'engine' / 'assets').mkdir(parents=True, exist_ok=True)
    for f in ENGINE_FILES:
        shutil.copy2(ENGINE / f, site / 'engine' / f)
    for f in (ENGINE / 'assets').glob('*.jpg'):
        shutil.copy2(f, site / 'engine' / 'assets' / f.name)
    order = [{**x, 'title': re.sub(r'`([^`]*)`', r'', x['title'])} for mod in parse_curriculum() for x in mod['lessons']]
    pub = {m['id']: s for s, m in reg['lessons'].items() if not m.get('poc')}
    meta_of = lambda slug: {**lesson_meta(LESSONS / slug), **{k: v for k, v in reg['lessons'].get(slug, {}).items() if k in ('published',)}}
    for slug in slugs:
        meta = meta_of(slug)
        copy_lesson(LESSONS / slug, site / 'lessons' / slug, meta, foot_links(order, pub, meta['id']))
    # the lesson before each newly staged one gets its "Next" link updated (page only, no media copy)
    ids = [x['id'] for x in order]
    for slug in slugs:
        lid = reg['lessons'].get(slug, {}).get('id')
        if lid not in ids:
            continue
        prev = next((pub[ids[j]] for j in range(ids.index(lid) - 1, -1, -1) if ids[j] in pub), None)
        if prev and prev not in slugs and (site / 'lessons' / prev).is_dir():
            m = meta_of(prev)
            (site / 'lessons' / prev / 'index.html').write_text(render_page(LESSONS / prev, m, foot_links(order, pub, m['id'])), encoding='utf-8')
    data = repo / DATA_FILE
    data.parent.mkdir(parents=True, exist_ok=True)
    data.write_text(json.dumps(course_data(reg), indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


def get(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'course-publisher', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read()
    except Exception:
        return 0, b''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson', nargs='?')
    ap.add_argument('--all', action='store_true', help='re-stage every published lesson')
    ap.add_argument('--data-only', action='store_true')
    ap.add_argument('--into', help='stage into this blog checkout instead of the publish worktree (no git)')
    ap.add_argument('--retire', metavar='OLD_SLUG', help='drop a previously registered lesson (e.g. a promoted proof of concept)')
    ap.add_argument('--no-push', action='store_true')
    ap.add_argument('--no-verify', action='store_true')
    a = ap.parse_args()
    reg = registry()
    slugs, msg = [], 'Courses: refresh course data'
    if a.lesson:
        L = lesson_dir(a.lesson)
        meta = lesson_meta(L)
        if not (L / 'audio' / 'mix.mp3').exists():
            raise SystemExit('no audio/mix.mp3: run narrate.py and mix.py first')
        old = reg['lessons'].get(L.name, {})
        meta['published'] = old.get('published') or datetime.date.today().isoformat()
        if a.retire and a.retire in reg['lessons']:
            meta['published'] = reg['lessons'][a.retire].get('published', meta['published'])
            meta['promoted'] = datetime.date.today().isoformat()
            reg['lessons'].pop(a.retire)
        meta['mp4'] = (L / 'out' / 'lesson.mp4').exists() or (L / 'out' / 'lesson-720.mp4').exists()
        reg['lessons'][L.name] = {**old, **meta}
        slugs = [L.name]
        msg = f"Courses: {'proof of concept ' if meta['poc'] else ''}{meta['id']} {meta['title']}"
    if a.all:
        slugs = sorted(reg['lessons'])
        for s in slugs:   # refresh what lesson.js / cues / voice say now; keep the dates
            keep = {k: reg['lessons'][s][k] for k in ('published', 'promoted') if k in reg['lessons'][s]}
            L = LESSONS / s
            reg['lessons'][s] = {**reg['lessons'][s], **lesson_meta(L), **keep,
                                 'mp4': (L / 'out' / 'lesson.mp4').exists() or (L / 'out' / 'lesson-720.mp4').exists()}
        msg = 'Courses: re-stage every lesson'
    if not slugs and not a.data_only and not a.all:
        raise SystemExit('name a lesson, or pass --all / --data-only')
    REGISTRY.write_text(json.dumps(reg, indent=1), encoding='utf-8')

    if a.into:
        stage(pathlib.Path(a.into), slugs, reg)
        print(f'staged {len(slugs)} lesson(s) + course data into {a.into} (no git)')
        return
    fresh_worktree()
    stage(WT, slugs, reg)
    git('add', SITE_DIR, DATA_FILE)
    if not git('status', '--porcelain', '--', SITE_DIR, DATA_FILE).stdout.strip():
        print('nothing changed on the site')
        return
    git('commit', '-q', '-m', f'{msg}\n\n{TRAILER}')
    if a.no_push:
        print('committed in the publish worktree; not pushed (--no-push)')
        return
    for attempt in range(3):
        r = git('push', 'origin', 'HEAD:main', check=False)
        if r.returncode == 0:
            break
        git('fetch', 'origin')
        git('rebase', 'origin/main')
    else:
        raise SystemExit('push failed three times:\n' + r.stderr)
    print(f'pushed {git("rev-parse", "--short", "HEAD").stdout.strip()}: {msg}')
    if a.no_verify:
        return
    # live = the course page (rebuilt by Astro on Cloudflare) links every staged lesson, and the files answer
    course_url = f'{SITE}/courses/{COURSE_SLUG}/'
    checks = []
    for slug in slugs:
        base = f'{course_url}lessons/{slug}/'
        checks += [base, base + 'audio/mix.mp3', base + 'lesson.js'] + ([base + 'lesson.mp4'] if reg['lessons'][slug].get('mp4') else [])
    deadline, ok = time.time() + 12 * 60, False
    while time.time() < deadline:
        status, body = get(f'{course_url}?v={int(time.time())}')
        if status == 200 and all(f'lessons/{s}/' in body.decode('utf-8', 'replace') for s in slugs):
            ok = True
            break
        time.sleep(20)
    print(('LIVE  ' if ok else 'NOT YET ') + course_url + ' (lists the lesson)')
    missing = [u for u in checks if get(u)[0] != 200]
    for u in checks:
        print(('LIVE  ' if u not in missing else 'MISSING ') + u)
    if not ok or missing:
        raise SystemExit('the site has not caught up after 12 minutes (did the Cloudflare build fail?)')


if __name__ == '__main__':
    main()
