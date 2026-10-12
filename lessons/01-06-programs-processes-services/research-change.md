# research-change: 01.06 Programs, processes & services
Checked 2026-10-11. Lens: the last five years (about October 2021 to October 2026), plus the durable core.
Status tags: established / new this year (2026) / beta or announced / speculation.
Source dates are the dates shown in the source. "undated" = living docs with no visible date. "not re-fetched" = from older knowledge, verify before putting it on screen.

Name checks from the orchestrator notes:
- "zombie processes" is used loosely by developers to mean *leftover / orphaned* processes (a dev server or MCP server still running after its terminal or agent closed, holding a port). A true Unix **zombie** is something narrower: a process that has already exited but whose parent has not yet collected its exit status; it uses no CPU and holds no port. Windows has no zombie state in that sense. The lesson should say "leftover" or "orphaned" and, if it uses "zombie", say it is the loose meaning. (Microsoft itself shipped a real-world "zombie Task Manager" bug in 2025, see section 2.)
- "MCP servers" = Model Context Protocol servers. A *local* (stdio) MCP server is literally a child process your AI app starts; a *remote* MCP server is a web service somewhere else.
- "Ollama" = the local model runner (ollama.com); it runs a background server on port 11434.
- "01.12" = "What AI is already on your PC?" (curriculum.md row 49).

## 1. The durable core: program vs process vs service (did NOT change)
- A program is a file of instructions on disk; a process is one running copy with its own resources. Microsoft's current definition: "Each process provides the resources needed to execute a program. A process has a virtual address space, executable code, open handles to system objects, a security context, a unique process identifier, environment variables, a priority class ... and at least one thread of execution." Status: established.
  - https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads (ms.date 2025-07-14)
- The same program can run as many processes at once (each with its own PID); one app can be many processes (browsers, Electron apps, VS Code). Status: established (not re-fetched; textbook).
- Every process is started by a parent and inherits a copy of its environment (links back to 01.05). Status: established (see 01.05 research-change section 1).
- A *job object* lets Windows manage a group of processes as a unit (this is how tools kill a whole process tree). Status: established.
  - same Microsoft page
- A Windows **service** is a process managed by the Service Control Manager: "It can be started automatically at system boot, by a user through the Services control panel applet, or by an application ... Services can execute even when no user is logged on to the system." Status: established (concept unchanged since Windows NT).
  - https://learn.microsoft.com/en-us/windows/win32/services/services (ms.date 2018-05-31, updated 2025-04-15)
- Linux: services are systemd units (`systemctl`, `journalctl`); the Unix word is "daemon". Ollama's own Linux docs still install it as `/etc/systemd/system/ollama.service` running `ollama serve` with `Restart=always` (i.e. the OS restarts it if it dies). Status: established.
  - https://docs.ollama.com/linux (undated, fetched 2026-10-11)
- macOS: launchd starts both login items and background items (LaunchAgents / LaunchDaemons). Status: established.
  - https://eclecticlight.co/2023/02/15/controlling-login-and-background-items-in-ventura/ (2023-02-15)
- Unix zombie / orphan definitions (parent must "wait" for a dead child; an orphan is adopted by init/systemd). Status: established (not re-fetched; man7.org wait(2) was unreachable on 2026-10-11).

## 2. Task Manager: what changed in five years (Windows)
- Five years ago (Windows 11 launched 2021-10-05) Task Manager still had the Windows 8/10 design. Status: established (not re-fetched).
- Windows 11 22H2 (September 2022): redesigned Task Manager (left navigation, dark mode, "Efficiency mode" to throttle a background process). Status: established.
  - https://pureinfotech.com/task-manager-new-features-windows-11-22h2/ (2022)
  - https://www.howtogeek.com/848017/windows-11-isnt-done-with-task-manager-updates/ (2022-11)
- Search/filter box (find a process by name, PID or publisher; Alt+F) arrived in preview build 22623.891 (November 2022) and shipped to 22H2 in the February 2023 update (KB5022913). Status: established.
  - https://windowslatest.com/2022/11/12/our-first-look-at-windows-11-22h2s-upcoming-task-manager-features (2022-11-12)
  - https://support.microsoft.com/kb/5022913 (2023-02-28)
- "End task" on the taskbar right-click menu: tested in Dev build 23430 (April 2023), shipped in 23H2 (build 22631.2715+, late 2023); OFF by default, turned on in Settings > System > For developers. Status: established.
  - https://bleepingcomputer.com/news/microsoft/windows-11-taskbar-has-a-hidden-end-task-feature-how-to-turn-it-on (2023)
  - https://www.elevenforum.com/t/enable-or-disable-end-task-in-taskbar-by-right-click-in-windows-11.14325/ (2023)
