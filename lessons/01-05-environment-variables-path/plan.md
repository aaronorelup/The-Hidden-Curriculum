# Plan: 01.05 Environment variables & PATH

Module 01 Your Computer, Under the Hood · District 1 The Machine · mid-module, so ~10 minutes (1190–1610 words; target ~1,500 words, ~635 s at about 140 words per minute). 16 sections (range 11–17). No [guest] sections (lesson is under 15 minutes).

Binding inputs: research-now.md and research-change.md (both checked 2026-10-10), COURSE.md, curriculum.md. Continuity: 01.03 (the you-are-here dot; a child program gets a copy of it) and 01.04 (the back room; `.env` already taught as a plain-text drawer of keys that "loads into environment variables", with the never-commit and never-paste rules). This lesson finishes that sentence; it does not re-teach `.gitignore`.

## 1. Purpose line and conclusion

- First spoken sentence (purpose): "In this lesson you'll learn how your computer finds the right program when you type a name like python, and about the hidden settings every program carries with it."
- One-sentence conclusion (title card, with the purpose line): "Every program starts with a copy of its parent's settings, called its environment; one of them, PATH, is an ordered list of folders where the first match wins, so which program runs, and which keys it can see, depends on who started it and when."
- Why care (second or third sentence of scene 01): "not recognized as a command", the wrong Python, and an AI tool billing the wrong account are all this one idea; and the agents that now set up your machine work inside it.

## 2. As of

As of October 2026 (research dated 2026-10-10). The mechanism (inherit a copy; search PATH in order) is decades old and unchanged. What changed is who edits the environment (installers and now agents), how Python lands on Windows, and how much is at stake when keys sit in it. Every changing claim is dated.

## 3. Change arc (required: the lesson touches AI and security)

- Durable core (did not change): a process gets a copy of its parent's environment when it starts and never sees later changes; PATH is an ordered list of folders, searched left to right, first match wins; "not recognized" / "command not found" means no folder on the list holds that name; activating a virtual environment just puts its folder first on PATH for that one shell; an environment variable is plain text any child process can read.
- About five years ago (2021): you installed Python from python.org and ticked "Add python.exe to PATH"; the Windows Store `python` stub already existed (May 2019); after an install you closed the whole terminal window; you activated a virtual environment by hand in every terminal; `.env` files were read by a dotenv library; putting API keys in environment variables was the textbook advice (Twelve-Factor, 2011), and the only programs reading your environment were the ones you started yourself.
- What changed, with dates:
  - Windows Terminal became the default console on Windows 11 (October 2022), and since Terminal 1.18 (May 2023) a new tab reloads the environment, so "close everything" became "open a new tab". Already-open tabs, editors and agents started earlier are still stale.
  - Python on Windows: the Python install manager (PEP 773, accepted 2025) became the recommended route with Python 3.14 (October 2025); the classic installer with the PATH checkbox is deprecated and will not be produced from Python 3.16. The official `python` and `py` commands are now themselves App Execution Aliases.
  - Tools that skip activation: `uv run` (2024 onward); uv 0.8 (July 2025) puts versioned Pythons on PATH; VS Code's Python Environments extension took over terminal activation (July–August 2025).
  - Runtimes read `.env` themselves: Node's `--env-file`, stable in v24.10 / v22.21 (October 2025); Bun loads `.env` automatically.
  - Coding agents (2025 onward) run your commands as their own child processes, so they inherit every variable in the terminal you launched them from, keys included.
  - Attackers went for the environment: s1ngularity (2025-08-26) stole `.env` files and tokens and drove victims' own AI command-line tools to hunt for more; the Shai-Hulud npm worm (September, second wave November 2025) harvested environment variables such as `GITHUB_TOKEN` and `NPM_TOKEN`; CISA told developers to rotate all credentials (2025-09-23).
  - Response: npm revoked all classic tokens (2025-12-09) in favour of two-hour session tokens and trusted publishing; GitGuardian (vendor) counted AI-service secret leaks up 81% in 2025.
- Now (October 2026): agents install tools, create virtual environments and write `.env` files for you. Vendors have started fencing what an agent's child processes inherit: Claude Code has opt-in credential scrubbing for its commands and MCP servers (new this year); Codex has an environment policy whose automatic KEY/SECRET/TOKEN filter is off by default in current docs; GitHub's Copilot cloud agent gets its own "Agents" secrets as environment variables. A forgotten `ANTHROPIC_API_KEY` in your environment makes Claude Code bill that key instead of your subscription.
- Where it is heading (hedged): keys injected for one command or swapped in by a proxy instead of sitting in every process's environment; short-lived, scoped keys per agent; agent defaults likely to keep tightening. Plain environment variables and `.env` are still the default everywhere: do not predict their end.

