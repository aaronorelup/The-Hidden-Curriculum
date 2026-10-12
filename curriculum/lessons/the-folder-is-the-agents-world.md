---
key: the-folder-is-the-agents-world
id: 01.01
title: The folder is the agent's world
district: First Build
module: 01 Your workbench
status: legacy
legacy: [01-03-folders-paths-the-working-directory, 01-04-hidden-files-dotfiles]
minutes: 6
concepts: [C123]
sources: [S206, S208, S211, S176, S160, S123, S052, S101, S061, S069, S175, S210, S129, S207]
lead: [S208, S211]
---

# The folder is the agent's world

**Purpose (the first spoken sentence):** In this lesson you'll learn why the folder you open an agent in becomes its whole world, and why that world is not a wall.

**Conclusion:** Every agent session stands in the folder you chose, which decides where it starts, which rules it reads and what it may touch without asking, but the folder is not a wall: your keys and AI logins sit in your home folder, hidden files are only out of sight, and a copy on the same drive is not a backup.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; module 01 Your workbench (first lesson of the module and of the district: the first thing every surface asks you for is a folder).

**Lead source (audit, 2026-10-12):** S208 (Anthropic (Claude Code docs)); S211 (Aaron Orelup (drafted by Claude from his transcripts)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S206, S208, S211, S176); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length note:** the course bible sets about 5 minutes for the first lesson of a module. This spec asks for 6 because it merges two published 10-minute lessons (01.03 and 01.04) and is the prerequisite for C046, C079, C089, C090, C097, C098 and C103. If Aaron holds the 5-minute rule, cut point 2 and point 7 to one sentence each and drop the trust half of point 3.

## What to teach (binding scope)

Rough time budget: points 1-2 1 min · point 3 1 min · point 4 1 min · point 5 1 min · point 6 1 min · points 7-9 1 min. Order: what the folder is (1-3), why it is not a wall (4-6), the habit (7-9). Recognition only: the agent types every path and command, so no `cd`, `..` or separator syntax to memorise.

### C123 The folder you open is the agent's world, and not a wall

1. **Every session starts by choosing a folder.** In the terminal the quickstart's first step is `cd /path/to/your/project` then `claude`, and "The Claude Code prompt appears with the version, current model, and working directory shown above it" (S206). In the desktop app you "Select **Local** to run Claude on your machine using your files directly. Click **Select folder** and choose your project directory" (S208). A path is an address; the working directory is where the session stands. This was Aaron's own first gap: in May 2025 he "could not `cd` into a directory", didn't know "where files go", or that "a file one directory over is a different file to Python" (S211, published 2026-08-08); AO-029 says he didn't know he had to open a terminal and change into the folder first (S210). (S206, S208, S211, S210) — **teach**
2. **That folder is the agent's default reach.** "By default, Claude has access to files in the directory where you launched it", extended only with `--add-dir`, `/add-dir` or settings; reads inside need no approval, edits follow the permission mode (S160). Claude Code's own list: "Files in your directory and subdirectories, plus files elsewhere with your permission" (S101). Other tools work the same way: Cursor staff, after a wiped drive, "Cursor limits commands to the folder it's opened in by default", and opening the project folder means "the Agent's scope is limited to that project instead of the whole disk" (S175, 2026-08-29). In the Claude desktop app, the Chat tab has "no file access", the Code tab "direct access to your local files" (S208); 01.02 owns the surfaces. (S160, S101, S175, S208) — **brief**
3. **Rules and trust climb upward.** Claude Code "loads `CLAUDE.md` and `CLAUDE.local.md` from your current working directory and every directory above it. Run Claude Code in `foo/bar/` and it loads instructions from `foo/bar/CLAUDE.md`, `foo/CLAUDE.md`"; files in subfolders load only when the agent works there (S123). Trust works the same direction: outside a git repository, trusting the folder you started in "covers any subdirectory of that directory" (S160). So a rules file one folder above your project shapes every session you start below it. Which files load in which sessions is 05.02; trust as a security decision is 07.04. (S123, S160) — **teach** (the direction and one example only)
4. **It is not a wall.** The agent's terminal runs "Any command you could run ... If you can do it from the command line, Claude can too" (S101). In auto mode (the starting mode for terminal and VS Code sessions since Claude Code v2.1.283), file reads outside the working folders run without a prompt except that "The first time Claude uses the Read, Grep, or Glob tool on a path outside them, Claude Code asks whether to allow that read", with an option to block such reads from then on (S052). And one wrong path is enough: a Cursor agent asked to delete one folder ran `rmdir /s /q` with broken quoting, the target collapsed to the D: drive root, about 80 GB went with no confirmation (S175). Permission modes and delete guards are 02.01; sandboxes are 07.02. (S101, S052, S175) — **teach**
5. **Your home folder is where the valuable things are.** The ChainDrop npm worm (StepSecurity, 2026-08-04) scanned about 140 paths, nearly all in the home folder: SSH keys and configs, `~/.aws/`, `~/.npmrc`, `~/.git-credentials`, shell histories, and AI tool credentials by name: `.claude/credentials.json`, `.claude.json`, `.codex/auth.json`, `.cursor/credentials.json`, `.gemini/.env` (S061). Claude Code itself treats your home directory as special: it never lets a rule approve `rm` on it (S052), and trust given there is "for the current session only" and never written to disk (S160). (S061, S052, S160) — **teach**
6. **Hidden is not locked: dotfiles hold history, instructions and secrets.** Name them, don't teach them:
   - `.git` is the project's history; Claude Code treats it as a protected directory because a bad write corrupts "repository state" (S052).
   - `.claude` and `CLAUDE.md` hold the agent's instructions and settings, and Claude Code also protects `.vscode`, `.mcp.json` and shell startup files such as `.zshrc` from unapproved writes, because they decide what runs (S052, S123).
   - The agent's own history: "Each message, tool use, and result is written to a plaintext JSONL file under `~/.claude/projects/`" (S101), and its notes about you sit in `~/.claude/projects/<project>/memory/` (S123).
   - `.env` files usually hold settings and secrets; when Claude Code uploads a local repository to a cloud session it treats them as files "named like credentials or keys" and leaves their uncommitted changes behind on macOS, Linux and WSL (S129; one line here, 01.02 owns the upload). What `.env` is and why it is a convention, not a vault, is 03.02.
   - Out of sight means only that: the stealer in point 5 read these files by name (S061). (S052, S123, S101, S061) — **teach** (names and what each holds; 15 seconds each at most)
