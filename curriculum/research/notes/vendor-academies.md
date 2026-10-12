# Research notes: What the tool makers now teach beginners

Theme: what the tool makers now teach beginners, and what a beginner course for non-coders still leaves out.
Batch read on 2026-10-12. Every point below comes from a page, transcript, slide deck or repository file fetched and read on that date. Dates were checked on the page itself or, where the page shows none, from its metadata (noted per source). Points are paraphrased; each source has at most one or two short marked quotes.

How the gated material was read (no account was created anywhere):
- Anthropic Academy lesson pages need a Skilljar login. The public course page embeds the full catalog record for each course (overview, per-section descriptions, stats) and links to the course's own slide screenshots on a public bucket. Those were read and the slide images viewed. The lesson videos and "Try it out" exercises were not readable.
- The OpenAI Academy replay page is public; its Vimeo player exposes an auto-generated English caption track, read in full (about 59 minutes). The slide deck PDF (36 pages) is linked publicly from the event page.
- DeepLearning.AI lesson pages embed each video's caption text; those transcripts were read.
- The web-search budget for this run was exhausted, so no extra companion sources were searched for. Only the listed URLs, and links found on them, were fetched.

---

## S005 - Claude Code 101 (Anthropic Academy)

- **Author:** Anthropic Academy
- **Date:** The page shows no date (footer "© 2026"). The course's own slide assets carry upload timestamps of 2026-04-09 in their file names, so the course has existed since about April 2026; it is live on 2026-10-12. The brief's 2026-10-05 does not appear on the page. Treat as 2026, within the last 12 months.
- **URL:** https://anthropic.skilljar.com/claude-code-101
- **Format:** 12 lectures, about 1.5 video hours, 1 quiz. Prerequisites: basic familiarity with a code editor and the command line; a Claude Pro, Max or Enterprise account, or an API key.

**Summary.** Anthropic's entry course for its coding agent, aimed both at people just entering software engineering, who should learn agent workflows from day one, and at experienced engineers who have not tried agents. It starts from first principles: how a coding agent differs from a chat assistant, the agentic loop, and how the context window, tools and permissions decide what the agent can see and do. It then covers install surfaces (terminal, VS Code, JetBrains, Claude Desktop, web; a screenshot also shows the Claude in Chrome extension), approval mode vs auto-accept vs Plan Mode as levels of oversight, the Explore → Plan → Code → Commit rhythm, code review with the agent, the context commands /compact, /clear and /context, and customisation: CLAUDE.md as persistent project memory, subagents, skills, MCP servers and hooks.

**Syllabus (in order):**
1. What is Claude Code? - What is Claude Code?; How Claude Code works. Agent vs chat; the loop drawn as your prompt → gather context → take action → verify results → done, with a side input where you interrupt, steer or add context; tools and permissions govern each step.
2. Your first prompt - Installing Claude Code; Your first prompt. Approval mode, auto-accept and Plan Mode, framed as choosing how much oversight a task needs.
3. Daily workflows - The explore → plan → code → commit workflow; Context management (/compact, /clear, /context); Code review (screenshot: spawning a `code-reviewer` subagent on the code just written).
4. Customizing Claude Code - The CLAUDE.md file; Subagents (delegate work and keep the main context clean); Skills; MCP (screenshot: connecting a Linear MCP server); Hooks (deterministic control of formatting, command blocking and notifications; screenshot of hooks in `.claude/settings.json`).
5. Quiz.

**Related, on the same page:** the catalog record of the follow-on course "Claude Code in Action" (undated) lists objectives that extend this: choose a permission mode per job from hands-on review to unattended pipelines; enforce rules that must not be skipped with hooks; keep CLAUDE.md lean so it is followed; package a verification skill that checks the agent's work; and verify an unsupervised run more, the less you watched it.

**Gaps it shows (topics the vendor now teaches a new developer on day one):**
1. **The agentic loop is the mental model, not the chat box.** Gather context, act, verify, repeat, with the human able to interrupt and steer mid-loop. The agent runs the "verify" step; deciding what counts as verified stays with the person.
2. **Oversight is a setting chosen per task.** Approval mode (approve each step), auto-accept (edits go through), Plan Mode (plans without editing). The follow-on course extends this to unattended runs and ties verification effort to how little you watched.
3. **Explore → Plan → Code → Commit.** Read and plan before editing; commit in reviewable steps.
4. **Context is a budget.** /context shows what fills the window, /compact summarises, /clear starts fresh; subagents keep side work out of the main context.
5. **Instructions vs guarantees.** CLAUDE.md is memory the agent reads and may not follow; hooks are code that runs every time. The follow-on course puts each rule on the surface that can enforce it.
6. **The agent reviews code too.** A reviewer subagent checks changes before they land.
7. **Extending the agent:** skills, MCP servers, subagents.

