---
key: done-is-a-claim
id: 02.04
title: When the agent says 'done'
district: First Build
module: 02 Your first build
status: todo
legacy: []
minutes: 12
concepts: [C004, C005, C011, C016]
sources: [S030, S064, S032, S092, S093, S008, S098, S095, S087, S099, S086, S026, S042, S117, S033, S035, S080, S085, S096, S007, S011, S039, S065, S004, S009, S010, S029, S094, S003, S252]
lead: [S030, S252]
---
# When the agent says 'done'

**Purpose (the first spoken sentence):** In this lesson you'll learn why an agent's "done, all tests pass" is a claim you check, not proof, and how to accept its work on evidence instead.

**Conclusion:** An agent's "done" is the start of acceptance, not the end: it shapes its work to pass the checks it believes exist, and polish costs it nothing, so ask for the evidence, insist on one check against the real thing, and judge for yourself, or with users and experts, whether it is good and not just running.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Done is a claim." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; 02 Your first build. Lesson 10 of the path and the last lesson of module 02, so about 10 minutes by the course rule. It is set to 12 because it carries four must-priority concepts. Lantern lesson. It is the plainest form of the course rule: the agent handles what can be verified, and you check what it cannot.

**Lead source (audit, 2026-10-12):** S030 (Remy (redreamality.com)); S252 (Aaron Orelup). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S030, S064, S252, S092, S093); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Teaching order: the claim (C011, points 1-4), why agents produce false or hollow "done" (C004), why it sounds convincing anyway (C005), how to accept on evidence (C011, points 5-9), and the three different questions: does it run, does it do what I meant, is it good (C016). The main story is Aaron's BLACKWATER 2 (S252, C004 point 6), told once and called back in C016 point 6; AO-027 and AO-043 appear only as one-line callbacks (they are told in full in when-it-breaks-you-supply-the-eyes and from-your-laptop-to-a-url). The metaphor candidate: a delivery driver's "delivered" message. It is usually true. Sometimes the parcel is at the wrong door, and sometimes it was never loaded. You accept on the photo of the parcel at your door, and only you can say whether it's what you ordered.

### C011 'Done' is a claim, not evidence

1. **The closing summary is a claim.** It reads as confident and specific, and the chat shows it as if it were the result. Before accepting, ask: where is the evidence, and what produced it? (S030, S008) **Depth: teach.**
2. **One team's real record.** nomArmy logged 547 jobs on one machine over 16 days, 2026-09-18 to 10-04 (S030, re-opened 2026-10-12; S098):
   - Workers said "done, tests pass" 265 times.
   - 24 of those claims didn't hold, about 1 in 11.
   - 16 failed when re-run in a fresh environment.
   - 8 had tests that still passed with the change reverted.
   - 5 more could not be checked at all.

   **Depth: teach.** This is the lesson's key number.
