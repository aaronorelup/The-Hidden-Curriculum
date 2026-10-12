"""publish.py: put a lesson on aaronorelup.com/courses/the-hidden-curriculum/ and verify it is live.

usage:
  python tools/publish.py <lesson>                 stage, commit, push, verify (a new lesson's key, or a legacy slug)
  python tools/publish.py --all                    re-stage every published lesson (after an engine/template change)
  python tools/publish.py --data-only              rebuild only the course data the site's course page reads
  python tools/publish.py --remove <key>           take a deleted / combined lesson off the site (its row gone from
                                                   curriculum.md, its key listed under ## Retired keys): git rm its
                                                   folder, drop it from course.json, refresh the data and every
                                                   page's Next link, verify the page answers 404
  python tools/publish.py ... --into <checkout>    stage into another blog checkout; no git, no push
  python tools/publish.py ... --no-push / --no-verify
  python tools/publish.py [<lesson>] --dry-run [--out data.json] [--curriculum <file>] [--registry <file>]
                                                   build the course data and the staged pages (no media) into a
                                                   temp folder: no git, no network, course.json untouched

The course order, the map and the lesson IDs come from curriculum.md through tools/course.py (the format with
lesson keys, and the older one). New lessons are matched by key (lessons/<key>/, registry entry <key>); the
lessons published before 2026-10-12 are legacy ("legacy": true in course.json): they stay listed and linked,
marked "legacy": true, in the module of the first slot they cover (curriculum.md's Legacy lessons table), and
their pages keep loading the frozen map (engine/legacy/map-v1.js) their videos were made with.

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

A new lesson's page loads ITS OWN copy of the course data (lessons/<key>/course.js on the site, written when the
lesson is staged), not the shared engine/course.js: after the curriculum changes, every lesson already on the site
keeps drawing the map its narration and MP4 were made with until it is re-narrated / re-rendered and republished.
Staging refuses a lesson that tools/course.py says still needs narration or a re-render (--all skips it and keeps
its current page; --allow-stale overrides). Restructuring: course.py remap --render, then one publish.py --all.

Before committing, the staged course data is checked against the blog's course page (src/pages/courses/
the-hidden-curriculum.astro, src/components/courses/LessonList.astro): a curriculum without six districts, a covered slot
("coveredBy") or a legacy row whose own ID differs from its slot's ("legacyId") needs the page to support it first.
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
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import ENGINE, LESSONS, MAPJS_LEGACY, MAPJS_NEW, MAPJS_OWN, ROOT, ffmpeg, lesson_dir, sync_scenes  # noqa: E402
import course as coursedata  # noqa: E402

BLOG = pathlib.Path(r'C:\Users\soulo\Organized\Personal\My Projects\My Blog\blog')
WT = ROOT / '.publish' / 'blog'
SITE = 'https://aaronorelup.com'
COURSE_SLUG = 'the-hidden-curriculum'
COURSE_TITLE = 'The Hidden Curriculum'
SITE_DIR = f'public/courses/{COURSE_SLUG}'
DATA_FILE = f'src/data/courses/{COURSE_SLUG}.json'
LIMIT = 24 * 1024 * 1024
ENGINE_FILES = ['kit.js', 'map.js', 'runtime.js', 'music.js', 'player.js', 'player.css']   # + course.js, legacy/*.js
REGISTRY = ROOT / 'course.json'
TRAILER = 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'

MEDIA = {'.mp3', '.mp4', '.wav', '.webm', '.mov', '.m4a'}
# set by main(): the parsed curriculum (tools/course.py) every function below reads
COURSE = None


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


def registry(path=None):
    path = pathlib.Path(path) if path else REGISTRY
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'lessons': {}}


def lesson_meta(L: pathlib.Path) -> dict:
    """id/title/module/summary/keep/poc out of lesson.js, without running it"""
    src = (L / 'lesson.js').read_text(encoding='utf-8')

    def grab(key):
        m = re.search(rf"\b{key}\s*:\s*(['\"])(.*?)(?<!\\)\1", src, re.S)
        return m.group(2).replace("\\'", "'") if m else ''
    cues = json.loads((L / 'cues.json').read_text(encoding='utf-8')) if (L / 'cues.json').exists() else {}
    voice = json.loads((L / 'voice.json').read_text(encoding='utf-8')) if (L / 'voice.json').exists() else {}
    out = {'id': grab('id'), 'title': grab('title'), 'module': grab('module'), 'summary': grab('summary'),
            'poc': bool(re.search(r'\bpoc\s*:\s*true', src)), 'duration': cues.get('duration'),
            'narrator': re.split(r'\s[-–—]\s', voice.get('name', ''))[0] or None}
    if grab('key'):
        out['key'] = grab('key')
    return out


def curriculum_lesson(slug, reg=None):
    """the curriculum.md row of a NEW lesson (by key), or None for legacy lessons, proofs of concept and tests"""
    if (reg or {}).get('lessons', {}).get(slug, {}).get('legacy'):
        return None
    return COURSE.lesson(slug) if COURSE and COURSE.format == 'new' and COURSE.lesson(slug) and COURSE.lesson(slug)['key'] == slug else None


def render_page(L: pathlib.Path, meta: dict, prev_next=('', ''), reg=None, own_data=True) -> str:
    """a lesson page from engine/lesson-template.html. {{MAPJS}}: legacy lessons load the frozen v1 map; a
    curriculum lesson its own course data snapshot (course.js in its folder, see copy_lesson) + engine/map.js
    (own_data=False: the shared engine/course.js, for a page staged before snapshots existed); anything else the
    shared engine/course.js. {{ID}}: a new lesson's ID from curriculum.md (lesson.js is kept in step by course.py
    sync); a legacy lesson keeps its own ID, the one its video's badge shows."""
    page = (ENGINE / 'lesson-template.html').read_text(encoding='utf-8')
    lid = meta['id']
    legacy = bool((reg or {}).get('lessons', {}).get(L.name, {}).get('legacy'))
    les = curriculum_lesson(L.name, reg)
    if les:
        lid = les['id']
    tag = MAPJS_LEGACY if legacy else MAPJS_OWN if les and own_data else MAPJS_NEW
    return (page.replace('{{SLUG}}', L.name).replace('{{ID}}', html.escape(lid)).replace('{{TITLE}}', html.escape(meta['title']))
                .replace('{{SUMMARY}}', html.escape(meta['summary'])).replace('{{DATE}}', meta.get('published') or datetime.date.today().isoformat())
                .replace('{{PREV}}', prev_next[0]).replace('{{NEXT}}', prev_next[1]).replace('{{MAPJS}}', tag))


