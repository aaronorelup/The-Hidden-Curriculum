"""course.py: the course map and the course order, as data.

curriculum.md is the one source of truth for the order of the course: its districts, modules, lessons,
the Lantern (AI) lessons and the legacy lessons. This tool reads it (the 2026-10-12 format with lesson
keys, and the older format without them), checks it, and writes what everything else reads:

  engine/course.js       window.COURSE = {...}: districts, modules, lessons, lanterns. Every new lesson
                         page loads it before engine/map.js, which lays the course map out from it.
  lessons/<key>/...      for every built NEW lesson: lesson.js id/module, the [map] section of script.md
                         (generated narration), course-sync.json (what the map looked like at the last sync).

usage (from the course folder; every command takes --curriculum <path> for testing):
  python tools/course.py check [--no-browser]         keys, IDs, spec files, legacy slugs, map labels, S-/C-IDs,
                                                      orphaned lesson folders / specs / registry entries
  python tools/course.py renumber [--write]           renumber lesson IDs, modules and districts in file order
                                                      (curriculum.md + spec front matter); prints a diff
  python tools/course.py sync [--dry-run]             course.js + every built new lesson; prints what needs
                                                      narration (map text changed) or only a re-render
  python tools/course.py remap [--render] [--dry-run] run those commands (narrate.py re-bills only changed
                                                      sections; mix.py; with --render also render.py)
  python tools/course.py next                         the first `todo` lesson, as JSON
  python tools/course.py lesson <key|id>              one lesson (row + spec), as JSON
  python tools/course.py map [--png out.png] [--pin <module|key|id>]
                                                      the map as text (or a rendered still)

Testing options: --lessons <dir> (built lessons, default lessons/), --course-js <file> (default
engine/course.js), --registry <file> (default course.json).

See docs/course-data.md for how curriculum.md, the spec files, course.js, the [map] section, sync and remap fit
together, and how to combine, split, add, delete, reorder or rename lessons, modules and districts.
"""
import argparse
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import ENGINE, LESSONS, ROOT  # noqa: E402

CURRICULUM = ROOT / 'curriculum.md'
COURSE_JS = ENGINE / 'course.js'
REGISTRY = ROOT / 'course.json'
COURSE_TITLE = 'The Hidden Curriculum'

# the module labels the hand-drawn map (engine/legacy/map-v1.js) used for the modules of the 2026-10-01 curriculum;
# in the OLD curriculum format a module whose full name matches one of these keeps its old label, so the old
# curriculum draws the old map. The new format never uses them (its auto labels keep the full name's casing).
# Any module can set its own label in curriculum.md: ## Module 05 — Long Name Here <!-- map: Short name -->
LEGACY_MAP_LABELS = {
    'Orientation: The Map and the Lantern': 'Orientation',
    'Your Computer, Under the Hood': 'Your computer',
    'The Command Line': 'The command line',
    'Development Environments': 'Dev environments',
    'Programming Languages': 'Languages',
    'Python & JavaScript Ecosystems (Packages)': 'Packages',
    'Data & Databases': 'Data',
    'Concurrency: Doing Many Things at Once': 'Concurrency',
    'Git, GitHub & Agents on Git': 'Git & GitHub',
    'Networking & the Internet': 'Networking',
    'APIs, Webhooks & MCP': 'APIs, webhooks & MCP',
    'Websites & Hosting': 'Websites',
    'Cloudflare & the Edge': 'Cloudflare',
    'Containers, Servers & the Cloud': 'Containers & cloud',
    'Identity, Authentication & Keys (Developer Side)': 'Identity & keys',
    'Personal Security & Secrets': 'Secrets & security',
    'Running Things Without You': 'Running without you',
    'What "an Application" Is': 'Applications',
    'Other Platforms: Phones, App Stores & Physical Devices': 'Other platforms',
    'Payments, Users & Selling Software': 'Payments & users',
    'Licenses & Legal': 'Licenses',
    'Capstone': 'Capstone',
}

MAP_LIMITS = {'districts': (4, 7), 'modules': 5}
KEY_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
ID_RE = re.compile(r'^(\d{2})\.(\d{2})([a-z]?)$')
REGION_RE = re.compile(r'^#\s+(Start|Finish|District\s+(\d+))\s*[·•:|-]\s*(.+?)\s+[—–]{1,2}\s+(.+?)\s*$')
REGION_RE_ASCII = re.compile(r'^#\s+(Start|Finish|District\s+(\d+))\s*[·•:|-]\s*(.+?)\s+-{1,2}\s+(.+?)\s*$')
MODULE_RE = re.compile(r'^##\s+Module\s+(\d+)\s*[—–-]+\s*(.*?)\s*$')
MAP_LABEL_RE = re.compile(r'<!--\s*map:\s*(.*?)\s*-->')
REGION_ID_RE = re.compile(r'\s*<!--\s*id:\s*(\S*?)\s*-->\s*')    # # District 3 · The Wire — how computers talk <!-- id: network -->
LINK_RE = re.compile(r'^\[(.+?)\]\((.+?)\)$')
BEGIN, END = '<!-- map:begin -->', '<!-- map:end -->'


# ------------------------------------------------------------------ small helpers
def plain(s: str) -> str:
    """markdown cell -> display text (backticks off, as the site shows titles)"""
    return re.sub(r'`([^`]*)`', r'\1', s or '').strip()


def slugify(title: str, maxlen=40) -> str:
    """kebab-case key from a title, the same rule new_lesson.py has always used for slugs, cut to maxlen at a hyphen"""
    s = re.sub(r'[^a-z0-9]+', '-', plain(title).lower()).strip('-')
    if len(s) > maxlen:
        s = s[:maxlen + 1]
        s = s[:s.rfind('-')] if '-' in s else s[:maxlen]
    return s.strip('-') or 'lesson'


def region_id(name: str) -> str:
    """the same district id publish.py has always written for the site: 'The Machine' -> 'machine'"""
    return re.sub(r'[^a-z]+', '-', re.sub(r'^the ', '', name.lower())).strip('-') or 'region'


def split_row(line: str):
    """cells of a markdown table row; a | inside `code` or escaped as \\| stays in its cell"""
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'):
        s = s[:-1]
    cells, cur, code, i = [], '', False, 0
    while i < len(s):
        ch = s[i]
        if ch == '\\' and i + 1 < len(s) and s[i + 1] == '|':
            cur += '|'; i += 2; continue
        if ch == '`':
            code = not code
        if ch == '|' and not code:
            cells.append(cur.strip()); cur = ''
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def id_list(cell: str, pattern=r'[A-Z]\d+'):
    if not cell or cell.strip() in ('—', '-', '–', 'none', 'None'):
        return []
    return re.findall(r'\b' + pattern + r'\b', cell)


def tokens(cell: str):
    """lesson references in a cell (IDs like 00.01 or keys like files-are-just-bytes), comma/space separated"""
    if not cell or cell.strip() in ('—', '-', '–', 'none', 'None'):
        return []
    return [t for t in re.split(r'[\s,;]+', plain(cell)) if t and t not in ('—', '-', '–', '+', 'and')]


def front_matter(text: str):
    """YAML-ish front matter: key: value, key: [a, b], key: then '- a' lines. Returns (dict, body)."""
    m = re.match(r'^﻿?---\s*\n(.*?)\n---\s*(?:\n|$)', text, re.S)
    if not m:
        return {}, text
    out, last = {}, None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue
        li = re.match(r'^\s+-\s*(.*)$', raw) or (re.match(r'^-\s*(.*)$', raw) if last else None)
        if li and last:
            if not isinstance(out[last], list):
                out[last] = [] if out[last] in ('', None) else [out[last]]
            out[last].append(_scalar(li.group(1)))
            continue
        kv = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*(.*)$', raw)
        if kv:
            last = kv.group(1)
            v = kv.group(2).strip()
            if v.startswith('[') and v.endswith(']'):
                out[last] = [_scalar(x) for x in split_csv(v[1:-1]) if x.strip()]
            else:
                out[last] = _scalar(v)
    return out, text[m.end():]


def split_csv(s):
    out, cur, q = [], '', None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in '"\'':
            q = ch; cur += ch
        elif ch == ',':
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out]


def _scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        return v[1:-1]
    if re.fullmatch(r'-?\d+', v) and not re.fullmatch(r'0\d+', v):
        return int(v)
    if re.fullmatch(r'-?\d+\.\d+', v) and not ID_RE.match(v):
        return float(v)
    if v.lower() in ('true', 'false'):
        return v.lower() == 'true'
    if v.lower() in ('null', '~', ''):
        return '' if v == '' else None
    return v


def sha(obj) -> str:
    return hashlib.sha1(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:16]


