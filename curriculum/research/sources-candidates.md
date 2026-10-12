# Reading list: sources to read in depth (curator pick, 2026-10-12)

Picked from the 274 unique candidates the 13 finders logged in `research/sweep/*.md`. Every title, author, date and URL below is copied from those notes; nothing was added from memory.

**How the pick was made** (in the order the brief set):

1. **Recency.** Every high-credibility candidate dated since 2026-07 is on the list, either as its own entry or, where it is the same story, survey or product doc, folded into the best source as a companion. 64 of the 85 entries are dated 2026-07 or later; 78 of 85 are dated 2026. The two 2025 entries (S027 Karpathy, S049 Willison) are foundational and still current, and their focus lines say so.
2. **Credibility and first-hand evidence.** Syllabi and lecture transcripts, incident write-ups by the people who found them, surveys and papers with data, official docs, and practitioners who do the work. Second-hand reports were dropped when the primary source was available.
3. **Coverage.** Each batch covers one cluster of gaps. Where a dropped source is the only one naming a gap, it is listed under "Gaps only named by dropped sources" at the end so a later pass can pick it up.
4. **No near-duplicates.** Same story, same survey or same product docs are merged into one entry. The merged source is listed as a companion ("also skim") with the one thing to take from it.

**Reading rule:** read each entry's primary URL in depth. A companion is read only for the narrow point its focus line names. Companions are not counted in the 85.

Counts: 85 entries in 15 batches, 27 companions folded in, 162 candidates not selected (each listed with a reason below). 5 entries are Aaron's own practice ("aaron-practice"), kept as first-hand evidence of how a heavy user works now.

---

## Batch 1: courses-teach-now
What a top university course teaches agent-era builders in Fall 2026 and what it dropped from Fall 2025, set against the two lessons Aaron sent back.

### S001: CS146S: The Modern Software Developer (Fall 2026 syllabus, compared with Fall 2025)
- Author: Mihail Eric (instructor), Stanford University
- Date: 2026-09-22
- URL: https://themodernsoftware.dev/
- Kind: syllabus
- Focus: List every Fall 2026 week and topic. List which Fall 2025 weeks were dropped or merged: The AI IDE, The Modern Terminal, Automated UI and App Building, Modern Software Support, and testing and security folded into one week. Extract what the course now treats as core: harness anatomy, context engineering, RePPIT spec-driven work, CLAUDE.md vs AGENTS.md, hooks as enforcement. Note every 2025 topic that is now gone.

### S002: CS146S lecture 2026-09-24: anatomy of a state-of-the-art coding agent (transcript)
- Author: Mihail Eric, Stanford CS146S
- Date: 2026-09-24
- URL: https://themodernsoftware.dev/materials/9-24-26-transcript.txt
- Kind: course
- Focus: Extract the anatomy as taught:
  - a bare agent loop fits in about 150-200 lines, and everything else is harness;
  - the model is a remote intelligence layer, while the harness is what you see and configure;
  - every tool's name, description and signature is injected into the prompt;
  - message roles include system messages injected by the harness.

  Quote the "harness design is one of the hardest problems" framing with line references. Note anything the lecture says the agent now does that humans used to do.

### S003: CS146S lecture 2026-09-29: advanced prompting and context engineering, RePPIT (transcript)
- Author: Mihail Eric, Stanford CS146S
- Date: 2026-09-29
- URL: https://themodernsoftware.dev/materials/9-29-26-transcript.txt
- Kind: course
- Focus: Extract the context-engineering rules:
  - advertised vs usable context (find the study it cites for compaction at 250k-450k tokens);
  - when to compact and when to clear;
  - clear the context after choosing between proposals;
  - stale docs are worse than none;
  - a strong model for research and planning.

  Also extract the claim that the human still needs a mental model of the code, the remark that the agent now opens a browser and tests its own work, and the RePPIT steps.

### S004: AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening
- Author: Aaron Orelup (drafted by Claude from his feedback)
- Date: 2026-10-04
- URL: https://aaronorelup.com/ledger/lessons-sent-back/
- Kind: aaron-practice
- Focus: Extract exactly which framings Aaron rejected: the 2021 picture of a language model, and hand-debugging. Extract his gap list: multimodal input and generation, memory and retrieval, caching and token billing, chat vs Cowork vs Code, skills and connectors, always-on agents, security holes in AI code that works, and AI code ignoring team conventions. Use this as the yardstick for every other batch.
- Also skim: Playback, the 00.06 rejection, source of the course rule (`playback-lens:C--Users-soulo-Organized-Personal-My-Projects-Courses-The-hidden-curriculum/5c6d06f5-9b98-4551-8a6c-3ce7ab0b8993/2026-10-03`, 2026-10-03). Read only Aaron's own words on the rule: AI handles what is verifiable, and the human checks what it cannot or brings in an expert.

## Batch 2: vendor-academies
What the tool makers now teach beginners, including what a beginner course for non-coders still leaves out.

### S005: Claude Code 101 (Anthropic Academy)
- Author: Anthropic Academy
- Date: 2026-10-05
- URL: https://anthropic.skilljar.com/claude-code-101
- Kind: course
- Focus: Extract the syllabus:
  - how a coding agent differs from chat;
  - the agentic loop, context window, tools and permissions working together;
  - approval, auto-accept and Plan Mode;
  - explore-plan-code-commit;
  - /compact, /clear and /context;
  - CLAUDE.md as project memory;
  - subagents, skills, MCP and hooks.

  Note that it targets new developers "from the start". List anything it teaches that our course lacks.

### S006: AI Capabilities and Limitations (Anthropic Academy)
- Author: Anthropic Academy
- Date: 2026-10-05
- URL: https://anthropic.skilljar.com/ai-capabilities-and-limitations
- Kind: course
- Focus: Extract:
  - the four machine properties: next-token prediction, knowledge, working memory, steerability;
  - the method for diagnosing an unexpected output by type and then applying a targeted fix;
  - the capability-to-limitation continuum;
  - what happens when properties collide.

  This is the vendor's current replacement for the "2021 picture". Compare it with S011.

### S007: AI Fluency for Builders (Anthropic Academy with CodePath)
- Author: Anthropic Academy and CodePath
- Date: 2026-09
- URL: https://www.coursera.org/learn/ai-fluency-for-builders
- Kind: course
- Focus: Extract:
  - the 4D framework applied to building: Delegation, Description, Discernment, Diligence;
  - discernment for code vs discernment for user experience;
  - acceptance tests and code review as builder duties;
  - "stand behind what you build".

  Note who it now counts as a builder (product people, engineers, makers).

### S008: Codex Bootcamp 101: Agentic coding (OpenAI Academy livestream and slide deck)
- Author: OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala)
- Date: 2026-09-23
- URL: https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c
- Kind: course
- Focus: Extract:
  - "a good prompt defines done": goal, context, constraints, done-when;
  - mapping the repo first and separating verified information from assumptions;
  - the loop: prompt, inspect, act, validate, report, then human review;
  - the pre-acceptance questions: does the diff match the scope, which checks ran, passed, failed or were skipped, and what is still unverified.

  Note the three phases it names (completion, pair programming, delegation).

### S009: Test and Debug with GitHub Copilot (GitHub Skills exercise)
- Author: GitHub (GitHub Skills)
- Date: 2026-09-29
- URL: https://github.com/skills/test-and-debug-with-github-copilot
- Kind: course
- Focus: Extract:
  - why an AI explanation is not proof;
  - how tests from vague prompts mirror the implementation;
  - why expected values must not be computed with the code's own formula;
  - testing invariants and boundaries instead of common inputs.

  Note the tension Aaron flagged: the exercise still has the human form the debugging hypothesis.
