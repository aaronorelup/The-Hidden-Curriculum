# Course data: from curriculum.md to every lesson's map

Since 2026-10-12 the course order and the course map are data. `curriculum.md` says what the course is; everything
else is generated from it, so restructuring the course is an edit to one file plus a few commands. This page explains
how the pieces fit together and how to combine, split, add, delete, reorder and rename lessons, modules and districts.

```
curriculum.md + curriculum/lessons/<key>.md       the source (people and the research workflow edit these)
        │
        ├── python tools/course.py renumber --write  IDs, module and district numbers back in file order
        ├── python tools/course.py check           is it consistent? does the map fit? anything left behind?
        ├── python tools/course.py sync            writes ↓
        │       engine/course.js                   window.COURSE: districts, modules, lessons, lanterns
        │       lessons/<key>/lesson.js            key / id / module of every built new lesson
        │       lessons/<key>/script.md            the generated [map] section (section 02)
        │       lessons/<key>/course-sync.json     what the lesson's map looked like at the last sync
        ├── python tools/course.py remap           re-narrates / re-renders the lessons sync flagged
        └── python tools/publish.py                the course page data and the lesson pages on the site
                                                   (each new lesson's page carries its own copy of the course data)
```

## 1. curriculum.md

```
# The Hidden Curriculum — Master Curriculum
<intro>
Status key: `todo` · `published` · `legacy`
Lantern lessons: model-vs-app-vs-agent coding-agents-in-your-editor ...     lesson KEYS whose subject is AI
---
# Start · Orientation — what this course is, and the lantern you carry
## Module 00 — Orientation: The Map and the Lantern
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 00.01 | [The hidden curriculum](curriculum/lessons/the-hidden-curriculum.md) | ... | C001 | S003 | todo |
# District 1 · The Machine — what's on your computer
## Module 01 — Your Computer, Under the Hood <!-- map: Your computer -->
...
# District 4 · The Network — how computers talk <!-- id: network -->
...
# Finish · Capstone — one small real project, from idea to running
## Module NN — Capstone
---
## Legacy lessons (published before 2026-10-12; kept, marked, rebuilt later)
| Legacy lesson | Slug | Covers | Note |
| 00.01 The hidden curriculum | 00-01-the-hidden-curriculum | the-hidden-curriculum, model-vs-app-vs-agent | ... |
## Retired keys
- mcp-servers — merged into what-an-api-is (2026-11-02)
## Deep-dive backlog (not scheduled)
## Build log
```

- **Regions.** One `# Start`, then `# District 1..N` (4 to 7, numbered in order), then one `# Finish`, each
  `<kind> · <name> — <question>`. The Start and the Finish hold **exactly one module each** (the map draws each as one
  circle with one number). A district's id is its name without "The", kebab-cased (`The Machine` → `machine`), unless
  the heading pins it: `<!-- id: network -->` at the end. The id is what scenes may name (`focus: 'network'`) and the
  site's `#district-network` anchor, so pin it before renaming a district whose id should not move (section 8).
- **Modules.** `## Module NN — <name>`, numbered 00, 01, ... in file order, at most 5 per district. The map shows a
  short label: an explicit `<!-- map: Short name -->` on the heading wins; otherwise the name before a colon, without a
  trailing `(parenthesis)`, in the name's own casing. (The old curriculum format, and only that, uses the hand-drawn
  map's labels from tools/course.py `LEGACY_MAP_LABELS`, so it still draws the old map.) `course.py check` says when a
  label does not fit the map and suggests one that does.
- **Lessons.** `ID` is display only (`MM.NN`, 01, 02, ... in each module in file order) and changes whenever lessons
  move: never type IDs by hand, run `python tools/course.py renumber --write` (section 3). The **key** is permanent:
  the spec file's name in the link, the lesson's folder `lessons/<key>/` and its URL
  `/courses/the-hidden-curriculum/lessons/<key>/`. Kebab-case, at most 40 characters, unique, no number in front (that
  pattern belongs to legacy slugs), and **never reused**: a dropped key goes under `## Retired keys` and check refuses it.
