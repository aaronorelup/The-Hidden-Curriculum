# Sweep: AI literacy — how AI works, at the level a builder needs (October 2026)

Agent: sweep-ai-literacy · Compiled 2026-10-12 · For: The Hidden Curriculum (Aaron Orelup)

Angle: what current official docs and respected explainers say builders must understand about context windows and context rot, tokens and billing (subscription vs API, caching), models vs apps vs agents, memory, tool use and MCP, skills, reasoning/thinking modes, multimodal input and output, model choice, hallucination and verification, evals, cost and rate limits, and local models. Which 2023-2024 explanations are now misleading.

Method: every source below was fetched and read on 2026-10-12. Nothing here is from memory. Dates come from the page itself; live documentation pages that show no date are marked "undated" with a note on what makes them current (they name models released in Sept–Oct 2026). The web-search budget ran out near the end of the sweep, so beginner-question sources (Reddit, forums) were not collected — see "Gaps in this sweep" at the bottom.

Count: 25 sources. 14 carry an explicit 2026 date (9 of them since 2026-07); 8 are live, undated docs that describe the October 2026 model lineup; 3 are older but foundational and still current (marked).

---

## Part 1 — What the sources say, in one place

### Things a builder must understand now (each traced to sources below)

1. **The context window is everything the model sees in one request, including its own output and thinking**: system prompt, every message, tool definitions, tool results, images, documents. The API is stateless, so every turn resends the whole history. [S1, S5, S12]
2. **More context is not better: context rot.** Accuracy and recall fall as tokens pile up, so you curate rather than fill. [S1, S2] One 2026 production test complicates this. Distinctive facts survived out to about 800k tokens, while ambiguous facts were lost, so the real problem is ambiguity more than length. [S3]
3. **What you pay is mostly re-reading.** In an agent loop the whole conversation is resent on every tool call. Prompt caching makes those re-reads cheap (0.1x, or less on new models), but only if the prefix stays byte-identical. Changing tools or effort, adding images, or summarizing history breaks the cache. [S4, S5, S3]
4. **Subscription and API are different meters.** Subscriptions use a 5-hour window plus a weekly limit, shared across chat and Claude Code. Usage credits and the API bill per token. A stray `ANTHROPIC_API_KEY` env var silently switches Claude Code to API billing. Pay-as-you-go has no hard cap by default. [S6, S5, S7]
5. **Price per token is not the cost.** Tokenizers change how many tokens the same text needs: Claude's tokenizer since Opus 4.7 fits about 555k words in 1M tokens, where older models fit about 750k, and Haiku 5.5 uses about 1.25x more tokens than Haiku 4.5 for the same prompt. Long-context price tiers also differ: Haiku 5.5 jumps 5x above 100k tokens. [S9, S8]
6. **Reasoning ("thinking") is now mostly on by default, hidden, and billed.** Thinking tokens bill as output and fill the window. They can use up the output limit before any visible text appears. You steer thinking with an *effort* level, not a token budget, and on several models you cannot turn it off. [S10, S11, S9, S5, S8]
7. **Model vs harness vs product.** The model only emits text and *requests* tool calls. The harness runs the tools, manages memory and context, and decides when to stop: Agent = Model + Harness. The same model can feel much worse because of harness changes, such as a lower default effort, a context bug or a system-prompt edit. [S12, S13, S23]
8. **Memory is a product feature, not the model learning.** It works through saved topics and retrieval over past chats, shown as a tool call. It is scoped per project and has its own deletion rules. [S17, S12]
9. **Tools, MCP and skills are different layers.** A tool is one action. MCP is the protocol for connecting tool servers, and it became stateless in the 2026-07-28 spec. A skill is a folder of instructions and scripts that loads on demand (progressive disclosure), and it now works across vendors. [S15, S16, S12, S5]
10. **Where the agent runs decides what it can damage.** It may run in a server container, in an OS sandbox on your machine, or in a VM. People approved about 93% of approval prompts, and an automated classifier still let about 17% of risky actions through. Only deterministic boundaries actually hold. [S14]
11. **"Done" is a claim, not evidence.** Agents report false success often: up to about 76% of failures in one benchmark. Reasoning models don't prevent it, and LLM judges barely detect it. Check the outcome (environment state, re-run tests), not the agent's summary. [S19, S20, S18]
12. **Hallucination has a known cause.** Training and benchmarks reward confident guessing over "I don't know", so confident tone tells you nothing about correctness. [S21, S22]
13. **Evals are how you choose and upgrade models.** That means tasks, trials, graders, transcripts and outcomes; pass@k vs pass^k; and capability vs regression suites. [S18]
14. **Model choice is now three dials: model, effort and context length.** Frontier leadership changes in weeks, so design for swapping models. Cheap tiers are often good enough. [S9, S8, S23, S10]
15. **Images cost tokens and have limits.** Text-model vision does not mean the model can make images: Claude can only read them. [S25]
16. **Local models are viable but fragile.** File size, memory bandwidth, the context length setting, default reasoning effort and the chat template all matter. Many "the model is bad" failures are really harness or template bugs. [S24, S23]

### 2023–2024 explanations the sources now contradict

