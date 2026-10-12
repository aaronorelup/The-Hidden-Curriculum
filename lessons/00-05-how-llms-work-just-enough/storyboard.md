# 00.05 — How AI models work today · storyboard (final: the clerk's desk under the lantern)

**The persistent object: "the desk under the lantern".** One drawing for the whole lesson. It is built once in 01, shrunk to its
2021 size in 03, then only ever grows, gains things, loses things or is reframed by the camera. Nothing is redrawn from scratch;
every later scene draws the same function `desk(t, state)` with a different state (size, papers, add-ons). The lantern that lights the
desk is the course's AI lantern (the same `K.map.lantern` glow), so the metaphor and the map are visibly one thing.

Standard parts (world coordinates on the 1920×1080 canvas, camera via `K.cam` / `K.withCam` only):

- **The lantern (lamp).** Cord `K.line(960, 112, 960, 168, {color:K.C.line2})`; `K.map.lantern(t, 0, {x:960, y:200, s:1.3, glowK:1.4})`;
  pool of light `K.glow(960, 560, 520, K.C.gold, 0.18)` on the desk. In 08 it grows two dials.
- **The desk.** Surface `K.card(960 − w/2, 600 − h/2, w, h, {r:24, fill:K.rgba(K.C.tile,.9), stroke:K.C.line2, glow:.15, shadow:true})`
  plus a front lip `K.card(960 − w/2, 600 + h/2 − 10, w, 22, {r:8, fill:K.C.line, stroke:K.C.line2})`. Sizes: **2021** w 420 h 200;
  **standard** w 1100 h 380; **hall** w 1600 h 520 (fills x 160–1760). Size changes ease over 0.8 s (`K.io`), never jump.
- **The clerk (the model).** `K.iconTile('sparkle', 960, 600 − h/2 − 70, 104)` standing behind the desk's far edge, pill
  `K.pill('the model', 960, 600 − h/2 − 140, {size:26})` shown only when named. Idle `K.wave` bob of 3 px. A small pen
  `K.icon('code', …, 34)` beside it ticks right one step per ~0.5 s when it "writes" (one token after another).
- **Papers.** Text cards `K.card(…, 120, 80, {r:10, fill:K.C.paper})` with two `K.line` rows; files via `K.file(x, y, 110, {ext, name, nameSize:26})`
  for `pdf`, `png`, `mp3`, `mp4`, `md`. Papers slide onto the desk from the edges (0.6 s, `K.rise`/`K.io`).
- **The token ruler.** A row of 14×14 tile squares along the desk's near edge (`K.card(…, 14, 14, {r:3})`, 6 px gaps), the ruler length tracking the
  desk width; a mono 30 px counter pill at the right end ("2K", "100K", "1M").
- **The letter slot door (left).** `K.card(130, 340, 170, 420, {r:18, stroke:K.C.line2})` with slot `K.card(160, 520, 110, 14, {r:7, fill:K.C.page})`
  and `K.pill('A P I' → displays 'API', 215, 300, {size:26})`. Letters: `K.icon('envelope', …, 44)`.
- **The studio (right).** `K.card(1610, 340, 190, 420, {r:18, stroke:K.C.accent})`, eyebrow "STUDIO", inside a 150×150 square "canvas" well
  (square element, brand rule 4) that shows noise or a picture; a phone line `K.arrow` from the clerk to it, `dash:[8,8]`.

All text inside x 80–1840, y 130–930; nothing essential below 930. Labels ≤ 8 words, ≥ 26 px (eyebrows 20). One `'back'` overshoot per scene
at most. Dated cards (versions, prices) carry a mono 22 px eyebrow "Oct 2026". Beta / research-preview features carry a `K.pill` badge.
Pink only as petals on 01 and 20. Guest scenes (18–19): lower-third `K.card(80, 846, 360, 64)` with `K.eyebrow('GUEST', 104, 872)` +
`K.text('June', 104, 900, {size:30, font:'ui', color:K.C.strong})` reading "guest · June", and the palette accent shifts brighter:
the lantern glow goes from `K.C.gold` to `K.mixColor(K.C.gold, K.C.head, .6)` at 1.4× strength, accents use `K.C.head` instead of `K.C.accent`.

---