**What it teaches that our current (pre-rework) curriculum lacks or only names:** Plan Mode and the approval / auto-accept / plan choice (only 14.12 mentions permission prompts); the explore-plan-code-commit rhythm; the agentic loop as an explicit model with a verify step (00.04 stops at "an agent is a car allowed to drive"); /context, /compact and /clear as everyday commands (03.10 is generic and still todo); hooks as deterministic guardrails as opposed to instruction files (no lesson); having the agent review code before it lands (08.06 covers human pull requests); verification effort scaled to how unattended the run was.

**What it leaves out (by its own syllabus):** no lesson on security review of what the agent built, on tests as the definition of done, on secrets and keys, or on deployment. Code review is one lesson with no stated objective.

**Framing it treats as outdated:** a coding assistant that suggests code for you to paste. The overview addresses people who tried an assistant and were underwhelmed, and promises to show what changes when you work with an agent.

**Quote:** "gather context, take action, verify results" (section 1 description).

---

## S006 - AI Capabilities and Limitations (Anthropic Academy)

- **Author:** Anthropic Academy
- **Date:** The page shows no date. The Wayback Machine has a 403 capture on 2026-03-31 and its first full capture on 2026-04-07, so it was live by early April 2026. The brief's 2026-10-05 does not appear on the page. Treat as 2026, within the last 12 months.
- **URL:** https://anthropic.skilljar.com/ai-capabilities-and-limitations
- **Format:** 13 lectures, about 0.25 video hours, 1 quiz. No prerequisites and no technical background assumed. Audience: anyone who uses or is about to use generative AI (educators, students, knowledge workers, team leads).

**Summary.** The vendor's current "how AI works" course for non-technical people, built as the companion to the 4D Framework: the 4Ds are the human competencies, this course covers the four machine properties they respond to. It opens on the familiar confusion (a polished summary followed by an invented citation; a detailed instruction followed, then a simple one ignored) and argues these moments only feel random without a mental model. Each property sits on a spectrum from capability to limitation and is paired with a hands-on exercise. The last section shows how the properties collide in real tasks and gives a three-step diagnostic for any unexpected output.

**The four properties (from the section descriptions):**
1. **Next Token Prediction** (where answers come from). Answers are built one token at a time. Strong on well-worn paths such as summarising and reformatting; can produce things that sound true and are not; learn to spot when a task needs more than prediction.
2. **Knowledge.** A model knows what appeared in its training data often, recently and consistently. Strong on mainstream topics and popular programming languages; weaker on anything rare, recent, niche or contested. Practise placing a question on that spectrum to decide when to trust it and when to bring your own sources.
3. **Working Memory.** The context window is all the model can attend to right now. Covers what fits, what silently drops off, why attention is uneven across a long document, and why a new session does not remember the last one. Size the task against the window before starting.
4. **Steerability.** Short, concrete, checkable instructions (a table; a word limit) land reliably; long reasoning chains, abstract requests and demands for exact precision are where steering slips. Rewrite a wobbly instruction into a followable one.
- "Getting started" narrows "AI" to large language models and explains how pretraining and fine-tuning turn a raw text predictor into an assistant (lesson "How AI Gets Its Character").

**When properties collide:** a long contract review strains working memory while reaching past the model's knowledge; a vague creative brief tests steerability exactly where prediction fills gaps with something plausible.

**Diagnostic:** (1) name the property in play, (2) place the task on that property's spectrum, (3) apply a targeted fix rather than retrying.

