# Sweep: lists and roadmaps (what people need to know, updated for AI)

Agent: sweep-lists. Compiled 2026-10-12. Every block below comes from a page that was fetched and read in this session. Dates were checked against bylines, page metadata, GitHub commit history, the dev.to API, or the HN Algolia API. Where a page shows no date, it says "undated".

Recency: 23 of 25 sources are dated 2026. 12 are from the last three months (since 2026-07). Two are older or undated: the Anthropic sandboxing post (2025-10-20) and the Claude Code best-practices doc (a living doc with no date).

## Cross-source read (what the lists agree on, and where they disagree)

Topics that recur across 5 or more independent lists:
1. **Verification loops.** Give the agent a check it can run (tests, build, screenshot), then review the evidence, not the agent's claim. Sources: Claude Code docs, Willison, Missing Semester, CS146S, Synfinity, roadmap.sh.
2. **Context as a resource.** The window fills up and quality drops. Know when to use clear, compact or rewind. Keep CLAUDE.md lean. Use skills and subagents. Sources: Missing Semester, Claude Code docs, roadmap.sh x2, CS146S, Synfinity.
3. **Git as the undo button.** Commit after every success. Revert with git, not the AI's own undo. Checkpoints do not capture Bash changes. Sources: roadmap.sh, Claude Code docs, Synfinity, Willison, Kunal.
4. **Security failures specific to AI-built apps.** RLS off by default, service_role and NEXT_PUBLIC_ keys, IDOR, webhook signatures, rate limits on things that cost money, prompt injection, excessive agency, denial-of-wallet. Sources: OWASP 2026, boxed-dev, Chizee, TechTimes, CS146S week 7, roadmap.sh.
5. **The human's remaining jobs.** Intent and architecture, checking code against the requirement, reviewing before inflicting code on others, and deciding scope and risk. Sources: CS146S, Fable guide, Willison, Dice, Missing Semester.
6. **Permissions and sandboxes.** Approval fatigue, YOLO mode only inside a VM or container, filesystem plus network isolation. Sources: Missing Semester, Anthropic sandboxing, Claude Code docs, roadmap.sh Claude Code, awesome-claude-code.

Contradictions the course should resolve explicitly:
- **Who checks security.** roadmap.sh (vibe coding) and Hack Safe tell readers to "ask AI to audit" security as a mandatory step, and neither says to verify the audit. The Claude Code docs say the agent doing the work should not be the one grading it, and that a reviewer asked for gaps always finds some. OWASP, TechTimes (Stanford RCT) and Chizee (the security-review Action is not hardened against prompt injection) show why an AI's "it's safe" cannot be the last word. This lines up with the course rule: the AI handles what is verifiable, and the human or an expert checks what it cannot verify.
- **Hand-debugging.** Dice (2026-09-23) treats hand-debugging as the skill juniors are losing. roadmap.sh, Missing Semester and the Claude Code docs say to hand the error to the agent and let it run the check. Read together: the agent fixes verifiable errors. The skill that remains human is checking code against intent, because passing tests can still miss the requirement (Dice, Kunal, Willison).
- **Gaps in the roadmaps themselves.** roadmap.sh's AI Product Builder roadmap (2026-07-13) has no security topic at all. All of its topic files were checked, and the only near-mention is "Supabase has built-in authentication". This is direct evidence that popular 2026 learning paths leave security out.

---

## 1. Agentic Coding (lecture), The Missing Semester of Your CS Education, 2026 edition
- **Author:** MIT Missing Semester team (missing-semester/missing-semester on GitHub)
- **Date:** 2026-01-21 (lecture date on the 2026 schedule). Notes were last revised 2026-02-24 per GitHub commits ("Explain deprecation of reusable prompts").
- **URL:** https://missing.csail.mit.edu/2026/agentic-coding/ (index: https://missing.csail.mit.edu/2026/)
- **Kind:** course | **Credibility:** high
- **Gaps it names:**
  - How the agent loop works: the harness resends the whole conversation every turn and feeds tool results back in
  - Context window limits, and performance degrading before the window overflows
  - Clearing vs rewinding vs compaction (the LLM summarizes the history prefix)
  - AGENTS.md / CLAUDE.md is loaded in full at session start
  - Skills load on demand; subagents return only their result
  - llms.txt for dependencies newer than the model's training data
  - Privacy: the provider may effectively receive your whole repo
  - YOLO mode (`--dangerously-skip-permissions`) only inside an isolated VM or container
  - Review output for correctness and security bugs; verifying can be harder than writing
  - Debugging spirals and rabbit holes
  - Set up feedback loops so the agent runs the failing check itself
  - Git worktrees for parallel agents
  - Agents use the wrong invocation (e.g. `python -m mypy`) and need correcting
