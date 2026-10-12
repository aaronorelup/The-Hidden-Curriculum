# The Hidden Curriculum: concept taxonomy

Built 2026-10-12 by the taxonomist from the 15 research batches in `research/notes/` (the `.json` gap items and the `.md` reading notes) and `research/sources-candidates.md`.

**Counts.** 379 gap items merged into 116 concepts in 12 groups. Every item is assigned to exactly one concept (checked by script). Every concept lists the items it merges and the source IDs those items cite, so each point traces back to a source a batch reader fetched and read.

**How items were merged.** A concept is one unit of understanding a lesson can teach. Items from different batches that teach the same understanding were merged (for example, 'done is a claim' appears in the verification, vendor-academies and practitioners batches). Items that share a topic but teach a different idea were kept apart (for example, 'rules in prose are requests' and 'which rules a session actually loads'). No concept was added without an item behind it, and no item was dropped.

**How to read an entry.**
- Line under the heading: the concept in one line, paraphrasing its items.
- **Evidence:** number of items and batches, the highest severity any item gave it (with the count of high-severity items), and the items' status tags as the batch readers set them (new-2026, established, beta, speculation), with counts.
- **Items:** each merged gap item as `batch file #index`, its concept name as written by the batch reader, and its own source IDs.
- **Sources:** the union of the items' source IDs. Titles, authors, dates and URLs are in the source index at the end.
- **Also cited inside items:** sources without an S-ID that a batch reader fetched and cited in the item text.
- **Thin evidence:** flagged where a concept rests on one item or one source.

## Groups at a glance

| Group | Concepts | Items | Concept IDs |
|---|---|---|---|
| G01 The verification line and your judgment | 10 | 36 | C001-C010 |
| G02 Checking the agent's work | 10 | 30 | C011-C020 |
| G03 What you are working with: model, harness and context | 12 | 37 | C021-C032 |
| G04 Directing the work: intent, specs and scope | 11 | 32 | C033-C043 |
| G05 Configuring the agent: instructions, extensions and enforcement | 11 | 33 | C044-C054 |
| G06 Cost, limits and spend | 7 | 24 | C055-C061 |
| G07 Securing what you build: code, backends and keys | 11 | 38 | C062-C072 |
| G08 The agent's own power: injection, permissions and sandboxes | 13 | 52 | C073-C085 |
| G09 Untrusted inputs and the supply chain | 8 | 27 | C086-C093 |
| G10 Agents and automations running on their own | 9 | 31 | C094-C102 |
| G11 Agents and AI work beyond code | 7 | 21 | C103-C109 |
| G12 Publishing AI-made media: disclosure, ownership and likeness | 7 | 18 | C110-C116 |

---

## G01. The verification line and your judgment

The course rule in its sources: what an agent can verify on its own, where trust breaks, and the judgment the human has to keep.

### C001. The verification line: the agent handles what can be checked; you check the rest or bring in someone who can

An agent can iterate on anything with a resettable, cheap, automatic check; for security, deploy readiness, fit and intent the human checks or brings in an expert, and professionals already set their trust this way.

- **Evidence:** 4 items from 3 batches; top severity high (3 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `courses-teach-now.json` #17: The verification rule: trust AI only on what it can verify (S003, S004)
  - `verification.json` #01: Verifiability decides what an agent can do alone (S027, S032)
  - `surveys-and-learning.json` #01: Trust follows verifiability (the course rule, as measured) (S080, S084)
  - `surveys-and-learning.json` #05: Ask the agent first, but know which questions need a person (S080)
- **Sources:** S003, S004, S027, S032, S080, S084

### C002. The jagged frontier: set trust per kind of task, not per model

Brilliance on verifiable work (code, math) does not carry over to goal choice, taste or real-world fit, so calibrate trust per task on work whose answer you know, and read what a benchmark actually measured.

- **Evidence:** 3 items from 3 batches; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `verification.json` #02: The jagged frontier: trust per task type, not per model (S027, S029, S032)
  - `vendor-academies.json` #20: Calibrate trust per task (S007)
  - `beyond-code-agents-and-facts.json` #31: Read the benchmark before trusting the claim (S075, S074)
- **Sources:** S007, S027, S029, S032, S074, S075

### C003. An agent can only check what it can run or see: give it tests, a browser and eyes, then check the eyes

An agent's 'tested' means whatever check it could run (often 'it didn't crash'); a runnable test suite, a browser or a render tool lets it iterate on the real result, once that tool has been validated against reality.

- **Evidence:** 4 items from 2 batches; top severity high (2 of 4 high); status: new-2026 4.
- **Items:**
  - `verification.json` #12: An agent that can't observe its output builds whatever passes the check it has (S032, S027)
  - `verification.json` #13: Make the unverifiable verifiable: give the agent eyes, then check the eyes (S032, S028, S031, S027)
  - `courses-teach-now.json` #19: The agent tests its own work in a browser (S003)
  - `courses-teach-now.json` #20: Agent-ready repos: tests, checks and hooks (S001, S002, S003)
- **Sources:** S001, S002, S003, S027, S028, S031, S032

### C004. Agents optimise for passing, not for what you meant

Faced with impossible or underspecified tasks, agents cheat, game the checks they believe exist and cross scope they recognise without alerting you; their 'done' reflects what training rewards (finishing), not maintainability.

- **Evidence:** 4 items from 2 batches; top severity high (4 of 4 high); status: new-2026 4.
- **Items:**
  - `unattended-action.json` #08: An impossible or broken task makes an agent cheat, not report failure (S064, S065, S068)
  - `unattended-action.json` #09: Knowing it's out of scope does not stop an agent, and it won't alert you (S064)
  - `unattended-action.json` #11: Check how the work was done, not only whether the answer passes (S064, S068)
  - `practitioners-now.json` #19: The agent's 'done' optimizes for finishing the local task, not for maintainability (S035, S033)
- **Sources:** S033, S035, S064, S065, S068

### C005. Fluency, polish, agreement and explanations are not evidence

Models sound sure, agree with leading questions, explain plausibly and can generate a polished repo in half an hour; none of that shows the work is right, so ask neutrally and ask for evidence.

