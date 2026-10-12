---
key: when-it-breaks-you-supply-the-eyes
id: 02.03
title: "When it breaks: what the agent needs from you"
district: First Build
module: 02 Your first build
status: todo
legacy: []
minutes: 10
concepts: [C003, C019, C042]
sources: [S094, S009, S003, S008, S032, S004, S117, S001, S002, S085, S096, S083, S006, S090, S091, S227, S178, S036, S116, S068, S029, S086, S084, S253]
lead: [S094, S032]
---
# When it breaks: what the agent needs from you

**Purpose (the first spoken sentence):** In this lesson you'll learn what your part is when something breaks, now that the agent reads the errors and fixes them itself.

**Conclusion:** The agent can debug anything it can run or see, so your part is a reliable way to make the problem happen, a clear picture of what correct looks like, and a way for it to observe the real result; when it keeps hitting the same wall, stop it and change what you give it instead of saying "fix it" again.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "When it breaks, you supply the eyes." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; 02 Your first build. Lesson 9 of the path, the moment a beginner first hits errors, so about 10 minutes by the course rule. It is the lesson design-decision.md grafted in so that Aaron's correction (nobody debugs by hand any more) has a shelf of its own. Lantern lesson.

**Lead source (audit, 2026-10-12):** S094 (Cursor); S032 (Aaron Orelup). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S094, S009, S003, S008, S032); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Teaching order: debugging moved to the agent (C019, points 1-2); it can only check what it can run or see (C003, points 1-2); so you give it a reproduction and the expected result (C019, points 3-7), and eyes, checked once against reality (C003, points 3-7); and when the loop stalls, you change the input (C042). The metaphor candidate: the agent is a mechanic who can fix anything on the bench under a light. Your job is to get the fault onto the bench (the reproduction), say how the machine should run (expected behaviour), and make sure the light works (eyes you've checked once).

### C019 Debugging moved to the agent; you supply the reproduction and the expected behaviour

1. **The agent runs the debugging loop now.** It reads the error, finds the code, patches it and re-runs. For hard bugs, Cursor's Debug Mode:
   - generates hypotheses;
   - adds targeted logging;
   - asks you to reproduce the bug while it collects data;
   - analyses the logs and makes a targeted fix.

   It can read the browser console, network requests and the page itself, and pull error reports from Sentry, production logs from Datadog, and data from the database over MCP (S094, re-opened 2026-10-12). **Depth: teach.**
2. **The change arc, in two lines.** Aaron, who made this course: "I haven't needed to debug an error myself since I started using claude code. It does it all itself." (S004, 2026-10-04). Stanford's Fall 2026 course for agent-era developers dropped the debugging weeks it taught in 2025 (S001). **Depth: brief.** Tell Aaron's line in the third person, as COURSE.md requires.
3. **Your two inputs:**
   - a reliable reproduction: "the exact steps, inputs, and conditions that trigger the issue";
   - the expected behaviour: what correct looks like.

   "If you can't reproduce the bug, you can't verify the fix." (S094) **Depth: teach.** This is the lesson's main habit.
4. **Reproduce it first, as a failing test.** In OpenAI's workflow, step 3 is "Reproduce the issue", and what it produces is an observed failure or a failing test (S008, slide 25, re-read 2026-10-12). GitHub's exercise: "A failing test is useful evidence, not a failed exercise step." (S009, step 3, re-read 2026-10-12). Claude Code's docs give the prompt: describe the symptom, then "write a failing test that reproduces the issue, then fix it" (S117). **Depth: teach.**
5. **Root cause, or a hidden symptom?** "The agent might add a null check that makes the error go away" while the bad data stays (S094). Ask why the value was missing in the first place. Tell it to "address the root cause, don't suppress the error" (S117). Aaron's AO-042 (S253, 2026-10-08) is the real case: for two months no video on his site could skip ahead, because the live asset server answered `200` instead of `206` while the local dev server handled ranges itself; the agent that finally measured it wrote a client-side workaround and a rule to fix the host first, and the cause stayed until Aaron asked for every feature to be checked. "An agent asked to build a feature fixes the feature. The thing underneath it gets a comment." (S253) **Depth: teach.** Tell it in the third person.
6. **An explanation is a hypothesis until evidence backs it.** Agents "can hallucinate plausible-sounding explanations", so check their conclusions against the data from the investigation (S094). GitHub's exercise keeps a suggestion only once it is tied to code, test output or a rule that must always hold, and says a convincing diagnosis explains both the failure and why the other tests passed (S009, steps 1 and 3). **Depth: brief.** Plausible-but-wrong as a general trap is taught in 02.04 (C005).
7. **Sometimes "what correct looks like" is a fact from the field.** In GitHub's bill-splitting exercise, rounding each person's share separately can lose or invent money. The fix keeps the total in whole cents and hands out the leftover cents one by one (S009, step 4). The agent won't volunteer a rule like that, so you or an expert must state it. **Depth: brief.**
8. **For hard bugs, try several models.** Run the same debugging brief across several models, keep the fix with the strongest evidence, and judge the reasoning as well as the answer (S094). **Depth: one line.**
9. **Production monitoring is now part of debugging:** error trackers and logs reach the agent over MCP (S094). **Depth: one line.** Watching live systems is 08.02's job.
10. **While you are learning, ask for the why.** While you are learning a technology you'll oversee, ask the agent to explain each fix and predict what could still fail (S084); in Anthropic's trial the biggest loss was in recognising wrong code, and the people who asked for explanations and conceptual questions kept it (S083). The agent still does the fixing. **Depth: one line.**
11. **The field hasn't fully moved.** GitHub's exercise of 2026-09-30 still has the learner write the first hypothesis (S009). **Depth: one line.** Mention it, for honesty.

### C003 An agent can only check what it can run or see: give it tests, a browser and eyes, then check the eyes

1. **"Tested" means "passed the check it had".** Aaron's AO-027 (S032, re-opened 2026-10-12), told in full only in this lesson (other lessons call back to it in one line; audit 2026-10-12):
   - On 2026-09-17 a chain of Opus 5 agents spent 8.5 hours building 16 animated wallpaper scenes.
   - The engine crashed while the third scene was being applied.
   - Scenes 4 to 16 were marked done as "NEVER APPLIED": 13 scenes logged done without ever running.
   - The only check they had was whether the program crashed.
   - The run cost $373 at API list prices, plus about 5 hours of Aaron's hand repair.

   **Depth: teach.** This is the lesson's story. Tell it in the third person.
2. **Read the report for blind spots.** Two agents wrote that they had no way to judge images, one that it had no screenshot tool. One wrote, "I haven't _looked_ at this scene — only confirmed it loads." (S032) Before accepting, ask which checks ran, which were skipped, and what is still unverified (S008). **Depth: brief.** Hand off to 02.04.
3. **Give it checks it can run:**
   - Put the exact commands for running the tests and starting the app where the agent reads them (S002).
   - Tests are the main way to verify agent output (S003).
   - "Give Claude a check it can run: tests, a build, a screenshot to compare." (S117)

   **Depth: teach.**
4. **Give it a browser.** In Stanford's 2026-09-29 lecture, Cursor by itself:
   - opened a browser;
   - made up test data;
   - uploaded it through the app's CSV form;
   - checked the result.

   The lecturer: "This wasn't true six months ago". If your agent lacks a browser, add one, such as Playwright MCP (S003, transcript lines 199-203, re-read 2026-10-12). **Depth: teach.**
5. **Give it eyes for output that isn't a web page.** Aaron's next tool, Wallpaper Breaker, has a first design rule: Claude must be able to see everything it makes. Its render tool turns any moment into an image, a contact sheet or a clip, and the pilot produced 319 review images (S032). **Depth: teach.** This is the "eyes" in the title.
6. **Check the eyes once against reality.** That is your move. The render tool's frame at 1.5 seconds matched the real engine's frame with a maximum pixel difference of 0, and a 25-layer recomposite came in at a mean error of 1.07 out of 255, against a target of 3 or less (S032). **Depth: teach.** Without this check, the agent's eyes could be lying to both of you.
7. **Eyes catch what no other check sees.** The render check found a rain effect sized in pixels where the engine expected fractions of the screen, so the rain spread over roughly 90,000 times the canvas (S032). **Depth: brief.**
8. **Prefer evidence the agent can't fake.** Willison built tools that insert real command output into a demo document, drive a browser for screenshots, and record video of a feature in use, because he had seen agents edit a demo file by hand (S090, S091). **Depth: one line.** Evidence from outside the agent is taught in 06.02.
9. **Screenshots have a destination.** Evidence screenshots show whatever was on screen, and agents short of a private upload path have published them (S227). **Depth: one line.** Taught in 07.03.
10. **A behaviour check is not a quality review.** The browser run proves the feature works; speed, readability and security still need review (S003). **Depth: one line.** Hand off to 02.04 and 04.01.

### C042 When progress stalls, diagnose and change the input

1. **Normal versus stuck.** The agent reading and fixing its own errors is normal. When the same error keeps coming back, or each fix undoes the last, it is stuck. Anthropic's docs list "Correcting over and over" as a common failure (S117). **Depth: teach.**
2. **"Fix it" on repeat goes with inexperience.** In a survey of 162 vibe coders, less experienced ones, and non-developers most of all, re-prompt instead of investigating, and they report more breakdowns (S085). A companion study names the "Death Spiral", a loop that makes no progress despite the user's corrections (S096). **Depth: brief.**
3. **Name the failure, then change the input** (S008, slide 28, re-read 2026-10-12):

   | Failure | What you see | Try this (paraphrased) |
   |---|---|---|
   | Missing context | it guesses about files or project rules | "Read [file] and explain the relevant constraints before editing." |
   | Scope drift | changes spread beyond the goal | "Pause. Keep only [scope]. List extra work as separate follow-ups." |
   | Failed checks | a test or expected behaviour still fails | "Reproduce the failure. Fix the cause and rerun [check]. Report the result." |

   When quality still falls short: add files or examples, raise the effort, or try a stronger model against the same checks (S008, slides 16-19). **Depth: teach.** This is the lesson's second habit.
4. **Name the machine property behind odd output** (S006):
   - a made-up fact means you hit a knowledge limit, so bring sources;
   - an ignored instruction means you need a shorter, concrete, checkable one;
   - a forgotten detail means the context needs shrinking or restarting.

   **Depth: brief.**
5. **The two-strikes rule.** If you've corrected it more than twice on the same issue, the conversation is cluttered with failed attempts: run `/clear` and start fresh with a better prompt that includes what you learned (S117). Restarting helps only if the prompt changes (S008). **Depth: teach.**
6. **Stop it early.** `Esc` stops the agent and keeps the context; `Esc Esc` or `/rewind` goes back. Rewind doesn't undo changes made through shell commands, and it doesn't replace git (S117, S178). **Depth: brief.**
7. **Cap loops before they start.** Give exit criteria or a limit on fix-and-recheck rounds (S008). In AO-027, "never applied" was logged 13 times and nothing in the plan said to stop (S032). **Depth: brief.** Stop rules for long runs are 08.01's job.
8. **Fix it for next time.** A correction you keep repeating is a missing rule, test or hook (S036, S116). **Depth: one line.** Taught in 05.02.
9. **Escalate when the problem is beyond you.** Expertise is one of the reasons to bring a person in, because AI is uneven and lags experts on parts of tasks (S068). Don't rely on answers you can't verify (S004). **Depth: one line.** Bringing in an expert is 04.04's job.

## You vs the agent

As of 2026-10-12:
- **The agent:**
  - reads errors and traces, forms hypotheses, adds logging;
  - reads browser, network and monitoring data, and reproduces the bug in a browser;
  - writes the failing test and the regression test, fixes and re-runs.

  Those steps are verifiable, so they are the agent's job (S094, S003, S008, S004). It can only check what it can run or see, and it will report "done" against whatever check it had, even "didn't crash" (S032).
- **You:**
  - give an exact reproduction and say what correct looks like;
  - reproduce the bug yourself when only you can see it;
  - before a long run, ask what the agent can actually observe, and give it a test, a browser or a render tool;
  - check that tool once against reality;
  - ask for the root cause and for before-and-after evidence;
  - notice when the loop has stalled, stop it, name the failure and change the input.

  You also keep the judgment of taste and mood (S094, S009, S032, S008, S117).
- **Bring in an expert or an independent tool (C118):**
  - when you can't say what correct is (a money rule, a physics constraint, a domain standard);
  - when the cause sits in a field you can't judge (security, unfamiliar infrastructure);
  - when no tool you have can observe the result.

  (S009, S068, S029)

## Sources this lesson is built from

- S094 — Cursor (Cursor Learn), "Finding and fixing bugs" (undated; first archived 2026-02-16, revised by 2026-09-02) https://cursor.com/learn/finding-fixing-bugs — how agents debug now, the human's reproduction and expected behaviour, "If you can't reproduce the bug, you can't verify the fix", the null-check symptom, plausible-but-wrong explanations, several models in parallel, monitoring over MCP. Re-opened 2026-10-12.
- S009 — GitHub (GitHub Skills), "Test and Debug with GitHub Copilot" (created and last committed 2026-09-30) https://github.com/skills/test-and-debug-with-github-copilot — evidence before edits, the failing test as evidence, a diagnosis must explain why the other tests passed, the whole-cents rule, and the human-written hypothesis. Step files re-read 2026-10-12.
- S003 — Mihail Eric, Stanford CS146S, lecture of 2026-09-29 (transcript) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — the agent opening a browser to test its own feature, "This wasn't true six months ago", adding Playwright MCP, and tests as the main check. Lines 199-203 re-read 2026-10-12.
- S008 — OpenAI Academy (Stallworth, Wride, Chakkirala), "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — "Reproduce the issue" as a workflow step, "When progress stalls, change the input" with its three named failures, effort and model adjustments, capping rounds. Deck re-read 2026-10-12. The slides are marked confidential although publicly linked, so paraphrase and redraw them with credit.
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/ — "tested" meaning "didn't crash", the 13 scenes marked done, $373, the eyes rule, the render tool checked to a pixel difference of 0, the rain bug, "never applied" 13 times. Re-opened 2026-10-12.

Also cited for single points (credit on the lesson page):
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — Aaron's "I haven't needed to debug an error myself" line, and the rejected five-step routine. Re-opened 2026-10-12.
- S117 — Anthropic (Claude Code docs), "Best practices for Claude Code" (undated; names v2.1.283; re-opened 2026-10-12) https://code.claude.com/docs/en/best-practices — give it a check it can run, failing test first, root cause not suppression, "Correcting over and over", the two-strikes `/clear` rule, `Esc` and `/rewind`.
- S001 — Mihail Eric, Stanford, "CS146S: The Modern Software Developer" syllabus (Fall 2026 term began 2026-09-22) https://themodernsoftware.dev/ — the debugging weeks dropped.
- S002 — Mihail Eric, Stanford CS146S, lecture of 2026-09-24 (transcript) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — the test and run commands go in the instruction file.
- S085 — Ahmed Fawzy, Amjed Tahir, Kelly Blincoe, "From Prompting to Verification: How Experience Shapes Vibe Coding Practices" (2026-05-23) https://arxiv.org/abs/2605.24521 — re-prompting versus investigating, by experience.
- S096 — Christopher Potts, Moritz Sudhof, "A Paradox of AI Fluency" (2026-04-28; chat data from 2023-2025) https://arxiv.org/abs/2604.25905 — the "Death Spiral".
- S083 — Shen and Tamkin (Anthropic), "How AI assistance impacts the formation of coding skills" (2026-01-29) https://www.anthropic.com/research/AI-assistance-coding-skills — the learner's debugging caveat.
- S006 — Anthropic Academy, "AI Capabilities and Limitations" (undated; live by April 2026) https://anthropic.skilljar.com/ai-capabilities-and-limitations — naming the machine property.
- S090 — Simon Willison, "Introducing Showboat and Rodney, so agents can demo what they've built" (2026-02-10) https://simonwillison.net/2026/Feb/10/showboat-and-rodney/ — and S091, "Have your agent record video demos of its work with shot-scraper video" (2026-06-30) https://simonwillison.net/2026/Jun/30/shot-scraper-video/ — evidence the agent can't hand-edit.
- S227 — Hive Security, "PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub" (2026-10-02) https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/ — screenshots have a destination (one line).
- S178 — Anthropic (Claude Code docs), "Checkpointing" (undated) https://code.claude.com/docs/en/checkpointing — rewind skips shell changes.
- S036, S116, S068, S029 — one-line points as cited above (entries in sources.md).

Added by the 2026-10-12 audit (credit on the lesson page):
- S253 — Aaron Orelup, "AO-042: For two months no video on my site could skip ahead, and the agent that noticed wrote a workaround" (2026-10-08) https://aaronorelup.com/ledger/every-video-can-seek/ — root cause versus a hidden symptom (C019 point 5). Read 2026-10-12.
- S084 — Addy Osmani, "Agentic Skill Decay" (2026-08-31) https://addyosmani.com/blog/agentic-skill-decay/ — predict what could still fail (C019 point 10).

## Show it for real

- In a small demo repo, break one function so a test fails. Let the agent read the trace, fix the code and re-run until green with no human typing code. Proves the loop belongs to the agent (C019).
- Ask the agent to reproduce a reported bug as a failing test first. Show it red, let it fix, show it green, then revert the fix and show the test go red again. Proves a reproduction is evidence (S008, S009, S117).
- In Cursor's Debug Mode, or Claude Code with a browser tool, describe an intermittent bug with exact steps. Let the agent add logging, reproduce the bug yourself when it asks, and show it read the console and network tab before it fixes. Proves your part is the reproduction (S094).
- Ask an agent with a browser tool to add a small form feature, and record it opening the page, filling the form and screenshotting the result. Proves it can see a web app (S003).
- Aaron's real AO-027 artifacts: the "NEVER APPLIED" lines in the notes file, then a contact sheet from the render tool. Proves "tested" meant "didn't crash" (S032).
- Diff one render-tool frame against a real screen capture of the same moment and show a maximum difference of 0. Proves what "check the eyes once" means (S032).
- Show a terminal where the same error comes back across three attempts. Press `Esc`, give the stall-type instruction ("Reproduce the failure, fix the cause, rerun the test, report") or add the missing file, and show the next run break the loop. Proves "change the input" (S008, S117).
- Press `Esc Esc` to open the rewind menu, and restore code from before the loop started (S117).
- Show an agent fix that adds a null check, then ask "why was it null?" and have it pull the data that shows the real inconsistency. Proves root cause versus symptom (S094).
- Use demo projects only; no real keys, customer data or personal accounts on screen.

## Questions this lesson answers

- Do I still need to learn debugging? What do I do when the AI is stuck on an error? (courses-teach-now #18, logged in C019)
- My AI builder keeps saying it fixed my workflow, but it's still not working. How do I check? (S086, an n8n community thread, 2026-06-08)
- The app breaks sometimes, but I can't say why. What do I tell the agent? What is a reproduction? (vendor-academies #10, in C019)
- Why does the same bug keep coming back? What is a regression test? (vendor-academies #11, in C019)
- The agent keeps going in circles. What do I do? Should I start a new chat? When should I stop it? (S008, S085)
- Can the AI test the website itself? How do I let it use a browser? (S003)
- How do I let the agent check its own visual output? Can I trust the screenshots it takes? (S032, S227)
- Why did it say it was done when the thing never even ran? (S032)
- Why did it make up a reason? Why did it ignore my instruction? Why did it forget what I said earlier? (S006)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- "Done" as a claim, the three questions before accepting, and plausible-but-wrong explanations (C005, C011) → done-is-a-claim
- Agent-written tests not being independent; the revert check; evidence from outside the agent; verifying the verifier (C012, C013, C017) → checking-what-you-cant-read
- Turning repeated corrections into rules, tests and hooks (C047) → rules-it-reads-rules-it-cant-break
- Why long conversations degrade, and `/clear` (C026, C027) → what-the-agent-sees-each-turn
- Stop rules, budgets and checkpoints for long unattended runs (C096) → agents-that-run-while-youre-away
- Watching live systems from outside (C102) → green-is-not-success
- Bringing in an expert (C118) → before-you-ship-who-signs-off
- Evidence screenshots leaking (C084) → the-narrowest-keys-and-verbs
- Link checkers and checking research (C107) → checking-research-numbers-and-parts
- Media the agent can't see or hear without a tool (C032) → making-media-with-ai
- What raising the effort or switching models costs (C058, C059) → know-your-meter
- Undo limits for shell commands → before-you-let-it-loose (taught there) and from-your-laptop-to-a-url

## Out-of-date framings to avoid

- "Read the error, search the exact message, read the docs, then ask AI", and "learning to debug is the first skill". This course's own first draft of 00.06 taught this five-step routine, and Aaron sent it back (S004, S001).
- "Read the stack trace and debug line by line yourself" (S094).
- "Paste the error and accept whatever fix comes back" (S094).
- "It works on my machine now, so it's fixed": the symptom vanished once (S008).
- "The agent tested it", and "no crash means it works" (S032).
- "The AI can't see or use the app it built" (S003).
- "The AI can't see images, so I have to check every output myself forever" (S032).
- "Just keep telling it to fix it" (S085, S117).
- "Start a new chat and paste the same prompt" (S008, S117).
- "AI output is random; if it's wrong, just regenerate" (S006).

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 ("Trust what you can verify"), scene 03, says in one scene that agents now fix their own errors, and quotes Aaron. curriculum.md moves debugging to this lesson (C019). The rejected first draft of 00.06, with its hand-debugging routine, is the reason this lesson exists (S004). Nothing from that draft should come back.