- **Everything else names lessons by key.** The `Lantern lessons:` line and a Legacy table's `Covers` take keys only;
  check fails on an ID there ("use the lesson key: IDs change when lessons move"), because after the next renumber the
  ID would silently name a different lesson. `renumber --write` converts any IDs it finds there into keys.
- **Status.** `todo` (the daily job takes the first one), `published`, or `legacy`: a legacy lesson covers this slot
  for now and the daily job skips it. `next` also skips a key that course.json already lists as published, and check
  warns when the status and course.json disagree.
- **Legacy table.** The 12 lessons published before 2026-10-12 (`"legacy": true` in course.json; check refuses any other
  folder here). `Covers` lists the new slots (keys) whose material each one covers. Legacy lessons are never rebuilt in
  place: their folders, videos and pages stay as they are, and their pages keep loading `engine/legacy/map-v1.js`.
  The first column keeps the legacy lesson's own old ID (`00.01 The hidden curriculum`): that is the ID its video's
  badge shows, so it never changes.
- **Retired keys.** `- key — why (date)` lines (or a table whose first column is the key) under `## Retired keys`.
- The old format (`| ID | Lesson | Key idea | Status |`, no keys, no Legacy table) still parses: keys are derived from
  the titles, the Lantern line takes IDs, legacy coverage comes from course.json's `"legacy": true` entries (each covers
  the row with its own ID). renumber refuses it.

## 2. Spec files: curriculum/lessons/<key>.md

