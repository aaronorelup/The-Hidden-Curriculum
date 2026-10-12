# research-change: 01.05 Environment variables & PATH
Checked 2026-10-10. Lens: the last five years (about late 2021 to October 2026), plus the durable core.
Status tags: established / new this year (2026) / beta or announced / speculation.
Source dates are the dates shown in the source. "undated" = living docs with no visible date. "not re-fetched" = from older knowledge, verify before putting it on screen.
Name check from the orchestrator notes: "Windows Store python alias" is the Windows **App Execution Alias** (fake `python.exe` / `python3.exe` in `%LocalAppData%\Microsoft\WindowsApps`), not "App Installer". "which python" is the Unix command; Windows equivalents are `where.exe python` (cmd) and `Get-Command python` (PowerShell). "venvs" = Python virtual environments (`.venv`).

## 1. Environment variables: inherited settings (the durable core)
- A process gets a copy of its parent's environment when it starts; changes made later in the parent, or in the system settings, do not reach a process that is already running. Status: established (not re-fetched; textbook OS behaviour).
- Claude Code's own docs state the same rule for an AI tool: "Claude Code reads shell environment variables at startup, so changes to them take effect the next time you launch `claude`." A variable set in a shell "lasts for that terminal session". Status: established.
  - https://code.claude.com/docs/en/env-vars (current docs, undated, fetched 2026-10-10)
- AI tools also inject their own variables: Claude Code `settings.json` has an `env` key whose values are passed in "whether or not the shell launched it"; "you can set a variable but you can't remove one". Status: established.
  - same page
- Windows keeps two stored layers (System and User); the PATH a new process sees is System PATH followed by User PATH. Status: established (not re-fetched).

## 2. Windows tools for viewing and editing variables (what changed)
- PowerToys 0.75 (end of October 2023) added an **Environment Variables** editor with "profiles" that override User/System values and restore them when un-applied. The old Control Panel "Environment Variables..." dialog still exists. Status: established.
  - https://betanews.com/2023/10/31/microsoft-releases-powertoys-v0-75-0-with-new-environment-variables-module-settings-dashboard-and-more/ (2023-10-31)
  - https://winaero.com/powertoys-0-75-released-with-dashboard-and-cool-environment-variable-editor (2023)
- Windows Terminal became the default console on Windows 11 22H2 (announced 2022-10-18; needs Terminal 1.15+). Command Prompt and PowerShell now open inside Windows Terminal. Status: established.
  - https://devblogs.microsoft.com/commandline/windows-terminal-is-now-the-default-in-windows-11/ (2022-10-18)
- `sudo` for Windows (preview build 26052, February 2024; needs Windows 11 24H2; default mode opens a new elevated window). Tangential to PATH, but it is another "Unix word now on Windows". Status: established.
  - https://betanews.com/2024/02/08/microsoft-introduces-linuxs-sudo-command-to-windows-11/ (2024-02-08)
  - https://www.elevenforum.com/t/introducing-sudo-for-windows-11.22324 (2024)

## 3. "Open a new terminal after installing" (what changed, what did not)
- Durable reason: the installer edits the stored PATH; your open terminal already holds its copy. Status: established.
- CHANGE: Windows Terminal 1.18 (Preview May 2023) made **new tabs and panes reload the system environment** by default (`compatibility.reloadEnvironmentVariables`, default true). Before that you had to close the whole Terminal window, not just a tab. Announcement: "No longer do you need to fully shut down the Terminal after installing something and changing the PATH – just open a new tab." Status: established.
  - https://devblogs.microsoft.com/commandline/windows-terminal-preview-1-18-release/ (2023-05-24)
  - https://github.com/microsoft/terminal/issues/1125 (the original complaint)
- Still true: a tab that was already open keeps the old PATH; a terminal inside an editor (VS Code) inherits from the editor process, so the editor usually needs a restart too. Status: established (VS Code part not re-fetched; widely documented).
- Same rule for agents: Claude Code reads variables at launch (section 1), so an agent started before an install does not see the new PATH until it is restarted. Status: established.

## 4. PATH: an ordered list, first match wins (durable)
- The shell walks PATH folders left to right and runs the first matching program. Unix `which` / `type -a`, Windows `where.exe` / `Get-Command -All` show which one wins. Status: established (not re-fetched).
- On Windows, `PATHEXT` decides which extensions count as programs; the old python.org installer's "PrependPath" option "Prepend install and Scripts directories to PATH and add .PY to PATHEXT". Status: established.
  - https://docs.python.org/3/using/windows.html (current docs, undated)
- Two error wordings to recognise: cmd: `'python' is not recognized as an internal or external command, operable program or batch file.`; PowerShell: `The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.`; macOS zsh: `zsh: command not found: python`; Ubuntu: `Command 'python' not found, did you mean: command 'python3'`. Status: established (wordings not re-fetched except Ubuntu below).