# ------------------------------------------------------------------ parsing curriculum.md
class Course:
    """everything curriculum.md says, in file order. Use load()."""

    def __init__(self, path):
        self.path = pathlib.Path(path).resolve()
        self.base = self.path.parent
        self.format = 'old'
        self.title = COURSE_TITLE
        self.regions, self.modules, self.lessons = [], {}, []
        self.module_heads = []       # every ## Module heading in file order (duplicates too), for renumber
        self.lanterns, self.legacy, self.backlog, self.build_log = [], [], [], []
        self.retired = []            # ## Retired keys: [{key, note, line}], keys that may never be used again
        self.problems = []           # (level, message) found while parsing
        self.lessons_dir = LESSONS
        self.registry_path = REGISTRY

    # lookups
    def lesson(self, ref):
        ref = str(ref).strip()
        for les in self.lessons:
            if ref in (les['key'], les['id']):
                return les
        return None

    def region(self, rid):
        return next((r for r in self.regions if r['id'] == rid), None)

    def module_region(self, n):
        m = self.modules.get(n)
        return self.region(m['district']) if m else None

    def spec_path(self, les):
        return (self.base / les['link']).resolve() if les.get('link') else self.base / 'curriculum' / 'lessons' / f"{les['key']}.md"

    def spec(self, les):
        p = self.spec_path(les)
        if not p.exists():
            return None, ''
        return front_matter(p.read_text(encoding='utf-8'))

    def registry(self):
        p = pathlib.Path(self.registry_path)
        return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {'lessons': {}}

    def built(self, les):
        """the lesson's folder when it has been scaffolded: lessons/<key>/ (new lessons only)"""
        d = pathlib.Path(self.lessons_dir) / les['key']
        return d if d.is_dir() else None

    def refs(self, les):
        """the tokens that may name this lesson in the Lantern line and a Legacy table's Covers: its key, and in
        the old format (no keys) its ID. The new format takes keys only: IDs change whenever lessons move, so an
        ID there would silently point at another lesson (check reports any)."""
        return (les['key'],) if self.format == 'new' else (les['key'], les['id'])

    def legacy_for(self, les):
        """legacy slugs that cover this lesson slot"""
        out = list(les.get('legacy') or [])
        for lg in self.legacy:
            if any(r in lg['covers'] for r in self.refs(les)):
                if lg['slug'] not in out:
                    out.append(lg['slug'])
        return out

    def retired_keys(self):
        return {r['key'] for r in self.retired}


def load(path=CURRICULUM, lessons_dir=None, registry=None) -> Course:
    c = Course(path)
    if lessons_dir:
        c.lessons_dir = pathlib.Path(lessons_dir)
    if registry:
        c.registry_path = pathlib.Path(registry)
    text = c.path.read_text(encoding='utf-8')
    lines = text.splitlines()
    region = module = None
    ctx, header, intro = None, None, []
    seen_region = False
    for no, line in enumerate(lines, 1):
        s = line.rstrip()
        # a region heading may pin its id: # District 3 · The Wire — how computers talk <!-- id: network -->
        rid_m = REGION_ID_RE.search(s) if s.startswith('# ') else None
        s_reg = REGION_ID_RE.sub(' ', s).rstrip() if rid_m else s
        if s.startswith('# ') and not seen_region and not REGION_RE.match(s_reg) and not REGION_RE_ASCII.match(s_reg):
            t = re.sub(r'\s+[—–-]+\s+Master Curriculum.*$', '', s[2:].strip())
            if t:
                c.title = t
            continue
        m = REGION_RE.match(s_reg) or REGION_RE_ASCII.match(s_reg)
        if m:
            seen_region = True
            kind = 'district' if m.group(2) else m.group(1).lower()
            name = plain(m.group(3).strip())
            rid = rid_m.group(1).strip() if rid_m else region_id(name)
            region = {'kind': kind, 'n': int(m.group(2)) if m.group(2) else None, 'id': rid, 'name': name,
                      'q': plain(m.group(4).strip()), 'mods': [], 'line': no, 'explicit_id': bool(rid_m)}
            if rid_m and not KEY_RE.match(rid):
                c.problems.append(('error', f"line {no}: region id {rid!r} must be kebab-case (<!-- id: network -->)"))
            c.regions.append(region)
            module, ctx, header = None, 'region', None
            continue
        m = MODULE_RE.match(s)
        if m:
            n = m.group(1).zfill(2)
            raw = m.group(2)
            lab = MAP_LABEL_RE.search(raw)
            full = plain(MAP_LABEL_RE.sub('', raw)).strip()
            # the label is settled after parsing (the old format's hand-made labels apply to the old format only)
            label = lab.group(1).strip() if lab else None
            module = {'n': n, 'name': label, 'full': full, 'district': region['id'] if region else None, 'lessons': [], 'line': no,
                      'explicit_label': bool(lab)}
            if n in c.modules:
                c.problems.append(('error', f'line {no}: module {n} appears twice'))
            c.modules[n] = module
            c.module_heads.append(module)
            if region is not None:
                region['mods'].append(n)
            else:
                c.problems.append(('error', f'line {no}: module {n} comes before any # Start / District / Finish heading'))
            ctx, header = 'module', None
            continue
        if s.startswith('## '):
            h = s[3:].strip().lower()
            module, header = None, None
            ctx = ('legacy' if h.startswith('legacy') else 'backlog' if h.startswith('deep-dive') or h.startswith('deep dive')
                   else 'buildlog' if h.startswith('build log') else 'retired' if h.startswith('retired') else None)
            continue
        if ctx == 'retired':
            # - old-key — why it was retired (date)        or a table row | old-key | why |
            rk = re.match(r'^\s*[-*]\s+`?([a-z0-9][a-z0-9-]*)`?(?:\s*[—–:-]+\s*(.*))?$', s)
            if rk:
                c.retired.append({'key': rk.group(1), 'note': plain(rk.group(2) or ''), 'line': no})
            elif s.lstrip().startswith('|'):
                cells = split_row(s)
                if cells and KEY_RE.match(plain(cells[0])):
                    c.retired.append({'key': plain(cells[0]), 'note': plain(cells[1]) if len(cells) > 1 else '', 'line': no})
            continue
        if s.strip() == '---':
            module, header = None, None
            if ctx in ('module', 'region'):
                ctx = None
            continue
        if not seen_region:
            ml = re.match(r'^Lantern lessons:\s*(.*)$', s)
            if ml:
                c.lanterns = [t for t in re.split(r'[\s,]+', plain(ml.group(1))) if t]
                continue
            if not s.startswith('Status key') and not s.startswith('|'):
                intro.append(s)
        else:
            ml = re.match(r'^Lantern lessons:\s*(.*)$', s)
            if ml:
                c.lanterns = [t for t in re.split(r'[\s,]+', plain(ml.group(1))) if t]
                continue
        if ctx == 'buildlog' and s.lstrip().startswith('- '):
            c.build_log.append(s.lstrip()[2:])
            continue
        if s.lstrip().startswith('|'):
            cells = split_row(s)
            if header is None:
                header = [x.strip().lower() for x in cells]
                continue
            if all(re.fullmatch(r':?-{2,}:?', x.strip()) for x in cells if x.strip()):
                continue
            row = dict(zip(header, cells))
            if ctx == 'module' and module is not None:
                les = lesson_row(row, header, cells, module, region, no, c)
                if les:
                    c.lessons.append(les)
                    module['lessons'].append(les['key'])
            elif ctx == 'legacy':
                lg = legacy_row(row, cells, no, header)
                if lg:
                    c.legacy.append(lg)
            elif ctx == 'backlog':
                c.backlog.append({'topic': plain(row.get('topic', cells[0])), 'concepts': id_list(row.get('concepts', ''), r'C\d+'),
                                  'sources': id_list(row.get('sources', ''), r'S\d+'), 'why': plain(row.get('why it waits', '')), 'line': no})
        else:
            header = None if not s.lstrip().startswith('|') else header
    c.intro = '\n'.join(intro).strip()
    # the new format links every lesson to its spec file and has a Legacy table; the old one has neither
    if c.legacy or any(les.get('link') for les in c.lessons) or any('concepts' in les['_cols'] for les in c.lessons):
        c.format = 'new'
    # map labels: an explicit <!-- map: ... --> wins; the old format keeps the hand-drawn map's labels; otherwise the
    # name before a colon, without a trailing (parenthesis), in the full name's own casing
    for m_ in c.modules.values():
        if not m_['explicit_label']:
            m_['name'] = (LEGACY_MAP_LABELS.get(m_['full']) if c.format == 'old' else None) or auto_label(m_['full'])
    # unique keys: in the old format they are derived from titles, so de-duplicate them
    seen = {}
    for les in c.lessons:
        k = les['key']
        if k in seen:
            if les['derived']:
                i = 2
                while f'{k}-{i}' in seen:
                    i += 1
                les['key'] = f'{k}-{i}'
            else:
                c.problems.append(('error', f"line {les['line']}: key {k} is used twice (also line {seen[k]['line']})"))
        seen[les['key']] = les
    for m_ in c.modules.values():
        m_['lessons'] = [les['key'] for les in c.lessons if les['module'] == m_['n']]
    # lanterns: lesson keys (the old format: IDs)
    lan = set(c.lanterns)
    for les in c.lessons:
        les['lantern'] = any(r in lan for r in c.refs(les))
    # old format: legacy coverage comes from the registry (a legacy lesson covers the row with its own ID)
    if c.format == 'old':
        reg = c.registry()
        for slug, meta in sorted(reg.get('lessons', {}).items()):
            if meta.get('legacy') and not meta.get('poc'):
                les = c.lesson(meta.get('id', ''))
                c.legacy.append({'slug': slug, 'id': meta.get('id', ''), 'title': meta.get('title', ''), 'covers': [meta.get('id', '')] if les else [],
                                 'note': 'from course.json (old curriculum format)', 'line': 0, 'derived': True})
    for les in c.lessons:
        les['legacy'] = c.legacy_for(les)
    return c


def auto_label(full: str) -> str:
    """map label from a module name: the part before a colon, without a trailing (parenthesis)"""
    s = full.split(':')[0].strip()
    s = re.sub(r'\s*\([^)]*\)\s*$', '', s).strip()
    return s or full