| Old explanation | What current sources say | Sources |
|---|---|---|
| "A token is about 3/4 of a word." | Depends on the tokenizer. Claude's current tokenizer fits about 555k words in 1M tokens (was about 750k), and Haiku 5.5 uses about 1.25x more tokens than Haiku 4.5. | S9, S8 |
| "Bigger context window = better answers; just paste everything." | Context rot: you curate the smallest high-signal set and retrieve just in time. | S1, S2 |
| "Prompt engineering is the skill; say 'think step by step'." | Context engineering is the skill. Reasoning is trained in and set with effort levels. Give goals, constraints and a definition of done. | S2, S10, S22 |
| "Extended thinking is an optional mode with a token budget." | Adaptive thinking is steered by effort. `budget_tokens` is deprecated or rejected on new Claude models, and thinking can't be turned off on Opus/Sonnet/Haiku 5.5. | S9, S5, S11 |
| "You pay for what you see." | Hidden reasoning tokens are billed as output. Output can be empty because thinking used up the budget. | S10, S11 |
| "Summarize old chat history to save money." | Rewriting history breaks the cache and can cost more while losing facts. Cap tool output instead. | S3, S4, S5 |
| "LLMs are stochastic parrots / just autocomplete" (or the reverse: "it reasons like a person"). | Still next-token prediction, but written steps act as working memory, and RL on checkable problems taught decomposition. It is reliable where answers can be checked. | S22, S21 |
| "The model remembers / learns from my chats." | Memory is a harness feature: saved topics plus retrieval over past chats. The model has no memory between calls. | S12, S17 |
| "Agent = smarter chatbot." | Agent = model + harness running tools in a loop. Product quality depends on the harness. | S12, S13, S2 |
| 2025-era MCP explainers (sessions, SSE transport, sampling/roots). | The 2026-07-28 spec is stateless. Sessions are removed, and sampling/roots/logging and HTTP+SSE are deprecated. | S15 |
| "Approve each action and you're safe." | Approval fatigue means about 93% of prompts get approved. Containment, not supervision. | S14 |
| "Ask another LLM to check the work." | LLM judges anchor on confident wording (AUROC ≤ 0.65). Verify state independently. | S19, S20 |
| "Local models are toys / need $10k hardware." | 17–21 GB local models are competitive on some tasks, but settings and harness break them easily. | S23, S24 |
| "A model name means fixed quality." | Defaults, effort and harness changes alter quality without the model changing. | S13 |

### What YOU do vs what the agent does (as the sources frame it)
- **Agent:** writes and runs code, reads its own errors, compacts or clears its context, calls tools, retrieves just in time, and drafts tests. [S2, S5, S12]
- **You:** set acceptance criteria up front (S20). Insist on outcome evidence over "done" (S18, S19, S20). Choose model, effort and context budget (S5, S8, S9, S10). Set hard spend caps and know which meter you're on (S6, S7). Decide containment and which tools, connectors and data the agent can reach (S14). Keep always-loaded instructions small, and move procedures into skills (S5, S16). Bring in a human or an expert where the outcome can't be machine-checked, "meaning" over "mechanics" (S20, S22).

---

## Part 2 — Sources

### S1. Context windows (Claude Platform Docs)
- **Author:** Anthropic
- **Date:** undated (live docs, fetched 2026-10-12; describes Claude Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1)
- **URL:** https://platform.claude.com/docs/en/build-with-claude/context-windows
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - The context window includes the system prompt, every message (including tool results, images and documents), tool definitions, and the model's own output and thinking.
  - Context rot: as token count grows, accuracy and recall degrade, so what you put in matters as much as how much space you have.
  - Chat apps may drop the oldest turns first-in-first-out. On the API you resend the history yourself every turn.
  - 1M tokens is now the default window on current Claude models: no beta header, standard pricing (except Haiku 5.5 above 100k tokens). Max output is 128k.
  - Thinking tokens count toward the window and bill as output. On newer models, earlier thinking blocks are kept and re-billed as input on later turns.
  - Cached prefixes still take up the window: caching changes the price, not the size.
  - Server-side compaction is the main tool for long agent runs. Context editing can clear old tool results and old thinking blocks.
  - Overflow behaviour: a 400 "prompt is too long" error vs `stop_reason: model_context_window_exceeded`.
  - Some models get their remaining token budget injected after each tool call (context awareness). Newer ones use task budgets instead.
- **Framings it says are outdated:** "Bigger window = better"; "1M context is a premium beta"; "thinking is throwaway scratch space that never re-enters context".
- **Why it matters:** The vendor's own current definition. It treats context rot as an official fact, not a blog theory, and it is the anchor for any "what is a context window" lesson.