def copy_lesson(L: pathlib.Path, dest: pathlib.Path, meta: dict, prev_next, reg=None, media=True):
    """media=False (dry run): the page, scripts and small files only; audio and video are listed, not copied.
    A curriculum lesson also gets course.js: the course data as it is now, i.e. what its narration and video were
    made with (stage() refuses a stale lesson), which its page draws the map from until it is republished."""
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    if media:
        sync_scenes(L)
    if curriculum_lesson(L.name, reg):
        data = coursedata.course_data(COURSE)
        (dest / 'course.js').write_text(coursedata.course_js_text(data, datetime.date.today().isoformat()), encoding='utf-8')
    (dest / 'index.html').write_text(render_page(L, meta, prev_next, reg), encoding='utf-8')
    for name in ['lesson.js', 'cues.js', 'scenes.js', 'captions.vtt']:
        if (L / name).exists():
            shutil.copy2(L / name, dest / name)
    for sub in ['scenes', 'assets']:
        if (L / sub).is_dir() and any((L / sub).iterdir()):
            if media:
                shutil.copytree(L / sub, dest / sub)
            else:
                shutil.copytree(L / sub, dest / sub, ignore=lambda d, names: [n for n in names if pathlib.Path(n).suffix.lower() in MEDIA])
    if not media:
        mp4, web = L / 'out' / 'lesson.mp4', L / 'out' / 'lesson-720.mp4'
        skipped = [x for x in (L / 'audio' / 'mix.mp3', mp4 if mp4.exists() and mp4.stat().st_size <= LIMIT else web) if x.exists()]
        (dest / 'MEDIA-NOT-COPIED.txt').write_text('dry run: would copy\n' + '\n'.join(str(x) for x in skipped) + '\n', encoding='utf-8')
        return
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


