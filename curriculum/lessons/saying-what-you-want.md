---
key: saying-what-you-want
id: 02.02
title: Saying what you want
district: First Build
module: 02 Your first build
status: todo
legacy: []
minutes: 12
concepts: [C033, C034, C035, C036, C038]
sources: [S037, S034, S008, S036, S081, S033, S117, S030, S098, S115, S029, S080, S084, S119, S031, S022, S007, S118, S121, S083, S116, S004, S005, S006, S009, S027, S032, S010]
lead: [S037, S034]
---
# Saying what you want

**Purpose (the first spoken sentence):** In this lesson you'll learn what your job is now that an agent writes and fixes the code: saying what you want clearly enough that it builds the right thing.

**Conclusion:** A current agent will grind its way to almost any goal you state clearly, so most failures now start in what you asked for; write the goal, the constraints and a checkable "done when", and have the agent show you what you don't know and what it is assuming before it builds.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; 02 Your first build. Lesson 8 of the path, in the middle of the module, so about 10 minutes by the course rule. It is set to 12 because it carries five concepts (design-decision.md lists it among the dense lessons). Lantern lesson. Requires C117 and C122 (01.02, 01.03), both taught earlier on the path.

**Lead source (audit, 2026-10-12):** S037 (Thariq Shihipar (Anthropic)); S034 (Thorsten Ball). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S037, S034, S008, S036, S081); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Teaching order: the job moved (C033), so the inputs are yours (C034), but you can only state what you know (C035), so let the agent show you the territory first (C036), then write the brief with a finish line (C038). The metaphor candidate is S037's map and territory: your prompt is the map, the codebase and the real world are the territory, and every gap between them is a place where the agent guesses.

### C033 The job moved from typing code to directing agents

1. **When it changed.** In November 2025, Claude Opus 4.5 and GPT-5.1, inside their coding harnesses, went from "often make mistakes" to "reliable enough to use on a day-to-day basis" (S033, re-opened 2026-10-12). **Depth: one line.** Put the date on screen.
2. **Three phases, and the loop you now direct.** OpenAI's bootcamp names the phases: suggest the next line, chat while coding, delegate the whole task (S008, slide 5). In delegation the agent runs a loop:
   1. Prompt: you set the goal, context, constraints and done criteria.
   2. Inspect: it reads the relevant files.
   3. Act: it edits and runs commands.
   4. Validate: it runs checks and fixes failures.
   5. Report: it summarises the changes, the evidence and the remaining risks.

   The human inspects the evidence, then accepts, asks for fixes, or stops (S008, slide 7, re-read 2026-10-12). **Depth: teach.** This is the frame for the rest of the lesson.
3. **How many developers already work this way.** JetBrains surveyed over 15,000 professional developers in May to July 2026 (S081, re-opened 2026-10-12):
   - On average about 47% of their code was fully written by agents, about 38% with AI assistance and about 27% by hand.
   - Say on screen that these are self-reported averages from answer buckets, which is why they add up to more than 100%.
   - Over half write less than 20% of their code by hand.
   - About 22% generate more than 80% of it with agents.
   - Seniors moved to agents first.

   **Depth: brief.**
4. **Delegation is not total.** Most of Anthropic's own engineers could fully delegate only 0-20% of their work; the rest still needs active supervision (S029). **Depth: one line.** Do not use the Stack Overflow "18.9% delegate changing production" figure: it was not re-found on 2026-10-12 (G01 notes, and this spec's re-check of S080).
5. **The skills that are yours now:** deciding what is worth doing, specifying the outcome, steering mid-flight, and verifying, meaning deciding when the evidence is enough (S084). The share of code humans type falls, but ownership doesn't (S115). **Depth: brief.**
6. **The command syntax belongs to the agent.** Thorsten Ball goes further: "The terminal is dead", and nobody needs to know command-line flags any more. He is a self-described lover of the terminal, and these are his beliefs about the future, not measurements (S034, re-opened 2026-10-12). What a beginner needs is the concept, which 01.02 and 01.03 teach. **Depth: one line.** Label it as a prediction.
7. **Do real work in an agent, not a chat window.** Copying code and errors between a chatbot and your editor is the slow pre-agent workflow (S116, S005). **Depth: one line.**

### C034 You supply the goal, the constraints and the tools; most bugs become "you asked for the wrong thing"

