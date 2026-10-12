# research-change: 01.03 Folders, paths & the working directory
Checked 2026-10-08. Lens: last five years (about 2021 to 2026).
Status tags: established / new this year / beta or announced / speculation.
Source dates are the dates shown in the source. "undated" means the page showed no date in what was fetched.

## 1. Path basics (absolute vs relative)
- The idea is stable. Microsoft still defines a full path as starting from a drive or root, and a relative path as resolved against the current directory. Status: established.
  - https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation (undated)
- Python's open() and most file APIs resolve a relative name against the process working directory, not the folder of the script. Status: established.
  - https://docs.python.org/3/using/cmdline.html (current docs; `-c` and `-m` put the current directory first on sys.path)

## 2. Windows separators and drive letters (C:\ vs /)
- Windows APIs and PowerShell accept forward slashes as well as backslashes. Status: established (long-standing behaviour; not re-fetched this session).
- Git Bash (MSYS) rewrites arguments that start with a single slash into Windows paths, so `/c/Users` is the Git Bash spelling of `C:\Users`. Arguments that already contain `C:` are passed through. Status: established in secondary sources; the MSYS2 runtime docs were not reached.
  - https://docs.cloudbees.com/docs/cloudbees-cd-kb/latest/cloudbees-cd-kb/kbec-00420-stopping-path-conversion-for-git-bash (undated)
  - Fix when needed: MSYS_NO_PATHCONV=1 on one command. Status: established in secondary sources.
- Claude Code on native Windows uses Git Bash for its Bash tool when Git for Windows is installed. Without it, Claude Code uses PowerShell. Status: established (current docs).
  - https://code.claude.com/docs/en/setup (current; prompt shows `PS C:\` in PowerShell and `C:\` in CMD)
- WSL puts Windows drives under `/mnt/c`. Status: established (long-standing; not re-fetched).

## 3. Long-path limit (260 characters, MAX_PATH)
- Since Windows 10 version 1607 (2016), the old MAX_PATH limit is removed only when BOTH the system setting LongPathsEnabled is 1 AND the app's manifest declares longPathAware. Status: established.
  - https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation (undated)
  - Process reads the registry value once; restart the process after changing it. Status: established as a third-party note.
  - Enabling the setting does not help apps not built for long paths. Status: established (vendor statement).

## 4. Working directory: how it is inherited and how agents change it
- A child process inherits the working directory from the process that started it. A relative path therefore depends on where the program was launched. Status: established (OS behaviour, long-standing).
- Claude Code (Bash tool): a `cd` in the main session carries over to later Bash commands while it stays inside the project or an additional directory. Subagent sessions never carry working-directory changes over. Status: established (current docs).
  - https://code.claude.com/docs/en/tools-reference (current; the page's dated release notes were not visible)
- Claude Code additional directories: `--add-dir`, `/add-dir`, or `permissions.additionalDirectories` add write and read access outside the launch folder. Status: established (current docs; the permissions page is the source the tools reference links to).
  - https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration (anchor from current tools reference)
- Codex CLI: `--add-dir` adds writable roots for one session while the main working directory stays the same. The example is `codex --cd apps/frontend --add-dir ../backend`. Status: established as a docs mirror; verify against the official Codex sandboxing page before quoting.
  - https://developers.openai.com/codex/llms-full.txt (mirror; date not shown)

## 5. Agent sandboxes and the working directory as a boundary (new in the last year)
- Anthropic announced Claude Code sandboxing about 2025-10-20, alongside Claude Code on the web (beta, Pro and Max). The filesystem boundary is the current working directory: the sandbox lets commands read and write there and cannot modify files outside it. Status: established (announcement).
  - https://anthropic.com/engineering/claude-code-sandboxing (post title "Beyond permission prompts: making Claude Code more secure and autonomous")
  - https://simonwillison.net/2025/Oct/20/claude-code-for-web/ (2025-10-20)
- Current writes allowed inside the sandbox: the working directory, a per-user temp directory, and any `--add-dir` directories. Status: established (current docs).
  - https://code.claude.com/docs/en/sandboxing (current)
- The sandbox is macOS, Linux and WSL2 only. Native Windows runs shell commands without the sandbox; use WSL2 for it. Status: established (current docs).
  - https://code.claude.com/docs/en/sandboxing (current); https://code.claude.com/docs/en/setup (current)
- Inside writable folders, the sandbox still denies writes to config Claude Code loads and runs: `.claude/` settings, skills, agents, hooks, `.mcp.json`, and in the working directory only `.bashrc`, `.zshrc`, `.gitconfig`, `.vscode`, `.idea`, and `hooks`/`config` in `.git`. Status: established (current docs).
  - https://code.claude.com/docs/en/sandboxing (current)
