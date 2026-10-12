# Storyboard — 01.06 Programs, processes & services

> Final (judge synthesis, 2026-10-11): draft A's storyboard, updated for the merged script (01 reordered: purpose, conclusion, three-shelves, one-idea, your-part, then the Notepad moment; 06 carries the "five years ago" line inside the `shortcut` beat; MCP and Ollama executable names live on screen, not in the voice).

Canvas 1920x1080; text inside x 80–1840, y 130–930; badge top-left (y < 110); nothing essential below y 930.
Kit only (engine/KIT.md): windows, terminals, editors, files, folders, cards, pills, arrows, line icons, the course map, the painted plate.

**Persistent metaphor: the kitchen roster, seen from above.** A recipe shelf at the top left (row of small `K.card` recipe cards, each with a `K.icon('program')` and a mono name: `node.exe`, `python.exe`, `ollama.exe`), a long counter across the middle (a wide low `K.card` split into stretches), cooks drawn as `K.icon('person')` tiles carrying a ticket pill (PID) and 01.05's satchel (the same small card-with-strap drawn in 01.05, redrawn identically). Later scenes add: the staff board on the right wall (becomes Task Manager), a door at the left (becomes the window), numbered serving hatches along the back wall (ports), a grey "night staff" tint for services, a glass fence (`K.card` with low-alpha fill and dashed gold stroke) for sandboxes. Each scene starts from the previous scene's kitchen state and transforms it; nothing is redrawn from scratch.

Colours: gold headings, terracotta accent for the thing being named, cream text; services drawn in `K.C.soft` grey; AI cooks get a small `sparkle` badge; blossom only on 01 and 16.

## 01 — The point
**Metaphor object:** a single file icon `hello.txt` (introduced at the end of 01; it becomes a recipe card on the shelf in 03).
**Frame:** title card. Painted plate `teahouse-night.jpg` via `K.plate(..., { shade: 0.45, mask: [620, 860] })` if it exists, else `K.bg({ glow: 0.5 })`. Eyebrow "01.06 · Your Computer, Under the Hood" at (160, 200); `K.title('Programs, processes & services', 160, 290, { size: 76 })`. Purpose line as `K.para` (x 160, y 360, w 1100, 34 px). Sparse `K.petals` with `avoid` rects over all text.
**Beats:**
- `purpose`: title and purpose line rise in (`K.rise`), 0.6 s.
- `conclusion`: the one-line conclusion fades in under the purpose line (gold-soft, 30 px, `K.para` w 1300, y 460).
- `three-shelves`: three pills slide in on one row at y 600: "program = file" · "process = running copy" · "service = kept alive by the OS" (30 px, terracotta outline on the middle one).
- `one-idea`: title block slides up and dims to 0.35; three small cards fan out at y 760: mono `EADDRINUSE :3000`, "still running after close", `sparkle` + "AI in the background"; a thin gold `K.ring` (rot 0) gathers all three: "one idea".
- `your-part`: cards settle; a `sparkle` agent tile at left with "finds · stops", a `person` tile at right with "judges what should run" (terracotta).
- `notepad`: tiles and cards fade; a `K.win(560, 300, 800, 440, { kind: 'notepad', title: 'hello.txt - Notepad', titleSize: 26 })` opens centre with `print("hello")` in it, and a `K.file(1500, 740, 150, { ext: 'txt', name: 'hello.txt', nameSize: 26 })` drops beside it.
- `sat-there`: Notepad window fades; the file sits alone, centre, with a still `clock` icon beside it; label "a program that never ran" (30 px, soft).
**Exit:** the lone `hello.txt` file, title dimmed above; petals idle.

