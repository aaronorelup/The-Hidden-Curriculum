---
key: agents-that-run-while-youre-away
id: 08.01
title: Agents that run while you're away
district: Running Alone
module: 08 Unattended work
status: todo
legacy: []
minutes: 14
concepts: [C094, C096, C105, C060, C095]
sources: [S167, S035, S019, S161, S168, S169, S069, S025, S016, S133, S173, S171, S032, S017, S018, S030, S036, S172, S170, S026, S033, S191, S190, S071, S139, S254]
lead: [S035, S167]
---
# Agents that run while you're away

**Purpose (the first spoken sentence):** In this lesson you'll learn where agents run when nobody is watching (in the cloud, on a schedule, in the background, or on a machine of their own around the clock) and the few decisions that keep them cheap, safe and stoppable.

**Conclusion:** An unattended agent acts with your access and your bill while you sleep, so you list where each one runs, keep what it does low-consequence, give every long run a stop rule and a budget that something outside the model enforces, and treat more agents as more to review, not more done.

**Where it sits on the map:** District 5 · Running Alone — "What runs while you're away?"; module 08 Unattended work, first lesson. It opens the district: 08.02 asks whether the unattended work actually happened, 08.03 whose account it ran as.

**Lead source (audit, 2026-10-12):** S035 (Armin Ronacher); S167 (Anthropic). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S167, S035, S019, S161); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Settings and versions (audit, 2026-10-12):** the spoken script teaches the vendor-neutral model. Setting names, flags and version numbers appear only on one dated "as of" card per concept and on the lesson page, never in narration (moved here: `--max-budget-usd` enforcement from v2.1.217; at most three idle goal check-ins since v2.1.246; the `/usage` Loops row from v2.1.242; S133, S016).

**Length note:** COURSE.md gives a module's first lesson about 5 minutes, but this slot carries five concepts (design-decision.md lists it among the five-concept lessons that must stay under 20 minutes). Target 14 minutes so no guest segment is needed. The 2026-10-12 audit flagged this as a breach of Aaron's length rule for module openers; the fix (move C105 always-on personal agents to its own lesson or into the-narrowest-keys-and-verbs, which brings this lesson to about 11 minutes, or retire the rule for modules 07-10) is on design-decision.md's "For Aaron to decide" list. Until he answers, keep 14. Budget: C094 about 4 min, C096 about 3.5 min, C105 about 3 min, C060 about 1.5 min, C095 about 1 min. C060 and C095 are brief segments; their deep material lives in 06.03 and the backlog.

## What to teach (binding scope)

### C094 Agents now run where you're not looking

1. **"Running without you" now comes in several kinds, and each has its own rules for where it runs, what it sees and when it fires.** Claude Code alone has three schedulers, compared in one table in its docs (S168, S169):
   - A **cloud routine** runs on Anthropic-managed infrastructure "so they keep working when your laptop is closed", fires on a schedule (minimum interval one hour), an API call or a GitHub event, and starts from a fresh clone of the repository's default branch (S167).
   - A **Desktop scheduled task** runs on your machine "only while the app is open and your computer is awake", against the working folder as it is, "including uncommitted changes" (minimum interval one minute) (S168).
   - A **`/loop`** lives inside one open session, stops when the session exits, and recurring loops "expire 7 days after creation" (S169).
   - Other vendors do the same: ChatGPT scheduled tasks "can now run when supported events occur in Gmail, Slack, or GitHub" (changelog, 2026-08-25) (S025), and Cowork "Scheduled tasks run on their own even when your computer is off" (S069).
   *Depth: teach. One drawn table: where it runs, needs the machine on?, sees local files?, asks permission?*
