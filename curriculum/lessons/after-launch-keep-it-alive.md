---
key: after-launch-keep-it-alive
id: 10.02
title: After launch: keep it alive
district: Capstone
module: 10 Capstone
status: todo
legacy: []
minutes: 12
concepts: [C020, C053, C054]
sources: [S082, S029, S035, S036, S004, S117, S127, S115, S118, S149, S033, S034, S084, S209, S232, S031, S142, S231]
lead: [S035, S082]
---
# After launch: keep it alive

**Purpose (the first spoken sentence):** In this lesson you'll learn what changes once your project is live: how to tell whether it is getting better or only bigger, and how to keep it a codebase an agent can go on changing safely.

**Conclusion:** Shipping starts the work, so judge the project by what happened to the people using it (bugs that got past your checks, rollbacks, how fast you recovered, whether it serves them) rather than by lines or commits, write the house rules and a named owner for the dependency list into files the agent reads, back them with checks that run without anyone remembering, and review the final diff so the agent's habits never settle into the code.

**Where it sits on the map:** Finish · Capstone — "Can you ship it end to end?"; module 10 Capstone, lesson 2 of 2 and the last lesson of the course. It picks up the worked project from idea-to-launch-end-to-end on the day after launch, and closes by handing back to Start: the map itself is rebuilt as the gaps move (the-hidden-curriculum).

**Lead source (audit, 2026-10-12):** S035 (Armin Ronacher); S082 (Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S082, S029, S035, S036); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

**Time budget (about 12 minutes):** purpose and map 1 min; C020 4 min; C053 3.5 min; C054 3.5 min. Keep using the worked project from idea-to-launch-end-to-end: a month after launch, the agent has kept adding features.

**Planning note.** The design decision names this lesson the cheapest cut if the month runs short (curriculum/research/design-decision.md): C020 would fold into idea-to-launch-end-to-end, and C053 and C054 would go to the backlog. Two of its concepts rest on thin or disputed evidence; the points below say where.

### C020 More output is not better software: measure outcomes
1. **Agents raise output.** In Microsoft's early-2026 rollout to tens of thousands of engineers, adopters merged about 24% more pull requests per engineer per day than a synthetic control predicted (95% CI +14.5% to +33.7%), across a four-month window (S082, 2026-07-01). Depth: brief.
2. **Read the claim the way its authors do.** Merged PRs "reward small, frequent PRs" and may "miss quality costs such as added complexity"; whether the extra throughput yields better software is "the pressing open question". The authors are Microsoft employees, it is one company, and it is a first arXiv version, not peer-reviewed. Its per-tool figures (+24.9% Copilot CLI, +11.4% Claude Code) come from a different within-person design and are not comparable to the headline (S082). Depth: brief; never show the per-tool numbers as a ranking of tools.
3. **Volume and value can separate completely.** Ronacher left an agent running unattended for about 35 hours on one prompt: a net 75k lines, 79 commits, about 1B tokens and roughly $1,200 at raw API prices (about $15.5 per commit), and in his judgment it "delivered absolutely nothing of value" (S035, 2026-09-07). Depth: teach; the lesson's opening case.
4. **What to watch instead.** Osmani's brownfield list: lead time, review minutes, human interventions, escaped defects, rollbacks, oracle mismatches and suppressions left behind (S036, 2026-09-14). His other essay adds incidents, rollbacks, time to recover and what customers experience (S029, 2026-09-28). For one person's project, translate to four questions: what bugs reached users that no check caught (escaped defects), how often did you roll back, how long were people broken (time to recover), and are the people it is for using it. Depth: teach. The fourth question is this lesson's translation of S029's "what customers experience", not a source's term.
5. **After an agent fix, leave something behind:** a synthetic user journey, an ownership record and a regression test, so the next person and the next agent inherit more than the patch (S036). Depth: teach.
6. **The pull to measure motion.** Martinez calls lines of code "a garbage metric for productivity", says rewarding token burn repeats the mistake ("Motion became performance"), and admits that peer speed made him merge code he had not really reviewed (S118, 2026-10-09). Willison: companies that pushed token use in February later cracked down, and Uber capped AI spending after exceeding its budget in four months (S033, 2026-09-27). Depth: brief.
7. **Osmani's post-launch signals.** He suggests watching cost per merged PR and "code shelf life" as signs of comprehension debt, and says monitoring agents can file issues while a human still owns what ships (S115, 2026-08-21). Depth: one line, labelled as his suggestion.