## 01 — The clerk at the desk
**Metaphor object:** the desk under the lantern, assembled for the first time (standard size), empty except one text card.
**Frame:** title card, noBadge. `K.plate('plate', t, {zoom:true, shade:0.55, mask:[640, 860]})` when `K.img.plate` exists (painted
teahouse street only in the lower band, the desk sits on it); else `K.bg({glow:.6, glowX:960, glowY:260})`. The card is complete on
`K.bg()` alone. `K.petals(t, {n:5, avoid:[[240,130,1680,360],[400,380,1520,820]]})`. From frame 0: `K.title('How AI models work today', 960, 190, {size:76, align:'center'})`;
purpose line `K.text('What they take in, make, remember, cost, and where you meet them.', 960, 252, {font:'read', size:30, color:K.C.body, align:'center'})`;
conclusion line `K.text('A model only knows what is on its desk.', 960, 300, {font:'ui', size:32, color:K.C.head, align:'center'})`.
The desk zone (y 380–820) holds only the lantern, dim.
**Beats:**
- `desk`: the lantern lights (glow 0 → 1, 0.8 s); the desk surface rises into its pool of light (`K.rise`), the clerk tile appears behind it; one text card lands on the desk.
- `desk-fills`: three things arrive in turn (stagger 0.15): a `png` file slides onto the desk, a dashed phone line draws to the right edge (studio outline faint), and the whole desk glides 40 px on a faint "where it sits" floor line.
- `shelves`: a row of six small gold pills fades in along y 880 ("Machine · Code · History · Network · Trust · Shipping"), 26 px, each with a tiny `K.icon('pin', …, 26)`, plus a quiet 26 px line above them "a minute or two each · own lessons later".
**Exit:** desk, clerk, lantern still; pills settle; title and lines hold.

