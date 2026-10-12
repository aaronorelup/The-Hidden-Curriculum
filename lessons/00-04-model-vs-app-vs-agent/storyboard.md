# 00.04 — Model vs app vs agent · storyboard (final: B's spine, A's Notepad contrast, C's stack discipline)

**The persistent object: "the engine, the car, the wheel".** One drawing, built in pieces in 01, taken apart in 03–06,
driven across the map in 08, rebuilt on the end card. Never redrawn from scratch: later scenes move, scale, dim or add to it.

- **The engine (the model).** `K.card(-100, -70, 200, 140, {r:24, stroke:K.C.gold, glow:0.25})` in local space, two meshing
  gears inside: `K.icon('gear', -34, 0, 64)` turning at `+0.8·t` rad and `K.icon('gear', 40, -8, 46)` at `−1.1·t` (each in
  `K.at(x, y, 1, rot, …)`), and `K.pill('model', 0, 104, {size:26})` under it. Text goes in and out as mono 26 px chips riding `K.arrow`s.
- **The car (the app)**, standard position, nose right: body `K.card(560, 500, 800, 180, {r:48, fill:K.rgba(K.C.tile,.55), stroke:K.C.line2})`;
  cabin `K.card(660, 372, 420, 140, {r:36})`; windshield `K.win(684, 388, 372, 108, {kind:'browser', title:'chat', titleSize:26})`;
  wheels `K.ring(740, 690, 58, 58, k, {rot:0})` and `K.ring(1180, 690, 58, 58, k, {rot:0})`, each with a `K.icon('gear', …, 40)` hub;
  headlight `K.glow(1372, 580, 110, K.C.gold, 0.5)` (a nod to the Lanterns). The engine sits in the hood at (1220, 590), scale 0.62,
  visible through the translucent body.
- **The wheel (the agent).** Steering ring `K.ring(820, 452, 34, 34, k, {rot:0})` in the cabin; a tool rack above the roof (y 290)
  holding `K.folder` ("your files"), `K.iconTile('terminal')`, `K.iconTile('code')`; a loop of three `K.arrow`s with `bend` circling the car;
  the passenger `K.icon('person', 980, 450, 54)` in the right seat.

All text inside x 80–1840, y 130–930; nothing essential below 930. Labels ≤ 8 words, ≥ 26 px (eyebrows 20). One `'back'` overshoot per
scene at most. Camera only via `K.cam` / `K.withCam`, 0.6–0.8 s. Lab and family names only, never version numbers (00.03); pickers show
generic "Model A / Model B / Auto". Pink only as petals on 01 and 09.

## 01 — Engine, car, driver
**Metaphor object:** the whole drawing, assembled for the first time: engine, then car, then wheel and passenger.
**Frame:** title card, noBadge. `K.plate('plate', t, {zoom:true, shade:0.5, mask:[620, 820]})` when `K.img.plate` exists (only the lower
band painted, so the car sits on the teahouse street), else `K.bg({glow:0.6, glowX:960, glowY:320})`; the card is complete on `K.bg()` alone.
`K.petals(t, {n:5, avoid:[[300,140,1620,330],[540,360,1400,760]]})`. From frame 0: title "Model vs app vs agent" (`K.title`, 80, centred, y 200);
purpose line (`K.text` 'read' 32 `K.C.body`, centred, y 266): "The difference between a model, its app, and an agent."; conclusion line
('ui' 32 `K.C.head`, centred, y 316): "Engine, car, and a car allowed to drive." The car area (x 540–1400, y 360–760) starts empty except a faint
ground line `K.line(480, 760, 1440, 760, {color:K.C.line, alpha:.5})`.
**Beats:**
- `[[engine]]` the engine pops in centred (960, 560, scale 1.0; `K.pop`), gears start turning; pill "model".
- `[[car]]` the engine eases into its hood slot (1220, 590, s 0.62, 0.7 s); body, cabin, windshield, wheels draw around it (`K.stagger` step 0.15, wheels as `K.ring` k 0→1); pill "app" at (960, 730).
- `[[driver]]` the steering ring draws in the cabin; on "passenger" (`S.find('passenger')`) the person icon fades into the right seat; pill "agent" beside the wheel (820, 336) lands with the scene's one `'back'`; the headlight eases on.
- `[[which-layer]]` a soft `K.ring` passes over engine, car body and wheel in turn (inner to outer), 0.4 s each; a terracotta `K.pill('which one?', 960, 880, {size:30})` rises.
**Exit:** title, both lines, the complete car at rest, gears turning slowly, headlight on, pill held.