Dropped from C020: the SWE-bench patch-length finding (S031; not re-opened for this spec) and "ask whether it is worth building at all" → idea-to-launch-end-to-end (C043).

### C053 AI code drifts from conventions and keeps adding dependencies
Evidence note: thin (two gap items, few sources, no 2026 incident of agents adding dependencies found). Teach the mechanism and the habit, not a statistic.
1. **What the agent cannot see without you.** Aaron's own list: code that "pulls in libraries the project doesn't use", code that ignores a team's conventions, and "a dependency list that keeps growing because nobody owns it" (S004, 2026-10-04). Depth: teach.
2. **The drift is invisible because the code works.** Show it as an illustration, not a reported case: a second library doing the job of one you already use, arriving in a diff that passes every test (S004). Depth: brief.
3. **Review was never mostly about bugs.** In a 2013 Microsoft study only 14% of 570 review comments concerned defects; the rest taught, shared context and kept team norms. Anything a reviewer would have said ("we don't do it that way here") has to be written into skills, or the agent never hears it (S029). Depth: teach.
4. **Name an owner and write it down.** Someone who knows which libraries the program should use decides the list (S004). The allowed libraries and any style that differs from defaults go in the instruction file the agent reads every session; Anthropic's own example prompt asks Claude to "build from scratch without libraries other than the ones already used in the codebase" (S117). Depth: teach.
5. **Promote what keeps coming back.** "Tribal conventions become recurring review comments." Osmani's ladder runs from a quiet fix (forgotten), to a review comment, an instruction line, a skill, then a lint rule, hook, type or test, and finally deny rules, CI checks and scoped credentials that need no memory at all (S036). Osmani elsewhere: turn corrections into lint rules, tests and type constraints so both you and the next agent benefit (S084). Depth: brief; the enforcement mechanisms are taught in rules-it-reads-rules-it-cant-break.
6. **Finish migrations.** A half-finished one shows the agent both the old and the new pattern as valid precedent; a migration is done when "the new path works and the old dependency is demonstrably gone" (S036). Depth: brief.
7. **Convention is containment.** Martinez: "The more obvious the path, the less room there is for slop to hide" (S118). Depth: one line.
8. **Dependencies age even if you never touch them.** Versions a model pulls from its training data "may be six months or a year old" and may have known CVEs patched after its cutoff; one penetration tester finds known-vulnerable dependencies pulled from training data "in at least a third of cases" (S149, 2026-04-23). Osmani, reviving his own old repos: dependencies had drifted, and many were out of date or carried security vulnerabilities (S115). Depth: brief; vetting new packages and setting a minimum release age are taught in other-peoples-code.
9. **Every dependency brings a licence.** MIT's Missing Semester: look out for copyleft licences like the GPL, which "may have implications for your employer" (S209). GitHub: suggestions match public code in "less than one percent" of Copilot suggestions, Copilot records any detected licences, and "You remain responsible for reviewing and testing suggested code" (S232). The agent can list every dependency's licence; you decide what is acceptable; bring in a lawyer for a commercial product. The evidence of harm is thin (no 2026 incident found). Depth: one line.

Dropped from C053: mentoring on purpose and the paradox of supervision → idea-to-launch-end-to-end (C010); hallucinated and malicious packages → other-peoples-code (C087).