def lesson_row(row, header, cells, module, region, no, c):
    rid = (row.get('id') or cells[0]).strip()
    if not ID_RE.match(rid):
        return None
    cell = (row.get('lesson') or (cells[1] if len(cells) > 1 else '')).strip()
    link, title, key, derived = None, cell, None, False
    lm = LINK_RE.match(cell)
    if lm:
        title, link = lm.group(1).strip(), lm.group(2).strip()
        km = re.search(r'(?:^|/)([^/]+)\.md$', link)
        key = km.group(1) if km else None
    if not key:
        km = re.search(r'<!--\s*key:\s*([\w-]+)\s*-->', cell)
        if km:
            key = km.group(1)
            title = re.sub(r'<!--.*?-->', '', title).strip()
    if not key:
        key, derived = slugify(title), True
    status = (row.get('status') or cells[-1]).strip().strip('`').lower()
    status = status.split()[0] if status else 'todo'
    les = {'id': rid, 'key': key, 'title': plain(title), 'raw_title': title, 'idea': plain(row.get('key idea', '')),
           'concepts': id_list(row.get('concepts', ''), r'C\d+'), 'sources': id_list(row.get('sources', ''), r'S\d+'),
           'status': status, 'module': module['n'], 'district': region['id'] if region else None,
           'link': link, 'line': no, 'derived': derived, '_cols': header, 'module_line': module['line']}
    if ID_RE.match(rid).group(1) != module['n']:
        c.problems.append(('error', f"line {no}: lesson {rid} sits under Module {module['n']} "
                                    f"(python tools/course.py renumber --write fixes the IDs)"))
    return les


def legacy_row(row, cells, no, header=()):
    first = plain(row.get('legacy lesson') or cells[0])
    slug = plain(row.get('slug') or (cells[1] if len(cells) > 1 else '')).strip()
    if not slug:
        return None
    m = re.match(r'^(\d{2}\.\d{2}[a-z]?)\s+(.*)$', first)
    col = list(header).index('covers') if 'covers' in header else 2
    return {'slug': slug, 'id': m.group(1) if m else '', 'title': m.group(2) if m else first,
            'covers': tokens(row.get('covers', cells[2] if len(cells) > 2 else '')),
            'note': plain(row.get('note', '')), 'line': no, 'covers_col': col}


# ------------------------------------------------------------------ the browser data (engine/course.js)
def course_data(c: Course) -> dict:
    """window.COURSE: what engine/map.js and the lesson pages need"""
    districts = [{'id': r['id'], 'kind': r['kind'], 'n': r['n'], 'name': r['name'], 'question': r['q'], 'modules': list(r['mods'])}
                 for r in c.regions]
    modules = [{'n': m['n'], 'name': m['name'], 'full': m['full'], 'district': m['district']} for m in c.modules.values()]
    lessons = []
    for les in c.lessons:
        d = c.built(les) if c.format == 'new' else None
        # lantern / legacy / slug only when set, to keep the file small (map.js treats a missing field as false / none)
        row = {'id': les['id'], 'key': les['key'], 'title': les['title'], 'module': les['module'], 'district': les['district'],
               'status': les['status']}
        if les['lantern']:
            row['lantern'] = True
        if les['legacy']:
            row['legacy'] = les['legacy']
        if d:
            row['slug'] = d.name
        lessons.append(row)
    data = {'title': c.title, 'format': c.format, 'districts': districts, 'modules': modules, 'lessons': lessons,
            'lanterns': list(c.lanterns),
            'legacy': [{'slug': lg['slug'], 'id': lg['id'], 'title': lg['title'], 'covers': lg['covers']} for lg in c.legacy]}
    data['mapHash'] = map_hash(data)
    return data


def map_hash(data: dict) -> str:
    """what the map DRAWING depends on (not statuses): regions, module labels, the number of lanterns, and map.js.
    The Start and the Finish are drawn as a circle with their module number and the fixed words 'Start' / 'Finish',
    so only their kind and module numbers count here (not even their id, which follows their name and is never
    drawn); their name, question and module label appear only in a Start / Finish lesson's own [map] scene, and
    lesson_state adds them to that lesson's drawing hash."""
    ends = {d['id']: d['kind'] for d in data['districts'] if d['kind'] in ('start', 'finish')}
    shape = {'districts': [[d['kind'], d['modules']] if d['id'] in ends else [d['id'], d['kind'], d['name'], d['question'], d['modules']]
                           for d in data['districts']],
             'modules': [[m['n'], ends[m['district']]] if m['district'] in ends else [m['n'], m['name'], m['district']] for m in data['modules']]}
    mj = ENGINE / 'map.js'
    shape['mapjs'] = hashlib.sha1(mj.read_bytes().replace(b'\r\n', b'\n')).hexdigest()[:12] if mj.exists() else ''
    return sha(shape)


def course_js_text(data: dict, generated: str) -> str:
    """one district / module / lesson per line, so a change to the curriculum reads as a small diff"""
    full = {'generated': generated, **data}
    parts = []
    for k, v in full.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            inner = ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in v)
            parts.append(f' {json.dumps(k)}: [\n{inner}\n ]')
        else:
            parts.append(f' {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}')
    return ('// generated by tools/course.py sync from curriculum.md; do not edit (edit curriculum.md, then run sync)\n'
            'window.COURSE = {\n' + ',\n'.join(parts) + '\n};\n')


def write_course_js(data: dict, target=COURSE_JS, dry=False):
    """write course.js only when its content changed; 'generated' is the date of the last real change"""
    target = pathlib.Path(target)
    old = target.read_text(encoding='utf-8') if target.exists() else ''
    m = re.search(r'"generated":\s*"([^"]*)"', old)
    if m and course_js_text(data, m.group(1)) == old:
        return False
    if not dry:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(course_js_text(data, datetime.date.today().isoformat()), encoding='utf-8', newline='\n')
    return True


# ------------------------------------------------------------------ the [map] section: narration written for the ear
# written forms the narrator says as a word, not letter by letter: (spoken form, caption pair or None).
# A caption pair applies to the WHOLE lesson's captions (narrate.py caption_map), so a pair is only given when the
# spoken form is not an ordinary word ('yamel', 'vee ram'); words like PATH, RAM or REST go to the voice as written
# (the voices read them as words, as 01-05's script does with PATH) and so need no pair: 'path=PATH' would turn
# every "path" in the lesson into PATH.
SAID_AS_WORDS = {'JSON': ('Jason', 'Jason=JSON'), 'SQL': ('sequel', 'sequel=SQL'), 'GUI': ('gooey', 'gooey=GUI'),
                 'OAuth': ('oh auth', 'oh auth=OAuth'), '2FA': ('two factor', 'two factor=2FA'), 'NASA': ('NASA', None),
                 'YAML': ('yamel', 'yamel=YAML'), 'TOML': ('tommel', 'tommel=TOML'), 'VRAM': ('vee ram', 'vee ram=VRAM'),
                 'JPEG': ('jay peg', 'jay peg=JPEG'),
                 'PATH': ('PATH', None), 'RAM': ('RAM', None), 'REST': ('REST', None), 'CORS': ('CORS', None),
                 'NAT': ('NAT', None), 'LAN': ('LAN', None), 'WAN': ('WAN', None)}