## 5. The Windows "python" alias that opens the Store
- Origin (older than five years): the Windows 10 May 2019 Update added fake `python.exe` and `python3.exe` on PATH that open the Microsoft Store when no Python is installed. Status: established (2019).
  - https://www.python.org/pipermail/python-dev/2019-May/157639.html (2019-05, Steve Dower)
  - https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/ (2019)
- What you see: "Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases." It is the first match on PATH winning: the alias folder `...\AppData\Local\Microsoft\WindowsApps` is on the user PATH. Status: established.
  - https://discuss.python.org/t/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store/80479 (2025)
  - https://bobbyhadz.com/blog/python-was-not-found-run-without-arguments-to-install (undated)
- The `py` launcher was "blind" to Store Python; it was changed to search PATH first in Python 3.13 (backported to 3.11.8 / 3.12.2). Status: established.
  - https://peps.python.org/pep-0773/ (PEP 773 text)

## 6. Python on Windows: the installer was replaced (biggest change in this lesson's area)
- PEP 773 "A Python Installation Manager for Windows" (Steve Dower) accepted around April 2025; the deprecation is tied to Python 3.14. Status: established.
  - https://peps.python.org/pep-0773/
  - https://discuss.python.org/t/pep-773-a-python-installation-manager-for-windows/77900 (2025)
- The **Python install manager** (`pymanager`, from the Microsoft Store or python.org MSIX, also WinGet) is now the recommended way. It provides `python`, `py`, `pymanager` (and `pythonw`, `pyw`); `python3` exists only "to catch accidental uses". `python` runs "the version requested by the script, an active virtual environment, or the default installed version". Status: established.
  - https://docs.python.org/3/using/windows.html (current docs, undated)
- Those commands are themselves App Execution Aliases ("Python (default)"); the docs' fix for "command not found or opens the Store" is to check those aliases and that `%UserProfile%\AppData\Local\Microsoft\WindowsApps` is on PATH. On first runtime install it offers to add `%LocalAppData%\Python\bin` to PATH (for versioned names like `python3.14.exe`). Status: established.
  - same page
- Legacy full installer (the one with the "Add python.exe to PATH" checkbox): "deprecated since 3.14 and will not be produced for Python 3.16 or later." Status: established; 3.15 is the last version with it.
  - same page; https://www.python.org/downloads/release/pymanager-261/ (2026-03-31: "The traditional executable installer will stop being released with Python 3.16")
- Python 3.15.0 was released 2026-10-09 (yesterday); 3.14 on 2025-10-07. Status: new this year.
  - https://www.python.org/downloads/ (fetched 2026-10-10)
- Install manager versions in 2026: 26.1 (2026-03-31); docs reference features up to 26.4. Status: new this year.
- Consequence for the mental model: on a 2026 Windows machine, "which python ran" can be an alias that dispatches to a managed runtime, not a plain folder on PATH. Status: established (inference from the docs above).

## 7. Multiple installs and new managers putting Python on PATH
- uv 0.8 (July 2025): `uv python install` now puts a versioned executable (e.g. `python3.13`) into a PATH folder (usually `~/.local/bin`) by default; plain `python`/`python3` only with `--default` (still preview). "should not be breaking unless it shadows a Python executable elsewhere on the PATH". Status: established (`--default` beta).
  - https://pydevtools.com/blog/uv-0-8-release-automatic-python-installation-to-path/ (2025-07)
- Apple Silicon Macs: Homebrew 3.0.0 (2021-02-05) officially supports Apple Silicon at `/opt/homebrew`, which is NOT on the default macOS PATH (Intel used `/usr/local/bin`, which is). Hence the very common `zsh: command not found: brew` until the `brew shellenv` line is added to `~/.zprofile`. Status: established.
  - https://brew.sh/2021/02/05/homebrew-3.0.0/ (2021-02-05)
  - https://mac.install.guide/homebrew/zsh-command-not-found-brew.html (undated)
- Linux: since Ubuntu 20.04 there is no `python` command by default, only `python3`; `python-is-python3` adds the link. PEP 394 (2019 update) lets each distribution decide what `python` means. Status: established.
  - https://lists.snapcraft.io/archives/foundations-bugs/2020-April/413880.html (2020-04)
  - https://peps.python.org/pep-0394/
- PEP 668 "externally-managed-environment" (Debian 12, Ubuntu 23.04+, Homebrew Python) refuses system-wide `pip install`, pushing everyone into virtual environments. Status: established (2023 onward; see 01.04 research).

