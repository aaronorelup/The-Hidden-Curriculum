# The Hidden Curriculum — Master Curriculum

Everyone can build almost anything with AI now. What stops people is small gaps in what they know, and those gaps move every week because the tools do. This course fills them in the order a builder meets them: first one real thing built and in other people's hands, with the safety checks that takes, then a district at a time that deepens what you met on the way. Its rule: the agent handles what can be verified; you check what it cannot, and when you cannot, you bring in an expert who can.

Every lesson is built from other people's current, hard-won knowledge (courses, practitioner essays, incident reports, surveys, standards, tool docs and real beginner questions), listed with dates in `curriculum/sources.md`, and teaches concepts from `curriculum/concepts.md`. Each row below names the concepts a lesson teaches and the 2 to 5 sources it is built on and credits.

Lesson numbers (00.01, 03.02 ...) are for display and change when the map changes. Each lesson's key (its file under `curriculum/lessons/` and its URL) never changes.

Something you wish you'd known, a question you want answered, a source the course should use, or something out of date: open an issue at https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose. Each one becomes evidence for a concept, and the map is rebuilt as the gaps move.

Status key: `todo` · `published` · `legacy` (a lesson published before 2026-10-12 covers this slot for now; it will be rebuilt later)

Lantern lessons: 00.02 00.03 01.02 02.01 02.02 02.03 04.01 04.03 05.01 05.02 05.03 06.01 06.02 06.03 07.01 07.02 07.03 08.01 09.01 09.02 09.03 09.04

---

# Start · Orientation — What this is, and your job