def say(s: str):
    """written name -> what the narrator should read (COURSE.md's spoken forms), plus the caption spellings
    narrate.py needs to turn it back on screen. API -> A P I, MCP -> M C P, & -> and, .py -> dot P Y,
    CI/CD -> C I C D (caption pair 'C I C D=CI/CD'), YAML -> yamel, PATH stays PATH (read as a word)."""
    pairs = []
    s = plain(s)
    s = s.replace('&', ' and ').replace('e.g.', 'for example')

    def word(w):
        """one written token (no '/') -> (spoken, pairs)"""
        if w in SAID_AS_WORDS:
            spoken, pair = SAID_AS_WORDS[w]
            return spoken, [pair] if pair else []
        m = re.fullmatch(r'([A-Z]{2,6})(s?)', w)
        if m:
            spoken = ' '.join(m.group(1)) + ('s' if m.group(2) else '')
            return spoken, [f'{spoken}={w}'] if m.group(2) else []
        m = re.fullmatch(r'\.([a-z0-9]{1,5})', w)
        if m:
            return 'dot ' + ' '.join(m.group(1).upper()), []
        return w, []

    # a token with a slash and an acronym in it (CI/CD, TCP/IP, HTTP/2) is said part by part, without the slash,
    # and captioned back as one token; 'and/or' and other plain words are left alone
    def slashed(m):
        tok = m.group(0)
        parts = tok.split('/')
        if not any(re.fullmatch(r'[A-Z]{2,6}s?', p) or p in SAID_AS_WORDS for p in parts):
            return tok
        said = [word(p) for p in parts if p]
        spoken = ' '.join(x[0] for x in said)
        for x in said:
            pairs.extend(x[1])
        pairs.append(f'{spoken}={tok}')
        return spoken
    s = re.sub(r'(?<![\w/])[\w.]+(?:/[\w.]+)+(?![\w/])', slashed, s)
    for w, (spoken, pair) in SAID_AS_WORDS.items():
        rx = r'(?<![\w.])' + re.escape(w) + r'(?![\w])'
        if re.search(rx, s):
            s = re.sub(rx, spoken, s)
            if pair:
                pairs.append(pair)

    def ext(m):
        return 'dot ' + ' '.join(m.group(1).upper())
    s = re.sub(r'(?<![\w])\.([a-z0-9]{1,5})\b', ext, s)

    def acro(m):
        if m.group(0) in SAID_AS_WORDS:         # PATH, RAM...: read as a word, left as written
            return m.group(0)
        letters, plural = m.group(1), m.group(2)
        spoken = ' '.join(letters)
        if plural:
            spoken += 's'
            pairs.append(f'{spoken}={letters}s')
        return spoken
    s = re.sub(r'\b([A-Z]{2,6})(s?)\b', acro, s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s, list(dict.fromkeys(pairs))


def map_narration(c: Course, les: dict):
    """the generated narration of a lesson's [map] section: 2-3 sentences, district and module named (with
    [[district]] and [[module]] cues), no numbers, no neighbouring titles. Returns (text, caption_pairs)."""
    r = c.region(les['district'])
    m = c.modules.get(les['module'])
    if not r or not m:
        return None, []
    name, p1 = say(r['name'])
    q, p2 = say(r['q'])
    mod, p3 = say(m['name'])
    pairs = p1 + p2 + p3
    q = q.rstrip('.?!')
    # three sentences: the opener (the map assembles under it), the place (the district comes into focus at
    # [[district]], the pin drops at [[module]]), and a fixed closing line that gives the you-are-here card time on screen
    opener = "Here's where this lesson sits on the map."
    close = "That's where everything in this lesson gets stored."
    same = mod.lower() == name.lower()
    if r['kind'] in ('start', 'finish'):
        place = 'the Start' if r['kind'] == 'start' else 'the Finish'
        if same:
            text = (f"{opener} We're at [[district]]{place}, [[module]]{name}: {q}. "
                    + ("Every district on the path builds on what we shelve here." if r['kind'] == 'start'
                       else "It's where every district on the path comes together."))
        else:
            text = f"{opener} We're at [[district]]{place}, {name}: {q}, on the shelf called [[module]]{mod}. {close}"
    else:
        text = f"{opener} We're in [[district]]{name}, the district about {q}, on the shelf called [[module]]{mod}. {close}"
    return text, sorted(set(pairs))


def map_block(c: Course, les: dict) -> str:
    text, pairs = map_narration(c, les)
    out = [BEGIN, '<!-- generated by tools/course.py sync from curriculum.md: change the curriculum and re-run sync, never this text -->']
    if pairs:
        out.append('<!-- captions: ' + '; '.join(pairs) + ' -->')
    out += [text, END]
    return '\n'.join(out)


MAP_SECTION = """## 02 — Where this sits on the map [map]
{block}
> Standard map section: generated from curriculum.md by tools/course.py sync; its scene is scenes/02.js,
> SCENE('02', (t, S) => K.map.intro(t, S)). Do not rewrite or re-animate it by hand.
"""
MAP_SCENE = "SCENE('02', (t, S) => K.map.intro(t, S));\n"
MAP_HEAD = re.compile(r'^##\s+(\d+)\s+[—–-]\s+.*\[map\].*$', re.M)


def refresh_script(script: str, block: str):
    """replace the block between the map markers in the [map] section. Returns (new_text, status) where
    status is 'same', 'changed', 'no-section' or 'no-markers'."""
    h = MAP_HEAD.search(script)
    if not h:
        return script, 'no-section'
    nxt = re.search(r'^##\s+\d+\s', script[h.end():], re.M)
    sec_end = h.end() + (nxt.start() if nxt else len(script) - h.end())
    sec = script[h.end():sec_end]
    i, j = sec.find(BEGIN), sec.find(END)
    if i < 0 or j < i:
        return script, 'no-markers'
    new_sec = sec[:i] + block + sec[j + len(END):]
    if new_sec == sec:
        return script, 'same'
    return script[:h.end()] + new_sec + script[sec_end:], 'changed'


def map_section_number(script: str):
    h = MAP_HEAD.search(script)
    return h.group(1) if h else None


# ------------------------------------------------------------------ lesson.js
def rewrite_lesson_js(src: str, les: dict, module_full: str):
    """set key/id/module of the LESSON({...}) call; nothing else changes"""
    start = src.find('LESSON(')
    if start < 0:
        return src
    head, body = src[:start], src[start:]

    def setv(body, k, v):
        rx = re.compile(r"(\b" + k + r"\s*:\s*)(['\"])(.*?)(?<!\\)\2", re.S)
        val = v.replace('\\', '\\\\').replace("'", "\\'")
        if rx.search(body):
            return rx.sub(lambda m: f"{m.group(1)}'{val}'", body, count=1)
        # add it right after LESSON({
        return re.sub(r'LESSON\(\s*\{', lambda m: m.group(0) + f"\n  {k}: '{val}',", body, count=1)
    body = setv(body, 'module', module_full)
    body = setv(body, 'id', les['id'])
    body = setv(body, 'key', les['key'])
    return head + body


# ------------------------------------------------------------------ sync
def lesson_state(c: Course, les: dict, data: dict, L: pathlib.Path):
    """per built lesson: what the map section says now vs what was narrated, and whether the map drawing changed
    since the lesson's video was rendered"""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import narrate  # noqa: E402  (no side effects; parse() is the same parser that bills ElevenLabs)
    out = {'key': les['key'], 'dir': L}
    script_p = L / 'script.md'
    script = script_p.read_text(encoding='utf-8') if script_p.exists() else ''
    out['section'] = map_section_number(script)
    out['narrated'] = None
    if out['section']:
        _, secs = narrate.parse(script)
        sec = next((s for s in secs if s['n'] == out['section']), None)
        aj = L / 'audio' / f"{out['section']}.align.json"
        if aj.exists() and sec:
            said = json.loads(aj.read_text(encoding='utf-8')).get('text', '')
            out['narrated'] = said == sec['text']
        out['map_chars'] = len(sec['text']) if sec else 0
    short = ''
    lj = L / 'lesson.js'
    if lj.exists():
        m = re.search(r"\bshort\s*:\s*(['\"])(.*?)(?<!\\)\1", lj.read_text(encoding='utf-8'), re.S)
        short = m.group(2) if m else ''
    # what the video shows that the curriculum decides: the map (mapHash), where the lesson sits on it, the card's
    # title, and the lesson ID (the badge in the corner of every scene shows it). A Start / Finish lesson's [map]
    # scene also shows the region's name and question in its note (mapHash leaves those out for everyone else)
    parts = [data['mapHash'], les['key'], les['id'], les['module'], les['district'], short or les['title']]
    r = c.region(les['district'])
    if r and r['kind'] in ('start', 'finish'):
        m = c.modules.get(les['module'])
        parts += [r['name'], r['q'], m['name'] if m else '']
    out['drawing'] = sha(parts)
    mp4s = [p for p in (L / 'out' / 'lesson.mp4', L / 'out' / 'lesson-720.mp4') if p.exists()]
    out['rendered_at'] = max((p.stat().st_mtime for p in mp4s), default=None)
    return out


def sync(c: Course, course_js=COURSE_JS, dry=False, quiet=False):
    """regenerate course.js, refresh every built new lesson, report what needs narration / a re-render"""
    data = course_data(c)
    changed_js = write_course_js(data, course_js, dry)
    say_ = (lambda *a: None) if quiet else print
    say_(f"{('would write' if dry else 'wrote') if changed_js else 'unchanged'}: {pathlib.Path(course_js)}")
    report = {'narrate': [], 'render': [], 'warnings': [], 'touched': []}
    if c.format != 'new':
        say_('old curriculum format: no lesson keys, so no built new lessons to sync (legacy lessons are never touched)')
        return data, report
    now = datetime.datetime.now().replace(microsecond=0).isoformat()
    for les in c.lessons:
        L = c.built(les)
        if not L:
            continue
        mod = c.modules[les['module']]
        # lesson.js: key, id and module from the curriculum
        lj = L / 'lesson.js'
        if lj.exists():
            src = lj.read_text(encoding='utf-8')
            new = rewrite_lesson_js(src, les, mod['full'])
            if new != src:
                report['touched'].append(f'{L.name}/lesson.js')
                if not dry:
                    lj.write_text(new, encoding='utf-8', newline='\n')
        # index.html of a new lesson loads course.js before map.js
        ix = L / 'index.html'
        if ix.exists():
            page = ix.read_text(encoding='utf-8')
            if 'engine/map.js' in page and 'engine/course.js' not in page:
                page = page.replace('<script src="../../engine/map.js"></script>',
                                    '<script src="../../engine/course.js"></script>\n<script src="../../engine/map.js"></script>')
                report['touched'].append(f'{L.name}/index.html')
                if not dry:
                    ix.write_text(page, encoding='utf-8', newline='\n')
        # the [map] section of script.md
        sp = L / 'script.md'
        if sp.exists():
            script = sp.read_text(encoding='utf-8')
            new, st = refresh_script(script, map_block(c, les))
            if st == 'changed':
                report['touched'].append(f'{L.name}/script.md')
                if not dry:
                    sp.write_text(new, encoding='utf-8', newline='\n')
            elif st in ('no-section', 'no-markers'):
                report['warnings'].append(f"{L.name}: script.md has {'no [map] section' if st == 'no-section' else 'a [map] section without the map:begin/map:end markers'}; not refreshed")
        # the map drawing this lesson's video shows: record when it last changed (dry run: judge the text sync WOULD write)
        st = lesson_state(c, les, data, L) if not dry else lesson_state_dry(c, les, data, L)
        rec_p = L / 'course-sync.json'
        rec = json.loads(rec_p.read_text(encoding='utf-8')) if rec_p.exists() else {}
        if rec.get('drawing') != st['drawing']:
            rec_new = {'key': les['key'], 'id': les['id'], 'module': les['module'], 'district': les['district'],
                       'drawing': st['drawing'], 'drawing_changed': now,
                       'note': ('written by tools/course.py sync. drawing = hash of what the curriculum decides in this '
                                "lesson's video (the map, its place on it, its card title, its ID in the badge); "
                                'a render older than drawing_changed is stale')}
            if not rec:
                rec_new['first_sync'] = now
            if not dry:
                rec_p.write_text(json.dumps(rec_new, indent=1) + '\n', encoding='utf-8', newline='\n')
            first = not rec
            rec = rec_new
        else:
            first = False
        changed_at = datetime.datetime.fromisoformat(rec['drawing_changed']).timestamp()
        if st['narrated'] is False:
            report['narrate'].append({'key': les['key'], 'id': les['id'], 'dir': L, 'section': st['section'], 'chars': st.get('map_chars', 0)})
        elif st['rendered_at'] is not None and st['rendered_at'] < changed_at and not first:
            report['render'].append({'key': les['key'], 'id': les['id'], 'dir': L})
        elif st['rendered_at'] is None and les['status'] == 'published' and not first:
            pub = c.registry().get('lessons', {}).get(les['key'], {}).get('published')
            if pub and pub < rec['drawing_changed'][:10]:
                report['render'].append({'key': les['key'], 'id': les['id'], 'dir': L, 'note': 'no local render; published before the map changed'})
    if not quiet:
        print_report(report, dry)
    return data, report


def lesson_state_dry(c, les, data, L):
    """lesson_state as if sync had already written the [map] text (for --dry-run)"""
    import shutil
    import tempfile
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='course-sync-'))
    try:
        for name in ('script.md', 'lesson.js'):
            if (L / name).exists():
                shutil.copy2(L / name, tmp / name)
        if (tmp / 'script.md').exists():
            s = (tmp / 'script.md').read_text(encoding='utf-8')
            s, _ = refresh_script(s, map_block(c, les))
            (tmp / 'script.md').write_text(s, encoding='utf-8')
        if (L / 'audio').is_dir():
            (tmp / 'audio').mkdir()
            for p in (L / 'audio').glob('*.align.json'):
                shutil.copy2(p, tmp / 'audio' / p.name)
        if (L / 'out').is_dir():
            (tmp / 'out').mkdir()
            for n in ('lesson.mp4', 'lesson-720.mp4'):
                if (L / 'out' / n).exists():
                    (tmp / 'out' / n).write_bytes(b'')
                    os.utime(tmp / 'out' / n, ((L / 'out' / n).stat().st_mtime,) * 2)
        st = lesson_state(c, les, data, tmp)
        st['dir'] = L
        return st
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def commands_for(report):
    """(key, [argv, ...]) per lesson. Every argv names the lesson by its FOLDER (the one sync looked at), never by
    key, so a test run on fixture lessons can never narrate or render the real lesson with the same key."""
    def tool(name, d):
        return [sys.executable, str(ROOT / 'tools' / name), str(pathlib.Path(d).resolve())]
    cmds = []
    for x in report['narrate']:
        cmds.append((x['key'], [tool('narrate.py', x['dir']), tool('mix.py', x['dir']), tool('render.py', x['dir'])]))
    for x in report['render']:
        cmds.append((x['key'], [tool('render.py', x['dir'])]))
    return cmds