- Anthropic's company-reported figure: sandboxing cut permission-prompt fatigue by 84%. Status: company-reported, not independently verified. Do not use as a fact in the lesson without a hedge.

## 6. Shell defaults
- macOS: zsh has been the default login and interactive shell since macOS Catalina (10.15). Announced at WWDC, June 2019; shipped in the fall of 2019. Bash is still installed. Status: established.
  - https://support.apple.com/en-au/HT208050 (undated fetched page; Catalina release 2019)
  - Reason for the switch (Bash GPLv2 licence): informed speculation, not stated by Apple. Status: speculation.
- Windows PowerShell 7: PowerShell 7.5 reached general availability 2025-02-12, built on .NET 9. It installs next to Windows PowerShell 5.1 as `pwsh.exe`. Status: established.
  - https://devblogs.microsoft.com/powershell/announcing-powershell-7-5-ga/ (2025-02-12)
- Support dates conflict across sources. One analyst report says 7.5 is supported until May 2026 (past). One Polish source says 7.4 LTS and 7.5 lose support 2026-11-10, and that 7.6 LTS shipped 2026-03-18. The 7.6 date is from one non-Microsoft source. Status: beta or unverified; check learn.microsoft.com before using any date.
  - https://www.directionsonmicrosoft.com/reports/powershell-7-5-generally-available-under-standard-support/ (2025-04-13)
  - https://kluczesoft.pl/wiedza/koniec-wsparcia/powershell-5-1-koniec-wsparcia (undated)
- Windows PowerShell 5.1: no new features per the same source; no official Microsoft page confirmed here. Status: unverified.

## 7. Python and the directory a script runs from
- Python 3.11 added the `-P` option and the `PYTHONSAFEPATH` environment variable. They stop Python from putting the current directory (for `-m`, `-c`, REPL) or the script's directory at the front of sys.path. Status: established (added in 3.11, released in 2022).
  - https://docs.python.org/3/using/cmdline.html (current docs)
  - Commit history: https://github.com/python/cpython/pull/92361 (no date fetched)
- The default has not changed: without `-P`, a script's own folder goes on sys.path first, and `-m` and `-c` use the current directory. Status: established.
- `-I` (isolated mode, added in 3.4) implies `-P`. Status: established.
- Trap for the lesson: Python's import path and open() use different rules. Imports use sys.path (script folder or current folder); open() uses the current working directory. Status: established.

## 8. Windows executable search and the current folder
- `NoDefaultCurrentDirectoryInExePath` is an environment variable Windows checks with `NeedCurrentDirectoryForExePathA`. When it is set, cmd.exe does not search the current directory for a bare executable name. A name containing a backslash always includes the current directory. Status: established.
  - https://learn.microsoft.com/windows/win32/api/processenv/nf-processenv-needcurrentdirectoryforexepatha (undated)
- The history of the variable (added in Vista) comes from one comment in a Go issue. Status: unverified.
- Practical rule: a program run by bare name in a folder can pick up a file from that folder on Windows. This is the current-folder security concern the lesson can name without detail. Status: established.

## 9. Storage and folder placement
- Windows Dev Drive is a ReFS volume set up for development. It is set at format time and cannot be converted later. Status: established.
  - https://learn.microsoft.com/windows/dev-drive (current)
- Performance claim: "up to 30%" file-system improvement in build I/O scenarios, shown at Build 2023. Vendor claim for specific scenarios. Status: announced, scenario-specific.
- Do not put this in the lesson unless a hedge is used; the lesson does not need Dev Drive.

## 10. Operating-system support and the path world
- Windows 10 support ended 2025-10-14. Windows 10 machines get no more security updates unless enrolled in ESU (paid). Status: established.
  - https://pureinfotech.com/windows-10-support-ends-october-14-2025/ (2025-10-14 deadline)
  - https://www.guru3d.com/story/microsoft-officially-ends-windows-10-support-today-october-14-2025/ (2025-10-14)
- Claude Code system requirements now list Windows 10 1809+ (and Windows Server 2019+). Status: established.
  - https://code.claude.com/docs/en/setup (current)

## 11. Agents in the terminal: when they arrived
- Claude Code launched as a terminal-first beta research preview in late February 2025 (coverage dated 2025-02-27). It ran on native Windows only through WSL at launch. Status: established (launch coverage). Later milestones: general availability is reported as 2025-05-22 by a secondary source. Status: unverified.
  - https://devclass.com/2025/02/27/anthropic-previews-claude-code-agentic-coding-capable-but-costly/ (2025-02-27)