**Comparison with S011** (Zhicheng Lin, "Six misconceptions about large language models: A minimal model and diagnostic taxonomy", PNAS Nexus 5(7), 2026-07-08, https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/, fetched for this comparison):
- Both replace "it's just autocomplete" with a predictor shaped by training (S006's character lesson; S011's point that instruction tuning and RLHF change the same weights rather than adding a filter).
- S006 is model-centred. S011's first distinction is pretraining vs the deployed system: inside tools, retrieval and an action loop the behaviour differs, so capability claims must name the system (its example: a tool-augmented model scoring 0.83 on a genomics benchmark where models without tools scored 0.00-0.44, with the model unchanged). S006's section descriptions do not mention tools, web search or the harness.
- Memory: S006 teaches the window and that a new session forgets. S011 says both "it remembers me" and "it remembers nothing" are wrong, because there are three layers: weights, context window, and external product storage (profiles, logs, retrieval stores). Taught alone, S006's line misleads users of products that have memory features.
- S011 adds decoding settings (temperature, sampling) as a cause of bland or variable output, and competence vs agency. S006 has neither.
- S006's diagnostic is more usable for a beginner than S011's research taxonomy. A lesson could combine S006's four properties with S011's "model vs deployed system" and its three memory layers.

**Gaps it shows:**
1. **Unexpected output comes in types, each with its own fix.** Invented fact → knowledge or prediction limit → bring sources. Ignored instruction → steerability → make it short, concrete, checkable. Forgotten detail → working memory → shrink or restart the context.
2. **Recency and rarity predict unreliability.**
3. **Checkable instructions steer best;** taste words and long reasoning chains slip.

**Framing it treats as outdated:** output as random; retrying without diagnosing.

**Quote:** "respond with a targeted fix instead of a generic retry" (course overview).

---

## S007 - AI Fluency for Builders (Anthropic Academy with CodePath)

