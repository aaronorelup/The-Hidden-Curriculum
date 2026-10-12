# 00.03 — How old is all this? · storyboard (final, extended rebuild)

> Final synthesis: draft B's spine and object (the building on the old street), with grafts from A and C (see script.md 01 notes).
> v1 (the published 5-minute cut) is kept in `drafts/v1/`. Reuse map: v1 `00-shared.js` (street, tags, lanterns, `M.lerpGeom`) is
> the base of a new `scenes/00-shared.js` that adds `M.building(t, {layout, sign, lock, lit})`; v1 01 -> 01 (title card, plus the
> building ghost), v1 02 -> 02 (map, plus the Code / History / Trust washes), v1 03 -> 03 (as is), v1 04 -> 04 (minus the Ethernet
> gloss), v1 05's birthday ring -> 05, v1 07's light-spread -> 13, v1 09's end-card layout -> 15. Scenes 06-12 and 14 are new, on the
> same geometry.

**The one metaphor: "the old street under constant renovation".** v1's street of years, kept exactly (reuse
`drafts/v1/scenes/00-shared.js`: `M.street`, `M.tag`, `M.lerpGeom`, the lanterns), plus one new object that lifts off it:
**the building**, which has three parts that age at three speeds and a light above it:

| part | meaning | speed | colour |
|---|---|---|---|
| **stone** (the base) | the idea: a file, a commit, a message across a network | barely moves | gold `K.C.head` |
| **paint** (the sign on the wall) | the version number | every year or so | cream `K.C.strong` on `K.C.tile` |
| **lock** (on the door) | security: how you sign in, how data is scrambled | fastest | terracotta outline `K.C.accent` |
| **lanterns** (over the roof) | AI | fastest of all | gold paper, terracotta glow (as v1 / K.map) |

**Street geometry (from v1):** street `K.line` 2 px at y 560 from x 160 to x 1760, `X(year) = 160 + (year - 1965) * 26.23`
(1969 → 265 · 1981 → 580 · 1991 → 842 · 2005 → 1209 · 2015 → 1472 · 2020 → 1603 · 2024 → 1708). Lanterns only at x ≥ 1600.

**Building geometry ("full" layout, centre x 960):** drawn only with kit cards, pills and line icons.
- stone: `K.card(660, 700, 600, 110, {fill: K.C.tile, stroke: K.C.head, r: 12})`; inside, `K.eyebrow('STONE · THE IDEA', 960, 762)`.
- walls: `K.card(700, 380, 520, 320, {fill: K.C.tile, stroke: K.C.line2, r: 24})`; roof line: two `K.line`s from (680, 380) to (960, 300) to (1240, 380), `K.C.line2`.
- paint (sign): `K.pill(signText, 960, 440, {size: 30})` on the wall; when repainted, the old text slides up and fades while the new
  one rises (0.5 s, `K.io`), a brief `K.glow` behind it (the "fresh paint").