## 02 — Where it lives
**Metaphor object:** the satchel from 01.05.
**Frame:** `K.map.draw(t, { focus: 'machine', pin: '01', pinDrop, pinGlowK, lanterns: 1 })` full canvas.
**Beats:**
- `map`: map fades in at full view, then `focus: 'machine'` lights District 1, its question "what's on your computer?" brightening.
- `pin`: pin drops onto module 01 (`pinDrop = K.io(t, a, .7, 'back')`, the scene's one overshoot); camera eases toward `K.map.chipPos('01')` (z 1.4).
- `satchel-callback`: a small satchel card slides out of the pinned row and lands at (1500, 300); four tiny cook tiles walk out behind it in a line, each with a satchel; a mono pill "how many right now?" at (1500, 420).
**Exit:** camera at rest on District 1, the satchel and four cooks idle (small bob).

## 03 — The recipe and the cooks
**Metaphor object:** the recipe shelf and the counter (the kitchen is built here).
**Frame:** kitchen from above. Shelf at x 140–860, y 170–330: four recipe cards (`K.card` 160x120, `program` icon, mono 26 px names `node.exe`, `python.exe`, `ollama.exe`, `hello.py`; the 01 file now renamed and on the shelf). Counter: wide `K.card(140, 560, 1640, 200)` divided into dashed stretches.
**Beats:**
- `shelf`: shelf cards pop in left to right (`K.stagger`); label "programs: instructions on disk" (eyebrow, y 145).
- `cook`: a cook tile steps from the left edge, takes the `node.exe` card (a copy of the card lifts and travels to the cook along `K.path`); label "process = one running copy".
- `ticket`: a mono pill `PID 18412` clips onto the cook.
- `counter`: one stretch of the counter in front of the cook lights gold; label "memory (its own)".
- `satchel`: the 01.05 satchel slides onto the cook from a door marker at x 100; a parent tile appears at the door, cycling with the words (`folder` File Explorer, `terminal`, `code`, `sparkle`); arrow "parent" from it to the cook.
- `same-card`: ten more cooks file in, each lifting a copy of the same `node.exe` card, each with a different PID pill; a counter pill "11 × node.exe" (mono, 30 px) and an observation tag "course laptop · Oct 2026" (26 px, soft).
**Exit:** eleven cooks at the counter, gentle idle bob, shelf above.

## 04 — What a process really is
**Metaphor object:** one cook, zoomed (camera pushes in on the first node cook).
**Frame:** `K.cam` zooms to the first cook (z 1.8); on the right, a `K.card(1100, 200, 680, 560)` labelled "a process" fills with rows.
**Beats:**
- `ingredients`: four rows stagger into the card, each a line icon + label: `lock` "private memory", mono `PID 18412`, `book` "copy of the environment", `person` "runs as you".
- `threads`: inside the cook's counter stretch, three small worker dots appear sharing it; label "threads → 07.01" (26 px).
- `count`: camera pulls back out past the kitchen; the counter extends off both edges, rows of tiny cook dots fill the frame; big mono number "457" (96 px) with "processes, one moment" beneath and the observation tag.
- `many-per-app`: three groups circle (`K.ring`) around clusters: browser (globe), V S Code (`code`), Ollama (`sparkle`), each "several processes".
- `breaks`: heading "Where the picture breaks" (gold); first card: `brain` icon crossed: "no judgement: follows the card".
- `cores`: second card: four lit lanes "cores", the cooks flicker between lanes in turn (slow, no flashing): "takes turns, very fast".
- `private`: third card: two counter stretches with a solid wall between them, `lock` icon: "can't see another's memory".
**Exit:** three break cards in a row, kitchen dim behind.

## 05 — The night staff: services and daemons
**Metaphor object:** the kitchen at night; service cooks in grey.
**Frame:** kitchen from 03, ambient glow lowered (`K.bg({ glow: 0.25 })`); a `house` icon "the building (OS)" top right.
**Beats:**
- `night`: front-room lights dim; three grey cooks enter from a back door marked with a `gear` icon (the OS's manager); no window frame around them; label "service: started by the OS, no window".
- `no-one-home`: the viewer's `person` tile leaves; grey cooks keep working; one stops, the gear pulses, it reappears: label "restarted by the manager".
- `svchost`: grey cooks cluster under one card `svchost.exe` (mono) labelled "Service Host"; numbers "97 Service Host processes · 166 services running in all" (30 px, two separate facts) with the observation tag; leave a few grey cooks standing on their own, outside the svchost card (services with their own .exe).
- `daemon`: pill row: "Windows: service" · "Mac / Linux: daemon"; small mono labels `launchd` · `systemd` beneath (26 px).
- `tray`: the person returns; a cook with a small clock-corner tray icon walks in with them; labelled "tray app (Ollama on Windows / Mac)".
- `three-kinds`: three-column card (x 200–1720, y 520–900): columns "app" · "tray app" · "service"; rows "who starts it" (you / sign-in / the OS), "window?" (yes / tray only / none), "survives sign-out?" (no / no / yes). Rows reveal with `K.stagger`.
**Exit:** the three-column card, kitchen dim behind.

## 06 — Task Manager: the staff board
**Metaphor object:** the staff board on the wall, which becomes Task Manager.
**Frame:** the board (a `K.card` on the kitchen's right wall) grows into a `K.win(240, 150, 1440, 760, { kind: 'explorer', title: 'Task Manager', titleSize: 28, focus: true })` with a left nav column and rows drawn as cards/pills (mock-up, not a screenshot).
**Beats:**
- `shortcut`: the board grows into the window; three key pills `Ctrl` `Shift` `Esc` pop above it; on "Five years ago" (`S.find('Five')`) a small faded card "2021: End task on a frozen app" shows at the lower right for about 2 s, then clears.
- `processes-tab`: nav "Processes" lights; three grouped headers appear: "Apps", "Background processes", "Windows processes", each with 2–3 rows (names + small bars).
- `details`: nav "Details" lights; table with a mono PID column (`18412`, `1168`, `22124`); each row links by a faint line to its cook in the kitchen behind.
- `services-tab`: nav "Services" lights; grey rows (the night staff) with "Running" / "Stopped" pills; then on "Startup" nav "Startup apps" lights briefly with two rows.
- `end-task`: one row highlighted; an "End task" pill; the row and its cook vanish (fade, 0.4 s); small `warning` "unsaved work lost".
- `new-columns`: two new column headers slide in, dashed outline: "NPU" and "Isolation"; tag "newer Windows 11 · hidden by default" (26 px).
- `elsewhere`: two small pills below the window (y 880): "Mac: Activity Monitor" · "Linux: top · htop · systemctl".
**Exit:** Task Manager window steady, Processes view.

## 07 — Closing the window isn't ending the process
**Metaphor object:** the door (window) and the cook behind it.
**Frame:** a `K.win(260, 260, 620, 420, { kind: 'browser', title: 'Ollama' })` (Ollama's own app window) framed as a door at left; a cook at the counter visible through it; the kitchen continues right.
**Beats:**
- `door`: window closes (scales to 0 at its title bar, 0.5 s); the cook stays at the counter, still working (`ollama app.exe` in the tray, `ollama.exe` still at 11434); label "window ≠ process".
- `outlive`: three cooks highlight in turn with tags: "tray app (Ollama)", "service: never had a door" (grey), "orphan: parent gone" (its parent tile fades, cook stays).
- `no-tree`: a parent tile with three children linked by lines; the parent is ended (fades), the children remain; then a dashed rounded box draws around a second family, label "job object" (mono 26 px), and that whole box clears together.
- `tm-bug`: a small Task Manager window closes, then three ghost copies stack faintly behind it; tag "late 2025 · fixed November" (26 px); a `check` icon settles.
**Exit:** kitchen with the lone working cook, door closed.

## 08 — Servers and ports: one cook per hatch
**Metaphor object:** numbered serving hatches along the back wall.
**Frame:** back wall at y 200–330, six hatches (`K.card` 220x120, square corners r 8) with mono numbers.
**Beats:**
- `hatch`: wall and hatches draw in; one cook walks to a hatch and waits; order slips (small cards) arrive through it; label "server = process waiting at a port".
- `one-per-hatch`: a second cook approaches the same hatch and is blocked by a soft bar; `cross` icon; "one process per port".
- `numbers`: hatch numbers fill in turn with owner pills: `3000` Node · `5173` Vite · `8000` Python · `8188` ComfyUI · `1234` LM Studio · `11434` Ollama (mono 30 px numbers, 26 px names). Eyebrow "numbers you'll often see".
- `localhost`: a `house` icon labelled "localhost = this machine"; small tag "more: 09.02 · 09.03".
- `listeners`: the wall extends; 27 small lit hatches in a strip; "27 open at once" with the observation tag.
**Exit:** six hatches, each with its cook.

## 09 — The surprises: port in use, leftovers and "zombies"
**Metaphor object:** hatch 3000 and hatch 5173.
**Frame:** left half: a `K.term` window (x 140–940, y 520–900); right half: the hatches from 08.
**Beats:**
- `eaddrinuse`: terminal types `npm run dev` then prints `Error: listen EADDRINUSE: address already in use :::3000` (accent, mono 26 px; widen the terminal so the line fits unsquashed).
- `meaning`: at hatch 3000 an old cook (slightly faded, "earlier copy") stands; the new cook bumps the bar.
- `vite-hop`: terminal prints `Port 5173 is in use, trying another one...`; the new cook walks one hatch over to `5174`; a small browser window still points at `localhost:5173` with a "still the old one" tag.
- `ollama-bind`: two Ollama cooks, one at `11434` (the running server, `ollama.exe`), the second blocked: label "bind error · 127.0.0.1:11434".
- `zombie`: NOT on the Task Manager board: a small Linux `ps` list card (mono) with one row marked `<defunct>` (name, no cook, no bar): label "zombie (strict, Unix): finished, entry only, uses nothing".
- `orphan`: back at hatch 3000, the old cook glows; its parent tile shown as a faded outline: label "alive: leftover / orphan".
**Exit:** the two labels side by side: "zombie: name only" · "orphan: alive, holding the port".

## 10 — The lantern: model servers on your own machine
**Metaphor object:** hatch 11434 and Ollama's two cooks.
**Frame:** small lantern icon top-right with eyebrow "the lantern"; the kitchen centre.
**Beats:**
- `then`: a split card at left, "about 2021": one terminal window, one hatch `3000`.
- `now`: right side "now": hatches multiply, several with `sparkle` badges.
- `model-server`: split card fades; camera eases to hatch `11434`; label "model server = long-running process on a port".
- `ollama-pair`: tray-app cook (mono `ollama app.exe`, PID 1168) with a parent arrow to the server cook (mono `ollama.exe`, PID 22124) at hatch 11434; tag "one app · two programs · two processes".
- `keep-alive`: a `brain` card on the counter in front of the server cook stays lit after the order slips stop; `clock` icon "~5 min by default".
- `others`: two more hatch pills: `1234` LM Studio (`llmster`, new 2026) · "Foundry Local" (Windows, GA 2026).
- `no-password`: the 11434 hatch has no `lock`; a `globe` fades in at the far side with a dashed line and a `warning`: "fine on localhost · risky on the network".
**Exit:** the two Ollama cooks, hatch 11434, lantern steady.

## 11 — The lantern: M C P servers are cooks your app hires
**Metaphor object:** the AI app as a head cook hiring a crew.
**Frame:** a `K.win(160, 180, 720, 420, { kind: 'code', title: 'AI app' })` at left showing a short config editor (`K.editor`, three entries `"command": "npx"`, `"uvx"`, `"python"`); the kitchen at right.
**Beats:**
- `mcp-hire`: the app's cook tile appears; five child cooks walk in, each linked by a parent line, mono pills `node`, `npx`, `uvx`, `python`, `node` (the screen carries `npx` / `uvx`; the voice says only node or python); label "local MCP server = child process".
- `inherit`: the config's `"env"` entry (with a key in plain text) is packed into each child's small satchel, not a full copy of the app's satchel; tag "your permissions · your keys".
- `shutdown`: the app window closes; a small "please stop" card goes to each child, a short pause, then a "force" card and the remaining ones fade; then (app open again) one child stumbles and reappears: "should restart".
- `remote`: a `cloud` icon at top right holding a tiny second kitchen, with a dashed line: "remote MCP = someone else's kitchen".
- `config-is-command`: the config line zooms (`"command": "npx"`), and it morphs into a terminal prompt line; label "a config line = a command to run"; small tag "researchers, 2026".
**Exit:** the config line beside its terminal twin.

## 12 — The lantern: agents start processes for you
**Metaphor object:** the agent as head cook, and the glass fence.
**Frame:** a terminal window at left (`K.term`, title "agent"), the kitchen at right.
**Beats:**
- `agent-children`: the agent tile (`sparkle`, a head cook) sends helper cooks into the kitchen, each linked back; one goes to hatch 5173: tag "dev server: the agent's child".
- `background`: a mono pill `/tasks` with two rows "dev server · running"; tag "Claude Code: cleaned up on exit"; one cook stays after the agent tile fades: "not every tool".
- `fences`: a glass fence (dashed gold `K.card`) draws around the agent's children; tags "Claude Code: Mac · Linux · WSL2", "Codex: Windows sandbox".
- `mxc`: a second, larger fence labelled "Execution Containers · Windows · GA Oct 2026"; tag "some agents now, others planned" (no agent logos).
- `isolation`: the Task Manager Isolation column from 06 slides in at the right edge, with only the MXC process-container cook's row marked (not the Claude Code or Codex cooks), tagged "AppContainer fences only".
- `heading`: the agent tile gains its own `person` badge: label "heading: agents with their own account" (dashed outline = direction, not done).
**Exit:** fenced cooks, Isolation column, agent tile.

## 13 — Background AI already on your PC
**Metaphor object:** the grey night staff from 05, now with AI badges.
**Frame:** the Services list from 06 in a smaller window (x 200–1100, y 200–760).
**Beats:**
- `ai-services`: three rows highlight one by one with `sparkle`: "Windows AI Components Host", "ChatGPT (Codex sandbox)", "Copilot elevation service"; observation tag.
- `chrome`: a browser window at right with a `brain` card downloading (progress line); a toggle pill "off switch (newer versions)".
- `inventory`: a small map chip "01.12 What AI is already on your PC?" slides in at the bottom right.
**Exit:** three highlighted rows, chip resting.

## 14 — Your job: judge what's running
**Metaphor object:** the whole kitchen, viewed by the manager (you).
**Frame:** camera pulls back to the full kitchen (shelf, counter, hatches, night staff, fence) on the left two thirds dimmed; a checklist card on the right (x 1180–1780, y 170–880).
**Beats:**
- `your-job`: agent tile "finds · stops" and person tile "judges" (from 01) return at the card's top; heading "Five questions".
- `q-what`: "1 · file, running copy, or service?" (ticks in; the shelf, a cook and a grey cook glow).
- `q-who`: "2 · who started it?" (parent lines glow).
- `q-port`: "3 · which port?" (hatches glow).
- `q-keys`: "4 · carries my keys?" (satchels glow).
- `q-fence`: "5 · fenced in?" (glass fence glows).
- `board`: the staff board on the wall lights: "almost everything shows up here (WSL / VMs: one row)".
**Exit:** five questions, kitchen softly lit.

## 15 — Safe to ignore for now
**Metaphor object:** a small "later" shelf.
**Frame:** `K.bg()`; heading "Safe to ignore for now" (gold, y 200).
**Beats:**
- `ignore`: three pills drop onto a low shelf: "threads & priorities", "each Service Host row", "Efficiency mode".
- `pids-change`: a PID pill `18412` flips to `30556`: "changes every run".
- `power-tools`: a fourth pill "Process Explorer" joins the shelf.
**Exit:** the shelf, calm.

## 16 — Keep this
**Metaphor object:** a recipe card, an empty doorway with a cook behind it, and a fenced cook with a sparkle: one icon per takeaway.
**Frame:** end card on the painted plate (`K.plate`, shade 0.5) or `K.bg({ glow: 0.5 })`; eyebrow "Keep this"; three rows (x 200–1720, y 260 / 460 / 660), each icon + bold lead (gold, 40 px) + rest (cream, 30 px, `K.para` w 1200). Sparse petals avoiding the rows.
**Beats:**
- `keep-1`: row 1 rises: recipe-card icon, "A program is a recipe; a process is a cook using it."
- `keep-2`: row 2: night-staff cook (no door) + door that closes, "A service is a process the system keeps alive with no window."
- `keep-3`: row 3: `sparkle` cook behind a glass fence, "Your AI tools are processes too."
**Exit:** all three rows held; petals drift; fade to night.
