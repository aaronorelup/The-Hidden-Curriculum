---
key: model-harness-and-memory
id: 00.02
title: What you're really using
district: Orientation
module: 00 Orientation
status: legacy
legacy: [00-04-model-vs-app-vs-agent, 00-05-how-llms-work-just-enough]
minutes: [5, 6]
concepts: [C021, C023]
sources: [S002, S014, S101, S011, S015, S128, S074, S103, S104, S105, S008, S125, S001, S004, S012, S013]
lead: [S002, S014]
---
# What you're really using

**Purpose (the first spoken sentence):** In this lesson you'll learn what you are really using when you use an AI: a model inside a harness, and where what it "knows" actually lives.

**Conclusion:** Results come from the whole setup (app and version, model, effort, tools, instruction files, memory), not from the model alone, so when results change, name the whole setup before you blame the model.

**Where it sits on the map:** Start · Orientation — what this is, and your job; module 00 Orientation. Status `todo` since the 2026-10-12 audit: the legacy videos that covered this slot teach framings this spec calls out of date and pin themselves on the retired map, so this is the second lesson the daily job makes, right after 00.01.

**Lead source (audit, 2026-10-12):** S002 (Mihail Eric, Stanford CS146S); S014 (Anthropic). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S002, S014, S101, S011); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length (audit, 2026-10-12):** about 5-6 minutes; COURSE.md (Aaron, 2026-10-01) gives orientation lessons and the first lesson of every module about 5 minutes. Keep at teach depth C021 points 1, 2, 5 and 9 and C023 points 1-4 and 9. Every other point is the cut list: a point marked brief becomes one line, and a point marked one line moves to the lesson page (C021 points 3, 4, 6, 7, 8; C023 points 5-8).

## What to teach (binding scope)

### C021 The model is not the product: you use a configuration, and 'it got dumber' is often the harness