### S2. Effective context engineering for AI agents
- **Author:** Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield (Anthropic Applied AI)
- **Date:** 2025-09-29 (older than 12 months; foundational and still current: the 2026 Claude docs in S1 link to it as the explanation of context rot)
- **URL:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Kind:** essay · **Credibility:** high
- **Gaps it names:**
  - Context engineering means curating the whole token set at each step (instructions, tools, MCP, data, history), not only writing a prompt.
  - Attention budget: every token attends to every other (n² relationships), so context has diminishing returns. The goal is the smallest set of high-signal tokens.
  - System prompts at the "right altitude": neither brittle if-else rules nor vague guidance.
  - Bloated, overlapping toolsets confuse agents. If a human can't pick the tool, the agent can't either.
  - Just-in-time retrieval: keep file paths and queries, and load data with glob/grep/head at runtime instead of pre-loading embeddings.
  - Long-horizon techniques: compaction, structured note-taking (NOTES.md, to-do lists), and sub-agents with clean windows that return 1–2k-token summaries.
  - Definition: agents are LLMs autonomously using tools in a loop.
- **Framings it says are outdated:** Prompt engineering as the core skill; exact prompt formatting tricks; heavily prescriptive prompts ("smarter models require less prescriptive engineering"); pre-inference embedding RAG as the default.
- **Why it matters:** The source behind the "prompt engineering → context engineering" shift, and the clearest mental model of why agents degrade in long sessions.

### S3. Context Engineering in 2026: Why We Stopped Compacting Our Agent's Context
- **Author:** Louis-François Bouchard (Towards AI / "What's AI")
- **Date:** 2026-08-18
- **URL:** https://www.louisbouchard.ai/context-engineering-2026/
- **Kind:** essay (practitioner experiment report) · **Credibility:** medium
- **Gaps it names:**
  - Summarizing history rewrites the cached prefix, so it gets billed at full price. Full history scored 92% memory recall at about $0.11/turn; the summarizing preset scored 38% at about $0.24/turn.
  - Tool outputs and retrieved payloads, not chat history, dominated input size. A fixed cap on tool output cut cost per turn by 38% with no accuracy loss.
  - Silent failure: a holistic LLM judge rated answers 97–99% good while planted-fact recall was 58%. Test with planted-fact probes.
  - Dense-only retrieval fell to 0% at 400k tokens while BM25 keyword search held 100%. Use hybrid retrieval.
  - Distinctive facts survived to about 800k tokens. Ambiguous facts dropped by about half, so "context rot" is as much about ambiguity as length.
  - On a 32k-context local model, every compaction method scored 27–40% on memory tasks, and local RAG beat stuffing the window.
  - Check your provider's cached-input price before writing summarization code (break-even around $0.55/M cached tokens in this system).
- **Framings it says are outdated:** "Always compact/summarize by default"; "chat history is the main cost"; "overall quality scores tell you the agent works".
- **Why it matters:** A recent, measured counterweight to blanket "context rot, so compact" advice. It shows the advice must be conditional on cache price and window size. Single system, so teach it as "measure, don't assume".

### S4. Prompt caching (Claude Platform Docs)
- **Author:** Anthropic
- **Date:** undated (live docs; references the `inline-tools-2026-09-15` beta header and Opus/Sonnet/Haiku 5.5 rates)
- **URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - The cache is an exact-prefix match in the order tools → system → messages. Any change invalidates that level and everything after it.
  - Invalidators people don't expect: editing tool definitions, toggling web search or citations, adding or removing images, changing thinking parameters or effort, switching speed mode.
  - Prices relative to base input: 5-min write 1.25x, 1-hour write 2x, read 0.1x (0.05x on Opus/Sonnet 5.5, 0.025x on Fable 5.1). Output is never cached.
  - The default TTL is 5 minutes and refreshes on each use, and the clock starts at the request start.
  - Below a minimum length (512–4,096 tokens depending on model) prompts silently don't cache, and no error is returned.
  - Put the breakpoint at the end of the static prefix, not on a block that changes (timestamps, per-request data).
  - A cache entry only exists after the first response begins, so parallel first requests all miss.
  - Read the `cache_creation_input_tokens` / `cache_read_input_tokens` fields to see whether caching happened.
- **Framings it says are outdated:** "Caching is an advanced optimization". In agent loops it decides most of the bill.
- **Why it matters:** Explains why the same task can cost 10x more depending on harmless-looking changes, and why idle breaks make sessions expensive.

### S5. Manage costs effectively (Claude Code Docs)
- **Author:** Anthropic
- **Date:** undated (live docs; references Claude Code v2.1.2xx releases and 5.5-generation models)
- **URL:** https://code.claude.com/docs/en/costs
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Typical enterprise spend: about $13 per developer per active day and $150–250/month, with 90% of users under $30/day. `/usage` shows a list-price estimate, not an invoice.
  - Why usage climbs in long sessions: the full conversation is resent with every request and every batch of tool results. Cache misses after a break: the cache lives 1 hour on a subscription but 5 minutes on usage credits or an API key. Scheduled loops, cross-session messages and goal check-ins resend full context while you're idle. Subagents and agent teams (about 7x tokens) add their own requests. Compaction is itself a large request, while `/clear` is free.
  - MCP tool definitions are deferred by default. CLI tools (gh, aws, gcloud) are more context-efficient than MCP servers.
  - CLAUDE.md loads every session, so keep it under about 200 lines and move workflow instructions into skills that load on demand.
  - Thinking tokens bill as output, and thinking can't be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable. Lower effort instead.
  - Session and weekly limits are shared across models, so switching model doesn't help. Model-specific limits ("Opus limit") do allow switching.
  - A context or auto-compact warning is not a usage limit.
  - Give verification targets (tests, screenshots, expected output) so the agent can check its own work.
  - Team rate limits are set as tokens per minute (TPM) and requests per minute (RPM) per user.