## 02 — Where it lives
**Metaphor object:** the course map; the car waits off-screen and returns, unchanged, in 03/04.
**Frame:** `K.bg()`; `K.map.draw(t, { focus:'00', pin:'00', pinDrop:K.io(t, S.cue('pin',1), .7, 'back'), lanterns:(i)=>K.stagger(t, S.cue('lanterns',3), i, .15), lanternLabels:K.io(t, S.cue('lanterns',3)+.9) })`, full canvas (the map fits the safe area). Badge on.
**Beats:**
- `[[pin]]` the pin drops on Start (00, y 408) — the scene's one overshoot; `pinGlowK` eases the Start ring up; camera eases toward `K.map.chipPos('00')` (z 1→1.2, 0.8 s) and back.
- `[[lanterns]]` the six lanterns light left to right along the string (stagger 0.15 s), then their label row fades in; districts held at `dim` 0.5.
- `[[open]]` camera eases toward the middle lantern (`K.map.lanternAt(2)`, z 1→1.5, 0.8 s); a gold `K.ring` circles it; beside it a small `K.card` (420 × 110) rises with three pills "model · app · agent" (26 px); the rest of the map dims to 0.3.
**Exit:** close on one glowing lantern with its three-part label, the map soft behind.

## 03 — The engine: the model
**Metaphor object:** the engine alone on a stand, before any car exists.
**Frame:** `K.bg({glow:.5, glowX:960, glowY:520})`. First frame: a `K.icon('lantern', 960, 520, 120)` at 0.6 alpha crossfades (0.6 s) into the engine at (960, 520), scale 1.6, on a stand (two short `K.line`s to a base line at y 660). Eyebrow "THE MODEL" at (960, 300).
**Beats:**
- `[[engine]]` the engine is lit, gears turning; on "weights" (`S.find('weights')`) a `K.file(1320, 520, 150, {ext:'bin', name:'weights', nameSize:26})` slides out to the right; inside the card a faint column of mono digits (`0.0213  −1.07 …`, alpha .35) scrolls slowly.
- `[[labs]]` three cards rise along the top, x 520 / 960 / 1400, y 170, 340 × 90, each on its spoken lab: "OpenAI → GPT", "Anthropic → Claude", "Google → Gemini" (`K.spans`, lab `K.C.soft`, family `K.C.head`, 30 px); a thin gold `K.arrow` from each card down to the engine, stagger 0.3 s. The "THE MODEL" eyebrow fades as the cards arrive.
- `[[words]]` a mono chip "text" rides an arrow into the engine's left side (x 520 → 800); gears spin up for 1 s; a chip "more text" rides out the right side (1120 → 1400). The weights file fades to 0.5.
- `[[stand]]` three ghost outlines appear around the engine, each softly crossed with `K.icon('cross', …, 40, {color:K.C.soft})` on its spoken word: a seat (small card, "seats"), a steering ring ("wheel"), a tiny chat bubble with a clock (`K.icon('clock')`, "memory").
**Exit:** engine on its stand, gears idling, three crossed ghosts at 0.4 alpha, lab cards held at 0.6.