## 8. Virtual environments: "activate" = edit PATH for this shell
- Durable: activating a venv prepends its `bin` (macOS/Linux) or `Scripts` (Windows) folder to PATH and sets `VIRTUAL_ENV`; it affects only that shell and its children. Status: established (not re-fetched).
- CHANGE: tools run inside the environment without manual activation: `uv run` (uv, 2024 onward) and the install manager's `python` honouring "an active virtual environment". Status: established.
  - https://docs.python.org/3/using/windows.html; https://docs.astral.sh/uv/ (undated)
- CHANGE: VS Code's Python Environments extension (rollout July-August 2025) took over terminal activation; setting `python-envs.terminal.autoActivationType` with modes "command" (default), "shellStartup" (edits `.zshrc`/PowerShell profile) and "off". Applies only to newly created terminals. Status: established.
  - https://devblogs.microsoft.com/python/python-in-visual-studio-code-august-2025-release/ (2025-08)
  - https://visualstudiomagazine.com/articles/2025/08/18/dedicated-python-environments-tool-rolls-out-in-vs-code-update.aspx (2025-08-18)
- Agents: each agent shell command may be a fresh process, so activation does not stick by itself. Claude Code's `CLAUDE_ENV_FILE` is a script "Claude Code runs before each Bash command ... Use to persist virtualenv or conda activation across commands." Status: established.
  - https://code.claude.com/docs/en/env-vars (undated, fetched 2026-10-10)

## 9. Secrets in environment variables and `.env` files
- Durable: the "config in the environment" idea (Twelve-Factor, 2011) and `.env` files read by dotenv libraries; `.env` is plain text kept out of git by `.gitignore`. Status: established (not re-fetched; see 01.04 research).
- CHANGE: runtimes read `.env` natively. Node.js `--env-file` (20.6.0, 2023, experimental); `process.loadEnvFile()` later; both marked stable in v24.10.0 / v22.21.0 per Node docs (2025). The built-in parser has no `${VAR}` expansion. Status: established (flag stability from a secondary guide; confirm in Node CLI docs).
  - https://env.dev/guides/nodejs-env-variables (undated)
  - https://beta.docs.nodejs.org/process/loadEnvFile (undated)
- AI tools name their keys by env var: `ANTHROPIC_API_KEY` "is used instead of your Claude Pro, Max, Team, or Enterprise subscription even if you are logged in" (prompted once in interactive mode). A stray key in your environment changes who gets billed. Status: established.
  - https://code.claude.com/docs/en/env-vars (undated)
- MCP: the 2025-03-26 spec says stdio servers "SHOULD NOT" use the OAuth flow and should "retrieve credentials from the environment" (the `env` block in MCP config files); HTTP servers moved to OAuth 2.1 (2025-03-26) and resource-server model (2025-06-18). Status: established; later revisions (2025-11-25, a reported 2026 revision) not verified.
  - https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization (2025-03-26)
  - https://auth0.com/blog/mcp-specs-update-all-about-auth/ (2025-06)
- 1Password "Environments" local `.env` destination (public beta 2025-10-29): a virtual `.env` served via named pipe, never on disk; Mac/Linux. Status: beta or announced (see 01.04 research).
  - https://1password.com/blog/1password-environments-env-files-public-beta (2025-10-29)

## 10. Why AI agents read env vars and `.env`, and the security turn (2024-2026)
- Agents run your commands as child processes, so by default they inherit every variable you have, secrets included. Claude Code sandbox docs: environment variables are "Inherited from Claude Code, including any secrets in its environment". Status: established.
  - https://code.claude.com/docs/en/sandboxing (undated, fetched 2026-10-10)
