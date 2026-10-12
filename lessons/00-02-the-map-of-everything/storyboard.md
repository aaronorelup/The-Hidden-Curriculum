# 00.02 — The map of everything · storyboard (final; spine of draft C)

**The persistent object: "the road".** Five stop-cards in a row, joined by arrows, left to right:
`your computer` (laptop) → `the network` (wifi) → `the internet` (globe) → `services` (server) → `AI` (brain).
Standard positions (03, 04, 07, 08): card centres x = 260, 610, 960, 1310, 1660; y = 520; each `K.card` 290 × 210, r 24;
icon `K.icon(name, x, y - 30, 72)`; label `K.text` 'ui' 32 `K.C.strong` at y + 60; eyebrow "STOP 1…5" (20 px) at y − 88.
Arrows `K.arrow` between card edges at y 520, `K.C.line2`, drawn with k. The lantern string (five `K.icon('lantern')`, s 44,
gold glow, on a `K.line` at y 250) hangs over the road whenever the Lanterns are named. The road is drawn once and only moves,
shrinks, dims or gains layers; it is never redrawn from scratch. All text inside x 80–1840, y 130–930; nothing essential below 930.
One `'back'` overshoot per scene at most. Labels ≤ 8 words, ≥ 26 px.

## 01 — One road, five stops
**Metaphor object:** the road, built for the first time.
**Frame:** title card. `K.plate('plate', t, {zoom:true, shade:0.45})` when `K.img.plate` exists, else `K.bg({glow:0.6, glowX:960, glowY:300})` (the card works fully on `K.bg()`). `K.petals(t, {n:6})`. Title "The map of everything" (`K.title`, 84 px) centred x 960, y 240; conclusion line from frame 0 (`K.text` 'read', 34, `K.C.body`, centred, y 312): "One road, five stops. Ask which stop." The road row at scale 0.8, y 610 (cards ghosted at 0.15 alpha from frame 0 so the shape is calm). noBadge.
**Beats:**
- `[[five-stops]]` the five cards light left to right, each on its spoken name (`S.find('computer')`, `'network'`, `'internet'`, `'services'`, `'AI'`; `K.stagger` step 0.35 as fallback); arrows between them draw as each next card lights.
- `[[which-stop]]` a terracotta `K.pill('which stop?', 960, 800, {size:34})` rises; a soft `K.ring` passes over each card once, left to right.
- `[[land]]` small gold `K.icon('pin')` markers (s 40) drop onto the top edge of each card, staggered 0.12 s: every later lesson will land somewhere here.
- On "road leading out of your room" (`S.find('road', 1)`) a gold dot (`K.glow` + 10 px dot) travels from card 1 to card 5 (2 s, `K.ease.io`) and parks at AI.
**Exit:** title, line and the full road at rest; pill held; dot glowing softly at AI.

## 02 — Where it lives
**Metaphor object:** the course map (the road waits off-screen and returns in 03).
**Frame:** `K.bg()`, then `K.map.draw(t, { t0: 0, focus: '00', pin: '00', lanterns: L, lanternLabels: LL })`, full canvas (the map already fits the safe area). Lanterns held back: `lanterns: 0`, `lanternLabels: 0` until the cue.
**Beats:**
- `[[pin]]` the map's own pin drops on 00 (Start, y 408), one `'back'` overshoot; `K.withCam` eases toward the Start label (z 1 → 1.25, target from `K.map.chipPos('00')`) over 0.8 s; pinned row wash `K.rr(c.x - 18, c.y - 19, c.w + 36, 38, 19)`.
- `[[gate]]` camera eases back to z 1 so all six districts show; districts at `dim` 0.5 except Start.
- `[[lanterns]]` `lanterns: (i) => K.stagger(t, S.cue('lanterns'), i, .15)` lights the six lanterns left to right; `lanternLabels` fades in after them.
**Exit:** whole map, Start pinned, six lanterns glowing gently.

## 03 — The road out of your room
**Metaphor object:** the road at standard positions and full size.
**Frame:** `K.bg({glow:0.5, glowX:260, glowY:520})`; the glow's x follows the lit card (eased). Cards begin as ghosts (alpha 0.15) so the whole shape is visible before each lights. Under each card a detail line (`K.text` 'ui', 26, `K.C.soft`, centred, y 680), ≤ 4 words.
**Beats:**
- `[[computer]]` card 1 lights (gold stroke glow); detail "files · folders · terminal"; `K.folder` and `K.file` (s 46) tucked in its lower corners. On "Aaron" (`S.find('Aaron')`) a `K.file(260, 790, 90, {ext:'txt', name:'script.txt'})` rises under card 1 with a soft `K.ring` (no red, no cross); on "stop one" (`S.find('one', 1)`) a thin gold arrow lifts from the file into card 1, then the file fades by `[[network]]`.
- `[[network]]` card 2 lights; detail "Wi-Fi · router"; arrow 1→2 draws.
- `[[internet]]` card 3 lights; detail "networks of networks"; arrow 2→3 draws; the globe sways a few px (`K.wave`).
- `[[services]]` card 4 lights; detail "someone else's computer"; three pills stagger in under it at y 760: "GitHub", "email", "payments" (`K.pill`, 26 px).
- `[[ai]]` card 5 lights; detail "a model, in a service"; a dashed `K.arrow` curls from card 5 back into card 4 (AI usually lives inside a service).
**Exit:** all five lit, arrows complete, pills resting; glow settles to centre.

