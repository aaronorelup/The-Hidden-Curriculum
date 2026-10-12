---
key: what-the-agent-sees-each-turn
id: 05.01
title: What the agent sees each turn
district: Directing Well
module: 05 What the agent sees
status: todo
legacy: []
minutes: [5, 6]
concepts: [C025, C026, C027, C028]
sources: [S002, S003, S107, S105, S001, S004, S008, S012, S015, S016, S036, S037, S101, S103, S128]
lead: [S002, S107]
---
# What the agent sees each turn

**Purpose (the first spoken sentence):** In this lesson you'll learn what your agent actually receives every time you press Enter, why it works worse as that package grows, and the three habits that keep it small: clear once a decision is made, carry plans in files, and brief helpers fully.

**Conclusion:** Every turn the agent re-reads one big package that is mostly text you never typed, and the fuller it gets the worse it works, so you decide what goes in, when to start clean, and what a helper agent must be told.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; module 05 What the agent sees (first lesson of the module). Builds on 00.02 `model-harness-and-memory` (a model inside a harness; weights, window and memory files).

**Lead source (audit, 2026-10-12):** S002 (Mihail Eric, Stanford CS146S); S107 (Rogerio Chaves (LangWatch)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S002, S003, S107, S105); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

*Length (audit, 2026-10-12):* about 5-6 minutes; COURSE.md (Aaron, 2026-10-01) gives orientation lessons and the first lesson of every module about 5 minutes. C025 and C026 are taught at the points marked teach; C027 and C028 get one line each (clear after deciding and carry the plan in a file; a subagent starts blind and returns a summary). Every point marked brief becomes one line, and every point marked one line moves to the lesson page.

## What to teach (binding scope)

### C025 What one request contains: the whole package is resent every turn
- **The model keeps nothing between requests; the harness resends everything.** Each turn's input "contains all previous conversation history plus the current user message", and everything in the request counts: system prompt, every message (tool results, images, documents included), tool definitions, and the reply with its thinking (S012). Claude Code's own docs: "The model doesn't remember anything between requests, so Claude Code re-sends the full context" (S128). — **teach**
- **Most of the package is loaded before you type.** In Anthropic's walkthrough a fresh Claude Code session holds a system prompt (about 4,200 tokens in the simulation), auto memory (the first 200 lines or 25KB of MEMORY.md), environment info, MCP tool names, skill descriptions and your CLAUDE.md files before the first prompt; the docs' line is "Your prompt is tiny compared to what's already loaded" (S105). The Stanford lecturer, reading an intercepted request: "By my first request, perhaps tens of thousands of tokens have already been consumed by material outside my control" (S002 line 232). — **teach**
- **Text you never typed rides inside your own message.** In the intercepted request, everything above the lecturer's typed question was "part of this user block, but it isn't something I explicitly entered there… The harness added it behind the scenes", including a system reminder carrying his CLAUDE.md that "says these instructions override default behavior and must be followed exactly as written" (S002 lines 277-282). Claude Code also adds output-style instructions, a note when a file it read changes on disk, and the commit and pull-request attribution lines (S101). — **teach**
- **The terminal hides what enters.** You see "Read auth.ts" while 2,400 tokens of file content go in, and a pass count while 1,200 tokens of test output go in (S105). — **teach**
- **Tool definitions are prompt text.** A tool's description, comments, name and full signature "becomes part of your prompt", and that is what the model uses to decide when to call it (S002 lines 93-95). — **one line** (cost of extensions belongs to 05.03)
- **Caching changes the price, not the size.** "Cached prompt prefixes still occupy the context window: prompt caching changes what you pay for those tokens, not whether they count" (S012); "a one-line question in a session that has been open all day still draws usage for the whole conversation" (S016). — **brief** (meters and cache rules belong to 06.03)
- `/context` shows the live breakdown by category, including which CLAUDE.md and memory files loaded (S105). — **one line**
- Dropped here: MCP schema deferral and per-extension cost (05.03, C051); CLAUDE.md size and loading rules (05.02, C044/C046); token-counting API (API builders only).