2. **Unattended usually means no approval prompts, and the actions are yours.** Routines have "no permission-mode picker" and run shell commands and every included connector "all without stopping for approval"; "all of your connected MCP connectors are included by default", and Claude "can use every tool from an included connector, including writes, without asking". Commits and pull requests "carry your GitHub user", and Slack messages and tickets use your linked accounts (S167). Cowork: "You remain responsible for all actions taken by Claude performed on your behalf", including scheduled tasks (S069). *Depth: teach. Hand the "as you" part to 08.03.*
3. **Or it stalls instead.** A Desktop task in Manual mode that needs a tool it lacks "stalls until you approve it". The docs' fix is to click Run now and choose "always allow" for each prompt, so future runs auto-approve the same tools; those approvals can be reviewed and revoked on the task's page (S168). Name the trade: a one-time yes becomes a standing one. *Depth: brief.*
4. **Keep the scheduled work itself low-consequence.** Anthropic's Cowork safety page: "Begin with low-risk tasks like generating summaries or compiling information"; "Don't schedule tasks that access sensitive files, send messages on your behalf, make purchases, or take other actions that are difficult to undo"; "Check the results of scheduled tasks regularly"; pause or delete tasks you no longer need. Its reason: "Because you can't monitor these tasks in real time, take extra care", and if Claude reads malicious content mid-task "it could act on those instructions" (S069). *Depth: teach. Injection itself belongs to 07.01.*
5. **Scope each unattended agent to what it needs.** Remove connectors it doesn't use; set the environment's network access (the Default environment allows only an allowlist, and blocked requests fail with `403` `host_not_allowed`); store API keys as network secrets, not environment variables, which are "visible to anyone who uses the environment"; and know that branch protection only blocks a routine's push if the GitHub access you connected cannot bypass it (S167). *Depth: teach (as a short checklist on screen, not steps).*
6. **A trigger anyone can pull.** An API-triggered routine has a bearer token "shown once"; anyone holding it can send text, which arrives wrapped as untrusted data that the routine acts on only if its saved prompt says to (S167). Store the token like a password. *Depth: one line.*
7. **Keep an inventory, and know where each kind is listed:** claude.ai/code/routines or `/schedule list`; the Desktop Routines page, with each local task's prompt on disk at `~/.claude/scheduled-tasks/<name>/SKILL.md`; asking Claude "what scheduled tasks do I have?" for `/loop` tasks; Cowork's "Scheduled" page (S167, S168, S169, S069). Routines "belong to your individual claude.ai account. They are not shared with teammates" (S167): nobody else will find them for you. *Depth: teach.*
8. **A task can change itself.** A Desktop scheduled task can rewrite its own schedule or prompt from inside a run with `update_scheduled_task` (S168). Look at the task as it is now, not as you set it up. *Depth: one line.*
9. **Several agents on one machine are a system.** Three sessions on Aaron's PC could not see each other's work; one blamed itself for a deletion another session made, and the false claim was filed in his notes as "a hard rule"; his first question now is "what else was running?" (S170). Each session also starts its own copies of its MCP servers: with 10 sessions open on 2026-09-24, one server ran 11 copies using about 6 GB of memory, next to 20 `npx` wrapper processes, and Aaron asked what the Node.js processes filling his memory were, not knowing a session could be closed (S254). So close the sessions you're done with, and before blaming one agent, ask what else was running (S170). One line, no retelling: a cloud session starts from a fresh clone of the default branch, so it never saw his laptop's uncommitted rules (S026; the full story is told in from-your-laptop-to-a-url). *Depth: brief (one story, S170).*
10. **Autonomy does not mean it asks when unsure.** In Aaron's 4 h 21 min autonomous run Claude "wasn't asked a single question", made "eight calls I'd normally be asked about", and when X hit a login wall it used his Chrome "where I'm already signed in" (S171). *Depth: brief (story, third person).*

### C096 Long runs need stop rules, budgets and checkpoints

1. **Longer is not more done.** Armin Ronacher's weekend run: "35 hours later, the factory has delivered absolutely nothing of value"; about 1B tokens, around 1,200 USD in raw API cost, a net 75k lines and 79 commits ("around 15.5 USD per commit"); its own task names drifted from "1, 2, 3, 5, 5a" to "8b2c2b2b checkpoint1". Shorter runs left "a maybe imperfect but still digestible piece of software" (S035, 2026-09-07). *Depth: teach (the lesson's anchor case, credited on screen).*
2. **Newer models keep going.** "It will keep going, and earlier models did not do that"; it "will continue until it succeeds, even if it burns through an entire subscription" (S035). So persistence is a reason for more limits, not fewer. *Depth: teach.*
3. **Size the work so it ends in something checkable**, and check in on the way: Shopify's rebuild ran through "agent-gated, screen-sized checkpoints" (S036). *Depth: brief.*
4. **Write the stop and escalate conditions into the plan, not only the success steps.** Aaron's overnight wallpaper agents ran 8.5 hours ($373 at list prices); their notes said "never applied" thirteen times in a row, and "the plan had no step where anyone had to stop because of it" (S032; one line, the story is told in full in when-it-breaks-you-supply-the-eyes). A status word in a log is not an alarm unless the plan says what happens when it appears. *Depth: teach* (the stop rule, not the story).
5. **Set the limits before it starts, and have something outside the model enforce them** (S133, S016, S019):
   - `--max-turns`: "No limit by default" (print mode).
   - `--max-budget-usd`: stops at a client-side estimate; "Spend can pass the cap, so leave headroom"; subagent spend counts (the version that enforces it is on the lesson page).
   - A plan with no spend limit shows `Unlimited` in `/usage`.
   - Some platforms cap each run: a Zapier agent run pauses "and asks for your input" after 10 activities on Free, 40 on paid.
   *Depth: teach (recognise the names; no flag tutorial). Caps that alert vs caps that stop are taught in 06.03.*
