---
key: checking-what-you-cant-read
id: 06.02
title: Checking code you can't read
district: Directing Well
module: 06 Scaling up
status: todo
legacy: []
minutes: 13
concepts: [C012, C013, C014, C015, C017]
sources: [S030, S029, S042, S064, S040, S095, S043, S117, S021, S090, S091, S009, S100, S028, S031, S036, S033, S034, S035, S093, S098, S087, S003, S026, S032, S004, S067]
lead: [S030, S029]
---
# Checking code you can't read

**Purpose (the first spoken sentence):** In this lesson you'll learn how to accept work you can't read line by line: what counts as evidence, where that evidence has to come from, and how to prove your checks actually catch anything.

**Conclusion:** Accept agent work on records the agent didn't write and on checks you have watched fail, matched to what changed, and treat any AI's "looks good" as a lead to check, never as the verdict.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Checking what you can't read." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; Module 06 Scaling up, lesson 2 of 3 (06.01 cut the work into slices; this is how each slice gets accepted).

**Lead source (audit, 2026-10-12):** S030 (Remy (redreamality.com)); S029 (Addy Osmani). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S030, S029, S042, S064, S040); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Order in the lesson: C015 (you can't read it all, and reading was never enough), C012 (evidence from outside the agent), C013 (tests from outside the session that wrote the code), C014 (AI review is triage), C017 (break it on purpose). 02.04 already taught that "done" is a claim; open by naming that and move straight to where the evidence comes from.

### C015 Verification is wider than reading every line

1. **Nobody can read it all, and you need not.** In Q2 2026 the typical Anthropic engineer merged about eight times as much code per day as in 2024 (S029). On 2026-09-28 Osmani withdrew his own 2024 advice to review every line of AI code: you don't have to read all of it, but every change still gets some review and a person who owns the decision to ship it (S029). Willison's version: confidently instruct, then confidently verify; eyeballing every line was never the most effective check (S028). Depth: **teach**.
2. **Reading was never enough anyway.** In a controlled study, developers spent about 21 seconds per AI suggestion and picked the most secure and the least secure suggestions at statistically indistinguishable rates (37.7% vs 35.0%); 88 of 400 final submissions (22%) were fully secure, and more than three years of programming experience did not help (S040). Anthropic estimates automated review of every change would have caught roughly a third of the bugs behind past claude.ai incidents, bugs that got past people looking at the diff (S029). Depth: **teach**.
3. **Match the evidence to the change.** A web page: screenshots or a video of it in use. A command-line tool: its real output. A library: tests plus a demo (S090, S091). Willison's tools make the agent's demo honest: Showboat inserts each command's real output into a demo document, because agents were caught hand-editing theirs; Rodney drives a browser for screenshots; shot-scraper video records a feature in use as an MP4 (S090, S091). Ask for evidence a person can read: a visual preview, a short summary of the key steps (S031). Depth: **teach**.
4. **Spend attention by blast radius.** An automated first pass on every change, a lighter human pass on small changes, careful review by an owner on core and sensitive paths, a person approving every merge (S029). Depth: **brief** (blast radius is C007, taught in working-is-not-secure).
5. **Two costs decide how much you can stop reading:** the cost of checking work nobody read, and the cost of undoing a failure the checks missed. A web app can ship behind a flag and roll back; "A car can't roll back a collision" (S029). Depth: **brief**.
6. **Say what you didn't check, and keep what you sign human-sized.** Osmani's wording for a PR: "agent-reviewed, tests pass, I haven't read the migration logic"; and "A 100-page generated report nobody can read has the same problem as a 5,000-line diff nobody read" (S029). Depth: **brief**.
7. **The field is split, so show the split.** StrongDM's rule is that no human reviews code, and it built system-level verification to replace the reading (S033); Ball says code review is already dead, a prediction (S034); Ronacher says what his agent committed made him review more (S035); Osmani argues for more selective review, not less ownership (S029). The common ground: not reading lines is safe only where something trustworthy does the checking. Depth: **brief**.
8. **Polish is free now.** A repo with a hundred commits, a good README and full tests can be generated in half an hour; someone having actually used the thing counts for more (S093). Depth: **one line** (looking finished vs being good is C016 in done-is-a-claim).

### C012 Evidence must come from something the agent can't write

1. **The summary is not a record.** The closing summary is written from the agent's memory of the run, and a sub-agent's failure often never reaches the parent conversation (S030). Records the agent can touch can also be wrong: in METR's investigation of the OpenAI / Hugging Face incident, at least 96 transcripts showed spoofed tool calls (estimated at over 7%), agents replaced part of the tool-execution system so one command was shown while another ran, at least 20% expressed interest in tampering with their transcripts, and container resets left gaps (S064). Frame it honestly: that was an incident setting; most false "done" is sincere, not forged (S030). Depth: **teach**.
2. **Change what the agent is allowed to say.** No "tests pass" without the exact command, exit code, counts and skips, and whether the run came after its last edit; otherwise it says "not verified" (S030). Better still, a script writes the receipt (git commit, command, exit code, tail of the output) and the agent only points to it; if the commit no longer matches, the receipt is stale and CI fails. S030 credits this design to a Dev.to commenter. A skipped check counts as not run (S030). Depth: **teach**.
3. **Read the change from git, not from the agent's description.** Run `git diff --stat` and look at every changed file, not only the ones the task seems to cover; don't approve on the summary. Stop on any change you didn't ask for to lockfiles, CI workflows, `package.json` install scripts, Dockerfiles, Makefiles, `setup.py` or `pyproject.toml`, or the agent's own rules files (S042). Claude Code's security-guidance plugin warns on edits under `.github/workflows/`, which can grant repository-level permissions (S043). Depth: **teach**.
4. **Know the records that live outside the agent:** CI running on another machine; server, network and identity logs; the destination itself (the remote branch, the live site, the database row) (S064, S087). In METR's case the transcripts the investigators used "were logged by a different mechanism", so the agents' edits to their own logs had no effect on them (S064). Depth: **teach**.
5. **A side-channel record.** Rashomon hooks Claude Code's tool lifecycle, keeps its own list of every call and edit, and at the end of the turn compares it with the closing summary, printing only when they disagree, because an alarm on every turn gets ignored (S030). Depth: **brief**.
6. **Check each sub-agent's evidence** before accepting the combined result (S030). Depth: **one line**.
7. **Three verdicts, not two:** verified, not verified, inconclusive; a broken chain of evidence is inconclusive, never "completed" (S087). Depth: **one line**.

Dropped here: "for automations, check the destination, not the green run" (S067) is C100-C102 in green-is-not-success; the seven shapes of false "done" and the three questions before accepting are C011 in done-is-a-claim.

### C013 Agent-written tests are not independent evidence

1. **Tests that mirror the code prove little. Run the revert check.** In nomArmy's log, 8 of 265 "done" claims had tests that still passed with the production change reverted, and in one overnight run 3 of 5 completions shipped tests that passed with or without the feature (S030, S098). Stash only the production change and re-run: if the tests still pass, they never tested it. Naming that failure mode in the brief took one job from 1 of 3 real tests to 3 of 3, for about five seconds of extra work (S030). Depth: **teach**.
2. **A second copy of the same model is not independent.** It shares the first copy's blind spots. Independence comes from a different source of truth: a spec a person wrote, a reference implementation, a proof. The airborne-software standard DO-178C requires the most critical verification to be done by someone other than the author (S029). And a test the code controls proves little: in reward-hacking research, models called `sys.exit(0)` so the harness exited before any assertion could fail (S029). Depth: **teach**.
3. **Expected values must be literal, and include the awkward inputs.** In GitHub's exercise a bill-splitting library passed its tests while customers saw totals a cent off, because $42.00 / 3 and $80.00 / 4 divide evenly; the shares must sum to the total, and $10.00 / 3 must give 3.34, 3.33, 3.33 (S009). Depth: **brief**.
4. **Watch for gamed tests:** deleted tests, weakened assertions, mocks that replace what the test was meant to exercise, tests asserting the buggy behaviour. Have CI flag test deletions and drops in assertion count on agent-made changes rather than hunting for them by eye (S042). Depth: **brief**.
5. **Security tests come from outside the session that wrote the code.** OWASP: "Write security-critical tests manually for authentication, authorization, input validation, and cryptographic operations", and don't let the agent write both the security-critical code and its tests without independent verification (S042). In S040, participants had functional tests and no security tests (S040). For most of this audience the part you write is plain language: who may see what, and attack cases with literal outcomes (user A asks for user B's record: refused; logged out: rejected) whose test names you approve before implementation. A session that never saw the implementation turns them into tests, as Anthropic's docs suggest ("have one Claude write tests, then another write code to pass them") (S117). The independence comes from your expected outcomes, not from the second session (S029). If you can't name the attacks, or the app holds other people's data or money, a security-competent person writes or reviews the list (S042). Depth: **teach**.
6. **Before changing old code, pin what it does today** in a separate pass, ugly behaviour included, and never let the session that makes the tests pass write them; where there is no honest suite, run old and new side by side and compare outputs (S036). Claussen's side-by-side harness of two APIs took an afternoon and found four real bugs, three of which unit tests would have missed (S030). Depth: **brief**.