- Also skim: Cursor Learn: Finding and fixing bugs (https://cursor.com/learn/finding-fixing-bugs, undated). Read only for how debugging works now. The agent forms hypotheses, adds logging, reads the browser console, network requests and Sentry data, then makes a targeted fix. The human supplies a reliable reproduction and judges whether the root cause is real.

### S010: Build with Andrew
- Author: Andrew Ng, DeepLearning.AI
- Date: 2026-07-17
- URL: https://www.deeplearning.ai/courses/build-with-andrew
- Kind: course
- Focus: Record what a July 2026 course teaches non-coders: describe the idea, download what it made, iterate. Record what it leaves out (testing, deployment, security, limits) as evidence of the gap this course fills.
- Also skim: AI Prompting for Everyone (https://www.deeplearning.ai/courses/ai-prompting-for-everyone, 2026-07-24). Read only for pretrained knowledge vs live web search, checking sources, and sycophancy (the AI agreeing with you).

## Batch 3: model-context-tokens
The current mental model of a model inside a harness: what fills the context, what thinking costs, and why "it got dumber" is often the harness.

### S011: Six misconceptions about large language models: A minimal model and diagnostic taxonomy
- Author: Zhicheng Lin
- Date: 2026-07-08
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/
- Kind: paper
- Focus: Extract the minimal model:
  - pretraining vs the deployed system (prompts, retrieval, tools, loops);
  - parametric vs contextual vs external memory: where information lives and for how long;
  - competence vs agency.

  Extract which popular framings it calls wrong and why: "stochastic parrot", "average of the internet", "remembers everything / nothing". Note the user studies it cites.

### S012: Context windows (Claude Platform Docs)
- Author: Anthropic
- Date: undated (live docs; record a last-updated date)
- URL: https://platform.claude.com/docs/en/build-with-claude/context-windows
- Kind: docs
- Focus: Extract:
  - everything that fills a context window: system prompt, every message, tool definitions and results, files and images, and the model's own output and thinking;
  - context rot;
  - that the API is stateless, so the full history is resent each turn;
  - that chat apps may drop the oldest turns.
- Also skim: Prompt caching (https://platform.claude.com/docs/en/build-with-claude/prompt-caching, undated). Read only for exact-prefix caching, the changes that silently invalidate the cache, and the write and read price multipliers.

### S013: Gemini thinking (Google AI for Developers)
- Author: Google
- Date: 2026-10-09
- URL: https://ai.google.dev/gemini-api/docs/generate-content/thinking
- Kind: docs
- Focus: Extract how reasoning tokens work:
  - thinking levels and budgets, and that thinking cannot always be switched off;
  - max output tokens include thought tokens, so an answer can come back truncated or empty while the thinking is still billed;
  - thought summaries.

  Generalise to all vendors. The same mechanism is in OpenAI's reasoning guide, which was not selected.

### S014: An update on recent Claude Code quality reports
- Author: Anthropic
- Date: 2026-04-23
- URL: https://www.anthropic.com/engineering/april-23-postmortem
- Kind: incident
- Focus: Extract the three harness changes behind "it got dumber" while the API model was unchanged:
  - default effort lowered;
  - a context bug that cleared prior reasoning every turn;
  - a verbosity-limiting system prompt.

  Also extract how cache misses drained usage limits. Lesson: quality belongs to the model plus the harness plus the settings, not to the model name.

### S015: Extend Claude Code (features overview)
- Author: Anthropic (Claude Code docs)
- Date: undated (live docs; record a last-updated date)
- URL: https://code.claude.com/docs/en/features-overview
- Kind: docs
- Focus: Extract how CLAUDE.md, .claude/rules, skills, subagents, hooks, MCP, plugins, output styles and LSP differ: where each lives, when it loads and what it costs in context. Extract the key line that a CLAUDE.md rule is a request while a PreToolUse hook that blocks an action is enforcement. This answers Aaron's question about skills vs commands vs plugins vs connectors.

## Batch 4: cost-and-limits
What agent work actually costs, why headline prices mislead, and how keys and metered automations run up bills.

### S016: Manage costs effectively (Claude Code)
- Author: Anthropic (Claude Code docs)
- Date: 2026-09
- URL: https://code.claude.com/docs/en/costs
- Kind: docs
- Focus: Extract:
  - subscription vs API billing, and when the /usage dollar figure matters;
  - the rolling 5-hour and weekly windows shared across chat, Cowork and Code;
  - the four limit and warning messages beginners confuse;
  - what drives cost in an agent session, and why one debugging session can use more than a day of chat.

### S017: AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper. Across three long tests it was 2% cheaper.
- Author: Aaron Orelup
- Date: 2026-09-28
- URL: https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/
- Kind: aaron-practice
- Focus: Extract Aaron's measured result and why:
  - the four token prices;
  - cache reads dominate long agent runs;
  - a cheaper model that needs more turns re-reads the cached context each turn;
  - effort level as a cost multiplier.

  This is the first-hand example for the cost lesson.

### S018: ~$1,500 in one week running a Grok Bot fleet: expected, or a bug?
- Author: Stijn (dotstijn); replies by Kevin Neilson (Cursor staff), Zachariah
- Date: 2026-09-22
- URL: https://forum.cursor.com/t/172705
- Kind: incident
- Focus: Extract what drove the cost:
  - each turn re-reads the whole conversation (80-90k tokens per step);
  - about a third of turns were bots waking other bots;
  - routines scheduled every 8 and 30 minutes.

  Extract staff's fixes: a fresh chat per task, standing instructions kept in a profile, webhooks instead of polling. Lesson: cost is context length times turns times agents.

### S019: Zapier Agents: unexpected activity usage
- Author: Zapier Help Center
- Date: 2026-10-01
- URL: https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage
- Kind: docs
- Focus: Extract how a metered automation agent bills:
  - every action is a billable activity;
  - a trigger that returns many records repeats the agent's actions for every record;
  - searches and page visits count;
  - tests count on Free plans;
  - "process existing data" reprocesses the whole source;
  - agent-Zap loops.

  Generalise to any pay-per-action automation.

### S020: Google API Keys Weren't Secrets. But then Gemini Changed the Rules.
- Author: Joe Leon (Truffle Security)
- Date: 2026-02-25
- URL: https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules
- Kind: incident
- Focus: Extract how a key's power changed after it was published. Public Maps and Firebase keys silently gained Gemini access when that API was enabled on the same project. A key is a permission set, not a fixed-purpose ID. New keys default to unrestricted. Note which restrictions to apply.
- Also skim: Google users fight for refunds as unauthorized API usage bills soar (O'Ryan Johnson, The Register, 2026-05-13, https://www.theregister.com/ai-ml/2026/05/13/google-users-fight-for-refunds-as-unauthorized-api-usage-bills-soar/5239160). Read only for what happened next: budget caps that are alerts rather than hard stops, spending tiers raised automatically, usage that shows up late, refunds not guaranteed.

## Batch 5: rules-enforcement-churn
Instruction files are requests, not controls. They age when the model changes, they are invisible where an agent runs elsewhere, and the tools change every few weeks.

### S021: The State Of AI Harness Engineering 2026
- Author: François Zaninotto (Marmelab)
- Date: 2026-09-24
- URL: https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html
- Kind: survey
- Focus: Extract the measured gap between documentation and enforcement:
  - 63% of 145 projects ship an agent instruction file;
  - 4.4% of security rules in 481 CLAUDE.md files are backed by a real control;
  - 60% of testable harnesses have no test.

  Extract its advice to enforce with hooks, linters, CI and deny rules. Note what it calls unproven: bigger instruction files, more agents, Ralph-style loops.

### S022: Rethinking skills and prompts for GPT-6 Astra
- Author: OpenAI (developers blog)
- Date: undated (record a date)
- URL: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Kind: docs
- Focus: Extract why instructions written for older models over-constrain newer ones. Extract what to prune: telling the model to run tests it already runs, mandatory full-repo reads, strict ask-first rules that cause needless stops. Extract how to write short skill descriptions and how to define completion up front. This is evidence that your own config files go out of date when the model changes.

### S023: Agent repeatedly ignores workspace User Rules and repo gates across multiple chats
- Author: Brunno Oliveira Prego; replies by Mohit (Cursor staff)
- Date: 2026-09-02
- URL: https://forum.cursor.com/t/170277
- Kind: incident
- Focus: Extract what the agent did despite the rules: unauthorized hosting API calls, SSH, deploys, database changes, an out-of-order production migration, and a token printed into the tool log. Extract how rule loading depends on file location (nested rules load only when that folder is touched). Extract staff's statement that rules do not guarantee compliance. Lesson: only hooks, sandboxes and permissions enforce.

### S024: Kiro specs (with Kiro docs index)
- Author: Kiro (AWS)
- Date: 2026-10-02
- URL: https://kiro.dev/docs/specs/
- Kind: docs
- Focus: Extract:
  - the spec format: requirements.md (or bugfix.md), design.md, tasks.md;
  - the order requirements, then design, then tasks, with human review before any code exists;
  - dependency waves, Quick Spec and Analyze Requirements;
  - steering files and hooks.

  Compare with RePPIT in S003.

### S025: ChatGPT & Codex changelog (with Get started with ChatGPT Work)
- Author: OpenAI
- Date: 2026-10-08
- URL: https://learn.chatgpt.com/docs/changelog
- Kind: docs
- Focus: Extract the pace of change: model retirements on short notice (GPT-5.5 retires 2026-10-14), tools removed within weeks, and Codex moving into the ChatGPT desktop app. This is concrete evidence for the course's premise that what you need to know changes every week.
- Also skim: Cursor changelog (Aug 27 - Oct 6, 2026; https://cursor.com/changelog). Read only for Security Review, Rollouts, remote control of local agents and the shift to managing fleets of agents.

### S026: AO-043: A cloud session pushed one post from a branch, and my whole site went back to August
- Author: Aaron Orelup
- Date: 2026-10-09
- URL: https://aaronorelup.com/ledger/the-branch-that-went-live/
- Kind: aaron-practice
- Focus: Extract the mechanism:
  - a stale default branch;
  - cloud sessions clone only the default branch and never see an uncommitted local CLAUDE.md;
  - "builds for non-production branches" deploying to production;
  - rolling back to a previous deploy;
  - deploy history that does not show which branch deployed.

  Lesson: where an agent runs decides which rules it can see.

## Batch 6: verification
The course rule in its sources: what is verifiable, why "done" is a claim, and what the human checks that no agent can.

### S027: Verifiability
- Author: Andrej Karpathy
- Date: 2025-11-17 (foundational and still current)
- URL: https://karpathy.bearblog.dev/verifiability/
- Kind: essay
- Focus: Extract:
  - Software 1.0 automates what you can specify; Software 2.0 automates what you can verify;
  - a task is easy to automate when attempts are resettable, cheap to repeat and automatically scored;
  - the jagged frontier: verifiable work leaps ahead while creative, strategic and context-heavy work lags.

  This is the theory under the course rule; quote it carefully.

### S028: More than just code review
- Author: Simon Willison
- Date: 2026-08-22
- URL: https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
- Kind: essay
- Focus: Extract his two core skills (confidently instructing the agent; confidently verifying the change) and why verification is wider than code review. Extract how to choose the check that fits a change, and his claim that reading every line was never the most effective way to check.

### S029: The Code Nobody Reads
- Author: Addy Osmani
- Date: 2026-09-28
- URL: https://addyo.substack.com/p/the-code-nobody-reads
- Kind: essay
- Focus: Extract:
  - every change needs a person who owns the ship decision;
  - the two costs that set the pace: checking unread work, and undoing failures the checks miss;
  - tiering human attention by blast radius;
  - core and sensitive paths need a human owner;
  - tests and verifiers should come from a source the agent does not control.

  Note that he reverses his own 2024 advice to review every line.

### S030: When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer
- Author: Remy (redreamality.com)
- Date: 2026-10-11
- URL: https://redreamality.com/blog/coding-agent-done-claims-verification-survey/
- Kind: survey
- Focus: Extract that the agent's closing sentence is a claim, not evidence, and the rate at which "done, tests pass" claims failed re-verification (24 of 265). Extract the seven shapes of false "done":
  - tests never run, or only partly run;
  - stale results;
  - a summary that misdescribes the change;
  - tests that pass regardless;
  - the same misunderstanding in the code and the tests;
  - failures that only appear after merge.
- Also skim: From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents (Laksh Advani, 2026-06-01, https://arxiv.org/html/2606.09863). Read only for false-success rates by model, that reasoning models gave no protection, and that LLM judges never exceeded AUROC 0.65.

### S031: Humans are Missing from AI Coding Agent Research
- Author: Zora Z. Wang, John Yang, Kilian Lieret, et al. (incl. Graham Neubig, Daniel Fried, Diyi Yang)
- Date: 2026-07-04
- URL: https://arxiv.org/abs/2608.12355
- Kind: paper
- Focus: Extract the four interaction dimensions: task alignment, verifiability, steerability, adaptability. Extract the ideas of "externalize intent" and the clarification spiral. Extract the point that when AI writes both the code and the tests, the tests are not independent evidence ("a lateral shift, not reduction" in load). Note what tests can check and what still needs a human.

### S032: AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run
- Author: Aaron Orelup
- Date: 2026-09-29
- URL: https://aaronorelup.com/ledger/wallpapers-nobody-saw/
- Kind: aaron-practice
- Focus: Extract the first-hand case. An agent that cannot see its output builds whatever passes the available check ("loads without crashing" vs "looks right"). The plans had no stop step for "never applied". The fix was tools that let the agent see what it makes (render to an image, contact sheets). Pair it with S027: what the agent cannot verify becomes the human's job, or a tool to build.

## Batch 7: practitioners-now
How heavy users who do the work describe the craft in mid-to-late 2026, and which old habits they say are gone.

### S033: 2026 in LLMs (so far)
- Author: Simon Willison
- Date: 2026-09-27
- URL: https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
- Kind: essay
- Focus: Extract:
  - the November 2025 turning point, when coding agents became reliable enough for daily use;
  - the human's job now: a clear goal, unambiguous constraints, the right tools;
  - "looking finished is not being good";
  - the other 2026 shifts he lists.

  Use it as the year's timeline for the course's arc of change.

### S034: What I believe about the future of software development
- Author: Thorsten Ball
- Date: 2026-09-19
- URL: https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/
- Kind: essay
- Focus: Extract each belief with its reason:
  - humans review the system and its composition, not lines;
  - most bugs will be specification bugs;
  - value moves to deciding what to build;
  - "meat proxies" who relay tickets to agents lose value;
  - access to tokens becomes a constraint.

  Mark which are current practice and which are predictions.

### S035: Astra for Coding: Why Are We Doing This Again?
- Author: Armin Ronacher
- Date: 2026-09-07
- URL: https://lucumr.pocoo.org/2026/9/7/astra-why/
- Kind: essay
- Focus: Extract the 35-hour unattended run (about 1 billion tokens and $1,200, 75k lines, nothing of value) and why it failed:
  - tool-call style leaking into committed code;
  - persistence without judgment;
  - training that rewards finishing the local task rather than maintainability.

  Lesson: long autonomous runs and the newest model are not automatically better engineering.

### S036: Brownfield Agentic Engineering
- Author: Addy Osmani
- Date: 2026-09-14
- URL: https://addyosmani.com/blog/brownfield-agentic-engineering/
- Kind: essay
- Focus: Extract:
  - why the repo is not a complete description (institutional knowledge and external constraints live outside it);
  - the green / yellow / red zone map, drawn by a person and not the agent;
  - red zones (auth, billing, permissions) need a human on every step;
  - characterization tests written in a separate pass.

  Note the outdated habits he names.

### S037: A field guide to Claude Fable 5: Finding your unknowns
- Author: Thariq Shihipar (Anthropic)
- Date: 2026-07-06
- URL: https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
- Kind: essay
- Focus: Extract:
  - known and unknown knowns and unknowns as the limit on agent output;
  - the blind-spot pass before unfamiliar territory;
  - brainstorms from cheapest to most ambitious;
  - throwaway prototypes with fake data;
  - the agent interviewing you, one question at a time, on ambiguities that change the architecture;
  - pointing at reference code instead of describing behaviour.

## Batch 8: insecure-ai-code
Why code that works is often not safe, why people believe the agent when it says it is, and what the official guidance tells you to check.

### S038: LLMs are getting smarter but not safer: Veracode 2026 GenAI Code Security Report
- Author: Veracode (Chris Wysopal quoted)
- Date: 2026-07-28
- URL: https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/
- Kind: report
- Focus: Extract the headline numbers: about 100% syntax pass vs 56% security pass, and about 44% security failures without security-specific guidance. Extract that larger or coding-specialized models were not more secure, and the "never ship it blind" scanning advice. Record the methodology and which vulnerability classes fail most.

### S039: Understanding the (In)Security of Vibe-Coded Applications
- Author: Junquan Deng, Zhiyu Fan, Ruijie Meng
- Date: 2026-06-22
- URL: https://arxiv.org/abs/2606.23130
- Kind: paper
- Focus: This is the core evidence for Aaron's security point. Extract:
  - 91.0% of 200 deployed vibe-coded apps were vulnerable, 65.77% Critical or High;
  - the top classes (broken access control, injection, auth failures);
  - "hidden security rules": server-side checks, validation and escaping omitted because the user never asked;
  - errors "fixed" by weakening a control;
  - the agent warning instead of fixing.

  Record how the apps were found and tested.

### S040: (Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code
- Author: Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka
- Date: 2026-09-17
- URL: https://arxiv.org/abs/2609.21020
- Kind: paper
- Focus: Extract:
  - developers picked the most-secure and least-secure AI suggestions at statistically indistinguishable rates;
  - only 22% of final submissions were fully secure;
  - about 21 seconds of review per suggestion, whatever its security level;
  - the cues people used instead of security;
  - experience did not protect them.

### S041: The 'vibe coding spectrum' approach to AI-assisted software development
- Author: Toby W, Principal Security Architect, UK NCSC
- Date: 2026-06-18
- URL: https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf
- Kind: essay
- Focus: Extract the oversight model scaled to risk:
  - what may be fully vibe-coded: prototypes, demos, internal tools with no sensitive data;
  - what must slide toward review: authentication and authorization, personal data, secrets and tokens, safety-critical code;
  - what review means for high-risk code.

  This is the official form of "check what the AI cannot verify, or bring in an expert".

### S042: Secure Coding with AI Cheat Sheet
- Author: OWASP Cheat Sheet Series
- Date: 2026-05-05 (first published; last updated 2026-10-04)
- URL: https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html
- Kind: docs
- Focus: Extract the current checklist:
  - verify a package exists, its age, downloads and maintainers before installing it;
  - indirect prompt injection via issues, PR comments, READMEs, error traces and fetched pages;
  - MCP server allowlists and pinned tool definitions;
  - rules files that can be silently tampered with;
  - why a passing AI-written test suite and AI review comments do not prove security.

### S043: Claude Code: Catch security issues as Claude writes code (security-guidance plugin)
- Author: Anthropic (live docs)
- Date: undated (record a last-updated date)
- URL: https://code.claude.com/docs/en/security-guidance
- Kind: docs
- Focus: Extract the three review layers: a per-edit pattern check, an end-of-turn model review, and an agentic review on commits. Note that the review is a separate model call. Then extract the limits the page states:
  - none of the layers block writes or commits;
  - the review model can miss issues;
  - commits made from your own shell are not reviewed;
  - it reads source code, not a running app.

  This defines what the agent's own security check cannot verify.

## Batch 9: exposed-backends-secrets
What "the app is public" means: open databases, keys in the browser, sites found within days, and how leaked secrets are caught.

### S044: Hacking Moltbook: The AI Social Network Any Human Can Control
- Author: Gal Nagli (Wiz Research)
- Date: 2026-02-02
- URL: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- Kind: incident
- Focus: Extract the mechanism:
  - Supabase exposes a REST API by default;
  - the public key in the JavaScript bundle is safe only if Row Level Security policies exist on every table;
  - anyone can read your shipped JavaScript and query your backend directly;
  - missing RLS, not the visible key, was the real bug.
- Also skim: Supabase Row Level Security docs (https://supabase.com/docs/guides/database/postgres/row-level-security, live docs). Read only for default grants on new public tables, that adding policies does not remove existing grants, that the service_role key bypasses RLS, and that views bypass RLS.

### S045: v0 security (with External APIs / environment variables)
- Author: Vercel (v0 docs)
- Date: 2026-10-09
- URL: https://v0.app/docs/security
- Kind: docs
- Focus: Extract:
  - the NEXT_PUBLIC_ prefix sends a variable to the browser;
  - environment variables are set per environment, and the preview sees only Development values;
  - use separate development and production keys, and rotate them;
  - generated code is treated as possibly insecure.
- Also skim: Lovable Docs: Security (https://docs.lovable.dev/features/security, undated; features dated 2026-07 to 2026-09). Read only for "a security review is not a certification", RLS per table retested after auth or schema changes, and rerunning scans after significant changes.

### S046: Update on Security at METR
- Author: METR
- Date: 2026-08-31
- URL: https://metr.org/blog/2026-08-31-security-update/
- Kind: incident
- Focus: Extract:
  - auth that fails open silently, so the app works but anyone can get in;
  - new sites are found within days through certificate-transparency logs, so there is no obscurity window;
  - an agent holding a key can simply be asked to reveal it;
  - keys without spend limits.

  Lesson: "nobody will find my side project" is false.

### S047: Secret scanning adds detectors for Lovable, Supabase, and more
- Author: GitHub Changelog
- Date: 2026-10-05
- URL: https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more
- Kind: docs
- Focus: Extract:
  - which AI-builder token types GitHub now detects;
  - what happens to partner secrets leaked in public repos (reported to the issuer for revocation);
  - what pattern detectors miss;
  - the new model-based detector and its opt-in status.
- Also skim: About push protection (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection). Read only for the defaults (user push protection on for public repos, repository push protection off) and who can bypass it.

### S048: Leaked n8n API Tokens Exposed Live Instances to Credential Theft
- Author: Guillaume Valadon (GitGuardian), on The Hacker News
- Date: 2026-08-05
- URL: https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
- Kind: report
- Focus: Extract:
  - the blast radius of one automation-platform token;
  - coding-agent permission files (.claude/settings.local.json) leaking API keys into public repos;
  - the instance URL committed next to the token;
  - old keys with no expiry;
  - what an attacker can do with stored credentials.
- Also skim: The State of Secrets Sprawl 2026 (GitGuardian, 2026-03, https://gitguardian.com/state-of-secrets-sprawl-report-2026). Read only for the leak rate of Claude Code co-authored commits (3.2% vs 1.5% baseline), MCP configuration files as a leak source, and how long leaked secrets stay valid.

## Batch 10: permissions-sandboxes-injection
Prompt injection as a structural risk, why approval prompts fail, what a sandbox does and does not cover, and least privilege for agents.

### S049: The lethal trifecta for AI agents: private data, untrusted content, and external communication
- Author: Simon Willison
- Date: 2025-06-16 (foundational and still current)
- URL: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Kind: essay
- Focus: Extract:
  - the three ingredients: private data, untrusted content, external communication;
  - why models cannot tell whose instructions they are reading;
  - why 95% guardrail detection is a failing grade in security;
  - how mixing MCP tools from different sources assembles the trifecta by accident.

  This is the one mental model for prompt-injection risk.

### S050: How we contain Claude across products
- Author: Anthropic Engineering
- Date: 2026-05-25
- URL: https://www.anthropic.com/engineering/how-we-contain-claude
- Kind: report
- Focus: Extract:
  - supervision vs containment;
  - users approving about 93% of permission prompts (approval fatigue);
  - the OS sandbox with network denied by default, which cut permission prompts by 84%;
  - credentials kept out of the agent's VM;
  - the case where an approved allowlisted domain was the exfiltration path.

  Lesson: a domain allowlist is a capability grant.

### S051: Auto mode is now the default in Claude Code for Pro, Max, and Team plans
- Author: Simon Willison
- Date: 2026-08-08
- URL: https://simonwillison.net/2026/Aug/8/auto-mode/
- Kind: essay
- Focus: Extract:
  - only 13.6% of 1,053 developers refused a dangerous command slipped into a prompt;
  - the classifier blocks 89%, which leaves 11%;
  - accidental damage and prompt injection are different risks;
  - vendor security claims need independent confirmation.
- Also skim: Breaking Claude Code Opus 5 Auto Mode (2026-08-27, https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/). Read for the confused-environment attack: a downloaded struct.py shadowed a standard-library module, with about 80% success. Auto mode is not a security boundary; run unattended agents in a container, VM or OS sandbox.

### S052: Choose a permission mode (Claude Code)
- Author: Anthropic (Claude Code docs)
- Date: 2026-09
- URL: https://code.claude.com/docs/en/permission-modes
- Kind: docs
- Focus: Extract the six permission modes and their trade-offs, that auto mode's classifier does not guarantee safety, and the protected paths that are never auto-approved.
- Also skim:
  - Claude Code: Security (https://code.claude.com/docs/en/security, also https://code.claude.com/docs/en/sandboxing). Read only for: the sandbox is off by default and covers shell commands only; file tools, MCP servers and hooks run outside it; the working-directory boundary is a prompt, not a wall.
  - Local sandboxing for GitHub Copilot now generally available (2026-10-07, https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available). Read only for what it sandboxes and that organizations can enforce it.

### S053: A CISO's guide to agentic AI
- Author: Jason Clinton, Deputy CISO, Anthropic
- Date: 2026-07-17
- URL: https://claude.com/blog/ciso-guide-to-agentic-ai
- Kind: essay
- Focus: Extract the four questions:
  - what untrusted content does the agent read;
  - what can it do, and under whose identity;
  - what is the blast radius;
  - can you tell agent actions from user actions.

  Also extract: no production credentials inside the agent's environment, egress allowlists, and why saying no to agents drives shadow adoption. Translate it into a solo builder's checklist.

### S054: One prompt let researchers take over AWS AgentCore agents (AgentCorruption)
- Author: Ana Maria Constantin (The Next Web), reporting Zenity Labs
- Date: 2026-10-08
- URL: https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents
- Kind: incident
- Focus: Extract the chain:
  - default execution roles far broader than one agent needs;
  - a web-request or shell tool reaching the cloud metadata credential endpoint;
  - persistent memory turning one injected prompt into a lasting instruction;
  - a public chatbot as a credential holder.

  Lesson: least privilege is the builder's job.

### S055: OWASP Top 10 for LLM Applications 2026
- Author: OWASP GenAI Security Project
- Date: 2026-08-04
- URL: https://github.com/GenAI-Security-Project/GenAI-LLM-Top10
- Kind: framework
- Focus: Extract the 2026 list and what moved: excessive agency up to #3, unbounded consumption up, and "system prompt leakage" replaced by hidden context exposure. Note that the ranking now weighs real incidents. Flag that tutorials citing the 2025 list are out of date.
- Also skim:
  - OWASP Top 10 for Agentic Applications for 2026 (https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026, 2025-12-09). Read only for the ASI01-ASI10 names.
  - CSA research note on the 2026 list and the new Agent Control Standard (https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/, 2026-09-04). Read only for inventorying each agent's reachable tools and data, and for permissions enforced when a tool is called.

## Batch 11: untrusted-inputs-supply-chain
Opening a repo, reading a ticket or installing a package can be code execution. How malicious content reaches the agent, and how to check what you install.

### S056: GitSpawn: AI coding agents run attacker code via git config
- Author: Francisco Rosales (Manifold Security)
- Date: 2026-09-01
- URL: https://www.manifold.security/blog/ai-coding-agents-git-hijack
- Kind: incident
- Focus: Extract how opening a folder with an agent becomes an execution event: repo git config such as core.fsmonitor runs programs when the agent calls git status or git diff. Note that this runs outside the sandbox and before workspace-trust prompts, and which agents were affected. Extract the advice: inspect .git/config, open untrusted repos in disposable containers.

### S057: How a Malicious Repo Tricked Claude Code into Running Malware
- Author: Brian Cumi (Straiker STAR Labs)
- Date: 2026-09-22
- URL: https://www.straiker.ai/blog/how-a-malicious-repo-tricked-claude-code-into-running-malware
- Kind: incident
- Focus: Extract:
  - agent configuration shipped inside a repo (.claude/agents/) steering who reviews it and what gets skipped;
  - why "ask the agent to security-review it" is no guarantee;
  - running a repo's tests (pytest, make) executes its code, so "11 passed" is not validation.

### S058: Agentjacking: MCP Injection Hijacks AI Coding Agents (CSA research note)
- Author: Cloud Security Alliance AI Safety Initiative, summarizing Tenet Security Threat Labs
- Date: 2026-06-12
- URL: https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/
- Kind: incident
- Focus: Extract:
  - data returned through an MCP server (errors, tickets, issues) can carry attacker instructions the agent cannot tell apart;
  - vetting a server's code does not cover the untrusted data it pipes in;
  - "public by design" identifiers like a Sentry DSN let anyone write into a queue your agent reads.

### S059: MCP Security Best Practices (specification revision 2026-07-28)
- Author: Model Context Protocol project
- Date: 2026-07-28
- URL: https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices
- Kind: docs
- Focus: Extract:
  - local MCP servers run with the client's privileges;
  - a malicious startup command can read ~/.ssh;
  - clients must show the exact command and get approval before adding a server;
  - confused deputy;
  - token passthrough is forbidden;
  - scope minimization.
- Also skim: The 2026-07-28 Specification (https://blog.modelcontextprotocol.io/posts/2026-07-28/). Read only for what 2025-era MCP explainers now get wrong (sessions, SSE transport, server-initiated sampling).

### S060: Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks (CSA research note)
- Author: Cloud Security Alliance AI Safety Initiative
- Date: 2026-04-19
- URL: https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/
- Kind: report
- Focus: Extract:
  - models invent package names, and 43% of invented names recur on every run, so attackers pre-register them;
  - agents install packages with no human moment to notice an odd name;
  - install scripts run where keys and tokens live;
  - how to check a new dependency: it exists, when it was registered, who publishes it.

  Note its caveat that rates differ for newer models.

### S061: ChainDrop npm Worm
- Author: Sai Likhith (StepSecurity)
- Date: 2026-08-04
- URL: https://stepsecurity.io/blog/chaindrop-npm-worm
- Kind: incident
- Focus: Extract:
  - "provenance proves which commit was built, not that the commit was authorized";
  - a committed lockfile does not protect installs that bypass it;
  - the protections that would have stopped it: --ignore-scripts, a minimum release age, CI egress allowlists;
  - stealers now targeting AI tool credential files.
- Also skim: Unvalidated npm trusted publishing configurations now expire (GitHub Changelog, 2026-10-02, https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire). Read only for how npm publishing is changing in response.

### S062: Playback: security moments (a malicious redirect, and verifying a download before install)
- Author: Aaron Orelup (typed and pasted prompts)
- Date: 2026-10-10
- URL: playback-lens:C--Users-soulo-Organized-Personal-My-Projects-Sandbox-2/7c75a0b6-4bcf-45ae-9869-1489cad914a6/2026-09-28 (also photoshop/dea3f681-154f-47d6-a4f4-05cb5da99bb5/2026-10-10)
- Kind: aaron-practice
- Focus: Extract the real situations Aaron hit:
  - an ad-network redirect and a fake CAPTCHA page, and what to check after clicking one;
  - checking a download before installing it: is the repo the genuine origin with real history, release assets, checksums and signatures, signed Windows builds, VirusTotal, typosquat lookalike sites, never disabling SmartScreen to make an install work.

  Topics only, no personal details.

## Batch 12: unattended-action
When agents and automations act alone: deletions, cheating on impossible tasks, workflows that succeed but do nothing, and what must never be delegated.

### S063: [Agent] Autonomous rd /s /q wiped the entire D: drive (Windows)
- Author: luck_li; reply by Colin (Cursor staff, Community Support Engineer)
- Date: 2026-10-09
- URL: https://forum.cursor.com/t/174156
- Kind: incident
- Focus: Extract how a shell quoting mistake turned a one-folder delete into a whole-drive delete. Extract staff's statements: Windows terminal commands do not run in a sandbox, and File-Deletion Protection covers only the agent's file-delete tool. Extract the run modes staff recommend.
- Also skim:
  - Forum thread 173688 (https://forum.cursor.com/t/173688, 2026-10-03). Read only for backups on the same drive, Git without a remote, deletes that skip the Recycle Bin, and Local History as a last resort.
  - Replit checkpoints and rollbacks (https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks). Read only for what a rollback does not restore: the production database.

### S064: Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident
- Author: Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR)
- Date: 2026-08-26
- URL: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- Kind: incident
- Focus: Extract:
  - impossible tasks pushed agents toward cheating and unsanctioned exploration instead of reporting failure;
  - shared infrastructure (package caches, registries) broke the isolation that was assumed;
  - agents misjudged how they were being checked and acted on it, including trying to alter logs;
  - a transcript is not a faithful record.

  Lesson: an agent's self-report is not evidence.

### S065: GenAI and Agentic AI Exploit Roundup Q3 2026
- Author: OWASP Gen AI Security Project (editor)
- Date: 2026-10-08
- URL: https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026
- Kind: report
- Focus: Extract the Q3 2026 exploit list with dates, and the lessons that cut across it:
  - prompt-level instructions alone are not a secure boundary;
  - enforce scope at the network and credential layer;
  - agents treat reachability and name similarity as permission;
  - an MCP server approved once can change its tool definitions later, so re-approve on change.

  Note whether it covers PixelLeak or Plugin4Shell.

### S066: Webhook works in test but not in production? The test vs. production URL trap
- Author: Syed Farzam Saadat
- Date: 2026-10-04
- URL: https://community.n8n.io/t/318716
- Kind: community
- Focus: Extract:
  - the test URL (works only while the editor listens) vs the production URL (works only when the workflow is Active);
  - saved is not active;
  - localhost is reachable only from your own machine;
  - setting WEBHOOK_URL when self-hosting;
  - "no execution logged" means the request never arrived.
- Also skim: Whatsapp Trigger not working because i am running n8n with docker on local machine (https://community.n8n.io/t/302932, 2026-07-12). Read only for external services not reaching localhost, an env panel that never reaches the container, restart vs redeploy, checking with printenv, and tunnel URLs that change on restart.

### S067: How do you catch workflows that run fine but do nothing?
- Author: Richard Rodrigues; 36 posts (Romeo Apps, Nathan, Adam, Cam, Michael Stables, Enzo Software)
- Date: 2026-08-21
- URL: https://community.n8n.io/t/308708
- Kind: thread
- Focus: Extract:
  - the three layers of checks: run health, output health, receipt health;
  - item-count checks that stop with an error on an unexpected zero;
  - field-shape checks, because a renamed field yields nulls that still pass count checks;
  - known-answer canary inputs on a schedule;
  - verifying at the destination.
- Also skim: The silent failure: when your n8n workflow succeeds but does nothing (https://community.n8n.io/t/307116, 2026-08-11). Read only for the five silent-success patterns:
  - a silent IF exit;
  - HTTP 200 with a failure body;
  - a Set node wiping data;
  - a loop ending early;
  - a webhook nobody calls.

### S068: Agency and Agents
- Author: Ethan Mollick
- Date: 2026-08-31
- URL: https://www.oneusefulthing.org/p/agency-and-agents
- Kind: essay
- Focus: Extract:
  - what agents must not do on their own: spend money, contact outsiders, access sensitive material;
  - when to escalate to humans (expertise, variance, interesting decisions);
  - checking how a problem was solved, not only whether the answer is right;
  - AI ideas converging, so seek diverse human input.

  Note his critique of automating everything except approvals.

## Batch 13: beyond-code-agents-and-facts
Desktop, browser and always-on agents for non-coding work, and checking AI research, spreadsheets and hardware designs.

### S069: Use Claude Cowork safely
- Author: Anthropic (Claude Help Center)
- Date: 2026-10
- URL: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- Kind: docs
- Focus: Extract:
  - where Cowork runs: an isolated temporary cloud environment, with connected local folders processed on Anthropic's servers;
  - read tools vs write tools and their risk;
  - the two conditions prompt injection needs;
  - what isolation does not limit (what Claude can read or do).
- Also skim: Updates to Consumer Terms and Privacy Policy (Anthropic, 2025-08-28, https://www.anthropic.com/news/updates-to-our-consumer-terms). Read only for the model-training setting and retention on Free, Pro and Max vs commercial plans. Check that it is still current.

### S070: Use Claude in Chrome safely (Anthropic Help Center)
- Author: Anthropic
- Date: undated (record a date)
- URL: https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely
- Kind: docs
- Focus: Extract:
  - you remain responsible for every action the agent takes, including purchases;
  - the agent screenshots tabs and cannot filter sensitive content;
  - use a separate browser profile with no bank, health or government logins;
  - the default is "Automatically approve", and how to switch to manual review;
  - where side-panel sessions are saved.

### S071: Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users
- Author: Ravie Lakshmanan (The Hacker News), reporting Koi Security and OpenSourceMalware
- Date: 2026-02-02
- URL: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- Kind: incident
- Focus: Extract:
  - a skill marketplace with little vetting (a week-old GitHub account could publish);
  - a "prerequisite" setup step as the malware delivery;
  - typosquatted names;
  - a polished README as false evidence of safety;
  - what the always-on agent held that was stolen.
- Also skim: OpenClaw Gateway Security docs (https://docs.openclaw.ai/gateway/security, undated). Read only for the current state: one trust boundary per gateway, container images that default to an exposed bind, cross-conversation sending by default, and the security audit command.

### S072: AI Hallucination Cases database
- Author: Damien Charlotin
- Date: 2026-10-10
- URL: https://www.damiencharlotin.com/hallucinations/
- Kind: list
- Focus: Extract:
  - the current count of court decisions involving hallucinated material (2,184 at the finder's read);
  - the share filed by non-lawyers using AI for their own filings (about 58%);
  - the types: fabricated, misrepresented, false quotes, outdated advice.

  Lesson: checking AI research is a non-coder's problem too.

### S073: Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents
- Author: Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania)
- Date: 2026-04-03
- URL: https://arxiv.org/html/2604.03173v1
- Kind: paper
- Focus: Extract:
  - the rates of fabricated and non-resolving URLs;
  - that deep research agents fabricated more (10.7%) than search-augmented models (4.8%);
  - how to tell link rot from fabrication (Wayback Machine);
  - that a live link does not mean the source supports the claim;
  - giving the agent a URL checker.

  This bears directly on this research crew's own method.

### S074: WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance
- Author: Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. (Columbia Business School)
- Date: 2026-05-21
- URL: https://arxiv.org/html/2605.22664v1
- Kind: paper
- Focus: Extract the best agent score (69.1/100) and the failure modes:
  - values hard-coded instead of formulas, which makes the workbook unauditable;
  - an off-by-one error hidden by a total that happened to match;
  - missing unit labels and error handling.

  Extract the checks a human should run on an AI-built spreadsheet: live formulas, traceable logic, behavior when assumptions change.

### S075: Can AI Now Design PCBs That Just Work?
- Author: Maya Posch, Hackaday
- Date: 2026-09-05
- URL: https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/
- Kind: essay
- Focus: Extract:
  - why vendor benchmark claims need independent checks;
  - the failures: discontinued replacement parts, footprints not made from datasheets, schematics with open circuits;
  - what still needs a human or expert: validation, safety and EMC compliance.

  This is the physical-device case of "bring in an expert who can".

## Batch 14: rights-and-disclosure
What creators must know before publishing AI-made media: disclosure law, ownership, likeness and platform rules.

### S076: EU AI Act: Transparency Obligations for AI-Generated Content (Article 50)
- Author: Julia Apostle, Orrick
- Date: 2026-08-14
- URL: https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50
- Kind: report
- Focus: Extract:
  - provider (tool maker) vs deployer (you) duties;
  - that personal non-professional use is exempt and commercial creators are deployers;
  - where deepfake disclosure must appear (at the start and at intervals; end credits alone fail);
  - a spoken disclaimer for audio deepfakes;
  - the reduced duty for artistic and satirical work;
  - the date the duties apply.

### S077: Suno Terms of Service
- Author: Suno, Inc.
- Date: 2026-08-10
- URL: https://suno.com/terms
- Kind: docs
- Focus: Extract:
  - free-tier songs are personal and non-commercial only;
  - the 2026-09-03 rule that commercial use needs a permitted download, with monthly limits by tier;
  - Suno does not promise that copyright vests in outputs;
  - remixes are never commercial;
  - embedded fingerprints and metadata must not be removed.
- Also skim: US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works (Morgan Lewis, 2026-03-06, https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works). Read only for: purely AI-made works are not copyrightable in the US, and you should document human direction and editing.

### S078: A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress
- Author: Erik Dullea, Evan Yahng (Husch Blackwell)
- Date: 2026-08-20
- URL: https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/
- Kind: report
- Focus: Extract:
  - the proposed federal right over everyone's voice and likeness, not just celebrities';
  - statutory damages per violating replica;
  - existing state laws (Tennessee ELVIS Act; New York disclosure for synthetic performers in ads);
  - getting consent before cloning a voice or face.

  Note the bill's status as of the article.

### S079: YouTube clarifies policies around AI slop and upsetting videos
- Author: Sarah Perez, TechCrunch
- Date: 2026-07-20
- URL: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Kind: report
- Focus: Extract the three demonetized categories (template or repetitive, distressing, AI personas on finance, legal or health). Extract that the originality-and-value test applies whether or not AI was used, and what costs a channel its Partner Program status.

## Batch 15: surveys-and-learning
Who uses agents and how much, trust tied to verifiability, and what heavy AI use does to understanding and skill.

### S080: Stack Overflow Developer Survey 2026 - full results site (AI, Knowledge, Community) and press release
- Author: Stack Overflow (press release quotes CEO Prashanth Chandrasekar)
- Date: 2026-10-06
- URL: https://survey.stackoverflow.co/2026/
- Kind: survey
- Focus: Extract:
  - trust conditional on verifiability: 48.0% trust AI only when they can easily verify it, 6.6% with important decisions;
  - missing context: incomplete 63.2%, outdated 56.5%, in people's heads 60.9%;
  - asking an AI agent first (70%);
  - token cost and model choice as everyday concerns.

  Record the sample size and survey dates.
- Also skim: the blog summary (https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/). Read only for which context sources developers trust most, and the 93% who need source attribution.

### S081: How Much Code Do Developers Really Let Agents Write? (JetBrains Research, Developer Ecosystem Survey 2026)
- Author: Mikhail Bogdanov (JetBrains Research)
- Date: 2026-08
- URL: https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/
- Kind: survey
- Focus: Extract the self-reported shares of agent-generated, AI-assisted and manual code, weekly agent use, and the differences by seniority and language. Note that the figures are self-reported and overlap, and the warning that tool rankings go stale within months.

### S082: Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI
- Author: Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva
- Date: 2026-07-01
- URL: https://arxiv.org/abs/2607.01418
- Kind: paper
- Focus: Extract:
  - +24% merged PRs per engineer per day, with no quality measure;
  - who the tools suit: seniors who can break down work and review output;
  - the worry that juniors won't develop a sense for good code;
  - the practices that mattered: small chunks, review for correctness.

  Lesson: more output is not proof of better software.

### S083: How AI assistance impacts the formation of coding skills (Anthropic)
- Author: Judy Hanwen Shen and Alex Tamkin
- Date: 2026-01-29
- URL: https://www.anthropic.com/research/AI-assistance-coding-skills
- Kind: paper
- Focus: Extract:
  - the trial result: 50% vs 67% on understanding;
  - the biggest gap was in debugging;
  - no significant speed gain while learning a new library;
  - which usage patterns kept learning (conceptual questions, generate then ask why) and which destroyed it (full delegation, "let AI debug it").

  Use it for how the course tells learners to use AI while learning.

### S084: Agentic Skill Decay
- Author: Addy Osmani
- Date: 2026-08-31
- URL: https://addyosmani.com/blog/agentic-skill-decay/
- Kind: essay
- Focus: Extract:
  - the four skills to practise: deciding, specifying, steering, verifying;
  - "verification is the floor and imagination is the ceiling";
  - plausible code arriving faster than your ability to judge it;
  - the code-vending-machine and amnesiac-new-hire metaphors;
  - how he says to keep skills sharp.

### S085: From Prompting to Verification: How Experience Shapes Vibe Coding Practices
- Author: Ahmed Fawzy, Amjed Tahir, Kelly Blincoe
- Date: 2026-05-23
- URL: https://arxiv.org/abs/2605.24521
- Kind: paper
- Focus: Extract the "perception-action gap": awareness of the risks is widespread, but the ability to evaluate depends on experience. Non-developers were the only group reporting that they never check AI code; about 45% of professionals always check.
- Also skim: A Paradox of AI Fluency (Potts and Sudhof, 2026-04-28, https://arxiv.org/abs/2604.25905). Read only for invisible failures (85.6% unseen by minimal-fluency users vs 22.1% for high-fluency users) and the named failure types: Confidence Trap, Silent Mismatch, Walkaway.

---

## Folded in as companions (27): read only for the point named in the parent entry

| Candidate | Date | Folded into | Why folded rather than read in full |
|---|---|---|---|
| Playback: the 00.06 rejection, source of the course rule | 2026-10-03 | S004 | Same event as AO-034; read for Aaron's own wording of the rule |
| AI Prompting for Everyone (DeepLearning.AI) | 2026-07-24 | S010 | Same author and month, same beginner audience |
| Cursor Learn: Finding and fixing bugs | undated | S009 | Same subject (how testing and debugging work with agents) |
| Prompt caching (Claude Platform Docs) | undated | S012 | Same vendor docs on what the context holds and costs |
| Google users fight for refunds as unauthorized API usage bills soar (The Register) | 2026-05-13 | S020 | Same story: Google keys and surprise Gemini bills |
| Cursor changelog (Aug 27 - Oct 6, 2026) | 2026-10-06 | S025 | Same extraction: how fast tools change |
| From Confident Closing to Silent Failure (false success in LLM agents) | 2026-06-01 | S030 | Same subject: false "done" claims |
| Row Level Security (Supabase Docs) | undated | S044 | The mechanism behind the S044 incident |
| Lovable Docs: Security | undated | S045 | Same kind: builder platform security docs |
| About push protection (GitHub Docs) | undated | S047 | Same GitHub feature |
| The State of Secrets Sprawl 2026 (GitGuardian) | 2026-03 | S048 | Same publisher's research on leaked secrets |
| Breaking Claude Code Opus 5 Auto Mode | 2026-08-27 | S051 | Same subject and author: auto mode |
| Claude Code: Security, and Configure the sandboxed Bash tool | undated | S052 | Same product docs |
| Local sandboxing for GitHub Copilot now generally available | 2026-10-07 | S052 | Same subject: what an agent sandbox covers |
| OWASP Top 10 for Agentic Applications for 2026 | 2025-12-09 | S055 | Same OWASP project, companion list |
| OWASP's 2026 LLM Top 10 and New Agent Control Standard (CSA) | 2026-09-04 | S055 | Same list; read for the Agent Control Standard |
| The 2026-07-28 Specification (MCP blog) | 2026-07-28 | S059 | Same spec revision |
| Unvalidated npm trusted publishing configurations now expire | 2026-10-02 | S061 | Same npm-worm story: GitHub's response |
| Errible: AI out of control, randomly deleting files (Cursor forum 173688) | 2026-10-03 | S063 | Same failure type in the same week |
| Replit checkpoints and rollbacks | undated | S063 | Same subject: what undo and backup actually restore |
| Whatsapp Trigger not working ... docker on local machine (n8n 302932) | 2026-07-12 | S066 | Same theme: local vs reachable environments |
| The silent failure: when your n8n workflow succeeds but does nothing (n8n 307116) | 2026-08-11 | S067 | Same theme, earlier thread |
| Updates to Consumer Terms and Privacy Policy (Anthropic) | 2025-08-28 | S069 | Same vendor: where your data goes |
| OpenClaw Gateway Security (official documentation) | undated | S071 | Same product: current state after the incident |
| US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works | 2026-03-06 | S077 | Same subject: who owns AI output |
| The results of the 2026 Developer Survey are here! (Stack Overflow blog) | 2026-10-06 | S080 | Same survey |
| A Paradox of AI Fluency | 2026-04-28 | S085 | Same subject: who notices AI failures |

---

## Not selected (162), with reasons

Listed in the order of the candidate list. "Covered by" means the selected entry carries the same gap with newer or stronger evidence.

### Courses and syllabi
- Missing Semester 2026: Agentic Coding lecture (2026-01-21, https://missing.csail.mit.edu/2026/agentic-coding/): its points (context degrades before overflow, AGENTS.md, skills, subagents, worktrees, letting the agent run the failing check) are taught in the newer Stanford lectures S002-S003. Its framing "AI folded into every lecture, not a standalone topic" is noted.
- Missing Semester 2026: Code Quality lecture (2026-01-23, https://missing.csail.mit.edu/2026/code-quality/): checks as the agent's feedback loop are covered by S029-S030. "Deliberately break code to confirm CI catches it" is flagged below.
- Missing Semester 2026: Beyond the Code lecture (2026-01-22, https://missing.csail.mit.edu/2026/beyond-code/): accountability for AI code is covered by S007, and "don't submit what you can't explain" by S084. Disclosure norms are flagged below.
- AI Agent Security (guest lecture, MIT 6.566) (2026-04, https://github.com/anishathalye/ai-agent-security-lecture): "guardrails give no guarantees" and the production-database deletion are covered by S049-S052 and S063.
- Building with AI: A Hands-On Course for Scientists and Engineers (2026-08-31, https://web.mit.edu/webcast/computing/s26/0926/1.html): thin webcast landing page, medium credibility. Audience signal only.
- Claude Code in Action (undated, https://anthropic.skilljar.com/claude-code-in-action): same Anthropic Academy material as S005, which is newer and dated.
- AI Fluency: Framework & Foundations (undated, https://anthropic.skilljar.com/ai-fluency-framework-foundations): the 4D framework is read in its builder form in S007.
- 10 free Anthropic AI courses launch today on Coursera (2026-10-05, https://blog.coursera.org/10-free-anthropic-ai-courses-launch-today-on-coursera-with-more-coming-each-month-to-help-learners-stay-current/): announcement of the same courses as S005-S007.
- Introduction to Claude Cowork (undated, https://anthropic.skilljar.com/introduction-to-claude-cowork): Cowork's risks are read on the official safety page (S069).
- Spec-Driven Development with Coding Agents (2026-04-18, https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents): the spec-driven workflow is covered by S003 (RePPIT) and S024 (Kiro specs).
- Building Coding Agents with Tool Execution (2026-04-22, https://www.deeplearning.ai/short-courses/building-coding-agents-with-tool-execution): medium credibility. Local vs container vs microVM trade-offs are covered by S050 and S052.
- Codex Bootcamp 101 companion (Codex best practices, 2026-09, https://learn.chatgpt.com/guides/best-practices): same Goal / Context / Constraints / Done-when structure as S008, from the same vendor.
- Cursor Learn: Reviewing and testing code (2026-02, https://cursor.com/learn/reviewing-testing): "passing tests isn't proof" and happy-path bias are covered by S009, S029 and S030.
- Replit Learn: AI Foundations (undated, https://learn.replit.com/docs/ai-foundations/lesson-1): its "just for me / my team / the world" levels echo the risk tiers in S041. The framing is flagged below.
- HN discussion: The Missing Semester of Your CS Education, Revised for 2026 (2026-02-23, https://news.ycombinator.com/item?id=47124171): opinion thread. Its gap list (testing and QA, git's data model, troubleshooting method) is flagged below.

### Topic maps and lists
- roadmap.sh: Vibe Coding roadmap (2026-02-27, https://roadmap.sh/vibe-coding): checkpoints and secrets hygiene are covered by S063 and S047. "Pick a popular stack the AI was trained on" is flagged below.
- roadmap.sh: Claude Code roadmap (2026-02-27, https://roadmap.sh/claude-code): permission modes, context pollution and subscription vs API are covered by S052, S015 and S016.
- roadmap.sh: AI Product Builder roadmap (2026-07-13, https://roadmap.sh/ai-product-builder): medium credibility, cut for space. Its framings are flagged below: app anatomy for reviewing AI output, and targeted vs structural change.
- Vibe Coding Best Practices: How To Get Consistent Results (roadmap.sh guide) (2026-04-20, https://roadmap.sh/vibe-coding/best-practices): context-file and /clear tips are covered by S003 and S021.
- Agentic Engineering Patterns (living guide) (2026-02-23, https://simonwillison.net/guides/agentic-engineering-patterns/): its core points are restated in Willison's newer S028 and S033.
- Best practices for Claude Code (official docs) (undated, https://code.claude.com/docs/en/best-practices): "give the agent a check it can run; the worker isn't the grader" is covered by S030, S031 and S002. Read it if a lesson needs Anthropic's own wording.
- Beyond permission prompts: making Claude Code more secure and autonomous (2025-10-20, https://www.anthropic.com/engineering/claude-code-sandboxing): superseded by S050 (2026-05), which carries the same 84% figure and newer lessons.
- OWASP Top 10 for LLM Applications 2026 (CSA research note, 2026-08-15, https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-llm-top10-2026-incident-weighted-202/): same list as S055. The later CSA note (2026-09-04) is the companion kept.
- vibe-coding-security: pre-launch checklist for AI-generated apps (2026-08-09, https://github.com/boxed-dev/vibe-coding-security): community checklist. Its items (RLS as anon, service_role, NEXT_PUBLIC_, IDOR, rate limits) are covered by S044, S045 and S042. Could serve as a lesson handout.
- You're Doing Vibe-Coding Wrong. Here's the 17-Point Fix. (2026-09-20, https://dev.to/chizee/youre-doing-vibe-coding-wrong-heres-the-17-point-fix-e9h): medium credibility click-level checklist. Server-side auth and validation are covered by S039 and S042.
- The Hidden Cost of Vibe Coding: What Junior Developers Stop Learning (2026-09-23, https://www.dice.com/career-advice/the-hidden-cost-of-vibe-coding-what-junior-developers-stop-learning): covered with stronger evidence by S083 and S084.
- Building an AI Coding Agent: 6 Lessons From Real Development (2026-09-29, https://dev.to/synfinity-dynamics-pvt-ltd/building-an-ai-coding-agent-6-lessons-from-real-development-46jo): medium credibility, aimed at people building agents. Covered by S002.
- Blog #4: My First Ever Agent and Things That I Wish I Knew Before Building This (2026-09-17, https://dev.to/aeronn_11/blog-4-my-first-ever-agent-and-things-that-i-wish-i-knew-before-building-this-18jl): low credibility anecdote.
- What we wish we knew about building AI agents (PostHog) (2026-03-24, https://newsletter.posthog.com/p/what-we-wish-we-knew-before-building): aimed at teams building agent products. "Try a single LLM call or a hardcoded workflow before an agent" is flagged below.
- AI Tooling for Software Engineers in 2026 (Pragmatic Engineer) (2026-03-03, https://newsletter.pragmaticengineer.com/p/ai-tooling-2026): superseded by S080 and S081 (August to October 2026).
- The impact of AI on software engineers in 2026, Part 1 (Pragmatic Engineer) (2026-04-14, https://newsletter.pragmaticengineer.com/p/the-impact-of-ai-on-software-engineers-2026): usage limits and cost are covered by S016-S018. "AI slop review burden on colleagues" and lock-in from subsidized plans are flagged below.
- awesome-claude-code (2026-10-12, https://github.com/hesreallyhim/awesome-claude-code): a link list, not evidence. S015 and S021 cover what its categories are for.
- Encyclopedia of Agentic Coding Patterns (2026-08, https://aipatternbook.com): medium credibility pattern book. Trust boundary and blast radius are covered by S053 and S049. A candidate glossary later.
- Vibe Coding for Non-Developers: 63% of Users Now Have No Coding Background (Tech Times, 2026-05-24, https://www.techtimes.com/articles/317077/20260524/vibe-coding-non-developers-63-users-now-have-no-coding-background-breaches-follow.htm): second-hand roundup. Moltbook is read at the source (S044).
- Vibe Coding Best Practices [2026]: 7 That Work, 3 That Fail (2026-06-20, https://www.kunalganglani.com/blog/vibe-coding-best-practices-2026): medium credibility personal list. "Isolated prompts produced three auth systems" is covered by S036.

### Practitioners
- Vibe coding and agentic engineering are getting closer than I'd like (Willison, 2026-05-06, https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/): the same ground is covered by his newer S028 and S033 and by S029. The term "normalization of deviance" is flagged below.
- The Coming Loop (Ronacher, 2026-06-23, https://lucumr.pocoo.org/2026/6/23/the-coming-loop/): partly covered by the same author's newer S035. "Loops pile up defensive code" is flagged below.
- The 80% Problem in Agentic Coding (Osmani, 2026-01-28, https://addyo.substack.com/p/the-80-problem-in-agentic-coding): comprehension debt and agent failure modes are covered by his newer S084 and by S085.
- Sequoia Ascent 2026 summary (Karpathy, 2026-04-30, https://karpathy.bearblog.dev/sequoia-ascent-2026/): jagged intelligence and verifiability are covered by S027 and S033.
- My AI Adoption Journey (Hashimoto, 2026-02-05, https://mitchellh.com/writing/my-ai-adoption-journey): covered by S033 and S037. "Redo your own past work with an agent to learn its limits" is flagged below.
- The Shape of Things to Come, Part 1 (Yegge, 2026-08, https://yegge.ai/essays/the-shape-of-things-to-come/): medium credibility and speculative (human review "gone by next year"). Orchestration is beyond this audience.
- if your team is too busy doing their 'normal job' to experiment with AI (Huntley, 2026-10-09, https://ghuntley.com/replaced/): career opinion. "Understand how a coding agent works inside" is covered by S002.
- Harness design for long-running application development (Anthropic Labs, 2026-03-24, https://www.anthropic.com/engineering/harness-design-long-running-apps): "self-evaluation leniency, so separate builder from judge" is covered by S030 and S031. Some of its model-specific advice is already marked outdated in its own notes.
- Harness engineering for coding agent users (Böckeler, 2026-04-02, https://martinfowler.com/articles/harness-engineering.html): S021 measures the same guides-vs-enforcement split in practice, and S015 states rules vs hooks. The "guides vs sensors" vocabulary is flagged below.

### Incidents
- Thousands of Vibe-Coded Apps Exposing Corporate, Personal Data: RedAccess (2026-05-07, https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/): medium credibility. "Published apps are found" is covered by S046. "Public by default; search engines index it" is flagged below.
- Cursor-Opus agent snuffs out startup's production database (The Register, 2026-04-27, https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442): over-broad tokens and backups on the same volume are covered by S054 and S063.
- Claude Opus 5 Wipes a Production Database - and It Wasn't Its Fault (IT-Connect, 2026-07-30, https://www.it-connect.tech/claude-opus-5-wipes-a-production-database-and-it-wasnt-its-fault/): medium credibility. "Production credentials reachable by the agent" is covered by S053 and S063. "Harmless-looking commands can be destructive" is flagged below.
- Methodology: How we discovered over 2k high-impact vulnerabilities in apps built with vibe coding platforms (Escape, 2025-10-29, https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/): anon key vs service-role key is covered by S044 and its Supabase companion.
- Mini Shai-Hulud: npm Worm Targets AI Developer Supply Chain (CSA, 2026-05-17, https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-ai-supply-chain-20260517-csa-st/): same npm-worm family as S061, which is newer. Its "AI assistant config files as persistence; uninstalling does not remove it" is flagged below.
- Surprise AI bills leave AWS and Google Cloud users aghast (The Kettle, 2026-05-18, https://www.theregister.com/ai-ml/2026/05/18/surprise-ai-bills-leave-aws-and-google-cloud-users-aghast/5241348): same story as S020's companion.
- PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub (2026-10-02, https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/): medium credibility relay of research. Flagged below. S065's reader should note whether the Q3 roundup covers it.
- AI coding agent vulnerabilities, October 2026: GitSpawn and more (Adversa, 2026-10-02, https://adversa.ai/blog/top-ai-coding-agent-security-resources-october-2026/): roundup. GitSpawn is read at the source (S056). Plugin4Shell is flagged below.
- AI coding tool Replit wiped a database and called it a 'catastrophic failure' (Fortune, 2025-07-23, https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure): "a code freeze stated in chat is not enforced" is covered by S023 (2026-09).
- Statement on CVE-2025-48757 (Matt Palmer, 2025-05-29, https://mattpalmer.io/posts/statement-on-CVE-2025-48757/): "RLS enabled is not RLS correct; scanners check presence" is covered by S044 and S045.
- Tea App Data Breach (Security.org, 2026-07-08, https://www.security.org/identity-theft/breach/tea-app/): medium credibility, and not an AI-built app. "Old storage left after a migration is still live" is flagged below.

### Security frameworks and docs
- Agentic MCP Security Best Practices Guide (draft) (CSA, 2026-03-27, https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/): tool poisoning and rug pulls are covered by the official S059 and by S065.
- Top MCP Security Resources, August 2026 (Adversa, 2026-08-06, https://adversa.ai/blog/top-mcp-security-resources-august-2026): link roundup covered by S058 and S065.
- RSAC: UK NCSC Head Urges Industry to Develop Vibe Coding Safeguards (2026-03-24, https://infosecurity-magazine.com/news/rsac-uk-ncsc-urges-vibe-coding/): second-hand. NCSC is read at the source (S041).
- Careful Adoption of Agentic AI Services (Five Eyes joint guidance) (2026-05-01, https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services): organization-level guidance. Least privilege, short-lived credentials and starting in low-risk environments are covered by S053 and S055.
- ASD urges care in the adoption of agentic AI for cyber defence (2026-07-27, https://www.govtechreview.com.au/content/gov-security/news/asd-urges-care-in-the-adoption-of-agentic-ai-for-cyber-defence-126772027): second-hand. The escaping-the-test-environment point is covered by S064.
- Codex: Agent approvals & security (undated, https://learn.chatgpt.com/docs/agent-approvals-security): the same "sandbox and approval are separate controls" model as S052. "danger-full-access exposes Codex credentials" is noted.
- Securing OpenAI Codex: What You Need to Know Before Rolling It Out (Pluto Security, 2026-05-08, https://pluto.security/blog/securing-openai-codex/): vendor blog. Covered by S052 and S057.
- Security-Focused Guide for AI Code Assistant Instructions (OpenSSF, 2025-08-01, https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions): its findings are flagged below for S042's reader to cross-check: "act as a security expert" prompts performed worse, and short specific rules beat copied rule sets.
- The OWASP Top 10 for Vibe-Coded Applications (Part 2) (Simon Roses Femerling, 2026-04-23, https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/): frontend-only role checks and similar issues are covered by S039 and S042.
- Vibe Coding Security Risks You Can't Ignore (Arnica, 2026-07-21, https://www.arnica.io/blog/vibe-coding-security-risks): vendor blog whose key statistic is second-hand. Covered by S039.
- Risks and mitigations for Copilot cloud agent (undated, https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations): the agent's self-checks (CodeQL, secret scanning) can be switched off. S052's Copilot companion covers the sandbox side.
- MCP Security Best Practices (tutorials page) (undated, https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices): older page with the same content as S059.

### Community threads
- How are people handling context across different AI coding tools? (Cursor forum 159891, 2026-05-06, https://forum.cursor.com/t/159891): stale context files and memories are covered by S022 and S026. A portable AGENTS.md is noted.
- Should a Coding Agent Be Allowed to Mark Its Own Task Complete? (Cursor forum 168557, 2026-08-16, https://forum.cursor.com/t/168557): "done is a claim" is covered by S030.
- MCP problem en code problem (Cursor forum 173052, 2026-09-26, https://forum.cursor.com/t/173052): "CI green while production broken" is covered by S030 and S066.
- What's the last AI-assisted change that created more recovery work than expected? (Cursor forum 168209, 2026-08-12, https://forum.cursor.com/t/168209): the recovery toolkit is covered by S063. "The agent treated a question as permission" is flagged below.
- My AI Workflow Builder keeps saying it fixed my workflow but it's still not working (n8n 298708, 2026-06-08, https://community.n8n.io/t/298708): "the AI says it fixed it" is covered by S067 and S030.
- Exposed API Keys and Secrets: The Vibe-Coder's First Fix (RedHub, 2026-09-10, https://blog.redhub.ai/app-secrets-and-api-keys): low credibility.
- Vibe Coding Reddit: Top Threads Decoded (2026) (2026-05-14, https://sorceress.games/blog/vibe-coding-reddit-top-threads-decoded-2026): low credibility second-hand summary.
- Vibe Coding Reddit: Top Tools from r/vibecoding in 2026 (2026-10-01, https://www.aitooldiscovery.com/guides/vibe-coding-reddit): low credibility.

### Surveys and studies
- State of Devs 2026 (Devographics) reported by Dr. Web (2026-10-03, https://www.drweb.de/state-of-devs-2026-ergebnisse-ki-burnout/): medium credibility and second-hand. Supervision fatigue ("AI brainfry") is flagged below. Read Devographics directly if a lesson uses it.
- Developers trust AI agents yet still verify code manually (Temporal, 2026-08-26, https://www.developer-tech.com/news/developers-trust-ai-agents-still-verify-code-manually/): medium credibility and second-hand. Agent-operations figures are aimed at teams running agent fleets.
- AI productivity: the METR number is out of date (devs group, 2026-08-17, https://devs-group.ch/en/blog/ai-productivity-studies-2026/): commentary on how productivity is measured, not a builder gap.
- (Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding (2026-07-29, https://arxiv.org/abs/2607.26375): medium credibility. Comprehension harm is covered by S083 and S085.
- Anthropic Economic Index report: Cadences (2026-06-26, https://www.anthropic.com/research/economic-index-june-2026-report): "most AI use is not code" is noted as an audience signal, not a gap.
- Pew Research: Americans and AI 2026 (reported by The Next Web, 2026-06-17, https://thenextweb.com/news/pew-research-americans-ai-chatbot-skepticism-regulation-distrust-2026?type=AI): general public, not builders.
- AI Increasingly Embraced by Web Devs (State of Web Dev AI 2026) (2026-05-20, https://www.i-programmer.info/news/87-web-development/18880-ai-increasingly-embraced-by-web-devs.html): second-hand. The share-of-code figures are superseded by S081.
- New DORA Report Claims Strong Engineering Foundations Drive AI Return on Investment (2026-05-11, https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/): second-hand and team-level. "AI amplifies the existing system" is noted.
- 2026 Work Trend Index Annual Report (Microsoft, 2026-05-05, https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization): corporate survey. "Quality control of AI output as the top skill" echoes S085.
- Safer Builders, Risky Maintainers (2026-03-29, https://arxiv.org/abs/2603.27524): medium credibility. "Agent confidence does not predict safe changes; refactors and chores are riskier" is flagged below.
- Anthropic Economic Index report: Learning Curves (2026-03-24, https://www.anthropic.com/research/economic-index-march-2026-report): "skill with AI grows with use" is covered in spirit by S085.
- We are Changing our Developer Productivity Experiment Design (METR, 2026-02-24, https://metr.org/blog/2026-02-24-uplift-update/): methodology of productivity studies, not a builder gap.
- Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? (2026-02-12, https://arxiv.org/abs/2602.11988): medium credibility. "Context files raise cost without general gains" is covered with newer data by S021 and S022.
- 2026 State of Code Developer Survey report (Sonar, 2026-01-08, https://www.sonarsource.com/state-of-code-developer-survey-report.pdf): its verification-gap figures are superseded by S080 (2026-10).
- Octoverse 2025 (GitHub, 2025-10-28, https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/): over 12 months old. "Typed languages make agent output checkable" and "broken access control is the top alert" are flagged below.
- How are developers using AI? Inside our 2025 DORA report (2025-09-23, https://blog.google/technology/developers/dora-report-2025/): superseded by the 2026 surveys.
- Stack Overflow 2025 Developer Survey - AI section (undated, https://survey.stackoverflow.co/2025/ai): superseded by S080.

### Tool docs
- Claude Code Auto Mode: What Changed, What It Blocks (Tried and Typed, 2026-08-30, https://triedandtyped.com/2026/08/30/claude-code-auto-mode-default/): same story as S051.
- Agent approvals & security (OpenAI Codex, .md version) (undated, https://learn.chatgpt.com/docs/agent-approvals-security.md): duplicate of the Codex approvals page above.
- Best practices for coding with agents (Cursor, Lee Robinson, 2026-01-09, https://cursor.com/blog/agent-best-practices): Debug Mode is covered by S009's companion. The TDD check that the agent did not modify tests to pass is covered by S030.
- An important update: Transitioning Gemini CLI to Antigravity CLI (2026-05-19, https://github.com/google-gemini/gemini-cli/discussions/27274): tool churn is covered by S025. "Your account type decides whether the tool works" is flagged below.
- Getting Started with Google Antigravity (codelab) (undated, https://codelabs.developers.google.com/getting-started-google-antigravity?hl=en): product walkthrough.
- Cognition Turns Windsurf Into Devin Desktop (2026-06-02, https://alphasignal.ai/news/cognition-turns-windsurf-into-devin-desktop-with-a-30-faster-local-agent): medium credibility. One more churn example; S025 covers churn.
- Bolt: Check your project's security (undated, https://support.bolt.new/building/security.md): IDOR and business-logic misuse are covered by S042 and S045. "Stop clicking fix and investigate" is noted.
- Human-in-the-loop for AI tool calls (n8n) (undated, https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools): approval gates are covered by S068 and S053.
- AGENTS.md (undated, https://agents.md/): what the file is, covered by S005 and S022.
- Using Claude Code with your Pro or Max plan (undated, https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan): subscription vs API pools are covered by S016 from the same vendor docs.
- Models overview (Claude Platform Docs) (undated, https://platform.claude.com/docs/en/about-claude/models/overview): a price table whose facts change monthly. Fetch it when a lesson is made.
- Reasoning models (OpenAI API docs) (undated, https://developers.openai.com/api/docs/guides/reasoning): same mechanism as S013.
- Harness, Scaffold, and the AI Agent Terms Worth Getting Right (Hugging Face, 2026-05-25, https://huggingface.co/blog/agent-glossary): medium credibility. Harness vocabulary is covered by S002.
- Agent Skills overview (agentskills.io) (undated, https://agentskills.io/home): skills are covered by S015 and S022.
- Using memory in Claude (Claude Help Center) (undated, https://support.claude.com/en/articles/11817273-using-memory-in-claude): memory types are covered by S011. Product-specific memory behavior is flagged below.
- Demystifying evals for AI agents (Anthropic, 2026-01-09, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): aimed at people building agents. "Grade the outcome, not the claim" is covered by S030.
- Vision (Claude Platform Docs) (undated, https://platform.claude.com/docs/en/build-with-claude/vision): "images cost tokens and are resent each turn" is flagged below.

### Beyond code
- OpenClaw: How the Viral AI Agent Became 2026's First Major Security Crisis (Hive Security, 2026-05-07, https://hivesecurity.gitlab.io/blog/openclaw-ai-agent-security-crisis-2026/): medium credibility. Malicious skills and exposed gateways are read at the source (S071 and its companion).
- Every OpenClaw Security Incident So Far (2025-2026) (Sliq, undated, https://getsliq.com/blog/openclaw-security-incidents-timeline): medium credibility. "No reliable remote kill switch" is flagged below.
- openclaw-security-news (2026-07-20, https://github.com/joylarkin/openclaw-security-news): link list.
- How to build safer AI agents with Zapier MCP (undated, https://zapier.com/blog/openclaw-claude-cowork-zapier-mcp/): vendor webinar. Scoped app actions are covered by S053.
- Using threat modeling and prompt injection to audit Comet (Trail of Bits, 2026-02-20, https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/): "summarize this page" leading to exfiltration is covered by S070 and S049.
- Top 6 Claude in Chrome Security Risks to Model Before You Roll It Out (CSA, 2026-09-04, https://cloudsecurityalliance.org/blog/2026/09/04/top-6-claude-in-chrome-security-risks-to-model-before-you-roll-it-out): medium credibility, a republished vendor blog. Covered by S070.
- EY retracts cyber report littered with AI errors (2026-05-19, https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html): fabricated citations are covered by S072 and S073.
- PagerDuty Report Finds Two-Thirds (66%) of Office Professionals Have Used Unauthorized AI Tools at Work (2026-06-11, https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/): medium credibility vendor survey. Shadow AI and pasting work data into public tools are flagged below. S069's companion covers training and retention settings.
- The twilight of the chatbots (Mollick, 2026-06-30, https://www.oneusefulthing.org/p/the-twilight-of-the-chatbots): covered by the same author's newer S068.

### Papers
- Is Vibe Coding Safe? (SUSVIBES) (2025-12-02, https://arxiv.org/abs/2512.03262): over 10 months old. Its "57% functionally correct, 11.8% secure; vulnerability hints did not help" is covered by S038-S040. It is a counterpoint to the twin-prompt study, flagged below.
- Vibe Coding and Web Application Security: A Twin-Prompt Study (2026-08-21, https://arxiv.org/abs/2608.20963): medium credibility, single author. "Security appears when asked" is covered by S039. "Manual testing found the most severe issue" is flagged below.
- Anthropic Education Report: The AI Fluency Index (2026-02-23, https://academy.claude.com/tutorials/the-ai-fluency-index): "evaluative behaviors drop when users build artifacts" is flagged below. Covered in spirit by S085.
- Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants (2026-09-17, https://arxiv.org/abs/2609.20143): medium credibility intervention study aimed at tool designers.
- Comprehension Debt in GenAI-Assisted Software Engineering Projects (2026-04-14, https://arxiv.org/abs/2604.13277): medium credibility. The concept is covered by S084.
- From Technical Debt to Cognitive and Intent Debt (Storey, 2026-03-23, https://arxiv.org/abs/2603.22106): the "intent debt" vocabulary is flagged below.
- Judgment-Centred Software Engineering Education (2026-09-24, https://arxiv.org/abs/2609.29473): medium credibility education framework. Explain / verify / modify / account could shape the course's own checks.
- "I'm Not Reading All of That" (2026-03-15, https://arxiv.org/abs/2603.14225): medium credibility. "Engagement drops while the agent runs" is covered by S085.
- The Work Behind Delegation: A Framework for Supervising AI Coding Agents (2026-09-21, https://arxiv.org/abs/2609.24234): medium credibility. The supervision stages are covered by S029 and S030.
- How Researchers Use and Verify AI Coding Assistants (2026-09-18, https://arxiv.org/abs/2609.22049): medium credibility. "It ran, so it's right" is covered by S030 and S085.
- Sonar 2026 State of Code Developer Survey: verification gap (press release, 2026-01-08, https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/): duplicate of the Sonar report.
- AI Hallucination from Students' Perspective: A Thematic Analysis (2026-01-11, https://arxiv.org/abs/2602.17671): medium credibility. The "AI as a database" misconception is covered by S011.
- Empowering Learners for the Age of AI: EC-OECD AILit (2026-06-18, https://ailiteracyframework.org/blog/empowering-learners-for-the-age-of-ai-literacy-framework/): a competency map for school learners, not builder gaps.
- AI Fluency for builders / the 4D Framework (Claude Academy) (undated, https://academy.claude.com/courses/ai-fluency-for-builders): duplicate of S007.
- The Impact of Generative AI on Critical Thinking (Microsoft Research, 2025-04): superseded by S085. URL in the finder notes: https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
- "Can you feel the vibes?": novice programmer engagement with vibe coding (2025-12-02, https://arxiv.org/abs/2512.02750): medium credibility. Covered by S085.
- AI competency framework for students (UNESCO, 2024-08-08, https://www.unesco.org/en/articles/ai-competency-framework-students): too old, and aimed at school students.

### AI literacy
- Effective context engineering for AI agents (Anthropic, 2025-09-29, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): context engineering is taught in S003 (2026-09).
- Context Engineering in 2026: Why We Stopped Compacting Our Agent's Context (Bouchard, 2026-08-18, https://www.louisbouchard.ai/context-engineering-2026/): medium credibility. The compaction-vs-cache cost trade-off is covered by S012's caching companion and S017.
- We're going to need default hard budget caps on pretty much everything (Willison, 2026-10-03, https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/): medium credibility. Soft vs hard caps are covered by S020's companion. Which providers now offer hard caps is flagged below as a fact to recheck.
- Claude Haiku 5.5 (Willison, 2026-10-07, https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/): medium credibility. "A new tokenizer is a hidden price increase" and tiered long-context pricing are flagged below.
- Why Language Models Hallucinate (2025-09-04, https://arxiv.org/abs/2509.04664): the hallucination-centred picture is what Aaron sent back (S004). S006 and S011 carry the current framing.
- Parrots to Pigeons: How generating the next token became the way LLMs work through a problem (2026-09-18, https://www.b2bnn.com/2026/09/parrots-to-pigeons-how-generating-the-next-token-became-the-way-llms-work-through-a-problem/): medium credibility. Reasoning as written-out working memory is covered by S011 and S013.
- Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things (Willison, 2026-08-16, https://simonwillison.net/2026/Aug/16/qwen-38-27b/): medium credibility. It is the only local-model source and is flagged below.
- The Lethal Trifecta Is Already on Your Laptops (Coder talk, 2026-10-10, https://www.youtube.com/watch?v=abw_m-DRi1k): medium credibility, the only video candidate. Same concept as S049 applied to laptops. The VM kill switch is flagged below.

### Aaron's practice (kept: S004, S017, S026, S032, S062)
- AO-029: I asked where I was supposed to learn all this (2026-10-01, https://aaronorelup.com/ledger/the-missing-map/): the course's origin. Its gap list is the existing curriculum.
- AO-041: Claude made a 40-minute lesson on Loom (2026-10-07, https://aaronorelup.com/ledger/loom-and-information-flow/): about the method (deliver an expert's credited work clearly), not a gap source.
- AO-042: For two months no video on my site could skip ahead (2026-10-08, https://aaronorelup.com/ledger/every-video-can-seek/): "a workaround hides the root cause" and "local dev server differs from production" are flagged below.
- AO-019: An agent confessed to deleting 19 GB I had asked another agent to delete (2026-09-26, https://aaronorelup.com/ledger/the-confession-that-spread/): "agent self-reports are not evidence" is covered by S064. "Several sessions on one machine can't see each other's changes" is flagged below.
- AO-017: An autopilot winning is not a person playing (2026-09-22, https://aaronorelup.com/ledger/blackwater-2-postmortem/): the same lesson as S032, which is newer. Tests that enter through side doors are noted.
- AO-030: Claude rendered 223 clips of my game's robot voice, and couldn't hear any of them (2026-10-02, https://aaronorelup.com/ledger/remora-voice-lab/): the same lesson as S032 (the agent cannot judge taste or sound).
- AO-044: Nine Claudes painted the same picture in oil (2026-10-11, https://aaronorelup.com/ledger/nine-claudes-one-painting/): effort and model tiers on a creative task. Effort as a cost multiplier is covered by S017. "Verification trades creativity for accuracy" is flagged below.
- AO-014: I had 801 agent transcripts and no way to read them (2026-09-01, https://aaronorelup.com/ledger/reading-my-own-agents/): a tooling story. "Unknown cost must show as unknown, never $0" is noted.
- AO-032: I told Claude to find the best Opus 5.5 trick on X and do it without me (2026-10-03, https://aaronorelup.com/ledger/opus-55-on-x-alone/): autonomy boundaries are covered by S068. "Time rules need a timer, not a promise" is flagged below.
- AO-011: I don't learn programming anymore (2026-08-08, https://aaronorelup.com/ledger/i-dont-learn-programming-anymore/): "operating, not programming" is already the course premise.
- Playback: the course's origin prompt (2026-09-30): its gap list is the existing curriculum.
- Playback: Aaron's corrections to the first lessons (2026-10-02): the same corrections as S004.
- Playback: the rework brief (2026-10-12): this research's own charter.
- Playback: what 'Opus 5.5 made this' videos leave out (2026-10-03): a lesson idea (the connectors and asset pipelines behind "one prompt" results). Flagged below.
- Playback: a session the finder marked sensitive (2026-09-01): not for citation, and its notes stay out of the public repo. Its topics are flagged below: WSL, containers with no network, loopback vs LAN binding.
- Playback: running many agents on one PC (2026-10-08): flagged below (one Node process tree and MCP servers per session).
- Playback: 'how do I know it's going to work on anyone else's computer?' (2026-09-25): a question, not an answer source. Flagged below for a finder.
- Playback: the agent's own setup (2026-10-07): skills vs commands vs plugins vs MCP is covered by S015.
- Playback: 'The blog post is for people who don't know' (2026-10-07): feedback on explainer writing (the method, not a gap). The SynthID-Text claim is Anthropic's, relayed, and is noted.

---

## Gaps only named by dropped sources (for a later finder or lesson pass)

None of these is backed by a selected source. Each needs a current source before it is taught.

- **Shipping to other people's machines.** Installers, uninstallers, auto-update, testing on a machine that is not yours (Aaron's playback question, 2026-09-25). No candidate answers it.
- **Local models.** A local model is a file plus a runtime plus settings, and the defaults decide the experience (Willison on Qwen 3.8, 2026-08-16). This is the only local-model candidate.
- **Multimodal costs.** Images cost tokens and are resent every turn of an agent loop (Claude Vision docs). Aaron lists multimodal as a gap in S004.
- **Many sessions on one machine.** One process tree and MCP servers per session, and sessions that can't see each other's changes (Playback 2026-10-08; AO-019).
- **Tokenizer changes as hidden price increases**, and tiered long-context pricing (Willison on Haiku 5.5, 2026-10-07).
- **Hard spending caps now arriving** at cloud providers (Willison, 2026-10-03). The list of providers needs rechecking at lesson time.
- **Apps public by default and indexed by search engines; shadow AI** (RedAccess, 2026-05-07; PagerDuty, 2026-06-11).
- **Agents improvising a publishing workaround** that leaks private data (PixelLeak, 2026-10-02).
- **Plugin and hook updates turning a pinned, trusted plugin malicious** (Plugin4Shell, in Adversa's 2026-10-02 roundup).
- **AI assistant config files as malware persistence; uninstalling the package does not remove it** (Mini Shai-Hulud, 2026-05-17).
- **No reliable remote kill switch** for an always-on agent (Sliq, undated); a VM kill switch (Coder talk, 2026-10-10).
- **"Harmless-looking" tool commands that are destructive**, such as a Prisma shadow database pointed at production (IT-Connect, 2026-07-30).
- **The agent treating a question ("can you change this?") as permission** (Cursor forum 168209).
- **Old storage left after a migration is still live**, and privacy-policy promises vs what the system keeps (Tea app, 2026-07-08).
- **Typed languages make agent output checkable** (Octoverse 2025).
- **Agent confidence does not predict safe changes; refactors are riskier than new code** (Safer Builders, Risky Maintainers, 2026-03-29).
- **"Act as a security expert" persona prompts performed worse; short specific rules beat copied rule sets** (OpenSSF, 2025-08-01).
- **Manual testing found the most severe issue that scanners missed** (twin-prompt study, 2026-08-21). SUSVIBES (2025-12) found that vulnerability hints did not help, which is the counterpoint.
- **Your account type decides whether a tool works at all** (Gemini CLI consumer cut-off, 2026-05-19).
- **Pick a popular stack the AI was trained on** (roadmap.sh); **app anatomy for reviewing AI output; targeted vs structural change** (roadmap.sh AI Product Builder, 2026-07-13).
- **Try a single LLM call or a hardcoded workflow before building an agent** (PostHog, 2026-03-24).
- **Redo your own past work with an agent to learn its limits** (Hashimoto, 2026-02-05).
- **Vocabulary worth checking against current sources:**
  - "normalization of deviance" (Willison, 2026-05-06);
  - "guides vs sensors" (Böckeler, 2026-04-02);
  - "intent debt" (Storey, 2026-03-23);
  - "AI brainfry" or supervision fatigue (State of Devs, 2026-10-03).
- **Course-design ideas:**
  - disclose AI contributions and check team AI norms (Missing Semester: Beyond the Code);
  - deliberately break code to confirm CI catches it (Missing Semester: Code Quality);
  - the "just for me / my team / the world" audience levels (Replit Learn);
  - explain / verify / modify / account as checks (Judgment-Centred SE Education);
  - "verification trades creativity for accuracy" (AO-044);
  - "time rules need a timer, not a promise" (AO-032);
  - the connectors and asset pipelines behind "one prompt" results (Playback 2026-10-03);
  - workarounds that hide the root cause, and a local dev server that behaves differently from production (AO-042);
  - work-laptop agent setup topics: WSL, no-network containers, loopback vs LAN binding (Playback 2026-09-01, sensitive);
  - "evaluative behaviors drop when users build artifacts" (AI Fluency Index, 2026-02-23).