## 04 — The car: the app
**Metaphor object:** the car built around the same engine (the engine moves; it is not redrawn).
**Frame:** `K.bg()`. Starts from 03's engine at (960, 520), scale 1.6 (crossed ghosts and lab cards gone). Eyebrow "THE APP" at (960, 160).
**Beats:**
- `[[car]]` the engine eases into its hood slot (1220, 590, s 0.62, 0.7 s); body, cabin, windshield and wheels draw around it (stagger 0.15). On each spoken name a pill fades in on a row at y 830: "ChatGPT", "Claude app", "Gemini app", "Copilot" (26 px).
- `[[parts]]` labelled tags attach on their spoken words (`S.find`), leader lines `K.line` 1.5 px `K.C.line2`: "chat window" on the windshield, "saved chats" on the cabin roof, "file uploads" on the trunk (small `K.file`, left end of the body), "safety checks" on the body side, "the bill" on the rear bumper.
- `[[rules]]` a folded note `K.note(140, 300, 360, 'SYSTEM PROMPT', 'Be helpful. Be brief. Never…', {size:26})` slides from the left and tucks behind the windshield; a short arrow from the note to the engine (the model reads it first). The five tags dim to 0.4.
- `[[many-cars]]` camera pulls back (z 1→0.62, 0.8 s): two simplified cars (body + cabin + wheels) appear left and right; a gold dashed `K.line` from the one engine reaches into all three hoods; labels under them (26 px after zoom-scale, i.e. drawn at 42): "the lab's app", "a code editor", "a help desk". On "swap" (`S.find('swap')`) the centre car's engine slides down and out and a second engine (gears in `K.C.accent`) slides in; a picker pill "Model A ▾" above the windshield flips to "Model B ▾" — the scene's one `'back'`.
- `[[names]]` camera returns to the centre car (z 1); side cars and product pills fade. Name chips land (mono 30): "ChatGPT" on the body (car), "GPT · #" on the engine ("#" literal, never a real number); then "Claude" and "Gemini" chips appear spanning car and engine, a `K.ring` drawn around each pair (same name, two things). On "layers" (`S.find('layers')`) the "#" fades and a small pill "layers, not numbers" settles at (960, 860).
**Exit:** one car at rest, name chips held at 0.7 alpha, gears turning slowly.

## 05 — Handing over the wheel: the agent
**Metaphor object:** the same car, now given tools, a loop and a passenger; Aaron's Notepad moment sits beside it as a comparison.
**Frame:** `K.bg()`. The car from 04 in standard position, chips gone, steering ring drawn in the cabin with a soft gold glow behind it. Eyebrow "THE AGENT" at (960, 160).
**Beats:**
- `[[tools]]` a tool rack draws above the roof (`K.line` 700 → 1220 at y 300); three tools drop onto it on their spoken words: `K.folder(760, 250, 90, {name:'your files', nameSize:26})`, `K.iconTile('terminal', 960, 250, 90)` "terminal", `K.iconTile('code', 1160, 250, 90)` "edit code" (the one `'back'` on the first tool only).
- `[[loop]]` a loop of three curved `K.arrow`s circles the car (x 420–1500, y 220–860), pills at its stations as spoken: "decide" (top-left), "do it" (right), "check" (bottom); a gold dot travels the loop once (1.6 s, `K.ease.io`). On "Claude Code" (`S.find('Code')`) a muted mono label inside the loop: "coding agents work this way".
- `[[notepad]]` the car eases left and shrinks (centre x 560, scale 0.6, loop arrows to 0.3). Right half: `K.win(1000, 230, 760, 360, {kind:'notepad', title:'script.txt - Notepad', titleSize:26})` with `K.editor` showing two lines of plain Python (mono 30); beside it at (1560, 700) a `K.file(…, 140, {ext:'txt', name:'script.txt', nameSize:26})`. Three ghost items at 0.3 alpha, each on its spoken word: pill ".py ?" by the file's extension, a dim terminal prompt `C:\Users\you>` with `cd` greyed, a ghost `K.folder(1200, 720, 80, {name:'.venv', nameSize:26})` with `K.icon('question', …, 32)`.
- `[[agent-steps]]` a small `K.win(1000, 620, 380, 200, {kind:'browser', title:'chat', titleSize:26})` types the same two lines (`K.typed`, fast), and a terracotta dashed `K.line` stops its text short of the file: pill "the rest is yours" (26 px). On "An agent" (`S.find('agent', 1)`) the dashed line opens; the terminal tile from the rack slides over: the file flips `txt` → `py` ("script.py"), the prompt types `cd project` (`K.term`, cps 30) and the `.venv` folder turns solid. No caption claims the agent was part of Aaron's story: the screen stays literal (a comparison).
- `[[ask]]` the Notepad group fades to 0.25; the car returns to centre at full size, dot parked at "do it". A small dialog `K.win(1240, 360, 520, 200, {title:'agent', titleSize:26})` by the passenger: "Run this command?" (30 px) with pills "Yes" / "No"; the passenger icon glows gold.
**Exit:** car stopped mid-loop, dialog open, passenger lit, loop arrows at 0.6 alpha.

