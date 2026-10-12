# 01.01 — Files are just bytes · storyboard (final; spine from draft A, grafts from B and C)

**The persistent object: the string of beads with a paper tag.** A horizontal cord (`K.line`, `K.C.line2`, w 4) with
12 beads. Each bead is a `K.card` 76 × 76, r 38 (a circle), fill `K.C.tile`, stroke `K.C.line2`, holding its byte value in
`K.text` 'mono' 28 `K.C.strong`. Standard position: beads centred on y 520, x = 400 + 100·i (i 0..11, x 400–1500).
The string reads `112 114 105 110 116 40 34 104 105 34 41 10` (`print("hi")` plus a newline in UTF-8; the numbers are real).
At the left end a short cord runs to a **paper tag**: `K.card` 260 × 90, r 12, fill `K.C.paper` at 0.9, slight tilt
(`K.at(..., rot -0.06)`), name in `K.text` 'mono' 34 `K.C.page`, hung at (230, 520). The tag starts as `hello.txt`.
Build it once as a helper (`drawString(t, {x, y, s, tag, letters, stamp, fold, faint})`) and only move, scale or add a
layer (code card, stamp, fold) to it; never redraw it as a different object. All text in x 80–1840, y 130–930; nothing
essential below 930. Labels ≤ 8 words, ≥ 26 px. At most one `'back'` overshoot per scene. No red, no flashing; "wrong"
is `K.C.accent` with a soft `K.ring`.

