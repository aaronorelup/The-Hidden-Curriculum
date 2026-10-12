---
key: idea-to-launch-end-to-end
id: 10.01
title: Idea to launch, end to end
district: Capstone
module: 10 Capstone
status: todo
legacy: []
minutes: 15
concepts: [C010, C018, C043]
sources: [S007, S115, S084, S083, S029, S037, S033, S118, S097, S068, S209, S117, S003, S004, S008, S009, S016, S020, S026, S030, S032, S034, S036, S039, S044, S052, S053, S060, S063, S067, S072, S076, S077, S094, S123, S143, S146, S208, S212, S214, S220, S231, S246]
lead: [S115, S084]
---
# Idea to launch, end to end

**Purpose (the first spoken sentence):** In this lesson you'll learn how one small, real project travels from an idea to a public launch with an agent doing the building, and which decisions and checks along the way stay with you.

**Conclusion:** The agent will build whatever you point it at, so the project stands or falls on what you decide (is it worth building, what does "done" mean, can I explain what it built) and on every check being run by the agent where it can be verified, and by you or an expert where it cannot.

**Where it sits on the map:** Finish · Capstone — "Can you ship it end to end?"; module 10 Capstone, lesson 1 of 2. The pin starts at Start and the project walks the whole map once, district by district, to Finish.

**Lead source (audit, 2026-10-12):** S115 (Addy Osmani); S084 (Addy Osmani). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S007, S115, S084, S083); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length (audit, 2026-10-12):** COURSE.md (Aaron, 2026-10-01) gives the first lesson of every module about 5 minutes; this one is 15. No lesson of about 5 minutes exists in this module to open it instead, and splitting would take the course past its 36-lesson cap, so the choice (retire the rule for these modules, or split and cut elsewhere) is on design-decision.md's "For Aaron to decide" list. Until he answers, keep 15.

## What to teach (binding scope)

This lesson is a walk, not a new district. It teaches three concepts in depth (deciding what is worth building, understanding before you merge, keeping the judgment you need to supervise) and names every other check in one line, at the moment the project meets it, with a pointer to the lesson that teaches it. Nothing taught in an earlier lesson is re-taught here.