6. **A goal loop stops only when its evaluator says so.** `/goal` keeps starting turns until a small fast model judges the condition met or impossible; that evaluator "doesn't run commands or read files", so write one measurable end state with a stated check and a clause such as "or stop after 20 turns" (S173). *Depth: brief.*
7. **Rules about time need a clock.** In Aaron's autonomous run a 30-minute check-in rule was broken three times (gaps of 43, 68 and 47 minutes), because the lead session runs "only when something wakes it"; his conclusion: the rule "needs a timer, not a promise" (S171). The harness's own guards are caps, not judgment: Claude Code "ignores the ninth consecutive stop-block after eight continuations" and "Cursor defaults to five auto follow-ups" (S030); `/goal` stops after several turns with no tool use (S173); recurring `/loop` tasks expire after 7 days (S169). *Depth: teach.*
8. **The opposite failure: waiting forever.** Two of Aaron's headless runs started a render and said they'd resume when it finished, but "in a headless run that's the end of the session", and nothing woke them; his launcher now treats "no video in the folder" as not finished and resumes (S017). A Manual-mode Desktop task stalls on a prompt (S168); a goal pauses on a usage limit (S173). *Depth: brief.*
9. **Keep a rejected column and look at intermediate results.** "The rejected column is the useful part" (S032); without watching, Ronacher says you are left with the diff viewer of the final artifacts (S035). *Depth: one line.*

### C105 Personal always-on agents are coding agents holding your keys

1. **What a "Claw" is.** Simon Willison: "A Claw is really just a coding agent wearing a less threatening hat"; they are "being rebranded as 'personal agents' or 'general agents'"; non-technical people queued at OpenClaw install parties, Bay Area Apple stores "sold out of Mac Minis"; Meta's Muse topped the free iPhone chart, and he is "not yet convinced you can't shoot yourself in the foot with Muse" (S033, 2026-09-27). *Depth: teach.*
2. **The machine becomes a credential vault.** OpenClaw's own docs: "Assume anything under ~/.openclaw/ ... may contain secrets or private data": gateway tokens in the config, channel credentials, MCP OAuth access and refresh tokens, model auth, and session transcripts that "can contain private messages and tool output", readable by anything with disk access. Hardening: `700`/`600` permissions, full-disk encryption, a dedicated OS user (S191). *Depth: teach.*
3. **What thieves took.** 341 malicious ClawHub skills (reported 2026-02-02) stole "exchange API keys, wallet private keys, SSH credentials, and browser passwords"; one sent the bot's `~/.clawdbot/.env` to webhook.site (S071). By 2026-02-28 the count was 1,184, about 20% of the registry (S161). *Depth: brief. Older than three months; it is the primary incident record. Skill marketplaces are taught in 05.03 and 07.04.*
4. **Exposure: teach the history and today's default.** In January public instances grew "from approximately 1,000 to over 21,000" in a week; one researcher found 42,665 exposed, 5,194 verified actively vulnerable, 93.4% with authentication-bypass conditions; the web interface then shipped on port 8080 "with authentication disabled" (S161, 2026-05-07). Today a host install "binds to loopback", but "container images default to an exposed bind", so pair them with auth; `openclaw security audit` reports drift from the defaults (S191, undated live docs). *Depth: teach.*
5. **Local is not the same as private.** A zero-click flaw (2026-03-01): loading a malicious web page was enough; the page guessed the gateway password without rate limiting and registered itself as a trusted device; fixed "within 24 hours". Advice: "Don't browse the open web in the same browser where you're logged into OpenClaw's control panel" (S190). *Depth: brief.*
6. **One gateway is one trust boundary.** The docs assume one operator or a team that trusts each other; agents with message-tool access can send "across conversations and channel providers by default"; people who don't fully trust each other need a "separate gateway + credentials, ideally separate OS users or hosts" (S191). *Depth: brief.*
7. **There may be no remote off switch.** A Meta AI security researcher asked her agent to suggest what to delete; it started deleting, ignored stop messages from her phone, and "I had to RUN to my Mac mini like I was defusing a bomb" (S190). Plan a local shutdown, and word delegation precisely ("suggest" vs "delete"). *Depth: teach (the story the viewer will remember).*
8. **You are its security team.** "There's no automatic update" (S190). After a suspected compromise, the docs' four steps: contain (stop the gateway, bind to loopback), rotate (gateway auth and every provider, bot and model key), audit (logs, transcripts, recent config changes, `openclaw security audit --deep`), collect evidence (S191). Never give it "your primary email, admin accounts, or crypto wallets"; use a "Dedicated VM, dedicated credentials"; "Treat any OpenClaw instance with access to corporate credentials as a critical-risk asset" (S161). *Depth: teach.*
9. **It can spend while you sleep.** Coding and personal agents make it easy to start services that cost money; waking to find a runaway service used "several hundred (or several thousand) more dollars" is the outcome to prevent, and soft caps "will not cut it" (S139). *Depth: one line; caps are 06.03.*

