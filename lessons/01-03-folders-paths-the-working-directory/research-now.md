# research-now: Folders, paths & the working directory (as of 2026-10-08)

Status tags: established / new this year / beta or announced / speculation / unsourced (needs a source before use).

## 1. Absolute and relative paths; separators

- Windows API: a local path is drive letter, colon, backslash, then names. "File I/O functions in the Windows API convert "/" to "\" ... except when using the "\\?\" prefix." Status: established. Source: https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation (page updated 2025-04-15).
- Because relative paths cannot use the "\\?\" prefix, relative paths are always limited to MAX_PATH total. Status: established. Same source.
- In "\\?\" paths you cannot use "/" as separator, "." for current directory, or ".." for parent. Status: established. Same source.
- Drive-letter form C:\ and POSIX form / are two spellings of the same idea (a root). Status: unsourced in this pass.
- "~" as home folder (on Windows, typically C:\Users\<name>): Status: unsourced in this pass. Git Bash / WSL spelling of C:\ (for example /c/ or /mnt/c/): unsourced in this pass.

## 2. Path length limit (Windows)

- Default MAX_PATH is 260 characters. Opt-in to long paths needs BOTH the registry value HKLM\SYSTEM\CurrentControlSet\Control\FileSystem LongPathsEnabled = 1 AND the app's manifest longPathAware = true. Status: established. Source: same MS page.
- Registry value is cached per process after first use; a reboot may be needed. Status: established. Same source.
- With "\\?\" the total is about 32,767 characters (approximate; component limit commonly 255). Status: established. Same source.
- Git has its own long-path switch (core.longpaths); apps such as Explorer and some Office features still struggle past 260. Status: established (third-party vendor note only; treat as "some apps still fail"). Source: https://www.den4b.com/docs/books/renamer/page/long-paths (secondary; not verified against Git docs this pass).

## 3. Working directory inheritance (general, stable)

- Python: with "python script.py", sys.path[0] is the script's own directory; with an interactive prompt or stdin it is the empty string. Status: established. Source: https://docs.python.org/3/library/sys.html (sys.path section; quoted via search result, page not fetched this pass).
- Python "-m": the starting working directory is placed in sys.path, and a CPython change (bpo-33053 / GH-6231) altered what that means so later os.chdir() calls do not change imports. Release version not confirmed. Status: established behaviour, version unconfirmed. Source: https://git.joshthomas.dev/mirrors/cpython/commit/d5d9e02dd3c6df06a8dd9ce75ee9b52976420a8b (mirror; verify on python.org before quoting).
- Docs disagree on -c vs -m (issue42483): with -c, sys.path[0] is an empty string; with -m it is a full path. Status: established. Source: https://mail.python.org/archives/list/docs@python.org/thread/WVPG6MVA4J4LCFIAGER5ZHERAFWJ65G5/
- Practical rule: use the script's own location (os.path.dirname(os.path.abspath(__file__))) rather than assuming the shell's folder. Status: established. Same Python sources.

## 4. Claude Code: how the Bash and PowerShell tools handle the working directory

- A cd in the main session carries over to later Bash commands only while the new path stays inside the project directory or an additional directory added with --add-dir, /add-dir, or additionalDirectories. Status: established (current docs; page undated in fetch). Source: https://code.claude.com/docs/en/tools
- Subagent sessions never carry over working-directory changes. Status: established. Same source.
- A cd outside the allowed directories resets to the project directory and appends "Shell cwd was reset to <dir>" to the tool result. Status: established. Same source.
- Environment variables do not persist between Bash calls; CLAUDE_ENV_FILE or a SessionStart hook can populate them. Status: established. Same source.
- CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1 makes every Bash command start in the project directory. Status: established. Same source.
- A cd inside a command moved to background does not carry over ("Session cwd remains <dir>"). Status: established. Same source.
- The PowerShell tool follows the same main-session reset rule, including CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR. Status: established. Same source.
- Community bug reports (not official): cwd resets between tool calls even inside the project, a June 2026 report says Bash and PowerShell reset to the primary working directory between every command; still open at time of search. Status: beta or reported bug, not confirmed. Sources: https://claudeissues.com/issue/72339-bug-working-directory-resets-between-tool-calls ; https://claudeissues.com/issue/42837-bash-cwd-no-longer-persists-between-calls-regression-even-without-claude-bash-ma ; https://claudeissues.com/issue/42844-can-no-longer-tell-claude-to-change-its-working-directory-mid-session-regression (one reported issue was closed 2026-05-29 per search summary).
- Reported: a custom statusLine command in settings.json was linked to cwd resets. Status: reported, unconfirmed. Source: https://claudeissues.com/issue/31471-custom-statusline-command-resets-shell-cwd-between-bash-tool-calls
- Practical workaround in the bug threads: absolute paths or "cd /path && command" in one call. Status: reported practice. Same sources.

