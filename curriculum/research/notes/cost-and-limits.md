# Research notes: what agent work actually costs, and how keys and metered automations run up bills

Agent: read-cost-and-limits. Read on 2026-10-12. Sources S016 to S020, plus two companion pages read only for detail: the Claude Code errors reference (S016 companion) and the Claude Help Center article on Pro and Max plans (S016 companion). The Register article (S020 companion) was read for the aftermath.

All five sources were fetched in full. No source was unreadable. Raw copies were pulled where the summarizer could lose detail: the Cursor thread as Discourse JSON (`/t/172705.json`, giving each poster's staff flag and timestamp), Aaron's ledger page, the Truffle post, The Register article and the Zapier article as HTML. Note: the session's shared web-search budget ran out after these fetches. One extra fact check could not be searched for, and is marked below where it matters.

## The idea that ties these sources together

What an agent costs is roughly **context length x turns x agents**, not the price per token. The scheduler behind the work also matters (routines, loops and triggers that fire on their own). Every request re-sends the whole conversation, so the biggest line on a long run is re-reading context. A cheaper model that needs more turns, a higher effort setting that takes more actions, and a bot fleet that wakes itself all multiply that line. Keys and metered automations then decide who pays and whether anything stops the bill.

---

## S016: Manage costs effectively (Claude Code)

- **Author:** Anthropic (Claude Code docs)
- **Date:** No date on the page. The newest version it cites is v2.1.271, which npm lists as released 2026-09-14, so the content dates from 2026-09-14 or later. Fetched 2026-10-12. The brief's "2026-09" is consistent with this.
- **URL:** https://code.claude.com/docs/en/costs
- **Companion pages read for detail:**
  - Claude Code errors reference, "Usage limits" section (https://code.claude.com/docs/en/errors). Undated; it cites up to v2.1.296, released 2026-10-09.
  - Claude Help Center, "Using Claude Code with your Pro or Max plan" (https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan). The page says only "Updated this week" (as of 2026-10-12).

**Summary.** There are two billing worlds. A subscription (Pro, Max, Team, Enterprise) draws from a plan allowance that resets on a rolling five-hour window and a weekly window. An API key, the Console or a cloud provider bills per token. The dollar figure in `/usage` is a local estimate at list price, and it does not matter for subscribers' billing. The page explains why usage climbs in a long session: the full conversation is re-sent on every request, cache misses after breaks, scheduled tasks, cross-session messages, goal check-ins, subagents, teammates and compaction. It lists the different limit messages and what each one means. Its rule for budgeting coding seats: "one debugging session can consume more than a day of chat."

**Gaps it gives evidence for**

1. **Two meters, not one: subscription allowance vs pay-per-token.**
   - On Pro and Max, the Session block's cost figure does not matter for billing. It is computed locally from token counts at list price. The authoritative bill is the Console usage page.
   - Teams and Enterprise seats draw from a per-seat allowance with a rolling five-hour window and a weekly window, and that allowance is shared with Claude chat and Cowork.
   - The Help Center says Pro and Max limits are shared across Claude and Claude Code. It does not name Cowork.
   - If `ANTHROPIC_API_KEY` is set in the environment, Claude Code uses that key instead of the subscription, which means API charges. The Help Center and the errors page both say so.
   - The errors page names two symptoms of a stray key: `Credit balance is too low` while on a subscription, and a 429 from a low-tier key. Fix: check the `API key` row in `/status`.
   - Max plans' included monthly API credits cannot be used in Claude Code (Help Center).
   - Enterprise averages: about $13 per developer per active day and $150-250 per month. For 90% of users it stays below $30 per active day.
2. **Rolling windows and what "limit" means.**
   - Usage counts against the session and weekly allowances at the same time. A large workflow fan-out can use up the weekly allowance before the session window resets (errors page).
   - The `/usage` breakdown (d/w toggles 24 h vs 7 days) is computed from local history only. It does not include claude.ai or other devices.
3. **The limit messages beginners confuse.** They mean different things:
   - `You've hit your session limit` and `You've hit your weekly limit` are shared across all models, so `/model` does not help. Wait for the reset, or use usage credits.
   - `You've hit your Opus limit` and `You've hit your Sonnet limit` cover one model family, so switching family works. But the next request re-reads the whole conversation with no cache hits, because each model has its own cache (errors page).
   - `You've hit your individual spend limit`, `org's monthly spend limit` and `team's shared budget` mean usage credits hit a cap that someone (you or an admin) set.
   - Lowercase `spend limit reached` comes from a self-hosted gateway's cap.
   - A context or auto-compact warning is not a usage limit at all.
   - Also: `Server is temporarily limiting requests (not your usage limit)` is a server throttle. The early warning reads `You've used 85% of your session limit`.
4. **What drives cost in an agent session.**
   - Claude Code sends the full conversation with every request, and every batch of tool results adds another request.
   - Cached history is re-read at the cache rate, so a one-line question in an all-day session pays for the whole conversation.
   - Thinking tokens are billed as output. Thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or the Fable models. Lower it with `/effort`.
   - Agent teams use about 7x the tokens of a standard session when teammates run in plan mode. Each teammate has its own context window and keeps consuming tokens until it exits.
5. **Cache lifetime and misses.**
   - The cache lifetime is an hour on a subscription. It drops to five minutes once you are drawing on usage credits, and is five minutes by default on an API key or cloud provider.
   - The first message after a longer break reprocesses the full context.
   - `/compact` is itself a large request. `/clear` costs nothing.
   - `/usage` now shows a `Prompt cache (main)` line with the hit share, misses and a likely cause. It needs v2.1.251 or later.
6. **Idle spend.**
   - Scheduled tasks and `/loop` fire while the session is idle, sending the full context each time.
   - So do messages from another of your sessions and goal check-ins. Check-ins are capped at three per goal; before v2.1.246 they were uncapped.
   - `/usage` has a Loops row listing the heaviest scheduled tasks, with per-run tokens.
7. **Context you did not type.**
   - CLAUDE.md is loaded at every session start (keep it under 200 lines). Specialised workflows belong in skills, which load on demand.
   - MCP tool definitions are deferred by default, but CLI tools (`gh`, `aws`, `gcloud`) are still more context-efficient.
   - Hooks can filter a 10,000-line log down to the error lines. Subagents keep verbose output out of the main context, but their requests still count.
8. **Seeing where usage goes.**
   - The `/usage` attribution shows the share by skill, subagent, plugin and MCP server, and flags behaviours that account for 10% or more of recent usage (long context, cache misses).
   - `--max-budget-usd` is a per-run cap that counts the session cost figure.
   - On Pro and Max with usage credits on and no spend limit set, the row reads `Unlimited`.

**Framing it says is outdated**
- The guidance shows that "a big context window is free once it's cached" is wrong: cached re-reads are the cost.
- "Switching models gets you past a limit" holds only for the model-family limits.
- The "uncapped idle check-ins" behaviour was removed in v2.1.246.
- The page records changed behaviours as notes ("Before v2.1.211 ...", "Before v2.1.222 ..."). Cost reporting itself changes month to month.

**Quotes**
- "one debugging session can consume more than a day of chat."
- "Stale context wastes tokens on every subsequent message."

---

## S017: AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper. Across three long tests it was 2% cheaper.

- **Author:** Aaron Orelup
- **Date:** 2026-09-28 (confirmed on the page: "AO-026 / Sep 28, 2026"). The post calls itself a live file that was updated as runs finished.
- **URL:** https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/

**Summary.** Aaron gave Opus 5.5 and Sonnet 5.5 three long tasks, with ten headless `claude -p` sessions per test (both models at every effort level from Low to Max). The tasks: Loom (an interpreter for an invented language), the Lockkeeper's Ledger (a canal-scheduling optimizer) and a no-rules 30-second music video. He measured the exact tokens from the transcripts with Playback Lens.

Sonnet is half price on every line except cache reads ($0.20 per million on both). On his whole history, 97% of tokens are cache reads, so repricing at Sonnet rates saves about 27%, not 50%. On Loom, Sonnet made 1.2-2.4x as many requests and cost 31% more. Over all three tests, Opus cost about $255 and Sonnet about $249, roughly 2% cheaper. Effort turned out to be a dial for how much work gets done: Max cost 16-18x Low for the same Loom score.

**Gaps it gives evidence for**

1. **The four (five) token prices, and which one dominates.**
   - Per million tokens, Sonnet 5.5 vs Opus 5.5: input $2 vs $4; output $10 vs $20; 5-minute cache writes $2.50 vs $5; 1-hour cache writes $4 vs $8; cache reads $0.20 vs $0.20.
   - Aaron's 31.6 billion tokens across 128,000 requests split like this: cache reads are 97.0% of tokens (45% of cost at Opus prices, 62% at Sonnet prices). Cache writes are 2.5% (34% / 24% of cost). Output is 0.43% (20% / 14%). Uncached input is 0.01% (about 0%).
   - An average Opus request reads about 334,000 cached tokens and writes about 1,000 output tokens. Uncached input is about 2 tokens per request, so the $2 vs $4 input line hardly affects his bill.
   - The exchange rate at Opus prices: 1 output token = 100 cache reads = 4 cache writes = 5 input tokens.
2. **A cheaper model that needs more turns re-reads more cached context.**
   - Loom: Opus $60.92, Sonnet $79.97, for identical scores.
   - Billed at Sonnet prices, Opus's own token counts would have cost $38.72. Sonnet used roughly twice the tokens.
   - Lockkeeper went the other way: Sonnet $132.00 vs Opus $151.97, 13% cheaper.
   - So the direction depends on the task. The lesson is to test on your own workload before assuming a saving.
3. **Effort is a cost multiplier because it changes how much work gets done.**
   - On Lockkeeper, Opus at Max took 9x as many actions as at Low but thought only 1.7x as long per action.
   - Loom: Max cost 16x Low on Opus and 18x on Sonnet, with the same 25/25.
   - Lockkeeper's hidden canals: both XHigh runs scored worse than both Low runs.
   - Max clearly earned its price only on open-ended creative work (the two most original videos, at $20 and $24).
4. **Long runs: context grows and cache reads take over.**
   - On the Lockkeeper Max runs, cache reads were 64% (Opus) and 72% (Sonnet) of cost.
   - 17 of the 20 Loom and Lockkeeper sessions passed 200,000 tokens of context.
   - Sonnet Max hit 968,364 tokens and auto-compacted to 19,886.
5. **Subscription vs API-equivalent dollars.**
   - The figures are API-equivalent dollars. On his Max plan the real constraint is the usage limit, but the ratios between models hold either way.
   - Sonnet Max hit the plan's usage limit 73 minutes in and was resumed after the reset.
6. **Agents do not decide when to stop or wait.**
   - Aaron stopped Sonnet Max by hand after 8 h 42 min, still tuning. Nothing inside the session would have stopped it.
   - Two headless Opus runs ended their turn while a background render ran, and nothing woke them. His launcher now resumes a session when no output file exists.
   - Ways to get more work out of a low-effort model are outside the model: explicit checklists, stop hooks, a director agent.

**Framing it says is outdated**
- "Sonnet is half the price, so it halves my bill."
- "Effort controls how hard the model thinks per step."
- "Max is the safe best setting."
- In 2025, compaction was hit constantly. With a million-token window it is now rare.

**Quotes**
- "Cache reads are the bill."
- "Effort is a work dial, not a thinking dial."

---

## S018: ~$1,500 in one week running a Grok Bot fleet: expected, or a bug?

- **Authors:** Stijn (dotstijn), CTO and co-owner of Angelo.be. Replies from Kevin Neilson (kevinn) and Zachariah.
  - Kevin Neilson is Cursor staff: the thread JSON flags him staff, admin and moderator.
  - Zachariah is **not** staff: he is a community member (staff=false).
- **Date:** Original post 2026-09-22 21:29 UTC. Kevin replied 22:42 UTC the same day, Stijn 22:53, Zachariah 2026-09-23 00:42, Stijn again 2026-09-23 09:34. Confirmed from the thread JSON.
- **URL:** https://forum.cursor.com/t/172705

**Summary.** Stijn runs a fleet of "colleague" bots and "tool" bots: a chief-of-staff bot that routes Slack mentions, plus code, design, review, docs, ops, Shopify, Klaviyo, Vercel and Supabase-migration bots. Tasks are tracked in Notion. In about one week the fleet burned roughly $1,500 in extra usage. He describes himself as a CTO "without a technical background."

Kevin found nothing anomalous. The cost comes from how the bots work: every turn re-reads that bot's whole conversation. The busiest bots re-read about 80-90k tokens per step, and about a third of all turns are bots waking other bots. Two routines run about every 8 and every 30 minutes. Fixes: a fresh chat per task, quieter handoffs, and spacing routines out. Stijn's last word: "Almost no polling." The burn was old context reused on almost every message.

**Gaps it gives evidence for**

1. **One long chat that "remembers everything" is the expensive design.**
   - A bot kept in one chat all week pays for its full history on every reply, even a one-line handoff.
   - Fix: start a fresh chat per bug or feature. Keep standing instructions in the bot's Edit Profile and task state in Notion, so a fresh chat loses very little. For the router bot: a fresh chat each morning with a short handoff summary.
   - Stijn had only just discovered the fresh-chat option, and felt it defeated the point of keeping everything in one window with one bot.
2. **Multi-agent chatter multiplies turns.**
   - Each message that wakes a bot costs a full turn on that bot's history, and its reply wakes the sender again.
   - The fix is one line in each bot's profile: message another bot only when it must act, send no acknowledgments, thanks or progress pings, and send one summary when the work is done.
3. **Scheduled routines cost a full turn each time they fire.**
   - Routines every 8 and 30 minutes should run hourly or a few times a day.
   - Zachariah (community, not staff) suggests webhooks instead of polling routines. The system that creates the task calls a webhook that wakes only the responsible bot, and the webhook can carry the message itself, which skips the list-read-search steps.
   - He also suggests a cheap, fast classification model for routing.
4. **Hitting the usage cap locks you out of fixing it.**
   - Stijn was nearly locked out and asked for a one-time reset so he could test the optimizations.
5. **Where to watch spend:** https://cursor.com/dashboard/usage (from the staff reply).

**Correction to the brief.** "Webhooks instead of polling" came from Zachariah, a community member, not from Cursor staff. Stijn then said they did almost no polling. The staff fixes are: fresh chat per task, quieter handoffs in profiles, and spacing out routines.

**Framing it says is outdated**
- "Cost depends on how much you ask" fails here. A one-line handoff paid for 80-90k tokens of history.

**Quotes**
- "Every turn re-reads that bot's whole conversation" (Kevin Neilson, Cursor staff)
- "Token burning is related to old context reused on almost every message." (Stijn)

---

## S019: Zapier Agents: unexpected activity usage

- **Author:** Zapier Help Center
- **Date:** "Updated October 01, 2026 07:59" (confirmed on the page, `datetime="2026-10-01T07:59:56Z"`)
- **URL:** https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage

**Summary.** Zapier Agents bill in "activities," and each action an agent performs is one activity. The symptom is a monthly quota draining fast, sometimes used up by one agent or a few runs.

The causes it lists:
- many steps per run
- a trigger that returns many records (each record repeats the actions)
- knowledge-source searches (one activity each)
- every web page visit and search query
- tests counting on Free plans
- processing all existing records instead of only new ones
- agent-to-Zap loops

Fixes: read the activity log, keep agents to 3-5 related actions, trigger on new or updated records only, break loops with filters, a "processed" flag or separate data sources, and rely on the built-in per-run cap (10 activities on Free, 40 on paid), after which the agent pauses and asks. The page also notes that Zapier is moving Agents to "AI by Zapier."

**Gaps it gives evidence for**

1. **Pay-per-action billing: the unit is an action, not a run or a prompt.**
   - One run can be dozens of billable actions.
   - Searches, page visits and knowledge lookups all count.
2. **Fan-out from triggers.**
   - A trigger returning 10 new leads makes the agent act on each one, so the activity count multiplies.
   - Pointing a trigger at a whole spreadsheet instead of at "new rows" reprocesses everything.
3. **Loops between an agent and an automation.**
   - An agent triggers a Zap that updates data the agent monitors, and the cycle can repeat forever.
   - Fixes: a filter that stops after one cycle, a "processed" checkbox the agent skips, separate input and output data sources.
4. **Testing is not free everywhere.** On Free plans, tests count against the monthly quota.
5. **Per-run caps exist and should be understood.**
   - 10 activities on Free and 40 on paid, then the agent pauses for input.
   - If runs hit the cap regularly, the instructions ask too much of one agent.

**Generalisation for the course.** Any pay-per-action automation works this way: Zapier, Make, n8n cloud, browser agents billed per step, API agents billed per call. The cost is actions per item x items per trigger x trigger frequency, and a loop makes it unbounded. This generalisation is the crew's inference from S019 plus S018, not a claim from Zapier.

**Framing it says is outdated**
- None explicitly.

**Quote**
- "the agent performs actions on each one, multiplying your activity count."

---

## S020: Google API Keys Weren't Secrets. But then Gemini Changed the Rules.

- **Author:** Joe Leon (Truffle Security, "The Dig")
- **Date:** 2026-02-25 (byline confirmed on the page). The page has no modified-date metadata.
- **URL:** https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules
- **Companion (aftermath):** O'Ryan Johnson, "Google users fight for refunds as unauthorized API usage bills soar," The Register.
  - Byline "wed 13 May 2026 // 00:03 UTC". The page metadata says modified 2026-06-01, when an update was added saying Google reimbursed both named sources.
  - https://www.theregister.com/ai-ml/2026/05/13/google-users-fight-for-refunds-as-unauthorized-api-usage-bills-soar/5239160
  - The Register's follow-up (https://www.theregister.com/devops/2026/05/15/google-reimburses-register-sources-who-were-victims-of-api-fraud/5241429) is linked from the update but was **not read**.

**Summary.** Google Cloud uses one key format (`AIza...`) both as a public project identifier and as a credential. For years Google told developers that Maps and Firebase keys are not secrets and can go in page HTML.

When someone enables the Generative Language (Gemini) API on a project, existing keys in that project gain Gemini access, including keys already public in JavaScript. No warning, confirmation or email is given. New keys also default to "Unrestricted."

With a scraped key, an attacker can read `/files/` and `/cachedContents/`, run up LLM charges and exhaust quotas. Truffle found 2,863 live vulnerable keys in the November 2025 Common Crawl (about 700 TiB), including one of Google's own keys that had been public since at least February 2023.

The Register's aftermath:
- Rod Danan had Maps bills under $50 a month, then was charged $10,138 within minutes, mostly for Veo 3 and Gemini image output. His caps produced only alerts.
- Isuru Fonseka set a $250 cap. Usage driven by the attacker met Google's Tier 3 criteria ($1,000 paid and 30 days), and the ceiling was raised automatically to about $100,000. The damage was about AUD 17,000.
- Support can take up to 36 hours to see a customer's usage.
- Both victims hesitated to issue chargebacks for fear of their projects being suspended. Google later reimbursed both, but kept its automatic limit increases.

**Gaps it gives evidence for**

1. **A key is a permission set, and its power can change after you publish it.**
   - A Maps key embedded in a page just as Google's docs instructed became a Gemini credential when anyone on the team enabled the Gemini API on the same project.
   - Whether a key is safe to expose depends on which APIs it can reach today, not on what it was created for.
2. **New keys default to unrestricted.**
   - An unrestricted key is valid for every enabled API in the project. The console shows a warning, but the default is wide open.
   - The Register reports that Google now requires API restrictions at creation, that a single key can no longer access both Gemini and Maps, and (per Leon) that there is a new Gemini key type prefixed "AQ."
3. **Restrictions to apply (Truffle's steps):**
   1. Check every project for the Generative Language API under APIs & Services > Enabled APIs.
   2. Audit Credentials for keys with the unrestricted warning icon or with the Generative Language API in their allowed list.
   3. Verify that none of those keys are public (client JS, public repos), starting with the oldest.
   4. Rotate any exposed key.
   5. Restrict by API service and by application (HTTP referrer, IP, Android app).
   6. Keep separate keys per environment (publishable vs secret).
   7. Scan with `trufflehog filesystem <path> --only-verified`.
   - Truffle notes that referrer allow-listing can be bypassed.
4. **Budget caps that alert rather than stop** (Register).
   - Danan's caps only sent alerts: spending continued until he shut down the API himself.
   - A cap can be raised automatically by the provider's tier system, and the abusive usage itself can qualify you for the higher tier.
5. **Delayed usage data.** Charges land in minutes, but support may need up to 36 hours to show what they were for.
6. **Refunds are not guaranteed.**
   - Google first said it found no evidence of fraud and refused.
   - Victims feared chargebacks would get their production projects suspended.
   - Reimbursement came only after press coverage (the update note).
7. **Leaked credentials are the common cause.** Google says most incidents come from keys committed to public repos and scraped. Fonseka said he never exposed his key. Not every surprise bill is the Maps-key escalation.

**Framing it says is outdated**
- "Google API keys (Maps, Firebase) are not secrets, so paste them in your HTML." This is Google's old guidance and Firebase's checklist. It is unsafe whenever the project has Gemini enabled or the key is unrestricted.
- "My budget cap will stop the spending." On Google Cloud budgets it alerted, and the tier ceiling auto-raised.

**Quotes**
- "Your public Maps key is now a Gemini credential." (Truffle)
- "all you get is alerts" (Rod Danan, in The Register)

---

## Cross-source notes for the lesson

- **One formula, three sources.** S016 says Claude Code sends the full conversation with every request. S017 measured cache reads at 97% of tokens. S018's staff reply measured 80-90k tokens re-read per step and a third of turns spent on bots waking bots. Together: cost is roughly context length x turns x agents, plus whatever fires on a schedule.
- **What the human must do (October 2026).**
  - The agent can count tokens, read `/usage`, filter logs and even write the webhook.
  - It cannot see your bill, knows nothing about your plan's caps or whether a cap is hard or alert-only, will not stop a long run on its own (S017), and will not notice that a teammate enabled Gemini on the project that holds your public Maps key (S020).
  - Those checks are the human's. When the human cannot do them (cloud key restrictions across many projects), that is the moment to bring in someone who can.
- **Demo candidates.**
  - Run `/usage` in Claude Code to show the Session block, the Prompt cache line, the plan bars and the attribution.
  - Run `/status` to show which credential is active.
  - Open the Zapier agent's Activity log.
  - Visit the Google Cloud Console's APIs & Services > Enabled APIs and the Credentials warning icons.
  - Show Aaron's Playback Lens token split.
