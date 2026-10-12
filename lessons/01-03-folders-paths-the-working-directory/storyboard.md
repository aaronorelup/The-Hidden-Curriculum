# 01.03 storyboard: the map and the dot (metaphor-first)

Metaphor object: THE MAP. A large cream-on-indigo card (the disk) with a gold ROOT edge along its top and a gold YOU-ARE-HERE DOT (the working directory). Every scene draws the same card at the same spot, so the dot is what moves. The second dot arrives in section 06; the agent gets its own copy of the card in section 10. Canvas 1920x1080; safe area x 80-1840, y 130-930. Badge top-left, untouched.

Shared frame, used from section 03 on:
- Map card: K.card(380, 200, 1160, 690, {r: 24, glow: true}); hairline K.line along its top edge at y 200, label "root" via K.text at (960, 170), gold, 30 px.
- Dot: gold filled circle with K.glow, radius 22, centre (960, 520); label "working directory" 26 px under it.
- Disk label inside the card top-left: "the disk", 26 px, at (420, 240).

Literal screen text (C:\, /, cd, PS C:\, Shell cwd was reset to) is shown exactly; the narration spells it for the ear.

## 01 — The point

**Metaphor object** — the map card, empty, dimmed.
**Frame** — title card. K.plate('plate', t, {zoom: true, shade: .35}) if the painted plate exists, otherwise K.bg({glow: .6}). Purpose line in K.para at x 160, y 300, width 1600, 40 px, cream. Conclusion line under it at y 560, 30 px, gold. K.petals with avoid rects covering the text block.
**Beats**
- [[point-purpose]]: the purpose line is on screen from the first frame (it is the first spoken sentence), fading in with K.env over the first 0.4 s.
- [[point-conclusion]]: the conclusion line fades in under the purpose line with K.stagger.
- [[nobody-handed]]: the map card rises from y 240 with K.io(t, a, .7, 'out') at 0.6 alpha; the text stays.
- [[point-shelf]]: the card and the text dim together to 0.35 alpha.
**Exit** — purpose line and card dimmed to 0.35, calm.

## 02 — Where it lives

**Metaphor object** — the map card, now not drawn; the course map is the full frame.
**Frame** — K.map.draw(t, {focus: 'machine', pin: '01', highlight: 'machine'}) fills the safe area. Eyebrow "DISTRICT 1 · THE MACHINE" at (960, 150), gold, 26 px.
**Beats**
- [[pin-drop]]: the district question "what's on your computer?" (38 px district type, K.map type) appears with districtK easing the district in; the pin drops onto module 01 with pinDrop = K.io(t, a, .7, 'back'); rowWash {'01': {k}} washes the row.
- [[path-role]]: a small K.file icon and a K.text line "every file has an address" sit under the map at y 880, 30 px.
**Exit** — map held with the pin on 01, gold ring calm.

## 03 — The mental model

**Metaphor object** — THE MAP and the gold dot.
**Frame** — shared frame. The card grows in from scale 0.9 to 1 at centre with K.io. Labels "root" and "working directory" fade in with the card.
**Beats**
- [[mental-model]]: a small directions strip at the top of the card reads "3 streets east, then 2 up", 26 px, with a K.path from a point at the root edge to a target, to show directions need a start. The dot is not yet visible. Windows note: the narration says each drive has its own root; the root edge is drawn once, and no second edge is drawn here.
- [[you-are-here]]: the gold dot drops in at (960, 520) with K.io(t, a, .6, 'back'); K.glow pulses with K.wave at small amplitude.
- [[dot-is-working-dir]]: the label "working directory" types in under the dot (K.typed, 26 px), with a hairline from the label to the dot.
**Exit** — card and dot calm, dot idling. The dot stays where it is for section 04.

## 04 — Absolute paths: the full address

**Metaphor object** — THE MAP; the root edge is now the start point of every address.
**Frame** — shared frame. Dot dims to 0.4 alpha at centre. Two pills inside the card: "C:\" (mono 30 px) at (560, 240) and "/" (mono 30 px) at (1300, 240), each K.pill.
**Beats**
- [[absolute]]: a K.path from the root edge at (960, 200) down to a target at (1300, 620), head drawn; a small gold tick marks the target. Reads as an address counted from the edge.
- [[windows-form]]: the "C:\" pill glows gold; the literal path C:\Users\you\project\data.csv is shown in mono 30 px at y 860, with the drive part lit first.
- [[unix-form]]: the "/" pill glows gold; a second literal form /home/you/project/data.csv appears under the first line at y 900 in mono 30 px.
- [[separators]]: two pills "backslash" and "forward slash" at 26 px, joined to the root label by hairlines. No command text.
**Exit** — the absolute arrow stays on the map from the root; the dot is still there, dim.