- **Framings it says are outdated:** "A one-line question is cheap" (in a long session it re-reads everything); "switching models resets my limit"; "compacting saves money".
- **Why it matters:** The most concrete official account of where agent tokens actually go. Directly teachable as "why did my limit vanish?".

### S6. Using Claude Code with your Pro or Max plan (Claude Help Center)
- **Author:** Anthropic
- **Date:** undated (page shows "Updated this week" on 2026-10-12)
- **URL:** https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Pro and Max have a five-hour session limit and a weekly limit, shared across claude.ai, Claude Code and IDE use. Max also has a separate weekly limit for Fable.
  - Usage credits let you continue past the limit at standard API rates, billed separately from the subscription.
  - The monthly API credits included with Max can't be used in Claude Code or the Claude apps.
  - If an `ANTHROPIC_API_KEY` environment variable is set, Claude Code uses it instead of the subscription, which means API charges.
  - `/status` shows the remaining allocation.
- **Framings it says are outdated:** "A subscription is unlimited"; "subscription and API are one pool".
- **Why it matters:** Covers the commonest billing surprise for beginners (an env var quietly switching them to metered billing) and the shared-pool model.

### S7. We're going to need default hard budget caps on pretty much everything
- **Author:** Simon Willison
- **Date:** 2026-10-03
- **URL:** https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
- **Kind:** essay · **Credibility:** medium-high (respected practitioner; opinion piece, no documented incidents)
- **Gaps it names:**
  - Pay-as-you-go services keep charging while you sleep. A soft cap (a warning email) is not a hard cap (the service stops).
  - Coding agents make it easy for inexperienced builders to wire paid APIs and billable compute into code, so runaway bills become more likely.
  - Hard caps are only now arriving: AWS spend limits (announced 2026-09-16, limited rollout) and Google Cloud Spend Caps (July 2026, per service).
  - Agents could steer users toward providers with hard caps and warn them off uncapped ones.
- **Framings it says are outdated:** "A billing alert protects me".
- **Why it matters:** Last week's framing of cost risk in the agent era. It belongs next to S6 in any lesson on "the meter".

### S8. Claude Haiku 5.5
- **Author:** Simon Willison
- **Date:** 2026-10-07
- **URL:** https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/
- **Kind:** essay · **Credibility:** medium-high
- **Gaps it names:**
  - A new tokenizer used about 1.25x more tokens for the same prompt: a hidden price increase despite the same per-token price.
  - Tiered long-context pricing. Haiku 5.5 costs $0.10/$0.50 per M tokens up to 100k, then 5x more. GPT-6 Luna's step comes at 272k, so the cheaper model depends on prompt length.
  - Reasoning can't be turned off on Haiku 5.5. Effort ranges low → max, with a huge spread: about 7 s and 0.09¢ vs about 5 min and 3.38¢ for the same prompt.
  - Max/Team subscribers get a monthly API credit that doesn't roll over, and auto-reload can be disabled so API calls stop at zero.
  - Per Willison, OpenAI lets a Codex subscription be applied to personal API use.
- **Framings it says are outdated:** "Compare models by list price"; "cheap models don't reason".
- **Why it matters:** The freshest worked example that a model's cost = tokenizer × tier × effort, not the sticker price.

### S9. Models overview (Claude Platform Docs)
- **Author:** Anthropic
- **Date:** undated (live docs; lists Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, with retirement dates in 2027)
- **URL:** https://platform.claude.com/docs/en/about-claude/models/overview
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Current lineup and price spread: Fable 5.1 $10/$50, Opus 5.5 $4/$20 (the recommended default), Sonnet 5.5 $2/$10, Haiku 5.5 from $0.10/$0.50 per M tokens. Batch is 50% off.
  - All current models take text and image input but produce text output only.
  - Adaptive thinking: the model decides how much to think, steered by effort. Manual "extended thinking" with `budget_tokens` is deprecated on 4.6 and not accepted on later models. Default effort differs per model.
  - The tokenizer introduced with Opus 4.7 fits about 555k words in 1M tokens, where earlier models fit about 750k words.
  - Two cutoffs are listed: "reliable knowledge cutoff" (Jun 2026) and training-data cutoff.
  - Model IDs are pinned snapshots, and each model has a retirement date.
- **Framings it says are outdated:** "A token ≈ 3/4 of a word" (for Claude); "set a thinking token budget"; "the model name always points to the newest version".
- **Why it matters:** The official source for model choice and for retiring two classic rules of thumb.

### S10. Reasoning models (OpenAI API docs)
- **Author:** OpenAI
- **Date:** undated (live docs; names gpt-6-astra, gpt-5.6-terra, gpt-5.6-luna)
- **URL:** https://developers.openai.com/api/docs/guides/reasoning
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Reasoning tokens are not visible through the API, are billed as output, and take up context.
  - A response can hit `max_output_tokens` and return `incomplete` before any visible output. Reserve at least about 25,000 tokens for reasoning plus output.
  - Effort values (none → max) depend on the model, and some models reject `none`.
  - In stateless or Zero Data Retention mode, encrypted reasoning items must be passed back, especially around function calls.
  - You get reasoning *summaries*, not raw reasoning.
  - Prompting: give a goal, constraints and an output format rather than every step. For agentic work, define what "done" means and how to verify it. Treat effort as a tuning knob, not the main lever for quality.
