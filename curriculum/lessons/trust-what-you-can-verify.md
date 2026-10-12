---
key: trust-what-you-can-verify
id: 00.03
title: Trust what you can verify
district: Orientation
module: 00 Orientation
status: legacy
legacy: [00-06-how-to-learn-anything-technical]
minutes: [5, 6]
concepts: [C001, C002, C006]
sources: [S004, S027, S080, S085, S088, S040, S096, S029, S032, S003, S068, S007, S089, S086, S087, S074, S075]
lead: [S027, S080]
---
# Trust what you can verify

**Purpose (the first spoken sentence):** In this lesson you'll learn which work you can hand to the agent and which you have to check yourself or hand to an expert.

**Conclusion:** Let the agent write, run and fix anything a machine can check, and for what no machine can check (security, deploy readiness, fit, intent) check it yourself or bring in someone who can, because a beginner's failures look like successes.

**Where it sits on the map:** Start · Orientation — what this is, and your job; module 00 Orientation. This is the course's rule; every later lesson applies it to one district. Status `todo` since the 2026-10-12 audit: the legacy video that covered this slot pins itself on the retired six-district map, so this is the third lesson the daily job makes.

**Lead source (audit, 2026-10-12):** S027 (Andrej Karpathy); S080 (Stack Overflow (press release quotes CEO Prashanth Chandrasekar)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S004, S027, S080, S085); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length (audit, 2026-10-12):** about 5-6 minutes; COURSE.md (Aaron, 2026-10-01) gives orientation lessons and the first lesson of every module about 5 minutes. COURSE.md's 8-11 minute exception for 00.03 was written for the legacy "How old is all this?" and does not carry over to this slot. Keep at teach depth C001 points 1-5 (points 1 and 2 as one beat), C002 points 1 and 6, and C006 points 1, 4 and 7. Every other point is the cut list: C002 point 2 drops to one line; a point marked brief becomes one line; a point marked one line moves to the lesson page (C001 points 6-9; C002 points 4 and 5; C006 points 2, 3, 5, 6 and 8 as one line at most). C002 point 3 (AO-027) is a one-line callback.

## What to teach (binding scope)

### C001 The verification line: the agent handles what can be checked; you check the rest or bring in someone who can