## 04 — Follow one message
**Metaphor object:** the road, with one message travelling on it.
**Frame:** road as left in 03 (pills gone, detail lines dimmed to 0.4). `K.win(80, 150, 420, 220, {kind:'browser', title:'AI chat'})` above card 1; `K.typed` writes "What is a terminal?" from t 0.3. The message is a `K.icon('chat')` (s 48, `K.C.accent`).
**Beats:**
- `[[leave]]` the bubble drops from the chat window into card 1, slides along 1→2 (0.6 s), and on "router" (`S.find('router')`) along 2→3; card 3 pulses once.
- `[[door]]` the bubble reaches card 4. On "really" (`S.find(/really/)`, first occurrence) a small `K.icon('person')` badge (s 40) appears at card 4's front door (left edge, y ~520); the chat bubble passes through the badge (not a key) into card 5 and returns to 4.
- `[[back]]` a cream reply bubble travels 4→1 right to left (`K.ease.io`, 1.6 s) and lands in the chat window, which prints "A window where you type commands to your computer." Then, on "Programs" (`S.find('Programs')`), a short gold side-counter line draws on card 4's lower left edge with `K.pill('API', 1150, 600, {size:30})` and a small grey program tile (`K.iconTile('code')`, s 40) slides up to it; on "key" (`S.find(/key/)`) a `K.icon('key')` (s 40) appears at that side counter. The chat bubble never touches the key.
- `[[breaks]]` gold eyebrow "WHERE THE PICTURE BREAKS" at x 960, y 150; card 4 sprouts two small cards (`K.card` 180 × 110: "storage", "payments") on branching arrows at y 760 (services call services); on "your own computer" (`S.find('own')`) a small `K.icon('brain')` appears inside card 1 with label "local model" (26 px), and arrows 1→5 dim to 0.3. This scene's one `'back'` overshoot is the local brain's pop.
**Exit:** road with its branches and the local brain, at rest.

## 05 — Every district on the road
**Metaphor object:** the road, now shelving the districts.
**Frame:** `K.bg()`. Road eases up and shrinks (0.8 s): cards 240 × 150 at y 360 (same x centres), icons s 56, labels 30 px. Under it, district "shelves": wide `K.card`s (alpha 0.85) spanning the stops they belong to, each with the district name (`K.text` 'head', 34, `K.C.head`) and module range (mono 22, `K.C.soft`). Two shelf rows, y 560 and y 740, so none overlap. Names read exactly as engine/map.js draws them.
**Beats:**
- `[[machine]]` shelf under card 1 at y 560 (x 115–405): "The Machine · The Code", "01–07"; a gold bracket rises to card 1.
- `[[history]]` thinner shelf at y 740 spanning card 1 to card 4 (x 115–1455): "The History · 08"; pills "git" over card 1 and "GitHub" over card 4, the GitHub pill arriving on "GitHub" (`S.find('GitHub')`).
- `[[network]]` shelf at y 560 under cards 2–3 (x 465–1105): "The Network", "09–13"; the arrows between cards brighten, and a faint dotted tick (`K.C.line2`, alpha 0.5) runs from the shelf's right edge up to card 4's API side-counter spot, so APIs sit where the road meets the doors.
- `[[trust]]` a `K.icon('lock')` (s 48) on card 4's left edge (its door, beside where the login badge and API side counter were); shelf at y 560 under card 4 (x 1165–1455): "Trust", "14–16".
- `[[shipping]]` a small card "your app" (laptop icon) slides from card 1 along the road into a slot beside card 4, landing with the scene's one `'back'` overshoot; shelf at y 740 under the right end (x 1515–1805): "Shipping", "17–20".
**Exit:** road with its shelves beneath it, calm.

