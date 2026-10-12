# Sweep: courses and syllabi for building with AI, 2025-2026

Swept 2026-10-12 by the `sweep-courses` research agent for The Hidden Curriculum.
Every source below was fetched and read, not listed from a search snippet. For JS-rendered pages (the Stanford CS146S syllabus) the page's own JavaScript bundle and the lecture transcripts the course publishes were downloaded and read. GitHub repos were read through the GitHub API. Dates are publication or lecture dates as shown on the page. Where a page shows no date, the block says so and gives the closest date that can be checked (Coursera "recently updated" stamp, repo creation date, or first web-archive capture).

25 sources. 19 are dated 2026; 12 of those fall in the last 3 months (since 2026-07). 6 pages show no date. Four of those are clearly 2026-era: three Anthropic Academy pages showing © 2026, and Lovable's security page, whose features are dated July-September 2026 in its changelog. The other two (a Cursor Learn lesson and Replit Learn) carry no date at all. The syllabus of each source (its list of topics, and what it assumes you already know) is the evidence. The "gaps" field records what that course treats as necessary knowledge that a beginner is unlikely to have.

Limitation: the shared web-search budget ran out partway through this sweep. Maven, Udemy, edX, Bolt and YouTube course series could not be searched, and no source is listed for them. A follow-up sweep should cover them.

## Cross-cutting patterns (read these first)

1. **The 2026 syllabi stopped teaching "how to prompt an AI IDE". They now teach "how the harness works and how to verify what it did".** Stanford CS146S dropped "The AI IDE", "The Modern Terminal" and "Automated UI and App Building" from its Fall 2025 version. Fall 2026 opens instead with the internals of coding agents: the agent loop, the read/write/edit/bash tool set, and system prompts. Then come context engineering, skills, AGENTS.md, agent-ready codebases, agentic code review, a standalone Security week, background agents and "the software factory". Missing Semester 2026 has no standalone AI lecture: AI is "folded into each lecture", and a new "Agentic Coding" lecture was added.
2. **The mental model taught first is "everything is text in the context window".** CS146S (9/24 lecture), Missing Semester and the MIT 6.566 security lecture all teach the same picture. An LLM samples the next token. Chat resends the whole history every turn. An agent is a loop that runs tool calls. System prompts, tool descriptions, CLAUDE.md/AGENTS.md, MCP tool lists, plan-mode prompts and skill files are all text injected into that window. Context quality degrades long before the advertised limit. Anthropic's 2026 "AI Capabilities and Limitations" course frames the same idea as four machine properties: next-token prediction, knowledge, working memory and steerability.
3. **Debugging by hand is gone from the agent-era syllabi. The human's job is now defining "done" and supplying evidence.**
   - Missing Semester: agents "work best in a feedback loop where they can run the failing check themselves".
   - Cursor Learn: Debug Mode generates hypotheses, adds logging and analyzes logs on its own. The human supplies a reliable reproduction and runtime data, and confirms that the fix addresses the root cause rather than a symptom.
   - OpenAI's Codex Bootcamp: "A good prompt defines done". The human checks the diff, which checks ran, and the "Unknowns: what is still unverified".
   - CS146S: the human's highest-leverage places are "intent and architecture, and code review".
   - Exception: the newest GitHub Skills exercise (2026-09-29) still has the learner forming the debugging hypothesis. Its real lesson is that the human must define the invariant ("never loses or invents a cent"), which the AI did not think of.
4. **Every serious course now has a verification unit. They converge on the same rule: passing checks is not proof.**
   - Cursor: "Passing tests isn't proof of correctness"; agents show happy-path bias.
   - GitHub Skills: "Its explanation is not proof"; generated tests "often mirror the implementation".
   - Missing Semester: "AI-written tests may not be meaningful".
   - Claude Code in Action (2026): "check unsupervised output in proportion to how closely it was watched" and "gate turns on real test results".
5. **Security is a separate, expert-shaped gap. Beginner courses leave it out.**
   - CS146S gave Security its own week in 2026 (SAST/SCA, secret leaks, prompt injection) with the Semgrep CEO as guest.
   - MIT 6.566 taught indirect prompt injection against agents. It notes there are "many heuristic defenses that provide no guarantees".
   - Lovable's own docs say its scans "cannot guarantee complete security" and that apps handling sensitive data need a professional review.
   - The beginner on-ramps (DeepLearning.AI's Build with Andrew, Replit's AI Foundations) do not cover security, testing or deployment at all.
   - Missing Semester 2026 dropped its "Security and Cryptography" and "Security and Privacy" lectures.
   - This is the gap Aaron's rule targets: the course must teach the beginner what the agent cannot verify and when to bring in an expert.
6. **Sandboxing and permission modes are now part of the curriculum.** Missing Semester: run "yolo mode" only in a VM or container. DeepLearning.AI/E2B: run agent-written code in isolated sandboxes. Claude Code 101 and Claude Code in Action: permission modes and hooks. The MIT 6.566 lecture lists a real agent that deleted a production database and its backups.
7. **"Vibe coding" is now named as the thing to grow out of.**
   - CS146S: "Sometimes people call this the vibe coding class. That's not what I want it to be called."
   - DeepLearning.AI: vibe coding "often produces code that doesn't match what you asked for", hence spec-driven development.
   - Replit: vibe coding is "not a replacement for understanding technical tradeoffs in production apps".
   - The replacement taught everywhere is spec, then plan, then implement, then verify. Each course has its own name for it: RePPIT, constitution + feature spec, explore → plan → code → commit, prompt → inspect → act → validate → report.