def regions_out(c):
    """the map's regions in order, as the site reads them: {kind, n, id, name, q, mods}"""
    return [{'kind': r['kind'], 'n': r['n'], 'id': r['id'], 'name': r['name'], 'q': r['q'], 'mods': list(r['mods'])} for r in c.regions]


def course_rows(reg):
    """every module's rows for the course page, in curriculum order, and the flat order of every row.

    Old format (no keys): published lessons are matched by ID, exactly as before 2026-10-12 (the 12 published
    lessons are the legacy ones, so they also get "legacy": true).
    New format: a slot whose new lesson is published (registry entry = its key) links to it; a slot with status
    `legacy` keeps its own row (its new title, locked) and the legacy lessons that cover it are listed right after
    it, once, at the first slot each covers (a slot whose legacy lessons are all listed in another module is one
    row marked "coveredBy" that links to them instead); a legacy lesson whose slots have all been rebuilt stays
    listed, right after the first slot it covered. Everything else is locked."""
    c = COURSE
    plain = lambda s: re.sub(r'`([^`]*)`', r'\1', s or '')
    entries = {s: m for s, m in reg['lessons'].items() if not m.get('poc')}

    def published_row(base, slug, m, legacy=False):
        row = dict(base)
        row.update({'status': 'published', 'slug': slug, 'url': f'/courses/{COURSE_SLUG}/lessons/{slug}/',
                    'duration': round(m.get('duration') or 0, 1), 'summary': m.get('summary', ''),
                    'published': m.get('published'), 'narrator': m.get('narrator'),
                    'poster': f'/courses/{COURSE_SLUG}/lessons/{slug}/poster.jpg' if m.get('mp4') else None})
        if legacy:
            row['legacy'] = True
        return row

    def base_row(les):
        row = {'id': les['id'], 'title': plain(les['raw_title']), 'idea': plain(les['idea'])}
        if les['lantern']:
            row['lantern'] = True
        return row

    modules, order = [], []
    if c.format == 'old':
        by_id = {m['id']: (slug, m) for slug, m in entries.items()}
        for n, mod in c.modules.items():
            rows = []
            for les in [x for x in c.lessons if x['module'] == n]:
                hit = by_id.get(les['id'])
                rows.append(published_row(base_row(les), hit[0], hit[1], bool(hit[1].get('legacy'))) if hit
                            else {**base_row(les), 'status': 'locked'})
            modules.append((mod, rows))
            order += rows
        return modules, order

    legacy = {lg['slug']: lg for lg in c.legacy if lg['slug'] in entries}
    for lg in c.legacy:
        if lg['slug'] not in entries:
            print(f"warning: legacy lesson {lg['slug']} is not in course.json; not listed")
    pos = {les['key']: i for i, les in enumerate(c.lessons)}
    first = {}
    for slug, lg in legacy.items():
        cov = sorted((c.lesson(t) for t in lg['covers'] if c.lesson(t)), key=lambda x: pos[x['key']])
        first[slug] = cov[0] if cov else None
    placed = {}

    def legacy_row(les, slug):
        m, lg = entries[slug], legacy[slug]
        row = published_row({'id': les['id'], 'title': plain(m.get('title') or lg['title']), 'idea': plain(les['idea'])}, slug, m, legacy=True)
        covered = [c.lesson(t) for t in lg['covers'] if c.lesson(t)]
        row['covers'] = [x['id'] for x in covered]
        row['coverTitles'] = [plain(x['raw_title']) for x in covered]     # the new lessons' titles, in "covers" order
        row['legacyId'] = m.get('id') or lg['id']
        if any(x['lantern'] for x in covered):
            row['lantern'] = True
        return row

    for n, mod in c.modules.items():
        rows = []
        for les in [x for x in c.lessons if x['module'] == n]:
            covering = [s_ for s_ in les['legacy'] if s_ in legacy]
            if les['status'] == 'legacy' and covering:
                fresh = [s_ for s_ in covering if s_ not in placed]
                elsewhere = not fresh and any(placed[s_] != n for s_ in covering)
                if not elsewhere:               # the slot's own row (its new title, locked), then its legacy lessons
                    rows.append({**base_row(les), 'status': 'locked', 'key': les['key']})
                for slug in fresh:              # every legacy lesson first met here is listed here, in table order
                    rows.append(legacy_row(les, slug))
                    placed[slug] = n
                if elsewhere:
                    slug = next(s_ for s_ in covering if placed[s_] != n)
                    # the slot's own lantern, never the legacy lesson's (which is set when any slot it covers has one)
                    row = {**{k: v for k, v in legacy_row(les, slug).items() if k != 'lantern'}, **base_row(les)}
                    row['coveredBy'] = slug     # listed in another module: this slot links to it
                    rows.append(row)
                continue
            m = entries.get(les['key'])
            if m and not m.get('legacy'):
                rows.append(published_row(base_row(les), les['key'], m))
            else:
                rows.append({**base_row(les), 'status': 'locked'})
            for slug in covering:
                if slug not in placed and first.get(slug) is les:
                    rows.append(legacy_row(les, slug))
                    placed[slug] = n
        modules.append((mod, rows))
    # legacy lessons covering no slot: at the end of the module of their old ID (or the Start)
    for slug, lg in legacy.items():
        if slug in placed:
            continue
        m = entries[slug]
        n = (m.get('id') or lg['id'] or '00')[:2]
        target = next((x for x in modules if x[0]['n'] == n), modules[0])
        row = published_row({'id': m.get('id') or lg['id'], 'title': plain(m.get('title') or lg['title']), 'idea': ''}, slug, m, legacy=True)
        row['covers'], row['coverTitles'], row['legacyId'] = [], [], m.get('id') or lg['id']
        target[1].append(row)
        placed[slug] = target[0]['n']
    for _, rows in modules:
        order += rows
    return modules, order


