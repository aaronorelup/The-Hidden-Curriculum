# Plan: 01.06 Programs, processes & services

Module 01 Your Computer, Under the Hood · District 1 The Machine · mid-module, so ~10 minutes (1190–1610 spoken words; target ~1,480 words, ~635 s at about 140 words per minute). 15 sections (range 11–17). No [guest] sections (lesson is under 15 minutes).

Binding inputs: research-now.md and research-change.md (both checked 2026-10-11), COURSE.md, curriculum.md. Continuity: 01.05 (the satchel copied at the door: every program starts with a copy of its parent's environment, keys included). This lesson shows who the "programs" carrying those satchels are, how many of them are running, and which ones never go home. It does not re-teach environment variables or PATH; one callback line is enough.

## 1. Purpose line and conclusion

- First spoken sentence (purpose): "In this lesson you'll learn the difference between a program on your disk, a process that is running it right now, and a service your computer keeps running in the background with no window at all."
- One-sentence conclusion (title card, with the purpose line): "A program is a file of instructions; a process is one running copy of it, with its own number, memory and copied settings; a service is a process the operating system starts and keeps alive by itself, and most of what your AI tools run (dev servers, model servers, MCP servers, an agent's commands) is processes you never see a window for."
- Why care (scene 01, second or third sentence): "port already in use", a server that is still running after you closed everything, and an AI tool doing things in the background are all this one idea; the agent can find and stop them, but you are the one who should know what ought to be running.

## 2. As of

As of October 2026 (research dated 2026-10-11). The core (program file, running process with a PID, OS-managed service) is decades old and unchanged. What changed is who starts processes on your machine (installers, AI apps, coding agents), how many of them are AI, and how they are now fenced in. Every changing claim is dated. Machine numbers (process counts, ports, services) are observations from one laptop on 2026-10-11 and are presented that way.

## 3. Change arc (required: the lesson touches AI and security)

- Durable core (did not change): a program is a file; a process is one running copy with its own memory, process ID (PID), security context ("runs as you") and a copy of its parent's environment; one program can run as many processes at once; a service (Windows) or daemon (Unix) is a process the operating system's service manager starts, often at boot, with no window, and can restart if it dies; a server is a long-running process listening on a numbered port, and only one process can hold a given port; closing a window is not the same as ending a process.
- About five years ago (late 2021): you met processes mostly as "an app froze, open Task Manager, End task" (Windows 11 had just launched, 2021-10-05, with the old Task Manager design). Services were Windows' own business. A builder ran maybe one dev server on port 3000, in a terminal window they started themselves. Running a language model as a background server on your own PC was not a mainstream thing. Nothing on your machine started programs for you except installers and the OS.
- What changed, with dates:
  - Task Manager redesigned in Windows 11 22H2 (September 2022: left-hand navigation, Efficiency mode), search box (February 2023), taskbar "End task" option (late 2023, off by default). macOS Ventura (October 2022) started listing and notifying about background items.
  - Vite moved its default dev port to 5173 (Vite 3, July 2022) and quietly hops to 5174 if 5173 is taken.
  - Local model servers went mainstream: llama.cpp (March 2023), Ollama (2023; Windows preview 2024-02-15, serving on localhost:11434 in the background), LM Studio's headless server `llmster` (0.4.0, 2026-01-28), Microsoft Foundry Local GA (2026-04-09).
  - MCP announced 2024-11-25: a local (stdio) MCP server is a child process the AI app launches. Current spec revision 2026-07-28.
  - Terminal coding agents arrived in 2025 (Claude Code GA 2025-05-22; Codex CLI April 2025; Gemini CLI 2025-06-25). They run your shell commands as their own child processes and can keep dev servers running in the background.
  - Security caught up: MCP and local-model processes run with your permissions and your environment (mcp-remote CVE-2025-6514, July 2025; OX Security's stdio "this config is a command to run" report, April 2026; internet-exposed Ollama servers with no authentication, Cisco 2025-09-01). Agent sandboxes appeared: Claude Code's OS sandbox for commands and their children on macOS/Linux/WSL2 (2025-10-08), Codex's native Windows sandbox (2026-03-04), Microsoft Execution Containers (MXC) announced at Build 2026 and GA for process, session and WSL containers on 2026-10-07.
  - AI moved into the OS's own background: Windows ML GA (2025-09-23), Windows AI components and services, NPU per-process columns and an "Isolation" column in Task Manager (rolled out June 2026, hidden by default).
- Now (October 2026): on an ordinary developer laptop hundreds of processes run at once; a growing share are AI (model servers, MCP servers, agent shells, vendor AI services). Agents start, background, list and stop their own processes; they cannot see what other tools or you started. The OS's own roster (Task Manager, Activity Monitor, `systemctl`) is still the one place everything shows up.
- Where it is heading (hedged): operating systems treating agents as their own kind of process, with their own account, container and audit trail (MXC, Windows Agent Workspace in preview); more agents shipping inside OS sandboxes by default; more AI work visible per process (NPU columns). Say "vendors are moving toward", not "will". Do not predict that unsandboxed agents or plain localhost servers go away.

## 4. MUST-COVER list (grouped by scene, in script order)

Depth key: TEACH = a full beat with a picture; BRIEF = one or two sentences; LINE = one spoken clause or one on-screen label.
Seconds budgets sum to ~635 s (target window 510–690 s). Word counts at ~140 wpm.

Scene 01 · The point (~35 s, ~82 words)
- Purpose line and conclusion (TEACH; the purpose sentence is mandatory and comes first).
- Why care: "port already in use", the server that outlived its window, AI running in the background are one idea; agents debug it, you judge what should be running (BRIEF).

Scene 02 · Where it lives (~18 s, ~42 words)
- District 1 The Machine, pin on module 01 ("what's on your computer"). LINE: last lesson, every program left with a satchel copied at the door; this lesson meets the programs carrying them, and counts how many are out there right now.

Scene 03 · The mental model: the recipe and the cooks (~45 s, ~105 words)
- A program is a recipe card on the shelf: instructions, doing nothing (TEACH).
- A process is one cook working from that card right now, with their own ticket number (PID), their own counter space (memory) and the satchel they were handed by whoever sent them in (environment, callback to 01.05) (TEACH).
- Many cooks can work from the same card at once: one recipe, many processes (TEACH; observed: 11 `node` processes running at once on the laptop this course is made on).
- Every cook was sent in by someone: the parent (Explorer, a terminal, an editor, an agent) (BRIEF).

Scene 04 · What's really going on: what a process actually is (~45 s, ~105 words)
- The real ingredients, screen labels only: its own private memory, a PID, a security context (it runs as a user, usually you), a copy of the environment, and at least one thread (TEACH).
- Threads in one line: a process can split into several workers sharing one counter; depth is 07.01 (LINE).
- Scale: on the laptop this course is made on, 457 processes at one moment (observed 2026-10-11) (BRIEF).
- One app is often many processes (a browser, V S Code, Ollama) (BRIEF).
- Where the metaphor breaks, said plainly: a cook has judgement; a process follows its card exactly. Cooks really work side by side; a computer runs only as many at once as it has processor cores and switches between the rest very fast. And "counter space" is private: one process cannot see another's memory (TEACH).

Scene 05 · Services and daemons: the night staff (~50 s, ~117 words)
- A service is a process the operating system's own manager starts, often at boot, with no window, that can run with nobody logged in, and that the manager can restart if it stops (TEACH; the cook the building hires, not you).
- Windows: the Service Control Manager; many services share one host process, `svchost.exe`, shown as "Service Host" rows (BRIEF; observed: 97 `svchost.exe`, 324 services installed, 166 running).
- Same idea, other names: "daemon" on Mac and Linux; `systemd` units on Linux, `launchd` on Mac (LINE; depth 01.08 / 16.01).
- The in-between kind: login items / tray apps, started when you sign in and gone when you sign out (BRIEF; Ollama on Windows and Mac is one of these, not a service).
- On-screen three-column card: who starts it · has a window? · survives closing the window / signing out? for app, tray app, service (TEACH).

Scene 06 · Task Manager: the staff board (~55 s, ~128 words)
- Ctrl+Shift+Esc; it is the roster of every cook in the building (TEACH).
- Processes tab, grouped into Apps, Background processes, Windows processes (TEACH).
- Details tab: one row per process with its PID; Services tab: the service list, Running/Stopped, and which PID hosts each; Startup apps: what starts when you sign in (BRIEF).
- End task stops a process immediately; unsaved work is lost (LINE).
- New this year: optional NPU columns (which process uses the AI chip, only on PCs with one) and an Isolation column (apps running in a sandbox), hidden by default (BRIEF; hedged, see section 8).
- Same board elsewhere: Activity Monitor on Mac, `top` / `htop` and `systemctl` on Linux (LINE, screen labels).

Scene 07 · Closing the window is not ending the process (~40 s, ~93 words)
- The window is a door to the cook, not the cook (TEACH).
- Three ways a process outlives its window: tray apps that keep serving (Ollama, LM Studio), services, and children whose parent went away (BRIEF).
- On Windows, ending a parent does not automatically end its children; tools that want "stop everything I started" have to group them (Windows calls the group a job object) (BRIEF; job object as a screen label only).
- Real example: in late 2025 a Windows update made Task Manager itself keep running after you closed it, with hidden copies piling up; fixed in November 2025 (BRIEF; dated, see section 8).

Scene 08 · Servers and ports: one cook per serving hatch (~40 s, ~93 words)
- A server is a process that stays running and waits at a numbered hatch, a port, for requests (TEACH).
- Only one process can hold a port (TEACH).
- The numbers you will see, on screen: 3000 (many Node apps, Next.js), 5173 (Vite), 8000 (Python), 8188 (ComfyUI), 1234 (LM Studio), 11434 (Ollama) (LINE).
- `localhost` means your own machine; depth is 09.03, ports 09.02 (LINE).
- Observed: 27 local listeners at once on the course laptop (LINE).

Scene 09 · The surprises: "port already in use", leftovers and "zombies" (~50 s, ~117 words)
- The message, on screen: `Error: listen EADDRINUSE: address already in use :::3000` (Node), "Port 5173 is in use, trying another one..." (Vite). Meaning: a cook is already at that hatch, usually an earlier copy of the same server you thought you stopped (TEACH).
- The quiet version: Vite does not fail; it opens 5174, so two copies run and your browser may still show the old one (TEACH).
- Same pattern with Ollama: starting it again while the server (`ollama.exe`) is serving gives a bind error on 11434 (LINE).
- Words: people call that leftover a "zombie". Strictly, a zombie is a process that has already finished and is only a name left on the roster until its parent collects it; it uses nothing. The thing holding your port is alive: a leftover, or orphan, whose parent is gone (BRIEF; say which meaning).

Scene 10 · Lantern: local model servers (~45 s, ~105 words)
- A local model server is just a long-running process on a localhost port (TEACH).
- Ollama, observed on the course laptop: the tray app `ollama app.exe` is the parent of `ollama.exe`, the server on port 11434: one app, two programs, two processes (TEACH; the visual).
- It keeps the model loaded for about five minutes after the last request, so memory stays taken after you stop chatting (BRIEF).
- LM Studio has a windowless server called `llmster` (port 1234); Microsoft's Foundry Local does the same job on Windows (LINE).
- Ollama's server has no password; it is safe on localhost, not when opened to the network (BRIEF; depth 01.10, 09.08).

Scene 11 · Lantern: MCP servers are cooks your AI app hires (~45 s, ~105 words)
- A local MCP server ("stdio") is a child process your AI app launches when it starts: five servers in your config means five extra processes, often `node`, `npx`, `uvx` or `python` (TEACH).
- They inherit the app's satchel and run with your permissions (TEACH; callback to 01.05).
- The app stops them when it closes (closes their input, waits, then force-stops them) and should restart one that crashes (BRIEF).
- A remote MCP server is somebody else's process, reached over the web (LINE).
- So an MCP config line is really "run this program": treat it like installing software (BRIEF; OX Security, April 2026, hedged). Depth is 10.08 / 10.09.

Scene 12 · Lantern: coding agents start processes for you (~50 s, ~117 words)
- A coding agent runs every command as its own child process; a dev server it starts belongs to the agent (TEACH).
- Long commands go to the background with a task ID; in Claude Code, `/tasks` lists them, and they are cleaned up when it exits. Not every tool does that, so leftovers happen (BRIEF; screen label `/tasks`).
- Fences: sandboxes now limit what an agent's commands and their children can touch: Claude Code's sandbox on Mac, Linux and WSL2 (not native Windows), Codex's Windows sandbox, which also stops leftover children, and Microsoft's Execution Containers, generally available as of this week (BRIEF; hedged, see section 8).
- Callback: the Task Manager Isolation column shows some of that fencing: only AppContainer-based fences (e.g. MXC process containers), not Claude Code's WSL2/bubblewrap or Codex's sandbox users (LINE). Depth: 03.08, 14.12.

Scene 13 · Background AI already on your PC (~30 s, ~70 words)
- Some of the services you find are AI: observed on the course laptop, "Windows AI Components Host", a Codex sandbox service shown as "ChatGPT", a Copilot elevation service (BRIEF; screen labels).
- Chrome downloads an on-device model in the background (BRIEF; hedged).
- Taking inventory of them, and what each can see, is 01.12 (LINE).

Scene 14 · Your job: judge what's running (~40 s, ~93 words)
- The agent can find the process and stop it; your part is the five questions (TEACH, on-screen checklist):
  1. File, running copy, or service that comes back after a restart?
  2. Who started it (its parent: you, a terminal, an agent, a tray app, the OS)?
  3. Which port does it hold?
  4. Does it carry my keys (inherited satchel)?
  5. Is it fenced in, or running with my full access?
- The OS roster is where nearly every process shows up, whichever tool started it; processes inside WSL2 or a VM hide behind one row (LINE).

Scene 15 · Safe to ignore, and keep this (~42 s, ~98 words)
- Safe to ignore for now (BRIEF): threads and priorities, what each `svchost` row is, memorising PIDs (they change every run), Efficiency mode, Process Explorer.
- Keep this (TEACH, end card, three bold-lead takeaways; also goes in `keep:`):
  - **A program is a recipe; a process is a cook using it.** One file can be running many times, each copy with its own number, memory and satchel.
  - **Closing a window doesn't end a process.** Services, tray apps and leftover servers keep running; "port already in use" usually means an old copy is still at the hatch.
  - **Your AI tools are processes too.** Model servers, MCP servers and agent commands run as you, with your keys; know what should be running and whether it is fenced in.

Totals: 35+18+45+45+50+55+40+40+50+45+45+50+30+40+42 = 630 s, ~1,470 words.

## 5. DEFERRED (introduced here only; owner lesson)

| Topic | Depth here | Owner |
|---|---|---|
| Threads vs processes | LINE | 07.01 Processes vs threads |
| Event loops, async servers | none | 07.02 / 07.03 |
| Job queues and worker loops (render queues) | none | 07.05 |
| Multi-agent fan-out (many agent processes) | none | 07.07 |
| Environment variables, PATH, inherited keys | callback only | 01.05 (published) |
| Users, admin, "runs as you", UAC | LINE (security context) | 01.07 Users, admin & permissions |
| Daemon/service names on Mac and Linux (systemd, launchd) | LINE | 01.08 Windows vs macOS vs Linux; 16.01 |
| CPU, RAM, GPU/VRAM, NPU hardware | LINE (NPU column) | 01.09 CPU, RAM, disk, GPU & VRAM |
| Running models locally (Ollama, LM Studio, VRAM, quantization) | BRIEF | 01.10 Running AI models on your own computer |
| Inventory of AI already on the PC (Recall, Phi Silica, AI components page, Copilot) | BRIEF | 01.12 What AI is already on your PC? |
| stdin/stdout/stderr, exit codes | none (MCP shutdown described in plain words) | 02.05 Input, output, pipes & redirects |
| Stopping processes by typing (taskkill, kill, lsof, Stop-Process) | none | NEW: 02 The Command Line, "Finding and stopping processes: process trees, signals and graceful shutdown" (conceptual: SIGTERM vs force-kill, tree kill, why agents use job objects) |
| Coding agents (how they read, edit, run) | BRIEF | 03.08 Coding agents in your editor and terminal |
| `npm run dev`, dev servers vs builds | LINE | 11.06 Build steps & dev servers; 05.05 |
| Ports, localhost, clients & servers | LINE | 09.02, 09.03, 09.04 |
| Exposing a local server (firewalls, port forwarding, tunnels) | LINE | 09.08; 12.05 |
| MCP itself; stdio vs HTTP transports and configs | BRIEF | 10.08; 10.09 |
| Containers (Docker) | none | 13.02 |
| Agent sandboxes, scoped keys, permission prompts | BRIEF | 14.12 Giving agents keys safely |
| Supply-chain risk of MCP/npx packages | LINE | 05.08; 10.12 |
| Prompt injection driving an agent's processes | none | 15.15 |
| Services in depth, running when logged out, SYSTEM account, persistence/malware | BRIEF | 16.01, 16.03, 16.04 |
| Scheduled tasks | none | 16.02; 16.08 |
| Logs of background processes | none | 16.06 |
| Background/scheduled agents, always-on personal agents | none | 16.11; 16.13 |
| How an .exe is loaded | none | 17.03 How executables work |

## 6. Mental model: the recipe card and the cooks (the kitchen roster)

- One metaphor, drawn as a kitchen seen from above, that transforms scene to scene:
  - Scene 03: a shelf of recipe cards (programs). A cook steps up, takes a card, gets a ticket number (PID), a stretch of counter (memory) and a satchel handed over at the door (01.05's satchel, redrawn the same way for continuity). Two more cooks take the same card.
  - Scene 05: the night staff: cooks hired by the building manager (the OS), in grey aprons, no window, working while the front room is dark; the tray-app cook clocks in when you arrive.
  - Scene 06: the staff board on the wall becomes Task Manager: each cook is a row.
  - Scene 07: the door (window) closes; the cook is still at the counter.
  - Scenes 08–09: the back wall gets numbered serving hatches (ports); one cook per hatch; a second cook finds 5173 taken and walks to 5174; a "zombie" is a timecard left on the board with no cook.
  - Scenes 10–12: the AI cooks: Ollama's two cooks (tray and server) at hatch 11434; the AI app hiring a crew of MCP cooks when it opens; the agent as a head cook sending helpers in, some behind a glass fence (sandbox).
  - Scene 14: the full kitchen, and the viewer as the manager reading the board with five questions.
- Where it breaks (say it plainly in scene 04): cooks think, processes only follow instructions; cooks truly work in parallel, a computer runs only as many processes at once as it has cores and switches between the rest; a cook can glance at a neighbour's counter, a process cannot see another's memory; and "End task" is not a polite word to a cook, it is the cook vanishing mid-dish, unsaved work and all.

## 7. Cut list (tempting, stays out)

- Task Manager's CPU formula change (2025): a real change but low value here, and the two research files disagree on the release (May 2025 KB5058411 vs August 2025 KB5064081). Cut.
- Efficiency mode, process priority, scheduling algorithms: how-to/tuning, not the model. Efficiency mode is at most a "safe to ignore" label.
- Virtual memory, handles, DLLs, Process Explorer's tree view: power-user depth.
- `fork` / `exec`, `wait()`, SIGTERM/SIGKILL by name: mechanism detail; deferred as a NEW lesson.
- Windows' own kind of "zombie" (exited process kept alive by an open handle): accurate but a third meaning of the word; would confuse.
- MCP 2026-07-28 spec details (stateless, `initialize` removed, `server/discover`, `Mcp-Session-Id`): protocol depth belongs to 10.08/10.09.
- OX Security's figures (150 million downloads, 200,000 instances) and the CVE list: vendor numbers; keep only the hedged idea.
- Ollama exposed-server counts (1,139 by Cisco; ~12,000 by LeakIX): methods differ; say only that exposed servers have been found.
- Version numbers (Ollama 0.40.x, LM Studio 0.4, Windows build/KB numbers): they move weekly; screen and voice say the product, not the version.
- Claude Code details: 5 GB output limit, `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`, timeouts in unattended sessions: churn monthly.
- GitHub anecdotes of background tasks alive for 177–268 hours: anecdotal.
- Windows Agent Workspace, "agents on the taskbar", MCP On-device Registry: preview features on a fast track; at most deferred to 01.12 / 14.12. (If a slot is needed, one hedged clause in scene 12, nothing more.)
- Recall, Phi Silica, Copilot+ 40 TOPS, the AI components Settings page: inventory belongs to 01.12.
- Typing commands to find or kill processes (`taskkill`, `netstat`, `lsof -i :3000`, `Get-NetTCPConnection`): how-to; agents do this.
- New anecdotes about Aaron: none exist for this subject in COURSE.md's list; do not invent one. Use "the laptop this course is made on" for observed numbers.

## 8. Facts to handle carefully (and the wording to use)

- Observed machine numbers (457 processes, 97 svchost, 324 services / 166 running, 11 node, 27 local listeners, Ollama PIDs): one laptop, one moment. Say "on the laptop this course is made on, at one moment this month, ..."; never "a typical PC has".
- Microsoft Execution Containers: GA announced 2026-10-07 for process, session and WSL containers; MicroVMs still experimental; Claude Code support is "planned", not shipped. Say "Microsoft's Execution Containers, a way to fence agents in on Windows, became generally available this month; some agents use them already, others say they will." Do not list Claude Code as supported.
- Claude Code sandbox: per current docs, applies to commands and their children on macOS, Linux and WSL2; on native Windows commands run unsandboxed; MCP servers and hooks run outside it. Say "as of this month" and that it changes often.
- Claude Code background tasks are "cleaned up when Claude Code exits" (docs); other tools vary. Say "Claude Code says it cleans these up when it exits; not every tool does".
- Codex Windows sandbox: "remaining child processes stop when the foreground command exits" (docs). Say "Codex's Windows sandbox stops leftover child processes", no mode names.
- Task Manager NPU and Isolation columns: rolled out June 2026 to Windows 11 24H2/25H2, hidden by default, NPU only on PCs with an NPU (the course laptop has none). Say "newer Windows 11 builds can show ... if you switch the column on". Animate from a mock-up, not a screenshot claim of Aaron's machine.
- Task Manager zombie bug: KB5067036 (2025-10-28) made closing Task Manager leave its process running; fixed in November 2025. Say "late last year, a Windows update briefly made Task Manager itself keep running after you closed it; Microsoft fixed it in November."
- "Zombie": strict Unix meaning = already exited, waiting for its parent to collect its exit status, uses nothing; Windows has no such state in that sense. Say "people call it a zombie; strictly, it's a leftover, or orphan, still alive".
- Windows does not tree-kill by default: "ending a parent doesn't automatically end what it started" (mechanism is established; avoid claiming exactly what taskbar "End task" kills, outlets disagree).
- Ollama on Windows/Mac is a login (tray) item, not a Windows service; on Linux it is usually a systemd service. Keep-alive default 5 minutes: say "about five minutes, by default".
- Ollama has no built-in authentication: say "no password by default; fine on localhost, risky if opened to the network; researchers have found many exposed on the internet". No counts.
- OX Security (April 2026): their claim that a stdio MCP config runs its command even if no valid server starts; Anthropic called it by design and advised caution. Say "security researchers pointed out this year that a local MCP config is, in effect, a command to run; the makers call it by design and their docs say to use it with caution". No figures.
- MCP spec: current revision 2026-07-28; "the client launches the server as a subprocess" and "SHOULD restart it" if it exits unexpectedly. Say "the app should restart it", not "will".
- Windows AI Components Host (`WSAIFabricSvc`): exists and was running; Microsoft does not document its exact role. Say "a Windows service named Windows AI Components Host" and nothing about what it does.
- Codex sandbox service displayed as "ChatGPT": observed name; show as seen, do not explain.
- Chrome on-device model: Google says Chrome has downloaded Gemini Nano in the background since 2024 (about 4 GB); an off switch began rolling out in February 2026. Say "Chrome can download its own on-device model in the background; newer versions have a switch to turn it off". No size on screen unless hedged "around 4 GB".
- LM Studio `llmster` (0.4.0, 2026-01-28) and Foundry Local GA (2026-04-09): new this year; name them, no version numbers.
- Ports: 3000 / 5173 / 11434 sourced; 8000, 1234 and 8188 are common defaults (8188 is ComfyUI on Aaron's own setup). Present as "numbers you'll often see", not rules.
- Vite text: "Port 5173 is in use, trying another one..." is the current message; `strictPort` makes it fail. Show the Node `EADDRINUSE` line exactly as in research.
- Direction of travel (agents as their own kind of process with their own accounts, sandboxes by default): speculation stated by vendors. Say "vendors are moving toward ..."; never "will".