**The worked project.** The lesson follows one small real project that is actually built and recorded for the lesson, never narrated from imagined results. It should have a handful of real users (Osmani's "just five users" frame, S115), a sign-in, stored data and a public URL, so that it touches every district: for example a sign-up sheet for a small club. Build it in a throwaway repo with test accounts and a test database. Which project to use is Aaron's decision; if it is one of his, tell it in the third person (COURSE.md).

**Time budget (about 15 minutes):** purpose and map 1 min; C043 3 min; the walk, part 1 (workbench to first slice) 2 min; C018 4 min; the walk, part 2 (going live to launch) 3 min; C010 2 min. Order follows the project: decide, build, explain, ship.

### C043 Deciding what is worth building stays human
1. **The agent will build anything, including things nobody needs.** Willison's "AI mania" in January 2026: any time the agent wasn't building felt like wasted time. It led him to build a JavaScript interpreter and a WebAssembly runtime in Python, and he concluded the world did not need a slow, buggy one (S033, 2026-09-27). Depth: teach.
2. **Three questions before the first prompt: who is it for, does it need to exist, what will it cost to keep?** Osmani asks whether old side projects an agent could now finish "deserve to exist", and notes that even "just five users" can mean ongoing maintenance and a quality bar (S115, 2026-08-21). Depth: teach. This is the opening beat of the worked project.
3. **Decide what not to build.** Martinez lists knowing what not to build as perhaps the most important human job, and says agents "cannot replace the human work of deciding what matters". Quoting SQLite's creator, he calls a pull request a request to maintain the code for you for the next twenty-five years (S118, 2026-10-09). Depth: teach.
4. **What stays yours, by name.** Someone still chooses the problem, the architecture and the quality bar, decides which verification signals deserve trust, and decides when the evidence is sufficient to ship; when it fails, "the agent wrote it" is not an explanation (S115). Depth: teach. These five decisions are the left-hand column of the lesson's "launch ledger" (see the walk below).
5. **Deciding is the first of four skills: deciding, specifying, steering, verifying** (S084, 2026-08-31). Depth: brief. The capstone walks all four in order.
6. **Looking like the thing is not being the thing.** Agents given screenshots of a 2022 game idea built games that were fun for about 75 seconds; a good gameplay loop was beyond them (S033). Depth: brief, as the reason "what good means" is your judgment.
7. **Keep the decisions worth making.** Mollick's reasons for an agent to bring a person in: approval (agents should not decide by themselves to spend money, contact outsiders or access sensitive material), expertise, variance (AI ideas converge) and interest; if people keep only the approvals, exceptions and failures, "we will have automated the wrong half of the job" (S068, 2026-08-31). Depth: brief.
8. **Current builder courses end on ownership.** Anthropic's AI Fluency for Builders (with CodePath) runs "from framing a customer problem to shipping a product" and closes on a module titled "Stand behind what you build" (S007, updated September 2026). Depth: one line. The module's contents are behind enrolment: concepts.md's "ship, fix or stop after launch" detail could not be re-confirmed from the public page on 2026-10-12, so do not attribute it on screen.

Dropped from C043 and taught elsewhere: measuring outcomes rather than output (C043 point 6) → after-launch-keep-it-alive (C020); Ball's "meat proxies" prediction (S034) → saying-what-you-want (C033).

### C018 Understand before you merge
1. **The middle position: not every line, not nothing.** You need the main flows, the boundaries, the data model and the product's behaviour; Martinez: the code need not be read line by line, but "the logic has to be understood" (S118). Depth: teach.
2. **A diff is a light understanding.** Behaviour depends on code paths the diff does not show, so reading diffs gives only "a light understanding" (S037, 2026-07-06). Depth: teach.
3. **The explainer-and-quiz gate.** After a long session, ask the agent for an HTML report explaining what it did, with context and intuition, ending in a quiz. Shihipar: "I only merge after I pass the quiz perfectly" (S037). Depth: teach; this is the centrepiece demo of the lesson.
4. **The "can I explain this?" test:** what the change does, what it touches and why it is safe to ship. Osmani: "You can only really be accountable for what you can explain" (S029, 2026-09-28). Depth: teach.
5. **Say in the pull request what you did not review**, in Osmani's example "agent-reviewed, tests pass, I haven't read the migration logic", so nobody assumes more review happened than did (S029). Depth: teach.
6. **Keep it human-sized.** A 100-plus-page AI report and a 30-tab spreadsheet is the same problem as an unread 5,000-line diff; asking for the one-page version "isn't obstruction. It's review" (S029). Depth: brief.
7. **Explainers bring in experts.** An explainer lets an expert see that you "accounted for the unknowns and common failure points" they would expect (S037). Depth: brief; how to brief an expert is taught in before-you-ship-who-signs-off (C118).
8. **It matters past you.** MIT's Missing Semester 2026: "Submitting AI-generated code you can't explain burdens maintainers", and "accepting a PR means accepting long-term responsibility" (S209). Depth: brief.
9. **What explaining catches that tests miss.** Osmani's hypothetical: asked to add GitHub as a sign-in provider, an agent drops another one because the UI "only had space for three", and it is the one "your customers actually wanted"; the tests pass and the intent is broken (S115). Depth: brief; label it a hypothetical on screen.

Dropped from C018 and taught elsewhere: the read-only "map the repository first" pass and research step (S008, S003) → plan-first-then-build-in-slices (C039); "in old code, explain before editing" (S036) → plan-first-then-build-in-slices.

### C010 Keep the judgment you need to supervise
**Framing guard.** This is not a call to debug by hand. In shipped work the agent reads, fixes and re-runs its own errors (S004; when-it-breaks-you-supply-the-eyes). C010 is about the parts of the stack you will have to oversee while you are still learning them.
1. **The trial.** Anthropic's randomized trial (2026-01-29; foundational and still current): 52 mostly junior engineers learning the Trio library. The AI group scored 50% on a follow-up quiz against 67% for hand-coders (Cohen's d 0.738, p = 0.01) and was about two minutes faster, which was not significant. The largest gap was on debugging questions: recognising when code is wrong and why, the skill you need to supervise (S083). Depth: teach.
2. **How you use AI decided the result.** Low scorers (under 40%) delegated fully, slid into progressive reliance, or used AI to debug and verify instead of to understand. High scorers (65% or more) generated code and then asked follow-ups, asked for code plus explanation, or asked conceptual questions only (the second-fastest group). Small sample, one library, an immediate quiz, and associations rather than causes (S083). Depth: teach.
3. **A newer study points the same way.** 54 students building a website: agents helped them finish but harmed comprehension and left them less prepared to extend the code without an agent; copy-paste prompting and auto-accepting edits went with lower comprehension; they still preferred agents (S097, 2026-07-29, in-progress preprint). Depth: brief.
4. **"Verification is the floor and imagination is the ceiling."** What you can safely keep is capped by whether you can recognise when the output is wrong and why (S084). Depth: teach.
5. **The habits (S084):** form a hypothesis before prompting; ask why (what it ruled out, what it assumed); read the diff and predict what could still fail, which Osmani calls the highest-value minute in the loop; on the parts you are still learning, ask conceptual questions (the high scorers' pattern in S083) and have the agent quiz you on its own explanation before you accept (the explainer-and-quiz gate, S037, C018 point 3); ask for explanations, not just output. Depth: teach. (Audit, 2026-10-12: "work some problems by hand" was cut, against Aaron's correction that nobody debugs by hand any more.) In the worked project, show one prediction written down before accepting a slice, then the agent testing exactly that case.
6. **Use a learning mode while learning:** Claude Code's Learning and Explanatory modes, ChatGPT Study Mode (S083). Depth: one line.
7. **Teams have to build supervision skills on purpose** (S029). Depth: one line. (Audit, 2026-10-12: the mentoring and "leave some work manual" detail was cut as team management, outside this audience.)
8. **People who stop deciding stop learning to decide:** they "stop developing the judgment they will need later" (S068). Depth: one line.

