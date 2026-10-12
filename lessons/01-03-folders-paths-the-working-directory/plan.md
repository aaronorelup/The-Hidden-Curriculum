# Plan: 01.03 Folders, paths & the working directory

Module 01 Your Computer, Under the Hood · District 1 The Machine · mid-module, so ~10 minutes (1190–1610 words; target ~1375 words, ~575 s at about 140 words per minute). No [guest] sections (lesson is under 15 minutes).

## 1. Purpose line and conclusion

- First spoken sentence (purpose): "In this lesson you'll learn how a path points to a file, and why the same name can point somewhere different depending on where a program was started."
- One-sentence conclusion (title card, with the purpose line): "A path is an address, and a relative path only makes sense from the working directory of the program that reads it."

## 2. As of

As of October 2026 (research dated 2026-10-08). The subject itself is stable; the agent section is the part that changes, and it is dated.

## 3. Change arc

- Five years ago (2021): the person at the keyboard typed every command and was the only one who ever ran `cd`. No mainstream terminal coding agent existed. A working-directory mistake was yours alone.
- Now (2026): coding agents run commands from a working directory they inherit. Claude Code launched as a terminal beta in February 2025 (on native Windows it ran only through WSL at launch). Codex CLI launched 2025-04-16. Claude Code on the web arrived October 2025, and its sandboxing was announced about 2025-10-20. Claude Code's additional-directory rules, worktrees (EnterWorktree, new this year, now asks approval before entering a path outside `.claude/worktrees/`) and sub-agent isolation are current.
- Where it is heading: speculation only. Agents will likely keep resolving paths for you. The lesson's line is "agents resolve paths for you; you still need to know which folder the agent is standing in and whether it is the project you think."
- The path model itself did not change. The Windows path rules are the same as they were in 2021 (the 260-character default was already opt-in). Do not present any of that as new.

## 4. MUST-COVER list (grouped by scene, in script order)

Depth key: TEACH = a full beat with a picture; BRIEF = one or two sentences; LINE = one spoken clause or one on-screen label.

Scene 01 · The point (~35 s, ~85 words)
- Purpose line and conclusion (TEACH, the sentence is mandatory).

Scene 02 · Where it lives (~20 s, ~45 words)
- District 1 The Machine, pin on module 01 ("what's on your computer"). Module 01 is the module about what is on your computer and how it is laid out. LINE: the path is what you type to say where a thing is.

Scene 03 · The mental model (~40 s, ~95 words)
- Metaphor: directions from where you're standing, with a you-are-here dot (TEACH). The dot is the working directory; the map is the disk.

Scene 04 · Absolute paths: the full address (~58 s, ~140 words)
- Absolute path starts from the root of the disk (TEACH). Microsoft's own wording: a full path starts from a drive or a root.
- Drive form C:\ on Windows versus / on macOS and Linux (TEACH, concept only; see section 8 for the check still owed).
- Separators: backslash and forward slash. Windows APIs and PowerShell accept both; the separator is a naming convention and the OS decides what the name means (BRIEF).

Scene 05 · Relative paths and the working directory (~69 s, ~165 words)
- Every running program has a working directory, set when it starts and inherited from whatever started it (TEACH, core idea).
- A relative path is measured from that directory, not from the file that contains it, and not from the disk root (TEACH).
- The prompt shows the folder: PowerShell's default prompt `PS C:\Users\you\project>` (BRIEF). The prompt is the dot on the map.

Scene 06 · The same name, two places (~50 s, ~120 words)
- "Works on my machine" explained: the same relative name, run from two folders, finds two different files or none (TEACH, the anti-confusion payoff).
- Example in words only: a script opens `data.csv` by its bare name; run from the project folder it works, run from another folder it fails. The code did not change; the dot moved.

