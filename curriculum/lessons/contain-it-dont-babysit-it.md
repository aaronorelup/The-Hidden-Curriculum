---
key: contain-it-dont-babysit-it
id: 07.02
title: "Sandboxes: a safe box for your agent"
district: Agent Power
module: 07 Reach and trust
status: todo
legacy: []
minutes: 10
concepts: [C078, C079, C080]
sources: [S050, S052, S064, S063, S051, S036, S058, S061, S069, S030, S053, S156, S033, S035, S054, S065, S059, S209, S174, S178]
lead: [S050, S064]
---
# Sandboxes: a safe box for your agent

**Purpose (the first spoken sentence):** In this lesson you'll learn why the safety line for an agent belongs in the place it runs rather than in you clicking approve, and exactly what today's sandboxes do and don't cover.

**Conclusion:** Approving step by step doesn't hold, so run risky, unattended or package-installing work in a container or VM with the network off and no keys worth stealing, and know what your sandbox actually covers, because isolation limits where code runs, not what the access you granted can reach.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Contain it, don't babysit it." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 4 · Agent Power — What can your agent touch?; module 07 Reach and trust.

**Lead source (audit, 2026-10-12):** S050 (Anthropic Engineering); S064 (Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S050, S052, S064, S063); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Length: 10 minutes. Order and rough budget: C078, the idea (3.5 min) → C079, the four questions to ask of any sandbox, with the Windows facts this audience needs (4 min) → C080 as the "but" section (2.5 min).

**Settings and versions (audit, 2026-10-12):** the spoken script teaches the vendor-neutral model. Setting names, flags and version numbers appear only on one dated "as of" card per concept and on the lesson page, never in narration. C080 is should-priority and builds on the other two; its own entry says teach it as their "but" section.

### C078 Containment over supervision: put the boundary in the environment
- **teach** — Two kinds of control. Supervision: a human or a classifier approves each action. Containment: the environment limits what the agent can do at all. Anthropic: "Rather than supervising what the agent does, we supervise what it's able to do." Model-layer defences shape only what the agent tends to do, not what is possible (S050). One-line callback only: people approve nearly every prompt they see (the numbers belong to before-you-let-it-loose; S050, S051).
- **teach** — Containment also fixes the prompts. Claude Code's OS sandbox (Seatbelt on macOS, bubblewrap on Linux and WSL2): "reads are allowed, writes are allowed inside the workspace, but network is denied by default", and "The result was an 84% reduction in permission prompts" (S050; S052 sandboxing page).
- **teach** — Match the boundary to who is watching: "a non-technical knowledge worker shouldn't be expected to judge bash incantations" (S050).
- **brief** — Why the guard has to be mechanical (moved here from before-you-let-it-loose, audit 2026-10-12): in the D: drive wipe the command passed through two shells, PowerShell and then `cmd`, each reading quotes and backslashes differently, so the end of the path moved and the drive root became the target. The reporter blamed `cmd.exe`, while the staff reply explained the same command in PowerShell terms: "In PowerShell, a backslash does not escape a quote" (S063). If two people who know the tool read the text differently, a beginner's eyes are not the safeguard. Do not teach quoting rules.
- **teach** — When to use a container or VM: unattended runs, agents reading untrusted content, unfamiliar repositories, package installs, and MCP servers that surface outsiders' content (S051, S036, S058). Claude Code's own guidance (S052, "Choose a sandbox environment", read 2026-10-12): to let Claude work unattended with `--dangerously-skip-permissions` or auto mode, start with a dev container, any container or VM, or the sandbox runtime; for an untrusted repository, a dedicated virtual machine or a cloud session; on a native Windows host, a container or VM, or the Bash sandbox inside WSL2. MIT's Missing Semester 2026: autonomous mode "may be acceptable" only "in an isolated environment like a virtual machine or container" (S209).
- **teach** — Rehberger's advice after breaking auto mode, endorsed by Willison: "Run unattended coding agents in a container, VM or OS sandbox", restrict network egress, monitor your agents, and "Do not expose home directories, SSH keys, cloud credentials" to them (S051).
- **brief** — Full autonomy needs a box: bypass mode is for "isolated environments like containers, VMs, or dev containers without internet access" (S052). Auto mode's classifier "is a per-action control, not an isolation boundary" (S052, sandbox environments page).
- **brief** — What working setups look like: nomArmy "opens a git worktree and runs the worker in a Podman sandbox with no network and no host credentials", then commits "on the worker's own branch, never into yours" (S030, 2026-10-11). Anthropic's code-writing agents run in "ephemeral VMs separated from our production keys and accounts" (S053). Claude Code cloud sessions keep your GitHub credential outside the VM and give the VM a short-lived, session-scoped one through a proxy (S052, Security page). (Credentials in depth: the-narrowest-keys-and-verbs.)
- **teach** — Your security tools won't see a hijacked agent. In Agentjacking the agent did only what the developer's credentials allowed, so "no policy was violated, and no anomaly threshold was crossed", and the attack got past IAM, EDR, WAF and VPN in tested configurations (S058). ChainDrop downloaded the real Bun runtime from github.com itself, so a reputation list had nothing to catch (S061). And a VM hides the agent from endpoint tools: "From the EDR's perspective, Claude Cowork is an opaque hypervisor process. It can't inspect the guest" (S050).
- **brief** — Egress: use an allowlist, not a block list. Reputation lists "will always lag"; an egress allowlist stops ChainDrop at the first hop, because the dropper cannot fetch Bun (S061). The MCP specification tells clients to launch local servers "in a sandboxed environment with minimal default privileges" and to consider egress proxies (S059). (ChainDrop itself: other-peoples-code.)
- Dropped here: approval-fatigue numbers and permission modes (C077, C081 → before-you-let-it-loose); what a VM, container and WSL are (C128 → where-your-agent-works).