def show_cmd(argv):
    """an argv from commands_for as a command to paste: tools by relative path, a real lesson by its key,
    any other folder quoted (the course path has spaces)"""
    tool_ = pathlib.Path(argv[1]).name
    d = pathlib.Path(argv[2])
    try:
        arg = d.name if d.parent.resolve() == LESSONS.resolve() else f'"{d}"'
    except OSError:
        arg = f'"{d}"'
    return f'python tools/{tool_} {arg}' + (' ' + ' '.join(argv[3:]) if len(argv) > 3 else '')


def freshness(c: Course, les: dict, data=None):
    """why a built new lesson's video or narration no longer matches the curriculum, or None when it does.
    publish.py refuses to publish a stale lesson: its page on the site carries its own copy of the course data
    (lessons/<key>/course.js) and must show the map its narration and MP4 were made with."""
    L = c.built(les)
    if not L:
        return f"lessons/{les['key']}/ does not exist"
    data = data or course_data(c)
    sp = L / 'script.md'
    if sp.exists() and refresh_script(sp.read_text(encoding='utf-8'), map_block(c, les))[1] == 'changed':
        return 'its [map] section is out of date: run python tools/course.py sync'
    st = lesson_state(c, les, data, L)
    rec_p = L / 'course-sync.json'
    rec = json.loads(rec_p.read_text(encoding='utf-8')) if rec_p.exists() else {}
    if rec.get('drawing') != st['drawing']:
        return 'the curriculum changed since the last sync: run python tools/course.py sync'
    if st['narrated'] is False:
        return f"section {st['section']} (the [map] section) changed since it was narrated: python tools/course.py remap --render"
    changed_at = datetime.datetime.fromisoformat(rec['drawing_changed']).timestamp()
    if st['rendered_at'] is not None and st['rendered_at'] < changed_at and rec.get('first_sync') != rec.get('drawing_changed'):
        return f"its video was rendered before the map changed ({rec['drawing_changed']}): python tools/render.py {les['key']}"
    return None


def print_report(report, dry=False):
    for t in report['touched']:
        print(f"{'would update' if dry else 'updated'}: lessons/{t}")
    for w in report['warnings']:
        print(f'warning: {w}')
    if report['narrate']:
        chars = sum(x['chars'] for x in report['narrate'])
        print(f"NEEDS NARRATION (the map text changed; about {chars:,} ElevenLabs characters for the [map] sections only):")
        for x in report['narrate']:
            print(f"  {x['id']} {x['key']} (section {x['section']})")
    if report['render']:
        print('NEEDS A RE-RENDER ONLY (the map drawing changed):')
        for x in report['render']:
            print(f"  {x['id']} {x['key']}" + (f"  ({x['note']})" if x.get('note') else ''))
    if not report['narrate'] and not report['render']:
        print('every built new lesson is up to date with the map')
        return
    print('commands (or: python tools/course.py remap --render):')
    for k, cmds in commands_for(report):
        for cmd in cmds:
            print('  ' + show_cmd(cmd))
    print('then republish what is live: python tools/publish.py --all (or publish.py <key> per lesson); '
          'publish.py refuses a lesson that still needs narration or a re-render')


def remap(c: Course, render=False, dry=False, course_js=COURSE_JS):
    data, report = sync(c, course_js, dry=dry)
    todo = commands_for(report)
    if not todo:
        return 0
    print(('DRY RUN: would run' if dry else 'running') + ':')
    for k, cmds in todo:
        for cmd in cmds:
            shown = show_cmd(cmd)
            if pathlib.Path(cmd[1]).name == 'render.py' and not render:
                print(f'  (skipped without --render) {shown}')
                continue
            print(f'  {shown}')
            if not dry:
                r = subprocess.run(cmd, cwd=str(ROOT))
                if r.returncode:
                    print(f'FAILED: {shown} (exit {r.returncode}); stopping')
                    return r.returncode
    return 0


# ------------------------------------------------------------------ renumber
def cell_spans(line: str):
    """(start, end) of every cell's text in a markdown table row, the same cells split_row() returns"""
    spans, i, n = [], 0, len(line)
    while i < n and line[i] in ' \t':
        i += 1
    if i < n and line[i] == '|':
        i += 1
    start, code = i, False
    while i < n:
        ch = line[i]
        if ch == '\\' and i + 1 < n and line[i + 1] == '|':
            i += 2
            continue
        if ch == '`':
            code = not code
        if ch == '|' and not code:
            spans.append((start, i))
            start = i + 1
        i += 1
    if line[start:].strip():
        spans.append((start, n))
    return spans


def renumber_plan(c: Course):
    """what renumber would write: {path: (old_text, new_text)} plus a list of notes"""
    notes = []
    lines = c.path.read_text(encoding='utf-8').split('\n')
    edits = {}                                   # line number (1-based) -> new line

    def put(no, new):
        if lines[no - 1] != new:
            edits[no] = new
    # districts 1..N in file order
    for i, r in enumerate([r for r in c.regions if r['kind'] == 'district'], 1):
        if r['n'] != i:
            put(r['line'], re.sub(r'District\s+\d+', f'District {i}', lines[r['line'] - 1], count=1))
    # modules 00.. in file order (every heading, duplicates included)
    new_mod = {}
    for i, m in enumerate(c.module_heads):
        nn = f'{i:02d}'
        new_mod[m['line']] = nn
        if m['n'] != nn:
            put(m['line'], re.sub(r'^(##\s+Module\s+)(\d+)', lambda x: x.group(1) + nn, lines[m['line'] - 1], count=1))
    # lesson IDs 01, 02... in each module, in file order
    old_to_key, dup, new_id = {}, set(), {}
    for les in c.lessons:
        if les['id'] in old_to_key:
            dup.add(les['id'])
        old_to_key[les['id']] = les['key']
    count = {}
    for les in c.lessons:
        mod = new_mod.get(les['module_line'], les['module'])
        count[les['module_line']] = count.get(les['module_line'], 0) + 1
        nid = f"{mod}.{count[les['module_line']]:02d}"
        new_id[les['key']] = nid
        if les['id'] != nid:
            put(les['line'], re.sub(r'^(\s*\|\s*)(\d{2}\.\d{2}[a-z]?)', lambda x: x.group(1) + nid, lines[les['line'] - 1], count=1))

    def to_key(m):
        t = m.group(0)
        if t in dup:
            notes.append(f'{t} names two lessons; left as it is: replace it with the key you mean')
            return t
        return old_to_key.get(t, t)
    # the Lantern line and Legacy Covers name lessons by key: convert any ID (before renumbering) to its key
    for no, line in enumerate(lines, 1):
        if re.match(r'^Lantern lessons:', line):
            put(no, re.sub(r'(?<![\w.])\d{2}\.\d{2}[a-z]?(?![\w.])', to_key, edits.get(no, line)))
    for lg in c.legacy:
        if lg.get('derived') or not lg.get('line'):
            continue
        line = edits.get(lg['line'], lines[lg['line'] - 1])
        sp = cell_spans(line)
        col = lg.get('covers_col', 2)
        if col < len(sp):
            a, b = sp[col]
            put(lg['line'], line[:a] + re.sub(r'(?<![\w.])\d{2}\.\d{2}[a-z]?(?![\w.])', to_key, line[a:b]) + line[b:])
    out = {}
    if edits:
        new_lines = [edits.get(i + 1, ln) for i, ln in enumerate(lines)]
        out[c.path] = ('\n'.join(lines), '\n'.join(new_lines))
    # spec front matter: id, module and district follow curriculum.md
    for les in c.lessons:
        p = c.spec_path(les)
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8')
        fm = re.match(r'^﻿?---\s*\n(.*?)\n---\s*(?:\n|$)', text, re.S)
        if not fm:
            continue
        mod_n = new_id[les['key']][:2]
        m = c.modules.get(les['module'])
        want = {'id': new_id[les['key']], 'module': f"{mod_n} {m['full']}" if m else None, 'district': spec_district(c, les)}
        body = fm.group(1)

        def fix(mm):
            k, v = mm.group(1), mm.group(3)
            w = want.get(k)
            if w is None or plain(str(_scalar(v))) == w:
                return mm.group(0)
            return f'{mm.group(1)}{mm.group(2)}{w}'
        new_body = re.sub(r'^(id|module|district)(\s*:\s*)(.*)$', fix, body, flags=re.M)
        if new_body != body:
            out[p] = (text, text[:fm.start(1)] + new_body + text[fm.end(1):])
    return out, sorted(set(notes))