def course_data(reg) -> dict:
    """everything the site's course page needs, as plain data: the same shape as before 2026-10-12, plus
    "legacy": true (with "covers" and "legacyId") on legacy rows and "key" on new-lesson rows"""
    c = COURSE
    for x in sorted(t for t in c.lanterns if not c.lesson(t)):
        print(f'warning: lantern lesson {x} is not in curriculum.md')
    mods, order = course_rows(reg)
    if c.format == 'new':
        keys = {les['id']: les['key'] for les in c.lessons}
        for row in order:
            if not row.get('legacy') and not row.get('coveredBy') and row['id'] in keys:
                row['key'] = keys[row['id']]
    modules, total, filed, runtime = [], 0, 0, 0.0
    for mod, rows in mods:
        total += len(rows)
        pub = [x for x in rows if x['status'] == 'published' and not x.get('coveredBy')]
        filed += len(pub)
        runtime += sum(x.get('duration') or 0 for x in pub)
        name = mod['full']
        modules.append({'n': mod['n'], 'name': name, 'short': name.split(':')[0].strip(),
                        'region': (c.region(mod['district']) or {}).get('name'), 'lessons': rows,
                        'filed': sum(1 for x in rows if x['status'] == 'published')})
    # the latest lesson is picked from the rows the page lists (a lesson deleted or merged out of curriculum.md
    # since it was published has no row, so it can never leave "latest" empty); ties go to the later row
    pos = {id(x): i for i, x in enumerate(order)}
    latest_row = max((x for x in order if x['status'] == 'published' and not x.get('coveredBy')),
                     key=lambda x: (x.get('published') or '', pos[id(x)]), default=None)
    first = next((x for x in order if x['status'] == 'published'), None)
    return {
        'slug': COURSE_SLUG, 'title': COURSE_TITLE, 'updated': datetime.date.today().isoformat(),
        'totalLessons': total, 'publishedLessons': filed, 'runtimeSeconds': round(runtime),
        'moduleCount': len(modules), 'districtCount': sum(1 for r in c.regions if r['kind'] == 'district'),
        'regions': regions_out(c), 'lanternCount': sum(1 for les in c.lessons if les['lantern']), 'modules': modules,
        'latest': latest_row, 'first': first,
    }