Scene 07 · Shortcuts, and where the picture breaks (~48 s, ~115 words)
- `~` home folder (LINE/BRIEF; concept only: the shell expands `~` to the home folder, on Windows typically C:\Users\name).
- `.` current folder and `..` parent folder (LINE; concept only, no command lists).
- Where the metaphor breaks: real places do not move when you walk away, but a working directory is a stored value per running program, and a child program gets its own copy (TEACH; this is where understanding lives).

Scene 08 · What is really going on (~40 s, ~95 words)
- A `cd` changes only the session that ran it. A child process does not move its parent (TEACH).
- Claude Code specifics belong in scene 10; here, only the general rule.
- Python keeps a second search list for imports that follows different rules (LINE; "that is 05.02's story").

Scene 09 · The surprises you'll hit (~75 s, ~180 words)
Each of these is a line the viewer will see; show it on screen, one at a time.
- `No such file or directory` (macOS, Linux and Git Bash style; BRIEF).
- `FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'` (Python; the name is right, the place is wrong; TEACH).
- PowerShell "Cannot find path ... because it does not exist" (BRIEF; exact wording must be checked, see section 8).
- Claude Code's tool result line `Shell cwd was reset to <dir>` (BRIEF; the folder went back to the project after a `cd` left the allowed area).
- Git Bash spelling: `C:\Users\you` appears as `/c/Users/you`, the same place in another spelling (BRIEF).

Scene 10 · The lantern: agents and the folder they stand in (~65 s, ~155 words)
- Five years ago the person typed `cd`. Now the agent does (TEACH, the change arc in one breath).
- Claude Code: a `cd` in the main session carries over to later commands only while the new folder stays inside the project or an added directory. Outside that, the shell resets to the project folder and the result says so (BRIEF, current docs).
- Subagents never carry a `cd` over (BRIEF).
- Sandbox: on macOS, Linux and WSL2, the sandbox lets commands write in the working directory and blocks writes outside it. Native Windows runs commands without that sandbox per the current docs (BRIEF; this matters for a Windows reader; verify before script, see section 8).
- Worktrees: a second folder for the same project, on its own branch, sharing one history (LINE; the detail is 08.11).
- Some users report the folder resetting between every command. This is a reported issue, not a confirmed rule (LINE, hedged; or cut if it crowds the scene).
- Closing line of the lantern: agents resolve paths for you, but you still need to know which folder the agent is in and whether it is the project you think (TEACH; the recurring lantern line).

Scene 11 · Safe to ignore for now (~29 s, ~70 words)
- Windows 260-character path default and the registry-plus-manifest opt-in (LINE; the detail is 01.08).
- Forward slashes generally work on Windows (LINE).
- WSL shows C: as `/mnt/c` (LINE).
- Python's `-P` and `PYTHONSAFEPATH` (LINE; the detail is 05.02).

Scene 12 · What it connects to (~25 s, ~60 words)
- 01.04 hidden files (`.git`, `.venv`, dotfiles are just paths with a dot in front).
- 01.05 PATH (how a bare name like `python` is found, a different lookup from a relative path).
- 02.03 moving around (`cd`, `ls`, the prompt).
- 05.02 running a file (interpreters and imports depend on the working directory).
- 08.11 agents on git (worktrees).

Scene 13 · Keep this (~21 s, ~50 words), three bold-lead takeaways on the end card
- **A path is an address.** Absolute starts at the root; relative starts where the program stands.
- **Every program has a working directory.** It is inherited from whatever started the program, and a `cd` moves only the session that ran it.
- **The same name can mean a different file.** When something is not found, check the folder the program is in, and with an agent check which project it is in.

Budget check: seconds 35+20+40+58+69+50+48+40+75+65+29+25+21 = 575 s. Word target 1375 (range 1190–1610).

## 5. DEFERRED (introduced here only; owned elsewhere)