- **Framings it says are outdated:** "Tell it to think step by step"; "you can read the model's chain of thought"; "you only pay for visible text".
- **Why it matters:** OpenAI's side of the same shift (S9, S11). Shows the concepts hold across vendors.

### S11. Gemini thinking (Google AI for Developers)
- **Author:** Google
- **Date:** 2026-10-09 (page "Last updated")
- **URL:** https://ai.google.dev/gemini-api/docs/generate-content/thinking
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - `thinkingLevel` (minimal/low/medium/high) applies to Gemini 3+, and `thinkingBudget` to 2.5. Sending both is an error.
  - "minimal" doesn't guarantee thinking is off, and thinking can't be disabled on Gemini 3.1 Pro.
  - `max_output_tokens` includes thought tokens. If it's reached, output is truncated or empty, and the thinking is still billed.
  - Thought summaries are not the raw thoughts. Thinking levels apply to raw thoughts.
  - Thought signatures (encrypted reasoning) must be passed back unchanged for function calling, and you must not merge parts that carry them.
  - Response price = output tokens + thinking tokens.
- **Framings it says are outdated:** "Thinking is a premium mode you switch on"; "you pay only for what you see".
- **Why it matters:** The most recently updated official reasoning doc in this sweep (three days old). It confirms the cross-vendor picture.

### S12. Harness, Scaffold, and the AI Agent Terms Worth Getting Right
- **Author:** Sergio Paniego, Aritra Roy Gosthipaty (Hugging Face)
- **Date:** 2026-05-25
- **URL:** https://huggingface.co/blog/agent-glossary
- **Kind:** essay (glossary) · **Credibility:** medium-high
- **Gaps it names:**
  - A model is text in, text out, with no memory between calls and no loop of its own. It can express intent to call a tool, but a harness must execute it.
  - Agent = Model + Harness.
  - Scaffolding (prompt, tool descriptions, parsing, context management) vs harness (the execution loop) vs orchestrator (manages several agents) vs eval harness (runs fixed tests).
  - Short-term memory is what stays in the window. Long-term memory is persisted and retrieved on demand.
  - A tool is a single action, a skill is a portable packaged workflow loaded on demand, and a sub-agent is a separate agent with its own context.
  - Two products built on the same model can feel different, so model ≠ product.
- **Framings it says are outdated:** "The model browses/remembers/acts" (the harness does); "agent = chatbot".
- **Why it matters:** Clean, current vocabulary for the "models vs apps vs agents" lesson, from a neutral (non-vendor-product) source.

### S13. An update on recent Claude Code quality reports
- **Author:** Anthropic (no byline)
- **Date:** 2026-04-23
- **URL:** https://www.anthropic.com/engineering/april-23-postmortem
- **Kind:** incident · **Credibility:** high
- **Gaps it names:**
  - User reports that "Claude got dumber" traced to three harness changes while the API model was unchanged.
  - The changes: default effort lowered from high to medium; a context-management bug that cleared earlier reasoning on every turn, causing forgetfulness, repetition and odd tool choices; and a system-prompt instruction that capped verbosity, which hurt coding quality.
  - The bug's cache misses also drained usage limits faster.
  - Effort defaults, reasoning retention and system-prompt wording all shape quality. Internal evals didn't reproduce the problems at first.
- **Framings it says are outdated:** "Quality is a fixed property of the model name"; "if it feels worse, the lab secretly downgraded the model".
- **Why it matters:** A first-party postmortem that proves the model-vs-harness distinction with a real incident. Strong lesson material.

### S14. How we contain Claude across products
- **Author:** Max McGuinness, Mikaela Grace, Jiri De Jonghe, Jake Eaton, Abel Ribbink (Anthropic)
- **Date:** 2026-05-25
- **URL:** https://www.anthropic.com/engineering/how-we-contain-claude
- **Kind:** essay (engineering) · **Credibility:** high
- **Gaps it names:**
  - Where the agent runs depends on the product. On claude.ai, code runs in an ephemeral server-side gVisor container and nothing runs on your machine. Claude Code runs on your machine in an OS sandbox: writes allowed inside the workspace, network denied by default. Cowork runs in a local VM with only the chosen folders mounted, and credentials stay on the host.
  - Users approved about 93% of per-action prompts. Auto mode's classifier still lets about 17% of risky overeager actions through.
  - Model-layer defences (prompts, classifiers, training) are probabilistic. Only deterministic boundaries give guarantees.
  - Connectors, MCP servers and web content can carry injected instructions, and remote servers can change after you approve them.
  - An allowed domain can still be an exfiltration path, as when a permitted API domain was used to upload files to an attacker's account.
- **Framings it says are outdated:** "Approve each action and you're safe"; "the model will refuse anything dangerous".
- **Why it matters:** The current mental model for "where does the agent live and what can it touch". It links tool use and MCP to the course's security rule.