YAML-ish front matter, then free text (what the lesson must cover):
`key`, `id`, `title`, `district`, `module`, `status`, `legacy: [slugs]`, `minutes` (a number, about that long, or
`[lo, hi]`), `concepts: [C...]`, `sources: [S...]` (every source the spec cites, the row's own 2-5 first) and
`lead: [S...]` (the source or two the title card credits as "Built on"). The production workflow reads the row's
sources in full, checks the other cited sources point by point, and credits every source it uses on the lesson page
(`credits` in lesson.js). curriculum.md wins over the front matter for the ID, title, status, module and district; check
warns when they differ (`module: 09 APIs, Webhooks & MCP`, or just the number or the name; `district: The Network` or
its id), and `renumber --write` rewrites `id`, `module` and `district` to match. The key must match. A spec file with
no row is reported. `python tools/course.py lesson <key>` prints a row plus its spec as JSON, and
`python tools/course.py next` the first `todo` lesson (id, key, title, district, module, minutes, spec path, sources).

## 3. tools/course.py

| command | does |
|---|---|
| `renumber [--write]` | rewrites, in file order, lesson IDs (01, 02... per module), module numbers (00..) and District numbers in curriculum.md; turns IDs in the Lantern line and Legacy Covers into keys; rewrites the spec files' `id` / `module` / `district`. Prints a unified diff; without `--write` it changes nothing. New format only |
| `check [--no-browser]` | unique keys, none retired; contiguous IDs and modules; region order and limits (4-7 districts, 5 modules, one module in the Start and in the Finish); keys (not IDs) in the Lantern line and Covers; spec files present and consistent; legacy slugs exist in lessons/ and are legacy in course.json; every `legacy` slot is covered; statuses vs course.json; what a deleted lesson leaves behind (a built `lessons/<key>/` or a spec file with no row, a published course.json entry with no row); the names scenes of built lessons hand the map (`pin`, `focus`, `highlight`, `K.map.chipPos('...')`...) still resolve; cited S-/C-IDs exist; the generated narration survives narrate.py's caption conversion (an error when an acronym does not come back); and the map itself, laid out by the real engine/map.js in headless Chromium with the real fonts. Exit 1 on errors |
| `sync [--dry-run]` | writes engine/course.js (only when it changed) and refreshes every built new lesson (section 6); prints what needs narration or a re-render, with the commands |
| `remap [--render] [--dry-run]` | sync, then runs those commands: `narrate.py` (re-bills only the changed sections), `mix.py`, and with `--render` `render.py`. Each command names the lesson's folder (never its key), so a fixture run never touches a real lesson |
| `next`, `lesson <key\|id>` | JSON for the production workflow |
| `map [--png out.png --pin <module\|key>]` | the map as text, or rendered to a PNG |

Every command takes `--curriculum <file>` for testing (and `--registry <file>` for course.json). With a fixture
curriculum, `sync` and `remap` also need `--course-js <file>` and never touch the real lessons (pass `--lessons <dir>`
to point them at test lessons); a `remap` that is not `--dry-run` refuses to run without `--lessons`.
`python tools/new_lesson.py <key>` takes the same `--curriculum`, `--lessons`, `--course-js` and `--registry`.

## 4. engine/course.js and the map

`window.COURSE = { generated, title, format, districts: [{id, kind, n, name, question, modules}], modules: [{n, name
(map label), full, district}], lessons: [{id, key, title, module, district, status, lantern?, legacy?, slug?}],
lanterns, legacy: [{slug, id, title, covers}], mapHash }`, one item per line. `generated` is the date of the last real
change. Local lesson pages load it before engine/map.js (the template's `{{MAPJS}}`), and map.js lays the map out from
it: see engine/KIT.md "The map" for the API and the layout rules. `mapHash` is a hash of what the map drawing depends
on (district names and questions, module labels, the module numbers of every region, map.js), not statuses, so
publishing a lesson never makes other lessons look stale. The Start and the Finish are drawn as a circle with a number
and the fixed words "Start" / "Finish", so their name, question and module label are left out of `mapHash`: changing
them flags only the lessons at the Start or the Finish (section 6).

## 5. The standard map section

Every new lesson's section 02:

```
## 02 — Where this sits on the map [map]
<!-- map:begin -->
<!-- generated by tools/course.py sync from curriculum.md: change the curriculum and re-run sync, never this text -->
<!-- captions: A P Is=APIs -->
Here's where this lesson sits on the map. We're in [[district]]The Network, the district about how computers talk,
on the shelf called [[module]]A P Is, webhooks and M C P. That's where everything in this lesson gets stored.
<!-- map:end -->
```

- Three sentences: the map assembles under the opener, the district comes into focus at `[[district]]`, the pin drops
  at `[[module]]`, and the fixed closing line keeps the "you are here" card on screen. Start / Finish lessons say
  "We're at the Start, Orientation: what this course is, and the lantern you carry ...".
- No numbers and no neighbouring titles, so the text changes only when the lesson's district or module (its name,
  label or question) changes, never when lessons are added or reordered around it.
- Written for the ear (COURSE.md): `&` → "and", acronyms spelled (`API` → "A P I", `MCP` → "M C P", plurals get a
  `<!-- captions: A P Is=APIs -->` pair), `JSON` → "Jason", `SQL` → "sequel", `YAML` → "yamel", `VRAM` → "vee ram",
  `.py` → "dot P Y"; words the voices read as words stay as written (`PATH`, `RAM`, `REST`, `CORS`, `NAT`, `LAN`), and a
  slashed token is said part by part (`CI/CD` → "C I C D", `HTTP/2` → "H T T P 2", each with a caption pair). Caption
  pairs apply to the whole lesson, so none is ever made for an ordinary word (`path=PATH` would turn every "path" into
  PATH). The list is `SAID_AS_WORDS` in tools/course.py. check runs every generated text through narrate.py's caption
  conversion and fails when the screen would not show the written form again.
- narrate.py treats `[map]` like any section (the tag is stripped from the title; cues.json marks it `"map": true`).
- The scene is one line, `scenes/02.js`: `SCENE('02', (t, S) => K.map.intro(t, S));`.

## 6. sync: what changes in a built lesson, and what has to be redone

A new lesson is "built" once `lessons/<key>/` exists (`python tools/new_lesson.py <key>` scaffolds it; it runs sync
and prints sync's report on stderr, so a curriculum change nobody synced yet shows up there too). For each built
lesson, sync rewrites `key`, `id` and `module` in lesson.js (legacy lessons are never touched), adds engine/course.js
to an index.html that lacks it, replaces the text between the map markers, and keeps `course-sync.json`:
`{drawing, drawing_changed}`, where `drawing` hashes what the lesson's video shows that the curriculum decides (the map,
the lesson's place on it, the card's title, the lesson ID in the badge on every scene, and for a Start / Finish lesson
the region's name and question and the module label its note shows).

- **Needs narration** when the [map] section's text differs from what was narrated (audio/02.align.json): narrate.py
  re-bills only that section (a few hundred characters), then mix.py and render.py.
- **Needs a re-render only** when the drawing changed after the video was rendered (out/lesson.mp4 older than
  `drawing_changed`; for a published lesson with no local render, published before it).
- Then republish what is live (section 7).

`python tools/course.py remap --render` runs all of it; `--dry-run` only prints it. Narrating spends ElevenLabs
characters: check the budget first (the missing-map skill has the one-liner).

## 7. Publishing

publish.py parses curriculum.md through course.py. New lessons are matched by key (course.json entry = the key) and
legacy lessons by their slug in the Legacy table. The JSON the site reads keeps its shape; a legacy row carries
`"legacy": true`, `"covers"` (the slot IDs), `"coverTitles"` (those slots' new titles, same order) and `"legacyId"`
(its own old ID) and is listed in the module of the first slot it covers, right after that slot's own row (a slot
with status `legacy` still gets its row: new title, locked), with that slot's `id` (for ordering); several legacy
lessons on one slot are listed in table order; a slot whose legacy lessons are all listed in another module is one
row that links to them (`"coveredBy"`, with the slot's own lantern); once all its slots are rebuilt a legacy lesson
stays listed right after the first one. New-lesson rows carry `"key"`. A legacy page's Next goes to the next row that
can be watched (past the last one, the next slot) and shows its `legacyId`; a new lesson's Next skips legacy rows;
"All N lessons" counts the curriculum's lessons, not rows. `"latest"` is the most recently published row the page
lists (never a lesson since deleted).

- **Each new lesson's page carries its own course data.** Staging a curriculum lesson writes
  `lessons/<key>/course.js` next to its page (the course data as it is at that moment) and the page loads that, not the
  shared `engine/course.js`. A later curriculum change therefore never redraws the map under a live page's old
  narration and MP4; the page changes when the lesson is re-narrated / re-rendered and republished. The shared
  `engine/course.js` is still written (proofs of concept load it), and `engine/legacy/` is copied with the engine.
- **A stale lesson is not published.** `publish.py <key>` stops when course.py says the lesson still needs a sync,
  narration or a re-render (`--allow-stale` overrides); `--all` skips such lessons and leaves their live pages as
  they are.
- **The blog's course page must support the data.** Before committing, publish.py reads the blog's
  `src/pages/courses/the-hidden-curriculum.astro` and `src/components/courses/LessonList.astro` (comments stripped;
  LessonList itself must handle the rows) and stops when the data needs
  something they do not handle yet: a district count other than six while the page hard-codes six, `"coveredBy"` rows,
  or legacy rows whose `"legacyId"` differs from their slot's `"id"`. Fix the page in the blog first.
- **Removing a lesson.** `python tools/publish.py --remove <key>` (the row gone from curriculum.md, the key under
  `## Retired keys`): `git rm` of its folder on the site, its course.json entry dropped, the course data and every
  live page's footer links rebuilt, pushed, and it waits until the lesson's URL answers 404. Legacy lessons cannot be
  removed this way.
- `python tools/publish.py --dry-run [--out data.json]` builds all of it into a temp folder (no git, no network,
  course.json untouched; stale lessons and blog-page gaps are warnings); `--curriculum` / `--registry` point it at test
  data. `--remove <key> --dry-run` says what it would do.

## 8. Restructuring the course

Edit the rows (and the spec files), then:

```
python tools/course.py renumber --write     # IDs, module numbers, District numbers, spec front matter
python tools/course.py check                # fix what it reports
python tools/course.py sync                 # course.js + every built lesson; prints what to redo
python tools/course.py remap --render       # narration of changed [map] sections, re-renders (spends ElevenLabs characters)
python tools/publish.py --all               # every live lesson: data, pages, Next links, their own course.js
                                            # (publish.py --data-only when no built lesson changed)
# then commit curriculum.md, the spec files, engine/course.js and the lessons sync touched
```

| change | in curriculum.md | what follows |
|---|---|---|
| **Add** a lesson | a row at its place, with a new key (never a retired one) and a spec file | renumber gives it and the later lessons in the module their IDs; sync rewrites their lesson.js and flags them for a re-render (the badge) |
| **Delete** a lesson | remove its row and spec; add its key under `## Retired keys`; renumber | check lists what it left behind. If it was built, archive `lessons/<key>/` by hand (old takes go to `Courses/_old-takes/`); if it was published, `python tools/publish.py --remove <key>` takes its page down and fixes the Next links |
| **Reorder** lessons | move rows, renumber | IDs change, keys do not: re-renders only. Lantern / Covers name keys, so they follow |
| **Move** a lesson to another module or district | move its row, renumber | the [map] text changes: narration of section 02 + re-render (sync says so) |
| **Combine** two lessons | keep one row (its key), delete the other; merge the specs; retire the dropped key | build the survivor; `publish.py --remove <dropped key>` if it was published; point Lantern / Covers at the survivor |
| **Split** a lesson | keep the key on the part that keeps the old intent, add a row with a new key for the new part, renumber | a built lesson keeps its folder and URL; the new key gets its own spec file |
| **Rename** a lesson | change the title (the key stays) | nothing on the map; lesson.js `title` / `short` are the lesson's own, change them if you want |
| **Rename a module** or give it a map label | the `## Module` heading or `<!-- map: ... -->` | every lesson in that module: narration of section 02 (the text names the module); every other new lesson: re-render. check fails if a scene still names the old name |
| **Rename a district** / change its question | the `#` heading; add `<!-- id: old-id -->` first if scenes or links use its id | its lessons: narration; all others: re-render. Without a pinned id the id (and the site anchor `#district-<id>`) follows the new name, and check fails on any scene that names the old name or id |
| **Change the Start or Finish** (name, question, module label) | its `#` heading or module heading | only the lessons at the Start / Finish: narration (their [map] text and note); nobody else re-renders |
| **Add / remove / reorder modules or districts** | move the headings, renumber | module numbers and IDs shift: re-renders; lessons whose district or module changed: narration. Keep 4 to 7 districts, at most 5 modules each, one module in the Start and one in the Finish (check enforces it) |
| A legacy lesson's material is **rebuilt** | the new slot's status `legacy` → `todo`, later `published`; keep the legacy row in the Legacy table | the legacy video stays listed (after its first slot) and keeps its URL |

Never change a key once a lesson is built: it is the folder and the public URL.

## 9. Testing

- `lessons/_maptest` (never published): four fixture courses in `fixtures/` (old = curriculum.md as of 2026-10-12;
  d4 / d5 / d7 = new-format fixtures with 4, 5 and 7 districts, d7 with long module names and map labels) and a
  synthetic timeline (no narration) whose scenes draw `K.map.draw` and `K.map.intro` for several pins: the card beside
  a district, over a neighbour's column, inside a wide district (scenes 21, 22), left of a district with the pin at the
  row's left end (scene 11), and Start / Finish notes with the card under or beside them.
  `python lessons/_maptest/make.py && python tools/stills.py _maptest --every 2`.
- `python tools/course.py check --curriculum lessons/_maptest/fixtures/d7/curriculum.md` (and d4, d5, old).
- `python tools/course.py renumber --curriculum <copy of a fixture>` to see a renumbering diff without writing.
- `python tools/publish.py --dry-run --curriculum lessons/_maptest/fixtures/d5/curriculum.md --out d5.json`.
- Legacy freeze (the 12 legacy lessons must stay byte-identical): `python tests/legacy_freeze/stills_hash.py <phase>
  --no-png`, then `python tests/legacy_freeze/compare.py before <phase>`; tests/legacy_freeze/README.md explains it.
