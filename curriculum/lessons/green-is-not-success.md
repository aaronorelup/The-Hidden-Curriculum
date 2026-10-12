---
key: green-is-not-success
id: 08.02
title: Automations that fail silently
district: Running Alone
module: 08 Unattended work
status: todo
legacy: []
minutes: 10
concepts: [C100, C101, C102]
sources: [S067, S182, S180, S032, S167, S168, S169, S181, S026, S030]
lead: [S067]
---
# Automations that fail silently

**Purpose (the first spoken sentence):** In this lesson you'll learn why an automation or an agent run can show green for weeks while doing nothing, and how to check that the thing you wanted actually happened and actually arrived.

**Conclusion:** A green status only means nothing crashed, so you decide what a successful run must produce, check it in layers (did it run, is the output right, did it arrive), feed a known answer through the live pipeline, and watch from outside with a heartbeat and at the destination.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Green is not success." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 5 · Running Alone — "What runs while you're away?"; module 08 Unattended work, second lesson. 08.01 set up where unattended work runs; this lesson is how you know it worked.

**Lead source (audit, 2026-10-12):** S067 (Richard Rodrigues; 36 posts (Romeo Apps, Nathan, Adam, Cam, Michael Stables, Enzo Software)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S067, S182, S180, S032); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length note:** about 10 minutes (middle of a module). Budget: C100 about 4 min (the gap and its shapes), C101 about 3 min (the layers and the canary), C102 about 3 min (outside watchers, skipped runs, the destination).

## What to teach (binding scope)

The anchor source is one n8n community thread, "How do you catch workflows that run fine but do nothing?" (S067, 2026-08-21 to 2026-10-08). It opens: "The workflow executes. Every node is green. No errors thrown. And zero records actually landed." Credit the posters by name on screen. Everything below was re-read in the thread on 2026-10-12.

### C100 Green is not success: automations that run but do nothing

1. **A green status means only that nothing threw.** n8n's error workflow runs "if an execution fails" (S180); in the thread, nathan3: the Error Trigger "only fires on unhandled exceptions, and your problem is exactly the case where nothing throws", and "never let 'workflow finished without error' be your only success signal" (S067, 2026-08-21). So decide what a successful run produces, and make the run fail loudly when it does not: n8n's Stop and Error node exists "to force executions to fail under your chosen circumstances" (S180). *Depth: teach.*
2. **The shapes of a silent success** (each one ends green), all from the thread (S067):
   - expired credentials or tokens, renamed fields, and "filters that silently match nothing" (Zahid_Rasool, 2026-09-22; huixin, 2026-10-05);
   - an HTTP call that sent `{"":""}` while "the endpoint answers 200": "All five were broken, and all of them were green" (enzosoftware, 2026-09-04 and 2026-09-08);
   - "IF/Switch paths, continue-on-error, empty batches and disconnected nodes" (nuveko, 2026-09-24);
   - "27 branches were skipped for weeks while every run still showed green" (Loordhu_Jeyakumar, 2026-10-07);
   - zero results: "A green execution with zero results can still be an incident", and the threshold is per workflow "because zero can be legitimate in some jobs" (Reqiii, 2026-10-08).
   *Depth: teach (as recognisable shapes, not n8n steps).*
3. **A missing step is not a failed step.** A node on a branch that stopped matching is "not in runData at all", and "The execution still returns status: success" (moneywithjjcom, 2026-08-29, S067). Look for what is absent, not for red. *Depth: teach.*
4. **The alarm itself can be off.** "An error workflow with no active published version is skipped in silence" (Benzy, 2026-09-20, S067). *Depth: one line.*
5. **The same gap in agent runs.** A routine's green status "means the session started and exited without an infrastructure error. It does not mean the task in your prompt succeeded"; blocked network requests, missing connector tools and task-level failures show only in the run's transcript; you can ask `/schedule why did my nightly review do nothing this morning?` (v2.1.227 or later) (S167). In an 80-agent session "An agent died four hours in and I never noticed": "80 agents started and 79 results returned", about $22 (Aaron, S181). An agent's closing "done" is a claim: re-run in a fresh sandbox, 24 of one log's claims did not hold (S030). *Depth: teach (agent runs are the lantern beat). "Done is a claim" itself is taught in 02.04.*
6. **A repeated status word is not an alarm.** Aaron's overnight agents logged "never applied" thirteen times in a row and nothing stopped (S032). *Depth: one line; stop rules belong to 08.01.*
7. **"Never worked" is not "stopped working".** A monitor that compares each run with its own history "is blind to it by construction" for a defect present from the first run, and "a pruned run is not evidence of absence" (moneywithjjcom, 2026-09-07, S067). *Depth: brief.*
8. **"Fixed does not mean shipped"** (enzosoftware, 2026-09-06, S067): check the copy the recipient actually gets, not your fixed one. *Depth: one line.*
9. **A check that always fires is broken too.** enzosoftware's own scanner "flagged 58 of the first 83" templates and found "70 defects that do not exist" (S067, 2026-09-07). *Depth: one line; verifying the verifier is taught in 06.02.*

