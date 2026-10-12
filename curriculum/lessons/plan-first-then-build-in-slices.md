---
key: plan-first-then-build-in-slices
id: 06.01
title: Plan first, then build in slices
district: Directing Well
module: 06 Scaling up
status: todo
legacy: []
minutes: [5, 6]
concepts: [C037, C039, C040, C041]
sources: [S003, S036, S117, S118, S037, S008, S031, S030, S024, S035, S002, S119, S004, S001, S068, S082, S085]
lead: [S003, S036]
---
# Plan first, then build in slices

<!-- minutes: [5, 6] since the 2026-10-12 audit applied COURSE.md's ~5-minute rule for a module's first lesson; see the Length line below. -->

**Purpose (the first spoken sentence):** In this lesson you'll learn how to take on anything bigger than a one-sentence change: find out what you want cheaply, have the agent map what is already there without touching it, choose between two options and approve a short plan, then build it in pieces small enough to check.

**Conclusion:** Agents made trying cheap and choosing expensive, so on a big change your job is to pick the direction from evidence and keep every piece small enough that you can still judge it.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; Module 06 Scaling up, lesson 1 of 3 (the scaling-up module opens here; 06.02 is how you check the slices, 06.03 what they cost).

**Lead source (audit, 2026-10-12):** S003 (Mihail Eric, Stanford CS146S); S036 (Addy Osmani). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S003, S036, S117, S118); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