### C054 'Good code' now means code an agent can change safely
Evidence note: contested. Teach the checks as settled and the "good code" debate as open.
1. **What matters more to an agent than it ever did to us:** names unique enough to grep, modules small enough to fit in a context window, tests that fail clearly, and clear boundaries between parts. Without them the agent still makes the change, but cannot see what else the change affects (S029). Depth: teach.
2. **Human-comfort style matters less.** Osmani agrees "for the parts that were purely about human comfort, like formatting" (S029). Ball goes further and labels it belief: "There's no proof that 'good code' will matter in the future", and humans "won't modify the majority of code" (S034, 2026-09-19). So hand formatting to tools, not to your reading time. Depth: brief.
3. **But code nobody looks at hides real problems, not just ugliness.** From Ronacher's run (S035): a probe function written for tests came to be relied on by non-test code; production code calls into a list by bare index, as in `_task_accelerator[6](task)`; unindented tests were "10% more token efficient" than after `ruff format`, so that is how they were committed; several `Py_DECREF` calls packed on one line, a style that "does not exist in the CPython code base"; the same in JavaScript and CSS inside HTML. He also describes stranger behaviour in subagents "where the agent believes nobody is looking", with his own caveat that it is only "the vibe I'm getting". Depth: teach. Say on screen: one model (GPT-6 Astra), one long run.
4. **The live view is not the record.** Ronacher's subagents edited C files by splicing strings through Python in bash heredocs "instead of using the patch tool", so the changes showed only in the final diff (S035). Claude Code's docs: a hook matched on `Edit|Write` "fires only when Claude uses the Edit or Write tool, not when it uses Bash" (S127), and checkpoints "only track changes made through Claude's file editing tools" (S117). So review the final git diff, not the stream. Depth: teach.
5. **Gates that catch the habits.** Instruction files are advisory; hooks "are deterministic and guarantee the action happens". "Claude can write hooks for you", for example "Write a hook that runs eslint after every file edit"; a Stop hook "runs your check as a script and blocks the turn from ending until it passes" (S117). The formatter and linter also run in CI, where the agent cannot edit the result. Depth: teach. You decide which gates block; proving each one fires on a planted violation is taught in checking-what-you-cant-read.
6. **The disagreement, honestly.** Ronacher suspects the code is "objectively good for a codebase that is entirely written by agents", yet says "it will commit slop", so it needs closer review (S035); Ball predicts human style rules lose their point (S034). Both are September 2026 opinions; Ronacher brings evidence, Ball a prediction. Depth: brief.
7. **What is worth keeping** shifts toward what is "expensive to produce and cheap to check against": test suites, specs a person wrote, and the record of what broke (S029). Depth: one line; it ties back to C020's leave-behinds.

