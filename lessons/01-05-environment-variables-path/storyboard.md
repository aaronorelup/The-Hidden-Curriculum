# Storyboard — 01.05 Environment variables & PATH

> Final (judge synthesis): draft B's storyboard, updated for the merged script (new cues [[purpose]], [[both-true]]; cmd current-folder footnote; Homebrew surprise; Trust-district neighbours).

**The one metaphor: the satchel copied at the door.** Every running program is a courier, drawn as a small program tile (`K.iconTile('terminal' | 'code' | 'sparkle' ...)`) wearing a satchel. The satchel is a kit drawing, not an illustration: a `K.card` (r 24, terracotta stroke) with a flap line (`K.line`) and a strap (`K.path`, no head). Inside it sit **cards**: small `K.card`s holding a mono `K.pill` name and a cream value (`HOME`, `TEMP`, `PATH`, later `ANTHROPIC_API_KEY`). The **door** is a tall gold-stroked `K.card` outline on the left ("home", with `K.icon('house')`), from which couriers leave to the right. The **PATH card** unfolds into **numbered streets**: horizontal hairlines (`K.line`, `K.C.line2`) with numbered pills 1..n on the left, each street carrying one **shop** = `K.folder` named for the real folder, with a `K.file` inside named `python.exe` where relevant. The street grid deliberately reuses the look of 01.03's map-on-the-disk (hairline streets, gold you-are-here dot) so the two lessons read as one world.

Persistent layout (from scene 03 on): home door at x 120–360, y 260–820; courier lane y 540; satchel "zoom" panel at x 700–1760, y 180–880 when a scene looks inside. Labels ≤ 8 words, ≥ 26 px; literal names only on screen (`PATH`, `.venv`, `.env`, `where.exe python`). Everything inside x 80–1840, y 130–930.

## 01 — The point
**Metaphor object:** the closed satchel, introduced as an emblem; the PATH card peeks out of it.
**Frame:** `K.plate('plate', t, {zoom:true, shade:.45})` if `engine/assets/teahouse-night.jpg` exists, else `K.bg({glow:.5, glowX:960, glowY:420})`. Title `K.title('Environment variables & PATH', 960, 300, {size:84, align:'center'})`, eyebrow "MODULE 01 · LESSON 5" above it at y 220. Purpose line (Georgia 34 px, cream, centred, `K.para` width 1300) at y 380–460. Satchel emblem centred at (960, 640), 300×200. `K.petals` (n 6, avoid the title and purpose rects). `noBadge`.
**Beats:**
- [[purpose]] title and eyebrow already resting; the purpose line writes in (fade + 12 px rise) under the title; satchel emblem closed.
- [[conclusion]] conclusion line fades in under the purpose line (gold-soft, 30 px, y 510); the satchel flap opens 20 degrees.
- [[path-card]] one long card slides up out of the satchel, mono pill `PATH`; behind it a ghost of three numbered streets, 1 2 3, draws left to right.
- [[depends]] two small pills appear either side of the satchel: "who started it" (left), "when" (right), joined to the satchel by short arrows.
- [[three-symptoms]] the pills give way to three symptom cards in a row at y 800: `'python' is not recognized...`, "the wrong Python", "the wrong account billed" (`K.icon('warning')` on each); then one gold `K.ring` draws around all three: "one idea".
- [[agents-inside]] a small courier tile with `K.icon('sparkle')` walks in from the right and stands beside the satchel, carrying a lantern glow (`K.glow`, gold, low).
**Exit:** symptom cards fade; title, conclusion and satchel rest, petals drifting.

## 02 — Where it lives
**Metaphor object:** the satchel shrinks to a corner token (x 1700, y 820, 110 px) and stays there.
**Frame:** `K.bg()`; `K.map.draw(t, {t0:0, focus:'machine', pin:'01', pinDrop:K.io(t, S.cue('pin'), .7, 'back'), pinGlowK})` full canvas.
**Beats:**
- [[map]] map fades in; district 1 The Machine lights, its question "what's on your computer?" in gold.
- [[pin]] terracotta pin drops on module 01; small pill under it "01.05 Environment variables & PATH".
- [[continuity]] two ghost chips beside the pin, "01.03 paths" and "01.04 back room", dim; then the satchel token in the corner gets a short arrow from the pin: "what goes out the door".
**Exit:** map holds with pin glowing; satchel token waiting in the corner.