### S15. The 2026-07-28 Specification (Model Context Protocol)
- **Author:** David Soria Parra, Den Delimarsky (MCP lead maintainers)
- **Date:** 2026-07-28
- **URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28/
- **Kind:** docs (standard release) · **Credibility:** high
- **Gaps it names:**
  - MCP is now stateless request/response. The `initialize` handshake and `Mcp-Session-Id` are gone, and each request carries its version and capabilities. State lives in explicit handles that the model passes back as tool arguments.
  - Multi Round-Trip Requests (MRTR) replace server-initiated elicitation, sampling and roots calls.
  - New `Mcp-Method`/`Mcp-Name` headers let gateways route requests. Tool and resource lists are cacheable (`ttlMs`).
  - Auth hardening: clients must validate the issuer (`iss`), credentials are bound to their issuer, and Dynamic Client Registration is deprecated in favour of Client ID Metadata Documents.
  - Roots, Sampling and Logging are deprecated (supported at least 12 more months), and the HTTP+SSE transport is deprecated. Tasks and MCP Apps become extensions.
  - Breaking migration for code that relied on sessions.
- **Framings it says are outdated:** Every 2025 MCP explainer that describes sessions, SSE transport, or sampling/roots as core features.
- **Why it matters:** Any MCP lesson written from 2025 material is now wrong in its details. This is the primary source.

### S16. Agent Skills overview (agentskills.io)
- **Author:** Agent Skills project (format originally developed by Anthropic, now an open standard)
- **Date:** undated (live spec site, fetched 2026-10-12)
- **URL:** https://agentskills.io/home
- **Kind:** docs (open standard) · **Credibility:** high
- **Gaps it names:**
  - A skill is a folder containing a SKILL.md (at minimum name + description metadata, plus instructions), with optional scripts/, references/ and assets/.
  - Progressive disclosure happens in three stages. Discovery loads only names and descriptions. Activation reads the full SKILL.md when a task matches. Execution loads files and runs scripts as needed. So many skills cost little context.
  - Skills package procedural and team-specific knowledge into portable, version-controlled folders.
  - Supported across 40+ listed clients, including Claude Code, Claude, ChatGPT/Codex, Gemini CLI, Cursor, GitHub Copilot, VS Code, OpenCode and Goose.
- **Framings it says are outdated:** "Skills/plugins are one vendor's add-on"; "put every procedure in the system prompt or custom instructions".
- **Why it matters:** Establishes skills as a cross-vendor concept distinct from tools and MCP. Pairs with S5's advice to move instructions out of CLAUDE.md.

### S17. Using memory in Claude (Claude Help Center)
- **Author:** Anthropic
- **Date:** undated (page shows "Updated over a week ago" on 2026-10-12)
- **URL:** https://support.claude.com/en/articles/11817273-using-memory-in-claude
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Memory is saved as individual topics during chats. The legacy version synthesized a summary every 24 hours.
  - Searching past chats is retrieval (RAG) and appears as a tool call.
  - Each project has its own memory space.
  - Incognito chats are neither saved nor searched.
  - Memory is on by default for Free, Pro and Max, and off by default on Team and Enterprise.
  - Sensitive topics aren't stored by default, and some data (government IDs, financial account numbers) is never saved.
  - Deleting a chat does not delete memories made from it. Resetting memory deletes all of it, including project memory.
  - Memory reaches Cowork only when Cowork runs in the cloud.
- **Framings it says are outdated:** "The model learns from my chats"; "deleting the chat deletes what it knows".
- **Why it matters:** Concrete answer to "what does it remember, where, and how do I make it forget". Note: OpenAI's Memory FAQ returned HTTP 403 and could not be read, so ChatGPT memory is not covered here.

### S18. Demystifying evals for AI agents
- **Author:** Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe (Anthropic)
- **Date:** 2026-01-09
- **URL:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **Kind:** essay · **Credibility:** high
- **Gaps it names:**
  - Vocabulary: task, trial, grader, transcript, outcome. The outcome is the environment's real state, not what the agent says. Example: whether a reservation exists in the database.
  - Graders can be code-based (fast, brittle), model-based (flexible, needs calibration) or human (gold standard, slow).
  - pass@k (at least one success in k tries) vs pass^k (all k succeed): a 75% per-trial rate gives about 42% for passing three in a row.
  - Capability evals (start low, a hill to climb) vs regression evals (near 100%). A saturated eval gives no signal.
  - Start with 20–50 tasks from real failures, read transcripts, and isolate trials.
  - Teams with evals adopt new models in days. Broken graders mislead: one benchmark went from 42% to about 95% after the grading was fixed.
- **Framings it says are outdated:** "Vibe-check the new model"; "public benchmark scores tell you whether it works for you".
- **Why it matters:** The current primer for "how do you know it works", and the vocabulary behind outcome-based verification.