## 01 — Bytes inside, a label outside
**Metaphor object:** the string of beads, small, as the title card's emblem.
**Frame:** title card. `K.plate('plate', t, {zoom:true, shade:0.45, mask:[640, 860]})` when `K.img.plate` exists, else `K.bg({glow:0.6, glowX:960, glowY:300})`; the layout is identical either way (all type sits on the dark upper band). `K.petals(t, {n:5, avoid:[[160,150,1760,420],[300,560,1620,780]]})`. Eyebrow "01.01 · YOUR COMPUTER, UNDER THE HOOD" (20 px) at (960, 170) centred. `K.title('Files are just bytes', 960, 250, {size:84, align:'center'})`. Purpose line from frame 0 (`K.text` 'read' 32 `K.C.body`, centred, y 320): "What a file is, and what .py does". The string at scale 0.7 centred at (960, 640), beads ghosted (alpha 0.15) from frame 0. noBadge.
**Beats:**
- `[[headline]]` beads light left to right (`K.stagger` step 0.08), numbers fade in; the tag `hello.py` swings in on its cord (the scene's one `'back'`). Conclusion rises under the purpose line (`K.text` 'read' 40 `K.C.head`, y 390): "Bytes inside, a label outside."
- `[[not-inside]]` a gold `K.mark` underlines the tag and a pill "label" (26 px) sits above it; a second pill "contents" sits above the beads.
- `[[agents]]` `K.icon('sparkle', 1560, 560, 56, {color:K.C.gold})` drifts in from the right and settles near the string's end with a soft `K.glow`.
**Exit:** title, both lines, the lit string with its two pills; sparkle resting.

## 02 — Where it lives: a dot T X T
**Metaphor object:** the course map, then Aaron's file (the string waits off-screen and returns in 03).
**Frame:** `K.bg({glow:0.45})`. Full-canvas map first; midway it dims to 0.2 behind a Notepad window.
**Beats:**
- `[[pin]]` `K.map.draw(t, {t0:S.cue('pin'), focus:'machine', pin:'01', pinDrop:K.io(t, S.cue('pin'), .7, 'back'), lanterns:0.5})`; `K.withCam` eases toward `K.map.chipPos('01')` (z 1 → 1.3, 0.8 s). The pinned row "Your Computer, Under the Hood" washes gold; District 1's question stays lit.
- `[[notepad]]` camera eases back, map dims to 0.2; `K.win(260, 220, 820, 520, {kind:'notepad', title:'Untitled - Notepad', titleSize:26})` rises; `K.editor` types `print("hi")` (size 36, `typeAt` = cue, cps 14). `K.iconTile('cap', 1400, 260, 90)` with pill "IT degree" (26 px). A gold `K.arrow` curves to `K.file(1400, 520, 200, {ext:'txt', name:'script.txt', nameSize:30})`.
- `[[rename]]` the file's label crossfades `script.txt` → `script.py` (ext 'txt' → 'py'); a soft `K.ring` circles only the ending; pill "only the label changed" (26 px) at (1400, 700). The editor text does not move.
- `[[missing]]` nothing new is drawn; the ring fades and a quiet line (`K.text` 'read' 30 `K.C.soft`, centred, y 820): "a missing semester".
**Exit:** Notepad with `print("hi")`, `script.py` icon, map faint behind.

## 03 — A string of beads with a tag
**Metaphor object:** the string of beads, at standard position and full size, for the first time.
**Frame:** `K.bg({glow:0.4, glowX:960, glowY:520})`. The cord draws across (`K.line` k 0 → 1 over the first 0.8 s), no beads yet. Eyebrow "ONE FILE" (20 px) at (960, 300).
**Beats:**
- `[[beads]]` beads drop onto the cord, staggered 0.1 s, numbers in; pill under bead 0 at y 640: "1 byte = 0 to 255" (30 px).
- `[[everything]]` four pills rise above the string at y 330 (x 660, 860, 1060, 1260): "photo", "song", "spreadsheet", ".py" (28 px); thin dashed `K.arrow`s fall from each to the cord. They fade by `[[tag]]`.
- `[[tag]]` the paper tag swings onto the left end (`hello.txt`); a gold `K.mark` underlines `.txt` and a pill "extension" (26 px) appears under the tag at (230, 620).
- `[[carry]]` the whole string slides right 120 px and back (0.8 s, `K.io`), as if carried; a faint `K.icon('question', 960, 400, 48, {alpha:0.4})` above the beads; quiet line `K.text` 'ui' 30 `K.C.soft` at (960, 760): "stored, moved, never understood".
**Exit:** the string at rest, tag `hello.txt`, "extension" pill resting.

## 04 — Text is an agreement
**Metaphor object:** the same string, gaining the **code card** layer.
**Frame:** `K.bg({glow:0.45, glowX:960, glowY:440})`. String at standard position. The code card is a translucent `K.card` 1240 × 120, r 20, fill `K.C.tile` at 0.85, stroke `K.C.gold`, eyebrow "CODE CARD" (20 px) at its top-left, held at y 300 until it slides down.
**Beats:**
- `[[code-card]]` the card fades in at y 300 with a small legend (`K.text` 'mono' 28): "112 → p   114 → r   105 → i"; the "112 → p" pair glows on "twelve".
- `[[letters]]` the card slides down over the beads (0.7 s, `K.io`); each bead's number crossfades to its letter, staggered 0.06 s: `p r i n t ( " h i " )` and a newline mark. The tag flips to `hello.py`. Pill below: "a .py file is text" (30 px); on "Nothing" (`S.find('Nothing')`) a dim pill "no 'Python' inside" (26 px) to its right.
- `[[garbled]]` the card shifts one notch, its stroke turns `K.C.accent` and its eyebrow reads "WRONG CARD" with a small mono tag "UTF-16"; the card reads the beads in pairs (thin brackets join each pair) and the twelve letters crossfade to six junk glyphs `牰 湩 ⡴ 栢 ≩ ੩` in mono (real: these 12 bytes decoded as UTF-16-LE); soft accent `K.ring`. Then it slides back and the letters return.
- `[[utf8]]` the eyebrow becomes "UTF-8"; two `K.note`s at y 700: (480, 700, 420) "WEB" / "≈99% of websites · W3Techs, Sep 2026"; (1020, 700, 420) "PYTHON 3.15" / "UTF-8 by default · due Oct 2026".
- `[[rendering]]` notes fade; `K.win(1180, 620, 560, 220, {kind:'notepad', title:'Notepad', titleSize:26})` shows **hi** in bold; at (760, 730) a mono strip `**hi**` with the stars ringed, and a thin `K.arrow` between them; pill "stored → shown" (26 px).
**Exit:** string under the UTF-8 card reading the Python line; Notepad mini-window and stored strip resting.

## 05 — The tag only picks the program
**Metaphor object:** the string with its card lifted away; the tag takes centre stage; a second string arrives.
**Frame:** `K.bg({glow:0.4, glowX:300, glowY:520})`. The code card fades off in the first 0.6 s; beads show numbers again. String scales to 0.8, centred at (900, 400), tag `hello.txt`. Right side reserved for programs.
**Beats:**
- `[[porter]]` a `K.icon('person', ...)` porter (s 64, `K.C.soft`) walks to the tag (0.8 s); a gold dashed `K.path` runs from the tag to `K.win(1460, 260, 360, 220, {kind:'notepad', title:'Notepad', titleSize:26})`. Pill "double-click reads the tag" (28 px) above the tag.
- `[[rename-py]]` the tag crossfades `hello.txt` → `hello.py`; the path re-routes to `K.win(1460, 260, 360, 220, {kind:'code', title:'Code editor', titleSize:26})`. Counter pill under the beads: "bytes changed: 0" (30 px, `K.C.gold`). Beads do not move.
- `[[python-runs]]` the tag flips to `notes.txt`; `K.win(1460, 540, 360, 200, {kind:'terminal', title:'Terminal', titleSize:26})` types `python notes.txt` → `hi` (`K.term`, size 26). Pill "the program ignores the tag" (26 px).
- `[[stamp]]` the first string shrinks up (scale 0.6, y 300); a second string slides in at y 640, its first four beads stamped gold and labelled `‰PNG` (mono 30); its tag reads `photo.jpg` with a dashed accent underline; gold `K.ring` round the stamp. Then a mini-row (s 0.5, y 800) stamped `%PDF-` and a pill ".docx = a zip inside" (26 px). On "Plain" (`S.find('Plain')`) the top string's first bead gets a faint empty ring: "no stamp".
- `[[breaks]]` the tag lifts off the first string (cord dashes, 0.6 s) and settles into a small `K.card` beside `K.folder(1500, 760, 160, {name:'folder', nameSize:28})` with rows "name · size · date" (`K.text` 'ui' 26). Eyebrow "WHERE THE PICTURE BREAKS" (20 px) above it.
**Exit:** PNG string with its stamp, folder card holding the name, tag cord dashed. Calm.

## 06 — The surprises you'll hit
**Metaphor object:** the tag, now misbehaving (folds, lies).
**Frame:** `K.bg({glow:0.35})`. Four surprise cards appear one per cue in a 2 × 2 grid (`K.card` 760 × 260, r 24, at (180, 200), (980, 200), (180, 500), (980, 500)); each holds one small drawing and a ≤ 6-word label (`K.text` 'ui' 30). The fifth surprise replaces the grid.
**Beats:**
- `[[hidden]]` card 1: a tag reading `hello.py.txt` folds its right end under (0.6 s), leaving `hello.py`; label "hidden extensions, still default".
- `[[png-jpg]]` card 2: a mini string stamped `‰PNG` whose tag swaps `photo.png` → `photo.jpg`; the stamp stays; label "renamed, not converted".
- `[[mojibake]]` card 3: mono `café` beside `cafÃ©`; label "wrong code card".
- `[[double-click]]` card 4: `K.file(.., {ext:'py', nameSize:26})` with three thin arrows fanning to `K.iconTile` 'code', 'file', 'question'; label "depends on the machine".
- `[[costume]]` the grid dims to 0.25; centred `K.file(960, 500, 240, {ext:'exe', name:'invoice.pdf.exe', nameSize:34})` whose name shows `invoice.pdf` with `.exe` folded away, then the fold opens (0.6 s); `K.icon('warning', 1260, 420, 64, {color:K.C.accent})`; pill "a tag can lie" (30 px) at y 760. No scare motion.
**Exit:** the unmasked `invoice.pdf.exe`, warning icon, pill; grid faint behind.

## 07 — The lantern: agents and your files
**Metaphor object:** the string of beads again (tag `hello.py`), now handled under the lantern.
**Frame:** `K.bg({glow:0.5, glowX:960, glowY:200})`. `K.map.lantern(t, 0, {x:960, y:170, glowK:1.8})` hangs top-centre. "Then" strip at (300, 300): `K.text` 'ui' 26 `K.C.soft` "then: you made every file". The string at scale 0.85, y 560.
**Beats:**
- `[[agent-hand]]` `K.icon('sparkle', ...)` (s 72, gold) drops from the lantern's glow to the string; pills "create", "read", "edit" (28 px) appear at y 420, staggered. "Then" dims; "now: agents work in your files" appears at (300, 340). On "pictures" (`S.find('pictures')`) two chips at y 740: "text → text", "image → picture".
- `[[agents-md]]` two files rise on the right: `K.file(1500, 560, 150, {ext:'md', name:'AGENTS.md', nameSize:26})` and `K.file(1700, 560, 150, {ext:'md', name:'CLAUDE.md', nameSize:26})`; a gold `K.ring` on the names only; pill "the name is the signal" (26 px); `K.note` "LINUX FOUNDATION" / "AGENTS.md · Dec 2025" (26 px) below.
- `[[magika]]` a thin gold scan bar (`K.line`, alpha 0.6) sweeps the beads left to right (1.2 s); pill "Google Magika: bytes, not names · since 2024" (26 px) at y 820. On "direction" (`S.find('direction')`) eyebrow "WHERE IT'S HEADING" (20 px) above the pill.
- `[[invisible]]` a short cluster of three faint dotted beads `226 128 139` (a zero-width space in UTF-8; alpha 0.3, dashed stroke) slides in between `h` and `i`; the sparkle's glow touches it; label "invisible to you, read by agents" (`K.text` 'ui' 28 `K.C.soft`).
**Exit:** lantern above, string with its faint three-bead cluster, the two instruction files at rest.

## 08 — Keep this
**Metaphor object:** one string, one tag, as the end-card emblem.
**Frame:** end card. `K.plate('plate', t, {shade:0.55, mask:[700, 880]})` if present, else `K.bg({glow:0.5})`; identical layout either way. `K.petals(t, {n:4, avoid:[[160,150,1760,860]]})`. Small string (scale 0.5) with tag `hello.py` at (960, 220). noBadge.
**Beats:**
- `[[ignore]]` five dim pills in a row at y 400: "hex", "bits", "UTF-16", "byte order marks", "line endings" (26 px, alpha 0.6), eyebrow "SAFE TO IGNORE FOR NOW" above them.
- `[[keep-1]]` the ignore pills fade; eyebrow "KEEP THIS" (20 px) at (960, 330); takeaway 1 at y 430 (`K.spans`, bold lead `K.C.head` 40 px, rest 'read' 32): **A file is just bytes.** "A string of numbers, each 0 to 255."
- `[[keep-2]]` takeaway 2 at y 540: **Text is bytes plus an agreement.** "Almost always UTF-8."
- `[[keep-3]]` takeaway 3 at y 650: **The extension is a label.** "It picks the program, not the contents."
- `[[next]]` quiet `K.text` 'ui' 28 `K.C.soft` at (960, 820): "Next on the map: 01.02 · File extensions & associations". No arrow, no teaser motion.
**Exit:** three takeaways, the emblem string, a few petals clear of the text.