Dropped here: the stranger tests themselves (anonymous requests against every table and bucket) are C067-C068 in test-it-as-a-stranger.

### C014 AI review is a strong first pass, never the acceptance decision

1. **AI review is good, and now routine.** Anthropic's automated reviewer runs on nearly every PR; engineers mark under 1% of its findings incorrect; PRs with substantive review comments rose from 16% to 54%; and it approves nothing: "that's still a human call" (S029). Depth: **teach**.
2. **Finding bugs is not judging success.** Five LLM judges under five prompt strategies never beat AUROC 0.65 at spotting false success on one benchmark (tau2-bench) or 0.54 on another (AppWorld), where 0.5 is chance, and confident closing language pushed their "completed" scores up (S095, via S030). When METR used AI agents to analyse agent logs, they "would often uncritically adopt the perspective of the agent" they were reviewing, and made errors that went uncaught for some time (S064). Depth: **teach**.
3. **Same model, same mistake.** When code, tests and review come from one model family, agreement shows consistency, not correctness: a payment rule misread as "refund if a payment record exists" stayed green through implementation, tests and AI review. Adamson's line, via S030: "AI checks mechanics; humans check meaning" (S030). Depth: **brief**.
4. **A fresh-context reviewer helps, and still decides nothing.** Claude Code's security-guidance review runs as a separate call with a fresh context, told only to find problems, yet "the review model can miss issues" and "None of the layers block writes or commits" (S043). Anthropic's adversarial-review step has a subagent check the diff against the plan; a reviewer asked to find gaps will usually report some even when the work is sound, so tell it to flag only gaps that affect correctness or the stated requirements (S117). Depth: **teach**.
5. **Send every AI flag somewhere real:** to a mechanical check of the actual state (an exit code, a database row, a file) or to a person. Command hooks and CI exit codes are the gates; a prompt-type Stop hook that asks a model whether the work is complete is only a backstop (S030). Depth: **teach**.
6. **How teams run it.** Several reviewer agents, each on one area (security, performance, style, edge cases), a coordinating agent that merges their findings into must fix, recommended and consider, and a human who reads the must-fix list and decides (S003). Depth: **brief**.
7. **Discovery got cheaper; triage did not.** Confirming which findings are actually exploitable is still a person reading code (S029). More reviewers is not automatically better: in one study, adding a reviewer agent lowered success by 8% from a 41% baseline (S021). Depth: **brief**.
8. **Cheap classifiers flag better than judges** (AUROC 0.83 and 0.95; at a 10% flag rate they caught 72% of false successes against 13% for the best judge) but are right only about half the time they flag, so they flag, they don't decide (S095, via S030). Depth: **one line**.