## 05 — Relative paths and the working directory

**Metaphor object** — THE MAP and the dot, bright again.
**Frame** — shared frame. Dot back to full brightness at (960, 520). A terminal strip at the bottom: K.win(80, 780, 900, 130, {title: 'PowerShell', kind: 'terminal'}) showing "PS C:\Users\you\project>" with a caret, 26 px. Keep it inside y 780-910.
**Beats**
- [[relative]]: a K.path from the dot to a target three steps away, with three small gold ticks labelled "three streets from here" (26 px). The arrow is measured from the dot, not from the root.
- [[inherit]]: a hairline from the dot up to a small K.icon('terminal') labelled "started from here" 26 px; the dot gets a faint ring.
- [[measured-from]]: a dashed grey K.path from a small K.file icon to the target, struck through with K.mark, showing the file is NOT the measuring point.
- [[prompt-dot]]: a hairline from the prompt strip to the dot; the prompt text lights up, showing the dot is printed on the screen.
**Exit** — the arrow from the dot stays; the crossed-out dashed line stays faint.

## 06 — The same name, two places

**Metaphor object** — THE MAP, now two copies side by side, each with a dot.
**Frame** — left card K.card(80, 200, 820, 690) and right card K.card(1020, 200, 820, 690). Left dot at (490, 520), right dot at (1430, 520). Each card has a K.file "data.csv" (nameSize 26): the left file sits where its dot can reach, the right card holds only empty ground. Labels 30 px.
**Beats**
- [[works-on-my-machine]]: a K.file ext 'py' labelled "script.py" fades in at the top centre of the page, between the two cards, as the script name is said.
- [[two-places]]: left card: a K.path from the dot to the file with head drawn; a gold pill "found" beside the file. Right card: the same arrow tries to reach the ground and stops in a K.mark (cross), with pill "no such file" at 26 px.
- [[same-name]]: the right dot slides in from the middle with K.io and sits on its own card; the left and right cards both hold while the eyebrow "same words, two dots" appears centred at y 150 (no cue; it holds through the cue).
**Exit** — both cards held, the found and crossed-out states still visible; calm.

## 07 — Shortcuts, and where the picture breaks

**Metaphor object** — THE MAP, collapsed back to one card with one dot.
**Frame** — one card at centre (shared frame). Dot at (960, 520).
**Beats**
- [[tilde]]: a K.icon('house') appears at the top right of the card with a hairline to the root; pill "home folder" 26 px. The screen shows only the icon and the pill; "tilde" is spoken.
- [[dots]]: a small arrow at the top edge points upward, ending in an open stop; pill "the folder above" 26 px. A second small pill "this folder" sits on a short arrow at the dot.
- [[break-copy]]: the dot splits into three small copies (K.stagger, 0.12 step), each with a thin gold border, in a row; the single big dot fades. Pill "one dot per running program" 26 px at y 860.
- [[root-end]]: a pill "nowhere further" 26 px hangs on the top-edge stop; the picture holds.
**Exit** — three copies hold, the top-edge stop visible; calm.

## 08 — What is really going on

**Metaphor object** — the dot copies from section 07, collapsed to one main dot plus one child.
**Frame** — main card and dot at left (560, 520); a smaller child card at right (1240, 520) with a child dot. Within safe area.
**Beats**
- [[cd-scope]]: a K.path from the main dot labelled "cd" (mono 26 px) shows the change stays in the main card; the pill "this session only" 26 px sits on the main card.
- [[child-process]]: a K.path from the main dot to the child dot labelled "a child copy"; the child dot moves only within its own card; the main dot holds still. Pill "does not move its parent" 26 px under the arrow.
- [[python-second]]: a side card at the right (1500, 240, 300, 150), labelled "import list" 26 px, with a dashed second arrow in K.mixColor of gold and accent, and pill "05.02" below.
**Exit** — main dot, child, and the dashed import arrow remain as the lesson's last picture of the rule.

## 09 — The surprises you'll hit

**Metaphor object** — THE MAP shrunk to a thin band at the top (y 160-230) with the dot as a small gold tick at centre; the error lines go on cards below.
**Frame** — one card at a time in the centre band (K.note-sized, 30 px body in mono). Each fades out before the next comes in.
**Beats**
- [[err-no-such-file]]: card 1 shows "no such file or directory" in mono, eyebrow "macOS, Linux, Git Bash" (26 px). Pill "name not found from this dot".
- [[err-python]]: card 2 shows the exact line "FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'" in mono 30 px, with the quoted name 'data.csv' marked by K.mark. Pill "the name is right, the place is wrong".
- [[err-powershell]]: card 3 shows "cannot find path ... because it does not exist" in mono. Eyebrow "PowerShell, file commands". Label "something like"; not presented as exact text.
- [[git-bash-spelling]]: card 4 shows "C:\Users\you" and "/c/Users/you", joined by a K.arrow labelled "same place". Pill at 26 px.
- [[agent-reset]]: card 5 is a Claude Code tool-result line in a K.win terminal, shown as written: "Shell cwd was reset to <dir>" (wording seen in local session transcripts; can change between versions). Pill "the shell went back to the project" with a small K.icon('warning') and "some users report this" 26 px.
**Exit** — card 5 held; the other lines faded; calm.