### C060 Automations bill per action and per wake-up

1. **A wake-up is a full turn.** A scheduled task "fires on its interval even while the session is idle, sending your full context each time"; so do messages from another of your sessions and goal check-ins (now capped at three idle check-ins per goal; before, uncapped). `/usage` has a Loops row showing how often each scheduled task fires, how many times it ran and its tokens per run (S016). *Depth: brief.*
2. **Interval arithmetic.** A Cursor bot fleet "burned roughly $1,500 in extra usage" in a week; "Every turn re-reads that bot's whole conversation", about 80-90k tokens per step for the busiest bots, roughly a third of turns were bots waking bots, and two routines ran about every 8 and 30 minutes; staff: "Hourly or a few times a day will help to save money". The owner later said the main driver was "old context reused on almost every message" (S018, 2026-09-22). Every 8 minutes is 180 runs a day (crew arithmetic). *Depth: brief.*
3. **Per-action meters multiply.** Zapier Agents: one activity per action; a trigger returning 10 records repeats the actions 10 times; each knowledge search, page visit and search query counts; tests count on Free plans; point triggers at new or updated records, not all existing ones; keep agents to "3-5 related actions" (S019, updated 2026-10-01). *Depth: brief.*
4. **Loops are unbounded.** "If an agent triggers a Zap that updates data the agent monitors, you can create an infinite loop"; fixes: a filter that stops after one cycle, a "processed" field, separate data sources for input and output (S019). *Depth: brief.*
5. **Routines draw on the same subscription usage as your interactive sessions**, with hourly run caps (for example 100 scheduled runs per hour per account); with usage credits on they can continue on metered overage (S167). *Depth: one line.*

### C095 More agents is not more done

1. **"Parallelize last."** Only after one stream has "a dependable judge, recovery path, and review format people can absorb"; "Parallelism multiplies the bottleneck you already have"; one senior reading every line ends in "ceremonial approval" (Addy Osmani, S036, 2026-09-14). *Depth: brief.*
2. **Passes alone, fails together.** Two parallel agents interfered "in 105/108 blind runs (97%) with clean textual merges"; a roughly 130-token message about the change that landed cut mean interference from 2.50 to 0.04; going from one to four local workers on one machine "produced no net throughput gain" (S030, 2026-10-11). *Depth: brief.*
3. **More agents cost more.** "Running several sessions or subagents at once multiplies token usage" (S172); agent teams use "approximately 7x more tokens" when teammates run in plan mode (S016). *Depth: one line.*
4. **Your review time sets the safe number**, spent first on "the largest blast radius and weakest oracle" (S036). Worktrees "isolate changes, not behavior" (S036), and agent teams don't isolate teammates in worktrees, so partition the files (S172). *Depth: one line. Fleets in depth stay in the backlog ("Parallel agents, worktrees and fleets").*