- Hidden files, dotfiles, `.git`, `.venv`, `AppData`, `~/.config` → 01.04
- PATH, "not recognized as a command", bare-name lookup (including the cmd.exe current-folder search that `NoDefaultCurrentDirectoryInExePath` controls; the research says this is cmd-specific) → 01.05
- Windows vs macOS vs Linux details: case sensitivity, slash conventions in practice, MAX_PATH 260 and the opt-in → 01.08
- Terminal, console, shell distinctions; cmd, PowerShell, bash, zsh, Git Bash, WSL → 02.01 and 02.02
- `cd`, `ls`/`dir`, `pwd`, tab completion as commands → 02.03
- Reading errors in depth → 02.08
- Python imports, `sys.path`, the script's folder vs `-m`/`-c`, `-P` and `PYTHONSAFEPATH` (3.11) → 05.02
- Virtual environments → 05.03
- How coding agents read, edit and run in the editor and terminal → 03.08
- Instruction files (CLAUDE.md) that are read from the project folder → 03.09
- Sandboxes, permission prompts, scoped access for agents → 14.12
- Git worktrees and branches, agents on git → 08.11 (branches in 08.03)
- Sub-agent orchestration → 07.07
- MCP roots (deprecated as of protocol version 2026-07-28; roots are informational, not an access control) → 10.08 (MCP); not taught here
- Codex sandbox history (CVE-2025-59532) and the older read-only-until-trusted docs → 14.12 (security framing), not taught here
- Dangerous files and double extensions → 15.17 (already introduced in 01.01 and 01.02)
- Environment variables set per session → 01.05

No NEW lesson needed for this topic set. Every deferred topic has an existing curriculum row.

## 6. Mental model

One metaphor for the whole lesson: **directions from where you're standing, with a you-are-here dot.**

- The disk is the map. The root (C:\ or /) is the edge of it.
- An absolute path is a full street address, counted from the root.
- A relative path is "three streets from here": it only means something from the dot.
- The working directory is the dot. Every program starts with a dot placed by whoever started it. A `cd` moves the dot for that one session.
- Transform for the lantern: the dot moves to the agent's own copy of the map. The question stays the same: where is the dot, and is it on the project I think it is on?

Where it breaks (say so plainly in scene 07):
- Real people carry their own dot; in a computer the dot is a stored value per running program, and a child program gets a copy, not a shared pointer.
- A relative path is not measured from the file that contains it. Most tools measure it from the working directory of the process.
- Python's import search is a second list with its own rules. The metaphor does not cover imports; say so and send the viewer to 05.02.
- `..` at the top of the disk has nowhere further to go. Do not extend the metaphor past that.

## 7. Cut list (tempting, stays out)

