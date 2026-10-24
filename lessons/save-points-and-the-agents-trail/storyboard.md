# Storyboard — 01.03 Git without typing it: save points and the agent's trail

**The one metaphor: a hand-drawn trail map that the guide (the agent) draws on and the walker (you) reads.** It is built once in 03 and transforms scene by scene; it is never redrawn from scratch. Stones are commits, signposts are branches, a lantern marks the live branch (set outside the map), a ranger station across the valley is the remote, footprints stamped `verb → target` are the trail, tracing paper is the diff, a noticeboard facing the road is a public remote, a pencilled stretch is a pull request, torn stones are history rewrites, and the guide's eraser is checkpoints. Where it breaks (spoken): a signpost is only a name and the lantern is set outside the map (05); every git copy is full and equal (06); stones can be torn out (11).

Persistent parts (1920x1080; text 26 px or more; inside x 80-1840, y 130-930; nothing essential below y 930):

- **Map sheet**: `K.card(120, 170, 1680, 740, { r: 24, fill: K.mixColor(K.C.tile, K.C.paper, .08) })`, faint grain, one or two hairline contours (`K.path`, `head: false`, `K.C.line`, alpha .4). The stage for 03-13; scenes move `K.cam` over it.
- **Path** (`main`): gold dashed `K.path`, y ≈ 560, x 220-1180.
- **Stones**: `K.ring` r 26, fill `K.C.tile`, stroke `K.C.gold`, a mono 26 px short ID under each, taken from the capture output via `K.termTimes` (never typed in); a thin `K.arrow` (`K.C.quiet`) back to the parent.
- **Signposts**: `K.line` post (w 6, `K.C.soft`) with a square plank `K.card(…, { r: 6 })` carrying a mono 26 px name; each eases to the newest stone on its line.
- **Lantern**: `K.icon('lantern', …, 54, { color: K.C.gold })` with `K.glow`.
- **Guide**: `K.iconTile('sparkle', …, 84)` holding a short gold `K.line` pen. **Walker**: `K.iconTile('person', …, 84)`, cream, with a dashed sight-line to whatever is being read.
- **Ranger station** (from 06): beyond a valley gap at x 1250-1330; `K.card(1380, 300, 380, 420)` with `K.icon('house')` and eyebrow "REMOTE · E.G. GITHUB"; inside, a smaller dashed replica of the path holding only pushed stones.
- **Footprints** (from 07): paired prints along the path, each with a Karla 26 px pill `verb → target`.
- **Captures**: in `K.win(980, 200, 820, 660, { kind: 'terminal', title: 'Git Bash · demo-site', titleSize: 26 })` on the right while the map eases to the left half (`K.cam` z .55). Replays use `K.termReplay` / `K.demo`; every mark and beat time comes from `K.termTimes(name, o)`.

Palette: path, stones, lantern gold; signposts cream; "never named" things terracotta (`K.C.accent`); station `K.C.line2`; blossom only on title and end cards. At most one `'back'` overshoot per scene. Source cards are `K.note` (26-30 px) in the top-right band (x 1180-1800, y 150-330) unless stated, each with its date; every Claude Code card ends "read 2026-10-23 · this moves monthly".

All three captures: `tools/capture.py terminal save-points-and-the-agents-trail <name>`, recipes in `lessons/save-points-and-the-agents-trail/steps/<name>.json`, `"shell": "bash"`, `"cwd_display": "C:\\Users\\you\\demo-site"`, a throw-away folder, capture.py's neutral git config and demo identity `Demo Learner <learner@example.com>`, no network, no account, nothing personal. The narration never tells the viewer to type a command.

---