## You vs the agent

As of 2026-10-12:

- **The agent does on its own:** once triggered it runs the whole task without asking, picks its own interval in a self-paced `/loop` (S169), makes judgment calls it would otherwise ask about (eight in S171), can rewrite its own schedule (S168), keeps going past the point of value (S035), and reports progress rather than budget (S017). An always-on agent runs whatever code its access allows (S033, S191). It does not notice that it has gone off the rails, that its port is open, or that its inputs were poisoned (S035, S161, S069).
- **The agent can do when asked, and verifiably:** list your routines and scheduled tasks (S167, S169), read a run's log and explain it (S167), set `--max-turns`, `--max-budget-usd` and a measurable `/goal` with a turn clause (S133, S173), run `openclaw security audit` and fix permissions it reports (S191), and test once whether a workflow re-triggers itself (S019).
- **You decide and check:** which work may run unattended at all (low-consequence first, S069); its repositories, connectors, network access and secrets (S167); the stop and escalate rules, the budget and a real timer for any time rule, before launch (S032, S171, S133); which machine an always-on agent lives on and which scoped, revocable keys it holds (S161, S191); the inventory of everything running, reading each run's output, and turning off what you no longer need (S069, S167); whether to fan out at all (S036).
- **Bring in an expert** before an unattended or always-on agent gets connectors to production systems, money, company credentials or other people's data: your organisation's admin (on Team and Enterprise an Owner can turn routines off for everyone, S167) or a security professional, treating the agent "as a critical-risk asset" with least privilege (S161). When you cannot write a measurable end state for a long run, neither you nor a goal evaluator can tell done from drifting (S173, S035): get someone who knows the domain to define done first.

## Sources this lesson is built from

Primary (from curriculum.md):
- S167 — Anthropic, "Automate work with routines" (Claude Code docs; undated live docs citing up to v2.1.268 and a 2026-04-01 beta header; re-read 2026-10-12) https://code.claude.com/docs/en/routines — what a routine is, no permission picker, connectors included by default, actions appear as you, scoping, API trigger, inventory, usage limits.
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — the 35-hour run, its cost and drift, "keep going".
- S019 — Zapier Help Center, "Zapier Agents: unexpected activity usage" (updated 2026-10-01) https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage — per-action billing, multiplying triggers, loops, per-run caps.
- S161 — Hive Security, "OpenClaw: How the Viral AI Agent Became 2026's First Major Security Crisis" (2026-05-07) https://hivesecurity.gitlab.io/blog/openclaw-ai-agent-security-crisis-2026/ — exposure figures, early defaults, isolation and least-privilege advice. Medium-credibility compilation; numbers credited as reported.

