# The Hidden Curriculum — Master Curriculum

Everyone can build almost anything with AI now. What stops people is small gaps in what they know, and those gaps move every week because the tools do. This course fills them, so you can build and do whatever you want, and it is rebuilt as the gaps change. Every lesson is a mental model, not a click-by-click tutorial: what the thing is, where it lives, what it connects to, what will surprise you, and what you must do versus what the agent does. The rule under all of it: the agent handles whatever can be verified; you check what it cannot, and when you cannot check it either, you bring in someone who can.

Lessons are built on other people's hard-won knowledge, never on what an AI assumes needs teaching. Each lesson teaches the concepts listed in `curriculum/concepts.md` (C-numbers) and is built from, and credits, the sources listed in `curriculum/sources.md` (S-numbers): courses and syllabi, practitioner essays, incident reports, surveys, standards, tool documentation and the questions real beginners ask.

Lesson numbers (00.01, 03.02...) are display only and may change as the map changes. Each lesson's key (its folder name and URL) never changes.

Something you wish you had known, a question you want answered, a source the course should be built on, or something wrong or out of date: open an issue at https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose. Each one becomes evidence for a concept, or a new one.

Status key: `todo` · `published` · `legacy` (a lesson published before 2026-10-12 covers this slot for now; it will be rebuilt later)

Lantern lessons: 00.02 00.03 00.04 02.03 03.01 03.02 03.03 04.01 04.03 05.02 06.01 07.01 07.02 08.01 08.02 09.01 09.02 09.03 10.01 11.01 11.02 12.01

---

# Start · Orientation — what is my job now?

## Module 00 — The Map and the Rule
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 00.01 | [The hidden curriculum](curriculum/lessons/the-gaps-and-the-map.md) | The biggest thing stopping you from building with AI is small gaps that move every week: since coding agents became reliable for daily work in November 2025 the job moved from typing code to directing and checking agents, and models and tools change within weeks, so this course fills the gaps, draws the map they sit on, and changes with them. | C033, C052 | S033, S081, S025, S001, S004 | legacy |
| 00.02 | [Trust what you can verify](curriculum/lessons/trust-what-you-can-verify.md) | Trust the agent on whatever a machine can check (a test passes, a page renders, a scanner runs); you own what no machine checks (security, intent, fit, ready to deploy), or bring in an expert, because fluent, agreeable answers and your own eyeballing are not evidence, and trust is set per kind of task, not per model. | C001, C005, C006, C002 | S027, S080, S040, S092, S004 | legacy |
| 00.03 | [Model, harness and agent](curriculum/lessons/model-harness-and-agent.md) | You use a model inside a harness (system prompt, tools, instruction files, memory, effort) on a surface (chat, desktop, terminal, cloud), and the harness changes results as much as the model does, so pick the surface by what the work must reach and check the harness when "it got dumber". | C021, C022 | S002, S014, S102, S249 | legacy |
| 00.04 | [What the model knows](curriculum/lessons/what-the-model-knows.md) | Knowledge is frozen in the weights with a date, the conversation exists only in a context window that is resent whole every turn (with tens of thousands of tokens you never typed), and "memory" is files the product writes and injects back, so check dates, versions and sources, and know what is on the model's desk. | C023, C024, C025 | S011, S002, S012, S105, S104 | legacy |

# District 1 · Ground Floor — what does the work stand on?