### The walk: every check, at the moment the project meets it
Depth: one line each, drawn as a "launch ledger" that fills in as the project moves across the map. Each row names who runs the check under the course rule. Facts and figures stay in the lesson that teaches them.

| Stage (district) | The agent runs it (verifiable) | You, or an expert (not verifiable by the agent) | Taught in |
|---|---|---|---|
| Decide (Start) | drafts options and lists what already exists | who it is for, whether it should exist, what it costs to keep (S115, S118) | here (C043) |
| Say what you want (1) | interviews you, writes the spec to a file, ending in an end-to-end verification step (S117) | the goal, the constraints, a checkable "done when", the out-of-scope list (S037) | saying-what-you-want |
| Workbench (1) | types every git command, commits each slice, pushes to the remote | which folder it opens, that a remote copy exists, which branch is live (S208, S026) | the-folder-is-the-agents-world, save-points-and-the-agents-trail |
| Before it runs (1) | works inside the mode you chose | the permission mode, a copy off the machine, the targets of any delete (S063, S052) | before-you-let-it-loose |
| Plan, then slices (3) | maps read-only, compares two options, builds one slice, runs its checks (S117) | review the short plan, choose on evidence, keep each slice reviewable (S036, S118) | plan-first-then-build-in-slices |
| When it breaks (1) | reads the error, adds logging, reproduces, fixes, re-runs (S094) | the reproduction, what correct looks like, a way for it to see the real result (S009, S032) | when-it-breaks-you-supply-the-eyes |
| "Done" (1) | shows evidence: the test output, the command and what it returned, a screenshot (S117) | one check against the real thing, and whether it is good (S030, S032) | done-is-a-claim |
| Explain before merge (Finish) | the explainer, the quiz, the PR description (S037) | pass the quiz; say what you did not review (S029) | here (C018) |
| Going live (2) | keeps secrets server-side, deploys previews (S212) | nothing secret in the browser, revoke and rotate anything leaked, know that rollback leaves data untouched (S020, S026) | what-runs-where, keys-public-secret-and-leaked, from-your-laptop-to-a-url |
| Safe for strangers (2) | runs scanners, the anonymous stranger test on every table and bucket, accessibility checkers, and lists every route, TODO and deploy step (S044, S220) | state the stakes, read what each fix to sign-in, payments or permissions changed, set AI-feature caps that stop spending, bring the inventory to a qualified expert, and own the ship decision (S039, S214) | working-is-not-secure, test-it-as-a-stranger, your-apps-ai-feature, before-you-ship-who-signs-off |
| Directing well (3) | reads the instruction file, runs the gates (S123) | keep the file short and dated, back rules with checks you have seen fire, accept on records the agent cannot write, set spending caps that stop (S030, S016) | rules-it-reads-rules-it-cant-break, checking-what-you-cant-read, know-your-meter |
| Agent power (4) | checks every new dependency exists and has a history (S060) | no production keys where it runs, the narrowest scopes, a human approves money, outsiders and publishing (S053) | the-narrowest-keys-and-verbs, other-peoples-code |
| Running alone (5), if the project has automations | heartbeats and known-answer checks at the destination (S067) | who each automation runs as, recovery codes, a second owner (S246) | green-is-not-success, every-automation-runs-as-someone |
| Beyond code (6), if it cites research or makes media | checks every cited link exists (S072) | whether each source supports the claim, the AI label, the generator's terms (S076, S077) | checking-research-numbers-and-parts, labelling-ai-media, own-it-sell-it-publish-it |
| Launch (Finish) | — | the ship decision is yours (S115) | after-launch-keep-it-alive takes over |

