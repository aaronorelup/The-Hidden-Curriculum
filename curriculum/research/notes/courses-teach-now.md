# Batch 1: courses-teach-now

What a top university course teaches agent-era builders in Fall 2026, what it dropped from Fall 2025, and how that compares with the two lessons Aaron sent back.

Read 2026-10-12 by the research crew (agent read-courses-teach-now). Every point below comes from a page fetched and read in full on 2026-10-12. Line numbers refer to the transcript text files as served on that date.

The lecture material is **paraphrased** with line references. The only direct quotes are the two per source in each "Quotes" list.

- Sources read: S001, S002, S003, S004 (with the Playback 00.06 prompt).
- One cited reading was fetched to check S003's numbers: the LangWatch compaction study (details under S003).
- Unreadable: none.

---

## S001: CS146S: The Modern Software Developer (Fall 2026 syllabus, compared with Fall 2025)

- **Author:** Mihail Eric (instructor), Stanford University. TAs: Isaac Kan and Vijay Daita in 2026, Febie Lin and Brent Ju in 2025.
- **Date:** the page has no publication date. **2026-09-22 is the first Fall 2026 session** (Tue 9/22, course intro and a coding agent built in 200 lines), not a page date. The page is a living page: it already links the 10/1 transcript.
- **URL:** https://themodernsoftware.dev/ (Fall 2025 version: https://themodernsoftware.dev/fall2025)
- **How it was read:** the Syllabus tab is rendered by JavaScript. Both full schedules and both grading tables were taken from the site's own bundle, `/_next/static/chunks/02aahykf~d51u.js`. In it, array `e_` is Fall 2026 and `eP` is Fall 2025; the page code picks `e_` when the term is fall2026.

**Summary.** The Fall 2026 course has been rebuilt around the agent harness. Week 1 covers the inside of a coding agent: the loop, the core read/write/edit/bash tools, and system prompts. After that it covers context engineering and RePPIT spec-driven work, skills, CLAUDE.md/AGENTS.md plus hooks plus subagents, agent-ready repos, agentic code review, security, background agents, and AI-native teams (MCP portals, LLM gateways, model routing). It ends with "the software factory".

The 2025 weeks on the AI IDE, the modern terminal (Warp), one-prompt UI/app building, and "Modern Software Support" (which included debugging) are gone. Grading changed:

| | Final project | Weekly assignments | Open-source contributions | Participation |
|---|---|---|---|---|
| Fall 2025 | 80% | 15% | none | 5% |
| Fall 2026 | 50% | 15% | 30% | 5% |

### Fall 2026 schedule (every week; topics condensed from the outline)

| Week | Title | Topics | Sessions |
|---|---|---|---|
| 1 | The Internals of Coding Agents | What an LLM is and what the agent loop looks like inside. The core tools (read, write, edit, bash). How production agents structure system prompts and tool definitions. | 9/22 intro + build Claude Code in 200 lines. 9/24 system prompts of state-of-the-art agents (S002) |
| 2 | Advanced Context Engineering | Advanced prompting and when each technique applies. RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development. MCP fundamentals (servers, clients, tools, transport). Tool design for agent ergonomics. | 9/29 prompting + RePPIT (S003). 10/1 MCP and tool-calling |
| 3 | Agent Skills and CLI | Skills: SKILL.md plus scripts encode a workflow. Web skills. Working effectively from the CLI. | 10/6 skills. 10/8 guest Lee Robinson |
| 4 | Customizing Your Agent and Repository | CLAUDE.md vs AGENTS.md, what goes where. Hooks for lint gates, test runs and guardrails. Subagent patterns (planner / implementer / reviewer). | 10/13 customizing your setup. 10/15 guest Boris Cherny |
| 5 | Agent-Ready Codebases | What makes a repo agent-ready (structure, docs, tests, checks). Scoring and auditing readiness. Common gaps that block agents. | 10/20 readiness. 10/22 guest Eno Reyes (Factory) |
| 6 | Agentic Code Review | What AI review catches and misses. Review architectures and custom rules. Fitting AI review into a team's PR workflow. | 10/27. 10/29 guest Silas Alberti (Cognition) |
| 7 | Security | SAST/SCA, dependency and secret-leak vulnerabilities. Prompt injection and agent-specific attack surfaces. Agent-assisted triage and remediation. | 11/3. 11/5 guest Isaac Evans (Semgrep) |
| 8 | Background Agents | Async, cloud-delegated agents. Fleets of parallel agents. Issue-to-PR pipelines triggered from Slack, Linear and GitHub. | 11/10. 11/12 guest Rajesh Bhatia (Cloudflare) |
| 9 | Building an AI-Native Team | MCP portals with centralized, permissioned tool access. LLM gateways, model routing, cost optimization. Org-wide adoption. | guests Elad Gil, Amjad Masad (Replit) |
| 10 | The Software Factory + The Future | Self-running, self-improving software systems. Running and securing agents after deployment. What comes next. | 12/1 agents in big teams. 12/3 the software factory |

