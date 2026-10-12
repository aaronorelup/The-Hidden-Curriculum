# 01.04 storyboard: the back room behind the shop

Final (judge synthesis of drafts A/B/C, spine B). Every [[cue]] in script.md has exactly one beat below.

Metaphor object: THE SHOP CROSS-SECTION. One drawing, built in 03 and kept in the same place through 15, so what changes is what moves in and out of it. Canvas 1920x1080; safe area x 80-1840, y 130-930; badge top-left untouched; nothing essential below y 930. Drawn only with the kit (cards, pills, lines, K.file / K.folder, K.win, K.icon, K.term, K.map, K.plate). Labels 26 px minimum, 30+ px for anything read; one idea per screen; screen carries literal forms (.git, .env, .venv), narration spells them.

Shared frame (from 03 on, same coordinates every scene):
- SHOP FLOOR: K.card(120, 200, 960, 690, {r: 24}); eyebrow "SHOP FLOOR" at (150, 236). Inside, a small K.win(170, 270, 860, 560, {kind: 'explorer', title: 'my-project', titleSize: 26}) listing visible items: K.folder "src", K.file "app.py", K.file "README.md" (nameSize 26).
- BACK WALL: K.line(1120, 200, 1120, 890, {color: K.C.line2, w: 3}).
- DOOR: K.card(1080, 440, 80, 300, {r: 8, stroke: K.C.gold}) on the wall line; doorknob K.glow(1146, 600, 6, K.C.gold, .8).
- SIGN: K.pill("staff only", 1120, 400, {size: 28}) above the door. The sign is the thing that changes kind (painted dot vs hung flag) in 04.
- BACK ROOM: K.card(1160, 200, 680, 690, {r: 24, fill: K.C.tile}); eyebrow "BACK ROOM" at (1190, 236). Three shelves as hairlines K.line at y 380, 560, 740 from x 1190 to 1810.
- PORTER: K.icon('person', x, 760, 64) walking along the shop floor (same porter as 01.02); idle bob K.wave(t, 1.2, 3).
- Camera: K.cam eases between "wide" (whole frame, z 1), "room" (z 1.35 centred on the back room, x 1500, y 545) and "floor" (z 1.25 on x 600). Moves 0.6-0.8 s, K.ease.io. One 'back' overshoot max per scene.

## 01 — The point

**Metaphor object** — the door with the "staff only" sign, alone, dim, at the right edge (foreshadow; no shop yet).
**Frame** — title card. K.plate('plate', t, {zoom: true, shade: .35}) if engine/assets/teahouse-night.jpg exists, otherwise K.bg({glow: .6}). Eyebrow "01.04 · HIDDEN FILES & DOTFILES" at (160, 250). Purpose line K.para at (160, 300), width 1180, 40 px, cream. Conclusion line K.para at (160, 520), width 1180, 32 px, gold. Door + sign drawn at x 1560, y 360-700, 0.5 alpha. K.petals with avoid rects over the text block and the door.
**Beats**
- [[point-purpose]]: purpose line on screen from the first frame, K.env fade over the first 0.4 s.
- [[point-conclusion]]: conclusion line fades in under it (K.stagger, 0.6 s).
- [[point-secrets]]: K.icon('key', 1560, 780, 56) fades in under the door, terracotta.
- [[point-agents]]: K.icon('sparkle', 1640, 780, 56) joins it; the door opens a crack (door card width eases 80 → 56, gold sliver of K.glow behind).
**Exit** — text and the ajar door hold; petals drift; calm.

## 02 — Where it lives

**Metaphor object** — off screen; the course map is the frame (the door returns in 03).
**Frame** — K.map.draw(t, {focus: 'machine', pin: '01', highlight: 'machine', lanterns: .6}) filling the safe area. Eyebrow "DISTRICT 1 · THE MACHINE" at (960, 150), gold, 26 px.
**Beats**
- [[pin-drop]]: district eases in via highlight {machine: k}; pin drops on module 01 with pinDrop = K.io(t, a, .7, 'back'); district question "what's on your computer?" 34 px at (960, 880).
- [[addresses]]: the question swaps (K.env) for a K.spans line at (960, 880): "every file has an address" (cream) + " · some are left off the tour" (gold).
**Exit** — map held, pin glowing on 01.

