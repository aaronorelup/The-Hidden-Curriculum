# The Hidden Curriculum — Master Curriculum

Everyone can build almost anything with AI now. What stops people is small gaps in what they know, and those gaps move every week because the tools do. This course fills them with conceptual mental models (what a thing is, where it lives, what it connects to, what will surprise you, and what you do versus what the agent does), not click-by-click tutorials, and it is rebuilt as the gaps change. Its rule: AI can handle anything that can be verified; you check what it cannot, and when you cannot, you bring in someone who can.

Every lesson is built on other people's current, hard-won knowledge. It teaches concepts listed in `curriculum/concepts.md`, it is built from the sources listed in `curriculum/sources.md` (by ID in the tables below), and it credits those people by name. The map is a Start, seven districts that each answer one question, and a Finish; the Lanterns are AI, strung over every district rather than given one of their own.

Lesson numbers such as 04.02 are display only and change whenever lessons move. Each lesson's key (the name of its spec file, its folder and its URL) never changes.

Something you wish you had known, a question you want answered, a source the course should be built on, or something wrong or out of date: open an issue at https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose. Each one becomes evidence for a concept, or a new one.

Status key: `todo` · `published` · `legacy` (a lesson published before 2026-10-12 covers this slot for now; it will be rebuilt later)

Lantern lessons: 00.02 00.03 01.02 04.01 04.02 04.03 04.04 05.01 05.02 06.01 07.01 08.01 08.02 09.01 10.01 11.01 11.02 12.02 13.01 14.01 20.01 21.01

---

# Start · Orientation — what this is, and the lantern