1. **The three inputs.** Willison: a current top model can solve your problem by brute force if you "clearly define the goal", give it unambiguous constraints and give it access to the tools it needs. He adds that this is "kind of what software engineering is" (S033, re-opened 2026-10-12). **Depth: teach.** This is the lesson's spine.
2. **Your clarity is now the limit.** Shihipar, at Anthropic: Claude Fable is the first model where "the quality of the work is bottlenecked by my ability to clarify its unknowns" (S037, re-opened 2026-10-12). **Depth: teach.**
3. **Bugs move upstream.** Ball predicts most bugs won't be "coding" bugs; they'll be "you asked for the wrong thing" bugs (S034). It is a prediction, so label it as one. **Depth: teach.**
4. **The wrong thing can pass every check.**
   - The requirement was "refund only after a successful capture". The model built "refund if a payment record exists", and the implementation, the tests and an AI review all stayed green (S030, re-opened 2026-10-12).
   - Asked to add GitHub sign-in, an agent dropped another sign-in provider that customers wanted, because the screen had room for only three (S115).

   **Depth: teach** one example on screen (the refund case), and give the other one line.
5. **Specificity cuts both ways.** Too specific, and the agent follows your instructions even when a change of course would be better. Too vague, and it falls back on generic industry practice that may not fit (S037). Instructions written for older models can over-constrain newer ones (S022). **Depth: brief.**
6. **When the output is wrong, first ask "what did I not say?"** The agent repairs code errors itself, but it can't infer a requirement nobody stated. "Claude can infer intent, but it can't read your mind": name the files, the constraints and an example to follow (S117, re-opened 2026-10-12). **Depth: teach.**
7. **Polished output hides the decision it made for you** (S118, a practitioner's judgment, not a measurement). **Depth: one line.**
8. **Choosing the goal is where models are weakest** (S029). Tasks with an automatic score race ahead; tasks without one lag (S027). **Depth: one line.**

### C035 Your unknowns and unwritten context limit the agent

1. **Map and territory, and four kinds of unknowns** (S037):
   - known knowns: what you tell the agent;
   - known unknowns: what you know you haven't worked out;
   - unknown knowns: too obvious to write down, but you'd recognise them on sight;
   - unknown unknowns: what you haven't considered at all.

   At each unknown, the agent guesses. **Depth: teach.** This is the metaphor.
2. **Tell it where you're starting from:** where you are in your thinking, your experience with the problem, and how well you know the codebase (S037). **Depth: brief.**
3. **Context lives in people's heads, even for professionals.** Stack Overflow 2026 (S080, figures re-found 2026-10-12 on the Knowledge pages):
   - information is incomplete (63.2%), lives in people's heads (60.9%) or is outdated (56.5%);
   - about 79% at least sometimes discover important context only after starting or finishing a task;
   - only 19.7% count compliance, security or policy requirements among the context they need.

   **Depth: brief.** Use one figure on screen.
4. **The repo isn't the whole system.** Osmani: as soon as an agent drops code you didn't decide line by line, you're in a "brownfield" project, and the repository is no longer a complete description of how the thing behaves (S036, re-opened 2026-10-12). What the code can't say has to come from people: owners, the history behind odd code, what production really does. **Depth: brief.**
5. **Write down what the code can't say, and nothing else** (S036): business nuance, the trade-offs behind the structure, guidelines no tool enforces, domain rules, and the history behind code that looks wrong. Bloated instruction files get ignored (S117). **Depth: brief.** Instruction files themselves are taught in 05.02.
6. **Ask it to surface its assumptions.** Ask in so many words: "Push back if my assumptions are wrong", and "Tell me what you're uncertain about" (S119). Agents should state assumptions and signal uncertainty (S031). While it works, ask what it ruled out and what it assumed (S084). **Depth: teach.**
7. **Every session starts from zero** (S084, S031). **Depth: one line.** What a session sees is 05.01's job.
8. **Name the constraints nobody lists:** security and privacy rules (19.7%, S080), and who decides which libraries the project uses (S004). **Depth: one line.** Stating the security stakes is taught in 04.01.

### C036 Let the agent teach you the territory first: the blind-spot pass

1. **When to run it:** before you work in an unfamiliar part of the code or an unfamiliar field, when you don't know what to ask, what good looks like, or where the potholes are (S037). **Depth: teach.**
2. **How to ask:** say "blind spot pass" and "unknown unknowns", and say what you know. S037 gives two examples (S037):
   - someone who knows nothing about a codebase's sign-in modules, before adding a new sign-in provider;
   - someone grading a launch video who doesn't know what colour grading is.

   **Depth: teach.** Show one of them.
3. **Let it interview you.** Shihipar asks Claude to question him one question at a time, putting first the questions whose answers would change the design (S037). Claude Code's docs give a ready prompt: interview me in detail, write the spec to `SPEC.md`, then start a fresh session to build it (S117). **Depth: brief.**
4. **Ask it what you'd ask a senior engineer:** how logging works here, which edge cases this flow handles, why this call and not that one (S117). **Depth: one line.**
5. **Keep learning on.** Claude Code's Explanatory and Learning output styles explain choices or leave decisions for you to make (S121). In Anthropic's randomised trial, people who asked conceptual questions kept their learning and were nearly as fast as those who delegated everything (S083). **Depth: one line.**
6. **Know its limits.** The pass teaches you enough to prompt and to judge; it doesn't make you the expert. Models are weakest on rare, recent or niche topics, so bring sources there (S006). Sign-in, billing and permissions still need someone who can verify (S036, S004). **Depth: one line.** Bringing in an expert is 04.04's job.
7. **Close the loop:** turn the list of unknowns it gives you into a better prompt (S037). **Depth: one line.**

*Note: C036 is should-priority, and its own entry says to teach it inside this lesson, not as a lesson of its own.*

### C038 Define done before you delegate

1. **The four-part brief: Goal, Context, Constraints, Done when.** OpenAI's example (S008, slide 13, re-read 2026-10-12):
   - Goal: change a savings rate shown as 4.02% to the approved 4.20%.
   - Context: find where the homepage value comes from, and the relevant tests.
   - Constraints: keep the change small; leave unrelated work alone.
   - Done when: a regression test is added, the checks run, and the evidence is reported.

   The slide's headline is "A good prompt defines done." Point out that "the approved 4.20%" is a fact only the human has. The presenters add that without a definition of done the model invents its own finish line (S008, talk at 36:01, from the batch reader's caption read). **Depth: teach.**