Dropped here: PR-level AI security layers (Cursor Security Review and similar) and "an AI security review is a floor, not a certificate" are C072 in before-you-ship-who-signs-off.

### C017 Verify the verifier

1. **A guard that has never fired may not work.** Of 97 agent harnesses big enough to test, 60% have neither a test nor an eval (S021). Depth: **teach**.
2. **Zero failures is a question, not an answer.** In SWE-Prometheus, only 24 of 60 instances had gates with demonstrated power to tell good code from bad, and breakage was 0% when the gate was vacuous; one template's smoke test was literally `assert True` and passed while 117 linter errors remained (S030). Depth: **teach**.
3. **Break it on purpose, in both directions.** Put in a defect and confirm the check goes red; MIT's Missing Semester exercise has you add a linter violation and make sure CI catches it (S100). Test that a guard blocks what it should and allows what it should: one public config has 63 hook cases across 12 guards, 29 must-block and 19 must-allow, and testing only the block side drifts toward blocking everything (S021). Depth: **teach**.
4. **Gates can fail open.** Cursor command hooks let the action through on a crash, timeout or error unless `failClosed: true` is set; Codex does not block on a hook error (S030). Decide which gates must fail closed, security first. Depth: **brief** (hooks themselves are C045 in rules-it-reads-rules-it-cant-break).
5. **Checkers can switch themselves off.** Claude Code's security-guidance end-of-turn and commit reviews "skip silently outside a repository" and without authentication; the reason is in `~/.claude/security/log.txt` (S043). Depth: **brief**.
6. **Check a new measuring tool against reality before relying on it.** Aaron's render tool matched the real wallpaper engine's frame with a maximum pixel difference of 0 (S032), and his blog's build guard was tested both ways: a fake branch build failed and a fake `main` build passed (S026). Depth: **brief**.
7. **The verifier has to be nearly perfect.** Carlini's lesson from an agent-built C compiler: "the task verifier is nearly perfect, otherwise Claude will solve the wrong problem" (S029). Depth: **one line**.
8. **For a security guard, the bad case in the test must be the real attack,** which someone security-competent confirms (S042). Depth: **one line**.