**Length (audit, 2026-10-12):** about 5-6 minutes; COURSE.md (Aaron, 2026-10-01) gives orientation lessons and the first lesson of every module about 5 minutes. Cut C037 and C039 to their brief points only (this spec's own cut list), and make C039 point 4 (the risk map) a one-line callback to working-is-not-secure, which teaches the same zone map (C007 point 2). C040 point 5 and C041 points 4 and 5 drop to one line each. Every other point marked brief becomes one line, and every point marked one line moves to the lesson page.

Order in the lesson: the size rule first (C040 point 1), then the cheap-discovery moves (C037), the read-only map (C039), the plan (rest of C040), and the slices (C041). One metaphor should carry it; the planner chooses it.

### C040 Spec before code, scaled to the task

1. **Scale the process to the size of the task.** Anthropic's rule of thumb: "If you could describe the diff in one sentence, skip the plan." Plan when you are unsure of the approach, when the change touches several files, or when you don't know the code (S117). The Stanford lecturer's ladder: a copy change or small fix, just ask; a small feature across several files, start with a plan; a medium feature, big refactor or migration, several rounds of research, proposals and planning in separate sessions; a very large project, split into issues with one agent per issue, stacked so each builds on the last (S003). Depth: **teach**.
2. **The five steps: research, propose, plan, implement, test** (Stanford CS146S, lecture of 2026-09-29; S003). Research documents only what exists, with no suggestions. Propose asks for two different options, each with trade-offs, validation and open questions; the lecturer has "seen diminishing returns beyond two" (S003). Say the five steps aloud rather than the acronym: the lecture transcript spells it REPIT, while concepts.md writes RePPIT. Depth: **teach**.
3. **What the plan holds.** Requirements, the files that change, tests, observability, security, rollout, and an explicit out-of-scope list; the lecturer calls calling out what is outside the scope "one of the most valuable things" and tells the agent "Don't touch this" (S003). Anthropic's version: the most useful specs name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step (S117). Put the decisions most likely to change first (data model, interfaces, user-facing flows) and mechanical refactoring last, so your review lands where it matters (S037). Depth: **teach**.
4. **Where you matter most: choosing and reviewing.** "The most important best practice is to review your specs" and the research, proposal and planning steps are "one of the highest-leverage places for a human today" (S003). After choosing a proposal, clear the context so the rejected one doesn't confuse the agent (S003). A person picks the path, and implementation stops if the map turns out to be wrong (S036). Depth: **teach**.
5. **Keep it human-sized.** Martinez's case: about ten bullets of scope came back as a twenty-page polished document, moving the unresolved ambiguity onto the people who had to review it; "Generation is cheap, but evaluation is expensive" (S118). Users had little appetite for long AI-generated specs (S030). A plan you can't review is not a plan you approved. Depth: **teach**.
6. **Implement in a fresh session from the written plan.** Start a new session with the spec as input (S117, S037), and have the agent log any departures from the plan in an implementation-notes file, choosing the conservative option at each edge case (S037). Depth: **brief**.
7. **Plan mode, demystified.** It is the harness switching into a read-and-plan phase that ends in a plan file (S002). In Claude Code, Shift+Tab until the status bar shows plan mode; Ctrl+G opens the plan in your editor before you approve it (S117). The lecturer says the built-in planning in Claude and Codex is "quite good" and he doesn't always use his own template (S003). Depth: **brief**.
8. **Spec tools exist.** Kiro writes requirements, design and tasks with an approval gate between each, can flag vague terms and contradictions, and says its gate-skipping Quick Spec is not for unfamiliar territory or high-stakes systems (S024). Depth: **one line**.

### C037 Find what you want cheaply before building it

1. **Brainstorm before choosing.** Shihipar's example prompt: brainstorm 10 places to intervene, "from cheapest to most ambitious", then pick (S037). Depth: **brief**.
2. **React to a throwaway mockup first.** Ask for a single HTML file with fake data, or "4 wildly different design directions", and react before the agent touches the real app (S037). Depth: **teach**.
3. **The prototype is not the product.** A vibe-coded prototype appears in about an hour and makes people believe the hard part is over; integration, the requirements it skipped, testing by a person and the decision whether it belongs at all are still ahead (S118). Start the real build in a fresh session, passing the decision and the mockup as artifacts (S037). Depth: **teach**.
4. **Let the agent interview you.** "Interview me one question at a time about anything ambiguous", putting first the questions whose answers would change the architecture (S037). Claude Code's docs give a fuller version: an interview with the AskUserQuestion tool that ends by writing SPEC.md, then a fresh session to build it (S117). Depth: **brief** (02.02 already taught surfacing unknowns).
5. **Point at a reference instead of describing it.** Give the agent source code that already behaves the way you want, even in another language: Shihipar's example reimplements a Rust rate-limiter's backoff in a TypeScript client (S037). Inside your own repo, name the existing component it should follow (S117). Depth: **brief**.
6. **Question it when it looks finished.** People building artifacts with AI give more direction up front but evaluate less: identifying missing context fell 5.2 points, checking facts 3.7, questioning reasoning 3.1 (S119). Depth: **one line**.

Dropped here: "bring your own variance, because AI ideas converge" (S068) belongs to C030 in making-media-with-ai (09.02).

### C039 Map before you change

1. **Start with a read-only pass.** OpenAI's map prompt asks for the directories and what each does, the files behind the core user flow, the conventions to keep, the install, run, test, lint and build commands, and the safest way to validate a small change, citing files, keeping verified facts apart from assumptions, with no edits yet (S008). Review the map, then delegate. Depth: **teach**.
2. **Check one assumption against the code** before you trust the map; when the agent guesses about files or rules, have it read the named file first (S008). Depth: **brief**.
3. **Your own vibe-coded app is already an existing codebase** once an agent has written code you didn't decide line by line (S036). Depth: **one line**.
4. **A person draws the risk map, not the agent.** Green: good tests, isolated, the agent works in a tight loop. Yellow: mixed quality, pin current behaviour with tests first. Red: authentication, billing, permissions, payroll: a human pairs on every step, or the work doesn't happen. Left alone, an agent starts in the scariest file, because it has the most interesting names (S036). Depth: **teach**.
5. **The research document is your mental model too.** You need map-level understanding (there is a frontend and a backend, this framework, data shaped like this), enough "to discern good from bad", not every detail (S003). Depth: **brief**.
6. **For risky work, write a comprehension memo** that outlives the session: entry points, owners, callers, tests, production signals, history and open questions, each claim citing a file, issue or dashboard (S036). Depth: **brief**.
7. **Use read-only tools for reading.** Plan mode reads and answers without changing files, and subagents keep a big investigation out of your main context (S117). Depth: **one line**.
8. **Trust existing docs only if someone maintains them;** the lecturer starts fresh otherwise (S003). Depth: **one line** (stale instructions are C048 in 05.02).

### C041 Slice work small enough to review

1. **Agent patches run long.** On SWE-bench Verified, agent patches are consistently longer than the human reference patches even when they solve the task; every model has over 15% of solved patches more than 1.5 times the reference length, attributed to verbose code, scope creep and over-defensive code (S031). Depth: **teach**.
2. **If it does more than you can review, you cannot manage it** (S008). A multi-thousand-line PR is beyond what a reviewer can understand, and a two-sentence request now comes back as a "whole not fully thought out feature set" (S118). Depth: **teach**.
3. **Bound every slice and catch drift.** Put "keep the change small, preserve unrelated work" in the request; when scope drifts, pause, keep only what was asked and list the rest as follow-ups (S008). Compare `git diff --stat` with what you asked for, and have the agent list and justify every file it touched (S031). Depth: **teach**.
4. **Size changes correctness, not only reviewability.** In a VB6-to-C# study, behavioural equivalence was 92% on simple features and 47% on complex ones: "unit size is the lever" (S036). Depth: **teach**.
5. **Trying is cheap; choosing is not.** Agents "have changed the price of trying several plausible implementations", not the evidence needed to choose: build competing options, run them against the same tests, profile them, then decide (S036), against the same success criteria (S008), never on the agent's description of them. Depth: **teach**.
6. **Test the prompt on a few items before fanning out.** Refine on the first 2-3 files, then run the full set; `/batch` splits a change across 5 to 30 subagents in their own worktrees (S117). Depth: **brief**.
7. **More agents is not more done.** Going from 1 to 4 local workers gave no net throughput gain in one team's log, and an orchestrating agent spent 4-8 times the tokens of fixing small, already-diagnosed tickets directly (S030). Parallelize last, once you have a dependable judge, a cheap recovery path and a review format people can absorb (S036). Depth: **brief** (fleets are C095 in 08.01).
8. **Long unattended runs need size limits, not more time.** Ronacher's 35-hour run used about 1B tokens and about $1,200 and "delivered absolutely nothing of value"; given a slightly too big task, the model keeps going (S035). Depth: **one line** (stop rules are C096 in 08.01).

Dropped here: the interference rate of parallel patches (105 of 108 constructed runs in Xia, Wu and Park, via S030) is C011's "pass alone, fail together" shape, taught in done-is-a-claim (02.04). If it is mentioned, add S030's own caveat: across 417 mined real Django PR pairs, only one run showed interference after grading was corrected.

## You vs the agent

As of 2026-10-12:

- **The agent does on its own (or when asked):** brainstorms options, builds throwaway mockups, interviews you, maps the code read-only and cites files, writes the research document, proposes options, drafts the plan and the out-of-scope list, implements each slice, tests in a browser, builds competing versions on separate branches, lists every file it touched and logs its deviations (S037, S117, S003, S008, S036). Planning is now built into the harnesses well enough that the Stanford lecturer often skips his own template (S003).
- **You must:** judge the size and risk of the task and pick how much process it gets; react to the mockups and choose; answer the questions that fix the architecture; read the map and check one assumption; draw the risk zones; choose between the proposals; approve a plan short enough to review, with its out-of-scope list; set slice size by what you can review; reject edits you didn't ask for; decide what evidence will choose between competing versions; stop the build when the map turns out wrong (S003, S008, S036, S117, S118). Whether the right thing is being built is the one thing the agent cannot verify (S003, S024).
- **Bring in an expert when:** a slice touches a red zone (authentication, billing, permissions, payroll), which gets its owner or someone who knows it on every step (S036); the plan's security and rollout sections need someone who can judge them (S003, S004); and a working prototype says nothing about readiness for real users, so integration, security and UX checks go to someone qualified (S118), the subject of before-you-ship-who-signs-off.

## Sources this lesson is built from

Built on (credited on screen):
- S003 — Mihail Eric (Stanford CS146S), "Advanced prompting and context engineering" lecture transcript (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — the five steps, two orthogonal proposals, the out-of-scope list, "review your specs", clearing context after choosing, and the size ladder from copy change to stacked issues.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — the green/yellow/red risk map drawn by a person, the comprehension memo, "stop if the map is wrong", "trying is cheap, choosing is not", and the 92% vs 47% unit-size result.
- S117 — Anthropic, "Best practices for Claude Code" (undated live docs, names v2.1.283, no earlier than 2026-09-25) https://code.claude.com/docs/en/best-practices — explore, plan, implement, commit; the one-sentence-diff rule; plan mode and Ctrl+G; the interview prompt and SPEC.md; test on a few before fanning out.
- S118 — Gabriel Martinez (G2i), "Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop", AI Engineer World's Fair 2026 (2026-10-09, YouTube upload date) https://ai.engineer/talks/6qkzlT962es — prototypes that make the hard part look done, ten bullets returned as twenty pages, unreviewable PRs, two-sentence requests returned as whole feature sets. His judgment, not a measurement; the talk ends with a product plug.
- S037 — Thariq Shihipar (Anthropic), "A field guide to Claude Fable 5: Finding your unknowns" (2026-07-06) https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns — brainstorm cheapest to most ambitious, single-file mockups, the one-question-at-a-time interview, reference code, likely-to-change decisions first, implementation notes.
- S031 — Zora Z. Wang, John Yang, Kilian Lieret et al., "Humans are Missing from AI Coding Agent Research" (2026-07-04) https://arxiv.org/abs/2608.12355 — agent patches measurably longer than human ones; check the diff against the scope and have every file justified.

Supporting (credited on the lesson page):
- S008 — OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala), "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — the read-only map prompt, the scope-drift reply, "if it does more than you can review, you cannot manage it".
- S030 — Remy, "When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer" (2026-10-11) https://redreamality.com/blog/coding-agent-done-claims-verification-survey/ — little appetite for long AI specs; 1 to 4 workers with no throughput gain; orchestration at 4-8x the tokens.
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — the 35-hour run that delivered nothing of value.
- S024 — Kiro (AWS), "Specs" docs (2026-10-02) https://kiro.dev/docs/specs/ — requirements, design and tasks with gates; Quick Spec's own warning.
- S002 — Mihail Eric (Stanford CS146S), "Anatomy of a state-of-the-art coding agent" lecture transcript (2026-09-24) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — plan mode as a harness phase that ends in a plan file.
- S119 — Kristen Swanson, Drew Bent, Zoe Ludwig, Rick Dakan, Joe Feller (Anthropic), "Anthropic Education Report: The AI Fluency Index" (2026-02-23; within 12 months) https://academy.claude.com/tutorials/the-ai-fluency-index — people evaluate polished artifacts less.
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — the course rule: don't take security or deploy-readiness claims you can't check.

How these were checked: S003 (raw transcript), S036, S117, S037 and S118 were re-opened for this spec on 2026-10-12. S118's YouTube captions could not be fetched (YouTube blocked the request), so its points come from the transcript and article on the ai.engineer talk page. The other sources rest on the research crew's reading in concepts.md (G04, re-checked 2026-10-12). The shared web-search budget was used up, so no search for sources newer than 2026-10-12 was run for this spec; re-check S117 and the Claude Code version numbers at lesson time.

Affiliation note for the page: S037 and S117 are Anthropic material and Osmani (S036) works at Anthropic; S008 is OpenAI's; S003, S031, S035 and S118 are independent.

## Show it for real

- Claude Code on a public open-source repo: Shift+Tab until the status bar shows plan mode, run the map prompt, and box the "assumptions" part of the answer; then open the cited file and check one assumption (proves the map is read-only, cited, and checkable). Desktop capture or terminal replay (S117, S008).
- A single local HTML file with four wildly different dashboard directions on fake data, opened in a browser; a pointer picks one (proves reacting is cheaper than describing; no personal data on screen) (S037).
- Two proposals open side by side, one chosen, `/clear`, then "implement the plan" from the plan file, with Ctrl+G showing the plan's out-of-scope section in the editor (proves the human checkpoint is a short, editable plan) (S003, S117).
- `git diff --stat` of an agent patch that also "improved" unrelated files, next to the request; the scope-drift reply, and the reduced diff with a follow-up list (proves drift is visible without reading code) (S031, S008).
- Two agent-built versions on separate branches run against the same tests and a quick timing check, ending in a small results table (proves choosing on evidence, not on the agent's description) (S036).
- A still of the ai.engineer talk page with the line "Generation is cheap, but evaluation is expensive" boxed (credits the source; public page) (S118).

## Questions this lesson answers

- "How do I get the AI to build something big without it going off the rails? Should I plan before coding with AI?" (courses-teach-now items, from S001 and S003)
- "When should I use plan mode? Why did the agent rewrite half my app for a small change?" (from S002, S003)
- "Why did it change 40 files when I asked for one fix? How big should a task for an agent be?" (vendor-academies item, from S008)
- "Why does the agent do well on small things but mess up big projects?" (surveys-and-learning item, from S082 and S085)
- "How do I figure out what I want before the AI builds it? I have no design taste; how do I get a good-looking UI?" (practitioners-now item, from S037)
- "How do I explain what I want when I don't have the words? Can the AI copy how another project does something?" (from S037)
- "How do I start with a codebase I didn't write? How do I know the agent understood my project?" (from S008)
- "Should I let the AI try several versions?" (from S036)
- "What should I review if I can't read the code?" (from S024; the plan, the out-of-scope list and the diff's file list)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Surfacing your unknowns, the blind-spot pass and a checkable "done when" → saying-what-you-want
- When the agent loops: stop it and change the input; the two-strikes `/clear` rule → when-it-breaks-you-supply-the-eyes
- Reading a diff and a branch (prerequisite, C124 and C117) → save-points-and-the-agents-trail
- Why context fills, clearing after a decision, subagents starting blind → what-the-agent-sees-each-turn
- Red zones and blast radius → working-is-not-secure
- How to check each slice (evidence the agent can't write, independent tests, AI review as triage) → checking-what-you-cant-read
- What orchestration and fan-out cost → know-your-meter
- Parallel fleets and stop rules for long runs → agents-that-run-while-youre-away
- Bringing in an expert, and who signs off → before-you-ship-who-signs-off
- Understanding before you merge, and whether it is worth building at all → idea-to-launch-end-to-end

## Out-of-date framings to avoid

- "Prompt, then fix what comes out, even for big features" (S024, S003).
- "Every task needs the same workflow", in either direction: always plan, or never plan (S003, S117).
- "Planning means approving a long AI-generated spec" (S030, S118).
- "Build the real thing first and adjust later" (S037).
- "A working clickable prototype means the hard part is done" (S118).
- "Just tell it what to build and let it pick where to start" (S008, S036).
- "Give the agent the whole app in one prompt" (S008, S118).
- "If the task is solved, the size of the change doesn't matter" (S031).
- "More agents in parallel means more output" (S030, S036).
- Don't present RePPIT/REPIT or Kiro as required tools: the lecturer himself says the built-in planning is good enough most days (S003).
- Don't claim the lecturer said vibe coding only works for small changes; his words are that everyone can vibe code "up to a point", and hard problems in difficult codebases need a level beyond it (S003).

## Legacy notes

No legacy lesson covers this slot.