### C101 Check outcomes in layers: run, output and receipt

1. **Three layers** (RomeoApps, 2026-08-21, S067):
   - **Run health:** "start/end, duration, retries, upstream status".
   - **Output health:** "expected count window, freshness, required fields, schema hash, and duplicate-key checks".
   - **Receipt health:** "a downstream record ID, acknowledgement, or an explicit exception entry".
   *Depth: teach (the lesson's drawn model: three lights, only the first is the one you see by default).*
2. **An unexpected zero is a review item.** "A green run with an unexpected zero should be review, not success"; "alert on consecutive misses so one legitimate empty result does not create noise" (RomeoApps; CameronDWills makes the same point; S067). *Depth: brief.*
3. **Gate the result, not the run.** Route anything that does not match the expected conditions into a Stop and Error path (nathan3, Lopez, Matteo_LP, S067; S180). Check fields and types, not only counts: "type/field validation before data reaches Sheets, Airtable or the next API" (valerynova, 2026-09-09, S067). *Depth: brief.*
4. **Feed a known answer through the live pipeline.** "The one check that catches that is a known answer canary", and "A canary that fails to report is itself the alert" (Adam13y, 2026-08-22). One version "sends a fixed test payload through the same production webhook path every hour", which "catches expired tokens, renamed fields, and filters that silently match nothing" (huixin, 2026-10-05); another uses "a Schedule-triggered workflow" that "POSTs a fixed test payload" (Zahid_Rasool, 2026-09-22) (all S067). *Depth: teach.*
5. **For agent work, the receipt is written by the runner, not the agent:** the command, exit code, pass, fail and skip counts, and the commit hash (S030). *Depth: one line; evidence from outside the agent is taught in 06.02.*
6. **For a deploy, the receipt is the live site.** Each build of Aaron's site writes `/version.json` with the commit, the branch, the build time and the newest post, so a session can compare what is live with what it pushed (S026; the incident behind it is told in full only in from-your-laptop-to-a-url). *Depth: one line.*
7. **A person still looks.** "I still think a small human spot check on a sample is necessary there" (valerynova, S067): a believable wrong value passes every automated layer. *Depth: one line.*

### C102 Watch from outside and at the destination

1. **A watcher has to live outside what it watches.** If the trigger dies, a check inside the workflow never runs; the thread's opening post asks for "something external" (Healthchecks.io, cron pings, a heartbeat node) (rodri.galloswork, S067). Healthchecks.io "listens for HTTP requests ('pings')" and "raises an alert as soon as a ping does not arrive on time": it "works as a dead man's switch". A check goes New, Up, Late, then Down once the Grace Time ("the additional time to wait before sending an alert when a check is late") has passed; optional `/start` and `/fail` signals report start and failure (S182; undated docs, © 2015-2026, foundational and current). *Depth: teach (dead man's switch drawn: silence is the alarm).*
2. **One heartbeat table for everything.** Every workflow "upserts one row into a heartbeats table: pipeline, last_seen, last_count, last_ok"; one watcher runs "every 15 min"; alert when the silence passes that pipeline's limit; and "Make the watcher itself heartbeat somewhere external (a cron ping service is fine)" (CameronDWills, 2026-08-21, S067). The outside-in alternative: the platform's executions endpoint "gives you, per workflow, when each run started and how it ended" (Miguel_Ruilope, 2026-08-31, S067). *Depth: brief.*
3. **Schedulers skip runs quietly. Look for skipped runs, not only failed ones.**
   - Desktop scheduled tasks: "If your computer sleeps through a scheduled time, the run is skipped"; on wake, one catch-up run for the most recent miss in the last seven days, so "A task scheduled for 9am might run at 11pm"; the history shows skipped runs and why (asleep, previous run still going, other tasks running) (S168).
   - Routines: with GitHub disconnected or expired, a routine "skips runs until you reconnect, for up to 72 hours", then turns off; GitHub events beyond the hourly caps "are dropped until the window resets" (S167).
   - `/loop`: stops when the session exits, with "No catch-up for missed fires" (S169).
   *Depth: teach.*
4. **Verify at the destination.** "Make the final 'success' check prove the artifact you care about exists" (Michael_Stables, 2026-08-22, S067): the downstream record ID, the business fields, the row in the sheet, the email in the inbox. *Depth: teach.*
5. **Read what was actually sent, once, before trusting any check.** enzosoftware points each integration "at a local server that logs the request body", which "says so in about four seconds": "run it once against a logging server before trusting it at all" (S067, 2026-09-04 and 2026-09-08). *Depth: brief.*
6. **Make the live system answer for itself** (the same `/version.json` as above, so no retelling; S026). For agent fleets, read the run records on disk rather than trusting the run ended well: Aaron's transcripts "pile up ... and nobody ever looks at them" (S181). *Depth: brief.*

## You vs the agent

As of 2026-10-12:

- **The agent does, once you state the expected outcome:** builds the Stop and Error paths, count and field gates, the canary workflow, the heartbeat table and watcher, the external ping, and the logging-server test; polls an executions endpoint; reads a run's log and explains why it did nothing (S067, S180, S167). It can wire a canary, but it cannot write the answer key.
- **The agent cannot:** notice its own scheduler not firing (from inside, a dead trigger and a quiet day look the same) (S067, S168); tell you that a believable value is wrong (S067); or be trusted when it says "done" without a receipt from the runner (S030, S167).
- **You decide and check:** what a successful run produces and which fields the business depends on; the expected count window and whether zero is ever legitimate (S067); the known answer for the canary; how long each automation may stay silent and where the alert goes (S067, S182); and, at least once, you look at the destination yourself and read the first runs' transcripts or outputs (S067, S167).
- **Bring in an expert** when the business depends on the automation (billing, customer records): someone who knows the destination system says what "arrived correctly" means, and a domain expert writes or checks the known answers when correctness is a domain judgment (financial, medical, legal figures). For a system other people rely on, someone who runs production monitoring sets thresholds and alert routes, because noisy alerts get ignored (the consecutive-misses point, S067).

## Sources this lesson is built from

- S067 — Thread started by rodri.galloswork, with replies from RomeoApps, nathan3, Adam13y, CameronDWills, Michael_Stables, moneywithjjcom, enzosoftware, Benzy, Zahid_Rasool, nuveko, huixin, valerynova, Loordhu_Jeyakumar, Reqiii and others, "How do you catch workflows that run fine but do nothing?" (n8n Community, 2026-08-21, replies to 2026-10-08) https://community.n8n.io/t/308708 — the gap, its shapes, the three layers, canaries, the heartbeat table, the logging server. (sources.md lists the author as Richard Rodrigues; the post shows the handle rodri.galloswork.)
- S182 — Healthchecks.io, "Healthchecks.io documentation" (undated; © 2015-2026; foundational and current) https://healthchecks.io/docs/ — the dead man's switch, Grace Time, check states.
- S180 — n8n, "Error handling" (n8n Docs; undated) https://docs.n8n.io/flow-logic/error-handling/ — the error workflow runs only when an execution fails; Stop and Error.
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — a status word that stopped nothing.
- S167 — Anthropic, "Automate work with routines" (undated live docs; cites up to v2.1.268) https://code.claude.com/docs/en/routines — green status is not task success; skipped runs without GitHub; dropped events.
- S168 — Anthropic, "Schedule recurring tasks in Claude Code Desktop" (undated; cites Desktop 1.1.5368) https://code.claude.com/docs/en/desktop-scheduled-tasks — skipped runs, catch-up, history.
- S169 — Anthropic, "Run prompts on a schedule" (undated; cites up to v2.1.248) https://code.claude.com/docs/en/scheduled-tasks — no catch-up for missed `/loop` fires.
- S181 — Aaron Orelup, "AO-014: I had 801 agent transcripts and no way to read them" (2026-09-01) https://aaronorelup.com/ledger/reading-my-own-agents/ — the agent that died unnoticed, 80 started and 79 returned.
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09) https://aaronorelup.com/ledger/the-branch-that-went-live/ — the only alarm was looking; `/version.json`.
- S030 — Remy (redreamality.com), "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — claims that did not hold; receipts written by the runner.