Two points about the walk as a whole (both brief):
- **Budget the checking time.** In Osmani's factory runs, tasks took "two to four times as long" once verification, retries, browser checks and review were counted; he runs fast checks (linting, type checking) early and heavier ones (mutation testing, browser tests, security checks) later (S115).
- **The closing rule, in Anthropic's own docs:** "If you can't verify it, don't ship it" (S117). Pair it with the course rule: what the agent cannot verify, you check, and what you cannot check, an expert does.

## You vs the agent
As of 2026-10-12:
- **The agent** builds every slice, runs and fixes its own errors, writes and runs tests, opens the browser on its own work, commits and opens pull requests, writes the spec from your answers, writes the explainer and the quiz, assembles the release inventory and the expert's scope pack, runs every scanner and stranger test it is given, and reports evidence instead of claims when asked (S117, S037, S115).
- **You** decide whether the project should exist, who it is for and when to stop (S115, S118); write what "done" means; keep each slice small enough to understand; pass the quiz or explain the change before merging, and say in the pull request what you did not review (S037, S029); predict what could still fail before accepting (S084); while learning a part you will oversee, keep the thinking (S083); and own the ship decision (S115).
- **Bring in an expert** when you cannot pass the quiz or judge a change: an experienced engineer reads the explainer (S037). For anything holding other people's data or money, a qualified security tester checks it before strangers arrive (before-you-ship-who-signs-off, S214). For whether the thing should exist, ask the people it is for (C043; S068).

## Sources this lesson is built from
- S115 — Addy Osmani, "Human judgment doesn't leave the software factory. It relocates." (2026-08-21) https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/ — the questions before building ("deserve to exist", "just five users"), the five decisions someone still owns, the sign-in-provider hypothetical, "two to four times as long" with verification, and the verification budget. Re-read 2026-10-12.
- S118 — Gabriel Martinez (G2i), "Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop", AI Engineer World's Fair 2026 (2026-10-09) https://ai.engineer/talks/6qkzlT962es — knowing what not to build, deciding what matters, the PR as a 25-year maintenance request, "the logic has to be understood". His judgment, not measurement; the talk ends with a plug for his company's tool. Transcript re-read on the ai.engineer page 2026-10-12 (YouTube captions returned HTTP 429).
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — AI mania, and screenshot-built games that were fun for about 75 seconds. Re-read 2026-10-12.
- S084 — Addy Osmani, "Agentic Skill Decay" (2026-08-31) https://addyosmani.com/blog/agentic-skill-decay/ — verification is the floor and imagination the ceiling; deciding, specifying, steering, verifying; the habits that keep judgment. Re-read 2026-10-12.
- S083 — Judy Hanwen Shen and Alex Tamkin (Anthropic), "How AI assistance impacts the formation of coding skills" (2026-01-29; foundational and still current) https://www.anthropic.com/research/AI-assistance-coding-skills — the randomized trial, its debugging gap, the six interaction patterns, learning modes. Re-read 2026-10-12.
- S097 — Balepur, Baumler, Chen, Choi, Rudinger, Boyd-Graber, "(Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding" (2026-07-29, in-progress preprint) https://arxiv.org/abs/2607.26375 — 54 students: faster, weaker comprehension, low-effort use, still preferred agents. Re-read 2026-10-12.
- S037 — Thariq Shihipar (Anthropic), "A field guide to Claude Fable 5: Finding your unknowns" (2026-07-06) https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns — the HTML explainer and quiz before merging, "a light understanding" from diffs, explainers for experts. Re-read 2026-10-12.
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — the "can I explain this?" test, saying what you did not review, human-sized reports, mentoring on purpose and the paradox of supervision. Re-read 2026-10-12.
- S068 — Ethan Mollick, "Agency and Agents" (2026-08-31) https://www.oneusefulthing.org/p/agency-and-agents — when an agent should bring a person in, "the wrong half of the job", judgment that stops developing. Re-read 2026-10-12.
- S209 — MIT Missing Semester 2026, "Beyond the Code" lecture (lectures 2026-01-12 to 01-23; still current) https://missing.csail.mit.edu/2026/beyond-code/ — code you can't explain burdens maintainers; accepting a PR is long-term responsibility. Re-read 2026-10-12.
- S117 — Anthropic, "Best practices for Claude Code" (undated live docs; names v2.1.283, 2026-09-25 or later) https://code.claude.com/docs/en/best-practices — the interview-then-spec prompt, specs that end in an end-to-end verification step, evidence instead of assertions, "If you can't verify it, don't ship it". Re-read 2026-10-12.
- S007 — Anthropic Academy with CodePath, "AI Fluency for Builders" (Coursera; "Recently updated" September 2026) https://www.coursera.org/learn/ai-fluency-for-builders — a current builder course that runs from a customer problem to shipping and ends on "Stand behind what you build". Public page re-read 2026-10-12; module contents need enrolment.