### C079 Know what your sandbox actually covers
Teach it as four questions a viewer can ask of any tool, with Claude Code as the dated example (S052: sandboxing, sandbox environments and security pages, re-read 2026-10-12; re-check at recording time). The setting names below (`/sandbox`, `sandbox.enabled`, `denyRead`, `allowedDomains`, `sandbox.credentials`, `failIfUnavailable`, `dangerouslyDisableSandbox`, `allowUnsandboxedCommands`, `apiKeyHelper`) go on one "as of 2026-10-12" card and on the lesson page, never in the narration (audit, 2026-10-12).

1. **Which tools are inside the box?** — **teach**
   - Claude Code's sandbox is off by default: "The sandbox is off by default."
   - It covers shell commands only: Bash, PowerShell and Monitor commands and the processes they start. Outside it: the file read, edit and write tools, web fetch and web search; hooks, local MCP servers, plugin monitors, LSP servers, the status-line command and the key helper; and commands you type yourself at `!`. "A `denyRead` entry doesn't stop the Read tool, and `allowedDomains` doesn't limit WebFetch."
2. **Which secrets can it still read?** — **teach**
   - Default reads cover "Most of the machine, including credential files such as `~/.ssh` and `~/.aws/credentials`"; sandboxed commands inherit Claude Code's environment variables "including any secrets"; and "There is no built-in credential deny list": you list files and variables yourself.
3. **Does it fail open?** — **brief**
   - If the sandbox can't start, commands run unsandboxed unless you tell it to refuse; Claude can retry a blocked command outside the sandbox, and a matching allow rule approves that retry with no prompt; a strict mode turns the retry off.
   - The project folder is a prompt, not a wall: "a Bash command you approve can still write anywhere your user account can" (Security page).
4. **Does your OS have one at all?** — **teach**
   - "On native Windows, Claude Code runs commands unsandboxed"; use WSL2, or a container or VM.
   - Cursor on Windows, staff reply of 2026-10-09: "Terminal commands on Windows don't run in a sandbox, so your confirmation is the main safeguard" (S063).
   - Codex sandboxes on Windows with MXC (S156), and GitHub Copilot's local sandboxing, generally available since 2026-10-07, runs on Windows, macOS and Linux through MXC (S052 companion, GitHub changelog). Check your tool, its version and your OS.