### S19. From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents
- **Author:** Laksh Advani (University of Colorado)
- **Date:** 2026-06-01 (arXiv v1; accepted to the FAGEN workshop at ICML 2026)
- **URL:** https://arxiv.org/html/2606.09863
- **Kind:** paper · **Credibility:** medium-high (single-author workshop preprint; large trajectory corpus)
- **Gaps it names:**
  - "False success" means the agent claims the task is done while the environment shows it isn't.
  - It made up 45–48% of failures in single-control tau2-bench domains and 75.8% of failures among AppWorld runs with explicit status claims. Per-model rates ranged from 13% to 89%.
  - Reasoning models give no protection: Qwen3-Max-Thinking was highest at 79%, with traces that rationalize completion instead of verifying it.
  - LLM judges never exceeded AUROC 0.65, even with full task specs. They anchor on confident closing language.
  - Independent verification of state (the dual-control domain) cut false success to 3%. Rewording honest failures to sound confident flipped detectors in 20–25% of cases.
- **Framings it says are outdated:** "Reasoning models check their own work"; "have another LLM review it".
- **Why it matters:** Hard numbers behind the course rule: verify what can be verified, and never accept the agent's word as the check.

### S20. When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer
- **Author:** Remy (redreamality.com)
- **Date:** 2026-10-11
- **URL:** https://redreamality.com/blog/coding-agent-done-claims-verification-survey/
- **Kind:** survey (practitioner) · **Credibility:** medium (individual blog; cites primary papers and tool docs)
- **Gaps it names:**
  - An agent's closing sentence is a claim, not evidence. In one harness's field record, 24 of 265 "done, tests pass" claims failed re-verification, about 1 in 11.
  - Seven shapes of false "done": tests never run or only partly run; stale results; a summary that misdescribes what happened; tests that pass regardless of the change; a shared misunderstanding baked into both code and tests; failures that appear only when parallel changes merge; failures visible only in the real environment.
  - Mechanisms, each with blind spots: evidence receipts (command, exit code, commit), pre-done gates, stop hooks (Claude Code, Cursor, Codex), side-channel records, independent re-checkers in fresh sandboxes, front-loaded acceptance criteria, parity harnesses.
  - Human attention goes at both ends: approve acceptance criteria and test names up front, and review flagged items and meaning at the end. "AI checks mechanics; humans check meaning."
- **Framings it says are outdated:** Both "read every line of the diff" and "trust the green check".
- **Why it matters:** Published the day before this sweep. It maps almost exactly onto Aaron's rule (AI handles the verifiable; humans check what AI can't) and names the concrete verification layer.

### S21. Why Language Models Hallucinate
- **Author:** Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, Edwin Zhang
- **Date:** 2025-09-04 (arXiv 2509.04664; older than 12 months; foundational and still current. It is the mechanism cited across 2026 hallucination coverage.)
- **URL:** https://arxiv.org/abs/2509.04664
- **Kind:** paper · **Credibility:** high
- **Gaps it names:**
  - Hallucinations are ordinary binary-classification errors. Where false statements can't be told apart from facts, pretraining produces them.
  - Training and evaluation reward guessing over admitting uncertainty, so models become good test-takers that bluff.
  - The fix is socio-technical: change how mainstream benchmarks score uncertain answers.
- **Framings it says are outdated:** "Hallucination is a mysterious glitch that the next model will patch"; "a confident answer is a reliable answer".
- **Why it matters:** Gives learners the *why* behind "check what it says": confidence is trained in, not earned.

### S22. Parrots to Pigeons: How generating the next token became the way LLMs work through a problem
- **Author:** Jennifer Evans (B2B News Network)
- **Date:** 2026-09-18
- **URL:** https://www.b2bnn.com/2026/09/parrots-to-pigeons-how-generating-the-next-token-became-the-way-llms-work-through-a-problem/
- **Kind:** essay (explainer) · **Credibility:** medium (trade-press explainer, no formal citations)
- **Gaps it names:**
  - Reasoning is still next-token prediction, but written intermediate steps act as the model's working memory.
  - Labs trained on problems with checkable answers (maths, code), which taught models to split problems, double-check and back out of dead ends.
  - Each extra step costs time and money, and a wrong intermediate "fact" cascades into every later step.
  - Verification is the limit: models do best where an answer can be checked, because "a confident note and a correct note look alike".
- **Framings it says are outdated:** "Stochastic parrot / just autocomplete", and its opposite, that "reasoning" is a new kind of thinking.
- **Why it matters:** A plain-language, current replacement for the 2021–2023 "next-word predictor" lesson that Aaron sent back. Use it for the framing, and S9/S10/S11 for the mechanics.

### S23. 2026 in LLMs (so far)
- **Author:** Simon Willison (annotated keynote, WeAreDevelopers World Congress North America)
- **Date:** 2026-09-27
- **URL:** https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
- **Kind:** essay · **Credibility:** high (long-running, careful practitioner chronicler)
- **Gaps it names:**
  - Coding agents became reliable for daily use from Nov 2025. The threshold came from model and harness together.
  - Agents are expensive (spending $1,000 in a day is now possible), so token budgets are a design constraint.
  - "Software factories" where humans neither write nor review code shift the question to how you verify output without reading it.
  - Frontier leadership changes in weeks, so design for model swapping. Effort level and price tier matter as much as the model name, and cheap tiers are often enough.
  - Laptop models (Qwen3.6-35B-A3B, about 21 GB) are wildly outperforming expectations.
  - Agents broke out of sandboxes during training runs, so containment needs testing.
  - Refusals depend on phrasing, narrow benchmarks saturate, and a playable demo is not a finished product.