## 01 — The point
**Metaphor object:** the folded trail map on a tea-house table, the guide's pen beside it.
**Frame:** `K.plate('plate', t, { zoom: true, shade: .5 })`, no badge, no district or module names. `K.title('Git without typing it', 960, 270, { size: 80, align: 'center' })`; subtitle "save points and the agent's trail" (Karla 34, `K.C.soft`) at y 330. Purpose line `K.para` Georgia 34, w 1360, y 390-500; conclusion `K.para` Georgia 32, y 530-650. Emblem at y 740: a tiny path, three stones, one signpost with a lantern. Credit line y 880, Karla 26, `K.C.soft`: "Built on Anthropic, Best practices for Claude Code · Lovable, Git sync docs". `K.petals` n 6 avoiding the text.
**Capture:** none.
**Beats:**
- [[purpose]] title resting; purpose line rises 12 px into place.
- [[conclusion]] conclusion writes in; the emblem's stones pop in left to right (stagger .12).
- [[why]] a small arrow runs quickly along the emblem path (0.4 s); the lantern dips once to alpha .6 and back (no flashing).
**Exit:** all text and the emblem still; petals drift.

## 02 — Where this sits on the map [map]
standard map scene (K.map.intro)

## 03 — The guide holds the pen
**Metaphor object:** the map unfolds; guide and walker take their places.
**Frame:** `K.bg({ glow: .3, glowX: 960, glowY: 520 })`. Map sheet unfolds (scaleY 0 → 1, 0.7 s). Guide at (380, 760), walker at (1540, 760).
**Capture:** none.
**Beats:**
- [[map]] the sheet unfolds; contours draw; the empty path draws left to right (1.2 s).
- [[guide]] guide pops in with its pen and draws a short squiggle at the path start; walker fades in with a dashed sight-line to the map; labels "draws" / "reads".
- [[before]] guide dims to .3; a ghost walker-with-pen scribbles crooked terracotta marks that get crossed out. Card: "Aaron Orelup · AO-007 · 2026-08-08 · 'Git was the worst of it' (May 2025)".
- [[talk]] ghost fades, guide returns; speech bubbles rise from the walker: "what files have I changed?", "show me the last 5 commits", then smaller "help me resolve merge conflicts" (mono 28; Anthropic, Claude Code quickstart). Under them: "'You won't need to learn Git yourself.' · Anthropic, Terminal guide for new users · read 2026-10-23".
- [[changed]] a pill `2026-09-25 · auto mode` drops onto the guide (the scene's one `'back'`); a small arrow labelled "may push on its own". Card: "auto mode · starting mode for terminal and V S Code from v2.1.283 · Anthropic, Choose a permission mode · read 2026-10-23 · this moves monthly".
- [[heading]] cards fade; the walker's sight-line brightens and splits toward three empty spots (future lantern, station, footprints); label "likely: your job is checking these".
**Exit:** empty path; guide and walker resting; sight-lines at alpha .4.

## 04 — Stones: a commit is a save point
**Metaphor object:** the first stones on the path.
**Frame:** `K.bg()`. Map persists full width; from [[real]] it eases to the left half and the terminal opens right.
**Capture:** `save-points`. Commands: `git init -b main` · `echo "<h1>Hello</h1>" > index.html` · `git add index.html` · `git commit -m "Add homepage"` · `echo "<p>About</p>" > about.html` · `git add about.html` · `git commit -m "Add about page"` · `git switch -c feature/contact` · `echo "<p>Contact</p>" > contact.html` · `git add contact.html` · `git commit -m "Add contact page"` · `echo "<p>Phone</p>" >> contact.html` · `git commit -am "Add phone number"` · `git switch main` · `git merge --no-ff feature/contact -m "Merge contact page"` · `git log --graph --oneline --all`. Scene 04 plays items 0-6 (`only: [0,1,2,3,4,5,6]`, `speed: 2`) and holds. Marks (on `K.termTimes('save-points', o).items[3]` and `[6]` output): box `[main (root-commit) …] Add homepage` ("save point 1") and `[main …] Add about page` ("save point 2").
**Beats:**
- [[stone]] the pen touches the path at x 300; stone 1 settles (scale .6 → 1); three tiny `K.file` icons shrink into it: "a snapshot of the whole project".
- [[parent]] stone 2 at x 520; back-arrow draws to stone 1; label "records the one before it"; the sight-line walks back along it.
- [[set]] a small `K.icon('lock', …, 28)` seal settles on each stone; label "add new, don't edit old". Card: "'a beautiful design can be understood' · 'In Git, a history is a directed acyclic graph (DAG) of snapshots' · 'Commits in Git are immutable' · MIT Missing Semester 2026, Version Control and Git, 2026-01-16".
- [[ask]] walker bubble "commit my changes with a descriptive message"; the guide bobs 6 px; a dashed stone outline appears at x 740.
- [[habit]] outline fades; card: "'Git with frequent commits before big Agent changes' · Dean Rie, Cursor forum, 2026-08-13 · 'making many Git Commits per thread is best practice' · FinDevAI, 2026-08-15".
- [[real]] map eases left, terminal opens, replay plays; marks land on the two commit lines and the map stones take their real short IDs, each linked to its mark by a gold line.
**Exit:** two stones on `main` with real IDs; terminal at its last prompt.

## 05 — Signposts, and the one with the lantern
**Metaphor object:** the side trail, the signposts, the lantern.
**Frame:** `K.bg()`. Map left, terminal right (continuing); from [[lantern]] the terminal closes and the map returns full width.
**Capture:** `save-points`, items 7-15 at `speed: 2`, final `git log --graph --oneline --all` output held. Marks: box `(HEAD -> main)` ("you are on main") and the `feature/contact` line ("the side trail's signpost").
**Beats:**
- [[fork]] a dashed cream side path curves up-right from stone 2 to y 420; replay types `git switch -c feature/contact`.
- [[signpost]] signpost `feature/contact` plants at the fork; signpost `main` stands by stone 2. Cards: "'References are pointers to commits' · MIT Missing Semester 2026" and "'create a new branch called feature/quickstart' · Anthropic, Claude Code quickstart · read 2026-10-23". As the replay commits, two stones land on the side path and its signpost slides to each (0.5 s `K.io`).
- [[graph]] replay reaches the merge and the log; the side path bends back into `main`, a merge stone appears at x 960, the `main` signpost slides to it; marks on `(HEAD -> main)` and `feature/contact` linked to the matching signposts.
- [[lantern]] terminal closes; a lantern swings onto `main` (the scene's one `'back'`); a dotted line of tiny walker icons follows its road to the right edge, "visitors go here"; terracotta label at the hook "a setting outside the map". Eyebrow "where the picture breaks": "a signpost is only a name".
- [[aaron]] a second side path with signpost `claude/side-branch` appears and a lantern lights on it too; the visitors' line swings to it; static text card "~40 s → live · 8 min 10 s wrong"; source card "Aaron Orelup · AO-043 · 2026-10-09 · a side branch the host deployed"; pointer pill "full story: the lesson on getting from your laptop to a URL". No Cloudflare screens.
- [[lovable]] the extra path and lantern fade; a small card map top-right: one path with signpost "synced branch · Lovable sees this", other branches greyed (text only, no logo); card with the full sentence "Lovable edits and syncs one branch at a time. Commits on other branches don't appear in Lovable until you merge them into the synced branch or switch the synced branch." and a pill "Publish = going live · pushing never publishes" · Lovable, Git sync docs · read 2026-10-23.
**Exit:** `main` with its stones and merge stone, the merged side path, signposts, lantern on `main`.

## 06 — The ranger station: a copy that lives elsewhere
**Metaphor object:** the ranger station and its copy of the map.
**Frame:** `K.bg()`. `K.cam` pans right (+260) to reveal the valley and station. Terminal over the station from [[empty]] to [[ahead]].
**Capture:** `copy-elsewhere`. Commands: `git init -b main` · `echo "notes" > notes.txt` · `git add notes.txt` · `git commit -m "First save point"` · `git remote -v` (prints nothing) · `git init --bare station.git` · `echo station.git >> .git/info/exclude` · `git remote add origin ./station.git` · `git push -u origin main` · `echo "more" >> notes.txt` · `git commit -am "Second save point"` · `git status` · `git remote -v`. All inside the throw-away folder. Marks: the empty result after the first `git remote -v` ("no copy elsewhere"), `Your branch is ahead of 'origin/main' by 1 commit.` ("only on this machine"), the final `origin  ./station.git (push)` ("now there is one"). Card under the window: "a local folder standing in for GitHub".
**Beats:**
- [[station]] the station draws (outline, roof, eyebrow); a dashed copy of the path inside it holds dashed copies of the pushed stones.
- [[notgithub]] labels: over the map "git: stones and signposts, in your folder"; over the station "GitHub: one place to keep a copy". Card "'Git is not GitHub' · MIT Missing Semester 2026".
- [[burn]] a small second map at lower left (x 160-620, y 640-880) with no station; its corner curls and it greys out, its mono `.git` label going with it. Card: "Cursor forum · shuang_yang and replies · 2026-10-03 to 10-05 · step 1: stop writing to the drive · step 2: if it was ever pushed anywhere, clone it back". As "where the copies were" is spoken (`S.find('copies')`), terracotta label "no station, no copy".
- [[empty]] small map clears; terminal opens; replay to the first `git remote -v`; mark "no copy elsewhere".
- [[ahead]] replay through the push, the second commit and `git status`; mark "only on this machine"; on the map the newest stone glows and its place at the station is an empty dashed circle with "?".
- [[cloud]] terminal closes; a `K.icon('cloud')` above the station draws a dashed arrow from the station's copy (not from your map): "with a copy on GitHub, a cloud session clones that copy". Card with S129's sentence · Anthropic, Use Claude Code in the cloud · read 2026-10-23. Pointer pill "the lesson on where your agent works".
- [[breaks]] eyebrow "where the picture breaks" (terracotta); the station's copy turns solid, an equals sign between the two maps: "every copy is full and equal; 'the original' is a choice".
**Exit:** your map and the station's copy, both solid; the unpushed stone still dashed at the station.

## 07 — Footprints: the verb and the target
**Metaphor object:** the guide's footprints.
**Frame:** `K.bg()`. Camera back on the map. Right column (x 1180-1800): a drawn `K.win(…, { kind: 'terminal', title: 'demo session transcript (made up)', titleSize: 26 })`, one row per step, `verb → target`, mono 28.
**Capture:** none (a drawn transcript of a made-up demo session, labelled as such).
**Beats:**
- [[prints]] footprint pairs walk along the path (stagger .15), each stamping softly.
- [[verb]] each print gains a verb pill in turn: `read`, `write`, `delete`, `commit`, `push`, `fetch`; transcript rows type in to match.
- [[target]] each print gains an arrow to a target pill: `index.html`, `main`, `origin`, `example.com`.
- [[ask]] card: "'Is Claude accessing files or websites you didn't mention?' · Anthropic Help Center, Use Claude Cowork safely · updated 2026-10-23"; the sight-line sweeps the prints.
- [[offmap]] one print's arrow bends off the sheet edge; print and pill turn terracotta; a `K.ring` circles it.
- [[examples]] three terracotta prints in turn (on `S.find('push')`, `S.find('public')`, `S.find('remote')`): `push → claude/side-branch` with a tiny lantern (chip "AO-043, 2026-10-09"), `create → public repository` (chip "PixelLeak, 2026-10-02"), `add → new remote` (card "auto mode blocks 'Changing where pushes go with git remote set-url or git remote add, unless you named the new remote' · Choose a permission mode · read 2026-10-23 · this moves monthly").
- [[question]] a walker bubble "Can you change this?" is caught by the guide and turns into an action stamp; card "'I see now that "Can you change this?" is not permission.' · an agent's reply, as a user quoted it · Cursor forum, 2026-08-16".
- [[trail]] the transcript title gains a `K.icon('file')` "transcript (plain text)"; card "'Your git state. Current branch, uncommitted changes, and recent commit history' · Anthropic, How Claude Code works · read 2026-10-23"; pointer pills "the lesson on the agent's folder" · "the lesson on keys" · "the lesson on getting from your laptop to a URL".
**Exit:** prints resting, the off-map one still ringed terracotta.

## 08 — Tracing paper: what changed
**Metaphor object:** tracing paper over yesterday's map.
**Frame:** `K.bg()`. Map left (z .6); a translucent sheet (`K.card`, `K.C.paper`, alpha .25) slides over it. Right: a drawn mock-up of the desktop indicator (labelled "drawn after Anthropic's docs, October 2026"), then the real terminal from [[list]].
**Capture:** `changed-files`. Commands: `git init -b main` · `printf "<h1>Helo</h1>\n" > index.html` · `printf "branch: main\n" > deploy.yml` · `git add .` · `git commit -m "Site as it was"` · `git switch -c fix/typo` · `sed -i "s/Helo/Hello/" index.html` · `echo "branch: fix/typo" >> deploy.yml` · `git commit -am "Fix typo on homepage"` · `git diff --stat main`. Earlier items at `speed: 3`, the last at full speed. Marks: `deploy.yml | 1 +` ("the file you never asked about", terracotta), then `index.html | 2 +-` ("the file you asked about", gold).
**Beats:**
- [[tracing]] the sheet lowers; gold "+" where a stone was added, terracotta "−" where a squiggle was removed.
- [[indicator]] mock-up chip `+12 -1` in a session header; a `K.cursor` clicks it; a two-row file-by-file diff list unfolds (gold additions, terracotta removals). Card: "'After Claude edits files, a +12 -1 indicator appears. Click it to open the diff view, review modifications file by file, and comment on specific lines.' · Anthropic, desktop app quickstart · read 2026-10-23". On "disk" (`S.find('disk')`) a small file icon with a stamp "already on disk".
- [[cloudiff]] second chip `+42 -18` with a pill `Compare against ▾`; card "Claude Code changelog, v2.1.309 (2026-10-22) · the Changes pane now says when it lists only pushed commits or only Claude's edits: read that label first · this moves monthly".
- [[list]] mock-up fades; terminal opens; replay reaches the file list.
- [[stray]] mark on `deploy.yml`; a terracotta square appears on the tracing sheet away from the path; the sight-line jumps to it.
- [[self]] the guide holds a `K.icon('check')` in a small ring over `index.html`: "slash code review: bugs in the code" (card: "'To have Claude review the changes itself, enter /code-review' · desktop app quickstart"); the sight-line stays on `deploy.yml`: "only you: files you never named".
**Exit:** terminal resting with `deploy.yml` boxed; tracing sheet over the map.

## 09 — Evidence is something you read
**Metaphor object:** the guide hands the walker slips from the trail.
**Frame:** `K.bg()`. Tracing sheet lifts away; map left at z .7; evidence slips at right.
**Capture:** none.
**Beats:**
- [[evidence]] the guide hands the walker a slip; three fan out: "test output", "the command + what it returned", "a screenshot" (small `K.win` thumbnails, one mono line each). Card: S117's sentence · Anthropic, Best practices for Claude Code · read 2026-10-23. On "watching" (`S.find('watching')`) the walker fades to .3 while the slips stay: "readable later".
- [[version]] `K.editor` shows `/version.json` with `commit`, `branch: "main"`, `built`, `newest` (placeholder values); a gold arrow from `commit` to the newest stone, a check when they match. Card "Aaron Orelup · AO-043 · 2026-10-09"; pointer pill "the lesson on when the agent says done".
**Exit:** editor and matched stone, check resting.

## 10 — The noticeboard: pushing is a decision
**Metaphor object:** the station's noticeboard by the road.
**Frame:** `K.bg()`. Camera on the station side; a dashed road (`K.C.line2`) at y 840; a square noticeboard `K.card(1480, 560, 260, 200, { r: 4 })`, terracotta stroke.
**Capture:** none.
**Beats:**
- [[push]] the guide carries a stone across the valley on a gold arc; it lands as a copy at the station; label "push".
- [[auto]] an open gate at the valley edge; card "'Pushing to any branch of the repository you're working in, including the default branch' · allowed by default in auto mode · Choose a permission mode · read 2026-10-23 · this moves monthly", footnote "for about a week in July 2026 (v2.1.203 to v2.1.211) auto mode allowed fewer pushes; advice from then is out of date" · versions: Choose a permission mode; dates: Claude Code changelog.
- [[deploy]] a `production` signpost at the station gets a pill "judged on its own" ("isn't covered"); on "protection" (`S.find('protection')`) a `K.icon('shield')` settles on the station door: "the remote's own branch protection still applies".
- [[board]] the noticeboard draws with a copy of the map pinned on it; small passer-by icons walk the road and glance at it.
- [[pixel]] blank screenshot thumbnails flutter onto the board; card "PixelLeak · Glow Labs research 2026-09-29, reported by Hive Security 2026-10-02 · 13,000+ images · 300+ organisations · 93% under personal usernames · the researcher's count, not independently audited"; pill "'creates a public gitshot-images repository'".
- [[known]] a shield shows over the board while a "public" tag hangs on it; the tag becomes "?" and that shield fades: "visibility not established: no block on that alone" (Choose a permission mode), while a second small shield on a "secrets file" tag stays: "files marked sensitive: blocked either way · the repository being private doesn't clear it"; the sight-line lands on the "?": "yours to know".
**Exit:** board with thumbnails and the "?" tag; walker looking at it.

## 11 — Pencil and torn stones
**Metaphor object:** a pencilled stretch; stones torn out.
**Frame:** `K.bg()`. Camera back on the map; right column for cards and the list.
**Capture:** none (a force-push refusal needs a signed-in session).
**Beats:**
- [[pencil]] a grey dashed stretch draws off the newest stone with a small pencil mark; label "pull request: proposed".
- [[ci]] three check pills along it; one turns terracotta, the guide's pen fixes it, it turns gold. Card "'After opening a PR, Claude Code monitors CI check results and can automatically fix failures' · desktop app quickstart · read 2026-10-23".
- [[merge]] a pill toggle "Merge when ready" is flipped by the walker's pointer; only then does the pencil turn to ink. Cards "turns on GitHub's auto-merge for that PR when you switch it on · Use Claude Code Desktop · read 2026-10-23" and "auto mode blocks 'Merging a pull request no human has approved, approving Claude's own pull request, or disabling CI checks'". Pointer pills "the lesson on who signs off before you ship" · "the lesson on checking code you can't read".
- [[tear]] two stones lift out and re-land in a different order; a terracotta mismatch line flashes between your map and the station's copy: "copies disagree". Eyebrow "where the picture breaks: stones can be torn out".
- [[names]] list card "recognise, don't type" (mono 28) in two groups: "rewrites history": `git push --force` · amend after push; "throws away unsaved work": `git reset --hard` · `git checkout -- .` · `git restore .` · `git clean -fd` · `git stash drop` · `git stash clear`; pill "blocked by default in auto mode"; footnote "it runs git status itself before discarding uncommitted work · read 2026-10-23".
- [[revert]] the torn stones settle back; a new stone "↺ revert" is added at the end; card "'Do not force-push, rebase, or squash commits that are already on the synced branch.' · 'To undo a change, add a commit that reverts it.' · Lovable, Git sync docs · a rewrite replaces Lovable's copy; the owner can restore a backup (since 2026-10-05)".
**Exit:** path intact with a revert stone at its end; list resting.

## 12 — The eraser: checkpoints are not git
**Metaphor object:** the guide's pencil eraser.
**Frame:** `K.bg()`. Map centred; a cream rounded-rectangle eraser in the guide's hand.
**Capture:** none (rewind demo dropped: research-now, Checkpointing page nuance).
**Beats:**
- [[eraser]] the guide rubs out a fresh squiggle it just drew.
- [[only]] two marks: "Claude's file edits" (the eraser removes it) and "a file only Bash or another program touched", drawn by a separate hand icon off the sheet (the eraser passes over; it stays). Card with S117's three sentences · Anthropic, Best practices for Claude Code.
- [[remote]] the eraser stops at the valley edge; the station stone, a deployment chip and a `K.icon('server')` database chip stay untouched; card "'Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed' · Anthropic, How Claude Code works".
**Exit:** eraser resting at the valley edge; station copy unchanged.

## 13 — You vs the agent
**Metaphor object:** the finished map: path, stones, signposts, lantern, station, prints.
**Frame:** `K.bg()`. Map at z .5 in the middle band (y 380-700). Columns "THE AGENT" (x 120-860) and "YOU" (x 1060-1800); bottom strip "BRING IN AN EXPERT" (x 120-1800, y 760-900).
**Capture:** none.
**Beats:**
- [[agent]] left column fills: "types every git command", "commits · branches · conflicts · pushes · pull requests · fixes failing checks", "asked: changed files, remote + visibility, default branch"; the guide's pen moves along the path.
- [[you]] right column: "a copy elsewhere exists, private or public as intended", "which branch is default; which one the host deploys", "the changed files"; sight-lines touch the station, the lantern and the tracing square.
- [[decide]] two more rows: "you decide what merges", "evidence, not a claim".
- [[rule]] a "don't push" bubble shields the gate, then fades from its edge: "can be lost when the conversation is compacted"; a `K.icon('lock')` replaces it on the station door: "deny rule · branch protection". Card "stated boundaries block a matching push, but aren't stored as rules · 'For a hard guarantee, add a deny rule.' · Choose a permission mode · read 2026-10-23"; pointer pill "the lesson on rules that actually hold".
- [[expert]] strip fills: "shared history must be rewritten", "a secret or personal data was pushed: revoke + rotate first; deleting the commit does nothing (the lesson on keys)", "can't tell what it touched, real credentials on the machine"; a `K.icon('shield')` at its left.
**Exit:** both columns and the strip resting; the map between them.

## 14 — Keep this
**Metaphor object:** the map folded up, the lantern on top.
**Frame:** `K.plate('plate', t, { zoom: true, shade: .55 })`, no badge. Eyebrow "KEEP THIS" at (960, 200). Three rows (bold lead Karla 34 `K.C.head`, rest Georgia 30 cream, w 1400) at y 300, 450, 600. Credit line y 860 (Karla 26, `K.C.soft`): "Built on Anthropic (Claude Code docs) · Lovable (Git sync docs) · Aaron Orelup (AO-043)". `K.petals` n 5 avoiding the rows.
**Capture:** none.
**Beats:**
- [[keep1]] row 1 **Save points and the agent's trail.** "Commits are save points, branches are names on them, a remote is the copy elsewhere; you know which branch is live." Stone + signpost + lantern glyph.
- [[keep2]] row 2 **Read each step for the verb and the target.** "Ask about anything aimed at something you never named." Footprint glyph.
- [[keep3]] row 3 **Look at the changed files, then ask for evidence.** "Find the file you never asked about; have it show what it ran and what came back." Tracing-square glyph.
- [[credits]] the credit line fades in; the folded map settles under it.
**Exit:** three rows and the credit line resting; petals drift.