Supporting:
- S168 — Anthropic, "Schedule recurring tasks in Claude Code Desktop" (undated; cites Desktop 1.1.5368) https://code.claude.com/docs/en/desktop-scheduled-tasks — the scheduler comparison table, stalls, always-allow, self-rescheduling, where prompts live.
- S169 — Anthropic, "Run prompts on a schedule" (undated; cites up to v2.1.248) https://code.claude.com/docs/en/scheduled-tasks — `/loop`, 7-day expiry, listing tasks.
- S069 — Anthropic Help Center, "Use Claude Cowork safely" (last modified 2026-10-06; page reads "Updated this week" on 2026-10-12) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — what to schedule and what not to, responsibility, injection risk.
- S025 — OpenAI, "ChatGPT & Codex changelog" (latest entry 2026-10-08) https://learn.chatgpt.com/docs/changelog — event-triggered scheduled tasks (2026-08-25).
- S016 — Anthropic, "Manage costs effectively" (undated; no earlier than 2026-09-14) https://code.claude.com/docs/en/costs — idle wake-ups, Loops row, `Unlimited`, agent-team token multiple.
- S133 — Anthropic, "CLI reference" (undated; cites up to v2.1.290) https://code.claude.com/docs/en/cli-reference — `--max-turns`, `--max-budget-usd`.
- S173 — Anthropic, "Keep Claude working toward a goal" (undated; cites up to v2.1.269) https://code.claude.com/docs/en/goal — the evaluator and how to bound a goal.
- S171 — Aaron Orelup, "AO-032: I told Claude to find the best Opus 5.5 trick on X and do it without me" (2026-10-03) https://aaronorelup.com/ledger/opus-55-on-x-alone/ — no questions asked, signed-in browser, "a timer, not a promise".
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — "never applied" thirteen times, no stop step.
- S017 — Aaron Orelup, "AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper..." (2026-09-28) https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/ — the run stopped by hand, headless runs nobody woke.
- S018 — Stijn (dotstijn), replies by Kevin Neilson (Cursor staff) and Zachariah, "~$1,500 in one week running a Grok Bot fleet: expected, or a bug?" (2026-09-22) https://forum.cursor.com/t/172705 — interval arithmetic and bots waking bots.
- S030 — Remy (redreamality.com), "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — parallel interference, harness stop caps.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — parallelize last, checkpoints.
- S172 — Anthropic, "Run agents in parallel" (undated live docs) https://code.claude.com/docs/en/agents — token multiplication, agent teams share files.
- S170 — Aaron Orelup, "AO-019: An agent confessed to deleting 19 GB I had asked another agent to delete" (2026-09-26) https://aaronorelup.com/ledger/the-confession-that-spread/ — sessions that can't see each other.
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09) https://aaronorelup.com/ledger/the-branch-that-went-live/ — the fresh clone that never saw local rules.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — what a Claw is, adoption, Muse.
- S191 — OpenClaw project, "Gateway Security; Secrets, storage, and logs; Operator incident response" (undated live docs) https://docs.openclaw.ai/gateway/security — current defaults, what is stored, the four incident steps.
- S190 — Sliq, "Every OpenClaw Security Incident So Far (2025-2026)" (undated; covers incidents to 2026-03-01) https://getsliq.com/blog/openclaw-security-incidents-timeline — the inbox deletion, the zero-click flaw, no automatic updates.
- S071 — Ravie Lakshmanan (The Hacker News), "Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users" (2026-02-02; older than three months, still the primary incident record) https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html — what the skills stole.
- S139 — Simon Willison, "We're going to need default hard budget caps on pretty much everything" (2026-10-03) https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/ — services that keep billing; soft caps.

Added by the 2026-10-12 audit (credit on the lesson page):
- S254 — Aaron Orelup, typed prompts in his recorded Claude Code history, with the process count the agent measured (2026-09-24 to 2026-10-08; Playback, not public) — each session starts its own MCP servers; closing sessions (C094 point 9). Re-read 2026-10-12.

## Show it for real

- Browser capture of the public docs table "Compare scheduling options" (code.claude.com/docs/en/desktop-scheduled-tasks): proves the three schedulers differ in where they run, whether the machine must be on and whether they ask permission (S168).
- Screenshot, animated with a pointer, of claude.ai/code/routines "New routine" in a throwaway account: the Connectors list with everything included by default and no permission-mode picker; then Run now and the run session (S167). Blur the account email.
- Desktop app, Routines → New routine → Local, then open `~/.claude/scheduled-tasks/<name>/SKILL.md` in an editor: proves a scheduled task is a prompt in a file on your disk (S168).
- Terminal replay in a throwaway folder: `claude -p --max-turns 3 --max-budget-usd 0.50 "<a task too big for 3 turns>"` exiting at the limit: proves a cap outside the model ends the run (S133). Costs cents; no keys on screen.
- `/loop 5m say the time` left to fire a few times, then `/usage` and the Loops row with tokens per run: proves an idle schedule spends (S016). Cancel it afterwards.
- `/goal all tests in test/auth pass, or stop after 20 turns`, then `/goal` status showing turns, token spend and the evaluator's reason (S173).
- Quote card of Ronacher's numbers over a screenshot of his public post (35 hours, about 1B tokens, about $1,200, 79 commits): the anchor case, credited (S035).
- Only in a disposable VM with no real credentials: `openclaw security audit`, and a listing of `~/.openclaw/` pointing at `credentials/`, the SQLite state and `sessions/` transcripts (S191). Never on Aaron's own machine.
- Browser capture of the public Zapier help article's activity-counting section and the agent-Zap loop paragraph (S019).

## Questions this lesson answers