## 03 — The mental model

**Metaphor object** — the shop cross-section is built for the first time.
**Frame** — shared frame, wide camera.
**Beats**
- [[shop-floor]]: SHOP FLOOR card rises (K.rise); the Explorer window inside fills with src, app.py, README.md (K.stagger).
- [[porter-tour]]: porter icon enters at x 200 and walks to x 900 along y 800 (K.io 1.6 s); a small K.pill "File Explorer · Finder" follows above it.
- [[staff-door]]: back wall line draws (K.line k), door card appears, sign pill pops in with the scene's one K.io 'back'. The porter walks past it and stops at x 980, facing back toward the floor.
- [[back-room]]: BACK ROOM card fades in behind the wall at 0.7 alpha; four line icons sit on the shelves, one each: gear (settings), clock (history), puzzle (supplies), key (keys); 26 px labels under each.
- [[keep-picture]]: camera eases to "wide" and the whole frame settles; door outline glows gold for 0.8 s.
**Exit** — full cross-section, porter idle on the floor, door closed, calm.

## 04 — Why it's hidden: two kinds of sign

**Metaphor object** — the sign on the door, which splits into two kinds.
**Frame** — shared frame, camera "wide" then splitting attention: the shop floor card dims to 0.4 and two sign cards appear over it: left K.card(160, 260, 440, 300) "Mac · Linux", right K.card(640, 260, 440, 300) "Windows".
**Beats**
- [[painted-dot]]: the sign pill above the door duplicates; two copies slide (K.io .7) into the two cards. In the Mac · Linux card, the name ".env" in mono 40 px; the leading dot fills gold, as if painted. Label under it: "a dot in the name" 28 px.
- [[pike]]: a K.win terminal (160, 590, 920, 240) types `ls` and shows only `app.py  src` while a ghost line `.  ..  .git  .env` fades to 0.25 (K.term). Caption 26 px: "as Rob Pike tells it · he later called it a mistake". No year, no name of who wrote the shortcut.
- [[flag-on-door]]: in the Windows card, a K.file icon with a small K.pill "Hidden" hung on its corner like a tag, swinging gently (K.wave, small).
- [[open-doors]]: in the Windows card a second file ".env" with no tag sits fully visible; beside it a K.folder ".git" with the "Hidden" tag and a small chip "Git for Windows". Label: "dot ignored · flag decides".
- [[show-hidden]]: the two cards fade to 0.3; four pills stack at (620, 400 → 760): "View > Show > Hidden items", "Cmd+Shift+.", "ls -a", "Get-ChildItem -Force" (mono, 28 px). Labels only.
**Exit** — the four pills hold, the door and its sign quiet behind.

## 05 — Two back rooms: the project's and yours

**Metaphor object** — the back room, which now comes in two: the shop's and the one in your house.
**Frame** — camera pulls back (z 1 → 0.8) so the whole shop shrinks to the left half (x 120-940); a second, smaller drawing appears on the right: K.icon('house', 1180, 260, 64) + its own back room card K.card(1100, 320, 740, 560) "HOME FOLDER", eyebrow "~".
**Beats**
- [[project-room]]: camera pull-back; the shop's back room fills with three K.folder icons (nameSize 26): ".git", ".venv", ".vscode"; a K.pill "travels with the project" under it.
- [[house-room]]: the house icon and its card fade in; the home card's eyebrow "your settings, not one project's" fades in.
- [[dot-config]]: inside the home card, one tidy K.folder "~/.config" top-left, gold outline; then four loose folders appear around it with a slight random offset (K.rng seed): ".ssh", ".aws", ".claude", ".codex".
- [[appdata]]: a K.folder "AppData" appears in the home card's lower half with a "Hidden" tag; three K.pill rooms fan out under it: "Roaming · follows a work login", "Local · this machine", "LocalLow · fewer permissions · mostly games".
- (optional, no cue; rides on [[appdata]] + 2 s) a small counter K.text "46" (60 px, gold) with label "dot-named items · one Windows home folder · 2026-10-09" (26 px) at (1470, 840). Screen only; observation on the course machine, not a general claim.
**Exit** — both back rooms visible; calm.