## 03 — The satchel copied at the door
**Metaphor object:** the home door, the parent courier, the first child courier; this is the picture the whole lesson lives in.
**Frame:** `K.bg()`. Home door outline at x 120–360 (label "home", `K.icon('house')`). Courier lane y 540 runs to x 1760.
**Beats:**
- [[courier]] a courier tile (`K.iconTile('terminal')`, 140 px) pops in at x 960, satchel on its side; label "a running program".
- [[parent]] four parent tiles fade in along the door edge: Explorer (`folder`), terminal, editor (`code`), agent (`sparkle`); the terminal one glows and gets label "parent". The courier slides back to stand beside it.
- [[satchel]] the parent's satchel (x 420) shows three cards; a dashed copy of each card flies into the courier's satchel (`K.stagger`, arrows `K.path` with `k`); label "a copy, at the door".
- [[door-closes]] the door swings shut (a gold line rotates closed); courier walks to x 1300. At home, a new card "+ NEW" appears in the parent's satchel; a short arrow toward the courier stops at the door with `K.icon('cross')`.
- [[no-return]] the courier's satchel changes one card (value retypes); its arrow back home stops at the door, another `cross`.
- [[dot-callback]] a gold you-are-here dot (01.03's dot) rides on the courier's satchel flap; small eyebrow "01.03 · same rule".
**Exit:** door closed, courier on the road, two crosses fading; calm.

## 04 — What's in the satchel
**Metaphor object:** the courier's satchel, now opened in the zoom panel.
**Frame:** camera (`K.cam`) eases from the road into the satchel; satchel panel x 700–1760, y 200–860; courier tile small at x 300, y 540 for continuity.
**Beats:**
- [[cards]] one card enlarges at centre: name pill `NAME` | value text, label "environment variable: name + text".
- [[examples]] two cards stack: `USERPROFILE` / `HOME` → `C:\Users\…`, `TEMP` → `C:\Users\…\AppData\Local\Temp`.
- [[path-long]] a third card, much longer, `PATH`, slides in and keeps going past the panel edge (clipped with a soft fade), gold outline.
- [[master-copy]] camera pulls back to the home door; inside it two drawers (`K.card`s): "user", "system", with arrows merging into one satchel at the door.
- [[zshrc]] beside the drawers a file `K.file(... {ext:'zshrc', name:'.zshrc', nameSize:26})` with eyebrow "Mac · Linux".
- [[peek]] three mono pills in a row at y 860: `echo $PATH` · `$env:PATH` · "Environment Variables dialog"; a small `K.win(kind:'explorer', title:'Environment Variables')` thumbnail behind the third.
**Exit:** the long PATH card glows; everything else dims to 50%.

## 05 — Path: a numbered list of streets
**Metaphor object:** the PATH card unfolds into the street grid (the lesson's second key picture).
**Frame:** `K.bg()`. Streets at y 260, 380, 500, 620, 740 from x 300 to x 1700, numbered pills 1–5 at x 220. Each street has a folder shop at x 1300 (`K.folder`, name 26 px). Courier waits at x 160, y 140 (top-left of grid, below badge).
**Beats:**
- [[list-of-streets]] the PATH card's text splits at each `;` and each folder drops onto a numbered street (`K.stagger`); small eyebrow pill top-right: "`;` Windows · `:` Mac/Linux".
- [[bare-name]] a terminal strip at y 860: `K.term` types `python`; the courier sets off down street 1.
- [[first-shop]] street 1's shop has no python; the courier walks street 2, where the shop `…\Python310` holds `K.file` `python.exe`; the courier enters it (shop glows gold).
- [[first-wins]] streets 3–5, which also hold `python.exe`, dim to 30% with a soft lock of dashes; label "first match wins. Later: never visited". On screen only, a small pill near the file: `PATHEXT: .EXE .CMD …`.
- [[system-first]] streets regroup into two bands with eyebrows "system" (top) then "user" (below); hedged label "system list first".
- [[shell-first]] a small gate before street 1 labelled "built-ins · aliases" with pill "02.02"; on "Command Prompt" (`S.find('Command')`) a small folder chip "current folder" appears before the gate with eyebrow `cmd`, and on "PowerShell" a `cross` lands on it with eyebrow `PowerShell`.
**Exit:** the courier inside shop 2, streets 3–5 quiet.

## 06 — "Not recognized as a command"
**Metaphor object:** the same street grid; the courier walks every street and finds nothing.
**Frame:** `K.bg()`; street grid as in 05, but no shop holds the name; terminal strip at y 860.
**Beats:**
- [[every-street]] courier walks streets 1–5 in turn (fast, 0.4 s each), each shop stamped with a small `cross`; arrives at the end of the grid empty-handed. Label "no shop by that name".
- [[not-installed]] cause card 1 at right (x 1450, y 260): "not installed".
- [[not-on-path]] cause card 2: "installed, folder not on the list"; a folder shop appears off-grid, outside the streets, dim.
- [[stale]] cause card 3: "list changed after this terminal left" (`K.icon('clock')`).
- [[typo]] cause card 4: `pyhton`.
- [[wordings]] the cause cards fade; three terminals stack (`K.win(kind:'terminal')`, 1500 wide, 110 tall each, mono 28 px), one per spoken outfit: cmd `'python' is not recognized as an internal or external command,` · PowerShell `The term 'python' is not recognized as the name of a cmdlet, …` · bash/zsh `python: command not found`.
**Exit:** three error lines rest, the empty street grid faint behind them.

## 07 — Which python actually ran?
**Metaphor object:** street grid with three shops all named python; one is a signpost.
**Frame:** `K.bg()`; three streets only (y 320, 500, 680), numbered 1–3.
**Beats:**
- [[many-shops]] four shop signs cycle in over the streets: installer, conda, uv, Store; all labelled `python.exe`. Courier at the start.
- [[observation]] eyebrow at top: "OBSERVED · this course's Windows PC · 2026-10-10"; the grid settles to three shops.
- [[candidates]] shops fill in order with mono paths: 1 `C:\Users\…\Python310\python.exe` · 2 `C:\Users\…\WindowsApps\python.exe` (drawn as a signpost: `K.card` with `K.icon('warning')`, not a folder) · 3 `C:\Users\…\miniconda3\python.exe`.
- [[winner]] courier enters shop 1 (gold); a pill on it "3.10 · end of life this month"; label under the grid "nobody chose this. The order did."
- [[store-stub]] camera eases to shop 2; a small terminal shows `Python was not found; run without arguments to install from the Microsoft Store…`; label "on the list ≠ installed".
- [[install-manager]] a card at right: "Python 3.14+: install manager"; beneath it an old installer checkbox "☐ Add python.exe to PATH" with a soft strike line, label "being retired"; a small signpost glyph beside the card, label "3.14+ `python` is a signpost too → check where it leads".
- [[ask-which]] three mono pills at y 860: `where.exe python` · `which -a python` · `Get-Command python -All`; a fourth: `sys.executable`.
**Exit:** courier in shop 1, the four pills resting.

## 08 — Virtual environments: a street pinned to the top
**Metaphor object:** the courier's PATH card with a new street pinned above street 1.
**Frame:** `K.bg()`; same three streets; a project folder `K.folder` "my-project" at left containing `.venv`.
**Beats:**
- [[activate]] a new street slides in above street 1 (the others shift down), numbered "0" in gold, its shop `my-project\.venv\Scripts`, with a `K.file` `python.exe`; a gold pin icon (`K.icon('pin')`) fixes it.
- [[project-python]] terminal strip types `python`; the courier walks only the pinned street and enters.
- [[one-shell]] a second courier tile (another terminal) appears below, carrying the unpinned card; a third, the agent tile (`sparkle`), the same. Each gets a small label "not activated".
- [[skip-activation]] one pill at the right: `uv run`, with an arrow straight to the .venv shop that skips the pinning, labelled "for this one command"; eyebrow "05.03 · 05.04".
- [[both-true]] two speech pills from the person icon (x 300): "I activated it" (left window, pinned card) and "wrong Python" (right window, unpinned card); a dashed line links the right pill to the second courier; label "different window".
**Exit:** pinned street glows; the other couriers wait.

## 09 — Why a new terminal after an install
**Metaphor object:** the home door again, the master copy, an old courier on the road and a new one.
**Frame:** `K.bg()`; home door at left with the master satchel; courier lane y 540.
**Beats:**
- [[installer-home]] an installer tile (`K.icon('gear')`) at home writes a new street onto the master PATH card (card grows a line, gold).
- [[old-satchel]] an old courier already on the road (x 1300) holds the old card; its terminal bubble: `'tool' is not recognized…`.
- [[new-courier]] the door opens; a new courier leaves with a fresh copy that includes the new street (copy animation from 03).
- [[new-tab]] split label: left "2021: close the whole window" (dim), right a mini Windows Terminal with two tabs: the new tab glows "picks up the change", the old tab stays dim "still stale"; eyebrow "since 2023".
- [[editor]] an editor tile (`code`) with a terminal inside it, nested; arrow from editor to inner terminal; label "restart the editor".
- [[agent-restart]] agent tile (`sparkle`) beside it with `K.icon('clock')`: "reads the environment at start".
**Exit:** the fresh courier walking right; old courier fades out.

## 10 — Where the picture breaks
**Metaphor object:** the satchel itself, shown failing as a metaphor in three ways.
**Frame:** `K.bg()`; satchel large at centre-left (x 600, y 520); three break cards at right, x 1150–1760.
**Beats:**
- [[no-seal]] a lock icon tries to close the flap and fails (`K.icon('lock')` fades, `cross`); cards fan out of the satchel into two child couriers. Break card 1: "no seal: every child can read every card".
- [[signposts]] break card 2: a signpost shop (from 07) with an arrow pointing off-screen; label "some shops are signposts (Store alias, install-manager alias, shims)".
- [[many-satchels]] break card 3: the satchel multiplies into a grid of small satchels, one per tile; label "one environment per running program".
**Exit:** three break cards rest; satchel grid gently breathing.

## 11 — Keys in the satchel
**Metaphor object:** a key card tucked into the courier's satchel, copied down a chain of couriers.
**Frame:** `K.bg()`; satchel panel at left (x 160–760); chain of couriers to the right.
**Beats:**
- [[named-key]] a card with `K.icon('key')` slides into the satchel: `ANTHROPIC_API_KEY` = `sk-…` (value always masked); a second ghost card `OPENAI_API_KEY`. Label "known name, key out of the code".
- [[env-file]] a `K.file` `.env` beside the satchel (callback to 01.04's drawer, eyebrow "01.04"); its lines flow into the key card; small pills "library · Bun: automatic · Node: `--env-file`".
- [[both-ways]] the courier leaves the door; the key card is copied into two children.
- [[agent-copies]] one child is the agent (`sparkle`); it sends three more couriers ("command", "package", "script"), each with a copy of the key card (stagger). The chain has five copies of the key.
- [[billing]] the agent courier gets a small card: "API key → pay per use" in terracotta, and "subscription" dimmed with a soft strike.
- [[status]] mono pill `/status` with label "shows which one pays".
**Exit:** the chain of five key copies glows faintly; calm.

## 12 — The lantern: agents pack satchels now
**Metaphor object:** the agent courier, now at the door editing the master copy and sending its own couriers.
**Frame:** `K.bg({glow:.35})`; timeline strip at y 200 with dated pins: 2021 · Aug 2025 · Autumn 2025 · Dec 2025 · Oct 2026.
**Beats:**
- [[then]] 2021 pin lights; only "you" (`K.icon('person')`) at the door sending couriers.
- [[now]] Oct 2026 pin lights; the agent tile with a lantern glow stands at the door: writes a street on the master PATH card, creates a `.venv` folder, writes a `.env` file, then sends couriers of its own.
- [[thieves]] Aug 2025 and Autumn 2025 pins light; a dark tile (`K.icon('warning')`) grabs a satchel, cards spill: `.env`, `GITHUB_TOKEN`, `NPM_TOKEN`; labels "poisoned package (Aug 2025)" and "npm worm (autumn 2025)". No numbers.
- [[responses]] Dec 2025 pin: card "npm revoked long-lived tokens"; beside it a satchel with a filter (`K.icon('shield')`) and a switch drawn off, label "key stripping: mostly opt-in".
- [[heading]] a single key card handed to one courier for one trip, then withdrawn; pill "heading · early".
**Exit:** the agent at the door with its lantern; timeline rests.

## 13 — Your job: two questions
**Metaphor object:** you, at the door, checking couriers.
**Frame:** `K.bg()`; person icon at the door (x 260); two question cards at right.
**Beats:**
- [[your-job]] the agent tile hands the person a clipboard-like card (`K.note`) "check the work".
- [[which-ran]] question card 1: "Which program ran?" with mono pills `where.exe python` · `which -a python`; behind it the street grid ghost with shop 1 glowing.
- [[where-keys]] question card 2: "Where do my keys live? Who can read them?" with four small pills: "which file" · "which variable" · "which terminal" · "which account pays".
- [[not-a-fence]] a polite note card "please don't read your keys" on a fence post that is only a dashed line; a solid fence (`K.icon('shield')`) beside it labelled "sandbox · scrubbing → 14.12".
**Exit:** two question cards resting, the person at the door.

## 14 — The surprises you'll hit
**Metaphor object:** each surprise shown as a small courier vignette in a 2-column card grid that fills one card per cue.
**Frame:** `K.bg()`; 7 cards (2 columns, 4 rows; the last centred), each 760×150 at x 120/1000, y 160–880; the current card full opacity, earlier ones at 50%.
**Beats:**
- [[same-terminal]] card: old courier icon + `'tool' is not recognized…` → "open a new terminal".
- [[store-opens]] card: signpost shop + "Microsoft Store opens" → "the stand-in won".
- [[py-vs-python]] card: two pills `python` / `py` with arrows to two different shops.
- [[mac-python3]] card: `zsh: command not found: python` beside `python3` with `K.icon('check')`; on "brew" (`S.find('brew')`) a second line in the card: `command not found: brew` → "Homebrew folder joins PATH".
- [[pip-import]] card: `pip install` arrow into shop A; `import` arrow from shop B with a cross; label "different Pythons".
- [[export-stick]] card: agent tile, three commands (`export …`, `activate`, `python`) each with its own fresh satchel; label "fresh shell per command".
- [[ghost-key]] card: a key card nobody put in, with `.env` file behind it; label "a runtime loaded it".
**Exit:** all seven cards at even opacity, quiet.

## 15 — Safe to ignore, and the neighbours
**Metaphor object:** the satchel set down; the map returns small.
**Frame:** `K.bg()`; left half: "safe to ignore" list of dim pills; right half: `K.map.draw` scaled to 0.55 (questions off) with module chips highlighted.
**Beats:**
- [[ignore]] dim pills appear and settle (stagger, one per spoken item): "registry by hand" · "command precedence rules" · "version-manager shims" · "environment editors", then a screen-only `setx` limits pill.
- [[neighbours]] map lights module rows 02 (shells) and 05 (many Pythons, virtual environments) via `rowWash`; small mono pills beside them: `02.02` · `05.01` · `05.03`.
- [[trust]] map lights module rows 14 and 15 via `rowWash`, pills `14.12` · `15.07` · `15.08`; `highlight: { trust: k }` warms the Trust outline.
**Exit:** map with four washed rows and six pills; no "next time".

## 16 — Keep this
**Metaphor object:** the satchel open, the PATH card on top (end card).
**Frame:** `K.plate` with shade .5 if present, else `K.bg({glow:.5})`; satchel at right (x 1500, y 560) with PATH card raised; three takeaway rows at left (x 140–1200), bold lead in `K.C.head`, rest in cream; `K.petals` (n 6, avoid text). `noBadge`.
**Beats:**
- [[keep-one]] row 1: **Every program carries a copy of its parent's environment.** Changes at home reach only programs started afterwards: open a new terminal.
- [[keep-two]] row 2: **PATH is an ordered list, and the first match wins.** To know which program ran, ask the shell.
- [[keep-three]] row 3: **Keys in the environment go wherever you send programs.** Agents included: know where yours live and who can read them.
**Exit:** three rows and the open satchel rest for the 3 s tail, petals drifting.

`keep:` for lesson.js:
- ["Every program carries a copy of its parent's environment.", "Changes at home reach only programs started afterwards: open a new terminal."]
- ["PATH is an ordered list, and the first match wins.", "To know which program ran, ask the shell."]
- ["Keys in the environment go wherever you send programs.", "Agents included: know where yours live and who can read them."]