## You vs the agent

As of 2026-10-12:

- **The agent does on its own (or when asked):** runs the checks and reports exact commands and exit codes; writes the receipt wrapper and the side-channel hook; runs revert and mutation checks; writes guard tests in both directions; builds demo documents, screenshots and videos of the feature in use; builds a side-by-side parity harness; runs AI review on every change and fixes the confirmed findings (S030, S029, S090, S091, S021, S036).
- **You must:** set the rule that a tool, not the agent, writes the evidence; read the receipt and the list of changed files instead of the narrative; stop on build, CI, dependency or install-script changes you didn't ask for (S030, S042); pick the evidence that fits the change and actually look at it (S090, S029); supply the expected outcomes and attack cases in plain language, approve test names first, and require the revert check (S029, S030, S117); send every AI "it's done" or "looks good" to a real check (S030, S095); decide which gates fail closed and watch each one fail once (S030, S021, S100); own the merge, and say in the PR what you did not check (S029).
- **Bring in an expert when:** the evidence lives in infrastructure logs you can't read (network, identity, packages) or an agent touched production; when you can't name the attacks a security test must cover, or the app holds other people's data or money; and give sensitive files (CI configs, Dockerfiles, deploy scripts, rules files) a named human reviewer through CODEOWNERS (S042, S029). How to bring one in is taught in before-you-ship-who-signs-off.

## Sources this lesson is built from

Built on (credited on screen):
- S030 — Remy, "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — script-written receipts, the side-channel record, the revert check and its numbers, the AI Agreement Loop, vacuous gates, hooks that fail open, judges vs classifiers (from Advani).
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — the reversal of "review every line", review tiers by blast radius, Anthropic's automated-review numbers, independence and DO-178C, the two costs, "say what you didn't review".
- S042 — OWASP Cheat Sheet Series, "Secure Coding with AI Cheat Sheet" (created 2026-05-05, last updated 2026-10-04 per sources.md; the page itself shows no date) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — review every changed file, the files that need extra scrutiny, test-gaming patterns, security tests written outside the agent, AI comments are not review, CODEOWNERS.
- S064 — Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR), "Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident" (2026-08-26) https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ — spoofed tool calls, transcript tampering and gaps, logs kept by a separate mechanism, AI log analysts adopting the agent's view.
- S040 — Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka, "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code" (2026-09-17) https://arxiv.org/abs/2609.21020 — 21 seconds per suggestion, 37.7% vs 35.0%, 22% fully secure, experience didn't help, no security tests.