8. **Courses now promise to keep changing.** The CS146S FAQ promises "weekly updates". Anthropic will "publish new courses each month". The Anthropic catalog grew to 23 entries, Coursera lists the Builders course as updated September 2026, and the DeepLearning.AI pages carry 2026 update stamps. This backs The Hidden Curriculum's premise that the topic list itself goes stale.
9. **Beginner courses still treat these as prerequisites** (assumed, not taught): the command line and a code editor (Claude Code 101), Git and pull requests (GitHub Skills, CS146S), basic Python (E2B, GitHub Skills), and a paid AI plan or API key (Claude Code 101). The non-programmer courses assume none of these, and those are exactly the courses that skip security and deployment.

---

## 1. CS146S: The Modern Software Developer (Fall 2026 syllabus, with Fall 2025 for comparison)
- **Author:** Mihail Eric (instructor), Stanford University; TAs Isaac Kan, Vijay Daita
- **Date:** 2026-09-22 (first lecture of Fall 2026); syllabus runs to 2026-12-03
- **URL:** https://themodernsoftware.dev/ (Fall 2025 version: https://themodernsoftware.dev/fall2025)
- **Kind:** syllabus
- **Credibility:** high. A Stanford course taught as it happens, with industry guests (Boris Cherny of Anthropic, Eno Reyes of Factory, Silas Alberti of Cognition, Isaac Evans of Semgrep, Amjad Masad of Replit) and open-source partners whose maintainers review student PRs.
- **Syllabus (Fall 2026):**
  - Week 1: Internals of coding agents (what an LLM is, the agent loop, the read/write/edit/bash tool set, how system prompts and tool definitions are structured; "build Claude Code in 200 lines")
  - Week 2: Advanced context engineering (RePPIT: Research, Propose, Plan, Implement, Test; spec-driven development; MCP servers, clients, tools and transport; designing tools for agent ergonomics; "The Context Tax: When to Compact")
  - Week 3: Agent skills and the CLI (SKILL.md plus scripts encode a workflow)
  - Week 4: Customizing your agent and repo (CLAUDE.md vs AGENTS.md; hooks for lint gates, test runs and guardrails; planner / implementer / reviewer subagents)
  - Week 5: Agent-ready codebases (structure, docs, tests and checks; scoring readiness; common gaps that block agents)
  - Week 6: Agentic code review (what AI review catches and what it misses)
  - Week 7: Security (SAST/SCA, dependency and secret-leak vulnerabilities, prompt injection and agent-specific attack surfaces)
  - Week 8: Background agents (async cloud agents, fleets of parallel agents, issue-to-PR pipelines)
  - Week 9: Building an AI-native team (MCP portals, LLM gateways, model routing, cost)
  - Week 10: The software factory (self-running, self-improving systems; running and securing agents after deployment)
  - Prerequisites: CS111/CS161-level programming; CS221/229 recommended. No prior AI tool experience required.
  - The 10/1 lecture transcript sets a grading rule: no "AI-slop PR"s. Review your own code before maintainers see it.
- **Gaps it names:**
  - What the harness is: system prompt, tool list, config files, plan mode, subagents, skills, hooks, compaction around one loop
  - Context engineering: when to compact or clear, and why advertised context is larger than usable context
  - Spec-driven development: turning product requirements into executable specs
  - AGENTS.md / CLAUDE.md, hooks as lint and test gates, subagent roles
  - Making a repo "agent-ready": docs, tests and checks the agent can run
  - What AI code review misses
  - Security of AI codebases: SAST/SCA, secret leaks, prompt injection, agent attack surfaces
  - Background and parallel agents, and issue-to-PR triggers
  - Cost and model routing
  - Securing agents after deployment
