# 00.01 — The hidden curriculum · storyboard (final)

Pairs with `script.md` (8 sections, 701 spoken words, about 4:40 at 150 wpm plus lead, gaps and tail).
Canvas 1920×1080. Safe text area x 80–1840, y 130–930; the badge sits top-left (y < 110) on 02–07.
Minimum sizes: 26 px labels, 30+ px for reading, 20 px eyebrows. Every call is from `engine/KIT.md`.

## Lesson-wide decisions

**The persistent object: four question tags.** They are Aaron's loose questions. Born in 02, lodged in the gap in 03,
joined by a fourth in 04, shelved onto the course map in 05, and from 06 on they live as pins on a folded **map tile**.
The viewer watches a pile of confusion get a home: that is the lesson's promise, done as motion.

- **Full tag** (w 440, h 76): `K.card(x, y, 440, 76, { r: 20, glow })`, `K.icon('question', x + 42, y + 38, 40, { color: C.accent })`,
  `K.text(label, x + 84, y + 49, { font: 'mono', size: 30, color: C.strong })`.
- **Compact tag** (w 340, h 56): same layout scaled by hand, icon 30, mono **26** (never smaller: it must stay readable).
- **Shelved**: the question icon becomes `K.icon('check', ..., { color: C.head })`.
- Labels, in order: `.txt → .py`, `cd`, `.venv`, `service account`.
- **Tray** (home): x 1360, slot tops at y 270 / 366 / 462 / 558. Right edge 1800.
- **Map tile**: `K.iconTile('map', x, y, s)` with small `K.icon('pin', ...)` marks drawn on it. Used from 06 on, because a
  scaled-down `K.map.draw` would push district text under 26 px.
- Write `tag(label, x, y, { compact, shelved, alpha, glow })` and `mapTile(x, y, s, pins)` once in `scenes/00-shared.js`.

**Plate.** `engine/assets/teahouse-night.jpg` exists. Its left half (x 80–1000, y 130–600) is empty night sky; the tea house
and its lantern string sit at x 1100–1600, y 270–720. Title (01) and end card (08) therefore keep all type in a **left column
at x 140**. Both call `K.bg({ glow: 0.5, glowX: 1350, glowY: 520 })` first, then `K.plate('plate', t, { zoom: true, shade })`;
`K.plate` returns early if the image is missing, so the cards still read on `K.bg()` alone (the warm glow stands in for the house).

**Overshoot budget.** One `'back'` per scene at most: 01 map tile, 03 breaking-things tile, 05 gate pin, 07 pins landing. None elsewhere.

**Word sync.** `S.find(word, nth)` is a case-insensitive *prefix* match, 0-indexed, on spoken tokens (punctuation other than
`' . -` is stripped). Spelled letters are separate tokens ("C", "D", "M", "I", "T"), so never `find` a letter: hang those beats on
the nearest cue or a real word. `vee-env` is one token.

**Terminal quirk.** `K.term(rect, t, [])` blinks the prompt together with the caret. For an idle prompt use
`[{ at, cmd: '' }]`, which keeps `C:\Users\you>` steady with only the caret blinking.

---