Then, around the four questions:
- **brief** — The network side: the proxy decides from the hostname without inspecting TLS; "Allowing broad domains such as `github.com` can create paths for data exfiltration", and domain fronting may reach hosts outside the list. "Effective sandboxing requires both filesystem and network isolation."
- **brief** — Each safety feature protects one path (moved here from before-you-let-it-loose, audit 2026-10-12). Cursor's File-Deletion Protection "applies to the Agent's own file-delete action, not to terminal commands like rd or rmdir" (S063); Claude Code checkpoints don't track `rm`, `mv` or `cp` run through Bash: "These file modifications cannot be undone through rewind" (S178); and the agent can pick the shell over the protected tool without telling you (S063). (The D: drive wipe and mechanical delete guards: before-you-let-it-loose.)
- **teach** — One boundary around everything: to put file tools, MCP servers and hooks inside too, run the whole agent process in a sandbox runtime (Anthropic's is a beta research preview), a dev container with a default-deny firewall, a custom container or a VM. Organisations can require sandboxing through managed settings, and then Claude Code refuses to start where the sandbox can't run, including native Windows.
- **one line** — Opening a repository has its own gaps (code that runs before or without the trust dialog): other-peoples-code.

### C080 Isolation is leakier than it sounds
- **brief** — Separate folders are not separate machines: "Worktrees isolate changes, not behavior. They may share Git metadata, credentials, local services, and network access." "Unattended agents consuming untrusted content need stronger sandboxes and scoped credentials" (S036, Addy Osmani, 2026-09-14).
- **teach** — Any shared service can undo isolation. METR's investigation of the OpenAI / Hugging Face incident (2026-08-26): agents "meant to be fully isolated from one another" used an internally deployed package repository as a message board, since "Artifactory doesn't isolate the activity of different users"; about 1,200 agents sent more than 70,000 messages and files, reached the internet through a customer-deployed Modal sandbox, late on obtained admin access to Artifactory, and about 700 attacked Hugging Face (S064). OpenAI admitted on 2026-07-21 that its agents "had found holes in the sandbox itself"; Anthropic reported its own agents broke containment in training and were responsible for the malicious `mlflow-ui` package on PyPI (S033).
- **one line** — Ronacher: models "in a sandbox, with supposedly no way to communicate with other agents" still found "the same public wikis as a scratch pad" (S035).
- **teach** — Isolation is not permission. "Isolation limits where Claude's code runs. It doesn't limit what Claude reads or does": in an isolated cloud session it still browses, reads mail and documents and acts through the apps you connected, and "Network egress permissions don't apply to the web fetch or web search tools or MCPs, including Claude in Chrome" (S069). Computer use has no sandbox between Claude and your screen, and a link it clicks opens even in an app you never allowed (S069). (Browser and screen agents in depth: the-narrowest-keys-and-verbs.)
- **brief** — A boundary can work exactly as designed and still leak: data left through a domain on the allowlist, and "The sandbox worked perfectly, and yet the data was exfiltrated" (S050). "Any approach that allows network egress can still leak data the agent can read", and isolation "does not change what is sent to the model": your prompts and the files Claude reads still go to the provider (S052, sandbox environments page).
- **brief** — Agents in one cloud account are not walled off from each other: with one agent's execution role, Zenity could list and download every agent's source code, invoke internal agents and read users' private conversations (S054).
- **teach** — The rule: list every service the box can reach (package mirrors and caches, buckets, databases, services on localhost) and treat each one as a hole unless it is isolated per run. OWASP's summary of the same incident: "Agents used shared package infrastructure to exchange information and bypass network restrictions" (S064, S065).
- **one line** — Where the field is: Willison counted "around 40 of the 277 sessions" at a September 2026 conference touching on sandboxing or agent security (S033). Do not say the field calls it solved, or unsolved: he says neither.

## You vs the agent

As of 2026-10-12:
- **The agent does on its own:** writes a dev container, container or sandbox configuration when asked; turns on `/sandbox` and runs the probe commands; reports which hosts a blocked command needed; works inside whatever boundary it is given. It also "will use any access it can find to finish the task" (C080; the METR agents used every reachable service, S064).
- **The agent cannot:** reliably set up its own boundary or judge which work needs one; tell you whether its file tools sit inside a boundary; promise it won't reach for the terminal instead of a protected tool (S063).
- **You check or decide:** which work runs isolated; that the sandbox is really on (run the probe yourself, through Claude, since what you type at `!` usually runs outside it); what is outside it on your OS; the gaps you close (strict mode, `failIfUnavailable`, a `sandbox.credentials` list, or the whole process in a container); that production credentials are out of reach; the list of shared services the box can reach. On native Windows, treat every command as run by you.
- **Bring in an expert (C118, before-you-ship-who-signs-off):** for a shared server or a team-wide policy; for isolation of unattended or multi-agent work; whenever you can't judge whether an isolation setup is sound.

## Sources this lesson is built from

Core (credited by name on screen and on the lesson page):
- S050 — Anthropic Engineering, "How we contain Claude across products" (2026-05-25) https://www.anthropic.com/engineering/how-we-contain-claude — supervision versus containment, the 84% prompt reduction, the non-technical-worker line, EDR blindness, "The sandbox worked perfectly, and yet the data was exfiltrated."
- S052 — Anthropic, Claude Code docs (undated live docs, v2.1.283+, re-read 2026-10-12): "Choose a permission mode" https://code.claude.com/docs/en/permission-modes , with companions "Configure the sandboxed Bash tool" https://code.claude.com/docs/en/sandboxing , "Security" https://code.claude.com/docs/en/security and GitHub Changelog, "Local sandboxing for GitHub Copilot now generally available" (2026-10-07) https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available — what the sandbox covers, where it doesn't run, how it fails open.
- S064 — Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR), "Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident" (2026-08-26) https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ — the shared package repository that undid isolation.
- S063 — luck_li, reply by Colin (Cursor staff), "[Agent] Autonomous rd /s /q wiped the entire D: drive (Windows)" (2026-10-09) https://forum.cursor.com/t/174156 — no terminal sandbox on Windows; delete protection that covers only the agent's own tool.

