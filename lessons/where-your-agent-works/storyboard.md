# Storyboard — 01.02 Where your agent works

**The one metaphor: one worker, your house of rooms, and the vendor's building across town.** The model is a single worker (`K.iconTile('sparkle', ..., 96)`, gold stroke) who can stand in any room. What changes from room to room is which of YOUR shelves it can reach. The street is built in 03 and then transforms; it is never redrawn from scratch. It breaks in three places, and the scenes show each break: a second worker (04), a room that moves (06), copies that stay behind (13).

Canvas 1920x1080. Text inside x 80-1840, y 130-930; labels 26 px or more, read text 30+ px. One `'back'` overshoot per scene at most. Beats hang on `S.cue('name')`, finer sync on `S.find('word')`. Capture positions come from `K.captureBox` / `K.captureAt` / `K.termTimes`, never typed-in numbers.

Persistent parts:

- **Your house** (your computer): `K.card(110, 250, 940, 600, { r: 24 })`, roof `K.path([[110,250],[580,150],[1050,250]], { head: false, color: K.C.line2 })`, eyebrow "YOUR COMPUTER" at (580, 205). **Shelves** along the top inside wall: four `K.folder(..., 70, { name, nameSize: 26 })` at y 300: `Documents`, `Projects`, `Photos`, `Finances` (terracotta stroke: never connected).
- **Three rooms** separated by `K.line` walls at x 420 and x 730, floor y 840: **front counter** (Chat, `K.icon('chat')`, a dashed glass partition between it and the shelves), **back office** (Cowork, `K.icon('clock')`, an in-tray of `K.file`s), **workshop** (Code, a bench with `K.icon('terminal')` and `K.icon('code')`, a dotted reach arrow up to the shelves). Door pills at y 800: `Chat`, `Cowork`, `Code`.
- **The road**: `K.line(1050, 860, 1840, 860, { dash: [14, 12], color: K.C.line2 })`, eyebrow "across town".
- **The vendor's building** (from 06): `K.card(1360, 230, 460, 620)`, `K.icon('cloud')` and `K.icon('server')` on the roof, eyebrow "ANTHROPIC'S SERVERS". It gains the back office (06), a spare workshop (11) and a logbook (13).
- **The hatch**: a small square `K.card(1032, 420, 36, 80, { r: 4 })` in the house's right wall (the brand's one square element), a gold `K.path` to the vendor building; it glows only while "desktop app open" is true.
- **Copies** are dashed outlines of the original icons; anything that crosses the road is a dashed copy, never the original.
- **Dated cards**: `K.card` r 24, eyebrow = publisher · date, body = the verbatim words (`K.para`, Georgia 30-34), footer pill in mono 26 `as of 2026-10-14 · moves monthly` (or the page's own date).

---

## 01 — The point
**Metaphor object:** the street at dusk, small: your house left, the road, an empty lot where the vendor's building will stand.
**Frame:** `K.plate('plate', t, { zoom: true, shade: .5 })`, `noBadge`. Eyebrow "LANTERN LESSON" at (140, 200); `K.title('Where your agent works', 140, 290, { size: 92 })` from frame 0; purpose line `K.para` Georgia 34, `K.C.strong`, w 1200, y 350, visible from frame 0. Title-card credit at y 880, Karla 26, `K.C.soft`: "Built on Ethan Mollick, An opinionated guide to which AI to use (Summer 2026) · MIT Missing Semester 2026". `K.petals` n 6, avoiding the text.
**Capture:** none.
**Beats:**
- [[purpose]] title and purpose line resting (the purpose line rises 12 px over 0.5 s).
- [[conclusion]] conclusion writes in (Georgia italic 32, `K.C.body`, w 1200, y 500-600); at right a small emblem: the sparkle worker between three tiny door pills `Chat · Cowork · Code`.
- [[gap]] dated card at (140, 660, 760, 130): eyebrow `AARON ORELUP · AO-034 · 2026-10-04`, body "chat, Cowork and Code across browser, desktop, CLI and cloud".
- [[overnight]] a notice card drops onto the emblem (the scene's `'back'`): eyebrow `ANTHROPIC HELP CENTER · 2026-10-06`, body "new Cowork tasks run in the cloud · you can't switch back", pill `Pro and Max`.
- [[same-app]] the emblem's Cowork pill slides right along a hairline to a small cloud icon; the app icon stays where it was. Label: "same app · different computer".
**Exit:** title, purpose, conclusion, cards and credit at rest; plate drift and petals only.

## 02 — Where this sits on the map [map]
standard map scene (K.map.intro)

## 03 — One worker, many rooms
**Metaphor object:** the house is built; the worker arrives.
**Frame:** `K.bg({ glow: .35, glowX: 580, glowY: 500 })`. The house full size left (x 110-1050); right half (x 1120-1820) holds the real screenshot.
**Capture:** `desktop-docs` (browser, public page, fresh profile, no login). Recipe `lessons/where-your-agent-works/steps/desktop-docs.json`: `goto https://code.claude.com/docs/en/desktop-quickstart`; `size [1024, 576]`, `dpr 1.875`; `wait_for` text "three tabs"; `mark tabs` with `boxes: { list: <the Chat / Cowork / Code list> }`; `shot tabs`; scroll to the environment section; `wait_for` text "SSH"; `mark envs` with `boxes: { list: <the Local / Cloud / SSH / WSL list> }`; `shot envs`. Decline non-essential cookies only if a decline button exists; never accept terms. Marks used: `tabs` (here), `envs` (07). Here: `K.shot('desktop-docs/tabs', t - S.cue('chat-room'), [1120, 220, 700], { zooms: [{ at: 0.4, box: K.captureBox('desktop-docs', 'tabs', 'list') }] })`, card under it "Anthropic docs · desktop quickstart · read 2026-10-14".
**Beats:**
- [[worker]] the sparkle worker walks in along the road from the empty vendor lot at right (1590, 860) to the front step (580, 880), gentle bob; small label "thinks in the vendor's building".
- [[house]] the house draws (outline, roof, walls); the shelves fill left to right.
- [[chat-room]] counter lights; worker steps behind it; the glass partition draws; label "no file access". Screenshot fades in at right, callout on "Chat".
- [[cowork-room]] back office lights; worker at the desk; a `K.file` drops into the in-tray and a small person icon walks out of frame. Callout on "Cowork": "autonomous background agent".
- [[code-room]] workshop lights; worker at the bench; dotted reach arrow to `Projects`. Callout on "Code": "direct access to your local files".
- [[before]] back office and workshop dim to 0.25; only the counter stays lit; small card at (300, 180): "before agents · the only question: your chat log · (training setting: 2025-08-28, covers Claude Code too)".
**Exit:** all three rooms at 0.8, worker at the counter, screenshot faded out.

## 04 — Pick the room by the output
**Metaphor object:** the house; three output objects arrive at the three doors; the worker splits in two.
**Frame:** `K.bg()`. House scaled 0.85, left (x 90-890). Card column x 980-1820.
**Capture:** none (S008's deck is footered confidential: its words on a card only).
**Beats:**
- [[output]] above each door an output object: speech bubble with a question mark (counter), `K.file` document (back office), running app `K.icon('program')` (workshop). Heading "pick by what you want back". Two grey logo-neutral pills `ChatGPT` / `Claude` fade to 0.3.
- [[openai]] card: eyebrow `OPENAI ACADEMY · CODEX BOOTCAMP 101 · 2026-09-23 · SLIDE 8`; rows "Use Chat when the answer is still taking shape" / "Use Work when the desired output is knowledge artifacts" / "Use Codex when the output is working software or applications"; footer "Codex now lives in the new ChatGPT desktop app"; arrows from each row to its door.
- [[not-same]] eyebrow "where the picture breaks" (terracotta); the counter's worker greys to 0.4, a brighter second worker with a `new model` pill lands over the back office and workshop only. Card `OPENAI CHANGELOG · 2026-09-22`: "available in Work and Codex, but not Chat"; footer "again 2026-09-29 and 2026-10-08". On `S.find('reach')` the reach arrows glow.
- [[stakes]] card `ETHAN MOLLICK · ONE USEFUL THING · 2026-07-23`: `low stakes → "all at least fine"`, `high stakes → most advanced model, at least High thinking`. Beside it a smaller unnarrated card: his picks by kind of work (research, images, video, voice, office documents; no model names; office row "okay"), footer "reissued every few months".
- [[meter]] a meter dial by the workshop door with pills `plan limits` and `API key · every token`; needle swings once. Card `ANTHROPIC HELP CENTER · read 2026-10-14`: "a set ANTHROPIC_API_KEY, once approved, is used instead of your subscription". Pointer chip "→ the lesson on your meter".
**Exit:** cards fade; house rests with output objects and both workers.

## 05 — The door labels are fading
**Metaphor object:** the three door pills fuse into one front door; three rooms stay behind it.
**Frame:** `K.bg()`. House centred (x 490-1430), camera eased onto the front wall.
**Capture:** none (the merged app needs a signed-in account; a drawn message box stands in).
**Beats:**
- [[merge]] date pill `2026-09-16`, card `ANTHROPIC · CLAUDE BLOG`: "Claude Cowork and chat are merging into one Claude"; footer `rolling out · Pro and Max first`. The door pills slide together and fuse into one wide `Claude` pill (the scene's `'back'`).
- [[one-door]] a drawn message box (blinking caret, placeholder "Ask or give a task") at the door; a request chip enters and branches along two `K.path` arrows: `quick answer` (counter) / `task` (back office).
- [[asks]] at the back-office door a pill "Allow this action?" with `K.icon('question')`; label "merged Claude · asks by default".
- [[still-rooms]] camera pulls back; the internal walls draw again through a translucent front wall: three rooms. Side card: "Unified Claude (beta) · Team and Free 'soon', no date · tabs may be gone by the time you watch".
**Exit:** one door, three rooms visible behind it.

## 06 — The back office moved across town
**Metaphor object:** the back office lifts out of your house and moves across the road into the vendor's building; the hatch opens.
**Frame:** `K.bg()`. Wide street: house x 110-1050, road, vendor lot x 1360-1820. The capture panel sits top right during [[move]]-[[removed]], then shrinks away.
**Capture:** `oct6` (browser, public help page). Recipe `steps/oct6.json`: `goto https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile`; `size [1024, 576]`, `dpr 1.875`; decline non-essential cookies only if a decline button exists (never accept, no login); `wait_for` text "On October 6, 2026"; scroll it into view; `mark change` with `boxes: { line1: <the "On October 6, 2026, new Cowork tasks on Pro and Max plans run in the cloud" sentence>, line2: <the "Only on your computer ... was removed" line> }`; `shot change`. Scene: `K.shot('oct6/change', t - S.cue('move'), [1040, 160, 800], { zooms: [{ at: 0.5, box: K.captureBox('oct6', 'change', 'line1') }, { at: S.cue('removed') - S.cue('move'), box: K.captureBox('oct6', 'change', 'line2') }] })`. Fallback if the page blocks the headless browser: a drawn quote card with the same two lines, eyebrow `ANTHROPIC HELP CENTER · 2026-10-06`.
**Beats:**
- [[move]] the vendor building draws on the right lot; the back office lifts out of the house as one block, travels along the road (`K.path`, 1.2 s, `K.io`) and settles inside it. Pill `new Cowork tasks · Pro and Max · since 2026-10-06`; card "isolated, temporary environment on Anthropic's servers". Screenshot zooms on line1.
- [[removed]] screenshot pans to line2; a toggle "Only on your computer" with `K.icon('cross')`. In your house the workshop bench glows: "runs on your machine → Claude Code"; a dashed line from the bench to the vendor lot: "what it reads still goes to the model". A small second house at bottom left, eyebrow `TEAM · ENTERPRISE`, keeps its back office: "local Cowork remains · cloud is a beta setting". Card footnote: "tasks started before 6 Oct stay local".
- [[hatch]] screenshot fades. The hatch opens; a gold path runs from the vendor's back office to it and on to `Projects` only. A laptop chip "desktop app open" beside it; at +3 s it dims and the path greys, then both return.
- [[openai-work]] compact card bottom right, eyebrow `OPENAI · GET STARTED WITH CHATGPT WORK · read 2026-10-14`: two columns `local: "can also use local files, apps, and the browser"` / `cloud: "cannot access that computer's files or tools"`; footer "can't switch from local to cloud during a turn".
- [[stale]] a yellowed note pins to the empty slot where the back office was: eyebrow `ANTHROPIC ENGINEERING · 2026-05-25 · COWORK'S FIRST VERSION`, quote "nothing else on the host is visible", stamp pill `stale for Pro and Max` (terracotta outline). A timeline strip at y 180: `May · local VM` · `16 Sep · merge` · `22 Sep · models split` · `6 Oct · cloud only (Pro, Max)`.
- [[moves]] eyebrow "where the picture breaks"; the empty slot pulses once; label "rooms move without you".
**Exit:** wide street: counter and workshop at home, back office across town, hatch path faintly gold.

## 07 — One coding agent, many doors
**Metaphor object:** the workshop gets more doors, a guest room (WSL) and a line to another machine (SSH).
**Frame:** `K.bg()`. Camera eases onto the workshop (z 1.5 around x 880, y 600); real `envs` shot at right.
**Capture:** `desktop-docs` shot `envs` (recorded with the 03 recipe): `K.shot('desktop-docs/envs', t - S.cue('picker'), [1100, 200, 720], { zooms: [{ at: 0.3, box: K.captureBox('desktop-docs', 'envs', 'list') }] })`. Card "Anthropic docs · desktop quickstart · read 2026-10-14".
**Beats:**
- [[workshop]] the workshop's door pill splits into a fan of five door chips around the bench; centre `K.icon('restart')` labelled "one loop".
- [[windows]] chips label themselves on their spoken words: `terminal` (terminal), `desktop app` (laptop), `code editor` (code), `browser` (globe), `Slack` (chat); all arrows lead to the one bench. Card "Anthropic · How Claude Code works · read 2026-10-14".
- [[envs]] the bench copies into three places on `S.find('Local')`, `S.find('Cloud')`, `S.find('Remote')`: in your house "Local · full access to your files, tools, and environment"; in the vendor building "Cloud · Anthropic-managed VMs, or self-hosted environments your organization operates"; in your house with a browser window pointing in "Remote Control · your machine, from a browser".
- [[picker]] envs screenshot zooms on Local / Cloud / SSH / WSL; a small guest room grows from the house's side wall: "WSL · Linux side, native paths".
- [[ssh]] a dashed `K.path` from the bench to a far tile `K.icon('server')` "your server · cloud VM · dev container"; chip "installs Claude Code there itself".
- [[expose]] a second axis as a vertical bar at the right edge, eyebrow `ETHAN MOLLICK · 2026-07-23`, label "what it shows you": top `the work itself` (`files changed`, `commands run`, `tests`) with pills `Codex` · `Claude Code`; bottom `the finished result` (one `K.file`) with `Work` · `Cowork`. Caption "where it runs ≠ what it shows you".
**Exit:** camera back to the wide street; the workshop with its fan of doors, guest room and SSH line.

## 08 — The speaking tube
**Metaphor object:** a speaking tube from the workshop bench to a terminal window; the shell at the far end.
**Frame:** `K.bg()`. House small at left (x 80-520, scale 0.45); tube `K.path` from its bench to two stacked terminals at x 600-1840.
**Capture:** `shells` (terminal), two recipes in a throw-away folder: `steps/shells-cmd.json` (shell `cmd`): `echo first && echo second` (prints `first`, `second`); `steps/shells-ps.json` (shell `powershell.exe`, Windows PowerShell 5.1, never `pwsh`, which accepts `&&`): `$PSVersionTable.PSVersion` (shows 5.1), then `echo first && echo second`, which prints `The token '&&' is not a valid statement separator in this version.` capture.py rewrites the user path to `C:\Users\you\...`. Scene: `K.demo('shells-cmd', t - S.cue('same-line'), [600, 180, 1240, 300], { title: 'Command Prompt', size: 30 })` and `K.demo('shells-ps', t - S.cue('fails') + K.termTimes('shells-ps').items[1].start, [600, 520, 1240, 300], { title: 'Windows PowerShell', size: 30, marks: [{ at: K.termTimes('shells-ps').items[1].out[0].at + .3, dur: 4, match: 'not a valid statement separator', text: 'PowerShell, not CMD' }] })`. Marks: each command's `done` and first output time from `K.termTimes`.
**Beats:**
- [[tube]] the tube draws from the bench; one terminal frame at its end, eyebrow "the terminal · just the window".
- [[shell]] inside it, `K.icon('program')` labelled "the shell · reads each line"; card `ANTHROPIC · CLAUDE CODE TERMINAL GUIDE · read 2026-10-14`: "two command-line programs: PowerShell and CMD".
- [[ps]] two prompt chips, mono 30: `PS C:\Users\you>` and `C:\Users\you>`; gold `K.ring` on `PS`; a quieter chip `zsh · macOS default`.
- [[same-line]] the frame splits into the two stacked terminals; the CMD capture types the line and prints both words; a small `check`.
- [[fails]] the PowerShell capture types the same line; the error prints and the mark boxes it. Card `ANTHROPIC · CLAUDE CODE QUICKSTART · read 2026-10-14`. Caption on `S.find('meaning')`: "same window · different shell · different meaning".
- [[as-you]] terminals shrink right; a key ring (`K.icon('key')` with a `person` badge) slides down the tube to the shell: "runs as you"; faint arrows fan from the shell to every shelf. Strip "'Any command you could run' · How Claude Code works". Pointer chip "→ the lesson on letting it loose".
**Exit:** tube, one terminal at rest with its real output, key ring by the shell.

## 09 — What you'll meet at the tube
**Metaphor object:** the same tube; three recognition notes pinned to it; a door that bypasses it.
**Frame:** `K.bg()`. Drawn terminal (`K.term`, not a capture) at x 600-1840, y 180-560; notes at y 600-900.
**Capture:** none (drawn lines; never a real user path).
**Beats:**
- [[not-recognized]] `K.term` types `claude` and prints `'claude' is not recognized as an internal or external command...`; note card "usually PATH · new terminal window after the fix · after an update: maybe a missing claude.exe". Chip with `K.icon('sparkle')`: "/doctor checks and fixes its own setup". Pointer chip "PATH itself → the lesson on keys". Card `ANTHROPIC · QUICKSTART, TERMINAL GUIDE, HOW CLAUDE CODE WORKS · read 2026-10-14`.
- [[their-shell]] two tube ends: the agent's `Git Bash` (with Git for Windows) or `PowerShell` (without); yours `PowerShell`. A command chip copied from the agent's end turns terracotta with `K.icon('warning')` on arrival.
- [[skip]] a desktop-app window draws a door straight into the workshop, bypassing the tube; inside it a small terminal pane still blinks: "still runs commands". Card "terminal guide: 'skip the terminal entirely'".
- [[deep]] dated book card with `K.icon('cap')`: "MIT Missing Semester 2026 · Jan 12 the shell · Jan 13 command-line environment".
**Exit:** terminal and the desktop door side by side.

## 10 — The house and the flat
**Metaphor object:** two rooms built for the work: a detached house and a flat in a shared block.
**Frame:** `K.bg({ glow: .3 })`. Centre stage x 260-1660, y 180-820. Blender clip if rendered, else the kit drawing.
**Capture:** optional Blender shot `house_and_flat` (`lessons/where-your-agent-works/blender/house_and_flat.py`, `tools/blender_shot.py`, GPU reserved via gpu-queue first; 6 s, 1280x720): left a detached house on its own slab; right a small block whose flats share one foundation and one service riser; slow push across both; the shared foundation glows once. `K.video('house_and_flat', t - S.cue('vm'), 260, 200, 1400, 788)`; canvas labels only, no 3D text. Fallback: two `K.card` buildings with foundation `K.line`s and `K.icon('house')`.
**Beats:**
- [[build-rooms]] your house shrinks to a top-left token; eyebrow "a computer inside your computer"; card `MIT MISSING SEMESTER · PACKAGING AND SHIPPING CODE · 2026-01-20`: "VMs abstract the entire computer".
- [[vm]] the detached house fills the left half; label "virtual machine · its own operating system"; its slab glows.
- [[container]] the flat block fills the right half; label "container · shares the host's kernel"; the shared foundation glows; a `Docker · a tool that makes containers` pill and a chip "on Aaron's list of gaps · AO-029 · 2026-10-01".
- [[weaker]] quote strip "'Docker's isolation is weaker than VMs' · MIT" with footnote "a concern on machines many people share".
- [[unattended]] the worker, tagged "skips approvals", walks into the flat block, not your house; card `MIT · AGENTIC CODING EXERCISES · 2026-01-21`: "not secure to use this mode directly" / "may be acceptable ... in a virtual machine or container". Pointer chip "→ the lesson on sandboxes".
**Exit:** both buildings at rest, worker inside the flat.

## 11 — The spare workshop works on a copy
**Metaphor object:** the vendor's spare workshop, working on a copy fetched from GitHub, not from your bench.
**Frame:** `K.bg()`. Wide street; a GitHub depot (`K.card` with a branch glyph from `K.path`) mid-road at x 1150-1290, y 620-780; a drawn terminal bottom left (x 110-760, y 600-860).
**Capture:** none (a real `claude --cloud` needs GitHub and an account and must not be recorded on native Windows). Drawn `K.term` with `claude --cloud`, never `--remote`.
**Beats:**
- [[cloud-session]] a spare workshop room appears in the vendor building; the worker moves in; label "isolated VM · Anthropic-managed". Your laptop closes its lid; a small gear in the spare workshop keeps turning. Card `ANTHROPIC · CLAUDE CODE IN THE CLOUD · read 2026-10-14`.
- [[copy]] `K.term` types `claude --cloud`; a bundle travels from the GitHub depot (not from your house) to the spare workshop; label "your pushed branch, not your local copy"; pill `push first`; a crossed-out dashed arrow from your bench.
- [[creds]] a key inside a locked box (`K.icon('lock')`) stays on the vendor building's outer wall: "credentials stay out of the VM · Anthropic-hosted".
- [[bundle]] the depot greys (no remote); a bundle leaves your house and crosses the road. On a "macOS · Linux · WSL" track a `.env` file drops out and stays on the front step with mono note `Left on this machine: .env`. Card footnote "also when the Claude GitHub App isn't installed on the repo". An untracked `.env` never leaves the house (`untracked: not included`); a committed key file rides in the bundle (`committed: goes up`).
- [[windows-caveat]] a second track "native Windows" replays the crossing: the `.env` (tracked, uncommitted) stays in the bundle and crosses with a terracotta outline. Line under both: "know what crosses".
**Exit:** spare workshop working; road quiet.

## 12 — Desktop no longer means "on your computer"
**Metaphor object:** traffic on the road: everything that crossed is a copy; the hatch narrows to one folder.
**Frame:** `K.bg()`. Street wide, camera slightly lower so the road is the centre.
**Capture:** none (dated quote cards).
**Beats:**
- [[processed]] heading over the road "where your files end up"; the house's desktop-app icon sends a document out through the hatch; it becomes a dashed copy and lands in the vendor's back office: "processed on Anthropic's servers"; pill `Pro and Max`. Card `ANTHROPIC HELP CENTER · USE COWORK SAFELY · 2026-10-06`.
- [[copies]] a `copy` stamp on the file ("a copy of just that file"); on `S.find('delete')` the session card fades and the copy with it; pill "per Anthropic's data retention practices". Card `HELP CENTER · 2026-10-06`.
- [[keeps-going]] the house's windows go dark; the vendor's clock ticks and a scheduled task runs. Strip "Close your laptop and Claude keeps going".
- [[hatch-narrow]] the hatch path returns; the path brightens: "any connected folder = reachable from the cloud"; then a dashed outline around the house "managed by your organization: your employer's files". Small pills by the hatch: `desktop app open` · `connected folders only` · `started on desktop or scheduled`.
- [[one-folder]] shelves dim except a new empty folder `Claude-work`; the hatch path reroutes to it only (`Finances` stays dark). Quote "a dedicated working folder for Claude rather than granting broad access"; chip "Mollick: 'a non-private part of my Google Drive' · 2026-07-23"; pointer chip "the habit from the lesson on the agent's folder".
**Exit:** one folder lit, hatch path thin and gold.

## 13 — Every landlord keeps a logbook
**Metaphor object:** the vendor building's logbook; a second landlord down the road.
**Frame:** `K.bg()`. Camera on the vendor building (z 1.3); ledger `K.card(1040, 180, 760, 620)` beside it; left side (x 120-900) holds the four questions at the end.
**Capture:** none (the privacy and memory settings need a signed-in account: drawn, dated cards); fix pass 2026-10-14: at [[training]] the oct6 shot's real line "the Help improve our AI models setting in Settings > Privacy" plays in browser chrome under the drawn toggle.
**Follow-ups (drawn instead of recorded; need a demo account or a run):** Settings > Privacy with the toggle and Settings > Memory with its topics list; the same task in Chat, Cowork and Code; Cowork's connected-folders list; the `Left on this machine:` notice from `claude --cloud`; a cloud session still running after the lid is closed. Also: oct6 needs a mark box `privacy` on that line (scene 13 crops it by source pixels).
**Beats:**
- [[logbook]] the ledger opens (hinge, no overshoot); eyebrow "THE LANDLORD'S LOGBOOK".
- [[training]] entry 1: drawn toggle "Help improve our AI models · Settings › Privacy"; pills `on · up to 5 years` and `off · purged within 30 days of deleting`; plan strip `Free · Pro · Max (incl. Claude Code) = consumer` / `Team · Enterprise · API · Gov · Education = commercial terms`; pill `Pro = consumer plan`. Cards `ANTHROPIC · 2025-08-28 (still current)`, `PRIVACY CENTER · 2026-07-01 · "up to 5 years", de-identified`.
- [[already]] the toggle flips off; a gear "training already started" keeps turning with a file inside: "Your data will still be included in model training that has already started".
- [[memory]] entry 2: a separate box "memory"; a chat card is deleted while two memory chips stay; note "remove under Settings › Memory". Footer (not narrated): "on by default Free, Pro, Max · off per member on Team and Enterprise · feedback kept 5 years". Card `HELP CENTER · 2026-09-30`.
- [[accounts]] entry 3: two account tiles `work` and `home` with a hairline between; quote "Shared logins aren't supported". Unnarrated notes: `Cowork on web and mobile: captured in Compliance API` (Help Center, 2026-10-06) · `cloud session shared as Public: visible to anyone logged into claude.ai; may contain code and credentials` (Claude Code in the cloud, read 2026-10-14).
- [[other-landlords]] a second building down the road, eyebrow `GOOGLE · GEMINI APPS PRIVACY HUB · updated 2026-10-13`: `human reviewers`, `reviewed chats · up to 3 years`, `not deleted when you delete your activity`, `Keep Activity off · 72 hours`; quote "Please don't enter confidential information that you wouldn't want a reviewer to see". Footnote "what changed on 10-13 isn't stated". No OpenAI column.
- [[four-questions]] both ledgers slide back; a four-row card at left, rows on their words: `training setting?` · `people review chats?` · `kept how long, with it off?` · `what does deleting reach?`. Footer `as of 2026-10-14 · moves monthly`.
- [[copies-stay]] eyebrow "where the picture breaks"; the deleted chat's two memory chips glow once inside the logbook: "copies can stay behind".
**Exit:** the four questions on the card, street dim behind.

## 14 — You and the agent
**Metaphor object:** the whole street faint behind; the worker on one side, you on the other, an expert at a gate.
**Frame:** `K.bg()`. Three columns, soft cards y 180-880: `the agent` (x 120-680, sparkle header), `you` (x 700-1260, person header), `bring in an expert` (x 1280-1820, shield header).
**Capture:** none.
**Beats:**
- [[agent-part]] agent column fills: `chat or task?` · `writes for its own shell` · `fixes its own setup (/doctor)` · `installs itself over SSH` · `usually fetches privacy pages → the four questions, dated (says when a page won't load)`.
- [[your-part]] you column: `the room, by the output` · `local or cloud` · `the account and its settings` · `one dedicated folder` (the gold folder from 12 slides in); each row's icon pulses on its object in the faint street.
- [[approval]] a fifth row `the approval level` with a dial `Auto ↔ ask first`; card, eyebrow `ANTHROPIC · HOW CLAUDE CODE WORKS; COWORK CHANGELOG`: "Auto: starting mode in Claude Code v2.1.283+ and new desktop Code tab sessions (since 2026-09-24) · a classifier blocks the risky ones instead of asking you"; quote chip "Until you trust the system ... ask for approval first · Ethan Mollick". Pointer chip "→ the lesson on letting it loose".
- [[expert]] expert column lights with its header question: "Is the data allowed to go there?"; a gate draws between the house and the road.
- [[who]] two entries: `managed computer → IT / security admin` and `patient records · client data under NDA · customers' personal data → compliance, legal or data-protection owner`.
**Exit:** three full columns and the gate at rest.

## 15 — Keep this
**Metaphor object:** the finished street from above at dusk: house with counter, workshop and one gold folder; the road; the vendor building with back office, spare workshop and logbook.
**Frame:** `K.plate('plate', t, { shade: .6, mask: [680, 860] })` under `K.bg({ glow: .5 })`; the street small at top (y 150-400). Three takeaways below, bold lead in Zen Maru 40 gold + Georgia 30 body, x 220-1700, y 450-820. `K.petals` n 5 avoiding the text. `noBadge`.
**Capture:** none.
**Beats:**
- [[keep-1]] **Pick the room by the output.** "The model may be shared; the reach never is." The doors glow.
- [[keep-2]] **Ask which computer runs the work.** "Yours, a box inside it, a machine down the line, or the vendor's cloud working on a copy." The road and the vendor building glow.
- [[keep-3]] **Check the account before anything private goes in.** "Training and memory settings, one dedicated folder; for work data, whoever owns it." The logbook and the gold folder glow.
- [[credits]] small line at y 880, Karla 26, `K.C.soft`: "Built on Ethan Mollick (One Useful Thing) · MIT Missing Semester 2026 · Anthropic (Claude blog, Help Center, Claude Code terminal guide) · all sources and dates on the lesson page".
**Exit:** street, takeaways and credit line at rest; plate drift and petals only.
