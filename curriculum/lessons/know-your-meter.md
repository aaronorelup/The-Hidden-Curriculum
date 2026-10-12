---
key: know-your-meter
id: 06.03
title: What your AI work really costs, and how to cap it
district: Directing Well
module: 06 Scaling up
status: todo
legacy: []
minutes: 15
concepts: [C055, C056, C057, C058, C059, C061]
sources: [S016, S017, S128, S139, S131, S132, S133, S137, S135, S138, S140, S141, S046, S018, S107, S136, S014, S012, S134, S003, S030, S033, S008, S080, S111, S035, S020]
lead: [S017]
---
# What your AI work really costs, and how to cap it

**Purpose (the first spoken sentence):** In this lesson you'll learn what your AI work actually costs and what stops the spending: which meter you are on, why every turn re-reads everything, what caching really discounts, why a cheaper model or a higher effort setting may not do what you expect, and why a budget alert is not a cap.

**Conclusion:** Most of the bill is the agent re-reading its own conversation, so know which meter you are on, keep sessions short, judge cost per useful result rather than per token, and put a cap that actually stops on every key.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Know your meter." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; Module 06 Scaling up, lesson 3 of 3 (06.01 cut the work into slices, 06.02 checked them; this is what the slices, the agents and the checks cost, and who stops it).

**Lead source (audit, 2026-10-12):** S017 (Aaron Orelup). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S016, S017, S128, S139); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Order in the lesson: C055 (which meter), C056 (what the meter counts), C057 (the cache discount and what breaks it), C058 and C059 (the two dials: model and effort), C061 (caps that stop). Every price, plan name, window, version number and default below goes on a card dated "as of 2026-10-12" and is re-checked on the day of recording: Anthropic itself warns that updates "may change how features work, including cost reporting" (S016).

**Settings and versions (audit, 2026-10-12):** the spoken script teaches the vendor-neutral model: which meter, context times turns times agents, the exact-prefix cache rule, and caps that alert versus caps that stop. Setting names, environment variables, flags and version numbers appear only on one dated "as of" card per concept and on the lesson page (see "On the lesson page, not in the narration" below), never in narration.

### C055 Know your meter