## 5. Claude Code: worktrees (separate working directories)

- A git worktree is a separate working directory with its own files and branch, sharing history and remote with the main checkout. Status: established. Source: https://code.claude.com/docs/en/worktrees (undated page; cites v2.1.xxx versions).
- Start in a worktree: claude --worktree <name> (or -w). Default location: .claude/worktrees/<name>/ at repo root, on branch worktree-<name>. Status: established. Same source.
- EnterWorktree tool lets Claude switch into a worktree mid-session; entering a path outside .claude/worktrees/ now asks for approval (changed before v2.1.206, when it did not). Status: new this year. Same source.
- Subagent frontmatter isolation: worktree gives each spawn its own worktree; auto-removed if no changes. Status: new this year (doc-described; version not stated in the text read). Same source.
- Hook paths: ${CLAUDE_PROJECT_DIR} stays at the project root; the hook input "cwd" follows Claude's current directory. Status: new this year (doc-described). Same source.
- Worktrees share the .git directory and project-scope plugins; approvals saved in one worktree go to the main checkout's settings.local.json (from v2.1.211). Status: new this year. Same source.
- Worktrees isolate file edits only; they do not isolate processes or ports. Status: established (doc says "They isolate file edits"). Same source.

## 6. Codex CLI: the agent's writable folder (OpenAI)

- Defaults (current page, undated in fetch): no network by default; write permission limited to the active workspace. On launch, Codex checks whether the folder is under version control: version-controlled folders get the Auto preset (workspace-write with on-request approvals); other folders start read-only. Status: established (current docs). Source: https://learn.chatgpt.com/docs/agent-approvals-security (redirect from https://developers.openai.com/codex/agent-approvals-security).
- Workspace = the working directory plus temporary directories such as /tmp; /status shows the directories in the workspace. Status: established. Same source.
- Outside the workspace, Codex asks for approval to edit files or run network-needing commands. Status: established. Same source.
- .git (as a directory or a file) is protected read-only inside writable roots, recursively; same for .agents and .codex directories where present. Status: established. Same source.
- Flags --cd <path> and --add-dir <path> set the working root and add writable roots. Status: unsourced from an official page (only third-party guides). Source (secondary): https://tutorialsdojo.com/openai-codex-cheat-sheet/
- Security history: CVE-2025-59532. In versions 0.2.0 to 0.38.0 a model-generated cwd could be treated as the sandbox writable root; fixed in 0.39.0 by anchoring the boundary to where the session started. Status: established (past, 2025). Source: https://osv.dev/vulnerability/CVE-2025-59532
- Older OpenAI-mirrored docs said the CLI is read-only until a directory is marked trusted. Status: superseded or disputed; do not present as current. Source (secondary): https://tutorialsdojo.com/?p=39354

## 7. MCP roots (how clients tell servers which folders matter)

- Roots are informational guidance, not an access-control mechanism; the protocol does not enforce that servers stay within them. Status: established. Source: https://modelcontextprotocol.io/specification/2026-07-28/client/roots (fetched; same text in the 2025 revisions).
- Roots are a file:// URI list returned by roots/list. Status: established. Same source.
- DEPRECATED as of protocol version 2026-07-28 (SEP-2577). Remains in spec at least 12 months after that revision. New implementations SHOULD NOT adopt; migrate to passing directories or files via tool parameters, resource URIs, or server configuration. Status: new this year. Same source.
- Roots are not a server's cwd; the spec does not define mapping a root to a process working directory. Status: established (spec silent). Same source.

## 8. Cursor agent terminal (current, reported)