1. **The loop is small; the harness is big.** A bare coding agent is about 150-200 lines: send the conversation to the model, run the tool it asks for, add the result, repeat (S002 line 46). Anthropic calls everything around the model "the agentic harness": "the layer around the model that provides the tools and manages the context the model sees" (S101). Stanford's lecturer calls harness design "probably one of the hardest and most important problems" in agents (S002 line 64). Depth: **teach** (this is the mental model).
2. **What a harness holds.** In Claude Code: a system prompt "you don't control" that goes into every request (S002 line 203), instruction files (CLAUDE.md, AGENTS.md), about 40 built-in tools the model has been post-trained to use, plan mode, subagents, skills, hooks and compaction (S002 lines 68-70, 86-88); the model itself is a private service you cannot inspect (S002 line 50). Depth: **teach as names on one drawing**; what each part does is taught later (see below).
3. **The loop it runs:** gather context, take action, verify results, and you can interrupt and steer at any point (S101); OpenAI teaches the same loop as Prompt, Inspect, Act, Validate, Report (S008 slide 7). Depth: **one line**.
4. **Same model, different results.** GeneGPT scored 0.83 on a genomics benchmark with API tools against 0.00-0.44 for models without them (S011); in WorkstreamBench the same Opus 4.6 generally scored higher inside the vendor's own agent than in the researchers' API harness (S074). Depth: **brief** (one example on screen).
5. **The April 2026 case: three harness changes, model untouched.** (a) Default effort lowered from high to medium on 2026-03-04, reverted 2026-04-07 ("This was the wrong tradeoff"), and "most users retained the medium effort default" despite in-product notices; (b) a change meant to clear old reasoning once from sessions idle over an hour cleared it on every turn from 2026-03-26 to 2026-04-10, so Claude "seemed forgetful and repetitive" and cache misses drained usage limits faster; (c) a system-prompt line "keep text between tool calls to ≤25 words" cost 3% on an evaluation and was reverted on 2026-04-20. "The API was not impacted", and Anthropic states "We never intentionally degrade our models" (S014). Depth: **teach** (the lesson's case).
6. **Nobody's tests caught it.** The reasoning bug passed human and automated code review, unit and end-to-end tests, automated verification and dogfooding, and took over a week to root-cause; user reports through `/feedback` and reproducible public examples found it (S014). Depth: **brief** (it is why your report matters).
7. **Effort is a setting the harness picks for you.** In Claude Code on 2026-10-12, Opus 5.5, Sonnet 5.5 and Haiku 5.5 default to `medium`, other models to `high` (Opus 4.7 to `xhigh`); `max` "is prone to overthinking"; `ultrathink` in a prompt deepens one turn, while "think hard" is ordinary text (S015, model-config page). Depth: **brief**. The same model can carry a different default elsewhere: the Claude API lists Sonnet 5.5's default effort as `high` (candidate source below; add its S-ID before using this line).
8. **The harness changes month to month.** The Claude Code system prompt shrank from about 200-250 lines to 50-80 within a month or two, the lecturer suspects because training absorbed instructions like how to use git (S002 lines 212, 225-227); a new Claude Code version "typically updates the system prompt or tool definitions" (S128). Depth: **brief** (ties to 00.01's pace).
9. **The habit: name the whole configuration.** When you compare tools, report a problem or say "it works / it doesn't", give app and version, model, effort, tools and data sources (S011; S014). Depth: **teach** (the takeaway).
- Dropped here: reasoning blocks that must be passed back intact between turns (C021 point 8, S012, S013) → deep-dive backlog "Thinking tokens and reasoning budgets" (C029); it matters to people building their own agent loop. The per-model eval suite Anthropic adopted (S014) → named only in You vs the agent.

### C023 Three places information lives: weights, context window, external memory

1. **Weights.** Knowledge frozen at training; ordinary chats do not change them; "stateless" means only "that those weights are fixed during inference" (S011). Depth: **teach**.
2. **Context window.** The current input (conversation, retrieved text, tool results), lasting only while it is in the window (S011). Each new Claude Code session "starts with a fresh context window, without the conversation history from previous sessions" (S101), and "the model doesn't remember anything between requests, so Claude Code re-sends the full context" every turn (S128). Depth: **teach** (one sentence on the resend; 05.01 owns what the package contains and how it degrades).
3. **External memory.** Logs, profiles, knowledge bases, vector stores and memory files outside the model, kept under the product's retention rules and put back into the prompt; most privacy and governance risk sits here (S011). Depth: **teach**.
4. **In Claude Code, memory is files.** CLAUDE.md you write, and auto memory Claude writes for itself, of which the first 200 lines or 25KB of MEMORY.md load at the start of each session (S101). Memory is a separate block concatenated into the request, stored at a project-level path (S002 lines 253-255), and flat files often work as well as retrieval systems (S002 lines 260-264). Depth: **teach** (short).
5. **Transcripts are a fourth store.** Every message, tool use and result goes to a plaintext JSONL file under `~/.claude/projects/` so you can resume, rewind or fork, but a new session does not read it (S101). Depth: **brief**.
6. **Rules you didn't write come from the harness too.** "If Claude follows a rule you didn't write, such as adding a Co-Authored-By trailer to a commit, the rule may have come from a system reminder" the harness adds alongside your messages (S101). Depth: **one line** (a recognisable surprise).
7. **Memory can go stale.** A forum reply on cross-tool memory: "A memory like 'we use Jest' survives a migration to Vitest and quietly poisons recommendations"; anything that duplicates code or config goes stale (S103, Dean Rie's reply; the page shows no staff label, although concepts.md calls him Cursor staff). Depth: **brief**.
8. **The external layer can reach a future model.** On Claude consumer plans with model improvement on, chats and coding sessions may be kept de-identified "for up to 5 years" in training pipelines; turning it off later does not remove data from training runs already in progress; deleted chats leave back-end storage within 30 days; commercial plans follow separate rules (S104, updated 2026-07-01). Depth: **one line** (01.02 owns where your data goes).
9. **The question to ask of any AI product:** "Where, in this product, is information actually stored, and how is it reused?" and under what retention and training-reuse policies (S011). Depth: **teach** (the second takeaway).
- Dropped here: what each request contains, context rot and curating the window (S105 beyond the `/context` demo) → what-the-agent-sees-each-turn; instruction files as requests vs enforcement and keeping them current → rules-it-reads-rules-it-cant-break; vendor privacy settings compared → where-your-agent-works and the backlog (C103).

## You vs the agent

As of 2026-10-12:
- **The agent** runs the loop on its own: reads, edits, runs commands and tests, fixes its own errors and reports (S101; S008 slide 7). It writes and reads its own memory files and reads whatever the harness injects (S002 line 219; S101).
- **The agent cannot** see its own harness version, a system-prompt change, or whether its earlier reasoning was dropped; in April 2026 the vendor's own reviews and tests missed exactly that (S014). It cannot tell you the vendor's retention or training policy for your account (S011).
- **You** choose the app, model and effort at the start and write that configuration down; when quality changes, check the version and changelog and file a reproducible `/feedback` report rather than silently switching tools (S014); know where memory lives in each tool, read and correct or delete wrong entries, keep secrets out of memory files, and check the training and retention setting instead of assuming the model "forgets" (S011; S104; S103).
- **Bring in an expert** when a product of yours depends on a prompt or harness you change: Anthropic's own fix was per-model evaluations and line-by-line ablations for every system-prompt change (S014), which needs someone who can build and read evals. For client or company data, the person who owns the data agreement (IT, privacy or legal) decides which product and plan may hold it (S104).

## Sources this lesson is built from

- S002 — Mihail Eric, Stanford CS146S lecture transcript, "anatomy of a state-of-the-art coding agent" (2026-09-24) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — the 150-200-line loop, the harness parts, the system prompt you don't control, ~40 post-trained tools, the shrinking system prompt, memory as a separate block, flat files vs RAG (line numbers re-checked 2026-10-12).
- S014 — Anthropic, "An update on recent Claude Code quality reports" (2026-04-23) https://www.anthropic.com/engineering/april-23-postmortem — the three harness changes, the API unaffected, what testing missed, `/feedback`.
- S101 — Anthropic, "How Claude Code works" (Claude Code docs, undated live page, read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — "agentic harness", the loop, fresh context per session, MEMORY.md limits, JSONL transcripts, system reminders.
- S011 — Zhicheng Lin, "Six misconceptions about large language models: A minimal model and diagnostic taxonomy" (PNAS Nexus, 2026-07-08) https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/ — the deployed configuration as the unit of analysis, three memory layers, the diagnostic question.
- Supporting, one line each on screen:
  - S015 — Anthropic, Claude Code docs, model configuration page (companion of "Extend Claude Code"; undated live page, read 2026-10-12) https://code.claude.com/docs/en/model-config — current effort defaults, `max`, `ultrathink`.
  - S128 — Anthropic, "How Claude Code uses prompt caching" (undated live docs) https://code.claude.com/docs/en/prompt-caching — the full context is re-sent every request; a new version typically changes the system prompt or tools.
  - S074 — Thomson Yen, Julian Poeltl, Hongseok Namkoong et al., "WorkstreamBench" (2026-05-21) https://arxiv.org/html/2605.22664v1 — same model, higher scores inside the vendor's own agent.
  - S103 — Pat2 and replies (Dean Rie), "How are people handling context across different AI coding tools?" (Cursor forum, 2026-05-06) https://forum.cursor.com/t/159891 — re-explaining across tools; stale memories.
  - S104 — Anthropic Privacy Center, "How long do you store my data?" (updated 2026-07-01) https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data — consumer retention and training.
  - S105 — Anthropic, "Explore the context window" (Claude Code docs, undated) https://code.claude.com/docs/en/context-window — what loads before you type, and `/context` / `/memory` to check your own session (demo only).
  - S008 — OpenAI Academy, "Codex Bootcamp 101: Agentic coding" (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — the same loop in OpenAI's words, and a presenter's colleague admitting the products confused him at first.
  - S125 — Anthropic, "Claude Code changelog" (entries to v2.1.296, 2026-10-09) https://code.claude.com/docs/en/changelog — demo only: the changelog entry for the version on screen.
- Candidate source, fetched and read 2026-10-12, **not yet in sources.md** (give it an S-ID before the script uses it):
  - Anthropic, "Models overview" (Claude Platform docs, undated live page) https://platform.claude.com/docs/en/about-claude/models/overview — the Claude API's default effort per model (Sonnet 5.5: `high`), against Claude Code's `medium` for the same model (S015): one model, two harness defaults.

## Show it for real

- Run a coding agent through a logging proxy (the CS146S assignment's setup) and open one captured request: model name, the system block, messages and the tools list side by side: proves you never send "just your prompt" to a bare model (S002 lines 97-104). Use a toy project, no keys on screen.
- `claude --version`, `/model` and `/effort` (showing the current default), then the changelog entry for that version: proves the harness has a version and settings you can name (S014, S015, S125 as background).
- Open the April 23 postmortem and highlight the three dated changes and "The API was not impacted": proves "it got dumber" was the harness (S014).
- `/memory` to open CLAUDE.md and the auto memory file, then `/context` in a fresh session listing them as loaded: proves memory is files put back into the prompt (S105, S101).
- Open `~/.claude/projects/`, show a session's JSONL transcript, then show a fresh session that does not know its contents: proves the transcript is a separate store (S101). Use a throwaway session with no personal data.
- The consumer privacy setting for model improvement, on a test account: proves the external layer can reach training (S104).

## Questions this lesson answers

- "What is the difference between Claude, Claude Code and Opus?" and "Why does the same model act differently in Cursor and in Claude Code?" (batch-reader list from S002)
- "Why does Claude Code feel worse this week? Did they downgrade the model?" (the user reports S014 answers)
- "What actually happens when I press enter?" (S002 batch-reader list)
- "I feel like I keep re-explaining the same things between tools." (Pat2, S103)
- "Is the memory local to each execution of Claude Code?" and "Where does retrieval happen? RAG or GraphRAG?" (Stanford students, S002 lines 253, 260)
- "Is my conversation used to train the model?" and "Why did it forget what I told it yesterday?" (batch-reader list, S011)
- "Why did it add a line to my commit that I never asked for?" (derived from S101's system-reminder example)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Chat, Cowork, desktop, terminal and cloud surfaces; where your data goes → where-your-agent-works
- What one request contains, context rot, compaction, subagents starting blind → what-the-agent-sees-each-turn
- Instruction files (CLAUDE.md, AGENTS.md): what they can and cannot enforce, which ones load, keeping them current → rules-it-reads-rules-it-cant-break
- Skills, MCP, hooks, plugins, subagents → skills-mcp-hooks-and-plugins
- Effort and model as cost, prompt caching → know-your-meter
- Models that see, hear and make media → making-media-with-ai
- Reasoning passed back between turns, thinking tokens → deep-dive backlog (C029)
- Which kinds of task to trust it on → trust-what-you-can-verify

## Out-of-date framings to avoid

- "LLMs are just next-token predictors / stochastic parrots / autocomplete" as a description of what you use: it describes the training objective; "The predictor is unchanged; the system is not" (S011).
- "Pick the best model and you're done"; "same model, same results everywhere" (S011; S074).
- "They secretly nerfed the model" (S014).
- "It learns from my chats and remembers me" and its mirror, "it is stateless and remembers nothing" (S011).
- "Memory means the model was retrained on me": memory is a block in the prompt (S002 line 255).
- "Learning AI starts with how the model is trained" and "prompt wording is the main skill" (Stanford's 2026 outline, S001 via concepts.md C021; S002 line 52: training is not covered).
- The 2021 picture as the lesson's core: tokens, a desk, temperature, top-p, hallucination rates (S004: the reason 00.05 v1 was sent back).
- "The model is the engine, the app is the car, the agent is the driver" with no harness in between: it hides the layer that changed results in April 2026 (S014).
- Effort defaults or system-prompt sizes stated as fixed facts: both changed within months (S014, S015, S002). Date every number on screen.

## Legacy notes

- **00-04-model-vs-app-vs-agent (covers this slot with 00.05 until this lesson is rebuilt).** Gets right: the model is a lab's set of weights run on its servers; one model sits in many products; the app adds a system prompt you don't see; agents are a model with tools, a loop and permissions; the model "starts cold" each message and the app resends the conversation; don't ask the model which model it is. Missing or outdated: the word and idea "harness" and that it changes results as much as the model; the April 2026 case (S014); effort as a setting; memory as files with a location; "text in, text out, no memory" without the external-memory layer and its privacy side (S104).
- **00-05-how-llms-work-just-enough (covers this slot only; unlinked from 05.01 and 09.02 by the 2026-10-12 audit, because its context, caching and media segments carry facts with no entry in sources.md).** About 20 minutes; split on rebuild as `curriculum.md` says. Its desk metaphor ("the model only knows what's on its desk right now"), "nothing stays overnight" and the five ways memory comes back map onto C023 and can be reused in shorter form. Its context, compaction and caching segments move to what-the-agent-sees-each-turn and know-your-meter; diffusion and media to making-media-with-ai; modes and platforms to where-your-agent-works; skills and plugins to skills-mcp-hooks-and-plugins; individual vs enterprise to where-your-agent-works and the backlog; personal agents to agents-that-run-while-youre-away. Facts in it that are not in sources.md (context-window history, Chroma's context-rot study, temperature errors, Sora's shutdown, the Claude Marketplace count, OpenClaw figures) must not be carried into this lesson without a source. Its guest myth round is out of scope here (this lesson is under 15 minutes).
