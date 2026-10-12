# 01.02 — File extensions & associations · storyboard (final: B spine, grafts from A and C)

**The one metaphor: the porter and the ledger.** It continues 01.01's string of beads (the bytes) with a paper tag tied
on the outside (the name). The porter is the operating system's file manager (File Explorer, Finder). The porter
stands at a desk with an open **ledger** (the file-association table). Behind the desk is a row of **doors**, each one a
program (drawn as `K.win` frames with a title, standing upright and narrow: Notepad, V S Code, Photos, Python, Browser).
The porter reads only the tag's last part, finds the row, and carries the string to that door.

How it transforms: the tag folds (05), gets rewritten (06), the porter is handed a note or a pen rewrites a row (07),
the ledger opens into a full book (08), other hands reach for the pen and some rows go behind glass (09), the ledger
splits into three (10), a small second ledger appears inside a door (11), a lantern-lit hand ties tags on new strings
(13), and the end card is one string, one tag, one ledger (14).

**Drawing kit only** (engine/KIT.md): the porter is a `K.icon('person')` at s 120 standing behind a `K.card` desk; the
ledger is a `K.card` (paper tone: `K.C.paper` at low alpha over `K.C.tile`) with mono rows `.txt → Notepad`, hairline
row dividers (`K.line`); the string of beads is a `K.path` (head: false) with small `K.glow` dots as beads; the tag is a
small `K.card` (r 10) hung by a `K.line` with mono text; doors are `K.win` frames (kind 'notepad'/'code'/'browser'/
'explorer', title 26 px); pens are drawn with `K.line` + a `K.pill`; glass is a translucent `K.card` with a
`K.icon('lock')`; agent hand is `K.icon('sparkle')` with `K.icon('lantern')` glow. Text inside x 80–1840, y 130–930.

**Standing layout (sections 03–09):** desk + porter left-centre (porter at x 420 y 470; desk card x 260–760, y 560–
700); ledger open on the desk, lifted into view as a card x 220–800, y 600–900 when read; doors in a row on the right
(x 1000–1800, door frames 150 × 360 at y 260–620, labels inside the title bar); the current string of beads enters
from the left at y 470. The camera (`K.cam`) moves between "desk" (x 520, z 1.25), "doors" (x 1400) and "whole room"
(z 1). Section 08 and 10 change the set; 11–13 return to the room.

---

## 01 — A label in the name, a ledger in the computer
**Metaphor object:** the string of beads with its tag `hello.txt`; the ledger appears as a closed book.
**Frame:** title card. Painted plate `K.plate('plate', t, { zoom: true, shade: 0.45, mask: [520, 760] })` in the lower
band if `teahouse-night.jpg` loads, otherwise `K.bg({ glow: 0.5, glowY: 700 })`. Purpose line as `K.title` (64 px)
centred at y 230, wrapped to 1400 px with `K.para`. Below it, the conclusion line "A label in the name, a ledger in the
computer." in Georgia italic 38 px at y 380. At y 560–720 a small still life: string of beads (x 620–1040) with tag
`hello.txt`, an arrow to a closed ledger card (x 1180–1360). `K.petals` with `avoid` around all text.
**Beats:**
- `[[headline]]` the tag on the string brightens and a pill "the extension = a label in the name" rises at y 820.
- `[[ledger]]` the ledger card opens (two halves slide apart) showing one row `.txt → Notepad`; pill swaps to "a table: label → program".
- `[[same-beads]]` the tag flips `hello.txt → hello.py` (text crossfade); the beads do not move (a tiny gold `K.ring` round the beads holds still). Pill: "rename = new label, same bytes".
- `[[edit]]` a pen (line + pill "Open with · Default apps") touches the ledger row and rewrites `Notepad → V S Code`.
- `[[agents]]` a `K.icon('sparkle')` drifts in from the right and ties a fresh tag `report.docx` on a second, shorter string; it sits beside the first. Pill: "AI makes files; the table still opens them".
**Exit:** the two strings, the open ledger, the conclusion line; petals settle. Calm.