## 01 — Nobody handed you the map
**Metaphor object:** the five tool pills (the hidden curriculum's contents) and the map tile (the promise). Both return later.

**Frame:** title card, noBadge. `K.bg(...)`, plate with `shade: 0.45`, `K.petals(t, { n: 6, seed: 3, alpha: 0.5 })`.
Left column, x 140, all inside the painted sky:
- `K.eyebrow('The Missing Map · 00.01 Orientation', 140, 220)`, fading in over 0–0.8 s.
- `K.title('The hidden curriculum', 140, 320, { size: 92 })`, fading in over 0.2–1.0 s (check in stills that it ends left of x 1250).
- Conclusion line `A gap in the syllabus, not in you.` (`font: 'read'`, italic, 44, `C.strong`) at (140, 400), fading in over 0.6–1.4 s.
  The title card carries the one-line conclusion from the first second; the narration confirms it at `[[not-you]]`.

**Beats**
- `[[topics]]`: five pills (size 30) rise left to right on y 490, starting at x 140 with 22 px gaps (place each by `K.measure` + 48):
  `terminals` `files` `git` `keys` `hosting`. Each rises (`K.rise`, 0.5 s) on its word: `S.find('terminals')`, `'files'`, `'git'`, `'keys'`, `'hosting'`.
- `[[not-you]]`: a terracotta `K.mark` (`color: C.accent`) draws under `not in you.` over 0.7 s
  (x = 140 + `K.measure('A gap in the syllabus, ', { font: 'read', italic: true, size: 44 })`, y 414).
- `[[map]]`: `K.iconTile('map', 188, 620, 96, { glow: 0.6 })` scales in with the scene's one `'back'`, and
  `what each thing is · where it goes` (Karla 30, `C.body`) fades in at (262, 631).
- `[[degree]]`: a card rises, `K.card(140, 712, 700, 104)`, with `K.icon('cap', 200, 764, 56, { color: C.head })` and
  `Information Systems` (Karla 32, weight 600, `C.strong`) at (252, 776). On `S.find('hard')` the cap tilts
  0.12 rad over 0.4 s and stays tilted (a small, dry joke).

**Exit:** eyebrow, title, underlined conclusion, five pills, map tile and degree card at rest. Only the plate drift and petals move.

## 02 — Python in a text file
**Metaphor object:** `script.txt`, and the first three question tags, which collect in the tray.

**Frame:** `K.bg()`. A compact degree chip fades in top-right over 0–0.6 s: `K.card(1360, 150, 440, 76)`,
`K.icon('cap', 1405, 188, 40, { color: C.head })`, `Information Systems` (Karla 28, `C.soft`) at x 1450. It stays the whole scene:
that is the quiet joke. The tray (x 1360, from y 270) starts empty.

**Beats**
- `[[notepad]]`: `K.win(100, 190, 820, 420, { title: 'script.txt - Notepad', kind: 'notepad' })` rises. `K.editor(rect, t,
  ['print("hello")', 'name = input("name? ")', 'print("hi", name)'], { syntax: 'none', size: 30, typeAt: cue + 0.4, cps: 24 })`:
  no colour, because Notepad does not highlight code. On `S.find('saved')`, `K.file(1110, 330, 170, { ext: 'txt', name: 'script.txt' })` pops in.
- `[[rename]]`: a ghost pill `.py ?` (size 28, `C.head`, alpha 0.7) appears at (1110, 520) under the file. The file itself stays `.txt`
  (he didn't know to rename it). At cue + 1.0 the ghost becomes tag 1 `.txt → .py` and glides on a gentle arc to tray slot 1 (1360, 270) over 0.7 s.
- `[[terminal]]`: `K.win(260, 560, 740, 300, { title: 'Command Prompt', kind: 'terminal', focus: true })` rises over Notepad's lower-left
  corner. `K.term(rect, t, [{ at: cue + 0.3, cmd: '' }], { size: 30 })`: a steady `C:\Users\you>` with a blinking caret, nothing typed.
  On `S.find('folder')`, tag 2 `cd` lifts off the prompt line and glides to slot 2 (1360, 366).
- `[[venv]]`: `K.folder(1110, 700, 130, { name: '.venv' })` pops in, with `K.icon('question', 1110, 612, 44, { color: C.accent })` bobbing
  above it (`K.wave`, amplitude 4). On `S.find('idea')` + 0.3, tag 3 `.venv` glides from the folder to slot 3 (1360, 462).
  On `S.find('hard')`, both windows, the file and the folder ease to alpha 0.45.
- `[[pile]]`: the three tray tags take `glow: 0.5`, with `K.glow(1580, 420, 260, C.head, 0.12)` behind the tray. On `S.find('place')`,
  `each one has a place` (Karla 28, `C.soft`) fades in centred at (1580, 690).

**Exit:** three glowing tags in the tray with their caption, the dimmed desk on the left, the degree chip top-right.

## 03 — Why nobody taught you
**Metaphor object:** the question tags, lodged in the gap between two halls.

**Frame:** `K.bg()`. Over 0–0.9 s the tray tags glide into the gap column and shrink to compact (340 × 56), top-left x 790,
tops at y 200 / 266 / 332. The degree chip fades out. The halls and the gap edges are not drawn until their cues.

**Beats**
- `[[cs]]`: left hall `K.card(120, 180, 600, 470)` rises. Eyebrow `Mostly the ideas` at (170, 236), `K.title('Computer science', 170, 300, { size: 48 })`.
  Pills (size 28) centred on x 420 at y 400 / 470 / 540: `algorithms`, `data structures`, `how computation works`,
  on `S.find('algorithms')`, `S.find('data')`, `S.find('how', 0)`.
- `[[is]]`: right hall `K.card(1200, 180, 600, 470)` rises. Eyebrow `Business systems` at (1250, 236), `K.title('Information systems', 1250, 300, { size: 44 })`.
  Pills centred on x 1500: `databases`, `processes`, `projects`, on their words.
- `[[gap]]`: two dashed edges draw downward at x 735 and x 1185 (`K.line`, `dash: [6, 10]`, `C.line2`, y 180 → 650),
  `K.glow(960, 430, 260, C.accent, 0.14)` fills the column, and the eyebrow `The gap` appears centred at (960, 168).
  Four noun pills (size 28) drop in on their words, two per row: `terminal` (870, 470) and `folders` (1050, 470) on `S.find('terminal')` / `'folders'`;
  `keys` (870, 545) and `hosting` (1050, 545) on `S.find('keys')` / `'hosting'`.
- `[[apprentice]]`: the halls ease to alpha 0.5. Three route tiles feed the gap from below, each with a thin `K.arrow` (`C.soft`, w 2, gentle bend)
  drawing from the tile top to the gap's bottom edge (960, 655):
  `K.iconTile('person', 560, 760, 96)` + `apprenticeship` on the cue; `K.iconTile('chat', 960, 760, 96)` + `forums` on `S.find('Forums')`;
  `K.iconTile('cross', 1360, 760, 96, { color: C.accent })` + `breaking things` on `S.find('breaking')`, scaling in with the scene's one `'back'`.
  Labels are Karla 30, `C.soft`, centred at y 850. On `S.find('Lots')` the cross tile gives two small tilts (±0.06 rad, `K.wave`, settling by 1.2 s).
- `[[holes]]`: the `folders` and `hosting` pills and the `.venv` tag fade to alpha 0.2: same column, different holes.

**Exit:** two dimmed halls, a glowing gap column with three faded holes, three route tiles with their arrows.

## 04 — It isn't just you
**Metaphor object:** the tray of tags. A fourth tag, `service account`, joins at the end.

**Frame:** `K.bg()`. Over 0–0.8 s the three tags glide from the gap back to tray slots 1–3 at full size (all at full alpha again);
the noun pills, halls and route tiles fade.

**Beats**
- `[[mit]]`: `K.win(120, 180, 1160, 470, { title: 'missing.csail.mit.edu', kind: 'browser' })` rises, with eyebrow `MIT` at (180, 290).
  On `S.find('Missing')`, `K.title('The Missing Semester', 180, 370, { size: 64 })` and `of Your CS Education` (head font 40, `C.strong`)
  at (180, 425) fade in.
- `[[rarely]]`: `“rarely covered” in class` (`font: 'read'`, italic, 34, `C.body`) appears at (180, 500). On `S.find('left')`,
  `“left to students to figure out”` appears under it at (180, 548).
- `[[agentic]]`: `K.icon('lantern', 210, 600, 44, { color: C.head })` with `K.glow(210, 610, 60, C.head, 0.3)`, then
  `K.pill('January 2026 · Agentic Coding', 470, 600, { size: 28, color: C.head, glow: 0.4 })`. The lantern is a nod to the map's AI district.
  On `S.find('allowed')` the browser eases to alpha 0.5 and `You're allowed to need a missing map.` (Georgia italic 40, `C.strong`) rises
  centred at (700, 760); on `S.find('map')` a gold `K.mark` draws under `missing map.`
- `[[work]]`: the browser and the italic line slide 60 px left and fade over 0.6 s. On `S.find('personal')` the left card appears:
  `K.card(120, 330, 500, 170)`, `K.icon('person', 200, 415, 72, { color: C.body })`, `personal account` (Karla 34) at (260, 427).
- `[[service]]`: `K.arrow(640, 415, 840, 415, { k, color: C.head })` draws over 0.6 s, then the right card appears: `K.card(860, 330, 460, 170)`,
  `K.icon('gear', 935, 415, 72, { color: C.head })`, `service account` (Karla 34) at (995, 427). On `S.find('credentials')`,
  `K.icon('lock', 1090, 560, 52, { color: C.head })` and `credentials stored properly` (Karla 28, `C.soft`, centred at (1090, 640)).
  On `S.find('either')`, tag 4 `service account` peels off the right card and glides to tray slot 4 (1360, 558); all four tags pulse once
  (glow 0 → 0.5 → 0.25 over 1 s).

**Exit:** the two work cards dimmed to 0.6, the arrow between them, four tags at rest in the tray.

## 05 — Where it lives
**Metaphor object:** the course map, which is the shelf. The four tags land on their shelves.

**Frame:** `K.bg()`, then `K.map.draw(t, { t0: S.cue('map', 1.2), focus, focusK, dim: 0.45, pin, pinK })` at default world coordinates,
no camera. Before the cue, the four tags sit in the tray. No map text sits below y 935; the tag stack stays in the clear corner below.

**Beats**
- `[[map]]`: the map's staggered reveal starts (lantern string, six districts, garden path). At the same moment the four tags shrink and slide
  into one stacked chip in the bottom-right corner, `K.card(1696, 846, 140, 70)`, with `K.icon('question', 1730, 881, 34, { color: C.accent })`
  and mono `×4` (28 px) at x 1756. That corner is outside The Network card and below the garden path.
  District roll call: `focus` is the most recently spoken district, from `S.find('Machine')`, `'Code'`, `'History'`, `'Network'`, `'Trust'`,
  `'Shipping'` (all nth 0); each light-up uses `focusK = K.io(t, thatTime, 0.5)`. Nothing lights before it is named.
- `[[lanterns]]`: `focus: 'ai'` (map.js brightens the lantern glow 1.8×) until `S.find('walk')` + 1.5, then focus eases off.
- `[[gate]]`: `pin: '00'`, `pinK = K.io(t, cue, 0.6, 'back')` (the scene's one overshoot), plus `K.glow(135, 440, 110, C.head, 0.25)` on the Start gate.
- `[[shelve]]`: the stack fans out. Each tag flies as a compact tag on a curved path to its row (`K.map.chipPos`), focus following it:
  - `.txt → .py` → `chipPos('01')`: leaves on the cue, lands at `S.find('Machine', 1)` + 0.1 (`focus: 'machine'`).
  - `cd` → `chipPos('02')`: leaves at cue + 0.4, lands at `S.find('Machine', 1)` + 0.5.
  - `.venv` → `chipPos('05')`: leaves at `S.find('Code', 1)` − 0.7, lands at `S.find('Code', 1)` + 0.1 (`focus: 'code'`).
  - `service account` → `chipPos('09')`: leaves at `S.find('Trust', 1)` − 0.8, lands at `S.find('Trust', 1)` + 0.1 (`focus: 'trust'`).

  On landing each tag collapses into its row using map.js's own pinned-row geometry: `K.rr(c.x - 18, c.y - 19, c.w + 36, 38, 19)` filled
  with `K.rgba(C.head, 0.14)`, plus `K.icon('check', c.x + c.w - 6, c.y - 2, 28, { color: C.head })`. Focus clears 1 s after the last landing.

**Exit:** the full map, no focus, the pin bobbing on the gate, four highlighted rows (01, 02, 05, 09) with gold checks, lanterns swaying.

## 06 — A map, not a manual
**Metaphor object:** the map, folded into the map tile and set against a manual; then the full map once more, to show where it is too tidy.

**Frame:** `K.bg()`. Over t −0.2 → 0.7 the 05 map shrinks and fades toward (1440, 400)
(`K.at(lerp(960, 1440, k), lerp(540, 400, k), lerp(1, 0.18, k), 0, () => { g.translate(-960, -540); K.map.draw(t, { pin: '00' }); })` with alpha 1 − k),
while `mapTile(1440, 400, 240)` fades in with the four shelved checks drawn as small gold pins and `K.icon('pin', 1530, 300, 44, { color: C.accent })`
bobbing on its corner (we are at the gate). On `S.find('map', 0)`, `a map` (Karla 36, `C.head`) appears centred at (1440, 580).

**Beats**
- `[[manual]]`: `K.iconTile('book', 480, 400, 240, { color: C.soft })` rises with `a manual` (Karla 36, `C.soft`) at (480, 580) and `step by step` (Karla 28, `C.quiet`)
  at (480, 625). The map side gains `what it is · where it lives` (Karla 28, `C.soft`) at (1440, 625).
- `[[five]]`: the book group fades out over 0.5 s. Five rows rise in the left column, a mono gold numeral at x 160 and Karla 38 `C.strong` text at x 220,
  baselines y 300 / 380 / 460 / 540 / 620: `What is it?` · `Where does it live?` · `What is it like?` · `What does it connect to?` · `What will surprise you?`,
  on `S.find('what', 0)`, `S.find('live')`, `S.find('like')`, `S.find('connect')`, `S.find('surprise')`.
- `[[recognise]]`: `K.glow(1440, 400, 200, C.head, 0.3)` blooms behind the map tile, and `K.pill('recognise it', 1440, 700, { size: 30, color: C.head })` rises.
  The tile is now a known place.
- `[[messy]]`: rows, tile and pill fade over 0.5 s; the full course map fades back in at default coordinates (`K.map.draw(t, { pin: '00', focus, focusK, dim: 0.6 })`, no `t0`).
  On `S.find('Git')`: `focus: 'history'`, `K.pill('git', chip06.x + chip06.w - 40, chip06.y, { size: 28, color: C.head })` and a gold `K.arrow` arcing from
  the History card's right side down into The Network (from (1640, 470) to (1640, 700), bend so it bows outward past x 1700), `k` over 0.8 s.
  On `S.find('Keys')`: `focus: 'trust'`, `K.pill('keys', chip09.x + chip09.w - 40, chip09.y, { size: 28, color: C.head })`, and three short dashed `C.head` arrows
  fan out from the Trust card across its borders: up into The Code (960, 640 → 960, 560), right into The Network (1160, 790 → 1240, 790),
  left into Shipping (760, 790 → 680, 790), staggered 0.15 s. On `S.find('everywhere')` all three arrowheads glow briefly (0.4 s, no flash).
- `[[skip]]`: the map eases to alpha 0.12. Eyebrow `Safe to skip: memorising commands` at (360, 262).
  `K.win(360, 290, 1000, 220, { title: 'Terminal', kind: 'terminal' })` rises, with `K.iconTile('lantern', 1440, 300, 96, { glow: 0.6 })` hanging just right of it.
  On `S.find('type')`, `K.term` types `python script.py` (cps 16). On `S.find('mean')`, a gold `K.mark` draws under the typed command, and
  `K.pill('know what it means', 860, 640, { size: 32, color: C.head, glow: 0.4 })` rises with a short `K.arrow` up to the command.
  At the same time `mapTile(1700, 220, 130)` with its pins fades in top-right, ready for 07.

**Exit:** the terminal with its underlined command lit by the lantern, the pill, a ghost of the map, the map tile top-right.

## 07 — The surprises you'll hit
**Metaphor object:** the map tile collecting pins. Every "just" becomes a pin, not a verdict.

**Frame:** `K.bg()`. The map tile starts at (1700, 220) s 130 and eases to (1560, 430) s 220 over 0–0.8 s. Everything else from 06 is gone.

**Beats**
- `[[just]]`: `K.title('just', 160, 250, { size: 96 })` rises. Three speech bubbles appear on `S.find('just', 1)`, `S.find('just', 2)`, `S.find('just', 3)`:
  `K.card(160, y, 960, 96, { r: 48 })` at y 310 / 430 / 550, each with `K.icon('chat', 210, y + 48, 44, { color: C.soft })` and mono 30 `K.spans` at x 260
  (`just` in `C.head`, the rest `C.strong`): `just cd into the folder` · `just activate the .venv` · `just add it to your PATH`.
  Sources pop in at each bubble's right end, `K.iconTile(name, 1060, y + 48, 64)`: `book` on `S.find('Tutorials')`, `person` on `S.find('Coworkers')`,
  `lantern` on `S.find('assistant')`.
- `[[skipped]]`: the gold `just` in each bubble lifts off as `K.icon('pin', ..., 40, { color: C.accent })` and arcs into the map tile, landing at tile offsets
  (−50, −40), (10, 10), (55, −25), staggered 0.3 s, with the scene's one `'back'`. On `S.find('pin')`, `K.pill('a pin on the map', 1560, 610, { size: 30, color: C.head })`.
- `[[error]]`: on `S.find('Run')` (about 2–3 s before the cue) the bubbles and headline drift up 30 px and fade; the tile and its pins ease back to (1700, 220) s 130.
  `K.win(160, 330, 1460, 330, { title: 'Command Prompt', kind: 'terminal', focus: true })` rises.
  `K.term(rect, t, [{ at: S.find('Run') + 0.4, cmd: 'python script.py', cps: 16 }, { at: S.cue('error'), out: <error>, color: C.accent }, { at: S.cue('error') + 0.5, cmd: '' }], { size: 28 })`,
  where `<error>` is two lines on screen:
  `python: can't open file 'C:\\Users\\you\\script.py':` / `[Errno 2] No such file or directory`
  (Python prints the path with doubled backslashes; in the JS string literal that means `\\\\`). The error prints on the cue.
- `[[wrong-folder]]`: `K.ring(297, 553, 140, 36, k, { color: C.head })` circles the fresh `C:\Users\you>` prompt (row 4 of the terminal body),
  `K.pill('wrong folder', 300, 760, { size: 30, color: C.head })` appears with `K.arrow(300, 730, 300, 590, { k, color: C.head, w: 2.5 })`,
  and the shelved `cd` tag (compact, gold check) slides in beside it at top-left (470, 732), tying the error back to its shelf.
  On `S.find('still')`, `K.file(1150, 760, 160, { ext: 'txt', name: 'script.txt' })` pops in on the right: the other cause, straight from 02.

**Exit:** the terminal with the terracotta error, the prompt circled in gold, `wrong folder` with the `cd` tag, `script.txt`, and the pinned map tile in the corner.

## 08 — Keep this
**Metaphor object:** the map tile with all its pins, on the tea-house plate, whose painted lantern string is "AI as the lanterns".

**Frame:** end card, noBadge. `K.bg(...)`, plate with `shade: 0.55`, `K.petals(t, { n: 6, seed: 7, alpha: 0.45 })`.
Left column x 140–1040 only, clear of the tea house. `K.eyebrow('The Missing Map · 00.01', 140, 200)` and `K.title('Keep this', 140, 285, { size: 72 })`
are visible from frame 0. `mapTile(960, 240, 110)` with its pins fades in over 0–0.8 s, sitting in the sky to the right of the title.
Rows at y 390 / 560 / 730: a bold lead (Karla 700, 40, `C.head`) at (140, y), and the rest as `K.para(rest, 140, y + 54, 880, { font: 'read', size: 32, color: C.body })`.
Row 3 wraps to two lines and ends near y 840. If stills show the ground of the plate hurting contrast, set the three rows on one soft panel
`K.card(110, 340, 960, 540, { fill: K.rgba(C.page, 0.6), stroke: false, shadow: false })`.

**Beats**
- `[[keep-1]]`: row 1 rises (`K.rise`, 0.6 s): **The gap is in the syllabus, not in you.** / Nobody handed you this map; it's a missing semester, not a character flaw.
- `[[keep-2]]`: row 2 rises: **Every confusing thing has a shelf.** / Seven districts, with AI as the lanterns over all of them.
  On `S.find('lanterns')`, when `K.img.plate` is loaded, `K.glow(1340, 490, 280, C.head, 0.18)` warms the painted lantern string (eased in, no pulse). On the
  `K.bg()` fallback, skip it.
- `[[keep-3]]`: row 3 rises: **Aim for recognition, not recipes.** / Once you know what a thing is and where it lives, the how-to is easy to find.

**Exit:** three takeaways at rest over the drifting plate, the pinned map tile, sparse petals. Hold through the 3 s tail. No teaser, no next-lesson card.

---

## Fact ledger
- MIT, *The Missing Semester of Your CS Education* (missing.csail.mit.edu, checked 2026-09-30): the front page says tool proficiency is
  "rarely covered" in classes and "left to students to figure out on their own"; the January 2026 (IAP) schedule lists "Agentic Coding" (1/21/26);
  a 2020 offering also exists. The script states no founding year.
- Python's message when the named file isn't in the current folder: `python: can't open file '...\\script.py': [Errno 2] No such file or directory`.
  On Windows the prefix may be the full path to `python.exe`; the narration says "something like". Python prints it before reading the script,
  so it never means the code is broken (a missing file opened by the code is a `FileNotFoundError` traceback instead); "usually" hedges only the causes.
- CS is described as teaching "the ideas", not "theory": CS degrees include hands-on programming and systems courses. Missing Semester's point is that
  students use the tools constantly but are rarely taught them, hence "used everywhere, rarely taught".
- Aaron's stories are limited to COURSE.md: Notepad and `.txt`; not knowing to rename to `.py`; not knowing to open a terminal and `cd`; not knowing `.venv`;
  a degree in Information Systems (Notion Identity & Bio: CSUF Business Administration, Information Systems concentration; the exact degree name is
  unresolved across sources, so say and show only "Information Systems"); work automations on personal accounts moved to service accounts with properly stored credentials.
  `script.txt` and its three lines of code are illustrative.
- Shelf placement (curriculum.md): `.py` → 01 Your computer, `cd` → 02 The command line (both The Machine), `.venv` → 05 Packages (The Code),
  service accounts → 09 Identity & keys (Trust). Git → 06 (The History) talking to 07 (The Network); keys → 09 (Trust).