**Fall 2026 readings:**
- Week 1: Building a Coding Agent (YouTube); Lessons from Building Claude Code (X post by trq212); Dive into Claude Code (arXiv 2604.14228).
- Week 2: The Context Tax: When to Compact (LangWatch); OpenSpec; Superpowers; Enterprise MCP (Cloudflare).
- Week 3: pstack (Cursor plugins); Matt Pocock's Skills; browse.sh.

### Fall 2025 schedule, and what happened to each week

| 2025 week (topics) | In Fall 2026 |
|---|---|
| 1 Introduction to Coding LLMs (what an LLM is; how to prompt effectively; sessions on how an LLM is made and "power prompting"; prompt-engineering readings and a prompting playground) | **Reframed.** "What an LLM is" survives only as half of one bullet, paired with the agent loop. How an LLM is made, power prompting and the playground are gone. Prompting is now one bullet under context engineering. |
| 2 The Anatomy of Coding Agents (architecture; tool use; MCP) | **Kept and deepened.** Now Week 1 (harness internals) plus Week 2 (MCP fundamentals, tool ergonomics). |
| 3 The AI IDE (context management; PRDs for agents; IDE integrations and extensions) | **Dropped as a week.** Context management moved to Week 2, and PRDs became RePPIT/spec-driven work. IDE integrations are gone. |
| 4 Coding Agent Patterns (autonomy levels; human-agent collaboration; "how to be an agent manager") | **Replaced** by Customizing Your Agent (instruction files, hooks, subagent patterns). Autonomy levels as a topic are gone. |
| 5 The Modern Terminal (AI-enhanced CLIs; terminal automation; Warp) | **Dropped as a week.** Survives as one bullet ("working effectively from the CLI") in Week 3. Warp is now an open-source partner that sells "software factories" (S003 line 45). |
| 6 AI Testing and Security (secure vibe coding; history of vulnerability detection; AI-generated test suites) | **Split.** Security is now its own week (Week 7). AI-generated test suites and the history of vulnerability detection are gone as topics. Testing now sits inside hooks (Week 4, test runs), agent-ready repos (Week 5, tests and checks) and the T of RePPIT. |
| 7 Modern Software Support (which AI code systems to trust; **debugging and diagnostics**; documentation generation; AI code review) | **Dropped.** Replaced by Agentic Code Review (Week 6). Debugging and diagnostics, and documentation generation, are gone. |
| 8 Automated UI and App Building (design and frontend for everyone; rapid prototyping; end-to-end apps from one prompt) | **Dropped.** The slot went to Background Agents. |
| 9 Agents Post-Deployment (monitoring; automated incident response; **triaging and debugging**) | **Merged** into Week 10 as one bullet (running and securing agents after deployment). Triaging and debugging are gone. |
| 10 What's Next for AI Software Engineering | Kept, as The Software Factory + The Future. |

