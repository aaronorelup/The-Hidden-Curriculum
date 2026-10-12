# Plan: 01.04 Hidden files & dotfiles

Module 01 Your Computer, Under the Hood · District 1 The Machine · mid-module, so ~10 minutes (1190–1610 words; target ~1435 words, ~610 s at about 140 words per minute). 15 sections. No [guest] sections (lesson is under 15 minutes).

Binding inputs: research-now.md and research-change.md (both checked 2026-10-09), COURSE.md, curriculum.md.

## 1. Purpose line and conclusion

- First spoken sentence (purpose): "In this lesson you'll learn about the hidden layer of files on your computer, what lives in it, and why you need to know it is there."
- One-sentence conclusion (title card, with the purpose line): "Every project and every app keeps its settings, history, secrets and now its AI instructions in files your computer hides by default, and hidden only means out of sight, never locked."
- Why care (second or third sentence of scene 01): your secrets live in that layer, and AI agents read and write it, so it is the layer you check when something changed that you did not see.

## 2. As of

As of October 2026 (research dated 2026-10-09). The hiding rules are decades old and unchanged; the AI-tool layer and the security picture are the parts that change, and every one of those claims is dated.

## 3. Change arc (required: the lesson touches AI and security)

- Durable core (did not change): a leading dot hides a name on Unix and macOS by convention only (an accident of early Unix `ls`); Windows hides by a file attribute and ignores the dot; `AppData` has held per-user app settings since Vista (2007); `~/.config` comes from the XDG spec (spec still at version 0.8, 2021). Hiding never protected anything.
- About five years ago (2021): the hidden layer of a project was `.git`, `.gitignore`, `.env`, `.vscode/`, `.idea/`, `.github/`. It was passive data that tools read; the worst common mistake was committing a `.env`. Folder names for Python environments varied (`venv`, `env`, `.venv`). GitHub push protection did not exist yet (pilot April 2022, GA May 2023).
- What changed, with dates:
  - Python 3.13 (October 2024) `venv` writes a `.gitignore` inside every new environment; uv also defaults to `.venv` and ignores it. `.venv` is now the de facto name.
  - GitHub push protection on by default for public repos since 2024-02-29 (catches recognised secret patterns only; can be bypassed).
  - A whole new AI-tool layer appeared in 2024–2025: MCP (Anthropic, 2024-11-25) and its config files; VS Code agent mode with `.vscode/mcp.json` (March 2025); Claude Code (preview 2025-02-24, GA 2025-05-22) with `CLAUDE.md`, `.claude/`, `.mcp.json`, `~/.claude/`, `~/.claude.json`; Cursor moved from `.cursorrules` to `.cursor/rules/`; `AGENTS.md` (August 2025); Agent Skills (`SKILL.md`, October 2025).
  - Hidden config files became instructions and commands that agents act on, and so an attack surface: Rules File Backdoor (March 2025), Cursor CurXecute and MCPoison (July–August 2025), Claude Code project-file flaws (`.claude/settings.json` hooks, `.mcp.json`, CVE-2025-59536, CVE-2026-21852; patched, published 2026-02-25).
  - Malware went straight for the hidden layer: s1ngularity/Nx (2025-08-26) ran victims' own AI command-line tools to hunt for secrets; the Shai-Hulud npm worms (September and November 2025) swept machines for tokens and keys.
  - Leak volume grew: GitGuardian's 2026 report counted 28.65 million new hardcoded secrets on public GitHub in 2025 (+34%), AI-service secrets up 81% (vendor figures).
- Now (October 2026): a typical AI-built project carries several instruction files and MCP configs, one set per tool, plus agents that write their own notes (Claude Code auto memory, 2026). Claude Code reads `AGENTS.md` when there is no `CLAUDE.md` (since v2.1.277, 2026-09-18). Agent transcripts can store anything the agent read, including a `.env`.
- Where it is heading (hedged): instruction files converging on `AGENTS.md` and tool wiring on MCP under the Linux Foundation's Agentic AI Foundation (formed 2025-12-09), while each vendor keeps its own folder; agents getting built-in "protected paths" they will not write to; secrets slowly moving out of plain-text `.env` (1Password's virtual `.env`, public beta since 2025-10-29; encrypted `.env` tools). Plain `.env` is still the default everywhere; do not predict its end.