def foot_links(order, slug):
    """(left, right) footer links of a lesson page: back to the whole curriculum, and on to the next row in
    curriculum order (a link when it is out; its title marked 'not released yet' while it is locked).
    A legacy page goes on to the next row that can be watched (past the last one, the next slot), so a new slot whose
    number repeats a legacy one never reads as its next lesson; a new lesson's page goes on to the next slot of the
    course, never to a legacy lesson listed beside it. "All N lessons" counts the curriculum's slots, not rows."""
    rows = [x for x in order if not x.get('coveredBy')]
    left = f'<a href="../../#curriculum">← All {len(COURSE.lessons) if COURSE else len(rows)} lessons</a>'
    i = next((k for k, x in enumerate(rows) if x.get('slug') == slug), -1)
    after = rows[i + 1:] if i >= 0 else []
    if rows and i >= 0 and rows[i].get('legacy'):
        nxt = next((x for x in after if x['status'] == 'published'), after[0] if after else None)
    else:
        nxt = next((x for x in after if not x.get('legacy')), None)
    if not nxt:
        return left, ''
    title = re.sub(r'`([^`]*)`', r'', nxt['title'])
    # a legacy row keeps "id" for its place in the order but shows its own old ID, the one its video's badge shows
    shown = nxt.get('legacyId') or nxt['id']
    if nxt['status'] == 'published':
        return left, f'<a href="../{nxt["slug"]}/">Next: {html.escape(shown)} {html.escape(title)} →</a>'
    return left, f'<a href="../../#module-{nxt["id"].split(".")[0]}">Next: {html.escape(shown)} {html.escape(title)} <span class="soon">(not released yet)</span></a>'


def stale_reason(slug, reg):
    """why a curriculum lesson's narration or video no longer matches the curriculum (tools/course.py freshness),
    or None. Legacy lessons, proofs of concept and tests are never stale."""
    les = curriculum_lesson(slug, reg)
    return coursedata.freshness(COURSE, les) if les else None