**Correction to the reading-list focus line.** "Testing and security in one week" describes **Fall 2025** (Week 6). In Fall 2026 security has its own week, and testing is no longer a week topic.

**New in 2026 (no 2025 equivalent):**
- harness and system-prompt anatomy
- RePPIT
- skills (SKILL.md)
- CLAUDE.md vs AGENTS.md
- hooks
- subagent patterns
- agent-ready codebases
- prompt injection as an agent attack surface
- secret-leak and dependency (SCA) scanning
- background agents and fleets
- issue-to-PR triggers
- MCP portals
- LLM gateways and model routing
- cost optimization
- the software factory
- open-source contributions as 30% of the grade

**Gone from 2025:**
- how an LLM is made
- power prompting
- the AI IDE and IDE extensions
- autonomy levels as a topic
- the AI terminal (Warp) as a week
- AI-generated test suites
- the history of vulnerability detection
- debugging and diagnostics
- documentation generation
- design and frontend for everyone
- end-to-end apps from one prompt
- triaging and debugging after deployment

### Gaps it shows
- **The agent harness is the subject.** The course opens on loop, tools and system prompts, not on how an LLM is trained.
- **Context engineering replaced prompt engineering.** Prompting is one bullet inside context engineering.
- **Instruction files, hooks and subagents** have their own week. The topic line pairs hooks with lint gates, test runs and guardrails. The hooks lecture is on 2026-10-13, so the only evidence today is that topic line.
- **Making a repo agent-ready** has a week: structure, docs, tests and checks, and the common gaps that block agents.
- **AI code review in a team PR workflow,** including what it misses and custom rules.
- **Security of AI codebases,** made specific: SAST/SCA, dependency and secret-leak vulnerabilities, prompt injection and agent-specific attack surfaces.
- **Background and parallel agents** triggered from Slack, Linear and GitHub.
- **Team-level cost and access:** LLM gateways, model routing, cost optimization, MCP portals with permissioned tool access.
- **What dropped out:** debugging appears nowhere in the 2026 outline. This supports Aaron's 00.06 rejection.

### Outdated framings it implies
- An agent course that starts with how an LLM is made and how to prompt.
- The AI IDE as the place the work happens.
- End-to-end apps from a single prompt.
- Debugging and diagnostics as a human skill to teach.

### Quotes
- "CLAUDE.md and AGENTS.md: what to put where" (Week 4 topic)
- "What AI review catches well, and what it misses" (Week 6 topic)

---

## S002: CS146S lecture 2026-09-24: anatomy of a state-of-the-art coding agent (transcript)

- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-24 (confirmed: the syllabus lists Thu 9/24, which is a Thursday in 2026, and the file is named 9-24-26). The HTTP Last-Modified header (2026-10-12 06:45) is a redeploy time, not the lecture date.
- **URL:** https://themodernsoftware.dev/materials/9-24-26-transcript.txt (371 lines, read in full)

**Summary.**
- Tuesday's class built a bare coding agent in roughly 150-200 lines (line 46).
- This lecture takes apart the harness around Claude Code running Opus 5.5, which the lecturer says had come out about two days earlier (line 59). It works from intercepted API requests captured through a proxy; the first assignment has students capture their own (lines 97-104).
- It covers the tools block (about 40 built-in tools plus MCP tools), the system prompt, the memory block, CLAUDE.md/AGENTS.md injection, plan mode, skills, subagents, hooks (only briefly) and compaction.
- It ends on the trend toward fewer tools and shorter prompts, and the seesaw between investing in the model and investing in the harness.