## 06 — What's on the project's shelves

**Metaphor object** — the project's back room, shelves filled.
**Frame** — camera "room" (z 1.35 on the back room); home drawing off screen.
**Beats**
- [[dot-git]]: camera eases in and the three shelf lines draw; top shelf: K.folder ".git" with K.icon('book') "ledger" beside it; a small stack of five thin cards behind it (versions). Then the folder fades to 0.2 while the shop floor files (seen through the doorway at left edge) stay at full: "files stay · history gone".
- [[toolbox]]: middle shelf: K.folder ".venv" with K.icon('puzzle') "toolbox"; tiny chip "link to Python + packages". On "Aaron", a small K.icon('cap') with a K.icon('question') beside the folder (label "IT degree", 26 px).
- [[self-ignore]]: a little K.file ".gitignore" pops inside the .venv folder with a check icon; label "Python 3.13+ · uv".
- [[gitignore]]: a K.file ".gitignore" pinned on the back-room wall (top-right), and a K.pill "never pack" next to it (the kit has no van icon; the pill carries the moving-van idea). Label "hides nothing · only tells git what not to pack".
- [[editor-settings]]: bottom shelf: K.folder ".vscode" (nameSize 26).
**Exit** — three shelves full, calm.

## 07 — The drawer of keys with no lock

**Metaphor object** — a drawer on the bottom shelf, the .env file.
**Frame** — camera "room", then nudges to the bottom shelf (z 1.5, y 700).
**Beats**
- [[env-file]]: a K.card drawer (1300, 760, 360, 100, r 8) slides out of the bottom shelf (K.io .7), with K.icon('key') inside; then a K.win editor (1180, 260, 640, 260, {kind: 'code', title: '.env', titleSize: 26}) rises above the drawer with K.editor lines: `API_KEY=xxxx-not-a-real-key`, `DB_PASSWORD=xxxx` (mono 28 px). Chip "→ environment variables · 01.05".
- [[no-lock]]: K.icon('lock', 1700, 800, 56) appears over the drawer, then gets a K.icon('cross') across it, terracotta. Label "plain text".
- [[never-commit]]: a K.arrow from the drawer toward a K.icon('cloud') labelled "git history" is cut by a gold K.line bar; the .env name gets written onto the .gitignore note on the wall (typed). Sub-label "already pushed? replace the key".
- [[never-paste]]: K.icon('chat') with a dashed K.arrow from the drawer, crossed out; then a small K.folder "~/.claude/projects/" with a K.file "transcript" appearing beside it, the key icon inside it, 26 px label "per Claude Code's docs".
- [[push-net]]: a K.pill "push declined: secret detected" slides across the arrow path like a net (dashed K.line under it). Label "some patterns · public repos · can override".
**Exit** — drawer open, net pill held, calm.

## 08 — Where the picture breaks

**Metaphor object** — the back wall and door: revealed as paint.
**Frame** — camera "wide".
**Beats**
- [[break]]: everything but the wall, door and sign dims to 0.4; then the wall line turns dashed (K.line dash) and the door card's fill fades to 0, leaving a dotted outline; the sign pill gains a small label "display choice".
- [[walk-in]]: four K.icon chips walk through the dotted door from the floor into the back room in a stagger: terminal ("script"), code ("program"), sparkle ("agent"), warning ("malware"). The porter alone stops at the wall.
- [[real-locks]]: three pills rise in the back room: "permissions · 01.07", "encryption", "secrets manager · 15.07", each with K.icon('lock').
**Exit** — dotted door, real-lock pills held, calm.

## 09 — The lantern: new staff in the back room

