# G04 Directing the work: intent, specs and scope

Concept entries C033-C043, written 2026-10-12 by the concepts-directing-work agent.

Built from `research/taxonomy.md` (which items each concept merges), the gap items and reading notes in `research/notes/` (practitioners-now, vendor-academies, surveys-and-learning, verification, courses-teach-now, rules-enforcement-churn, unattended-action) and `research/sources-candidates.md`. Every point ends with the sources it rests on. S-IDs are in the source index at the end of `taxonomy.md`; G04-N IDs are the new sources listed below.

## How this was checked

- **Re-opened on 2026-10-12** (raw page text, not a tool summary), because whole concepts lean on them:
  - S037: the four kinds of unknowns, the "bottlenecked" line, and every technique prompt quoted below.
  - S033: the November 2025 threshold, the Fable-class definition, AI mania.
  - S034: spec bugs, terminal flags, meat proxies.
  - S081: the 47 / 38 / 27 split and its bucket caveat.
  - S029: "fully delegate only 0-20%", the 8x merge figure, the goal-choice gap.
- **Thin-evidence concepts.** The taxonomy flagged C036 and C037 as resting on S037 alone. This pass added Anthropic docs (G04-N1, G04-N2), one independent practitioner (G04-N5) and one independent caution (G04-N3). C036 is still mostly vendor-sourced, and its entry says so.
- **Search budget.** The shared web-search budget for this turn was used up before this agent's first search. The new sources were fetched directly from URLs that were already logged in `research/sweep/*.md` or in the notes' lead lists. No URL was guessed.

## New sources read for this group (no S-ID yet)

Give them S-IDs if the crew adopts them.