### Anatomy as taught (with line references)
- **Bare loop vs harness.** About 150-200 lines give a working agent (line 46). The loop is: the user talks to the harness, the harness talks to the LLM, the LLM requests tools, and results come back. Everything around that loop is "the harness" (lines 52-57, 72).
- **Model as a remote intelligence layer.** The model runs privately on the provider's servers and can't be inspected; the harness can (line 50). The lecturer estimates the models at two trillion parameters or more; treat that as his estimate, not a fact.
- **The framing (line 63).** The lecturer calls harness design one of the hardest and most important problems in coding agents and in agents generally. It applies beyond coding: sales, legal, support (lines 63-66). Line 84 adds that agents outside coding are increasingly built around coding capabilities.
- **Standard components** (lines 68-70): system prompt; config files (AGENTS.md, CLAUDE.md); tool lists; plan mode; subagents; skills; hooks; compaction.
- **About 40 built-in tools** in Claude Code, and the model is post-trained to use them (lines 86-88). Categories (lines 141-143):
  - files and Bash
  - cron-style monitoring and scheduling
  - web search and LSP search
  - agent tools, planning and isolation
  - artifacts and MCP resources
  - asking the user, invoking skills, notifications, feedback
- **Every tool's definition is injected into the prompt.** Its name, description, comments and full signature all become prompt text (line 93). Clear docstrings and argument types matter because they are what the model reads to decide when to use a tool (line 95). The whole tools block goes with every request (lines 130-134, 150).
- **MCP tools** carry an `mcp__` prefix (line 173). Every loaded MCP server's tools ride along in every request (line 150). In late 2024 GitHub's MCP server shipped with about 110 tools (line 194). More irrelevant material makes the agent perform worse (line 154).
- **Message roles** (lines 115-123):
  - user: what you typed, and also tool results
  - system-level messages that the harness injects behind the scenes
  - assistant: tool calls
- Above his first typed question sat text he never typed: a system reminder carrying his CLAUDE.md, headed by a line telling the model the instructions override its defaults (lines 277-282).
- **The system prompt is not yours.** The harness sets it, you can't change it, and it is in every request (line 203).
  - It identifies the model as Claude Code (line 210). The Opus 5.5 version is about 50-80 lines, with security instructions, session information and a large memory section (lines 212-216).
  - It was 200-250 lines until a month or two before. Instructions on how to use Git were cut because training seems to have absorbed them (lines 225-227).
  - Before the user's first message, tens of thousands of tokens are already spent on text the user didn't write (line 232).
- **Memory** is a fairly new implicit mechanism that learns from your behaviour. It is stored in files at a project-level location, in a format the prompt prescribes (lines 219-221, 253). Flat files are often as good as RAG/GraphRAG for retrieval; his own company uses flat files (lines 260-264).
- **CLAUDE.md vs AGENTS.md** (lines 266-295):
  - They are functionally the same. AGENTS.md is the cross-tool standard, which Anthropic began supporting a few weeks before the lecture. You can symlink one to the other.
  - CLAUDE.md is the part of the prompt the user controls, as opposed to the system prompt.
  - Include the exact commands for tests and starting the server, but not whole blocks of code. Too much overconstrains the agent.
- **Plan mode** (lines 304-319): harnesses added it nine or more months ago. A tool enters the mode, and the harness injects a prompt with phases (understand requirements and send agents to explore, design, review, final plan). Its artifact is a plan file, and another tool exits the mode.
- **Skills** (lines 148-152, 181-183, 322-336):
  - A skill is a written procedure: tool calls and scripts tied together with prompts, defined in SKILL.md.
  - Only its metadata sits in context until it is relevant (progressive disclosure). It is invoked by the user or proactively.
  - An MCP tool is a primitive, like one API call; a skill wraps tools into multistep operations.
- **Subagents** get fresh context windows, run in parallel, and return their results to the main loop (lines 341-345).
- **Compaction** runs automatically near the window limit or when invoked manually. His example squeezes 500k tokens into 150k (lines 350-352). "Dumb zone" is an informal name for when the model gets less effective (line 367).
- **Trend:** fewer, more powerful tools (Bash, SQL) and shorter prompts. The field keeps swinging between investing in the model and investing in the harness (lines 190-196, 356-369). The lecture says Claude Code became popular around December 2025 for its minimalist harness (line 190).