## Show it for real

- A local n8n (Docker, no credentials): a two-node workflow whose IF can never match runs and shows green "Succeeded" with nothing downstream; then add a Stop and Error node on the other branch and run again to see red: proves the status measures the run, not the outcome (S067, S180).
- A terminal and a Healthchecks.io check in a throwaway account (Period and Grace Time one minute each): `curl` the ping URL, then stop pinging and watch the check go Up → Late → Down: proves silence is the alarm (S182). The ping URL works like a secret: blur it and delete the check after recording.
- A tiny local request logger (run in a throwaway folder) receiving an HTTP node's call: the raw body `{"":""}` next to what the node panel shows: proves the sender's view and the bytes sent can differ (S067, enzosoftware's method).
- A real screenshot of a Desktop scheduled task's history with a skipped run, pointer hovering to show why: proves "scheduled" is not "ran" (S168).
- A green routine run in a throwaway claude.ai account whose transcript shows a blocked request (`403`, `host_not_allowed`): proves the dot and the transcript disagree (S167).
- Terminal replay: `curl https://aaronorelup.com/version.json` next to `git log -1` in the site repo: the live site answering for itself (S026). The file is public; on 2026-10-12 it returned `commit`, `branch`, `built`, `posts` and `newest`.

## Questions this lesson answers

- My workflow says success but nothing happened. Why? How do you catch workflows that run fine but do nothing? (S067's own title)
- The API returned 200; why didn't anything happen? (S067, enzosoftware)
- Why did my routine do nothing this morning? (S167's example)
- How do I know my automation is actually working? What should I monitor? (batch-reader records from S067)
- What is a canary check? How do I test an automation that's already live? (S067)
- How do I get alerted if my automation stops running? What is a heartbeat or dead man's switch? (S067, S182)
- Why didn't my scheduled task run? (the scenario S168 documents)
- How do I see exactly what my workflow sent? (S067)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Stop and escalate rules for long runs → agents-that-run-while-youre-away
- An expired token is an account problem: whose account the automation runs as → every-automation-runs-as-someone
- "Done" is a claim → done-is-a-claim
- Evidence from something the agent can't write; verify the verifier → checking-what-you-cant-read
- Give the agent eyes on the real result → when-it-breaks-you-supply-the-eyes
- Test vs production webhook URLs, localhost, preview vs live, rollback → from-your-laptop-to-a-url
- Caps that stop spending → know-your-meter

## Out-of-date framings to avoid

- "No error alert means it worked" and "Set up an error workflow and you're covered" (S067, S180).
- "200 OK means it worked" (S067).
- "The run is green, so the agent did the task" (S167).
- "The run finished, so every agent in it finished" (S181).
- "If rows arrived, the data is fine" and "Monitoring means watching for errors" (S067).
- "I scheduled it, so it runs." It is skipped while the computer sleeps, without GitHub, or when the session closes (S168, S167, S169).
- "I fixed it, so it's fixed for everyone" (S067).

## Legacy notes

No legacy lesson covers this slot.

**Evidence notes for the writer (2026-10-12 re-read).** concepts.md C100-C102 also cite these from S067: a Set node's "Keep Only Set" wiping data, a loop ending early on one bad record, an OAuth token failing with no HTTP status, a dedupe step dropping a whole dataset, and a YouTube upload whose hashtags were never applied. None of them was found on either page of the thread re-read today (they may come from linked threads such as 307116, which were not re-opened), so they are left out of this spec; add them back only after reading where they come from. The concepts' "every key page returns 200, a video answers with 206" deploy check (S026) was not re-checked and is left out. The thread is n8n-only; the G10 notes say a search for Zapier and Make write-ups is still open, and the shared web-search budget was used up during this pass, so none was added.