| ID | Title | Author | Date | URL | How much was read |
|---|---|---|---|---|---|
| G04-N1 | Best practices for Claude Code | Anthropic (Claude Code docs) | Undated live doc. Content is no earlier than 2026-09-25: it names v2.1.283, which the Claude Code changelog dates to that day. Fetched 2026-10-12 | https://code.claude.com/docs/en/best-practices | Full (markdown version) |
| G04-N2 | Output styles | Anthropic (Claude Code docs) | Undated live doc. Content is no earlier than 2026-08-20: it names v2.1.237, which the changelog dates to that day. Fetched 2026-10-12 | https://code.claude.com/docs/en/output-styles | The built-in styles section |
| G04-N3 | Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop (AI Engineer World's Fair 2026) | Gabriel Martinez, G2i | 2026-10-09 (YouTube uploadDate) | https://ai.engineer/talks/6qkzlT962es (video: https://www.youtube.com/watch?v=6qkzlT962es) | Full transcript. Ends with a plug for his company's workflow tool (ORC); his claims are judgment, not measurement |
| G04-N4 | Human judgment doesn't leave the software factory. It relocates. | Addy Osmani (Anthropic, member of technical staff) | 2026-08-21 | https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/ | Full |
| G04-N5 | My AI Adoption Journey | Mitchell Hashimoto | 2026-02-05. Older than 3 months, within 12. He says he has no ties to AI companies | https://mitchellh.com/writing/my-ai-adoption-journey | Full |
| G04-N6 | From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI | Margaret-Anne Storey | v1 2026-03-23, v4 2026-04-06 | https://arxiv.org/abs/2603.22106 | Abstract only |
| G04-N7 | Anthropic Education Report: The AI Fluency Index | Kristen Swanson, Drew Bent, Zoe Ludwig, Rick Dakan, Joe Feller (Anthropic) | The page says "originally published February 23, 2026"; its BibTeX says 2026-02-16. Data from 2026-01-20 to 01-26 | https://academy.claude.com/tutorials/the-ai-fluency-index | Full |
| G04-N8 | Spec-Driven Development with Coding Agents | Paul Everitt (JetBrains), DeepLearning.AI | "Updated Apr 18, 2026" | https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents | Course page and outline only |

**Also cited inside points.** These were fetched by other batch readers and have no S-ID:
- LangWatch, "The Context Tax" (2026-08-02), from the S003 notes.
- The nomArmy findings and Advani's paper, from the S030 notes.
- "A Paradox of AI Fluency" (2026-04-28), the companion to S085.
- SWE Refactor Bench, as reported in S036.

**Affiliation.** Some sources come from the vendors whose tools they describe:
- Anthropic staff: S029, S036, S084 and G04-N4 (Osmani), and S037 (Shihipar).
- Anthropic material: S005, S006, S007, G04-N1, G04-N2 and G04-N7.
- OpenAI: S008 and S022.
- Independent: S001-S003 (Stanford), S030, S031, S033, S034, S035, S068, S080-S083, S085, G04-N3, G04-N5 and G04-N6. (S083 is Anthropic research, but it is a randomized trial.)

---

### C033 The job moved from typing code to directing agents

- **In one line:** Coding agents became reliable for daily work in November 2025. Developers now self-report that about 47% of last month's work code was fully agent-generated. Delegation is the default: the agent owns the command syntax and the edit-run-fix loop, and the human decides, specifies, steers and verifies.

- **Why it is a gap:**
  - **Old picture.** Many people formed their view of AI coding from 2023-2024 chat assistants: paste code in, then fix the snippet by hand. Willison dates the change to November 2025. That month Claude Opus 4.5 and GPT-5.1, paired with their harnesses, went from "often make mistakes" to reliable for everyday use (S033).
  - **The baseline has moved.**
    - JetBrains surveyed 15,000+ developers in May-July 2026. On average about 47% of their code was fully agent-generated, 38% AI-assisted and 27% manual. Over half write less than 20% of their code by hand, and about 22% generate over 80% with agents (S081).
    - Stack Overflow 2026: 65.9% use coding assistants or agents at work, and 73.0% of those use them daily. 69.9% turn to an AI agent first when they hit a problem (S080).
  - **The vendors teach delegation from day one.** OpenAI's beginner bootcamp names three phases (next-line completion, pair chat, delegating the whole task) and calls the user a manager of agents (S008). Anthropic's entry course opens with agent versus chat and the agentic loop (S005).
  - **This course already fell into the old frame.** Aaron sent back a lesson that taught a five-step hand-debugging habit (S004). Stanford's Fall 2026 CS146S dropped its debugging and diagnostics topics entirely (S001).

- **What to teach (specific points):**
  1. **When it changed.** Agents became reliable for day-to-day work in November 2025. By September 2026 Willison says his January prediction, that it would become undeniable that LLMs write good code, has come true (S033). In Q2 2026 the typical Anthropic engineer merged about 8x as much code per day as in 2024, described as "directing and reviewing, rather than typing" (S029).
  2. **Three phases.** AI in software went from completion to pair programming to delegation. In delegation your job is to scope the task and to understand and review what the agent did (S008). The agent's loop is gather context, act, verify, repeat, and you can interrupt and steer it mid-loop (S005, S008).
  3. **Read the numbers carefully.**
     - The ~47% is a self-reported average built from answer buckets, so the three averages sum to more than 100%. Seniors move to agents first; juniors stay with AI-assisted work (S081).
     - Tool rankings depend on the survey. JetBrains cites 39% work adoption for Claude Code; Stack Overflow reports 65.5% "used in the past year". Treat tool popularity as a snapshot (S081, S080).
  4. **Delegation is not total.**
     - Anthropic surveyed its own engineers: most could fully delegate only 0-20% of their work. The rest still needs active supervision, especially on high-stakes work (S029).
     - In the last 30 days, only 18.9% of developers delegated "changing production" to an agent, against 72.9% who delegated writing code (S080).
  5. **More output, unknown quality.** Microsoft engineers who adopted the tools merged about 24% more PRs per day than a synthetic control predicted. The authors say a merged PR is not the value it delivers, and quality is now the open question (S082).
  6. **The four skills the human now needs:**
     - deciding what is worth doing;
     - specifying the outcome;
     - steering mid-flight;
     - verifying, that is, deciding when the evidence is enough (S084).

     The share of code humans type falls, but ownership does not. Someone still chooses the problem, the architecture and the quality bar, and decides when the evidence is enough to ship (G04-N4).
  7. **Command syntax belongs to the agent.** What a beginner needs is the concept: what a terminal is, what a command can touch, and how to read what the agent ran. Ball's "the terminal is dead, nobody needs to know flags" is a prediction. Willison still describes agents working by writing and running code on your computer (S034, S033).
  8. **Do real work in an agent, not a chat window.** An agent can at least read files, run programs and make HTTP requests. Copying code and command output between a chatbot and your editor is the slow pre-agent workflow (G04-N5, S005).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** reads the project, writes code, runs it, reads the errors and fixes them in a loop. It can open a browser and test its own work, which the Stanford lecturer says was not possible six months earlier (S003, S033).
  - **The human:** decides what to build; states the goal, the constraints and what done means; connects the tools; steers; and checks what the agent cannot verify (S033, S084).
  - **When to bring in an expert:** wherever you cannot check the result, such as security, deploy readiness, payments and auth (S004, S029). Professionals themselves rarely let agents change production (S080).

- **Currency:** Established since November 2025 (S033). The survey baselines are new in 2026: S080 fieldwork ran 2026-06-23 to 08-05, and S081 surveyed May-July 2026. Changing now: Stanford rebuilt its course around the agent harness this fall (S001). Ball's claims that terminals and flag knowledge disappear are speculation (S034).

- **Outdated framings to avoid:**
  - "AI coding is autocomplete, or pasting snippets from a chat window" (S008 phase 1; S033; G04-N5).
  - "Real developers write their own code." Purely manual coding is now a minority practice (S081).
  - Hand-debugging as the core skill to teach (S004, S001).
  - The opposite overclaim, "agents do everything now". Most Anthropic engineers fully delegate only 0-20% of their work (S029). Few developers delegate production changes (S080). Nobody has measured whether quality improved (S082).
  - "Memorize command-line flags" as a beginner requirement. This rests on a prediction (S034).

- **Questions it answers** (logged in the gap items):
  - Do I still need to write code myself? What is my job if the agent writes everything? (S008)
  - Is AI actually good at writing code now, or is that hype? Why do people say they don't write code by hand any more? (S033)
  - Do professional developers really let AI write their code? Am I cheating if the agent writes everything? (S081)
  - Do I need to learn the command line? What is the agent doing in that terminal window? (S034)

- **Show it for real:**
  - A timeline (Feb 2025 Claude Code; Nov 2025 Opus 4.5 and GPT-5.1; June 2026 Claude Fable 5). Then a coding agent in a terminal reads a project, makes a change, runs the tests and fixes its own error while no human types code (practitioners-now #01 demo; S033).
  - The same small feature built three ways: an inline completion, a chat answer pasted in, and an agent run that edits, tests and reports. Compare how much the human typed and how much they had to review (vendor-academies #02 demo; S008).
  - An agent's terminal transcript, annotated with what each command touched (files read, network calls, installs) and no flags explained (practitioners-now #16 demo; S034).

- **Priority:** must.
  - It is the frame for every other lesson in this group and for the course rule.
  - It has 4 items from 3 batches, plus three current sources re-read or added here (S029, G04-N4, G04-N5).
  - Each item was rated medium severity, but the course has already shipped one lesson that missed this frame (S004).

---

### C034 You supply the goal, the constraints and the tools; most bugs become "you asked for the wrong thing"

- **In one line:** Current models brute-force any clearly defined goal when they get unambiguous constraints and the tools to check their own work. So failures move upstream, into what was asked for. The agent fixes code bugs itself; it cannot know what you never said.

- **Why it is a gap:**
  - **People expect a stronger model to need less from them.** Willison's definition says the opposite. A "Fable class model" solves your problem "through brute force" if you:
    - clearly define the goal,
    - give unambiguous instructions about the constraints, and
    - give it access to the necessary tools.

    He adds that this is "kind of what software engineering is" (S033).
  - **Anthropic's own practitioner agrees.** Shihipar says Claude Fable is the first model where the quality of the work is bottlenecked by his ability to clarify its unknowns (S037).
  - **Ball's prediction:** most bugs won't be coding bugs; they will be "you asked for the wrong thing" bugs (S034, a prediction).
  - **Real cases where the wrong thing passed every check:**
    - The requirement was "refund only after a successful capture". The model built "refund if a payment record exists", and code, tests and AI review were all green (S030).
    - Asked to add GitHub as an auth provider, an agent dropped another provider that customers wanted, because the UI had room for only three (G04-N4).
  - **Anthropic's builder course names the pattern.** When a user need is badly translated, the code works but the product doesn't, or the tests pass but don't solve the real problem. The failure sits upstream of the prompt (S007).

- **What to teach (specific points):**
  1. **The three inputs only you can supply:** the goal, the constraints, and access to the tools the agent needs to reach the goal (S033). Give it a check it can run. Without one, "looks done" is the only signal the agent has, and you become the verification loop (G04-N1). What an agent can score automatically is what it can grind on (S027).
  2. **Specificity cuts both ways.** Too specific, and the agent follows your instructions even when a pivot would be better. Too vague, and it falls back on generic industry best practice that may not fit your task (S037). Constraints written for older models can over-constrain newer ones (S022).
  3. **Long tasks drift.** Every unknown forces the agent to guess what you want, and more work means more unknowns (S037).
  4. **When the output is wrong, ask "what did I not say?" before hunting for a code bug.** The agent repairs code errors itself; it cannot infer a requirement nobody stated (S034, S037, S007). It "can infer intent, but it can't read your mind", so reference the specific files, constraints and example patterns (G04-N1).
  5. **Green checks prove only what they encode.**
     - A shared misunderstanding passes code, tests and AI review together (S030).
     - Asked to pass a test, an agent may change the test, or the logic, without following your intent (G04-N4).
  6. **Choosing the goal is where models are weakest.** Anthropic's own assessment: Claude matches skilled researchers at running a well-specified experiment, but large gaps remain in choosing goals (S029). Tasks with an automatic score race ahead; tasks without one lag (S027).
  7. **A guess hides the decision.** Polished output conceals that a decision was needed at all, so you never notice the choice and the unknown unknowns stay unknown (G04-N3).
  8. **Your effort moves upstream,** from implementation to specification and evaluation (S031).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** builds, runs, fixes and iterates inside the bounds you set, brute-forcing toward whatever check it has (S033, S027).
  - **The human:** owns the specification: who the users are, what must happen, what must never happen, and which edge cases matter. The human checks results against intent, not just "it runs" (S034, S037, S007).
  - **When to bring in an expert:** when you cannot state a domain's constraints yourself. GitHub's own exercise shows a domain rule the agent won't volunteer: rounding each share of a bill separately loses or invents money (S009). Security and deploy-readiness claims are the same case (S004).

- **Currency:** New in 2026.
  - The Fable-class framing dates from June 2026 (Claude Fable 5) and now also covers GPT-6 Astra (S033).
  - S037 describes current practice (July 2026). Ball's version is a September 2026 prediction (S034).
  - Changing now: vendors are telling users to prune instructions written for weaker models (S022).

- **Outdated framings to avoid:**
  - "Better models need less direction" (S033, S037).
  - "Prompting is about magic phrasing." The skill is goals, constraints and tools (S033). OpenAI's presenter also rejects "prompting is dead" (S008).
  - "If it compiles and the tests pass, it's correct" (S030, G04-N4, S007).
  - "The more detail in the prompt, the better." Over-specifying blocks useful pivots (S037, S022).
  - "Bugs are typos and logic errors that you find by debugging" (S034, S004).

- **Questions it answers** (logged in the gap items):
  - What do I actually need to tell the agent? Why did it build something that technically works but isn't what I wanted? If the AI can build anything, what is left for me to do? (S033, S037)
  - The AI did exactly what I said, so why is it wrong? How do I write a good spec for an agent? Why does the agent keep making assumptions? (S034, S037)

- **Show it for real:**
  - Give the same agent two task statements side by side: "make a booking site", and one with a clear goal, explicit constraints and the tools wired up (a test database, a browser preview). Show the second run checking its own work while the first one guesses (practitioners-now #02 demo).
  - Give a one-line feature request and let the agent build it. Then reveal a rule the user assumed but never said ("only admins can delete"), and show the agent fixing it as soon as it is stated (practitioners-now #14 demo).
  - Walk through S030's refund case on screen: every check green, wrong behaviour.

- **Priority:** must.
  - Both items are rated high severity and are new in 2026.
  - The claim now rests on six sources from different angles: S033, S037, S034, S030, S007 and G04-N4, and the S033/S034 author and the S030 survey are independent of any vendor.
  - It is the upstream half of the course rule: whether the agent built the right thing is exactly what it cannot verify.

---

### C035 Your unknowns and unwritten context limit the agent

- **In one line:** Constraints in your head, team history, past decisions and how production really behaves never reach the agent unless someone writes them down. The repo is not the whole system. Externalize your intent in files the agent reads, and have it surface its assumptions before it builds.

- **Why it is a gap:**
  - **Professionals say context is the hard part** (Stack Overflow 2026, n = 12,374):
    - context is incomplete (63.2%), lives in people's heads (60.9%) or is outdated (56.5%);
    - 78.6% discover important context only after starting or finishing a task, at least sometimes;
    - only 19.7% list compliance, security or policy requirements among the context they need (S080).

    The agent inherits all of these gaps.
  - **Every session starts from zero.** Each new session is like onboarding a new hire with amnesia (S084). Users report "prompt fatigue" from re-establishing context, and a preference such as "use logging instead of print" may not survive to next week (S031).
  - **The clarification spiral:** the agent builds without inferring your unstated constraints, you reject the result, and new misunderstandings appear (S031).
  - **The repo is not the system.** Institutional knowledge, legacy services and other teams' expectations live outside the code. Once an agent drops code you didn't decide line by line, you are in a brownfield project, which covers every vibe-coded app (S036).
  - **People rarely say how they want to work.** Only 30% of conversations set the terms of the collaboration. When people build artifacts, they identify missing context less often (-5.2 points) (G04-N7).
  - **Aaron's own case:** without someone who knows which libraries the project should use, the AI keeps adding dependencies (S004).

- **What to teach (specific points):**
  1. **Map versus territory.** Your prompts, skills and context are the map; the codebase and its real constraints are the territory. The gap between them is unknowns, and at each one the agent guesses (S037). There are four kinds (S037):
     - known knowns: what is in your prompt;
     - known unknowns: what you know you haven't figured out;
     - unknown knowns: too obvious to write down, but you'd recognize it on sight;
     - unknown unknowns: what you haven't considered at all.
  2. **Tell the agent your starting point:** where you are in your thinking, and how much experience you have with the problem and the codebase (S037).
  3. **Put intent outside your head:** instructions, relevant context and constraints. Agents should infer goals, surface their assumptions and signal uncertainty (S031). Ask for that explicitly, with lines like "Push back if my assumptions are wrong" and "Tell me what you're uncertain about" (G04-N7). While it works, ask what it ruled out and what it assumed (S084).
  4. **Put lasting context where every session loads it:** project goals, past decisions and why they were made, and constraints including security and privacy rules. Turn corrections into lasting artifacts (a lessons file, lint rules, types, tests), not chat memory that compaction erases (S084, S080). CLAUDE.md holds what the agent can't infer from the code (commands it can't guess, non-default style, architectural decisions, gotchas), and a bloated one gets ignored (G04-N1).
  5. **Write down what the code can't say, and nothing else** (S036):
     - business and team nuance;
     - the trade-offs behind the structure;
     - guidelines no tool enforces;
     - domain rules and external constraints;
     - the history behind code that looks wrong.

     Storey calls the lack of this "intent debt": missing rationale, goals and constraints that both humans and agents need (G04-N6).
  6. **Get what lives outside the repo from people:** who depends on what, what production actually does, and why odd code exists (S036). Watch what the agent is doing, because you may know something you didn't tell it (S008).
  7. **Settings change how much the agent assumes.** Claude Code's Proactive output style makes reasonable assumptions on routine decisions instead of asking. Plan mode reads and answers questions without changing files (G04-N2, G04-N1).
  8. **Name the constraints nobody lists:** security and compliance rules (listed by only 19.7%), and who owns the dependency list (S080, S004).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** reads whatever files and docs it is given, maps the code, drafts the notes, and surfaces its assumptions when asked (S080, S036, S031).
  - **The human:** supplies goals, constraints, past decisions and the reasons behind them, including security and privacy rules. The human keeps these in files the agent loads every session, and updates them after each correction (S080, S084).
  - **When to bring in an expert:** knowledge that lives in other people has to come from them: the owners of legacy services, compliance, whoever decides which libraries the project uses (S036, S004).

- **Currency:**
  - Established as an idea (brownfield, S036).
  - New in 2026 as measured: Stack Overflow's knowledge-and-context chapter is new this year (S080), and S031 and S037 are from July 2026.
  - Changing now: Anthropic advises keeping CLAUDE.md short and pruning it (G04-N1), and Osmani names stuffing markdown files into context as an outdated habit (S036).

- **Outdated framings to avoid:**
  - "The AI knows my project" (S080, S084).
  - "The agent remembers what I told it last week" (S031, S084).
  - "The agent can read the whole codebase, so it knows the whole system" (S036).
  - "A better model will fix miscommunication" (S031). S037 says the better model is exactly what makes your unknowns the bottleneck.
  - "Put a markdown file for everything into context" (S036). A bloated CLAUDE.md gets ignored (G04-N1).

- **Questions it answers** (logged in the gap items):
  - Why does the agent keep making the same mistake? Why did it build the wrong thing? What should I tell it before it starts? (S080, S084)
  - Why does the agent keep building the wrong thing even after I correct it? Why do I have to re-explain my preferences every session? (S031)
  - Why did the AI break something it couldn't see? My app is only three months old, so why is it hard to change? (S036)
  - How do I tell the AI what I want when I don't know the field? (S037)

- **Show it for real:**
  - Make the same request twice: in a fresh session with no project notes, then with a short project file listing the goal, one privacy rule and one past decision. Show the outputs side by side (surveys-and-learning #04 demo).
  - Show a chat that goes through three rounds of "no, not like that". Restart with the constraints written up front plus an instructions file the agent reads, and show the first attempt landing (verification #18 demo).
  - Run `/context` to show what the session actually loaded (G04-N1).

- **Priority:** must.
  - 3 of its 4 items are rated high severity.
  - It is backed by a survey of more than 12,000 respondents (S080), an academic position paper (S031), two practitioners (S036, S037), and now G04-N6 and G04-N7.
  - All sources date from 2026.

---

### C036 Let the agent teach you the territory first: the blind-spot pass

- **In one line:** In an unfamiliar codebase or domain, ask the agent to find your unknown unknowns and explain them before you prompt for the work. Then you know what to ask for and what good looks like. You still judge the output yourself, or bring in someone who can.

- **Why it is a gap:**
  - **Beginners in unfamiliar territory guess, or pick blind.** They either guess at a prompt or choose among variations without knowing what good looks like. Shihipar did the second with color grading for a launch video, then asked Claude to teach him instead (S037).
  - **You can only ask for what you can imagine.** Osmani's line: verification is the floor, imagination is the ceiling. His 3D album site rendered, but it used the wrong interaction pattern and ran poorly on mobile, and it took expertise to notice (S084).
  - **Smooth output keeps you ignorant.** When AI output arrives smoothed over, the engineer never hits the ambiguity, so the unknown unknowns stay unknown (G04-N3).
  - **Delegating without understanding costs skill.** In Anthropic's randomized trial, people who let AI write everything scored lowest on the follow-up quiz. People who asked conceptual questions kept their learning and were the second-fastest group (S083).

- **What to teach (specific points):**
  1. **When to run it:** when you enter a new part of a codebase or a new domain, where you don't know what questions to ask, what good looks like, what has been done before, or which potholes to avoid (S037).
  2. **How to ask:** use the literal words "blind spot pass" and "unknown unknowns", and say who you are and what you know. S037's two example prompts:
     - adding a new auth provider in modules you know nothing about;
     - color grading a video when you don't know what color grading is (S037).
  3. **What the agent brings.** It searches the codebase and the web very fast, and it knows more about the average topic than you (S037).
     - In a codebase, ask it what you would ask a senior engineer: how logging works, which edge cases a flow handles, why this call and not that one (G04-N1).
     - A research document of what the code does today seeds the agent and gives you a mental model at the same time (S003).
  4. **Other ways to surface unknown unknowns:**
     - Hashimoto ran parallel agents on vague ideas, not to ship them but to illuminate unknown unknowns before he started the task the next day. He also ran research agents to survey a field (G04-N5).
     - Open questions such as "what would you improve in this file?" surface things you wouldn't have thought to ask (G04-N1).
  5. **Keep learning on.** Claude Code's Explanatory output style adds short "Insight" blocks that explain the choices behind the code. The Learning style also leaves real design decisions for you to write (G04-N2). Asking for explanations and conceptual answers preserves learning; pure delegation does not (S083, S084).
  6. **Know its limits.** A model's knowledge is weakest on rare, recent, niche or contested topics, so bring your own sources there (S006). The pass teaches you enough to prompt and to judge; it does not make you the expert. Red-zone areas such as auth, billing and permissions still need a human on every step (S036, S004).
  7. **Close the loop.** Turn the list of unknowns it returns into a better prompt (S037).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** maps the territory, explains concepts, lists what you didn't know to ask, and can quiz you on a change before you merge it (S037, G04-N1).
  - **The human:** admits what they don't know, states their level, reads the result, decides what matters, and still owns the judgment of the output (S037, S084).
  - **When to bring in an expert:** in red zones (auth, billing, permissions) and on anything you will have to vouch for. There the pass is a starting point, not a substitute for someone who can verify (S036, S004).

- **Currency:**
  - New in 2026 as a named technique (S037, July 2026).
  - The underlying move (use the agent to learn the code or the domain first) also appears in Anthropic's live docs (G04-N1) and in Hashimoto's independent practice (G04-N5, February 2026).
  - Changing now: teaching modes have become product features, Explanatory and Learning in Claude Code (G04-N2), and S083 also names ChatGPT Study Mode.

- **Outdated framings to avoid:**
  - "Ask for several variations and pick one," when you don't know what good looks like (S037).
  - "Pretend to know the domain and prompt confidently" (S037).
  - "Once the agent can do it, you don't need to understand it" (S084, S083).
  - The opposite, "never use AI while learning." Conceptual-inquiry users kept their learning and were nearly as fast as the delegators (S083).

- **Questions it answers** (logged in the gap items):
  - How do I start working in a part of the code I don't understand? How do I learn enough to judge what the AI made? What should I ask before I ask it to build? (S037)
  - How do I tell the AI what I want when I don't know the field? (S037)
  - How do I understand a repo I didn't write? (S003)

- **Show it for real:**
  - In a coding agent on an unfamiliar project, type the auth-provider blind-spot prompt. Show the list of unknowns it returns, then the better follow-up prompt built from that list (practitioners-now #33 demo).
  - Switch Claude Code to the Explanatory style with `/output-style` and show an Insight block after a change (G04-N2).

- **Priority:** should.
  - Its one item is rated high severity, and it is the course's own premise turned into a technique.
  - But the named technique still rests mainly on one Anthropic author (S037). This pass added Anthropic docs (G04-N1, G04-N2) and one independent practitioner (G04-N5).
  - Teach it inside the C035 or C037 lesson rather than as a lesson of its own, until a second independent source names it.

---

### C037 Find what you want cheaply before building it

- **In one line:** Before you wire anything up:
  - brainstorm options from cheapest to most ambitious;
  - react to throwaway mockups that use fake data;
  - have the agent interview you, one question at a time, about the ambiguities that would change the architecture;
  - point it at reference code instead of describing the behaviour.

  Then build the real thing from the decision, in a fresh session.

- **Why it is a gap:**
  - **Discovering what you want during the build is expensive.** Beginners build the real feature in the real app, then find out what they wanted once the code is tangled. Small changes to a spec can cause drastically different code, and it is harder for the agent to revert earlier changes (S037).
  - **Behaviour is hard to put into words.** Beginners fall back on vague descriptions or screenshots (S037).
  - **Prototypes mislead.** A clickable prototype built in an hour makes stakeholders believe the hard part is done. Still ahead are integration, the requirements the prototype skipped, manual UX testing, and deciding whether the feature belongs at all (G04-N3).
  - **People scrutinize polished output less.** When building artifacts with AI, people give more direction up front (clarifying the goal +14.7 points) but evaluate less: identifying missing context -5.2, checking facts -3.7, questioning reasoning -3.1 (G04-N7).

- **What to teach (specific points):**
  1. **Brainstorm first.** Shihipar starts almost every coding session with exploration, so the scope is neither too narrow nor too wide. Example: search the codebase and brainstorm 10 places to intervene, from cheapest to most ambitious (S037).
  2. **Prototype as cheaply as possible:** a single HTML file with fake data, or several wildly different design directions to react to, before the agent touches the real app (S037). Agents make trying several options cheap; choosing still needs evidence such as tests and profiling (S036).
  3. **The prototype is not the product.** It skips integration, the requirements it bypassed, testing by a person, and the decision whether it belongs (G04-N3). Start the real build in a new session and pass it the spec and the prototype as artifacts (S037).
  4. **Have the agent interview you,** one question at a time, prioritizing questions where your answer would change the architecture (S037).
     - Anthropic's docs give a fuller version: have Claude interview you with the AskUserQuestion tool about implementation, UI/UX, edge cases and trade-offs; skip obvious questions; write the result to SPEC.md; then implement in a fresh session (G04-N1).
     - Kiro's Analyze Requirements does a similar job on a written spec. It flags vague terms, contradictions, unstated assumptions and missing edge cases (S024).
  5. **Point at a reference instead of describing.** Source code is the best reference, even in another language: S037's example has the agent reimplement a Rust crate's backoff behaviour in a TypeScript client (S037). Inside your own repo, name an existing component the agent should follow (G04-N1).
  6. **Bring your own variance.** AI-generated ideas tend to be commercially viable but very similar to each other; a human widens the range (S068).
  7. **Question the output when it looks finished.** Polished output gets less scrutiny, so that is the moment to ask what is missing (G04-N7).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** generates options, mockups, questions and the spec, and reads reference code and carries its behaviour over (S037, G04-N1).
  - **The human:** reacts, picks and sets the scope; answers the questions that fix the data model and structure; chooses the reference; and brings the variance the AI's ideas lack (S037, S068).
  - **When to bring in an expert:** a prototype proves nothing about readiness. Before real users arrive, the integration, security and UX checks need someone who can judge them (G04-N3, S004).

- **Currency:** New in 2026.
  - Sources: S037 (July 2026), G04-N1's interview section (live September-October 2026), G04-N3 (October 2026).
  - Changing now: the tools now ship features for this, such as AskUserQuestion in Claude Code (G04-N1) and Analyze Requirements in Kiro (S024).

- **Outdated framings to avoid:**
  - "Build the real thing first and adjust later" (S037).
  - "Design by describing what you want in words, or with a screenshot" (S037).
  - "Answer a wall of clarifying questions at once." The technique asks one at a time (S037).
  - "A working clickable prototype means the hard part is done" (G04-N3).

- **Questions it answers** (logged in the gap items):
  - How do I figure out what I want before the AI builds it? I have no design taste; how do I get a good-looking UI? (S037)
  - How do I get the AI to ask me the right questions? (S037)
  - How do I explain what I want when I don't have the words? Can the AI copy how another project does something? (S037)

- **Show it for real:**
  - Ask for one HTML file with four wildly different dashboard directions, using fake data. Open it in a browser, pick one, and start the real build from that choice (practitioners-now #34 demo).
  - Run the interview prompt and show that the first question is architectural ("single user or multiple accounts?") rather than cosmetic (practitioners-now #35 demo). In Claude Code, show the AskUserQuestion dialog and the SPEC.md it produces (G04-N1).

- **Priority:** should.
  - Three medium-severity items, all new in 2026.
  - It used to rest on S037 alone. Anthropic docs (G04-N1), Kiro docs (S024) and an independent caution (G04-N3) now back it.
  - High value for builders without design or product training, but no direct safety or money risk.

---

### C038 Define done before you delegate

- **In one line:** Before the agent starts, write down:
  - the goal;
  - the context;
  - the constraints;
  - a checkable "done when": acceptance criteria, test names, what is out of scope, and the evidence to report.

  This is where shared misunderstandings are cheap to catch. Without it, the agent invents its own finish line.

- **Why it is a gap:**
  - **Without a definition of done, the model invents its own** (S008).
  - **The non-coder on-ramp leaves it out.** Andrew Ng's beginner course teaches five prompt blocks (goal, input, output, layout, features) with no done-when and no check (S010).
  - **Beginners review the wrong end.** They jump straight to prompting and judge only the agent's final summary. That skips the one point where a shared misunderstanding is cheap to catch (the acceptance criteria) and reviews the least reliable artifact (the narrative) (S030).
  - **"Done" is a claim.** In one team's log, 24 of 265 "done, tests pass" claims did not hold when the harness re-verified them (S030).
  - **Newer models can stop too early.** GPT-6 Astra may pause for review after a first implementation unless the request says that running, inspecting and fixing are part of the task (S022).
  - **Migrations pass tests without finishing.** In SWE Refactor Bench, tests stay green while the new code still calls the legacy implementation. Across 520 agent runs, only 28 passed the migration audit, the behavioural tests and independent verification (S036).

- **What to teach (specific points):**
  1. **The four-part prompt: Goal, Context, Constraints, Done when.** OpenAI's worked example (S008):
     - Goal: change a savings APY shown as 4.02% to the approved 4.20%.
     - Context: find where the homepage value comes from, and its tests.
     - Constraints: a small change; leave unrelated work alone.
     - Done when: a regression test is added, the checks run, and evidence is reported.

     The approved 4.20% is a fact only the human has.
  2. **Write acceptance criteria before the code, from the user need,** not from what the AI produced (S007).
     - Make the criteria checkable, and include what is out of scope.
     - Approve the test names before the agent implements.
     - Name the failure modes you fear. In nomArmy, naming "no inert tests" moved a job from 1 of 3 real tests to 3 of 3 (S030).
  3. **Give the agent a check it can run:** example test cases, a build, a screenshot to compare (G04-N1). Let it launch the app, drive a real browser and read the logs (S021). Say in the request that running, inspecting and fixing are part of the job, and grant standing permission for known-safe loops such as the local test suite (S022).
  4. **Ask for evidence, not assertion:** the test output, the command and what it returned, a screenshot (G04-N1); a report of changes, evidence and remaining risks (S008). Before accepting, ask (S008):
     - Does the diff match the requested scope?
     - Which checks ran, and which passed, failed or were skipped?
     - What is still unverified?
  5. **Put stop rules in the brief.** Osmani's small factory prompt says: implement only the stated acceptance criteria; if a required check cannot run, stop and explain why; list any decision a human still needs to make; do not merge (G04-N4). Cap the fix-and-recheck rounds, or give exit criteria, so a ten-minute job doesn't run for an hour (S008).
  6. **Keep it human-sized.** Before an agent touches anything, write down what you're building, what it must not break, and how you'll know it worked. It needn't be long; it is where your judgment goes now (S029).
  7. **A migration is done when the old path is demonstrably gone and the traffic runs on the new path,** not when the tests pass (S036).
  8. **Name what the agent cannot verify,** such as whether it looks right or is secure, and check that yourself or with an expert (S032, S004).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** finds the code, makes the change, writes and runs the tests, reports the evidence, and can draft acceptance criteria when asked (S008, S022).
  - **The human:** supplies the facts only they know (the right value, the business rule), writes or approves the acceptance criteria and test names, defines what is out of scope, and checks the result against them rather than against the summary (S008, S030, S007).
  - **When to bring in an expert:** when "done" includes "secure" or "ready to deploy," the agent's word is not evidence. Bring in someone who can check it (S004).

- **Currency:**
  - Established in vendor teaching (S007 and S008, both September 2026).
  - New in 2026: the evidence on false "done" claims (S030, October 2026) and model-specific early stopping (S022, GPT-6 Astra, September 2026).
  - Changing now: tools add mechanical gates for done, such as Claude Code's `/goal` condition and Stop hooks (G04-N1).

- **Outdated framings to avoid:**
  - "Prompting is dead; describe the vibe and keep asking until it looks right" (S008, S010).
  - "Reviewing means reading the agent's final summary" (S030).
  - "The agent said the tests pass" (S030).
  - "The tests pass, so the migration is done; clean up the old code later" (S036).
  - "Make it stop for review after every step." This pulls the model toward stopping early (S022).
  - "Planning means approving a long AI-generated spec" (S030).

- **Questions it answers** (logged in the gap items):
  - How do I write a good prompt for an agent? How does the agent know when to stop? Why did it change things I didn't ask for? (S008)
  - Why does the agent stop before it's finished? How do I tell it what "done" means? Should I make it check in with me after each step? (S022)
  - What should I write before I start an agent? What should I look at when it finishes? (S030)
  - How do I know the switch to the new library actually happened? (S036)

- **Show it for real:**
  - Run "fix the homepage", then the four-part prompt, on the same repo. Compare the two diffs and the two final reports side by side (vendor-academies #03 demo).
  - Give the same task twice, once plainly and once with a done-when list (tests pass, the page loads in a browser, no console errors). Show the second run opening the browser and fixing an error on its own (rules-enforcement-churn #17 demo).
  - Write a five-line acceptance file before prompting, then check the result against it rather than against the summary (verification #17 demo).
  - After an agent "finished" a migration, search the repo for the old import and find it still called behind a shim (practitioners-now #28 demo).

- **Priority:** must.
  - 4 items from 4 batches, 2 of them high severity.
  - Both OpenAI's and Anthropic's courses put it first (S007, S008), and independent evidence shows "done" claims failing (S030).
  - Almost every source is from the last 3 months.

---

### C039 Map before you change

- **In one line:** In an existing codebase, including your own vibe-coded app, start with a read-only pass. The agent maps the structure, the commands and the conventions, cites files, and separates verified facts from assumptions. You read the map and correct it, then delegate a focused change.

- **Why it is a gap:**
  - **Beginners start blind.** They type "build X" into a codebase that neither they nor the agent has examined. Both OpenAI and Anthropic teach a read-only first pass (S008, S005).
  - **Most beginners have only built new projects alone,** and then struggle with existing ones. Stanford now grades open-source contributions at 30% of the course (S001).
  - **Unsupervised agents in old code go wrong quietly.** They produce something that "works" but has the wrong system design and brittle tests. Left to choose, the agent starts in the scariest file (S036).
  - **Your own app becomes brownfield fast** (S036).

- **What to teach (specific points):**
  1. **OpenAI's map prompt** (S008). Ask for:
     - the directories and what each is responsible for;
     - the files behind the core user flow;
     - the conventions to keep;
     - the install, run, test, lint and build commands;
     - the safest way to validate a small change.

     Have it cite files and keep verified facts apart from assumptions, with no edits yet. Review the map, then delegate.
  2. **Use the tool's read-only mode.** Anthropic teaches Explore → Plan → Code → Commit (S005). In plan mode Claude reads files and answers questions without changing anything (G04-N1). For big investigations, send subagents so the reading doesn't fill your main context (G04-N1).
  3. **The research step builds your mental model too.** RePPIT's research step documents only what the code does today, with no suggestions. The document seeds the agent and gives you a mental model (S003). You need a map-level model (there is a frontend and a backend, it uses this framework, the data model looks like this), not every detail (S003).
  4. **For risky work, make the research outlast the session.** Write a comprehension memo: entry points, owners, callers, tests, production signals, history and open questions, with each claim citing a file, issue or dashboard. Start with zero-risk work: first have the agent explain how the code works, then add characterization tests (S036).
  5. **A person draws the risk map, not the agent** (S036):
     - green: good tests, isolated; the agent works in a tight loop;
     - yellow: mixed quality; characterization tests come first;
     - red: auth, billing, permissions, anything few people understand; a human on every step.
  6. **Check the assumptions.** Check at least one against the code. When the agent guesses about files or rules, have it read the named file and state the constraints before it edits (S008).
  7. **Trust existing docs only if they are maintained.** Stale docs are worse than none (S003).
  8. **In someone else's project,** follow its contribution rules and expect a maintainer to review your PR (S003, S001).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** explores, maps, cites files, flags its uncertainty and answers codebase questions (S008, G04-N1).
  - **The human:** asks for the map, reads it, corrects wrong assumptions, draws the risk zones and approves the plan (S008, S036).
  - **When to bring in an expert:** red-zone code (auth, billing, permissions), and any surface that only production traffic really understands, needs its owner or someone who knows it (S036).

- **Currency:**
  - Established: taught in the vendor courses (S005, S008) and at Stanford (S003).
  - New in 2026: comprehension memos and zone maps for agent work (S036, September 2026).

- **Outdated framings to avoid:**
  - "Just tell it what to build and let it figure out the code" (S008).
  - "Contributing to open source means reading the whole codebase first." The research step builds the map for you and the agent (S003).
  - "Feed the agent all the existing docs." Stale docs are worse than none (S003).
  - "Let the agent choose where to start" (S036).

- **Questions it answers** (logged in the gap items):
  - How do I start with a codebase I didn't write? What is Plan Mode for? How do I know the agent understood my project? (S008)
  - How do I use AI to contribute to an open-source project? How do I understand a repo I didn't write? (S001, S003)
  - Can I point an agent at my company's old codebase? (S036)

- **Show it for real:**
  - Press Shift+Tab in Claude Code until the status bar shows plan mode, or tell Codex "do not edit files yet". Run the map prompt on an unfamiliar repo, point at the part marked as assumptions, and check one against the code (vendor-academies #04 demo; G04-N1).
  - Clone an open-source repo, run a research prompt, and open the resulting map next to the folder tree (courses-teach-now #29 demo).

- **Priority:** should.
  - Two established, medium-severity items, consistent across OpenAI, Anthropic, Stanford and Osmani.
  - It matters to anyone extending an existing app, including contributors to this course's own repo.
  - Less new, and less often the cause of harm, than C038 and C041.

---

### C040 Spec before code, scaled to the task

- **In one line:** For anything bigger than a one-sentence change, keep research and planning separate from implementation:
  - research what exists;
  - compare two options;
  - plan, with an explicit out-of-scope list;
  - review the plan;
  - implement in a fresh context and test.

  Scale the process to the size of the task, and keep the spec short enough that a person will actually review it.

- **Why it is a gap:**
  - **Vibe coding doesn't reach existing code.** It works for small changes but not for extending a codebase you didn't write (S003). DeepLearning.AI's course says vibe coding often produces code that doesn't match what you asked for (G04-N8).
  - **The cheapest checkpoint gets skipped.** Beginners prompt straight to code and review only the result, though requirements and design are the cheapest place to catch a wrong intent or a contradiction (S024, S003). Letting the agent jump straight to coding can solve the wrong problem (G04-N1).
  - **The process is the wrong size.** Beginners either over-process a one-line fix or try a whole migration in one prompt (S003).
  - **The opposite failure is real too.**
    - Users had little appetite for long AI-generated specs (S030).
    - Ten bullets of scope come back as a twenty-page document, and the unresolved decisions move to the reviewer (G04-N3).

- **What to teach (specific points):**
  1. **RePPIT,** taught in week 2 of Stanford's Fall 2026 CS146S (S003, S001):
     - **Research:** document what exists, with no suggestions.
     - **Propose:** two orthogonal options, each with trade-offs, validation and open questions. Returns fall off after two.
     - **Plan:** requirements, the files that change, tests, observability, security, rollout, and an explicit out-of-scope list.
     - **Implement:** the prompt is little more than "implement the plan".
     - **Test:** including in a browser.
  2. **Where the human matters most:** choosing between the proposals and reviewing the plan. The lecturer calls reviewing your specs the most important practice. Clear the context after choosing, so the rejected option doesn't confuse the agent (S003). A human picks the path, and implementation stops if the map turns out to be wrong (S036).
  3. **Scale the process to the task** (S003):
     - a copy change or small fix: just ask;
     - a small feature across several files: make a plan;
     - a medium feature, refactor or migration: repeated research, propose and plan, in separate sessions;
     - a very large project: split it into issues, one agent per issue.

     Anthropic's rule of thumb: if you could describe the diff in one sentence, skip the plan. Plan when you are unsure of the approach, when the change touches several files, or when you don't know the code (G04-N1).
  4. **Plan mode, demystified.** A tool switches the harness into planning, injects a prompt with phases, and ends by writing a plan file (S002). In Claude Code, Shift+Tab enters plan mode and Ctrl+G opens the plan in your editor before you approve it (G04-N1).
  5. **Spec tools: Kiro** (S024).
     - It writes requirements.md in EARS form ("WHEN condition, THE SYSTEM SHALL behaviour"), then design.md, then tasks.md, with an approval gate between each.
     - Quick Spec skips the gates. Kiro says it is not for unfamiliar territory or for compliance-sensitive or high-stakes systems.
     - Analyze Requirements finds vague terms and contradictions in minutes.

     Specs live in version control next to the code and are kept in sync with it (S024, G04-N8).
  6. **What a good spec contains:** the files and interfaces involved, what is out of scope, and an end-to-end verification step at the end (G04-N1). Put the decisions you are most likely to change first (data model, interfaces, anything user-facing) and the mechanical refactoring last (S037).
  7. **Implement in a fresh session from the written artifacts,** and have the agent log any deviations in an implementation-notes file (S037, G04-N1, S003). For vague requests, split planning and execution into separate sessions (G04-N5).
  8. **Keep it human-sized.** The real loop is understand, act, inspect, clarify, adjust; planning still happens, but not as one long document (S030). A spec that AI has expanded without resolving the ambiguity hands the thinking to the reviewer (G04-N3). Keep what you ask people to sign human-sized: a 100-page generated report has the same problem as a 5,000-line diff nobody read (S029). Choosing Quick Spec, or skipping the plan, is your decision to skip your own review (S024).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** researches, proposes, writes the spec and the task list, runs the requirements analysis, implements and tests (S003, S024).
  - **The human:** judges the size and risk of the task, picks the level of process, chooses between the proposals, and approves the requirements, design and scope. Whether the right thing is being built is the one thing the agent cannot verify (S003, S024).
  - **When to bring in an expert:** compliance-sensitive and high-stakes systems should not skip the review gates (S024). The security and rollout sections of a plan need someone who can judge them (S003, S004).

- **Currency:**
  - Established as practice: S003 calls spec-driven work the de facto industry method for hard tasks.
  - New in 2026 as core teaching: RePPIT is new in the Fall 2026 syllabus (S001), Kiro's docs were updated through October 2026 (S024), and DeepLearning.AI's course dates from April 2026 (G04-N8).
  - Changing now: built-in planning in Claude and Codex is good enough that the lecturer doesn't always use his own framework (S003), and practitioners are pushing back on long spec documents (S030, G04-N3).

- **Outdated framings to avoid:**
  - "Prompt, and fix what comes out, even for big features" (S024, S003).
  - "Every task needs the same workflow" (S003, G04-N1).
  - "A spec is a one-time document" (S024).
  - "Specs are bureaucracy; just describe the feature and let it go" (S003, G04-N8).
  - "A long up-front spec is enough," because unknowns surface mid-implementation (S037). Likewise "the human checkpoint is a long plan document" (S030).

- **Questions it answers** (logged in the gap items):
  - How do I get the AI to build something big without it going off the rails? What is spec-driven development? Should I plan before coding with AI? (S001, S003)
  - When should I use plan mode? Why did the agent rewrite half my app for a small change? (S002, S003)
  - What should I review if I can't read the code? (S024)

- **Show it for real:**
  - In a real repo, run research, propose and plan as three prompts. Open the two proposals, pick one, clear the context, and implement from the plan file (courses-teach-now #14 demo).
  - In Kiro, create a feature spec and show requirements.md in EARS form. Run Analyze Requirements to surface a vague term, approve the design, and run all tasks to show the waves executing (rules-enforcement-churn #18 demo).
  - In Claude Code, press Shift+Tab into plan mode and Ctrl+G to edit the plan. Compare that with a direct request for a one-line copy change (courses-teach-now #15 demo; G04-N1).

- **Priority:** must.
  - 3 items (1 rated high) from 2 batches, now joined by Anthropic docs, a DeepLearning.AI course, and independent pushback that sharpens the lesson (S030, G04-N3).
  - It is a core week at Stanford this fall (S001).
  - The lesson has to teach the scaling rule and the brevity rule, not just "write a spec".

---

### C041 Slice work small enough to review

- **In one line:** Agent patches run long and drift in scope, and long unattended runs can burn money without delivering anything. The people who do well with agents break work into slices they can review, keep each diff to the requested scope, try competing options cheaply and choose on evidence.

- **Why it is a gap:**
  - **One big prompt yields more than anyone can review,** and if the agent does more than you can review, you cannot manage it (S008).
  - **Agent patches are measurably longer.** On SWE-bench Verified they are consistently longer than the human "gold" patches, even when they solve the task. Every model has more than 15% of solved patches over 1.5 times the gold length. LLM judges attribute this to verbose code (about 60%), scope creep (50-65%) and overly defensive code (20-30%) (S031).
  - **Experience shows in how work is cut.** Microsoft survey respondents (609, self-selected) said the tools suit experienced developers who can break work into smaller chunks (S082). Professionals give richer context and work iteratively; non-developers rely more on AI-led generation (S085).
  - **Long runs can deliver nothing.** Ronacher's 35-hour GPT-6 Astra run used about 1B tokens and about $1,200 of API cost, and "delivered absolutely nothing of value". Give it a slightly too big task and it keeps going until it "succeeds", even if that burns a whole subscription (S035).
  - **Huge requests produce unreviewable results.** A multi-thousand-line PR is beyond what a human can understand, and a two-sentence request comes back as a whole, half-thought feature set (G04-N3).

- **What to teach (specific points):**
  1. **Keep tasks bounded.** Ask for the smallest change, in clear slices, and put "keep the change small, preserve unrelated work" in the prompt (S008). Break sessions into separate, clear tasks, and don't try to "draw the owl" in one mega session (G04-N5).
  2. **Scope drift is a named failure.** Pause, keep only the requested scope, and list the extra work as follow-ups (S008). Before the PR, check that the diff contains only the focused change (S009). Compare `git diff --stat` with what you asked for, and have the agent list and justify every file it touched (S031).
  3. **Size changes correctness, not just reviewability.** In a VB6-to-C# study, behavioural equivalence was 92% on simple features and 47% on complex ones: "unit size is the lever" (S036).
  4. **Trying is cheap; choosing is not.** Have agents build competing options, then choose on tests, profiling and parity, not on the agent's description (S036). Compare the strategies against the same success criteria (S008).
  5. **Parallel agents multiply your bottleneck.**
     - Your attention does not scale with the number of agents (G04-N4, S084).
     - In nomArmy, going from 1 to 4 local workers gave no net throughput gain.
     - Parallel patches with no textual conflict can still break each other (S030).

     Parallelize last, once you have a dependable judge, a recovery path and a review format people can absorb (S036). Beginners should not start with multi-agent setups (S008).
  6. **Delegation has overhead.** On small, already-diagnosed tickets, an orchestrating agent spent 4-8x the tokens of fixing the bug directly (S030).
  7. **For big jobs, test the prompt on a few items before fanning out to all of them** (G04-N1). Very large projects become stacked issues, one agent per issue (S003).
  8. **Long unattended runs need stop rules and size limits,** not just more time (S035, S032).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** implements each slice, can propose the slicing, builds competing options and lists what it touched (S008, S036, S031).
  - **The human:** sets the slice size by what they can review, rejects unrelated edits, decides what evidence will choose between options, and keeps units small (S008, S036, S082).
  - **When to bring in an expert:** slices you cannot review (authentication, billing, permissions) go to someone who can, with a human on every step (S036).

- **Currency:**
  - Established: small reviewable changes predate AI (G04-N3).
  - New in 2026: measured patch bloat (S031, July 2026), survey data (S082, July 2026), the failed 35-hour run (S035, September 2026) and the parallel-worker data (S030, October 2026).
  - Changing now: tools make fanning out a single command. Claude Code's `/batch` splits a change across 5 to 30 subagents (G04-N1), which makes this lesson more urgent.

- **Outdated framings to avoid:**
  - "Give the agent the whole app in one prompt" (S008, S082, G04-N5).
  - "If the task is solved, the size of the change doesn't matter" (S031).
  - "Longer autonomous runs get more done" (S035).
  - "Big-bang rewrites by agents are safe if the model is good" (S036).
  - "More agents in parallel means more output" (S030, S036, G04-N4).
  - "Agents make experience irrelevant" (S082, S081).

- **Questions it answers** (logged in the gap items):
  - Why did it change 40 files when I asked for one fix? How big should a task for an agent be? (S008)
  - Why does the agent do well on small things but mess up big projects? Why do experienced developers get more out of the same tool? (S082, S085)
  - Why did the agent change 12 files for a one-line fix? How do I keep it from rewriting things I didn't ask about? (S031)
  - Should I let the AI try several versions? (S036)

- **Show it for real:**
  - Show a diff where the agent also "improved" unrelated files. Reply with the scope-drift prompt and show the reduced diff plus a follow-up list (vendor-academies #05 demo).
  - Put `git diff --stat` for the agent's patch next to the minimal fix (verification #19 demo).
  - Request the same feature as one big prompt and as a three-step plan with a check after each step, and compare how much of each the user can review (surveys-and-learning #09 demo).
  - Have agents build two or three versions in separate branches, run the same tests and a quick performance check on each, and choose from the results table (practitioners-now #29 demo).

- **Priority:** must.
  - 4 items from 4 batches, 2 of them high severity.
  - Measured evidence (S031, S082, S030) plus practitioners (S035, S036, G04-N3, G04-N5).
  - A first big project that skips this produces work nobody can review (S008, S031).

---

### C042 When progress stalls, diagnose and change the input

- **In one line:** The agent reading and fixing its own errors is normal. When that becomes a loop, with the same error coming back or fixes undoing each other, stop it. Name the failure (missing context, scope drift, a failed check, a property of the model) and change the input. Saying "fix it" over and over goes with inexperience and breakdowns, not with progress.

- **Why it is a gap:**
  - **The beginner reflex is wrong.** It is to repeat the request louder, or start over with the same prompt. OpenAI and Anthropic both teach diagnosing the type of failure instead (S008, S006).
  - **Re-prompting goes with inexperience.** Less experienced vibe coders re-prompt instead of debugging, non-developers significantly more than professionals, and they report more breakdowns (S085). The companion study names the "Death Spiral": a loop that makes no progress despite the user's corrections (S085 companion).
  - **It also costs learning.** In Anthropic's randomized trial, "iterative AI debugging" (asking the AI to fix things without trying to understand them) was a low-learning pattern, and slower too (S083).
  - **Anthropic's docs list it as a common failure:** "correcting over and over" (G04-N1).
  - **This lesson replaces a rejected one.** The course dropped hand-debugging because the agent does it. What the human still needs is to notice when the agent's own loop has stopped working (S004).

- **What to teach (specific points):**
  1. **Name the failure, then change the input** (S008):
     - missing context (it is guessing about files or rules): have it read the named file and state the constraints before it edits;
     - scope drift: pause, keep only the requested scope, list the rest as follow-ups;
     - a failed check: reproduce the failure, fix the cause, rerun the named check, report the result;
     - quality still short: add files or examples, raise the reasoning effort, or compare a stronger model on the same checks.
  2. **Name the machine property behind odd output** (S006):
     - an invented fact: a knowledge or prediction limit, so bring sources;
     - an ignored instruction: steerability, so make the instruction short, concrete and checkable;
     - a forgotten detail: working memory, so shrink or restart the context.

     Then apply a targeted fix, not a generic retry.
  3. **The two-strikes rule.** After two failed corrections on the same issue, the context is cluttered with failed approaches. Run `/clear` and start fresh with a better prompt that includes what you learned (G04-N1). Restarting helps only if the prompt changes (S008). Long sessions degrade decisions: in one measured case, 41.9% of the user's messages after a compaction contained a correction, against a 17.7% baseline (the LangWatch study cited in S003).
  4. **Stop it early.** Esc stops the agent mid-action and keeps the context. Esc Esc or `/rewind` restores earlier conversation and code. Checkpoints don't capture changes made through Bash and are not a replacement for git (G04-N1).
  5. **Cap loops in advance.** Give exit criteria or a limit on fix-and-recheck rounds (S008). Plans need stop rules: in Aaron's overnight run, "never applied" was logged thirteen times in a row and nothing told anyone to stop (S032).
  6. **Other moves that work:**
     - split the task smaller (S082);
     - steer mid-flight (S084);
     - supply the missing context (S080);
     - ask conceptual questions to understand the failure (S083);
     - ask for the root cause to be fixed, not the error suppressed (G04-N1).
  7. **Fix it for next time.** Every repeated correction is a missing piece of the harness: an instruction line, a lint rule, a test or a hook (S036, G04-N5).
  8. **Escalate when the stall is beyond you.** Expertise is one of the reasons to bring a person in, because AI is jagged and lags experts on parts of tasks (S068). Don't ask questions whose answers you can't verify (S004).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** reads errors, fixes them and re-runs. That loop is verifiable, so it is the agent's job (S004, S003).
  - **The human:** notices the loop, stops it, names its type, and supplies what is missing or narrows the task (S008, S085).
  - **When to bring in an expert:** when the stall is in a domain you cannot judge, such as security or unfamiliar infrastructure. Bring in someone who knows it rather than re-prompting (S068, S004).

- **Currency:**
  - Established: the vendors' diagnostics (S006, S008).
  - New in 2026: the measured evidence (S085, May 2026; S083, January 2026).
  - Changing now: tools add mechanical stall handling. Claude Code's `/goal` evaluator eventually stops a stalled run (G04-N1). S030 notes that Claude Code ignores the ninth Stop-hook block in a row.

- **Outdated framings to avoid:**
  - Hand-debugging, line by line, as the core skill (S004, S001).
  - "Just keep telling it to fix it" (S085, G04-N1).
  - "Start a new chat and paste the same prompt" (S008). G04-N1 says restart, but with a better prompt.
  - "AI output is random; if it's wrong, just regenerate" (S006).

- **Questions it answers** (logged in the gap items):
  - The agent keeps going in circles; what do I do? Should I start a new chat? (S008)
  - The AI keeps going in circles on the same bug; what do I do? When should I stop the agent? (S085)
  - Why did it make up a citation? Why did it ignore my instruction? Why did it forget what I said earlier? (S006)

- **Show it for real:**
  - Show a terminal where the same error comes back across three agent attempts. Stop it with Esc, add the missing constraint or split the task, and rerun (surveys-and-learning #14 demo; G04-N1).
  - Show an agent stuck on a failing check. Reply "reproduce the failure, fix the cause, rerun the test, report" and show it break the loop (vendor-academies #14 demo).
  - Press Esc Esc to open the rewind menu and restore the code to before the loop started (G04-N1).

- **Priority:** must.
  - 3 medium-severity items from 2 batches, now backed by 14 sources, including the vendor doc that names this as a common failure (G04-N1).
  - It is the right replacement for the hand-debugging lesson Aaron rejected (S004).
  - "The agent keeps going in circles" comes up as a beginner question in two separate batches (S008, S085).

---

### C043 Deciding what is worth building stays human

- **In one line:** When building is cheap, the scarce skill is choosing the problem: who it is for, whether it should exist, and when to stop. The agent will build anything you point it at. Relaying tickets to agents adds nothing the agent can't do itself.

- **Why it is a gap:**
  - **AI mania.** Willison describes feeling that any time your agent isn't building something is wasted time. It led him to build a JavaScript interpreter and a WebAssembly runtime in Python before asking whether the world needed a slow, buggy, half-baked one (S033).
  - **"Deep Blue."** This is the ennui engineers feel because the AI can do anything (the term is credited to Adam Leventhal). Willison's job feels harder, because everything easy now goes to the agent (S033).
  - **Choosing goals is a known weak spot.** Anthropic's own assessment: Claude matches skilled researchers on well-specified experiments, but large gaps remain in choosing goals (S029).
  - **Output metrics reward the wrong thing.**
    - Microsoft's merged PRs rose about 24%, and nobody knows whether quality did (S082).
    - Merge counts can reward the people who skip judgment. Martinez admits he merged code with less scrutiny under that peer pressure (G04-N3).
  - **Approval-only roles are a trap.** Mollick: if humans keep only "the approvals, the exceptions, and the failures," we will have automated the wrong half of the job (S068).

- **What to teach (specific points):**
  1. **Before building, ask who it is for, whether it needs to exist, and what it will cost to keep.** Osmani asks this of old side projects an agent can now finish quickly: even five users means maintenance and a quality bar (G04-N4). Every accepted addition is something someone has to maintain for years (G04-N3).
  2. **Decide what not to build.** Agents can scaffold anything, but they cannot decide what matters, own the system, or know what to leave out (G04-N3). Part of Hashimoto's efficiency gain was knowing when not to reach for an agent, and he doesn't want to run agents just for the sake of running them (G04-N5).
  3. **Know the ownership list.** Someone still chooses the problem, the architecture and the quality bar, which verification signals deserve trust, and when the evidence is enough to ship (G04-N4). Anthropic's builder course ends on owning what ships: from whether it should exist at all, to ship, fix or stop after launch (S007).
  4. **Deciding is the first of the four agent-era skills:** deciding, specifying, steering, verifying (S084).
  5. **Keep the decisions worth making.** Mollick gives four reasons for an agent to bring in a person: approval (money, outside contact, sensitive access), expertise, variance (AI ideas converge) and interest, meaning people should keep the decisions worth making (S068).
  6. **Measure outcomes, not output.** Count incidents, rollbacks, time to recover and lead time, not lines, PRs or tokens (S029, S036, S082, G04-N3).
  7. **Looking like a game is not being a good game.** Agents given only screenshots of a 2022 game idea built games that were fun for about a minute. A good gameplay loop was beyond every agent Willison tried (S033).
  8. **Ball's prediction:** the craft of building software (solving business problems, knowing how other software did it and why, when and how to ship, getting feedback) matters more than ever. Engineers who just relay tickets to agents ("meat proxies") lose their value. Teach this as a prediction (S034).

- **You vs the agent (as of 2026-10-12):**
  - **The agent:** builds whatever it is pointed at, including things nobody needs (S033).
  - **The human:** picks the problem, the user and when to stop, and decides from feedback whether to ship, fix or stop (S007, S033, G04-N4).
  - **When to bring in others:** the agent cannot tell you whether the thing should exist, so get feedback from the people it is for (S007, S034). Keep the approval, expertise and interest decisions with people (S068).

- **Currency:**
  - New in 2026: S033 (September 2026), G04-N4 (August 2026), G04-N3 (October 2026).
  - Partly speculation: Ball's predictions (S034) and Mollick's proposed design for human escalation (S068).

- **Outdated framings to avoid:**
  - "More projects shipped equals more value" (S033).
  - "If the AI does the work, the job gets easier." Willison says it gets harder; quoting Greg LeMond, you just get faster (S033).
  - "My job is to pass tickets to the agent and report back" (S034, S068).
  - "Human in the loop means clicking approve" (S068).
  - Lines of code, merged PRs or tokens burned as a measure of productivity (S082, S029, G04-N3).

- **Questions it answers** (logged in the gap items):
  - I can build anything now, so why do I feel stuck? Should I keep my agents running all the time? What skills still matter if the AI writes the code? (S033, S034)
  - Will AI replace developers? What job is left for me if the agent does the tickets? (S034)

- **Show it for real:** There is little to show on screen, and neither item proposes a demo. Two options:
  - Play the kind of screenshot-built game Willison describes for one minute, to show that something can look like a game without being a good one (S033).
  - Take a list of side projects an agent could now finish and run each through "who is it for, and will I maintain it?" (G04-N4).

  Mostly this is narration around one worked decision.

- **Priority:** should.
  - Two medium-severity items from one batch, one of them speculation.
  - Now supported by eight sources across practitioners, vendors and Mollick (S007, S029, S033, S034, S068, S084, G04-N3, G04-N4).
  - It matters to an audience that can now build anything, but no direct safety or money harm attaches to it.