**Metaphor object** — the back room, now with lantern-carrying staff, a notes wall and a wiring board.
**Frame** — camera "room". Solid wall restored but kept slightly dashed (continuity with 08).
**Beats**
- [[new-staff]]: two K.icon('sparkle') figures enter through the door, each with a small K.icon('lantern') glow above it (K.glow gold, small sway).
- [[pinned-notes]]: a notes wall (top half of the back room) fills with pinned K.card notes, stagger: "CLAUDE.md", "AGENTS.md", "GEMINI.md" (screen only), ".cursor/rules/", ".github/copilot-instructions.md" (mono 26 px). Dashed arrows from each staff icon to the notes (reading).
- [[wiring-board]]: below, a board K.card with three sockets (K.ring) and plugs (K.icon('puzzle')); labels ".mcp.json", ".cursor/mcp.json", ".vscode/mcp.json", "claude_desktop_config.json (AppData)" (only .mcp.json is spoken).
- [[staff-notebooks]]: camera eases briefly right to the home back room (from 05, re-entering) where K.folder "~/.claude", "~/.codex", "~/.cursor" (screen) gain a small K.icon('book') each; sub-label "skills · auto memory".
- [[converging]]: back to the notes wall: a K.arrow from the Copilot note to "CLAUDE.md"; a second arrow from a "Claude Code" chip to "AGENTS.md" with a "new · Sept 2026" pill; then "AGENTS.md" and ".mcp.json" both get a small gold outline and a shared pill "Linux Foundation · Dec 2025".
**Exit** — staff idle, lantern glow swaying small; calm.

## 10 — Then and now: from notes to orders

**Metaphor object** — the pinned notes, which transform into orders.
**Frame** — split time: a K.eyebrow "2021" left half and "NOW" right half above the same back-room drawing, duplicated small: left copy (120-940) and right copy (980-1800).
**Beats**
- [[then]]: left copy shows the 2021 back room: .git, .gitignore, .env, .vscode; notes are plain cream cards; no staff. Chip ".env committed · the classic mistake".
- [[now-orders]]: right copy: the same notes turn terracotta-edged and each gains a K.icon('terminal') — notes became orders; the staff icons act on them (K.arrow from note to staff to a "runs" chip).
- [[strangers-note]]: a new note slides in from outside the right copy, labelled "cloned repo"; the staff obey it (arrow). Three small chips stack under it: "hidden characters in a rules file · Mar 2025 · research", "repo's Claude settings ran commands · fixed", "these files are code". Optional fourth chip, not spoken: "Cursor mcp.json swapped · 2025 · fixed". CVE ids, if used, at 26 px only.
- [[malware]]: K.icon('warning') "poisoned package · Aug 2025" enters the right copy and points the staff's own lanterns at the key drawer (arrows).
- [[leak-figure]]: K.text "~80%" (64 px gold) with label "AI-service key leaks, 2025 vs 2024 · GitGuardian (vendor figure)".
**Exit** — both copies held, the right one busier; calm.

## 11 — Your job: check the back room

**Metaphor object** — the back room, after the staff leave; the owner walks in.
**Frame** — camera "wide" then "room". Staff icons fade out; K.icon('person', gold) labelled "you" enters through the door.
**Beats**
- [[owner]]: the owner icon enters; label "owner".
- [[after-staff]]: changed items in the back room get a soft gold K.ring (the .claude folder, .mcp.json, one note).
- [[diff]]: a K.win terminal (180, 300, 880, 420) on the shop floor types `git status` then shows `Changes not staged for commit:` / `modified:   .mcp.json` / `modified:   AGENTS.md` / `Untracked files:` / `.claude/` (K.term, 28 px).
- [[review-as-code]]: a K.win editor beside it shows a two-line diff of .mcp.json (no status red/green: accent for the removed line, gold for the added one), label "review like code".
- [[polite-note]]: a pinned note "please don't read .env" on the wall, with label "request, not a lock"; next to it a real K.icon('lock') pill "deny rules · sandbox · protected paths · 14.12".
- [[heading]]: on the drawer, a K.pill "virtual .env · beta" with a dashed outline; under it "plain .env · still the default".
**Exit** — owner in the room, rings faded, calm.