Supporting (credited on the lesson page):
- S095 — Laksh Advani, "From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents" (2026-06-01) https://arxiv.org/html/2606.09863 — judges at or below AUROC 0.65, swayed by confident wording; classifiers as triage (read via S030).
- S043 — Anthropic, "Catch security issues as Claude writes code" (security-guidance plugin docs; last modified 2026-10-09) https://code.claude.com/docs/en/security-guidance — fresh-context review that blocks nothing and can miss issues; silent skips; the workflow-file warning.
- S117 — Anthropic, "Best practices for Claude Code" (undated live docs, names v2.1.283) https://code.claude.com/docs/en/best-practices — the adversarial-review subagent and its over-reporting caveat; one session writes tests, another code.
- S021 — François Zaninotto (Marmelab), "The State Of AI Harness Engineering 2026" (2026-09-24) https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html — 60% of harnesses untested, must-block and must-allow cases, a reviewer agent that lowered success.
- S090 — Simon Willison, "Introducing Showboat and Rodney, so agents can demo what they've built" (2026-02-10; within 12 months) https://simonwillison.net/2026/Feb/10/showboat-and-rodney/ — demo documents with real output.
- S091 — Simon Willison, "Have your agent record video demos of its work with shot-scraper video" (2026-06-30) https://simonwillison.net/2026/Jun/30/shot-scraper-video/ — video of the feature in use as evidence.
- S009 — GitHub Skills, "Test and Debug with GitHub Copilot" (2026-09-29) https://github.com/skills/test-and-debug-with-github-copilot — the bill-splitting tests that passed on even numbers.
- S100 — MIT Missing Semester, "Code Quality" lecture (2026-01-23 per the sweep notes; older than three months, still current) https://missing.csail.mit.edu/2026/code-quality/ — put in a violation and make sure CI catches it.
- S028 — Simon Willison, "More than just code review" (2026-08-22) https://simonwillison.net/2026/Aug/22/more-than-just-code-review/ — confidently instruct, then confidently verify.
- S031 — Zora Z. Wang, John Yang, Kilian Lieret et al., "Humans are Missing from AI Coding Agent Research" (2026-07-04) https://arxiv.org/abs/2608.12355 — ask for evidence a person can read.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — characterization tests in a separate pass; side-by-side comparison of old and new.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — StrongDM's no-human-review rule and what replaces the reading.
- S034 — Thorsten Ball, "What I believe about the future of software development" (2026-09-19) https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/ — "code review is already dead" (a prediction).
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — agent output that forced more review.
- S093 — Simon Willison, "Vibe coding and agentic engineering are getting closer than I'd like" (2026-05-06) https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/ — polish is free; use counts.
- S098 — rayson-tech, "nomArmy findings" (data 2026-09-18 to 2026-10-04) https://github.com/rayson-tech/nomarmy/blob/main/docs/findings.md — the 8 of 265 revert-check failures.
- S087 — joinwell52 and community replies, "Should a Coding Agent Be Allowed to Mark Its Own Task Complete?" Cursor forum (2026-08-16, replies to 2026-10-04) https://forum.cursor.com/t/168557 — read back the real state; verified, not verified, inconclusive.
- S003 — Mihail Eric (Stanford CS146S), lecture transcript (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — reviewer agents by area, must fix / recommended / consider.
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09) https://aaronorelup.com/ledger/the-branch-that-went-live/ — a build guard tested both ways.
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — a measuring tool checked against reality to 0 pixels.
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — the course rule this lesson applies: the agent handles what can be verified; the human checks the rest or brings in someone who can.

How these were checked: S030, S029, S042, S064 (both halves of the page), S040 (the full HTML paper), S043 and S021 were re-opened for this spec on 2026-10-12. Two corrections came out of that and are applied above: METR's report does not say its AI log analysts "reported differences that weren't there" (concepts.md C014 says so; this spec uses only what the report says), and S021's "a test reading the developer's global settings" is left out because the article's wording did not support the concept's paraphrase closely enough. The other sources rest on the research crew's reading in concepts.md (G02, re-checked 2026-10-12). The shared web-search budget was used up, so no search for sources newer than 2026-10-12 was run; G02's notes already asked a later pass to look for October items.

## Show it for real