## 02 — Where it lives
**Metaphor object:** the lantern over the desk, lifted out to become one of the map's lanterns, then returned.
**Frame:** `K.bg()`; `K.map.draw(t, {focus:'00', pin:'00', pinDrop, lanterns, lanternLabels})`. The desk from 01 shrinks (scale 1 → 0.28) and
slides to the lower-left corner (x 260, y 800, decorative only), crossfading out by 0.8 s.
**Beats:**
- `pin`: pin drops onto Start / 00 (`pinDrop: K.io(t, a, .7, 'back')`, the scene's one overshoot); `pinGlowK` eases in; the Start question stays as the map draws it.
- `lanterns`: the six lanterns light left to right (`lanterns: i => K.stagger(t, a, i, .12)`), the label row fades in (`lanternLabels`).
- `tour`: (also carries "you won't be able to do it yet") lantern 0 is lifted (`lanternHide`) and redrawn larger with `K.map.lantern(t, 0, {s:1.6})` as it glides to centre (960, 360); under it a faint ghost of the desk fades in (alpha 0.35): this lantern is the lamp over our desk.
- `shelve`: three `K.arrow`s draw from the lantern down to rows on the map, each row washed (`rowWash`): '06' (The Code), '10' (The Network), '15' and '16' (Trust); tiny labels "memory", "plugins · caching", "plans · personal agents" (26 px) beside the arrows.
**Exit:** map calm, pin glowing, the lantern back in its place on the string (`lanternHide` → 0), arrows faded.

## 03 — The desk, five years ago and now
**Metaphor object:** the desk at its 2021 size, then the hall-sized desk; the clerk stays the same tile in both.
**Frame:** `K.bg({glowX:960, glowY:220})`. Standard parts at centre. Year eyebrow top-right (x 1700, y 160, mono 30): "2021" then "Oct 2026".
**Beats:**
- `clerk`: camera eases in a touch (z 1 → 1.08); the clerk tile glows; pill "the model" pops above it; a `K.note(1260, 200, 480, 'BUILDS ON 00.04', 'model · app · agent')` fades in small at top-right and out after 3 s.
- `small-desk`: the desk shrinks to its **2021** size (420×200); the year eyebrow reads "2021"; two text cards only; the token ruler shows a short row of squares with pill "~2K tokens"; the letter-slot door fades in at left and one envelope slides through the slot onto the desk. Faint crossed-out pills drift in above and fade: "chat app", "memory", "tools" (each with `K.icon('cross', …, 26)`).
- `now`: the desk eases to **hall** size (0.8 s); the year eyebrow becomes "Oct 2026"; a `png`, a `pdf` and an `mp3` file land on it; around it, faint outlines of rooms (three dashed `K.card`s at top-left/top-right, labels "rooms"), phone lines (two dashed arrows out to the right edge) and the studio door at right.
- `same`: everything except desk, clerk and one text card dims to 30%; the pen beside the clerk writes: a row of small token squares appears one at a time (0.35 s apart), pill "one piece at a time".
- `overnight`: a moon `K.icon('clock', 1700, 300, 56)` turns; the papers slide off the desk and fade, then slide back on together (all at once, 0.6 s): pill "handed over every time".
**Exit:** hall desk with three papers, clerk idle, lantern glow steady.

## 04 — Tokens, and a desk that grew
**Metaphor object:** the token ruler on the desk's near edge, and the desk's growth from 2K to 1M.
**Frame:** `K.bg()`. Desk at standard size, slightly lower (y 640) so a word strip fits above it at y 200.
**Beats:**
- `tokens`: a word strip `K.spans` at y 220, 40 px mono: "un|believ|able" splits into three tile chips (gaps open 0.5 s); caption pill "≈ 4 characters of English"; the chips drop onto the ruler as three squares.
- `all-counts`: six things land on the desk in turn (stagger .18), each with a 26 px label: "hidden instructions" (pinned card), "messages" (two text cards), "files" (`pdf`), "images" (`png`), "tool results" (`K.iconTile('terminal')`), "thinking + reply" (pen card). The ruler fills to match.
- `growth`: a dated timeline card (`K.card(160, 160, 1600, 120)`, eyebrow "CONTEXT WINDOW · Oct 2026"): ticks "2020 · ~2K", "2023 · 100K (Claude)", "2024 · 1M (Gemini)", "2026 · 1M on Claude's bigger models"; as each tick lights, the desk eases wider (420 → 800 → 1600 px; the last step is the hall).
- `meter`: a slim app status bar slides in at the top-right (`K.card(1240, 180, 560, 64)`): a gold fill bar with mono 26 px "context: 38% used · 62% left" (illustrative); the bar ticks up as one more paper lands.
- `compare`: two small cards side by side at y 380: the same sentence above each, "Model A: 100 tokens", "newer Claude: up to ~135 tokens"; pill "counts don't compare".
- `breaks`: the "where it breaks" beat: the clerk tile fades and three translucent copies appear briefly, each reading the whole desk at once (a soft scan band sweeping the entire desk in one pass, not line by line); eyebrow "WHERE THE PICTURE BREAKS" at y 160.
**Exit:** hall-sized desk, full ruler with counter "1M", single clerk back.

## 05 — A fuller desk is a worse desk
**Metaphor object:** the hall desk piled high; the tidy-up tools.
**Frame:** `K.bg()`. Hall desk; a stack of 30 paper cards builds up across it (deterministic jitter via `K.rng(5)`).
**Beats:**
- `pile`: the pile grows over 2 s; a quality meter (vertical bar at x 1760, y 260–700, label "accuracy") falls as the pile grows, well before the ruler reaches its end; pill "context rot" with eyebrow "CHROMA · 2025 · 18 models".
- `middle`: one gold-edged card in the middle of the pile is ringed (`K.ring`), then its ring fades as the cards above it dim it: label "lost in the middle". The clerk's scan band covers the whole pile at once; the middle cards stay darker.
- `compact`: eyebrow "TIDYING THE DESK" fades in at y 160; the pile slides together into one page (`K.card` 240×300, title "summary"); a terminal strip at the top-right `K.win(1180, 200, 600, 140, {kind:'terminal', title:'claude'})` prints "auto-compact" and then `/compact`.
- `sweep`: three grey tool-result cards slide off the desk's left edge and fade.
- `second-clerk`: a second, smaller desk appears at right (scale 0.45) with its own sparkle clerk; a dashed arrow sends a task card to it; a short report card returns.
- `context-eng`: pill "prompt engineering" morphs into "context engineering" (crossfade, 0.6 s) above the tidy desk; a small shelf chip "own lesson · The Machine" with `K.icon('map')` fades in at bottom-right (x 1640, y 880).
**Exit:** tidy hall desk with one summary page, quality meter back up, second clerk dimmed at right.

## 06 — Seeing, hearing, and making
**Metaphor object:** the desk receiving many kinds of input; the studio door opens; the phone line to it.
**Frame:** `K.bg()`. Hall desk left-centre (centre x 860), studio door at right (x 1610).
**Beats:**
- `inputs`: `png`, `pdf`, `mp3`, `mp4` files fall onto the desk one after another; the word "multimodal" (`K.title`, 56 px) appears at y 170 and splits into three numbered slots below it ("1 reads", "2 makes", "3 hands off").
- `reads`: slot 1 lights; two dated cards at top-left: "Claude: text · images · PDF in" and "Gemini: text · image · audio · video in" (eyebrow "Oct 2026").
- `makes`: slot 2 lights; a small picture appears on the desk from the clerk's pen, then gets a "rare" pill (quiet colour).
- `handoff`: slot 3 lights brightest; the phone line draws from the clerk to the studio door; the studio door opens (card stroke brightens), label "separate model · API or tool".
- `claude-text`: the clerk writes a code card (`K.editor` strip, 4 lines, syntax 'py') that turns into a small bar chart; beside it, a connector plug arrow to the studio; caption "Claude writes text only".
- `stitched`: a "ChatGPT" window `K.win(1180, 220, 560, 260, {kind:'browser', title:'ChatGPT'})` appears; behind it, slides out to show three tiles stitched with lines: "chat model", "image model", "voice model".
- `sora`: a small card "Sora app" at top-right gets a "closed · spring 2026" pill and fades to 30%. Then a chat input bar (`K.card(560, 820, 800, 70)`) with a `K.icon('puzzle')` paperclip stand-in: a `png` and `pdf` chip get a check, an `mp4` chip a `K.icon('cross')` ("accepts some files, refuses others"); shelf chip "own lesson · The Network".
**Exit:** desk with mixed files, studio door open, phone line glowing softly.

## 07 — Diffusion: from static to picture
**Metaphor object:** inside the studio: the square canvas well, from static to picture.
**Frame:** the scene opens already inside the studio (06 ends on its open door; the crossfade reads as walking through): a big square canvas well `K.card(660, 230, 600, 600, {r:6})` centre (square element), a step counter at right.
**Beats:**
- `noise`: the well fills with deterministic static (grid of 4 px squares, `K.rng(7)` greys, re-seeded per frame step of 0.1 s; low contrast, no flashing).
- `steps`: a vertical strip of five thumbnails in the right column (x 1340–1500, y 230–830), each less noisy; a pill "prompt: a teahouse at night" nudges each step (arrow to each thumbnail).
- `picture`: the big well resolves into a simple drawn picture made from kit shapes (a lantern icon, a roof line, a moon ring); eyebrow "compressed space → expand" small at top.
- `families`: four pills orbit the well: "images", "video", "audio", "music"; a fifth, quieter: "flow matching: fewer steps".
- `not-all`: a second small canvas at left builds a picture tile by tile in reading order (left to right, row by row); label "piece by piece, like text (reported)".
- `text-diffusion`: a small page card at left: a smudged paragraph (blurred grey bars) sharpens all at once into lines; pills "Mercury (Inception)", "Google, experimental"; badge "fast · not frontier".
- `frontier`: below it, the clerk's pen card writes tokens one by one; label "top chat models: one token after another"; then eyebrow "WHERE THE PICTURE BREAKS" with line "not a clerk at all", and shelf chip "own lesson · The Machine".
**Exit:** finished picture in the well, calm static gone, side items dimmed.

## 08 — The knobs, then and now
**Metaphor object:** the lantern over the desk grows dials.
**Frame:** `K.bg()`. Camera eases up to the lantern (z 1.15, centre y 380): lantern at (960, 260), three round dials (`K.ring` + needle line) hanging from its base at x 700, 960, 1220, y 520, labels 26 px under each.
**Beats:**
- `temperature`: dial 1 "temperature" needle sweeps; the clerk's next word chip flickers between three candidates (slowly, 0.5 s each).
- `top-p`: dial 2 "top-p · top-k"; a row of five candidate word chips, the last three fade out (fewer choices).
- `max`: dial 3 "max output tokens"; a reply card with a hard gold line where it gets cut.
- `taped`: strips of tape (`K.card`, rotated −8°, fill `K.C.line2`) cover dials 1 and 2; an error card slides in at right `K.win(1240, 600, 560, 160, {kind:'terminal', title:'response'})` printing "temperature is not supported for this model" (generic wording); eyebrow "NEWEST CLAUDE MODELS · 2026".
- `effort`: a new, larger dial appears under the lantern: "effort", with a segmented picker `low · medium · high · xhigh · max` (pills); the needle moves from medium to high; the clerk's scratch-paper stack grows with it. A small app picker row: "model · effort · speed".
- `wrong`: a reply card with a confident gold tick turns out wrong (tick becomes `K.icon('warning')`); two follow-up pills: "wrong action", "invented package name"; shelf chip "settings · The Network".
**Exit:** taped old dials, the effort dial lit, lantern steady.

## 09 — How it "remembers"
**Metaphor object:** five paths by which paper returns to the hall desk.
**Frame:** `K.bg()`. Hall desk centre-low (y 680, w 1300 h 300); five sources arranged in an arc above it (y 220–400) at x 260, 610, 960, 1310, 1660, each a tile with number badge.
**Beats:**
- `five`: title line "the clerk keeps nothing" (eyebrow) at y 150; five empty numbered slots appear in the arc.
- `convo`: 1 "conversation": a stack of message cards drops onto the desk from slot 1 (arrow), with a loop arrow "every turn".
- `profile`: 2 "memory it keeps": a profile card `K.card` with `K.icon('person')` and three lines; the pen edits one line; pills "Claude · ChatGPT · Gemini".
- `search`: 3 "past chats": a filing cabinet (stacked cards) with `K.icon('question')`; a status line on the desk "Searched past chats" (illustrative, mono 26 px); a small pill "free on Claude since Mar 2026" sits under slot 2.
- `external`: 4 "files · Notion · Drive": a `K.folder` with `memory.md`, and a globe tile labelled "Notion / Drive" joined by a dashed connector line; label "tool call".
- `rag`: 5 "RAG": a catalogue of index cards; three cards are pulled, laid on the desk, then the clerk writes; mini flow "fetch → desk → answer"; small pills "vector search" and "file search (coding agents)".
- `cost`: each arrow into the desk gets a small tile counter tick on the ruler; pill "each costs desk space"; shelf chip "memory · RAG · The Code".
**Exit:** five sources in an arc, papers on the desk, arrows faded to 30%.

## 10 — Notes pinned to the desk
**Metaphor object:** sticky notes pinned along the desk's far edge.
**Frame:** `K.bg()`. Standard desk centre (y 640); a pin rail along its far edge (y 470); right side a file tree for a project.
**Beats:**
- `system`: note 1 pinned (gold pin): "system prompt · the app's"; a small `K.pill('published by Anthropic', …)` under it.
- `yours`: note 2 pinned: "your instructions"; loop arrow "every turn".
- `claude-md`: an explorer window `K.win(1260, 200, 520, 420, {kind:'explorer', title:'my-project'})` shows `CLAUDE.md`, `src/`, `README.md`; `CLAUDE.md` glows and flies to the desk as note 3, pinned automatically ("loads at session start"); two faint extra notes "user folder" and "company" slide in behind it.
- `agents-md`: `AGENTS.md` appears faintly in the tree beside `CLAUDE.md`, with a pill "open version" and a small note "Claude Code: only if no CLAUDE.md"; small chips "GEMINI.md", "Cursor rules".
- `not-lock`: a padlock icon `K.icon('lock')` drops beside the notes and is labelled "hooks · permissions = lock"; the notes get the label "a note asks"; a long note sags and its text fades halfway ("long notes: followed less"); shelf chip "own lesson · The Machine".
**Exit:** three notes on the rail, tree dim, lock icon at the side.

## 11 — Keeping the desk warm: caching
**Metaphor object:** the desk laid out in order under a timer.
**Frame:** `K.bg()`. Desk viewed as three ordered layers stacked top to bottom on its surface: "tools" (top), "system prompt", "messages" (bottom), each a wide card band; a timer `K.icon('clock')` with ring progress at top-right (x 1640, y 240).
**Beats:**
- `layout`: (the narration opens with "re-sending the whole desk is slow and expensive": a ghost of the desk slides in from the left three times, then the glow settles) the layers lay themselves out (stagger); a warm glow (`K.glow` gold) settles on the whole layout; label "prefix · stored by the provider".
- `order`: numbers 1, 2, 3 appear beside the bands; arrow downward "order".
- `swap`: a card in the top band is swapped for a different one; everything below it lifts off and re-lays from scratch (0.8 s), glow goes cold then warm again; label "change early → rebuild".
- `timer`: timer ring runs; label "time to live: 5 min · or 1 h"; each new message makes the ring snap back to full ("reuse resets"); dated card: "Claude Code: 1 h subscription · 5 min API key" (eyebrow "Oct 2026").
- `cold`: the ring runs out; the glow fades to cold blue-grey (`K.C.line2`); a coffee cup `K.icon('tea')` at the side; the next message makes the whole layout rebuild.
- `breakers`: a list card at right, items appearing one by one (26 px): "switch model", "tools change", "old images dropped", "compaction", "effort (older models)", then a quiet struck-through chip "edit CLAUDE.md: waits for next session".
- `not-memory`: eyebrow "WHERE THE PICTURE BREAKS": "stored arithmetic, not memory".
**Exit:** layout warm, timer full, list dimmed.

## 12 — The four meters
**Metaphor object:** four meters on the wall above the warm desk.
**Frame:** `K.bg()`. The desk from 11 drops lower (y 760, scale 0.8); four round meters across the wall at y 330, x 330, 750, 1170, 1590 (`K.ring` + needle + mono label); each meter's label is the `usage` field in mono 26 px under a plain-word label.
**Beats:**
- `input`: meter 1 "fresh input · full price" / `input_tokens`; fresh paper lands on the desk.
- `write`: meter 2 "cache write" / `cache_creation_input_tokens`; tag "1.25× · 5 min" and "2× · 1 h" (eyebrow "Claude API, Oct 2026").
- `read`: meter 3 "cache read" / `cache_read_input_tokens`; tag "≤ 0.1×".
- `output`: meter 4 "output (incl. thinking)" / `output_tokens`; tag "≈ 5×"; meter 4's needle swings furthest.
- `fields`: the four mono field names under the meters brighten together inside a small `K.win(..., {kind:'code', title:'usage'})` frame drawn around them (no new text).
- `long-chat`: a chat thread grows in a narrow card at left; each new turn re-sends the whole desk (the layout pulses), meters 1–3 tick each turn; caption "cheap only while warm".
- `still-fills`: cache-read papers keep their size on the ruler; pill "cheaper, not smaller".
- `others`: small chips "OpenAI · automatic", "Google · automatic", "Claude API · one setting"; shelf chip "own lesson · The Network".
**Exit:** four meters still, desk warm.

## 13 — Rooms and buildings: modes and platforms
**Metaphor object:** the desk placed into rooms (modes) inside buildings (platforms).
**Frame:** `K.bg()`. Camera pulls back (z 1 → 0.7) so the desk becomes a small icon inside a floor plan: three rooms side by side (cards at y 260–560): "Chat", "Cowork", "Code", each containing a mini desk.
**Beats:**
- `mode-vs-platform`: two labels: "mode = the kind of job" over the rooms, "platform = where it runs" over a row of building tiles beneath (y 640–820).
- `modes`: the three rooms light; Cowork gets a small tag "Jan 2026 · office work on your files".
- `merge`: the wall between Chat and Cowork slides away; the two rooms merge into one labelled "Claude"; tabs "Chat · Cowork · Code" crossfade to "Claude · Claude Code"; a pill "rolling out · Pro and Max first" (badge style); "Code" stays its own room.
- `buildings`: building tiles appear in a row: `K.iconTile('globe')` browser, `K.iconTile('laptop')` desktop, `K.iconTile('phone')` phone, `K.iconTile('terminal')` CLI, `K.iconTile('code')` editor, `K.iconTile('cloud')` cloud.
- `local-cloud`: the laptop tile and cloud tile enlarge side by side; laptop: a folder icon + a moon that turns its desk dark ("stops when it sleeps"); cloud: a lit window that stays lit ("keeps going, sees what you give it").
- `equivalents`: a dated card at top-right: "OpenAI: Chat · Work · Codex (Jul)", "Google: Gemini CLI → Antigravity (Jun)" (eyebrow "Oct 2026"); shelf chip "coding agents · The Machine".
**Exit:** merged room, Code room, building row calm.

## 14 — Skills, connectors, plugins
**Metaphor object:** a shelf of manuals, phone lines and boxed kits beside the desk.
**Frame:** `K.bg()`. Standard desk at left-centre (centre x 760); shelf at right (x 1180–1780, y 220–560); a shop counter row at the bottom (y 640–860).
**Beats:**
- `skill`: three book spines (`K.card` 40×200, gold edges) on the shelf; only a small label card from one sits on the desk; when the clerk reaches for it, the full book opens: `SKILL.md` file + a `py` script; pill "open format".
- `connector`: phone lines draw from the desk to three tiles: "Gmail", "Notion", "GitHub"; label "built on MCP".
- `plugin`: a box (`K.card` with a lid line) gathers a book, a phone plug, a command chip "/" and a hook icon `K.icon('gear')`; label "plugin = a kit".
- `shops`: the counter row shows four shop tiles (shelf chip "own lessons · The Network" at the end): "in-app directory", "Claude Marketplace · expanded Sep 2026", "plugin marketplaces = git repos" (`K.folder` with a branch line), "OpenAI apps · plugins".
- `trust`: a `K.icon('warning')` drops on a plugin box; caption "third-party = code you trust"; small card "OpenClaw skill store · Feb 2026: hundreds malicious".
**Exit:** shelf, lines, box; warning icon dimmed to 40%.

## 15 — Individual vs enterprise
**Metaphor object:** the same desk in a home office and in a company building.
**Frame:** `K.bg()`. Split screen: left a house outline (`K.icon('house')` large, x 160–900) holding the desk; right a company building card (x 1020–1760) holding an identical desk. Divider line at x 960.
**Beats:**
- `home`: left lights: plan pills "Free · Pro · Max" with a usage gauge; a small toggle card "training: on unless you switch off" (since autumn 2025).
- `company`: right lights; around its desk appear: a badge door `K.icon('key')` "single sign-on", an approved list card "allowed connectors · plugins · skills", a log book `K.icon('book')` "audit logs", a clock `K.icon('clock')` "retention", and instruction notes pushed to three small laptops.
- `no-training`: a toggle on the right reads "not trained on by default"; a calendar card "notice before changes".
- `third-party`: an OpenClaw tile tries to plug into the home desk's subscription; the plug is blocked (`K.icon('cross')`), rerouted to a tile "billed separately · pay as you go / API key"; caption "since April 2026"; shelf chip "work plans · Trust".
**Exit:** both buildings calm, same clerk in each.

## 16 — More rooms: design and voice
**Metaphor object:** two new rooms attached to the floor plan: a design studio and a phone booth.
**Frame:** `K.bg()`. Left half: design room card (x 120–900, y 200–800); right half: voice booth card (x 1020–1800, y 200–800).
**Beats:**
- `design`: in the design room a prompt card "a poster for a tea house" becomes a layout of `K.card` blocks and a code strip; badges "Launched Apr 2026" and "Beta · in chats · Sep 2026"; small tiles "Docs · Slides (Beta)".
- `voice`: the booth lights; a `K.icon('phone')` and a sound wave (sine line).
- `pipeline`: three boxes in a row: "speech → text" → "model" → "text → speech", arrows drawing in order; label "takes turns".
- `native`: below it, one box "speech ↔ speech" with a wave in and out simultaneously; label "interrupt mid-sentence"; chips "GPT-Live", "Gemini Live".
- `claude-voice`: a Claude chip sits beside the pipeline row with a "?" (`K.icon('question')`) and caption "takes turns · build not disclosed"; small pill "bigger models + connected apps (Jul 2026)"; two shelf chips "builders · Shipping", "voice · The Network".
**Exit:** both rooms lit, waves idling.

## 17 — Desks that never close: personal agents
**Metaphor object:** a desk in its own office, lit at night, that you text from your phone.
**Frame:** `K.bg({glow:.4})`. Night: a small office card at centre (x 640–1280, y 240–640) with a desk and its own lantern, window lit; a phone `K.iconTile('phone')` at bottom-left sending chat bubbles (`K.icon('chat')`) to it.
**Beats:**
- `always-on`: the office's window glows and stays lit while a clock icon spins; labels around it: "always on", "own computer", "message from chat apps", "long memory", "broad permissions".
- `self-hosted`: the office slides left into a house outline ("your machine"); tiles "OpenClaw (was Clawdbot) · Jan 2026" and "Hermes Agent · Nous Research · Feb 2026" (a tiny `SKILL.md` file pops out of the Hermes tile: "makes its own skills"); caption "your keys, your risk".
- `security`: warning icons drop on the house: "hundreds of malicious skills", "100,000+ exposed installs" (eyebrow "Feb 2026").
- `hosted`: a second office appears at right inside a tall company building ("their computer"); tiles "Muse · Meta · Sep (US)", "dots · OpenAI · rolling out", "Gemini Spark · Pro and Ultra"; caption "their approval rules".
- `anthropic`: between them, three small chips: "cloud sessions", "routines", "Dispatch (preview)"; shelf chip "own lesson · Trust".
- `handover`: everything dims to 50%; a lower-third preview card slides in at bottom-left "guest · June" and the palette accent begins to brighten.
**Exit:** two offices dim, guest card in place.

## 18 — Myth or still true? Part one [guest]
**Metaphor object:** the desk becomes a quiz table: each myth is a card placed on the desk and flipped to its true side.
**Frame:** `K.bg({glow:.75})` with the brighter guest accent. Lower-third "guest · June" (x 80, y 846; the only element below 830, decorative label, captions-safe at the left edge). Hall desk at y 640, a counter "myth 1/10" mono 30 at top-right (x 1700, y 170).
**Beats:**
- `myth-1`: card "temperature 0 = same answer" lands; stamp "wrong" (`K.icon('cross')`); flips to "error on newest Claude · 0 never guaranteed"; the taped dial from 08 reappears small beside it.
- `myth-2`: card "it remembers me" flips to three icons: profile card, filing cabinet, folder (from 09).
- `myth-3`: card "bigger window = remembers all" flips to the pile from 05 and a terminal chip "auto-compact".
- `myth-4`: card "all AI art is diffusion" flips to "mostly, not all": static well + tile-by-tile canvas from 07, small.
- `myth-5`: card "Claude can draw that" flips to a code card and a phone line to the studio; a paintbrush icon (`K.icon('sparkle')` in the studio) labelled "someone else's brush".
**Exit:** five flipped cards in a fan at the top of the desk, counter "5/10".

## 19 — Myth or still true? Part two [guest]
**Metaphor object:** the same quiz table, cards 6–10.
**Frame:** as 18; the fan of five cards shrinks to the left edge (scale 0.5); counter continues.
**Beats:**
- `myth-6`: card "cached tokens are free" flips to the four meters from 12 (write meter highlighted) and the cold timer ring from 11 with a tea cup.
- `myth-7`: card "Pro = not trained on" flips to the home/company split from 15, with the two toggles.
- `myth-8`: card "my subscription runs any agent" flips to the blocked plug → "billed separately".
- `myth-9`: card "CLAUDE.md is a rule" flips to the pinned note and the padlock from 10: "note ≠ lock".
- `myth-10`: card "Sora is where AI video lives" flips to the "closed · spring 2026" Sora tile and the studio door still open.
- `back`: ("Back to you.") the ten cards gather into one neat stack on the desk; the guest lower-third slides out; palette accent eases back to normal.
**Exit:** one stack on the desk, calm palette, counter "10/10" fading.

## 20 — Keep this
**Metaphor object:** the whole desk, pulled back: lantern, desk, studio, rooms, meters; then the end card.
**Frame:** first part `K.bg()` with the full drawing seen from far away (camera z 0.6): the desk under the lantern in the centre, studio door, rooms and buildings around it, four meters faint. Second part (from `keep-1`): end card (noBadge in lesson.js), `K.plate('plate', t, {shade:0.6, mask:[680, 860]})` if present, else `K.bg()`; `K.petals(t, {n:4, avoid:[[120,130,1800,860]]})`.
**Beats:**
- `fewer-modes`: three arrows lead out from the drawing to the right edge, each with a dated label; first: "fewer modes, one agent (Sep 2026)" while the merged room glows.
- `own-computers`: second arrow: "agents on their own computers" while the lit cloud office glows.
- `curate`: third arrow: "curate the desk" (eyebrow "what the companies did in 2026") while the summary page on the desk glows; a fourth, dashed arrow ends in a `K.icon('question')`: "beyond that: nobody knows yet".
- `ignore`: three grey pills float up and fade: "version numbers", "leaderboards", "the maths inside".
- `keep-1`: the drawing shrinks to a small emblem at top-centre (desk + lantern, y 200); `K.title('Keep this', 960, 300, {size:64, align:'center'})` (the narrator's "Three things to keep" lands here); takeaway 1 card (x 200–1720, y 360–500): bold lead "The model only knows what's on its desk right now." + "Memory and instruction files are text put back on the desk, and a fuller desk is a worse desk." in Georgia 30 (same text as lesson.js keep).
- `keep-2`: takeaway 2 card (y 520–660): "Most multimodal is a hand-off." + rest.
- `keep-3`: takeaway 3 card (y 680–820): "Same model, many rooms, four meters." + rest.
**Exit:** end card complete and still; the lantern emblem glows gently; petals drift away from the text.