## 02 — Where it lives: the rename Aaron didn't know
**Metaphor object:** the string with tag `hello.txt` (carried over from 01.01's look).
**Frame:** `K.map.draw(t, { focus: '01', pin: '01', pinDrop: K.io(t, pinA, .7, 'back'), lanterns: .5 })` full canvas,
then the camera eases into District 1 (target from `K.map.district('machine')`, z 1.6). Later the map dims to 0.2 and
a centred story frame takes over.
**Beats:**
- `[[pin]]` pin drops on Module 01 "Your computer"; the district question "what's on your computer" glows; small eyebrow "Module 01 · stop 2" next to the chip (`K.map.chipPos('01')`).
- `[[beads]]` map dims; the string of beads draws across x 560–1360 at y 480, the tag `hello.txt` swings on at its right end (sway via `K.wave`, small). Eyebrow "from 01.01: bytes inside, name outside".
- `[[notepad]]` a `K.win` kind 'notepad' (x 420–1100, y 300–700, title "hello.txt — Notepad") with three lines of Python in `K.editor` (`print("hello")` etc., no syntax colours); title bar titleSize 26; a card at right (x 1180–1640) reads "Aaron · IT degree · nobody told him"; a ghost tag `.py` hovers near the title bar, unattached.
- `[[why]]` the window shrinks into the string again; a hand-drawn arrow points at the tag, label "the why behind the rename".
**Exit:** string and tag alone, centre, gently swaying.

## 03 — The porter and the ledger
**Metaphor object:** the porter, the desk, the ledger, the doors (introduced here, persist through 09).
**Frame:** whole room. Porter + desk left, doors right: Notepad, V S Code, Photos, Browser (four `K.win` frames, 160 ×
360, x 1040/1240/1440/1640, y 280–640). The string with tag `hello.txt` lies at the porter's left (x 120–320, y 470).
**Beats:**
- `[[porter]]` porter icon pops in behind the desk (`K.pop`); two small pills under it "File Explorer" · "Finder" (Karla 28).
- `[[reads-tag]]` camera to desk (z 1.3). The tag enlarges; `hello` dims to 30%, `.txt` stays bright and a gold underline (`K.mark`) runs under it. Label "only after the last dot".
- `[[ledger-open]]` ledger card lifts up (x 220–800, y 560–900) with five rows: `.txt → Notepad`, `.py → V S Code`, `.png → Photos`, `.html → Browser`, `.pdf → Browser`.
- `[[finger]]` a gold highlight bar slides down the rows and stops on `.txt → Notepad` (`K.io`, 0.6 s).
- `[[carry]]` camera back to whole room; the string travels along a `K.path` from the desk to the Notepad door, which gets `focus: true` (gold stroke). The beads keep their spacing the whole way (never untied).
- `[[term]]` the ledger title writes itself "file associations" (mono 30); eyebrow "one row = one association".
- `[[per-user]]` the ledger duplicates: two ledger cards side by side, each under a small `K.icon('person')` labelled "you" / "a second account"; in the second, the `.txt` row reads `.txt → V S Code`. Label "one ledger per user".
**Exit:** one porter, one ledger (the second fades), string resting at the Notepad door.

## 04 — What a ledger row holds
**Metaphor object:** a single ledger row, pulled out and enlarged.
**Frame:** camera to desk; the `.py` row lifts out of the ledger and grows into a wide card (x 240–1680, y 360–600)
with four column cells.
**Beats:**
- `[[row-opens]]` the row card expands from the ledger (scale 0.4 → 1, `K.io`); label at its left `.py`.
- `[[columns]]` three cells stagger in (`K.stagger`): "door: V S Code" (with `K.icon('code')`), "icon" (a `K.file` ext 'py', s 120), "type name: Python file". Below the card, a `K.file` named `hello.py` (nameSize 30) at x 960, y 760.
- `[[menu]]` a fourth cell: a small stacked list "Open · Edit · Run" drawn as three thin pills; label "right-click menu".
- `[[icon-flip]]` the file below is renamed `hello.txt → hello.py` (name crossfade); the icon swaps on the same frame; the beads strip drawn under the icon (eight dots) does not move; caption "no bead moved".
- `[[no-row]]` a second file appears, `notes.xyz`, with a blank icon (`K.file` no ext, alpha 0.6) and a `K.icon('question')` above it; mono caption "Select an app to open this .xyz file" (30 px) at y 880.
**Exit:** row card, two files below it, calm.

## 05 — The folded tag: hidden extensions
**Metaphor object:** the tag, now folded at the last dot.
**Frame:** a tag enlarged to centre (x 560–1360, y 360–520), mono 56 px, plus the porter small at left. Later a
settings card at right.
**Beats:**
- `[[folded]]` the tag reads `hello.py.txt`; its right end folds back along the last dot (scaleX of the `.txt` part → 0, with a crease line), leaving `hello.py` visible. Date card at top: "Windows 11 26H2 · macOS 27 · still hidden by default · Oct 2026".
- `[[fold-trap]]` a dashed `K.ring` around the hidden part; small label below "still a text file"; the Notepad door glows faintly at right.
- `[[unfold]]` a gold pill "Show file extensions" slides in and the fold opens back out; `.txt` reappears in accent colour.
- `[[advanced]]` a settings card (x 1180–1720, y 600–780): eyebrow "WINDOWS 11 25H2+", line "Advanced (formerly For developers)". No path.
- `[[mac-per-file]]` two files in one folder (`K.folder` frame, x 260–860, y 600–860): `photo.png` shows its extension, `photo2` hides it; tiny label "Mac: hide extension, per file".
- `[[builders]]` the tag on the main string is shown unfolded, and a `K.icon('check')` settles beside the pill.
**Exit:** unfolded tag `hello.py.txt` centre, the pill, calm.

## 06 — Renaming: a new tag, the same beads
**Metaphor object:** the string and its tag; a second string `photo.png`.
**Frame:** room again (desk + doors). String `hello.txt` at the desk.
**Beats:**
- `[[rewrite]]` the tag text is crossed out (`K.line` through `.txt`) and `.py` writes itself in (`K.typed`); the beads hold still (gold ring around them). Card: "renaming won't convert · Microsoft".
- `[[aaron-payoff]]` the porter's highlight bar moves from `.txt → Notepad` to `.py → V S Code`; the string travels to the V S Code door, which opens to show the same Python lines, now with syntax colours (`K.editor` syntax 'py'). Small eyebrow "Aaron's fix".
- `[[png-jpg]]` second string with tag `photo.png` (beads a different colour) is renamed `photo.jpg`; the beads do not change (ring holds still); pill "nothing converts"; small caption "may still open · still a PNG".
- `[[export]]` a small `K.win` (title "Photos", x 1240–1720, y 640–880) shows two pills "Save As" · "Export"; an arrow from it produces a third string with visibly different beads. Card: "convert = inside an app".
- `[[warning]]` a `K.note` card with `K.icon('warning')`: eyebrow "RENAME WARNING", body "might become unusable · Keep .txt / Use .py" (paraphrased, not a dialog mock); a dotted arrow from the card to the ledger row labelled "you're moving rows".
- `[[classic-trap]]` a typed name field (`K.typed`) types `hello.py`; on Enter, a ghost `.txt` grows at the end (folded, faint) giving `hello.py.txt`. Pill: "can happen · hidden extensions". On "isn't" (`S.find('isn')`) the fold opens and `.txt` shows in accent.
**Exit:** two strings: `hello.py` at the V S Code door, `photo.jpg` beside the Photos door; calm.

## 07 — Open with: just once, or always
**Metaphor object:** a note handed to the porter; the pen over a ledger row.
**Frame:** desk close-up (camera z 1.3), ledger open, string `hello.py` in the porter's hand.
**Beats:**
- `[[note]]` a small paper card slides from the left into the porter's hand: "→ Notepad". Label "Open with".
- `[[once]]` two generic pills appear, "Just once" · "Always" (not a dialog mock); "Just once" lights; the string goes to the Notepad door; the ledger row `.py → V S Code` stays unchanged (it pulses once, untouched).
- `[[always]]` "Always" lights; a pen (line + nib) strikes `V S Code` in the `.py` row and writes `Notepad`; next, two more `.py` strings walk to the Notepad door.
- `[[mac-change-all]]` a Finder-style info card (`K.card`, eyebrow "MAC · FILE INFO") with "Open with: TextEdit" for one file and a pill "Change All".
- `[[per-file]]` two labels side by side: "Mac: per file" (a tag with its own little note pinned to it) · "Windows: per label" (a ledger row).
**Exit:** pen resting beside the ledger; row restored to `.py → V S Code` for continuity; calm.

## 08 — Default apps: the whole ledger
**Metaphor object:** the ledger, opened as a full book.
**Frame:** the desk recedes; the ledger opens to a two-page book card (x 200–1720, y 220–860). Left page "by label",
right page "by app". Eyebrow "DEFAULT APPS".
**Beats:**
- `[[book]]` ledger grows into the book (`K.io`, 0.8 s); title "Default apps" (`K.title` 56 px, y 180); eyebrow "Windows Settings". On "default app" (`S.find('default app', 1)`) one row's door cell glows: "default app = the door on a row".
- `[[by-label]]` left page lists rows `.pdf → Browser`, `.py → V S Code`, `.txt → Notepad`, `.png → Photos`; the `.pdf` row highlights.
- `[[by-app]]` right page: a `K.icon('globe')` header "Browser" and every label it can open, each linked by a thin line from the left page (`.htm`, `.html`, `.pdf`, `http`, `https`); each row shows who holds it now, with `.pdf` and `.htm` still pointing at another app (e.g. "Acrobat", "Edge").
- `[[proof]]` date card "Windows 11 launch · Oct 2021"; the five rows are rewritten one at a time by the pen, with a small counter "1 · 2 · 3 · 4 · 5".
- `[[one-click]]` date card "Set default returns · Mar 2022"; one pill "Set default" and all five rows rewrite together.
- `[[europe]]` date card "EEA only · Jul 2025"; the same pill now rewrites a longer column (eight more rows appear and flip); label "same ledger, a bigger pen".
**Exit:** book open, all rows calm.

## 09 — Who gets to write in the ledger
**Metaphor object:** the ledger and the pen; other hands; glass over some rows.
**Frame:** back to the room at z 1.15. Ledger large on the desk (x 300–1100, y 380–860). Hands around it are icons:
`K.icon('person')` "you", `K.icon('gear')` "installer", `K.icon('clock')` "update".
**Beats:**
- `[[hands]]` the three icons arrive around the ledger, each with a little pen line pointing at it.
- `[[installer]]` the installer's pen rewrites `.py → Python` (row flips); pill "installers claim labels".
- `[[update]]` date card "Windows 11 23H2 · Oct 2023"; two new rows appear: `.7z → File Explorer`, `.rar → File Explorer`.
- `[[ask-rule]]` date card "Microsoft's principles · Mar 2023"; the installer's pen turns into a small card "Ask in Settings" pointing to `K.icon('person')`.
- `[[glass]]` translucent glass cards with `K.icon('lock')` slide over the `http`, `https` and `.pdf` rows; only the "you" pen passes through. Cards "guarded rows · 2024", "locked record · 2025".
- `[[side-effect]]` a pen stroke on a guarded row fades back to the old value (the change "doesn't stick"); pill "sometimes · after upgrades → reset defaults".
- `[[grab]]` a faint grey `K.icon('gear')` (alpha 0.5) tugs at an unglazed row, label "people still report this"; no app named.
**Exit:** ledger with glass on three rows, calm.

## 10 — Where the picture breaks
**Metaphor object:** the ledger splits into three; a person bypasses the porter.
**Frame:** three ledger cards side by side (x 120–620, 710–1210, 1300–1800; y 220–560), each with an eyebrow.
**Beats:**
- `[[three-ledgers]]` the one ledger splits into three: "WINDOWS · registry", "MAC · label → type → app" (with a small note pinned per file), "LINUX · peeks at contents · a text file" (`K.icon('file')` with an eye-like ring over the beads).
- `[[front-door]]` cards shrink up; below, the room returns at small scale with a big door frame labelled "front door: double-click · Open with · open command".
- `[[walk-past]]` a terminal (`K.win` kind 'terminal', x 1060–1780, y 600–860) types `python notes.txt`; a dashed `K.path` carries the `notes.txt` string straight from the terminal to the Python door, curving around the porter, whose ledger stays shut.
- `[[two-pythons]]` two Python doors: "Python (ledger's)" and "Python (.venv)"; `script.py` double-clicked goes to the first; the typed `.venv\Scripts\python script.py` (mono, names the program) goes to the second. Labels `.venv` mono 30.
- `[[web]]` a parcel card arrives from a `K.icon('globe')` with a stamp "Content-Type: text/html"; its tag says `page.txt` but the stamp wins (tag dims). Eyebrow "the web: the server's label · 09.06".
**Exit:** three ledgers top, the two doors below, calm.

## 11 — A second ledger inside your editor
**Metaphor object:** a small ledger inside the V S Code door.
**Frame:** the V S Code door zooms to fill (camera z 2.2 on it), becoming a `K.win` kind 'code' (x 360–1560, y 200–860)
with a small ledger card pinned at the right (x 1180–1520, y 260–520).
**Beats:**
- `[[inner-ledger]]` the mini-ledger slides in: `.py → Python`, `.md → Markdown`, `.json → JSON`.
- `[[vscode]]` editor shows `hello.py` with syntax colours; status-bar pill "language mode: Python"; a pen draws a remap row `.txt → Python`, then removes it.
- `[[two-tables]]` the file tab becomes `hello.py.txt`; colours drain to plain cream; at the left a tiny Notepad door glows: "two ledgers, one label".
- `[[guess]]` a tab "Untitled" with no extension; the mini-ledger has no row; a `K.icon('question')` resolves into "Python (guessed from content)".
- `[[ai-labels]]` the editor fades; three tag cards in a row: `.safetensors` ("loads data only"), `.ckpt` / `.pt` ("older: could run code"), `.gguf` ("local model"), and a fourth `.mcpb` drawn as a zip-folder (`K.folder` name `.mcpb`) next to `.docx` "zips with their own label".
- `[[no-disguise]]` the `.ckpt` tag is rewritten to `.safetensors`; a loader door shows `K.icon('cross')` "won't load". Small card "safe ≠ renamed · 15.17".
**Exit:** the four tag cards, calm.

## 12 — The surprises you'll hit
**Metaphor object:** the room, with five quick moments at the porter's desk; each a small vignette card on a 3 × 2 grid
(cards 520 × 300 at x 120/700/1280, y 180/540).
**Beats:**
- `[[flash]]` card 1: `script.py` double-clicked; a terminal window pops and closes within 0.4 s (fade, no flash), label "it ran, then closed".
- `[[how-open]]` card 2: porter with `K.icon('question')` over a ledger with no row for `.xyz`; caption mono "Select an app to open this .xyz file".
- `[[no-ext]]` card 3: `K.file` with no extension, blank icon, same question.
- `[[doesnt-stick]]` card 4: a guarded (glass) row, pen stroke fades back; caption "sometimes won't stick after upgrade · locked record side effect · reset defaults".
- `[[wont-open]]` card 5: `notes.txt` renamed `notes.png`, icon swapped to `.png`, Photos door with `K.icon('cross')`: "new door can't read these bytes".
- `[[costume]]` card 6: tag `invoice.pdf.exe` folded to show `invoice.pdf`; under the fold a tiny `K.icon('gear')` "a program in a costume · Trust · 15.17". No red, no warning siren.
**Exit:** six cards, calm.

## 13 — The lantern: AI makes the file, the ledger still opens it
**Metaphor object:** a lantern-lit hand (the agent) that ties tags onto new strings, then either asks the porter or
walks to a door itself.
**Frame:** the room at z 1, a `K.icon('lantern')` glow hanging top-right (x 1680, y 180) casting warm light; agent icon
`K.icon('sparkle')` at x 1500, y 760.
**Beats:**
- `[[five-years]]` small card "2021" at left: a hand (person icon) tying a tag on a single string by itself; beside it a tiny editor with a faint grey autocomplete ghost line, label "AI = autocomplete".
- `[[assistants]]` card "AI assistants make real files · 2023 → 2025"; the sparkle ties tags on four new strings: `report.docx`, `budget.xlsx`, `deck.pptx`, `brief.pdf`, plus `app.py` and `README.md` labelled "coding agents".
- `[[show-run]]` split: left arrow from the sparkle to the porter labelled "show → asks the porter" (`.pdf` goes to Browser door via the ledger); right dashed arrow straight to the Python door labelled "run → names the program".
- `[[ai-actions]]` a right-click menu card next to a `photo.png` file lists "AI actions"; card "Oct 2025 · .jpg .jpeg .png · varies by market"; hovering a `.txt` file shows the menu without them.
- `[[connector]]` card "File Explorer connector · preview": a folder `K.folder` with `K.icon('lock')`, a list row `name: report · extension: .docx` (extension as its own field).
- `[[mac-names]]` card "macOS 27 · Sept 2026": a tag writes a suggested name "Trip receipts" while its `.pdf` stays bright and goes to the Preview door.
- `[[heading]]` eyebrow "THE DIRECTION LOOKS LIKE" over two pills: "more guarded rows" · "permissioned doors for agents".
**Exit:** room under the lantern's glow, strings at their doors, calm.

## 14 — Keep this
**Metaphor object:** one string, one tag, one ledger.
**Frame:** end card. `K.plate` (shade 0.5) if available else `K.bg({ glow: 0.4 })`; at top-left a small "Safe to ignore"
note; centre a stack of three takeaway rows (x 300–1620, y 330–720), each a gold bold lead in Zen Maru 44 px; a tiny
still life of string + tag + ledger at right (x 1500–1780, y 760–900). `K.petals` avoiding text.
**Beats:**
- `[[ignore]]` `K.note` (x 120–720, y 150–300) eyebrow "SAFE TO IGNORE FOR NOW", body "registry · ProgIDs · Mac type identifiers · Linux MIME files · menu paths"; fades to 40% after.
- `[[keep-1]]` "**The extension is a label in the name.**"
- `[[keep-2]]` "**Your computer keeps a ledger from label to program.**"
- `[[keep-3]]` "**Renaming changes the label; Open with's Always and default apps change the ledger.**"
- `[[next]]` small map strip: `K.map.chipPos('01')` area shown with an eyebrow "Next stop · 01.03 Folders, paths & the working directory" (no teaser).
**Exit:** three takeaways, the still life, petals drifting; held through the 3 s tail.