- door: `K.card(900, 520, 120, 180, {r: 0, stroke: K.C.line2})` (the brand's one square element) with the lock icon
  `K.icon(lockIcon, 960, 610, 56, {color: K.C.accent})`; compound locks stack two icons side by side at s 44.
- lanterns: three `K.icon('lantern', x, 230, 44)` at x 860 / 960 / 1060 on a `K.line` string at y 200; lit = gold `K.glow`.
- **"left" layout** (scenes 06–11): the same building at scale 0.8 about its centre, translated so its centre sits at x 520
  (`K.at(520 - 960*0.8, ..., 0.8)`), stone top at y ~730; the right column x 1000–1800 holds that scene's content. The building
  slides between layouts with `K.io` 0.8 s, never redrawn from scratch.
- Speed labels (used 01, 05, 14, 15): `K.text` 'ui' 600, 30, left-aligned at x 1320: "barely moves" (y 760, gold), "every year"
  (y 448, `K.C.strong`), "fastest" (y 618, `K.C.accent`), "fastest of all" (y 238, `K.C.accent`), each with a short `K.arrow`
  pointing back at its part.

All text inside x 80–1840, y 130–930; nothing essential below 930. Labels ≤ 8 words, ≥ 26 px (eyebrows 20 px). One `'back'`
per scene at most. "Broken" is shown by dimming to `K.C.quiet` and a soft diagonal `K.line` (dashed), never red, never a cross.

## 01 — Old stone, fresh paint, new locks
**Metaphor object:** the building, full layout, as a ghost (0.15) under the title; the street of years ghosted at y 860.
**Frame:** title card, noBadge. `K.plate('plate', t, {zoom: true, shade: 0.5})` when `K.img.plate` exists, else
`K.bg({glow: 0.6, glowX: 960, glowY: 280})` (complete on `K.bg()`; the plate only adds atmosphere). `K.petals(t, {n: 6})`.
From frame 0, in the top band: eyebrow "00.03 · ORIENTATION" (960, 150); `K.title('How old is all this?', 960, 220, {size: 80})`;
purpose line ('read' 32, `K.C.strong`, centred, y 290): "How old your tools are, and how fast each part changes."
The building sits below, full layout but scaled 0.7 about (960, 640) so its roof clears y 330; ghosted 0.15.
**Beats:**
- `[[conclusion]]` conclusion line rises (`K.rise`, 'read' 30, `K.C.body`, y 340): "Decades-old ideas. Never frozen."
  The ghost building fades up to 0.6.
- `[[slow]]` the stone brightens to full, gold edge glows; speed label "barely moves" settles beside it (scaled positions).
- `[[medium]]` the sign pill reads "v1" then repaints to "v2" (the repaint move); label "every year".
- `[[fast]]` the door lock swaps key → lock → shield in quick 0.4 s steps; label "fastest" (terracotta).
- `[[ai-fastest]]` the three lanterns over the roof light left to right (`K.stagger` step 0.15; the scene's one `'back'` on the first);
  label "fastest of all".
**Exit:** title, purpose and conclusion held; the building lit with its four speed labels, lanterns swaying gently, petals drifting.

## 02 — Where it lives
**Metaphor object:** the course map; the lanterns are held back so they can be "strung up last".
**Frame:** `K.bg()`, then `K.map.draw(t, { t0: 0, focus: '00', dim, pin: '00', pinDrop, pinGlowK, lanterns: L, lanternLabels: LL })`,
full canvas. `lanterns: 0`, `lanternLabels: 0` until named.
**Beats:**
- `[[pin]]` pin drops on 00 (Start, y 408): `pinDrop = K.io(t, S.cue('pin'), .7, 'back')` (the scene's one overshoot), `pinGlowK`
  eases 0 → 1 over 0.6 s; `K.withCam` eases toward Start (z 1 → 1.25, target from `K.map.chipPos('00')`) over 0.8 s.
- `[[districts]]` camera eases back to z 1; the six districts brighten from `dim` 0.6 to 0.3 one by one (`K.stagger` step 0.12).
  A 20 px gold eyebrow "OLD STREETS" fades in centred at y 572, between the rows. On "Code" (`S.find('Code')`) row 05 Packages
  washes gold (`K.rr` around `K.map.chipPos('05')`) with a 26 px pill "versions" beside it; on "History" (`S.find('History')`) row 08
  washes the same way with a pill "git". Both washes ease back to 0.4 on `[[trust]]`.
- `[[trust]]` a gold `K.ring` draws around Trust (`K.map.district('trust')`: centre x 960, rows y 584–920; `rot: 0`) and its rows 14 and 15
  wash (`K.rr` around `K.map.chipPos('14')`, `chipPos('15')`); a small `K.icon('lock', d.x + d.w - 40, d.y + 40, 34, {color: K.C.accent})`
  appears in the card's top-right corner. The eyebrow swaps to "LOCKS · LATER, IN TRUST" (terracotta).
- `[[lanterns]]` `lanterns: (i) => K.stagger(t, S.cue('lanterns'), i, .15)` lights the six lanterns, then `lanternLabels` fades in;
  on "rehung" (`S.find('rehung')`) each lantern does one small extra sway (`K.wave` amplitude ×2 for 1 s, then back).
**Exit:** whole map, Start pinned and glowing, Trust ringed, lanterns lit, eyebrow faded.

## 03 — Missing the oldest things
**Metaphor object:** Aaron's four missing things, each getting a year stamp (those years are buildings on the street in 04).
**Frame:** reuse v1 scene 03 as is (`drafts/v1/scenes/03.js`): `K.bg({glow: .5, glowX: 620, glowY: 480})`; Notepad window
`K.win(200, 230, 840, 520, {title: 'script.txt - Notepad', kind: 'notepad'})` with three plain lines; right column x 1180–1760.
**Beats:**
- `[[notepad]]` Notepad rises, editor types (`typeAt` = cue, cps 24); `K.file(1300, 330, 110, {ext: 'txt', name: 'script.txt', nameSize: 26})`.
- `[[rename]]` dashed `K.arrow` to a ghost `K.file(1580, 330, 110, {ext: 'py', name: 'script.py', nameSize: 26})` at 0.35.
- `[[terminal]]` ghost `K.win(1180, 470, 580, 190, {kind: 'terminal'})`, `K.term` with neutral `$` and `cd python` typed faintly.
- `[[venv]]` `K.folder(1300, 760, 90, {name: '.venv', nameSize: 26})` at 0.5 with `K.icon('question', 1380, 735, 34)`. Year pills stamp on
  each spoken year: `S.find('1985')` on the Notepad title bar · `S.find('1991')` on script.py · `S.find('1971')` "Unix shell · 1971" on
  the terminal · `S.find('2012')` on .venv (`'back'` on the first only).
- `[[oldest]]` everything but the four year pills dims to 0.4; line at y 880 ('read' 32, `K.C.strong`): "Not the latest things. The oldest."
**Exit:** dimmed objects, four gold year pills glowing, the line held.

## 04 — One long street of years
**Metaphor object:** the street of years, drawn in full (v1's `M.street`); every year pill is a building's birthday.
**Frame:** reuse v1 scene 04 (`drafts/v1/scenes/04.js`) with one change: no Ethernet gloss (the narration lost it), and the
closing brackets stay. `K.bg({glow: .4, glowX: 265, glowY: 560})`, glow x easing along with the newest lit year; lantern string
ghosted (0.15) at the far right from frame 0.
**Beats:**
- `[[seventies]]` street draws to 1976; "1969 · Unix" above (265, 470), "1973 · Ethernet" below (370, 650), each on its spoken year.
- `[[eighties]]` to 1986; "1981 · MS-DOS" (580, 400), "1983 · DNS" (632, 720, `K.icon('globe')`).
- `[[nineties]]` to 1999; "~1991 · web · Python · Linux" (842, 470), "1995 · JavaScript" (947, 650).
- `[[two-thousands]]` to 2018; "2005 · Git", "2008 · GitHub", "2013 · Docker", "2015 · VS Code" stagger on each spoken name.
- `[[far-end]]` street completes to 2026; lanterns light on `S.find('Copilot')`, `S.find('ChatGPT')`, `S.find('November')` with terracotta
  pills right-aligned at x 1800 (y 360 / 420 / 480). On `S.find('fifty')` the two brackets at y 800: "50+ years of street" (gold) and
  "a few years of lanterns" (terracotta, right-aligned at 1800), 30 px.
**Exit:** whole street with every pill, brackets held, lanterns glowing.

## 05 — Stone, paint and lock
**Metaphor object:** the building is born from the street: the "~1991 · Python" pill lifts and becomes the building (Python is the
building whose stone, paint and lock the next scenes keep using).
**Frame:** `K.bg({glow: .45, glowX: 960, glowY: 520})`. Start frame = 04's exit; the brackets fade; the street dims to 0.3 and slides
down to y 900 (0.8 s), staying as a reminder strip with its pills hidden except "~1991".
**Beats:**
- `[[birthday]]` (the scene's first words; the scene opens calm on 04's exit) a soft `K.ring` passes over "~1991" on the strip; a pill "a birthday, not a finish line" (30, gold) rises at (960, 200),
  and holds until `[[building]]`.
- `[[building]]` the birthday pill fades; from the "~1991" pill a building grows upward into the full layout (stone, then walls and roof,
  then door, staggered 0.15 s; the scene's one `'back'` on the walls' scale). Small mono eyebrow on the roof peak: "PYTHON · 1991" (20 px,
  `K.C.soft`, (960, 280)).
- `[[stone]]` the stone's edge lights gold; three small line icons appear inside it, left to right, on the spoken nouns: `K.icon('book')`
  on "file" (`S.find('file')`), `K.icon('check')` on "commit", `K.icon('envelope')` on "message" (s 34, at x 820 / 960 / 1100, y 735;
  the eyebrow "STONE · THE IDEA" moves to y 790). Label "barely moves" at x 1320, y 760.
- `[[paint]]` the sign pill appears blank, then paints "Python 3.13" (repaint move); label "every year" at x 1320, y 448.
- `[[lock]]` the door's `K.icon('lock')` appears; on "scrambled" (`S.find('scrambled')`) a small `K.icon('key')` turns inside it
  (rotation 0 → 0.5 rad). On "burglars" the lock does a small shake (±4 px, 0.4 s); label "fastest" (terracotta) at x 1320, y 618.
**Exit:** one lit building, three speed labels, the dim street strip at the bottom.

## 06 — The paint: old tools, new versions
**Metaphor object:** the building's sign, repainted again and again (building in "left" layout).
**Frame:** `K.bg({glow: .4})`. The building slides to the left layout (0.8 s, starting at local t 0). The roof eyebrow becomes a
small tab row above the roof, two tabs at (400, 260) and (640, 260): `K.pill('git', ...)` and `K.pill('Python', ...)` (26 px),
the active one gold. Right column x 1060–1780: a vertical "paint log": dated rows, each a mono year (26, `K.C.head`) at x 1080 and a
label ('ui' 30, `K.C.strong`) at x 1200, rows y 300, 390, 480, 570, 660.
**Beats:**
- `[[git-paint]]` tab "git" active; roof eyebrow "GIT · 2005"; the sign keeps "git checkout" at full brightness while "git switch" slides in beside it (mono 30; checkout still works, nothing is replaced). Log row 1:
  "2019 · git switch, git restore".
- `[[main]]` the sign gets a second line: a pill "master" (`K.C.soft`) slides off left as a pill "main" (gold) slides in; log row 2:
  "2020 · GitHub: main, not master".
- `[[python-paint]]` tab "Python" active; eyebrow "PYTHON · 1991"; the sign repaints through "3.11" → "3.12" → "3.13" (one repaint
  per 0.5 s, the last on "October"); log row 3: "every October · new version". On "retired" a ghost pill "Python 2" (`K.C.quiet`) at
  (520, 880) gets a dashed strike; log row 4: "2020 · Python 2 retired". On "threads" (`S.find('threads')`) four small squares (`K.card`
  40×40, r 6) appear beside the sign, one lit; on "once" (`S.find('once')`) all four light together: the experimental free-threaded
  build. Log row 5: "2024 · 3.13 · optional no-GIL build".
- `[[editor-paint]]` a third tab "VS Code" appears and goes active; the sign shows a small label "monthly" that
  repaints to "weekly · 2026" on "2026" (`S.find('2026')`, 06's repaint move, then holds; no flashing); no log row (the log stays at five).
- `[[same-stone]]` the stone glows gold steadily while the sign does one last repaint; a line at y 880 ('read' 32, `K.C.strong`,
  centred at 960): "Same stone. Fresh paint."
**Exit:** building (left) with "VS Code" sign, the five-row paint log, the line held.

## 07 — The market that never closes
**Metaphor object:** the building's paint now comes from a market: stalls of packages beside it.
**Frame:** `K.bg({glow: .4, glowX: 1300})`. Building stays left (log from 06 fades out). Right side: two market stalls, `K.card`
340 × 300 at (1060, 230) and (1440, 230), eyebrows "NPM · JAVASCRIPT" and "PYPI · PYTHON" (20 px), each holding small package
`K.file` icons (s 60, `nameSize: 26` not needed: unlabeled) that arrive from above in a slow loop (deterministic: `K.rng(7)` sets
x offsets; one new box every ~0.8 s, pure function of t).
**Beats:**
- `[[market]]` stalls rise (`K.stagger`); package boxes start arriving; a `K.icon('clock', 1440, 580, 34)` with label "every day" (26).
- `[[semver]]` a big version pill at (1340, 640): mono 40 "2.4.1"; under each part a 26 px label: "2" → "may break" (terracotta),
  "4" → "new features", "1" → "fixes" (`K.C.soft`). The "2" glows on "first part".
- `[[lockfile]]` a `K.file(1200, 830, 70, {ext: 'lock', name: 'lockfile', nameSize: 26})` slides beside the building; a short gold
  `K.arrow` from the version pill into it; the sign on the building stops flickering (frozen to the pinned version).
- `[[supply-chain]]` a box in the npm stall labelled "colors-kit" (mono 26) gets a look-alike neighbour "co1ors-kit" (mono 26,
  `K.C.accent` outline); a small `K.icon('question', ...)` hovers over it. (Invented names only: no real package or attack on screen.)
  On "pin" (`S.find('pin')`) a small `K.icon('pin', ...)` drops onto the lockfile and the version pill gets a thin gold `K.ring`
  (rot 0): pinned, updated on purpose.
- `[[tools]]` three pills along y 850 (x 1060, 1360, 1660): "pip", "Poetry · 2018", "uv · 2024" (26 px), each popping on its spoken name
  (`S.find('pip')`, `S.find('Poetry')`, `S.find('2024')`); the row sits at y 850, with "all still in use" (26, `K.C.soft`) centred
  under it at y 900 (inside the safe area).
**Exit:** two stalls with slowly arriving boxes, the version pill, the lockfile beside the building, the tool row.

## 08 — The lock: from passwords to codes
**Metaphor object:** the building's door lock, replaced step by step. The paint and market fade; the camera eases in on the door.
**Frame:** `K.bg({glow: .5, glowX: 520, glowY: 620})`. `K.cam` eases from z 1 to z 1.15 toward the door (left layout) over 0.8 s.
Right column: the **lock line**, a horizontal row of five lock stages that will run across scenes 08 and 09, at y 300, x 1060 → 1760
(stage centres x 1090, 1240, 1390, 1540, 1690), each a `K.iconTile` s 90 with a 26 px
label under it at y 380; stage 4–5 slots are empty dashed tiles until 09.
**Beats:**
- `[[password]]` door shows `K.icon('key')` alone; tile 1 "password" (`K.icon('key')`). On "leaked" the key icon dims and a faint
  copy of it drifts away right (0.8 s): copied and reused.
- `[[two-factor]]` the door gets a second icon beside the key (stacked lock): `K.icon('phone')`; a 30 px line under the door
  "know + have" ('ui' 600, gold).
- `[[sms]]` tile 2 "text code" (`K.icon('envelope')` on a phone). On "SIM" (`S.find('SIM')`) a small diagram in the right column at y 520–700:
  `K.icon('phone', 1180, 600, 60)` (yours) and `K.icon('phone', 1600, 600, 60)` (theirs), a dashed terracotta `K.arrow` carrying a pill
  "your number" from the left phone to the right one. On "2017" tile 2 dims to 0.4 and gets the soft dashed diagonal; a 20 px eyebrow
  "NIST · 2017 · RESTRICTED" under it (y 420).
- `[[app]]` tile 3 "authenticator app" (`K.icon('clock')` inside a phone: time-based codes); the SIM-swap diagram fades; in its place a
  phone card showing a mono 40 six-digit code "482 913" with a draining `K.line` under it and a 26 px label "new code every 30 s";
  the drain is sped up on screen (one roll every 3 s, digits from `K.rng`, pure of t, no flashing). Eyebrow "STANDARD · 2011".
  The door's phone icon gains the clock.
- `[[push]]` the phone card's code is replaced by a small `K.note` "Was this you?" with two pills "Yes" (gold) and "No" (`K.C.soft`);
  "Yes" glows once on "this you".
**Exit:** door with key + app, three tiles filled (tile 2 dimmed), the push prompt held.

## 09 — The lock: your device is the key
**Metaphor object:** the same door and the same lock line; the key and code are replaced by the device itself.
**Frame:** continues 08's layout and camera (z 1.15 on the door); the push prompt fades out at local t 0.
**Beats:**
- `[[device]]` tile 4 "your device" (`K.icon('laptop')`); the door's key icon slides off and fades; the phone icon moves to the
  centre of the door.
- `[[passkey]]` tile 5 "passkey" (`K.icon('key')` inside `K.icon('phone')`); in the right column at y 520–760 a mini diagram:
  phone (1180, 640) holding a small gold key, site `K.win(1460, 540, 300, 200, {kind: 'browser', title: 'site'})`; on "never sent"
  a dashed `K.arrow` starts from the phone toward the site and stops halfway, the key staying put (no arrowhead reaches the site).
  On "fake" (`S.find('fake')`) a second, slightly crooked browser window (title "examp1e-login", invented, terracotta outline) slides
  in behind the first at 0.7 alpha, with a 26 px pill "nothing to steal" (`K.C.soft`) under it.
  Pills "face", "fingerprint", "PIN" (26) pop around the phone on their spoken words. Eyebrow "WEB STANDARD · 2019" then
  "APPLE · GOOGLE · MICROSOFT · 2022" (20 px, y 470) on their years.
- `[[no-password]]` tile 1 "password" fades to 0.3 and slides left out of the row; the row recentres (0.6 s).
- `[[required]]` the passkey diagram fades to 0.3; two notes rise in turn on their years, `K.note` at x 1180, width 560, `size: 26`,
  y 640 and 790: 'GITHUB · 2021' "No account passwords for git" (`S.find('2021')`) and 'GITHUB · 2023' "Two factor required to
  contribute code" (`S.find('2023')`). The door frame gets a thin terracotta `K.ring` (rot 0): not optional anymore.
- `[[old-lock]]` the camera eases back to z 1; the lock line's dimmed tiles (password, text code) settle under a gold 26 px label
  "the old locks" and the live tiles under "today's locks" (terracotta). The scene's one `'back'`: the passkey tile's settle.
**Exit:** door with the phone/passkey lock, the lock line sorted old → today, the two GitHub notes held.

## 10 — A gatehouse for everything
**Metaphor object:** a gatehouse is built at the end of the street: the building's lock now points to it.
**Frame:** `K.bg({glow: .4, glowX: 1400})`. The lock line and diagrams fade; the building stays left at scale 0.8. The dim street
strip returns along y 900 (0.3 alpha, no pills).
**Beats:**
- `[[gatehouse]]` a gatehouse card rises at right: `K.card(1240, 300, 440, 300, {r: 24})` with `K.icon('shield', 1460, 390, 64)` and the
  label "logins" ('ui' 600, 30); a pill "Sign in with Google" (26) under it at (1460, 540). A dashed gold `K.arrow` from the
  building's door to the gatehouse: the door no longer checks keys itself.
- `[[service-everything]]` the gatehouse shrinks (0.6 s) and two more small gatehouses (card + shield/lock icon, same style) join it in a
  column at right, each with a 26 px tag on its spoken word: "logins" (the first one), "secrets", "keys". A dashed gold arrow runs from the
  main building's door out to each gatehouse (staggered): one separate service per job, not everything through the login service.
- `[[aaron-work]]` an inset `K.note(140, 250, 640, 'AARON, AT WORK', '', ...)` replaces the building's sign area (the building dims to
  0.3 behind it). Inside: a `K.icon('person', 220, 360, 48)` labelled "personal account" (26) with a dashed arrow to three pills that
  pop on their spoken names, stacked at x 520, y 340 / 400 / 460: "service accounts", "Credential Manager", "Entra app registration"
  (26 px). The person icon dims once the arrow lands: the automations stop riding on him. On "job" (`S.find('job')`) a 30 px line
  ('read', `K.C.strong`) under the inset: "A login for the job, not the person."
- `[[renamed]]` the "Entra app registration" pill repaints (06's repaint move, reused on purpose) from "Azure Active Directory" to
  "Microsoft Entra", with a 20 px eyebrow "RENAMED · 2023" above it.
**Exit:** building (dim) with Aaron's inset, the three gatehouses (logins, secrets, keys) with the door's arrows into them, the renamed pill held.

## 11 — The metal wears out
**Metaphor object:** the lock opened up: its metal (the math) shown as a row of lock cores that age and crack.
**Frame:** `K.bg({glow: .45, glowX: 960, glowY: 520})`. The gatehouses and inset fade; the building's door lock flies to the centre
and grows into a large cut-away lock: `K.icon('lock', 960, 330, 120, {color: K.C.accent})` with a 26 px label "the metal: the math".
Below it a "metal shelf": five `K.card`s 260 × 150 at y 560, centres x 290, 620, 950, 1280, 1610, each with a mono 30 name and a mono 22
year eyebrow, appearing on their beats.
**Beats:**
- `[[metal]]` the big lock's shackle opens and closes once (tilt 0.2 rad, 0.6 s); on "faster" a `K.icon('gear', 1300, 330, 48)` starts a
  slow turn beside it.
- `[[hashes]]` card 1 "MD5" (eyebrow "BROKEN · 2004") rises and immediately dims to `K.C.quiet` with the soft dashed diagonal.
  On "S H A 1" (`S.find('fell')`) card 2 "SHA-1" rises; two small `K.file` icons (s 60, `ext: 'pdf'`) appear over it, a gold `K.arrow`
  from each into one shared mono pill "same fingerprint" (26); then the card dims with the diagonal; eyebrow "BROKEN · 2017".
- `[[tls]]` card 3 "TLS" rises with a mini browser address bar (`K.win(..., {kind: 'browser', url: 'https://', urlLock: true})`
  squeezed into the card) that stays at full brightness, padlock lit; inside the card a mono version chip "TLS 1.0 · 1.1" dims with the soft
  dashed diagonal while a small "TLS 1.3" chip beside it stays lit (only the old versions retired, HTTPS itself is fine); eyebrow "RETIRED · 2021". On "quantum" (`S.find('quantum')`) card 4 "post-quantum" rises at full
  brightness, gold edge glow, eyebrow "NIST · 2024" (the scene's one `'back'`).
- `[[git-hash]]` card 5 "git" shows the mono pill "SHA-1" sliding out and "SHA-256" sliding in (06's repaint move), eyebrow "MOVING";
  the gold arrow of time `K.arrow(290, 700, 1610, 700)` draws under the shelf: old cores dim on the left, new ones bright on the right.
- `[[breaks]]` the big lock's shackle lifts on its own (0.6 s) and a terracotta door-gap glow opens behind it; two lines at
  y 820 / 870 ('read' 32): "Real street: an old lock has charm." (`K.C.body`) / "Software: someone may have learned to pick it."
  (`K.C.strong`).
**Exit:** the shelf of five cores old → new, the open lock, the two lines held.

## 12 — The surprises you'll hit
**Metaphor object:** the building, small (scale 0.45) at top centre (960, 230), with a gold/terracotta marker that jumps to the part
each surprise lives in: sign (paint) or door (lock).
**Frame:** `K.bg({glow: .4})`. Five cards in a 3 + 2 grid: row 1 centres x 380, 960, 1540 at y 480; row 2 centres x 670, 1250 at y 760;
each `K.card` 500 × 230, r 24, with a 20 px eyebrow (the part) and one literal form in mono 30.
**Beats:**
- `[[tutorial]]` card 1 (eyebrow "PAINT"): a mini `K.win(..., {kind: 'terminal'})` with `K.term`: `$ tool --old-flag` then the output
  line "unknown option '--old-flag'" (`K.C.soft`). Marker on the sign.
- `[[master-main]]` card 2 ("PAINT · GITHUB 2020"): two branch pills side by side, "master" (`K.C.soft`) and "main" (gold), joined by a
  26 px "=".
- `[[deprecated]]` card 3 ("PAINT"): mono line `npm warn deprecated` (`K.C.head`, not red) with the label "still works, plan to move"
  (26, `K.C.body`).
- `[[python-two]]` card 4 ("PAINT · PYTHON 2"): `print "hello"` (dim, `K.C.quiet`) above `print("hello")` (full).
- `[[forced]]` card 5 ("LOCK"): a mini sign-in screen (`K.win(..., {kind: 'browser'})`) with the 26 px line "Set up an authenticator
  app to continue" and a `K.icon('phone')`; marker jumps to the door (terracotta). On "replaced" (`S.find('replaced')`) the small
  building's door lock does 08's swap move once.
**Exit:** five cards resting, the small building with its marker on the door.

## 13 — The lantern: newest and fastest
**Metaphor object:** the building back at full layout, lanterns over the roof brighter than ever; an agent (sparkle) beneath them.
**Frame:** `K.bg({glow: .5, glowX: 960, glowY: 220})`. Building full layout but shifted left to centre x 700 (scale 0.9) so the right column
x 1240–1780 is free. The dim street strip at y 900.
**Beats:**
- `[[models]]` the three lanterns swap one by one for new ones: each old lantern fades and a new one drops in on its string (0.5 s,
  `K.stagger` step 0.3), then the first does it again: the fastest swap rate in the lesson. 20 px eyebrow "EVERY FEW MONTHS" (y 150).
- `[[stale]]` a `K.icon('brain', 1360, 330, 60)` with a vertical dashed `K.line` labelled "training ended" (26); three greyed mono
  chips stack at x 1500, y 450 / 510 / 570, appearing on their spoken nouns: "old version", "retired command", "old login"; each draws
  a thin dashed arrow to the matching part of the building (sign, sign, door).
- `[[agent]]` `K.icon('sparkle', 700, 250, 56)` (the agent) drops under the lanterns and three mono chips travel from it to the stone:
  "cd project", ".venv", "git commit" (26), landing inside the stone on "C D", "V E N V", "git". The stone glows gold: it works on old ground.
- `[[check]]` a gold `K.ring` (rot 0) circles the sign and the door in turn; `K.icon('chat', 1300, 700, 40)` with the pill
  "which version are you assuming?" (30, gold) at (1540, 700).
- `[[light]]` the recurring line ('read' 34, `K.C.strong`, centred, y 820): "It lights every district. It doesn't walk the streets for you."
  Lantern light spreads down over the whole building (`K.glow` growing over 1.2 s).
**Exit:** lit building, agent's chips resting in the stone, the line held.

## 14 — Safe to ignore for now
**Metaphor object:** the building and lanterns as a sorting key: four labelled parts.
**Frame:** `K.bg()`. Building full layout at scale 0.85, centre x 700. Three ignore pills at the top (y 180, x 560, 960, 1360), 30 px,
`K.C.soft`, each getting a soft `K.mark` underline in `K.C.quiet` as it is dismissed.
**Beats:**
- `[[no-dates]]` pill "memorizing dates" appears; on "which algorithm" a second pill "which algorithm replaced which".
- `[[no-chase]]` pill "every release"; all three dim to 0.5. On "Security" (`S.find('Security')`) a fourth pill under the row at
  (960, 250), "except security updates: take those" (30, `K.C.accent` outline, full brightness): the only one that does not dim.
- `[[question]]` `K.pill('street or lantern?', 1440, 340, {size: 34})` rises (the scene's one `'back'`); on "which part" (`S.find('which part')`)
  it gets a second line, 30 px gold "which part?".
- `[[answers]]` the four speed labels, now as rules, settle beside their parts on each spoken word (`S.find('Stone')`, `'Paint'`, `'Lock'`,
  `'Lantern'`), 30 px at x 1240: "stone · learn it once" (y 760, gold), "paint · check the version" (y 448, `K.C.strong`),
  "lock · assume it changed" (y 618, terracotta), "lantern · check the date" (y 238, terracotta), each with a short `K.arrow` to its part.
**Exit:** the building with its four rules, the question pill held, ignore pills dimmed.

## 15 — Keep this
**Metaphor object:** the building, small, bottom-right (scale 0.4, centre x 1620, y 760, 0.6 alpha), lanterns glowing, a fresh sign.
**Frame:** end card, noBadge. `K.plate('plate', t, {zoom: true, shade: 0.55})` when available, else `K.bg({glow: 0.6})`. `K.petals(t, {n: 5})`.
Eyebrow "KEEP THIS" (960, 170). Three rows left-aligned at x 200, y 300 / 480 / 660: bold lead ('ui' 600, 36, `K.C.head`) and a 'read' 30
`K.C.body` line under it (`K.para`, width 1100 so it clears the building).
**Beats:**
Each bold lead is the action (mirrors 14's rule); the 'read' line under it is the reason.
- `[[keep-1]]` row 1: **Learn the old ideas once.** / "Files, the shell, the web and git had decades to settle."
  The small building's stone glows on "old".
- `[[keep-2]]` row 2: **Check the version.** then, on "assume", **Assume the lock has changed.** / "Versions move every year, and
  security moves faster still." The sign repaints once on "version" and the door lock swaps once on "lock".
- `[[keep-3]]` row 3: **Check the date on anything AI tells you.** / "It is the newest and fastest of all, especially about versions
  and locks." The lanterns brighten on "AI".
**Exit:** three rows held, the small building lit at bottom right, petals drifting.