1. **Two billing worlds.** Pro, Max, Team and Enterprise draw on a plan allowance; an API key, the Claude Console or a cloud provider (Bedrock, Google Cloud, Foundry) bills every token; in a mixed organisation each developer is metered by however they signed in (S016). Depth: **teach**.
2. **A stray key switches you silently.** If `ANTHROPIC_API_KEY` is set, Claude Code uses that key instead of your Pro or Max subscription, and the work is billed as API charges "rather than using your subscription's included usage" (S132). A stray key can also route you through a low-tier key and its 429 errors; run `/status` and confirm the active credential is the one you expect (S131). `claude auth status` reports `authMethod` as `claude.ai`, `api_key` and so on (S133). Depth: **teach** (where environment variables come from is C126, taught in keys-public-secret-and-leaked).
3. **The dollar figure in `/usage` is not your bill on a plan.** The Session block is computed locally at list price; for Pro and Max subscribers it "isn't relevant for billing purposes"; for API users the authoritative bill is the Console's Usage page. The plan breakdown is built from local history on this machine, so usage on claude.ai and other devices is left out (S016). Depth: **teach**.
4. **What the allowance is.** A rolling five-hour window and a weekly window, shared between Claude and Claude Code, with a separate weekly Fable limit on Max (S132); on Team and Enterprise the seat allowance is also shared with chat and Cowork (S016). "A single burst of heavy activity, such as a large workflow fanout, can exhaust the weekly allowance before the session window resets" (S131). Depth: **teach**.
5. **Read the limit message before acting.** A session or weekly limit is shared across all models, so `/model` doesn't help; an Opus or Sonnet limit covers one family, so switching family does; a spend limit is a cap someone set; "Server is temporarily limiting requests (not your usage limit)" is a short throttle; a context or auto-compact warning is not a usage limit at all; the early warning reads `You've used 85% of your session limit` (S131, S016). Depth: **brief**.
6. **Usage credits keep you going at API rates.** With credits on and no monthly spend limit, `/usage` shows `Unlimited`; while you draw on credits, the main conversation's cache lifetime drops from an hour to five minutes (S016, S128). Depth: **brief**.
7. **Hitting a limit no longer always stops the work.** Claude Code can now wait out the reset and continue the interrupted task on its own (S016, S134; the version that added it is on the lesson page). Depth: **one line** (unattended continuation is part of C060 in agents-that-run-while-youre-away).
8. **Max's included API credits "can't be used in Claude Code or the Claude apps"** (S132); separately, Anthropic began a new monthly API credit for Max and Team subscribers the week of 2026-10-07 (S135). Depth: **one line**.

Dropped here: Zapier's per-activity billing and other automation meters are C060 in agents-that-run-while-youre-away.

### C056 Cost is context length times turns times agents

1. **The model remembers nothing between requests.** Each turn re-sends the system prompt, project context, every earlier message and tool result, and the new message; each batch of tool results is another request; so "a one-line question in a session that has been open all day still draws usage for the whole conversation" (S128, S016). Depth: **teach** (what fills the window is C025-C026 in what-the-agent-sees-each-turn; this lesson is the bill).
2. **Aaron's own numbers.** 31.6 billion tokens across 128,000 requests: cache reads were 97.0% of tokens; an average Opus request read about 334,000 cached tokens to write about 1,000 output tokens; uncached input was about 2 tokens a request (S017). Depth: **teach**.
3. **Agents multiply it.** Each agent has its own context window; agent teams use about 7x the tokens of a standard session when teammates run in plan mode, and each teammate keeps consuming tokens until it exits; subagents keep verbose output out of your conversation but their requests still draw on your usage (S016). A fork inherits the parent's whole history, while a fresh subagent starts small (S128); two forked subagents started at 523K and 304K tokens and ran for 10.7 and 8.7 hours (S107). Depth: **teach**.
4. **A fleet case.** A CTO's Cursor bot fleet cost about $1,500 in a week: the busiest bots re-read "roughly 80k to 90k tokens per step", and about a third of all turns were bots waking other bots; staff found nothing wrong with billing, only with how the bots were used (S018). Depth: **brief**.
5. **What works.** `/clear` between unrelated tasks costs nothing and resets the Session totals (S016); keep standing instructions in CLAUDE.md or skills and task state in files, so a fresh start loses little (S016); past a few hundred thousand tokens, write what matters to a file and start fresh from it (S003); tell bots to message each other only when the other must act, with no thanks or progress pings (S018). Depth: **teach**.
6. **Shorter is not automatically cheaper.** `/compact` is itself a large request (S016), and on a cold cache it re-processes the full history uncached, the most expensive way to resume (S128); one team found summarizing cost about twice as much as keeping the full history, because it rewrote the cached prefix (S136). Test on your own work. Depth: **brief**.
7. **Orchestration has overhead:** on small, already-diagnosed tickets an orchestrating agent spent 4-8 times the tokens of fixing them directly (S030). Depth: **one line**.
8. **Budget a coding seat above a chat seat:** "one debugging session can consume more than a day of chat"; enterprise deployments average about $13 per developer per active day, $150-250 a month, with 90% of users under $30 a day (S016). Depth: **one line**.

### C057 Prompt caching: an exact-prefix discount that silently breaks

1. **The cache matches the start of each request exactly.** A change anywhere in that prefix recomputes everything after it; "There is no per-file or per-segment caching". Claude Code orders each request so what rarely changes comes first: system prompt and tool definitions, then project context (CLAUDE.md, memory), then the conversation (S128). Depth: **teach**.
2. **Cached is cheaper, not free.** Current list prices per million tokens, Opus 5.5 vs Sonnet 5.5: input $4 vs $2; five-minute cache write $5 vs $2.50; one-hour write $8 vs $4; cache read $0.20 vs $0.10; output $20 vs $10. Reads cost 0.05x input on these two models (0.025x on Fable 5.1, 0.1x on others) (S137); Sonnet 5.5's cache-read price was halved on 2026-10-07 (S135). In Aaron's history, cache reads were 45% of cost at Opus prices, and cache writes were 2.5% of tokens but 34% of cost (S017). Depth: **teach**.
3. **A miss is expensive.** The next request re-processes the context and writes it back at the write rate; on Opus 5.5 a one-hour write costs 40 times a read per token ($8 vs $0.20; the research crew's arithmetic from S137). Depth: **brief**.
4. **How long the cache lives.** The main conversation gets one hour on a subscription within plan usage, five minutes on usage credits, an API key or a cloud provider; subagents, workflows, teammates, forks and compaction get five minutes even on a subscription; every hit resets the timer, and the first message after a longer break re-processes everything. A setting chooses the lifetime; its name and version are on the lesson page (S128, S016). Depth: **teach**.
5. **What breaks it, and what doesn't.** Breaks: switching model (including `opusplan` plan-mode toggles, a skill that names another model, automatic fallback), changing effort on most models, turning on fast mode, connecting or removing an MCP server when tools load upfront, denying a whole tool without tool search, `/compact`, many images piling up, upgrading Claude Code. Keeps: editing repo files, editing CLAUDE.md (which also doesn't apply until `/clear`, `/compact` or a restart), changing permission mode or output style, invoking skills, `/recap`, `/rewind`, spawning a subagent. On Opus, Sonnet and Haiku 5.5 and Fable 5.1 with an API key or subscription, changing effort keeps the cache, but not on Bedrock, Google Cloud or a Claude apps gateway (S128). Depth: **teach** (as one card, not a recited list).
6. **Where to see it.** `/usage` now shows a prompt-cache line: the share of input served from cache, the misses, a likely cause, and whether the cache is warm or cold (versions on the lesson page); Claude Code asks before a model switch while the cache is warm; on Pro and Max it offers to resume a large session from a summary after a long break (S016, S128). Depth: **brief**.
7. **A real case of a silent drain.** In April 2026, dropped thinking blocks caused cache misses that Anthropic believes drove reports of usage limits draining faster than expected; it reset all subscribers' limits on 2026-04-23 (S014). Depth: **one line**.
8. **For people building apps on the API:** stable content first, variable content last; a timestamp at the top means the cache never hits (S012); if both cache fields read 0 nothing was cached; a gateway that strips the cache markers bills the whole history as uncached input on every turn (S128). Depth: **one line** (the depth belongs to the backlog item "Prompt caching and model choice in depth").

### C058 A cheaper model is not a cheaper result

1. **Half the price on paper, about 2% cheaper in practice, at the old price.** Aaron's gauntlet (2026-09-28): on Loom, Opus cost $60.92 and Sonnet $79.97 for identical 10/10 scores, with Sonnet making 1.2-2.4 times as many requests at the same effort; on Lockkeeper, Sonnet was cheaper ($132.00 vs $151.97) but Opus won four of five head-to-heads; across all three tests about $249 vs $255, about 2% cheaper for Sonnet (S017). Depth: **teach**.
2. **Why, and why the number is already stale.** A model that needs more turns re-reads the cached conversation on every extra turn, and at the time cache reads cost $0.20 on both models (S017). On 2026-10-07 Sonnet 5.5's cache reads were halved to $0.10 (S135, S137), so the 2% figure must not be quoted as current: teach the method, and re-run or re-price before quoting any ratio. Depth: **teach**.
3. **Per-token prices don't compare across tokenizers.** Haiku 5.5's tokenizer uses about 1.25 times the tokens Haiku 4.5 used for the same prompt, "a hidden price increase", and its price rises fivefold for prompts over 100,000 tokens (S135, S137). Depth: **brief**.
4. **Pick a model per phase, then measure.** The Stanford lecturer uses a strong model for research, proposals and planning, where the thinking happens, and lighter models to implement and test (S003); Anthropic's docs say Sonnet "handles most coding tasks well and costs less than Opus" and suggest `model: haiku` for simple subagents (S016). Treat both as starting points to measure. Depth: **brief**.
5. **Measure cost per useful result on your own work.** Quality is part of the price (Opus won four of five Lockkeeper head-to-heads), and Aaron counted exact tokens per session from transcripts instead of estimating (S017). Depth: **brief**.
6. **What professionals do:** only 6.4% of tool switches were for lower cost against 25.1% for better output, and 38.1% of organisations set limits on usage or spending (S080). Depth: **one line**.

### C059 Effort is a work dial and a quality knob

1. **Effort mostly buys more steps.** On Lockkeeper, Opus at Max made about 9 times the requests of Low but thought only about 1.7 times as long per action; on Loom, Max cost 16 times Low on Opus ($2.00 to $32.40) and about 18 times on Sonnet ($2.45 to $43.86), for the same 10/10 score (S017). Willison's Haiku 5.5 test: about 0.09 cents and 7 seconds at low effort, about 3.38 cents and 5 minutes 9 seconds at max (S135). Depth: **teach**.
2. **More is not reliably better.** Both XHigh runs on Lockkeeper scored worse than both Low runs on the hidden canals (S017). Anthropic: `max` "may show diminishing returns and is prone to overthinking, so test before adopting it broadly" (S138). Depth: **teach**.
3. **Where higher effort earns its price:** `high` for work where verification matters or edge cases are likely, such as fixing a bug in an existing codebase; `max` for hard problems Claude works through without you, such as finding security vulnerabilities (S138). Depth: **brief**.
4. **Defaults move under you.** Claude Code lowered its default effort on 2026-03-04 and reverted on 2026-04-07, calling it "the wrong tradeoff", and most users never touched the default (S014). Today the default is `medium` on Opus, Sonnet and Haiku 5.5, `xhigh` on Opus 4.7, `high` elsewhere; Pro's default model changed to Opus 5.5; an effort level set in your user settings "doesn't count for Opus 5.5" (setting name and version on the lesson page); and the scale is calibrated per model, so the same name is not the same amount of work on two models (S138). Check `/effort` and `/model` after an update. Depth: **brief**.
5. **Thinking is billed as output, the dearest kind,** and can't be turned off on Opus, Sonnet and Haiku 5.5 or the Fable models (S016). `ultrathink` in a prompt deepens one turn; "think hard" is not a keyword (S138). Depth: **one line** (thinking tokens in depth are C029, in the backlog).
6. **Cap open-ended loops.** In print mode `--max-turns` has no limit by default and `--max-budget-usd` sets a dollar ceiling (S133); give "fix until the checks pass" a round limit or exit criteria (S008); Aaron stopped a Sonnet Max session by hand after 8 hours 42 minutes (S017). Depth: **brief** (stop rules for long runs are C096 in agents-that-run-while-youre-away).
7. **Thoroughness can come from outside the model** instead of from Max: a checklist, or a stop hook that won't let the session end until the list is done (S017, S111). Depth: **one line**.

### C061 Caps that alert are not caps that stop

1. **An alert is not a cap.** Rod Danan had spending caps, was charged about $10,138, mostly for Veo 3 video and Gemini image output he never used, and said "all you get is alerts" (S140). GitHub's changelog of 2026-10-07: "Budget alerts alone don't stop usage"; configure "Stop usage when budget limit is reached" (S141). Willison, 2026-10-03: soft caps "will not cut it" (S139). Depth: **teach**.
2. **A cap can move.** Isuru Fonseka set a $250 cap on a Firebase project; attacker usage met Google's Tier 3 criteria (at least $1,000 paid and 30 days as a customer), his limit rose automatically to about $100,000, and the damage came to about AUD 17,000; Google kept automatic upgrades (S140). Depth: **teach**.
3. **Free credits hide theft.** An attacker prompted an exposed METR agent app to reveal its model-provider key and used it for about three weeks: about $600,000 of credits. Nobody noticed because rate-limit errors were routine, the dashboard didn't show rate-limited requests for all users, free credits meant no bill spiked, and that key type could not take a spending limit (S046). Treat unexplained rate-limit errors as a signal. Depth: **teach** (leaked keys and rotation are C071 in keys-public-secret-and-leaked).
4. **Usage data arrives late.** Charges landed within minutes, while Google support can take up to 36 hours to see a customer's usage (S140). Depth: **one line**.
5. **Where the caps that stop live, for Claude:** Console workspace spend limits; Team and Enterprise spend limits at organisation, group or member level; the Pro and Max monthly spend limit on usage credits (without one, `Unlimited`); your cloud's budget controls; per-user limits on a Claude apps gateway (S016). Per run, `--max-budget-usd` stops at Claude Code's client-side estimate, counts subagent spend, and spend "can pass the cap", so leave headroom (S133). Depth: **teach**.
6. **Hard caps are arriving, slowly.** AWS announced project spend limits on 2026-09-16 ("your project is paused for that month"), rolling out to a limited number of customers; Google Cloud launched Spend Caps in July 2026; Willison wants hard caps by default and agents that steer builders toward capped providers, a wish, not current behaviour (S139). Check what each of your providers offers today. Depth: **brief**.
7. **What agents spin up keeps billing:** paid APIs, hosted apps, storage, compute; you can wake to find a rogue service ran up "several hundred (or several thousand) more dollars" (S139). Depth: **brief** (automation meters are C060 in agents-that-run-while-youre-away).
8. **Know your kill switch, and don't count on a refund.** The fastest stop is disabling the key or the API; both Register cases were reimbursed only after press coverage, and both feared a chargeback would get their projects suspended (S140). Depth: **brief**.
9. **A prepaid balance stops when it runs out; auto-reload removes that stop,** so pair it with per-workspace spend caps (S131, per concepts.md C061; this spec's agent could not re-read that part of S131, so re-check before teaching). Depth: **one line**.

Dropped here: "a key's power can change after you publish it" (Gemini quietly reaching existing Google Maps keys, S020) is C069-C071 in keys-public-secret-and-leaked; per-user and global caps for an AI feature strangers can run are C121 in your-apps-ai-feature.

## On the lesson page, not in the narration

Moved out of the narration by the 2026-10-12 audit (they go stale in weeks); each goes on the lesson page or on the concept's one dated "as of 2026-10-12" card:
- C055 point 7: waiting out a limit and continuing needs Claude Code v2.1.234 or later (S016, S134).
- C057 point 4: `promptCacheTtl` or `CLAUDE_CODE_PROMPT_CACHE_TTL` (v2.1.242 or later) chooses the cache lifetime (S128, S016).
- C057 point 6: the `/usage` line is `Prompt cache (main)` (v2.1.251 or later); its likely-cause field needs v2.1.260 or later (S016, S128).
- C059 point 4: Pro's default model became Opus 5.5 at v2.1.280; the setting is a top-level `effortLevel` in your user settings (S138).

## You vs the agent

As of 2026-10-12:

- **The agent does on its own (or when asked):** runs `/usage`, `/status` and `claude auth status` and explains any limit message (S016, S131, S133); tallies tokens from transcripts and runs the same task on two models or two effort levels when asked (S017); adds caching to an app and shows the write-then-read numbers (S012); puts `--max-turns` and `--max-budget-usd` on scripted runs (S133). On its own it keeps working in one growing conversation, spawns subagents and forks, answers other bots, works at whatever effort it was given, and does not feel the bill (S018, S107, S016, S017).
- **It cannot:** see claude.ai Settings > Usage, the Console bill or your other devices; turn usage credits on or off, set a spend limit or buy credits (S016); tell whether a provider's cap alerts or stops (S140, S141); notice that you are about to walk away and let the cache go cold (S128); and it will not stop because a run is getting expensive (S046, S035).
- **You must:** know which meter each tool is on, and re-check `/status` after any change to your environment; keep stray keys out of shell profiles (S131, S132); set the monthly spend limit on purpose instead of leaving it `Unlimited` (S016); decide where tasks begin and end, and clear between them (S016); pick model and effort at the start of a session and change them mid-task only for a reason (S128); decide what counts as a useful result and re-check your model choice after price changes (S017, S135); put a hard cap or a "stop usage" setting on every key before an agent or app gets it, prefer prepaid balances without auto-reload where you can, and practise the cut-off once (S141, S131, S140).
- **Bring in an expert when:** you are on Team or Enterprise (only the admin who owns Organization settings > Usage can raise limits; S016); team-wide model routing runs through an LLM gateway (its owner); keys and budgets span several cloud projects (someone who knows that cloud's identity and billing); money is already gone (the provider's billing support) (S016, S140).

## Sources this lesson is built from

Built on (credited on screen):
- S016 — Anthropic (Claude Code docs), "Manage costs effectively" (undated; content no earlier than 2026-09-14, names v2.1.271) https://code.claude.com/docs/en/costs — the two billing worlds, what `/usage` shows and doesn't, limit messages, usage credits, spend-limit locations, agent-team and subagent costs, why usage climbs in a long session.
- S017 — Aaron Orelup, "AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper. Across three long tests it was 2% cheaper." (2026-09-28) https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/ — the 97% cache-read split, the gauntlet results, and effort as a work dial. Measured before the 2026-10-07 cache price cut.
- S128 — Anthropic (Claude Code docs), "How Claude Code uses prompt caching" (undated; mentions up to v2.1.283) https://code.claude.com/docs/en/prompt-caching — exact-prefix matching, cache lifetimes, what breaks and keeps the cache, the effort exception, compaction on a warm or cold cache.
- S139 — Simon Willison, "We're going to need default hard budget caps on pretty much everything" (2026-10-03) https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/ — soft caps "will not cut it", AWS and Google Cloud hard caps, services agents spin up that keep billing.
- S140 — O'Ryan Johnson, The Register, "Google users fight for refunds as unauthorized API usage bills soar" (2026-05-13, later updated) https://www.theregister.com/ai-ml/2026/05/13/google-users-fight-for-refunds-as-unauthorized-api-usage-bills-soar/5239160 — caps that only alerted, a $250 cap raised to about $100,000, 36-hour usage visibility, refunds only after coverage.
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — the stolen key that ran about $600,000 of credits for three weeks unnoticed.

Supporting (credited on the lesson page):
- S131 — Anthropic (Claude Code docs), "Errors reference" (undated; cites up to v2.1.296, 2026-10-09) https://code.claude.com/docs/en/errors — limit messages, the stray key behind 429s, a fan-out exhausting the weekly allowance.
- S132 — Anthropic (Claude Help Center), "Using Claude Code with your Pro or Max plan" ("Updated this week" as of 2026-10-12) https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan — `ANTHROPIC_API_KEY` bills the API; limits shared with Claude; the Fable weekly limit; Max API credits don't cover Claude Code.
- S133 — Anthropic (Claude Code docs), "CLI reference" (undated live docs) https://code.claude.com/docs/en/cli-reference — `--max-budget-usd`, `--max-turns`, `claude auth status`.
- S137 — Anthropic, "Pricing" (Claude Platform docs, undated live page, read 2026-10-12) https://platform.claude.com/docs/en/about-claude/pricing — current per-token prices and cache multipliers.
- S135 — Simon Willison, "Claude Haiku 5.5" (2026-10-07) https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/ — Sonnet 5.5 cache reads halved, the Haiku 5.5 tokenizer, low vs max effort costs, new monthly API credits.
- S138 — Anthropic (Claude Code docs), "Model configuration" (undated live docs, cites up to v2.1.293) https://code.claude.com/docs/en/model-config — effort levels, defaults, when `high` and `max` earn their price, the setting that doesn't apply to Opus 5.5.
- S141 — GitHub Changelog, "Purpose-built model for leaked secret detection" (2026-10-07) https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection — "Budget alerts alone don't stop usage".
- S018 — Stijn (dotstijn), with Cursor staff replies, "~$1,500 in one week running a Grok Bot fleet: expected, or a bug?" (2026-09-22) https://forum.cursor.com/t/172705 — bots re-reading 80-90k tokens per step and waking each other.
- S107 — Rogerio Chaves (LangWatch), "The Context Tax: When to Compact" (2026-08-02) https://langwatch.ai/blog/context-tax-when-to-compact — forked subagents starting at hundreds of thousands of tokens.
- S136 — Louis-François Bouchard, "Context Engineering in 2026: Why We Stopped Compacting Our Agent's Context" (2026-08-18) https://www.louisbouchard.ai/context-engineering-2026/ — summarizing cost twice as much as keeping full history.
- S014 — Anthropic, "An update on recent Claude Code quality reports" (2026-04-23; within 12 months) https://www.anthropic.com/engineering/april-23-postmortem — the default-effort change and revert, and cache misses that drained limits.
- S012 — Anthropic, "Context windows" (Claude Platform docs, undated live page) https://platform.claude.com/docs/en/build-with-claude/context-windows — a timestamp in the cached prefix as a common mistake.
- S134 — Anthropic (Claude Code docs), "Interactive mode: Wait for a usage limit to reset" (undated; needs v2.1.234 or later) https://code.claude.com/docs/en/interactive-mode — automatic continuation after a reset.
- S003 — Mihail Eric (Stanford CS146S), lecture transcript (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — a strong model for planning, lighter ones to implement; start fresh past a few hundred thousand tokens.
- S030 — Remy, "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — orchestration at 4-8x the tokens.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — how easy it has become to spend $1,000 a day on tokens.
- S008 — OpenAI Academy, "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — cap fix-and-recheck loops.
- S080 — Stack Overflow, "Developer Survey 2026" (released 2026-10-06) https://survey.stackoverflow.co/2026/ — how often professionals switch tools for cost, and how many organisations cap spend.
- S111 — Aaron Orelup, "AO-044: Nine Claudes painted the same picture in oil, and the first tries were the art" (2026-10-11) https://aaronorelup.com/ledger/nine-claudes-one-painting/ — checking against a reference beat raw effort.
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — a model that keeps going until it "succeeds", even through a whole subscription; a 35-hour run at about $1,200.

How these were checked: S016, S017, S128, S139, S140, S046, S141, S132, S133, S135, S137, S138 and part of S131 were re-opened for this spec on 2026-10-12, and every price and version number above matches those pages on that date. S131's sections on "Credit balance is too low" and prepaid auto-reload were not reachable in the part of the page that loaded, so point 9 of C061 rests on concepts.md and is flagged. The other sources rest on the research crew's reading in concepts.md (G06, re-checked 2026-10-12). The shared web-search budget was used up, so no search for changes after 2026-10-12 was run: prices, plan windows, defaults and which providers offer hard caps must be re-checked on the day the lesson is made.

## Show it for real

- `/usage` in Claude Code on a plan: the Session block's dollar estimate beside the plan bars, the "isn't relevant for billing purposes" note from the docs boxed, `d` and `w` switching the 24-hour and 7-day views (proves the dollar figure on a plan is an estimate, not a bill). Terminal or desktop capture (S016).
- `/status` with its credential row boxed; in a second shell set `ANTHROPIC_API_KEY` to an obviously invalid placeholder and run `/status` again to show the credential change (proves a stray environment variable switches the meter). Never a real key on screen (S131, S132).
- `/usage` showing the `Prompt cache (main)` line; switch `/model` mid-session, show the confirmation prompt, send one message, and show the miss with its likely cause (proves a model switch re-reads everything) (S016, S128).
- `claude -p "hello" --output-format json` with `usage.cache_creation` boxed (proves the cache is visible in the raw numbers) (S128).
- The same small task with `--effort low` and `--effort max` and `--output-format json`, the requests, tokens and time side by side; then Aaron's Loom table from AO-026 (proves effort mostly buys more steps) (S138, S017).
- Aaron's own token split (97% cache reads) as a still from the ledger post (proves where the money goes) (S017).
- `claude -p --max-budget-usd 0.25 "..."` stopping at the cap (proves a cap that stops exists for a run) (S133).
- A throwaway cloud billing project: a budget alert that only emails next to a hard spend cap; GitHub's "Stop usage when budget limit is reached" setting; the Claude Console workspace Limits page (proves alert and stop are different settings in different places). Blur every account ID and key (S139, S141, S016).

## Questions this lesson answers

- "Why does `/usage` say I spent $40 when I pay a flat monthly price?" (cost-and-limits batch, from S016 and S017)
- "Why did Claude Code say `Credit balance is too low` when I have Max? Am I paying per token or per month?" (cost-and-limits batch)
- "Does using Claude in the browser use up my Claude Code limit? When does my limit reset?" (cost-and-limits batch)
- "I hit my limit: can I just switch to Sonnet? Is the context warning the same as a usage limit?" (cost-and-limits batch)
- "Why did a one-line question cost so much? Should I keep one chat open all day or start new ones? Do subagents cost extra?" (cost-and-limits items 4 and 9; courses-teach-now item 9)
- "What is a cache read, and why is my bill mostly cache reads? Why did my first message after lunch use so much? Is it bad to switch models mid-session?" (courses-teach-now item 10; model-context-tokens items 14-15)
- "Is Sonnet really cheaper than Opus? Which model should I use for planning and which for coding?" (cost-and-limits item 5; courses-teach-now item 11)
- "Should I always use max? Why did the same task cost 16 times more on max? What is ultrathink?" (cost-and-limits item 6; vendor-academies item 24)
- "If I set a budget cap, can I still get a huge bill? What's the difference between a budget alert and a spending limit? How do I put a dollar cap on a run? Can an AI agent run up a huge bill?" (cost-and-limits items 10 and 14; practitioners item 5)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Environment variables, where a stray key comes from (prerequisite, C126); leaked keys, restriction and rotation → keys-public-secret-and-leaked
- What fills the context window; clearing after a decision; subagents starting blind → what-the-agent-sees-each-turn
- Every enabled extension costs context → skills-mcp-hooks-and-plugins
- Slicing work, and what orchestration costs in practice → plan-first-then-build-in-slices
- Your app's AI feature as a meter strangers can run → your-apps-ai-feature
- Keeping production keys away from where the agent runs → the-narrowest-keys-and-verbs
- Schedules, loops and automations that bill while you sleep; stop rules and budgets for long runs → agents-that-run-while-youre-away
- Media billed per second, per resolution and in credits → making-media-with-ai
- Thinking tokens in depth (C029), and prompt caching for API builders in depth → backlog

## Out-of-date framings to avoid

- "The `/usage` dollar figure is my bill." Only on API or cloud billing (S016).
- "With a subscription, Claude Code can never charge me per token." An environment key or usage credits do exactly that (S132, S016).
- "Switching to a cheaper model gets me past the limit." Only for a model-family limit (S131).
- "Chat and coding have separate allowances"; "my Max API credits cover Claude Code" (S132, S016).
- "You pay for what you type and read"; "one long chat is cheaper because the model already has the context" (S016, S017, S018).
- "Cached tokens are free"; "caching saves context space" (S017, S012).
- "Changing effort always throws the cache away" (S128); "compacting always saves money" (S136, S128).
- "Half the per-token price means half the bill" (S017); and the opposite trap, "Sonnet is only 2% cheaper", which was measured at the pre-2026-10-07 price (S135, S137).
- "Max effort is the safe default"; "effort sets how hard it thinks per step"; "typing 'think hard' makes it think harder"; "my saved effort setting applies to every model" (S017, S138).
- "A budget cap stops spending"; "free credits mean no risk"; "rate-limit errors are just noise"; "my provider will refund fraud" (S140, S141, S046).
- "It's hard to spend much on AI tokens." Willison: you can now spend $1,000 in a day doing real work (S033).
- Effort as "how long the clerk works before it answers" (legacy 00.05) without the cost curve: see Legacy notes.
- Prices, plan windows, version numbers and defaults stated as permanent facts; they belong on dated cards (S016).

## Legacy notes

No legacy lesson covers this slot, but legacy 00.05 "How AI models work today" (`00-05-how-llms-work-just-enough`) has two sections that touch it, and curriculum-draft.md moves that material here when 00.05 is rebuilt: section 11 "Keeping the desk warm: caching", section 12 "The four meters", and myth six in the guest segment.

- **What it gets right:** the exact-prefix match and the order (tools, system prompt, messages); a change near the top re-lays everything below it; one hour on a subscription and five minutes on an API key; every hit resets the timer, so a long break rebuilds the desk; model switches, tool changes, dropped images and compaction break the cache, while editing CLAUDE.md doesn't and waits for the next session; a long chat costs more every turn; cached tokens are cheaper, not smaller; output costs about five times input (true today: $20 vs $4 on Opus 5.5, S137).
- **What needs updating:** "a tenth of the input price, or less" still holds, but the dated card should show today's 0.05x on Opus and Sonnet 5.5 and Sonnet's read price halving on 2026-10-07 (S137, S135); effort breaking the cache "on older models" is roughly right but should say "on most models", since the 5.5 models keep the cache only with an API key or subscription and not on Bedrock, Google Cloud or a gateway (S128); effort as "how long the clerk works before it answers" leans toward the per-step picture, when it mostly sets how many steps get taken (S017); and it doesn't say that subagents, forks and usage credits get the five-minute lifetime even on a subscription (S128, S016).
- **What is missing entirely:** which meter you are on and the stray-key switch (C055), cost as context times turns times agents with Aaron's 97% (C056), the cheaper-model trap (C058), effort's cost curve and moving defaults (C059), and caps that alert versus caps that stop (C061).