- **Outdated framings:** Reusable prompt templates are superseded by skills (the notes were revised to say so). Fixing compiler, linter and test errors is listed as an agent use case: the agent runs the failing check in a loop.
- **Why it matters:** This is the canonical "missing semester" list, rewritten for 2026 with agentic coding as one of five new lectures. Its human-vs-agent split (write specs, audit tests, confirm tool calls, keep your own understanding) maps directly onto the course rule. Gaps it does not cover: prompt injection and cost.

## 2. Beyond the Code (lecture), The Missing Semester 2026
- **Author:** MIT Missing Semester team
- **Date:** 2026-01-22 (lecture date on the 2026 schedule)
- **URL:** https://missing.csail.mit.edu/2026/beyond-code/
- **Kind:** course | **Credibility:** high
- **Gaps it names:**
  - LLM-written commit messages describe only the diff unless you give them the why
  - Disclose meaningful AI contributions and say which parts
  - Don't hand unexplained AI code to overloaded maintainers
  - AI review is a first pass, not a replacement for human review
  - Report vulnerabilities privately via SECURITY.md
  - Check the license (copyleft/GPL, employer implications) before contributing
  - Minimal reproducible bug reports
  - Having AI do the work while learning can be self-defeating
  - Covert AI use where it is prohibited is a serious mistake
- **Outdated framings:** None stated outright. The implied update is that commit and PR hygiene now includes feeding the agent the context it lacks.
- **Why it matters:** It covers the social and legal layer of building with AI (licensing, disclosure, responsibility for code you did not write), which beginners never hear about.

## 3. HN discussion: "The Missing Semester of Your CS Education, Revised for 2026"
- **Author:** Hacker News community (457 points)
- **Date:** 2026-02-23 (HN Algolia API created_at)
- **URL:** https://news.ycombinator.com/item?id=47124171
- **Kind:** thread | **Credibility:** medium
- **Gaps it names:**
  - Testing and QA called a major gap, especially as AI-generated code grows
  - You still need git's underlying data model even when AI supplies the commands
  - Troubleshooting methodology
  - Code quality beyond formatting: complexity, modularity
  - Open-source contribution etiquette
  - Agents do well on well-known problems but struggle to reformulate problems
- **Outdated framings:** Memorizing git commands is giving way to understanding git's model, since the AI writes the commands. Some commenters argue the reverse (drop agentic coding, it's a fad), so the thread is a live disagreement, not a settled view.
- **Why it matters:** It shows what practitioners think the official list still misses, and where they disagree about AI.

## 4. Stanford CS146S: The Modern Software Developer, Fall 2026 syllabus and lecture transcripts
- **Author:** Mihail Eric (instructor), Stanford University
- **Date:** 2026-09-22 (Fall 2026 term start; lectures run to 12/3). Read: the syllabus, plus transcripts of the 9/24, 9/29 and 10/1/2026 lectures.
- **URL:** https://themodernsoftware.dev/ (transcripts at /materials/9-29-26-transcript.txt, etc.)
- **Kind:** syllabus | **Credibility:** high
- **Gaps it names:**
  - Where humans remain useful: intent and architecture, and code review (9/29 lecture)
  - RePPIT (Research, Propose, Plan, Implement, Test) and spec-driven development
  - Stale docs are worse than none: the agent should start fresh rather than ingest outdated docs
  - Clear context after choosing between proposals, so the rejected one doesn't confuse the agent
  - Designing tools for agent ergonomics; MCP servers, clients and transport
  - Skills (SKILL.md + scripts) as encoded workflows
  - CLAUDE.md vs AGENTS.md, and hooks for lint and test gates
  - Agent-ready codebases: structure, docs, tests and checks
  - Agentic code review: what AI review catches well and what it misses
  - Security: SAST/SCA, dependency and secret leaks, prompt injection, agent-specific attack surfaces
  - Background agents and fleets; issue-to-PR pipelines
  - MCP portals, LLM gateways, model routing and cost
  - Running and securing agents after deployment
  - Unit, integration and smoke tests as the main verification, because implementation details matter less