def stage(repo: pathlib.Path, slugs, reg, media=True, stale='error'):
    """copy engine + the given lessons into a blog checkout and write the course data file. A curriculum lesson
    whose narration or video is behind the curriculum is not staged: stale='error' stops, 'skip' leaves its page
    on the site as it is (its own course.js keeps it consistent), 'warn' stages it anyway. Returns the data file."""
    site = repo / SITE_DIR
    (site / 'engine' / 'assets').mkdir(parents=True, exist_ok=True)
    (site / 'engine' / 'legacy').mkdir(parents=True, exist_ok=True)
    for f in ENGINE_FILES:
        shutil.copy2(ENGINE / f, site / 'engine' / f)
    # the shared course data, current: proofs of concept and pages staged before per-lesson snapshots load it.
    # A curriculum lesson's page loads its own lessons/<key>/course.js instead (copy_lesson), so rewriting this
    # file never changes the map under a lesson that is already live.
    data = coursedata.course_data(COURSE)
    (site / 'engine' / 'course.js').write_text(coursedata.course_js_text(data, datetime.date.today().isoformat()), encoding='utf-8')
    for f in (ENGINE / 'legacy').glob('*.js'):
        shutil.copy2(f, site / 'engine' / 'legacy' / f.name)
    for f in (ENGINE / 'assets').glob('*.jpg'):
        shutil.copy2(f, site / 'engine' / 'assets' / f.name)
    _, order = course_rows(reg)
    staged = []
    for slug in slugs:
        if not (LESSONS / slug).is_dir():
            print(f'warning: {slug} has no folder in lessons/; not staged')
            continue
        why = stale_reason(slug, reg)
        if why:
            if stale == 'error':
                raise SystemExit(f'{slug} is behind the curriculum: {why}\n(publish.py --allow-stale publishes it anyway)')
            print(f"warning: {slug} is behind the curriculum: {why}; "
                  + ('its page on the site is left as it is' if stale == 'skip' else 'staged anyway'))
            if stale == 'skip':
                continue
        copy_lesson(LESSONS / slug, site / 'lessons' / slug, meta_of(slug, reg), foot_links(order, slug), reg, media)
        staged.append(slug)
    # the pages whose "Next" now points at a newly staged lesson get it updated (page only, no media copy): the
    # nearest released row before it (a legacy page goes on to the next released row) and the nearest new-lesson
    # row before it when that one is released (a new lesson's page goes on to the next new-lesson row)
    rows = [x for x in order if not x.get('coveredBy')]
    for slug in staged:
        i = next((k for k, x in enumerate(rows) if x.get('slug') == slug), -1)
        before = rows[i - 1::-1] if i > 0 else []
        prev_any = next((x for x in before if x['status'] == 'published'), None)
        prev_new = next((x for x in before if not x.get('legacy')), None)
        for prev in {x['slug'] for x in (prev_any, prev_new) if x and x['status'] == 'published'}:
            if prev not in staged:
                refresh_page(site, prev, order, reg)
    out = repo / DATA_FILE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(course_data(reg), indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return out


def meta_of(slug, reg):
    return {**lesson_meta(LESSONS / slug), **{k: v for k, v in reg['lessons'].get(slug, {}).items() if k in ('published',)}}


def refresh_page(site, slug, order, reg):
    """re-render one lesson page already on the site (its footer links), nothing else; its own course.js stays"""
    d = site / 'lessons' / slug
    if not d.is_dir() or not (LESSONS / slug).is_dir():
        return False
    (d / 'index.html').write_text(render_page(LESSONS / slug, meta_of(slug, reg), foot_links(order, slug), reg,
                                              own_data=(d / 'course.js').exists()), encoding='utf-8')
    return True


BLOG_PAGES = ['src/pages/courses/the-hidden-curriculum.astro', 'src/components/courses/LessonList.astro']
# comments in those files: a word that only appears in a comment is not handling
BLOG_COMMENTS = re.compile(r'<!--.*?-->|/\*.*?\*/|(?:^|(?<=\s))//[^\n]*', re.S | re.M)


def blog_problems(repo, data):
    """what the staged course data needs that the blog's course page does not support yet (the page is the blog's,
    edited there; this only reads it, comments stripped). The rows are drawn by LessonList, so it must handle
    "coveredBy" and "legacyId" itself; the page needs "legacyId" too, for the hero. Returns a list of sentences;
    empty when the page can show the data."""
    code = {}
    for rel_ in BLOG_PAGES:
        f = pathlib.Path(repo) / rel_
        if f.exists():
            code[rel_] = BLOG_COMMENTS.sub('', f.read_text(encoding='utf-8'))
    if not code:
        return []
    src = '\n'.join(code.values())
    page_src, rows_src = code.get(BLOG_PAGES[0], ''), code.get(BLOG_PAGES[1], '')
    out = []
    rows = [x for m in data.get('modules', []) for x in m.get('lessons', [])]
    if data.get('districtCount') != 6 and (re.search(r'\[\s*0\s*,\s*1\s*,\s*2\s*,\s*3\s*,\s*4\s*,\s*5\s*\]', src)
                                           or re.search(r'\bsix districts\b|\ball six\b|\bthe six\b', src, re.I)):
        out.append(f"the course page hard-codes six districts (copy and lantern row) but this curriculum has "
                   f"{data.get('districtCount')}: use d.districtCount and Array.from({{length: d.districtCount}}) there")
    if any(x.get('coveredBy') for x in rows) and 'coveredBy' not in rows_src:
        out.append('rows covered by a legacy lesson in another module ("coveredBy") would show as ordinary published '
                   'lessons linking to another video: render them as "covered in <legacy title>"')
    if any(x.get('legacy') and x.get('legacyId') and x['legacyId'] != x['id'] for x in rows) and not (
            'legacyId' in rows_src and 'legacyId' in page_src):
        out.append('legacy rows would show their slot\'s ID instead of their own ("legacyId"), with duplicate numbers: '
                   'show l.legacy ? l.legacyId : l.id in LessonList and the hero')
    return out


def get(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'course-publisher', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:          # 404 and friends: the status is the answer (--remove waits for 404)
        return e.code, b''
    except Exception:
        return 0, b''


def push(msg, no_push=False):
    """commit what is staged in the publish worktree and push it (three tries, rebasing on a race). Returns
    False when only committed (--no-push)."""
    git('commit', '-q', '-m', f'{msg}\n\n{TRAILER}')
    if no_push:
        print('committed in the publish worktree; not pushed (--no-push)')
        return False
    for attempt in range(3):
        r = git('push', 'origin', 'HEAD:main', check=False)
        if r.returncode == 0:
            break
        git('fetch', 'origin')
        git('rebase', 'origin/main')
    else:
        raise SystemExit('push failed three times:\n' + r.stderr)
    print(f'pushed {git("rev-parse", "--short", "HEAD").stdout.strip()}: {msg}')
    return True


def check_blog(repo, out, dry=False):
    """refuse (or, in a dry run, warn) when the blog's course page cannot show the staged course data yet"""
    probs = blog_problems(repo, json.loads(pathlib.Path(out).read_text(encoding='utf-8')))
    for pr in probs:
        print(('warning: ' if dry else 'BLOCKED: ') + 'the blog\'s course page: ' + pr)
    if probs and not dry:
        raise SystemExit(f'land these in the blog ({", ".join(BLOG_PAGES)}) first, then publish again; '
                         'nothing was committed')


def remove(key, reg, a):
    """take a lesson that is no longer in curriculum.md off the site: git rm its folder, drop its registry entry,
    rebuild the course data and every live page's footer links, push, and wait for its URL to answer 404"""
    if COURSE.lesson(key):
        raise SystemExit(f'{key} still has a row in curriculum.md: delete the row (and its spec file) first')
    meta = reg['lessons'].get(key)
    if meta and meta.get('legacy'):
        raise SystemExit(f'{key} is a legacy lesson: legacy lessons stay on the site (they are listed, marked legacy)')
    if COURSE.format == 'new' and key not in COURSE.retired_keys():
        raise SystemExit(f'list {key} under "## Retired keys" in curriculum.md first, so the key (a public URL) is never '
                         f'used again; python tools/course.py check enforces it')
    reg['lessons'].pop(key, None)
    url = f'{SITE}/courses/{COURSE_SLUG}/lessons/{key}/'
    if a.dry_run:
        print(f'DRY RUN: would remove {SITE_DIR}/lessons/{key}/ from the site, drop {key} from course.json'
              f"{'' if meta else ' (it has no entry)'}, rebuild the course data and the footer links of every page "
              f'still on the site, push, and wait for {url} to answer 404')
        return
    repo = pathlib.Path(a.into) if a.into else WT
    if not a.into:
        fresh_worktree()
    site = repo / SITE_DIR
    target = site / 'lessons' / key
    if not target.is_dir():
        print(f'note: {SITE_DIR}/lessons/{key}/ is not on the site')
    elif a.into:
        shutil.rmtree(target)
    else:
        git('rm', '-r', '-q', '--', f'{SITE_DIR}/lessons/{key}')
    REGISTRY.write_text(json.dumps(reg, indent=1), encoding='utf-8')
    out = stage(repo, [], reg)
    _, order = course_rows(reg)
    n = sum(refresh_page(site, s, order, reg) for s in sorted(reg['lessons']))
    print(f'refreshed the footer links of {n} page(s) still on the site')
    check_blog(repo, out)
    if a.into:
        print(f'removed {key} from {a.into} (no git)')
        return
    git('add', '-A', SITE_DIR, DATA_FILE)
    if not git('status', '--porcelain', '--', SITE_DIR, DATA_FILE).stdout.strip():
        print('nothing changed on the site')
        return
    if not push(f'Courses: remove {key} (no longer in the curriculum)', a.no_push) or a.no_verify:
        return
    deadline = time.time() + 12 * 60
    while time.time() < deadline:
        status, _ = get(f'{url}?v={int(time.time())}')
        if status == 404:
            print(f'GONE  {url} (404)')
            return
        time.sleep(20)
    raise SystemExit(f'{url} still answers after 12 minutes (did the Cloudflare build fail?)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson', nargs='?')
    ap.add_argument('--all', action='store_true', help='re-stage every published lesson')
    ap.add_argument('--data-only', action='store_true')
    ap.add_argument('--into', help='stage into this blog checkout instead of the publish worktree (no git)')
    ap.add_argument('--retire', metavar='OLD_SLUG', help='drop a previously registered lesson (e.g. a promoted proof of concept)')
    ap.add_argument('--remove', metavar='KEY', help='take a lesson deleted from curriculum.md off the site (git rm, registry, links, 404)')
    ap.add_argument('--allow-stale', action='store_true',
                    help='publish a lesson even though its narration or video is behind the curriculum (course.py sync says so)')
    ap.add_argument('--no-push', action='store_true')
    ap.add_argument('--no-verify', action='store_true')
    ap.add_argument('--dry-run', action='store_true',
                    help='stage the course data and the pages (no media) into a temp folder: no git, no network, course.json untouched')
    ap.add_argument('--out', help='--dry-run: also write the course data JSON here')
    ap.add_argument('--curriculum', help='read this curriculum.md instead of the course\'s (testing; --dry-run only)')
    ap.add_argument('--registry', help='read this course.json instead of the course\'s (testing; --dry-run only)')
    a = ap.parse_args()
    if (a.curriculum or a.registry) and not a.dry_run:
        raise SystemExit('--curriculum / --registry are for testing: use them with --dry-run')
    global COURSE
    COURSE = coursedata.load(a.curriculum or coursedata.CURRICULUM, registry=a.registry)
    reg = registry(a.registry)
    if a.remove:
        return remove(a.remove, reg, a)
    slugs, msg = [], 'Courses: refresh course data'
    if a.lesson:
        L = lesson_dir(a.lesson)
        meta = lesson_meta(L)
        if not (L / 'audio' / 'mix.mp3').exists() and not a.dry_run:
            raise SystemExit('no audio/mix.mp3: run narrate.py and mix.py first')
        why = stale_reason(L.name, reg)
        if why and not a.allow_stale and not a.dry_run:
            raise SystemExit(f'{L.name} is behind the curriculum: {why}\n(publish.py --allow-stale publishes it anyway)')
        les = COURSE.lesson(L.name) if COURSE.format == 'new' else None
        if les:                      # a new lesson: registered under its key, its ID from curriculum.md
            meta['key'], meta['id'] = les['key'], les['id']
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
    if a.dry_run:
        import tempfile
        if not slugs and not a.data_only:
            slugs = sorted(s for s in reg['lessons'] if (LESSONS / s).is_dir())
        tmp = pathlib.Path(tempfile.mkdtemp(prefix='publish-dry-run-'))
        out = stage(tmp, slugs, reg, media=False, stale='warn')
        if a.out:
            shutil.copy2(out, a.out)
        check_blog(BLOG, out, dry=True)              # reads the blog checkout's course page; changes nothing
        data = json.loads(out.read_text(encoding='utf-8'))
        print(f'DRY RUN (no git, no network, course.json untouched): {len(slugs)} lesson page(s) + course data staged into {tmp}')
        print(f"course data: {data['totalLessons']} lessons, {data['publishedLessons']} published "
              f"({sum(1 for m in data['modules'] for x in m['lessons'] if x.get('legacy') and not x.get('coveredBy'))} legacy), "
              f"{data['moduleCount']} modules, {data['districtCount']} districts -> {out}" + (f' and {a.out}' if a.out else ''))
        return
    if not slugs and not a.data_only and not a.all:
        raise SystemExit('name a lesson, or pass --all / --data-only')
    REGISTRY.write_text(json.dumps(reg, indent=1), encoding='utf-8')
    coursedata.write_course_js(coursedata.course_data(COURSE))      # engine/course.js in step with curriculum.md

    # one lesson: stop when it is stale (unless --allow-stale); --all / --data-only: leave stale lessons' pages as they are
    stale = 'warn' if a.allow_stale else 'error' if a.lesson and not a.all else 'skip'
    if a.into:
        out = stage(pathlib.Path(a.into), slugs, reg, stale=stale)
        check_blog(pathlib.Path(a.into), out, dry=True)
        print(f'staged {len(slugs)} lesson(s) + course data into {a.into} (no git)')
        return
    fresh_worktree()
    out = stage(WT, slugs, reg, stale=stale)
    check_blog(WT, out)
    git('add', SITE_DIR, DATA_FILE)
    if not git('status', '--porcelain', '--', SITE_DIR, DATA_FILE).stdout.strip():
        print('nothing changed on the site')
        return
    if not push(msg, a.no_push) or a.no_verify:
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