- Claude Code on the web (cloud sessions): October 2025. Status: established.
- Codex CLI: open-source, terminal-run coding agent launched 2025-04-16 (TechCrunch). Status: established.
  - https://techcrunch.com/2025/04/16/openai-debuts-codex-cli-an-open-source-coding-tool-for-terminals (2025-04-16)
  - Windows is experimental with WSL recommended. Status: reported by a secondary source dated 2026-04. Verify before use.
- Five years ago (2021) there was no mainstream terminal coding agent. Working-directory questions came from the person typing commands. Status: established (general knowledge; no source needed for the lesson's "then vs now" line; keep it qualitative).

## 12. The durable part of the model (did NOT change)
- A path is an address. Absolute paths start from the root of a drive (or `/` on Unix and macOS). Status: established.
- Every running process has a current working directory. It is set when the process starts and inherited by its child processes. A relative path is measured from it. Status: established.
- The same relative name can point to different files in different working directories. This is the root of "file not found" and "works on my machine". Status: established.
- A `cd` changes only the shell or agent session that ran it. Sub-processes and subagents do not change their parent. Status: established (Claude Code docs say subagent sessions never carry over; the general rule holds for all processes).
- The separator and the drive letter are naming conventions. The operating system decides what the name means. Status: established.
- `..` means the parent folder and `.` means the current folder. Status: established.
- `~` is a shell expansion to the home folder (Unix shells; PowerShell `~` expands to the user profile; Windows has no `~` in cmd). Status: established. Note: `~` is expanded by the shell, not the program; a quoted `"~/x"` may not expand in some tools. (Not re-fetched; stable general behaviour.)

## 13. Forward links from this lesson (check they still hold)
- 01.04 hidden files: a path can point at dot-files and `.venv` on Windows and Unix alike. Status: established.
- 02.03 moving around in a terminal: `cd` and what the prompt shows. Status: established; PowerShell prompt shows `PS C:\...`. Status: established (Claude Code docs quote this prompt form).
- 05.02 running a file: interpreters and imports depend on working directory and sys.path, as in section 7. Status: established.

## Traps: things commonly said that are now wrong or incomplete
1. "Windows paths are limited to 260 characters." Wrong since 1607 when both the system setting and the app manifest opt in. Still true for apps that did not opt in.
2. "Only Linux uses forward slashes." Windows APIs and PowerShell accept `/`. Git Bash rewrites `/c/...` into `C:\...`.
3. "Python imports from the current folder by default, so the script works in any folder." Python 3.11 added `-P` and `PYTHONSAFEPATH` to stop that. The default still includes the current folder for `-m` and `-c`, and the script's folder for a script.
4. "Bash is the default terminal on a Mac." zsh has been the default since macOS Catalina (2019). Bash is still installed.
5. "Windows 10 is still supported." Support ended 2025-10-14. Claude Code's native Windows install still runs on Windows 10 1809+ as listed in its docs; no security updates from Microsoft without ESU.
6. "Claude Code's sandbox protects Windows." The sandbox runs on macOS, Linux and WSL2 only. Native Windows runs commands unsandboxed.
7. "The agent knows which folder it is in, so I don't need to." The agent's folder is the launch folder plus `--add-dir` directories, and a `cd` in the main session carries over. Check which folder and which project the agent is in; subagents do not carry the change.
8. "The sandbox only blocks writes outside the folder." Inside the folder, the sandbox still denies writes to config files that Claude Code loads and runs (`.claude/`, `.mcp.json`, `.bashrc`, `.gitconfig`, hooks, `.git/hooks`).
9. "PowerShell 5.1 is the current PowerShell." PowerShell 7.x installs separately as `pwsh.exe`. 7.5 is GA since 2025-02-12. Exact support end dates conflict across sources; check learn.microsoft.com.
10. "Relative paths are relative to the file they're written in." Most tools resolve them against the working directory of the process. Python's sys.path is the one place where a script's folder matters, and only for imports.
11. "Codex or Claude Code can only see the folder I opened." Both can add more directories (`--add-dir`), with different access rules. Claude Code's additional directories give access but not configuration.
12. "The sandbox stops everything." Excluded commands run outside it (`sandbox.excludedCommands`). Docs warn that a broad pattern can let an excluded command run a script the agent wrote in the working directory.
13. "Anthropic says sandboxing cut prompts by 84%." That is a company-reported internal figure. Hedge it or cut it.
14. "Long paths just work now." They need the registry setting and the app manifest; processes read the setting once, so restart after changing.