## Module 01 — Your Computer
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 01.01 | [The terminal and the agent's trail](curriculum/lessons/terminal-and-the-agents-trail.md) | The terminal is a window where a shell runs each command as you, on everything you can reach; the agent does the typing, so your skill is recognition, not syntax: read its trail for the verb (read, write, install, delete, push, send) and the target (a path, a URL, a host), and ask about anything it touched that you never named. | C122, C117 | S207, S206, S208, S069 | todo |
| 01.02 | [The folder is the agent's world](curriculum/lessons/the-folder-is-the-agents-world.md) | Every agent session starts in a folder that becomes its world (paths, the working directory, rules that climb upward), but it is not a wall: your home folder holds SSH keys and AI-tool logins, hidden dotfiles hold history, secrets and instructions out of sight but not locked, and a copy on the same drive is not a backup. | C123 | S206, S211, S176, S052 | legacy |
| 01.03 | [Environment variables](curriculum/lessons/environment-variables.md) | An environment variable is a named setting a program copies when it starts, so a change needs a new terminal, a restart or a redeploy; values live in the shell, user settings, a .env file, a hosting dashboard per environment or a container, and build-time prefixes such as NEXT_PUBLIC_ put values into what the public downloads. | C126 | S213, S212, S207 | legacy |

## Module 02 — Your Project
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 02.01 | [Git: save points and remotes](curriculum/lessons/git-save-points-and-remotes.md) | A commit is a snapshot, a branch a parallel line, a remote another copy of the history and a pull request a change you review before it lands; the agent types every git command, and you check that a remote exists, which branch is live and what a pull request changes. | C124 | S026, S212, S207, S142 | todo |
| 02.02 | [What runs where in your app](curriculum/lessons/what-runs-where-in-your-app.md) | Your app lives in several places: the browser is public, the server is where secrets and permission checks must live, the database keeps its own data and backups, and localhost, preview and production differ in URL, keys and settings, so a rollback, an env var or a webhook works only where it was set. | C125, C127, C099 | S212, S066, S026, S045 | todo |
| 02.03 | [What the agent loads](curriculum/lessons/what-the-agent-loads.md) | Before your first word the agent loads instruction files, skill descriptions, MCP tools and hooks, each costing context, and which rules a session gets depends on where the file sits, when you edited it, the kind of session and the branch it cloned, so know what each extension is, keep the files short and true, and prune the rest. | C044, C046, C049, C051, C048, C050 | S123, S015, S021, S026, S022 | todo |

# District 2 · Trust — what can act as you?

## Module 03 — Undo and Permissions
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 03.01 | [Undo has limits](curriculum/lessons/undo-has-limits.md) | Every command the agent runs acts with your full permissions, and each undo covers only part of what it can change (checkpoints skip shell deletes, rollback leaves the production database alone, a sent message cannot be recalled), so use tools that block dangerous deletes mechanically, keep a copy off the machine, check targets rather than syntax, and send, pay and publish yourself. | C097, C098, C084 | S063, S052, S225, S179, S069 | todo |
| 03.02 | [Requests and walls](curriculum/lessons/requests-and-walls.md) | A rule in CLAUDE.md or a prompt is a request; only a deny rule, a blocking hook, a sandbox, CI or a credential the agent never gets is a wall, and since people approve almost every prompt and auto mode's classifier is a filter, not a boundary, choose the mode per task and put every must-never, and every repeated correction, behind a wall you have seen fire. | C045, C081, C077, C076, C047 | S052, S051, S050, S023, S021 | todo |
| 03.03 | [Sandboxes, containers and VMs](curriculum/lessons/sandboxes-containers-and-vms.md) | Containment beats supervision: a VM, container, WSL or remote machine separates some things and shares others (mounted folders, forwarded keys, the network), and Claude Code's sandbox is off by default, covers shell commands only and does not exist on native Windows, so run risky or unattended work in a box with no credential worth stealing. | C128, C078, C079, C080, C082 | S050, S052, S064, S046, S209 | todo |

## Module 04 — What You Let In
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 04.01 | [Prompt injection and the trifecta](curriculum/lessons/prompt-injection-and-the-trifecta.md) | Everything the agent reads (issues, web pages, logs, MCP output, even from official servers) enters the same stream as your request, so anyone who can write text it reads can steer it: never let one agent hold private data, untrusted content and a way to send data out, grant the narrowest access, and ask four questions before connecting it to anything real. | C073, C074, C086, C083, C085 | S049, S058, S042, S053, S054 | todo |
| 04.02 | [Installing is running](curriculum/lessons/installing-is-running.md) | Most of a project is other people's code from registries anyone can publish to, models invent package names that attackers then register, and installing can run code at once on the machine where your keys live, so have the agent vet every new name (it exists, its age, its publisher), set a minimum release age, and never paste a command a web page gives you. | C130, C087, C088, C093 | S060, S061, S158, S062, S209 | todo |
| 04.03 | [Repos, skills and plugins run as you](curriculum/lessons/repos-skills-and-plugins-run-as-you.md) | Opening a repo can run its code before you type, "trust this folder" accepts its hooks, rules and reviewers, and skills, plugins and local MCP servers are code that runs as you and can change after you approve them, so know where each came from, read the permissions it asks for, keep a short pinned list, and review what lands in memory and rules files. | C089, C090, C091, C092, C075 | S056, S057, S160, S071, S162 | todo |

## Module 05 — Keys and Your Data
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 05.01 | [Keys are permission sets with a bill](curriculum/lessons/keys-are-permission-sets.md) | A key is a permission set with a bill attached: anything shipped to the browser is public, keys leak through agent permission files, MCP configs, logs and chat, a leaked key works until you revoke and rotate it, and budget alerts do not stop spending, so keep secret keys server-side and put a hard cap on every key. | C069, C070, C071, C061 | S020, S048, S046, S139, S140 | todo |
| 05.02 | [Where your data goes](curriculum/lessons/where-your-data-goes.md) | Your AI tools may process your files on the vendor's servers, may train on consumer chats depending on one setting and keep memory that outlives deleted chats, screen and browser agents see everything visible and act as you, and always-on personal agents hold your keys, so choose the account, settings, profile and machine before connecting anything. | C103, C104, C105 | S184, S187, S070, S189, S161 | todo |

# District 3 · Going Public — what changes once it's public?

## Module 06 — Securing Your App
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 06.01 | [Working is not secure](curriculum/lessons/working-is-not-secure.md) | AI code nearly always compiles but passes security checks only about 56% of the time, public apps get found and probed, most real flaws come from requirements nobody stated, and agents clear errors by weakening controls, so state the stakes, see every fix that touches auth, keys, grants or tests, and treat "it works" and "it's safe" as separate checks. | C062, C063, C064, C065 | S039, S038, S041, S145 | todo |
| 06.02 | [Logged in is not allowed](curriculum/lessons/logged-in-is-not-allowed.md) | Being logged in says who someone is, not what they may touch, so every request is checked on the server, and on Supabase-style backends anyone can query your tables with the public key, so test every table, view, function and storage bucket as a stranger and as a second user, after every schema change and after Supabase's 2026-10-30 default change. | C067, C068 | S044, S148, S039, S149, S216 | todo |
| 06.03 | [What you owe your users](curriculum/lessons/what-you-owe-your-users.md) | Once strangers use it you owe them more: collect less, know every copy of their data and delete it for real; cap what your AI feature lets anyone spend and treat its output as untrusted; say it is AI and ask before their data goes to an AI provider; and make it work by keyboard and screen reader, which only a person can fully check. | C119, C121, C131, C120 | S216, S055, S233, S221, S220 | todo |
| 06.04 | [Ship day: inventory and expert](curriculum/lessons/ship-day-inventory-and-expert.md) | Real users, data, money or mains power are the moment a prototype needs a production pass: inventory every route, TODO and step left to you, treat scans and AI security reviews as a floor, bring in a qualified expert with a written scope and expect a retest, and know that a person, not the agent, owns the decision to ship and the patches after. | C008, C066, C072, C118, C009 | S039, S043, S047, S214, S029 | todo |

## Module 07 — Publishing Media
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 07.01 | [Labelling AI media](curriculum/lessons/labelling-ai-media.md) | The tool's watermark is not your label: under the EU AI Act (from 2 August 2026) the tool maker marks output for machines while you, publishing professionally, must disclose it to people where they see it, AI-written public-interest text needs a responsible human fact-checker or a label, and platforms such as YouTube add their own rules on top. | C110, C111, C112, C116 | S076, S195, S198, S200, S205 | todo |
| 07.02 | [Who owns AI media](curriculum/lessons/who-owns-ai-media.md) | Your generator's plan decides what you may sell, the model's licence is a second contract even on your own machine, purely AI-made work has no US copyright unless you add and document human creative work, cloning anyone's voice or face needs written consent, and owning an output does not clear it of someone else's logo, character or trade mark. | C113, C114, C115, C132, C133 | S077, S203, S078, S235, S238 | todo |

# District 4 · Delegation — how do you direct and check?

## Module 08 — Directing
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 08.01 | [Define done before you delegate](curriculum/lessons/define-done-before-you-delegate.md) | Agents now brute-force any clearly defined goal, so most failures move upstream into what was asked: before the agent starts, write down the goal, the context only you know, the constraints, a checkable "done when" and what is out of scope, plan before coding anything bigger than a one-sentence change, and slice the work small enough to review each piece. | C034, C035, C038, C040, C041 | S008, S037, S034, S003, S036 | todo |
| 08.02 | [When it breaks, you supply the eyes](curriculum/lessons/when-it-breaks-you-supply-the-eyes.md) | Debugging moved to the agent, which reads errors, reproduces bugs and re-runs until fixed, but only on what it can run or see, so you supply a reliable reproduction, what correct looks like and a way for it to observe the result (checked once against reality), and when it loops, stop it, name the failure and change the input. | C019, C003, C042 | S094, S009, S003, S032, S117 | todo |

## Module 09 — Checking
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 09.01 | [Done is a claim](curriculum/lessons/done-is-a-claim.md) | An agent's "done, tests pass" is a claim to check (in one team's log about 1 in 11 were false) and agents shape results to pass the checks they believe exist, so accept work on records something outside the agent writes: a runner's receipt, the real diff and list of changed files, CI on another machine, and the destination itself. | C011, C012, C004 | S030, S095, S064, S087 | todo |
| 09.02 | [Their tests, their review](curriculum/lessons/their-tests-their-review.md) | Tests written in the same session as the code tend to mirror it, and an AI reviewer shares the author's blind spots, so run both on every change as a first pass, get at least one source of truth from outside that session (your cases with literal expected values, a fresh-context reviewer, the revert check), and break each guard on purpose to prove it fires. | C013, C014, C017 | S029, S030, S042, S089 | todo |
| 09.03 | [Where to spend your attention](curriculum/lessons/where-to-spend-your-attention.md) | Reading every line cannot keep up and never was the best check, so pick evidence that fits the change (tests, demos, screenshots, real use), remember that running, looking finished and being good are separate checks only people complete, be able to explain what changed, and give auth, billing, permissions, personal data and secrets a human, or an expert, on every step. | C015, C016, C007, C018 | S029, S036, S090, S007, S041 | todo |

## Module 10 — Cost and Limits
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 10.01 | [The window and the meter](curriculum/lessons/the-window-and-the-meter.md) | Every turn re-reads the whole conversation, so a filling window both degrades answers and multiplies the bill, caching discounts only an identical, still-warm prefix and breaks silently, and a stray API key can switch you from a plan allowance to per-token billing, so clear or hand off through files at natural breaks and know which meter you are on. | C026, C027, C056, C057, C055 | S016, S128, S107, S131, S018 | todo |

## Module 11 — Beyond Code
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 11.01 | [Facts, figures and circuit boards](curriculum/lessons/facts-figures-and-circuit-boards.md) | Existence is the machine's check and support is yours: make the agent verify that every link and citation exists, then read the cited passage against the claim (over 2,000 court decisions concern AI citation errors); let a separate session audit a spreadsheet's structure while you judge the business logic; and get an engineer before a board meets mains power. | C106, C107, C108, C109 | S072, S073, S074, S194, S075 | todo |
| 11.02 | [Media it can't see or hear](curriculum/lessons/media-it-cannot-see-or-hear.md) | A model that reads images is not one that makes them, the agent cannot see or hear its own media without a tool, results vary every run and converge across users, video is billed per second, resolution and retry, and a local model is a file plus a runtime plus settings, so test cheap (stills, low resolution, short clips) and keep taste for yourself or a craft expert. | C032, C030, C134, C031 | S110, S113, S244, S242, S112 | todo |

# District 5 · On Its Own — what runs while you're away?

## Module 12 — Unattended Runs
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 12.01 | [Agents that run while you're away](curriculum/lessons/agents-that-run-while-you-are-away.md) | Cloud, scheduled and event-triggered agents now run with no one watching, each with its own files, permissions and bill, and they neither stop nor wait well on their own, so list where yours run, keep scheduled work low-stakes, enforce stop rules and a budget outside the model, and fan out only once you can check one stream. | C094, C096, C095, C060 | S167, S035, S173, S019, S172 | todo |
| 12.02 | [Green is not success](curriculum/lessons/green-is-not-success.md) | Error alerts catch only runs that throw, so an expired token, a renamed field or a filter that matches nothing can "succeed" for weeks: define what a good run produces, check the output and a receipt at the destination, watch from outside with a heartbeat, and know whose account each automation runs as before that person changes role or leaves. | C100, C101, C102, C135 | S067, S180, S182, S246, S245 | todo |

# Finish · Capstone — can you take an idea live?

## Module 13 — Capstone
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 13.01 | [Capstone: idea to running](curriculum/lessons/capstone-idea-to-running.md) | One small real project walked through every district: decide whether it should exist and for whom, find what you want cheaply with throwaway mockups and the agent's questions, let it teach you the territory, then direct, check, contain, secure, ship and automate it, and judge it by outcomes its users feel, keeping enough understanding to supervise rather than counting what the agent produced. | C043, C037, C036, C020, C010 | S037, S118, S068, S082, S083 | todo |

---

## Legacy lessons (published before 2026-10-12; kept, marked, rebuilt later)
| Legacy lesson | Slug | Covers | Note |
|---|---|---|---|
| 00.01 The hidden curriculum | 00-01-the-hidden-curriculum | 00.01 | Rebuild around Aaron's 2026-10-12 core idea (the gaps move every week; the community adds them), with C033's evidence that the job moved to directing agents; the new map (Start, five districts, Finish) replaces the old six-district one. |
| 00.02 The map of everything | 00-02-the-map-of-everything | 00.01 | Its five-stop road (computer, network, internet, services, AI) is replaced by this map, which moves into the rebuilt 00.01 and every lesson's opening; not rebuilt as its own lesson. |
| 00.03 How old is all this? | 00-03-how-old-is-all-this | 00.01 | Its change arc stays; the rebuild moves the emphasis from decades of history to the pace now (models retired on about 30 days' notice, a CLI command removed 12 days after deprecation: C052). |
| 00.04 Model vs app vs agent | 00-04-model-vs-app-vs-agent | 00.03 | Add the harness as the thing that changes results (the April 2026 postmortem, S014) and the surfaces and where each runs (C021, C022). |
| 00.05 How AI models work today | 00-05-how-llms-work-just-enough | 00.04 | Rebuild at orientation length (it runs about 20 minutes): keep weights, window and memory (C023, C025), add dated knowledge and checked sources (C024); its context, caching and modes material moves to 10.01 and 00.03, plugins to 02.03, personal agents to 05.02, media models to 11.02. |
| 00.06 Trust what you can verify | 00-06-how-to-learn-anything-technical | 00.02 | Add the evidence (Karpathy's verifiability, S027; Stack Overflow 2026, S080), C005 (fluency and agreement are not evidence) and C006 (you cannot see failures you cannot evaluate); how to bring in an expert moves to 06.04 (C118). |
| 01.01 Files are just bytes | 01-01-files-are-just-bytes | 01.02 (background only) | No current concept: concepts.md's G13 notes say this gap came from the copy-from-chat workflow agents replaced. Not rebuilt as its own lesson; one line may survive in 01.02. |
| 01.02 File extensions & associations | 01-02-file-extensions-associations | 01.02 (background only) | Same as 01.01: no current concept, not rebuilt as its own lesson. |
| 01.03 Folders, paths & the working directory | 01-03-folders-paths-the-working-directory | 01.02 | Rebuilt together with 01.04 as one lesson on C123: the folder is the agent's world (rules and trust climb upward) but not a wall (the home folder holds SSH keys and AI logins), and a same-drive copy is not a backup. |
| 01.04 Hidden files & dotfiles | 01-04-hidden-files-dotfiles | 01.02 | Merged into 01.02 with 01.03; keep "hidden means out of sight, never locked" and the AI instruction files. |
| 01.05 Environment variables & PATH | 01-05-environment-variables-path | 01.03 (PATH also 01.01) | Add build-time prefixes and per-environment hosting dashboards (C126); PATH and "not recognized" move to 01.01 (C122). |
| 01.06 Programs, processes & services | 01-06-programs-processes-services | 01.01 (partly), 02.02 (partly) | No concept of its own (G13 notes): "a command starts a program" goes to 01.01, servers and functions to 02.02. Not rebuilt as its own lesson. |

## Deep-dive backlog (not scheduled)
| Topic | Concepts | Sources | Why it waits |
|---|---|---|---|
| The dials: model choice, effort, thinking tokens and subagents | C058, C059, C029, C028 | S017, S135, S138, S013, S008 | All should-priority. The mechanism they share (every turn re-reads the window; cost is context times turns times agents; caching) is taught in 10.01. C058's measured result was priced before Anthropic halved Sonnet 5.5 cache reads on 2026-10-07 (S135), so it waits for a re-run; C029 matters mostly to people building on the API. |
| Map before you change (extending an existing app) | C039 | S036, S008, S003 | Should-priority, established and medium severity; concepts.md rates it less new and less often the cause of harm than C038 and C041, which are in 08.01. |
| House style, dependency ownership and agent-friendly code | C053, C054 | S004, S029, S035, S117 | Should-priority. C053's evidence is thin (2 items, 3 sources) and needs one more current source before it carries a lesson; C054 is partly speculative and its debate is open (concepts.md). |
| Your accounts are part of your app | C129 | S212, S142, S061 | Should-priority account hygiene (2FA or passkeys, recovery codes, narrowest roles). The keys it protects are in 05.01 and the automation identity in 12.02; its beginner questions are derived, not observed, because the G13 prerequisites research batch has not run yet. |
| Physical devices in depth: from bench to product | C109, C008 | S075, S194, S251 | C109 is could-priority as a standalone lesson: one medium-severity item, and the only measured example comes from a benchmark run by an interested vendor (S194). Its high-stakes half (distributor checks, simulation, an engineer for mains) is in 11.01 and the production moment in 06.04; the EU Cyber Resilience Act scope needs a firmer source. |
| Shipping to app stores and chatbots under law | C131, C121 | S233, S234, S248 | The three duties to users are in 06.03. Store-by-store submission rules and California SB 243 wait: the SB 243 page returned HTTP 403 to the research crew and must be fetched before anything is taught. |

## Rationale

### What the order is built on

Every slot was placed by two measures taken from `concepts.md`: the cost of not knowing (the severity of the incidents, bills and losses in each concept's "Why it is a gap" and "Priority" fields) and how many batches and sources name the gap. Prerequisites then fixed the floor: 31 concepts carry a **Requires** field pointing at the G13 ground floor (`research/challenge-log.md`, finding 20), and G13's notes say it is "taught first". The order that results is: Start, the ground floor the later lessons require, the risks to you on your own machine, the risks to other people once you ship, the craft of directing and checking, unattended work, and the capstone.

The daily job takes the first `todo` slot, so map order is also generation order. Six slots are `legacy` (00.01 to 00.04, 01.02, 01.03), so the job starts at 01.01 and the 29 new lessons arrive riskiest-first after the ground floor. By my own arithmetic, starting 2026-10-13 at one lesson a day, 06.02 lands before Supabase's 2026-10-30 default change (C068) and 07.01 lands about five weeks before the EU AI Act's 2 December 2026 marking deadline for generators already on the market (C110).

### Why these districts

The legacy map (Machine, Code, History, Network, Trust, Shipping) came from Claude's 2026-10-11 intuition. The evidence asks different questions, so the districts follow the thirteen concept groups instead, merged where they answer the same question:

- **Start · Orientation** (what is my job now?) holds the course rule (C001) and the picture of model, harness and context that every later lesson assumes (C021-C025). Six legacy lessons cover its four slots for now.
- **Ground Floor** (what does the work stand on?) is G13 plus the one part of G05 that Trust needs first: what the agent loads (C044, C046, C049), because C045 and C091 assume it. It also takes C099 (local, preview and production are different places), whose Requires field names four G13 concepts. Beginner courses still assume the command line and git without teaching them (`research/sweep/courses.md`, finding 9), and every concept here is taught as recognition, not syntax, as G13's framing requires.
- **Trust** (what can act as you?) is G08, G09 and the keys half of G07 (with C061, spending caps, from G06), plus the data and screen-agent half of G11. It comes before Going Public because everyone in the audience runs an agent on their own machine from day one, while only some ship to strangers, and because its losses are permanent: wiped drives (S063, S174, S175, S176), wiped production databases (S225, S226), 341 malicious skills in one marketplace (S071), npm worms (S158, S061), credential theft at an 85% success rate in testing (S058) and a stolen key that ran up about $600,000 (S046). Deletes and undo (C097, C098) sit here rather than in the unattended-work group because they bite in the first session.
- **Going Public** (what changes once it's public?) is the rest of G07 and G12. It is the pitfall Aaron singled out: people believe the agent when it says the app is safe. 91% of 200 deployed vibe-coded apps were exploitable (S039), and the beginner courses that assume no programming are exactly the ones that skip security and deployment (`research/sweep/courses.md`, finding 9). Publishing AI media sits here too, because labelling and rights become duties at the moment of publication.
- **Delegation** (how do you direct and check?) is G04, G02, the remaining G01 concepts, the context and cost concepts of G03 and G06, the media-model concepts (C030-C032, C134) and the checking half of G11. It comes after the security districts because the rule itself is already in Start (00.02) and because its failures mostly cost time rather than cause breaches. Within it, "define done" (C038) comes before "done is a claim" (C011), whose acceptance step relies on it; both OpenAI's and Anthropic's courses put defining done first (C038, S007, S008). Debugging is taught as the agent's job with the human supplying the reproduction, the expected behaviour and the eyes (08.02), which is Aaron's correction and matches Stanford dropping debugging as a topic (S001).
- **On Its Own** (what runs while you're away?) is the rest of G10. Its concepts build on checking (C100 extends C011; C096 needs a defined end state), so it follows Delegation.
- **Finish · Capstone** walks one small project through every district. It also holds the should-priority concepts that need the whole map before they make sense: deciding what is worth building (C043), finding what you want cheaply (C037), the blind-spot pass (C036), measuring outcomes (C020) and keeping the judgment you need to supervise (C010).

The Lanterns stay over every district: 22 of the 35 lessons are about AI itself and are listed on the Lantern line, but no district or module is named for AI, and each sits where AI shows up (permission modes under Trust, AI review under Checking, AI media under Publishing).

### How it differs from the strongest current syllabus

Stanford's CS146S (Fall 2026) runs agent internals, context and specs, skills, customizing the agent, agent-ready repos, code review, then security in week 7 (3 November) and background agents in week 8 (S001; `research/notes/courses-teach-now.md`). This design keeps its pieces but moves the ground floor first and security forward. CS146S teaches developers who already have the terminal and git (it dropped its terminal week), while this audience often has neither (S211; `research/sweep/courses.md`, finding 9). And the courses aimed at people who do not program are the ones that skip security and deployment (the same finding), so here the security districts come before the craft of review rather than after it.

### Density, and where it may split

The size is 35 lessons: 6 `legacy` and 29 `todo`, about a month at one a day. Nine lessons list five concepts and 02.03 lists six (three must, three small segments). Counted by must-priority concepts, the densest are 08.01 (five) and 03.02, 04.01, 06.04 and 10.01 (four each). These are the first candidates to split when feedback arrives. 08.01 is the most likely: it would become "Say what you want" (C034, C035, C038) and "Plan, then slice" (C040, C041), which uses the one slot left under the 36-lesson cap.

### What went to the backlog, and why

Every must-priority concept (85) is in a core lesson. Of the 46 should-priority concepts, 38 are in core lessons; eight wait (C028, C029, C039, C053, C054, C058, C059, C129), each for the reason in the backlog table: thin or stale evidence, a mechanism already taught in a core lesson, or a beginner-question batch not yet run. All four could-priority concepts sit inside a core lesson as short segments (C031 in 11.02, C050 in 02.03, C109 in 11.01, C112 in 07.01). Two backlog rows are deep dives on topics the core already touches (physical devices; app stores and chatbot law), waiting for firmer sources or for pages the research crew could not read.

### Known limits of the evidence behind this design

These carry over from `concepts.md` and should shape the per-lesson specs: the G13 concepts have no beginner-sourced questions yet (search was unavailable and Reddit blocks the fetcher); C108 rests on one source; C085 is flagged thin; C103's non-Anthropic vendor columns are incomplete (OpenAI's data-use page returned HTTP 403); Stanford's security lecture (2026-11-03) has not happened yet; and C058's price comparison must be re-measured before it is taught.