### What the agent now does that people (or the harness) used to
- The model no longer needs Git instructions spelled out (lines 225-227).
- Built-in plan mode runs the requirements-design-review loop and sends agents to explore the code (line 315).
- Memory is extracted automatically from behaviour (line 219).

### Gaps it shows
- **What the harness is, and which parts you control.** You control CLAUDE.md, skills, MCP servers, plan mode and when to compact. You do not control the system prompt or the model.
- **What one request carries:**
  - every tool's full definition
  - the system prompt
  - memory
  - your instruction file
  - injected reminders
  - all previous messages
  - Tens of thousands of tokens are used before you type.
- **MCP servers have a context cost.** Each enabled server's tool list is sent on every turn.
- **Memory is files on disk** that the harness writes and injects.
- **AGENTS.md and CLAUDE.md** are the same idea under two names. Keep them short: commands, not code dumps.
- **Plan mode is an injected prompt plus a plan file.**

### Outdated framings it implies
- The model as a next-word predictor behind a chat box, with nothing around it. The lecture skips training entirely (line 52) and starts from the loop.
- "Enable every MCP server you can find."
- "A longer system prompt or CLAUDE.md is better" (overconstraining, lines 291-293).

### Quotes
- "harness design is probably one of the hardest and most important problems" (line 63)
- "tens of thousands of tokens have already been consumed by material outside my control" (line 232)

---

## S003: CS146S lecture 2026-09-29: advanced prompting and context engineering, RePPIT (transcript)

- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-29 (confirmed: the syllabus lists Tue 9/29, and the file is named 9-29-26)
- **URL:** https://themodernsoftware.dev/materials/9-29-26-transcript.txt (287 lines, read in full; the last ~25 lines are garbled after-class talk)
- **Spelling:** the transcript writes "REPIT". The syllabus spells it RePPIT (Research, Propose, Plan, Implement, Test).