- Claude Code controls now: permission deny rules (e.g. `Read(./.env)`) block the file tools only, not `cat .env` in Bash; the OS sandbox (macOS, Linux, WSL2; off by default; native Windows unsandboxed) adds `filesystem.denyRead`, `sandbox.credentials` with `deny` (unset variable) or `mask` (command sees a placeholder, proxy substitutes the real value for allowed hosts), and `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips credentials from Bash, hooks and stdio MCP servers. "There is no built-in credential deny list." Status: established; masking features carry 2026 version requirements (v2.1.2xx), so treat as new this year.
  - https://code.claude.com/docs/en/sandboxing; https://code.claude.com/docs/en/env-vars; https://code.claude.com/docs/en/settings (all undated)
- OpenAI Codex: `shell_environment_policy` controls which variables reach spawned commands; current docs say `ignore_default_excludes` "defaults to `true`, which skips automatic filtering for variable names containing KEY, SECRET, or TOKEN" (i.e. no filtering unless you opt in). Earlier docs/PRs described the filter as on by default: the default appears to have flipped. Status: established (current docs) with a noted conflict.
  - https://learn.chatgpt.com/docs/config-file/config-basic (current docs, fetched 2026-10-10; redirected from developers.openai.com/codex/local-config)
  - https://codex.danielvaughan.com/2026/04/28/codex-cli-shell-environment-policy-subprocess-secrets-defence/ (2026-04-28, third party)
- Turning point 1, s1ngularity (2025-08-26): malicious Nx npm versions stole `.env` files, SSH keys and tokens and prompted installed AI CLIs (Claude, Gemini, Q) with flags like `--dangerously-skip-permissions` / `--yolo` to hunt for secrets; GitGuardian counted 2,349 leaked secrets across 1,346 repos. Status: established.
  - https://www.wiz.io/blog/s1ngularity-supply-chain-attack (2025-08)
- Turning point 2, Shai-Hulud worm (September 2025; second wave November 2025): harvested environment variables (`GITHUB_TOKEN`, `NPM_TOKEN`, `AWS_ACCESS_KEY_ID`...) and ran TruffleHog on developer machines; CISA alert 2025-09-23 ("over 500 packages", "Immediately rotate all developer credentials"). Status: established.
  - https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem (2025-09-23)
- Response, away from long-lived secrets in env vars: npm revoked all classic tokens 2025-12-09; `npm login` now gives two-hour session tokens; trusted publishing (OIDC) "eliminates long-lived tokens entirely" in CI. Status: established.
  - https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/ (2025-12-09)
- GitHub push protection on by default for all pushes to public repos (rollout from 2024-03-01). Status: established.
  - https://github.blog/news-insights/product-news/keeping-secrets-out-of-public-repositories/ (2024-02-29)
- Scale (GitGuardian State of Secrets Sprawl 2026, March 2026): ~28.65 million new secrets in public GitHub commits in 2025 (+34%); 1,275,105 AI-service secrets (+81%); commits made with Claude Code showed a 3.2% secret-leak rate vs 1.5% baseline; MCP config files are a named leak source. Status: new this year (vendor report; vendor sells detection).
  - https://thehackernews.com/2026/03/the-state-of-secrets-sprawl-2026-9.html (2026-03)
  - https://gitguardian.com/state-of-secrets-sprawl-report-2026 (2026)
- Where it is heading: secrets injected per command or proxied (masking, named-pipe `.env`, OIDC short-lived tokens) instead of sitting in the environment of every process. Status: beta or announced / speculation for wide adoption.

## Ideas that did NOT change (the durable mental model)
- A process inherits a copy of its parent's environment at birth; later changes do not reach it.
- PATH is an ordered list of folders; the first match wins; "not recognized / command not found" means no folder on the list holds that name.
- Installing edits the stored settings, not your open terminal; something must be (re)started to see it.
- Activating a venv is just putting its folder first on PATH for that shell.
- An env var or `.env` file is plain text readable by any program you run, including AI agents and anything they install.
- To know which program ran, ask the shell (`which` / `where.exe` / `Get-Command`), or ask the program itself (`python -c "import sys; print(sys.executable)"`).

## Traps (commonly said, now wrong or misleading)
- "Tick 'Add python.exe to PATH' in the python.org installer." That installer is deprecated since 3.14 and ends with 3.15; the recommended route is the Python install manager (Store/MSIX/WinGet).
- "The `python` that opens the Store is a bug, just disable the aliases." In 2026 the official Python commands on Windows are themselves App Execution Aliases; disabling them can break the install manager.
- "Use `py`, not `python`, on Windows." The install manager's docs now recommend `python`; `py` is for picking versions.
- "Close Windows Terminal completely after installing." Since Terminal 1.18 (2023) a new tab reloads the environment; only already-open tabs (and editors/agents started earlier) are stale.
- "Type `python` on Linux/Mac." Ubuntu has no `python` by default since 20.04; macOS ships no `python` (only `python3` via Command Line Tools, not re-fetched).
- "Homebrew lives in /usr/local/bin." Only on Intel Macs; Apple Silicon uses `/opt/homebrew`, which is not on PATH by default.
- "`.env` is safe because it is in `.gitignore`." Git ignores it; every process you run, including agents and malicious packages (s1ngularity, Shai-Hulud, 2025), can still read it.
- "A deny rule stops the agent seeing my `.env`." In Claude Code, `Read(./.env)` blocks the file tool, not `cat .env` in Bash; only the OS sandbox / credential scrubbing covers subprocesses, and the sandbox is off by default and absent on native Windows.
- "Codex hides KEY/SECRET/TOKEN variables by default." Current docs say the automatic filter is off by default (`ignore_default_excludes = true`).
- "Being logged in to Claude means my subscription pays." A set `ANTHROPIC_API_KEY` overrides the subscription (always in `-p` mode).
- "Long-lived npm tokens in an env var for CI." Classic npm tokens were revoked on 2025-12-09; trusted publishing (OIDC) is the replacement.
- "`node` needs the dotenv package to read `.env`." Node has `--env-file` natively since 20.6 (stable in 22.21 / 24.10), though without variable expansion.