## 06 — The surprises you'll hit
**Metaphor object:** the road, small, as a "you are here" strip.
**Frame:** `K.bg()`. Road compressed to a strip at y 220 (cards 200 × 110, labels 26 px). One surprise at a time in the centre (x 480–1440, y 380–820), each replacing the last (crossfade 0.4 s). A gold `K.icon('pin')` (s 48) above the strip marks the stop the surprise belongs to.
**Beats:**
- `[[localhost]]` `K.win(510, 400, 900, 300, {kind:'browser'})`, address bar types `localhost:3000`, body "Hello from your own computer"; pin drops on stop 1; a curved `K.arrow` loops from card 1 back into card 1.
- `[[my-machine]]` two `K.win` 'terminal' side by side (each 440 × 260): "your laptop" showing `✓ tests passed`, "server" showing `Error: file not found`; between them "It works on my machine" (`K.text` 'read', 34, italic). Pins on stops 1 and 4.
- `[[four-oh-one]]` a card with `401 Unauthorized` (mono 40, `K.C.accent`) and, right of it, `K.icon('lock')` + "a key it won't accept" (30 px); pin on stop 4; on "Trust" (`S.find('Trust')`) a `K.pill('Trust')` settles beside the pin.
- `[[which-stop]]` the panel clears; the strip enlarges slightly and `K.pill('Which stop am I at?', 960, 600, {size:34, glow:true})` sits centre; the five strip cards pulse once in sequence (no flashing).
**Exit:** strip plus the question pill, still.

## 07 — The lantern: AI at every stop
**Metaphor object:** the road with its lantern string.
**Frame:** `K.bg({glow:0.7, glowY:250})`. Road at standard x, y 560 (headroom for the string). The string (`K.line`, `K.C.line2`) at y 230, x 160–1760, waits unlit.
**Beats:**
- `[[agent]]` a `K.win(80, 255, 380, 170, {kind:'code'})` above card 1; one line edits itself via `K.editor`; the lantern over card 1 lights.
- `[[across]]` a dotted arrow runs from card 1 across 2 and 3 to card 5; lanterns over cards 2 and 3 light.
- `[[mcp]]` `K.pill('MCP', 1310, 430, {size:30})` on card 4's top edge; arrows branch to two small tiles (`K.iconTile('envelope')`, `K.iconTile('book')`) at y 780; lanterns over 4 and 5 light. On "keys" (`S.find('keys')`) a small `K.icon('key')` hangs on the agent's arrow.
- `[[light]]` the whole string glows (one gentle pulse); the line "it lights every district, but doesn't walk the streets for you" fades in (`K.text` 'read', 32, `K.C.body`, centred, y 880).
**Exit:** five lit lanterns over the road, the line at rest.

## 08 — Safe to ignore for now
**Metaphor object:** the road, dimmed behind a "later" tray.
**Frame:** `K.bg()`. Road at standard row, alpha 0.35. Centred `K.card(510, 300, 900, 420)` with eyebrow "SAFE TO IGNORE FOR NOW". Items are pills that settle into the card.
**Beats:**
- `[[packets]]` two pills drop in: "router paths", "packet insides"; a faint `K.icon('wifi')` beside them.
- `[[which-cloud]]` pill "which cloud is best".
- `[[acronyms]]` a mini `K.win` (520 × 160) inside the card shows a settings row (`DNS · DHCP · subnet mask`, mono 26) that fades to 0.4 and slides down into the tray.
**Exit:** tray set aside; the road brightens back to 0.8 in the last 0.8 s, a pin glowing over "your computer" (you are here).

## 09 — Keep this
**Metaphor object:** the road, shrunk to a header ribbon over the end card.
**Frame:** end card. `K.plate('plate', t, {shade:0.55})` if present, else `K.bg({glow:0.6})`; `K.petals(t, {n:5})`. Eyebrow "KEEP THIS" at y 160. The road as a ribbon at y 230 (five icons, s 44, short arrows, lanterns above at y 180). Three rows at y 380 / 540 / 700, x 200–1720: bold lead (`K.text` 'head', 40, `K.C.head`) above its rest (`K.text` 'read', 30, `K.C.body`, maxW 1400). noBadge.
**Beats:**
- `[[keep-1]]` row 1 rises: **Everything sits on one road.** / "Your computer, the network, the internet, services, and AI lighting all of it." The ribbon's icons light in turn.
- `[[keep-2]]` row 2 rises: **Ask which stop first.** / "A problem in your room and a problem at a service's door need different fixes." A gold ring passes over the ribbon.
- `[[keep-3]]` row 3 rises: **A service is someone else's computer, with its door open.** / "Most of the AI you use lives there, and answers back to yours." A faint outbound arc first runs from the computer icon to the services icon; the services icon glows; then a reply arc returns along it to the computer icon (a reply, never an unprompted reach).
**Exit:** three rows and the ribbon held, petals drifting slowly, for the 3 s tail.