**Summary.**
- Working with agents in big codebases runs into context limits: some agents advertise a million tokens, but not every token in that window is useful (line 51).
- He calls spec-driven engineering the de facto industry method for hard tasks (line 55). He demonstrates RePPIT live, extending a vibe-coded Mint clone (Vue, which he says he doesn't know) with a spending trend line.
- Along the way he gives rules on stale docs, when to compact or clear, which model to use for which phase, and where the human stays: intent/architecture and code review.
- The agent (Cursor) opened a browser and tested its own feature, something he says agents could not do six months earlier (lines 199-201).

### RePPIT steps as taught
1. **Research** (lines 87-93, 119-123, 189). A skill documents only what exists today (the code's behavioural contracts) and suggests no improvements. The output is a structured research document.
   - The document has two jobs: it seeds the agent, and it gives the human a mental model.
   - He validates research less than he used to, because research is compression and agents are very good at it.
2. **Propose** (lines 125-137, 149-151). The agent proposes **two** distinct, orthogonal solutions; he sees diminishing returns beyond two. Each covers context, overview, key changes, trade-offs, validation and open questions.
   - He says the human should be most involved in this step and the next. The human chooses.
3. **Plan** (lines 167-185). A design-document template covers:
   - current state
   - functional and nonfunctional requirements
   - decisions and trade-offs
   - technical design, including which files change, with line numbers
   - testing and observability
   - security and rollout
   - **an explicit out-of-scope list**, which stops the agent wandering into unrelated work
4. **Implement** (line 197). The prompt is little more than "implement the plan".
5. **Test** (lines 193-211). Unit, integration and smoke tests are among the best verification. If implementation quality matters less and less, checking the output must be strict.
   - The browser run was a behavioural check. Performance, quality and readability belong to code review.
- **Notes on the skills:**
  - They were built iteratively over about 1-1.5 years and are committed to a team repo, where others test them (lines 101-103).
  - Skills committed to a repo come free with a clone, or can be packaged as org-wide plugins (line 111).
  - Context7 is an MCP server that pulls current third-party docs (line 107).
- **Adapt it, don't worship it.** Built-in planning in Claude and Codex is good (line 163), and a healthcare student extended the framework (line 165). Superpowers (300,000 stars by his count) is just a set of skills; OpenSpec is another option (lines 257-261).

### Context-engineering rules
- **Advertised vs usable context.** A 1M window is not 1M useful tokens (line 51). The cited study puts compaction at 250k-450k tokens, and his takeaway is to compact often (lines 227-231). His intuition is that the useful share of the window is half to three-quarters (line 241).
- **Clear after choosing.** After picking a proposal he would normally clear the context, because the rejected alternative left in it can confuse the agent about which one it is building (line 233).
- **Hand off through a file.** Past a few hundred thousand tokens, he writes what matters to a file and starts a fresh context from it (line 235).
- **Stale docs are worse than none.** Reuse existing docs only if they are well maintained. Choosing between bad docs and none, he starts from scratch. Outdated docs should be deleted or updated, and agents can run on a schedule to keep docs current (lines 141-145).
- **Model per phase.** Use a strong model for research, proposals and planning, where the thinking happens; lighter models are fine for implementation and testing (line 237).
- **Match process to task size** (lines 245-255):
  - copy change or small fix: just ask
  - small multi-file feature: make a plan
  - medium feature, refactor or migration: repeated research/propose/plan, separate sessions, subagents
  - very large: split into issues, one agent per issue, stacked issues
- **Review your specs.** He calls this the most important best practice (line 243).

### Where the human stays
- **A mental model of the code** (lines 121-123). He needs enough to tell good from bad: not every detail, but knowing there is a frontend and a backend, that it uses Vue, and what form the models take.
- **Intent and architecture, and code review** (line 155) are the two main places humans still help. The early stages are among the highest-leverage places for a human today (line 157). He leaves open whether that holds in two years (line 159).
- **Specifying the output** (line 195). Developers' time goes to saying how the output should behave.
- **The agent self-tests** (lines 199-203). Cursor opened a browser, made synthetic data and uploaded it through the app's CSV form on its own, which he says was not possible six months earlier. If your agent lacks this, add a browser tool such as Playwright MCP.
- **AI code review in practice** (lines 213-217) runs four or five agents, each on one area (security, performance, style, consistency, edge cases), triggered by a GitHub action, with a coordinating agent that merges the reports. His demo skill sorts findings into must fix / recommended / consider.

### The cited study (fetched to verify line 227)
- **The Context Tax: When to Compact Your Coding Agent.** Rogerio Chaves, LangWatch, **2026-08-02** (byline and `datePublished`). https://langwatch.ai/blog/context-tax-when-to-compact. Assigned as a Week 2 reading in S001.
- **TL;DR:** compact between 250k and 450k tokens. The author found no benefit in letting an agent run near 1M.
- **Correction 1:** the post's range varies **by kind of work**, not by model as the lecture put it:
  - PR driving: 200-250k
  - research: 250-300k
  - QA: 250-350k
  - building and code understanding: 300-450k
- **Correction 2:** the lecture's "about half a million useful tokens" (line 231) is not what the post measured. As the window grew 16.6x, the part judges marked as actually used stayed at about 8k tokens (7,949 to 8,452). The share in use fell from 47.5% below 50k to 2.5% above 600k.
- **Cost growth:** each doubling of context costs about 6x more (a power law with exponent about 2.55). With 25 tool calls at 500k context, you pay for 25 x 500k, not one request.
- **Caching:** cached reads are about 10x cheaper per token, yet they were 95% of the blowup day's spend. A cached token is bought again on every step.
- **The incident:** the author's session limit ran out within minutes, twice. The day had used 2.25 billion tokens, 82% of them from subagents.
  - Two forked subagents (spawned with a full copy of the parent's conversation) used 1.14 billion tokens.
  - They started at 523K and 304K tokens instead of the roughly 30k a fresh subagent gets.
  - Told to do one thing and stop, they ran 10.7 and 8.7 hours.
  - One test run cost about 568k tokens of context.
- **Compaction loses almost everything:** a median 574,875-token window becomes a 4,382-token summary.
- **Quality after compaction:** for at least 30 steps afterwards, 41.9% of the user's messages contain a correction, against a 17.7% baseline. The tool-error rate stays flat, so the calls still work but the decisions get worse.

### Gaps it shows
- A 1M context is not 1M usable tokens, and long sessions cost more than they look.
- You must clear context after decisions, so rejected options don't linger.
- Old docs mislead agents.
- Use a strong model for thinking and a cheap one for doing.
- Process weight should scale with task size.
- You still need a map-level mental model of the code.
- Agents now test their own work in a browser, which is why hand-debugging is no longer the lesson.
- Review moves to specs (before) and to multi-agent code review (after).

### Outdated framings it implies
- Vibe coding as the method for hard tasks (lines 59-63). It is fine for a copy change (line 251).
- "A bigger context window is better."
- "Feed the agent all the existing docs."
- "The human writes and debugs the implementation."

### Quotes
- "we still need a mental model of the code as it exists" (line 123)
- "This wasn't true six months ago" (line 201, about the agent opening a browser to test its own work)

---

## S004: AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening

- **Author:** Aaron Orelup (drafted by Claude from his feedback)
- **Date:** **2026-10-04** (confirmed: the page header reads "AO-034 / Oct 04, 2026")
- **URL:** https://aaronorelup.com/ledger/lessons-sent-back/
- **Also read:** Playback, session 5c6d06f5-9b98-4551-8a6c-3ce7ab0b8993 ("The Hidden Curriculum: daily lesson"). This is Aaron's prompt of 2026-10-03 22:49 UTC rejecting 00.06 v1. Only his own words were used.

**Summary.**
- Agents published seven lessons in five days, and Aaron sent two back as out of date.
- **00.05 v1**, "How LLMs work (just enough)", covered tokens, next-token guessing, the context window as a desk, temperature and hallucination. That is the 2021 picture of a model behind a chat box with nothing around it. It was replaced by the 19:54 "How AI models work today".
- **00.06 v1**, "How to learn anything technical", came through the new research step with current numbers but taught a five-step habit for debugging an error. Aaron hasn't debugged an error himself since he started using Claude Code. It was replaced by "Trust what you can verify".
- The lesson for the course: research makes facts current but cannot tell when the **topic** is out of date. The rejections added 14 lessons, taking the curriculum from 183 to 210.

### Framings Aaron rejected
- **The 2021 LLM picture.** Tokens, next-token guessing, the context window as a desk, temperature and hallucination as the whole story. None of it is wrong, but it shows nothing around the model.
- **Hand-debugging.** The 00.06 row was the five-step habit: read the error, search the message, read docs, ask AI with context, make a tiny test. Aaron said the agent does all of that itself. It can be mentioned, but it should not be the lesson.
- **The row assumed the learner reads the error.** Every agent worked inside that assumption, and the research only made the wrong lesson more convincing.

### His gap list (the yardstick for every batch)
From the 00.05 rejection:
1. Models that take and make images, audio and video (multimodal).
2. Models getting worse as their context fills.
3. The different ways they remember: searching old chats, keeping their own memory, files and Notion reached through tool calls.
4. System prompts and instruction files.
5. Diffusion.
6. Caching, and the difference between cache reads, cache writes, input and output tokens.
7. Chat, Cowork and Code across browser, desktop, CLI and cloud.
8. Skills, connectors and plugins.
9. Always-on personal agents like OpenClaw.

From the 00.06 rejection (post plus Playback):
10. A security hole in code that runs.
11. Code that ignores a team's conventions, or imports libraries the project doesn't use. Playback: some projects have a fixed set of modules they import.
12. A dependency list that grows because nobody owns it. Playback: without someone who knows which libraries the program should use, the AI keeps adding dependencies.
13. Asking a model "make sure it's secure" or "make sure it's ready to deploy" when you have no way to check its answer.

Lessons the rebuild plans added:
- From 00.05: diffusion models, context engineering, how AI apps remember, plugin marketplaces, prompt caching and token meters, multimodal APIs, voice AI, enterprise plans, always-on personal agents, AI design tools.
- From 00.06: team norms for AI-written code, prompt injection, review and security agents, checks before real users.

Second-hand facts the post reports (from the lessons' research; not re-checked here):
- The chat/Cowork merge was announced 16 September.
- Meta's Muse and OpenAI's dots launched in September.
- Stack Overflow's new questions are down about 99% from their peak.
- In the 2025 developer survey, "almost right" AI answers were the top frustration.
- In a 2026 study, about one AI coding answer in twenty named a package that doesn't exist.

### The rule, in Aaron's words (Playback, 2026-10-03, paraphrased except the quote below)
- **Security:** you can ask the AI to make the code secure, but you can't verify its answer. At that point you either learn to check it yourself or bring in an expert to review it.
- **Deployment:** someone who knows how to code should verify a product before it ships. Asking the AI "is this ready to deploy?" is where problems start.
- **Teams:** AI-written code can differ from the team's norms and use different libraries than the project's set, which makes life harder for people who write code by hand. Someone who knows the libraries should decide the dependencies.
- **The saying:** don't ask questions you can't verify the answer to. He adds that the AI gets better at verifying its own work every day.

### Gaps it shows
All 13 items above. CS146S (S001-S003) covers 2, 3 (partly), 4, 6 (only through the cost of context), 8, 10, 11 (code review, custom rules) and 13 (security week).

CS146S does **not** cover:
- multimodal input and generation
- diffusion
- the chat/Cowork/Code surfaces
- always-on personal agents
- voice AI
- enterprise plans

Those need other batches.

### Outdated framings
- The 2021 picture of an LLM.
- The five-step debugging habit as the core skill.
- Asking the AI to make the code secure or deploy-ready, and believing it.

### Quotes
- "You can only trust AI on what AI can verify." (Playback, 2026-10-03)
- "I haven't needed to debug an error myself since I started using claude code" (Playback, 2026-10-03)

---

## Cross-source notes

- **Hand-debugging is gone from both.** Aaron's rejection of it is matched by Stanford dropping debugging and diagnostics (2025 Week 7) and triaging and debugging (2025 Week 9). The 2026 lecture shows the agent testing its own work in a browser (S003 line 199).
- **Both moved off the 2021 LLM picture.** Stanford demoted how an LLM is made and power prompting. The 2026 Week 1 starts from the agent loop and the harness, and the lecture skips training (S002 line 52).
- **Where the human is needed.** Stanford: intent and architecture, specs, code review, a map-level mental model (S003 lines 121-123, 155-157, 243). Aaron's rule adds: whatever the AI cannot verify (security, deploy readiness), the human checks or hands to an expert.
- **How fast things changed, for the course's "updated weekly" premise:**
  - Opus 5.5 was about two days old at the lecture.
  - The system prompt shrank from 200-250 lines to about 50-80 within a month or two.
  - Anthropic began supporting AGENTS.md a few weeks earlier.
  - Agents could not test in a browser six months earlier.
  - The 2025 syllabus was largely rewritten within a year.
- **Leads for other batches:**
  - The 10/1/26 MCP and tool-calling transcript exists at https://themodernsoftware.dev/materials/10-1-26-transcript.txt. It was not read in this batch; read it for the connectors/MCP gap.
  - The Week 4 (hooks, 10/13) and Week 7 (security, 11/3) lectures have not happened yet. Re-check the syllabus for their transcripts.