## 4. MUST-COVER list (grouped by scene, in script order)

Depth key: TEACH = a full beat with a picture; BRIEF = one or two sentences; LINE = one spoken clause or one on-screen label.

Scene 01 · The point (~35 s, ~85 words)
- Purpose line and conclusion (TEACH; the purpose sentence is mandatory and comes first).
- Why care: three symptoms you will meet (not recognized, the wrong Python, the wrong account billed) are one idea; agents now work inside it (BRIEF).

Scene 02 · Where it lives (~18 s, ~42 words)
- District 1 The Machine, pin on module 01 ("what's on your computer"). LINE: the last two lessons showed where files live and the back room; this one shows what every running program carries out the door. (Continuity with the map dot from 01.03.)

Scene 03 · The mental model: the satchel copied at the door (~40 s, ~95 words)
- Every program is sent out by another program (its parent: Explorer, a terminal, an editor, an agent) with a satchel of named settings, copied from the parent's satchel at the moment it leaves (TEACH).
- After it leaves, nothing at home reaches it, and nothing it changes comes back (TEACH; this is the key to scenes 08, 09 and 11).
- Callback, LINE: the you-are-here dot from 01.03 travels the same way, as a copy.

Scene 04 · What is in the satchel (~35 s, ~82 words)
- An environment variable is a name and a text value (TEACH, with three harmless examples on screen: `USERPROFILE` / `HOME`, `TEMP`, `PATH`).
- Where the starting copy comes from: on Windows two stored layers, user and system, that new programs combine; on Mac and Linux the shell's startup files (`.zshrc`) (BRIEF; depth is 15.08).
- How to peek, screen labels only: `echo $PATH`, `$env:PATH`, the Environment Variables dialog (LINE).

Scene 05 · PATH: the ordered list of streets (~55 s, ~130 words)
- PATH is one variable: a list of folders, separated by semicolons on Windows and colons on Mac and Linux (TEACH).
- Typing a bare name: the shell walks the list left to right and runs the first file with that name; first match wins, everything later is never looked at (TEACH; the core picture).
- Windows also tries the extensions it counts as programs, so `python` finds `python.exe` (LINE; `PATHEXT` on screen only).
- On Windows the system list comes first, then the user list, so a system copy beats a user copy of the same name (BRIEF; hedged, see section 8).
- Shells check a few things before PATH (built-ins, aliases; cmd even checks the current folder first, PowerShell deliberately does not) (LINE; depth is 02.02).

Scene 06 · "Not recognized as a command" (~40 s, ~95 words)
- Meaning: no folder on the list held that name (TEACH).
- Four causes: not installed; installed but its folder is not on PATH; on PATH but this terminal is older than the change; a typo (BRIEF).
- The wordings, on screen one at a time (LINE each): cmd `'python' is not recognized as an internal or external command...`; PowerShell `The term 'python' is not recognized as the name of a cmdlet...`; bash / zsh `command not found`.

Scene 07 · Which python actually ran? (~60 s, ~140 words)
- Many copies of the same name can sit on the list: an installer's Python, conda, uv, the Store stub. The shell takes the first (TEACH).
- Real observation (TEACH, the scene's picture): on the Windows machine this course is made on, typing python had three candidates in order: a Python 3.10 install, the Microsoft Store stub, and a Miniconda Python. The first won, and 3.10 reached end of life this month. Nobody chose that; the order did.
- The Store stub: Windows puts a fake `python.exe` on PATH that opens the Microsoft Store when no Python is installed. "Found on PATH" does not mean "installed" (BRIEF). Its message on screen: "Python was not found; run without arguments to install from the Microsoft Store..." (LINE).
- Since Python 3.14 the official Python commands on Windows are themselves such aliases, via the Python install manager; the classic installer with the PATH checkbox is on its way out (BRIEF; depth 05.01).
- Asking which one wins: `which -a python`, `where python`, `Get-Command python -All`; or ask Python itself where it lives (`sys.executable`) (LINE; screen labels).

Scene 08 · Virtual environments: a street pinned to the top (~40 s, ~95 words)
- Activating a `.venv` puts its folder first on PATH for that one shell, so `python` now means the project's Python (TEACH; ".venv" spoken "dot V E N V").
- Only that shell and its children; another terminal, or an agent's separate shell, is not in it (BRIEF).
- Newer tools skip activation: `uv run` picks the project's environment directly, for that one command. (Fact-check 2026-10-10: the install manager's `python` uses only an already-ACTIVE venv via VIRTUAL_ENV; it does not skip activation.) (LINE; depth 05.03, 05.04).