## Module 00 — Orientation
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 00.01 | [The hidden curriculum](curriculum/lessons/the-hidden-curriculum.md) | Building with AI is open to anyone now, and what stops people is small gaps nobody teaches, which move every few weeks as models retire, tools merge and harnesses ship new releases; so the course is a map rebuilt as they move, and your habit is to re-check what you know after every update. | C052 | S004, S001, S025, S033 | todo |
| 00.02 | [What you're really using](curriculum/lessons/model-harness-and-memory.md) | You never use a bare model but a model inside a harness (system prompt, tools, instruction files, memory, effort setting) that changes results as much as the model does; its knowledge stops at a date and its "memory" is files the product writes and puts back in the prompt, so ask what it looked up, not what it knows. | C021, C023, C024 | S002, S014, S011, S101 | legacy |
| 00.03 | [Trust what you can verify](curriculum/lessons/trust-what-you-can-verify.md) | An agent can keep iterating on anything with a cheap, automatic check, so let it write, run and fix; set trust per kind of task, not per model, and for what no machine can check (security, deploy readiness, fit, intent) check it yourself or bring in an expert, because a beginner's failures look like successes. | C001, C002, C006 | S004, S027, S080, S085 | legacy |

# District 1 · First Build — How do I build my first thing?

## Module 01 — Your workbench
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 01.01 | [The folder is the agent's world](curriculum/lessons/the-folder-is-the-agents-world.md) | Every agent session starts in a folder that becomes its world (paths resolve from it, rules and trust climb up from it), but it is not a wall: your home folder holds keys and AI logins, hidden dotfiles hold history, secrets and instructions, and a copy on the same drive is not a backup. | C123 | S206, S208, S211, S176 | legacy |
| 01.02 | [Where your agent works](curriculum/lessons/where-your-agent-works.md) | Chat, Cowork, desktop apps and terminal agents can share a model but differ in what they can reach, which machine the work runs on (yours, a VM, a container, a cloud box) and where your files go; the terminal is just a window where a shell runs commands as you, so pick the surface by the output you need and check where the data goes before you hand it anything private. | C022, C103, C122, C128 | S102, S184, S207, S209, S249 | todo |
| 01.03 | [Save points and the agent's trail](curriculum/lessons/save-points-and-the-agents-trail.md) | Git gives you save points (commits), parallel lines (branches) and a copy that lives elsewhere (the remote), and the agent types every command; your part is recognition: read its trail for the verb and the target, check the diff and which branch is live, and notice anything it touched that you never named. | C117, C124 | S026, S208, S212, S117 | todo |

## Module 02 — Your first build
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 02.01 | [Before you let it loose](curriculum/lessons/before-you-let-it-loose.md) | A command the agent runs has your permissions on every drive you can reach, shell deletes skip the Recycle Bin, and people approve nearly every prompt they are shown; so choose the permission mode on purpose, prefer a tool with mechanical delete guards, keep a copy off the machine, and at a prompt check the targets, not the syntax. | C077, C081, C097 | S063, S052, S051, S226 | todo |
| 02.02 | [Saying what you want](curriculum/lessons/saying-what-you-want.md) | The job moved from typing code to directing: agents brute-force any clearly stated goal, so most failures move upstream into what you asked for; write the goal, the constraints and a checkable "done when", and have the agent surface your unknowns and its own assumptions before it builds. | C033, C034, C035, C036, C038 | S037, S034, S008, S036, S081 | todo |
| 02.03 | [Done is a claim](curriculum/lessons/done-is-a-claim.md) | The agent now reads, fixes and re-runs its own errors, but its closing "done, tests pass" was false about 1 time in 11 in one team's log; give it a way to see the real result (tests, a browser, a screenshot), supply the reproduction and what correct looks like, and judge yourself whether the result is good, not just running. | C003, C005, C011, C016, C019 | S030, S032, S003, S094, S093 | todo |

# District 2 · Going Live — How do others safely use it?

## Module 03 — Putting it online
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 03.01 | [What runs where](curriculum/lessons/what-runs-where.md) | An app is several places, not one: the browser is public, the server is where secrets and permission checks must live, and the database is a separate service with its own rules and backups, so rolling back code does not roll back data; the bar for all of it rises the moment real users, data or money arrive. | C008, C125 | S212, S039, S041, S010 | todo |
| 03.02 | [Keys: public, secret and leaked](curriculum/lessons/keys-public-secret-and-leaked.md) | A key is a permission set that reaches a program as a setting (from your shell, a .env file or a hosting dashboard): anything shipped to the browser is public, secret keys never are, agent logs and config files leak them, and a leaked key stays live until you revoke and rotate it, because deleting the commit does nothing. | C069, C070, C071, C126 | S020, S048, S213, S061 | todo |
| 03.03 | [From your laptop to a URL](curriculum/lessons/from-your-laptop-to-a-url.md) | Deploying is build, upload and switch on a host that keeps earlier versions, under a domain you rent and point with DNS; local, preview and production are different places with different settings, the host's rollback leaves your database and sent messages untouched, and a public URL is likely found and probed within days. | C063, C098, C099, C127 | S212, S026, S066, S046, S179 | todo |

## Module 04 — Safe for strangers
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 04.01 | [Working is not secure](curriculum/lessons/working-is-not-secure.md) | AI code almost always compiles but passes security checks only about 56% of the time, because agents skip security nobody stated and clear errors by weakening controls; so state the stakes, spend your attention where a mistake costs most (sign-in, payments, permissions, personal data, secrets), and read what every fix to those changed. | C007, C062, C064, C065 | S039, S038, S040, S029 | todo |
| 04.02 | [Test it as a stranger](curriculum/lessons/test-it-as-a-stranger.md) | Logged in is not allowed: authorisation must be checked on the server for every request, a Supabase-style database and its storage answer anyone holding the public key, and your users' data also lives in logs, analytics, AI providers and backups; so test every table and bucket as an anonymous stranger, collect less, and know every copy. | C067, C068, C119 | S044, S148, S152, S216, S055 | todo |
| 04.03 | [Your app's AI feature](curriculum/lessons/your-apps-ai-feature.md) | An AI feature in a public app is a meter strangers can run and a voice that speaks for you: require sign-in before any model call, set per-user and global caps that stop spending, treat the model's output as untrusted, say it is AI, ask before users' data goes to an AI provider, and let them report what it makes. | C121, C131 | S055, S220, S233, S195 | todo |
| 04.04 | [Before you ship: who signs off](curriculum/lessons/before-you-ship-who-signs-off.md) | Scans, AI security reviews and checklists are a floor, not a certificate: list every route, TODO and deploy step the build left to you, let the agent run every check a machine can (accessibility checkers included), bring that list to a qualified expert for what no machine can verify, and remember that a person, not the agent, owns the ship decision and the patches after it. | C009, C066, C072, C118, C120 | S043, S146, S214, S218, S221 | todo |

# District 3 · Directing Well — How do I direct it well?

## Module 05 — What the agent sees
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 05.01 | [What the agent sees each turn](curriculum/lessons/what-the-agent-sees-each-turn.md) | Every turn resends the whole package (system prompt, tool definitions, instruction files, memory and the full history), and accuracy falls as the window fills, so curate what goes in, clear once a decision is made, carry plans in files rather than chat, and brief subagents fully because they start blind and return only a summary. | C025, C026, C027, C028 | S002, S003, S107, S105 | todo |
| 05.02 | [Rules it reads, rules it can't break](curriculum/lessons/rules-it-reads-rules-it-cant-break.md) | An instruction file (CLAUDE.md, AGENTS.md) is a short map the agent reads on every request, but anything in prose is a request it may skip; only a deny rule, a blocking hook, a sandbox, CI or a withheld credential makes an action impossible, a rule works only in sessions that load it, and a stale file misleads, so keep it short, dated and backed by checks. | C044, C045, C046, C047, C048 | S123, S021, S023, S026, S022 | todo |
| 05.03 | [Skills, MCP, hooks and plugins](curriculum/lessons/skills-mcp-hooks-and-plugins.md) | A skill is a written procedure, an MCP server connects outside tools, a hook is code the harness runs on an event, a subagent is an isolated worker and a plugin bundles them; each one you enable costs context, and skills, plugins and local MCP servers are code running with your permissions that can change after you approve them. | C049, C050, C051, C091, C092 | S015, S130, S071, S162 | todo |

## Module 06 — Scaling up
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 06.01 | [Bigger work: plan, slice, unstick](curriculum/lessons/plan-slice-and-unstick.md) | For anything bigger than a one-line change, keep research and planning apart from building: react to cheap mockups first, have the agent map what exists, compare options and write a short plan with an out-of-scope list, build in reviewable slices, and when it loops on the same error, stop and change the input instead of saying "fix it" again. | C037, C039, C040, C041, C042 | S003, S036, S117, S118 | todo |
| 06.02 | [Checking what you can't read](curriculum/lessons/checking-what-you-cant-read.md) | You cannot read every line an agent writes and need not: accept work on evidence something outside the agent wrote (the real diff, CI, server logs, the destination), keep one source of truth outside the session that wrote the code, treat AI review as triage, expect agents to game the checks they can see, and break things on purpose to prove your checks bite. | C004, C012, C013, C014, C015, C017 | S030, S029, S064, S042 | todo |
| 06.03 | [Know your meter](curriculum/lessons/know-your-meter.md) | Know which meter you are on (a subscription's rolling allowances, or an API key that bills every token, which a stray key in your environment switches you to), that cost is context times turns times agents, that caching discounts only an identical prefix, that a cheaper model is not always a cheaper result and higher effort mostly buys more steps, and that budget alerts don't stop spending, so set caps that do. | C055, C056, C057, C058, C059, C061 | S016, S017, S128, S139 | todo |

# District 4 · Agent Power — What can your agent touch?

## Module 07 — Reach and trust
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 07.01 | [Whose words is it reading?](curriculum/lessons/whose-words-is-it-reading.md) | Everything an agent reads (web pages, issues, READMEs, tool output, even data from an official MCP server) lands in the same stream as your request, so anyone who can write text it reads can try to steer it; filters catch most attempts but attackers retry, so never give one agent private data, untrusted content and a way to send data out at once, and review what gets written into its memory and rules. | C073, C074, C075, C076, C086 | S049, S050, S058, S051, S054 | todo |
| 07.02 | [Contain it, don't babysit it](curriculum/lessons/contain-it-dont-babysit-it.md) | Approving each step does not hold, so put the boundary in the environment: run risky, unattended or package-installing work in a container or VM with the network off and no production keys, know exactly what your sandbox covers (Claude Code's is off by default, shell-only and absent on native Windows), and remember isolation limits where code runs, not what your granted access can reach. | C078, C079, C080 | S050, S052, S064, S063 | todo |
| 07.03 | [The narrowest keys and verbs](curriculum/lessons/the-narrowest-keys-and-verbs.md) | Assume anything the agent can see can be extracted and anything it can reach it will treat as permitted: keep production keys out of where it runs, grant the narrowest verbs, roles, targets and domains, give browser agents a separate profile, and keep spending, messages to outsiders, sensitive data and publishing behind a human approval. | C082, C083, C084, C085, C104 | S053, S046, S055, S070, S189 | todo |
| 07.04 | [Other people's code](curriculum/lessons/other-peoples-code.md) | Installing a package, opening or testing a repo, trusting a folder and pasting a command all run someone else's code as you, so check that every new dependency the agent names exists and has a history, set a minimum release age, open untrusted repos only in a disposable box, and never run a command a web page tells you to. | C087, C088, C089, C090, C093, C130 | S060, S061, S056, S057, S062 | todo |

# District 5 · Running Alone — What runs while you're away?

## Module 08 — Unattended work
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 08.01 | [Agents that run while you're away](curriculum/lessons/agents-that-run-while-youre-away.md) | Background, cloud, scheduled and always-on personal agents act without a prompt, each with its own files, rules, permissions and bill; list where yours run, keep scheduled work low-consequence, give long runs stop rules, budgets and checkpoints enforced outside the model, and treat more agents as more to review, not more done. | C060, C094, C095, C096, C105 | S167, S035, S019, S161 | todo |
| 08.02 | [Green is not success](curriculum/lessons/green-is-not-success.md) | An automation can run green for weeks while doing nothing (an expired token, a renamed field, a filter that matches nothing), so check outcomes in layers (did it run, is the output right, did it arrive), feed known answers through the live pipeline, and watch from outside with a heartbeat and at the destination. | C100, C101, C102 | S067, S182, S180, S032 | todo |
| 08.03 | [Every automation runs as someone](curriculum/lessons/every-automation-runs-as-someone.md) | Every automation acts as the account that owns it, and every shipped app rests on a chain of accounts (code host, hosting, domain, database, AI provider, payments); so list each one with its owner, protect them with passkeys or 2FA and stored recovery codes, and move anything a business depends on to a service account with narrow access and a second owner. | C129, C135 | S246, S245, S247, S142 | todo |

# District 6 · Beyond Code — What if it isn't software?

## Module 09 — Facts, media, rights
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 09.01 | [Checking research, numbers and parts](curriculum/lessons/checking-research-numbers-and-parts.md) | Whether a cited link exists is something the agent can check, so make it; whether the source supports the claim, whether a spreadsheet's logic is right and whether a part fits a real board are not, so you or an expert check those, with a known-answer test, a separate checker session and the distributor's data, before anything is filed, sent or ordered. | C106, C107, C108, C109 | S072, S073, S074, S075 | todo |
| 09.02 | [Making media with AI](curriculum/lessons/making-media-with-ai.md) | A model that reads images is not one that makes them: generation runs through separate media models, in the cloud or on your own machine, whose results vary run to run and converge across users, cost per second, resolution and retry, and cannot be seen or heard by the agent without a tool, so test cheap before the expensive render and bring your own taste. | C030, C031, C032, C134 | S110, S111, S244, S242 | todo |
| 09.03 | [Labelling AI media](curriculum/lessons/labelling-ai-media.md) | A generator's watermark is for machines, not your label: publishing professionally in the EU means telling people where they see it (from first exposure, spoken for audio), AI-written public-interest text needs a responsible human reviewer or a label, and each platform's own rules on AI content apply on top. | C110, C111, C112, C116 | S076, S195, S200, S079 | todo |
| 09.04 | [Own it, sell it, publish it](curriculum/lessons/own-it-sell-it-publish-it.md) | The generator's terms, the model's own licence and copyright law each decide something different: free tiers can be personal-use only, purely AI-made work has no US copyright, a local model's licence can forbid commercial use, voices and faces need written consent, and owning an output doesn't clear someone else's logo or character, so log which plan made each asset and bring in an IP lawyer before selling. | C113, C114, C115, C132, C133 | S077, S201, S203, S235, S238 | todo |

# Finish · Capstone — Can you ship it end to end?

## Module 10 — Capstone
| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 10.01 | [Idea to launch, end to end](curriculum/lessons/idea-to-launch-end-to-end.md) | One small real project walked through every district: you choose a problem worth building and what "done" means, the agent builds in checked slices, you can explain what it built before you merge, and every check the course taught is run by the agent where it can be verified and by you or an expert where it cannot. | C010, C018, C043 | S007, S115, S084, S083 | todo |
| 10.02 | [After launch: keep it alive](curriculum/lessons/after-launch-keep-it-alive.md) | Shipping starts the work: agents keep adding output and dependencies, so judge the project by outcomes (escaped defects, rollbacks, users served) rather than lines, write the house rules and a named owner for the dependency list into files the agent reads, and keep the code one an agent can change safely, with formatters, linters and a final-diff review catching its habits. | C020, C053, C054 | S082, S029, S035, S036 | todo |

---

## Legacy lessons (published before 2026-10-12; kept, marked, rebuilt later)
| Legacy lesson | Slug | Covers | Note |
|---|---|---|---|
| 00.01 The hidden curriculum | 00-01-the-hidden-curriculum | 00.01 (partly) | Its core ("the gap is in the syllabus, not in you") stands, but it lays out the old six-district map and the change it describes is years, not weeks. 00.01 stays `todo` so the daily job rebuilds the front door first, with the new map and the weekly-change evidence of C052. |
| 00.02 The map of everything | 00-02-the-map-of-everything | 00.01 (partly: the map) | The five-stop road (your computer, network, internet, services, AI) is retired as the course map; the new map is drawn in the rebuilt 00.01. Its "which stop broke?" habit comes back in 03.01 What runs where. |
| 00.03 How old is all this? | 00-03-how-old-is-all-this | 00.01 (partly: how fast things change) | Teaches change over years (versions, logins, TLS). Rebuild at the scale of weeks: models retired on about 30 days' notice, a CLI command removed 12 days after deprecation, products merging (C052; S025, S033). |
| 00.04 Model vs app vs agent | 00-04-model-vs-app-vs-agent | 00.02 | Engine, car, driver holds for now. Rebuild around model plus harness (S002), with the April 2026 quality drop that came from three harness changes while the model was untouched (S014) as the case. |
| 00.05 How AI models work today | 00-05-how-llms-work-just-enough | 00.02 (with 00.04) | A 20-minute tour. When 00.02 is rebuilt, its segments move to their own lessons (context 05.01, skills and plugins 05.03, meters 06.03, personal agents 08.01, media and diffusion 09.02) and the overview shrinks to about 8 minutes; add "generated is not looked up" (C024). |
| 00.06 Trust what you can verify | 00-06-how-to-learn-anything-technical | 00.03 | Already teaches the rule and that agents fix their own errors. On rebuild add the jagged frontier (C002), Stack Overflow 2026's verify-first trust figures (S080), and a pointer to 04.04 for how to bring in an expert (C118). Its "job moved" segment now has its own home in 02.02 (C033). |
| 01.01 Files are just bytes | 01-01-files-are-just-bytes | none (backlog: Files, bytes and file types) | No current gap item: agents now make, name and open files, so the copy-from-chat confusion this fixed is fading (concepts.md, G13 notes). Stays published as background. |
| 01.02 File extensions & associations | 01-02-file-extensions-associations | none (backlog: Files, bytes and file types) | Same as 01.01. Its "extension is a label, not the contents" idea is reused briefly in 07.04 (downloads that are not what their name says). |
| 01.03 Folders, paths & the working directory | 01-03-folders-paths-the-working-directory | 01.01 | With 01.04 it covers C123 well enough for now. Rebuild both as one lesson: the folder as the agent's world and not a wall, rules and trust climbing upward, keys and AI logins in the home folder (S206, S208). |
| 01.04 Hidden files & dotfiles | 01-04-hidden-files-dotfiles | 01.01 | Merges into the rebuilt 01.01; its "the drawer of keys with no lock" and "new staff in the back room" scenes carry over. |
| 01.05 Environment variables & PATH | 01-05-environment-variables-path | 01.02 (partly: PATH), 03.02 (partly: environment variables) | Covers the local half of C126 and PATH for C122. Hosting dashboards per environment, build-time prefixes baked into the public bundle and ".env is a naming convention, not a vault" are new in 03.02. |
| 01.06 Programs, processes & services | 01-06-programs-processes-services | 01.02 (partly), 03.01 (partly) | "A command starts a program" feeds C122 and "servers and ports" feeds C125. Task Manager, leftover processes and "port in use" go to the backlog unless beginners ask for them. |

## Deep-dive backlog (not scheduled)
| Topic | Concepts | Sources | Why it waits |
|---|---|---|---|
| Thinking tokens and reasoning budgets | C029 | S013, S015, S033 | Should-priority, but its own entry says it mostly matters to people building on the API or watching bills; 06.03 names it in a sentence. The only concept not taught in a core lesson. |
| Files, bytes and file types (legacy 01.01, 01.02) | C123 | S211, S210 | No current gap item: the confusion came from the copy-from-chat workflow agents replaced (G13 notes). Return if beginners report it. |
| Processes, ports and servers on your machine (legacy 01.06) | C122, C125, C127 | S207, S212 | Core lessons cover commands (01.02) and servers (03.01). The G13 research batch on beginner questions never ran (search budget, Reddit blocked), so there is no evidence yet that "port in use" or leftover processes are live gaps. |
| Hardware and physical devices, including the EU Cyber Resilience Act | C109, C008 | S075, S194, S251 | C109 is could-priority as a standalone lesson: one medium-severity item, and the only measurement comes from a vendor-funded benchmark (S194). 09.01 carries a segment. First candidate to grow, since Aaron asked for physical devices (S248). |
| Mobile apps and app stores | C131, C116 | S233, S234, S248 | Aaron asked for mobile apps and stores (S248), and 04.03 covers the stores' AI rules. Signing, review and submission have no concept yet, so a research batch must find those gaps first. |
| Local and open-weight models in depth | C031 | S112, S033, S011 | Could-priority with two sources; 09.02 covers local media models. A full lesson needs measured hardware and runtime evidence. |
| Accessibility audits | C120 | S221, S222, S223, S224 | 04.04 teaches the split (the agent runs checkers; people do keyboard and screen-reader passes). A full lesson is a must for public-sector, shop, banking-type and e-book services, and the EU dates must be re-checked first: the Commission's EAA page gives no application date. |
| Your users' data and the law | C119 | S219, S216, S154 | 04.02 teaches the engineering habits. Legal duties differ by country and are a lawyer's job; GDPR Article 33's breach clock (S219) is the one fixed point read so far, and S154 is an unverified vendor scan. |
| Comparing AI vendors' privacy settings | C103 | S186, S187, S241 | Only Anthropic's and Google's pages were readable; OpenAI's returned HTTP 403 twice (challenge log). A fair per-vendor lesson waits for a readable source. |
| Parallel agents, worktrees and fleets | C095, C080 | S172, S030, S036 | 08.01 teaches "more agents is not more done". The popular setups (reviewer chains, swarms, overnight loops) are unproven per C095, so a how-to-run-them lesson would teach something not yet shown to work. |
| Building MCP servers other people use | C067, C092 | S059, S164 | Only for people who publish servers; C067 says their auth design needs someone who can verify it, and S164 is marked draft. |
| Prompt caching in depth | C057 | S128, S135, S137 | 06.03 teaches the rule. Deeper mechanics matter to API builders, and Sonnet 5.5 cache-read prices halved on 2026-10-07, so ratios must be re-measured before teaching (G06 notes). |
| Game storefronts | C116, C133 | S239, S250 | 09.03 and 09.04 cover platform rules and infringement. A lesson for game makers waits for community questions; the G12 pass collected none. |
| AI-written public-interest text | C112 | S076, S195 | Could-priority; its entry says to teach it as a two-minute segment of the labelling lesson, which 09.03 does. |
| Writing skills that load at the right time | C050 | S022, S130, S015 | Could-priority, vendor sources only; one sentence in 05.03. |
| Spreadsheets with agents in depth | C108 | S074 | One benchmark source and no second found (G11 notes); 09.01 carries the segment. |
| Code licences and matching public code | C053 | S209, S232 | The challenge pass marked the evidence of harm thin (finding 19); 10.02 names it. |

## Rationale

**Journey first.** The evidence shows exactly where today's courses stop and what they assume. DeepLearning.AI's beginner course ends with a single-file app on your own machine and does not cover testing, deployment or security (S010); Claude Code 101 assumes the command line, an editor and a paid plan (S005); and the course sweep found that the non-programmer on-ramps are the very courses that skip security and deployment (`research/sweep/courses.md`, patterns 5 and 9). Replit's own beginner course (sweep entry 25, undated, not yet in `sources.md`) names the ladder this map follows: just for me, then my team, then the world, each step adding hosting, accounts, security and data work. So:
- **Start** (3 lessons, about 5 minutes each) gives the shelf and the rule: what this course is, what you are really using, trust what you can verify.
- **District 1, First Build** (6) supplies the ground floor the courses assume (G13: folder, terminal and surface, git and the agent's trail) and the first build itself: the safety you need before an agent acts on your machine (02.01, because it acts with your permissions from its first command: in 2026 an agent's delete wiped a whole drive (S063) and a schema command that never says "delete" wiped 22 production tables (S226)), saying what you want, and treating "done" as a claim.
- **District 2, Going Live** (7) takes the build to a URL and makes it safe for strangers, in the order the risks bite: the app's parts, keys, deploying (and being found within days), then the security checks, the AI feature, and the ship decision with an expert. The learner has something at a URL by the 12th lesson, and module 04 stands between that URL and inviting anyone in. It is the largest district because security is where the course rule matters most: 91% of 200 deployed vibe-coded apps had at least one vulnerability (S039), and that is the part people believe the agent when it says it is safe.
- **Districts 3 to 6** each deepen something met on the way. Directing Well deepens the build (context, instruction files, extensions, planning, checking, cost: Stanford CS146S weeks 1 to 6 and the vendor academies, S001-S005, S008). Agent Power deepens 02.01's safety (injection, containment, least agency, supply chain) and comes after Directing Well because it needs that district's vocabulary of MCP, skills and hooks. Running Alone needs Agent Power's containment and least agency. Beyond Code serves the many in the audience who make research, spreadsheets, devices and media; it sits last because its checks reuse the rule, and its lessons stand alone, so a media maker can jump there after District 1.
- **Finish** walks one real project through every district (10.01) and then the month after launch (10.02), and carries the judgment concepts that span the whole path (choosing what to build, keeping the judgment you need, understanding before you merge, measuring outcomes).

**Districts and names.** Six districts, each one question, replace The Machine / The Code / The History / The Network / Trust / Shipping. Those were organised by technology layer; the evidence is organised by what a builder does next and where trust breaks, so the districts follow the journey. Plain names (First Build, Going Live, Directing Well, Agent Power, Running Alone, Beyond Code) were chosen over metaphors so the map reads at a glance.

**The Lanterns.** 22 of 35 lessons are about AI itself (directing, checking, context, rules, permissions, injection, media), which is what a course on building with AI should look like in 2026. None of them is grouped into an AI district: each sits where the builder meets it.

**Coverage.** All 85 must-priority concepts land in core lessons. 45 of 46 should-priority concepts do too, mostly as segments of denser lessons; only C029 (thinking tokens) goes to the backlog, for the reason its own entry gives. The four could-priority concepts (C031, C050, C109, C112) are segments, as their entries suggest. Every concept is taught in exactly one core lesson. Each lesson's sources are ones its concepts actually cite, picked for recency and first-hand weight (dated 2026-07 or later where possible; S027, S049, S203 and S214 are older but foundational and still current, as `sources.md` notes).

**Order respects the Requires fields.** Where a concept needs a ground-floor concept, the ground floor comes first: C128 (other machines) joined 01.02 because C022 requires it; C098 (undo has limits) moved to 03.03 because it requires C125 and C127; C099 (local vs preview vs production) follows C126 and C127; C103 (where your data goes) follows the folder lesson C123; C033 moved from orientation to 02.02 because it requires the terminal and the agent's trail.

**Size and pace.** 35 lessons: 3 are covered by legacy lessons for now (00.02, 00.03, 01.01), so 32 are new, about a month at one a day. The first `todo` is 00.01 on purpose: the front door should show the new map. Start lessons run about 5 minutes; most others 10 to 15; the densest (06.02, 06.03 and 07.04, six concepts each) near 15; none over 20.

**What was cut, and why.** The old curriculum's topics with no gap item in the current evidence are not scheduled: CPU, RAM and VRAM; Windows vs macOS vs Linux; pipes, redirects and script files; networking internals; OAuth flows; payments integration; Docker as a topic of its own (containers appear in 01.02 and 07.02 where the evidence puts them). They come back if community issues show the gap. Everything else that needs more than a segment is in the backlog with its reason.

**Known weak spots.** G13's ground-floor concepts have no beginner-question evidence yet (the prerequisites research batch never ran); C036, C085 and C108 rest on thin evidence; OpenAI's privacy page and California SB 243 could not be read; all law covered is EU or US. These are the first places for community contributions to change the map.