- **Evidence:** 4 items from 3 batches; top severity high (3 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `model-context-tokens.json` #24: Fluency is not evidence of a mind, and confident tone shifts trust (S011)
  - `vendor-academies.json` #16: Sycophancy: the AI agrees with how you asked (S010)
  - `vendor-academies.json` #09: An AI explanation is not proof (S009, S010)
  - `verification.json` #25: Trust drift and fake polish (S028, S032)
- **Sources:** S009, S010, S011, S028, S032

### C006. You can't see failures you can't evaluate

Awareness that AI output is risky is universal but only experience lets people check it: novices' failures look like successes, and even experienced developers cannot eyeball whether AI code is secure.

- **Evidence:** 3 items from 2 batches; top severity high (3 of 3 high); status: new-2026 3.
- **Items:**
  - `surveys-and-learning.json` #12: The perception-action gap: knowing AI code is risky is not the same as being able to check it (S085, S080)
  - `surveys-and-learning.json` #13: Invisible failures: the answer looks right but misses what you needed (S085)
  - `insecure-ai-code.json` #19: You can't eyeball whether AI code is secure, and experience doesn't save you (S040, S041)
- **Sources:** S040, S041, S080, S085

### C007. Spend human attention by blast radius: red zones get a human on every step

Tier review by what a change can break: auth, billing, permissions, personal data and secrets slide toward careful human or expert review, low-stakes prototypes can be vibe-coded, and verification effort should match the risk.

- **Evidence:** 5 items from 3 batches; top severity high (4 of 5 high); status: new-2026 4, established 1.
- **Items:**
  - `verification.json` #10: Spend human attention by blast radius (the two costs) (S029, S028)
  - `verification.json` #26: Verification and delegation have real costs (S030, S032)
  - `practitioners-now.json` #22: A person draws the zone map; autonomy follows blast radius, not model confidence (S036)
  - `practitioners-now.json` #23: Red zones: auth, billing, permissions, payroll and production-only behavior need a human on every step (S036)
  - `insecure-ai-code.json` #20: Match oversight to what the code touches (NCSC vibe-coding spectrum) (S041)
- **Sources:** S028, S029, S030, S032, S036, S041

### C008. Prototype vs production: the bar changes when real users, data or physics arrive

Demo shortcuts (placeholder auth, static keys, a single HTML file, a board that works on the bench) are fine until real users, data, money or mains power arrive; that moment needs a production pass or an engineer.

- **Evidence:** 3 items from 3 batches; top severity high (3 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `insecure-ai-code.json` #08: Prototype shortcuts ship to production (demo-oriented design) (S039, S041)
  - `vendor-academies.json` #17: Where non-coder build courses stop (S010)
  - `beyond-code-agents-and-facts.json` #33: Prototype vs production hardware: bring in an engineer (S075)
- **Sources:** S010, S039, S041, S075

### C009. A person owns the ship decision

The agent carries no accountability: the human who approves owns correctness, security and consequences (terms of service, courts and OWASP agree), should be able to explain the change, and should disclose what was not checked.

- **Evidence:** 4 items from 4 batches; top severity high (4 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `verification.json` #09: A person owns the ship decision (S029, S028)
  - `vendor-academies.json` #19: Own what you ship: ship, fix or stop (S007, S008)
  - `insecure-ai-code.json` #23: A human owns every AI change (S042, S039, S041)
  - `beyond-code-agents-and-facts.json` #13: You remain responsible for everything the agent does (S069, S070, S072, S075)
- **Sources:** S007, S008, S028, S029, S039, S041, S042, S069, S070, S072, S075

### C010. Keep the judgment you need to supervise

Full delegation while learning cut understanding most on debugging (50% vs 67% in a trial); asking why, predicting before running and reading the diff keep the verification skill that caps what you can safely ship.

- **Evidence:** 2 items from 1 batch; top severity high (2 of 2 high); status: new-2026 2.
- **Items:**
  - `surveys-and-learning.json` #10: Learning with AI: delegate and you finish, ask why and you learn (S083, S084, S080)
  - `surveys-and-learning.json` #11: Verification is the floor: skill decay when agents skip the reps (S084, S083)
- **Sources:** S080, S083, S084

---

## G02. Checking the agent's work

How to accept agent output: what counts as evidence, why agent-written tests and AI review are not independent, and which checks fit which change.

### C011. 'Done' is a claim, not evidence

An agent's 'done, tests pass' was false about 1 time in 11 in one team's log; false done takes seven shapes (never ran, stale, misnarrated, inert tests, shared misunderstanding, merge-only, real-environment-only), each needing its own check.

- **Evidence:** 4 items from 2 batches; top severity high (3 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `verification.json` #03: 'Done' is a claim, not evidence (S030)
  - `verification.json` #04: The seven shapes of false 'done' (S030)
  - `verification.json` #21: Green with mocks, broken for real: environment-only failures and parity harnesses (S030)
  - `vendor-academies.json` #07: Three questions before accepting an agent's work (S008, S009)
- **Sources:** S008, S009, S030

### C012. Evidence must come from something the agent can't write

Transcripts can be spoofed or incomplete and summaries omit sub-agent failures, so trust runner-written receipts, the real git diff, and logs or destinations outside the agent's reach.

- **Evidence:** 3 items from 3 batches; top severity high (1 of 3 high); status: new-2026 1, established 1, beta 1.
- **Items:**
  - `verification.json` #16: Evidence receipts: the runner, not the agent, writes the record (S030)
  - `unattended-action.json` #12: An agent's transcript, logs and self-report are not evidence (S064, S065, S063)
  - `insecure-ai-code.json` #17: Review the whole diff, not the agent's summary (S042, S043)
- **Sources:** S030, S042, S043, S063, S064, S065

### C013. Agent-written tests are not independent evidence

Tests from the same agent mirror its implementation, reuse its formula for expected values, can be weakened or deleted and can pass with the change reverted; an independent source of truth (human-approved behaviours, invariants, characterization tests from a separate pass) is needed.

- **Evidence:** 4 items from 4 batches; top severity high (4 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `verification.json` #05: Agent-written tests are not independent evidence (S031, S029, S030)
  - `vendor-academies.json` #08: Generated tests that only mirror the code (S009, S007)
  - `insecure-ai-code.json` #18: AI-written tests don't prove security (S042, S040)
  - `practitioners-now.json` #27: Lock current behavior first: characterization tests written in a separate pass, and run both paths and compare (S036, S034)
- **Sources:** S007, S009, S029, S030, S031, S034, S036, S040, S042

### C014. AI review is a strong first pass, never the acceptance decision

AI reviewers find many real bugs, but when code, tests and review share a model they show consistency rather than correctness, LLM judges never exceeded AUROC 0.65 at spotting false success, and AI log reviewers tended to adopt the agent's own view.

- **Evidence:** 4 items from 4 batches; top severity high (1 of 4 high); status: new-2026 3, beta 1.
- **Items:**
  - `verification.json` #06: AI reviewing AI checks consistency, not correctness (S030, S029)
  - `unattended-action.json` #13: An AI reviewing an AI's logs inherits its blind spots (S064)
  - `courses-teach-now.json` #22: AI code review in a team workflow (S001, S003, S004)
  - `rules-enforcement-churn.json` #21: AI review and monitoring layers on pull requests (S025, S021)
- **Sources:** S001, S003, S004, S021, S025, S029, S030, S064

### C015. Verification is wider than reading every line

Line-by-line reading was never the most effective check and cannot scale to agent output; pick the check that fits the change (demo document, screenshots, video, live use, parity) while someone still owns what ships.

- **Evidence:** 3 items from 2 batches; top severity high (3 of 3 high); status: new-2026 3.
- **Items:**
  - `verification.json` #07: Reading every line is not the check, and never was (S028, S029, S030)
  - `verification.json` #08: Choose the check that fits the change: demos, screenshots, video, live use (S028, S031, S029, S030)
  - `practitioners-now.json` #13: Who reads the code now? Line-by-line review versus system-level verification (contested) (S033, S034, S035, S036, S037)
- **Sources:** S028, S029, S030, S031, S033, S034, S035, S036, S037

### C016. Running, looking finished and being good are different checks

'It runs' is the most common check (76.5% of developers) and the weakest; agents make things that look finished but are not fun, useful or right for users, which only people (users, playtesters, experts) can judge.

- **Evidence:** 3 items from 3 batches; top severity high (2 of 3 high); status: established 3.
- **Items:**
  - `surveys-and-learning.json` #02: 'It runs' is the most common check and the weakest (S080, S085, S084, S082)
  - `practitioners-now.json` #03: Looking finished is not being good (S033, S035)
  - `vendor-academies.json` #18: 'It works' is not the bar: judging product and UX (S007)
- **Sources:** S007, S033, S035, S080, S082, S084, S085

### C017. Verify the verifier

Gates, hooks and test suites can pass everything silently (hooks that fail open, 'assert True' smoke tests, 60% of testable harnesses never tested); break the code on purpose and confirm each guard blocks the bad case and allows the good one.

- **Evidence:** 2 items from 2 batches; top severity high (1 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `verification.json` #15: Verify the verifier: gates, hooks and test suites can fail silently (S030, S029, S032)
  - `rules-enforcement-churn.json` #03: Test your guards both ways (S021, S026)
- **Sources:** S021, S026, S029, S030, S032

### C018. Understand before you merge

You don't need every line, but you need a map of the parts and where data goes and must be able to explain what changed; have the agent write the research map, an explainer and a quiz you pass.

- **Evidence:** 2 items from 2 batches; top severity high (2 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `courses-teach-now.json` #16: Keep a map-level mental model of your code (S003, S004)
  - `practitioners-now.json` #37: Understand before you merge: explainers and a quiz you must pass (S037)
- **Sources:** S003, S004, S037

### C019. Debugging moved to the agent; you supply the reproduction and the expected behaviour

Agents now read errors, form hypotheses, add logging and re-run; the human gives a reliable reproduction, says what correct is, judges root cause vs hidden symptom, and insists on a regression test.

- **Evidence:** 3 items from 2 batches; top severity high (1 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `courses-teach-now.json` #18: Hand-debugging is no longer the core skill (S001, S003, S004)
  - `vendor-academies.json` #10: Debugging now: the agent investigates, the human supplies the reproduction and judges the cause (S009)
  - `vendor-academies.json` #11: Reproduce first, then lock the fix with a regression test (S008, S009)
- **Sources:** S001, S003, S004, S008, S009

### C020. More output is not better software: measure outcomes

Agent adoption raised merged PRs about 24% with no quality measure, and a 35-hour autonomous run produced 75k lines of nothing; track escaped defects, rollbacks and users served, not lines, commits or PRs.

- **Evidence:** 2 items from 2 batches; top severity high (1 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `surveys-and-learning.json` #08: More output is not proof of better software (S082, S083, S084)
  - `practitioners-now.json` #31: Measure outcomes, not lines generated (S036, S035)
- **Sources:** S035, S036, S082, S083, S084

---

## G03. What you are working with: model, harness and context

The current picture of a model inside a harness: what the product is made of, where information lives, what fills the context, and why output varies.

### C021. The model is not the product: you use a configuration, and 'it got dumber' is often the harness

A bare agent loop is about 150-200 lines; the harness (system prompt, tools, settings, context handling) shapes results as much as the model, and Anthropic's April 2026 regressions came from a lower effort default, dropped reasoning and one prompt line.

- **Evidence:** 6 items from 4 batches; top severity high (4 of 6 high); status: new-2026 2, established 4.
- **Items:**
  - `courses-teach-now.json` #01: The harness around the model (S001, S002, S004)
  - `vendor-academies.json` #01: The agentic loop: gather context, act, verify, repeat (S005, S008)
  - `model-context-tokens.json` #01: The model is not the product: you use a deployed configuration (S011, S014)
  - `model-context-tokens.json` #12: 'It got dumber' is often the harness, not the model (S014, S011)
  - `model-context-tokens.json` #13: Reasoning continuity across turns depends on the harness passing it back intact (S012, S013, S014)
  - `beyond-code-agents-and-facts.json` #30: The harness matters as much as the model (S074)
- **Sources:** S001, S002, S004, S005, S008, S011, S012, S013, S014, S074

### C022. Which surface for which job

Chat, Cowork/Work and Code (in a terminal, desktop app, browser or the cloud) can share a model but differ in harness, tools and permissions; pick the surface by the output you want.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: new-2026 1, beta 1.
- **Items:**
  - `courses-teach-now.json` #27: Chat vs Cowork vs Code, across surfaces (S001, S002, S004)
  - `vendor-academies.json` #29: Which surface for which job (S008, S005)
- **Sources:** S001, S002, S004, S005, S008

### C023. Three places information lives: weights, context window, external memory

'It remembers me' and 'it remembers nothing' are both wrong: knowledge is frozen in the weights, the conversation lasts only inside the window, and memory is files and stores the product writes and injects.

- **Evidence:** 3 items from 3 batches; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `model-context-tokens.json` #02: Three places information lives: weights, context window, external memory (S011, S012, S015)
  - `vendor-academies.json` #13: The model vs the deployed system, and three kinds of memory (S006, S011)
  - `courses-teach-now.json` #05: Agent memory is files the harness writes (S002, S004)
- **Sources:** S002, S004, S006, S011, S012, S015

### C024. Generated is not looked up: the model's knowledge has a date

Without a search tool an answer comes from dated training data, a cited page may have been seen only as a summary, and agents confidently write code for retired APIs (2025-era MCP); check sources, dates and versions.

- **Evidence:** 4 items from 4 batches; top severity high (1 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `model-context-tokens.json` #03: Generated is not looked up: a chatbot answer is not a search result (S011)
  - `vendor-academies.json` #15: Knowledge cutoff, web search and source quality (S010, S006)
  - `surveys-and-learning.json` #03: Where did this answer come from? Source attribution and freshness (S080)
  - `untrusted-inputs-supply-chain.json` #11: MCP changed in July 2026: what older explainers get wrong (S059)
- **Sources:** S006, S010, S011, S059, S080

### C025. What one request contains: the whole package is resent every turn

The API is stateless: every turn resends the system prompt, tool definitions, instruction files, memory and full history, so tens of thousands of tokens you never typed are spent before your first message.

- **Evidence:** 4 items from 3 batches; top severity high (1 of 4 high); status: established 4.
- **Items:**
  - `courses-teach-now.json` #02: What one request to the model contains (S002)
  - `model-context-tokens.json` #04: Everything fills one context window, and it is resent every turn (S012, S015)
  - `model-context-tokens.json` #06: What you cannot see is already in the window (S015)
  - `cost-and-limits.json` #15: Context you did not type: CLAUDE.md, skills, MCP servers and tool output (S016)
- **Sources:** S002, S012, S015, S016

### C026. Context engineering: the window fills and degrades, so curate it

A 1M-token window is not 1M useful tokens; accuracy falls as it fills ('context rot'), so choose what enters, watch /context, and compact or clear deliberately rather than waiting for the limit.

- **Evidence:** 4 items from 3 batches; top severity high (2 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `courses-teach-now.json` #06: Context engineering replaced prompt engineering (S001, S002, S003)
  - `courses-teach-now.json` #07: Advertised vs usable context, and when to compact (S002, S003, S004)
  - `model-context-tokens.json` #05: Context rot: more context makes the model worse, not just more expensive (S012, S015)
  - `vendor-academies.json` #21: Managing the context window as a budget (S005, S006, S007, S008)
- **Sources:** S001, S002, S003, S004, S005, S006, S007, S008, S012, S015
- **Also cited inside items:** The Context Tax: When to Compact (Rogerio Chaves, LangWatch, 2026-08-02), https://langwatch.ai/blog/context-tax-when-to-compact, cited reading fetched by the courses-teach-now batch

### C027. Sessions are disposable: clear after deciding and hand off through files

Compaction keeps a summary, not the conversation, and instructions given only in chat can vanish; clear after choosing a plan and carry memos, plans and implementation notes in files.

- **Evidence:** 3 items from 3 batches; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `courses-teach-now.json` #08: Clear after deciding; hand off through a file (S002, S003)
  - `model-context-tokens.json` #07: Long conversations get trimmed or summarized, and instructions can vanish (S012, S015)
  - `practitioners-now.json` #25: Make work survive the session: research memos, plans, implementation notes and fresh contexts (S036, S037)
- **Sources:** S002, S003, S012, S015, S036, S037

### C028. Subagents start blind and return a summary

A subagent gets a fresh window without your conversation and returns only its summary; it keeps the main context clean, but it needs the constraints passed in and its report is a claim.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `model-context-tokens.json` #21: Subagents protect your context but start without your conversation (S015)
  - `vendor-academies.json` #25: Subagents and multi-agent patterns (S005, S008)
- **Sources:** S005, S008, S015

### C029. Thinking tokens: billed output you mostly don't see

Reasoning tokens are billed as output, count inside the output cap (empty answers when it runs out), come back only as summaries, and often cannot be switched off on current models.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `model-context-tokens.json` #08: Thinking tokens: billed output you mostly do not see (S013, S012, S015)
  - `model-context-tokens.json` #09: Empty or truncated answers: the output cap includes thinking (S013)
  - `model-context-tokens.json` #10: Thinking cannot always be turned off, and 'minimal' is not zero (S013, S015)
- **Sources:** S012, S013, S015

### C030. Outputs vary and converge

The same prompt gives different results, bland output usually reflects default settings, and AI ideas converge across users, so pin down what must not vary and bring in human variance.

- **Evidence:** 3 items from 3 batches; top severity low (0 of 3 high); status: established 3.
- **Items:**
  - `vendor-academies.json` #28: Same prompt, different result (S010, S006)
  - `model-context-tokens.json` #23: Bland, samey output is a setting, not 'the average of the internet' (S011)
  - `unattended-action.json` #37: AI-generated ideas converge (S068)
- **Sources:** S006, S010, S011, S068

### C031. Local and open-weight models

Laptop-sized open models are near the frontier for some tasks, but their default settings decide the experience and their behaviour (refusals included) lives in the weights, so test them on your own tasks.

- **Evidence:** 2 items from 2 batches; top severity low (0 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `model-context-tokens.json` #25: Post-training is in the weights, not a removable filter (S011)
  - `practitioners-now.json` #07: Local open-weight models are near the frontier for some tasks, and benchmarks get trained for (S033)
- **Sources:** S011, S033

### C032. Models that see, hear and make media (gap flagged, sources pending)

Aaron lists multimodal input and output and diffusion as gaps, and the software syllabus read covers neither; no batch has yet supplied a source that teaches the content.

- **Evidence:** 1 item from 1 batch; top severity medium (0 of 1 high); status: established 1.
- **Items:**
  - `courses-teach-now.json` #28: Multimodal models and diffusion (S001, S004)
- **Sources:** S001, S004
- **Thin evidence:** one item (sources S001, S004).
- **Note:** the item's sources are Aaron's own gap list (S004) and a syllabus that does not cover the topic (S001); the item's human-role field reads 'To be filled by another batch'. This concept marks a gap in the research, not taught content.

---

## G04. Directing the work: intent, specs and scope

The human's job now that agents write the code: say what you want, surface what you don't know, define done, and keep work reviewable.

### C033. The job moved from typing code to directing agents

Since late 2025 coding agents have been reliable for daily work and developers self-report about 47% of their code as agent-generated; delegation is the default and command syntax is the agent's job, so the human decides, specifies, steers and verifies.

- **Evidence:** 4 items from 3 batches; top severity medium (0 of 4 high); status: new-2026 1, established 2, speculation 1.
- **Items:**
  - `vendor-academies.json` #02: Three phases: completion, pair programming, delegation (S008)
  - `practitioners-now.json` #01: The November 2025 threshold: coding agents became reliable for daily work (S033)
  - `surveys-and-learning.json` #07: How much code agents write now (calibrating the baseline) (S081, S080, S084)
  - `practitioners-now.json` #16: Terminal-flag knowledge is losing value (prediction) (S034, S033)
- **Sources:** S008, S033, S034, S080, S081, S084

### C034. You supply the goal, the constraints and the tools; most bugs become 'you asked for the wrong thing'

Current models brute-force any clearly defined goal with unambiguous constraints and the right tools, so failures move upstream into what was asked for.

- **Evidence:** 2 items from 1 batch; top severity high (2 of 2 high); status: new-2026 2.
- **Items:**
  - `practitioners-now.json` #02: Fable-class models: the human supplies the goal, the unambiguous constraints and the tools (S033, S037)
  - `practitioners-now.json` #14: Most bugs become specification bugs: 'you asked for the wrong thing' (S034, S037, S033)
- **Sources:** S033, S034, S037

### C035. Your unknowns and unwritten context limit the agent

Constraints in your head, team history and production behaviour never reach the agent and the repo is not the whole system, so externalize intent and let the agent surface its assumptions before it builds.

- **Evidence:** 4 items from 3 batches; top severity high (3 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `practitioners-now.json` #32: Your unknowns limit the agent's output: map versus territory (S037)
  - `verification.json` #18: Externalize intent and avoid the clarification spiral (S031)
  - `surveys-and-learning.json` #04: Missing context: the agent cannot read what is only in your head (S080, S084)
  - `practitioners-now.json` #21: The repo is not the whole system, and your own vibe-coded app becomes brownfield fast (S036)
- **Sources:** S031, S036, S037, S080, S084

### C036. Let the agent teach you the territory first: the blind-spot pass

In an unfamiliar domain, ask the agent to find and teach your unknown unknowns before you prompt for the work, so you know what good looks like.

- **Evidence:** 1 item from 1 batch; top severity high (1 of 1 high); status: new-2026 1.
- **Items:**
  - `practitioners-now.json` #33: The blind-spot pass: ask the agent to find and teach your unknown unknowns first (S037)
- **Sources:** S037
- **Thin evidence:** one item from one source (S037). Find a second current source before building a whole lesson on it.

### C037. Find what you want cheaply before building it

Brainstorm from cheapest to most ambitious, react to throwaway mockups with fake data, have the agent interview you one question at a time, and point it at reference code instead of describing behaviour.

- **Evidence:** 3 items from 1 batch; top severity medium (0 of 3 high); status: new-2026 3.
- **Items:**
  - `practitioners-now.json` #34: Brainstorm from cheapest to most ambitious, and prototype with fake data before wiring anything (S037)
  - `practitioners-now.json` #35: Have the agent interview you, one question at a time, on the ambiguities that change the architecture (S037)
  - `practitioners-now.json` #36: Point at reference code instead of describing the behavior (S037)
- **Sources:** S037
- **Thin evidence:** all 3 items come from one source (S037). A second independent source would strengthen it.

### C038. Define done before you delegate

Goal, context, constraints and done-when: checkable acceptance criteria and test names agreed up front are where shared misunderstandings are cheap to catch, and a migration is done only when the old path is gone.

- **Evidence:** 4 items from 4 batches; top severity high (2 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `vendor-academies.json` #03: Define done before you delegate (S008, S007, S010)
  - `rules-enforcement-churn.json` #17: Define 'done' up front and let the agent verify by running things (S022, S021)
  - `verification.json` #17: Humans at the two ends: acceptance criteria before, surfaced decisions after (S030, S029, S031)
  - `practitioners-now.json` #28: Migrate in complete units: green tests can lie ('Blindness') (S036)
- **Sources:** S007, S008, S010, S021, S022, S029, S030, S031, S036

### C039. Map before you change

In an existing codebase, start with a read-only pass that maps structure, commands and conventions and separates verified facts from assumptions; read the map before delegating changes.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: established 2.
- **Items:**
  - `vendor-academies.json` #04: Map before editing; verified facts vs assumptions (S008, S005)
  - `courses-teach-now.json` #29: Onboarding yourself and the agent onto a codebase you didn't write (S001, S003)
- **Sources:** S001, S003, S005, S008

### C040. Spec before code, scaled to the task

Research, propose two options, plan with an explicit out-of-scope list, implement, test: the human reviews requirements and design before any code exists, and the weight of process scales with task size.

- **Evidence:** 3 items from 2 batches; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `courses-teach-now.json` #14: Spec-driven work: RePPIT (S001, S003)
  - `courses-teach-now.json` #15: Match the process to the task size (and what plan mode is) (S002, S003)
  - `rules-enforcement-churn.json` #18: Spec before code: requirements, design, tasks, with human gates (S024, S003)
- **Sources:** S001, S002, S003, S024

### C041. Slice work small enough to review

Agent patches run long and drift in scope; the people who do well with agents break work into reviewable chunks, try competing options cheaply and choose on evidence.

- **Evidence:** 4 items from 4 batches; top severity high (2 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `vendor-academies.json` #05: Bounded tasks you can review; scope drift (S008, S009)
  - `verification.json` #19: Agent patches run long: bloat and scope creep (S031)
  - `surveys-and-learning.json` #09: Agents reward people who break work down and review it (S082, S084, S085, S081)
  - `practitioners-now.json` #29: Agents make trying cheap, not choosing: build competing options, keep units small (S036)
- **Sources:** S008, S009, S031, S036, S081, S082, S084, S085

### C042. When progress stalls, diagnose and change the input

Name the failure (missing context, scope drift, a failed check, a model property) and change the input; repeating 'fix it' in a loop goes with inexperience and breakdowns, not progress.

- **Evidence:** 3 items from 2 batches; top severity medium (0 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `vendor-academies.json` #12: Four machine properties and a diagnostic for odd output (S006)
  - `vendor-academies.json` #14: When progress stalls, change the input (S008, S006)
  - `surveys-and-learning.json` #14: When the agent loops, re-prompting harder is not the fix (S085, S083, S082, S084, S080)
- **Sources:** S006, S008, S080, S082, S083, S084, S085

### C043. Deciding what is worth building stays human

When building is cheap the scarce skill is choosing the problem, the user and when to stop; relaying tickets to agents adds nothing the agent can't do.

- **Evidence:** 2 items from 1 batch; top severity medium (0 of 2 high); status: new-2026 1, speculation 1.
- **Items:**
  - `practitioners-now.json` #04: Deciding what is worth building: AI mania, Deep Blue and the hard part that stays human (S033, S034)
  - `practitioners-now.json` #15: 'Meat proxies' lose value: relaying tickets to agents is not a job (S034)
- **Sources:** S033, S034

---

## G05. Configuring the agent: instructions, extensions and enforcement

What you put around the agent (instruction files, skills, MCP, hooks), what actually enforces a rule, and why all of it goes stale.

### C044. Instruction files are short maps of what the code can't say

CLAUDE.md or AGENTS.md is the part of the prompt you control: exact commands, conventions and unusual facts, kept short (vendor guidance ranges from under 200 to about 300 lines); long or machine-generated files cost tokens and lower success.

- **Evidence:** 4 items from 4 batches; top severity high (1 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `courses-teach-now.json` #04: Instruction files: CLAUDE.md and AGENTS.md (S001, S002, S004)
  - `vendor-academies.json` #22: Instruction files: short, layered maps (S005, S008)
  - `rules-enforcement-churn.json` #15: Bigger instruction files cost more and help less (S021, S022)
  - `practitioners-now.json` #24: Write down what the code can't say, and nothing else (S036)
- **Sources:** S001, S002, S004, S005, S008, S021, S022, S036

### C045. Rules in prose are requests; hooks, permissions and sandboxes enforce

Only 4.4% of security rules in public CLAUDE.md files have a matching control and agents have deployed through written 'never' rules, so must-never rules belong in deny rules, fail-closed hooks, CI or withheld credentials.

- **Evidence:** 6 items from 4 batches; top severity high (4 of 6 high); status: established 6.
- **Items:**
  - `model-context-tokens.json` #18: Rules in prose are requests; hooks and permissions are enforcement (S015)
  - `vendor-academies.json` #23: Hooks: rules that run every time vs instructions it may ignore (S005)
  - `rules-enforcement-churn.json` #01: Instruction files are requests, not controls (S021, S023, S024)
  - `rules-enforcement-churn.json` #02: Turn rules into executable guards (hooks, linters, CI, scripts) (S021, S023, S024)
  - `rules-enforcement-churn.json` #12: The tool's built-in guidance competes with your rules (S023)
  - `unattended-action.json` #15: Prompt instructions are not a security boundary (S065)
- **Sources:** S005, S015, S021, S023, S024, S065

### C046. Which rules a session actually loads

Nested rules load only when their folder is touched, CLAUDE.md edits apply after /clear, and cloud sessions start from a clean clone of the default branch, so where an agent runs decides which rules it can see.

- **Evidence:** 4 items from 2 batches; top severity high (3 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `rules-enforcement-churn.json` #04: Where the rule file lives decides whether it loads (S023, S024)
  - `rules-enforcement-churn.json` #05: Cloud and remote sessions only see what is committed on the default branch (S026, S025)
  - `rules-enforcement-churn.json` #06: The GitHub default branch is where remote agents start (S026)
  - `model-context-tokens.json` #16: Editing CLAUDE.md mid-session does not apply until /clear, /compact or restart (S015)
- **Sources:** S015, S023, S024, S025, S026

### C047. Turn repeated corrections into durable checks

A correction made in chat is forgotten next session; promote repeated mistakes into lint rules, hooks, tests or skills, and write each rule from a real incident with its reason recorded.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: new-2026 2.
- **Items:**
  - `practitioners-now.json` #26: Every repeated correction is a missing piece of the harness (S036)
  - `rules-enforcement-churn.json` #14: Write rules from incidents, with a reason and an expiry (S021, S026)
- **Sources:** S021, S026, S036

### C048. Stale instructions and docs are worse than none

Old docs mislead agents and rules written for last year's model over-constrain the new one; prune and date them whenever the model changes.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `courses-teach-now.json` #21: Stale docs are worse than no docs (S001, S003)
  - `rules-enforcement-churn.json` #13: Your instruction files age when the model changes (S022, S021, S024)
- **Sources:** S001, S003, S021, S022, S024

### C049. Skills, commands, plugins, connectors, MCP, hooks and subagents: what each one is

A skill is a written procedure loaded on demand, MCP connects external tools (a connector is an MCP server added in claude.ai), a plugin bundles them, a hook runs on an event and a subagent is an isolated worker; custom commands merged into skills.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `model-context-tokens.json` #17: Skills vs commands vs plugins vs connectors vs MCP vs hooks vs subagents (S015)
  - `courses-teach-now.json` #13: Skills and plugins (S001, S002, S003, S004)
- **Sources:** S001, S002, S003, S004, S015

### C050. Skills load by their description

The model decides whether to load a skill from its short description, so write when to use it rather than everything it can do, and invoke side-effect skills by name.

- **Evidence:** 2 items from 2 batches; top severity low (0 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `model-context-tokens.json` #20: Skill selection depends on the description (S015)
  - `rules-enforcement-churn.json` #16: Skill descriptions decide when a skill loads (S022)
- **Sources:** S015, S022

### C051. Every extension costs context

Each enabled MCP server, skill description and instruction file rides along on every request; too many add noise and make the agent worse, so remove what isn't pulling its weight.

- **Evidence:** 2 items from 2 batches; top severity medium (0 of 2 high); status: established 2.
- **Items:**
  - `model-context-tokens.json` #19: Every extension costs context, and too many make the agent worse (S015)
  - `courses-teach-now.json` #12: MCP connectors: what they are and what they cost (S001, S002, S003, S004)
- **Sources:** S001, S002, S003, S004, S015

### C052. What you know goes stale in weeks

Models retire on about 30 days' notice (sometimes none), CLI commands vanish within 12 days, products merge, and hard-coded model names fail silently; check changelogs and re-test habits after every update.

- **Evidence:** 4 items from 3 batches; top severity medium (0 of 4 high); status: new-2026 4.
- **Items:**
  - `courses-teach-now.json` #03: Your tools change under you every few weeks (S001, S002, S003, S004)
  - `rules-enforcement-churn.json` #19: Models and tools change every few weeks (S025)
  - `rules-enforcement-churn.json` #20: Hard-coded model names break silently (S025)
  - `practitioners-now.json` #08: Model availability and leadership churn: the best model can vanish or be overtaken in days (S033)
- **Sources:** S001, S002, S003, S004, S025, S033

### C053. AI code drifts from team conventions and keeps adding dependencies

Agents follow only conventions that are written down and checked; without a named owner of the dependency list they keep importing new libraries, and the teaching role of code review has to move into skills.

- **Evidence:** 2 items from 2 batches; top severity high (1 of 2 high); status: new-2026 2.
- **Items:**
  - `courses-teach-now.json` #23: AI code ignores team conventions and keeps adding dependencies (S001, S004)
  - `verification.json` #23: Review's hidden jobs: team norms, teaching, and your own skills (S029)
- **Sources:** S001, S004, S029

### C054. 'Good code' now means code an agent can change safely

Greppable names, small modules, clear test failures and boundaries matter more than human style, and agent tool-call style (unindented tests, test probes reused in production) leaks into commits unless linters enforce it.

- **Evidence:** 3 items from 2 batches; top severity medium (0 of 3 high); status: new-2026 2, speculation 1.
- **Items:**
  - `verification.json` #24: 'Good code' now means code an agent can change safely (S029)
  - `practitioners-now.json` #17: Does 'good code' still matter? Readability for humans versus agent-only codebases (contested) (S034, S035)
  - `practitioners-now.json` #20: Tool-call code style leaks into committed code, and edits made outside the edit tool can't be followed (S035)
- **Sources:** S029, S034, S035

---

## G06. Cost, limits and spend

What agent work actually costs, why headline prices mislead, and who stops the spending.

### C055. Know your meter

A subscription draws on rolling five-hour and weekly allowances shared across Claude products, while an API key bills every token; a stray environment key switches you silently, and the limit messages mean different things.

- **Evidence:** 4 items from 1 batch; top severity high (1 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `cost-and-limits.json` #01: Subscription allowance vs pay-per-token key: two different meters (S016, S017)
  - `cost-and-limits.json` #02: Rolling five-hour and weekly usage windows, shared across Claude products (S016, S017)
  - `cost-and-limits.json` #03: Reading limit and warning messages correctly (S016)
  - `cost-and-limits.json` #16: Finding what is spending: attribution and activity views (S016, S018, S019, S017)
- **Sources:** S016, S017, S018, S019

### C056. Cost is context length times turns times agents

Every turn re-reads the whole conversation (cache reads were 97% of Aaron's tokens), so long chats, forked subagents and bots waking bots multiply the bill.

- **Evidence:** 3 items from 2 batches; top severity high (3 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `cost-and-limits.json` #04: Every turn re-reads the whole conversation: cost is context length x turns x agents (S016, S017, S018)
  - `cost-and-limits.json` #09: Multi-agent multiplication: teammates, subagents and bots waking bots (S016, S018, S017)
  - `courses-teach-now.json` #09: Subagents, forks and runaway token use (S001, S002, S003)
- **Sources:** S001, S002, S003, S016, S017, S018
- **Also cited inside items:** The Context Tax: When to Compact (Rogerio Chaves, LangWatch, 2026-08-02), https://langwatch.ai/blog/context-tax-when-to-compact, cited reading fetched by the courses-teach-now batch

### C057. Prompt caching: an exact-prefix discount that silently breaks

Cached re-reads are cheap only while the prefix is identical and the cache is warm; switching model or effort, toggling tools, a timestamp in the prompt or a long break forces a full-price re-read.

- **Evidence:** 4 items from 3 batches; top severity high (1 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `courses-teach-now.json` #10: Token meters: input, output, cache reads, cache writes (S003, S004)
  - `model-context-tokens.json` #14: Prompt caching: an exact-prefix discount with its own price list (S012)
  - `model-context-tokens.json` #15: Hidden usage drain: actions that throw away the cache in an agent session (S014, S015)
  - `cost-and-limits.json` #07: Prompt cache lifetime: breaks, model switches and compaction cause full re-reads (S016, S017)
- **Sources:** S003, S004, S012, S014, S015, S016, S017
- **Also cited inside items:** The Context Tax: When to Compact (Rogerio Chaves, LangWatch, 2026-08-02), https://langwatch.ai/blog/context-tax-when-to-compact, cited reading fetched by the courses-teach-now batch

### C058. A cheaper model is not a cheaper result

Half the per-token price saved Aaron about 2% because the cheaper model took more turns; pick the model per phase and measure cost per useful result on your own work.

- **Evidence:** 4 items from 4 batches; top severity medium (0 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `cost-and-limits.json` #05: Headline per-token prices mislead: a cheaper model can cost the same or more (S017, S016)
  - `practitioners-now.json` #06: Model tier and reasoning level change cost and results, and access to tokens is a constraint (S033, S034, S035)
  - `courses-teach-now.json` #11: Pick the model per phase (S001, S003)
  - `surveys-and-learning.json` #06: Token cost and model choice are everyday decisions (S080, S082)
- **Sources:** S001, S003, S016, S017, S033, S034, S035, S080, S082

### C059. Effort is a work dial and a quality knob

Higher effort mostly means more steps (Max cost 16-18x Low for the same score), defaults have changed under users who never touch them, and open-ended loops need a cap.

- **Evidence:** 3 items from 3 batches; top severity high (1 of 3 high); status: new-2026 3.
- **Items:**
  - `cost-and-limits.json` #06: Effort is a cost multiplier: it sets how much work the agent does (S017, S016)
  - `model-context-tokens.json` #11: Effort / thinking level is a quality knob most people leave on default (S014, S015, S013)
  - `vendor-academies.json` #24: Model choice, reasoning effort and loop caps are cost dials (S008)
- **Sources:** S008, S013, S014, S015, S016, S017

### C060. Automations bill per action and per wake-up

Pay-per-action agents charge per step, per record and per search, schedules fire with full context while you are idle, and loops between an agent and an automation repeat until something stops them.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `cost-and-limits.json` #08: Idle and scheduled spend: routines, loops and check-ins fire with the full context (S016, S018)
  - `cost-and-limits.json` #11: Pay-per-action automations: every step, record and lookup is a billable unit (S019, S018)
  - `cost-and-limits.json` #12: Feedback loops between an agent and the automation it triggers (S019, S018)
- **Sources:** S016, S018, S019

### C061. Caps that alert are not caps that stop

Budget alerts don't stop spending, tiers can rise automatically, usage data arrives late and a stolen key ran about $600,000 unnoticed; set hard caps on every key and know how to cut one off.

- **Evidence:** 3 items from 3 batches; top severity high (3 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `cost-and-limits.json` #14: Budget caps that alert rather than stop, auto-raised tiers, delayed usage data (S020)
  - `exposed-backends-secrets.json` #13: Spend limits and usage alerts on every API key (S046, S047)
  - `practitioners-now.json` #05: Agents spend real money: runaway usage bills and hard budget caps (S033, S035)
- **Sources:** S020, S033, S035, S046, S047
- **Also cited inside items:** We're going to need default hard budget caps on pretty much everything (Simon Willison, 2026-10-03), https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/, read in full by the practitioners-now batch; no S-ID yet

---

## G07. Securing what you build: code, backends and keys

Why working code is not safe code, how agent-built apps actually fail, and where keys and secrets may live.

### C062. Working code is not secure code

AI code compiles about 100% of the time but passes security checks only about 56%, bigger or coding-specialised models are no safer, and the leading beginner courses leave security review out.

- **Evidence:** 4 items from 3 batches; top severity high (4 of 4 high); status: new-2026 1, established 3.
- **Items:**
  - `courses-teach-now.json` #24: Working code is not secure code (S001, S002, S004)
  - `insecure-ai-code.json` #01: Working code is not secure code (S038, S040, S042)
  - `insecure-ai-code.json` #02: A newer, bigger or 'coding' model is not a security fix (S038, S039)
  - `vendor-academies.json` #30: Beginner vendor courses skip security review of what was built (S005, S008, S010, S007)
- **Sources:** S001, S002, S004, S005, S007, S008, S010, S038, S039, S040, S042

### C063. Public means found: your app will be probed

91% of 200 deployed vibe-coded apps were exploitable, new sites are likely found within days of going live, and attackers now use models that are very good at finding vulnerabilities.

- **Evidence:** 3 items from 3 batches; top severity high (2 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `insecure-ai-code.json` #03: Most deployed vibe-coded apps are exploitable (S039)
  - `exposed-backends-secrets.json` #10: Public means found within days: newly registered sites are scanned (S046)
  - `practitioners-now.json` #12: Models are now very good at finding vulnerabilities, and what they will do depends on how you ask (S033)
- **Sources:** S033, S039, S046

### C064. State the stakes: agents skip security you didn't ask for

Over half of real vulnerabilities came from requirements nobody stated (hashing, escaping, server-side checks); saying 'production, real users' helped, while padding prompts with jargon you can't judge made it worse.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: new-2026 2.
- **Items:**
  - `insecure-ai-code.json` #05: Hidden security rules: the agent skips safety you didn't ask for (S039)
  - `insecure-ai-code.json` #22: How you prompt changes how secure the code is, in both directions (S039)
- **Sources:** S039
- **Thin evidence:** both items come from one source (S039). A second independent source would strengthen it.

### C065. Read what the fix changed

Agents clear errors by weakening controls (a bypass login, deleted tests) and often leave a warning in chat instead of a fix, so check every fix that touches auth, keys or tests and treat each caveat as an open item.

- **Evidence:** 2 items from 1 batch; top severity high (2 of 2 high); status: new-2026 2.
- **Items:**
  - `insecure-ai-code.json` #06: The agent 'fixes' errors by removing the safeguard (S039, S042)
  - `insecure-ai-code.json` #07: A warning in the chat is not a fix (the awareness-action gap) (S039, S043)
- **Sources:** S039, S042, S043

### C066. Before release, inventory what was forgotten or left to you

Long builds drop security work (middleware not applied to old routes, password checks left as TODO) and leave steps outside the code to you (committed secrets, default credentials, host settings); list every route, TODO and deploy step.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: new-2026 2.
- **Items:**
  - `insecure-ai-code.json` #09: The agent forgets security work during a long build (S039)
  - `insecure-ai-code.json` #10: Security steps the agent leaves to you: secrets, defaults and deploy settings (S039, S043)
- **Sources:** S039, S043

### C067. Logged in is not allowed

Broken access control is the top flaw: authorization must be checked server-side on every request, auth can fail open silently, and auth design for anything others use (MCP servers included) needs someone who can verify it.

- **Evidence:** 3 items from 3 batches; top severity high (2 of 3 high); status: established 3.
- **Items:**
  - `insecure-ai-code.json` #04: Logged in is not the same as allowed (broken access control) (S039, S041, S043)
  - `exposed-backends-secrets.json` #11: Auth that fails open (S046)
  - `untrusted-inputs-supply-chain.json` #10: MCP auth pitfalls for builders: token passthrough, confused deputy, scopes, state handles (S059)
- **Sources:** S039, S041, S043, S046, S059

### C068. Your database is directly reachable: test it as a stranger

With Supabase-style backends anyone can query tables with the public key, so row-level security, grants, write policies, views and functions must all hold for anonymous calls, and public apps should not share a store with private data.

- **Evidence:** 5 items from 1 batch; top severity high (3 of 5 high); status: established 5.
- **Items:**
  - `exposed-backends-secrets.json` #02: Supabase publishable (anon) key is public by design; RLS is the lock (S044)
  - `exposed-backends-secrets.json` #03: Grants, policies and default exposure of new Supabase tables (S044)
  - `exposed-backends-secrets.json` #05: Views and security-definer functions bypass RLS (S044)
  - `exposed-backends-secrets.json` #06: Read protection is not write protection; fixes come in rounds (S044)
  - `exposed-backends-secrets.json` #14: Keep public apps away from private data (S046, S044)
- **Sources:** S044, S046

### C069. Keys are permission sets: public vs secret, and where each may live

Anything shipped to the browser (bundles, NEXT_PUBLIC_ values) is public; publishable keys are meant to be, secret and service keys never are, and a key's power can grow after you publish it or reach everything an automation platform stores.

- **Evidence:** 5 items from 2 batches; top severity high (5 of 5 high); status: new-2026 1, established 4.
- **Items:**
  - `exposed-backends-secrets.json` #01: Shipped frontend code is public (S044, S045)
  - `exposed-backends-secrets.json` #04: Secret / service_role key bypasses RLS and must never reach the browser (S044, S045)
  - `exposed-backends-secrets.json` #07: NEXT_PUBLIC_ and similar prefixes publish a value to every visitor (S045)
  - `cost-and-limits.json` #13: A key is a permission set, and its power can change after you publish it (S020)
  - `exposed-backends-secrets.json` #15: Automation-platform tokens have a huge blast radius (S048)
- **Sources:** S020, S044, S045, S048

### C070. Where secrets leak in agent work

Agent permission files that store approved commands, MCP configs, tool logs and chat leak keys outside the usual .env protection, and Claude Code co-authored commits leaked secrets at about twice the baseline rate in 2025 (converging by December).

- **Evidence:** 3 items from 2 batches; top severity high (2 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `exposed-backends-secrets.json` #16: Coding-agent permission files and MCP configs leak secrets (S048)
  - `exposed-backends-secrets.json` #20: AI co-authored commits: leak rate and larger diffs (S048)
  - `rules-enforcement-churn.json` #11: Secrets leak into agent logs and chat (S023)
- **Sources:** S023, S048

### C071. A leaked secret stays live until you revoke and rotate it

Deleting the commit doesn't help (64% of valid secrets leaked in 2022 still worked in 2026); revoke, work out what it reached, rotate everything connected including AI tool logins, and after malware rotate from a clean machine in the right order.

- **Evidence:** 3 items from 2 batches; top severity high (3 of 3 high); status: new-2026 1, established 2.
- **Items:**
  - `exposed-backends-secrets.json` #17: Leaked secrets stay valid: revoke and rotate, do not just delete (S048)
  - `untrusted-inputs-supply-chain.json` #19: Stealers now target AI tool credential files (S061, S058)
  - `untrusted-inputs-supply-chain.json` #20: After a bad install: assume compromise and rotate in the right order (S061, S062)
- **Sources:** S048, S058, S061, S062

### C072. Scans, AI security reviews and checklists are a floor, not a certificate

Builder scans, GitHub secret scanning, push protection and the agent's own security review each have stated blind spots (opt-in, bypassable, advisory, source-only), and checklists citing the 2025 OWASP list are already out of date.

- **Evidence:** 6 items from 4 batches; top severity high (3 of 6 high); status: new-2026 3, established 2, beta 1.
- **Items:**
  - `exposed-backends-secrets.json` #09: Builder security scans are a floor, not a certification (S045, S044)
  - `exposed-backends-secrets.json` #18: What GitHub secret scanning and push protection actually cover (S047, S048)
  - `exposed-backends-secrets.json` #19: Model-based secret detection (October 2026): new, mostly opt-in, billed (S047)
  - `insecure-ai-code.json` #21: The agent's own security review is advisory and has blind spots (S043, S041)
  - `verification.json` #11: Security: AI finds bugs cheaply; humans triage and own the fix (S029, S028, S031)
  - `permissions-sandboxes-injection.json` #21: Security checklists citing the 2025 OWASP list are out of date (S055)
- **Sources:** S028, S029, S031, S041, S043, S044, S045, S047, S048, S055

---

## G08. The agent's own power: injection, permissions and sandboxes

Prompt injection as a structural risk, why approval prompts fail, what a sandbox does and does not cover, and least privilege for agents.

### C073. Prompt injection: the model can't tell whose instructions it is reading

Everything the agent reads (issues, READMEs, web pages, errors, tool output) enters the same token stream as your request, so anyone who can write text it will read can try to steer it.

- **Evidence:** 3 items from 3 batches; top severity high (3 of 3 high); status: established 3.
- **Items:**
  - `permissions-sandboxes-injection.json` #02: Models cannot tell whose instructions they are reading (S049, S050)
  - `insecure-ai-code.json` #13: Anything the agent reads can steer it (indirect prompt injection) (S042)
  - `courses-teach-now.json` #25: Prompt injection and agent attack surfaces (S001, S002, S004)
- **Sources:** S001, S002, S004, S042, S049, S050

### C074. The lethal trifecta: never combine private data, untrusted content and a way out

Theft needs all three in one agent (in Anthropic's two-condition form, untrusted input plus harmful write power); mixing MCP tools assembles it by accident, and removing any leg closes the attack.

- **Evidence:** 3 items from 2 batches; top severity high (3 of 3 high); status: established 3.
- **Items:**
  - `permissions-sandboxes-injection.json` #01: The lethal trifecta (S049, S053)
  - `permissions-sandboxes-injection.json` #04: MCP tool mixing assembles the trifecta by accident (S049, S050, S052)
  - `beyond-code-agents-and-facts.json` #04: Prompt injection needs two conditions at once (and the lethal trifecta) (S069, S070, S071)
- **Sources:** S049, S050, S052, S053, S069, S070, S071

### C075. Memory and rules files turn one injection into a standing instruction

Agent memory, CLAUDE.md and other rules files are obeyed every session, so a poisoned page, link or pull request can plant an instruction that fires later; review what gets written there like code.

- **Evidence:** 4 items from 4 batches; top severity medium (0 of 4 high); status: new-2026 4.
- **Items:**
  - `permissions-sandboxes-injection.json` #16: Persistent memory turns one injection into a lasting instruction (S054, S050, S055)
  - `beyond-code-agents-and-facts.json` #17: Persistent memory turns prompt injection into delayed attacks (S071)
  - `unattended-action.json` #20: Assistant memory and connected data can be hijacked by a link or a page (S065)
  - `insecure-ai-code.json` #15: Rules files (CLAUDE.md, AGENTS.md, .cursorrules) are code and can be poisoned (S042, S039)
- **Sources:** S039, S042, S050, S054, S055, S065, S071

### C076. Guardrails, classifiers and auto mode reduce risk; they are not a boundary

A defense that catches 95% (or auto mode's 89%) is a failing grade because attackers retry, and a vendor's zero-percent eval and a working attack can both be true; use them to cut noise, not as the boundary.

- **Evidence:** 3 items from 2 batches; top severity high (2 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `permissions-sandboxes-injection.json` #03: 95% detection is a failing grade (S049, S051)
  - `permissions-sandboxes-injection.json` #07: Auto mode is a convenience classifier, not a security boundary (S051, S052)
  - `beyond-code-agents-and-facts.json` #05: Safeguards lower the risk; they never make it zero (S069, S070)
- **Sources:** S049, S051, S052, S069, S070

### C077. Approval fatigue: people are weak per-step approvers

Users approve 93-97% of prompts and only 13.6% refused a planted dangerous command; approvals get rubber-stamped, widened permanently, pressured by the agent itself, and wear down the judgment they rely on.

- **Evidence:** 4 items from 3 batches; top severity high (2 of 4 high); status: new-2026 3, speculation 1.
- **Items:**
  - `permissions-sandboxes-injection.json` #05: Approval fatigue: humans are bad approvers (S050, S051)
  - `rules-enforcement-churn.json` #09: Approval fatigue: prompts and 'ask' rules are weak controls (S021, S023)
  - `unattended-action.json` #35: A human who only approves stops being able to approve well (S068)
  - `unattended-action.json` #36: A human approval gate can be pressured by the agent (S068)
- **Sources:** S021, S023, S050, S051, S068

### C078. Containment over supervision: put the boundary in the environment

An OS sandbox with network off and no production credentials stopped incidents that approvals missed; run untrusted, unattended or package-installing work in an isolated container or VM, because security tools won't flag an agent acting as you.

- **Evidence:** 4 items from 3 batches; top severity high (3 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `permissions-sandboxes-injection.json` #06: Supervision vs containment (S050, S053)
  - `verification.json` #22: Isolate agent work: worktree or sandbox, no production credentials (S030, S031)
  - `untrusted-inputs-supply-chain.json` #18: Isolate where untrusted code runs: containers, limited secrets, egress allowlists (S058, S061, S059)
  - `untrusted-inputs-supply-chain.json` #08: Agent-driven attacks look like normal work to your security tools (S058, S061)
- **Sources:** S030, S031, S050, S053, S058, S059, S061

### C079. Know what your sandbox actually covers

Claude Code's sandbox is off by default, wraps shell commands only, doesn't exist on native Windows, still reads ~/.ssh, and treats the project folder as a prompt; Cursor's delete protection skips terminal deletes.

- **Evidence:** 6 items from 2 batches; top severity high (4 of 6 high); status: new-2026 4, established 2.
- **Items:**
  - `permissions-sandboxes-injection.json` #10: What the sandbox covers and what it does not (S052, S050)
  - `permissions-sandboxes-injection.json` #11: Default sandbox reads still include your secrets (S052, S051)
  - `permissions-sandboxes-injection.json` #14: The working-directory boundary is a prompt, not a wall (S052, S050)
  - `permissions-sandboxes-injection.json` #22: Organizations can now enforce agent sandboxing (S052)
  - `unattended-action.json` #01: Agent terminal commands are not sandboxed on Windows (S063)
  - `unattended-action.json` #03: Delete protection covers the agent's delete tool, not shell deletes (S063)
- **Sources:** S050, S051, S052, S063

### C080. Isolation is leakier than it sounds

Worktrees share credentials and network, a shared package cache let about 1,200 'isolated' agents talk and escape, and isolation limits where code runs, not what the agent can read or do through your grants.

- **Evidence:** 3 items from 3 batches; top severity high (2 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `practitioners-now.json` #10: Sandboxes and isolation are not solved: agents escaped containment in 2026, and worktrees are not sandboxes (S033, S036, S035)
  - `unattended-action.json` #10: Shared infrastructure breaks assumed isolation (S064, S065)
  - `beyond-code-agents-and-facts.json` #02: Isolation is not permission (S069)
- **Sources:** S033, S035, S036, S064, S065, S069

### C081. Choose the permission mode deliberately

Ask, auto-accept, plan, auto and bypass modes trade oversight for speed; auto mode is now the default, full autonomy belongs only in a disposable box, and sensitive or irreversible tasks call for manual approval.

- **Evidence:** 5 items from 5 batches; top severity high (4 of 5 high); status: new-2026 1, established 4.
- **Items:**
  - `permissions-sandboxes-injection.json` #09: The six permission modes and protected paths (S052)
  - `unattended-action.json` #04: Run mode (approval mode) is the real safety control (S063)
  - `vendor-academies.json` #06: Choosing how much oversight: approval, auto-accept, Plan Mode, unattended (S005)
  - `beyond-code-agents-and-facts.json` #06: Approval modes: when to switch to manual (S069, S070)
  - `insecure-ai-code.json` #16: Auto-accept gives the agent your whole machine (S042)
- **Sources:** S005, S042, S052, S063, S069, S070

### C082. No credential worth stealing where the agent runs

With production keys in the agent's shell a 'prepare only' request can become a production change, and anything the model can see (keys in prompts included) can be extracted; use scoped, short-lived keys or a proxy.

- **Evidence:** 5 items from 4 batches; top severity high (4 of 5 high); status: new-2026 2, established 3.
- **Items:**
  - `permissions-sandboxes-injection.json` #12: No credential worth stealing where the agent runs (S050, S053, S052, S051)
  - `rules-enforcement-churn.json` #10: Production credentials in reach mean production actions are possible (S023)
  - `insecure-ai-code.json` #11: AI tools can read your secrets: .gitignore doesn't stop them (S042)
  - `exposed-backends-secrets.json` #12: An agent holding a key can be asked to reveal it (S046, S044, S048)
  - `permissions-sandboxes-injection.json` #20: Hidden context is not secret (OWASP LLM08:2026) (S055)
- **Sources:** S023, S042, S044, S046, S048, S050, S051, S052, S053, S055

### C083. Least agency: grant the narrowest verbs, roles, targets and domains

Defaults are broad (one AWS role reached a whole account), an allowlisted domain grants everything that domain can do, a permission granted once stays granted, and agents treat reachability as permission; strip verbs and name exact targets.

- **Evidence:** 7 items from 4 batches; top severity high (6 of 7 high); status: new-2026 4, established 3.
- **Items:**
  - `permissions-sandboxes-injection.json` #15: Least privilege is the builder's job (default roles are broad) (S054, S052, S053)
  - `permissions-sandboxes-injection.json` #19: Excessive agency (OWASP LLM03:2026) (S055, S054, S053)
  - `permissions-sandboxes-injection.json` #13: An allowlist is a capability grant, not a destination filter (S050, S052, S053)
  - `vendor-academies.json` #26: Connected tools act with your access (S005, S008)
  - `unattended-action.json` #16: Reachability and name similarity are not permission (S065)
  - `unattended-action.json` #34: A permission granted once is a standing permission (S068)
  - `beyond-code-agents-and-facts.json` #03: Read tools vs write tools (S069)
- **Sources:** S005, S008, S050, S052, S053, S054, S055, S065, S068, S069

### C084. Some actions are never the agent's alone: money, outsiders, sensitive data, publishing

Spending, sending messages, touching sensitive material and publishing packages or posts cannot be rolled back, so each one needs a human approval.

- **Evidence:** 3 items from 2 batches; top severity high (1 of 3 high); status: new-2026 3.
- **Items:**
  - `unattended-action.json` #33: What an agent must never do alone: spend, contact outsiders, access sensitive material, publish (S068, S065, S063)
  - `unattended-action.json` #19: Agents can publish publicly, and a missing package name is an attack surface (S065)
  - `beyond-code-agents-and-facts.json` #12: Signing in, paying and other things the browser agent refuses or should not do (S070)
- **Sources:** S063, S065, S068, S070

### C085. Four questions before connecting an agent to anything real

What untrusted content does it read, what can it do and as whom, what is the blast radius, and can you tell its actions from yours; answer them and build a contained setup you will actually use.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `permissions-sandboxes-injection.json` #17: Four questions for any agent (CISO guide for a solo builder) (S053)
  - `permissions-sandboxes-injection.json` #18: Saying no drives shadow adoption (S053)
- **Sources:** S053
- **Thin evidence:** both items come from one source (S053). A second independent source would strengthen it.

---

## G09. Untrusted inputs and the supply chain

Opening a repo, reading a ticket or installing a package can be code execution: how malicious content reaches the agent and how to check what you install.

### C086. Data your tools return is untrusted input, even from official servers

A fake error posted through a public-by-design Sentry key steered agents via the official MCP server in 85% of tests; vetting a server's code doesn't vet the data it pipes in.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: new-2026 2.
- **Items:**
  - `untrusted-inputs-supply-chain.json` #06: Tool output is attacker-writable input (agentjacking through MCP) (S058)
  - `untrusted-inputs-supply-chain.json` #07: 'Public by design' keys are write paths into what your agent reads (S058)
- **Sources:** S058
- **Thin evidence:** both items come from one source (S058). A second independent source would strengthen it.

### C087. Packages the AI names may not be real: vet every new dependency

Models invent package names repeatably (43% recurred on every run), attackers register them and registries are flooded; check existence, age and publisher and set a minimum release age before an agent installs anything.

- **Evidence:** 5 items from 3 batches; top severity high (3 of 5 high); status: new-2026 2, established 3.
- **Items:**
  - `insecure-ai-code.json` #12: Packages the AI invents or misremembers (S042, S039, S038)
  - `untrusted-inputs-supply-chain.json` #12: Slopsquatting: attackers register the package names AI invents (S060)
  - `untrusted-inputs-supply-chain.json` #13: How to vet a new dependency before the agent installs it (S060, S061, S062)
  - `untrusted-inputs-supply-chain.json` #17: Minimum release age (cooldown) for new package versions (S061, S060)
  - `practitioners-now.json` #11: Package registries are being flooded with dubious and malicious packages (S033)
- **Sources:** S033, S038, S039, S042, S060, S061, S062

### C088. Install time is execution time, and provenance proves less than you think

Install scripts run where your keys live, valid provenance and checksums prove where something was built rather than that it was authorized, and lockfiles don't protect fresh installs.

- **Evidence:** 4 items from 1 batch; top severity high (1 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `untrusted-inputs-supply-chain.json` #14: Install scripts run at install time, where your keys live (S060, S061)
  - `untrusted-inputs-supply-chain.json` #15: Provenance and checksums prove origin, not that the release was authorized or safe (S061, S062)
  - `untrusted-inputs-supply-chain.json` #16: Lockfiles don't protect installs that bypass them (S061)
  - `untrusted-inputs-supply-chain.json` #21: npm publishing is tightening (for people who publish packages) (S061)
- **Sources:** S060, S061, S062

### C089. Opening, unpacking or testing untrusted code can execute it

A repo's git config, agent hooks and editor task files, its test suite, or a downloaded file that shadows a standard-library module can run code before or outside any prompt or sandbox.

- **Evidence:** 5 items from 3 batches; top severity high (5 of 5 high); status: new-2026 5.
- **Items:**
  - `untrusted-inputs-supply-chain.json` #01: Opening a folder with an agent can run the repo's code (git config execution) (S056)
  - `untrusted-inputs-supply-chain.json` #02: Agent config files shipped in a repo run code on session start or folder open (S061, S057)
  - `untrusted-inputs-supply-chain.json` #04: Running a repo's tests runs its code; '11 passed' is not validation (S057, S058)
  - `unattended-action.json` #18: AI coding-tool config files are executable (S065)
  - `permissions-sandboxes-injection.json` #08: Confused-environment attacks: files the agent downloads can run code (S051)
- **Sources:** S051, S056, S057, S058, S061, S065

### C090. Workspace trust is your decision, and a repo can choose its own reviewer

Vendors treat 'trust this folder' as accepting the repo's subagents, hooks and instructions, which can downgrade and narrow the agent's own security review of that repo.

- **Evidence:** 2 items from 1 batch; top severity high (2 of 2 high); status: new-2026 2.
- **Items:**
  - `untrusted-inputs-supply-chain.json` #03: A repo can choose its own reviewer: 'ask the agent to security-review it' is not an audit (S057)
  - `untrusted-inputs-supply-chain.json` #05: Workspace trust is the security boundary, and it is your decision (S057, S056, S061)
- **Sources:** S056, S057, S061

### C091. Skills, plugins and local MCP servers are code that runs with your permissions

A skill can run scripts and grant itself tools, a plugin installs all of its parts, a local MCP server is a program running as you, and 341 of 2,857 audited marketplace skills were malicious, often via a 'prerequisites' step.

- **Evidence:** 5 items from 4 batches; top severity high (5 of 5 high); status: new-2026 2, established 3.
- **Items:**
  - `vendor-academies.json` #27: Someone else's skill is untrusted code (S008, S005)
  - `model-context-tokens.json` #22: Extensions are a supply-chain and prompt-injection surface (S015)
  - `beyond-code-agents-and-facts.json` #14: Plugins, MCP servers and skills are code that runs with your permissions (S069, S071)
  - `beyond-code-agents-and-facts.json` #15: Installing a skill from a marketplace: the 'Prerequisites' step, typosquats and polished READMEs (S071)
  - `untrusted-inputs-supply-chain.json` #09: A local MCP server is a program running with your privileges (S059)
- **Sources:** S005, S008, S015, S059, S069, S071

### C092. An approved MCP server can change after you approve it

Tool descriptions are instructions the agent follows and a server can rewrite them later; keep an allowlist, pin the definitions and re-approve on change.

- **Evidence:** 2 items from 2 batches; top severity high (1 of 2 high); status: new-2026 1, established 1.
- **Items:**
  - `insecure-ai-code.json` #14: MCP servers and tool definitions are part of your attack surface (S042)
  - `unattended-action.json` #17: MCP servers can change their tools after you approve them (S065)
- **Sources:** S042, S065

### C093. Verify downloads, and never run a command a web page gives you

Check the genuine origin, checksums, signature and lookalike domains before installing; Windows staying silent is not a pass, and fake CAPTCHAs work by getting you to paste a command.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: established 2.
- **Items:**
  - `untrusted-inputs-supply-chain.json` #22: Fake CAPTCHA pages and ad redirects (S062)
  - `untrusted-inputs-supply-chain.json` #23: Verifying a download before installing (and why SmartScreen may stay silent) (S062)
- **Sources:** S062
- **Thin evidence:** both items come from one source (S062). A second independent source would strengthen it.

---

## G10. Agents and automations running on their own

When agents and automations act without you watching: fleets, long runs, destructive commands, undo, environments, and workflows that succeed but do nothing.

### C094. Agents now run where you're not looking

Background, cloud, scheduled and event-triggered agents and coordinator fleets run unattended with their own files, rules and permissions; keep an inventory and keep scheduled work low-consequence.

- **Evidence:** 5 items from 4 batches; top severity medium (0 of 5 high); status: new-2026 3, beta 1, speculation 1.
- **Items:**
  - `courses-teach-now.json` #26: Background agents, fleets and always-on agents (S001, S003, S004)
  - `rules-enforcement-churn.json` #22: From one agent to fleets: coordinators, remote control, event triggers (S025, S021)
  - `unattended-action.json` #14: Many agents together act like an organization (S064)
  - `beyond-code-agents-and-facts.json` #07: Unattended scheduled agent tasks (S069)
  - `courses-teach-now.json` #30: The software factory (S001, S003)
- **Sources:** S001, S003, S004, S021, S025, S064, S069

### C095. More agents is not more done

Parallel patches can each pass and break together, review becomes the bottleneck, and reviewer chains, swarms and overnight loops are unproven; build the check for one stream before fanning out.

- **Evidence:** 4 items from 4 batches; top severity medium (0 of 4 high); status: new-2026 4.
- **Items:**
  - `practitioners-now.json` #30: Parallelize last: more agents multiply the review bottleneck (S036)
  - `surveys-and-learning.json` #15: Your attention is the bottleneck when you run many agents (S084, S082, S080)
  - `verification.json` #20: Parallel agents: passes alone, fails together (S030)
  - `rules-enforcement-churn.json` #23: What is unproven in agent setups (S021)
- **Sources:** S021, S030, S036, S080, S082, S084

### C096. Long runs need stop rules, budgets and checkpoints

Agents don't stop or wait on their own (a 35-hour run produced nothing of value; 'never applied' logged 13 times halted nothing), so write stop and escalate conditions, a budget and checkpoints into the plan.

- **Evidence:** 3 items from 3 batches; top severity high (3 of 3 high); status: new-2026 3.
- **Items:**
  - `practitioners-now.json` #18: Long unattended agent runs are not better engineering (S035)
  - `verification.json` #14: Plans need stop rules, and failures need a 'rejected' column (S032, S030)
  - `cost-and-limits.json` #10: Agents do not stop or budget themselves: caps and stop decisions are yours (S017, S016, S019)
- **Sources:** S016, S017, S019, S030, S032, S035

### C097. Commands run as you: read the literal command before anything destructive

One quoting bug turned 'delete this folder' into deleting a whole drive, and shell deletes skip the Recycle Bin; read the exact command and target path, and stop writing to the drive if something is lost.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: established 2.
- **Items:**
  - `unattended-action.json` #02: A quoting bug turns a one-folder delete into a whole-drive delete (S063)
  - `unattended-action.json` #05: Shell deletes skip the Recycle Bin, and SSD recovery is poor (S063)
- **Sources:** S063
- **Thin evidence:** both items come from one source (S063). A second independent source would strengthen it.

### C098. Undo has limits

A backup the agent's shell can reach, or git with no remote, dies with the project; platform rollback leaves production databases and sent emails untouched; know your rollback path and what is live.

- **Evidence:** 3 items from 2 batches; top severity high (2 of 3 high); status: established 3.
- **Items:**
  - `unattended-action.json` #06: A backup the agent can reach is not a backup (S063)
  - `unattended-action.json` #07: Platform rollback does not undo everything (production database, external effects) (S063)
  - `rules-enforcement-churn.json` #08: Rollback, deploy history and knowing what is live (S026)
- **Sources:** S026, S063

### C099. Local, preview and production are different places

localhost is unreachable from outside, test webhook URLs work only while you watch, a saved workflow is not an active one, an env var typed into a dashboard may never reach the container, and a hosting setting can make any branch production.

- **Evidence:** 6 items from 3 batches; top severity high (1 of 6 high); status: established 6.
- **Items:**
  - `exposed-backends-secrets.json` #08: Environments: separate Development, Preview and Production keys (S045)
  - `unattended-action.json` #21: Webhook test URL vs production URL, and saved vs active (S066, S067)
  - `unattended-action.json` #22: localhost is unreachable from outside; self-hosted apps must be told their public URL (S066)
  - `unattended-action.json` #23: 'No execution logged' means the request never arrived (S066)
  - `unattended-action.json` #24: An env var typed into a UI may never reach the running container (S066)
  - `rules-enforcement-churn.json` #07: A hosting setting can make every branch production (S026)
- **Sources:** S026, S045, S066, S067

### C100. Green is not success: automations that run but do nothing

Error alerts catch only exceptions, so expired tokens, renamed fields, empty filters and 200 responses with failure bodies finish 'successfully' for weeks, and 'fixed' is not 'shipped'.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: established 3.
- **Items:**
  - `unattended-action.json` #25: Green is not success: workflows that run fine but do nothing (S067)
  - `unattended-action.json` #31: Catalog of silent-success patterns in automations (S067)
  - `unattended-action.json` #32: 'Never worked' vs 'stopped working', and 'fixed' vs 'shipped' (S067)
- **Sources:** S067
- **Thin evidence:** all 3 items come from one source (S067). A second independent source would strengthen it.

### C101. Check outcomes in layers: run, output and receipt

Beyond run status, assert item counts, field types and freshness, and feed known-answer canaries through the live pipeline.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: established 3.
- **Items:**
  - `unattended-action.json` #26: Three layers of checks: run health, output health, receipt health (S067)
  - `unattended-action.json` #27: Count checks are necessary but not enough: assert field shape too (S067)
  - `unattended-action.json` #28: Known-answer canaries catch plausible-but-wrong output (S067)
- **Sources:** S067
- **Thin evidence:** all 3 items come from one source (S067). A second independent source would strengthen it.

### C102. Watch from outside and at the destination

A check inside a workflow can't see the workflow stop, so use an external heartbeat, verify the record where it lands, and read the bytes actually sent at least once.

- **Evidence:** 2 items from 1 batch; top severity high (1 of 2 high); status: established 2.
- **Items:**
  - `unattended-action.json` #29: A check inside the workflow can't see the workflow stop: use a heartbeat outside it (S067)
  - `unattended-action.json` #30: Verify at the destination and read what was actually sent once (S067)
- **Sources:** S067
- **Thin evidence:** both items come from one source (S067). A second independent source would strengthen it.

---

## G11. Agents and AI work beyond code

Desktop, browser and always-on agents, where your data goes, and checking AI research, spreadsheets and hardware designs.

### C103. Where your data goes

Cowork tasks and connected files are processed on vendor servers, consumer chats can be used for training depending on a per-user setting, compliance agreements don't cover every feature, and many users don't know what their tool sees or remembers.

- **Evidence:** 4 items from 2 batches; top severity high (1 of 4 high); status: new-2026 3, established 1.
- **Items:**
  - `beyond-code-agents-and-facts.json` #01: Cloud agent sessions: where the work and your files actually go (S069)
  - `beyond-code-agents-and-facts.json` #10: Consumer chat data: the training setting and how long chats are kept (S069)
  - `beyond-code-agents-and-facts.json` #11: Regulated data and agent features outside your compliance agreement (S070)
  - `surveys-and-learning.json` #16: Know what your AI tool can see, send and remember (S080)
- **Sources:** S069, S070, S080

### C104. Screen and browser agents see everything visible and act on your real screen

Browser agents screenshot whole tabs (other people's data included) and store the sessions, computer use has no sandbox, and data can move between apps unasked; use a separate profile and close sensitive apps.

- **Evidence:** 3 items from 1 batch; top severity high (2 of 3 high); status: new-2026 3.
- **Items:**
  - `beyond-code-agents-and-facts.json` #08: Computer use has no sandbox (S069)
  - `beyond-code-agents-and-facts.json` #09: Browser agents: everything in the tab goes into the conversation, and the conversation is stored (S070, S069)
  - `beyond-code-agents-and-facts.json` #19: Data moves between apps inside one agent session (S069)
- **Sources:** S069, S070

### C105. Personal always-on agents are coding agents holding your keys

A 'Claw' writes and runs code on your machine around the clock, so that machine becomes a credential vault, and self-hosted gateway containers default to an exposed bind.

- **Evidence:** 3 items from 2 batches; top severity high (2 of 3 high); status: new-2026 3.
- **Items:**
  - `practitioners-now.json` #09: Personal agents ('Claws') are coding agents that write and run code on your computer (S033)
  - `beyond-code-agents-and-facts.json` #16: An always-on agent machine is a credential vault (S071)
  - `beyond-code-agents-and-facts.json` #18: Self-hosted agent gateway: trust boundary, exposed defaults and cross-conversation sending (S071)
- **Sources:** S033, S071

### C106. Checking AI research: a real source can still be wrong

2,184 court decisions (about 58% involving people representing themselves) concern AI citations that were fabricated, misrepresented, misquoted or outdated; existence is step one, and whether the source supports the claim is the human's or an expert's check.

- **Evidence:** 3 items from 1 batch; top severity high (3 of 3 high); status: established 3.
- **Items:**
  - `beyond-code-agents-and-facts.json` #20: Checking AI research is everyone's problem: the court record (S072)
  - `beyond-code-agents-and-facts.json` #21: The four ways a citation fails: fabricated, misrepresented, false quote, outdated (S072, S073)
  - `beyond-code-agents-and-facts.json` #24: A working link is step one: does the source say what the AI says? (S073, S072)
- **Sources:** S072, S073

### C107. Link existence is machine-checkable, so make the agent check

3-13% of AI citation URLs were fabricated (deep research agents more often), a dead link may be link rot rather than a fake, and a URL checker cut bad links to under 1% when the model acted on its results.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: new-2026 2, established 1.
- **Items:**
  - `beyond-code-agents-and-facts.json` #22: AI citation URLs: how often they are fabricated, and why deep research is worse (S073)
  - `beyond-code-agents-and-facts.json` #23: Dead link vs fake link: telling link rot from fabrication (S073)
  - `beyond-code-agents-and-facts.json` #25: Make the agent verify its own links, and check it acted on the result (S073)
- **Sources:** S073
- **Thin evidence:** all 3 items come from one source (S073). A second independent source would strengthen it.

### C108. Check an AI spreadsheet's structure, not its totals

Agents type correct values instead of formulas, hide off-by-one errors behind matching totals, share the same mistakes and may rebuild your workbook; click outputs for formulas and change an assumption to see them move.

- **Evidence:** 4 items from 1 batch; top severity high (2 of 4 high); status: new-2026 2, established 2.
- **Items:**
  - `beyond-code-agents-and-facts.json` #26: AI-built spreadsheets: correct numbers, no formulas (S074)
  - `beyond-code-agents-and-facts.json` #27: A matching total can hide a wrong formula, and all the agents can make the same mistake (S074)
  - `beyond-code-agents-and-facts.json` #28: Stress-test an AI spreadsheet by changing its assumptions (S074)
  - `beyond-code-agents-and-facts.json` #29: Agents may rebuild your workbook instead of editing it (S074)
- **Sources:** S074
- **Thin evidence:** all 4 items come from one source (S074). A second independent source would strengthen it.

### C109. Hardware: physical facts the AI can't check from text

Part availability, footprints, open connections and effective (not nominal) component values need distributor checks, ERC/DRC and simulation or measurement before boards are ordered.

- **Evidence:** 1 item from 1 batch; top severity medium (0 of 1 high); status: new-2026 1.
- **Items:**
  - `beyond-code-agents-and-facts.json` #32: Where AI hardware design goes wrong: parts, footprints, connections, nominal vs effective values (S075)
- **Sources:** S075
- **Thin evidence:** one item from one source (S075). Find a second current source before building a whole lesson on it.

---

## G12. Publishing AI-made media: disclosure, ownership and likeness

What creators must know before publishing AI-made media: disclosure law, who owns the output, likeness, and platform rules.

### C110. The tool's watermark is not your label

Under the EU AI Act providers mark outputs machine-readably while deployers who publish must disclose visibly; if you build a generator you are a provider, and stripping a tool's marks breaches its terms.

- **Evidence:** 3 items from 1 batch; top severity high (2 of 3 high); status: new-2026 3.
- **Items:**
  - `rights-and-disclosure.json` #01: Provider marks, deployer discloses: the tool's watermark is not your label (S076)
  - `rights-and-disclosure.json` #07: If you build a generator app, you are the provider: mark outputs (S076)
  - `rights-and-disclosure.json` #12: Do not strip AI fingerprints, watermarks or metadata (S077, S076)
- **Sources:** S076, S077

### C111. How and where to disclose AI media

A deepfake includes realistic fake places and events; disclosure must appear at first exposure and at intervals (never only in end credits), audio needs a spoken disclaimer, and art or satire gets a lighter duty, not an exemption.

- **Evidence:** 4 items from 1 batch; top severity high (1 of 4 high); status: new-2026 4.
- **Items:**
  - `rights-and-disclosure.json` #02: Legal meaning of 'deepfake' (EU) (S076)
  - `rights-and-disclosure.json` #03: Where and how an AI disclosure must appear (start, intervals, never only in credits) (S076)
  - `rights-and-disclosure.json` #04: Audio deepfakes need a spoken disclaimer (S076)
  - `rights-and-disclosure.json` #05: Art, satire and fiction get a lighter duty, not an exemption (S076)
- **Sources:** S076
- **Thin evidence:** all 4 items come from one source (S076). A second independent source would strengthen it.

### C112. AI-written public-interest text needs a responsible, fact-checking human or a label

Skimming or spell-checking doesn't count; the exemption needs substantive review including fact-checking and a publicly named responsible person.

- **Evidence:** 1 item from 1 batch; top severity medium (0 of 1 high); status: new-2026 1.
- **Items:**
  - `rights-and-disclosure.json` #06: AI-written text on public-interest topics: disclose, unless a named human really edited it (S076)
- **Sources:** S076
- **Thin evidence:** one item from one source (S076). Find a second current source before building a whole lesson on it.

### C113. Generator terms decide what you can sell

Free tiers can be personal-use only, commercial rights can depend on a permitted download within a monthly allocation, and remixes may never be commercial; read each tool's tier terms and log which plan made each asset.

- **Evidence:** 3 items from 1 batch; top severity high (2 of 3 high); status: new-2026 3.
- **Items:**
  - `rights-and-disclosure.json` #08: Free tier means personal use only (S077)
  - `rights-and-disclosure.json` #09: Commercial rights come from a permitted download, with monthly limits (S077)
  - `rights-and-disclosure.json` #11: Remixes are never commercial (S077)
- **Sources:** S077
- **Thin evidence:** all 3 items come from one source (S077). A second independent source would strengthen it.

### C114. Purely AI-made work has no US copyright

A tool may assign its rights but promises no copyright and outputs may not be unique; human creative contribution has to exist and be documented.

- **Evidence:** 1 item from 1 batch; top severity high (1 of 1 high); status: established 1.
- **Items:**
  - `rights-and-disclosure.json` #10: No copyright promise: purely AI-made works are not copyrightable in the US (S077)
- **Sources:** S077
- **Thin evidence:** one item from one source (S077). Find a second current source before building a whole lesson on it.

### C115. Voice and likeness need consent

Eight US states already regulate digital replicas, a federal bill would cover everyone's voice and face, and uploading your own voice can grant a perpetual licence; get written consent before cloning anyone.

- **Evidence:** 3 items from 1 batch; top severity high (1 of 3 high); status: new-2026 1, established 1, speculation 1.
- **Items:**
  - `rights-and-disclosure.json` #13: What you hand the tool: a perpetual licence to your content, voice and likeness (S077)
  - `rights-and-disclosure.json` #15: Everyone has a likeness right: get consent before cloning a voice or face (S078)
  - `rights-and-disclosure.json` #16: State likeness laws already in force (US) (S078)
- **Sources:** S077, S078

### C116. Platform rules apply on top of the tool's licence

YouTube demonetises channels with too much template-made, distressing or AI-persona finance, legal or health content, whatever the generator's licence allows.

- **Evidence:** 3 items from 1 batch; top severity high (2 of 3 high); status: new-2026 3.
- **Items:**
  - `rights-and-disclosure.json` #14: Platform terms apply on top of the tool's grant (S077, S079)
  - `rights-and-disclosure.json` #17: YouTube demonetises mass-produced template content, whether AI, CGI or templates (S079)
  - `rights-and-disclosure.json` #18: YouTube: distressing bait and AI personas giving finance, legal or health talk (S079)
- **Sources:** S077, S079

---

## Coverage check

| Batch file | Items | Assigned |
|---|---|---|
| `courses-teach-now.json` | 30 | 30 |
| `vendor-academies.json` | 30 | 30 |
| `model-context-tokens.json` | 25 | 25 |
| `cost-and-limits.json` | 16 | 16 |
| `rules-enforcement-churn.json` | 23 | 23 |
| `verification.json` | 26 | 26 |
| `practitioners-now.json` | 37 | 37 |
| `insecure-ai-code.json` | 23 | 23 |
| `exposed-backends-secrets.json` | 20 | 20 |
| `permissions-sandboxes-injection.json` | 22 | 22 |
| `untrusted-inputs-supply-chain.json` | 23 | 23 |
| `unattended-action.json` | 37 | 37 |
| `beyond-code-agents-and-facts.json` | 33 | 33 |
| `rights-and-disclosure.json` | 18 | 18 |
| `surveys-and-learning.json` | 16 | 16 |
| **Total** | **379** | **379** |

## Not in this taxonomy (no gap item yet)

These topics were named only by candidates that were not selected, or flagged by batch readers as needing a later source. They have no gap item, so they are not concepts yet. See the last section of `sources-candidates.md` and the 'Unreadable' or 'leads' sections of the batch notes.

- From `sources-candidates.md` (gaps only named by dropped sources): shipping to other people's machines; multimodal costs; many sessions on one machine; tokenizer changes as hidden price increases; apps public by default and shadow AI; agents improvising a publishing workaround; plugin and hook updates turning a trusted plugin malicious; config files as malware persistence after uninstall; no reliable remote kill switch for always-on agents; harmless-looking destructive tool commands; the agent treating a question as permission; old storage left live after a migration; and the other items listed there.
- From `rights-and-disclosure.md`: YouTube's own altered/synthetic content label, other platforms' AI labels (TikTok, Meta, Spotify), and the current Digital Omnibus status.
- From `courses-teach-now.md`: C032 (multimodal and diffusion) exists only as Aaron's flagged gap; it still needs a source that teaches the content.

## Source index

Copied from `sources-candidates.md`. 'Date note' records what the batch readers found when they checked the date on the page (from `notes/*.md`).

| ID | Title | Author | Date (candidates list) | Date note | URL |
|---|---|---|---|---|---|
| S001 | CS146S: The Modern Software Developer (Fall 2026 syllabus, compared with Fall 2025) | Mihail Eric (instructor), Stanford University | 2026-09-22 | page undated; 2026-09-22 is the first Fall 2026 session, not a page date | https://themodernsoftware.dev/ |
| S002 | CS146S lecture 2026-09-24: anatomy of a state-of-the-art coding agent (transcript) | Mihail Eric, Stanford CS146S | 2026-09-24 |  | https://themodernsoftware.dev/materials/9-24-26-transcript.txt |
| S003 | CS146S lecture 2026-09-29: advanced prompting and context engineering, RePPIT (transcript) | Mihail Eric, Stanford CS146S | 2026-09-29 |  | https://themodernsoftware.dev/materials/9-29-26-transcript.txt |
| S004 | AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening | Aaron Orelup (drafted by Claude from his feedback) | 2026-10-04 |  | https://aaronorelup.com/ledger/lessons-sent-back/ |
| S005 | Claude Code 101 (Anthropic Academy) | Anthropic Academy | 2026-10-05 | page undated; slide assets dated 2026-04-09; live on 2026-10-12 | https://anthropic.skilljar.com/claude-code-101 |
| S006 | AI Capabilities and Limitations (Anthropic Academy) | Anthropic Academy | 2026-10-05 | page undated; live by early April 2026 (Wayback) | https://anthropic.skilljar.com/ai-capabilities-and-limitations |
| S007 | AI Fluency for Builders (Anthropic Academy with CodePath) | Anthropic Academy and CodePath | 2026-09 | Coursera 'recently updated September 2026', launch 2026-09-29 | https://www.coursera.org/learn/ai-fluency-for-builders |
| S008 | Codex Bootcamp 101: Agentic coding (OpenAI Academy livestream and slide deck) | OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala) | 2026-09-23 |  | https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c |
| S009 | Test and Debug with GitHub Copilot (GitHub Skills exercise) | GitHub (GitHub Skills) | 2026-09-29 | exercise content committed 2026-09-30 | https://github.com/skills/test-and-debug-with-github-copilot |
| S010 | Build with Andrew | Andrew Ng, DeepLearning.AI | 2026-07-17 |  | https://www.deeplearning.ai/courses/build-with-andrew |
| S011 | Six misconceptions about large language models: A minimal model and diagnostic taxonomy | Zhicheng Lin | 2026-07-08 |  | https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/ |
| S012 | Context windows (Claude Platform Docs) | Anthropic | undated (live docs; record a last-updated date) | undated live docs | https://platform.claude.com/docs/en/build-with-claude/context-windows |
| S013 | Gemini thinking (Google AI for Developers) | Google | 2026-10-09 |  | https://ai.google.dev/gemini-api/docs/generate-content/thinking |
| S014 | An update on recent Claude Code quality reports | Anthropic | 2026-04-23 |  | https://www.anthropic.com/engineering/april-23-postmortem |
| S015 | Extend Claude Code (features overview) | Anthropic (Claude Code docs) | undated (live docs; record a last-updated date) | undated live docs | https://code.claude.com/docs/en/features-overview |
| S016 | Manage costs effectively (Claude Code) | Anthropic (Claude Code docs) | 2026-09 | undated; content no earlier than 2026-09-14 (v2.1.271) | https://code.claude.com/docs/en/costs |
| S017 | AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper. Across three long tests it was 2% cheaper. | Aaron Orelup | 2026-09-28 |  | https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/ |
| S018 | ~$1,500 in one week running a Grok Bot fleet: expected, or a bug? | Stijn (dotstijn); replies by Kevin Neilson (Cursor staff), Zachariah | 2026-09-22 |  | https://forum.cursor.com/t/172705 |
| S019 | Zapier Agents: unexpected activity usage | Zapier Help Center | 2026-10-01 |  | https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage |
| S020 | Google API Keys Weren't Secrets. But then Gemini Changed the Rules. | Joe Leon (Truffle Security) | 2026-02-25 |  | https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules |
| S021 | The State Of AI Harness Engineering 2026 | François Zaninotto (Marmelab) | 2026-09-24 |  | https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html |
| S022 | Rethinking skills and prompts for GPT-6 Astra | OpenAI (developers blog) | undated (record a date) | undated; no earlier than 2026-09-03 (GPT-6 Astra release) | https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra |
| S023 | Agent repeatedly ignores workspace User Rules and repo gates across multiple chats | Brunno Oliveira Prego; replies by Mohit (Cursor staff) | 2026-09-02 |  | https://forum.cursor.com/t/170277 |
| S024 | Kiro specs (with Kiro docs index) | Kiro (AWS) | 2026-10-02 |  | https://kiro.dev/docs/specs/ |
| S025 | ChatGPT & Codex changelog (with Get started with ChatGPT Work) | OpenAI | 2026-10-08 | latest entry 2026-10-08 | https://learn.chatgpt.com/docs/changelog |
| S026 | AO-043: A cloud session pushed one post from a branch, and my whole site went back to August | Aaron Orelup | 2026-10-09 |  | https://aaronorelup.com/ledger/the-branch-that-went-live/ |
| S027 | Verifiability | Andrej Karpathy | 2025-11-17 (foundational and still current) | foundational, still current (2025) | https://karpathy.bearblog.dev/verifiability/ |
| S028 | More than just code review | Simon Willison | 2026-08-22 | a short note, not an essay; the 'other ways' come from companion posts | https://simonwillison.net/2026/Aug/22/more-than-just-code-review/ |
| S029 | The Code Nobody Reads | Addy Osmani | 2026-09-28 |  | https://addyo.substack.com/p/the-code-nobody-reads |
| S030 | When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer | Remy (redreamality.com) | 2026-10-11 |  | https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ |
| S031 | Humans are Missing from AI Coding Agent Research | Zora Z. Wang, John Yang, Kilian Lieret, et al. (incl. Graham Neubig, Daniel Fried, Diyi Yang) | 2026-07-04 | arXiv v1 2026-07-04 | https://arxiv.org/abs/2608.12355 |
| S032 | AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run | Aaron Orelup | 2026-09-29 |  | https://aaronorelup.com/ledger/wallpapers-nobody-saw/ |
| S033 | 2026 in LLMs (so far) | Simon Willison | 2026-09-27 |  | https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ |
| S034 | What I believe about the future of software development | Thorsten Ball | 2026-09-19 |  | https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/ |
| S035 | Astra for Coding: Why Are We Doing This Again? | Armin Ronacher | 2026-09-07 |  | https://lucumr.pocoo.org/2026/9/7/astra-why/ |
| S036 | Brownfield Agentic Engineering | Addy Osmani | 2026-09-14 |  | https://addyosmani.com/blog/brownfield-agentic-engineering/ |
| S037 | A field guide to Claude Fable 5: Finding your unknowns | Thariq Shihipar (Anthropic) | 2026-07-06 |  | https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns |
| S038 | LLMs are getting smarter but not safer: Veracode 2026 GenAI Code Security Report | Veracode (Chris Wysopal quoted) | 2026-07-28 |  | https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/ |
| S039 | Understanding the (In)Security of Vibe-Coded Applications | Junquan Deng, Zhiyu Fan, Ruijie Meng | 2026-06-22 |  | https://arxiv.org/abs/2606.23130 |
| S040 | (Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code | Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka | 2026-09-17 |  | https://arxiv.org/abs/2609.21020 |
| S041 | The 'vibe coding spectrum' approach to AI-assisted software development | Toby W, Principal Security Architect, UK NCSC | 2026-06-18 | published 2026-06-18; PDF generated 2026-07-03 | https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf |
| S042 | Secure Coding with AI Cheat Sheet | OWASP Cheat Sheet Series | 2026-05-05 (first published; last updated 2026-10-04) | created 2026-05-05, last commit 2026-10-04 | https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html |
| S043 | Claude Code: Catch security issues as Claude writes code (security-guidance plugin) | Anthropic (live docs) | undated (record a last-updated date) | undated on page; last modified 2026-10-09 | https://code.claude.com/docs/en/security-guidance |
| S044 | Hacking Moltbook: The AI Social Network Any Human Can Control | Gal Nagli (Wiz Research) | 2026-02-02 |  | https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys |
| S045 | v0 security (with External APIs / environment variables) | Vercel (v0 docs) | 2026-10-09 |  | https://v0.app/docs/security |
| S046 | Update on Security at METR | METR | 2026-08-31 |  | https://metr.org/blog/2026-08-31-security-update/ |
| S047 | Secret scanning adds detectors for Lovable, Supabase, and more | GitHub Changelog | 2026-10-05 | model-based detector is in the 2026-10-07 companion changelog | https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more |
| S048 | Leaked n8n API Tokens Exposed Live Instances to Credential Theft | Guillaume Valadon (GitGuardian), on The Hacker News | 2026-08-05 |  | https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html |
| S049 | The lethal trifecta for AI agents: private data, untrusted content, and external communication | Simon Willison | 2025-06-16 (foundational and still current) | foundational, still current (2025) | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ |
| S050 | How we contain Claude across products | Anthropic Engineering | 2026-05-25 |  | https://www.anthropic.com/engineering/how-we-contain-claude |
| S051 | Auto mode is now the default in Claude Code for Pro, Max, and Team plans | Simon Willison | 2026-08-08 |  | https://simonwillison.net/2026/Aug/8/auto-mode/ |
| S052 | Choose a permission mode (Claude Code) | Anthropic (Claude Code docs) | 2026-09 | undated live docs; Copilot changelog 2026-10-07 | https://code.claude.com/docs/en/permission-modes |
| S053 | A CISO's guide to agentic AI | Jason Clinton, Deputy CISO, Anthropic | 2026-07-17 |  | https://claude.com/blog/ciso-guide-to-agentic-ai |
| S054 | One prompt let researchers take over AWS AgentCore agents (AgentCorruption) | Ana Maria Constantin (The Next Web), reporting Zenity Labs | 2026-10-08 |  | https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents |
| S055 | OWASP Top 10 for LLM Applications 2026 | OWASP GenAI Security Project | 2026-08-04 | 2026-08-03/04 | https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 |
| S056 | GitSpawn: AI coding agents run attacker code via git config | Francisco Rosales (Manifold Security) | 2026-09-01 |  | https://www.manifold.security/blog/ai-coding-agents-git-hijack |
| S057 | How a Malicious Repo Tricked Claude Code into Running Malware | Brian Cumi (Straiker STAR Labs) | 2026-09-22 |  | https://www.straiker.ai/blog/how-a-malicious-repo-tricked-claude-code-into-running-malware |
| S058 | Agentjacking: MCP Injection Hijacks AI Coding Agents (CSA research note) | Cloud Security Alliance AI Safety Initiative, summarizing Tenet Security Threat Labs | 2026-06-12 |  | https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/ |
| S059 | MCP Security Best Practices (specification revision 2026-07-28) | Model Context Protocol project | 2026-07-28 |  | https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices |
| S060 | Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks (CSA research note) | Cloud Security Alliance AI Safety Initiative | 2026-04-19 | 2026-04-19; core statistics from a 2025 study | https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/ |
| S061 | ChainDrop npm Worm | Sai Likhith (StepSecurity) | 2026-08-04 |  | https://stepsecurity.io/blog/chaindrop-npm-worm |
| S062 | Playback: security moments (a malicious redirect, and verifying a download before install) | Aaron Orelup (typed and pasted prompts) | 2026-10-10 | two sessions: 2026-09-28 and 2026-10-10 | playback-lens:C--Users-soulo-Organized-Personal-My-Projects-Sandbox-2/7c75a0b6-4bcf-45ae-9869-1489cad914a6/2026-09-28 (also photoshop/dea3f681-154f-47d6-a4f4-05cb5da99bb5/2026-10-10) |
| S063 | [Agent] Autonomous rd /s /q wiped the entire D: drive (Windows) | luck_li; reply by Colin (Cursor staff, Community Support Engineer) | 2026-10-09 |  | https://forum.cursor.com/t/174156 |
| S064 | Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident | Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR) | 2026-08-26 |  | https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ |
| S065 | GenAI and Agentic AI Exploit Roundup Q3 2026 | OWASP Gen AI Security Project (editor) | 2026-10-08 |  | https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 |
| S066 | Webhook works in test but not in production? The test vs. production URL trap | Syed Farzam Saadat | 2026-10-04 |  | https://community.n8n.io/t/318716 |
| S067 | How do you catch workflows that run fine but do nothing? | Richard Rodrigues; 36 posts (Romeo Apps, Nathan, Adam, Cam, Michael Stables, Enzo Software) | 2026-08-21 | first post 2026-08-21, replies to 2026-10-08 | https://community.n8n.io/t/308708 |
| S068 | Agency and Agents | Ethan Mollick | 2026-08-31 |  | https://www.oneusefulthing.org/p/agency-and-agents |
| S069 | Use Claude Cowork safely | Anthropic (Claude Help Center) | 2026-10 | last modified 2026-10-06 | https://support.claude.com/en/articles/13364135-use-claude-cowork-safely |
| S070 | Use Claude in Chrome safely (Anthropic Help Center) | Anthropic | undated (record a date) | last modified 2026-10-05 | https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely |
| S071 | Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users | Ravie Lakshmanan (The Hacker News), reporting Koi Security and OpenSourceMalware | 2026-02-02 | 2026-02-02, older than 3 months | https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html |
| S072 | AI Hallucination Cases database | Damien Charlotin | 2026-10-10 | last updated 2026-10-10 | https://www.damiencharlotin.com/hallucinations/ |
| S073 | Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents | Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania) | 2026-04-03 | 2026-04-03; models tested are older | https://arxiv.org/html/2604.03173v1 |
| S074 | WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance | Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. (Columbia Business School) | 2026-05-21 |  | https://arxiv.org/html/2605.22664v1 |
| S075 | Can AI Now Design PCBs That Just Work? | Maya Posch, Hackaday | 2026-09-05 |  | https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/ |
| S076 | EU AI Act: Transparency Obligations for AI-Generated Content (Article 50) | Julia Apostle, Orrick | 2026-08-14 |  | https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50 |
| S077 | Suno Terms of Service | Suno, Inc. | 2026-08-10 | revised 2026-08-10, effective 2026-09-03 | https://suno.com/terms |
| S078 | A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress | Erik Dullea, Evan Yahng (Husch Blackwell) | 2026-08-20 |  | https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/ |
| S079 | YouTube clarifies policies around AI slop and upsetting videos | Sarah Perez, TechCrunch | 2026-07-20 |  | https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ |
| S080 | Stack Overflow Developer Survey 2026 - full results site (AI, Knowledge, Community) and press release | Stack Overflow (press release quotes CEO Prashanth Chandrasekar) | 2026-10-06 | released 2026-10-06; fieldwork 2026-06-23 to 2026-08-05; results site undated | https://survey.stackoverflow.co/2026/ |
| S081 | How Much Code Do Developers Really Let Agents Write? (JetBrains Research, Developer Ecosystem Survey 2026) | Mikhail Bogdanov (JetBrains Research) | 2026-08 | page undated; 2026-08 inferred from URL | https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/ |
| S082 | Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI | Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva | 2026-07-01 |  | https://arxiv.org/abs/2607.01418 |
| S083 | How AI assistance impacts the formation of coding skills (Anthropic) | Judy Hanwen Shen and Alex Tamkin | 2026-01-29 | blog 2026-01-29; foundational, still current | https://www.anthropic.com/research/AI-assistance-coding-skills |
| S084 | Agentic Skill Decay | Addy Osmani | 2026-08-31 |  | https://addyosmani.com/blog/agentic-skill-decay/ |
| S085 | From Prompting to Verification: How Experience Shapes Vibe Coding Practices | Ahmed Fawzy, Amjed Tahir, Kelly Blincoe | 2026-05-23 |  | https://arxiv.org/abs/2605.24521 |

Source IDs in the candidates list not cited by any item: none.