- Reported bug: the agents window opened terminals in the first workspace folder rather than the active one; staff reply says a fix shipped after the report, version not named. Workaround: cd into the project. Status: reported, fix unconfirmed. Source: https://forum.cursor.com/t/terminal-working-directory-fails-to-follow-active-workspace-changes/160383 (version 3.3.30 cited in the thread). Also reported to affect WSL workspaces.
- Cursor CLI changelog (June 29, 2026): repeat --add-dir to add directories at launch, including with --workspace; /add-dir refreshes skills and commands. Status: new this year. Source: https://cursor.com/docs/cli/changelog.md
- Multi-root workspaces (v3.2, April 24, 2026, per a third-party aggregator; not verified against Cursor's own changelog). Status: new this year, unverified. Source: https://www.havoptic.com/blog/deep-dive-cursor-q2-2026 (secondary).

## 9. Windows shells: Windows PowerShell 5.1 vs PowerShell 7.x

- Windows PowerShell 5.1 is the version that ships in Windows. It uses the full .NET Framework (Windows only). Microsoft no longer adds features to it; support follows the Windows version. Status: established. Source: https://learn.microsoft.com/en-us/powershell/scripting/what-is-windows-powershell (updated 2025-11-21).
- PowerShell 7 is built on modern .NET and runs on Windows, Linux and macOS. Status: established. Same source.
- PowerShell 7.6 GA announced March 18, 2026; described as the next LTS release, built on .NET 10 (LTS). The post gives no support end date. Status: new this year. Source: https://devblogs.microsoft.com/powershell/announcing-powershell-7-6/
- Support end date for 7.6 (one analyst article says November 2028): not confirmed against Microsoft lifecycle page. Status: unverified. Source (secondary): https://www.analyticsinsight.net/technology/what-is-powershell-features-uses-and-why-powershell-7-matters-in-2026
- Coexistence of 5.1 and 7.x on one machine: stated by a secondary guide; not confirmed by Microsoft page read this pass. Status: unverified.

## 10. Lantern: agents and the folder they are standing in

- Claude Code runs commands with the project directory as its home base; a cd can reset (see section 4). Status: established.
- Codex's sandbox writable area is the folder the session started in (see section 6); CVE-2025-59532 showed the boundary must be anchored to where the session started. Status: established.
- Worktrees give an agent its own folder and branch (section 5). Status: established.
- Speculation: agents will keep resolving paths for the user. Status: speculation (not sourced). Keep to "agents resolve paths for you; you still need to know which folder the agent is in and whether it is the project you think."

## Traps (commonly said, now wrong or incomplete)

- "The terminal's folder is the project folder, always." Claude Code's shell cwd can reset to the project directory when a cd leaves the allowed directories; subagents never inherit a cd. Source: https://code.claude.com/docs/en/tools
- "cd persists, so set it once." Community reports say cwd resets between calls; use absolute paths or "cd X && cmd" in one call. Source: claudeissues links in section 4 (reported, not confirmed).
- "Environment variables set in one command carry to the next." Claude Code docs: they do not persist. Source: https://code.claude.com/docs/en/tools
- "Windows paths are capped at 260 characters." Default yes; opt-in via registry and manifest; "\\?\" lifts the OS limit. Source: MS path-limit page.
- "PowerShell 7.4 is the current LTS." Outdated: 7.6 GA March 18, 2026 is the new LTS. Source: https://devblogs.microsoft.com/powershell/announcing-powershell-7-6/
- "Windows PowerShell 7 is the one that ships with Windows." Wrong: Windows ships 5.1; 7.x is installed separately. Source: https://learn.microsoft.com/en-us/powershell/scripting/what-is-windows-powershell
- "MCP roots keep a server inside a folder." Informational only, and deprecated as of 2026-07-28. Source: https://modelcontextprotocol.io/specification/2026-07-28/client/roots
- "Codex starts in read-only mode everywhere." Current docs: version-controlled folders get workspace-write with on-request approvals. Older docs said read-only until trusted. Source: https://learn.chatgpt.com/docs/agent-approvals-security
- "A git worktree is a copy of the folder." It is a separate working directory on its own branch sharing one .git history. Source: https://code.claude.com/docs/en/worktrees
- "python -m ... imports from the current folder" as a settled rule. Behaviour changed (bpo-33053 / GH-6231) and docs disagree; do not state it as fixed. Source: CPython mirror commit above.
- "Mention Cursor's agent terminal always opens the active workspace." Reported bug with a fix whose version is unknown. Source: https://forum.cursor.com/t/terminal-working-directory-fails-to-follow-active-workspace-changes/160383

## Gaps for the planner
- Unsourced this pass: "~" home folder, C:\ vs / equivalence, Git Bash /c/ mapping, WSL /mnt/c mapping. Needs one more search before scripting.
- Claude Code tools page is undated in fetch; use "as of 2026-10-08" wording.