- Can Claude work while I sleep? What is a background agent? (batch-reader records listed under C094 in concepts.md; S025, S069)
- Can I have Claude send my weekly emails automatically? (C094; S069 says start with summaries, not messages sent as you)
- How do I check what my scheduled agent did? (C094; S167, S168)
- Is it safe to leave an always-on agent running? Why do people run their AI agent on a separate Mac mini? Where does my agent keep its API keys? (C105; S033, S191, S161)
- Can I just let the agent run overnight? How do I put a dollar cap on a run? Why did my agent stop halfway? (C096; batch-reader records from S035, S017, S032, S019)
- Why is my usage going up when I'm not using it? How often should a scheduled agent run? Why did my Zapier agent use my whole month in a day? (C060; S016, S018, S019)
- Should I run multiple agents at once? How many agents can I manage? (C095; S030, S036)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Runs that finish green but did nothing; skipped runs; heartbeats → green-is-not-success
- "Appears as you": whose account an automation runs as → every-automation-runs-as-someone
- Prompt injection in what a scheduled agent reads → whose-words-is-it-reading
- Running an always-on agent in a VM or container with no production keys → contain-it-dont-babysit-it
- Narrow keys and keeping money, messages to outsiders and publishing behind a human → the-narrowest-keys-and-verbs
- Malicious skills and marketplaces → skills-mcp-hooks-and-plugins, other-peoples-code
- Caps that alert vs caps that stop; which meter you are on → know-your-meter
- Rotating a leaked key → keys-public-secret-and-leaked
- A cloud session sees only committed files on the default branch; preview vs production → from-your-laptop-to-a-url
- "Done" is a claim → done-is-a-claim
- Parallel fleets, reviewer chains, swarms → backlog ("Parallel agents, worktrees and fleets")

## Out-of-date framings to avoid

- "An agent only acts while I'm chatting with it." Routines and Cowork tasks run with the computer off; ChatGPT tasks fire on Gmail, Slack and GitHub events (S167, S069, S025).
- "Automations are safe once they work the first time." Check results regularly (S069).
- "Autonomy means the agent asks when unsure." It asked nothing in 4 h 21 min (S171).
- "Each agent is independent." (S170)
- "The longer the agent runs on its own, the more it gets done", and "a newer, more persistent model needs less supervision" (S035).
- "The agent will stop when it is finished" and "it will warn me before it spends too much" (S017, S016).
- "Tell it to check in every 30 minutes." It needs a timer (S171).
- "Logging the problem is enough" (S032).
- "An idle session costs nothing" and "polling every few minutes is harmless" (S016, S018).
- "More agents means more done" and "no merge conflict means the merge is safe" (S036, S030).
- "It's my own machine at home, so it's private and safe" (S071, S161, S190).
- "Running it in Docker isolates it from the internet." Container images default to an exposed bind (S191).
- "OpenClaw ships with auth disabled." True in January (S161), no longer true for host installs (S191): teach both.
- "If it goes wrong I'll tell it to stop." (S190)

## Legacy notes

No legacy lesson covers this slot. Legacy 00.05 (00-05-how-llms-work-just-enough, section 17 "a desk that never closes") introduces personal agents (OpenClaw, Hermes Agent, Muse, OpenAI dots, Gemini Spark) and Anthropic's cloud sessions, routines and Dispatch in about a minute, and the curriculum's legacy table moves that material here when 00.05 is rebuilt. What it gets right: a personal agent runs all the time on its own computer, "your machine, your keys, your risk". What is missing: the schedulers' different rules, no-prompt runs acting as you, stop rules and budgets, and the current OpenClaw defaults. One figure to replace: 00.05 says "more than a hundred thousand installs left open to the internet" in February; no source read for this spec supports that number, and S161 reports 42,665 exposed (5,194 verified actively vulnerable). Its Hermes, dots and Gemini Spark mentions have no source in sources.md and are not part of this spec.

**Evidence notes for the writer (2026-10-12 re-read).** Two points in concepts.md C105 were not found on the S191 pages re-read today and are left out: "anyone allowed to message the bot can make it call its tools" and "never sign a shared agent into personal Apple or Google accounts or password managers". concepts.md's C094 mention of Cursor Projects and Cursor remote control cites S025, which is OpenAI's changelog and does not contain them; they are left out. The shared web-search budget was used up during this pass, so no newer sources were searched for; every source above was re-fetched and read on 2026-10-12.
