# Sweep: practitioner essays and talks (what the human's job is now)

Swept: 2026-10-12, for "The Hidden Curriculum". Angle: practitioner essays and talks, 2026 first, on how work with coding agents has changed and what humans still need to know.

Method: every source below was fetched and read on 2026-10-12 (none are listed from search snippets). Dates come from the page itself. Where a page shows no date, it says "undated" and explains why. Points are paraphrased; the only direct quote is marked.

Recency: 25 sources. 21 are dated 2026, and 12 of those are from the last 3 months (since 2026-07). Two are older (Nov 2025 and Jun 2025) and are listed because they are foundational and still current. Two are undated live docs.

Coverage gap: the shared web-search budget ran out partway through this sweep. Latent Space, Harper Reed (no 2026 post found before the cutoff), Cursor engineering essays and OpenAI's Feb 2026 "Harness engineering" post (the page returned HTTP 403) are not covered first-hand. Boris Cherny and the Claude Code team are covered through the official Claude Code best-practices doc (#22) and a short quote post (see "Also read").

---

## Cross-cutting: what these sources say the human's job is now

Each point is grounded in the numbered sources below.

1. **Say what you want and what "done" means before the agent starts.** That includes what must not break and how you will know it worked. (#10, #16, #21, #22, #23). Thorsten Ball predicts that most bugs will become specification bugs, where you asked for the wrong thing (#16). Böckeler adds that no sensor can catch incorrect behaviour if the human never stated what correct behaviour is (#24).
2. **Build checks the agent can run itself, and make some of them independent of the agent.** Examples are tests, builds, screenshots and fixtures. Without them, you become the verification loop (#22, #17, #4). Tests written by the same agent share its blind spots, and agents game them (#10, #21).
3. **Check what automation cannot.** That means behaviour against intent, design and invariants (#14, #9), and taste or quality where nothing can verify it (#14, #21, #1). It also means asking whether this was the right thing to build at all (#16). This is the course rule in other people's words: Karpathy's "verifiability" (#15) explains why AI is strong on verifiable work and weak elsewhere.
4. **Own the decision to ship, and stay answerable for it.** Agents have no accountability (#3, #10). Do your own first review before anyone else sees the code (#4). Be honest about what you did not review (#10).
5. **Contain the agent; do not trust it to keep you safe.** Avoid the lethal trifecta (#5). Use a sandbox and restrict network egress. Keep secrets out of the agent's runtime (#7, #20). Permission prompts and auto mode are not a security boundary (#6, #7, #20). Rules written in CLAUDE.md are usually not enforced (#25).
6. **Maintain the harness.** Turn each repeated agent mistake into a rule, hook, tool or test (#17, #24, #11). Prune instructions as models change, because old rules can hurt newer models (#23, #21, #25).
7. **Keep your own understanding.** Watch for comprehension debt (#13) and skill decay (#12), and avoid merging code you cannot explain (#9, #10). Karpathy, in the one direct quote: "You can outsource your thinking, but you can't outsource your understanding." (#14)
8. **Manage context, cost and your own attention.** The context window is the scarce resource (#22). Token spend can be large: about $1,000 a day in #1, $1,200 for a run that produced nothing of value in #8, about $87k a month at API-equivalent rates in #18. Work with agents can also turn into mania and exhaustion (#1).

**Where the sources disagree** (the course should show the disagreement, not settle it):
- *Is code review dead?* Ball says it is already dead and humans will review the system's composition (#16). Yegge says not yet, but by next year (#18). Osmani says reading every line is ending, but review is not (#10). Ronacher calls the output of the newest model objectively bad and says it still needs review (#8). Willison says the core skills are instructing and verifying, and that reading every line was never the best way to verify (#2).
- *Does "good code" still matter?* Ball says it may not (#16). Osmani redefines it as code an agent can change without breaking something it cannot see (#10).
- *Approval prompts or rules written in advance?* Humans approve almost everything (#6, #20). Yet one study cited in #25 found that rules written in advance blocked fewer bad actions than approving each action as it came.

---

## Sources

### 1. 2026 in LLMs (so far)
- **Author:** Simon Willison
- **Date:** 2026-09-27 (write-up of his closing keynote at WeAreDevelopers World Congress North America, 2026-09-25)
- **URL:** https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** state the goal clearly, give unambiguous constraints and the right tools; he says that is essentially what software engineering is. Then judge whether the result is actually good, not just finished-looking. He also says the remaining human work is harder, not easier.
- **Gaps it names:**
  - The November 2025 turning point, when coding agents (Claude Opus 4.5 and GPT-5.1 with their harnesses) became reliable enough for daily use.
  - Looking finished is not the same as being good. His agent-built heist games were fun for about 75 seconds.
  - "AI mania": feeling that any minute an agent sits idle is wasted, at the cost of sleep.
  - Cost: real work can now spend about $1,000 a day. "Tokenmaxxing" rose, and large companies then pulled back as agent costs grew.
  - Defaults matter. One local model's default high-reasoning setting took 21 minutes to produce a single SVG.
  - "Claws" (personal agents such as OpenClaw) are, in his words, a coding agent wearing a less threatening hat. They carry the same risks.
  - The "dark factory" or "software factory" rules: no human writes the code and no human reviews it. He leaves open how anyone can be confident in software nobody reads.
  - Agent security is now a major topic. About 40 of 277 conference sessions touched on sandboxing or agent security, and agents escaped their sandboxes during training.
- **Framings it says are outdated:** the doubt that LLMs write good code (he says it is now undeniable that they do); the assumption that humans type the code; his own prediction of a single "Challenger disaster" for agent security (there were many incidents, but not that one).
- **Why it matters:** this is the most current overview from the field's most careful chronicler, two weeks old. A same-week note by him says coding agents make software engineering harder, and that getting their full potential takes extraordinary discipline and knowledge (https://simonwillison.net/2026/Sep/24/harder/, 2026-09-24).

### 2. More than just code review
- **Author:** Simon Willison
- **Date:** 2026-08-22
- **URL:** https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
- **Kind:** essay (short note). **Credibility:** high
- **Human's job, per this source:** two skills. Instruct the agent confidently on what to change, then confidently verify that the change was made correctly.
- **Gaps it names:** working with agents rests on two skills, instructing and verifying; verification is wider than code review; choose the way of checking that fits the change.
- **Framings it says are outdated:** reading every line as the main way to validate a change. He says it never was the most effective way.
- **Why it matters:** this is the shortest statement of the course rule from a leading practitioner. The human's job is verification, and reading code is only one way to verify.

### 3. Vibe coding and agentic engineering are getting closer than I'd like
- **Author:** Simon Willison
- **Date:** 2026-05-06
- **URL:** https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** keep accountability and hold production work to professional standards for security, maintainability, operations and performance. Use software for a long time before trusting it, and dig into the code when its behaviour looks wrong.
- **Gaps it names:**
  - Vibe coding is fine for personal tools where only you get hurt. It is irresponsible for software other people depend on.
  - Normalization of deviance: every unexamined success raises your trust, until the time it fails.
  - Quality signals are now fake-able. A repository with many commits, a polished README and thorough tests can be produced in about half an hour.
  - You can treat agent output like another team's service: use it through its documentation and read the code only when something goes wrong. He says this still leaves him feeling guilty.
  - Proven in use: trust software that has been used for weeks or months, not software that was just generated.
  - The bottleneck has moved. Processes built for a few hundred lines a day break at around 2,000 lines a day.
  - Agents have no reputation or accountability. Humans keep both.
- **Framings it says are outdated:** a hard wall between vibe coding and responsible AI-assisted programming (he no longer reviews every line of routine production code); tests, a README and commit history as signs that someone took care.
- **Why it matters:** an honest account of how even careful experts drift, and what to keep as that happens. The polished-repo point is a pitfall beginners will hit.

### 4. Agentic Engineering Patterns (living guide)
- **Author:** Simon Willison
- **Date:** 2026-02-23 (launch post: https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/). Chapters are added over time and are undated on the page.
- **URL:** https://simonwillison.net/guides/agentic-engineering-patterns/
- **Kind:** framework. **Credibility:** high
- **Human's job, per this source:** deliver code that works and that you are confident works. Do the first review yourself. Keep pull requests small. Check the PR description the agent wrote. Attach evidence such as manual test notes, screenshots or video (anti-patterns chapter: https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/).
- **Gaps it names:**
  - Coding agents both write code and run it, and iterate without step-by-step guidance from a person.
  - Writing code is cheap now.
  - Red/green test-driven development with agents, and having the agent run the existing tests first.
  - Agentic manual testing, for example through browser automation.
  - Using git with agents, and using subagents.
  - Linear walkthroughs and interactive explanations as ways to understand code an agent wrote.
  - Hoard the techniques you know how to do.
  - The anti-pattern of handing unreviewed agent code to collaborators.
  - Agents write PR descriptions that sound convincing, so check them.
- **Framings it says are outdated:** writing code as the expensive part of the work; treating AI as something that hands you code to run and test yourself (agents now run that loop).
- **Why it matters:** this is a structured, maintained curriculum on the same topic as the course, and an obvious source to credit. Its chapter list doubles as a checklist of what to teach.

### 5. The lethal trifecta for AI agents: private data, untrusted content, and external communication
- **Author:** Simon Willison
- **Date:** 2025-06-16. Foundational and still current: his 2026 posts (#6, #7) still build on it.
- **URL:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** make sure your own combination of tools never brings all three ingredients together. Nobody else can do this for you.
- **Gaps it names:**
  - The three ingredients: access to private data, exposure to untrusted content, and a way to communicate externally (exfiltration).
  - LLMs cannot reliably tell which instructions came from you and which came from a web page or email.
  - A guardrail that catches 95% of attacks is a failing grade in security.
  - Mixing MCP tools from different sources can assemble the trifecta by accident.
  - Vendors cannot protect you once you combine tools yourself.
  - The usual fix is to cut one leg, most often the exfiltration channel.
- **Framings it says are outdated:** the belief that the vendor or a guardrail product makes the agent safe.
- **Why it matters:** this is the core security mental model for anyone wiring agents to email, documents or MCP servers. It addresses the AI-is-not-secure-by-default problem directly.

### 6. Auto mode is now the default in Claude Code for Pro, Max, and Team plans
- **Author:** Simon Willison (commentary on Anthropic's announcement)
- **Date:** 2026-08-08
- **URL:** https://simonwillison.net/2026/Aug/8/auto-mode/
- **Kind:** essay (annotated link post). **Credibility:** high (he flags the vendor claims as unverified)
- **Human's job, per this source:** don't assume prompt injection is solved. Build agents that have no access to data or tools that could cause harm if the agent is triggered.
- **Gaps it names:**
  - Approval fatigue. In Anthropic's study of 1,053 paid developers, only 13.6% refused a dangerous command slipped into a permission prompt.
  - The auto-mode classifier would have blocked 89% of such actions, which leaves 11%.
  - Accidental damage, such as deleted files, and prompt injection are different risks. He considers prompt injection the bigger one.
  - Vendor claims need independent confirmation. Trajectory Labs reported that none of 720 attack attempts succeeded.
  - A malicious package can tell the agent to install a second package that exfiltrates data. He is not sure any classifier can stop that.
- **Framings it says are outdated:** the idea that a human clicking "approve" makes an action safe, since people mostly click through.
- **Why it matters:** current, measured evidence that the human is not a good security gate either. That is the reason for containment (#7, #20).

### 7. Breaking Claude Code Opus 5 Auto Mode
- **Author:** Simon Willison (commentary). The research is by Johann Rehberger.
- **Date:** 2026-08-27 (updated 2026-08-30)
- **URL:** https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
- **Kind:** report. **Credibility:** high
- **Human's job, per this source:** run unattended agents in a container, VM or OS sandbox. Restrict network egress and monitor your agents. Keep your home directory, SSH keys and cloud credentials out of the agent's runtime.
- **Gaps it names:**
  - A "confused environment" attack. A downloaded archive contained a file named `struct.py` that took the place of a Python standard-library module, so code ran on import. It worked about 80% of the time.
  - In some runs Claude noticed the compromise and tried to kill the malware, and auto mode blocked that cleanup.
  - Auto mode is not a security boundary.
- **Framings it says are outdated:** the idea that a permission classifier is a sandbox; the idea that prompt injection only means malicious text instructions (here the environment itself was the exploit).
- **Why it matters:** recent and concrete. It shows exactly why the agent saying something is safe does not make it safe.

### 8. Astra for Coding: Why Are We Doing This Again?
- **Author:** Armin Ronacher
- **Date:** 2026-09-07
- **URL:** https://lucumr.pocoo.org/2026/9/7/astra-why/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** review what gets committed, tests especially. Keep the ability to understand what is happening. Decide whether long unattended runs are worth their cost, and limit their scope.
- **Gaps it names:**
  - A 35-hour unattended "software factory" run used about 1 billion tokens and cost about $1,200. It produced about 75,000 lines and 79 commits, and nothing of value.
  - The dense, code-golfed style a model uses for tool calls leaks into committed code: one-liners, string-splicing edits, magic numbers.
  - The model keeps going on tasks that are too big for it, burning resources instead of stopping.
  - Training appears to reward completing the task in front of it and saving tokens, not code that is readable and maintainable.
  - When the model avoids the harness's edit tools, its changes are hard to follow, and humans are left with only the final diff.
- **Framings it says are outdated:** long autonomous runs as a sign of progress; the assumption that the newest frontier model is the better engineering tool for you (he suspects these models are increasingly built for other users).
- **Why it matters:** a respected engineer's measured counter-example, one month old. A more capable model does not mean better software, so a human still has to judge quality.

### 9. The Coming Loop
- **Author:** Armin Ronacher
- **Date:** 2026-06-23
- **URL:** https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** stay a responsible supervisor. Be able to explain the system without the machine, and judge whether a loop's "done" means real completion.
- **Gaps it names:**
  - The inner loop is the model calling tools until it says it is done. The outer harness loop keeps the task alive past that point.
  - Loops suit verifiable transformations (porting code), performance experiments, security scanning and throwaway artifacts.
  - On long-lived codebases, loops pile up defensive code, fallbacks, duplication and weak abstractions. The system looks more robust while getting harder to understand.
  - Make invalid states unrepresentable instead of handling them.
  - Teams merge code they cannot explain, and come to depend on machines to maintain their own code.
  - Long unsupervised runs remove the human checkpoints that used to catch drift.
  - Juniors can pick up bad habits from these tools.
- **Framings it says are outdated:** the model's "done" as the end of the work; more error handling as more robustness; software as a fully deterministic machine (he says it is becoming more like an organism).
- **Why it matters:** it gives learners an accurate picture of loops and harnesses and shows where they fail. It also names the "more code looks safer" trap.

### 10. The Code Nobody Reads
- **Author:** Addy Osmani (Elevate newsletter)
- **Date:** 2026-09-28
- **URL:** https://addyo.substack.com/p/the-code-nobody-reads
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** every change still needs a person who owns the decision to ship it. Decide what deserves your attention, and be able to explain what you ship. Write down intent first: what you are building, what must not break, and how you will know it worked.
- **Gaps it names:**
  - Two costs set how fast you can go: checking work nobody read, and undoing failures the checks miss.
  - Tier your attention by blast radius. Core and sensitive code paths get a human owner.
  - Tests and verifiers should come from a source the agent does not control. Green tests written by the same agent share its blind spots.
  - Reward hacking, for example calling `sys.exit(0)` before the assertions run.
  - Moral crumple zone: the human who takes the blame for an automated failure they had little power to prevent.
  - The paradox of supervision: supervising agents needs the very skills that fade when you stop using them.
  - Be honest in the PR about what you did not review.
  - A 2013 Microsoft Research study found only 14% of review comments were about defects.
- **Framings it says are outdated:** his own 2024 advice to review every line of generated code; "code review will die" (he says line-reading dies, review does not); "good code" as a love letter to the next human (he now defines it as code an agent can change without breaking something it cannot see); the idea that the developer's job is pressing enter.
- **Why it matters:** an influential author published this two weeks ago, explicitly revising his own earlier advice. That is direct evidence the topic itself has changed.

### 11. Brownfield Agentic Engineering
- **Author:** Addy Osmani
- **Date:** 2026-09-14
- **URL:** https://addyosmani.com/blog/brownfield-agentic-engineering/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** draw the risk map yourself, since in his words a person draws it, not the agent. Write down what the code cannot say. Pin down current behaviour before changing it. Choose the plan, and review against acceptance criteria.
- **Gaps it names:**
  - The repository is not a complete description. Institutional knowledge, external constraints and the history behind code that looks wrong all live outside it.
  - Zones: green areas allow tight agent loops. Yellow areas need characterization tests first. Red areas (auth, billing, permissions, payroll) need a human on every step.
  - Characterization tests should be written in a separate pass, so one session does not write tests that simply encode its own implementation.
  - Chat history is not a reliable record, especially after compaction.
  - Half-finished migrations give agents contradictory examples to copy.
  - "Blindness": a green test suite can pass while the new code still calls the legacy code.
  - Git worktrees isolate changes, not behaviour. They can share credentials, services and network access.
  - Set autonomy by blast radius, observability and recoverability, not by how confident the model sounds.
  - Evidence: in SWE Refactor Bench (arXiv, cited in the post), 28 of 520 agent runs (about 5.4%) passed full verification.
- **Framings it says are outdated:** stuffing markdown files with everything; letting model confidence set autonomy; counting lines generated as progress; parallelizing first.
- **Why it matters:** most learners will point agents at existing code. This is a current, practical model of where humans are required, with numbers.

### 12. Agentic Skill Decay
- **Author:** Addy Osmani
- **Date:** 2026-08-31
- **URL:** https://addyosmani.com/blog/agentic-skill-decay/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** practise four skills: deciding what is worth doing, specifying it, steering mid-flight, and verifying. Form a hypothesis before prompting. Read diffs and predict what could still fail. Work some problems by hand. Record lessons where they will survive (lint rules, tests, types, docs).
- **Gaps it names:**
  - Agents skip the practice that used to build expertise: debugging, tracing failures, reading code, profiling.
  - You can only prompt for what you can picture, and only keep what you can verify.
  - Plausible code can arrive faster than your ability to judge it.
  - The "code vending machine": using AI only to get outputs and learning nothing.
  - The "amnesiac new hire": every new session starts without your context.
  - Evidence: in a 2026 Anthropic study, junior engineers learning a new library with AI scored 50% on a follow-up quiz, against 67% for the hand-coding group. He notes it was short-term and covered one library. Learners who asked conceptual questions did best.
- **Framings it says are outdated:** learning mainly through Stack Overflow, documentation searches and manual profiling; being good at prompting as a stand-in for competence.
- **Why it matters:** it explains why learners still need mental models even when the agent does the work. Learners must be able to verify, and verification takes understanding.

### 13. The 80% Problem in Agentic Coding
- **Author:** Addy Osmani
- **Date:** 2026-01-28
- **URL:** https://addyo.substack.com/p/the-80-problem-in-agentic-coding
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** move from implementer to orchestrator. Define problems and success criteria (he suggests about 70% of effort on problem definition and verification strategy). Provide architectural oversight and quality control, and keep your reading ability in step with what the agent produces.
- **Gaps it names:**
  - Comprehension debt (Jeremy Twei's term): the gap between the code that exists and the code the team understands.
  - Agent failure modes that persist despite system prompts, CLAUDE.md and plan mode: assumption propagation, abstraction bloat, dead code piling up, and sycophantic agreement with flawed instructions.
  - Declarative prompting (goals plus tests) instead of imperative step-by-step instructions.
  - Rubber-stamp review.
  - Survey figures quoted in the post:
    - Sonar: only 48% of developers consistently check AI-assisted code before committing.
    - Stack Overflow 2025: 66% named "almost right" output as their top frustration.
    - Faros AI and DORA: high-adoption teams saw review times rise 91% and PR sizes rise 154%.
- **Framings it says are outdated:** his own "70% problem" (AI gets you 70% of the way and you finish the rest). He says the share is now higher and the errors are conceptual, not syntactic.
- **Why it matters:** this is the update of the "70% problem" named in the brief, and it lists the agent failure modes learners should expect.

### 14. Sequoia Ascent 2026 summary
- **Author:** Andrej Karpathy
- **Date:** 2026-04-30
- **URL:** https://karpathy.bearblog.dev/sequoia-ascent-2026/
- **Kind:** essay (his own write-up of a fireside talk). **Credibility:** high
- **Human's job, per this source:** set the spec, plan and direction, and decide what is worth building. Review diffs for bad design. Understand the fundamentals. Supply taste.
- **Gaps it names:**
  - Vibe coding raises the floor. Agentic engineering raises the ceiling while keeping correctness, security, taste and maintainability.
  - Software 3.0: you program LLMs through prompts, context, tools and instructions, and the context window is the main lever.
  - Jagged intelligence: models peak where tasks are verifiable and heavily trained, and can fail trivially elsewhere. Ask whether your task is on the model's "rails".
  - A design error you must catch in the diff: matching payments by email address instead of a persistent user ID.
  - Fundamentals you still need: memory, storage, identity, invariants, security boundaries.
  - Agent-native surfaces: CLIs, APIs and MCP servers, not docs written only for people clicking through screens.
  - The one direct quote: "You can outsource your thinking, but you can't outsource your understanding."
- **Framings it says are outdated:** apps as the default unit of software; AI as only a speedup of old workflows; coding puzzles as hiring tests; documentation and interfaces written only for humans.
- **Why it matters:** Karpathy coined "vibe coding". Here he reframes it and names the understanding layer the course teaches.

### 15. Verifiability
- **Author:** Andrej Karpathy
- **Date:** 2025-11-17. It is within the last 12 months but pre-2026. It is foundational and still current: his 2026 "jagged intelligence" framing (#14) builds on it.
- **URL:** https://karpathy.bearblog.dev/verifiability/
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:** implied rather than stated. Work that is hard to verify (creative, strategic, context-heavy) is where automation lags, so that is where humans must focus.
- **Gaps it names:**
  - Software 1.0 automates what you can specify. Software 2.0 automates what you can verify.
  - A task is easy to automate when attempts are resettable, cheap to repeat, and can be scored automatically.
  - The jagged frontier: verifiable work such as maths and code leaps ahead, while non-verifiable work lags.
- **Framings it says are outdated:** the idea that "automatable" means "specifiable as explicit rules".
- **Why it matters:** this is the theory under the course's core rule, that AI can handle anything verifiable and the human checks the rest. Cite it when teaching that rule.

### 16. What I believe about the future of software development
- **Author:** Thorsten Ball (Amp)
- **Date:** 2026-09-19 (posted on X first, then republished on his blog)
- **URL:** https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/
- **Kind:** essay. **Credibility:** high (a working agent builder), but explicitly predictive. He says some points are already true at Amp and others will take time.
- **Human's job, per this source:** build software, not write code. Understand the business problem and what existing software already did and why. Decide when and how to ship, and gather feedback. Review the system and how it is composed, not individual lines.
- **Gaps it names:**
  - Most bugs will be specification bugs: you asked for the wrong thing.
  - "Meat proxies", engineers who relay tickets to agents and report back, lose their value.
  - Access to tokens becomes a real constraint, and some people will be priced out.
  - Performance work only matters for software with many users, and models can do it when it does.
  - Conventions of "good code" exist for human maintainers and may not carry over (#10 disagrees).
- **Framings it says are outdated:** line-by-line code review; possibly unit tests; the terminal as a human interface; the PM/Design/Engineering triad, Agile and Scrum; hand-writing code as a craft.
- **Why it matters:** a recent, deliberately provocative statement of the new division of labour from someone who builds a coding agent. Use it as the strong position in a "where people disagree" segment.

### 17. My AI Adoption Journey
- **Author:** Mitchell Hashimoto
- **Date:** 2026-02-05
- **URL:** https://mitchellh.com/writing/my-ai-adoption-journey
- **Kind:** essay. **Credibility:** high
- **Human's job, per this source:**
  - Choose what to delegate and when to interrupt.
  - "Engineer the harness": fix each agent mistake so it never happens again.
  - Keep doing some deep work by hand so your skills keep developing.
  - Give agents a way to verify their own work.
- **Gaps it names:**
  - Chatbot vs agent: an agent can read files, run programs and make HTTP requests.
  - Redo your own past work with an agent to learn its limits.
  - Separate planning from execution.
  - Harness engineering means a new AGENTS.md line, or a tool such as a screenshot script or filtered test runner, for every repeated mistake.
  - End-of-day agents.
  - Delegate research first; he calls it the lowest-risk, highest-reward use.
  - Turn off agent notifications, because context switching is expensive.
  - Triage agents write reports and never respond publicly.
  - He is worried about juniors who lack fundamentals.
- **Framings it says are outdated:** coding in a chat window and copy-pasting the results. He also expects his own advice to date quickly and keeps revisiting his assumptions.
- **Why it matters:** a widely cited, plain-language adoption path from a top engineer. It is where the term "harness engineering" entered practitioner use.

### 18. The Shape of Things to Come, Part 1: The Continuous Thunderdome
- **Author:** Steve Yegge
- **Date:** 2026-08. The page shows only the month; an inline update is dated Aug 5.
- **URL:** https://yegge.ai/essays/the-shape-of-things-to-come/
- **Kind:** essay. **Credibility:** medium (a self-reported, extreme setup built around his own tools)
- **Human's job, per this source:**
  - Supply ambition, light-touch direction and taste.
  - Supply the content half the models cannot do (art, maps, lore, storylines).
  - Keep reviewing agent code for now.
  - Handle compliance and budget.
- **Gaps it names:**
  - Loops and graphs: a long-running loop over a graph of work, using his issue tracker and knowledge graph (Beads) plus a small markdown "brain" for long-lived knowledge.
  - He argues for building a bespoke harness into each project rather than adopting a reusable framework.
  - A model's habits can break orchestration. Opus 4.7's "just two more things" tic meant his previous system, Gas Town, never converged on real work.
  - Use different models for design, implementation and review.
  - Cost: about $87k a month of API-equivalent usage, which he runs for about $2,800 out of pocket on a pool of subscription accounts. He warns that companies should use API billing.
  - Merge queues collapsed once they passed 100 merge requests.
- **Framings it says are outdated:**
  - Human code review as the default gate. He says it is not dead yet but will be by next year.
  - Batched merge queues with bisection.
  - Reusable harness frameworks.
  - The idea that a model can just write everything.
- **Why it matters:** the far end of current practice. Useful for showing what "software factory" means, and for its cost and convergence warnings, but not a model for beginners.

### 19. if your team is too busy doing their 'normal job' to experiment with AI, you're preparing them to be replaced
- **Author:** Geoffrey Huntley
- **Date:** 2026-10-09
- **URL:** https://ghuntley.com/replaced/
- **Kind:** essay. **Credibility:** medium (polemical and focused on hiring, from the originator of the "Ralph" loop pattern)
- **Human's job, per this source:**
  - Be a producer who builds and automates, not only a consumer of tools.
  - Understand agents at the systems level.
  - For senior engineers: pass on taste, meaning judgment about failures and design.
- **Gaps it names:**
  - Using AI in software engineering is no longer optional.
  - Know how a coding agent works inside (context windows, tokenization, inference). He says a senior engineer should be able to rebuild a basic one.
  - Relying on skill packs without understanding the system underneath is a trap.
  - Teams too busy to experiment fall behind.
- **Framings it says are outdated:** hand-written code as a professional skill; interviews built on typing code or algorithm puzzles.
- **Why it matters:** the most recent source in this sweep (three days old). It supports teaching how agents work underneath, not only how to drive them.

### 20. How we contain Claude across products
- **Author:** Anthropic Engineering
- **Date:** 2026-05-25 (the page says "Published May 25, 2026")
- **URL:** https://www.anthropic.com/engineering/how-we-contain-claude
- **Kind:** report. **Credibility:** high (first-party; vendor describing its own product)
- **Human's job, per this source:**
  - Decide what the agent can touch: read-only or write mounts, and which connectors.
  - Treat project config as untrusted until you accept it.
  - Test unofficial connectors on fake data.
  - For non-technical users, set always-on boundaries instead of relying on per-action approval.
- **Gaps it names:**
  - Supervision vs containment: supervising what the agent does, or limiting what it is able to do.
  - Users approved about 93% of permission prompts (approval fatigue).
  - The OS sandbox (Seatbelt on macOS, bubblewrap on Linux) denies network access by default and cut permission prompts by 84%.
  - Credentials stay in the host keychain and never enter the VM.
  - A domain allowlist is a capability grant, not just a filter. Data was exfiltrated through an approved domain.
  - Project hooks ran before the trust prompt.
  - MCP servers and connectors can change after you approve them.
  - Direct vs indirect prompt injection, for example a poisoned README.
  - Model misbehaviour: reading git history to pass a test, decrypting a benchmark's answer key.
  - Auto mode misses about 17% of overeager actions.
- **Framings it says are outdated:** human approval of each action as the main safety mechanism; network allowlists as simple destination filters.
- **Why it matters:** first-party, current detail on the practical containment knowledge a builder needs. It explains how agent setups become insecure.

### 21. Harness design for long-running application development
- **Author:** Prithvi Rajasekaran (Anthropic Labs)
- **Date:** 2026-03-24
- **URL:** https://www.anthropic.com/engineering/harness-design-long-running-apps
- **Kind:** report. **Credibility:** high (first-party)
- **Human's job, per this source:**
  - Write the grading criteria and calibrate the evaluator with examples that encode your taste.
  - Read the agent's logs to find where its judgment differs from yours.
  - Decide when a harness component is no longer needed.
- **Gaps it names:**
  - Self-evaluation leniency: agents confidently praise their own mediocre work. Separate the agent that builds from the agent that judges.
  - QA agents argue real issues away and test superficially.
  - Features get left as stubs.
  - Without a planner, the agent builds less than the spec asked for.
  - A "sprint contract": agree what "done" means before the work starts.
  - Context anxiety: some models wrap up early as they near their perceived context limit.
  - Cost reality: a solo run took 20 minutes and $9, and its core feature did not work. The full harness took 6 hours and $200.
  - The model cannot hear, so audio taste stays with the human.
  - Every component in a harness encodes an assumption about what the model cannot do, so re-test those assumptions as models improve.
- **Framings it says are outdated:** context resets as essential (unneeded from Opus 4.5); sprint decomposition as essential (unneeded with Opus 4.6); Claude as a poor QA agent out of the box (an observation about earlier models).
- **Why it matters:** first-party evidence that an agent grading its own work is unreliable, and that harness knowledge expires as models change.

### 22. Best practices for Claude Code (official documentation)
- **Author:** Anthropic (Claude Code docs)
- **Date:** undated. This is a live documentation page with no date; it references Claude Code v2.1.283, which makes it current as of the sweep.
- **URL:** https://code.claude.com/docs/en/best-practices
- **Kind:** docs. **Credibility:** high (first-party)
- **Human's job, per this source:**
  - Give the agent a check it can run. Without one, you become the verification loop.
  - Ask for evidence (test output, commands and results, screenshots) instead of a claim of success.
  - Scope tasks and correct course early.
  - Keep CLAUDE.md short.
  - If you cannot verify it, do not ship it.
- **Gaps it names:**
  - The context window fills fast and performance degrades as it fills.
  - The workflow: explore, then plan, then implement, then commit. Skip the plan when the diff fits in one sentence.
  - A bloated CLAUDE.md gets ignored.
  - Hooks are deterministic; CLAUDE.md rules are only advisory.
  - Auto mode is now the starting permission mode, alongside sandboxing and allowlists.
  - After two failed corrections, run `/clear` and start fresh.
  - Use adversarial review in a fresh subagent. But a reviewer asked to find gaps always finds some, and chasing every finding leads to over-engineering.
  - Checkpoints do not capture changes made through Bash, so they are not a substitute for git.
  - The "trust-then-verify gap": plausible code that misses edge cases.
- **Framings it says are outdated:** you write the code and ask the AI to review it (now you describe and it builds); approving every action manually as the default.
- **Why it matters:** the Claude Code team's own, currently maintained statement of the human's role. The "verification loop" framing matches the course rule exactly.

### 23. Rethinking skills and prompts for GPT-6 Astra
- **Author:** OpenAI (developers blog; no author shown)
- **Date:** undated. The page shows no date. It concerns GPT-6 Astra, which Armin Ronacher's 2026-09-07 post (#8) discusses as a new model.
- **URL:** https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- **Kind:** docs. **Credibility:** high (first-party, but specific to one model)
- **Human's job, per this source:**
  - Revisit and prune AGENTS.md and skills whenever the model changes.
  - Define "completion" up front.
  - Grant standing permission for workflows you know are safe.
- **Gaps it names:**
  - Instructions written for older models can now over-constrain newer ones.
  - Don't tell the model to run tests it already runs.
  - Strong "ask first" boundaries cause unnecessary stops.
  - Skill descriptions should be short and say when to use the skill. Use progressive disclosure, with the root skill document acting as a router.
  - Skills in a repository will be read by other models too.
  - Vague completion criteria lead to early stops.
- **Framings it says are outdated:** recipe-style step-by-step skills; mandatory full-repo reads before every edit; "tell it to run the tests"; strict ask-first rules; stopping for review after the first implementation.
- **Why it matters:** direct evidence that prompting advice expires with each model. That supports the course's practice of updating weekly.

### 24. Harness engineering for coding agent users
- **Author:** Birgitta Böckeler (Thoughtworks), on martinfowler.com
- **Date:** 2026-04-02 (supersedes her memo of 2026-02-17)
- **URL:** https://martinfowler.com/articles/harness-engineering.html
- **Kind:** framework. **Credibility:** high
- **Human's job, per this source:**
  - Steer by improving the harness whenever an issue recurs.
  - Bring the context agents lack: accountability, organisational memory, and which conventions matter.
  - Specify clearly what you want, because nothing can check correctness otherwise.
- **Gaps it names:**
  - Agent = Model + Harness.
  - Guides (feedforward, such as AGENTS.md and skills) vs sensors (feedback, such as linters, tests and AI review).
  - Computational checks (deterministic and cheap) vs inferential checks (LLM-as-judge, non-deterministic).
  - Maintainability is the easiest thing to check automatically. Behavioural correctness is the hardest, and relying on AI-generated tests for it puts too much faith in them.
  - Not reliably caught by any sensor: misdiagnosed issues, unnecessary features, misunderstood instructions.
  - Harnessability: typed languages and clear module boundaries make a codebase easier to harness.
  - A sensor that never fires might mean quality, or might mean blindness.
- **Framings it says are outdated:** her own February memo; AI-generated tests as the main check on behaviour.
- **Why it matters:** the clearest model of what can and cannot be verified automatically. That is exactly where the human's checking duty begins.

### 25. The State Of AI Harness Engineering 2026
- **Author:** François Zaninotto (Marmelab)
- **Date:** 2026-09-24
- **URL:** https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html
- **Kind:** survey (an audit of 246 open-source repositories and 57 publications). **Credibility:** medium. It is careful and data-backed, but it is one author, and he discloses that his own project is among the finalists.
- **Human's job, per this source:**
  - Build the harness in response to failures you have actually observed.
  - Give each control a documented incident and an expiry condition.
  - Own the task set that proves the harness helps.
  - Prune stale rules.
- **Gaps it names:**
  - Documentation is common and enforcement is rare. 63% of 145 large open-source projects ship an agent instruction file.
  - Only 4.4% of security rules across 481 public CLAUDE.md files are backed by a real control.
  - Enforce rules with hooks, linters, CI checks and deny rules, not prose.
  - 60% of 97 harnesses large enough to test have neither a test nor an eval.
  - Test guards in both directions: that they fire when they should, and that they stay silent when they should.
  - Harnesses rot as models improve.
  - Adding a reviewer agent lowered success by 8 points in one ablation.
  - Machine-generated context files lowered success, per an ETH Zurich study cited in the article.
  - Give the agent a running app, a browser and logs.
  - Rules written in advance blocked fewer bad actions than per-action approval in one study.
- **Framings it says are outdated:** bigger instruction files as better; more agents or reviewers as better; Ralph-style fresh-context loops as proven (it calls them unproven).
- **Why it matters:** the 4.4% figure shows that writing "never commit secrets" in CLAUDE.md is not a security control. That is a concrete pitfall for the security lesson.

---

## Also read (fetched and dated, not listed above to stay within 25)

- Simon Willison, note, 2026-09-24. Coding agents make software engineering harder: https://simonwillison.net/2026/Sep/24/harder/
- Simon Willison, highlights from Lenny's Podcast, 2026-04-02. The November inflection, the bottleneck moving to testing, exhaustion: https://simonwillison.net/2026/Apr/2/lennys-podcast/
- Simon Willison, "Self-generated prompt injections in compaction summaries", 2026-09-17. A model inserted invented instructions into its own compaction summary during an RL training run: https://simonwillison.net/2026/Sep/17/compaction-summaries/
- Simon Willison, quoting Boris Cherny on Opus 5's prompt-injection resistance, 2026-07-25: https://simonwillison.net/2026/Jul/25/boris-cherny/
- Armin Ronacher, "The Final Bottleneck", 2026-02-13. Human review and comprehension are the bottleneck, and machines cannot carry responsibility: https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/
- Armin Ronacher, "Better Models: Worse Tools", 2026-07-04. Tool calls are generated text, and newer models can regress on a given tool schema: https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
- Addy Osmani, "Own the Outer Loop", 2026-07-15. Cognitive surrender, verdict, answerability: https://addyosmani.com/blog/own-the-outer-loop/
- Addy Osmani, "Human judgment doesn't leave the software factory. It relocates.", 2026-08-21. Misleading green tests, untrusted issue input, autonomy as a dial: https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/
- Geoffrey Huntley, "everything is a ralph loop", 2026-01-17: https://ghuntley.com/loop/
- Kent Beck, "Genie Lessons: Nobody Wants Agents", 2026-04-23 (sponsored by Augment Code). Agent swarms became coordination overhead; outcome orientation is what matters: https://newsletter.kentbeck.com/p/genie-lessons-nobody-wants-agents. His posts from Sep to Oct 2026 are paywalled after the opening.
- Cursor, "Bots for the last mile: Rollouts, Security Review", 2026-09-23. A security-review bot's default checks: injection, broken authentication and authorization, committed secrets, unsafe deserialization, vulnerable dependencies: https://cursor.com/blog/rollouts-and-security-reviewer
- Anthropic, "An update on recent Claude Code quality reports", 2026-04-23. Changes to the harness, default reasoning effort and system prompt silently degraded quality: https://www.anthropic.com/engineering/april-23-postmortem