Scene 09 · Why you need a new terminal after an install (~45 s, ~105 words)
- The installer writes the stored PATH at home; the terminal you had open left with the old satchel (TEACH; the satchel picture does all the work).
- What changed: since 2023 a new tab in Windows Terminal picks up the new settings; a tab that was already open does not (BRIEF).
- A terminal inside an editor inherits from the editor, so the editor usually needs a restart too (BRIEF).
- Same for agents: Claude Code reads the environment when it starts, so an agent launched before an install does not see it until restarted (BRIEF).
- WinGet still does not refresh the open terminal (LINE, optional).

Scene 10 · Where the picture breaks (~25 s, ~60 words)
- A satchel can be sealed; an environment cannot. Any program, script or agent you start can read every value in it (TEACH; sets up scene 11).
- The list is not always pointing at real shops: some entries are stand-ins (the Store alias, version-manager "shims") that forward you elsewhere, so "which" can name a signpost, not the program (BRIEF).
- There is no single "the environment": every running program has its own copy (LINE).

Scene 11 · Keys in the satchel (~55 s, ~130 words)
- Why keys live here: AI SDKs and tools look for a named variable by default (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`), so the key stays out of the code (TEACH).
- `.env` from 01.04 is how the key usually gets into the satchel: the program, a library, or the runtime itself (Node, Bun) loads the file at start (BRIEF; callback, no re-teaching of the git rules).
- Inheritance cuts both ways: a key in your terminal is copied to every program you start from it, including an agent and every command and package the agent runs (TEACH).
- Billing surprise: with `ANTHROPIC_API_KEY` set, Claude Code uses that key instead of your subscription, even when you are logged in (BRIEF; `/status` shows which on screen, LINE).

Scene 12 · The lantern: agents work in your environment (~50 s, ~118 words)
- Five years ago only your own programs opened the satchel. Now agents install tools, edit PATH, create environments and write `.env` files for you, and run their commands as children of themselves (TEACH).
- Attackers noticed: in August 2025 a poisoned package stole `.env` files and steered victims' own AI command-line tools to search for keys; the Shai-Hulud worm that autumn harvested tokens from environment variables (BRIEF; no victim counts).
- Responses, dated: npm revoked long-lived publish tokens in December 2025; agent tools began offering ways to strip keys from what their commands inherit, mostly opt-in (BRIEF).
- Heading, hedged: keys handed over for one command, or swapped in by a proxy, rather than sitting in every satchel (LINE).

Scene 13 · Your job: two questions to verify (~35 s, ~82 words)
- Which program actually ran? Ask the shell, or ask the agent to show you (BRIEF; screen: `where python`, `which -a python`).
- Where do my keys live, and who can see them? Which file, which variable, which terminal the agent was started from, which account pays (BRIEF).
- A polite rule telling an agent not to read `.env` is not a fence; real fences are sandboxes and scrubbing, owned by 14.12 (LINE).

Scene 14 · The surprises you'll hit (~50 s, ~118 words). Show each on screen, one at a time.
- You install something and the same terminal still says "not recognized": open a new one (BRIEF).
- `python` opens the Microsoft Store: that is the alias stub winning (BRIEF).
- `python` and `py` can start different Pythons (LINE).
- On a Mac, `python` is not found but `python3` is (LINE); on Apple Silicon, `command not found: brew` until Homebrew's folder is added to PATH (LINE).
- `pip install` worked but the import fails: the package went to a different Python than the one that ran (LINE; depth 05.03).
- An agent's `export` or activation "didn't stick": each of its commands may start a fresh shell (LINE).
- A program sees a key you never set: a runtime loaded a `.env`, or a key was exported earlier in that terminal (LINE, optional).

Scene 15 · Safe to ignore, and the neighbours (~30 s, ~70 words)
- Safe to ignore for now (LINE each): editing the registry by hand, `PATHEXT` and command-precedence rules, version-manager shims, the PowerToys environment editor and profiles, `setx` and its limits.
- Neighbours as map pins (LINE each): 02.02 shells, 05.01 many Pythons, 05.03 virtual environments, 14.12 giving agents keys safely, 15.07 keeping secrets out of plain text, 15.08 user vs system variables. No "next time".

Scene 16 · Keep this (~22 s, ~50 words), three bold-lead takeaways on the end card
- **Every program carries a copy of its parent's environment.** Changes at home reach only programs started afterwards: open a new terminal.
- **PATH is an ordered list, and the first match wins.** To know which program ran, ask the shell.
- **Keys in the environment go wherever you send programs.** Agents included: know where yours live and who can read them.

Budget check: seconds 35+18+40+35+55+40+60+40+45+25+55+50+35+50+30+22 = 635 s (~10.6 min). Words 85+42+95+82+130+95+140+95+105+60+130+118+82+118+70+50 = 1,497 (range 1190–1610). Sixteen sections (range 11–17).

Spoken forms (COURSE.md rules plus these): PATH "path" (screen shows `PATH` in capitals); `.env` "dot E N V"; `.venv` "dot V E N V" (never "vee-env"; keep `.env` and `.venv` out of the same sentence); `where.exe` "where"; `Get-Command` "Get Command"; `which` "which"; `py` "the P Y command"; `uv` "U V"; `ANTHROPIC_API_KEY` "the Anthropic A P I key variable"; `OPENAI_API_KEY` "the Open A I key variable"; `PATHEXT` screen only; `%LOCALAPPDATA%` "Local App Data"; `npm` "N P M"; `CLI` "C L I"; `.zshrc` "the Z shell startup file" (screen shows the name).

## 5. DEFERRED (introduced here only; owned elsewhere)

- Programs vs processes, parent and child processes in depth → 01.06
- Admin vs standard user; system variables needing admin; `sudo` for Windows → 01.07
- Windows vs Mac vs Linux differences (`;` vs `:`, no `python` on Mac/Ubuntu, Homebrew paths) → 01.08
- Terminal vs shell; Windows Terminal → 02.01
- Shells and their command precedence (aliases, built-ins, cmd's current-folder search vs PowerShell's `.\`) → 02.02
- Running programs, arguments and flags → 02.04
- Script files and PowerShell execution policy → 02.06
- OS package managers (WinGet, Homebrew) and their PATH behaviour → 02.07
- Reading errors without panic ("command not found" in depth) → 02.08
- VS Code integrated terminal and its environment → 03.02
- Dev containers and standardised environments → 03.07
- Coding agents in the terminal (how they spawn shells) → 03.08
- Many Pythons: install manager, `py`, Store Python, uv-installed Python, conda, Python 3.10 end of life → 05.01
- Virtual environments and activation in depth → 05.03
- pip, uv, `uv run` → 05.04
- Node, npm, `--env-file`, Bun → 05.05
- Supply-chain attacks (s1ngularity, Shai-Hulud, install scripts) → 05.08
- `.env` and `.gitignore` mechanics → 01.04 (taught) and 08.07
- GitHub Actions secrets, trusted publishing (OIDC) → 08.09
- Copilot cloud agent and agent secrets on GitHub → 08.11 (agents on git) and 14.12
- MCP config files and their `env` blocks / `${VAR}` expansion → 10.09
- Subscriptions vs API billing (the `ANTHROPIC_API_KEY` override in depth) → 10.11
- Dev, staging and prod environments; environment settings on hosting dashboards → 13.07 (and 11.09)
- API keys, secret vs publishable → 14.03
- Short-lived tokens → 14.04
- Giving agents keys safely: deny rules, sandboxes, Claude Code scrubbing, Codex environment policy → 14.12
- Moving secrets out of plain text (`op run`, Infisical, dotenvx, 1Password Environments beta) → 15.07
- User vs system environment variables, where they are stored, `setx` truncation → 15.08
- Credential Manager as a better home for keys → 15.09
- When a key leaks: rotate, revoke, npm token revocation → 15.11
- Installers writing PATH → 17.06
- Version managers and shims (mise, pyenv, nvm, asdf): no lesson owns them yet → NEW: suggest "Version managers & shims" in Module 05 (Python & JavaScript Ecosystems), after 05.01.

## 6. Mental model

One metaphor for the whole lesson: **the satchel copied at the door.** It sits on the course's map of streets (00.02, 01.03) and keeps 01.03's you-are-here dot.

- (03) Every program is a courier sent out by another program. At the door, the parent copies its own satchel of labelled cards (name, value) and hands the copy over. Once the courier leaves, the satchel is its own.
- (04) Cards in the satchel: home folder, temp folder, and one long card, PATH. At home the master copy is kept in two drawers (user, system) or written by a startup file.
- (05) The PATH card is a numbered list of streets. Told "get python", the courier walks the streets in order and enters the first shop with that name. Later shops with the same name are never visited.
- (06) Every street walked, no such shop: "not recognized".
- (07) Three shops called python on the list; the first one wins. One of them is a signpost that sends you to the Store.
- (08) A virtual environment pins one new street to the top of this courier's card only.
- (09) An installer adds a street to the master copy at home. Couriers already out on the road still carry the old card; send a new one.
- (10) Break: see below.
- (11) Keys tucked into the satchel get copied into every courier you send, and every courier they send.
- (12) Lantern: a courier carrying a lantern (an agent) now sends couriers of its own and even edits the master copy. A thief who gets one satchel gets every key in it.
- (13) You, at the door: check which shop was entered, and what you put in the satchel.
- (16) End card: the satchel open, the PATH card on top.

Where it breaks (say it plainly in scene 10):
- A real satchel can be sealed and a courier can keep a card private. An environment has no seal: any program, script or agent you start can read every value, and copies them on to its own children.
- Some shops on the list are signposts, not shops: the Store alias and version-manager shims forward you elsewhere, so asking "which" can name a stand-in rather than the program that really runs.
- Shells do not only walk the streets: they first check their own built-ins and aliases, and old cmd looks in the current folder before the list.
- There is no single "the environment": there are as many satchels as running programs.

## 7. Cut list (tempting, stays out)

- Step-by-step instructions for editing PATH (dialog clicks, `setx`, profile edits, registry keys): how-to; COURSE.md forbids step lists. The dialog appears only as a picture.
- `setx` 1,024-character truncation and Aaron's 1,226-character user PATH: a real trap, but it is how-to territory; one "safe to ignore" label at most, depth in 15.08.
- Registry key names, `WM_SETTINGCHANGE`, the 32,767-character limit: mechanism below what a learner needs.
- PowerShell's full command-precedence order and `NoDefaultCurrentDirectoryInExePath`: one line in scene 05 covers it; depth in 02.02.
- The full `PATHEXT` list: screen label only.
- PowerShell 7.6 vs 5.1 wording differences and PowerShell lifecycle dates: show the 5.1 wording (observed, what Windows ships); the pwsh variant is unverified wording.
- Python 3.15's release (2026-10-09) and install-manager version numbers: too fresh and not needed; "since Python 3.14" carries the change.
- Python's own troubleshooting table and the legacy `py.exe` priority problem: one surprise line ("python and py start different Pythons") is enough; depth in 05.01.
- mise, shims and the March 2026 mise shadowing fix: one clause in the break scene; owner to be created (section 5).
- Claude Code's `CLAUDE_ENV_FILE`, SessionStart hooks, `settings.json` `env` block, `CLAUDE_CODE_MCP_ALLOWLIST_ENV`, credential masking: vendor detail that changes monthly; 14.12.
- Codex `shell_environment_policy` details and the conflicting default: name only as "agent tools began offering ways to strip keys"; the conflict makes any specific claim risky.
- Copilot `COPILOT_MCP_` prefix: too deep.
- The MCP spec's stdio-vs-OAuth credential rules: 10.09 and 14.12.
- GitGuardian's full statistics, including the 3.2% vs 1.5% Claude Code co-authored leak rate and 24,008 secrets in MCP configs: vendor figures, easy to misread, and 01.04 already used one GitGuardian figure. At most the 81% figure, attributed, and only if scene 12 has room.
- Shai-Hulud and s1ngularity victim counts: vary by source.
- Sonar's canary test of `.env` keys in agent traffic: vendor test; the point is carried by "whatever the agent reads goes to the model" which 01.04 already made.
- Historical Claude Code bug reports about auto-loading a project's `.env`: closed, current behaviour unverified; do not mention.
- `/proc/<pid>/environ`, crash dumps, the systemd "not for secrets" quote: systemd source was not fetched; the break scene's "no seal" carries the idea.
- Twelve-Factor history beyond one clause, `sudo` for Windows, Windows 11 servicing dates, PowerToys profiles: off topic or trivia.
- Windows Terminal default-console history beyond "since 2023 a new tab reloads": enough for the change arc.
- Any new Aaron anecdote. The observation about the course machine's three Pythons is presented as an observation, not a story about Aaron's habits. The `.venv` and "didn't know to `cd`" stories were told in 01.03 and 01.04; do not retell.
- Teasers for the next lesson: scene 15 names neighbours on the map, no "next time".

## 8. Facts to handle carefully (with the hedged wording to use)

- System PATH before user PATH on Windows: from a secondary source plus direct observation; Microsoft's own wording was not found. Say: "On Windows, the system's list comes first and your own list is added after it." Do not say "Microsoft documents"; if challenged, cut the clause, the lesson does not depend on it.
- The course machine's three Pythons (observed 2026-10-10): Python310 user install first, WindowsApps stub second, Miniconda third; Python310 listed twice in PATH. Say: "On the Windows machine this course is made on, typing python had three candidates." Do not generalise to every PC. Show paths with the user name shortened (`C:\Users\…\Python310\python.exe`).
- Python 3.10 end of life: python.org lists it as end-of-life with support ending in October 2026 (one source says 2026-10-01, another 2026-10-31). Say: "Python 3.10 reached its end of life this month." No day.
- Store alias stub: established since the May 2019 Windows 10 update. Message text comes from forums and Python docs, not observed this pass; put it on screen as "Python was not found; run without arguments to install from the Microsoft Store…" truncated with an ellipsis, not as a quote presented in full.
- Install manager: recommended since Python 3.14 (October 2025); the classic installer "will not be produced for Python 3.16 or later". Say: "Since Python 3.14, the recommended way to install Python on Windows is a new install manager, and the classic installer with the add-to-path checkbox is being retired." Do not say it is already gone.
- `py` vs `python` guidance flipped: the install manager's docs now recommend `python` and keep `py` for choosing versions. Avoid a firm "always type X"; the surprise line "python and py start different Pythons" is safe.
- Error wordings: cmd and Windows PowerShell 5.1 texts observed verbatim on 2026-10-10; bash observed; zsh from secondary source. Use these exact texts. Do not show the PowerShell 7 wording as Microsoft's.
- Windows Terminal new tabs reloading the environment: Terminal 1.18 (Preview, May 2023, setting default on). Say: "Since 2023, a new tab in Windows Terminal picks up the change; a tab that was already open does not."
- VS Code needing a restart: widely documented, not re-fetched this pass. Say: "an editor's built-in terminal usually needs the editor restarted."
- Claude Code reads environment variables at startup: current docs. Say: "Claude Code's documentation says it reads your environment when it starts, so it needs a restart to see a change."
- `ANTHROPIC_API_KEY` overriding the subscription: current docs; interactive mode asks once, `-p` mode always uses it. Say: "If that variable is set, Claude Code uses the key, and its pay-per-use billing, instead of your subscription, even when you are logged in. It asks you once first." Show `/status` on screen as where to check.
- Agents' exports not persisting: Claude Code docs ("An export in one command won't be available in the next"). Say: "In some agents each command gets a fresh shell, so an export or an activation doesn't stick." Do not claim it for every agent.
- Node native `.env`: stable in v24.10 / v22.21 (October 2025); Bun auto-loads. Say: "Some runtimes, like Node and Bun, can load a dot E N V file themselves." No version numbers spoken.
- s1ngularity (2025-08-26): established. Say: "In August 2025, a poisoned package stole dot E N V files and steered its victims' own AI command-line tools to search their disks for keys." No counts.
- Shai-Hulud (September and November 2025): established, CISA alert 2025-09-23. Say: "That autumn, a self-spreading worm in N P M packages harvested tokens from developers' environment variables."
- npm token revocation (2025-12-09): established. Say: "In December 2025, N P M revoked its old long-lived publishing tokens."
- Agent environment fencing: Claude Code scrubbing is opt-in and new this year; Codex's current docs say its KEY/SECRET/TOKEN filter is off by default while older docs said on (conflict). Say only: "Agent tools have started offering ways to strip keys from what their commands inherit; most of them are switched off until you turn them on." Do not name a default for Codex.
- GitGuardian 81% (vendor report, March 2026): if used, say: "GitGuardian, a company that scans for leaked keys, counted AI-service keys leaking about eighty percent more in 2025." Always attribute; 01.04 already used it, so prefer to skip.
- Where it is heading: direction is stated in 2026 security writing (some of it vendor-sponsored); 1Password Environments is a public beta (since 2025-10-29, Mac and Linux). Say: "The direction is to hand a key to one command for one run, or keep it behind a proxy, instead of leaving it in every program's environment. That's still early." Mark beta if any product is named.
- Deny rules vs subprocesses: Claude Code docs say file-tool deny rules do not cover a shell `cat`; the sandbox is off by default and absent on native Windows. Say: "A rule asking an agent not to read your keys is a request, not a fence." Do not claim any tool's protections are broken.