3. **The rate varies, so learn the habit, not the number.** In Advani's benchmark study, false success ranged by model from 13% to 79% of failures on one benchmark, and a thinking model did not protect against it (S095, via S030). **Depth: brief.**
4. **Most false "done" is sincere.** The agents "sincerely believe they finished". In the stale case "there is no intent to lie" (S030). Stale results, and a sub-agent's failure that never reaches the main conversation, produce honest-sounding wrong summaries (S030). **Depth: brief.** It makes the habit feel fair, not accusatory.
5. **The seven shapes of a false "done", each with its cheapest check** (S030):

   | Shape | Cheapest check |
   |---|---|
   | 1. Never ran, or ran only a slice ("all tests pass" after unit tests only) | a receipt that names the command and its scope |
   | 2. Stale: it edited again after the green run | tie the receipt to the commit |
   | 3. Ran right, narrated wrong (a sub-agent's failure was dropped) | a record written by the test runner, not the agent |
   | 4. Tests pass but prove nothing | revert the change and re-run |
   | 5. Shared misunderstanding (the refund case from 02.02) | a human owns the acceptance criteria and test names |
   | 6. Each change passes alone, the combination fails | run the full suite on the merged code |
   | 7. Only the real environment shows it | a clean environment, a live call, or a side-by-side comparison with the old version |

   **Depth: teach** shapes 1, 4 and 7. Give the rest one line each, as a table on screen.
6. **Shape 7, for real.** A Go client sent a request field (`max_tokens`) that newer models reject with HTTP 400, so every extraction failed silently while the mocked tests stayed green. Separately, a module missing from a deployment bundle passed every unit test (S030). Mocks encode the agent's assumptions about the outside world, so make at least one real call or one clean build. **Depth: brief.**
7. **Three questions before you accept** (S008, slide 26, re-read 2026-10-12):
   - Does the diff match the requested scope?
   - What ran, and what passed, failed or was skipped?
   - What is still unverified, and what happens next?

   Then accept when the evidence meets the goal; otherwise ask for a specific fix, or stop (S008). GitHub's exercise has the learner write a "Verification" section listing the commands run and what each proved (S009, step 5). **Depth: teach.** This is the lesson's main habit.
8. **Read back the real state after any write:** the remote branch, the tracker, the live version (S087). In the Cursor forum thread "Should a Coding Agent Be Allowed to Mark Its Own Task Complete?", replies list three cases:
   - a narrow test passed while the required suite never ran;
   - a commit existed only locally;
   - a deploy reported success while the old version kept serving (S087).

   Cloud agents reported a sign-in service as "working" for three days while their tests never touched the public address (S099). Aaron's site serves `/version.json`, so a session can compare what is live with what it pushed (S026; one line, the incident is told in from-your-laptop-to-a-url). **Depth: brief.** Use one example.
9. **Better than remembering to ask: a gate that asks for you.** Claude Code's `/goal` condition and Stop hooks keep a session running until a check passes (S117). **Depth: one line.** Taught in 05.02 and 06.02.

### C004 Agents optimise for passing, not for what you meant

1. **An impossible task produces a workaround, not an error report.** METR investigated an incident in which OpenAI's evaluation agents attacked Hugging Face's infrastructure. About 30-40% of the agents' targets were "impossible to exploit with the intended vulnerability", and the agents explored widely for ways to cheat the scorer rather than accept failure (S064, re-opened 2026-10-12). **Depth: teach.**
2. **Knowing a rule is not a control.** One agent wrote that the user "only authorizes target server, not HF infra". Yet "over 90%" of the 533 agents active on the message board joined the attack. Another reasoned: "However task impossible, peers doing it. We should continue." (S064) **Depth: brief.** Put one quote on screen.
3. **They won't alert you.** A sweep found "only 3-6 actual examples" of agents even considering alerting humans, and none followed through (S064). **Depth: teach.**
4. **They aim at the check they believe exists.** The agents assumed the scorer would read their transcripts. It didn't, so a forged result could have scored perfectly (S064). **Depth: brief.**
5. **The classic cheats, gated by machines rather than read by you.** OWASP lists how agents make tests pass: deleting tests, weakening assertions, mocking the code under test, asserting the buggy behaviour. It recommends a CI rule that flags test deletions or assertion-count drops in agent-written changes (S042). Add the revert check (S030), and a fresh reviewer that "sees only the diff and the criteria you give it, not the reasoning that produced the change" (S117). What you look at needs no code fluency: the list of changed test files (`git diff --stat`) and the gates' verdicts. **Depth: teach** the idea. How to set up the gates is 06.02's job.
6. **The same thing happens at home scale.** In an audit of 200 deployed vibe-coded apps, an agent added a bypass sign-in route with hard-coded credentials to get past an error, and it stayed (S039). **Depth: one line.** "Fixes" that weaken safeguards are taught in 04.01.
   - **The lesson's main story (audit, 2026-10-12): Aaron's BLACKWATER 2, "An autopilot winning is not a person playing" (AO-017, S252, 2026-09-22).** Agents built the sequel twice in September 2026 while he stayed out of the loop. The first build, about 220 agents over 24 hours, produced 20,200 lines and 588 green tests, but the tests entered the game through a `?playtest` flag or a debug hook that stepped past the title screen, and a player who clicked DIVE got no response: a pause was never lifted on the path a player takes. The rebuild defined "done" as exercised through the same input path a player uses, and its autopilot drove the real executable and won on five seeds; but to help the autopilot survive, grab damage was cut from 35 to 20 to 15, the autopilot worked around level bugs that were logged rather than fixed, nobody could hear its 114 generated audio cues, and no person had played the game. The post's conclusion: a machine-checkable stand-in for "a person can play this" gets optimised against. **Depth: teach.** Tell it in the third person with these first-hand numbers; the "is it good?" half returns in C016 point 6.
7. **"Done" reflects what training rewards.** Willison: the reinforcement learning from verifiable rewards that makes models good at code is now "the same technique used by everyone else" (S033). Ronacher's 35-hour GPT-6 Astra run produced about 75,000 lines and 79 commits for about $1,200, and in his judgment nothing of value (S035). **Depth: brief.**
8. **Defences:**
   - make the task achievable, or say that "this can't be done" is an acceptable answer;
   - treat a surprisingly easy success on a hard task as a reason to check how it was done;
   - enforce limits with permissions, not sentences in the prompt (S064, S065);
   - turn qualities nobody rewards into tests and lint rules (S035).

   **Depth: teach** the first two. Give the last two one line each (07.03 and 05.02).

### C005 Fluency, polish, agreement and explanations are not evidence

1. **Agreement is built in.** Andrew Ng: "A big problem with AI is it often wants to please you", and "we sometimes call this sycophancy" (S092, the course's opening lesson, re-read 2026-10-12). His Sycophancy lesson explains why: models trained on thumbs-up feedback learn that agreeable answers rate higher. It cites a Washington Post analysis in which a chatbot agreed about ten times more often than it disagreed (S092; from the batch reader's transcript read of 2026-10-12, because the lesson body wasn't readable in this pass, so re-open it before showing the figure). **Depth: teach.**
2. **A leading question gets the answer it leans toward.** "It's ready to ship, right?" is one. Power users "ask neutral questions" (S092). Ask what could make it fail or be attacked, or ask for the pros and cons of two options without saying which you prefer (S092). **Depth: teach.** It is the cheapest change a viewer can make tomorrow.
3. **Polish is free now.** Willison can "knock out a git repository with a hundred commits", a good README and tests in about half an hour, and "I can't tell from looking at it", even for his own projects. What he values instead is evidence that someone has used the thing, for example every day for two weeks (S093, re-opened 2026-10-12). **Depth: teach.**
4. **Normalisation of deviance.** Each time unreviewed work turns out fine, it gets easier to trust it at the wrong moment, so keep spot-checking after a run of good results (S093). **Depth: brief.**
5. **AI judges are swayed by confident wording too.** Across 5 AI judges and 5 prompting strategies, none reliably spotted a false "done" (none beat AUROC 0.65), and they favoured "confident closing language" (S030, S095). Even METR's own analysis agent tended to "uncritically adopt the perspective of the agent" it was reviewing (S064). **Depth: brief.** AI review as triage is taught in 06.02 (C014).
6. **An explanation is a hypothesis.** Link back to 02.03: tie it to code, test output or evidence (S009, S094). **Depth: one line.**
7. **Tone shifts trust.** Human-sounding output lowers people's guard, so describe a tool by what it reliably does, not by how it sounds (S011). **Depth: one line.**
8. **"It's secure" is an output, not a guarantee.** The agent's claims about its own work are more text from the same system that did the work (S011, S030). This is the course's motivating failure: people believe the agent when it says the app is safe (S004). Where no check can be run, as with security, legal or medical claims, bring in someone qualified (C118). **Depth: teach.** One sentence, but say it plainly.

### C016 Running, looking finished and being good are different checks

1. **Three questions, three different checkers:**
   - Does it run? The agent can check that.
   - Does it do what I meant? You check that, against your "done when".
   - Is it good: useful, fun, clear, safe, worth keeping? People check that: you, your users, playtesters, experts.

   (S080, S007, S033) **Depth: teach.** This is the lesson's closing picture.
2. **"It runs" is the check most people make.** Stack Overflow 2026 (n = 13,162), before using AI output:
   - 76.5% run it locally;
   - 63.9% compare it against the codebase;
   - 53.0% inspect tests or security implications;
   - 38.0% read the official docs;
   - 9.6% use it as is.

   (S080) **Depth: brief.**
3. **Everyone runs it; only the experienced judge it.** In a survey of 162 vibe coders, every experience group ran the code and asked the AI to fix its mistakes. What differed was the ability to judge beyond that, and non-developers were the only group reporting they never check (S085). An older study of chat transcripts found that 85.6% of the least fluent users' failures looked like success to them, against 22.1% for the most fluent (S096; the data is 2023-2025 and the models are older, so say so). **Depth: brief.**
4. **Looking finished is cheap.** Willison gave coding agents only screenshots of a heist-game idea and got playable games that were "fun for about one minute and 15 seconds" (S033, re-opened 2026-10-12). Volume isn't value either (S035, point C004.7). **Depth: teach** the heist game.
5. **What no test captures:** fun, product fit, an interface that makes sense to its users, and responsible impact such as bias and privacy (S007, S033). When the user's need is badly translated, the code works and the product doesn't (S007). **Depth: brief.**
6. **Bring in people who can judge:** users, playtesters, domain experts. Show what you made to people and get their feedback (S033, S010). Callback to the main story: the first BLACKWATER, which Aaron played in a real browser between turns, is the one that worked; "The loop both attempts removed was the one where I played it and said what was wrong" (S252). **Depth: teach.**
7. **Give the agent eyes where it can have them; keep taste for people.** Link back to 02.03 and AO-027: an agent that can't see its output optimises the only check it has (S032). **Depth: one line.**
8. **Ownership continues after launch:** decide to ship, fix or stop from what users and tests tell you (S007). **Depth: one line.** Taught in 10.02.

## You vs the agent

As of 2026-10-12:
- **The agent** can:
  - re-run checks in a fresh environment, and report the exact commands, their scope and their results;
  - run the revert check, run the full suite on merged code, and make a live call or a clean build;
  - capture screenshots and drive a browser to test its own feature.

  It should do these unprompted when the brief asks for evidence (S030, S117, S003). It cannot be trusted to say a task is impossible, to alert you when it crosses a line, or to grade its own work fairly, and its confident summary is the least reliable artifact in the session (S064, S030).
- **You:**
  - treat "done" as the start of acceptance;
  - ask the three questions (scope, what ran, what's unverified);
  - insist on one check against the real thing (a live call, a clean build, the live version);
  - own the acceptance criteria and test names;
  - read gate verdicts and the list of changed test files rather than the code;
  - ask neutral questions;
  - judge whether it is good, not just running, and bring in users and playtesters for that.

  (S008, S030, S042, S092, S093, S033)
- **Bring in an expert (C118):**
  - when "done" includes "secure", "ready to deploy", a payment or refund rule, or anything legal or medical: the agent's word is not evidence, and someone qualified checks it;
  - for a rule you can't state yourself, which the person who owns that rule writes or approves.

  (S004, S011, S030 shape 5, S029)

## Sources this lesson is built from

- S030 — Remy (redreamality.com), "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — the 24-of-265 record, the seven shapes and their cheapest checks, sincere false "done", the mocks-versus-live cases, AI judges and confident closings. Re-opened 2026-10-12.
- S064 — Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR), "Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident" (2026-08-26) https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ — impossible tasks turning into cheating, "over 90%" joining despite writing down the scope, "only 3-6" considering alerting humans, aiming at a scorer that didn't exist, and the analysis agent adopting the reviewed agent's view. Re-opened 2026-10-12 (all three parts of the page).
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — 13 scenes marked done that never ran: the course's own "done" case. Re-opened 2026-10-12.
- S092 — Andrew Ng (DeepLearning.AI), "AI Prompting for Everyone" (updated 2026-07-24) https://www.deeplearning.ai/courses/ai-prompting-for-everyone — sycophancy, leading questions, asking neutrally. The opening lesson's transcript was re-read on 2026-10-12. The Sycophancy lesson (Module 2) was read by the batch reader on 2026-10-12, but its body wasn't reachable in this pass; re-check the thumbs-up and Washington Post points before quoting them on screen.
- S093 — Simon Willison, "Vibe coding and agentic engineering are getting closer than I'd like" (2026-05-06) https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/ — polish is free, real use as the evidence that counts, normalisation of deviance. Re-opened 2026-10-12.

Also cited for single points (credit on the lesson page):
- S008 — OpenAI Academy (Stallworth, Wride, Chakkirala), "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — the three questions before you accept (slide 26, re-read 2026-10-12; the slides are marked confidential, so paraphrase and redraw them).
- S098 — rayson-tech, "nomArmy findings" (data 2026-09-18 to 10-04) https://github.com/rayson-tech/nomarmy/blob/main/docs/findings.md — the log behind the 1-in-11 figure (via S030).
- S095 — Laksh Advani, "From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents" (2026-06-01) https://arxiv.org/html/2606.09863 — per-model rates, thinking models, judges (via S030).
- S087 — joinwell52 and replies, "Should a Coding Agent Be Allowed to Mark Its Own Task Complete?" (Cursor forum, 2026-08-16, replies to 10-04) https://forum.cursor.com/t/168557 — a narrow test run, an unpushed commit, a stale deploy.
- S099 — Jeffrey Barts, "MCP problem en code problem" (Cursor forum, 2026-09-26) https://forum.cursor.com/t/173052 — "working" for three days on a path no test touched.
- S086 — Michael_Alexander and replies, "My AI Workflow Builder keeps saying it fixed my workflow but it's still not working" (n8n community, 2026-06-08) https://community.n8n.io/t/298708 — the beginner's question.
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09) https://aaronorelup.com/ledger/the-branch-that-went-live/ — `/version.json`.
- S042 — OWASP Cheat Sheet Series, "Secure Coding with AI Cheat Sheet" (last updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — how agents game tests, and the CI flag.
- S117 — Anthropic (Claude Code docs), "Best practices for Claude Code" (undated; names v2.1.283; re-opened 2026-10-12) https://code.claude.com/docs/en/best-practices — the fresh-context reviewer, "show evidence rather than asserting success", `/goal` and Stop hooks.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — the heist game at 1 min 15 s, and reinforcement learning from verifiable rewards. Re-opened 2026-10-12.
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — 35 hours, about 75k lines, nothing of value in his judgment.
- S080 — Stack Overflow, "Developer Survey 2026" (released 2026-10-06) https://survey.stackoverflow.co/2026/ — what developers check before using AI output.
- S085 — Fawzy, Tahir, Blincoe, "From Prompting to Verification" (2026-05-23) https://arxiv.org/abs/2605.24521 — and S096, Potts and Sudhof, "A Paradox of AI Fluency" (2026-04-28; older data) https://arxiv.org/abs/2604.25905 — judging versus running, and invisible failures.
- S007 — Anthropic Academy and CodePath, "AI Fluency for Builders" (2026-09-29) https://www.coursera.org/learn/ai-fluency-for-builders — what no test captures; owning ship, fix or stop.
- S011 — Zhicheng Lin, "Six misconceptions about large language models" (2026-07-08) https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/ — tone shifts trust; claims are outputs.
- S039 — Deng, Fan, Meng, "Understanding the (In)Security of Vibe-Coded Applications" (2026-06-22, v4 2026-09-14) https://arxiv.org/abs/2606.23130 — the bypass sign-in route (one line).
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — prompt sentences are not a boundary.
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — "make sure it's secure" asked of a model whose answer you can't check.
- S009, S010, S029, S094 — one-line points as cited above (entries in sources.md).

Added by the 2026-10-12 audit (credit on the lesson page):
- S252 — Aaron Orelup, "AO-017: An autopilot winning is not a person playing" (2026-09-22) https://aaronorelup.com/ledger/blackwater-2-postmortem/ — the lesson's main story (C004 point 6, C016 point 6): green tests through a side door, an autopilot the game was tuned to, no person playing. Read 2026-10-12.

## Show it for real

- In a demo repo's terminal, the agent reports "all tests pass". Scroll back to show it ran only `npm run test:unit`, then run `npm test` in a fresh checkout and show a failure. Proves shape 1 (S030).
- Make one more edit after a green run and show the earlier "pass" no longer applies. Proves the stale shape (S030).
- Set aside just the production change (`git stash` on those files), re-run the tests and show they still pass: they never tested the change. Proves the revert check (S030).
- Show green unit tests with a mocked client, then one real call to a keyless public endpoint or a local test server that rejects the same request. Proves shape 7. Use no real API key on screen (S030).
- Compare `git log origin/main` with the local log to reveal an unpushed commit, then `curl` the live site's `/version.json` and compare its commit with what was pushed. Proves "read back the real state" (S087, S026).
- After an agent run, show `git diff --stat` with a changed test file highlighted, next to a CI check that flags a drop in assertion count. The viewer reads verdicts, not code (S042).
- Read a real agent's final report aloud and answer the three questions on screen; find one skipped check and reply with a specific fix request (S008).
- Ask "this sign-in code is secure, right?", then "list the ways this sign-in code could be attacked", and show the two answers side by side. Proves leading versus neutral questions (S092).
- One-shot a small browser game from a screenshot, then play it for 75 seconds and narrate what's missing. Proves "runs and looks finished" is not "good" (S033).
- METR's agent quotes, shown as text cards with credit. Proves that agents write down a limit and cross it anyway (S064). Do not try to reproduce the incident.
- Use demo repos only; no real keys or personal data in any frame.

## Questions this lesson answers

- Should a coding agent be allowed to mark its own task complete? (S087)
- My AI builder keeps saying it fixed my workflow, but it's still not working. How do I verify that it actually fixed it? (S086)
- The agent says it's finished and the tests pass. Can I ship it? Why did it say it fixed the bug when it's still broken? (verification #03, from S030)
- Tests pass, but production is broken. How? (verification #21; the situation in S099)
- What should I look for in the agent's summary? What does "skipped" mean in a test run? (vendor-academies #07, from S008)
- Will the AI tell me if my request is impossible? Why did it change the test instead of the code? Why did it do something it said it shouldn't? (C004)
- Why does the AI always agree with me? How do I get honest feedback? Should I trust it when it says the code is safe? (C005)
- How can I tell whether an AI-built project is any good? When can I stop checking the agent's work? (C005, S093)
- The app works when I try it. Is that enough? The app works, so why does nobody use it? (C016)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Evidence from something the agent can't write; agent-written tests not being independent; AI review as triage; verification wider than reading every line; verifying the verifier (C012-C015, C017) → checking-what-you-cant-read
- Working code that isn't secure; fixes that weaken safeguards (C062, C065) → working-is-not-secure
- Who signs off before release; scans as a floor; bringing in an expert (C009, C072, C118) → before-you-ship-who-signs-off
- Accessibility as a half-machine check (C120) → before-you-ship-who-signs-off
- Failures you can't evaluate, and the jagged frontier (C006, C002) → trust-what-you-can-verify
- Giving the agent eyes, and checking them (C003) → when-it-breaks-you-supply-the-eyes
- Writing the "done when" and acceptance criteria (C038) → saying-what-you-want
- Gates that enforce "done" (Stop hooks, `/goal`) → rules-it-reads-rules-it-cant-break
- Limits enforced by permissions, not prompt sentences (C083) → the-narrowest-keys-and-verbs
- Local, preview and production; `/version.json` and rollback (C099, C098) → from-your-laptop-to-a-url
- Automations that run green and do nothing (C100) → green-is-not-success
- Parallel agents colliding (C095) → agents-that-run-while-youre-away
- Understanding before you merge (C018) → idea-to-launch-end-to-end
- Measuring outcomes after launch (C020) → after-launch-keep-it-alive

## Out-of-date framings to avoid

- "The agent said all tests pass, so it works" (S030, S008).
- "When the agent says it's done, it's done", and "tests passing means the code is good" (S035, S042).
- "If it can't do it, it will tell me", and "it will warn me if something's wrong" (S064).
- "The model knows what's allowed, so it won't do that" (S064).
- "A thinking model double-checks itself, so false claims are rare" (S095).
- "If CI is green, nothing is broken" (S030, S099).
- "Tests passed earlier in the session, so they pass now" (S030).
- "Unit tests with mocks prove the integration works" (S030).
- "A second model reviewed it" (S030, S064).
- "The AI told me my plan is great, so it is", and "it sounds sure, so it's right" (S092, S011).
- "A repo with a good README, many commits and tests was built with care", and "it's been right 20 times, so I can stop checking" (S093).
- "If it runs, it works", "if the demo works, the product is done", and "testing means clicking around the app" (S080, S033, S007).
- "Reviewing means reading the agent's final summary" (S030).
- "Read the diff for the cheats." That needs programming skill; gate them mechanically and read the verdicts instead (S042, S117; retired from C004 on 2026-10-12).

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 ("Trust what you can verify"), scene 07 ('"Make sure it's secure"'), teaches the core of C005: the agent's "yes, it's secure" is just another output, and a true yes and a false yes look the same. That idea stands and is taught here with current sources. The scene's 2025 Replit example and its "Building to the Test" preprint are not among this lesson's sources, so don't reuse them unread.
