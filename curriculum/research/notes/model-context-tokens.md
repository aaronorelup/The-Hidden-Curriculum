# Research notes: The model inside a harness

Theme: the current mental model of a model inside a harness. What fills the context, what thinking costs, and why "it got dumber" is often the harness.
Batch read on 2026-10-12. Every point below comes from a page fetched and read on that date. Dates were checked on the page itself, in the page metadata or in the HTTP headers.

Research note: the shared WebSearch budget for this run was already used up when this batch started. No new sources were discovered by search. Every page below was fetched directly: the five assigned URLs, plus vendor pages that the assigned pages link to, which are listed as companion sources.

---

## S011 - Six misconceptions about large language models: A minimal model and diagnostic taxonomy

- **Author:** Zhicheng Lin (sole author), Department of Psychology, Yonsei University, Seoul
- **Venue:** PNAS Nexus 5(7): pgag236 (Perspective). DOI 10.1093/pnasnexus/pgag236. PMCID PMC13378163. CC BY 4.0.
- **Date:** published 2026-07-08 (received 2025-12-20, accepted 2026-06-29). Confirmed on the page.
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/

**Summary.** The paper treats popular slogans about LLMs as folk theories. Each slogan holds a real kernel of truth but takes it for the whole. It proposes a "minimal model" built on four distinctions:
- A: pretraining versus the deployed system.
- B: the learned distribution versus a particular sample.
- C: parametric, contextual and external memory.
- D: task competence versus agency.

It uses these to diagnose six misconceptions, then applies the same lens to publisher AI policies (APS, APA, SAGE). Its main claim is that the deployed configuration, not the base model, is the right unit of analysis. That configuration is wrapper + system prompt + tools + retrieval + decoding + filters + logs.

**The minimal model (components named in the paper)**
- **Pretraining:** next-token cross-entropy on large corpora. The weights are then frozen.
- **Post-training:** instruction tuning and RLHF change the same weights that hold knowledge and skills.
- **Decoding policy:** greedy, temperature or top-p sampling, plus optional safety filters.
- **System prompts and context:** instructions, dialogue history and retrieved content assembled into the input.
- **Wrapper:** the product layer, meaning the UI, system prompt, safety filters, tool APIs, retrieval and sometimes actuators.
- **Tools and closed loops:** tool output goes back into the next prompt. The paper says this "loop can function as a decision-making controller", even though each call is still next-token prediction.
- **Input and output filters:** external classifiers that can be added or removed without retraining.
- **Logs:** product-level records that may be reused for future training.

**Memory layers (distinction C)**

| Layer | Where it lives | How long it lasts |
|---|---|---|
| Parametric | In the weights, as a lossy and biased compression of training data | Until the model is retrained |
| Contextual | Conversation history, retrieved text and tool results in the current input | Only while it stays inside the context window |
| External / product | Logs, user profiles, knowledge bases and vector stores outside the model | Set by product retention policy; selectively injected into prompts |

The paper says "this is where many privacy and governance risks concentrate", meaning the external layer.

**Gaps it shows**

1. **"The model" is not the product you use.**
   - "Just next-token prediction" describes the training objective, not the deployed system.
   - Tools change capability sharply. GeneGPT (Jin et al. 2024) scored 0.83 on GeneTuring with NCBI API tools, against 0.00-0.44 without them.
   - Retrieval raised GPT-4's factual accuracy on FreshQA by 32.6-49.0% (relative) (Vu et al. 2024).
   - PaperQA2 reached 85.2% precision on LitQA2, against 73.8% for PhD-level experts with internet access (Skarlinski et al. 2024).
   - The fix: when you describe or judge a capability, name the wrapper, the tools and the decoding policy.
2. **The workflow matters as much as the model.**
   - In a 2024 randomized trial (Goh et al., JAMA Netw Open), physicians given GPT-4 scored only 2 points above the control group, which was not significant. GPT-4 alone scored 16 points above control.
   - A redesigned collaborative workflow (Everett et al. 2026, npj Digit Med) raised clinician diagnostic accuracy to 82-85%, against 75% with conventional resources.
   - The paper concludes that evaluation should treat "the deployed configuration ... as the unit of analysis".
3. **Where information lives: three memory layers, not "it remembers me" and not "it remembers nothing".**
   - "Stateless" means only that the weights are fixed during ordinary use.
   - Persistence comes from context, which is bounded and lasts only while in the window, and from external storage such as logs, profiles and memory features, which follows product policy.
   - Ordinary chats do not update the weights.
   - Diagnostic question to ask: where is this stored, how long is it kept, and how is it reused?