- CPU % changed meaning (2025): the Processes tab used to use "Processor Utility" (one busy core on a 16-core CPU could read as 100%, turbo could exceed 100%). Since the May 2025 update (24H2 KB5058411) it uses the industry-standard formula (CPU time / elapsed time x logical processors), so one busy core on an 8-core PC now shows 12.5%. Old metric remains as a hidden "CPU Utility" column on Details. Status: established.
  - https://windowslatest.com/2025/03/01/windows-11-standardizes-task-managers-cpu-usage-calculation-aligns-with-industry (2025-03-01)
  - https://windowslatest.com/2025/05/26/windows-11-24h2s-task-manager-new-cpu-usage-formula-rolls-out-to-everyone (2025-05-26)
- Real-life "zombie" lesson from Microsoft itself: after KB5067036 (2025-10-28), closing Task Manager with X did not end its process; hidden copies piled up and used CPU. Fixed in KB5068861 (November 2025). Good illustration that "window closed" is not "process ended". Status: established.
  - https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-task-manager-bug-affecting-performance/ (2025-11)
  - https://cyberinsider.com/microsoft-shares-solution-for-task-manager-zombie-problem/ (2025)
- NPU columns (2026): optional "NPU" and "NPU engine" columns on Processes/Users/Details, plus "Dedicated NPU memory" / "Shared NPU memory" on Details, and an "Isolation" column (AppContainer). Preview in KB5089573 (2026-05-26), broad rollout KB5094126 (2026-06-09), Windows 11 24H2/25H2. Hidden by default (right-click a column header). Lets you see which process is using the AI chip. Status: new this year.
  - https://www.it-connect.tech/is-your-pc-really-using-its-npu-windows-11-can-now-tell-you/ (2026-08-20)
  - https://mezha.ua/en/news/npu-in-windows-11-task-manager-309964/ (2026)
- Durable: tabs Processes (grouped Apps / Background processes / Windows processes), Details (PID, executable name), Services, Startup apps. Status: established (not re-fetched).

## 3. Background items you never started: macOS and Windows got more visible
- macOS Ventura (October 2022) moved login items into System Settings > General > Login Items with two lists: "Open at Login" and "Allow in the Background", and began notifying when an installer adds a background item. Status: established.
  - https://mjtsai.com/blog/2022/10/27/venturas-open-at-login-vs-allow-in-the-background/ (2022-10-27)
  - https://eclecticlight.co/2023/02/15/controlling-login-and-background-items-in-ventura/ (2023-02-15)
- Windows: Settings > System > AI components page (first hidden in build 26016, December 2023; visible on Copilot+ PCs) lists on-device AI models such as Phi Silica. Status: established.
  - https://pureinfotech.com/windows-11-ai-components-settings/ (2023-12-15)
- A model-management view showing each AI model's publisher, version, install date, size and usage, with Phi Silica removable, is being tested in Experimental build 26300.8553. Status: beta or announced (not shipped).
  - https://pureinfotech.com/windows-11-uninstall-ai-models-settings/ (2026-06-02)

## 4. Dev servers and "port already in use" (mostly durable, details changed)
- Durable: a dev server is a long-running process that listens on a port; only one process can hold a port; a leftover one causes `EADDRINUSE` / "address already in use". Status: established (not re-fetched).
- Vite moved its default dev port from 3000 to **5173** in Vite 3 (July 2022), to stop colliding with other tools on 3000. If the port is taken, Vite "will automatically try the next available port", so a leftover server makes the new one silently appear on 5174, 5175... (`strictPort` makes it fail instead). Status: established.
  - https://v3.vite.dev/guide/migration (2022)
  - https://github.com/vitejs/vite/commit/1cc2e2d (PR merged 2022-05-12)
- Next.js 16 (2025-10-21) made Turbopack the default for `next dev` and `next build`; Next still defaults to port 3000. Status: established (port not re-fetched).
  - https://nextjs.org/16 (2025-10-21)