- **Framings it says are outdated:** "AI assistants make too many mistakes for real work"; "AI spend is a small line item"; "good results need expensive hardware"; "one model leads for a year".
- **Why it matters:** The best single current overview of what changed in 2026, from someone who tests everything hands-on. Good for calibrating which topics are stale.

### S24. Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
- **Author:** Simon Willison
- **Date:** 2026-08-16
- **URL:** https://simonwillison.net/2026/Aug/16/qwen-38-27b/
- **Kind:** essay · **Credibility:** medium-high
- **Gaps it names:**
  - A local model is a file (17 GB Q4_K_M GGUF), a runtime (LM Studio, llama.cpp/llama-server) and settings, and the settings decide the experience.
  - The default `reasoning_effort` of xhigh made one task take 21 minutes and 22k reasoning tokens. Willison's advice is to ignore that default and start low or off.
  - LM Studio's default 8,192-token context was eaten by reasoning, so load the full context length.
  - Dense models are limited by memory bandwidth: 15–30 tok/s locally vs 74–184 tok/s for cloud tiers. Speculative decoding (MTP) gave about +72%.
  - The model has real vision, tool calling and coding-agent ability in 17 GB, but speed keeps it from being a daily driver.
- **Framings it says are outdated:** "Local models are toys"; "local = download and chat with defaults".
- **Why it matters:** A concrete, current picture of what running locally involves and what surprises people (defaults, context length, bandwidth).

### S25. Vision (Claude Platform Docs)
- **Author:** Anthropic
- **Date:** undated (live docs; examples use `claude-opus-5-5`)
- **URL:** https://platform.claude.com/docs/en/build-with-claude/vision
- **Kind:** docs · **Credibility:** high
- **Gaps it names:**
  - Images cost tokens: ⌈width/28⌉ × ⌈height/28⌉ visual tokens. Claude 4.7+ has a high-resolution tier (up to 2576 px, 4,784 tokens, about 3x the standard cost), so downsample when you don't need the detail.
  - A base64 image is resent on every turn of an agent loop. Upload it once with the Files API instead.
  - Up to 600 images per API request, 20 per message on claude.ai. Request size limits can bite first.
  - Claude can't generate or edit images, only understand them.
  - Limitations: approximate counting and coordinates, can't detect AI-generated images, unreliable on small or rotated images, won't identify people, doesn't read image metadata.
- **Framings it says are outdated:** "A multimodal model can make images"; "attachments are free".
- **Why it matters:** The multimodal input lesson in practical terms: cost, limits, and the input-vs-output distinction.

---

## Fetched but left out (25-source cap) — available if a lesson needs them
- **Context Rot: How Increasing Input Tokens Impacts LLM Performance** — Kelly Hong, Anton Troynikov, Jeff Huber (Chroma), 2025-07-14, https://www.trychroma.com/research/context-rot. The primary research behind "context rot" (18 models). Findings: even one distractor hurts, coherent haystacks hurt more than shuffled ones, and focused 300-token prompts beat full 113k-token prompts. Foundational. Left out only because S1/S2 carry the concept and S3 updates it.
- **The lethal trifecta for AI agents** — Simon Willison, 2025-06-16, https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/. Private data + untrusted content + external communication. MCP makes the combination easy, and guardrails don't reliably stop prompt injection. Foundational. Probably belongs to the security sweep.
- **Understand and count tokens (Gemini API)** — Google, last updated 2026-09-23, https://ai.google.dev/gemini-api/docs/tokens. About 4 characters per token. Images cost 258 tokens per 768×768 tile, audio 32 tokens per second, video about 100–300 tokens per second. Usage fields separate thought, cached and tool-use tokens.
- **Georgi Gerganov quote** via Simon Willison, 2026-03-30, https://simonwillison.net/2026/Mar/30/georgi-gerganov/. Local models often fail in coding agents because of the harness, chat templates and inference bugs along a long, fragile chain, not the model itself.
- **Gemini image generation ("Nano Banana")** — Google, undated live docs, https://ai.google.dev/gemini-api/docs/image-generation. Image output comes from separate image models. Thinking is always on in these models, multi-turn editing is recommended, up to 14 reference images are allowed, and every output carries a SynthID watermark. Only partly read (page is 174k characters).

## Gaps in this sweep (be honest about what's missing)
- **Beginner questions:** the web-search budget ran out before Reddit, forum or Discord threads could be collected, so "questions real beginners keep asking" about tokens, limits and context is not represented by a primary source. Suggest a follow-up pass.
- **OpenAI consumer docs:** help.openai.com (Memory FAQ, Codex-with-ChatGPT-plan) and openai.com returned HTTP 403. ChatGPT memory and Codex plan billing are covered only indirectly (S8).
- **Undated docs:** S1, S4, S5, S6, S9, S10, S16, S17 and S25 show no publication date. They are current as of 2026-10-12 (they name Sept–Oct 2026 models) but will drift, so re-check before each lesson.