def renumber(c: Course, write=False):
    """renumber lesson IDs (01, 02... per module), modules (00.. in file order) and districts (1..N) in curriculum.md,
    turn IDs in the Lantern line and the Legacy Covers into keys, and bring the spec files' id / module / district
    front matter in step. Prints a diff; --write applies it."""
    import difflib
    if c.format != 'new':
        print('renumber needs the new curriculum format (lesson keys): in the old format a lesson is named by its ID '
              '(the Lantern line, the legacy lessons in course.json), so renumbering would re-point those silently', file=sys.stderr)
        return 2
    plan, notes = renumber_plan(c)
    for p, (old, new) in plan.items():
        sys.stdout.writelines(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True),
                                                   fromfile=f'a/{rel(p)}', tofile=f'b/{rel(p)}', n=0))
        if not new.endswith('\n') and not old.endswith('\n'):
            print()
    for n in notes:
        print('note:', n)
    if not plan:
        print('already numbered in file order: nothing to change')
        return 0
    if not write:
        print(f'\nDRY RUN: {len(plan)} file(s) would change; run python tools/course.py renumber --write to apply')
        return 0
    for p, (_, new) in plan.items():
        pathlib.Path(p).write_text(new, encoding='utf-8', newline='\n')
    print(f'\nwrote {len(plan)} file(s). Next: python tools/course.py check, then python tools/course.py sync')
    return 0


# ------------------------------------------------------------------ check
def check(c: Course, browser=True, quiet=False):
    errors, warnings = [], []
    E, W = errors.append, warnings.append
    for lvl, msg in c.problems:
        (E if lvl == 'error' else W)(msg)
    if not c.lessons:
        E('no lesson rows found')
    # regions
    kinds = [r['kind'] for r in c.regions]
    if not kinds or kinds[0] != 'start':
        E('the first region must be "# Start · <name> — <question>"')
    if not kinds or kinds[-1] != 'finish':
        E('the last region must be "# Finish · <name> — <question>"')
    if kinds.count('start') > 1 or kinds.count('finish') > 1:
        E('one Start and one Finish only')
    dists = [r for r in c.regions if r['kind'] == 'district']
    lo, hi = MAP_LIMITS['districts']
    if not lo <= len(dists) <= hi:
        E(f'{len(dists)} districts: the map lays out {lo} to {hi}')
    for i, r in enumerate(dists, 1):
        if r['n'] != i:
            E(f"line {r['line']}: District {r['n']} should be District {i} (districts are numbered in order; "
              f"python tools/course.py renumber --write fixes the numbers)")
        if len(r['mods']) > MAP_LIMITS['modules']:
            E(f"district {r['name']} has {len(r['mods'])} modules: the map fits {MAP_LIMITS['modules']} per district")
    for r in c.regions:
        if not r['mods']:
            E(f"{r['kind']} {r['name']} has no modules")
        elif r['kind'] in ('start', 'finish') and len(r['mods']) != 1:
            E(f"the {r['kind']} must hold exactly one module (the map draws one circle with one number); "
              f"it holds {' '.join(r['mods'])}: move the others into a district")
    ids_r = [r['id'] for r in c.regions]
    for x in sorted(set(i for i in ids_r if ids_r.count(i) > 1)):
        E(f'two regions share the id {x} (rename one)')
    # modules contiguous and in order
    ns = list(c.modules)
    want = [f'{i:02d}' for i in range(len(ns))]
    if ns != want:
        E(f"modules must be numbered 00, 01, ... in file order; found {' '.join(ns)} "
          f"(python tools/course.py renumber --write fixes the numbers)")
    # lessons: unique keys, contiguous ids
    keys = {}
    for les in c.lessons:
        k = les['key']
        if not KEY_RE.match(k) or len(k) > 40:
            E(f"line {les['line']}: key {k!r} must be kebab-case, at most 40 characters")
        if re.match(r'^\d{2}-\d{2}', k) or k.startswith(('poc-', '_')):
            E(f"line {les['line']}: key {k!r} looks like a legacy slug / test folder; keys carry no numbers in front")
        keys.setdefault(k, []).append(les)
    by_mod = {}
    for les in c.lessons:
        by_mod.setdefault(les['module'], []).append(les)
    for n, rows in by_mod.items():
        for i, les in enumerate(rows, 1):
            m = ID_RE.match(les['id'])
            if m.group(1) != n or int(m.group(2)) != i or m.group(3):
                E(f"line {les['line']}: {les['id']} should be {n}.{i:02d} (IDs run 01, 02, ... in each module, in file order; "
                  f"python tools/course.py renumber --write fixes them)")
                break
    for n in c.modules:
        if n not in by_mod:
            W(f'module {n} has no lessons yet')
    ids = [les['id'] for les in c.lessons]
    for x in sorted(set(i for i in ids if ids.count(i) > 1)):
        E(f'lesson id {x} appears twice')
    statuses = {'todo', 'published', 'legacy', 'scripted', 'narrated', 'animated'}
    for les in c.lessons:
        if les['status'] not in statuses:
            E(f"line {les['line']}: unknown status {les['status']!r}")

    def by_key(t, where):
        """the new format names lessons by key only: an ID in the Lantern line or a Covers cell would silently
        point at a different lesson as soon as lessons move"""
        les = c.lesson(t)
        if c.format == 'new' and ID_RE.match(t):
            E(f"{where}: {t} is a lesson ID; use the lesson key ({les['key'] if les else 'the key of the lesson you mean'}): "
              f"IDs change when lessons move (python tools/course.py renumber --write converts them)")
            return False
        if not les:
            E(f'{where}: {t} is not a lesson in curriculum.md')
            return False
        return True
    # lanterns
    for t in c.lanterns:
        by_key(t, 'Lantern lessons')
    # legacy
    slugs = [lg['slug'] for lg in c.legacy]
    reg = c.registry().get('lessons', {})
    for lg in c.legacy:
        if not (LESSONS / lg['slug']).is_dir():      # legacy lessons always live in the real lessons/ folder
            E(f"legacy lesson {lg['slug']} has no folder in lessons/")
        if not lg.get('derived') and not reg.get(lg['slug'], {}).get('legacy'):
            E(f"{lg['slug']} is not a legacy lesson in course.json (no \"legacy\": true entry); "
              f"only the lessons published before 2026-10-12 belong in the Legacy lessons table")
        for t in lg['covers']:
            by_key(t, f"legacy lesson {lg['slug']} (Covers)")
        if not lg['covers'] and not lg.get('derived'):
            W(f"legacy lesson {lg['slug']} covers no lesson slot; the course page lists it in module {lg['id'][:2] or '00'}")
        if keys.get(lg['slug']):
            E(f"legacy slug {lg['slug']} is also a lesson key")
    for x in sorted(set(s for s in slugs if slugs.count(s) > 1)):
        E(f'legacy lesson {x} is listed twice')
    for les in c.lessons:
        if les['status'] == 'legacy' and not les['legacy']:
            E(f"line {les['line']}: {les['id']} has status legacy but no legacy lesson covers it")
    if c.format == 'new':
        listed = set(slugs)
        for slug, meta in reg.items():
            if meta.get('legacy') and slug not in listed:
                E(f'course.json marks {slug} legacy, but the Legacy lessons table does not list it')
    # retired keys are never used again (a key is a folder and a public URL)
    retired = c.retired_keys()
    for r in c.retired:
        if not KEY_RE.match(r['key']):
            E(f"line {r['line']}: retired key {r['key']!r} is not a key")
    for les in c.lessons:
        if les['key'] in retired:
            E(f"line {les['line']}: key {les['key']} is retired (## Retired keys); a dropped key is never reused: pick a new key")
    # what is published vs what curriculum.md says (the daily job's `next` trusts the status column)
    pub_reg = published_in_registry(c)
    for les in c.lessons:
        hit = pub_reg.get(les['key']) or (pub_reg.get(('id', les['id'])) if c.format == 'old' else None)
        if les['status'] == 'todo' and hit:
            W(f"line {les['line']}: {les['id']} {les['key']} is `todo` but course.json lists it as published ({hit}); "
              f"set its status to published (`next` skips it either way)")
        if les['status'] == 'published' and not hit and not les['legacy']:
            W(f"line {les['line']}: {les['id']} {les['key']} is `published` but course.json has no entry for it "
              f"(python tools/publish.py {les['key']} registers it)")
    # orphans: what a deleted / combined lesson leaves behind
    if c.format == 'new':
        rows = {les['key'] for les in c.lessons}
        ldir = pathlib.Path(c.lessons_dir)
        if ldir.is_dir():
            for d in sorted(ldir.iterdir()):
                if (d / 'course-sync.json').exists() and d.name not in rows:
                    W(f"lessons/{d.name}/ was built from curriculum.md but has no row any more: archive the folder "
                      f"(Courses/_old-takes/){'; it is published: python tools/publish.py --remove ' + d.name if d.name in reg else ''}"
                      f"{'' if d.name in retired else '; and list ' + d.name + ' under ## Retired keys'}")
        spec_dir = c.base / 'curriculum' / 'lessons'
        linked = {c.spec_path(les).resolve() for les in c.lessons}
        if spec_dir.is_dir():
            for p in sorted(spec_dir.glob('*.md')):
                if p.resolve() not in linked:
                    W(f'{rel(p)} has no row in curriculum.md: delete it or merge it into the lesson that took its material')
        for slug, meta in reg.items():
            if not meta.get('legacy') and not meta.get('poc') and slug not in rows:
                W(f'course.json lists {slug} (published {meta.get("published")}), which has no row in curriculum.md: '
                  f'python tools/publish.py --remove {slug} takes its page off the site'
                  + ('' if slug in retired else f'; list {slug} under ## Retired keys'))
    # map references in the scenes of built new lessons: a renamed district or module must not leave a scene
    # pinning or focusing on a name the map no longer knows
    scene_refs = scene_map_refs(c)
    # spec files and S-/C-IDs
    src_ids = defined_ids(c.base / 'curriculum' / 'sources.md', 'S')
    con_ids = defined_ids(c.base / 'curriculum' / 'concepts.md', 'C')
    for les in c.lessons:
        cited_s, cited_c = list(les['sources']), list(les['concepts'])
        if c.format == 'new':
            p = c.spec_path(les)
            if not p.exists():
                E(f"line {les['line']}: spec file {rel(p)} is missing")
            else:
                fm, _ = front_matter(p.read_text(encoding='utf-8'))
                if not fm:
                    E(f'{rel(p)}: no front matter')
                else:
                    if str(fm.get('key', '')) != les['key']:
                        E(f"{rel(p)}: key is {fm.get('key')!r}, curriculum.md says {les['key']!r}")
                    for f_, want_v in (('id', les['id']), ('status', les['status'])):
                        if f_ in fm and str(fm[f_]) != want_v:
                            W(f"{rel(p)}: {f_} is {fm[f_]!r}, curriculum.md says {want_v!r} (curriculum.md wins)")
                    if 'title' in fm and plain(str(fm['title'])) != les['title']:
                        W(f"{rel(p)}: title is {fm['title']!r}, curriculum.md says {les['title']!r}")
                    for f_, ok, want_v in (('module', spec_module_ok, spec_module(c, les)), ('district', spec_district_ok, spec_district(c, les))):
                        if f_ in fm and not ok(c, les, fm[f_]):
                            W(f"{rel(p)}: {f_} is {fm[f_]!r}, curriculum.md says {want_v!r} (curriculum.md wins; "
                              f"python tools/course.py renumber --write rewrites it)")
                    for s in as_list(fm.get('legacy')):
                        if s not in slugs:
                            E(f"{rel(p)}: legacy {s} is not in the Legacy lessons table")
                    cited_s += [str(x) for x in as_list(fm.get('sources'))]
                    cited_c += [str(x) for x in as_list(fm.get('concepts'))]
        if src_ids is not None:
            for s in sorted(set(cited_s) - src_ids):
                E(f"{les['id']} {les['key']}: cites {s}, which curriculum/sources.md does not define")
        if con_ids is not None:
            for s in sorted(set(cited_c) - con_ids):
                E(f"{les['id']} {les['key']}: cites {s}, which curriculum/concepts.md does not define")
    for b in c.backlog:
        if src_ids is not None:
            for s in sorted(set(b['sources']) - src_ids):
                E(f"backlog {b['topic']}: cites {s}, which curriculum/sources.md does not define")
        if con_ids is not None:
            for s in sorted(set(b['concepts']) - con_ids):
                E(f"backlog {b['topic']}: cites {s}, which curriculum/concepts.md does not define")
    # map narration round trip through narrate.py's caption conversion: a viewer must see the written form
    cap_problems = caption_roundtrip(c)
    for p in cap_problems:
        E(p)
    # the map itself: lay it out in a browser (the real map.js, real fonts) and audit it
    audit = None
    data = course_data(c)
    if browser:
        try:
            audit = browser_audit(data, sorted({r for _, r in scene_refs}))
        except Exception as exc:  # no Playwright / no network: fall back to a length heuristic
            W(f'map layout not checked in a browser ({type(exc).__name__}: {str(exc)[:160]}); using a length estimate')
    if audit:
        for e in audit['errors']:
            E('map: ' + e)
        for w in audit['warnings']:
            W('map: ' + w)
    else:
        for m in c.modules.values():
            if len(m['name']) > 26:
                W(f"map: module {m['n']} label {m['name']!r} is long ({len(m['name'])} characters); it may wrap. "
                  f"Give it a short label: ## Module {m['n']} — {m['full']} <!-- map: Short name -->")
    unresolved = set(audit['unresolved']) if audit and 'unresolved' in audit else {r for _, r in scene_refs if not resolves(c, r)}
    for where, r in scene_refs:
        if r in unresolved:
            E(f"{where}: the map has no {r!r} (a district, module, lesson or Start / Finish name); a renamed district or "
              f"module breaks this pin / focus / highlight. Name it as the curriculum does now, or use 'lesson'")
        elif re.fullmatch(r'\d{1,2}', r) or ID_RE.match(r):
            W(f"{where}: {r!r} is a number, which moves when modules or lessons are renumbered; name the module, "
              f"district or lesson key instead (or 'lesson')")
    if not quiet:
        print(f'{rel(c.path)}: {c.format} format, {len(c.regions)} regions ({len(dists)} districts), {len(c.modules)} modules, '
              f"{len(c.lessons)} lessons ({sum(1 for x in c.lessons if x['status'] == 'todo')} todo, "
              f"{sum(1 for x in c.lessons if x['status'] == 'published')} published, {sum(1 for x in c.lessons if x['status'] == 'legacy')} legacy), "
              f'{len(c.lanterns)} lantern lessons, {len(c.legacy)} legacy lessons')
        if audit:
            lay = audit.get('summary', {})
            print(f"map layout: {lay.get('rows')} cards per row, card widths {lay.get('widths')}, rows y {lay.get('rowsY')}, "
                  f"{'compact rhythm' if lay.get('compact') else 'standard rhythm'}, {len(audit.get('wrapped', []))} wrapped labels")
        for w in warnings:
            print('warning:', w)
        for e in errors:
            print('ERROR:', e)
        print('OK' if not errors else f'{len(errors)} ERRORS')
    return errors, warnings, audit