## 12 — The surprises you'll hit

**Metaphor object** — the cross-section stays dimmed at 0.3 behind; the surprises are cards pinned one at a time across it.
**Frame** — one K.card(360, 300, 1200, 420) at a time, centred, swapping with K.env; each card: a literal screen fragment (mono 30 px) on top, a 30 px plain explanation below. The relevant spot in the dim cross-section glows behind each card.
**Beats**
- [[no-git]]: card: Explorer window listing `src  app.py` and a terminal line `git status` → `On branch main`; under: "it's there, just hidden". Glow on .git.
- [[windows-open]]: card: Explorer listing of the project `.claude  .env  .vscode  app.py` (no .git), plus a small second line for the home folder `C:\Users\you` with `.ssh  .claude` visible; under: "the flag, not the dot".
- [[still-on-github]]: card: `.gitignore` with `.env` added, beside a GitHub-style K.win (browser, url "github.com/you/project") still listing `.env`; under: "already committed · replace the key".
- [[push-declined]]: card: terminal `git push` → `push declined: secret detected` (generic label, not GitHub's exact text); under: "the net caught a key".
- [[roaming-path]]: card: a path in mono `C:\Users\you\AppData\Roaming\Claude\` ; under: "your home back room". Glow on AppData in the home back room.
- [[ds-store]]: card: Finder-like K.win listing `.DS_Store` in a project; under: "Finder leaves these behind".
- [[leftovers]]: card: a home-folder listing with a dimmed K.folder ".some-old-tool" among live ones; under: "left behind by a tool you tried once". Glow on the home back room.
**Exit** — last card fades; dim cross-section remains; calm.

## 13 — Safe to ignore for now

**Metaphor object** — a corner of the home back room, with boxes you can leave closed.
**Frame** — camera on the home back room; a K.card(1100, 320, 740, 560) list of muted pills (soft colour, 28 px).
**Beats**
- [[ignore]]: pills stagger in, each with a soft K.icon('clock') "later": "~/.cache · ~/.local", "~/Library (Mac)", "which settings file wins".
- [[dotfiles-repos]]: last pill "dotfiles repos"; on "Recognise the names" all pills settle to 0.6 alpha.
**Exit** — muted pills held, calm.

## 14 — What it connects to

**Metaphor object** — doors out of the back room, each to another lesson.
**Frame** — K.map.draw(t, {focus: 'machine', pin: '01', chips: true}) at 0.5 scale on the left (K.at(500, 540, .55)); on the right, a column of doors (small door cards, same style as the main door) each with a pill.
**Beats**
- [[env-vars]]: door 1 "environment variables · 01.05"; the map's 01 row glows.
- [[venv-git]]: doors 2-3 "virtual environments · 05.03", ".gitignore & secrets · 08.07"; map highlights code and history districts.
- [[ai-files]]: doors 4-5 "instruction files · 03.09", "MCP config · 10.09"; the lanterns over the map light (lanterns k).
- [[secrets]]: door 6 "secrets out of plain text · 15.07"; trust district highlights.
**Exit** — six doors and the small map held, calm.

## 15 — Keep this

**Metaphor object** — the door, ajar, with its sign and a little gold light coming through.
**Frame** — end card. K.plate('plate', t, {shade: .45}) if present, else K.bg({glow: .6}). Door + sign at x 1600, y 320-700, ajar (width 56), K.glow behind. Three takeaways at x 160, y 300 / 470 / 640, width 1200: bold lead in K.title 44 px gold, rest in K.para 30 px cream. K.petals with avoid rects over text and the door.
**Beats**
- [[keep-1]]: takeaway 1 rises: **Hidden means out of sight, not locked.**
- [[keep-2]]: takeaway 2 rises: **Your secrets live in the hidden layer.**
- [[keep-3]]: takeaway 3 rises: **Agents read and write this layer.** The door's light brightens a little.
**Exit** — three takeaways and the ajar door hold for the 3 s tail; petals drift; calm.