Real questions quoted in this lesson come from S231 (Ask HN, "Vibe-coded prototypes: what happens when they go into production?", early 2026, re-read 2026-10-12), S143 (Ask HN, "Is vibe coding bad for SaaS projects?", 2026-10-01) and S146 (Ask HN, frontier models and security reviews, 2026-10-07); credit them where the question appears.

The walk table also points at the sources of the lessons it names (S009, S016, S020, S026, S030, S032, S036, S039, S044, S052, S053, S060, S063, S067, S072, S076, S077, S094, S123, S208, S212, S214, S220, S246); those lessons credit them. They are cited here only for the one-line check each row names.

## Show it for real
- **The decision, on screen:** a short list of project ideas run through "who is it for, does it need to exist, will I maintain it?" with the agent drafting and the human striking ideas out. Proves the first decision is yours (S115). A still with `K.shot`.
- **Interview, then spec (terminal):** the agent interviewing the builder and writing `SPEC.md` with a "done when" and an out-of-scope list, then the file opened. Proves "done" is written before code (S117). Terminal replay or screenshots.
- **The slices (terminal replay):** `git log --oneline` of the worked project showing one commit per slice, and `git diff --stat` of one slice. Proves the work arrived in pieces small enough to understand.
- **Evidence instead of a claim:** the agent's end-of-slice report with the command it ran and its real output, plus a screenshot of the running page. Proves what "done" should come with (S117).
- **The explainer-and-quiz gate (browser capture):** the agent's HTML change report opened in a clean browser profile; the quiz taken, one answer wrong, back to the explanation, then passed. Proves understanding is checked before merging (S037). The centrepiece recording.
- **A prediction before accepting:** one line typed before accepting a slice ("if two people sign up at once, the count is wrong"), then the agent testing exactly that case. Proves the C010 habit (S084).
- **The pull request:** the description with a line saying what was not reviewed. Proves disclosure (S029).
- **The stranger test and the ledger:** the anonymous-key query against the test database being refused, then the launch ledger with its two columns filled in (agent's checks with evidence links, the human's and the expert's with names). Proves every check has an owner (test-it-as-a-stranger, before-you-ship-who-signs-off).
- Safety: throwaway repo, test database project, test accounts with `@example.com` addresses, no real keys or personal data on screen; check every still before committing (docs/showing-real-computer-actions.md).

## Questions this lesson answers
- "Vibe-coded prototypes: what happens when they go into production?" (Hacker News, early 2026, S231). The thread's answer: small apps for a few people usually keep working; ones that grow either get shut down or are taken over by professionals.
- "Is vibe coding bad for SaaS projects?" (Hacker News, 2026-10-01, S143). Replies: it depends on whether you are validating an idea or running a product, and on whether you test and assess security before real use.
- "Do I need to understand the code AI writes? How much programming do I need to know now?" (courses-teach-now #16, via C018).
- "How do I understand what the AI changed? How do I get someone else to review AI work quickly?" (practitioners-now #37, via C018).
- "How do you maintain depth of understanding and velocity when using AI?" (Ask HN by civicsquid, 2026-09-29, https://news.ycombinator.com/item?id=49901420; read 2026-10-12, not yet in sources.md). Replies: plan then approve, very small single-purpose PRs, have the AI interview you, a separate reviewing agent before human review, explainer docs.
- "Will using AI make me a worse programmer? How should I use AI when I'm learning something new?" (C010; S083).
- "I can build anything now, so why do I feel stuck? Should I keep my agents running all the time?" (C043; S033).
- "Which frontier model can do extensive code security reviews, close to a security firm's quality?" (Hacker News, 2026-10-07, S146): the walk points to before-you-ship-who-signs-off.
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Writing the goal, constraints and a checkable "done when" → saying-what-you-want
- The folder, git save points, the remote and the live branch → the-folder-is-the-agents-world, save-points-and-the-agents-trail
- Permission modes, deletes, a copy off the machine → before-you-let-it-loose
- Mapping first, planning, slices, choosing on evidence → plan-first-then-build-in-slices
- The agent debugs; you supply the reproduction and the eyes → when-it-breaks-you-supply-the-eyes
- "Done" as a claim, evidence and one check against the real thing → done-is-a-claim
- Records the agent cannot write, AI review as triage, verifying the verifier → checking-what-you-cant-read
- Browser, server and database; keys; deploys, environments and rollback → what-runs-where, keys-public-secret-and-leaked, from-your-laptop-to-a-url
- Security of working code, the stranger test, AI-feature caps, release inventory, bringing in an expert, the ship decision → working-is-not-secure, test-it-as-a-stranger, your-apps-ai-feature, before-you-ship-who-signs-off
- Instruction files and enforcement; spending caps → rules-it-reads-rules-it-cant-break, know-your-meter
- Injection, containment, narrow keys, dependencies → whose-words-is-it-reading, contain-it-dont-babysit-it, the-narrowest-keys-and-verbs, other-peoples-code
- Automations, green runs, accounts → agents-that-run-while-youre-away, green-is-not-success, every-automation-runs-as-someone
- Research, media, labels and rights → checking-research-numbers-and-parts, making-media-with-ai, labelling-ai-media, own-it-sell-it-publish-it
- Measuring outcomes, house rules, the dependency owner, code an agent can change safely → after-launch-keep-it-alive

## Out-of-date framings to avoid
- The capstone as a hand-debugging marathon, or "learn to build by fixing errors by hand" as a work method (S004, S083).
- A click-by-click build tutorial. The course is a map; the walk names checks and owners, not keystrokes (COURSE.md).
- "You must understand every line the AI writes", and its opposite, "you don't need to understand anything" (S029, S118, S037).
- "Skimming the diff is reviewing" and "the agent summarised it, so I understand it" (S037).
- "More projects shipped is more value"; "keep your agents building all the time" (S033).
- "The AI said it's secure and ready to deploy" taken as a check (S004).
- "The agent (or the expert) decides whether it ships." A person owns the decision (S115; before-you-ship-who-signs-off).
- "Human in the loop means clicking approve" (S068).
- "Using AI while learning automatically makes you learn faster", and "never use AI while learning" (S083).
- "Once it launches, it's done." Shipping starts the work (after-launch-keep-it-alive).

## Legacy notes
No legacy lesson covers this slot. The idea of a capstone that "uses every district" is older than the 2026-10-12 rework (COURSE.md's map listed a "21 Capstone"); the lesson must walk the current map (Start, First Build, Going Live, Directing Well, Agent Power, Running Alone, Beyond Code, Finish), not the retired one (The Machine, The Code, The History...).

Research notes for the builder: the shared web-search budget for this turn was used up, so no new searches were run for this spec; every source above was re-opened directly by URL on 2026-10-12. No current (since 2026-07) postmortem of a small AI-built project taken from idea to launch was found in the crew's notes; if one is found, it is the first candidate to add, since it would replace the "for example" in the worked project with a real case.