### C026 Context engineering: the window fills and degrades, so curate it
- **Context rot.** "As token count grows, accuracy and recall degrade, a phenomenon known as context rot. This makes curating what's in context just as important as how much space is available" (S012). — **teach**
- **Advertised is not usable.** "Some have up to a million tokens, but not all tokens are created equal" (S003 line 51). LangWatch measured it across 2,451 sessions: as the window grew 16.6x (median 38,886 to 644,962 tokens), the part judged in use stayed near 8k (7,949 to 8,452), falling from 47.5% of the window below 50k to 2.5% above 600k: "the useful part stays put while the window you pay for grows around it" (S107). — **teach**. The lecturer's own paraphrase ("closer to half a million truly useful tokens", S003 line 231; "half and, at most, three-quarters… more intuition", S003 line 241) disagrees with the study; teach the measurement and say his figure is intuition.
- **Long context costs more than it looks.** "Each doubling of context costs roughly 6x more, so be deliberate about which work earns a big window" (S107). — **brief**
- **Compaction is lossy.** The median compaction turned a 574,875-token window into a 4,382-token summary; in the five steps after, 41.9% of user messages contained a correction against a 17.7% baseline, and the rate stayed high for at least 30 steps (S107). — **teach**
- **When to compact, by kind of work** (S107): driving a PR 200-250k; research 250-300k; QA 250-350k; building and code understanding 300-450k; "I could find no justifiable benefit in letting an agent run anywhere near 1M." Stanford assigned this study (S003 lines 227-231). — **brief** (show as one card, don't read the table aloud)
- **The levers in Claude Code.** Sessions on native-1M models auto-compact at about 967K tokens by default; `/autocompact 500k` compacts earlier (S015 companion: model-config page); `/compact focus on <task>` at a natural break; `/clear` between unrelated tasks ("Old conversation crowds out the files you need next and costs tokens on every message"); send large reads to a subagent (S105). — **teach**
- **Nothing warns you.** Opus 4.7 and later, Sonnet 5.5, Haiku 5.5 and the Fable and Mythos 5.x models get no injected "Token usage: X/Y; Z remaining" warnings; only older models track their remaining budget, and explicit task budgets are in beta (S012). So watch `/context` yourself. — **brief**
- Irrelevant material makes the agent worse, not just slower: "The more irrelevant material you include, the more likely the coding agent is to perform poorly" (S002 line 154). — **one line** (which extensions to prune: 05.03)

### C027 Sessions are disposable: clear after deciding and hand off through files
- **Compaction keeps a summary, not the conversation.** What comes back from disk after compaction: root CLAUDE.md and unscoped rules, auto memory, the plan-mode plan, a fresh git status, up to five recently modified files (a file over 5,000 tokens comes back as a path only), and invoked skills (5,000 tokens each, 25,000 total, oldest dropped). What is summarised away: instructions given only in chat, context hooks added earlier; path-scoped rules and nested CLAUDE.md come back only when a matching file is touched again (S105). Teach it as "files come back, chat doesn't", with the table on screen, not read aloud. — **teach**
- "Put persistent rules in CLAUDE.md rather than relying on conversation history"; "detailed instructions from early in the conversation may be lost" (S101). — **brief** (what makes a rule hold is 05.02)
- **Clear after choosing.** The Stanford lecturer admitted skipping it in his own demo: "Otherwise, both proposals remain there even though you've committed to one. That can confuse the agent about which it's implementing" (S003 line 233). — **teach**
- **Carry the decision in a file, not the chat.** "Once I see a few hundred thousand tokens, I try to write the relevant information to a file, ingest that compressed representation into a fresh context" (S003 line 235). Osmani: "Chat history isn't a great system of record, especially after compaction", and "A human picks the path" (S036). Shihipar starts implementation in a new session from the spec and prototype, which "gives Claude a fresh context window but with all of the information it compiled from your planning", and keeps an `implementation-notes.md` where the agent logs deviations (S037). — **teach**
- Handoff files go stale like memory: point to commands and config rather than copying them (S103); stale files are 05.02's subject. — **one line**
- Chat apps such as claude.ai can drop the oldest turns first in, first out (S012). — **one line**
- Dropped here: the full research → plan → build workflow (06.01, C039-C041).

### C028 Subagents start blind and return a summary
- **Fresh window in, summary out.** "Each subagent starts with a fresh, isolated context window. It doesn't see your conversation history, the skills you've already invoked, or the files Claude has already read. Claude composes a delegation message that summarizes the task" (S015 companion: Subagents docs, "What loads at startup"). In Anthropic's walkthrough the subagent read 6,100 tokens of files and 420 came back (S105). — **teach**
- **What it does load:** its own system prompt, CLAUDE.md and the same MCP and skill setup, and the task the lead agent wrote; not your history and not the main session's auto memory. The built-in Explore and Plan agents skip CLAUDE.md and the git status (S105; S015). So a constraint you said only in chat reaches the subagent only if the lead agent writes it into the brief (follows from S105). — **teach**
- **A fork is the opposite, and expensive.** A fork inherits the whole conversation. In LangWatch's audit, 82% of one day's 2.25 billion tokens came from subagents; two forked subagents (of 34) used 1.14 billion, started at 523K and 304K tokens of context against roughly 30,000 for a fresh one, and ran 10.7 and 8.7 hours; one test run at that context cost about 568,000 tokens (S107). — **brief**
- Subagent requests still draw on your usage; agent teams use about 7x the tokens of a standard session when teammates run in plan mode (S016). — **one line** (cost: 06.03; fleets: 08.01)
- **Starting blind is also the point**: a clean reviewer "is more likely to notice when a test proves the implementation while missing the requirement" (S036). — **one line** (fresh-context review: 06.02)
- The summary that comes back is a claim (S008 slide 27, "Inspect each agent's evidence before accepting the synthesis", per concepts.md; the event page re-opened 2026-10-12 does not carry the deck, so re-check before quoting). — **one line** (taught in 02.04)

## You vs the agent
As of 2026-10-12:
- **The harness and agent do on their own:** assemble and resend the package every turn; read files on demand; compact automatically near the limit; delegate side tasks to subagents and write their briefs; merge their summaries; write memos, plans and implementation notes and log deviations when asked (S101, S105, S036, S037).
- **What the agent cannot do for you:** tell you its quality is dropping (the newest Claude models get no context-budget warnings, S012); follow a constraint nobody wrote down; carry a chat-only instruction through compaction (S101, S105); see a rule you never put in the brief (S015 companion: Subagents docs).
- **You check and decide:** what enters (files, docs, servers) and which work earns a big window (S107); `/context` when results slip; when a decision is final, then write it to a file and `/clear` (S003, S036); that a delegated task carries the constraints that matter, and caps or exit criteria so a short job does not run for hours (S107's 10.7-hour forks); that each returned summary is checked against evidence (02.04).
- **Bring in someone who can:** deciding which existing docs are accurate enough to feed the agent needs a person with a map-level picture of the code (S003 lines 121-123, 141-145). Otherwise no expert is needed for this lesson.

## Sources this lesson is built from
- S002 — Mihail Eric, Stanford CS146S, "Lecture 2026-09-24: anatomy of a state-of-the-art coding agent (transcript)" (2026-09-24) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — the intercepted request: tens of thousands of tokens before the first message, the system reminder carrying CLAUDE.md above the typed question, tool definitions as prompt text, a student's "Is this all the body of one request?" (lines re-checked 2026-10-12).
- S003 — Mihail Eric, Stanford CS146S, "Lecture 2026-09-29: advanced prompting and context engineering, RePPIT (transcript)" (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — "not all tokens are created equal"; clear after choosing a proposal; write to a file and start a fresh context; bad docs versus none (lines re-checked 2026-10-12).
- S107 — Rogerio Chaves (LangWatch), "The Context Tax: When to Compact Your Coding Agent" (2026-08-02) https://langwatch.ai/blog/context-tax-when-to-compact — about 8k tokens in use as the window grows; 6x cost per doubling; compaction thresholds by kind of work; the correction rate after compaction; the forked-subagent incident (re-read 2026-10-12).
- S105 — Anthropic, "Explore the context window" (Claude Code docs; undated live docs, mentions v2.1.198; re-read 2026-10-12) https://code.claude.com/docs/en/context-window — what loads before you type; what the terminal hides; the subagent's 6,100 to 420 tokens; what survives compaction; `/compact`, `/autocompact`, `/clear`, `/context`.

Also cited for specific points (credit on the lesson page):
- S012 — Anthropic, "Context windows" (Claude Platform Docs; undated live docs listing Opus 5.5, Fable 5.1 and Haiku 5.5; re-read 2026-10-12) https://platform.claude.com/docs/en/build-with-claude/context-windows — what one request contains; context rot; cached tokens still count; which models get no budget warnings.
- S101 — Anthropic, "How Claude Code works" (undated live docs; re-read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — text Claude Code adds on its own; instructions lost at compaction.
- S128 — Anthropic, "How Claude Code uses prompt caching" (undated; mentions up to v2.1.283) https://code.claude.com/docs/en/prompt-caching — "re-sends the full context" every message.
- S015 — Anthropic, "Extend Claude Code" (features overview; undated live docs; re-read 2026-10-12) https://code.claude.com/docs/en/features-overview — what a subagent loads; with its companion pages, re-read 2026-10-12: "Subagents" (https://code.claude.com/docs/en/sub-agents, "What loads at startup") and "Model configuration" (https://code.claude.com/docs/en/model-config, the 967K auto-compact default). Suggest giving the Subagents page its own S-ID.
- S016 — Anthropic, "Manage costs effectively" (undated; no earlier than 2026-09-14) https://code.claude.com/docs/en/costs — the all-day session; subagent usage; agent teams about 7x.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — chat history is not a system of record; a human picks the path; the fresh reviewer.
- S037 — Thariq Shihipar (Anthropic), "A field guide to Claude Fable 5: Finding your unknowns" (2026-07-06) https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns — new session from the spec and prototype; `implementation-notes.md`.
- S103 — Pat2 and Dean Rie (Cursor staff), "How are people handling context across different AI coding tools?" (2026-05-06; within 12 months) https://forum.cursor.com/t/159891 — re-explaining projects to every tool; point to config rather than copying it.
- S008 — OpenAI Academy, "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — one line only, and only after the deck is re-checked.

## Show it for real
- Fresh Claude Code session in a demo repo, run `/context` before typing anything: the categories already filled (system prompt, memory files, skills, MCP tools) prove the package exists before your first word (S105).
- Ask it to read one file, watch the terminal print a one-line "Read …", then run `/context` again and point at the jump: the terminal shows a line, the window took the whole file (S105).
- One request captured through a logging proxy, as Stanford's first assignment does: collapse the tools list and system block, then find the system reminder carrying CLAUDE.md sitting above the typed question (S002 lines 97-104, 277-282). Use a demo project and blank out the API key header and any account details.
- A small script calling the API in a loop that prints the input token count each turn, so the number visibly climbs while you type one word each time (S012). Key read from an environment variable, never on screen.
- In a long session: `/context`, then `/compact focus on <task>`, then `/context` again, and open the summary that replaced the conversation (S105).
- Rule given only in chat, `/compact`, ask the agent to restate it; then the same rule in CLAUDE.md, `/clear`, and `/context` listing it as loaded: chat fades, files come back (S105, S101).
- The handoff: have the session write `plan.md`, run `/clear`, start with "read plan.md and implement it", and show `/context` nearly empty (S003 line 235, S037).
- Ask for a subagent to search the codebase, expand the Agent tool call to show the brief it was given, then `/context` to show only the summary arrived (S105). Then `/usage` and its attribution line for subagents (S016).
- LangWatch's chart of context in use against window size, as a credited screenshot (S107).

## Questions this lesson answers
- "Is this all the body of one request?" (Stanford student, S002 line 145)
- "Why is my first message already using thousands of tokens?" and "Does the model see my CLAUDE.md every time?" (batch-reader lists from S002, S016)
- "Why does Claude get dumber in long sessions?", "When should I use /compact?" and "Is a 1M-context model worth it?" (batch-reader lists from S002, S003)
- "If the project already has a lot of Markdown docs, should the agent just read them?" (Stanford student, S003 line 139; answer: only if they are well maintained, S003 lines 141-145)
- "Should I start a new chat or keep going?", "What is the difference between /clear and /compact?" and "What does 'Conversation compacted' mean?" (batch-reader lists from S003, S012, S015, S036)
- "I keep re-explaining the same things between tools" (Pat2, S103)
- "Why did the subagent ignore what we discussed?" and "What is a subagent?" (batch-reader list from S015)
- "Why does Claude use natural language rather than vectors when it kicks off agents?" (Stanford student, S002 line 159; the brief is text the lead agent writes)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Weights, window and memory files as three different stores → `model-harness-and-memory` (00.02, C023)
- What an instruction file should hold, which sessions load it, and why prose is not enforcement → `rules-it-reads-rules-it-cant-break` (05.02, C044-C046)
- What each extension is and what it costs to keep loaded → `skills-mcp-hooks-and-plugins` (05.03, C049, C051)
- Cache pricing, the meters, cost as context × turns × agents, effort → `know-your-meter` (06.03, C055-C059)
- Research, plan and build as separate phases → `plan-first-then-build-in-slices` (06.01, C039-C041)
- A subagent's summary is a claim; fresh-context review → `done-is-a-claim` (02.04, C011) and `checking-what-you-cant-read` (06.02, C014)
- Many agents at once, teams and fleets → `agents-that-run-while-youre-away` (08.01, C095)
- Everything in the package can steer the agent, including text from web pages and tools → `whose-words-is-it-reading` (07.01, C073, C086)
- Thinking tokens → deep-dive backlog (C029)

## Out-of-date framings to avoid
- "The model only sees my prompt" (S002) and "The agent sees what I see in the terminal" (S105).
- "Only my new message is sent" / "the model remembers the conversation between messages" (S012, S128).
- "Caching saves context space" (S012).
- "A bigger context window is always better; paste the whole codebase" and "A 1M window means it remembers everything I said" (S012, S003, S107).
- "Let the agent run until it compacts by itself" (S107).
- "Prompt engineering is the core skill" (S001: Stanford's 2026 syllabus replaced it with context engineering).
- "Keep everything in one conversation so the AI has full context" (S003 line 233) and "The chat history is the record of what was decided" (S036).
- "Once I tell it something, it remembers for the whole session" (S101, S105).
- "A subagent sees the whole conversation" (S015 companion: Subagents docs) and "Delegating to subagents is free" (S016, S107).
- From the legacy lesson: the 2021 picture (tokens, temperature, next-token guessing) as the core of what a builder needs, which Aaron sent back (S004).

## Legacy notes
`00-05-how-llms-work-just-enough` (00.05, published 2026-10-02, about 20 minutes) no longer stands in for this slot: the 2026-10-12 audit unlinked it, because its context, caching and media segments carry facts with no entry in sources.md. For the record, the material it had was in its sections 04-05 ("Tokens, and a desk that grew"; "A fuller desk is a worse desk") and the context parts of 10-12.
- **What it gets right and can be reused:** "nothing stays overnight; every request starts with a clean desk, and everything is handed over again"; "everything on the desk counts"; "a fuller desk is a worse desk"; compaction and `/compact`; a subagent gets its own fresh desk and hands back a short report; cached tokens are cheaper, not smaller. The desk metaphor still fits this lesson.
- **What is outdated or unsourced:** its context-rot evidence is Chroma (July 2025) and "lost in the middle" (2023), neither in `sources.md`; replace with S012's wording and S107's 2026 measurements. It spends its time on tokens, the growth of window sizes and the retired temperature dial, the 2021 picture this lesson must not repeat (S004). Its "own lesson in The Machine" pointers refer to the retired map.
- **What is missing:** that most of the package is text you never typed, shown in a real request (S002, S105); that the terminal hides what enters (S105); what survives compaction and the measured cost of compacting late (S105, S107); clearing after a decision and handing off through files (S003, S036, S037); that a subagent starts blind and a fork does the opposite (S015 companion, S107); that the newest models get no budget warning (S012).