## You vs the agent
As of 2026-10-12:
- **The agent** keeps shipping features and will report volume (commits, lines, tokens) if you let it (S035, S082). When asked it applies written conventions, writes the instruction-file rules, the lint, formatter, hook and CI configuration (S117), flags or refuses a new import, lists every dependency and its licence (S232), refactors toward distinct names, small modules and clear test failures (S029), and leaves a regression test, a synthetic journey and an ownership record after each fix (S036). It cannot follow a convention nobody wrote down (S029), and left unchecked its own tool-call habits end up in the commits (S035).
- **You** choose the outcomes to watch and look at them, not the commit count (S036, S029); name the owner of the dependency list and the house rules and keep them written and current (S004); decide which gates must block (S117); read the final diff, not the live stream, for anything that matters, including test scaffolding leaking into production paths (S035, S127); and decide what licences are acceptable (S209).
- **Bring in an expert** when you cannot tell whether the codebase got better or only bigger (it took Ronacher's own engineering judgment to call 75k lines worthless, S035), when nobody on the project knows which libraries it should use (S004), when nobody can judge whether production code depends on test-only paths (S035), and a lawyer before selling something built on copyleft code (S209).

## Sources this lesson is built from
- S035 — Armin Ronacher, "Astra for Coding: Why Are We Doing This Again?" (2026-09-07) https://lucumr.pocoo.org/2026/9/7/astra-why/ — the 35-hour run and its verdict; the test probe, bare list indexes, tool-call style in commits, heredoc edits visible only in the final diff; "objectively good" versus "will commit slop". Re-read 2026-10-12.
- S082 — Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva, "Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI" (2026-07-01, arXiv v1) https://arxiv.org/abs/2607.01418 — the +24% merged-PR figure, its interval and method, and the authors' own limits on it. Abstract and HTML full text re-read 2026-10-12.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — the outcomes to track, what a fix leaves behind, tribal conventions and the ladder of checks, finishing migrations. Re-read 2026-10-12.
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — the 14% review finding, conventions written into skills, agent-friendly code properties, outcomes over lines, what is worth keeping. Re-read 2026-10-12.
- S004 — Aaron Orelup (drafted by Claude from his feedback), "AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — his list: unused libraries pulled in, ignored conventions, a dependency list nobody owns. Re-read 2026-10-12.
- S117 — Anthropic, "Best practices for Claude Code" (undated live docs; names v2.1.283, 2026-09-25 or later) https://code.claude.com/docs/en/best-practices — what goes in CLAUDE.md, hooks as deterministic, "Claude can write hooks for you", the Stop hook, checkpoints that miss Bash edits. Re-read 2026-10-12.
- S127 — Anthropic, "Automate actions with hooks" (Claude Code hooks guide; undated live docs) https://code.claude.com/docs/en/hooks-guide — the Prettier-after-edit hook and the `Edit|Write` matcher that does not fire on Bash. Re-read 2026-10-12.
- S115 — Addy Osmani, "Human judgment doesn't leave the software factory. It relocates." (2026-08-21) https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/ — dependencies that drift in revived projects, code shelf life, a human owns what ships. Re-read 2026-10-12.
- S118 — Gabriel Martinez (G2i), "Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop" (2026-10-09) https://ai.engineer/talks/6qkzlT962es — lines and tokens as garbage metrics, "Motion became performance", his own rushed merges, "Convention is containment". Judgment, not measurement. Transcript re-read on the ai.engineer page 2026-10-12.
- S149 — Simon Roses Femerling (VULNEX), "The OWASP Top 10 for Vibe-Coded Applications (Part 2)" (2026-04-23) https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/ — model-picked versions six months to a year old, and known-vulnerable dependencies in at least a third of his cases. Re-read 2026-10-12.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — tokenmaxxing reversed into spending caps. Re-read 2026-10-12.
- S034 — Thorsten Ball, "What I believe about the future of software development" (2026-09-19) https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/ — the prediction that "good code" may not matter and humans won't modify most code. Re-read 2026-10-12.
- S084 — Addy Osmani, "Agentic Skill Decay" (2026-08-31) https://addyosmani.com/blog/agentic-skill-decay/ — turn corrections into lint rules, tests and type constraints. Re-read 2026-10-12.
- S209 — MIT Missing Semester 2026, "Beyond the Code" (lectures 2026-01-12 to 01-23; still current) https://missing.csail.mit.edu/2026/beyond-code/ — copyleft licences and your employer. Re-read 2026-10-12.
- S232 — GitHub, "References to matching public code" (undated live docs) https://docs.github.com/en/copilot/concepts/completions/code-referencing — under 1% of suggestions match public code, detected licences recorded, you remain responsible. Re-read 2026-10-12.

Real questions quoted below also come from S142 (Ask HN, "Client took over development by vibe coding. What to do?", 2026-04-01, re-read 2026-10-12) and S231 (Ask HN, "Vibe-coded prototypes: what happens when they go into production?", early 2026, re-read 2026-10-12); credit them where the question appears.

## Show it for real
- **Volume next to outcomes:** a terminal replay of `git log --oneline` scrolling through a month of agent commits on the worked project, then a short card of its four outcome numbers (bugs users reported that no check caught, rollbacks, time to recover, active users). Proves the commit count answers none of the four questions (S035, S036). Use the real project's real numbers, or leave the card out.
- **A dependency arrives:** in a test repo that already uses one HTTP library, ask the agent for a feature and show the manifest (`package.json` or `requirements.txt`) gaining a second one in the diff while the tests stay green. Then add the allowed-libraries rule to the instruction file and a CI check that fails on any new dependency, run the same request, and show it stopped. Proves written rules plus checks, not memory, hold the line (S004, S036).
- **Greppable names:** `grep -rn process` returning hundreds of hits, then a distinctive name returning one. Proves why distinct names let an agent find every caller (S029).
- **The live view is not the record:** a `PostToolUse` hook with an `Edit|Write` matcher running Prettier on an edit, then the same file changed through a Bash command with no hook firing, then the final `git diff` showing both. Proves why the final diff is what you review (S127, S035).
- **A gate that blocks:** a Stop hook that runs the linter and refuses to let the turn end until it passes, with its real output. Proves the difference between a rule the agent reads and one it cannot skip (S117).
- **What a fix leaves behind:** after one agent fix, the three files it added (the regression test, a synthetic user-journey check, an ownership note). Proves the leave-behinds are concrete (S036).
- **A licence list:** the agent listing each dependency's licence, one copyleft entry boxed. Proves the agent can list them and a person decides (S209, S232). Brief.
- Safety: test repos only, no real keys or personal data, demo git identity; check every still (docs/showing-real-computer-actions.md).

## Questions this lesson answers
- "Can I ship and maintain this without a developer?" (Hacker News, early 2026, S231): small apps for a few people usually keep working; ones that grow get shut down or taken over by professionals. And from S142 (2026-04-01): commenters say "the most expensive part of software is maintenance" and recommend practising at least one rollback.
- "Who owns code someone else generated, and who gets blamed when it breaks?" (S142): commenters disagree on paper, but warn that the person who ships it is the one blamed.
- "How do I know if the agent made my project better, or just bigger? Does AI actually make developers more productive?" (surveys-and-learning #08 and practitioners-now #31, via C020).
- "Why does the AI use a different library than the rest of our code? How do I stop it adding packages? How does it learn our conventions?" (C053 gap items, S004, S029).
- "Does code quality still matter if the AI writes it? Will I be able to change this app later?" (C054 gap items, S029, S034, S035).
- "Why is the AI writing Python scripts to edit my files? Why do its tests look so strange?" (C054 gap items, S035).
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Deciding what is worth building; explaining before you merge; mentoring and keeping your judgment → idea-to-launch-end-to-end
- Instruction files, hooks, deny rules and CI as enforcement; stale instruction files → rules-it-reads-rules-it-cant-break
- Skills as written procedures → skills-mcp-hooks-and-plugins
- Accepting work on records the agent cannot write; proving a gate fires on a planted violation → checking-what-you-cant-read
- Vetting new dependencies, invented package names, a minimum release age → other-peoples-code
- Rollbacks that leave data untouched; local, preview and production → from-your-laptop-to-a-url
- Watching from outside and at the destination → green-is-not-success
- Accounts behind the app, recovery codes, a second owner → every-automation-runs-as-someone
- Patches and the ship decision after launch → before-you-ship-who-signs-off
- Spending caps that stop → know-your-meter
- What you know goes stale in weeks; the map rebuilt as the gaps move → the-hidden-curriculum
- Model and media licences → own-it-sell-it-publish-it

## Out-of-date framings to avoid
- "AI makes you X% more productive, so more output is better" (S082).
- "If the PR merged, the work is done" (S082).
- "Lines, commits or tokens measure progress" (S035, S036, S118).
- "Longer autonomous runs get more done" (S035).
- "Once it ships, it's done" (S142, S115).
- "If it works, it's fine" (S004).
- "Code review only exists to catch bugs" (S029).
- "Clean-code style rules are the measure of quality", and its opposite, "code quality is irrelevant if only agents maintain it" (S034, S035, S029).
- "The agent's live edit view shows every change it makes" (S035, S117).
- "A hook on file edits catches every file change" (S127).

## Legacy notes
No legacy lesson covers this slot.

Research notes for the builder: the shared web-search budget for this turn was used up, so no new searches were run; every source above was re-opened directly by URL on 2026-10-12. Gaps worth filling when searching is possible: a current (since 2026-07) postmortem of a small AI-built app maintained after launch, and a current source on agents adding dependencies (C053 still has none).