2. **Write the acceptance criteria from the user's need, before the code**, not from what the AI produced (S007). Make them checkable, include what is out of scope, and approve the test names before the agent builds (S030). **Depth: teach.**
3. **Name the failure you fear.** In one team's log, adding to the brief that tests must fail without the change moved a job from 1 of 3 real tests to 3 of 3, for about five extra seconds (S030, S098). **Depth: brief.**
4. **Give it a check it can run:** example cases, a build, a screenshot to compare. "Without a check it can run, 'looks done' is the only signal", and then "you become the verification loop" (S117). **Depth: teach.** Hand off to 02.03.
5. **Say that running, inspecting and fixing are part of the task.** OpenAI warns that GPT-6 Astra may otherwise stop for review after a first implementation (S022). **Depth: one line.**
6. **Put stop rules in the brief:**
   - implement only the stated criteria;
   - if a check can't run, stop and say why;
   - list any decision a human still has to make;
   - don't merge (S115).

   Also cap the rounds of fix-and-recheck (S008). **Depth: brief.**
7. **Keep it human-sized:** what you're building, what it must not break, and how you'll know it worked. It needn't be long; it's where your judgment goes now (S029). **Depth: one line.**
8. **Name what the agent can't verify** (does it look right, is it secure) and plan who checks it (S032, S004). **Depth: one line.** Hand off to 02.04 and 04.01.

## You vs the agent

As of 2026-10-12:
- **The agent** reads the project, maps unfamiliar code, explains the territory, interviews you and lists your unknowns. It drafts specs and acceptance criteria when asked. It builds, runs, fixes and iterates toward whatever check it has, and it reports what it assumed when asked (S033, S037, S117, S008).
- **You:**
  - decide what is worth building;
  - supply the facts only you have (the approved number, the business rule, who the users are, what must never happen);
  - write or approve the goal, the constraints, the "done when" and the test names;
  - say what you don't know and ask the agent to surface its assumptions;
  - when the result is wrong, ask "what did I not say?" before assuming a code bug.

  (S008, S030, S034, S037)
- **Bring in an expert (C118):**
  - when you can't state a field's rules yourself. GitHub's exercise shows one the agent won't volunteer: rounding each share of a bill separately loses or invents cents (S009).
  - for sign-in, payments and permissions, where the pass gives you vocabulary, not verification (S036, S004).
  - for knowledge that lives in other people (legacy owners, compliance, whoever decides which libraries the project uses), which has to come from them (S036, S004).

## Sources this lesson is built from