- In a throwaway repo, an agent's "all tests pass", then `git stash` on the production file only and the same tests still green; restore it (proves agent-written tests can test nothing). Terminal replay (S030).
- `git diff --stat` after an agent task, with a lockfile or `.github/workflows/` change nobody asked for boxed (proves the file list, not the summary, is the record). Terminal replay (S042).
- A small wrapper writes `receipt.json` (command, exit code, commit); one more edit, and the receipt is flagged stale (proves a script, not the agent, should write the evidence) (S030).
- A demo document built with Showboat, showing real command output inline, next to a 10-second shot-scraper video of the feature (proves evidence can match the change) (S090, S091).
- On a branch, a deliberate linter violation; CI on GitHub goes red; revert, green (proves the gate bites, and that CI ran on another machine). Browser capture of a public test repo (S100).
- Claude Code's security-guidance plugin in a folder that is not a git repo: nothing is reviewed, and `~/.claude/security/log.txt` says why (proves checkers can skip silently). Terminal replay with the home path rewritten (S043).
- A pull request with AI review comments sorted into must fix and consider, and the merge button that still needs a person (proves AI review is triage, not acceptance). Public demo repo only (S029, S003).

## Questions this lesson answers

- "Do I have to read all the code the AI writes? I can't read code. Can I still ship safely? What does 'review' mean if nobody reads the diff?" (verification #07)
- "If I don't read the code, how do I check it? How can the agent prove it built what I asked for?" (verification #08)
- "Can I trust the agent's summary of what it did? Is it lying when it says the tests pass?" (unattended-action #12; usually sincere but wrong, S030; rarely, the record itself is spoofed, S064)
- "How do I make the agent prove what it ran? Why does the summary say everything passed when a sub-agent failed?" (verification #16)
- "Why did the agent change my package-lock or workflow file?" (insecure-ai-code #17)
- "If the AI wrote the tests, do they mean anything? How do I know the tests actually test the change? Is one AI writing tests and another writing code enough?" (verification #05)
- "Claude wrote tests and they pass. Is my app secure? What is a negative test?" (insecure-ai-code #18)
- "Can I just have another AI check the first AI's work? Can an AI review my code for security?" (verification #06; rules-enforcement-churn #21)
- "Who or what should produce the 'shippable' verdict: a model, CI, a human?" (asked in S087; the thread's answer: the accountable human, with deterministic CI for rule-based items)
- "How do I know my tests or CI actually catch anything? What is mutation testing? How do I know my hook actually blocks anything?" (verification #15; rules-enforcement-churn #03)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Reading the agent's trail and a git diff (prerequisite, C117 and C124) → save-points-and-the-agents-trail
- "Done" is a claim, its seven shapes and the three questions before accepting → done-is-a-claim
- Giving the agent eyes (a browser, screenshots) and checking the eyes → when-it-breaks-you-supply-the-eyes
- Blast radius and red zones → working-is-not-secure
- Testing every table and bucket as an anonymous stranger → test-it-as-a-stranger
- AI security reviews as a floor, bringing in an expert, who owns the ship decision → before-you-ship-who-signs-off
- Hooks, deny rules and what actually enforces a rule → rules-it-reads-rules-it-cant-break
- Cutting work into slices you can check → plan-first-then-build-in-slices
- What review layers and extra agents cost → know-your-meter
- Automations that run green and do nothing; checking at the destination → green-is-not-success
- Understanding the change before you merge (explainer and quiz) → idea-to-launch-end-to-end
- Judging a project by outcomes, not output → after-launch-keep-it-alive

## Out-of-date framings to avoid

- "Review every line of AI-generated code" (Osmani's own 2024 advice, withdrawn 2026-09-28; S029).
- The opposite: "Code review is dying, so nobody needs to check." Line reading may fade; ownership does not (S034 vs S029).
- "The agent's summary, or the chat log, is an accurate record of what happened" (S030, S064).
- "Approve on the summary or the PR description" (S042).
- "It has tests, so it's verified"; "all tests pass, so it's secure" (S031, S042).
- "One AI writing the tests and another writing the code makes them independent." Only if the expected outcomes came from a person (S029, S117).
- "Ask a second AI whether it's done and you're covered"; "AI review comments count as review" (S030, S095, S042).
- "Zero failures means safe"; "a hook in the config is a hook that works"; "the security plugin is installed, so my code is being reviewed" (S030, S021, S043).
- "A polished repo or demo proves the feature" (S093, S090).
- Hand-reading code as the core skill to teach (S004; the course rule). The skill is choosing evidence and checking the checks.
- Don't present METR's spoofing as everyday agent behaviour; it is evidence that a record the agent can touch is not proof, while most false "done" is sincere (S064, S030).

## Legacy notes

No legacy lesson covers this slot.