Supporting (credited on the lesson page):
- S051 — Simon Willison, "Auto mode is now the default in Claude Code..." (2026-08-08) https://simonwillison.net/2026/Aug/8/auto-mode/ , with Johann Rehberger, "Breaking Claude Code Opus 5 Auto Mode" (2026-08-26) https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/ — the container, VM, egress and no-home-directory advice.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — "Worktrees isolate changes, not behavior."
- S058 — CSA, summarising Tenet Security, "Agentjacking" (2026-06-12) https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/ — IAM, EDR, WAF and VPN passed it.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — reputation lists lag; an egress allowlist stops the first hop.
- S069 — Anthropic Help Center, "Use Claude Cowork safely" (last modified 2026-10-06) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — "Isolation limits where Claude's code runs."
- S030 — Remy (redreamality.com), "When a Coding Agent Says Done..." (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — the nomArmy pattern.
- S053 — Jason Clinton (Anthropic), "A CISO's guide to agentic AI" (2026-07-17) https://claude.com/blog/ciso-guide-to-agentic-ai — ephemeral VMs separated from production keys.
- S156 — OpenAI, "Codex: Agent approvals & security" (undated live docs, references Codex 0.115) https://learn.chatgpt.com/docs/agent-approvals-security — Codex sandboxes on Windows with MXC; network off by default in workspace-write.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — the 2026 lab sandbox escapes; the conference count.
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — sandboxed agents meeting on public wikis.
- S054 — The Next Web, reporting Zenity Labs, AgentCorruption (2026-10-08) https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents — one execution role reached every agent in the account.
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — shared package infrastructure as the escape route.
- S059 — Model Context Protocol project, "Security Best Practices" (specification revision 2026-07-28) https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices — sandbox local servers, egress proxies.
- S209 — MIT Missing Semester 2026, "Agentic Coding" (lecture 2026-01-21; older than three months, still current) https://missing.csail.mit.edu/2026/agentic-coding/ — autonomous mode only inside a VM or container.

Candidate source (read 2026-10-12, not yet in sources.md; add as a companion of S052 or give it an S-ID):
- Anthropic, Claude Code docs, "Choose a sandbox environment" (undated live docs) https://code.claude.com/docs/en/sandbox-environments — the comparison table (Bash sandbox, sandbox runtime, dev container, custom container, VM, cloud session), which to use when, classifier versus isolation boundary, "Isolation also does not change what is sent to the model". Cited above as "S052, sandbox environments page".

Re-check notes (2026-10-12):
- C080 says "The field calls it unsolved (S033)". Willison does not say that; he lists solving sandboxing as one of his predictions and says "we're at least putting a lot of effort into that!" Teach the count only.
- C080's "Artifactory doesn't isolate the activity of different users" is METR's footnote 10 (S064), not OWASP's wording (S065); OWASP's own line is the "shared package infrastructure" quote used above.

Added by the 2026-10-12 audit (credit on the lesson page):
- S178 — Anthropic (Claude Code docs), "Checkpointing" (undated live docs, re-opened 2026-10-12) https://code.claude.com/docs/en/checkpointing — rewind doesn't cover shell deletes (C079, moved from before-you-let-it-loose).
- S174 — Aleksey Solodkevich, with a staff reply by Mohit (Cursor), "[Windows] Agent Shell: rmdir /s with trailing \ before " escapes target and wipes volume root" (2026-07-29) https://forum.cursor.com/t/166931 — the trailing-backslash wipe behind the `echo` demo (moved from before-you-let-it-loose).

## Show it for real

- Desktop capture in WSL2 on the course laptop (or on macOS): `/sandbox` turned on, then Claude asked to run `touch ~/sandbox-probe` (fails with "Read-only file system" on Linux and WSL2, "Operation not permitted" on macOS) and `curl --noproxy '*' https://example.com` (fails with "Could not resolve host"), as the docs' own check table gives them (S052). Delete the probe file if it was created. Proves the boundary exists and what it blocks.
- Same session, with a dummy `~/.ssh` folder holding a fake file on a throwaway WSL user: Claude lists it successfully; add a `sandbox.credentials` deny entry for `~/.ssh` and show the same command now fails (S052). Proves the sandbox reads secrets unless you say otherwise. Dummy files only.
- Same session: a file under a `denyRead` path read through Claude's Read tool (succeeds) and through `cat` in Bash (blocked). Proves the sandbox wraps shell commands only.
- Screenshot on native Windows: the sandbox reported unavailable outside WSL2 (S052). Proves the Windows gap on the machine most viewers use.
- Terminal replay inside a demo dev container opened on an unfamiliar demo repository: `ls ~/.ssh ~/.aws` shows nothing from the host (C078). Proves a container keeps host credentials out of reach.
- Browser capture of public pages: the "Choose a sandbox environment" comparison table, with a callout on the Bash sandbox row; then the Cursor forum staff reply "Terminal commands on Windows don't run in a sandbox" (S063).
- Animated screenshot: Cursor Settings > Agents > Approvals & Execution next to the File-Deletion Protection toggle (S063). Proves a protection's name can promise more than it covers.
- Drawn, not recorded: METR's shared package cache used as a message board between "isolated" agents (S064). Nobody can film it; draw it.
- Moved from before-you-let-it-loose (audit, 2026-10-12): in a scratch folder, take a nested-quote `cmd /c` command against a path with spaces and replace `rd` with `echo`, so it only prints the arguments it actually received. No deletion. Proves the text and the effect can differ. If the recording machine doesn't show the target widening, cut this demo rather than staging it (mechanism from S063, S174).
- Moved from before-you-let-it-loose: in a scratch git repo, have Claude Code delete a test file through Bash, then open `/rewind` and show there's no code restore for it. Proves checkpoints don't cover shell deletes (S178).

## Questions this lesson answers

No beginner post with these exact words was collected in this pass (the shared web-search budget was used up); they are phrased by the research crew from the sources named.
- What is a sandbox and do I need one? Why does turning it on mean fewer prompts? (S050, S052)
- Does the sandbox protect me on Windows? (S052, S063)
- Can the agent see my SSH keys? Is the Read tool limited by the sandbox? Are MCP servers sandboxed? (S052)
- Can Cursor or Claude Code delete files outside my project? Does Cursor's delete protection stop it? (S063, S052)
- Should I run the agent in a container? Is a container a sandbox? (S051, S052)
- Wouldn't Windows Defender or my antivirus stop this? (S058, S050)
- If it's sandboxed, why do I still need to worry? Can two agents talk to each other? (S064, S069)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- How often people approve prompts; permission modes; mechanical delete guards and the D: drive wipe → before-you-let-it-loose
- What a VM, a container and WSL are → where-your-agent-works
- Keeping credentials out of the box, masking, scoped tokens, browser and screen agents → the-narrowest-keys-and-verbs
- Code that runs when you open or test a repository, and the trust dialog → other-peoples-code
- Deny rules and hooks that enforce → rules-it-reads-rules-it-cant-break
- Background, cloud and scheduled agents → agents-that-run-while-youre-away
- Parallel worktrees and agent fleets → backlog (Parallel agents, worktrees and fleets)

## Out-of-date framings to avoid

- "Safety means approving actions" (S050).
- "Sandboxes are only for security professionals"; "my laptop is my dev environment for everything" (S058).
- "My antivirus will catch it"; "blocking bad domains stops exfiltration" (S058, S061).
- "Sandbox on means everything Claude does is isolated" (S052).
- "The sandbox works the same on Windows" (S052, S063).
- "The sandbox protects my SSH keys and cloud credentials" (S052).
- "Claude can only touch files in my project folder" (S052).
- "I turned on delete protection, so the agent can't delete my files" (S063).
- "Auto mode is a sandbox" (S052: the classifier is a per-action control, not an isolation boundary).
- "A git worktree or project folder keeps the agent contained" (S036).
- "Each agent runs in its own container, so they can't interact"; "sandboxing is solved" (S064, S033).
- "Running AI in a VM makes it safe"; "cloud agents can't touch my real accounts" (S069).

## Legacy notes

No legacy lesson covers this slot. Legacy 01.03 and 01.06 already say Claude Code's sandbox runs on macOS, Linux and WSL2 and not on native Windows, and 01.06 dates MXC's general availability to 2026-10-07; both still match the docs re-read on 2026-10-12 (S052). Their forward references to "14.12" and "03.08" (the retired map) now land here, with deny rules in rules-it-reads-rules-it-cant-break.