- **Outdated framings:**
  - Fall 2025 weeks the 2026 syllabus dropped or folded in: "The AI IDE", "The Modern Terminal", "Automated UI and App Building", "Modern Software Support", "Agents Post-Deployment"
  - "AI Testing and Security" as one week; 2026 splits it into "Agentic Code Review" and "Security"
  - The course as "the vibe coding class"
  - Tool names as the subject. The Stanford Bulletin description (https://bulletin.stanford.edu/courses/2274401, still listed for 2026-2027 Autumn) is built around tools ("Cursor and Warp", "Coderabbit and Qodo"). The 2026 course site is built around practices (MCP, skills, specs, loop engineering, the software factory). The bulletin's still-valid line: learn "not just how to use the latest AI-powered workflows, but also when and why to trust them".
- **Why it matters:** This is the clearest year-over-year evidence that the topics themselves went stale within 12 months. The FAQ promises "weekly updates to reflect the rapidly evolving landscape", which matches The Hidden Curriculum's own premise. Its week list is a strong checklist of topics for the course.

## 2. CS146S lecture, 2026-09-24: "The anatomy of a state-of-the-art coding agent" (transcript)
- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-24
- **URL:** https://themodernsoftware.dev/materials/9-24-26-transcript.txt
- **Kind:** course
- **Credibility:** high (primary lecture transcript; live demo intercepting Claude Code's requests with a proxy)
- **Syllabus (this lecture):**
  - Recap: a bare-bones coding agent fits in about 150-200 lines (built in the previous class)
  - Harness components: system prompt, AGENTS.md/CLAUDE.md, tool lists (about 40 built-in tools in Claude Code, plus MCP tools), plan mode, subagents, skills, hooks, compaction
  - Assignment 1: intercept Claude Code traffic and unpack the requests and responses
- **Gaps it names:**
  - The model is a remote, private "intelligence layer". The harness around it is what you can see and configure.
  - Every tool's name, description and signature becomes part of the prompt, so clear tool docstrings decide whether the model uses a tool correctly
  - Messages have roles: user, assistant, and system-level messages the harness injects behind the scenes
  - The system prompt is set by the harness and not controlled by you. CLAUDE.md is the user-controlled counterpart, and both are injected every request.
  - Plan mode and skills are literally blocks of text injected when invoked
  - You can inspect what is really sent by putting an intercepting proxy in front of the agent
- **Outdated framings:**
  - The agent as a "chatbot that writes code"
  - The idea that the model is the whole product; the lecture calls harness design "probably one of the hardest and most important problems"
- **Why it matters:** The best current source for a "what is actually sent to the model" lesson. It replaces the 2021 picture of a language model with the 2026 picture of model plus harness plus injected context.

## 3. CS146S lecture, 2026-09-29: "Advanced prompting and context engineering: RePPIT" (transcript)
- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-29
- **URL:** https://themodernsoftware.dev/materials/9-29-26-transcript.txt
- **Kind:** course
- **Credibility:** high (primary lecture transcript; worked live demo extending a vibe-coded app the instructor did not write)
- **Syllabus (this lecture):** the five steps of RePPIT, demonstrated on a Mint-clone feature. Each step is a skill.
  - Research: document only what exists, no suggestions
  - Propose: two orthogonal solutions with trade-offs
  - Plan: a design doc with in-scope and out-of-scope sections and security and rollout notes
  - Implement
  - Test: behavioral checks in a browser, then agentic code review
  - The lecture also covers when to compact or clear context, which model strength to use at each step, and a task-complexity ladder for how much process each task needs
- **Gaps it names:**
  - Advertised 1M-token windows are not 1M useful tokens. A cited study put the compaction point around 250k-450k tokens depending on model.
  - Clear the context after choosing a proposal, so the unchosen alternative doesn't confuse the agent
  - Stale docs are worse than none: re-research rather than ingest bad docs
  - The human still needs a mental model of the code "to discern good from bad"
  - Use a strong model for research, proposals and planning; implementation and testing can use lighter ones
  - Write an explicit out-of-scope list to stop the agent from going off the rails
  - Behavioral contracts (input to output) are checked by tests and browser runs. Performance, readability and security are code review's job, often split across several review agents.
  - Match process weight to task size: a copy change needs only a prompt; a migration needs repeated research and planning in separate sessions, split into stacked issues
- **Outdated framings:**
  - Vibe coding ("Jesus, take the wheel") as enough for hard problems in real codebases
  - The human hand-testing the result. The agent now opens a browser, makes synthetic data and tests the feature; "This wasn't true six months ago."
  - Validating the research step heavily; agents are now good at compressing code into a summary
- **Why it matters:** States the human/agent split in plain words: today the human's highest-leverage places are "intent and architecture, and code review". This is the "what YOU must do vs what the agent does" frame the course is built around.

## 4. Missing Semester of Your CS Education, 2026 edition: "Agentic Coding" lecture (and course overview)
- **Author:** MIT (Missing Semester instructors; IAP 2026, supported by SIPB and MIT Open Learning)
- **Date:** 2026-01-21 (lecture date in the 2026 schedule; course ran 2026-01-12 to 2026-01-23)
- **URL:** https://missing.csail.mit.edu/2026/agentic-coding/ (overview: https://missing.csail.mit.edu/)
- **Kind:** course
- **Credibility:** high (the canonical "tools nobody teaches you" course, now revised for AI; the 2026 edition has YouTube recordings and an HN discussion)
- **Syllabus:**
  - 2026 lectures: Shell; Command-line Environment; Development Environment and Tools; Debugging and Profiling; Version Control and Git; Packaging and Shipping Code; Agentic Coding; Beyond the Code; Code Quality
  - The overview says there is "not a standalone AI lecture", because AI tools are folded into each lecture
  - The Agentic Coding lecture: how agents work (LLM as a probability distribution, chat as repeated inference, agent as a tool-call loop); use cases (features, fixing errors, refactoring, review, code understanding, agent as shell, vibe coding); advanced features (reusable prompts and skills, parallel agents with git worktrees, MCP, context management with clear, rewind, compaction, llms.txt, AGENTS.md, skills and subagents); pitfalls; security and privacy
  - Exercises: build one feature four ways (by hand, with autocomplete, with inline chat, with an agent); build an AGENTS.md, a skill and a subagent; run yolo mode inside a VM or container
- **Gaps it names:**
  - The agent loop and the context window as the limiting resource
  - Context degrades as it grows, before overflow
  - AGENTS.md / CLAUDE.md as a README for agents, loaded at session start; skills load on demand; subagents keep research out of the main context
  - Git worktrees for parallel agents
  - Agents work best when they can run the failing check themselves
  - Writing a spec detailed enough to aim the agent without doing the work yourself; TDD with human-audited tests
  - Checking code can be harder than writing it, so critical code may warrant writing by hand
  - Debugging spirals and confident wrongness
  - Standard setups may send the whole repo and all interactions to the provider
  - Review AI code for security bugs
  - Never run yolo mode outside an isolated environment
- **Outdated framings:**
  - AI as a separate topic bolted onto a tools course
  - The 2020/2019 topic list. The page lists "Security and Cryptography" and "Security and Privacy" among topics "we did not cover in 2026", so security left the basics course just as AI arrived.
- **Why it matters:** The most-copied "hidden curriculum" course has itself been rebuilt around agents. Its pitfall list and human/agent split are concrete and well sourced. Its dropping of security is a warning that beginners can now finish the standard tools course without any security unit.

## 5. Missing Semester 2026: "Code Quality" lecture
- **Author:** MIT Missing Semester
- **Date:** 2026-01-23 (lecture date; the examples use January 2026 dates)
- **URL:** https://missing.csail.mit.edu/2026/code-quality/
- **Kind:** course
- **Credibility:** high
- **Syllabus:** formatting; linting (incl. Semgrep custom rules); testing (unit, integration, functional, TDD, regression, property-based, mocking, coverage); pre-commit hooks; CI as a check-only gate; continuous deployment; command runners; regular expressions
- **Gaps it names:**
  - Linters, type checkers, tests and CI as the feedback signals an agent iterates against ("Make sure the AI agent can run the linter and observe the results")
  - Coverage reports show the agent which lines lack tests
  - AI-written tests may not be meaningful, so the human judges their quality
  - CI catches violations regardless of who wrote the code
  - Deliberately break code to confirm CI catches it
- **Outdated framings:** code-quality tooling as style policing for humans. Here it is the verification layer that lets you delegate to agents.
- **Why it matters:** This is the "make it verifiable" half of Aaron's rule. Checks the agent can run turn unverifiable work into verifiable work.

## 6. Missing Semester 2026: "Beyond the Code" lecture
- **Author:** MIT Missing Semester
- **Date:** 2026-01-22 (lecture date)
- **URL:** https://missing.csail.mit.edu/2026/beyond-code/
- **Kind:** course
- **Credibility:** high
- **Syllabus:** writing for others (comments that carry the "why", READMEs, commit messages as Problem → Solution → Implications); collaboration (bug reports, minimal reproducible examples, focused PRs, reviewing code); asking good questions; AI etiquette; licensing and open-source etiquette
- **Gaps it names:**
  - Disclose meaningful AI contributions, and which parts
  - Check team or project norms first, since some teams restrict AI for compliance or data-residency reasons
  - Don't submit AI code you can't explain; maintainers inherit long-term responsibility for it
  - An LLM writing a commit message sees only the "what" in the diff, so give it the "why"
  - AI review is a first pass, not a substitute for human review
  - Check the license your contribution falls under (copyleft caution)
  - Report security vulnerabilities privately
  - Using AI to finish learning tasks defeats their purpose
- **Outdated framings:** "if it passes, submit it". AI output you can't explain is a burden you pass to someone else.
- **Why it matters:** These are the social and ownership gaps that come with AI-written work: disclosure, licensing and explainability. No beginner platform course covers them.

## 7. AI Agent Security (guest lecture in MIT 6.566, with code demos)
- **Author:** Anish Athalye (MIT CSAIL)
- **Date:** 2026-04 (README says April 2026; repo created 2026-04-29)
- **URL:** https://github.com/anishathalye/ai-agent-security-lecture (video: https://www.youtube.com/watch?v=w0oGeKxD5Fc)
- **Kind:** course
- **Credibility:** high (MIT security course lecture with runnable demos; reading is the CaMeL paper, "Defeating Prompt Injections by Design")
- **Syllabus:**
  - Demos build up the stack in numbered scripts: base-model completion → chat via role-play and control tokens → tools → a tool-call loop (the "agent harness") → native tools → ReAct agents → CodeAct
  - Security goals: integrity/alignment, confidentiality, safety
  - Attacks: direct and indirect prompt injection, jailbreaking, data poisoning, training-data extraction
  - Partial defenses: training, system prompts, guardrails, tool-confirmation UI, sandboxes
  - Principled defenses: the dual-LLM pattern, and CaMeL capabilities that track where data came from and who may read it
- **Gaps it names:**
  - An agent often runs with high privilege between the user and an environment that may hold attacker-controlled data
  - Agents are "not robust (even under natural inputs)". The example given is an agent that deleted a production database and its backups.
  - Indirect prompt injection through web pages, docs, meeting notes and email
  - The gap between stated goal and intended behavior ("organize my inbox" → deletes unread mail)
  - Defenses that only protect control flow still leak data
  - With "a nondeterministic model at the heart of the system", guarantees are hard; "AI and agents are evolving faster than security can keep up"
- **Outdated framings:**
  - "A good system prompt / guardrail makes the agent safe". The lecture calls these "many heuristic defenses that provide no guarantees".
- **Why it matters:** The most rigorous course-level treatment of why agent security can't be verified by the agent itself. It gives the course a precise vocabulary (direct vs indirect injection, privileged vs quarantined LLM) for the "bring in an expert" lesson.

## 8. Building with AI: A Hands-On Course for Scientists and Engineers (MIT Schwarzman College of Computing)
- **Author:** Wojciech Matusik (MIT) and Hanspeter Pfister (Harvard)
- **Date:** 2026-08-31 to 2026-09-04
- **URL:** https://web.mit.edu/webcast/computing/s26/0926/1.html
- **Kind:** course
- **Credibility:** medium-high (MIT and Harvard faculty; the webcast page gives only the module list)
- **Syllabus:** five modules: Introduction to AI Agents (tools, retrieval, multi-step tasks, scheduled jobs, reusable skills); AI Coding for Non-CS; Data Scraping and Cleanup; Data Visualization; Foundation Models and Fine-Tuning. No prior coding assumed.
- **Gaps it names:**
  - For non-CS professionals: agents that use tools and complete multi-step tasks
  - Automating repetitive work with scheduled jobs and reusable skills
  - Building with AI copilots without a CS background
  - Getting and cleaning data before analysis
- **Outdated framings:** none stated explicitly. The structure itself treats "AI coding for non-CS" as a standard module for scientists, not a novelty.
- **Why it matters:** A very recent example of top universities teaching non-programmers to build with agents. The page names "reliable software" as a goal but lists no verification or security module, which is the gap The Hidden Curriculum can fill.

## 9. Claude Code in Action (Anthropic Academy, 2026 edition)
- **Author:** Anthropic Academy
- **Date:** undated (page © 2026; the outline is a rebuilt edition covering routines, headless mode, verification skills, plugins and managed code review)
- **URL:** https://anthropic.skilljar.com/claude-code-in-action
- **Kind:** course
- **Credibility:** high (first-party course from the tool's maker)
- **Syllabus:**
  - Steer the work: plan mode, controlling compaction, the rewind menu, hands-on vs autonomous runs
  - Configure Claude: a concise CLAUDE.md, verification skills, permission modes, hooks that enforce required rules
  - Automate repeat work: routines and headless mode; GitHub Actions and managed code review
  - Verify and share: "Trust It: Verifying Unsupervised Runs"; plugins
  - Audience: developers who already use Claude Code for single prompts
- **Gaps it names:**
  - Scope a task in plan mode before running it
  - Make compaction keep the key details
  - Choose a permission mode per job
  - Enforce rules with hooks rather than instructions
  - "Check unsupervised output in proportion to how closely it was watched"
  - "Gate turns on real test results"
  - Package a trusted setup as a team plugin
- **Outdated framings:**
  - Agent use as one prompt at a time. The course is about long, hands-off, team-wide runs and how to trust them.
- **Why it matters:** The vendor's own 2026 course puts verification of unsupervised runs at the center. That matches the course rule: the AI handles what is verifiable, and the human sets up and checks the verification.

## 10. Claude Code 101 (Anthropic Academy; on Coursera from 2026-10-05)
- **Author:** Anthropic Academy
- **Date:** 2026 (Skilljar page © 2026; launched on Coursera 2026-10-05 per the Coursera blog)
- **URL:** https://anthropic.skilljar.com/claude-code-101
- **Kind:** course
- **Credibility:** high (first-party)
- **Syllabus:** what Claude Code is; how it works (agentic loop, context window, tools, permissions); install (terminal, VS Code, JetBrains, Desktop, web); first prompt (approval mode, auto-accept, Plan Mode); explore → plan → code → commit; context management (/compact, /clear, /context); code review; CLAUDE.md; subagents; skills; MCP; hooks (formatting, command blocking, notifications)
  - Prerequisites: basic familiarity with a code editor and the command line; a Pro, Max or Enterprise account or an API key
- **Gaps it names:**
  - How an agent differs from chat AI
  - How the agentic loop, context window, tools and permissions fit together
  - Permission and approval modes
  - The explore → plan → code → commit workflow
  - Managing context explicitly
  - Persistent project memory in CLAUDE.md
  - Delegating to subagents
  - Connecting tools via MCP
  - Hooks that block dangerous commands
- **Outdated framings:**
  - Agent coding as an add-on for experienced engineers. The audience now explicitly includes "new developers who want AI-assisted workflows from the start".
- **Why it matters:** Shows what the maker treats as day-one knowledge. It also shows what it assumes and does not teach: the command line, an editor, and a paid account. Those prerequisites are exactly the hidden-curriculum gaps for non-programmers.

## 11. AI Fluency for Builders (Anthropic Academy with CodePath)
- **Author:** Anthropic Academy and CodePath
- **Date:** 2026-09 (Coursera "Recently updated: September 2026"; announced on Coursera 2026-10-05)
- **URL:** https://www.coursera.org/learn/ai-fluency-for-builders (also https://anthropic.skilljar.com/ai-fluency-for-builders)
- **Kind:** course
- **Credibility:** high (first-party, built with a CS-education nonprofit; beginner level, about 5 hours)
- **Syllabus:**
  - Introduction and the 4D Framework (Delegation, Description, Discernment, Diligence)
  - How AI works: capabilities and limitations
  - The 4Ds for builders: Delegation and the builder's toolkit; Description and building great things
  - Discernment for builders: "Discernment for code"; "Discernment for user experience"
  - Tying it together: "Stand behind what you build"
  - Skill tags: Context Engineering, Software Technical Review, Acceptance Testing, Code Review, Responsible AI
  - Prerequisite (recommended): AI Fluency: Framework & Foundations
- **Gaps it names:**
  - Deciding what to delegate across the path from customer problem to shipped product
  - Describing intent well enough to build from
  - Discernment applied separately to code and to user experience
  - Owning and standing behind AI-built work: acceptance testing and code review as builder skills
- **Outdated framings:**
  - "Builder" meaning engineer only. The audience is "product people, engineers, and makers", owning "the full path from problem to shipped solution".
- **Why it matters:** The closest first-party match to The Hidden Curriculum's audience (non-engineer builders). Its explicit "Stand behind what you build" module supports the course's accountability theme. The lesson bodies are behind registration; only the structure was read.

## 12. AI Capabilities and Limitations (Anthropic Academy)
- **Author:** Anthropic Academy
- **Date:** 2026 (page © 2026; launched on Coursera 2026-10-05, beginner, 4 hours)
- **URL:** https://anthropic.skilljar.com/ai-capabilities-and-limitations
- **Kind:** course
- **Credibility:** high (first-party; companion to the 4D Framework course)
- **Syllabus:** What We Mean by AI; How AI Gets Its Character; Next Token Prediction; Knowledge; Working Memory; Steerability (each with a "Try it out"); When Properties Collide
- **Gaps it names:**
  - A working mental model of "how modern generative AI systems behave and why"
  - Diagnosing an unexpected output by type, then applying a targeted fix
  - Placing a task on a capability-to-limitation continuum
  - The four machine properties the human competencies respond to: next-token prediction, knowledge, working memory, steerability
- **Outdated framings:**
  - Teaching AI fluency as human habits only. Anthropic now pairs it with a separate course on the machine's properties.
- **Why it matters:** A current, first-party "how it works" syllabus to check against, so the course's model lesson doesn't fall back to the 2021 picture.

## 13. AI Fluency: Framework & Foundations (Anthropic Academy)
- **Author:** Anthropic, with Prof. Joseph Feller (University College Cork) and Prof. Rick Dakan (Ringling College)
- **Date:** undated (page © 2026; the Coursera blog of 2026-10-05 names it as the recommended first course)
- **URL:** https://anthropic.skilljar.com/ai-fluency-framework-foundations
- **Kind:** framework
- **Credibility:** high (foundational and still current: every 2026 role-specific AI Fluency course builds on it)
- **Syllabus:** Introduction and the 4D Framework; Deep Dive 1: What is Generative AI? (fundamentals, capabilities and limitations); Delegation (incl. project planning); Description; Deep Dive 2: Effective prompting techniques; Discernment (incl. the Description-Discernment loop); Diligence; certificate
- **Gaps it names:**
  - Delegation: what to hand to AI
  - Description: how to communicate intent
  - Discernment: evaluating output
  - The Description-Discernment loop: iterate between saying what you want and judging what came back
  - Diligence: responsible, ethical, safe use
- **Outdated framings:**
  - Prompting as the whole skill. Prompting is one "deep dive" inside a four-part competency model.
- **Why it matters:** The framework the angle asked about. The 4Ds map neatly onto "what the agent does vs what you must check" (Discernment and Diligence are the human's job).

## 14. "10 free Anthropic AI courses launch today on Coursera, with more coming each month" (Coursera Blog)
- **Author:** Coursera Blog
- **Date:** 2026-10-05
- **URL:** https://blog.coursera.org/10-free-anthropic-ai-courses-launch-today-on-coursera-with-more-coming-each-month-to-help-learners-stay-current/
- **Kind:** list
- **Credibility:** medium-high (platform announcement; lists course scopes and audiences)
- **Syllabus (the catalog):**
  - For everyone: AI Capabilities and Limitations
  - For developers: Claude Code 101, Claude Platform 101, Introduction to Subagents, Introduction to Agent Skills
  - For business, product and creatives: AI Fluency for Small Businesses, AI Fluency for Builders, AI Fluency for Creative Work
  - For teachers: pK-12 Educators, and pK-12 Train the Trainer
- **Gaps it names:**
  - Subagents: what to hand off and how to design them
  - Skills that replace repetitive prompts and get shared with a team
  - Preserving a creator's voice when using AI in creative work
  - Protecting student data
- **Outdated framings:**
  - Courses as fixed artifacts. Anthropic "will continue to publish new courses each month to help learners keep pace", because "there's always something new to learn".
- **Why it matters:** Recent (one week old) evidence that the biggest vendor treats its curriculum as monthly-updated, which supports The Hidden Curriculum's update model. It also shows how the field now splits curricula by role.

## 15. Introduction to Claude Cowork (Anthropic Academy)
- **Author:** Anthropic Academy
- **Date:** undated (page © 2026; banner says Cowork is rolling out to Pro and Max plans)
- **URL:** https://anthropic.skilljar.com/introduction-to-claude-cowork
- **Kind:** course
- **Credibility:** high (first-party), but the lesson bodies are behind registration; only the outline was read
- **Syllabus:** Meet Claude Cowork (set up, first task, make it yours); standing context (global instructions, projects), skills, plugins; Claude in Chrome and Claude for Microsoft 365; Sharing and safety ("Best practices for working safely", "Validating skills for plugins", sharing with your team)
- **Gaps it names:**
  - An agent that reads and edits your real files, folders and apps (not chat)
  - Standing context vs one-off prompts
  - Validating a skill or plugin before trusting or sharing it
  - Safe habits for multi-step work that will be shared with a team
- **Outdated framings:**
  - Agents as developer-only tools. This course targets knowledge workers working on their own files.
- **Why it matters:** Shows agentic work reaching non-programmers on their own computers. "Validating skills for plugins" points to a supply-chain trust gap (installing someone else's instructions) that non-programmers have no model for.

## 16. Spec-Driven Development with Coding Agents (DeepLearning.AI with JetBrains)
- **Author:** Paul Everitt (JetBrains), DeepLearning.AI
- **Date:** 2026-04-18 (page "Updated Apr 18, 2026")
- **URL:** https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents
- **Kind:** course
- **Credibility:** high (Andrew Ng's platform; IDE-vendor instructor)
- **Syllabus:** Why spec-driven development; workflow overview; creating the constitution (mission, tech stack, roadmap); feature specification; implementation; feature validation; project replanning; second feature; the MVP; legacy support (specs from existing docs); build your own workflow as an agent skill; agent replaceability
  - Prerequisites: basic familiarity with a programming language and experience with LLM coding tools
- **Gaps it names:**
  - Writing a project constitution and per-feature markdown specs
  - A plan-implement-validate loop with an explicit validation step
  - Replanning between features
  - Generating specs for legacy code
  - Packaging the workflow as a skill that works across agents and IDEs ("agent replaceability")
- **Outdated framings:**
  - Vibe coding as a way to ship: it "often produces code that doesn't match what you asked for"
- **Why it matters:** A 2026 beginner-level course that names the move from vibe coding to specs. "Agent replaceability" teaches that the spec, not the tool, is the durable asset.

## 17. Build with Andrew (DeepLearning.AI)
- **Author:** Andrew Ng, DeepLearning.AI
- **Date:** 2026-07-17 (page "Updated Jul 17, 2026")
- **URL:** https://www.deeplearning.ai/courses/build-with-andrew
- **Kind:** course
- **Credibility:** high as evidence of the beginner on-ramp, but intentionally minimal
- **Syllabus:** Creating an app with AI; Telling AI what you want; Download and open your app; Customize your app; Now you can build more apps; You're a builder now!; final project. Builds a browser birthday-message generator and a ping-pong game. "Assumes no prior knowledge of AI or coding."
- **Gaps it names:**
  - Describing an idea in words so AI can build it
  - Downloading and opening the file it made
  - Iterating by describing changes
  - (By omission) The page does not cover testing, deployment, security or the limits of vibe coding beyond troubleshooting
- **Outdated framings:**
  - "App building is too hard" for non-coders. The course's pitch is that it isn't.
- **Why it matters:** This marks where mainstream non-programmer courses stop, at a single-file app on your own machine. Everything past that point (hosting, data, accounts, keys, security) is The Hidden Curriculum's territory.

## 18. AI Prompting for Everyone (DeepLearning.AI)
- **Author:** Andrew Ng, DeepLearning.AI
- **Date:** 2026-07-24 (page "Updated Jul 24, 2026")
- **URL:** https://www.deeplearning.ai/courses/ai-prompting-for-everyone
- **Kind:** course
- **Credibility:** high
- **Syllabus:**
  - Module 1, Finding information: the AI novice vs the AI power user; pretrained knowledge vs web search; web search sources; deep research
  - Module 2, AI as thought partner: brainstorming; context; AI desktop apps; reasoning; sycophancy; writing; AI critique
  - Module 3, Multimedia and code: images; image generation; building apps; data analysis; final project
  - No technical background required
- **Gaps it names:**
  - Pretrained knowledge vs live web search, and checking sources
  - When to use deep research
  - Giving context
  - Sycophancy: AI agreeing with you, and how to ask for honest critique
  - Using AI critique on your own work
- **Outdated framings:**
  - Prompting as clever wording. The course is organized around information sources, context and critique.
- **Why it matters:** Its "Sycophancy" lesson backs the course's warning that people believe the agent when it says the app is fine. The model is trained to tell you what you want to hear.

## 19. Building Coding Agents with Tool Execution (DeepLearning.AI with E2B)
- **Author:** Tereza Tizkova and Francesco Zuppichini (E2B), DeepLearning.AI
- **Date:** 2026-04-22 (page "Updated Apr 22, 2026")
- **URL:** https://www.deeplearning.ai/short-courses/building-coding-agents-with-tool-execution
- **Kind:** course
- **Credibility:** medium-high (taught by a sandbox vendor, so it has an interest in the conclusion, but the syllabus is concrete)
- **Syllabus:** Inside a coding agent; your first coding agent; tool execution environments (local vs containers vs sandboxed microVMs); running code in the cloud; data-analyst agent; full-stack agent; hands-on project
  - Prerequisites: basic Python and LLM familiarity
- **Gaps it names:**
  - Coding agents write and run their own code, so their behavior isn't fully predictable
  - Isolation and resource controls protect your systems
  - Trade-offs between local, container and cloud execution
  - Summarizing context at runtime for long multi-file work
- **Outdated framings:**
  - Running agent-generated code directly on your own machine as the default
- **Why it matters:** Gives a course-level "where does the code run, and what can it touch" lesson to place next to Missing Semester's yolo-mode-in-a-VM advice.

## 20. Codex Bootcamp 101: Agentic coding (OpenAI Academy livestream and slide deck)
- **Author:** OpenAI Academy (presenters Marcus Stallworth, Tanner Wride, Aruna Chakkirala)
- **Date:** 2026-09-23 (livestream; the deck's model-guidance slide is dated 22 September 2026)
- **URL:** https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c (deck linked from that page: https://d2xo500swnpgl1.cloudfront.net/slide-upload/oaiacademy/Codex-Bootcamp-101-Sept-29911778-d7ed-4e74-b028-f5ff6f6782c7-1790179444559.pdf)
- **Kind:** course
- **Credibility:** high (first-party, three weeks old; part of a 101/201/301 series running 2026-09-23 to 2026-10-07)
- **Syllabus:**
  - Agenda: understand the workflow; prepare your workspace (repo context, AGENTS.md at personal, project and folder levels, checks); choose capabilities (models, reasoning effort, skills, plugins, scheduled tasks); make a verified change (ticket → reviewable PR); build repeatable habits (subagents, a "usage coach" skill)
  - Four habits: delegate a bounded task; prepare the repository; review the evidence; reuse what works
- **Gaps it names:**
  - "A good prompt defines done": goal, context, constraints, and "Done when" (e.g. add a regression test, run checks, report evidence)
  - Ask the agent to map the repo and "Separate verified information from assumptions" before any edit
  - The agent loop as prompt → inspect → act → validate → report, with a human review gate
  - Before accepting a change, check: does the diff match the scope; which checks ran, passed, failed or were skipped; "Unknowns: what is still unverified"
  - Model choice is separate from reasoning effort; keep the lightest setting that meets your quality bar
  - When progress stalls, change the input: name the failure (missing context, scope drift, failed checks)
  - Plugins act on tickets "with explicit authorization"; ask before installing or changing shared instructions
- **Outdated framings:**
  - The three-phase history the deck itself draws: code completion → pair programming → "agentic delegation: delegate entire task"
  - Prompting as asking for a fix ("Fix the homepage") rather than defining a bounded, verifiable task
- **Why it matters:** The newest vendor syllabus in this sweep. Its review checklist (scope, checks, unknowns) is almost exactly the course rule: the agent produces evidence; the human checks what the evidence doesn't cover.

## 21. Test and Debug with GitHub Copilot (GitHub Skills exercise)
- **Author:** GitHub (GitHub Skills)
- **Date:** 2026-09-29 (repo created; last pushed 2026-09-30)
- **URL:** https://github.com/skills/test-and-debug-with-github-copilot
- **Kind:** course
- **Credibility:** high (first-party, graded exercise)
- **Syllabus:**
  - Five steps: explain unfamiliar code and record a falsifiable hypothesis; generate focused tests from an explicit behavior contract; add the edge cases Copilot missed; use a failing test to diagnose, fix and refactor; review the diff and write "Verification" and "Copilot review" sections in the PR
  - The exercise builds a bill-splitting library "that never loses or invents a cent"
  - Prerequisites: Getting Started with GitHub Copilot; basic Python, Git and terminal
- **Gaps it names:**
  - Copilot's explanation "is not proof". Keep suggestions only when they connect to code, test output or an invariant.
  - Tests generated from vague prompts "often mirror the implementation instead of checking useful behavior"
  - Don't compute the expected value with the same formula as the code under test
  - Generated tests overrepresent common inputs; test invariants and boundaries (rounding, money)
  - Avoid binary floating point for money
  - Never weaken a test to match buggy output
  - Treat AI review as "another hypothesis"
  - Document what you verified independently
- **Outdated framings:**
  - "Passing tests prove it works": "passing tests alone do not prove that every Copilot suggestion was appropriate"
  - Tension to note: this exercise still has the human form the debugging hypothesis by hand. What lasts is that only the human can state the domain invariant the tests must enforce.
- **Why it matters:** A two-week-old, concrete lesson in "what the human must supply": the invariant. It also has a ready-made worked example (losing a cent when splitting a bill).

## 22. Cursor Learn: "Reviewing and testing code"
- **Author:** Cursor (Anysphere)
- **Date:** 2026-02 (first archived 2026-02-15; revised versions captured through 2026-09-29). The page shows no date.
- **URL:** https://cursor.com/learn/reviewing-testing
- **Kind:** course
- **Credibility:** medium-high (first-party; partly promotes Cursor features such as Bugbot)
- **Syllabus:**
  - Cursor Learn lessons, as linked from the /learn index (order not shown): How AI models work; Hallucinations and limitations; Tokens and pricing; Context; Tool calling; Agents; Working with agents; Understanding your codebase; Creating features; Finding and fixing bugs; Reviewing and testing; Customizing agents; Putting it together
  - This lesson: agent code gets the same merge bar as human code; self-review before peer review; small logical commits; tests, type checks, linting and browser testing as checks the agent can run; AI review and Bugbot; parallel edge-case testing with cloud agents; speed up slow test suites
- **Gaps it names:**
  - Code can compile and pass tests while "missing edge cases, hiding security issues, or duplicating existing logic"
  - "Passing tests isn't proof of correctness" (tests may check the wrong behavior)
  - Happy-path bias
  - Agents reimplement code that already exists
  - Split changes too large to review
  - The more automated checks you have, the more you can delegate
  - Slow CI multiplies across agent sessions
- **Outdated framings:**
  - Review as something done after the fact by a colleague. Now you watch the diff form, steer early, and have the agent review its own branch first.
- **Why it matters:** States plainly that verification capacity is what limits how much you can delegate, which is the course's rule restated as engineering practice.

## 23. Cursor Learn: "Finding and fixing bugs"
- **Author:** Cursor (Anysphere)
- **Date:** undated (part of Cursor Learn, which was first archived 2025-09; the lesson describes Debug Mode and MCP access to Sentry and Datadog)
- **URL:** https://cursor.com/learn/finding-fixing-bugs
- **Kind:** course
- **Credibility:** medium-high (first-party)
- **Syllabus:**
  - Simple bugs: paste the error and the agent patches it
  - Harder bugs: Debug Mode (hypotheses → targeted logging → you reproduce → log analysis → targeted fix)
  - The agent reads the browser console and network requests; pulls data from Sentry or Datadog via MCP; the same prompt can be run across several models
- **Gaps it names:**
  - The human's debugging job is now a reliable reproduction, a clear brief and runtime data
  - Review the agent's reasoning, not just the fix
  - Confirm the root cause: a null check that makes the error disappear can hide a data problem
  - Agents produce plausible but wrong explanations
  - Add a regression test so the bug stays fixed
- **Outdated framings:**
  - The human reading stack traces and stepping through code. The agent gathers evidence and proposes the fix; "Treat the tool's recommended solution as a suggestion to evaluate, not a verdict."
- **Why it matters:** Directly answers Aaron's correction about the hand-debugging lesson. It lays out what changed and what the human still owns (reproduction, root-cause judgment, the regression test).

## 24. Lovable Docs: Security
- **Author:** Lovable
- **Date:** undated page. The features it describes (scan on every publish, 10 free fixes, Trust Center, dependency-scan filtering, Security view redesign) are dated 2026-07-25 to 2026-09-23 in Lovable's changelog (https://docs.lovable.dev/changelog, latest entry 2026-10-07).
- **URL:** https://docs.lovable.dev/features/security
- **Kind:** docs
- **Credibility:** high (the platform describing the limits of its own scanner)
- **Syllabus:**
  - What the platform checks: a Quick scan on every publish (missing or permissive RLS, leaked-password protection, critical npm vulnerabilities, unauthenticated MCP server); an on-demand Deep scan (access control, abusable endpoints, injection, leaked secrets, payment logic, auth, exposed personal data); Secrets steering; optional auto-fix; admins can block publishing
  - What you must do yourself: listed under gaps
- **Gaps it names:**
  - Row Level Security per table, and testing it after auth or schema changes
  - Secrets belong server-side, never in client code
  - Enable leaked-password protection
  - Check auth flows and API routes; an in-chat security review "is not a certification"
  - Rerun scans after significant changes
  - Some vulnerabilities are deliberately not raised as findings
  - The tools "cannot guarantee complete security"; apps with sensitive data or critical functions need a professional review
- **Outdated framings:**
  - "The platform scanned it, so it's safe". The vendor itself rules this out.
- **Why it matters:** The vibe-coding platform's own docs state the course rule for security. The scan is a check the AI can run; what it can't verify needs a human expert.

## 25. Replit Learn: AI Foundations
- **Author:** Replit
- **Date:** undated (no date on the page)
- **URL:** https://learn.replit.com/docs/ai-foundations/lesson-1 (course hub: https://learn.replit.com/)
- **Kind:** course
- **Credibility:** medium (vendor on-ramp; short lessons)
- **Syllabus:** What's an app?; Introduction to AI (how LLMs work, tokens, why responses vary); What is vibe coding?; Your first app; What makes an idea buildable?; Scope your next project; Build your idea. "Intro to Replit" and "Advanced vibes" are listed as coming soon.
- **Gaps it names:**
  - "Accessible doesn't mean effortless"
  - A three-question buildability test: one sentence, one problem, a basic version in hours
  - Three audience levels with rising work: just for me (no deployment); my team (must be deployed, reliable); the world (user accounts, security, data management, scale)
  - Cut scope ruthlessly
  - Design changes get expensive late
  - Describe → critique → iterate, with acceptance criteria in the prompt
- **Outdated framings:**
  - "Press one button and it's done"
  - Vibe coding as a replacement for "understanding technical tradeoffs in production apps"
- **Why it matters:** Its "just for me / team / world" ladder is a useful frame for the course: each step up adds hidden-curriculum requirements (hosting, then accounts, security and data). The platform names them but does not teach them.