- **Outdated framings:** The Fall 2025 weeks "The AI IDE", "The Modern Terminal" and "Automated UI and App Building" were replaced in Fall 2026 by context engineering, skills and CLI, agent-ready codebases, agentic code review, background agents and the software factory (both lists are in the site's code). The instructor says he validates the agent's research less than he used to and focuses on implementation. He also says agents now test their own work unprompted, which was not true six months earlier.
- **Why it matters:** This is the most current university syllabus on the topic, running right now. Comparing the 2025 and 2026 syllabi is a direct measure of how fast the topics themselves go out of date.

## 5. roadmap.sh: Vibe Coding roadmap
- **Author:** roadmap.sh (Kamran Ahmed and contributors)
- **Date:** 2026-02-27 (launch per roadmap.sh changelog). Content last synced 2026-09-17 (GitHub kamranahmedse/developer-roadmap).
- **URL:** https://roadmap.sh/vibe-coding (topic text: github.com/kamranahmedse/developer-roadmap/tree/master/roadmaps/vibe-coding)
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - Commit after every successful AI task, and start each feature on a clean git slate
  - Revert with git rather than the AI's built-in undo (unreliable across multiple files)
  - Never hardcode credentials; keep .env in .gitignore
  - Pick a popular stack, because the AI was trained on it
  - If the AI fails after 3 prompts, start a fresh chat
  - Paste the error message and let the AI do the rest
  - When you find a bug, have the AI write a breaking test first
  - Use MCP (e.g. Playwright) so the AI can drive a browser
  - Keep CLAUDE.md updated; one task at a time; plan MVP phases
- **Outdated framings:** Your role changes from writing code to directing it. Debugging by hand is replaced by pasting the error.
- **Caution:** It tells readers to "explicitly ask AI to perform a security audit" as a mandatory pre-launch step, with no instruction to verify that audit. This is exactly the trust trap the course rule warns against. The course should cite it as an example of the misconception.
- **Why it matters:** It is the most-visited learning-path site's take on vibe coding. Its git and credentials items are solid; its security item is the pitfall.

## 6. roadmap.sh: Claude Code roadmap
- **Author:** roadmap.sh
- **Date:** 2026-02-27 (launch per changelog). Content last synced 2026-10-01 (GitHub commits).
- **URL:** https://roadmap.sh/claude-code (topic text: github.com/kamranahmedse/developer-roadmap/tree/master/roadmaps/claude-code)
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - What a coding agent is; the agentic loop
  - Permission modes, from Plan (read-only) to BypassPermissions ("YOLO")
  - Security framed as "an intern with root access", exposed to prompt injection and data exfiltration
  - Sandboxing
  - Every MCP server, skill and subagent consumes context ("context pollution")
  - Subscription vs pay-per-token API pricing
  - Hooks (PreToolUse/PostToolUse), headless mode, git worktrees, scheduling jobs, channels
  - Prompt caching and reducing token usage
- **Outdated framings:** None stated.
- **Why it matters:** It shows the full surface area of one 2026 agent tool. Useful as a map of which concepts beginners will meet (hooks, permission modes, context cost).

## 7. roadmap.sh: AI Product Builder roadmap
- **Author:** roadmap.sh, built with Bit Cloud
- **Date:** 2026-07-13 (launch per changelog). Synced 2026-10-01.
- **URL:** https://roadmap.sh/ai-product-builder (topic text: github.com/kamranahmedse/developer-roadmap/tree/master/roadmaps/ai-product-builder)
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - The AI product creation cycle: prototyping, generation, refinement, collaboration, deployment
  - App anatomy (front end, back end, database, API), which you need in order to review what the AI generates
  - Browser DevTools are the first place to look when the front end breaks
  - Targeted change (edit the code with an agent) vs structural change (go back through the generation tool)
  - Unit, integration, e2e and user testing
  - Choosing hosting (Vercel, Railway, Render, Cloudflare, AWS/GCP/Azure); Supabase/Postgres/Mongo
- **Outdated framings:** Writing code from scratch is replaced by generating a working product, testing it with real users, and refining in cycles.
- **Observed gap:** None of its topic files covers security, secrets or authorization. (All files were grepped; the only hit is Supabase's "built-in authentication".)
- **Why it matters:** This is the newest roadmap written for exactly this course's audience, and it leaves out security entirely. That is concrete evidence for why the course must teach it.

## 8. Vibe Coding Best Practices: How To Get Consistent Results (roadmap.sh guide)
- **Author:** Ekene Eze
- **Date:** 2026-04-20 (datePublished; modified 2026-04-27)
- **URL:** https://roadmap.sh/vibe-coding/best-practices
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - Keep the context file lean (under about 50 lines)
  - Use /clear between features; check the summary after /compact; /rewind is not a substitute for /clear
  - Plan mode: list files, signatures, edge cases and assumptions before any code
  - Review every diff for deletions, public API changes, new dependencies, hard-coded credentials and schema changes
  - Run typecheck, tests and lint after every accepted change
  - Declare off-limits zones (auth, payments, middleware, migrations, .env)
  - Review all AI-generated access-control logic
  - Require a migration plan with up/down SQL and rollback
  - Turn a prompt you have run 3-4 times into a SKILL.md
- **Outdated framings:** None stated.
- **Why it matters:** A concrete per-change checklist. It includes a "security review pass" skill but does not say to verify that skill's output.

## 9. Agentic Engineering Patterns (living guide)
- **Author:** Simon Willison
- **Date:** 2026-02-23 (introduction post). Chapters are added and updated over time and show no individual dates.
- **URL:** https://simonwillison.net/guides/agentic-engineering-patterns/
- **Kind:** essay | **Credibility:** high
- **Gaps it names:**
  - How coding agents work: LLM + system prompt + tools in a loop; token caching; reasoning
  - Writing code is cheap, but good code is not. Good code: it works, you know it works, it solves the right problem, handles errors, is simple, tested, documented, changeable, and meets security and accessibility needs
  - Never assume generated code works until it has been run ("agentic manual testing" with python -c, curl, browser automation)
  - All tests can pass while the app crashes on startup or hides a key UI element
  - Red/green TDD; run the existing tests first
  - Linear walkthroughs and interactive explanations to understand code the agent wrote
  - Don't open PRs with code you haven't reviewed; show evidence of manual testing; agents write convincing PR descriptions, so check those too
  - Hoard things you know how to do
- **Outdated framings:** Code is expensive, so planning and estimates should conserve coding time. Skipping refactors, docs or tests to save an hour. One engineer works on one task at a time. Vibe coding (unreviewed, prototype-grade) is distinct from agentic engineering.
- **Why it matters:** A practitioner-written, continuously updated pattern list. Its definition of "good code" is a ready-made checklist for what the human still owns.

## 10. A field guide to Claude Fable 5: Finding your unknowns
- **Author:** Thariq Shihipar (Anthropic, member of technical staff)
- **Date:** 2026-07-06
- **URL:** https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
- **Kind:** essay | **Credibility:** high
- **Gaps it names:**
  - Known knowns, known unknowns, unknown knowns and unknown unknowns as the real limit on agent output
  - Run a "blind spot pass" before working in unfamiliar territory
  - Brainstorms from cheapest to most ambitious; throwaway prototypes (one HTML file with fake data)
  - Have the agent interview you, one question at a time, about architecture-changing ambiguities
  - Point at reference code instead of describing the behavior
  - Plans that lead with the decisions you are most likely to change (data model, interfaces, user flows)
  - Start a fresh session with spec, prototype and plan as artifacts
  - An implementation-notes file logging deviations, taking the conservative option at edge cases
  - Explainer plus quiz before merging; ask the model to teach you what "good" looks like in a field you don't know
- **Outdated framings:** Output quality is now limited by how clearly the user resolves unknowns, not by model capability. A complete spec written upfront gives way to iterative discovery through prototypes and interviews.
- **Why it matters:** It is a "hidden curriculum" in miniature: a method for finding what you don't know you don't know, written by the tool's maker. awesome-claude-code lists it first under "Start Here".

## 11. Best practices for Claude Code (official docs)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** undated living document. Fetched 2026-10-12; it refers to Claude Code v2.1.283, auto mode, /goal and /verify, so it is current.
- **URL:** https://code.claude.com/docs/en/best-practices
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Give the agent a check it can run (tests, build exit code, screenshot). Without one, you become the verification loop
  - Have the agent show evidence (test output, command and result, screenshot) instead of asserting success
  - Gate the stop with a /goal condition, a Stop hook, or a fresh-context verification subagent, so the worker isn't the grader
  - A reviewer asked to find gaps will find some even in sound work; chasing them all leads to over-engineering
  - The "trust-then-verify gap": plausible code that misses edge cases. If you can't verify it, don't ship it
  - The context window is the key resource and quality drops as it fills
  - CLAUDE.md is advisory; hooks are deterministic. An over-long CLAUDE.md gets ignored
  - Approval fatigue: after many prompts you click through instead of reviewing. Use allowlists, the sandbox, or auto mode's classifier
  - Checkpoints don't capture changes made through Bash, so they are no replacement for git
  - After two failed corrections, /clear and rewrite the prompt
  - Have the agent interview you, write SPEC.md, then implement in a fresh session
  - Failure patterns: kitchen-sink session, over-specified CLAUDE.md, infinite exploration
- **Outdated framings:** "You write code and ask Claude to review it" has flipped to "you describe what you want and Claude builds it". Manual approval of every action is giving way to auto mode, now the default starting mode, where a classifier blocks risky actions.
- **Why it matters:** The vendor's own statement of the course rule: the agent iterates on anything with a pass/fail signal, and what has no check falls back to the human.

## 12. Beyond permission prompts: making Claude Code more secure and autonomous
- **Author:** David Dworken and Oliver Weller-Davies (Anthropic Engineering)
- **Date:** 2025-10-20
- **URL:** https://www.anthropic.com/engineering/claude-code-sandboxing
- **Kind:** docs | **Credibility:** high (just under 12 months old; foundational and still current)
- **Gaps it names:**
  - Approval fatigue: frequent prompts make users stop scrutinizing what they approve
  - You need both filesystem isolation and network isolation; either alone fails
  - Prompt injection leading to exfiltration of SSH keys
  - The sandbox's purpose: contain an injection that has already succeeded
  - In cloud sessions, credentials stay outside the sandbox and are checked by a proxy
- **Outdated framings:** "Permission prompts are the safety mechanism" is replaced by predefined boundaries (the post reports 84% fewer prompts).
- **Why it matters:** It explains the mental model behind sandboxes and why clicking "allow" is not a security control.

## 13. OWASP Top 10 for LLM Applications 2026 (CSA research note)
- **Author:** Cloud Security Alliance AI Safety Initiative, summarizing the OWASP GenAI Security Project
- **Date:** 2026-08-15 (note). The OWASP list itself was released 2026-08-03.
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-llm-top10-2026-incident-weighted-202/
- **Kind:** framework | **Credibility:** high
- **Gaps it names:**
  - Prompt injection (#1 for three years), now including cross-modal attacks and memory persistence
  - Sensitive information disclosure
  - Excessive agency (rose from #6 to #3): scope agent permissions tightly
  - Unbounded consumption (rose from #10 to #6): cost and availability blowups when one request fans out into many tool or subagent calls
  - Improper output handling: generated code can still cause XSS or RCE
  - Hidden context exposure
  - Supply chain, now including model weights
  - Require a human or independently verified checkpoint before purchases, deployments or account changes
  - Design so that a fooled model breaks nothing important (blast radius)
  - The "defense effect": few incidents does not mean low risk
- **Outdated framings:** "System Prompt Leakage" was renamed "Hidden Context Exposure". Rankings are now weighted about 25% on real incident data (6,639 classified incidents).
- **Why it matters:** The standard list of what goes wrong when you ship an AI feature. Anyone who adds an LLM to an app inherits these risks.

## 14. vibe-coding-security: pre-launch checklist for AI-generated apps
- **Author:** boxed-dev (GitHub)
- **Date:** 2026-08-09 (latest commit, "Aug 2026 refresh: 65 -> 69 checks"). Repo created 2026-05-01.
- **URL:** https://github.com/boxed-dev/vibe-coding-security
- **Kind:** list | **Credibility:** medium (small repo, 15 stars; sells a $10 kit; corrected its stats to primary sources in its commit history)
- **Gaps it names:**
  - RLS must block the anon role without an explicit policy; grep for service_role
  - Audit every NEXT_PUBLIC_ variable; OpenAI/Anthropic/xAI keys never in frontend code
  - IDOR test: change a record ID in the request
  - Rate limits: expect HTTP 429 at about 100 requests/minute
  - Webhook HMAC, mass assignment, SSRF, CORS
  - Prompt-injection boundaries; no secrets in system prompts; per-user token and cost caps (denial-of-wallet)
  - Slopsquatting (packages with hallucinated names)
  - Backups the agent can't reach; human approval for destructive actions; separate dev and prod credentials; scoped cloud tokens
  - Named incidents: CVE-2025-48757 (Lovable RLS, 170+ apps; severity disputed), Moltbook (1.5M API tokens, Feb 2026)
- **Outdated framings:** None stated.
- **Why it matters:** The most current itemized list covering both app security and agent supply-chain security in one place.

## 15. You're Doing Vibe-Coding Wrong. Here's the 17-Point Fix.
- **Author:** Chizee (DEV Community)
- **Date:** 2026-09-20 (edited 2026-09-23, per the dev.to API)
- **URL:** https://dev.to/chizee/youre-doing-vibe-coding-wrong-heres-the-17-point-fix-e9h
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - Server-side auth on admin routes (a hidden link is not protection)
  - Authorization on the server, because the browser can be edited
  - Force RLS and verify as anon
  - Email verification
  - Password hashing (bcrypt/scrypt/Argon2, never SHA-256 or MD5)
  - Session tokens in httpOnly cookies, not localStorage
  - Client-side validation is UX, not security
  - File-upload validation; webhook signature checks
  - Rate-limit anything that sends email or costs money
  - No wildcard CORS with credentials
  - Disable debug endpoints, GraphQL introspection and source maps
  - `git check-ignore .env`; keep secrets out of logs
  - Anthropic's security-review Action is not hardened against prompt injection: run it only on trusted PRs
- **Outdated framings:** None stated. It flags several popular statistics as disputed or sample-limited.
- **Why it matters:** A recent, specific list that even warns that the AI security reviewer can itself be attacked. That reinforces the rule that an AI's "safe" verdict is not the last word.

## 16. The Hidden Cost of Vibe Coding: What Junior Developers Stop Learning
- **Author:** Nate Swanner (Dice)
- **Date:** 2026-09-23
- **URL:** https://www.dice.com/career-advice/the-hidden-cost-of-vibe-coding-what-junior-developers-stop-learning
- **Kind:** essay | **Credibility:** medium
- **Gaps it names:**
  - "Being stuck was the curriculum": productive struggle disappears
  - Reading unfamiliar code; architectural reasoning
  - Checking code against what was actually intended. Code can pass every test and still miss the requirement
  - Knowing how code fails (e.g. when a call times out)
  - Asking colleagues for help, which is declining
  - Require developers to explain assumptions, edge cases and failure behavior before approval
  - Keep a log of when the AI was wrong and how it was caught
- **Outdated framings:** Syntax mastery is the least endangered skill. AI has become the developer's mentor in place of colleagues.
- **Why it matters:** It names the knowledge AI hides, which is this course's premise. Caution: its call to preserve hand-debugging conflicts with the course rule. The durable part is checking against intent, which the AI cannot verify.

## 17. Building an AI Coding Agent: 6 Lessons From Real Development
- **Author:** Synfinity Dynamics Pvt Ltd (DEV Community)
- **Date:** 2026-09-29 (dev.to API)
- **URL:** https://dev.to/synfinity-dynamics-pvt-ltd/building-an-ai-coding-agent-6-lessons-from-real-development-46jo
- **Kind:** essay | **Credibility:** medium
- **Gaps it names:**
  - A coding agent is a tiny loop (about 40 lines): propose, run, feed back
  - Better tools beat a better prompt; error messages that help the agent recover
  - Context fills with file reads and command output, so truncate and summarize
  - The agent rewrote a whole file and deleted code it didn't understand; fix with targeted edits, a branch, and commits before and after each task
  - Without tests, the agent reports success on broken code
  - Get approval before deleting files, running unfamiliar commands or pushing
- **Outdated framings:** "Gains come from tuning the system prompt" is replaced by "gains come from better tools".
- **Why it matters:** A builder's view of why agents misbehave. It explains from the inside why tests and git are the human's safety net.

## 18. Blog #4: My First Ever Agent and Things That I Wish I Knew Before Building This
- **Author:** Aeron (DEV Community)
- **Date:** 2026-09-17 (dev.to API)
- **URL:** https://dev.to/aeronn_11/blog-4-my-first-ever-agent-and-things-that-i-wish-i-knew-before-building-this-18jl
- **Kind:** essay | **Credibility:** low (small personal post; included for recency)
- **Gaps it names:**
  - Evals won't pass 100% consistently, because LLM output varies; change one thing at a time
  - Token cost of A/B-testing evals: set caps and rerun only the eval you are fixing
  - A chunker overfit to one document broke on multi-document ingestion
- **Outdated framings:** None stated.
- **Why it matters:** Fresh evidence that non-determinism and token cost surprise first-time agent builders.

## 19. What we wish we knew about building AI agents
- **Author:** Ian Vanagas (PostHog)
- **Date:** 2026-03-24
- **URL:** https://newsletter.posthog.com/p/what-we-wish-we-knew-before-building
- **Kind:** essay | **Credibility:** high
- **Gaps it names:**
  - Consider an MCP server, a single LLM call, or a hardcoded workflow before building an agent
  - Your harness is not your moat; use an existing SDK
  - Coordinator-plus-subagents setups became a black box that lost context
  - A capability exists only if you write a tool for it (they ended up with 44 hand-written tools)
  - Observability and evals from day one; manual "traces hours" reviewing real interactions
  - Users' complaints: inconsistent results, vague errors, unclear capabilities, no signals of uncertainty or progress
- **Outdated framings:** Building a custom harness. "More capabilities matters more than solving users' problems."
- **Why it matters:** A hard-won lesson list from a real product team, for the audience members who build agent features.

## 20. AI Tooling for Software Engineers in 2026
- **Author:** Gergely Orosz and Elin Nilsson (The Pragmatic Engineer)
- **Date:** 2026-03-03 (survey of about 906 respondents, 2026-01-27 to 2026-02-17)
- **URL:** https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- **Kind:** survey | **Credibility:** high (self-selected subscriber sample)
- **Gaps it names:**
  - 95% use AI weekly; 55% regularly use agents
  - Most engineers use 2-4 tools; Claude Code is the most-used tool
  - Nearly all AI code is still reviewed and refined by humans; common setup is a terminal agent plus an IDE for review
  - A company's default model may be a worse experience than one you choose
- **Outdated framings:** 18 months earlier, AI meant code generation and tab completion. That is now the past.
- **Why it matters:** A baseline for what "normal" use looks like in 2026.

## 21. The impact of AI on software engineers in 2026: key trends, Part 1
- **Author:** Gergely Orosz and Elin Nilsson (The Pragmatic Engineer)
- **Date:** 2026-04-14
- **URL:** https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026
- **Kind:** survey | **Credibility:** high (free portion read)
- **Gaps it names:**
  - Usage limits (about 30% have hit them) and costs ($100-200/month per engineer for top plans)
  - Vendor lock-in from subsidized plans
  - "AI slop" review burden falls on colleagues
  - Fast shippers add tech debt and may build the wrong things
  - Knowing which model fits which task (cheap vs premium)
- **Outdated framings:** Typing code is no longer the bottleneck; the focus moves from how to build to what to build.
- **Why it matters:** Cost, limits and review burden are practical gaps no tutorial mentions.

## 22. awesome-claude-code
- **Author:** hesreallyhim and contributors (GitHub, about 55k stars)
- **Date:** 2026-10-12 (latest commit; repo created 2025-04-19)
- **URL:** https://github.com/hesreallyhim/awesome-claude-code
- **Kind:** list | **Credibility:** medium (curated directory; each tool has its own license and must be evaluated)
- **Gaps it names:**
  - The ecosystem map: skills, hooks, status lines, orchestration loops ("Ralph Wiggum"), memory and context persistence, observability and cost
  - Security tooling: secret-leak guardrails, devcontainers and microVMs for bypass mode, safety-net hooks that catch destructive git and filesystem commands, credential gateways so agents never see keys
  - "Start Here" picks: the Fable field guide, CLAUDE.md craft (instruction budget, progressive disclosure), and building a minimal agent in a few hundred lines
- **Outdated framings:** None stated.
- **Why it matters:** It shows what practitioners are actually building around agents right now. Its Security section is effectively a list of the failures people have had (several entries were "born from a real incident").

## 23. Encyclopedia of Agentic Coding Patterns
- **Author:** Wolf McNally (per awesome-claude-code); site credits Bartley Editions / Bartley Labs
- **Date:** 2026-08 (HTTP Last-Modified 2026-08-31; no date on the page)
- **URL:** https://aipatternbook.com
- **Kind:** list | **Credibility:** medium
- **Gaps it names:**
  - Foundations: product judgment, acceptance criteria, source of truth
  - Security and trust: trust boundary, least privilege, blast radius, tool poisoning, agent trap, adversarial cloaking (sites serving different content to agents), RAG poisoning, agentic payments, action-selector
  - Smells: AI smell (output tuned for plausibility over understanding), jagged frontier, benchmark mirage, load-bearing code, pinning, footgun
  - Governance: approval policy, bounded autonomy, eval, agent sprawl
- **Outdated framings:** It describes its entries as "best current practice", expected to change.
- **Why it matters:** The broadest single vocabulary list (314 articles) for naming concepts beginners lack, useful as a checklist of candidate lesson topics.

## 24. Vibe Coding for Non-Developers: 63% of Users Now Have No Coding Background, Breaches Follow
- **Author:** Richard L. Wells (Tech Times)
- **Date:** 2026-05-24
- **URL:** https://www.techtimes.com/articles/317077/20260524/vibe-coding-non-developers-63-users-now-have-no-coding-background-breaches-follow.htm
- **Kind:** report | **Credibility:** medium (several statistics are secondary or vendor-linked)
- **Gaps it names:**
  - Moltbook (Feb 2026): RLS never enabled; 1.5M API tokens and 35k emails exposed, found by Wiz 3 days after launch
  - A Lovable BOLA flaw stayed open 48 days after a bug-bounty report was closed
  - Stanford RCT: developers using AI wrote less secure code but were more confident in it
  - Non-developers lack a baseline for calibrating how much to trust AI security
  - Scope: personal tools and prototypes are fine; health data, payments and regulated apps need professional review
- **Outdated framings:** None stated.
- **Why it matters:** It ties the exact pitfall in the course rule (believing the agent's "it's safe") to a named incident and a controlled study.

## 25. Vibe Coding Best Practices [2026]: 7 That Work, 3 That Fail
- **Author:** Kunal Ganglani
- **Date:** 2026-06-20 (updated 2026-09-16)
- **URL:** https://www.kunalganglani.com/blog/vibe-coding-best-practices-2026
- **Kind:** list | **Credibility:** medium (practices are first-hand; statistics are second-hand)
- **Gaps it names:**
  - Prime context before each session; build iteratively instead of generating the whole app in one shot
  - Aggressive diff review
  - Put security constraints in persistent config
  - Checkpoint commits
  - AI-written tests can be "dangerously circular"; let the spec drive the tests
  - Know when to stop: switch to manual work when the AI loops (the author codes manually about 30% of the time)
  - Prompting features in isolation produced three separate auth systems; reference an architecture decision record in prompts
- **Outdated framings:** One-shot app generation works for demos but not for maintained code.
- **Why it matters:** Recent, concrete failure stories (circular tests, duplicate auth systems) that show what the human must still catch.

---

### Fetched but left out of the 25 (for the next sweep)
- OpenSSF, Security-Focused Guide for AI Code Assistant Instructions (2025-08-01), https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions.html. Foundational: slopsquatting (19.7% of proposed packages did not exist); persona prompts ("act as a security expert") performed worse; the developer is fully responsible.
- HumanLayer, Writing a Good CLAUDE.md (2025-11-25), https://www.humanlayer.dev/blog/writing-a-good-claude-md. The model is stateless; instruction budget of about 150-200; CLAUDE.md may be ignored as "not relevant".
- The Vibe Coder's Pre-Launch Security Checklist (Hack Safe, 2026-06-11), https://dev.to/hacksafe/the-vibe-coders-pre-launch-security-checklist-25-checks-for-cursor-lovable-bolt-replit-apps-12i. Only 10 of its 25 items are detailed; it recommends AI audit prompts with no verification step.
- Lenny's Newsletter, How to build AI product sense (Tal Raviv and Aman Khan, 2026-02-03), https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense. Mostly paywalled; learn by using coding agents instead of chat UIs; tool calling is its own skill.
- Supabase, The Vibe Coding Master Checklist (2025-08-16), https://supabase.com/blog/the-vibe-coding-master-checklist. Over 12 months old and vendor-promotional.

### Not reached (web-search budget ran out mid-sweep)
Every (compound engineering), Latent Space, Addy Osmani's 2026 essays, Karpathy's agentic-engineering post (The New Stack page returned no body), the Reddit r/vibecoding top posts (Reddit can't be fetched), and the Forbes "What Nobody Tells You About Vibe Coding" piece (HTTP 403). A follow-up sweep should cover these.
