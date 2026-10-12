# 00.06 — Trust what you can verify · storyboard (final: B spine, grafts from A and C)

**The one metaphor: the house, the crew and the owner.** AI is a tireless building crew; you are the owner who
signs off. One house is built in scene 01 and never leaves the screen; it is transformed, cut away, put on a
street, supplied, moved into, measured, and finally pulled back to as one house among many.

**How the house is drawn (kit only, reused in every scene; build it once as a helper `house(x, y, s, o)` in the
lesson):** a large `K.icon('house', x, y, s)` outline (s 300–420) in `K.C.line2`, warm `K.glow` in its windows when
"lights on". Cutaway mode (05, 08, 12): the house outline stays, and 3–4 `K.card` rooms (r 12, fill `K.C.tile`) fade
in inside it, each with a small line icon (door = `lock`, window = `globe`, back door = `key`). **The crew** = 2–3
`K.icon('sparkle')` (the kit's AI-agent icon) with a tiny `K.wave` bob. **The owner** = `K.icon('person')` in
`K.C.head` gold. **Inspector** = `K.icon('person')` + `shield`. **Burglar** = `K.icon('person')` in `K.C.quiet`
with a `key`. **Suppliers** = `K.card` "vans" (pill-shaped cards) carrying `K.file` / `puzzle` icons. Colour code
across the lesson: what the machine can check is gold `K.C.head` / `check`; what it cannot see is terracotta
`K.C.accent` / `warning`. No status green or red (brand rule).

Safe area for all text: x 80–1840, y 130–930; badge top-left; nothing essential below y 930. Labels ≤ 8 words,
26 px minimum (30+ for anything read). One `'back'` overshoot per scene at most.

---

## 01 — The point
**Metaphor object:** the house is built for the first time: small, finished, lights on.
**Frame:** `K.plate('plate', t, {zoom: true, shade: 0.45})` if engine/assets/teahouse-night.jpg exists, else
`K.bg({glow: 0.5, glowX: 960, glowY: 640})` (design reads the same on both). `noBadge`. Eyebrow "00.06 · ORIENTATION"
at (960, 200). Title "Trust what you can verify" `K.title` 84 px at (960, 290). Purpose line `K.para` Georgia 34 px,
w 1300, centred at y 380. House (s 260) at (960, 690), two crew sparkles beside it at (1150, 640) and (1210, 700),
owner at (760, 740). Sparse `K.petals` with `avoid` rects over all text and the house.
**Beats:**
- `[[purpose]]` purpose line rises in under the title: "Judging what you can't see. Above all: is it safe?"
- `[[conclusion]]` a gold pill appears at (960, 470): "Trust only what can be checked".
- `[[hand-off]]` the pill splits into three small pills beneath it: "a machine · you · someone who knows"; the
  last one in terracotta.
- `[[leaks]]` ("Code that runs and leaks") the house's lights come on (window glow); a thin terracotta `K.path` trickles out of the back of the
  house to the right with a small label "runs… and leaks" (30 px, accent).
**Exit:** title, pills and lit house hold; the leak line rests; petals drift.

## 02 — Where it lives
**Metaphor object:** the house shrinks to a tiny house icon sitting on the Start gate of the map.
**Frame:** `K.bg()`. `K.map.draw(t, {focus: '00', pin: '00', pinDrop: K.io(t, pin, .7, 'back'), lanterns, lanternLabels})`
full canvas. The tiny house (`K.icon('house', …, 48)`) sits just under the Start gate.
**Beats:**
- `[[pin]]` pin drops on Start / 00 (the scene's one overshoot); Start ring glows (`pinGlowK`).
- `[[lanterns]]` the six lanterns light left to right (`lanterns: i => K.stagger(t, a, i, .1)`), label row fades
  in; caption pill at (960, 900): "AI lights every district".
- `[[walking]]` a dashed gold `K.path` "walk" leaves the Start gate along the street toward the districts; pill
  "The walking stays yours".
- `[[districts]]` ("There are four") a four-pill strip appears at y 880: "packages · review · security · going live"
  (the lesson's skimmable spine, from draft C); then `highlight: ['code', 'history', 'trust', 'shipping']` lights the
  four districts in sequence (one per spoken name, `S.find('Code')`, `S.find('History')`, `S.find('Trust')`,
  `S.find('Shipping')`), the matching pill brightening as each district lights.
**Exit:** map holds, Start pinned, four districts softly outlined, four-pill strip resting, lanterns swaying.

## 03 — They fix their own errors now
**Metaphor object:** the house under construction, three eras of building it.
**Frame:** `K.bg()`. A horizontal era strip at y 200: three `K.pill`s "2021 · autocomplete", "2022 · paste into
chat", "2025– · agents", at x 420 / 960 / 1500, joined by a hairline. Below, the build site: a half-built house
outline (s 340) at (1260, 620). Left, a `K.term` window (x 140, y 360, w 760, h 420, title "agent").
**Beats:**
- (no cue; scene opens on `S.find('Notepad')`) a `K.win(…, {kind: 'notepad', title: 'script.txt'})` card at
  (140, 360, 760, 420) with two lines of Python and a `K.file` "script.txt" (nameSize 26); on `S.find('agent')` a crew
  sparkle drifts over it and the file label flips to "script.py", then the window cross-fades into the agent terminal
  before `[[autocomplete]]`. The strip pills stay ghosted until their cues.
- `[[autocomplete]]` first pill lights; a single `person` (owner, gold) lays one brick (a small `K.card`) on the
  house while a faint ghost line suggests the next one: you did every brick, AI guessed the next.
- `[[paste]]` second pill lights; a `chat` icon appears between the owner and the house with two short arrows
  ("error →", "← fix").
- `[[agents]]` third pill lights; owner steps back to (1700, 760); three crew sparkles take over the wall. The
  terminal types the loop: `> python -m pytest` → `2 failed, 3 passed` (accent) → `fixing…` → `> python -m pytest` → `5 passed` (gold).
- `[[aaron]]` a small card under the strip at (1260, 290): "Aaron: no hand-debugging since Claude Code" (30 px).
- `[[share]]` the card swaps for a dated card: "Google, Apr 2026: ~75% of new code by AI" / "Anthropic: most of its
  own" (eyebrow "AS OF OCT 2026").
- `[[machine-check]]` the "5 passed" line gets a gold `K.ring`; a `check` icon pops on the wall that just
  stood: label "A crash is machine-checkable".
- `[[agentic]]` the owner gets a pill above him: "agentic engineering: direct, oversee" with tiny "Karpathy, Feb 2026".
**Exit:** wall complete, crew bobbing, terminal resting on "5 passed", owner watching.

## 04 — The builder and the owner
**Metaphor object:** the finished house; the owner's walkthrough. This is the mental model scene.
**Frame:** `K.bg({glow: .35, glowX: 960, glowY: 600})`. House large (s 420) centred at (960, 600). Crew sparkles at
left (420, 560–700); owner at right (1500, 700). Eyebrow "THE MENTAL MODEL" at (960, 170).
**Beats:**
- `[[crew]]` crew sparkles pop in with label "the crew: AI" (gold, 32 px) at (420, 470).
- `[[owner]]` owner appears with label "the owner: you, who signs off" at (1500, 610).
- `[[rebuild]]` one wall of the house wobbles and falls (a card rotates down, `K.at` rot), a crew sparkle sweeps
  over it and it rises back into place; small `check` pops.
- `[[walkthrough]]` gentle `K.cam` push (z 1 → 1.15) into the house; owner moves inside along a dotted path; three
  window glows switch on in time with "lights" and "taps" (`S.find`); a gold pill "It works" at (960, 330).
- `[[cant-see]]` the camera holds; the pill "It works" dims to `K.C.soft`; a new terracotta pill replaces it: "What
  can't I see from in here?" (36 px). A faint dashed outline hints at rooms behind the walls (no detail yet).
**Exit:** house lit, owner inside, the question pill resting.

## 05 — It works, and it's unsafe
**Metaphor object:** the house in cutaway: what the owner can't see from inside.
**Frame:** `K.bg()`. House (s 420) at (700, 600), now cut away into 4 room cards. Right column x 1240–1800 for the
data card and labels.
**Beats:**
- `[[loud]]` left of the house, a small "2021" ghost house collapses (outline falls apart) with a `cross` icon
  and pill "loud: it crashed".
- `[[quiet]]` ghost fades; in the real house a burglar figure (quiet colour) slips in through the back-door room,
  whose `lock` icon is drawn open; pill "quiet: it works, and leaks".
- `[[valid]]` data card on the right: "Veracode, Jul 2026" eyebrow; first row "valid code: ~100%" with a full gold bar.
- `[[half]]` second row "passes security: 56%" with a half terracotta bar; small grey note "2025: 55%". Three
  labels fade in under the cutaway rooms: "injection", "cross-site scripting", "missing access checks" (26 px, on-screen only).
- `[[stanford]]` row 3: "Stanford, 2022: less secure, more confident" (eyebrow "EARLY TOOLS").
- `[[someone-else]]` the owner's view (a soft gold cone from the owner inside the front room) lights only the front
  rooms; the back door sits outside it in terracotta. Label: "Security = what someone else can do". On
  `S.find('attacker')` a second label under it: "you test as you · they test as everyone".
**Exit:** cutaway house, owner's cone, the unlocked back door glowing faintly terracotta.

## 06 — What that looks like
**Metaphor object:** the house on a real street: one whose public key (normal) opened every room because a database setting was off, then a whole street of open doors.
**Frame:** `K.bg()`. Left half: one house (s 300) at (520, 560). Right half: a street of 9 small houses (s 120) in a
3×3 grid around (1400, 560).
**Beats:**
- `[[moltbook]]` left house appears with dated card above "Moltbook, Jan 2026 · fully AI-built"; a `key` icon is
  pinned to its front door.
- (no cue; on `S.find('public key')`) a `K.win(…, {kind: 'browser', url: 'app.example'})` slides out of the door
  showing `anon key: eyJ…` in page source (truncated, generic; neutral/gold, small tag "normal: meant to be public").
- `[[rls]]` a separate small card labelled "database settings" appears beside the house (not in the browser) with
  the mono line `row-level security: off` (accent); the door key glows and every room behind it lights up.
- `[[fixed]]` a gold `check` and small pill "fixed within hours of the report".
- `[[redaccess]]` the street of 9 houses fades in; card "RedAccess, May 2026: ~5,000 of ~380,000 exposing data".
- `[[public]]` a toggle pill "Public / Private" appears; it sits on "Public"; doors on 3 of the 9 houses swing open
  (terracotta).
- `[[words]]` four pills line up at y 860: "row-level security", "public", "anon key", "exposed" (the surprise literals).
**Exit:** street holds, four pills resting.

## 07 — "Make sure it's secure"
**Metaphor object:** the owner asks the foreman (crew) "is it safe?"; the wall with two doors.
**Frame:** `K.bg()`. House (s 300) at (420, 600) with crew sparkle beside it; owner at (900, 660). A chat area
in the middle top (x 640–1280, y 200–420).
**Beats:**
- `[[ask]]` owner chat bubble (card) "Make sure it's secure."
- `[[yes]]` crew reply bubble "Yes, it's secure." with a gold `check`.
- `[[two-yeses]]` the reply duplicates into two identical cards side by side, labelled underneath "true?" and
  "false?" in the same colour: they look the same.
- `[[replit]]` small dated card at (1500, 250): "Replit agent, Jul 2025: deleted prod DB, said no rollback" and,
  appearing on "study" (`S.find('study')`), "Preprint, Jun 2026: tests pass, thing hollow".
- `[[wall]]` a tall wall (`K.card` 40×600, `K.C.line2`) rises at x 1180 between the owner and the right side; label "the wall".
- `[[learn]]` door 1 opens in the wall (gap + `book` icon): "learn to check it".
- `[[expert]]` door 2 opens (gap + inspector `person` + `shield`): "bring in an expert". On `S.find('companies')` a
  small pill under the wall: "vendors: doesn't replace human review".
**Exit:** owner facing the wall with two open doors; the "yes" bubbles fade to `K.C.soft`.

## 08 — Where the picture breaks
**Metaphor object:** the cutaway house again, with the analogy visibly cracking.
**Frame:** `K.bg()`. House cutaway (s 380) at (960, 560). Eyebrow "WHERE THE PICTURE BREAKS" at (960, 170).
**Beats:**
- `[[rooms]]` inspector walks a dotted path through all 4 rooms; each gets a `check`.
- `[[not-proven]]` the house explodes into a thicket: a dense web of thin `K.path` lines (seeded `K.rng`) spreads
  past the walls, far more paths than rooms; pill "inspected ≠ proven safe".
- `[[own-report]]` a clipboard card "inspection report" appears with a crew sparkle as its signature; then the
  inspector's own badge turns into a sparkle (AI inspector = crew). Label "AI inspector = another crew member".
- `[[every-door]]` the camera pulls back (z 1 → 0.7) to show a row of houses; many small burglar figures try every
  door at once (staggered), a `sparkle` on some of them: "every door, automatically, with AI".
**Exit:** pulled-back row of houses, burglar figures settling to a slow idle.

## 09 — Working with other people
**Metaphor object:** the house sits on a street with a style code; the crew brings non-matching bricks.
**Frame:** `K.bg()`. A street of 5 houses along y 620 (s 220), all with the same roof and window shape; our house is
the middle one. Hand-coders (2 `person` icons, soft colour) by the neighbouring houses.
**Beats:**
- `[[street]]` the street draws in left to right; eyebrow "THE TEAM'S STREET".
- `[[norms]]` three small pills over the street: "naming", "file layout", "error handling".
- `[[hand-coders]]` the two hand-coders gain labels "write by hand"; our house's new wing appears in a different
  shape and colour (accent outline): it drifts from the style.
- `[[gitclear]]` a duplicate of the street's shared `gear` helper appears inside our house instead of using the one
  on the street; dated card "GitClear, 2026: more copies, less reuse".
- `[[other-libs]]` a row of approved module chips ("requests", "pandas") under the street; the crew adds two different
  chips in accent; a hand-coder holds one with a `question` icon: "parts they never chose".
- `[[disclose]]` a small sign card "AI used? A human read it?" on the street; tiny dated pill "curl, Jan 2026: bug bounty ended".
**Exit:** the street with one off-style wing, sign holding.

## 10 — Writing the house rules down
**Metaphor object:** the building code posted on the site wall.
**Frame:** `K.bg()`. House (s 300) at (1400, 620) with crew. Left: `K.win(140, 220, 820, 560, {kind: 'explorer', title: 'my-project'})`.
**Beats:**
- `[[claude-md]]` `K.file` "CLAUDE.md" appears in the explorer.
- `[[agents-md]]` `K.file` "AGENTS.md" beside it; tiny caption "open · Linux Foundation, Dec 2025".
- `[[rule]]` the file opens into a `K.editor` card with a typed line: `- Use only libraries already in this project.`;
  a copy of the card pins itself to the house's site wall like a posted notice.
- `[[not-a-lock]]` a `lock` icon appears next to the notice and is struck through (accent `K.line`); pill "a note, not a lock".
  The editor scrolls through many lines (long file) and one crew sparkle skims past the rule.
- `[[ignored]]` a gold owner/person stands beside the notice with an eye on the crew: "someone who knows the norms".
**Exit:** notice on the wall, person beside it, editor resting.

## 11 — Who owns the supplier list
**Metaphor object:** suppliers' vans arriving at the site; each gets a key.
**Frame:** `K.bg()`. House (s 300) at (520, 600). A road running right from the house to x 1800 at y 720 with vans
(pill cards with `puzzle` icons) driving in.
**Beats:**
- `[[suppliers]]` two vans pull up; label "dependencies: other people's code".
- `[[decide]]` a clipboard card "approved suppliers" appears in the owner's hands (gold person at 300, 760).
- (no cue; on "adding more", `S.find('adding')`) three more vans queue up quickly behind; dated pill "GitClear CEO,
  Jul 2026 (paraphrase): a package for every want".
- `[[stranger]]` each parked van gets a small `key` floating to it from the house: "a stranger's code, with your keys".
- `[[vulnerable]]` one van gets a `warning` badge: "agents' picks: less secure on balance" (one study, 2026).
- `[[fake]]` a dashed-outline van arrives with no name on it; a burglar figure at the wheel: "a name that didn't exist".
- `[[worms]]` dated cards "Shai-Hulud, Sep 2025", "waves Nov 2025 → 2026" and "keyv worm, Aug 2026"; a small `file` appears inside the newest van's
  source crate (the supplier's own code, not the owner's house), wired to an editor icon: "runs when opened in an AI editor".
- `[[diff]]` vans fade; a `K.editor` card at (1100, 260, 680, 360) shows `package.json` with five gold `+` lines
  nobody asked for.
**Exit:** house, owner with the approved list, the diff card resting.

## 12 — "Is it ready to deploy?"
**Metaphor object:** move-in day; keys handed to real tenants.
**Frame:** `K.bg({glow: .3})`. House (s 360) at (700, 600); a line of 3 tenant `person` icons at right (1300–1600, 700).
Checklist card at (1180, 200, 620, 380).
**Beats:**
- `[[move-in]]` a ribbon pill "move-in day" over the house; a `key` hovers between house and tenants.
- `[[same-trap]]` owner asks "Ready to deploy?" (shown from `S.find('ready')`), crew answers "Yes" (re-used bubble from 07, smaller); pill "same trap".
  Checklist card appears with gold ticked rows: "builds", "tests pass".
- `[[who-sees]]` unticked accent row "who can see what".
- `[[cost]]` unticked row "cost under real load".
- `[[rollback]]` unticked row "how to roll back".
- `[[sign]]` a signature line at the bottom of the checklist; a person with `code` icon signs it; the key moves to
  the tenants only after the signature.
- (no cue; `S.find('scanners')`) a small pill under the checklist: "pre-launch scanners: helpful, not enough".
**Exit:** tenants holding the key; signed checklist.

## 13 — What AI can verify, today
**Metaphor object:** the crew's tool belt: what tools can measure, and what no tool reads.
**Frame:** `K.bg()`. Split screen: left column "MEASURED" (x 120–900), right column "NOT MEASURED" (x 1020–1800),
both eyebrows at y 180. The house (s 200) sits centred at (960, 800).
**Beats:**
- `[[pass-fail]]` the divider draws; left eyebrow "PASS OR FAIL" gold.
- `[[builds]]` left list stacks with `check` icons: "builds", "given tests pass", "linter + types clean".
- `[[scanner]]` "known pattern flagged", "page loads".
- `[[weak]]` right list in accent with `question` icons: "right tests?", "what you meant?", "who sees what?",
  "threats newer than the model".
- `[[checkers]]` the lists dim; a dated card fills the centre: "/security-review · Aug 2025", "security-guidance plugin ·
  May 2026", "Claude Security · Beta (Apr 2026)", "Codex Security · Preview (Mar 2026)", "CodeMender · Preview (Jul 2026)", "Copilot agentic autofix · Preview (Jul 2026)",
  each with its badge pill (rows 34 px, badge pills 26 px; card x 300–1620, y 200–760); on `S.find('review agents')`
  a last row "review agents · every change".
- `[[human-yes]]` a gold `person` icon appears at the end of every row; footer pill "As of Oct 2026: a human still reviews".
**Exit:** card with badges and the human at every row's end.

## 14 — The old rule, adapted
**Metaphor object:** the rule as a plaque fixed to the house.
**Frame:** `K.bg({glow: .4, glowX: 960, glowY: 420})`. House (s 300) at (960, 680). Plaque card above it at (560, 200, 800, 180).
**Beats:**
- `[[the-rule]]` plaque reveals: "Trust only what can be verified" (gold, 44 px).
- `[[younger]]` small card at right: "Irving Younger, 1975 · trial lawyers' rule" with "Don't ask what you don't know".
- `[[adapted]]` below the plaque, a second line types: "Don't rely on an answer you can't check."
- `[[agent-side]]` the house splits left/right: left half gold with chips "crashes", "builds", "tests" and a crew sparkle:
  "the agent verifies".
- `[[your-side]]` right half accent with chips "security", "team fit", "dependencies", "deploys" and owner + inspector:
  "you, or an expert".
**Exit:** the whole lesson in one picture: plaque above, house split in two halves.

## 15 — Where it's heading
**Metaphor object:** the line between the halves moves outward; the burglars' tool belt grows too.
**Frame:** `K.bg()`. The split house from 14, smaller (s 260) at (960, 560). The gold/accent boundary is a vertical
dashed line through it.
**Beats:**
- `[[outward]]` the dashed boundary slides right in three small steps (eased), the gold side growing; a small date
  scale under it "2025 · 2026 · next".
- `[[verifier]]` a second sparkle with a `shield` appears beside the crew, labelled "verifier ≠ builder"; caption
  "confirms the bug before reporting".
- `[[first-time]]` a pill "first-draft security: ~flat" in accent stays put while the line moves: the gap is honest.
- `[[attackers]]` the burglar figure on the right gains a sparkle: "attackers get the same tools".
- `[[forecast]]` pill "Anthropic engineers: better than us within a year" with a `FORECAST` badge (eyebrow style).
- `[[unknown]]` a `question` icon over the owner; pill "human yes: still required today".
**Exit:** boundary resting further right than it started, owner still at the door.

## 16 — Keep this
**Metaphor object:** pull back to the whole street at night; the house lit among the others.
**Frame:** `K.plate('plate', t, {shade: 0.5, mask: [680, 860]})` lower band if the plate exists, else `K.bg({glow: .4})`.
`noBadge` ('16' is in lesson.js `noBadge`). Street of houses small along y 860 band (stays above 930). End card `K.card` (360, 180, 1200, 600).
Sparse `K.petals` with `avoid` over the card.
**Beats:**
- `[[ignore]]` small eyebrow at top of card "SAFE TO IGNORE FOR NOW": "which scanner · jargon · percentages" (30 px soft), then it fades
  as "Keep this" is spoken (`S.find('Keep')`), replaced by the eyebrow "KEEP THIS".
- `[[k1]]` takeaway 1: bold lead "The agent fixes the crashes; you own what it can't see." + Georgia line.
- `[[k2]]` takeaway 2: "\"Yes, it's secure\" is just another answer." + line.
- `[[k3]]` takeaway 3: "Someone has to own the rules and the supplier list." + line.
**Exit:** all three takeaways resting on the card, the street lit below, petals drifting slowly.