def as_list(v):
    if v is None or v == '':
        return []
    return v if isinstance(v, list) else [v]


def published_in_registry(c: Course):
    """course.json's published new lessons: key -> published date (old format: ('id', id) -> date as well)"""
    out = {}
    for slug, meta in c.registry().get('lessons', {}).items():
        if meta.get('legacy') or meta.get('poc'):
            continue
        out[slug] = meta.get('published') or 'registered'
        if meta.get('id'):
            out[('id', meta['id'])] = out[slug]
    return out


# spec front matter: `module: 09 APIs, Webhooks & MCP` and `district: The Network` (what renumber writes)
def spec_module(c, les):
    m = c.modules.get(les['module'])
    return f"{m['n']} {m['full']}" if m else les['module']


def spec_district(c, les):
    r = c.region(les['district'])
    return r['name'] if r else les['district']


def spec_module_ok(c, les, v):
    m = c.modules.get(les['module'])
    v = plain(str(v)).strip().lower()
    if not m:
        return True
    names = {m['full'].lower(), m['name'].lower()}
    mm = re.match(r'^(\d{1,2})(?:\s+(.*))?$', v)
    if mm:
        return mm.group(1).zfill(2) == m['n'] and (not mm.group(2) or mm.group(2).strip() in names)
    return v in names


def spec_district_ok(c, les, v):
    r = c.region(les['district'])
    if not r:
        return True
    v = re.sub(r'^(start|finish|district\s+\d+)\s*[·•:|-]\s*', '', plain(str(v)).strip().lower())
    return v in (r['name'].lower(), r['id'].lower())


SCENE_REF_RES = [
    re.compile(r'\b(?:focus|pin|highlight)\s*:\s*([\'"])(.*?)(?<!\\)\1'),
    re.compile(r'K\.map\.(?:chipPos|district|districtOf|resolve|pinAt|lesson)\(\s*([\'"])(.*?)(?<!\\)\1'),
]
SCENE_LIST_RE = re.compile(r'\bhighlight\s*:\s*[\[{]([^\]}]*)[\]}]')


def scene_map_refs(c: Course):
    """[(where, ref)]: the string literals the scenes of every built new lesson hand to the map (pin, focus,
    highlight, K.map.chipPos('...'), ...). check resolves each against the current curriculum, so renaming a
    district or module cannot silently break a scene. Template strings and variables are not followed."""
    out = []
    if c.format != 'new':
        return out
    for les in c.lessons:
        L = c.built(les)
        if not L:
            continue
        files = sorted((L / 'scenes').glob('*.js')) if (L / 'scenes').is_dir() else []
        if (L / 'lesson.js').exists():
            files.append(L / 'lesson.js')
        for f in files:
            src = f.read_text(encoding='utf-8')
            found = []
            for rx in SCENE_REF_RES:
                found += [m.group(2) for m in rx.finditer(src)]
            for m in SCENE_LIST_RE.finditer(src):
                found += [x.group(2) for x in re.finditer(r'([\'"])(.*?)(?<!\\)\1', m.group(1))]
            for ref in found:
                if ref and not ref.startswith(('${', '#')):
                    out.append((f'lessons/{L.name}/{f.relative_to(L).as_posix()}', ref))
    return out