- S037 — Thariq Shihipar (Anthropic), "A field guide to Claude Fable 5: Finding your unknowns" (2026-07-06) https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns — map and territory, the four kinds of unknowns, the "bottlenecked" line, specificity both ways, telling it your starting point, the blind-spot pass, the interview. Re-opened 2026-10-12.
- S034 — Thorsten Ball, "What I believe about the future of software development" (2026-09-19) https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/ — "you asked for the wrong thing" bugs, and "the terminal is dead", both as predictions. Re-opened 2026-10-12.
- S008 — OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala), "Codex Bootcamp 101: Agentic coding" livestream and slide deck (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — the three phases, the Prompt-Inspect-Act-Validate-Report loop, and the Goal-Context-Constraints-Done-when brief. The deck text was re-read on 2026-10-12. Its slides are marked "Confidential and proprietary" although the deck is publicly linked, so paraphrase them and redraw the content with credit; don't show the slides themselves.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — every agent-written project is brownfield, the repository is not the whole system, and write down what the code can't say. Re-opened 2026-10-12.
- S081 — Mikhail Bogdanov (JetBrains Research), "How Much Code Do Developers Really Let Agents Write?" (2026-08, from the URL; the page shows no day) https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/ — the 47 / 38 / 27% split with its caveat, the over-half and 22% figures, seniors first. Re-opened 2026-10-12.

Also cited for single points (credit on the lesson page):
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — the November 2025 threshold, and the goal-constraints-tools definition. Re-opened 2026-10-12.
- S117 — Anthropic (Claude Code docs), "Best practices for Claude Code" (undated; names v2.1.283; re-opened 2026-10-12) https://code.claude.com/docs/en/best-practices — "can't read your mind", the interview prompt, the senior-engineer questions, "you become the verification loop", short instruction files.
- S030 — Remy (redreamality.com), "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — the refund case; humans own acceptance criteria; naming the failure mode. Re-opened 2026-10-12.
- S098 — rayson-tech, "nomArmy findings" (data to 2026-10-04) https://github.com/rayson-tech/nomarmy/blob/main/docs/findings.md — the 1-of-3 to 3-of-3 brief change (via S030).
- S115 — Addy Osmani, "Human judgment doesn't leave the software factory. It relocates." (2026-08-21) https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/ — the dropped sign-in provider, stop rules, ownership.
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — 0-20% fully delegated; human-sized done; goal choice.
- S080 — Stack Overflow, "Developer Survey 2026" (released 2026-10-06; fieldwork 2026-06-23 to 08-05) https://survey.stackoverflow.co/2026/ — the context figures (re-found 2026-10-12 on the Knowledge pages).
- S084 — Addy Osmani, "Agentic Skill Decay" (2026-08-31) https://addyosmani.com/blog/agentic-skill-decay/ — the four skills; ask what it assumed; sessions start from zero.
- S119 — Swanson, Bent, Ludwig, Dakan, Feller (Anthropic), "Anthropic Education Report: The AI Fluency Index" (2026-02-23) https://academy.claude.com/tutorials/the-ai-fluency-index — "Push back if my assumptions are wrong".
- S031 — Wang, Yang, Lieret et al., "Humans are Missing from AI Coding Agent Research" (2026-07-04) https://arxiv.org/abs/2608.12355 — agents should surface their assumptions.
- S022 — OpenAI, "Rethinking skills and prompts for GPT-6 Astra" (undated; no earlier than 2026-09-03) https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra — over-constraining; saying that running and fixing are part of the task.
- S007 — Anthropic Academy and CodePath, "AI Fluency for Builders" (2026-09-29) https://www.coursera.org/learn/ai-fluency-for-builders — acceptance criteria from the user's need.
- S118 — Gabriel Martinez (G2i), "Generation Is Cheap, Review Is Expensive" (2026-10-09) https://ai.engineer/talks/6qkzlT962es — polish hides decisions (his judgment).
- S121 — Anthropic (Claude Code docs), "Output styles" (undated; names v2.1.237) https://code.claude.com/docs/en/output-styles — the Explanatory and Learning styles.
- S083 — Judy Hanwen Shen and Alex Tamkin (Anthropic), "How AI assistance impacts the formation of coding skills" (2026-01-29; foundational and still current) https://www.anthropic.com/research/AI-assistance-coding-skills — conceptual questions keep learning.
- S116 — Mitchell Hashimoto, "My AI Adoption Journey" (2026-02-05) https://mitchellh.com/writing/my-ai-adoption-journey — work in an agent, not a chat window.
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — the dependency list nobody owns; questions you can't verify.
- S005, S006, S009, S027, S032 — one-line points as cited above (entries in sources.md).

## Show it for real

- On the same small repo, run "fix the homepage", then the four-part brief (goal, context, constraints, done when). Put the two diffs and the two final reports side by side. Proves the brief changes what comes back (S008).
- Give a one-line feature request and let the agent build it. Then reveal a rule the "user" assumed but never said ("only admins can delete") and show the agent fix it within a minute of being told. Proves the gap was in the ask, not the code (C034 demo).
- In an unfamiliar open-source project, type a blind-spot-pass prompt ("I know nothing about the sign-in modules here; do a blind spot pass for my unknown unknowns"). Show the list of unknowns it returns, then the sharper prompt built from it (S037).
- Paste Claude Code's interview prompt and answer three of its questions on screen, ending with a `SPEC.md` the agent wrote. Proves the agent can pull your unknowns out of you (S117).
- Make the same request in a fresh session with no project notes, then with a five-line project file (the goal, one privacy rule, one past decision). Show both outputs. Proves unwritten context is what was missing (C035 demo).
- An animated walk-through of the refund case: requirement, build, tests and review all green, behaviour wrong. A drawn scene, not a recording (S030).
- Use a demo repo with no real keys or personal data in any frame.

## Questions this lesson answers

- Do I still need to write code myself? What is my job if the agent writes everything? (S008)
- Is AI actually good at writing code now, or is that hype? Do professional developers really let AI write their code? Am I cheating if the agent writes everything? (S033, S081)
- What do I actually need to tell the agent? Why did it build something that works but isn't what I wanted? (S033, S037)
- The AI did exactly what I said, so why is it wrong? Why does the agent keep making assumptions? (S034, S037)
- Why do I have to re-explain my preferences every session? (S031)
- How do I tell the AI what I want when I don't know the field? How do I start in a part of the code I don't understand? (S037)
- How do I write a good prompt for an agent? How does the agent know when to stop? What should I write before I start? (S008, S030)
- Do I need to learn the command line? (S034)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Agents testing their own work, and what to do when it breaks → when-it-breaks-you-supply-the-eyes
- Accepting the result on evidence; "done" as a claim → done-is-a-claim
- Cheap mockups first, mapping before changing, specs scaled to the task, slicing (C037, C039-C041) → plan-first-then-build-in-slices
- Instruction files (CLAUDE.md, AGENTS.md) and turning repeated corrections into checks → rules-it-reads-rules-it-cant-break
- What each session sees and why it starts from zero → what-the-agent-sees-each-turn
- Stating security stakes the agent won't assume (C064) → working-is-not-secure
- Bringing in an expert (C118) → before-you-ship-who-signs-off
- Deciding what is worth building, and keeping the judgment you need (C043, C010) → idea-to-launch-end-to-end
- Who owns the dependency list (C053) → after-launch-keep-it-alive
- Model versus harness → model-harness-and-memory
- Effort settings and model choice → know-your-meter

## Out-of-date framings to avoid

- "AI coding is autocomplete, or pasting snippets from a chat window" (S008, S033, S116).
- "Prompting is about magic phrasing", and its opposite, "prompting is dead; describe the vibe and keep asking until it looks right" (S033, S008).
- "Better models need less direction." The better model is what makes your unknowns the bottleneck (S033, S037).
- "The more detail in the prompt, the better" (S037, S022).
- "The AI knows my project" and "it remembers what I told it last week" (S080, S084, S031).
- "Put a markdown file for everything into context." Osmani calls this a passing habit, and bloated files get ignored (S036, S117).
- "Pretend to know the field and prompt confidently", or "ask for several variations and pick one" when you can't tell which is good (S037).
- "Make it stop for review after every step" (S022).
- The overclaim "agents do everything now" (S029).
- "Memorise command-line flags" as a beginner requirement. That rests on a prediction (S034).
- Beginner courses that teach a prompt as goal, input, output, layout and features, with no "done when" and no check (S010, Andrew Ng's no-code course).

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 ("Trust what you can verify"), scene 03, carried a short "the job moved" arc (autocomplete, then pasting into chat, then agents that fix and re-run). curriculum.md moves that segment here (C033). That scene's code-share figures (Google, Anthropic) are not among this lesson's sources, so don't reuse them; use S081 with its caveat instead.