4. **Users misread chatbots as search engines and misunderstand memory.**
   - Brachman et al. 2025 (IUI '25, "Building appropriate mental models: what users know and want to know about an agentic AI chatbot") found users "conflate generation with search".
   - Jones et al. 2025 (CHI '25 Extended Abstracts, "Users' expectations and practices with agent memory") found users "misunderstand what different memory layers store and reuse".
5. **Parametric knowledge has a date on it.**
   - The weights hold a lossy, biased compression that changes only when the model is retrained.
   - The paper quotes the APS policy's correct kernel: some LLMs are trained only on content published before a particular date, so they give an incomplete picture.
   - Retrieval and tools are what bring in current facts (FreshQA result above).
6. **Bland, samey output is a product setting, not "the average of the internet".**
   - Models learn a conditional distribution with a long tail.
   - Homogenized output "usually reflects product choices": low-temperature or greedy decoding, alignment pressure and uniform assistant prompts.
   - Doshi & Hauser 2024: LLM-assisted stories were rated more creative one by one but became more similar to each other.
   - Zhou, Lee & Gu 2025 (31,076 creators): the idea frontier expanded through volume, but creativity per artifact declined.
   - The fix: vary prompts and decoding, and record which settings were used.
7. **"It just regurgitates training data" is an empirical question, not a rule.**
   - Most output is recombination.
   - Models can still reproduce boilerplate or famous passages, which raises privacy and copyright concerns.
   - Audit outputs and filter for leakage rather than assuming either way.
8. **Fine-tuning and RLHF are not a removable filter on a neutral core.**
   - Post-training changes the same weights.
   - Separate server-side filters also exist and can be added or removed without retraining.
   - DeepSeek-R1 case (Box 2): weight-level alignment plus server-side filters. Independent groups have realigned its open weights, and local censorship persists in the weights (Naseh et al. 2025).
   - The practical upshot: running open weights locally does not remove behaviour trained into the weights.
9. **Fluency is not evidence of a mind, and "no understanding at all" is also wrong.**
   - Models show functional competence in bounded domains but lack embodiment, persistent learning and stable internal state.
   - Anthropomorphic interface cues change users' accuracy and risk judgments (Cohn et al. 2024; Inie et al. 2024). Mental-state attributions influence trust (Colombatto et al. 2025).
   - Perceived human-likeness of AI has risen over time (Cheng et al. 2026). Anthropomorphic language in computer-science papers has increased (Cheng et al. 2024, AnthroScore).
   - The fix: describe competence functionally. Ask which tasks are done reliably.
10. **Liability follows the deployment.**
    - *Moffatt v. Air Canada* placed liability on the operator of the deployed chatbot.
    - *Mata v. Avianca* led to disclosure and certification orders.
    - The NIST Generative AI Profile (2024) separates pretrained, adapted and deployed systems.

**Framings it calls outdated or wrong**
- "Just next-token predictors", "stochastic parrots", "glorified autocomplete".
- "The average of the internet, edited for tone" and "regresses to the mean".
- "A blurry JPEG of all the text on the Web". The paper cites Chiang 2023 among the slogans; it is not the paper's own view.
- "Just memorizes and regurgitates its training data".
- "Learns from my chats and remembers me", and the opposite, "stateless and remembers nothing".
- "RLHF is a superficial filter on a neutral core".
- "Thinks like a human" versus "has no understanding at all".

**Quotes**
- "The predictor is unchanged; the system is not." (misconception 1)
- "The model did not change; the workflow did." (evaluation section)

---

## S012 - Context windows (Claude Platform Docs), with Prompt caching

- **Author:** Anthropic
- **Date:** undated live docs. There is no visible date and no Last-Modified header (HTTP check 2026-10-12). The content is current as of the fetch: it lists Claude Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1 and Mythos 5.1.
- **URL:** https://platform.claude.com/docs/en/build-with-claude/context-windows
- **Companion source read:** Prompt caching (Claude Platform Docs), undated live docs, https://platform.claude.com/docs/en/build-with-claude/prompt-caching (the first 100,000 characters were read).

**Summary.** The context window is everything the model can reference for one response, including the response itself. The docs call it "working memory", separate from the training corpus. Everything in the request counts:
- the system prompt;
- every message, including tool results, images and documents;
- the tool definitions;
- the output for this turn, including its thinking.

The API is stateless. Each turn sends all previous history plus the new message, and the output becomes input for the next turn. As tokens grow, accuracy and recall degrade ("context rot"), so curating what goes in matters as much as window size. Current Claude models have 1M-token windows with up to 128k output tokens per request. Prompt caching changes what you pay for a repeated prefix, not whether it counts toward the window.

**Gaps it shows**

1. **Everything you and the tools send fills the same window, and you pay for it again every turn.**
   - Each turn's input is "all previous conversation history plus the current user message".
   - Tool definitions, tool results, images, PDFs and the model's own output and thinking all count.
   - The `usage` field reports what each request consumed. A token counting API can estimate a request before you send it.
2. **More context is not better: context rot.**
   - "As token count grows, accuracy and recall degrade."
   - Curating what is in the window is as important as how much space there is.
3. **Chat apps and the API behave differently when the conversation gets long.**
   - Via the API, previous turns "are preserved completely" until you hit the limit.
   - A footnote says chat interfaces such as claude.ai "can also manage the context window on a rolling 'first in, first out' basis". The oldest turns can drop out silently.
4. **What happens at the limit.**
   - If the input alone exceeds the window, the API returns a 400 `invalid_request_error` ("prompt is too long") on every model.
   - On Claude 4.5 and newer, input plus `max_tokens` may exceed the window. Generation then stops with `stop_reason: "model_context_window_exceeded"`.
   - Server-side compaction (beta, Claude 4.6 and later) summarizes earlier parts so a conversation can continue.
   - Context editing can clear old tool results and old thinking blocks.
5. **Window sizes as of October 2026.**
   - 1M tokens is the default with no beta header on Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5.5, Opus 5, Opus 4.8, 4.7, 4.6, Sonnet 5.5, Sonnet 5, Sonnet 4.6, Haiku 5.5 and Mythos Preview.
   - On those models, long context bills at standard pricing, except Haiku 5.5, where prompts over 100,000 tokens cost more.
   - Other models, including Sonnet 4.5 (deprecated), have 200k.
   - Up to 600 images or PDF pages per request (100 on 200k models). Request size limits may hit before the token limit.
6. **Thinking tokens: billed as output, part of `max_tokens`, and sometimes carried forward.**
   - Thinking tokens are a subset of `max_tokens`, billed as output, and count toward rate limits.
   - On Opus 4.5 and later, Sonnet 4.6 and later, Haiku 5.5, Fable and Mythos models, earlier thinking blocks are kept by default. They count as input on later turns and are billed again as input.
   - On older models they are stripped automatically.
   - During tool use you must return the thinking block unmodified, with its cryptographic signature. A modified block causes an error.
7. **Context awareness differs by model.**
   - Sonnet 5, Sonnet 4.6, Sonnet 4.5 and Haiku 4.5 get an injected token budget and "Token usage: X/Y; Z remaining" warnings after each tool call.
   - Opus 4.7 and later, Sonnet 5.5, Haiku 5.5, Fable and Mythos 5.x do not. On these, explicit "task budgets" are available in beta.
8. **Prompt caching: an exact-prefix cache with its own price list.**
   - "Cache hits require 100% identical prompt segments", in the order tools, then system, then messages.
   - A change at one level invalidates that level and everything after it.
   - Write price: 1.25x base input for the 5-minute TTL, 2x for the 1-hour TTL.
   - Read price: 0.1x by default. Opus 5.5 and Sonnet 5.5 read at 0.05x; Fable 5.1 and Mythos 5.1 at 0.025x.
   - The TTL refreshes free each time the cache is read.
   - Minimum cacheable prefix: 512 tokens on current 5.x models, up to 4,096 on Opus 4.5/4.6 and Haiku 4.5. Shorter prompts are silently not cached, with no error.
9. **What silently breaks the cache.**
   - Changing tool definitions breaks everything.
   - Toggling web search or citations, or switching between fast and standard speed, breaks the system and messages levels.
   - Changing `tool_choice` or adding or removing images breaks the messages level.
   - Changing thinking parameters always invalidates the message cache. Dropped thinking blocks invalidate messages too.
   - Common mistake: a per-request timestamp in the cached prefix means a new hash every request, so it never hits.
   - The 20-block lookback can miss an earlier cache entry in a long conversation.
   - Check `cache_creation_input_tokens` and `cache_read_input_tokens` in `usage`. If both are 0, nothing was cached.

**Framings it implies are outdated**
- "A bigger context window means it remembers everything I said." Context rot, and FIFO dropping in chat apps.
- "The model remembers the conversation between messages." The API is stateless and the whole history is resent.
- "Caching saves context space." It saves money and time only.
- "200k tokens is the Claude limit." Current models are 1M by default.

**Quotes**
- "As token count grows, accuracy and recall degrade"
- "Cache hits require 100% identical prompt segments" (Prompt caching page)

---

## S013 - Gemini thinking (Google AI for Developers)

- **Author:** Google
- **Date:** last updated 2026-10-09 UTC. Confirmed by the page footer and by the HTTP Last-Modified header, "Fri, 09 Oct 2026 22:11:39 GMT".
- **URL:** https://ai.google.dev/gemini-api/docs/generate-content/thinking
- **Note:** the page title reads "Gemini thinking | Gemini Generate Content API (Legacy)". Google now labels the generateContent API "Legacy".
- **Companion source read (cross-vendor):** OpenAI, "Reasoning models" guide, undated live docs, https://developers.openai.com/api/docs/guides/reasoning. platform.openai.com/docs/guides/reasoning 301-redirects there.

**Summary.** Gemini 3 and 2.5 models think by default. On Gemini 3 you control depth with `thinkingLevel` (`minimal`, `low`, `medium`, `high`). Gemini 2.5 uses `thinkingBudget` instead: a token range, `-1` for dynamic, `0` to disable where allowed.
- Some models cannot turn thinking off: Gemini 3.1 Pro, 2.5 Pro, and the Gemini 3 Flash and Flash-Lite models. `minimal` is not the same as zero.
- `max_output_tokens` includes thought tokens. If the cap is hit while the model is still thinking, the answer comes back truncated or empty and the thinking is still billed.
- You are billed for the full thoughts but receive only optional summaries.

OpenAI's guide describes the same mechanism:
- Reasoning tokens are invisible, billed as output, and occupy the context window.
- `max_output_tokens` covers them. Hitting it gives `status: incomplete` "before any visible output" while input and reasoning are still billed.
- OpenAI advises reserving at least 25,000 tokens when starting out.

**Gaps it shows**

1. **Thinking is billed output you mostly do not see.**
   - Gemini bills the full thought tokens even though only a summary is returned.
   - OpenAI bills reasoning tokens as output, and the API never returns the raw reasoning.
   - Claude bills thinking tokens as output. Claude Code docs: "You are charged for all thinking tokens generated, even when collapsed or redacted."
   - Where to see it: `thoughtsTokenCount` (Gemini) and `usage.output_tokens_details.reasoning_tokens` (OpenAI). OpenAI's example shows 1,024 reasoning tokens out of 1,186 output tokens.
2. **Empty or cut-off answers are often a token-cap problem, not a model failure.**
   - The output cap includes thinking. Hitting it during reasoning gives `finish_reason: MAX_TOKENS` (Gemini) or `status: incomplete` with reason `max_output_tokens` (OpenAI), with little or no visible text, and still billed.
   - Google's advice: to save cost, lower `thinking_level` rather than setting a small `max_output_tokens`.
3. **Thinking cannot always be switched off.**
   - Gemini 3.1 Pro: "You cannot disable thinking." 2.5 Pro: the budget starts at 128. Gemini 3 Flash and Flash-Lite also cannot fully turn it off.
   - OpenAI: GPT-6 Astra rejects `none` with HTTP 400, and GPT-6.1 Sol rejects `none` and `minimal`.
   - Claude Code docs: thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models.
   - The `minimal` level may still reason a little on complex tasks.
4. **Defaults differ by model and vendor, and you are probably on the default.**
   - Gemini defaults: `high` for 3.1 Pro, `medium` for 3.8 Flash and 3.6 Flash.
   - OpenAI defaults to `medium` on gpt-5.5, GPT-5.6, GPT-6.1 Sol, GPT-6 Sol and GPT-6 Luna.
   - Higher levels raise latency: with `high`, the first output token may take significantly longer to arrive.
5. **Budgets are hints, not hard limits.**
   - "Depending on the prompt, the model might overflow or underflow the token budget."
   - Thinking levels and budgets apply to the raw thoughts, not to the summaries.
6. **Thought summaries are not the reasoning.**
   - Summaries are condensed versions, opt-in (`includeThoughts`, or OpenAI `reasoning.summary`).
   - They are useful for seeing where the model went wrong, but they are not a transcript.
7. **The API is stateless, so the reasoning context has to travel with the request.**
   - Gemini "thought signatures" carry encrypted thought context and are required for function calling on Gemini 3. Pass the entire response back, and do not merge or concatenate signed parts. The SDK does this automatically. Hand-edited history or raw REST breaks it.
   - OpenAI: carry `encrypted_content` reasoning items back in stateless mode (`store: false` or Zero Data Retention). For function calling, pass back all reasoning items, function calls and outputs since the last user message.
   - OpenAI: reasoning can carry over only within the same model family. GPT-5.6 renders earlier turns' reasoning by default, and pre-5.6 models do not.
   - Signatures add input tokens.
8. **Match thinking level to the task.**
   - Easy tasks such as fact retrieval and classification need little or none.
   - Medium tasks such as comparisons need the default.
   - Hard tasks such as complex math and coding need high.
   - For long outputs, steer the amount of thinking in the prompt so more of the budget goes to the answer.

**Framings it implies are outdated**
- "Tokens = the words in the answer." Hidden reasoning tokens are often most of the output bill.
- "Turn thinking off to save money." Often not possible on current flagship models.
- "An empty response means the model broke." It is often the output cap eaten by thinking.

**Quotes**
- "returns truncated or empty output (while still billing for any thinking tokens generated)"
- "You cannot disable thinking." (Gemini 3.1 Pro)

---

## S014 - An update on recent Claude Code quality reports (postmortem)

- **Author:** Anthropic (Engineering blog). No individual author is named.
- **Date:** 2026-04-23. Confirmed on the page.
- **URL:** https://www.anthropic.com/engineering/april-23-postmortem

**Summary.** Users reported that Claude Code had got worse. Anthropic traced it to three separate changes in Claude Code, the Agent SDK and Cowork. None of them touched the API or the model weights: Anthropic says it confirmed the API and inference layer were unaffected. Because each change hit a different slice of traffic on a different schedule, the combined effect looked like broad, inconsistent degradation. All three were fixed by 2026-04-20 (v2.1.116), and usage limits were reset for all subscribers on 2026-04-23.

**The three changes**
1. **Default reasoning effort lowered.**
   - Claude Code's default went from `high` to `medium` on 2026-03-04, for Sonnet 4.6 and Opus 4.6.
   - The reason was that `high` sometimes thought so long the UI looked frozen, with high latency and token use.
   - Internal evals showed `medium` slightly less intelligent but much faster.
   - Users felt Claude got less intelligent. Most kept the default even after UI notices and an inline effort selector were added.
   - Reverted 2026-04-07. Anthropic wrote: "This was the wrong tradeoff."
   - Defaults afterwards: `xhigh` for Opus 4.7, `high` for the others.
2. **A context-management bug cleared prior reasoning on every turn.**
   - Shipped 2026-03-26. It was meant to clear old thinking once from sessions idle for more than an hour (API header `clear_thinking_20251015`, `keep:1`), to cut the cost of resuming.
   - The bug cleared thinking on every later turn for the rest of the session, keeping only the latest reasoning block.
   - Claude seemed forgetful and repetitive, made odd tool choices and lost track of why it had acted.
   - The dropped blocks also caused cache misses, which Anthropic believes drained usage limits faster than expected.
   - Fixed 2026-04-10 (v2.1.101).
   - It was hard to find. It appeared only in stale sessions and was masked by two unrelated experiments.
   - It passed human and automated code review, unit and end-to-end tests, automated verification and dogfooding. Root-causing it took more than a week.
   - In back-testing, Opus 4.7 with full repository context found the bug in Code Review and Opus 4.6 did not.
3. **A verbosity system prompt.**
   - Shipped 2026-04-16 with Opus 4.7. It said "keep text between tool calls to ≤25 words" and capped final answers at 100 words unless the task needed more.
   - Combined with other prompt changes, it caused a 3% drop on a broader eval for both Opus 4.6 and 4.7.
   - It had passed the earlier internal evals. Reverted 2026-04-20.

**What Anthropic is changing**
- More staff on the public build.
- A per-model eval suite and line-by-line ablations for every system prompt change.
- Model-specific changes gated to the models they target.
- Soak periods and gradual rollouts for anything that trades against intelligence.
- An @ClaudeDevs account on X and centralized GitHub threads.
- It credits `/feedback` reports and reproducible public examples for helping.

**Gaps it shows**

1. **Quality is model + harness + settings + version, not the model name.**
   - Same weights, same API. A default setting, a context bug and a system prompt line changed perceived intelligence.
2. **Effort is a quality knob most people never touch.**
   - Most users kept a lower default even after it was surfaced in the UI.
   - Lower effort is faster and cheaper but measurably less capable.
3. **What stays in context between turns shapes behaviour.**
   - Losing earlier reasoning made the agent repeat itself and forget its own plan.
   - The symptom looks like "the model got dumber". The cause was the harness.
4. **Cache misses quietly multiply cost and drain plan limits.**
   - The bug's dropped thinking blocks broke the cache prefix, so each turn re-processed the full history.
5. **Small system-prompt wording changes can cost real capability.**
   - A 25-word limit between tool calls cost 3% on evals.
6. **Regressions can slip past tests, review and dogfooding.**
   - Your own reproducible examples and feedback reports are part of how harness regressions get found.

**Framings it implies are outdated**
- "They secretly nerfed the model." Here the API model was unchanged. Anthropic states it "never intentionally degrade[s]" its models.
- "If it got worse, switch models." The cause may be the harness version, the effort default or the context state.

**Quotes**
- "This was the wrong tradeoff." (on lowering default effort)
- "Length limits: keep text between tool calls to ≤25 words." (the system prompt line)

---

## S015 - Extend Claude Code (features overview)

- **Author:** Anthropic (Claude Code docs)
- **Date:** undated live docs. There is no visible date and no Last-Modified header (ETag only, HTTP check 2026-10-12). It covers recent features such as dynamic workflows, cross-session messaging and Artifacts.
- **URL:** https://code.claude.com/docs/en/features-overview
- **Companion sources read (same docs set, all undated live docs; the version numbers they mention are noted):**
  - "Explore the context window", https://code.claude.com/docs/en/context-window (mentions v2.1.198)
  - "How Claude Code uses prompt caching", https://code.claude.com/docs/en/prompt-caching (mentions up to v2.1.283)
  - "Model configuration", https://code.claude.com/docs/en/model-config (first 100,000 characters read; mentions v2.1.293)
  - "Skills", https://code.claude.com/docs/en/skills (first 100,000 characters read)
  - "MCP", https://code.claude.com/docs/en/mcp (first 100,000 characters read)

**Summary.** Claude Code is a model plus built-in tools in an agentic loop. Extensions plug into different points of that loop:
- **CLAUDE.md:** always-on context.
- **`.claude/rules/`:** always-on, or path-scoped.
- **Output styles:** role, tone and format.
- **Skills:** on-demand knowledge and workflows. Custom commands are now merged into skills.
- **Code intelligence (LSP):** symbol navigation and type errors.
- **MCP:** external tools and data. claude.ai "connectors" are MCP servers.
- **Subagents:** isolated context.
- **Dynamic workflows:** scripted fan-out of subagents.
- **Hooks:** deterministic scripts on lifecycle events.
- **Plugins:** the packaging layer.

Each extension has a different context cost. The key line: an instruction in CLAUDE.md or a skill "is a request, not a guarantee", while a PreToolUse hook that blocks the action "is enforcement".

**Where each lives, when it loads, and what it costs (from the page and its companions)**

| Feature | Lives in | Loads | Context cost |
|---|---|---|---|
| CLAUDE.md | `~/.claude/CLAUDE.md`, project root, subfolders (nested load on demand) | Session start, full content | Every request. Keep under 200 lines. |
| `.claude/rules/` | `.claude/rules/*.md`, optional `paths:` frontmatter | Every session, or when a matching file is touched | Unscoped: every request. Scoped: only after a match. |
| Output style | built-in or custom | Session start / on switch | Every request (none for Default) |
| Skill | `~/.claude/skills/<name>/SKILL.md`, `.claude/skills/...`, `<plugin>/skills/...`, managed | Description at start, full body when used | Low. Descriptions are sent every turn, truncated at 1,536 chars. Zero for `disable-model-invocation: true`. |
| Command | `.claude/commands/x.md` | Same as a skill | "Custom commands have been merged into skills" |
| MCP server | local/user scope in `~/.claude.json`, project scope in `.mcp.json`; claude.ai connectors auto-available | Session start: tool names and server instructions. Schemas deferred via tool search (on by default). | Low until a tool is used. Output over 10k tokens warns; 25k is the default cap. |
| Subagent | built-in or custom agent files | When spawned | Its own window. Only the summary comes back. |
| Hook | settings.json | On lifecycle event; runs outside the model | Zero unless it returns `additionalContext`. Plain stdout on exit 0 goes to the debug log only. |
| Plugin | installed from a marketplace; namespaced (`/plugin:skill`) | Bundles skills, hooks, subagents and MCP | The cost of its parts |
| Code intelligence | plugin per language | After edits and on lookup | Low. Can reduce file reads. |

**Gaps it shows**

1. **Rules in prose are requests. Hooks and permissions are enforcement.**
   - "never edit .env" in CLAUDE.md or a skill is a request. A PreToolUse hook that blocks the edit is enforcement.
   - On CLAUDE.md and output styles: "Claude follows both as instructions, so neither is enforced."
   - "If a rule must hold every time, make it a hook."
2. **Skills vs commands vs plugins vs connectors vs MCP, untangled.**
   - A command and a skill both create `/name`; commands were merged into skills.
   - A skill is knowledge or a workflow. MCP is a connection to an external system with tools. A connector is an MCP server added in claude.ai, which is auto-available in Claude Code when you are logged in with that account.
   - A plugin is the installable bundle of skills, hooks, subagents and MCP servers, distributed through a marketplace.
   - A subagent is an isolated worker. A hook is a script triggered by an event.
3. **Everything you add costs context and can make Claude worse.**
   - "Too much can fill up your context window, but it can also add noise."
   - The page warns that skills may not trigger correctly, or Claude may lose track of your conventions.
   - CLAUDE.md is sent in full on every request. Skill descriptions are sent every turn "whether or not Claude ever uses it".
   - `/context` shows the live breakdown, and `/context all` shows per-MCP-tool token use.
4. **Before you type a word, the window is already full of things you cannot see.**
   - The simulation shows: system prompt (~4,200 tokens), auto memory (first 200 lines or 25KB of MEMORY.md), environment info, deferred MCP tool names, skill descriptions, user and project CLAUDE.md.
   - "Your prompt is tiny compared to what's already loaded."
   - The terminal shows a one-line "Read auth.ts" while 2,400 tokens enter context.
   - Test output shows as a pass count while 1,200 tokens enter context.
5. **Skill choice depends on the description.**
   - Claude matches your task against skill descriptions. Vague or overlapping descriptions lead to the wrong skill or none.
   - Invoke a skill with `/name` to be sure.
   - Put the key use case first, because of the 1,536-character truncation.
6. **Compaction keeps a summary, not the conversation.**
   - Auto-compaction runs near the limit, by default around 967K tokens on native-1M models.
   - It replaces the conversation with a structured summary: requests, key concepts, files, errors and fixes, pending tasks. "Full tool outputs and intermediate reasoning are gone."
   - Restored afterwards: system prompt, output style, root CLAUDE.md, unscoped rules and auto memory (from disk); a fresh git status; the plan-mode plan; up to 5 recently modified files (a file over 5,000 tokens comes back as a path only); invoked skills (capped at 5,000 tokens each and 25,000 total, oldest dropped first).
   - Lost: path-scoped rules and nested CLAUDE.md are summarized away (they reload on demand), the skill listing is not re-injected, and instructions you gave only in chat survive only as summary.
   - Tools: `/compact focus on X`, `/rewind` "Summarize from here", `/autocompact 500k`, and `/clear` between unrelated tasks.
7. **Editing CLAUDE.md mid-session does nothing until `/clear`, `/compact` or a restart.**
   - Root and user CLAUDE.md are read once at session start.
8. **Hidden cost: actions that throw away the prompt cache.**
   - The model does not remember between requests. Claude Code "re-sends the full context" every turn and relies on an exact-prefix cache.
   - Cache-breakers mid-session:
     - switching models (each model has its own cache), including `opusplan` plan-mode toggles and skills that name another model;
     - changing effort on most models (kept on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 with an API key or a subscription);
     - turning on fast mode;
     - adding or removing MCP servers when tools are loaded upfront;
     - denying a whole tool without tool search;
     - `/compact`;
     - accumulating many images;
     - a Claude Code upgrade.
   - Cache-safe: editing repo files, editing CLAUDE.md, changing permission mode, changing output style, invoking skills, `/recap`, `/rewind`, spawning a subagent.
   - Cache lifetime:
     - The main conversation gets a 1-hour TTL on a subscription within plan usage.
     - It gets 5 minutes on an API key, a cloud provider, or once you are on usage credits.
     - Subagents get 5 minutes by default.
     - The first turn back after a break re-processes everything. `/compact` on a cold cache is the most expensive.
   - `/usage` shows a "Prompt cache (main)" line with hit ratio, misses and the likely cause.
9. **Subagents protect your context but start blind.**
   - Only the final summary returns: in the example, the subagent read 6,100 tokens and returned 420.
   - A subagent starts without your conversation history or auto memory. It gets CLAUDE.md, except the built-in Explore and Plan agents, and the task prompt Claude writes for it.
10. **Effort and thinking are settings you own.**
    - Effort levels are `low`, `medium`, `high`, `xhigh`, `max`.
    - Defaults: `medium` on Opus 5.5, Sonnet 5.5 and Haiku 5.5; `xhigh` on Opus 4.7; `high` elsewhere.
    - Opus 5.5 is the default model on Pro, Max, Team, Enterprise and the Anthropic API.
    - `max` "is prone to overthinking".
    - `ultrathink` in a prompt deepens reasoning for one turn. "Think hard" is not a keyword.
    - Thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models. You are charged for thinking even when it is collapsed.
11. **Extensions are a trust and supply-chain surface.**
    - MCP docs: "Verify you trust each server before connecting it". Servers that fetch external content can expose you to prompt injection.
    - Project `.mcp.json` servers need approval in interactive sessions.
    - Skills docs: skills "can bundle and run scripts in any language".
    - A project skill's `allowed-tools` applies even in a `-p` run in a folder you have never trusted. A skill can grant itself broad tool access, so review `allowed-tools` of skills checked into a repository before running Claude Code there.
    - Use `disable-model-invocation: true` for skills with side effects, so they run only when you name them.
12. **Build the setup from triggers, not up front.**
    - If Claude gets a convention wrong twice, add it to CLAUDE.md.
    - If you paste the same playbook a third time, make it a skill.
    - If you keep copying data Claude cannot see, connect it with MCP.
    - If a side task floods your context, use a subagent.
    - If something must happen every time, write a hook.
    - If a second repo needs the same setup, make a plugin.
    - A repeated mistake is a CLAUDE.md edit, not a one-off correction in chat.

**Framings it implies are outdated**
- "Put every rule in the system prompt / CLAUDE.md and the agent will obey."
- "Slash commands and skills are different things." They were merged.
- "More tools and skills make the agent smarter." Each one adds context and noise.
- "The agent sees what I see in the terminal." It sees far more: the full file contents and tool output.

**Quotes**
- "is a request, not a guarantee" (about "never edit .env" in CLAUDE.md or a skill)
- "A PreToolUse hook that blocks the edit is enforcement."

---

## Cross-source synthesis (for lesson writers; every point is traced above)

- **One sentence:** the answer you get is produced by a configuration (S011, S014), not by "the model". That configuration is weights + harness system prompt + what is in the context window + tools + effort/thinking level + decoding + cache state + version.
- **Where things live:**
  - In the weights: frozen and dated.
  - In the context window: bounded, resent every turn, degrading as it grows, summarized or dropped when full.
  - Outside: memory files, CLAUDE.md, logs, connectors, governed by the product.
- **What thinking costs:** hidden output tokens, billed in full, inside the output cap, often impossible to switch off. The effort default decides how much you get. On Claude Code's default model (Opus 5.5) the default effort is `medium` as of this fetch.
- **Why "it got dumber" is often the harness:** in the April 2026 postmortem, a lowered effort default, dropped reasoning between turns and one system-prompt line each degraded quality while the API model was unchanged. The context bug also broke the cache and drained plan limits.
- **Human vs agent:** the agent can manage its own context, read its own errors, and use tools. It cannot see or vouch for:
  - which harness version and settings it runs under;
  - whether earlier reasoning was dropped;
  - whether an MCP server or skill is trustworthy;
  - whether a rule written in prose will hold.

  These are the human's job: choose effort and model at the start, keep the context clean, put must-hold rules in hooks or permissions, vet extensions, and report reproducible regressions.