- Common ports a learner will meet in 2026: 3000 (Next.js, many Node apps), 5173 (Vite), 8000 (Python), 11434 (Ollama), 1234 (LM Studio server, not re-fetched), 8188 (ComfyUI, Aaron's own setup). Status: established (11434 sourced below; others not re-fetched).

## 5. MCP servers: a new kind of child process (did not exist five years ago)
- MCP announced by Anthropic 2024-11-25; donated to the Agentic AI Foundation (a Linux Foundation directed fund, co-founded by Anthropic, Block and OpenAI) on 2025-12-09; "more than 10,000 active public MCP servers" at that point. Status: established.
  - https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (2025-12-09)
- Current spec version is **2026-07-28** (previous 2025-11-25). Two standard transports: **stdio** ("the client launches the MCP server as a subprocess") and **Streamable HTTP** (a web endpoint). Status: new this year (the version); stdio-as-subprocess is established since 2024.
  - https://modelcontextprotocol.io/specification (fetched 2026-10-11, schema 2026-07-28)
  - https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio
- Process lifecycle in the spec (good for the mental model): the client shuts a server down by closing its stdin, waiting, then force-killing (SIGTERM then SIGKILL on POSIX; TerminateProcess or Job Objects on Windows). "If the server process exits unexpectedly, the client SHOULD restart it." Servers may log to stderr. Status: new this year (wording in 2026-07-28 spec).
  - same stdio page
- 2026-07-28 made MCP stateless: no `initialize` handshake, no protocol sessions / `Mcp-Session-Id`; old HTTP+SSE transport (deprecated since 2025-03-26) formally Deprecated. Status: new this year.
  - https://modelcontextprotocol.io/specification/2026-07-28/changelog
- Security consequence: a local MCP server is code running on your machine with your permissions. Claude Code's sandbox docs say MCP servers and hooks "are separate processes that run unconstrained on the host". Status: established.
  - https://code.claude.com/docs/en/sandboxing (undated, fetched 2026-10-11)
- CVE-2025-6514 (July 2025, CVSS 9.6): the `mcp-remote` bridge, a local process, could be made to run OS commands by a malicious remote MCP server (fixed 0.1.16). Status: established.
  - https://thehackernews.com/2025/07/critical-mcp-remote-vulnerability.html (2025-07)

## 6. Local model servers (Ollama, LM Studio): background services for AI
- Ollama Windows preview 2024-02-15: "Ollama's API automatically runs in the background, serving on http://localhost:11434." Status: established.
  - https://ollama.com/blog/windows-preview (2024-02-15)
- Ollama's GUI app for macOS and Windows: 2025-07-30. Current Windows docs: after install "Ollama will run in the background"; quit it from the tray; `ollama serve` is how you run it yourself / as a service. Status: established.
  - https://ollama.com/blog/new-app (2025-07-30)
  - https://docs.ollama.com/windows (undated, fetched 2026-10-11)
- Typical surprise: starting `ollama serve` while the background copy is already running gives a bind error on 11434 (same "port in use" pattern). Status: established (third-party guides).
  - https://pinggy.io/know_your_port/localhost_11434/ (undated)
- Exposure risk: Ollama's API has no built-in authentication; Cisco found 1,139 internet-exposed Ollama servers (214 serving models) in a Shodan scan. Status: established.
  - https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama (2025-09-01)
  - https://blog.leakix.net/2026/02/ollama-exposed/ (2026-02, ~12,000 instances; counts vary by method)
- LM Studio 0.4.0 (2026-01-28) split out **llmster**, "the core of the LM Studio desktop app, but packaged to be server-native, without reliance on the GUI" (`lms daemon up`). The desktop app can also keep its server running in the tray after the window closes. Status: new this year.
  - https://lmstudio.ai/blog/0.4.0 (2026-01-28)
  - https://lmstudio.ai/docs/developer/core/headless (undated)
- Five years ago: running an LLM locally as a background server was not a mainstream thing for non-specialists; it took off after llama.cpp (March 2023) and Ollama (2023). Status: established (not re-fetched).

## 7. Coding agents spawn and keep processes (new in the last ~18 months)
- Terminal coding agents arrived in 2025: Claude Code research preview 2025-02-24, GA 2025-05-22; OpenAI Codex CLI April 2025; Google Gemini CLI 2025-06-25. Each runs shell commands as child processes of itself. Status: established.
  - https://www.anthropic.com/news/claude-4 (2025-05-22)
  - https://www.scriptbyai.com/claude-code-timeline/ (2026, secondary)
  - https://patmcguinness.substack.com/p/google-launches-gemini-cli-an-ai (2025-06)
- Claude Code background tasks (current docs): a command can run "in the background", returns a task ID; Ctrl+B backgrounds a running command; `/tasks` lists "running shells and subagents"; tasks "are automatically cleaned up when Claude Code exits"; a command that hits its timeout is moved to the background instead of being stopped. A dev server started by an agent is therefore a process owned by the agent. Status: established (features evolve monthly).
  - https://code.claude.com/docs/en/interactive-mode (undated, fetched 2026-10-11)
- Sandboxing of agent subprocesses: Anthropic "Beyond permission prompts" (2025-10-08): OS-level sandbox (Seatbelt on macOS, bubblewrap on Linux/WSL2) applies to every Bash command "and its child processes"; native Windows not supported by that sandbox. Status: established.
  - https://claude.com/resources/articles/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous (2025-10-08)
  - https://code.claude.com/docs/en/sandboxing (undated)
- The learner's job: judge what is running (which agent started it, which port, should it still be alive), not type the kill commands. Status: course stance, not a fact claim.

## 8. Background AI services on the PC (link forward to 01.12)
- Copilot+ PCs (announced May 2024) defined by an NPU of 40+ TOPS. Status: established.
  - https://learn.microsoft.com/en-us/windows/ai/npu-devices/ (undated)
- Recall: announced May 2024, pulled back for privacy redesign, made opt-in, GA on Copilot+ PCs April 2025 (KB5055627). Status: established.
  - https://bleepingcomputer.com/news/microsoft/windows-11s-recall-ai-is-now-rolling-out-on-copilot-plus-pcs (2025-04-25)
- Windows ML GA 2025-09-23: Windows itself ships and updates a shared on-device inference runtime (ONNX Runtime + execution providers for CPU/GPU/NPU). Status: established.
  - https://blogs.windows.com/windowsdeveloper/2025/09/23/windows-ml-is-generally-available (2025-09-23)
- Chrome: downloads Gemini Nano (~4 GB `weights.bin` in `OptGuideOnDeviceModel`) in the background, Google says since 2024; an "On-device AI" off switch began rolling out February 2026. Status: established (the switch: new this year).
  - https://9to5google.com/?p=714000 (2026-05-06)
- Windows agentic platform: Ignite 2025 (November) announced MCP on Windows (public preview), an On-Device Registry of "agent connectors" (MCP servers; File Explorer and Settings first), and **Agent Workspace** (agents run under their own low-privilege account in a separate desktop session). Status: beta or announced (sources disagree on private vs public preview).
  - https://techspective.net/2025/11/18/windows-becoming-operating-system-for-ai-agents/ (2025-11-18)
  - https://www.elevenforum.com/t/ignite-2025-furthering-windows-11-as-premier-platform-for-developers-governed-by-security.42138/ (2025-11)
- "Agents on taskbar" (agent tasks show progress on the taskbar): Dev/Beta build 26220.7523 (2025-12-19); Release Preview builds 26100.8313 / 26200.8313 (KB5083631, 2026-04-17). Status: new this year (rollout gradual; Microsoft 365 Copilot licence needed at first).
  - https://blogs.windows.com/windows-insider/2025/12/19/announcing-windows-11-insider-preview-build-26220-7522-dev-beta-channels/ (2025-12-19)
  - https://forest.watch.impress.co.jp/docs/news/insiderpre/2103399.html (2026-04)
- Where it is heading: OSes treating agents as first-class processes with their own accounts/identities and audit trails (Agent Workspace, Agent IDs, MCP registry); more AI work moving to the NPU, now visible per process in Task Manager. Status: speculation (direction stated by vendors, not yet general).

## 9. Five years ago vs now (one-line arc)
- ~2021: a learner meets processes mainly as "apps that froze" (Ctrl+Alt+Del, End task) and maybe one dev server on port 3000. Services were Windows' own business.
- 2022-2023: Task Manager redesign + search; macOS shows background items; Vite moves to 5173.
- 2024: local model servers (Ollama on Windows), MCP announced, Copilot+ PCs and NPUs.
- 2025: terminal coding agents start and background processes for you; MCP servers become everyday child processes; Recall GA; CPU % formula changes; agent sandboxes.
- 2026: MCP 2026-07-28 (stateless); NPU per-process columns in Task Manager; LM Studio daemon; Windows agents on the taskbar; AI-model listing/removal in Settings in testing.

## Traps (commonly said, now wrong or misleading)
- "Closing the window ends the program." False for tray apps (Ollama, LM Studio keep serving), dev servers started by agents, services, and even Task Manager itself in the KB5067036 bug (Oct-Nov 2025).
- "100% CPU on one process in Task Manager means it is using the whole CPU." Pre-May-2025 Windows could show that for one busy core; now the Processes tab uses the standard formula.
- "Vite runs on localhost:3000." Since Vite 3 (2022) it is 5173, and it hops to 5174+ if a leftover server holds the port.
- "Zombie process = a stuck process you need to kill." In Unix terms a zombie has already exited; the stuck thing holding your port is a leftover/orphaned live process.
- "Services are only Windows system stuff." AI tools now install their own background servers (Ollama, LM Studio llmster, MCP servers, Chrome's on-device model, Windows AI components).
- "An MCP server is something on the internet." A stdio MCP server is a program your AI app launches on your own machine, with your permissions.
- "MCP uses SSE / sessions." HTTP+SSE was replaced by Streamable HTTP in 2025-03-26 and is formally Deprecated; sessions and the initialize handshake were removed in 2026-07-28.
- "Local AI is private, so it is safe to leave running." Ollama's API has no authentication; thousands of instances are internet-exposed when bound beyond localhost (Cisco 2025-09-01, LeakIX 2026-02).
- "The agent's sandbox covers everything it starts." Claude Code's sandbox covers Bash commands and their children, not MCP servers or hooks, and not native Windows.
- "Task Manager shows CPU, memory, disk, GPU" as the full list. Since June 2026 it can also show NPU use per process (hidden columns).