7. **The tools mark the dangerous places, and so should you.** Claude Code's critical paths are "the filesystem root, your home directory, and your working directory" and its parents: no allow rule or hook can approve `rm` or `rmdir` on them. Its protected paths (`.git`, `.claude`, `.vscode`, `.mcp.json`, shell startup files) are never auto-approved for writes (S052). Say that this is one vendor's list (Claude Code, read 2026-10-12) and that other tools differ. (S052) — **one line**
8. **"Elsewhere" means another disk or another place.** On 2026-10-03 a Cursor user approved the agent's own cleanup plan ("Okay, follow the recommendation and delete them"); the command used a wrong path, and `rmdir /s /q`, which skips the Recycle Bin, removed the source, the `.git` folder, the published build, a `_file_backup` folder and a manual backup in the root of the same E: drive. The first question the user asked was whether the files could be recovered from the SSD. A reply the next day: keep a backup "that the agent's shell can't reach at all", on another disk or in versioned cloud storage (S176). Git with no remote dies the same way (01.03); undo limits are 03.03. (S176) — **teach**
9. **The habit: open the agent on one project folder.** Not a whole drive (point 4 already showed why), and not your home folder: Claude Code won't even keep trust there beyond one session (S160), and Anthropic's Cowork advice is to "Consider creating a dedicated working folder for Claude rather than granting broad access" and to avoid "local files with sensitive information, like financial documents" (S069). (S160, S069) — **teach** (the closing takeaway). The D: drive quote was cut by the 2026-10-12 audit so each incident is told once: the E: drive wipe (point 8) is told in full only here, and before-you-let-it-loose opens on a different wipe and calls back to this one in a line.