## 06 — Where the picture breaks
**Metaphor object:** the car opened up to show the real mechanism (the hood lifts; the car is not replaced).
**Frame:** `K.bg()`. Car in standard position shifted left (centre x 820), body alpha 0.35 so the engine reads clearly. Eyebrow "WHERE THE PICTURE BREAKS" at (960, 160).
**Beats:**
- `[[cold]]` the gears stop between messages (card alpha 0.5). A stack of four small chat lines (`K.card`s, 200 × 34) sits in the cabin; on "rereads" the whole stack slides from the cabin into the engine (arrow, 0.6 s), the gears spin once, then stop; it repeats once with one more line. On "memory lives" a pill on the cabin: "memory lives in the car" and a gold `K.ring` around the stack (not the engine).
- `[[bench]]` a second engine on a bare stand appears at right (1500, 600, s 1.0) with no car around it; a small program window `K.win(1340, 280, 340, 150, {kind:'code', title:'program.py', titleSize:26})` sends an arrow to it, with a `K.icon('key', …, 44)` on the arrow and a mono label "API" (26). Crossed-out ghosts beside the bench: "chat window", "saved chats" (26 px, 0.5 alpha).
- `[[driver]]` back on the car: the steering ring fades to an outline; a `K.icon('question')` appears in the driver's seat, then fades — there is no separate driver. Over the engine a label "engine: writes text" (26 px).
- `[[app-runs]]` a mono chip rises from the engine: `run: npm test` (screen literal; never spoken); it travels into the car body, waits at a small `K.icon('lock', …, 36)`, a pill "allowed" appears (the scene's one `'back'`), and the chip lands in a `K.iconTile('terminal')` that lights. Label "app: runs it" over the body.
**Exit:** car with lifted hood, engine idle, the run chip resting in the lit terminal tile, bench engine dimmed to 0.4.

## 07 — The surprises you'll hit
**Metaphor object:** the car, small at left (centre x 400, scale 0.45), as the anchor; a gold `K.icon('pin', …, 36)` above it marks which layer each surprise belongs to (engine, car body, or passenger).
**Frame:** `K.bg()`. Eyebrow "THE SURPRISES" at (400, 200). Four cards in a 2 × 2 grid on the right: x 760–1820, y 170–880, each 500 × 330, r 24, 20 px eyebrow "SURPRISE 1"…"4", caption ('ui' 30 `K.C.head`) top-left inside. Active card alpha 1, earlier cards 0.45.
**Beats:**
- `[[different]]` card 1 "same question, two apps": two tiny chat windows (`K.win` kind 'browser', 220 × 170) both showing "Name a first project?" and different replies ("A to-do app" / "A website", 26 px); a small "system prompt" pill under each in different colours. Pin on the car body.
- `[[api-memory]]` card 2 "the API doesn't know your chats": a small code window with a `K.icon('key')` and mono `history: [ ]` (26); a dashed line from the car's "saved chats" stops short of it. Pin on the engine. On "different door" a pill "same engine, different door".
- `[[allow]]` card 3 "it asks first": a terminal with the prompt "Allow this command?", the command `npm test` (mono 26) and pills "Yes" / "No"; the passenger on the small car glows. On "Read" (`S.find('Read')`) a gold `K.mark` underlines the command — the scene's one `'back'` is the card's landing.
- `[[which-model]]` card 4 "which model is this?": a title bar with a picker showing "Auto ▾"; it opens to "Model A / Model B / Model C" (26 px), "Auto" glows on "choose for you"; on "ask the model" a chat bubble "Which model are you?" gets a reply bubble with a `K.icon('question')` and a terracotta pill "not reliable". Pin on the car body.
**Exit:** four cards at 0.8 alpha, small car idling at left.

## 08 — Driving across the map
**Metaphor object:** the car, shrunk to a small marker (body + cabin + wheels, ~110 px long, headlight on), driving the course map — the "where it connects" scene.
**Frame:** `K.bg()`; `K.map.draw(t, { focus:null, dim:0.55, pin:'00', pinK:0.4, lanterns:L, lanternLabels:0.6, rowWash:W })`. The mini car starts at the Start gate (x ~135, y 408); a gold `K.line` route draws behind it (alpha .8).
**Beats:**
- `[[machine]]` the mini car drives to The Machine (`K.map.district('machine')`); row 03 washes gold (`rowWash`), pill "your files, your terminal" (26) above the district.
- `[[history]]` it drives on to The History (`K.map.chipPos('08')`); row 08 washes; pill "git".
- `[[trust]]` it drives to Trust (`K.map.chipPos('14')`); row 14 washes; a `K.icon('key', …, 36)` hangs from the mini car; pill "keys to your accounts".
- `[[lantern-line]]` all six lanterns brighten together (glow eased up, then back to 1, no flash); on "where you let it" a small `K.icon('lock', …, 36)` closes in front of the mini car at the Trust edge, and the drawn route glows once.
- `[[later]]` a `K.card` (380 × 90) "this month's #1 model" (with three grey bars, no numbers) drifts in at top right and slides down to a "LATER" shelf (eyebrow at (1600, 860), `K.line` at y 880), dimming to 0.4.
**Exit:** map held, route drawn, mini car parked at Trust behind its lock, three rows washed, the leaderboard card resting on the shelf.

## 09 — Keep this
**Metaphor object:** the complete drawing again, as in 01: engine, car, wheel, tools and passenger.
**Frame:** end card, noBadge. `K.plate('plate', t, {shade:0.55, mask:[620, 820]})` when present, else `K.bg({glow:.6, glowX:960, glowY:300})`; `K.petals(t, {n:4, avoid:[[120,130,1800,930]]})` (far margins only). Eyebrow "KEEP THIS" at (960, 150). The car at the top, centre (960, 330), scale 0.62. Three takeaway rows at x 260, y 600 / 690 / 780: bold lead `K.C.head` (`K.spans`, 'ui' 34, weight 600) + rest `K.C.body` ('read' 30), each ≤ 8 words of rest on screen:
1. **The model is the engine.** Numbers from a lab. No memory.
2. **The app is the car.** Window, chats, instructions, bill.
3. **An agent is the car you let drive.** Tools, a loop, your say.
**Beats:**
- `[[keep-1]]` row 1 rises; the engine in the car glows gold for 1 s.
- `[[keep-2]]` row 2 rises; the car body outline brightens.
- `[[keep-3]]` row 3 rises; the steering ring, tool rack and passenger glow; the headlight eases fully on.
**Exit:** all three rows held, car at rest with headlight lit, petals drifting in the margins.