1. **What AI masters is what can be verified.** Karpathy: "Software 2.0 easily automates what you can verify." A task can be practised when its environment is resettable (a new attempt can start), efficient (many attempts can be made) and rewardable (an automated process scores every attempt) (S027, 2025-11-17, foundational and still current). Depth: **teach** (the mechanism under the rule).
2. **The same three conditions decide whether an agent can loop on your task.** A test suite, compiler or render it can re-run is resettable, cheap and scored; "does this look right?" with no tool to look is none of the three (S027; S032). Depth: **teach**.
3. **The rule.** If a machine check exists (a test passes, a page renders, a scanner runs), let the agent run it and fix what fails; nobody debugs by hand any more, the agent reads, fixes and re-runs its own errors (S004). If none exists (security, legal, deploy readiness, fit with the team, whether it meets the real goal), check it yourself or bring in someone who can (S004; S088). Depth: **teach** (the lesson's core).
4. **Watch the questions you ask.** "Make sure it's secure" or "is it ready to deploy?" asked of the agent gets an answer you cannot check, and a true yes and a false yes look the same; that is exactly where the line falls (S004). Depth: **teach**.
5. **Professionals already set trust this way.** Stack Overflow 2026 (n = 14,304): the largest group, 48.0%, trust AI output "when I can easily verify the output"; only 6.6% trust it "for many tasks, including important work decisions" (S080). The site's own headline, "more than 87% ... had some level of trust ... up from 31%", counts verify-first trust as trust, so do not read it as "trust tripled" (S080). Depth: **teach** (one chart).
6. **Running it proves it runs.** The most common check before using AI output is "Run it locally" (76.5%, n = 13,162); "Inspect tests/security implications" is 53.0%; "Use as-is" 9.6% (S080). 36.0% do not use AI for deploying, operating or troubleshooting production and do not plan to (n = 12,547) (S080). Depth: **brief**.
7. **A behaviour check is not a quality check.** An agent opening a browser to upload a CSV and see the chart is "a check of the app's behavior" (Stanford CS146S, 2026-09-29, S003 lines 207-209); whether it is readable, fast or safe is review. Depth: **one line**.
8. **"Someone who can check" includes an independent source of truth.** In Datasette's 2026 security fixes, frontier models audited the code and then "one of us would create the automated tests highlighting the issue, then the other would implement the fix" (S089). Depth: **one line** (06.02 owns independent evidence).
9. **The line moves.** Agents testing their own work in a browser "wasn't true six months ago" (S003 line 201), and Aaron notes the AI gets better at verifying its own work every day (S088), so re-ask "what can it check now?" for each task. Depth: **brief**.
- Dropped here: the S080 figures on questions too specific to one's company (22.6%) and coworkers as the top source (71.9%), because they were not re-located on 2026-10-12; re-find them before using them anywhere.

### C002 The jagged frontier: set trust per kind of task, not per model

1. **Progress is jagged because verifiable tasks can be practised.** Verifiable tasks "progress rapidly"; tasks that are "creative, strategic, tasks that combine real-world knowledge, state, context and common sense" lag (S027). Depth: **teach**.
2. **Anthropic says it about its own model.** Claude can match skilled researchers at running a well-specified experiment, but "large performance gaps persist when it comes to Claude exercising judgement in choosing goals" (Anthropic's assessment, quoted by Osmani, S029). Depth: **teach**.
3. **One run can show both edges.** In one night of Aaron's AO-027, an agent timed a lightning bolt's shock ring to the character's grip to 1.02 seconds, while 13 scenes were marked done that never ran (S032). Depth: **one line** (a callback: the story is told in full only in when-it-breaks-you-supply-the-eyes, 02.03; audit 2026-10-12).
4. **Expensive failures sit at the joins** between a requirement and reality: Ariane 5's reused code overflowed on a trajectory its specification never included; Mars Climate Orbiter got pound-force seconds where newton-seconds were expected (S029). Depth: **one line**.
5. **Mollick:** AI is "still jagged, and can lag far behind human experts on parts of their work", which is one of his four reasons an agent should bring a human in (S068, 2026-08-31). Depth: **one line**.
6. **Calibrate on work whose answer you know.** Pick a task you do regularly, have the AI redo past examples, compare with your own, note what it gets right and wrong, and test again (S007, as summarised by the research batch; the course landing page shows only module titles, so check the wording inside the course before quoting it). Depth: **teach** (the habit).
- Dropped here: reading what a benchmark measured (S075) and right numbers hiding wrong spreadsheet structure (S074) → checking-research-numbers-and-parts; trust per product, not just per model (S074) → model-harness-and-memory.

### C006 You can't see failures you can't evaluate

1. **The perception-action gap.** A 2026 survey of 162 vibe coders (non-developers, novices, professionals): awareness of AI code's risks is widespread, but "the capacity to evaluate, debug, and verify remains experience-dependent"; vibe coding widens access without spreading the expertise to judge (S085). Depth: **teach**.
2. **Who checks.** About 45% of professionals always check code before use; non-developers are the only group that reports never checking, and they re-prompt instead of debugging more often (S085, per concepts.md C006; the abstract does not carry these figures, re-check them in the paper before showing numbers). Depth: **brief**.
3. **"Run it and ask the AI to fix it" is universal,** and only experience adds real evaluation (S085); compare S080's 76.5% "run it locally". Depth: **brief**.
4. **You cannot eyeball security.** In a controlled study of 100 developers (to appear at IEEE S&P '27), participants picked the most-secure AI suggestion 37.7% of the time and the least-secure 35.0%, with no significant difference; 88 of 400 submissions (22%) were fully secure; only 5% of participants were secure on all four tasks (S040). Depth: **teach** (the quiz below).
5. **Review took seconds, and cues misled.** About 21 seconds per suggestion; 18 of 23 interviewees judged security by visible edge-case handling, which was not a reliable sign (S040). Depth: **brief**.
6. **Experience doesn't save you.** More than 3 years of programming predicted more vulnerabilities (β = 0.2, p = 0.011) (S040). Depth: **one line**.
7. **Invisible failures.** In 26,958 annotated chat transcripts, 85.6% of minimal-fluency users' failures were invisible (they looked like success but missed the need), against 22.1% for high-fluency users; named patterns include the Confidence Trap, the Silent Mismatch and the Walkaway (S096). Caveat on screen: chats from May 2023 to July 2025 with older models (GPT-3.5-turbo to GPT-4.1-mini). Depth: **teach**.
8. **The fix is an evaluator, not "being careful".** Write the goal and a one-line acceptance check before you start and compare the result against it (S096); put anything with real users or data in front of someone competent (S088). Depth: **brief**; how to write "done when" is 02.02, how to accept "done" is 02.04, independent security tests are 04.01 and 06.02, how to bring in an expert is 04.04.

## You vs the agent

As of 2026-10-12:
- **The agent** writes, runs and fixes its own errors (S004), re-runs tests and drives a browser to check behaviour (S003), and runs AI security audits (S089). It will loop on anything resettable, cheap and scored (S027).
- **The agent cannot** score what has no automatic check: intent, taste, fit with real users and the team, security of a live app, deploy readiness (S004, S027, S029). Its "yes, it's secure" is another output, not evidence (S004).
- **You**, before handing work over, ask what check the agent can run by itself and whether that check measures what you actually want (S027); write the goal and a one-line acceptance check first (S096); calibrate trust per kind of task on work whose answer you know (S007); and own the scoring for intent, taste, real-world fit, security and deploy readiness (S004).
- **Bring in an expert** whenever you cannot check the answer yourself: the security of anything with real users or data, deploying a product, legal or other high-stakes documents. A person who cannot evaluate the code does not fix that by trying harder (S040, S085, S088). Who, what to hand them and what comes back: 04.04 before-you-ship-who-signs-off.

## Sources this lesson is built from

- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — the rule's origin: the hand-debugging lesson sent back, and "make sure it's secure" as a question you cannot check.
- S027 — Andrej Karpathy, "Verifiability" (2025-11-17; foundational and still current) https://karpathy.bearblog.dev/verifiability/ — resettable, efficient, rewardable; jagged progress.
- S080 — Stack Overflow, "Developer Survey 2026" (released 2026-10-06; fieldwork 2026-06-23 to 2026-08-05) https://survey.stackoverflow.co/2026/ — trust conditional on verification (48.0%), what developers check (76.5% run it locally), production use, the 87% vs 31% headline.
- S085 — Ahmed Fawzy, Amjed Tahir, Kelly Blincoe, "From Prompting to Verification: How Experience Shapes Vibe Coding Practices" (2026-05-23) https://arxiv.org/abs/2605.24521 — the perception-action gap.
- Supporting, credited on screen where used:
  - S088 — Aaron Orelup, prompt rejecting lesson 00.06 (Playback session 5c6d06f5, 2026-10-03; not public) — check it yourself or bring in an expert; the AI gets better at verifying its own work every day.
  - S040 — Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka, "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code" (2026-09-17; to appear at IEEE S&P '27) https://arxiv.org/abs/2609.21020 — secure picks at chance, 22% fully secure, 21 seconds, misleading cues (figures re-checked in the HTML 2026-10-12).
  - S096 — Christopher Potts, Moritz Sudhof, "A Paradox of AI Fluency" (2026-04-28; chat data 2023-05 to 2025-07) https://arxiv.org/abs/2604.25905 — invisible failures, 85.6% vs 22.1%, the named patterns (re-checked 2026-10-12).
  - S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — Anthropic's own assessment of the goal-choosing gap; the joins.
  - S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29; describes a 2026-09-17 run) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — both edges of the frontier in one night.
  - S003 — Mihail Eric, Stanford CS146S lecture transcript (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — an agent testing its own feature in a browser; "wasn't true six months ago".
  - S068 — Ethan Mollick, "Agency and Agents" (2026-08-31) https://www.oneusefulthing.org/p/agency-and-agents — AI is still jagged; when an agent should bring a human in.
  - S007 — Anthropic Academy with CodePath, "AI Fluency for Builders" (Coursera, updated September 2026) https://www.coursera.org/learn/ai-fluency-for-builders — calibrating trust on work whose answer you know.
  - S089 — Simon Willison, "Datasette 1.0a39 and 0.65.4 security releases" (2026-09-11) https://simonwillison.net/2026/Sep/11/datasette-security/ — AI audits, then one person writes the test and another the fix.
  - S086 — Michael_Alexander and replies, n8n community thread (2026-06-08) https://community.n8n.io/t/298708 — a real beginner question (below).
  - S087 — joinwell52 and replies, Cursor forum thread (2026-08-16) https://forum.cursor.com/t/168557 — a real question (below), and false "done" cases.

## Show it for real

- In a terminal, give an agent a failing test and let it loop from red to green unaided: proves anything with a cheap automatic check can be left to it (S027). Toy repo, no keys.
- Ask the same agent to make a page "feel calmer" with no screenshot tool and watch it declare done; add a screenshot step and show it start iterating on what it sees: proves it can only loop on what it can check (S027, S032).
- Ask the agent "is this secure?" about a small app with a planted missing authorisation check, get a confident yes, then run a test that fetches another user's record and fails: proves the yes was unverifiable (S004). Planted demo app only.
- The 20-second quiz: two versions of one function side by side, one missing a bounds or authorisation check; viewers pick, then the reveal with S040's 37.7% vs 35.0%: proves you cannot eyeball security.
- Give the agent a slightly ambiguous request, show it complete a plausible but different interpretation without complaint, then check the result against a one-line acceptance test written beforehand: proves a Silent Mismatch looks like success (S096).
- After one finished task, put its claims in two columns on screen: "verified by the agent" (with its test run or screenshot) and "only a person can check" (does it meet the user's need, is the data handling safe), and show who takes the right-hand column: proves the line (S080, S004).
- The Stack Overflow 2026 trust chart with 48.0% highlighted: proves professionals already trust by verifiability (S080).

## Questions this lesson answers

- "My AI Workflow Builder keeps saying it fixed my workflow but it's still not working. How can I verify whether the AI actually fixed the workflow?" (n8n community, 2026-06-08, S086)
- "Should a coding agent be allowed to mark its own task complete?" (Cursor forum, 2026-08-16, S087)
- "Can I trust it when it says the app is secure?" and "When do I need a real developer, or when should I pay an expert?" (C001 gap items; S004)
- "Why does the agent nail a tricky algorithm and then miss something obvious?" (C002; S027, S032)
- "I'm not a developer. How can I check code I can't read?" and "If I read the code, will I see the security problems?" (C006; S085, S040)
- "Why did the AI say it was done when it wasn't what I asked for?" (C006; S096)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Giving the agent eyes (tests, a browser, render tools) and checking the eyes; debugging moved to the agent → when-it-breaks-you-supply-the-eyes
- Writing the goal and a checkable "done when" → saying-what-you-want
- "Done" as a claim; polish is not evidence → done-is-a-claim
- Independent evidence, agent-written tests, AI review as triage → checking-what-you-cant-read
- Security failures in working code; spending attention by blast radius → working-is-not-secure
- Bringing in an expert: who, what you hand them, what comes back; who owns the ship decision → before-you-ship-who-signs-off
- Checking benchmarks, research, spreadsheets and parts → checking-research-numbers-and-parts
- Keeping the judgment you need to supervise → idea-to-launch-end-to-end

## Out-of-date framings to avoid

- "Debug errors by hand" or "the human's job is to find bugs by reading code" (S004): the legacy 00.06 had to be rebuilt for this.
- "If the AI says it's secure or done, it is" (S004).
- "If the model is smart enough to write it, it is smart enough to judge it"; "AI will first automate rote, easy-to-specify tasks" (S027).
- "The model is good enough now, so it is equally reliable at everything"; "if it can solve a hard coding problem, it can decide what to build" (S027, S029).
- "Developers don't trust AI" (the 2024-25 headline) and its mirror, "trust in AI tripled" (S080).
- "Being aware of AI risks is enough"; "vibe coding democratises software engineering" without the second half: access widened, the ability to judge did not (S085).
- "Trust, but verify" as a description of practice: people neither verify nor fully trust (S040).
- "An experienced developer will spot the problem"; "code that handles edge cases is careful code" (S040).
- "If the AI didn't report an error, it worked" (S096).

## Legacy notes

- **00-06-how-to-learn-anything-technical ("Trust what you can verify", 2026-10-03; covers this slot).** Made from Aaron's 2026-10-03 correction, it already teaches the rule, that agents now fix their own errors, "make sure it's secure" as the unverifiable question, and the two doors (learn to check it, or bring in someone who can); its builder-and-owner metaphor still fits. Missing: the mechanism (Karpathy's resettable, efficient, rewardable, S027), the jagged frontier and per-task calibration (C002), Stack Overflow 2026's verify-first figures (S080), and the evidence that beginners cannot see their own failures (S085, S040, S096). Out of scope now: security statistics and incidents (Veracode, Moltbook, RedAccess, Replit) → working-is-not-secure and test-it-as-a-stranger; team norms, instruction files and the dependency list → rules-it-reads-rules-it-cant-break and after-launch-keep-it-alive; deploy readiness and AI security tools → before-you-ship-who-signs-off; "the job moved" → saying-what-you-want; debugging → when-it-breaks-you-supply-the-eyes. Facts in it with no entry in sources.md (Google's "about three quarters of new code", the Irving Younger 1975 cross-examination rule, the GitClear and curl cards) must not be reused without a source.