- **Author:** Anthropic Academy, built with CodePath from research with engineers and product builders. Presenters on the slides include Michael (CodePath) and Kristen (Anthropic).
- **Date:** Coursera shows "Recently updated! September 2026"; the page metadata gives a launch of 2026-09-29. The Skilljar version (https://anthropic.skilljar.com/ai-fluency-for-builders) is older: its slide assets carry upload timestamps of 2026-05-13 and 2026-06-24. Confirmed: September 2026 on Coursera.
- **URL:** https://www.coursera.org/learn/ai-fluency-for-builders
- **Format:** Coursera: 6 modules of readings, about 5 hours, beginner, free, no certificate. Skilljar: 10 lectures, about 1 video hour, 1 quiz. Examples use Claude.ai; any assistant works.
- **Read:** Coursera page and module list; the Skilljar catalog record (section descriptions); 12 public slide images (marked CC BY-NC-SA). The lesson readings are behind enrolment and were not read.

**Summary.** The 4D Framework (Delegation, Description, Discernment, Diligence) applied to building, from framing a customer problem to shipping. It counts product people, engineers and makers as builders. Builders hand AI a reusable brief carrying their values, constraints and context; tell the inner loop from the outer loop; decide what to delegate and which judgment to keep; write acceptance tests that define done before any code exists; follow a "Description Chain" from a messy user need to a precise instruction; evaluate AI-generated code through five lenses and critique AI-built user experiences with actionable feedback; and own what ships, from whether it should exist to whether it serves users after launch, deciding to ship, fix or stop with feedback loops and tests as the safety net.

**Module list (Coursera):** 1 Introduction and AI Fluency framework (Welcome; The 4D Framework). 2 How AI works (AI capabilities & limitations). 3 The 4D framework for builders (Delegation & the builder's toolkit; Description & building great things). 4 Discernment for builders (Discernment for code; Discernment for user experience). 5 Tying it all together (Stand behind what you build). 6 Wrapping up. Skill tags include Acceptance Testing, Code Review, Software Technical Review, Context Engineering, Responsible AI.

**What the slides show (paraphrased):**
- Diligence: owning what you build and keeping your AI use transparent, ethical and accountable.
- Delegating as a builder is two decisions: what to delegate, and how.
- Four steps toward good Description: user voice → product requirement → technical spec → AI instruction.
- When the user need is badly translated: the code works but the product doesn't; tests pass but don't solve the real problem; the failure sits upstream of the prompt.
- Discernment for code, lens "Responsible impact": is it responsible; bias, privacy and unintended consequences; don't let code carry harmful assumptions forward. Only this one of the five code lenses is publicly visible.
- Discernment for UX, "Clarity": form and function together, respecting users' mental models; users bring expectations from other software and the world; map the interface to concepts they recognise.
- Building confidence: start with a specific recurring task, compare with past examples, keep testing, note what the AI gets right and wrong, refine and test again.
- The context window holds your prompts, the AI's responses and anything else you shared.

**Gaps it shows:**
1. **"It works" is not the finish line.** A builder judges product fit, UX clarity and responsible impact, not only whether code runs.
2. **Define done before code exists:** acceptance tests from the user need, not from what the AI produced.
3. **Most failures start upstream of the prompt:** a need badly turned into a requirement yields passing tests for the wrong product.
4. **Ownership continues after launch:** ship, fix or stop from feedback and tests; ask whether it should exist.
5. **Calibrate trust per task** on work whose right answer you already know.

**Framing it treats as outdated:** working code as the finish line; prompting as the whole skill.

**Quote:** "'it works' stops being the bar" (section 4 description).

---

## S008 - Codex Bootcamp 101: Agentic coding (OpenAI Academy livestream and slide deck)

- **Author:** OpenAI Academy. Presenter Marcus Stallworth (Builder ADM, OpenAI); Q&A with Tanner Wride (Builder ADM) and Aruna Chakkirala (AI Deployment Manager).
- **Date:** 2026-09-23, 17:00-18:00 GMT, confirmed on the event page. Replay posted 2026-09-24. The deck's model slide is labelled task guidance of 22 September 2026.
- **URL:** https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c
- **Also read:** the replay https://academy.openai.com/public/videos/september-23-codex-bootcamp-101-2026-09-24 (auto-generated captions, about 59 minutes; model names are garbled in places) and the deck "Codex Bootcamp 101 - Sept" (36 pages, linked from the event page; every slide is marked confidential although the deck is publicly linked): https://d2xo500swnpgl1.cloudfront.net/slide-upload/oaiacademy/Codex-Bootcamp-101-Sept-29911778-d7ed-4e74-b028-f5ff6f6782c7-1790179444559.pdf

**Summary.** OpenAI's intro to agentic coding in the Codex app (now inside the ChatGPT desktop app), pitched as shipping production-ready code with agents. It names three phases of AI in software (code completion, pair programming, agentic delegation) and four habits: delegate a bounded task; prepare the repository; review the evidence; reuse what works. Its loop is Prompt → Inspect → Act → Validate → Report, then human review that accepts, asks for fixes or stops. It teaches a read-only "map the repository first" prompt, a four-part prompt (goal, context, constraints, done-when), layered AGENTS.md files, model choice and reasoning effort as separate dials, a six-step engineering workflow with an artifact per step, three pre-acceptance questions, subagent patterns, and what to do when progress stalls. The presenter's theme: you are now a manager of agents, so keep their work small enough to review.

**Points (deck slide / talk minute, paraphrased):**
- **Three phases** (slide 5; talk 08:01-09:01): suggest the next line → chat while coding → delegate the whole task.
- **Prompt into evidence** (slide 7): Prompt (goal, context, constraints, done criteria) → Inspect (read relevant files, find existing patterns) → Act (edit, run commands, use connected tools) → Validate (run checks, fix failures) → Report (changes, evidence, remaining risks). Every file read and check adds context for the next step. Human review: accept, ask for fixes, or stop.
- **Surfaces** (slide 8): Chat while the answer is still forming; Work when the output is a knowledge artifact; Codex when the output is working software.
- **Map the repository first** (slide 11): directories and responsibilities, the files behind the core user flow, conventions to keep; install, run, test, lint and build commands and the safest way to validate a small change; cite files; keep verified facts apart from assumptions and flag uncertainty; no edits yet. Review the map, then delegate.
- **Define done** (slide 13): Goal: change a savings APY shown as 4.02% to the approved 4.20%. Context: find where the homepage value comes from and the relevant tests. Constraints: small change, leave unrelated work alone. Done when: regression test added, checks run, evidence reported. Talk (36:01): without a definition of done the model invents its own; give goals, boundaries and a way to verify.
- **Manager of agents** (talk 37:03): if the agent does more than you can review, you cannot manage it; ask for bounded, smallest changes.
- **AGENTS.md layers** (slide 14): personal (`~/.codex/AGENTS.md`), project (`AGENTS.md`), folder (`src/AGENTS.md`); they combine and the more specific rule wins. Talk (55:02-57:01): keep it to roughly 200-300 lines; use it as a map of the repo and how to use each part (plus a rubric for plans), not as the home of every guardrail; settings like default reasoning go in `config.toml`; Codex can draft it.
- **Model vs effort** (slides 16-19): pick the model for the task and the effort level for its complexity (Low → Medium → High → Extra high → Ultra); more effort costs more time and tokens; use the lightest setting that meets your quality bar; adjust from evidence (missing context → add files; competing approaches → more effort; still short → try a stronger model). Talk (20:02-21:00): Ultra spawns parallel agents and burns many tokens; OpenAI says it does not want "token maxing".
- **Loop limits** (talk 41:01-42:02): when asking it to implement, review and fix until checks pass, cap the rounds or give exit criteria so a ten-minute job doesn't run for an hour.
- **Engineering workflow** (slide 25): choose the task (requirement, acceptance criteria) → prepare the workspace → reproduce the issue (failing test) → plan and implement (approved approach, focused diff) → verify and review (check results, reviewable PR) → update the record (outcome, evidence, remaining work).
- **Before you accept** (slide 26): Does the diff match the requested scope? Which checks ran, and which passed, failed or were skipped? What is still unverified, and what happens next? Accept only when the evidence meets the goal, else ask for a specific fix or stop. Talk (31:01-35:02): watch what it is doing, since you may know something you didn't tell it; steer mid-task; read the diffs so you can explain them.
- **Subagents** (slide 27): review loop (read-only review → fix confirmed findings → recheck); parallel build with explicit file ownership; compare strategies against the same success criteria; specialists with a bounded task, context and handoff; inspect each agent's evidence before accepting the combined result. Talk (45:01): beginners should not start with multi-agent proposals.
- **When progress stalls** (slide 28): name the failure, then change the input. Missing context (guessing about files or rules) → have it read the named file and state the constraints before editing. Scope drift → pause, keep only the requested scope, list the rest as follow-ups. Failed checks → reproduce, fix the cause, rerun the check, report.
- **Connected tools** (slides 21-22; talk 11:01-13:04): plugins connect Codex to services, with ticket updates done under explicit authorisation; scheduled tasks repeat a workflow; the presenter connects Gmail, Drive, GitHub, Atlassian and Slack and still checks every update because he is responsible for the work.
- **Third-party skills** (talk 52:01-56:02): be sceptical of skills others built; be very careful running executables; usually rebuild the skill yourself from examples of its output; inside a company, an undocumented skill should not be trusted; scan with a security plugin.
- **Coach prompt** (slide 30): a scheduled skill that reviews your Codex history and recommends changes, and must ask before installing anything or changing shared instructions.

**Gaps it shows:**
1. Define done (goal, context, constraints, done-when) before delegating.
2. Map before editing; make the agent separate verified facts from assumptions.
3. Keep tasks small enough to review; scope drift is a named failure.
4. Read the report for what was skipped and what is unverified, not only what passed.
5. Model and reasoning effort are two cost dials; cap loops.
6. Diagnose a stall (missing context, scope drift, failed checks) rather than re-prompting blindly.
7. Instruction files are short maps, layered personal → project → folder.
8. Connectors act with your access; writes need explicit authorisation.
9. Someone else's skill is untrusted code.

**Framing it treats as outdated:** AI as next-line completion (phase 1); "prompting is dead" (the presenter disagrees, 36:01); vibe coding as the goal rather than value you can deploy (09:01); spending tokens for their own sake.

**Quotes:** "A good prompt defines done." (slide 13). "Inspect each agent's evidence before accepting the synthesis." (slide 27)

---

## S009 - Test and Debug with GitHub Copilot (GitHub Skills exercise)

- **Author:** GitHub (GitHub Skills); commits co-authored by Aaron Stewart and the Copilot App.
- **Date:** Repository created 2026-09-29; the exercise content was committed on 2026-09-30 (three commits). Confirmed through the GitHub API.
- **URL:** https://github.com/skills/test-and-debug-with-github-copilot
- **Read:** README, the DEBUGGING.md template, all five step files and the review page (`.github/steps/1-step.md` to `5-step.md`, `x-review.md`).

**Summary.** A 45-minute exercise for developers with basic Python. A bill-splitting library passes its tests, yet a customer reports totals off by a cent. The learner investigates before editing (Copilot explains; the learner records the baseline test run and a falsifiable hypothesis), gives Copilot an explicit behaviour contract for new tests, adds edge cases that check an invariant (the shares must sum to the rounded total, to the cent), uses the failing tests to get a diagnosis, approves a plan before the fix (integer cents, quotient and remainder, leftover cents to the earliest shares), and opens a pull request with a "Verification" section and a "Copilot review" section, checking every Copilot claim against code and tests.

**Gaps it shows:**
1. **An AI explanation is not proof.** Copilot is a partner, not an authority: keep a suggestion only once it is tied to code, test output or an invariant. Treat Copilot's review of the diff as one more hypothesis to check.
2. **Tests from vague prompts mirror the implementation.** Give explicit inputs, outputs, names and constraints; read each assertion; a passing test is worth something only if it proves something intended.
3. **Never compute the expected value with the code's own formula.** If a generated test recomputes the answer the way the production code does, replace it with a literal expected value.
4. **Generated tests over-sample common inputs.** Add rounding, boundary, invalid-data and invariant cases. The original tests passed because $42.00 / 3 and $80.00 / 4 divide evenly; $10.00 / 3 must give 3.34, 3.33, 3.33.
5. **Don't weaken expected values to match buggy output;** reject plans that change expected values, weaken tests or add unrelated dependencies.
6. **A convincing diagnosis explains both the failure and why the other tests passed.**
7. **Passing tests don't prove every suggestion was right.** Inspect the diff, tie each change to a requirement, and record what you verified yourself.
8. **Domain detail the agent won't volunteer:** rounding each share separately loses or invents money; use integer cents and spread the remainder; avoid binary floating point.

**Tension (flagged by Aaron):** this exercise, published 2026-09-30, still has the human write the debugging hypothesis and treats Copilot as the explainer. Cursor's lesson (below) gives hypothesis-forming and instrumentation to the agent. The human part common to both: the behaviour contract (what the right answer is), the invariant, the reproduction, and judging whether the evidence supports the claimed cause.

**Quote:** "Its explanation is not proof." (step 1)

### Companion: Cursor Learn, "Finding and fixing bugs"

- **Author:** Cursor (Anysphere); no byline.
- **Date:** Undated on the page and in its metadata. The Wayback Machine first captured it on 2026-02-16; its 2026-09-02 capture is about twice the size of earlier ones, so the page had been revised by then. Read live on 2026-10-12.
- **URL:** https://cursor.com/learn/finding-fixing-bugs (chapter 4 of 7 in "Coding Agents"; Cursor Learn also has an "AI Foundations" track: How AI models work, Hallucination & limitations, Tokens & pricing, Context, Tool calling, Agents).

**Summary.** The fundamentals hold whoever does the debugging: a reliable reproduction, a minimal case, one change at a time, specific hypotheses, instrumentation, a regression test. For simple errors you paste the error and when it happens, and the agent reads the stack trace and patches. For hard bugs, Debug Mode generates hypotheses, adds targeted logging, asks you to reproduce the bug while it collects data, analyses the logs and makes a targeted fix. Hard bugs can go to several models in parallel; keep the fix with the strongest evidence and judge the reasoning, not only the result. The agent can work from code alone, from pasted runtime evidence (terminal output, a Postgres EXPLAIN ANALYZE), from the integrated browser (console, network, DOM), and from Sentry, Datadog, databases or issue trackers over MCP; monitoring alerts can start an investigation before a human looks. The failure pattern: accepting a fix you don't understand, such as a null check that hides a data inconsistency.

**Gaps it shows:**
1. **Debugging is now agent-led evidence gathering.** For a bug that appears only when two users edit at once, the lesson's quiz answer is Debug Mode (instrument, reproduce, analyse), not reading the code by hand.
2. **The human's inputs:** a reliable reproduction (exact steps, inputs, conditions), when it happens, and the judgment of root cause vs hidden symptom (why is the value null; what changed).
3. **Agents give plausible but wrong explanations;** confirm the cause with the investigation's data.
4. **Every fix ends with a regression test.**
5. **Production observability is part of debugging now** (Sentry, Datadog via MCP; alert-triggered agent runs).

**Quote:** "agents can hallucinate plausible-sounding explanations" (failure-pattern section).

---

## S010 - Build with Andrew (DeepLearning.AI)

- **Author:** Andrew Ng, DeepLearning.AI (contributors named in the last video: Summer Rae, Andres Gonzalez, Tommy Nelson).
- **Date:** "Updated Jul 17, 2026", confirmed on the page.
- **URL:** https://www.deeplearning.ai/courses/build-with-andrew
- **Format:** 1 hour, beginner, 5 videos, 3 chatbot readings, 2 graded items (Pro), for people who have never written code. All five video transcripts were read from the lesson pages.

**Summary.** A no-code first build. You prompt any chatbot (ChatGPT, Gemini, Claude or the site's own) to write a single HTML page, download it, double-click it in your Downloads folder, and iterate. The prompt "building blocks" are goal, input, output, layout and special features; more specific prompts give more predictable results, and the same prompt gives a different app each run. Projects: a birthday-card generator, a ping-pong game, and a fill-in-the-blanks story app as the final project, which an AI grader checks for whether it appears to work. Bugs are handled by describing the symptom to the AI and downloading the new file; the learner is told not to bother with the AI's technical explanation. Andrew closes by warning that people who only build, without courses, miss core concepts and can spend months reinventing the wheel.

**What it teaches:** describe (five building blocks), generate, download and open, iterate, ask the AI for feature ideas, report symptoms to the AI, show the app to people for feedback.

**What it leaves out (evidence of the gap):**
1. **Testing:** none; "does it work" is clicking plus an AI grader.
2. **Hosting and sharing:** the app is a local HTML file; sharing with friends is never explained beyond the download.
3. **Security, keys, data and accounts:** not mentioned. The chosen apps have no server, no stored data and no users.
4. **Costs and limits of the AI tools:** not mentioned.
5. **Understanding the fix:** the learner is told to skip the explanation and just see whether the new file works.
6. **What makes an app hard:** absent here; the companion course only says an internet multiplayer game is much harder.

**Framing to avoid (ours, from this evidence):** if it runs when I click it, it's done.

**Quote:** "just don't worry about what the AI is saying here" (Customize your app).

### Companion: AI Prompting for Everyone (DeepLearning.AI)

- **Author:** Andrew Ng, DeepLearning.AI. **Date:** "Updated Jul 24, 2026" (confirmed). **URL:** https://www.deeplearning.ai/courses/ai-prompting-for-everyone
- **Read:** transcripts of "Pretrained knowledge", "Web search", "Web search sources", "Sycophancy" and "Building apps".

**Summary.** Pretrained knowledge mirrors how often something appears in the training text (cooking: a lot; quasars, Cantonese: little; your company's private data: nothing) and includes misconceptions and outdated material. Training stops at a knowledge cutoff; questions about recent, local or niche things trigger web search, or you can ask for it. Web search draws on what is most available rather than most reliable (he cites one report ranking Reddit first among sites AI cites, then Wikipedia and YouTube) and can surface pages decades out of date (his example: a running spot recommended from a twenty-year-old page, now closed to the public); ask for official or scientific sources. Under the hood a helper model searches and summarises pages for the model you talk to, so the answering model may cite a page whose summary it misread. Sycophancy: models trained on thumbs-up feedback learn to agree; he cites a Washington Post analysis finding about ten times more agreement than disagreement; leading questions and subtle cues (asking only for the positive measures) bend the answer; use neutral framing and ask for pros and cons. Building apps: start with self-contained apps that need no uploaded files or outside information.

**Gaps it shows:**
1. Know the knowledge cutoff and whether the tool searched; recent and rare means less reliable.
2. Ask for source types and open the cited page, since the answering model may have seen only a summary.
3. Leading questions get agreement; ask neutrally.
4. Self-contained apps are the easy case; data, users and networks are where difficulty starts.

**Quote:** "it's only seen summaries of those web pages" (Web search sources).

---

## Cross-source observations

- **Who the vendors now teach:** Anthropic teaches its coding agent to people just entering software engineering (S005) and counts product people, engineers and makers as builders (S007); OpenAI's bootcamp shows non-engineering builds (games, product launches, 3D rooms) beside repo work (S008); Andrew Ng tells first-time HTML builders they are builders now (S010).
- **Shared spine across vendors (S005, S007, S008, S009, Cursor):** define done first → agent explores and plans → keep the change bounded → agent acts and runs checks → human reviews the evidence (diff, checks run or skipped, unknowns) → regression test → own the result.
- **What none of these beginner courses teaches:** security review of what was built (S005's syllabus has none; S008 mentions a security plugin in passing; S010 never mentions security), secrets and keys, deployment, or cost control beyond S008's effort dial. The non-coder course (S010) stops exactly where real apps begin: data, users, accounts, a server.
- **Debugging has moved:** Cursor's Debug Mode hands hypotheses and instrumentation to the agent; GitHub's September 2026 exercise still has the human write the hypothesis. Both keep the reproduction, the expected behaviour and the root-cause judgment with the human.