## Module 00 — Orientation

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 00.01 | [The hidden curriculum](curriculum/lessons/the-hidden-curriculum.md) | Everyone can build with AI now, and what stops people is small gaps that move every week (models retire, commands vanish, and the model's own knowledge has a date), so this course is a map of those gaps, rebuilt as the tools change and fed by the people who use it; check the date on anything you learn. | C024, C052 | S004, S033, S025, S125, S011 | todo |
| 00.02 | [Trust what you can verify](curriculum/lessons/trust-what-you-can-verify.md) | An agent can loop on anything with a resettable, cheap, automatic check, so let it; for what no machine can check (security, deploy readiness, fit, intent) you check it or bring in someone who can, and you set that trust per kind of task, not per model. | C001, C002 | S004, S027, S080, S029 | legacy |
| 00.03 | [Model, harness and context](curriculum/lessons/model-harness-and-context.md) | You never use a bare model: you use a configuration (model, harness, tools, instruction files, memory, effort) that resends the whole package every turn and knows only its frozen training plus what is in its window, so when results change, name the whole setup before blaming the model. | C021, C023, C025 | S002, S014, S101, S011 | legacy |

# District 1 · The Ground — where does the work happen?

## Module 01 — Your machine

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 01.01 | [The folder is the agent's world](curriculum/lessons/the-folder-is-the-agents-world.md) | Every agent session starts in one folder and treats it as its world but not as a wall: rules and trust climb to parent folders, your home folder holds keys and AI logins, and dotfiles are hidden, not locked, so you open the agent on one project folder and keep copies somewhere else. | C123 | S206, S211, S176, S175 | legacy |
| 01.02 | [Reading the agent's trail](curriculum/lessons/reading-the-agents-trail.md) | The agent types every command, so you need recognition, not syntax: a shell runs each line as you, on whichever machine the session lives (laptop, WSL, container, SSH box or cloud VM, depending on the surface you chose), and you read the trail for the verb and the target and ask about anything it touched that you never named. | C117, C122, C128, C022 | S207, S208, S117, S209, S249 | todo |

## Module 02 — Save points

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 02.01 | [Git: save points and copies](curriculum/lessons/git-save-points-and-copies.md) | Git keeps snapshots on named, movable lines, with copies elsewhere and proposed changes you review; the agent types every git command, and you check which branch is live, that a remote copy exists and what a pull request changes, because checkpoints are not git and rewriting history breaks the other copies. | C124 | S209, S026, S212, S117 | todo |

## Module 03 — Your app's parts

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 03.01 | [What runs where in your app](curriculum/lessons/what-runs-where-in-your-app.md) | An app is several places with different rules (a public browser, a server where secrets and permission checks must live, a database with its own access rules and backups, settings each program receives when it starts, some baked into the public bundle, and other people's downloaded code), and you need this map before you can judge anything the agent says about safety or rollback. | C125, C126, C130 | S212, S209, S213, S045 | todo |
| 03.02 | [From your laptop to a URL](curriculum/lessons/from-your-laptop-to-a-url.md) | localhost is only your machine; going live means build, upload and switch to a public URL, where preview and production are separate places with their own settings, a rented domain points through DNS, a cloud agent sees only what you pushed, and every account in the chain is part of the app, so you check what is live and who owns each account. | C127, C099, C129 | S026, S212, S066, S167 | todo |

# District 2 · The Workbench — how do you get it built?

## Module 04 — Directing the work

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 04.01 | [The brief: goal, constraints and done](curriculum/lessons/the-brief-goal-constraints-and-done.md) | Directing agents is the job now, and agents brute-force any clearly stated goal and fix their own code bugs, so most failures come from what you never said: surface your unknowns first, then give the goal, the constraints, a check the agent can run and a written "done when", because whether it built the right thing is yours to judge. | C033, C034, C035, C036, C038 | S037, S008, S117, S033, S029 | todo |
| 04.02 | [Plan first, then build in slices](curriculum/lessons/plan-first-then-build-in-slices.md) | Trying is cheap and choosing is not: explore with throwaway mockups, have the agent map the code read-only and propose two options, review a plan scaled to the task, then build in slices small enough to review, and add parallel agents only once one stream has a check you trust. | C037, C039, C040, C041, C095 | S003, S036, S118, S030 | todo |
| 04.03 | [The context window fills up](curriculum/lessons/the-context-window-fills-up.md) | Every turn resends the whole conversation, so a long session gets both worse (context rot, lossy compaction) and dearer (cost multiplies with context, turns and agents, discounted only while the cached prefix stays identical): clear after deciding, hand off through files, give side tasks to subagents that start blind, and watch what is loaded. | C026, C027, C028, C056, C057 | S107, S105, S128, S017 | todo |
| 04.04 | [When the agent goes in circles](curriculum/lessons/when-the-agent-goes-in-circles.md) | The agent now reads errors, adds logging and re-runs until fixed, so your part is a reliable reproduction, what correct looks like, and the question "root cause or hidden symptom?"; when the same error keeps coming back, stop it, name what is missing and change the input rather than saying "fix it" again. | C019, C042 | S094, S117, S008, S004 | todo |

## Module 05 — House rules

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 05.01 | [Instruction files: what to write, what loads](curriculum/lessons/instruction-files-and-what-loads.md) | CLAUDE.md or AGENTS.md rides on every request, so keep it a short map of what the code can't say; a rule works only in sessions that actually load it (folder, timing, surface and branch decide), repeated corrections belong in checks, and a stale rule misleads more than no rule, so prune it when the model changes. | C044, C046, C047, C048, C053 | S123, S021, S022, S026 | todo |
| 05.02 | [Skills, MCP and hooks](curriculum/lessons/skills-mcp-and-hooks.md) | Skills, commands, MCP servers, connectors, hooks, subagents and plugins each do one job and each costs context, but only a blocking hook, a deny rule, a sandbox or CI can make an action impossible: everything written in prose is a request, so every "must never" needs a control behind it that you have seen fire. | C049, C045, C050, C051 | S015, S127, S130, S023 | todo |

## Module 06 — The meter

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 06.01 | [Know your meter](curriculum/lessons/know-your-meter.md) | Know which meter you are on (a plan allowance, or per-token API billing that a stray environment variable can switch you to), that a cheaper model or higher effort changes how many turns the work takes more than the price per token, that thinking is billed output you mostly don't see, and that alerts don't stop spending: set caps that stop. | C055, C058, C059, C029, C061 | S016, S017, S138, S140, S139 | todo |

## Module 07 — Making media

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 07.01 | [Making media with AI](curriculum/lessons/making-media-with-ai.md) | A model that reads images is not one that makes them: media comes from separate models (diffusion turns seeded noise into a picture in steps) inside pipelines you assemble, the same prompt gives different results, it is metered per second, resolution and credit, and a local model carries its own licence; the agent can't see or hear its output without a tool, so the pick stays yours. | C032, C030, C134, C132 | S244, S243, S242, S235, S110 | todo |

# District 3 · The Proof — how do you know it's right?

## Module 08 — Evidence

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 08.01 | ['Done' is a claim](curriculum/lessons/done-is-a-claim.md) | An agent's closing "done, tests pass" is a claim (about 1 in 11 were false in one team's log), and agents optimise for passing rather than for what you meant, so accept work only on records something outside the agent wrote (the runner's receipt, the real diff, CI, the destination) and treat a broken chain of evidence as not verified. | C011, C012, C004 | S030, S064, S042, S087 | todo |
| 08.02 | [Checks the agent can't game](curriculum/lessons/checks-the-agent-cant-game.md) | Give the agent checks it can run (tests, a browser, a render tool checked against reality) and let AI review every change, but neither its own tests nor another model's "looks good" is independent: revert-check the tests, keep expected values literal, write the attack cases in plain language yourself (or have a security-competent person do it), and make sure every guard actually fires. | C013, C014, C003, C017 | S029, S030, S032, S003, S042 | todo |

## Module 09 — Judgment

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 09.01 | [Sounding right is not evidence](curriculum/lessons/sounding-right-is-not-evidence.md) | Models agree with leading questions, explain plausibly, polish for free and cite real-looking sources, and nobody, experts included, can eyeball whether AI code is secure: ask neutrally, demand evidence, let the agent check that links exist, read the passage yourself for every claim that matters, and keep the judgment you need by asking why. | C005, C006, C010, C106, C107 | S040, S085, S092, S072, S073 | todo |
| 09.02 | [Runs, looks done, is good](curriculum/lessons/runs-looks-done-is-good.md) | "It runs", "it does what I meant" and "it is good" are three checks with different checkers: spend attention by blast radius (auth, billing, permissions and personal data get a human every step), match the evidence to the change instead of reading every line, understand the map before you merge, and bring in people for taste, fit and accessibility. | C016, C015, C007, C018, C120 | S029, S036, S041, S037, S221 | todo |

# District 4 · The Fence — what can your agent do to you?

## Module 10 — Whose words?

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 10.01 | [Prompt injection: whose words?](curriculum/lessons/prompt-injection-whose-words.md) | Everything an agent reads (issues, web pages, error reports, tool output, screenshots) enters the same stream as your request, so anyone who can write text it will read can try to steer it, even through an official server: never give one agent private data, untrusted content and a way to send data out, and review what lands in its memory and rules files. | C073, C074, C075, C086 | S049, S050, S058, S054, S065 | todo |

## Module 11 — Containment

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 11.01 | [Put the boundary in the environment](curriculum/lessons/put-the-boundary-in-the-environment.md) | People approve 93-97% of permission prompts and classifiers miss some attacks, so approvals and auto mode reduce risk but are not a boundary: choose the permission mode on purpose, keep your approvals for the few irreversible actions and check their targets, and put the real boundary in the environment, an isolated box with limited network and nothing worth stealing inside. | C076, C077, C078, C081 | S051, S050, S052, S021 | todo |
| 11.02 | [What your agent holds and may do](curriculum/lessons/what-your-agent-holds-and-may-do.md) | A sandbox covers less than it sounds (in Claude Code it is off by default, wraps shell commands only, can read ~/.ssh and doesn't exist on native Windows), so keep anything worth stealing out of where the agent runs, grant the narrowest verbs, roles, targets and domains, and answer four questions before connecting it to anything real. | C079, C080, C082, C083, C085 | S052, S053, S064, S225, S023 | todo |

## Module 12 — Code from others

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 12.01 | [Installing and opening run code](curriculum/lessons/installing-and-opening-run-code.md) | Models invent package names that attackers register, installing a package can run its code where your keys live, and opening, unpacking or testing someone's repo can execute it before any prompt, so vet every new dependency, set a minimum release age, install without scripts where you can, and treat "trust this folder" as accepting the repo's own hooks, tests and reviewer. | C087, C088, C089, C090 | S060, S061, S056, S057, S160 | todo |
| 12.02 | [Extensions and downloads run as you](curriculum/lessons/extensions-and-downloads-run-as-you.md) | A skill, plugin or local MCP server is code that runs with your permissions and can change after you approve it, and the most dangerous step is often one you run yourself (a "Prerequisites" command, a fake CAPTCHA's paste), so prefer verified extensions, re-approve on change, verify downloads at their real origin, and never run a command a web page gives you. | C091, C092, C093 | S071, S059, S162, S062 | todo |

## Module 13 — Acting as you

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 13.01 | [Assistants that act as you](curriculum/lessons/assistants-that-act-as-you.md) | Browser, desktop and always-on agents act inside every account you are logged into, see everything on your screen, process your files on the vendor's servers or hold your keys around the clock, so give them a separate profile and one working folder, know each vendor's training and memory settings, and keep spending, messaging outsiders, sensitive data and publishing behind your own approval. | C103, C104, C105, C084 | S069, S070, S184, S191, S227 | todo |

# District 5 · The Night Shift — what runs while you're away?

## Module 14 — Running unattended

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 14.01 | [Agents that run without you](curriculum/lessons/agents-that-run-without-you.md) | Cloud routines, scheduled tasks and automations run without approval prompts, act as someone (often you) and bill per action and per wake-up, so keep a list of what runs where and as whom, keep unattended work low-consequence, move business automations to a non-human owner, and give every long run stop rules, a budget and checkpoints enforced outside the model. | C094, C135, C096, C060 | S167, S035, S032, S246, S018 | todo |

## Module 15 — Damage and undo

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 15.01 | [Deletes run as you; undo has limits](curriculum/lessons/deletes-and-the-limits-of-undo.md) | A command the agent runs has your permissions on every drive you can reach, shell deletes skip the Recycle Bin, and commands that never say "delete" can wipe production, while each undo covers only part of what changed: choose a tool and mode with mechanical delete guards, check the printed targets rather than the syntax, and keep a copy the agent's shell cannot reach. | C097, C098 | S063, S226, S225, S178, S176 | todo |

## Module 16 — Silent failures

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 16.01 | [Green is not success](curriculum/lessons/green-is-not-success.md) | A green run means only that nothing threw: expired tokens, renamed fields, filters that match nothing and 200 responses with failure bodies all finish "successfully", so define what a successful run produces, check the output and the receipt at the destination, and watch from outside, because a check inside a workflow cannot see the workflow stop. | C100, C101, C102 | S067, S182, S167, S030 | todo |

# District 6 · The Locks — who can get in?

## Module 17 — Your app's doors

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 17.01 | [Working is not secure](curriculum/lessons/working-is-not-secure.md) | AI code nearly always runs but often fails security checks, most audited AI-built apps were exploitable, and public apps get probed by attackers using the same models, while agents skip security nobody asked for: state the stakes in plain words, never accept "it's secure" from the agent, and treat scanners, AI reviews and checklists as a floor, not a certificate. | C062, C063, C064, C072 | S039, S038, S145, S043 | todo |
| 17.02 | [Logged in is not allowed](curriculum/lessons/logged-in-is-not-allowed.md) | Most AI-app holes are authorisation holes: the screen is not the boundary, anyone can query a Supabase-style database with the public key, and agents clear errors by weakening controls, so the server checks every request, you run the stranger test on reads, writes and storage after every schema change, and you look at what each "fix" to auth, keys, grants or tests changed. | C065, C067, C068 | S044, S148, S039, S216 | todo |

## Module 18 — Keys and secrets

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 18.01 | [Keys, secrets and leaks](curriculum/lessons/keys-secrets-and-leaks.md) | A key is a permission set whose power is whatever it can reach today: anything shipped to the browser is public, secret keys belong in server-side stores, agent work leaks them through permission files, MCP configs, logs and AI-tool logins, and deleting a leaked key from the code does nothing, so revoke it, check what it reached and rotate everything connected. | C069, C070, C071 | S020, S048, S045, S061, S047 | todo |

# District 7 · The Release — what changes when people arrive?

## Module 19 — The production pass

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 19.01 | [Before real users arrive](curriculum/lessons/before-real-users-arrive.md) | Demo shortcuts are fine until real users, data, money or mains power arrive; at that moment run a production pass: have the agent list every route and its guard, every TODO and deploy step, and the usual omissions (webhooks, rate limits, uploads, debug mode, logs, backups), then hand that scope to a qualified expert for what you cannot check yourself. | C008, C066, C118 | S039, S041, S214, S220 | todo |

## Module 20 — Your users

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 20.01 | [Your users' data and your app's AI](curriculum/lessons/your-users-data-and-your-apps-ai.md) | Your users' data lives in more places than the database (buckets, logs, analytics, backups, the AI provider you send it to), and an AI feature lets strangers run your meter and speak for you: collect less, map every copy and delete for real, put model calls behind sign-in with caps that stop, treat model output as untrusted, say it is an AI, and ask before data goes to a provider. | C119, C121, C131 | S216, S055, S233, S195 | todo |

## Module 21 — Publishing media

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 21.01 | [Publishing AI media](curriculum/lessons/publishing-ai-media.md) | Before you publish AI-made media, answer four separate questions: must you label it (in the EU, visibly and at first exposure, whatever the tool's watermark), may you sell it under the plan that made it, do you own any of it (purely AI-made work has no US copyright), and does it use someone's voice, face or mark without consent; ask a lawyer when money is at stake. | C110, C111, C113, C114, C115, C133 | S076, S077, S203, S078, S200 | todo |

# Finish · Capstone — one project, idea to running

## Module 22 — Capstone

| ID | Lesson | Key idea | Concepts | Sources | Status |
|---|---|---|---|---|---|
| 22.01 | [One project, idea to running](curriculum/lessons/one-project-idea-to-running.md) | Take one small real project from idea to running through every district: decide whether it is worth building and for whom, brief, build and check it, fence the agent, lock the app, run the production pass, then own the ship decision and what follows (patches, outcomes, users), because the agent carries no accountability and you do. | C043, C009, C020 | S007, S115, S068, S229 | todo |

---

## Legacy lessons (published before 2026-10-12; kept, marked, rebuilt later)

| Legacy lesson | Slug | Covers | Note |
|---|---|---|---|
| 00.01 The hidden curriculum | 00-01-the-hidden-curriculum | 00.01 | Its idea (the gap is in the syllabus, not in you) still holds, but it draws the old six-district map and predates the weekly-change and community parts of the core idea, so the new 00.01 (C024, C052, the new map, GitHub issues) replaces it. |
| 00.02 The map of everything | 00-02-the-map-of-everything | 00.01 | Its five-stop road (computer, network, internet, services, AI) is superseded by the district map; its "which stop broke?" habit survives as the what-runs-where map in 03.01 and 03.02 (C125, C127). |
| 00.03 How old is all this? | 00-03-how-old-is-all-this | 00.01 | Covers the "versions change every year, security and AI fastest" half of C052. The new 00.01 adds the weekly cadence (retirements, removed commands, changelogs) and the model's own knowledge date (C024); fold what still holds into the 00.01 rebuild. |
| 00.04 Model vs app vs agent | 00-04-model-vs-app-vs-agent | 00.03 | Engine, car and driver cover model vs harness (C021). Rebuild adds the April 2026 harness regressions (S014) and "name the whole configuration"; surfaces (C022) now live in 01.02. |
| 00.05 How AI models work today | 00-05-how-llms-work-just-enough | 00.03, 04.03, 07.01 | Its desk model covers C023 and C025, so it carries 00.03 with 00.04. Its context, caching and diffusion segments partly stand in for 04.03 and 07.01 until those are made; at about 20 minutes it should be split when rebuilt. |
| 00.06 Trust what you can verify | 00-06-how-to-learn-anything-technical | 00.02 | Made on 2026-10-03 from Aaron's correction, it covers C001 well. Rebuild adds the jagged frontier and benchmark reading (C002) and points to how to bring in an expert (C118, taught in 19.01). |
| 01.01 Files are just bytes | 01-01-files-are-just-bytes | — | No current concept: the gap came from the copy-from-chat workflow that agents replaced (concepts.md, G13 notes and C123). Kept as background; rebuild only if a new gap appears. |
| 01.02 File extensions & associations | 01-02-file-extensions-associations | — | Same as 01.01. If it is ever rebuilt, C093's finding that installers silently register "Open with" entries is the current hook. |
| 01.03 Folders, paths & the working directory | 01-03-folders-paths-the-working-directory | 01.01 | With 01.04 it covers C123's paths, working directory and hidden-not-locked points. Rebuild adds the folder as scope but not a wall, the home folder's valuables, one project folder, and copies on another disk. |
| 01.04 Hidden files & dotfiles | 01-04-hidden-files-dotfiles | 01.01 | Covers "hidden is not locked" (C123 point 4) and AI instruction files as dotfiles; see 01.03. |
| 01.05 Environment variables & PATH | 01-05-environment-variables-path | 01.02, 03.01 | Covers PATH (C122 point 3) and "each program gets a copy when it starts" (C126 point 1). 03.01 adds build-time values that ship to every visitor, `.env` as a convention not a vault, and per-environment values. |
| 01.06 Programs, processes & services | 01-06-programs-processes-services | 01.02, 03.01 | No concept of its own (G13 notes): a command starts a program (C122, in 01.02) and servers and functions are processes (C125, in 03.01). Decide at rebuild time whether it survives as a segment. |

## Deep-dive backlog (not scheduled)

| Topic | Concepts | Sources | Why it waits |
|---|---|---|---|
| Local and open-weight models | C031 | S033, S112 | Could: two low-severity items and two sources. Its licence half (C132) and media-model half (C032) are taught in 07.01; give it a lesson when running models locally becomes a main route for the audience. |
| What "good code" means when agents change it | C054 | S029, S035, S034 | Should, but partly speculative and openly disputed (Ball's prediction against Ronacher's evidence). Its concrete checks are already core: formatter and linter gates (C047 in 05.01), hooks that miss Bash edits (C045 in 05.02), and reading the final git diff (C012 in 08.01). |
| Checking an AI spreadsheet | C108 | S074 | Should, but all four items rest on one source (WorkstreamBench) and the concept itself asks for a second independent source before a full lesson. Its values-versus-structure example already appears in 00.02 through C002. |
| Hardware and physical devices | C109 | S075, S194, S251 | Could: one medium-severity item built on reader comments and a benchmark run by a tool vendor. The high-stakes half (mains power, compliance, production sign-off, the EU Cyber Resilience Act reporting duty since 2026-09-11) is taught in 19.01 through C008. Needs an independent incident or test-lab source first. |
| Monetising on platforms and storefronts | C116 | S205, S079, S239, S250 | Should: the stakes are high for people who earn from AI video or sell games, but the rules are specific to monetising creators, and YouTube is the only video platform the research read (TikTok, Meta and Spotify are a known gap). 21.01 teaches that stores and platforms are a separate layer that puts infringement on you (C133). |
| AI-written public-interest text in the EU | C112 | S076, S195, S197 | Could: one medium-severity item, EU-only, resting on non-binding interpretation. Teach it as a two-minute segment of 21.01 when that lesson is rebuilt, or with C116. |

## Rationale

### The map at a glance

| Region | Question | Modules | Lessons | New | Legacy-status | Lantern |
|---|---|---|---|---|---|---|
| Start · Orientation | what this is, and the lantern | 1 | 3 | 1 | 2 | 2 |
| 1 · The Ground | where does the work happen? | 3 | 5 | 4 | 1 | 1 |
| 2 · The Workbench | how do you get it built? | 4 | 8 | 8 | 0 | 8 |
| 3 · The Proof | how do you know it's right? | 2 | 4 | 4 | 0 | 3 |
| 4 · The Fence | what can your agent do to you? | 4 | 6 | 6 | 0 | 5 |
| 5 · The Night Shift | what runs while you're away? | 3 | 3 | 3 | 0 | 1 |
| 6 · The Locks | who can get in? | 2 | 3 | 3 | 0 | 0 |
| 7 · The Release | what changes when people arrive? | 3 | 3 | 3 | 0 | 2 |
| Finish · Capstone | one project, idea to running | 1 | 1 | 1 | 0 | 0 |
| **Total** | | **23** | **36** | **33** | **3** | **22** |

36 slots, the top of the 30-36 range: 33 new lessons (about a month at one a day) plus 3 slots that published lessons already cover well enough for now. District names are at most 15 characters, questions at most 32, module names at most 19. `tools/course.py check` on this file reports only the 36 spec files that do not exist yet, and its browser audit lays the map out with every module label on one line.

### Why these districts

Each district is one shelf the evidence fills, phrased as the question a builder asks at that moment, and the order follows the concepts' own **Requires** fields so that no district leans on a later one.

- **Start** keeps Aaron's approved frame: what the course is and the lantern you carry. It holds only what every later lesson assumes: the gaps move weekly (C052) and the model's knowledge has a date (C024), the course rule (C001, C002), and what you are actually talking to (C021, C023, C025).
- **The Ground** is the challenge pass's G13 group: the folder, the trail and terminal, git, the parts of an app, and the road to a URL. 35 concepts in other groups list these under **Requires**, so the ground floor comes first. C126 (environment variables) and C130 (dependencies) sit inside "what runs where" because their dangerous points (build-time values are public, installs run code) are about which part of the app holds what. C129 (accounts) sits with the URL lesson because going live is when the chain of accounts appears, and because C135 later requires it.
- **The Workbench** answers how work gets made now: directing (G04 plus the context window, since context engineering is choosing what goes on the agent's desk), house rules (G05), the meter (G06) and making media (C032, C030, C134, C132). It sits before the Proof because a check needs something to check, and because 04.01 ("done when") sets up 08.01 ("done is a claim").
- **The Proof** is G01 and G02: evidence the agent cannot write, checks it cannot game, why sounding right is not being right (including AI research and citations, C106-C107), and where human attention goes. The course rule is taught in 00.02; this district is that rule turned into habits.
- **The Fence** is G08, G09 and the agent-acting-as-you half of G11. It is named for its central lesson: the boundary goes in the environment, not in approvals (C078), so a fence rather than a leash. It comes right after the Proof because its risks start the first day someone runs an agent (auto mode is the default; C081), long before they ship anything.
- **The Night Shift** is G10: agents and automations that run unattended, deletes and undo, and failures that finish green. It extends the Fence (no approval prompts; everything runs as someone) and needs the Ground's git, URL and accounts.
- **The Locks** is the code-and-backend half of G07: insecure working code, authorisation and reachable databases, keys and leaks. It comes after the Fence so that "where secrets leak in agent work" (C070) can lean on "no credential worth stealing where the agent runs" (C082), and it sits next to the Release because securing the app is the gate before people arrive.
- **The Release** answers what changes when real people, data, money or an audience arrive: the production pass with an expert (C008, C066, C118), what you owe your users and what your app's AI may do (C119, C121, C131), and publishing AI media (G12). Its question is C008's own trigger.
- **Finish** is one worked project through every district, and it owns the three concepts that only make sense at the end: whether it is worth building (C043), who owns the ship decision and the patches after it (C009), and measuring outcomes rather than output (C020).

The order makes two arcs: the agent's power (Fence, then Night Shift) and the product's exposure (Locks, then Release, then Finish). Security, which Aaron singles out, gets two districts and 9 of the 33 new lessons (10.01 to 13.01 and 17.01 to 18.01), plus the security-test independence point in 08.02 and the production pass in 19.01.

Three placements were forced by the Requires fields and are worth knowing: C022 (surfaces) requires C128 (other machines), so it moved from the Start into 01.02; C033 (the job moved to directing) requires C117 and C122, so it opens the Workbench (04.01) rather than the Start; C135 (every automation runs as someone) requires C129, so accounts moved into the Ground (03.02).

### The Lanterns

22 lessons have AI itself as their subject (the model, the agent, how you direct, configure, pay for and contain it, and what it makes), and they hang over seven of the nine regions. The Ground has one (01.02, reading the agent's trail and choosing a surface); the Locks and the Finish have none, because they are about the world the agent acts on. The Workbench is lit throughout because in 2026 building means directing agents (C033: about 47% of last month's work code fully agent-generated, self-reported), but its question and its shelves (directing the work, house rules, the meter, making media) are about the work, not about "AI" as a topic, so it is not an AI district under another name. A lesson is marked only when AI is its subject: 15.01 (deletes and undo) and 12.01 (packages and repos) involve agents but are about your files and other people's code, so they are not marked.

### Density, and what the specs should cut first

Every lesson fills several gaps, and some are dense: 04.01, 04.02, 04.03, 05.01, 06.01, 09.01, 09.02 and 11.02 carry five concepts each, and 21.01 carries six. Most concepts in those lessons share one mechanism (for example, 04.03's five concepts all follow from "the whole conversation is resent every turn"), so the spec should teach the mechanism once and keep each concept to its two or three most surprising points, cutting supporting statistics first. Should and could concepts inside a lesson (C036, C095, C028, C053, C050, C029, C030, C010, C107, C018, C120, C080, C085, C092, C111, C133) are the first to shrink to a sentence if a lesson runs over 15 minutes. None should need more than 20.

### Coverage

All 135 concepts are placed: 129 in the 36 core slots and 6 in the backlog. Every must concept (including those marked must only for some builders: C119, C120, C121, C131, C132, C133, C134, C135) is in a core lesson. Every should concept is in a core lesson except C054, C108 and C116, which wait in the backlog with their reasons; three of the four could concepts (C031, C109, C112) wait there too, and the fourth (C050) is a segment of 05.02. Each concept sits in exactly one core lesson, and no concept is taught before a concept it requires.

### Legacy decisions

- **Legacy-status slots (3).** 00.02 (legacy 00.06, made from Aaron's correction on 2026-10-03, covers C001), 00.03 (legacy 00.04 and 00.05 together cover the model-in-a-harness and desk models, C021, C023, C025) and 01.01 (legacy 01.03 and 01.04 cover C123, as the concepts file itself records). Their missing points are taught where they bite later (for example the folder's scope in 05.01, 11.02 and 15.01).
- **Rebuilt as new (00.01).** The old 00.01 and 00.02 draw maps that no longer exist, and every new lesson opens on the new map, so the first lesson must introduce it, together with the weekly-change and community parts of Aaron's core idea.
- **Partial cover.** 00.05 is listed against 04.03 and 07.01, and 01.05 and 01.06 against 01.02 and 03.01, so the course page can offer them until the new lessons exist; those slots stay `todo`.
- **No cover.** 01.01 (files are bytes) and 01.02 (extensions) match no current concept; the G13 notes say that gap belonged to the copy-from-chat workflow. They stay published and listed, covering no slot.

### What was cut to the backlog, in one line each

Local models (C031, could), "good code" for agents (C054, disputed, its checks already core), AI spreadsheets (C108, one source), hardware (C109, could, its high-stakes half in 19.01), platform monetisation and storefronts (C116, creator-specific, one platform read) and EU public-interest text (C112, could, EU-only).

### Alternatives considered

- **Six districts, with one "Trust" district** holding both the Fence and the Locks (Aaron's earlier district name). Rejected: it would need all five module slots for eight or nine lessons, and it merges two mental models a learner should keep apart, "what can my own agent do to me" and "who can get into what I built".
- **Locks straight after the Proof.** It keeps "checking" and "security checking" adjacent, but it would split the Locks from the Release and put agent safety after shipping, though agent risks start on day one.
- **A cost district and a media district of their own.** Rejected for size: cost fits one dense Workbench lesson plus pieces placed where they bite (C060 in 14.01, C121's meter strangers can run in 20.01), and media divides naturally into making (07.01) and publishing (21.01).
- **Keeping 01.05 as its own legacy slot.** Rejected: C126's dangerous points (build-time values are public, per-environment settings) belong with what runs where, and the freed slot paid for making media.

### For Aaron to decide

1. Whether 36 slots is right. If the month runs short, the cheapest cut is 07.01 (Making media with AI): it is the only lesson whose concepts are all should priority, and legacy 00.05 already stands in for part of it. The next is folding 16.01 (Green is not success) into 14.01, which makes a lesson of about 20 minutes.
2. Whether legacy 01.01 and 01.02 stay listed as background or are unlisted from the course page.
3. Whether 00.03 is really covered well enough by 00.04 and 00.05 for now, given that the April 2026 harness postmortem (S014) is the strongest current case for C021 and neither legacy lesson has it.

### Evidence notes

- This design draws only on `curriculum/concepts.md`, `curriculum/sources.md`, `curriculum/research/challenge-log.md`, `COURSE.md` and `course.json` as they stood on 2026-10-12; no new sources were fetched, and every S-ID cited above is defined in `sources.md`. The old curriculum was used only to place the legacy lessons.
- The sources picked for each lesson favour the most recent credible ones. The 36 lessons make 160 citations of 119 distinct sources: 72 are dated 2026-07 or later; 25 are live documentation, terms or law pages without a page date, read on 2026-10-12 (most name a software version or change from September or October 2026); and 22 are older. Of those 22, three were updated in the last three months (S039 v4 2026-09-14, S041 2026-07-03, S042 2026-10-04); four are marked foundational and still current (S027 Karpathy 2025-11, S049 Willison 2025-06, S203 US Copyright Office 2025-01, S214 NCSC); eight are the primary record of an incident or platform change with no newer equivalent (S014, S020, S044, S060, S071, S140, S148, S225); five are courses, studies or reports from 2026-01 to 2026-06 (S050, S058, S085, S209, S221); one is a paper whose tested models are older (S073); and one is the Next.js advisory from 2025-12 that 22.01 uses for patches after launch (S229).
- Thin spots the lesson planners inherit from the concepts file: C036 rests mainly on one Anthropic author; C085 on one core source; C093's download checklist mainly on Aaron's own session (S062); C131 still needs California's SB 243 re-fetched; C103's OpenAI column could not be filled (HTTP 403); the G13 concepts have no collected beginner questions yet because search was used up and Reddit blocks the fetcher.