## 4. MUST-COVER list (grouped by scene, in script order)

Depth key: TEACH = a full beat with a picture; BRIEF = one or two sentences; LINE = one spoken clause or one on-screen label.

Scene 01 · The point (~35 s, ~85 words)
- Purpose line and conclusion (TEACH; the sentence is mandatory and comes first).
- Why care: secrets live here, and agents read and write here (BRIEF).

Scene 02 · Where it lives (~18 s, ~42 words)
- District 1 The Machine, pin on module 01 ("what's on your computer"). LINE: the last lesson gave every file an address; this one shows the addresses your computer leaves off the tour. (Continuity with 01.03's map and dot.)

Scene 03 · The mental model (~40 s, ~95 words)
- Metaphor: the back room behind the shop, with a "staff only" sign (TEACH). The porter from 01.02 (the file manager) gives the tour of the shop floor and walks past the back-room door. Your documents are on the shop floor; the settings, history and supplies that keep the shop running are in the back room.

Scene 04 · Why it is hidden: an accident, and two different signs (~55 s, ~130 words)
- Unix and macOS: a name starting with a dot is skipped in listings. It began as a shortcut in early Unix `ls` meant to hide `.` and `..`; programmers then put config files behind a dot, and a convention was born. Rob Pike later called it a mistake (TEACH; hedge the details, see section 8).
- Windows: no dot rule. Hiding is a switch on the file itself, the Hidden attribute (TEACH). So a `.env` or `.claude` folder is plain to see in Windows Explorer unless something sets the switch. Git for Windows sets it on `.git` only (BRIEF).
- How you see it, named only, screen labels not steps: Explorer View > Show > Hidden items; Finder Command-Shift-Period; `ls -a` / `Get-ChildItem -Force` (LINE; the "Advanced (formerly For developers)" Settings page was already shown in 01.02, so at most a screen label).

Scene 05 · Two kinds of back room: the project's and yours (~45 s, ~105 words)
- Per-project: dot-folders and dot-files inside the project folder travel with the project (TEACH).
- Per-user, in your home folder: `~/.config` (the tidy XDG answer, followed by some tools), plenty of top-level dot-folders that ignore it (`.ssh`, `.gitconfig`, `.npmrc`, `.claude`, `.codex`), and on Windows `AppData` with Roaming (follows a work login between machines), Local (this machine only) and LocalLow (sandboxed programs such as browsers) (TEACH for the split, BRIEF for the three AppData folders).
- Real example, hedged as an observation: on the Windows machine this course is made on, the home folder held 46 dot-named items on 2026-10-09 (LINE, optional).

Scene 06 · What is in the project's back room (~50 s, ~120 words)
- `.git`: the project's entire history and git's settings live in one hidden folder. Delete it and the files stay, the history is gone (TEACH).
- `.venv`: a whole private copy of Python and the project's packages, hiding in the project. Aaron, who made this course, didn't know what dot V E N V was (true story from COURSE.md; do not embellish). Since Python 3.13 (October 2024) and in uv, a new `.venv` tells git to ignore itself (BRIEF).
- `.gitignore`: a visible-but-dotted list of what git must never pack up (BRIEF; it hides nothing from you, the OS or an agent).
- `.vscode/` and similar editor settings folders (LINE).

Scene 07 · `.env`: the secrets drawer with no lock (~65 s, ~155 words)
- Convention: `KEY=value` lines at the project root, loaded into environment variables when the program starts (TEACH; environment variables themselves are 01.05). Node reads `.env` natively now; Python still uses a library (LINE, optional).
- Plain text. Hidden means out of sight, not encrypted, not protected (TEACH).
- Judgment rule 1: `.env` is never committed. It belongs in `.gitignore` before the first commit; adding it afterwards does not remove it from history, and the only fix for a leaked key is replacing it (rotating) (TEACH; mechanics are 08.07 and 15.11).
- Judgment rule 2: never paste it into a chat or let an agent print it. With agent tools, whatever the agent reads can be written into its transcript, which is another hidden folder (Claude Code docs: transcripts in `~/.claude/projects/`, not encrypted) (BRIEF).
- GitHub push protection catches some known key patterns on public repos and can be bypassed; it is a net, not a plan (LINE).

Scene 08 · Where the picture breaks (~25 s, ~60 words)
- A real "staff only" sign is a rule people respect. A hidden file's sign is only a display choice: every program, every script, every agent and every piece of malware walks straight in (TEACH; this is the core understanding).
- Real protection is file permissions, encryption or a secrets manager, other lessons (LINE: 01.07, 15.07).

Scene 09 · The lantern: the AI-tool back room (~60 s, ~140 words)
- Instruction files: `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, `.github/copilot-instructions.md`, `GEMINI.md`. Notes pinned on the back-room wall that new staff read before starting work (TEACH; depth belongs to 03.09).
- Tool-wiring files (MCP configs): `.mcp.json`, `.cursor/mcp.json`, `.vscode/mcp.json`, `claude_desktop_config.json` inside `AppData` on Windows. They say which tools the agent may plug into (BRIEF; MCP is 10.08 and 10.09).
- Per-user AI folders: `~/.claude/`, `~/.claude.json`, `~/.codex/`, `~/.cursor/` (LINE). Skills, agents and auto memory (notes Claude writes about you itself) live there too (LINE).
- Convergence, hedged: tools now read each other's files (Copilot reads `CLAUDE.md`; Claude Code reads `AGENTS.md` when there is no `CLAUDE.md`), and `AGENTS.md` and MCP sit under the Linux Foundation since December 2025 (BRIEF).

Scene 10 · Then and now: from notes to orders (~55 s, ~130 words)
- The change arc in one scene: in 2021 hidden config was passive notes; since 2025 some of these files are orders an agent follows or commands it runs (TEACH).
- Evidence, two or three named incidents only: hooks in a repo's `.claude/settings.json` and auto-approved `.mcp.json` servers could run code when an untrusted repo was opened (fixed; published February 2026); an approved Cursor `mcp.json` could be swapped silently (2025); invisible characters hidden in rules files (March 2025) (BRIEF).
- Malware targets the layer: the August 2025 s1ngularity attack used victims' own AI tools to search their disks for secrets (BRIEF). GitGuardian: AI-service key leaks up about 80% in 2025 (LINE, vendor figure).

Scene 11 · Your job: check the back room (~45 s, ~105 words)
- The learner's judgment role (TEACH): when an agent finishes, look at what changed, including hidden files. `git status` and `git diff` show changes to dot-files like any other (LINE; git is 08.02).
- Review a change to `.claude/`, `.mcp.json`, `AGENTS.md` or a rules file like a change to code (BRIEF).
- A polite note ("don't read .env") in an instruction file is not a lock; tools offer real deny rules and sandboxes, and some agents now refuse to write their own settings files (protected paths) (BRIEF; details are 14.12).
- Heading, hedged: secrets moving out of plain `.env` into secret managers (LINE, beta).

Scene 12 · The surprises you'll hit (~55 s, ~130 words). Show each on screen, one at a time.
- "My project has no `.git`", yet git works: it is hidden (Explorer, Finder) (BRIEF).
- On Windows, `.env`, `.claude` and `.ssh` are right there in Explorer, while `.git` is not (BRIEF).
- You added `.env` to `.gitignore` and it is still on GitHub: it was already committed (BRIEF).
- A push rejected because it "contains a secret" (push protection) (LINE; exact message must be checked, see section 8).
- A path with `AppData\Roaming` in it, in a guide for a desktop AI app's config (LINE).
- `.DS_Store` files appearing in Mac projects and commits (LINE).
- Leftover dot-folders from tools you stopped using, e.g. `.gemini` after Gemini CLI's consumer service ended in June 2026 (LINE, optional).

Scene 13 · Safe to ignore for now (~20 s, ~45 words)
- The XDG variables beyond `.config` (`.local/share`, `.cache`, `.local/state`), what LocalLow is for in detail, the macOS hidden flag on `~/Library`, settings-precedence chains between user and project files, "dotfiles repos" for syncing config across machines (all LINE).

Scene 14 · What it connects to (~20 s, ~45 words)
- 01.05 environment variables (what `.env` fills), 05.03 virtual environments, 08.07 `.gitignore` and secrets, 03.09 instruction files, 10.09 MCP config files, 15.07 keeping secrets out of plain text (LINE each, as map pins).

Scene 15 · Keep this (~22 s, ~50 words), three bold-lead takeaways on the end card
- **Hidden means out of sight, not locked.** A dot on Mac and Linux, a switch on Windows; anything can still read it.
- **Your secrets live in the hidden layer.** `.env` is plain text: never commit it, never paste it, replace a key that leaked.
- **Agents read and write this layer.** After an agent works, check what changed, hidden files included.

Budget check: seconds 35+18+40+55+45+50+65+25+60+55+45+55+20+20+22 = 610 s (~10.2 min). Words 85+42+95+130+105+120+155+60+140+130+105+130+45+45+50 = 1437 (range 1190–1610). Fifteen sections (range 11–17).

Spoken forms (COURSE.md rules plus these): `.env` "dot E N V"; `.venv` "dot V E N V" (never "vee-env"; keep the two clearly apart, ideally not in the same sentence); `.git` "dot git"; `.gitignore` "dot git ignore"; `AppData` "App Data"; `~/.config` "the dot config folder in your home folder"; `CLAUDE.md` "Claude dot M D"; `AGENTS.md` "agents dot M D"; `.mcp.json` "dot M C P dot Jason"; `MCP` "M C P"; `ls -a` on screen only.

## 5. DEFERRED (introduced here only; owned elsewhere)

- Environment variables, what `.env` loads into, PATH → 01.05
- File permissions as real protection, admin vs standard → 01.07
- Windows vs macOS vs Linux naming and hiding differences in depth, `.DS_Store` → 01.08
- Shells and listing commands (`ls -a`, `dir /a`, `Get-ChildItem -Force`) → 02.02, 02.03
- Coding agents in the editor and terminal → 03.08
- Instruction files (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, Copilot instructions) as prompts-as-code → 03.09
- Config file formats (JSON, TOML, YAML) → 04.06
- Hidden Unicode characters in text → 04.07 (mechanism), 15.15 (attack)
- Python versions and uv → 05.01, 05.04
- Virtual environments (`.venv`) in depth → 05.03
- Node and npm (`.npmrc`, `node --env-file`) → 05.05
- Supply-chain malware (s1ngularity, Shai-Hulud, install scripts) → 05.08
- How AI apps remember; Claude Code auto memory → 06.07
- What a repo is; `git status` and `git diff` → 08.01, 08.02
- `.gitignore` and never committing secrets (mechanics, history rewriting) → 08.07
- Agents on branches and worktrees; reviewing agent changes in git → 08.11
- MCP itself → 10.08; MCP config files and installing servers → 10.09
- Skills, plugins and marketplaces (`.claude/skills/`) → 10.10, 10.12
- API keys, which keys may be public → 14.03
- SSH keys (`~/.ssh`) → 14.06
- Giving agents keys safely: deny rules, sandboxes, protected paths, permission prompts → 14.12
- Moving secrets out of plain text (1Password Environments, dotenvx, credential stores, `op run`) → 15.07
- User vs system environment variables → 15.08
- Credential Manager and DPAPI → 15.09
- When a key leaks: rotate, revoke, push protection, secret scanning → 15.11
- AI privacy and what transcripts retain → 15.13
- Enterprise-managed settings files → 15.14
- Prompt injection through files; Rules File Backdoor; the Claude Code and Cursor config CVEs → 15.15
- Leftover `AppData` after uninstalling → 17.08

No NEW lesson needed. Every deferred topic has an existing curriculum row. (Syncing your config across machines with a "dotfiles repo" has no owner, but it is cut, not introduced; see section 7.)

## 6. Mental model

One metaphor for the whole lesson: **the back room behind the shop, with a "staff only" sign.** It continues 01.02's porter (the file manager) and 01.03's map.

- (03) The shop floor is what Explorer or Finder shows you: your documents and code. The porter gives the tour and walks past a door marked "staff only". Behind it: the things that keep the shop running.
- (04) Two kinds of sign. On Mac and Linux the sign is painted into the name (the dot). On Windows it is a little flag hung on the door (the Hidden attribute), and Windows ignores painted dots, so some doors with dots stand open.
- (05) Two back rooms: one behind each shop (the project's dot-folders) and one in your own house (home folder: `.config`, top-level dot-folders, `AppData` with its three rooms).
- (06) Inside the project back room: the ledger of every past version (`.git`), the shop's private toolbox and supplies (`.venv`), the list of what never goes on the moving van (`.gitignore`).
- (07) A drawer of keys with no lock (`.env`). The sign on the door is the only protection.
- (08) Break: see below.
- (09) New staff arrive carrying lanterns (the course's AI motif): the agents. Notes are pinned to the back-room wall for them (`CLAUDE.md`, `AGENTS.md`), and a wiring board shows which tools they may plug into (MCP configs). They keep their own notebooks in your house's back room (`~/.claude/`).
- (10) Transform: the pinned notes stop being notes and become orders the staff follow; a stranger's note pinned to the wall (a cloned repo, a malicious package) gets obeyed too.
- (11) You, the owner, walk in after the staff leave and check the logbook of what moved (`git diff`), including on the back-room wall.
- (15) End card: the door, ajar, with the sign.

Where it breaks (say it plainly in scene 08):
- A real "staff only" sign is a social rule people obey. The dot or the Hidden flag is only a display choice; every program, script, agent and piece of malware walks straight through. There is no door, really; just a tour that skips it.
- The back room is not one place: it is scattered across every project and your home folder, and each tool picks its own corner (only some follow `~/.config`).
- `.gitignore` is not a lock either: it only tells git what not to pack. It hides nothing from you, the OS or an agent, and it cannot unpack something already shipped.

## 7. Cut list (tempting, stays out)

- Step-by-step instructions to show hidden files on each OS, or commands to create a `.env`: how-to; COURSE.md forbids step lists. Screen labels at most.
- The Windows Settings "Advanced (formerly For developers)" page history: already shown in 01.02; repeating it wastes time.
- The full Claude Code file map (`settings.local.json`, `.claude/rules/`, `agents/`, `commands/`, `workflows/`, `agent-memory/`, `.worktreeinclude`, settings precedence, `CLAUDE_CONFIG_DIR`, `claude purge`): too deep for one lesson; vendor detail that changes monthly. Owned by 03.09 and 10.10.
- Every CVE number and fix date: name two or three incidents in plain words; numbers go on screen at most, depth in 15.15.
- GitGuardian's full statistics (3.2% vs 1.5% Claude Code co-authored leak rate, 24,008 secrets in MCP configs, internal repos 6x, 64% unrevoked): vendor figures, easy to misread; the 3.2% figure could read as an attack on one tool without context. At most one figure (AI-service leaks up about 80%), attributed.
- Shai-Hulud counts (25,000 developers, 294,842 secret occurrences): the numbers vary by source; one named incident (s1ngularity) carries the point.
- 1Password named-pipe mechanics and dotenvx key handling: beta or niche; one hedged line, depth in 15.07.
- `node --env-file` and `process.loadEnvFile()` version history: one optional clause at most; owned by 05.05.
- PEP 668 "externally-managed-environment": real but belongs to 05.03.
- uv's centralized-envs preview: preview feature, not needed.
- The `.gitignore` Explorer naming papercut (`.gitignore.` trailing dot): current Windows 11 behaviour not confirmed in research; do not claim either way.
- macOS `chflags hidden`: unsourced in this pass.
- Plan 9's `$HOME/lib`: trivia.
- `.cursorignore` and `.geminiignore` details: one sentence on "a polite note is not a lock" covers it; `.geminiignore` details unconfirmed.
- AGENTS.md adoption numbers (60,000+, ~96,600): counting method unclear; use "widely adopted" or nothing.
- Dotfiles repos and settings sync across machines: a nice power-user topic with no owner in the curriculum and no research behind it; at most a "safe to ignore" line.
- Any new Aaron anecdote. Only the true `.venv` line from COURSE.md fits; the Notepad and `.txt` story is already told in 00.01, 00.03 and 01.02 and should not be retold.
- Teasers for the next lesson (COURSE.md voice rule): scene 14 names neighbours on the map, no "next time".

## 8. Facts to handle carefully (with the hedged wording to use)

- Origin of dotfiles. Pike's recollection, details disputed (TUHS thread). Say: "As Rob Pike, one of the early Unix programmers, tells it, hiding dot files began as a shortcut in the list command, meant to hide two special entries. It hid every name that starts with a dot, and people started putting settings there." Do not give a year, or the name of the person who wrote the shortcut.
- Git for Windows hides only `.git` by default (`core.hideDotFiles = dotGitOnly`). Established, but sourced from a 2016-era commit. Say: "Git for Windows sets the switch on its own dot git folder." Not "every tool does this".
- AppData hidden by default: established in practice; no Microsoft page found stating it this pass. Say: "App Data is hidden by default" only with "on a normal Windows install"; avoid citing Microsoft.
- Roaming "follows you between machines": true for domain or work accounts with roaming profiles, not for a home PC. Say: "Roaming is meant to follow a work login from machine to machine."
- The 46 dot-named items: direct observation on Aaron's Windows machine, 2026-10-09. Say: "On the Windows machine this course is made on, the home folder held forty-six of them." Do not generalise to "every PC".
- Python 3.13 `venv` self-ignore and uv's `.venv` default: established. Say: "Since Python 3.13, and in the tool uv, a new dot V E N V tells git to ignore itself." Older Python and other tools do not.
- Node native `.env`: added in 20.6 (2023); stable status reported for v24.10 and v22.21 from a docs mirror and a secondary source. If used, say only: "Node can now read a dot E N V file by itself." No version numbers spoken.
- GitHub push protection: on by default for public-repo pushes since 2024-02-29; recognised patterns only; bypassable; repository-level for private repos needs a paid product. Say: "GitHub now blocks some known kinds of key from reaching public repositories, but only the kinds it recognises, and you can override it." The exact rejection text has NOT been researched: put a generic screen label ("push declined: secret detected"), not a quoted message, unless verified against GitHub docs before scripting.
- Claude Code transcripts storing secrets: current docs say values a tool reads are written to `~/.claude/projects/<project>/<session>.jsonl`, not encrypted at rest. Say: "Claude Code's own documentation says that anything a tool reads, a key included, ends up in a transcript file in another hidden folder."
- Claude Code reading `AGENTS.md`: from v2.1.277 (2026-09-18), only when no `CLAUDE.md` or `CLAUDE.local.md` exists. Say: "Since September, Claude Code reads agents dot M D when a project has no Claude dot M D." New this month-ish; mark new.
- Copilot reading `CLAUDE.md` and `GEMINI.md`: Copilot coding agent, since 2025-08-28. Say: "GitHub's Copilot coding agent reads Claude dot M D too." Not "all of Copilot".
- Agentic AI Foundation: formed 2025-12-09 with MCP, AGENTS.md and goose. Say: "Since December 2025, both agents dot M D and M C P belong to a Linux Foundation group." Convergence beyond that is speculation: "Tools are drifting toward shared file names; each still keeps its own folder."
- Claude Code project-file flaws: three issues, all patched before publication (2026-02-25). Say: "Researchers showed that a repository's own Claude settings could run commands or leak a key when someone opened it. Those holes were fixed, but the lesson stuck: these files are code." Do not imply they are open now.
- Cursor MCPoison and CurXecute: fixed (1.3, 2025-07-29). Say "in 2025" and "fixed".
- Rules File Backdoor (March 2025): research demonstration by Pillar Security, not a documented mass attack. Say: "Researchers hid invisible instructions in a rules file."
- s1ngularity / Nx (2025-08-26): established; counts vary. Say: "In August 2025 a poisoned package ran its victims' own AI command-line tools to search their disks for keys." No victim counts.
- GitGuardian 2026 figures: vendor report. Say: "GitGuardian, a company that scans for leaked keys, counted AI-service keys leaking about eighty percent more in 2025 than the year before." Always attribute.
- Protected paths: Claude Code's sandbox refuses writes to its own settings, `.mcp.json`, `.git/config` and hooks; Codex makes `.git` and `.codex` read-only. The sandbox is off by default and not on native Windows. Say: "Some agents now refuse to rewrite their own settings files." No claim that it protects a Windows user by default.
- Deny rules are not airtight: single unverified user reports say shell commands can bypass them; Cursor staff confirmed `.cursorignore` does not stop terminal or MCP tools (2026-02-18). Say: "A note asking the agent not to read your keys is a request, not a lock." Do not claim Claude Code's deny rules are broken.
- 1Password Environments virtual `.env`: public beta since 2025-10-29, Mac and Linux only. Say: "Some password managers are testing a fake dot E N V that never touches the disk." Mark beta.
- Gemini CLI: consumer service ended 2026-06-18; replaced by Antigravity CLI. If used, say: "a dot gemini folder can be a leftover from a tool Google has since replaced." Optional; drop if it crowds scene 12.
- Microsoft's new Settings > System > Advanced page: rollout per build not confirmed; do not use (01.02 already covers it).