**Dropped from C123 for this lesson:** the full CLAUDE.md loading rules (subfolders, compaction, cloud sessions) → 05.02 (C046); what a sandbox leaves readable in `~/.ssh` → 07.02 (C079); `.git/config` that runs a program and workspace trust prompts → 07.04 (C089, C090); `.env` and environment variables → 03.02 (C126); file extensions, renaming `.txt` to `.py`, file associations → not taught (C123's outdated framings; backlog item "Files, bytes and file types").

## You vs the agent

As of 2026-10-12:

- **The agent** resolves every path, moves around inside the folder, reads and writes files, and can list and explain the hidden files it finds. Asked, it lists which instruction files it loaded (`/context`, S123) and whether it has read anything outside the folder. In Claude Code it refuses `rm` on critical paths, asks before writes to protected paths, and asks on its first file-tool read outside the working folders (S052).
- **You** choose which folder it opens (one project; never a whole drive or your home folder), answer the "read outside the folder" and trust prompts on purpose rather than by reflex, know which hidden files hold instructions and secrets, and keep at least one copy of the work on another disk or in versioned cloud storage the agent's shell can't reach (S175, S176, S160, S052, S069).
- **Bring in an expert** (C118) if anything you did not trust may have read your home folder, for example a package that ran install scripts on a machine holding real credentials. ChainDrop shows why this is not a do-it-yourself job: it watches for the stolen GitHub token to be revoked and then runs an attacker's handler, so the monitor has to be removed before credentials are rotated (S061). Treat it as a possible compromise; the response order is 07.04 (C088) and 03.02 (C071).

## Sources this lesson is built from

- S206 — Anthropic (Claude Code docs), "Quickstart" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/quickstart — `cd` into the project before starting; the working directory shown above the prompt.
- S208 — Anthropic (Claude Code docs), "Get started with the desktop app" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/desktop-quickstart — Local plus "Select folder" as the first step; Chat has no file access, Code has direct access to local files.
- S211 — Aaron Orelup, "AO-007: No VS Code, no terminal, no idea" (2026-08-08, describes May 2025) https://aaronorelup.com/ledger/no-vs-code-no-terminal/ — the course's own learner: "a file one directory over is a different file to Python", "I could not `cd` into a directory".
- S210 — Aaron Orelup, "AO-029: I asked where I was supposed to learn all this. Two hours later, 44 agents had made the first lesson." (2026-10-01) https://aaronorelup.com/ledger/the-missing-map/ — not knowing to open a terminal and change into the folder first, with an Information Systems degree.
- S176 — shuang_yang, replies by ActionGate and sattyamjjain, "Errible: AI out of control, randomly deleting files, 6-month project wiped out" (Cursor forum, 2026-10-03, replies to 2026-10-05) https://forum.cursor.com/t/173688 — source, `.git` and both backups on the one drive the command wiped; "a backup that the agent's shell can't reach at all".
- S175 — Mr.Cheng, staff replies by Dean Rie (Cursor), "Agent wiped D: drive instead of deleting one folder" (Cursor forum, 2026-08-29) https://forum.cursor.com/t/169919 — one bad path reached the whole drive; staff: open the project folder to limit the agent's scope.
- S160 — Anthropic (Claude Code docs), "Configure permissions" (undated live docs; mentions up to v2.1.292; read 2026-10-12) https://code.claude.com/docs/en/permissions — default access is the launch folder; trust keyed on the repo root or the start folder and its subfolders; home-folder trust lasts one session.
- S123 — Anthropic (Claude Code docs), "How Claude remembers your project" (undated; mentions versions up to v2.1.285, 2026-09-29) https://code.claude.com/docs/en/memory — CLAUDE.md loads from the working directory and every directory above it; where auto memory is stored.
- S052 — Anthropic (Claude Code docs), "Choose a permission mode" (undated live docs; v2.1.283+, mentions v2.1.292; read 2026-10-12) https://code.claude.com/docs/en/permission-modes — critical paths (root, home, working directory and parents), protected paths (`.git`, `.claude`, `.vscode`, `.mcp.json`, shell startup files), the first-read-outside prompt.
- S101 — Anthropic (Claude Code docs), "How Claude Code works" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — what the agent can access ("Any command you could run"); transcripts as plaintext JSONL under `~/.claude/projects/`.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — the home-folder paths a 2026 stealer reads, AI-tool login files by name.
- S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — a dedicated working folder rather than broad access; keep sensitive files such as financial documents out.
- S129 — Anthropic (Claude Code docs), "Use Claude Code in the cloud" (undated live docs; mentions up to v2.1.289; read 2026-10-12) https://code.claude.com/docs/en/claude-code-on-the-web — `.env` treated as a file "named like credentials or keys" (one line; 01.02's source).
- S207 — Anthropic (Claude Code docs), "Terminal guide for new users" (undated live docs; example output shows v2.1.211; read 2026-10-12) https://code.claude.com/docs/en/terminal-guide — beginners are told they can skip the terminal, which is why path syntax is not taught here.

## Show it for real

- The Claude desktop app's Code tab: choose Local, click Select folder, pick a small demo project (S208). Proves the folder is the first decision, before any prompt.
- The same demo project in a terminal: `cd` into it, start `claude`, zoom on the working directory shown above the prompt (S206). Proves the terminal makes the same choice.
- Put a `CLAUDE.md` in a parent demo folder and another in the project, start the session, run `/context` and show both under Memory files (S123). Proves rules climb upward.
- In auto mode, ask the agent to read a file outside the demo folder and record the first-read prompt with its four answers (S052). Proves the folder is not a wall, and where the one built-in speed bump is.
- Turn on "show hidden items" in Explorer or Finder on the demo project: `.git`, `.claude`, `CLAUDE.local.md` and a `.env` with obvious fake values. Proves hidden is a display choice.
- Open `~/.claude/projects/` and show a demo session's `.jsonl` transcript scrolling past (a session created for the recording, nothing private). Proves the agent's history is a plain file in your home folder (S101).
- Animated diagram of S176's E: drive: source, `.git`, `publish`, `_file_backup` and the manual backup on one disk, one command, all gone; a second disk beside it untouched. Built from the forum post's own list.
- Animated card of ChainDrop's AI-tool credential paths (S061), as path names only, no file contents.

## Questions this lesson answers

- "Can the deleted files be recovered from the SSD?" (the S176 author's first follow-up, posted four minutes after the report, 2026-10-03). The lesson's answer is to plan as if not: keep a copy the agent's shell can't reach.
- "What is the `.claude` folder in this repo and should I care?" (listed in concepts.md under C089 and C123).
- "Which folder should I open the agent in?", "Is it OK to open my whole drive?" (derived from S175, S206 and S208; not yet seen in a beginner post).
- "Why can't the program find a file that is right there?" (derived from S211; Aaron's own May 2025 gap).
- "Does the agent only see the folder I opened?" (derived from S101, S052 and S160).
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Surfaces, where a session runs, and what a cloud session can reach through connected folders → where-your-agent-works
- Git, the remote copy, and why git with no remote dies with the folder → save-points-and-the-agents-trail
- Permission modes, delete guards and a copy off the machine → before-you-let-it-loose
- `.env`, environment variables and where secrets live → keys-public-secret-and-leaked
- Rollback and undo limits → from-your-laptop-to-a-url
- Which instruction files load, when and in which sessions → rules-it-reads-rules-it-cant-break
- What a sandbox covers and leaves readable (`~/.ssh`) → contain-it-dont-babysit-it
- Keeping credentials out of where the agent runs → the-narrowest-keys-and-verbs
- Workspace trust, `.git/config` and repos that ship their own hooks and agents → other-peoples-code

## Out-of-date framings to avoid

- "Learn `cd`, `ls`, relative paths, `..` and separators first." The agent resolves paths and types the commands (S206, S207); the legacy 01.03 spent most of its time here.
- "Rename `.txt` to `.py`" and file extensions as the gap. That gap came from the copy-from-chat workflow of May 2025 (S211); agents now write files directly ("Claude Code reads your project files as needed", S206). C123 marks it outdated.
- "The agent can only touch the folder I opened" (S101, S052, S175).
- "Hidden files are private" or "locked" (S061).
- "A backup folder inside my project, or on the same drive, is a backup" (S176).
- "Opening my whole drive or home folder just lets it see more" (S175, S160, S069).
- "Telling the agent not to read my `.env` protects it." A request in prose is not a control (01.04 said "never let an agent read it"; enforcement is 05.02 and 07.03).

## Legacy notes

Covered for now by 01.03 "Folders, paths & the working directory" (published 2026-10-08, about 10.6 minutes) and 01.04 "Hidden files & dotfiles" (published 2026-10-09, about 10.5 minutes). The rebuild merges them into one short lesson.

- **What they get right.** 01.03: a path is an address; the working directory as a "you-are-here dot"; the agent carries its own dot; "with an agent, check which project it's in too"; native Windows has no Claude Code sandbox (still true: S052 lists the Bash sandbox on macOS, Linux and WSL2). 01.04: "hidden only means out of sight, never locked"; two back rooms, the project's and your home folder's; instruction files and MCP config as dotfiles; Claude Code reads AGENTS.md when there is no CLAUDE.md (still true per S123); "after an agent works, check what changed, hidden files included". The you-are-here dot and the back room are both good metaphor candidates; pick one.
- **What is missing.** The folder as the agent's default reach and its limits (S160, S101, S052); rules and trust climbing upward (S123, S160); the home folder as where AI logins and keys sit, named by a 2026 stealer (S061); critical and protected paths (S052); same-drive backups (S176, October 2026); the desktop app's Select folder step (S208); transcripts and memory in `~/.claude/projects/` (S101, S123).
- **What is outdated.** Both point to the retired map ("District One, The Machine") and to retired lesson numbers (01.05, 01.07, 02.03, 05.02, 05.03, 08.07, 08.11, 10.09, 14.12, 15.07). 01.03 spends most of its time on typing paths by hand (relative paths, separators, `FileNotFoundError`, Python's `-P` and `PYTHONSAFEPATH`), which the agent now handles, and repeats a hedged "Shell cwd was reset" report. 01.04's Windows Hidden attribute versus the dot, AppData's three rooms and `.DS_Store` are below recognition level for this course now; its incident roll-call (2025) belongs to 07.04, and its `.env` rules to 03.02.