- Step-by-step `cd`, `ls`, `pwd` command lists: how-to, belongs in 02.03. COURSE.md forbids step-by-step.
- Shell version history and PowerShell versions (7.4, 7.5, 7.6, support dates, the 5.1 vs 7.x coexistence): unverified support dates and owned by 02.02. The 7.6 LTS date is from one vendor post and one non-Microsoft source.
- zsh becoming the macOS default since Catalina (2019): interesting, owned by 02.02, not needed here.
- Windows 10 end of support (2025-10-14) and ESU: not about paths; cut.
- Dev Drive and the "up to 30%" build-I/O claim: vendor scenario claim, and the lesson does not need it.
- Anthropic's "cut permission prompts by 84%" figure: company-reported and not verified. Do not use.
- Cursor agent terminal opening the wrong workspace folder: a reported bug with an unconfirmed fix; the general rule ("check the folder") already covers it. Cut the vendor name.
- Cursor multi-root workspaces and the Cursor CLI add-dir changelog: third-party aggregator sources, unverified. Cut.
- MCP roots (deprecated 2026-07-28): spec detail for 10.08.
- Codex CVE-2025-59532 and the old "read-only until trusted" docs: security history for 14.12 and 15.15; they would take a minute away from the core model.
- Scheduled tasks and cron and their "start in" folder: a real surprise for later lessons, but nothing in the research sources it. Owned by 16.02 if it is ever sourced.
- The Python `-m` / `-c` history (bpo-33053, GH-6231, the docs disagreement issue42483): verify on python.org before any use; too deep for this lesson.
- Windows `\\?\` long-path prefix and the 32,767-character figure: approximate and not needed.
- The Notepad story: already told in 00.03 and 01.02. Do not repeat it here.
- Any new "Aaron" anecdote. None fits this lesson.

## 8. Facts to handle carefully (hedged wording)

1. Claude Code `cd` rule. Say: "In the current docs, a `cd` in the main session carries over only while the new folder stays inside the project or an added directory." Do not say "always" or "never".
2. Subagents. Say: "Subagents don't carry a `cd` over." Source: current docs. Fine to state as current.
3. Resets between calls. Say: "Some people have reported the folder resetting between commands. That is a reported issue, not a rule." Never state it as a confirmed behaviour.
4. Sandbox platforms. Say: "Claude Code's sandbox runs on macOS, Linux and WSL2, according to the docs read this month." Check once before scripting; the research marks it as established from the current sandboxing page.
5. Native Windows and sandbox. Say: "Native Windows runs commands without that sandbox, so on Windows the folder rule is the one that matters." Hedge with "per the current docs". Do not present it as permanent.
6. Worktrees. Say: "A worktree is a second folder for the same project, on its own branch, sharing one history." Established.
7. Agents resolving paths. Say: "Agents can resolve paths for you when they know the folder. You still need to know which folder they are in." The "agents will keep resolving paths for you" line is speculation and must be marked as a guess if said at all.
8. Python. Say: "The rules for the import list depend on how Python starts: a script's folder for `python script.py`, the current folder for `-m` and `-c`. Python 3.11 added `-P` and `PYTHONSAFEPATH`." Do not say "imports always come from the current folder". Detail to 05.02.
9. Windows path length. Say: "Windows paths have a 260-character default that apps must opt into lifting." Not "Windows paths are limited to 260". The lift needs both the system setting and the app's manifest.
10. Forward slashes. Say: "Windows generally accepts forward slashes too." Long-standing; not re-fetched this month, so keep it light.
11. Git Bash `/c/`. Say: "Git Bash shows C:\ as /c/." Established in secondary sources only; hedge with "in Git Bash".
12. WSL `/mnt/c`. Say: "WSL reaches the Windows drives under /mnt/c." Long-standing; not re-fetched.
13. The `~` shorthand. Say: "The shell expands `~` to your home folder." Do not promise that a quoted `"~/x"` will expand; some tools do not expand it.
14. PowerShell error text. The line "Cannot find path ... because it does not exist" is the usual wording for file cmdlets. Before scripting, confirm the exact text by running it in PowerShell, or show it as "something like" and do not put a quote in as exact.
15. Claude Code's reset text. The quoted line `Shell cwd was reset to <dir>` is from the current tools docs. Show it as written.

Gaps still owed before scripting (planner's note):
- The equivalence of `C:\` and `/` as "two spellings of a root": the research marked it unsourced. The safe version: "Windows drives start at a drive letter; macOS and Linux start at one root." Get one source before the line is scripted, or use the Microsoft wording: a full path starts from a drive or a root.
- The `~` home folder on Windows: the research marks it unsourced. Keep it to the concept; say "typically C:\Users\name" only as "usually".

## 9. Spelling for the ear (per COURSE.md)

`C:\` → "C colon backslash" · `PS C:\` → "P S C colon backslash" · `cd` → "C D" · `ls` → "L S" · `.venv` → "dot V E N V" · `.git` → "dot G I T" · `.py` → "dot P Y" · `CSV` → "see-S-V" · `API` → "A P I" · `CLI` → "C L I" · `WSL` → "W S L" on second mention (first mention: Windows Subsystem for Linux) · `/c/` → "slash C slash" · `/mnt/c` → "slash mount slash C" · `..` → "dot dot" · `.` → "dot" · `~` → "tilde" · `sys.path` → "sys dot path" · `PYTHONSAFEPATH` → "P Y T H O N safe path" · `Errno` → "err-no".
