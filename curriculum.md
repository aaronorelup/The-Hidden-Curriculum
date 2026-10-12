# The Hidden Curriculum — Master Curriculum

The "hidden curriculum": everything working developers are assumed to know that nobody formally teaches.
**Conceptual, not how-to.** Each lesson builds a mental model (what it is, where it lives on the map,
what it's like, what it connects to, what will surprise you) so nothing is confusing when you meet it.
See `COURSE.md` for the lesson contract. Live at aaronorelup.com/courses/the-hidden-curriculum/ ("for Dummies" is a Wiley trademark).

Each lesson = one animated video: ~5 min for orientation and each module's first lesson, ~10 min mid-module, 20 min max (COURSE.md). IDs are stable once a lesson is published; the daily job takes the first `todo` in order.

Status key: `todo` · `scripted` · `narrated` · `animated` · `published`  (proof-of-concept builds don't change status)

The map: **Start** (00) · six districts, each a run of modules — **1 The Machine** (01–03) · **2 The Code** (04–07) · **3 The History** (08) · **4 The Network** (09–13) · **5 Trust** (14–16) · **6 Shipping** (17–20) · **Finish** (21, the capstone).
The `# District` headings below are read by `tools/publish.py` (the site draws the map from them) and must match engine/map.js.

AI is not a district: it is the lanterns strung over every district (COURSE.md). Lessons whose subject is AI sit in the
district they belong to and are listed here; the course page marks them with a lantern. Keep this list in sync when IDs change.
Lantern lessons: 00.04 00.05 00.06 01.10 01.11 01.12 01.13 03.08 03.09 03.10 06.06 06.07 07.07 08.11 08.12 10.06 10.08 10.09 10.10 10.11 10.12 10.13 10.14 10.15 10.16 12.04 14.12 15.13 15.14 15.15 15.16 16.10 16.11 16.12 16.13 17.10 18.17 20.06 21.02

---

# Start · Orientation — what this course is, and the lantern you carry

## Module 00 — Orientation: The Map and the Lantern
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 00.01 | The hidden curriculum | CS teaches theory, IS teaches business systems; the day-to-day tooling is learned by apprenticeship, forums and breaking things | published |
| 00.02 | The map of everything | One picture: your computer → the network → the internet → services → AI, and where every later lesson sits | published |
| 00.03 | How old is all this? | A timeline from Unix (1969) to MCP (2024) — most of it is older than you think, the AI layer is brand new | published |
| 00.04 | Model vs app vs agent | GPT/Claude/Gemini (models) vs the apps wrapping them vs agents that act | published |
| 00.05 | How AI models work today | ~20 min. Five years of change: LLMs → multimodal models (see/hear/generate, some via API), diffusion models (image, video, audio; rarely text); tokens, context and why models degrade as it fills; memory and RAG (chat search, self-kept memory, files/Notion via tools); system prompts and injected instruction files (CLAUDE.md); settings (temperature, top-p...); caching and token billing (input, output, cache write, cache read); modes (chat, Cowork, Code) and platforms (web, desktop, CLI, cloud); skills vs connectors vs plugins and their marketplaces; individual vs enterprise; other surfaces (Claude Design, voice modes); personal agents (OpenClaw and similar). Brief here, own lessons later | published |
| 00.06 | Trust what you can verify | Agents now write, run and debug their own code, so hand-coding and hand-debugging are nearly obsolete; your new job is judging what you cannot see: security holes in code that works, team norms and the project's chosen libraries (AI drifts and keeps adding dependencies), and "ready to deploy" claims. You can only trust AI on what it can verify; past that, learn to check it yourself or bring in an expert | published |

# District 1 · The Machine — what's on your computer

## Module 01 — Your Computer, Under the Hood
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 01.01 | Files are just bytes | A .py file is a text file; the extension is a label that tells the OS which program opens it | published |
| 01.02 | File extensions & associations | Showing hidden extensions, renaming .txt → .py, "Open with", default apps | published |
| 01.03 | Folders, paths & the working directory | Absolute vs relative paths, `C:\` vs `/`, why "run it from the right folder" matters | published |
| 01.04 | Hidden files & dotfiles | `.git`, `.env`, `.venv`, `AppData`, `~/.config` — the invisible config layer | published |
| 01.05 | Environment variables & PATH | How typing `python` finds the right program; why "not recognized as a command" happens | published |
| 01.06 | Programs, processes & services | A program on disk vs a running process vs a background service; Task Manager tour | published |
| 01.07 | Users, admin & permissions | Admin vs standard, UAC prompts, "Run as administrator", file permissions | todo |
| 01.08 | Windows vs macOS vs Linux | Same ideas, different names: line endings, path slashes, case-sensitivity, package managers | todo |
| 01.09 | CPU, RAM, disk, GPU & VRAM | What each does and why AI cares about the GPU and its VRAM | todo |
| 01.10 | Running AI models on your own computer | Ollama, LM Studio, ComfyUI; VRAM limits; quantization | todo |
| 01.11 | The copilot zoo | OS (Windows Copilot, Apple Intelligence), browser, email, IDE (GitHub Copilot), vendor (NVIDIA app/G-Assist), Office — what each can see | todo |
| 01.12 | What AI is already on your PC? | How to inventory assistants, background AI services and their data access | todo |
| 01.13 | How image, video and sound generators work | Diffusion and flow models: noise to picture in steps; why image, video, music and voice generators work this way; diffusion for text exists but is rare | todo |

## Module 02 — The Command Line
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 02.01 | Terminal vs console vs shell vs CLI | Terminal = the window; shell = the interpreter inside it; CLI = any program you drive by typing; console = the old name | todo |
| 02.02 | The shells: cmd, PowerShell, bash, zsh, Git Bash, WSL | Which one you're in, why syntax differs, when to use each | todo |
| 02.03 | Moving around | `cd`, `ls`/`dir`, `pwd`, tab-completion, up-arrow history, opening a terminal in a folder | todo |
| 02.04 | Running programs: commands, arguments, flags | `python app.py --verbose`: program, argument, flag; `--help` | todo |
| 02.05 | Input, output, pipes & redirects | stdout, stderr, `|`, `>`, exit codes — how programs talk to each other | todo |
| 02.06 | Script files: .bat, .cmd, .ps1, .sh | Saving commands to a file; execution policy; shebangs; double-click vs run | todo |
| 02.07 | OS package managers | winget, Chocolatey, Scoop, Homebrew, apt — installing software by typing | todo |
| 02.08 | Reading errors without panic | Stack traces, "command not found", permission denied, and what each means | todo |

## Module 03 — Development Environments
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 03.01 | Text editor vs IDE | Notepad → VS Code → full IDEs; what an IDE adds | todo |
| 03.02 | VS Code tour | Explorer, integrated terminal, extensions, command palette, settings | todo |
| 03.03 | The IDE family | Cursor/Windsurf, JetBrains (PyCharm etc.), Visual Studio, Xcode, Android Studio, Unity/Godot editors — when to use which | todo |
| 03.04 | Linters, formatters & type checkers | Tools that catch mistakes before you run | todo |
| 03.05 | The debugger | Breakpoints and stepping instead of print() everywhere | todo |
| 03.06 | Notebooks | Jupyter, Colab — when notebooks beat scripts and when they don't | todo |
| 03.07 | WSL, dev containers & cloud dev environments | Linux on Windows, Codespaces, why teams standardize environments | todo |
| 03.08 | Coding agents in your editor and terminal | Claude Code, Codex, Copilot agent, Cursor — how they read, edit, run | todo |
| 03.09 | Instruction files: prompts as code | Instructions files (CLAUDE.md etc.), versioning prompts | todo |
| 03.10 | Context engineering: managing the window | Why models get worse as the window fills (context rot); compaction, clearing tool results, sub-agents, loading tools and skills on demand | todo |

# District 2 · The Code — what programs are made of

## Module 04 — Programming Languages
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 04.01 | What a programming language actually is | Human-readable instructions → something the machine runs | todo |
| 04.02 | Compiled vs interpreted vs bytecode | C/Rust/Go vs Python/JS vs Java/C# — what "runtime" means | todo |
| 04.03 | The language tour | Python, JavaScript/TypeScript, HTML/CSS, SQL, Bash/PowerShell, C/C++, C#, Java/Kotlin, Swift, Go, Rust, Lua/GDScript — what each is for | todo |
| 04.04 | Choosing a language | By target: web, AI/data, scripting, mobile, games, systems, automation | todo |
| 04.05 | Libraries, frameworks, SDKs & runtimes | Library = you call it; framework = it calls you; SDK = a vendor's toolkit | todo |
| 04.06 | Data formats | JSON, YAML, TOML, CSV, XML, Markdown — config and data files you'll meet daily | todo |
| 04.07 | Text encoding: Unicode, UTF-8 and garbled characters | Text is bytes plus an agreement: code points, UTF-8 vs UTF-16, why Ã© (mojibake) appears and how to read it (deferred from 01.01) | todo |

## Module 05 — Python & JavaScript Ecosystems (Packages)
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 05.01 | Why there are so many Pythons on your computer | Installer vs Store vs uv; multiple versions; the `py` launcher; which one "python" means | todo |
| 05.02 | What "running a file" really means | An interpreter reads your text file; the working directory decides what it can find; why imports fail from the wrong folder | todo |
| 05.03 | Virtual environments (.venv) | Per-project package boxes; activate/deactivate; why global installs break things | todo |
| 05.04 | pip, requirements.txt, pyproject.toml, uv | Declaring and reproducing dependencies | todo |
| 05.05 | Node.js, npm & npx | package.json, node_modules, scripts (`npm run dev`), npx one-offs | todo |
| 05.06 | Lockfiles & semantic versioning | 1.4.2 means what; why lockfiles exist | todo |
| 05.07 | Who can publish packages? | Anyone — PyPI/npm accounts, publishing flow, trust signals | todo |
| 05.08 | Supply-chain risk | Typosquatting, malicious packages, install scripts, how to vet a package | todo |
| 05.09 | Version managers & shims | mise, pyenv, nvm, asdf: tools that put a stand-in (shim) first on PATH and pick the version per project; why `which python` can name a shim, not the real program (deferred from 01.05) | todo |

## Module 06 — Data & Databases
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 06.01 | Why apps need databases | Beyond files | todo |
| 06.02 | SQL & relational databases | SQLite, Postgres, tables, queries | todo |
| 06.03 | NoSQL & key-value stores | Documents, KV, when they fit | todo |
| 06.04 | Hosted backends | Supabase, Firebase, Neon, Cloudflare D1 | todo |
| 06.05 | Migrations & backups | Changing a database without losing data | todo |
| 06.06 | Vector databases & embeddings | How AI "searches by meaning" (RAG) | todo |
| 06.07 | How AI apps remember | The model keeps nothing: memory is text put back in the window. Re-sent conversation, self-kept memory, chat search, memory files and connectors (Notion, Drive) via tool calls | todo |

## Module 07 — Concurrency: Doing Many Things at Once
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 07.01 | Processes vs threads | Separate houses vs roommates | todo |
| 07.02 | The event loop | One worker juggling many waiting tasks (JavaScript, Python asyncio) | todo |
| 07.03 | async / await | Writing code that waits without freezing | todo |
| 07.04 | Worker threads & worker pools | Handing heavy work to helpers | todo |
| 07.05 | Job queues & the worker loop | "Take a job, do it, report, repeat" — how render queues and AI pipelines work | todo |
| 07.06 | Race conditions & locks | Why two workers touching one thing breaks it | todo |
| 07.07 | Multi-agent orchestration | Fan-out, review, verify; cost and when it's worth it | todo |

# District 3 · The History — how work is saved & shared

## Module 08 — Git, GitHub & Agents on Git
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 08.01 | What version control is | Save points for code with a full history | todo |
| 08.02 | Git basics | repo, stage, commit, log, diff | todo |
| 08.03 | Branches & merging | Parallel timelines; merge conflicts demystified | todo |
| 08.04 | Git vs GitHub | Git = the tool on your PC; GitHub/GitLab/Bitbucket = hosting + collaboration | todo |
| 08.05 | Remotes: clone, push, pull, fork | Syncing your copy with the server copy | todo |
| 08.06 | Pull requests, issues & code review | How teams (and agents) propose changes | todo |
| 08.07 | .gitignore & never committing secrets | What stays out of the repo and why | todo |
| 08.08 | Gists | Tiny single-file repos for sharing snippets | todo |
| 08.09 | GitHub Actions (CI/CD) | Robots that test/build/deploy on every push | todo |
| 08.10 | Releases, tags & GitHub Pages | Shipping versions and free static hosting | todo |
| 08.11 | How AI coding agents use git | Agents on branches/worktrees, opening PRs, why git makes agent work safe to undo | todo |
| 08.12 | Contributing with AI: team norms and AI policies | Mixed human/AI teams: AI code drifting from conventions and the agreed libraries, open-source AI disclosure policies, reviewing AI-written pull requests | todo |

# District 4 · The Network — how computers talk

## Module 09 — Networking & the Internet
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 09.01 | LAN, WAN & the internet | Your home network vs everyone else's; router, switch, Wi-Fi | todo |
| 09.02 | IP addresses & ports | Address = building, port = apartment; private vs public IPs | todo |
| 09.03 | localhost | 127.0.0.1 — your computer talking to itself; `localhost:3000` explained | todo |
| 09.04 | Clients & servers | Who asks, who answers; any computer can be a server | todo |
| 09.05 | DNS & domains | Names → numbers; registrars, records (A, CNAME, TXT, MX) | todo |
| 09.06 | HTTP & HTTPS | Requests, responses, methods, status codes, headers | todo |
| 09.07 | TLS certificates | The padlock; Let's Encrypt; why HTTPS is free now | todo |
| 09.08 | Firewalls, NAT, port forwarding & VPNs | Why your PC isn't reachable from the internet (and how to change that safely) | todo |
| 09.09 | CDNs, latency & bandwidth | Why sites are copied worldwide | todo |

## Module 10 — APIs, Webhooks & MCP
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 10.01 | What an API is | A menu of things a program lets other programs do | todo |
| 10.02 | Web APIs & REST | Endpoints, JSON bodies, GET/POST/PUT/DELETE | todo |
| 10.03 | Anatomy of one API call | URL, method, headers, key, JSON body, status code: one request taken apart | todo |
| 10.04 | SDKs, rate limits, pagination & errors | The practical realities of APIs | todo |
| 10.05 | Webhooks | "Don't call us, we'll call you" — reverse APIs; polling vs push | todo |
| 10.06 | WebSockets & streaming | Live two-way connections; why AI replies stream token by token | todo |
| 10.07 | GraphQL & RPC (brief) | Other API styles you'll bump into | todo |
| 10.08 | MCP — Model Context Protocol | A standard plug that lets AI apps use tools; client, server, tools, resources | todo |
| 10.09 | MCP transports & installing servers | stdio (local program) vs HTTP (remote); config files; auth for remote MCP | todo |
| 10.10 | Tools, skills & MCP in practice | Giving an agent abilities | todo |
| 10.11 | Subscriptions vs API billing | Chat plans vs pay-per-token keys | todo |
| 10.12 | Plugin and skill marketplaces | Skills vs connectors vs plugins; directories, the Claude Marketplace, git-repo plugin marketplaces; every add-on is code you trust (malicious skills in the wild) | todo |
| 10.13 | Prompt caching and the token meters | Input, cache write, cache read, output; the prefix rule and what breaks a cache; time to live (5 min / 1 h); why long chats cost more each turn | todo |
| 10.14 | Multimodal APIs | Sending images, audio, video and PDFs to a model; models that generate media natively vs apps that hand off to a generator model | todo |
| 10.15 | Voice AI | Voice modes: speech-to-text, model, text-to-speech pipelines vs native speech-to-speech; turn-taking and interruptions | todo |
| 10.16 | What "Opus made this" leaves out | ~20 min, case study (Aaron asked for it out of sequence, 2026-10-03/04). Bare Opus 5.5 vs Opus connected to engines, generators and pipelines, from controlled experiments run for this lesson: what the model really did, what references, generators, songs and people supplied, its narrow default taste, that it never hears or plays its own work, and the bill (Seedance 2.5, keep ratios, the 10,000-character "one prompt"). Uses real media exhibits (first lesson with video clips and played audio) | todo |

## Module 11 — Websites & Hosting
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 11.01 | HTML, CSS, JavaScript | Structure, style, behavior | todo |
| 11.02 | Static vs dynamic sites | Pre-made pages vs pages built per request | todo |
| 11.03 | SSG, SSR, SPA & islands | The rendering acronyms explained | todo |
| 11.04 | Astro | Content-first static sites with islands of interactivity | todo |
| 11.05 | React, Next.js & friends | When you need a heavier framework | todo |
| 11.06 | Build steps & dev servers | `npm run dev` vs `npm run build`, the `dist` folder | todo |
| 11.07 | How a domain name finds your site | Registrar → DNS → host: who owns what in the chain | todo |
| 11.08 | Where to host | GitHub Pages, Cloudflare Pages, Vercel, Netlify, VPS — tradeoffs and costs | todo |
| 11.09 | Deploying from git | Push → auto-deploy; preview deployments | todo |

## Module 12 — Cloudflare & the Edge
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 12.01 | What Cloudflare is | DNS, CDN, proxy, DDoS shield in front of your site | todo |
| 12.02 | Pages & Workers | Hosting sites and running code at the edge | todo |
| 12.03 | Storage: KV, D1, R2, Durable Objects | Where edge apps keep data | todo |
| 12.04 | Workers AI & the Agents SDK | Running models and stateful agents on Cloudflare | todo |
| 12.05 | Tunnels & Zero Trust | Safely exposing localhost; protecting private apps | todo |

## Module 13 — Containers, Servers & the Cloud
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 13.01 | "Works on my machine" | The problem containers solve | todo |
| 13.02 | Docker: images, containers, Dockerfile | Recipe → packaged box → running box | todo |
| 13.03 | Volumes, ports & docker compose | Data and multiple services | todo |
| 13.04 | When to use Docker (and when not) | Servers and reproducibility yes; simple desktop scripts usually no | todo |
| 13.05 | VMs vs containers vs serverless | Three ways to rent compute | todo |
| 13.06 | The big clouds | AWS, Azure, GCP — and the simpler PaaS options | todo |
| 13.07 | Environments: dev, staging, prod | Why you don't test on live users | todo |

# District 5 · Trust — who may do what

## Module 14 — Identity, Authentication & Keys (Developer Side)
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 14.01 | Authentication vs authorization | Who are you vs what may you do | todo |
| 14.02 | Sessions & cookies | How a website remembers you're logged in | todo |
| 14.03 | API keys, app keys, secret vs publishable keys | Shared secrets; which keys may appear in a browser and which never may | todo |
| 14.04 | Tokens & JWTs | Access tokens, refresh tokens, expiry, bearer headers | todo |
| 14.05 | Public/private key cryptography | Lock anyone can close, only you can open; signing vs encrypting | todo |
| 14.06 | SSH keys | Passwordless login to servers and GitHub | todo |
| 14.07 | OAuth 2.0: the big idea | Letting an app act for you without giving it your password | todo |
| 14.08 | OAuth flows | Authorization Code + PKCE, Client Credentials, Device Code, refresh — which to use when | todo |
| 14.09 | OpenID Connect, SSO & "Sign in with Google" | OAuth + identity | todo |
| 14.10 | Scopes, consent & revoking access | Least privilege for apps | todo |
| 14.11 | Service accounts & machine identities | Logins for robots | todo |
| 14.12 | Giving agents keys safely | Scoped tokens, sandboxes, permission prompts, human-in-the-loop | todo |
| 14.13 | Signed webhooks (HMAC) | Proving a webhook really came from Stripe/GitHub | todo |

## Module 15 — Personal Security & Secrets
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 15.01 | Passwords & password managers | Bitwarden, 1Password: vaults, master password, autofill | todo |
| 15.02 | Two-factor authentication | SMS vs authenticator (TOTP) vs push vs hardware keys | todo |
| 15.03 | Passkeys | Public-key login that can't be phished | todo |
| 15.04 | Recovery codes & recovery keys | The backup door — where to keep them | todo |
| 15.05 | Hashing vs encryption vs encoding | One-way, two-way, and not-security-at-all (base64) | todo |
| 15.06 | Encryption at rest & in transit | BitLocker/FileVault, HTTPS, end-to-end | todo |
| 15.07 | Keeping app secrets out of plain text | .env + .gitignore → OS credential store → `op run`/Bitwarden Secrets Manager → cloud secret stores | todo |
| 15.08 | Environment variables: user vs system | Where they live, who can read them, what's fine to put there (paths, flags) and what isn't (long-lived secrets) | todo |
| 15.09 | Windows Credential Manager & DPAPI | The OS vault; encryption tied to a Windows account, so only that account can read it (Keychain / libsecret on Mac & Linux) | todo |
| 15.10 | The bootstrap secret problem | Every automation needs one first secret; where that one secret can safely live | todo |
| 15.11 | When a key leaks | Rotate, revoke, scan history; secret scanning | todo |
| 15.12 | Least privilege & threat modeling for solo devs | What could go wrong, and cheap defenses | todo |
| 15.13 | AI privacy & data use | What gets sent, trained on, and retained | todo |
| 15.14 | AI at work: enterprise plans and admin controls | Individual vs Team/Enterprise: SSO, admin allow-lists for connectors, plugins and skills, audit logs, retention, managed instruction files, training defaults | todo |
| 15.15 | Prompt injection and attacks on agents | Text in a page, file or email can steer an agent that reads it; why tool access turns that into real damage, and the defenses so far | todo |
| 15.16 | AI that checks code: review and security agents | What 2026 review and security agents (scanners, /security-review, autofix) catch, what they miss, and why a human still approves | todo |
| 15.17 | Dangerous files | Double extensions (invoice.pdf.exe), Mark of the Web, risky attachment types: a file's name can lie about what it does (deferred from 01.01) | todo |

## Module 16 — Running Things Without You
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 16.01 | Background processes & services/daemons | Programs with no window | todo |
| 16.02 | Scheduling | Task Scheduler, cron, scheduled cloud jobs | todo |
| 16.03 | Running without being logged in | Services, "run whether user is logged on or not", SYSTEM account | todo |
| 16.04 | The implications | Stored credentials, security, persistence, what malware does the same way | todo |
| 16.05 | Headless machines & servers | Computers with no screen; remote access (SSH, RDP) | todo |
| 16.06 | Logs & monitoring | How you find out what happened while you were away | todo |
| 16.07 | When you leave, does it break? | The "bus factor": automations tied to personal accounts; moving them to company-owned identities | todo |
| 16.08 | Windows service accounts & scheduled tasks | A login for a robot on one machine, and the scheduled tasks that use it | todo |
| 16.09 | Robot identities in the cloud | Entra ID app registrations and service principals: how a Microsoft 365 automation runs as an app instead of a person | todo |
| 16.10 | Workflow automation platforms | n8n, Zapier, Make — when no-code wins | todo |
| 16.11 | Scheduled & background agents | Agents that run daily without you | todo |
| 16.12 | Evals & cost tracking | Knowing whether your automation actually works and what it costs | todo |
| 16.13 | Always-on personal agents | OpenClaw, Hermes Agent, Meta Muse, OpenAI dots: self-hosted vs hosted assistants that act for you around the clock, and their security record | todo |

# District 6 · Shipping — getting it to people

## Module 17 — What "an Application" Is
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 17.01 | Anatomy of an app | Frontend, backend, database, storage, auth | todo |
| 17.02 | Kinds of apps | CLI, desktop, web, mobile, game, browser extension, bot, agent | todo |
| 17.03 | How executables work | Double-click → OS loads machine code; .exe, .app, ELF | todo |
| 17.04 | Turning scripts into apps | PyInstaller, Electron, Tauri, bundlers | todo |
| 17.05 | Code signing & "Windows protected your PC" | Certificates, SmartScreen, Gatekeeper, notarization | todo |
| 17.06 | Installers | What they actually do: copy files, registry, shortcuts, PATH; MSI, MSIX, Inno Setup, NSIS | todo |
| 17.07 | Updaters | Checking a server for new versions, auto-update frameworks | todo |
| 17.08 | Uninstallers | Undoing the installer; leftover AppData | todo |
| 17.09 | Desktop app stores | Microsoft Store, Mac App Store, Steam, itch.io: why distribute through a store at all (phone stores are 18.06–18.09) | todo |
| 17.10 | AI design and app builders | Claude Design, Docs and Slides, and other AI tools that build layouts, pages and apps; what they make (code, not pictures) and where the result lives | todo |
| 17.11 | Ready to ship? What to check before real users | Who can see what, secrets, costs, rollback and monitoring: the checks an agent cannot vouch for when you ask "is it ready to deploy?" | todo |

## Module 18 — Other Platforms: Phones, App Stores & Physical Devices
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 18.01 | Why cross-platform is hard | Different OSes, CPUs (x64 vs ARM), screen sizes: one program, many machines | todo |
| 18.02 | Compatibility basics | Minimum vs target OS version, API levels, backward vs forward compatibility, deprecations, CPU architectures, screen sizes and densities, "check for the feature, not the version" | todo |
| 18.03 | How a phone app is different | Sandboxes, permission prompts, the app lifecycle (the OS can pause or kill you), push notifications, battery and offline | todo |
| 18.04 | Native, cross-platform or web | Swift/Kotlin vs Flutter, React Native, .NET MAUI vs Electron/Tauri vs Unity/Godot vs installable web apps (PWAs): what each trades away | todo |
| 18.05 | The mobile toolchains | Xcode (why iOS apps need a Mac) and Android Studio; SDKs, simulators vs emulators, running on your own phone | todo |
| 18.06 | The app stores | App Store, Google Play, Microsoft Store, Mac App Store, Steam, Amazon and Galaxy stores, EU alternative marketplaces, sideloading; what each one is for and the 15–30% cut | todo |
| 18.07 | Getting your app into a store | Developer accounts and fees, identity checks, review guidelines and rejections, privacy labels and data-safety forms, beta testing (TestFlight, Play testing tracks) | todo |
| 18.08 | Signing, IDs & releasing updates | Bundle/package IDs, certificates, provisioning profiles, keystores, version numbers vs build numbers, staged rollouts; why losing a signing key is a disaster | todo |
| 18.09 | Selling inside apps | In-app purchases and subscriptions, store billing rules, why outside payment links were restricted and how that is changing | todo |
| 18.10 | VMs, emulators & cloud devices | Testing without owning the hardware | todo |
| 18.11 | CI build matrices | GitHub Actions building Mac/Linux/Windows, iOS and Android for you | todo |
| 18.12 | How physical devices work | Microcontrollers vs single-board computers (Arduino, ESP32 vs Raspberry Pi), firmware, sensors and actuators, pins | todo |
| 18.13 | Prototyping electronics | Dev boards, breadboards, power and voltage levels, the parts that let the magic smoke out | todo |
| 18.14 | Firmware & talking to devices | Flashing, serial over USB, Bluetooth LE, Wi-Fi, MQTT; the companion app on your phone | todo |
| 18.15 | From breadboard to product | Circuit boards (KiCad, ordering PCBs), enclosures, CAD and 3D printing, small-batch manufacturing | todo |
| 18.16 | Certification & selling hardware | FCC/CE marks, pre-certified radio modules, safety, crowdfunding and hardware stores | todo |
| 18.17 | AI on devices | On-device and edge AI (phone NPUs, tiny models on microcontrollers), and coding agents that write firmware | todo |

## Module 19 — Payments, Users & Selling Software
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 19.01 | Adding login to your app | Auth providers: Clerk, Auth0, Supabase Auth, Firebase Auth — don't roll your own | todo |
| 19.02 | How online payments work | Card networks, processors, never touching card numbers | todo |
| 19.03 | Stripe | Checkout, products/prices, subscriptions, test mode | todo |
| 19.04 | Merchant of record | Lemon Squeezy, Paddle, Gumroad — they handle sales tax/VAT | todo |
| 19.05 | Fulfillment via webhooks | Payment succeeded → unlock access | todo |
| 19.06 | License keys for desktop software | Issuing, validating, offline activation | todo |
| 19.07 | Legal pages | Terms of service, privacy policy, refunds, GDPR/CCPA basics | todo |

## Module 20 — Licenses & Legal
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 20.01 | Copyright is the default | No license = all rights reserved | todo |
| 20.02 | Permissive licenses | MIT, BSD, Apache 2.0 — do almost anything, keep the notice | todo |
| 20.03 | Copyleft licenses | GPL, LGPL, AGPL — share-alike obligations | todo |
| 20.04 | Creative Commons & content licenses | For art, docs, media | todo |
| 20.05 | Proprietary, EULAs & dual licensing | How closed software is licensed | todo |
| 20.06 | AI model licenses | Open weights vs open source, non-commercial licenses, output rights | todo |
| 20.07 | API terms of service | What you agree to when you use someone's API | todo |

# Finish · Capstone — one small real project, from idea to running, using every district

## Module 21 — Capstone
| ID | Lesson | Key idea | Status |
|---|---|---|---|
| 21.01 | Idea → plan | Scoping a small real product | todo |
| 21.02 | Build with an agent | Repo, venv/npm, git, secrets done right | todo |
| 21.03 | Ship it | Domain, hosting, auth, payments | todo |
| 21.04 | Run it | Logs, updates, backups, support | todo |

---

## Suggested "Season 1" fast path (~25 lessons, zero → shipped)
00.01, 01.01–01.05, 02.01–02.04, 03.02, 05.02–05.05, 08.01–08.07, 09.03, 10.01, 10.02, 15.07, 11.02, 11.08

## Timeline cheat-sheet (for 00.03)
Unix & the shell 1969–71 · Ethernet/LAN 1973 · public-key crypto 1976 · MS-DOS & .bat 1981 · DNS 1983 · the Web 1989–91 · Python 1991 · Linux 1991 · JavaScript 1995 · REST 2000 · PyPI 2003 · Git 2005 · PowerShell 2006 · OAuth 1.0 2007 · GitHub & Gists 2008 · Cloudflare 2009–10 · npm 2010 · TOTP standard 2011 · Stripe 2011 · OAuth 2.0 2012 · Python venv 2012 · Docker 2013 · VS Code 2015 · Cloudflare Workers 2017 · GitHub Actions 2019 · GitHub Copilot 2021 · Astro 2021 · ChatGPT 2022 · passkeys go mainstream 2022 · MCP Nov 2024

## Build log
- 2026-10-01: map restructured (Aaron): AI is the lanterns over every district, not a district; modules 21 (AI landscape) and 22 (AI automation) were split into the districts their lessons belong to, and the modules were renumbered so each district is one contiguous run (Start 00 · Machine 01–03 · Code 04–07 · History 08 · Network 09–13 · Trust 14–16 · Shipping 17–20 · Finish 21). Only 00.01 was published, so no live lesson changed its ID.
- 2026-09-30: proof of concept of 00.01 built as a proof of concept (promoted to the official 00.01 on 2026-10-01). 5:15, 8 scenes, 44 agents over ~2 h 7 min (3 scripts → judge → 2 fact-checkers → narrator → designer → 8 animators → 2×2 reviewers + fixes). Narrator RClayton (ElevenLabs voice library; first pick Manish Sharma hesitated and is blocked). 13,127 characters billed incl. the re-roll (final script 3,862). Render 151 s for 9,445 frames. Live: https://aaronorelup.com/course/lessons/poc-00-01-the-hidden-curriculum/ . Master MP4 in digiKam `Library/missing_map/`.
- 2026-10-01: Aaron promoted the proof of concept to the official 00.01 (folder renamed to `lessons/00-01-the-hidden-curriculum/`, the old `poc-` address redirects). Course folder moved to `My Projects/Courses/The-hidden-curriculum`.
- 2026-10-01: 00.01 re-voiced and re-rendered for the restructured map: sections 05 and 08 now say "six districts" and that the Lanterns (AI) are "not a district of its own" (same narrator, RClayton; 930 characters billed, QA 0–3% word error); the map draws six lanterns, Start/Finish and the new module numbers (service accounts shelve on 14). 5:15, render 191 s. Old takes are backed up outside the repo.
- 2026-10-01: 00.02 The map of everything published (daily job). 4:36 (276 s, 8,290 frames), render 144 s on 4 workers. Narrator Adrian - Optimistic and Clear Narrator (ElevenLabs voice library). 3,715 characters billed. 1080p master 44.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (10.9 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-02-the-map-of-everything/
- 2026-10-01: 00.03 How old is all this? published (Aaron asked for the next lesson). 5:04 (304 s, 9,121 frames), render 188 s on 4 workers. First lesson under Aaron's new standing rule: the first spoken sentence and the title card state the lesson's purpose. Narrator Ember - Warm & Conversational (ElevenLabs voice library). 3,915 characters billed. 1080p master 54.6 MB in digiKam `Library/missing_map/`; site serves the 720p copy (12.5 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-03-how-old-is-all-this/
- 2026-10-01: 00.03 revoiced with the roster narrator RClayton (Aaron's new two-voice rule): 5:17 (317 s), 3,915 characters billed, render 168 s, pushed d28b9e9. Ember master kept in digiKam as Superseded; new master `..._1080p_rclayton.mp4`.
- 2026-10-01: Module 18 widened (Aaron) to phones, app stores, compatibility and physical devices: 18.01–18.17 (was four lessons; old 18.02 cross-platform frameworks folded into 18.04, old 18.03/18.04 now 18.11/18.10). 17.09 narrowed to desktop stores. No module renumbered; the map label for 18 stays "Other platforms". Lantern list gains 18.17.
- 2026-10-01: 00.03 How old is all this? rebuilt and extended (Aaron asked for how much everything keeps changing): 10:45 (644.8 s, 19,343 frames, 15 sections), render 375 s on 4 workers, pushed abc3e10. Keeps the purpose line, the street of years and Aaron's Notepad story; adds three speeds of change (stable ideas, moving versions of git/Python/npm/VS Code, security fastest: passwords to two-factor, SMS codes to authenticator apps, device sign-in and passkeys, sign-in services) and aging encryption (MD5, SHA-1, old TLS, post-quantum). Narrator RClayton - Clear, Polished and Direct (unchanged). 15,856 characters billed. 1080p master 89.0 MB in digiKam `Library/missing_map/` as `..._1080p_extended.mp4` (Stage/Final; `..._1080p_rclayton.mp4` now Superseded); site serves the 720p copy (23.1 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-03-how-old-is-all-this/
- 2026-10-01: 00.04 Model vs app vs agent published (Aaron asked for the next lesson). 4:43 (283.2 s, 8,496 frames), render 169 s on 4 workers, pushed 930a324. Lantern lesson: the model is the engine, the app is the car, an agent is a car allowed to drive. Narrator Adrian - Optimistic and Clear Narrator (ElevenLabs voice library, roster). 4,023 characters billed. 1080p master 52.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (12.4 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-04-model-vs-app-vs-agent/
- 2026-10-02: 00.05 How LLMs work (just enough) published (Aaron asked for the next lesson). 5:30 (330.0 s, 9,899 frames, 9 sections), render 190 s on 4 workers, pushed 5701a1c. Lantern lesson: tokens, next-token guessing, the context window as a desk, temperature, hallucination as a confident wrong guess. Narrator RClayton - Clear, Polished and Direct (ElevenLabs voice library, roster). 4,191 characters billed. 1080p master 51.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (12.9 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-05-how-llms-work-just-enough/
- 2026-10-02: 00.05 rebuilt as "How AI models work today" (Aaron rejected v1 as five years out of date; new currency rule): 19:54 (1194.2 s, 35,827 frames, 20 sections, guest segment by June in sections 18-19 as a myth-or-still-true round), render 1135 s on 4 workers, pushed 58b0a41. Replaces the 5:30 tokens/temperature/hallucination lesson at the same URL with the five-year change arc: text-only LLMs to multimodal models, diffusion models, tokens and context rot, memory and RAG, system prompts and CLAUDE.md, model settings, prompt caching and token billing, modes and platforms, skills/connectors/plugins, individual vs enterprise, Claude Design, voice modes, always-on personal agents. Narrator RClayton - Clear, Polished and Direct (unchanged). 25,093 characters billed. 1080p master 157.9 MB in digiKam `Library/missing_map/` as `..._1080p_v2.mp4` (Stage/Final; v1 master now Superseded). render.py's crf-26 720p copy was 44.9 MB, over the 24 MiB Pages limit, so the site serves a two-pass 720p copy (95k video, 64k AAC, 25.1 MB). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-05-how-llms-work-just-enough/
- 2026-10-02: ten lessons added from the 00.05 rebuild's plan (topics 00.05 now only introduces): 01.13 generators/diffusion, 03.10 context engineering, 06.07 how AI apps remember, 10.12 plugin and skill marketplaces, 10.13 prompt caching and token meters, 10.14 multimodal APIs, 10.15 voice AI, 15.14 enterprise plans and admin controls, 16.13 always-on personal agents, 17.10 AI design and app builders. All Lantern lessons. render.py now two-pass encodes the 720p web copy to fit Pages when CRF 26 overshoots (long lessons).
- 2026-10-03: 00.06 How to learn anything technical published (Aaron asked for the next lesson; first lesson built with the new Research + Plan phases). 5:17 (316.9 s, 9,508 frames, 8 sections), render 413 s on 4 workers. Case-file model: read the error, search its exact words, check the official docs, brief the AI with the evidence, settle it with a tiny test; 2021 Stack Overflow loop to 2026 agents, llms.txt and docs MCP servers, invented packages and flags. Narrator Adrian - Optimistic and Clear Narrator (roster). 4,763 characters billed. Pushes 7a7cb8d and f50a440 hit a Cloudflare Workers Builds outage (status-page incident 'Workers Build failing to start', 2026-10-03); went live after Cloudflare's fix with retry commit 7de3fa2. 1080p master 43.7 MB in digiKam `Library/missing_map/`; site serves the 720p copy (12.0 MB). Review stills (28 GB across lessons) deleted; the shipper now cleans them after each publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-06-how-to-learn-anything-technical/
- 2026-10-03: 00.06 rebuilt as "Trust what you can verify" (Aaron rejected v1 as out of date: since he started using Claude Code he has not had to debug an error himself, the agent reads, fixes and re-runs its own errors; the lesson is now about the person's new role, not debugging). 11:07 (667.0 s, 20,011 frames, 16 sections), render 690 s on 4 workers (971 s wall incl. the 720p web copy). Agents write, run and debug code, so the failures that matter become invisible ones: security holes in code that runs (Moltbook Jan 2026, RedAccess May 2026 scan), the verification wall ('make sure it's secure' you cannot check: learn to check or bring an expert), team conventions and the project's chosen libraries in mixed teams, someone owning dependencies so AI does not keep adding them (supply chain), 'ready to deploy' as the same trap, and the rule: trust AI only on what can be verified, with 2026 security/review agents (beta) moving that line. Narrator Adrian - Optimistic and Clear Narrator (roster). 9,323 characters billed. Pushed 8403f7e (publish.py's live check passed on the still-cached v1 page; the new page went live about a minute later). 1080p master 92.4 MB in digiKam `Library/missing_map/` as ..._1080p_v2.mp4 (v1 master re-tagged Superseded); site serves the 720p copy (23.8 MB). Review stills deleted after publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/00-06-how-to-learn-anything-technical/
- 2026-10-03: four lessons added from the 00.06 rebuild's plan (topics 00.06 only introduces): 08.12 contributing with AI (team norms, AI policies), 15.15 prompt injection and attacks on agents, 15.16 AI review and security agents, 17.11 pre-launch checks. 00.06, 08.12, 15.15, 15.16 join the Lantern list.
- 2026-10-04: 01.01 Files are just bytes published (daily job; first lesson of District 1 · The Machine). 5:07 (307.0 s, 9,209 frames), render 274 s on 4 workers (317 s wall incl. the 720p web copy), pushed e97f7c6. Every file is a row of bytes with a name tag outside: text is bytes through a code card (UTF-8, ~99% of the web), file-type stamps (PNG, PDF, PK = zip inside .docx) are a better clue than the tag, invoice.pdf.exe shows a tag can lie, and agents now read and write these files for you. Narrator RClayton - Clear, Polished and Direct (ElevenLabs voice library, roster). 3,854 characters billed. 1080p master 52.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (12.9 MB). Review stills deleted after publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/01-01-files-are-just-bytes/
- 2026-10-07: 01.02 File extensions & associations published (daily job). 10:09 (609.2 s, 18,274 frames, 14 sections), render 338 s on 4 workers, pushed 8f2cf19. The extension is a tag in the name; the OS keeps a ledger mapping tags to apps (the porter reads the tag, never the bytes): hidden extensions, renaming .txt to .py (Aaron's Notepad story), Open with once vs always, default apps and who may rewrite them, editors' own language ledgers, .ckpt vs .safetensors, and AI tools that create files the ledger still opens. Narrator Adrian - Optimistic and Clear Narrator (roster). 8,354 characters billed (on 2026-10-05). Built 2026-10-05, paused mid-animation by the weekly usage limit, resumed today with a resume workflow (audit fixed scene 13 throwing for 25 s, two review/fix rounds, final check); the shipper agent declined to push from an automated run, so the orchestrator ran publish.py per the task's authorisation. 1080p master 85.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (23.4 MB). Review stills deleted after publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/01-02-file-extensions-associations/
- 2026-10-08: 01.03 Folders, paths & the working directory published (District 1 · The Machine, mid-module). 10:37 (637.4 s, 19,122 frames, 13 sections, 1,532 spoken words), render 532 s encode on 4 workers (637 s frame pass), pushed 58ac236. Narrator RClayton - Clear, Polished and Direct (ElevenLabs voice library, roster). 10,352 characters billed. 1080p master 72.8 MB in digiKam `Library/missing_map/`; site serves the 720p copy (21.0 MB). Review stills deleted after publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/01-03-folders-paths-the-working-directory/
- 2026-10-09: 01.04 Hidden files & dotfiles published (daily job; District 1 · The Machine, mid-module). 10:32 (632.3 s, 18,968 frames, 15 sections, ~1,600 spoken words), render 417 s on 4 workers (459 s wall incl. the 720p web copy), pushed 0c09842. Shop with a staff-only back room: dot-prefix convention on Unix and the Hidden attribute / AppData on Windows, project config (.git, .venv, .vscode) vs home-folder settings (~/.config, AppData), .env secrets in plain text and .gitignore, the AI-tool layer (CLAUDE.md, AGENTS.md, GEMINI.md, .cursor/rules, MCP config files), and reviewing what an agent changed with git status / git diff. Narrator Adrian - Optimistic and Clear Narrator (ElevenLabs voice library, roster). 9,474 characters billed. 1080p master 86.6 MB in digiKam `Library/missing_map/`; site serves the 720p copy (23.2 MB). Review stills deleted after publish. Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/01-04-hidden-files-dotfiles/
- 2026-10-10: 01.05 Environment variables & PATH published (daily job; District 1 · The Machine, mid-module). 11:22 (682.3 s, 20,469 frames, 16 sections, ~1,500 spoken words), render 9 m 08 s on 4 workers incl. the 720p web copy, 62 agents over ~89 min, pushed 18df673. Satchel copied at the door: every process gets a copy of its parent's environment; PATH as an ordered folder list where the first match wins; "not recognized as a command" and its four causes; which python ran (Store alias stub, Python 3.14 install manager); venv activation prepends PATH; why a new terminal is needed after an install; API keys in env vars and .env reach agents and everything they run (ANTHROPIC_API_KEY billing override, s1ngularity / Shai-Hulud 2025). Narrator RClayton - Clear, Polished and Direct (roster). 13,402 characters billed. The workflow's shipper declined to publish (no live user); the scheduled job ran publish.py under the task's authorisation. 1080p master 99.1 MB in digiKam `Library/missing_map/`; site serves the 720p copy (23.9 MB). Review stills deleted after publish. Added 05.09 Version managers & shims (deferred by the 01.05 plan; appended at the end of module 05 so published cross-references to 05.0x stay valid). Live: https://aaronorelup.com/courses/the-hidden-curriculum/lessons/01-05-environment-variables-path/
- 2026-10-11: 01.06 Programs, processes & services published (daily job; District 1 · The Machine, mid-module). 10:46 (645.8 s, 19,375 frames, 16 sections, ~1,600 spoken words), render 6 m 32 s on 4 workers plus the 720p web copy, 61 agents over ~107 min, pushed 458da1f. Kitchen metaphor: recipe cards = programs, cooks with PID tickets = processes, night staff = services, serving hatches = ports; Task Manager tour, closing a window is not ending a process, EADDRINUSE and Vite port-hopping, orphan vs zombie, Ollama tray app + server, MCP stdio servers as child processes, coding-agent background tasks and sandboxes, background AI services (forward to 01.12). Narrator Adrian (Optimistic and Clear Narrator), 9,962 characters billed. Engine: new opt-in `dip` transition, empty sections draw K.bg, new `pointer`/`restart` icons. Note: the ship agent rendered but refused to publish without live approval; the main session ran publish.py under the scheduled task's authorisation. Master in digiKam `Library/missing_map/`.