## 10 — The lantern: agents and the folder they stand in

**Metaphor object** — THE MAP, with a second copy for the agent, drawn with the sparkle icon and the lantern (K.map.lantern beside it, lit). The lantern is the AI.
**Frame** — left card K.card(80, 200, 820, 690): the human's map and dot. Right card K.card(1020, 200, 820, 690): the agent's map and dot, same shape, with a small lantern icon above it. Dots at (490, 520) and (1430, 520).
**Beats**
- [[lantern-change]]: under each card a time pill. Left: "2021: you typed cd". Right: "now: the agent types cd". Two small pills sit on a dated rule at y 880: "Claude Code research preview, Feb 2025" and "Codex CLI, Apr 2025", 26 px.
- [[lantern-rule]]: a K.path runs from the lantern to the agent's dot, labelled "cd carries over to the next command" (26 px). A dashed second arrow from the agent's card back to a project-folder card is labelled "reported: pulled back to project" (26 px). The human card dims to 0.5 alpha.
- [[lantern-sandbox]]: a faint dashed K.rr around the agent's card; inside, a K.file icon on writable ground; outside, a K.mark on a file. Pill "macOS, Linux, WSL2 (per docs read this month)" 26 px at the bottom.
- [[lantern-reported]]: a small reported-issue pill with K.icon('warning') and text "reported, not a rule" 26 px.
- [[lantern-worktree]]: a second small card K.card below the agent's card with a K.folder and the label "same project, own branch" 26 px.
- [[lantern-close]]: the closing line appears under both cards at y 900, 30 px cream; both dots hold, with a gentle idle sway (K.wave).
**Exit** — both maps and dots, the lantern lit, the closing line calm.

## 11 — Safe to ignore for now

**Metaphor object** — THE MAP, dimmed, at 0.25 alpha in the background.
**Frame** — four small pills in a row at y 420, each 26 px with a small K.icon: "260 characters" (puzzle), "forward slashes" (code), "/mnt/c" (server), "import list" (puzzle, different colour). Each labelled "later" in quiet text beneath.
**Beats**
- [[ignore-260]]: pill 1 appears; "01.08" shown beneath it.
- [[ignore-slashes]]: pill 2 appears; no code shown beyond the pill.
- [[ignore-wsl]]: pill 3 appears with the literal /mnt/c in mono 30 px.
- [[ignore-python]]: pill 4 appears with "05.02" beneath it.
**Exit** — four pills held, dim, calm.

## 12 — What it connects to

**Metaphor object** — THE MAP, with neighbour shelves lit in the map's own district layout.
**Frame** — K.map.draw(t, {focus: 'machine', pin: '01', highlight: ...}) drawn at the top (y 180-600) with chips 01 (lit), 02 and 05 (lit as neighbours), 04 and 08 (lit at 0.4). Five labelled cards below (y 640-900): "01.04 hidden files", "01.05 PATH", "02.03 moving around", "05.02 running a file", "08.11 worktrees". Labels 26 px minimum.
**Beats**
- [[connect-hidden]]: the 01.04 card slides up with K.stagger; a K.arrow from the pin to it.
- [[connect-path]]: the 01.05 card slides up; a K.arrow from the pin to it.
- [[connect-move]]: the 02.03 card appears with K.stagger.
- [[connect-running]]: the 05.02 card appears with K.stagger.
- [[connect-worktrees]]: the 08.11 card appears last, held at the end of the section.
**Exit** — five cards and the small map held; arrows calm.

## 13 — Keep this

**Metaphor object** — THE MAP, full size again, dimmed to a backdrop, with the dot and the root marked in gold.
**Frame** — end card: K.plate with mask [680, 860] for the lower band; three takeaway cards stacked at x 260-1660, y 240-740, each with a gold eyebrow "1", "2", "3" and the bold lead in K.para at 34 px, the rest at 30 px. Petals with K.petals avoid rects set to the card rects, so no petal sits on text.
**Beats**
- [[keep-one]]: card 1 pops in (K.pop) with "A path is an address."
- [[keep-two]]: card 2 pops in with "Every running program has a working directory."
- [[keep-three]]: card 3 pops in with "The same name can mean a different file."
**Exit** — three cards held, petals calm; end card still.