def resolves(c: Course, x) -> bool:
    """map.js resolve() in Python (used when no browser is available): does the map know this name?"""
    s = str(x).strip()
    if not s:
        return False
    if re.fullmatch(r'\d', s):
        s = '0' + s
    low = s.lower()
    bare = re.sub(r'^the\s+', '', low)
    if low in ('lesson', 'ai', 'lanterns', 'the lanterns', 'gate', 'start', 'end', 'finish') or s in c.modules:
        return True
    for r in c.regions:
        if s == r['id'] or low == r['id'] or bare == re.sub(r'^the\s+', '', r['name'].lower()):
            return True
    if any(low in (m['name'].lower(), m['full'].lower()) for m in c.modules.values()):
        return True
    return c.lesson(s) is not None


def defined_ids(path: pathlib.Path, letter):
    if not path.exists():
        return None
    return set(re.findall(r'\b' + letter + r'\d+\b', path.read_text(encoding='utf-8')))


def rel(p):
    try:
        return pathlib.Path(p).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(p)


def caption_roundtrip(c: Course):
    """the generated map narration, run through narrate.py's caption conversion: every spoken acronym must
    come back as its written form on screen"""
    import narrate  # noqa: E402
    problems, seen = [], set()
    for les in c.lessons:
        sig = (les['district'], les['module'])
        if sig in seen:
            continue
        seen.add(sig)
        text, pairs = map_narration(c, les)
        if not text:
            continue
        spoken = narrate.CUE.sub(' ', text)
        words = [[w, i * 0.4, i * 0.4 + 0.3] for i, w in enumerate(spoken.split())]
        over = narrate.caption_map('<!-- captions: ' + '; '.join(pairs) + ' -->') if pairs else []
        shown = ' '.join(w[0] for w in narrate.caption_words(words, over))
        r, m = c.region(les['district']), c.modules[les['module']]
        src = plain(' . '.join((r['name'], r['q'], m['name'])))
        # every acronym (API, YAML, PATH...) and every slashed token with one in it (CI/CD, HTTP/2) must be shown
        # on screen exactly as written
        for written in re.findall(r'(?<![\w/])[\w.]+(?:/[\w.]+)+(?![\w/])|(?<![\w/])[A-Z]{2,6}s?(?![\w/])', src):
            if '/' in written and not any(re.fullmatch(r'[A-Z]{2,6}s?', p) or p in SAID_AS_WORDS for p in written.split('/')):
                continue
            if not re.search(r'(?<![\w/])' + re.escape(written) + r'(?![\w/])', shown):
                problems.append(f"map narration for module {m['n']}: {written} does not come back in the captions ({shown!r}); "
                                f"add it to SAID_AS_WORDS in tools/course.py, or give the module a <!-- map: ... --> label")
    return problems


# ------------------------------------------------------------------ the map in a real browser
HARNESS = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@500;700&family=Karla:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
</head><body style="margin:0;background:#101220"><canvas id="c" width="1920" height="1080"></canvas></body></html>"""


def _harness(page, data):
    page.set_content(HARNESS)
    page.add_script_tag(path=str(ENGINE / 'kit.js'))
    page.add_script_tag(content='window.COURSE = ' + json.dumps(data) + ';')
    page.add_script_tag(path=str(ENGINE / 'map.js'))
    page.evaluate('async () => { await K.fontsReady(); K.use(document.getElementById("c").getContext("2d")); }')


def browser_audit(data, refs=()):
    """K.map.audit() on this course data, plus which of `refs` (names scenes hand to the map) K.map.resolve() cannot place"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={'width': 1920, 'height': 1080})
        _harness(page, data)
        out = page.evaluate('(refs) => ({ ...K.map.audit(), unresolved: refs.filter((r) => !K.map.resolve(r)) })', list(refs))
        b.close()
    return out


def render_png(data, out, pin=None):
    import base64
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={'width': 1920, 'height': 1080})
        _harness(page, data)
        url = page.evaluate("""(pin) => { const c = document.getElementById('c'); K.use(c.getContext('2d'));
            K.bg(); const o = pin ? { pin, focus: pin } : {}; K.map.draw(10, o); return c.toDataURL('image/png'); }""", pin)
        b.close()
    pathlib.Path(out).write_bytes(base64.b64decode(url.split(',', 1)[1]))


# ------------------------------------------------------------------ JSON views
def lesson_json(c: Course, les: dict, with_body=False):
    r, m = c.region(les['district']), c.modules.get(les['module'])
    fm, body = c.spec(les)
    p = c.spec_path(les)
    out = {'id': les['id'], 'key': les['key'], 'title': les['title'], 'idea': les['idea'], 'status': les['status'],
           'module': les['module'], 'moduleName': m['full'] if m else None, 'moduleLabel': m['name'] if m else None,
           'district': r['name'] if r else None, 'districtId': les['district'], 'districtKind': r['kind'] if r else None,
           'question': r['q'] if r else None, 'lantern': les['lantern'], 'legacy': les['legacy'],
           'minutes': (fm or {}).get('minutes'), 'spec': rel(p) if p.exists() else None,
           'sources': sorted(set(les['sources']) | set(str(x) for x in as_list((fm or {}).get('sources')))),
           # the 2-5 sources the lesson is built on (its curriculum.md row) and the spec's lead sources (title card);
           # 'sources' above also has every source the spec cites for a single point
           'rowSources': list(les['sources']), 'lead': [str(x) for x in as_list((fm or {}).get('lead'))],
           'concepts': sorted(set(les['concepts']) | set(str(x) for x in as_list((fm or {}).get('concepts')))),
           'folder': f"lessons/{les['key']}" if c.format == 'new' else None,
           'built': bool(c.built(les)) if c.format == 'new' else False}
    if with_body:
        out['specFields'] = fm or {}
        out['specBody'] = body.strip() if fm else None
    return out


def print_map(c: Course):
    for r in c.regions:
        head = {'start': 'Start', 'finish': 'Finish'}.get(r['kind'], f"District {r['n']}")
        print(f"{head} · {r['name']} — {r['q']}   [{r['id']}]")
        for n in r['mods']:
            m = c.modules[n]
            rows = [x for x in c.lessons if x['module'] == n]
            lan = sum(1 for x in rows if x['lantern'])
            st = {s: sum(1 for x in rows if x['status'] == s) for s in ('published', 'legacy', 'todo')}
            label = m['name'] + ('' if m['name'] == m['full'] else f'   ({m["full"]})')
            print(f"   {n}  {label}: {len(rows)} lessons" + ''.join(f', {v} {k}' for k, v in st.items() if v) + (f', {lan} lantern' if lan else ''))
    print(f'The Lanterns · AI (not a district): {len(c.lanterns)} lessons')
    if c.legacy:
        print('Legacy lessons:')
        for lg in c.legacy:
            print(f"   {lg['slug']}  covers {', '.join(lg['covers']) or '-'}")


# ------------------------------------------------------------------ CLI
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('command', choices=['check', 'renumber', 'sync', 'remap', 'next', 'lesson', 'map'])
    ap.add_argument('ref', nargs='?', help='lesson key or id (for "lesson")')
    ap.add_argument('--curriculum', default=str(CURRICULUM))
    ap.add_argument('--lessons', help='built lessons folder (default lessons/)')
    ap.add_argument('--registry', help='course.json to read (default course.json)')
    ap.add_argument('--course-js', default=str(COURSE_JS))
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--render', action='store_true')
    ap.add_argument('--write', action='store_true', help='renumber: apply the changes (default: print the diff only)')
    ap.add_argument('--no-browser', action='store_true', help='check: skip the in-browser map layout audit')
    ap.add_argument('--png', help='map: render the map to this PNG')
    ap.add_argument('--pin', help='map --png: pin this module / lesson')
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    fixture = pathlib.Path(a.curriculum).resolve() != CURRICULUM.resolve()
    if fixture and a.command in ('sync', 'remap') and a.course_js == str(COURSE_JS):
        print('with --curriculum <fixture>, sync and remap need --course-js <file> too, so a test never overwrites '
              'engine/course.js', file=sys.stderr)
        return 2
    if fixture and a.command == 'remap' and not a.dry_run and not a.lessons:
        print('remap with --curriculum <fixture> runs narrate.py / mix.py / render.py, which spend ElevenLabs characters '
              'and write lesson folders: pass --lessons <dir> (the fixture lessons) or --dry-run', file=sys.stderr)
        return 2
    # a fixture curriculum never touches the real lessons: no lesson folder counts as built unless --lessons says where
    c = load(a.curriculum, a.lessons or (None if not fixture else pathlib.Path(a.curriculum).resolve().parent / 'no-lessons'), a.registry)
    if a.command == 'check':
        errors, _, _ = check(c, browser=not a.no_browser)
        return 1 if errors else 0
    if a.command == 'renumber':
        return renumber(c, write=a.write)
    if a.command == 'sync':
        sync(c, a.course_js, dry=a.dry_run)
        return 0
    if a.command == 'remap':
        return remap(c, render=a.render, dry=a.dry_run, course_js=a.course_js)
    if a.command == 'next':
        # the status column is set by hand after publishing; a lesson course.json already lists as published is
        # never handed out again, even when that step was missed (check warns about it)
        pub = published_in_registry(c)
        les = next((x for x in c.lessons if x['status'] == 'todo' and x['key'] not in pub
                    and not (c.format == 'old' and ('id', x['id']) in pub)), None)
        print(json.dumps(lesson_json(c, les) if les else None, indent=1, ensure_ascii=False))
        return 0 if les else 1
    if a.command == 'lesson':
        les = c.lesson(a.ref or '')
        if not les:
            print(f'no lesson {a.ref!r} in {rel(c.path)}', file=sys.stderr)
            return 1
        print(json.dumps(lesson_json(c, les, with_body=True), indent=1, ensure_ascii=False))
        return 0
    if a.command == 'map':
        if a.png:
            pin = a.pin
            if pin and c.lesson(pin):
                pin = c.lesson(pin)['module']
            render_png(course_data(c), a.png, pin)
            print(a.png)
        else:
            print_map(c)
        return 0


if __name__ == '__main__':
    sys.exit(main())
