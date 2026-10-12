# research-change: 01.04 Hidden files & dotfiles
Checked 2026-10-09. Lens: last five years (about 2021 to 2026), plus the durable core.
Status tags: established / new this year (2026) / beta or announced / speculation.
Source dates are the dates shown in the source. "undated" = no date visible in what was fetched. "not re-fetched" = from older knowledge, verify before quoting on screen.
Name check from the orchestrator notes: all names are real and spelled correctly. "MCP configs" means files such as `.mcp.json` (Claude Code), `.cursor/mcp.json` (Cursor), `.vscode/mcp.json` (VS Code). "The AI-tool layer" = `.claude/`, `CLAUDE.md`, `.cursor/`, `AGENTS.md`, `.github/copilot-instructions.md`, `.gemini/`, `~/.codex/`.

## 1. Why dotfiles are hidden on Unix (the durable origin story)
- The "hidden dotfile" began as a shortcut: early Unix `ls` skipped any name starting with `.` to hide the `.` and `..` entries; other programmers then put config files in home folders behind a leading dot. Rob Pike (Bell Labs) called the hidden-file idea an unintended consequence and "a mistake"; his memory of exact details is hedged by him. Status: established (as Pike's recollection, essay dated 2012-08-03, original Google+ post deleted).
  - https://tookmund.com/2022/03/rob-pike-shortcuts (2022-03, archived copy of the 2012 essay)
  - https://linux-audit.com/linux-history-how-dot-files-became-hidden-files/ (undated)
- Hiding is only a display convention: the file is not protected, encrypted or special. `ls -a` shows it. Status: established.
- Pike's point that still matters: the files serve a purpose, the naming does not; Plan 9 put config in `$HOME/lib` with no dotfiles. Status: established.

## 2. `~/.config` and the XDG Base Directory spec (the tidy-up that is still incomplete)
- XDG Base Directory spec dates from 2003; `$XDG_CONFIG_HOME` defaults to `~/.config`. Many tools still ignore it and drop dotfiles straight into `~`. Status: established.
  - https://wiki.archlinux.org/title/XDG_Base_Directory (living wiki, undated)
- Git reads both legacy `~/.gitconfig` and `~/.config/git/config` (plus `~/.config/git/ignore`). Status: established.
  - same ArchWiki page
- Current example of the AI layer using XDG: Claude Code, on first writing `.claude/settings.local.json`, adds `**/.claude/settings.local.json` to the global git excludes file, which defaults to `$XDG_CONFIG_HOME/git/ignore` or `~/.config/git/ignore`. Status: established (current docs). Note for the lesson: an agent editing a hidden file in your home folder you never opened.
  - https://code.claude.com/docs/en/settings (current docs, undated)
- AI CLIs mostly did NOT follow XDG: they use top-level home dotfolders `~/.claude/`, `~/.claude.json`, `~/.codex/`, `~/.gemini/`, `~/.cursor/`. Status: established (docs cited in section 7). The "home folder full of dotfiles" Pike complained about grew again with AI tools.

## 3. Windows: the Hidden attribute, AppData, and where the toggle moved
- Windows hides files with a file-system attribute (Hidden, and a stronger "protected operating system file"/System flag), not by name. A dot-name is not hidden on Windows; `.git` is hidden there only because Git sets the attribute on it. Status: established (not re-fetched; the Git-for-Windows `core.hideDotFiles` default is from older knowledge).
- `AppData` (`%USERPROFILE%\AppData\Roaming`, `Local`, `LocalLow`) is the per-user app-settings home since Vista (2007); Roaming = follows a domain user between machines. Status: established.
  - https://learn.microsoft.com/en-us/windows/win32/msi/appdatafolder (undated; AppDataFolder = full path of the Roaming folder)
  - https://learn.microsoft.com/en-us/Windows/win32/shell/knownfolderid (undated)
  - AppData being hidden by default: established in practice but not found stated on a Microsoft page this session.
- CHANGE: the Settings toggle moved. Windows 11 had File Explorer toggles ("Show file extensions", "Show hidden and system files", "Show full path in title bar") under System > For developers; Microsoft announced at Build 2025 a System > Advanced page that "replaces the For developers tab" and keeps those toggles. Status: established (announced 2025-05-19; guides tie the Advanced page to 25H2 and later).
  - https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-new-advanced-settings-for-windows-11 (2025-05-19)
  - https://www.elevenforum.com/t/show-hidden-files-folders-and-drives-in-windows-11.4962/ (living tutorial)
- The old routes still work: Explorer View > Show > Hidden items (ordinary hidden only); Folder Options for protected system files. Status: established.
- Long-standing papercut: Explorer used to refuse a name like `.gitignore` ("You must type a file name"); the workaround was typing `.gitignore.` (trailing dot). Status: established as history (2014); whether current Windows 11 still refuses was NOT confirmed this session, so do not claim either way.
  - https://www.hanselman.com/blog/how-to-create-a-file-with-a-dot-prefix-in-windows-explorer (2014)

## 4. macOS
- Finder: Command + Shift + Period toggles hidden files (they show faded). Has existed since macOS Sierra (2016, not re-fetched). Status: established.
  - https://www.computerhope.com/issues/ch001006.htm (undated)
- macOS hides both dot-names (Unix rule) and items with the `hidden` flag (e.g. `~/Library`). `.DS_Store` is the classic accidental commit. Status: established (not re-fetched).

## 5. `.env` files: from a library convention to built into runtimes
- Background: the `.env` file comes from the Twelve-Factor "config in the environment" idea (2011) and the dotenv libraries (Ruby ~2012, then Node, Python). Status: established (not re-fetched).
- CHANGE: Node.js v20.6.0 (2023) added `--env-file` natively; first version had no multi-line values, no expansion, one file. `process.loadEnvFile()` arrived later (v21.7.0, backported to 20.12; sources disagree slightly). Status: established.
  - https://philna.sh/blog/2023/09/05/nodejs-supports-dotenv/ (2023-09-05)
  - https://pawelgrzybek.com/node-js-with-native-support-for-env-files-you-may-not-need-dotenv-anymore/ (2023)
- CHANGE: secrets managers now mount a fake `.env`. 1Password "Local .env file" destination (public beta 2025-10-29): a virtual `.env` served through a UNIX named pipe, never written to disk, not trackable by Git; Mac and Linux only (Windows "being explored"). Any local process can read it while unlocked. Status: beta or announced.
  - https://1password.com/blog/1password-environments-env-files-public-beta (2025-10-29)
  - https://developer.1password.com/docs/environments/local-env-file (current docs)
- Durable: `.env` is plain text. It is "secret" only because `.gitignore` lists it and because people keep it out of chats. Status: established.

## 6. `.venv` and Python environments
- CHANGE: Python 3.13 (released October 2024) `venv` writes a `.gitignore` (containing `*`) inside every new environment by default; opt out with `--without-scm-ignore-files`. So a fresh `.venv` now ignores itself. Status: established.
  - https://docs.python.org/ja/3.13/library/venv.html (3.13 docs: "venv now creates a .gitignore file for Git by default")
- CHANGE: uv (Astral) creates the project environment in `.venv` next to `pyproject.toml` by default and auto-excludes it from git with an internal `.gitignore`. A preview feature (`centralized-project-envs`) moves the real env into uv's cache and leaves a `.venv` link. Status: established (default); beta (centralized envs).
  - https://docs.astral.sh/uv/concepts/projects/layout/ (current docs)
- CHANGE: PEP 668 "externally-managed-environment": Debian 12 / Ubuntu 23.04 and Homebrew Python refuse system-wide `pip install`, pushing everyone into a venv. Status: established (2023 onward).
  - https://pydevtools.com/handbook/explanation/what-is-pep-668/ (undated)
- Five years ago `venv`/`env`/`virtualenv` folder names varied; `.venv` (hidden) is now the de facto default name. Status: established (trend; inferred from the two defaults above).

## 7. The AI-tool layer (entirely new in five years)
- 2021: no such layer. Hidden project config was `.git`, `.gitignore`, `.env`, `.vscode/`, `.idea/`, `.github/`. Status: established.
- MCP introduced by Anthropic 2024-11-25; donated to the Linux Foundation's Agentic AI Foundation (AAIF) 2025-12-09; announcement cites 10,000+ public MCP servers and adoption by ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code. Status: established.
  - https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (2025-12-09)
- VS Code 1.99 (March 2025 release) brought agent mode to Stable with MCP servers configured in `.vscode/mcp.json` (top-level key `servers`, unlike `mcpServers` in Claude/Cursor). Status: established.
  - https://code.visualstudio.com/updates/v1_99 (March 2025)
- Claude Code: research preview 2025-02-24, GA 2025-05-22. Its current file map (docs): project `CLAUDE.md` and `.mcp.json` (committed); `.claude/settings.json`, `.claude/rules/`, `.claude/skills/<name>/SKILL.md`, `.claude/agents/`, `.claude/commands/` (committed); `.claude/settings.local.json` (gitignored); home `~/.claude.json` (sign-in session, MCP configs, trust decisions; "you don't need to edit it"), `~/.claude/settings.json`, `~/.claude/CLAUDE.md`, `~/.claude/projects/<project>/memory/` (auto memory). Commands and skills are now "the same mechanism". Status: established.
  - https://code.claude.com/docs/en/claude-directory (current docs)
  - https://code.claude.com/docs/en/settings (current docs)
  - https://www.havoptic.com/releases/claude-code/2025/5 (1.0.0 on 2025-05-22)
- Agent Skills (`SKILL.md` folders) unveiled by Anthropic October 2025; published as an open standard (agentskills.io) 2025-12-18; adopters reported to include OpenAI, Microsoft, GitHub, Cursor. Status: established (October day unconfirmed).
  - https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure (Dec 2025)
- Auto memory in Claude Code (Claude writes its own notes under `~/.claude/projects/.../memory/`) shipped around Feb 2026 (v2.1.59 per one guide). Status: new this year (version per secondary source).
  - https://www.morphllm.com/claude-code-memory-files (2026)
- Cursor: root `.cursorrules` (2023 era) is "still supported, but deprecated"; replaced by `.cursor/rules/*.mdc` files with frontmatter (`description`, `globs`, `alwaysApply`). Exact version of the switch is disputed (0.43 vs 0.45, late 2024 / Jan 2025). Status: established.
  - https://docs.cursor.com/context/rules (current docs)
- AGENTS.md: launched August 2025 (OpenAI Codex origin), contributed to AAIF 2025-12-09; OpenAI claims 60,000+ projects. GitHub Copilot coding agent reads AGENTS.md (root or nested), `.github/copilot-instructions.md`, `.github/instructions/**.instructions.md`, `CLAUDE.md`, `GEMINI.md` (2025-08-28). Copilot code review added AGENTS.md 2026-06-18. Status: established; adoption number is vendor-claimed.
  - https://openai.com/index/agentic-ai-foundation/ (2025-12-09)
  - https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions (2025-08-28)
  - https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements (2026-06-18)
- OpenAI Codex CLI announced 2025-04-16; config in `~/.codex/` (format moved from YAML/JSON early on to `config.toml` + AGENTS.md). Status: established (format history hedged).
  - https://huggingface.co/blog/lynn-mikami/openai-codex-cli (2025-04-17)
- Gemini CLI launched 2025-06-25 (`~/.gemini/settings.json`, project `.gemini/settings.json`); Google announced 2026-05-19 it is transitioning to the closed-source Antigravity CLI; consumer Gemini CLI stopped serving 2026-06-18 (enterprise / paid API keys unchanged). Status: new this year. So `.gemini/` folders on learners' machines may be leftovers.
  - https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (2026-05-19)
  - https://geminicli.com/docs/get-started/configuration (current docs)
- Direction of travel: consolidation on shared, tool-neutral filenames (AGENTS.md, SKILL.md, MCP) under the Linux Foundation, while each vendor keeps its own hidden folder. Status: speculation (trend reading).

## 8. Secrets, `.gitignore` and the five-year security arc
- CHANGE: GitHub push protection (blocks pushes containing detected secrets) piloted April 2022, GA May 2023, on by default for all pushes to public repos from 2024-02-29; can be bypassed. Personal push protection is on by default; repository-level is off by default and needs GitHub Secret Protection. Status: established.
  - https://github.blog/news-insights/product-news/keeping-secrets-out-of-public-repositories/ (2024-02-29)
  - https://docs.github.com/ko/code-security/concepts/secret-security/push-protection (current docs)
- GitGuardian State of Secrets Sprawl 2026 (covers 2025): 28.65 million new hardcoded secrets on public GitHub in 2025 (+34% YoY); 1,275,105 leaked AI-service secrets (+81%); 8 of 10 fastest-growing leak categories AI-related; 64% of valid secrets from 2022 still not revoked; leaked secrets +152% since 2021 vs developer base +98%. Vendor claim: commits co-authored with Claude Code leaked at 3.2% vs 1.5% baseline. Status: new this year (vendor report, March 2026).
  - https://thehackernews.com/2026/03/the-state-of-secrets-sprawl-2026-9.html (2026-03)
  - https://dev.to/gitguardian/the-state-of-secrets-sprawl-2026-ai-service-leaks-surge-81-and-29m-secrets-hit-public-github-2bgj (2026-03)
- Durable: deleting a committed `.env` in a later commit does not remove it from history; the only fix is rotating the key. Status: established.

## 9. When hidden config files became an attack surface for AI agents (2025-2026)
- Rules File Backdoor (Pillar Security; disclosed to Cursor 2025-02-26, public 2025-03-18): hidden Unicode instructions in AI rule files (`.cursor/rules`, Copilot instructions) make the assistant write malicious code; persists through forks. GitHub responded with a hidden-Unicode warning on github.com; Cursor said it is the user's responsibility. Status: established.
  - https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html (2025-03-18)
- Cursor CurXecute (CVE-2025-54135, fixed in 1.3 on 2025-07-29) and MCPoison (CVE-2025-54136, Check Point): once a project MCP config was approved, later edits to it were trusted silently, so a shared repo could swap in a malicious server. Status: established.
  - https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability.html (2025-08)
- Nx "s1ngularity" (2025-08-26): compromised npm package ran installed AI CLIs (Claude, Gemini, Q) with `--dangerously-skip-permissions`, `--yolo`, `--trust-all-tools` to hunt secrets and wallets; succeeded in hundreds of cases; data dumped into public `s1ngularity-repository` repos. Status: established.
  - https://wiz.io/blog/s1ngularity-supply-chain-attack (2025-08)
- Shai-Hulud npm worm (found 2025-09-14/15): ran TruffleHog over the filesystem and dumped environment variables to steal tokens; self-propagated through 500+ packages. Status: established. (Sources don't specifically say `.env`; say "files and environment variables".)
  - https://sysdig.com/blog/shai-hulud-the-novel-self-replicating-worm-infecting-hundreds-of-npm-packages (2025-09)
- Claude Code project files (Check Point, "Caught in the Hook", 2026-02-25): repo-controlled `.claude/settings.json` hooks, `.mcp.json` auto-approval and an `ANTHROPIC_BASE_URL` env override could run commands or leak API keys on opening an untrusted repo (CVE-2025-59536, CVE-2026-21852); all patched before publication. Status: new this year.
  - https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files/ (2026-02-25)
  - https://www.theregister.com/2026/02/26/clade_code_cves/ (2026-02-26)
- Agents reading `.env`: Cursor staff confirmed (2026-02-18, Cursor 2.5.17) that the default `.env*` ignore applies only to indexing, not to the Agent's Read File or Tab; `.cursorignore` does not block terminal or MCP tools, so `cat .env` still works. Status: new this year.
  - https://forum.cursor.com/t/cursor-reads-env-files-by-default/152167 (2026-02-18)
- Claude Code's documented control is a permissions deny rule, e.g. `Read(./.env)` and `Read(./.env.*)` in settings. User reports (2026, unverified) say deny rules don't cover every path (shell commands, search tools). Status: established (docs); claims of gaps are speculation-grade single reports.
  - https://code.claude.com/docs/en/settings (current docs)
  - https://github.com/anthropics/claude-code/issues/26286 (2026, user report)
- The shift in one line for the planner: in 2021 a hidden config file was passive data; by 2025-2026 files like `.claude/settings.json`, `.mcp.json`, `.cursor/rules` and `AGENTS.md` are instructions or commands an agent acts on, so reviewing diffs of hidden files is a security habit. Status: established (supported by every incident above).

## 10. What did NOT change (durable mental model)
- A leading dot hides a name on Unix/macOS by convention only; Windows hides by attribute. Nothing about hiding protects contents.
- Hidden = "config the tool manages, not your work" (`.git` is the whole history; deleting it deletes the history, not your files).
- `.gitignore` decides what Git tracks; it does not hide files from your OS, your editor, or an agent.
- Per-user settings live in your home folder (`~/.something`, `~/.config`, `AppData`); per-project settings live in dot-folders inside the project.
- Secrets in plain files are only as safe as the habits around them: ignore, never paste, rotate when exposed.
- The way to see the layer: `ls -a` / `dir /a` / `Get-ChildItem -Force`, Explorer "Hidden items", Finder Cmd+Shift+. (and `git status` / `git diff` to see what an agent changed, including hidden files).

## Traps (commonly said, now wrong or misleading)
- "Dotfiles are a Linux power-user thing." Now every AI coding tool on Windows too writes `.claude/`, `.cursor/`, `.vscode/mcp.json`, `AGENTS.md`, `~/.claude.json`.
- "Hidden config files are passive." Since 2025 they are instructions agents follow and commands they run (hooks, MCP servers); they have CVEs.
- "Put it in `.gitignore` and the AI can't see it." `.gitignore` and even Cursor's default `.env*` ignore cover indexing or git, not every agent tool (Cursor staff, 2026-02-18).
- "Use `.cursorrules`." Deprecated; `.cursor/rules/*.mdc` or tool-neutral `AGENTS.md`.
- "Gemini CLI / `.gemini/` is Google's current terminal agent." Consumer access ended 2026-06-18; Antigravity CLI replaced it.
- "Remember to add your venv to `.gitignore`." Python 3.13 `venv` and uv now ignore it automatically (older Python and other tools do not).
- "You need the dotenv package to read `.env`." Node 20.6+ reads it natively; Bun and others too (Bun not re-checked this session).
- "In Windows 11, show hidden files under Settings > For developers." On newer builds it is Settings > System > Advanced (Build 2025 announcement).
- "GitHub won't let you push a secret." Push protection only catches recognised token patterns and can be bypassed; the internal-repo leak rate is higher (32.2% vs 5.6%, GitGuardian 2026).
- "Deleting the leaked `.env` fixes it." History keeps it and 64% of leaked valid secrets from 2022 were never revoked; rotate.
- "A `.env` file is encrypted / hidden means secure." It is plain text; hiding is cosmetic.
