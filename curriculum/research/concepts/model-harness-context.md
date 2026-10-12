# G03. What you are working with: model, harness and context

Concept entries C021-C032, written 2026-10-12 by agent `concepts-model-harness-context` for The Hidden Curriculum.

**How this file was built.** Every point traces to a source that a batch reader fetched and read (S-IDs, see `taxonomy.md` source index) or that this agent fetched and read on 2026-10-12 (the MHC-X IDs below). The key pages behind the strongest claims were re-opened today as raw text, not through a summariser: S002 and S003 transcripts (line numbers checked), S012, S013, S014, S033, S069, the Claude Code docs pages listed below, and the LangWatch study. The shared web-search budget was used up before this agent started, so no new sources were found by search; the MHC-X sources are pages already named in the research folder (`sweep/`, batch notes) or linked from an S-source, plus two of Aaron's own posts and one Playback prompt.

**Sources cited (dates as checked on the page).**

| ID | Source | Date | URL |
|---|---|---|---|
| S001 | CS146S syllabus, Fall 2026 vs Fall 2025 (Mihail Eric, Stanford) | page undated; Fall 2026 starts 2026-09-22 | https://themodernsoftware.dev/ |
| S002 | CS146S lecture: anatomy of a coding agent (transcript) | 2026-09-24 | https://themodernsoftware.dev/materials/9-24-26-transcript.txt |
| S003 | CS146S lecture: context engineering, RePPIT (transcript) | 2026-09-29 | https://themodernsoftware.dev/materials/9-29-26-transcript.txt |
| S004 | AO-034: I sent back two of my course's first seven lessons (Aaron Orelup) | 2026-10-04 | https://aaronorelup.com/ledger/lessons-sent-back/ |
| S005 | Claude Code 101 (Anthropic Academy) | undated; live since about 2026-04 | https://anthropic.skilljar.com/claude-code-101 |
| S006 | AI Capabilities and Limitations (Anthropic Academy) | undated; live by 2026-04-07 | https://anthropic.skilljar.com/ai-capabilities-and-limitations |
| S008 | Codex Bootcamp 101 (OpenAI Academy livestream + deck) | 2026-09-23 | https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c |
| S010 | Build with Andrew, with companion "AI Prompting for Everyone" (Andrew Ng) | 2026-07-17 / 2026-07-24 | https://www.deeplearning.ai/courses/build-with-andrew |
| S011 | Six misconceptions about large language models (Zhicheng Lin, PNAS Nexus) | 2026-07-08 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/ |
| S012 | Context windows (Claude Platform Docs), with Prompt caching | undated live docs (lists Opus 5.5, Fable 5.1) | https://platform.claude.com/docs/en/build-with-claude/context-windows |
| S013 | Gemini thinking (Google), with OpenAI "Reasoning models" guide as companion | last updated 2026-10-09 | https://ai.google.dev/gemini-api/docs/generate-content/thinking |
| S014 | An update on recent Claude Code quality reports (Anthropic postmortem) | 2026-04-23 | https://www.anthropic.com/engineering/april-23-postmortem |
| S015 | Extend Claude Code (features overview), with companions Model configuration, Prompt caching, Skills, MCP | undated live docs (model-config mentions v2.1.293) | https://code.claude.com/docs/en/features-overview |
| S016 | Manage costs effectively (Claude Code) | no earlier than 2026-09-14 | https://code.claude.com/docs/en/costs |
| S025 | ChatGPT & Codex changelog, with "Get started with ChatGPT Work" | latest entry 2026-10-08 | https://learn.chatgpt.com/docs/changelog |
| S032 | AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run (Aaron Orelup) | 2026-09-29 | https://aaronorelup.com/ledger/wallpapers-nobody-saw/ |
| S033 | 2026 in LLMs (so far) (Simon Willison) | 2026-09-27 | https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ |
| S036 | Brownfield Agentic Engineering (Addy Osmani) | 2026-09-14 | https://addyosmani.com/blog/brownfield-agentic-engineering/ |
| S037 | A field guide to Claude Fable 5: Finding your unknowns (Thariq Shihipar, Anthropic) | 2026-07-06 | https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns |
| S059 | MCP Security Best Practices, spec revision 2026-07-28, with the 2026-07-28 spec post | 2026-07-28 | https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices |
| S068 | Agency and Agents (Ethan Mollick) | 2026-08-31 | https://www.oneusefulthing.org/p/agency-and-agents |
| S069 | Use Claude Cowork safely (Anthropic Help Center) | last modified 2026-10-06 | https://support.claude.com/en/articles/13364135-use-claude-cowork-safely |
| S074 | WorkstreamBench (Yen, Poeltl, Namkoong et al., Columbia) | 2026-05-21 | https://arxiv.org/html/2605.22664v1 |
| S080 | Stack Overflow Developer Survey 2026 | released 2026-10-06 | https://survey.stackoverflow.co/2026/ |
| MHC-X01 | How Claude Code works (Anthropic, Claude Code docs; companion of S015) | undated live docs, read 2026-10-12 | https://code.claude.com/docs/en/how-claude-code-works |
| MHC-X02 | Explore the context window (Anthropic, Claude Code docs; companion of S015) | undated live docs, mentions v2.1.198 | https://code.claude.com/docs/en/context-window |
| MHC-X03 | The Context Tax: When to Compact (Rogerio Chaves, LangWatch; the Week 2 reading of S001, cited by S003) | 2026-08-02 | https://langwatch.ai/blog/context-tax-when-to-compact |
| MHC-X04 | Claude Cowork and chat are now one Claude (Anthropic, Claude blog) | 2026-09-16 | https://claude.com/blog/cowork-is-now-claude |
| MHC-X05 | How long do you store my data? (Anthropic Privacy Center; companion of S069) | 2026-07-01 | https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data |
| MHC-X06 | Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things (Simon Willison) | 2026-08-16 | https://simonwillison.net/2026/Aug/16/qwen-38-27b/ |
| MHC-X07 | Vision (Claude Platform Docs) | undated live docs (names Opus 5, Claude 4.7+) | https://platform.claude.com/docs/en/build-with-claude/vision |
| MHC-X08 | Understand and count tokens (Gemini API docs) | last updated 2026-09-23 | https://ai.google.dev/gemini-api/docs/tokens |
| MHC-X09 | Image generation, "Nano Banana" (Gemini API docs) | last updated 2026-10-09 | https://ai.google.dev/gemini-api/docs/image-generation |
| MHC-X10 | AO-030: Claude rendered 223 clips of my game's robot voice, and couldn't hear any of them (Aaron Orelup) | 2026-10-02 | https://aaronorelup.com/ledger/remora-voice-lab/ |
| MHC-X11 | AO-044: Nine Claudes painted the same picture in oil, and the first tries were the art (Aaron Orelup) | 2026-10-11 | https://aaronorelup.com/ledger/nine-claudes-one-painting/ |
| MHC-X12 | Playback: Aaron's prompt on what "Opus 5.5 made this" videos leave out (typed prompt; `sweep/aaron.md` P05) | 2026-10-03 | playback-lens: C--Users-soulo-Organized-Personal-My-Projects-My-Blog / 271db68b-18fe-40eb-bf03-9ff7bf1c1529, line 579 |
| MHC-X13 | How are people handling context across different AI coding tools? (Cursor forum; Pat2, replies by Dean Rie, Cursor staff) | 2026-05-06 | https://forum.cursor.com/t/159891 |
| MHC-X14 | Ask HN: I still don't understand why AI agents need "skills" (skeptic_ai and 18 commenters) | 2026-08-02 | https://news.ycombinator.com/item?id=49139845 |

---

### C021 The model is not the product: you use a configuration, and 'it got dumber' is often the harness

- **In one line:** What you use is a model inside a harness (system prompt, tools, instruction files, memory, effort setting, context handling), and the harness changes results as much as the model does: Anthropic's April 2026 quality drop came from three harness changes while the model was untouched.
- **Why it is a gap:**
  - Aaron sent back lesson 00.05 v1 because it taught the 2021 picture (tokens, next-token guessing, the window as a desk, temperature), a model with nothing around it (S004).
  - Stanford's Fall 2026 course dropped "how an LLM is made" and "power prompting" and now opens with the agent loop, the core tools and system prompts; the 2026-09-24 lecture says it will not cover training at all (S001; S002 lines 52, 72).
  - Both vendors' beginner courses now open with the loop, not the model (S005 section 1; S008 slide 7).
  - Users read quality swings as "the model got worse". In spring 2026 Anthropic traced exactly those reports to a default setting, a context bug and one system-prompt line, with the API and inference layer unaffected; most users had kept the lowered default even after in-product notices (S014).
  - Lin (PNAS Nexus, July 2026) argues the deployed configuration, not the base model, is the unit of analysis, because the same model scores very differently with and without tools, retrieval or a redesigned workflow (S011).
- **What to teach (specific points):**
  1. A working coding agent is about 150-200 lines: send the conversation to the model, run the tool it asks for, add the result, repeat (S002 lines 46, 72). Anthropic's own docs call everything around the model "the agentic harness": the layer that provides the tools and manages the context the model sees (MHC-X01).
  2. The harness of Claude Code includes a system prompt you cannot change, instruction files (CLAUDE.md / AGENTS.md), about 40 built-in tools the model is post-trained to use, plan mode, subagents, skills, hooks and compaction; the model itself is a private service you cannot inspect (S002 lines 50, 68-70, 86-88, 203).
  3. The loop is gather context, take action, verify results, and you can interrupt and steer at any point (S005; MHC-X01). OpenAI teaches the same loop as Prompt, Inspect, Act, Validate, Report, then human review (S008 slide 7).
  4. Same model, different results: GeneGPT scored 0.83 on a genomics benchmark with API tools against 0.00-0.44 for models without them, and retrieval raised GPT-4's FreshQA accuracy by 32.6-49.0% relative (S011). In WorkstreamBench the same Opus 4.6 generally scored higher inside the vendor's own agents than in the researchers' API harness (S074).
  5. The April 2026 regressions, all harness: (a) default effort lowered from high to medium on 2026-03-04, reverted 2026-04-07 ("This was the wrong tradeoff"); (b) a change meant to clear old thinking once from sessions idle over an hour cleared it on every turn from 2026-03-26 to 2026-04-10, so Claude seemed forgetful and repetitive, and the cache misses drained usage limits; (c) a system-prompt line "keep text between tool calls to ≤25 words" cost 3% on a broad eval and was reverted on 2026-04-20 (S014).
  6. The context bug passed human and automated code review, unit and end-to-end tests, automated verification and dogfooding, and took over a week to root-cause; `/feedback` reports and reproducible public examples are what found it (S014).
  7. Effort is a quality dial you own. In Claude Code today Opus 5.5, Sonnet 5.5 and Haiku 5.5 default to `medium`, `max` "is prone to overthinking", and `ultrathink` in a prompt deepens reasoning for one turn while "think hard" is ordinary text (S015, model-config page).
  8. Earlier reasoning survives between turns only if the harness sends it back intact: Claude signed thinking blocks (a modified block returns an error), Gemini thought signatures, OpenAI encrypted reasoning items (S012; S013). Dropping it is what made the agent forgetful in March-April 2026 (S014).
  9. The harness changes month to month: the Claude Code system prompt shrank from 200-250 lines to about 50-80 within a month or two because training seems to have absorbed instructions like how to use Git (S002 lines 212, 225-227).
  10. When you compare tools or report "it works / it doesn't", name the whole configuration: app and version, model, effort, tools, data sources (S011; S014).
- **You vs the agent (as of 2026-10-12):** The agent runs the loop on its own: reads, edits, runs commands and tests, fixes its own errors and reports (S008 slide 7; MHC-X01). It runs inside whatever harness, tools and settings it is given and cannot see its own harness version, a system-prompt change or whether its earlier reasoning was dropped; in April 2026 the vendor's own tests and reviews missed the bug (S014). The human chooses the app, model and effort at the start, records that configuration, and when quality changes checks the version and changelog and files a reproducible `/feedback` report rather than silently switching tools (S014). Anyone building their own agent loop should use the official SDK conversation helpers so reasoning is passed back intact, and have the agent test multi-turn tool calls after any history trimming (S012; S013). Bring in an expert when a product depends on a prompt or harness you change: Anthropic's own fix was a per-model eval suite and line-by-line ablations for every system-prompt change (S014), which needs someone who can build and read evals.
- **Currency:** Established idea (harness vs model: S011, S002), with new-in-2026 evidence (the April 2026 postmortem, S014). Changing now: per-model effort defaults (Opus 5.5 defaults to `medium`, one level below Opus 5's `high`, per S015 model-config), system prompts getting shorter (S002), and the harness version moving every few days (S016 cites up to v2.1.271; its companion errors page cites v2.1.296).
- **Outdated framings to avoid:**
  - "LLMs are just next-token predictors / stochastic parrots / glorified autocomplete" as a description of what you use: Lin calls it a description of the training objective, not the deployed system (S011).
  - "Pick the best model and you're done" / "same model, same results everywhere" (S011; S074).
  - "They secretly nerfed the model": in the April case the API and inference layer were unaffected, and Anthropic states it never intentionally degrades its models (S014).
  - "Learning AI starts with how the model is trained" and "prompt wording is the main skill": both dropped from Stanford's 2026 outline (S001).
- **Questions it answers:**
  - "Why does the same model act differently in Cursor and in Claude Code?" and "What is the difference between Claude, Claude Code and Opus?" (S002 reading, batch-reader list).
  - "Why does Claude Code feel worse this week? Did they downgrade the model?" (the user reports S014 answers).
  - "What actually happens when I press enter?" (S002, batch-reader list).
  - The presenter's colleague at OpenAI's bootcamp admitted the difference between the products confused him at first (S008 talk 28:01).
- **Show it for real:** Run a coding agent through a logging proxy, as the CS146S assignment does, and open one captured request: model name, system block, messages, tools list side by side (S002 lines 97-104). Run `claude --version`, `/model` and `/effort`, open the changelog for that version, and show `/feedback` (S014). Ask the same recent-events question in a bare API playground and in an agent with web search, and point at the tool call in the second transcript (S011 demo).
- **Priority:** must. Six items from four batches, four rated high; it is the exact reframe Aaron demanded after 00.05 (S004), Stanford and both vendors now open with it (S001, S005, S008), and the postmortem is a vivid, dated incident (S014).

---

### C022 Which surface for which job

- **In one line:** Chat, Claude's merged chat-and-Cowork app, ChatGPT Work, and the coding agents (Claude Code, Codex) in a terminal, desktop app, browser or the cloud can share a model but differ in harness, tools, permissions and where the work runs; pick the surface by the output you want and by what it must be able to reach.
- **Why it is a gap:**
  - At OpenAI's 2026-09-23 bootcamp the presenter's colleague admitted the difference between ChatGPT, Work and Codex confused him at first (S008 talk 28:01).
  - Aaron lists "chat, Cowork and Code across browser, desktop, CLI and cloud" as a gap (S004), and Stanford's course does not cover it (S001).
  - The map moved four times in three months: Codex folded into the ChatGPT desktop app (2026-07-09), voice across Chat, Work and Codex (2026-07-23), Claude Cowork and chat merged (2026-09-16), and Cowork tasks on Pro and Max moved to the cloud (2026-10-06) (S025; MHC-X04; S069). A picture formed in the summer is already wrong.
- **What to teach (specific points):**
  1. OpenAI's rule: use Chat while the answer is still taking shape, Work when the output is a knowledge artifact, Codex when the output is working software; the same models sit behind every surface (S008 slide 8, talk 29:00-30:00).
  2. On 2026-09-16 Anthropic merged Cowork and chat into "one Claude", rolling out to Pro and Max: Claude decides whether a request is a quick answer or a task, and by default asks before taking an action (MHC-X04; S069). The choice between modes is disappearing from the screen; the difference in what the session can do is not.
  3. Where the work runs decides what it can reach. Cowork sessions run in the cloud on Anthropic's servers, reach your computer only through the Claude Desktop app while it is open and only for folders you connected, and any local file they open is processed on Anthropic's servers; on Pro and Max, new desktop tasks have run in the cloud since 2026-10-06 (S069).
  4. ChatGPT Work runs a task locally (your files, apps, browser) or in the cloud (keeps going while your computer sleeps, cannot reach its files); a task cannot switch from local to cloud mid-turn (S025).
  5. Claude Code runs the same loop and tools in every interface: terminal, desktop app, IDE extensions, claude.ai/code, Remote Control, Slack and CI/CD. Its three execution environments are local (full access to your files and tools), cloud (Anthropic-managed VMs, for repos you don't have locally) and Remote Control (your machine, driven from a browser) (MHC-X01; S005 lists terminal, VS Code, JetBrains, Desktop and web).
  6. A product's harness can beat the same model elsewhere: in WorkstreamBench, Claude Web was the best agent at 69.1/100 and vendor GUI agents generally beat the same model in a research harness (S074).
  7. Surfaces often draw on one allowance: Team and Enterprise seats share one per-seat allowance across Claude chat, Cowork and Claude Code, and Pro and Max limits are shared across Claude and Claude Code (S016 and its Help Center companion).
- **You vs the agent (as of 2026-10-12):** In the merged Claude app the agent now decides whether a request needs a task run, and in coding agents it chooses its own tools (MHC-X04; MHC-X01). The human decides where the work may run (local or cloud) when files must stay on the machine, which folders and connectors a session gets, and the approval mode (S069; S025), and sets boundaries such as "stop before sending anything" in the prompt (S025). On a computer your organisation manages, connecting a folder makes it reachable from a cloud session (S069), so bring in your IT or security admin before connecting work data.
- **Currency:** New in 2026 and still moving: the chat/Cowork merge is rolling out to Pro and Max with Team, Free and Enterprise to follow (MHC-X04); cloud Cowork is in beta on Team and Enterprise (S069). Re-check this concept monthly.
- **Outdated framings to avoid:**
  - "Claude is a chat website" (S004 item).
  - "Codex and ChatGPT are different AIs" (S008).
  - "Chat and Cowork are separate modes you pick" (S069; MHC-X04).
  - "A desktop AI agent keeps your files on your computer": false for Cowork on Pro and Max since 2026-10-06 (S069).
- **Questions it answers:** "What is the difference between ChatGPT and Codex?"; "Should I use Claude chat, Cowork or Claude Code?"; "Should I use the desktop app or the CLI?" (batch-reader lists from S008 and S004; the S008 colleague's confusion is the recorded instance).
- **Show it for real:** Give the same small task to the Claude app, to a Cowork/merged session with one folder connected, and to Claude Code in a project folder, and compare what each could touch (S004 demo). Show the new message box without the "Chat" and "Cowork" options (S069). In ChatGPT Work, show the local vs cloud choice and what a cloud task cannot see (S025).
- **Priority:** should. Two items, medium severity, but it is on Aaron's own gap list (S004), it changed four times since July (S025, MHC-X04, S069), and it decides where your files go.

---

### C023 Three places information lives: weights, context window, external memory

- **In one line:** "It remembers me" and "it remembers nothing" are both wrong: knowledge is frozen in the weights, the conversation exists only inside the context window, and "memory" is files and stores the product writes, keeps and injects back into the prompt.
- **Why it is a gap:**
  - Lin cites Jones et al. (CHI 2025) finding users "misunderstand what different memory layers store and reuse", and traces both wrong beliefs to mixing up the three layers (S011).
  - Anthropic's own beginner course teaches that a new session does not remember the last, which misleads users of products with memory features (S006, as compared with S011 by the vendor-academies batch).
  - Stanford students asked during the 2026-09-24 lecture whether Claude Code's memory is local to each run and where retrieval happens (S002 lines 253, 260).
  - Aaron lists "the different ways they remember: searching old chats, keeping their own memory, files and Notion reached through tool calls" as a gap (S004).
  - Cross-tool users keep re-explaining the same project to every tool (MHC-X13).
- **What to teach (specific points):**
  1. Weights: a lossy, biased compression of training data that changes only when the model is retrained; ordinary chats do not update them, and "stateless" means only that (S011).
  2. Context window: the current input (conversation, retrieved text, tool results), Anthropic's "working memory", lasting only while it stays inside the window (S011; S012). Each new Claude Code session starts with a fresh window and none of the previous conversation (MHC-X01).
  3. External memory: logs, profiles, knowledge bases, vector stores and memory files outside the model, kept under product retention rules and selectively injected into prompts; most privacy and governance risk sits here (S011).
  4. In Claude Code, memory is files: CLAUDE.md you write, and auto memory Claude writes for itself, of which the first 200 lines or 25KB of MEMORY.md load into every session (MHC-X01; S015). Memory is a separate block concatenated into the request, stored at a project-level path (S002 lines 253-255), and flat files often work as well as RAG (S002 lines 260-264).
  5. Transcripts are a fourth store: Claude Code writes every message, tool use and result to a JSONL file under `~/.claude/projects/` so you can resume, rewind or fork, but a new session does not read them (MHC-X01).
  6. The external layer can reach a future model's weights: on Claude consumer plans, if you allow model improvement, chats and coding sessions may be kept de-identified for up to 5 years in training pipelines; turning it off later does not pull data out of training runs already in progress or models already trained; deleted chats leave back-end storage within 30 days (MHC-X05).
  7. Stale memory poisons quietly. Cursor's staff: a memory like "we use Jest" survives a migration to Vitest and "quietly poisons recommendations"; anything that duplicates code or config goes stale, anything that points to it stays correct; shared MCP memory across tools is still mostly experimental (MHC-X13).
  8. Ask of any AI product: where is this stored, for how long, and how is it reused? (S011)
- **You vs the agent (as of 2026-10-12):** The agent writes and retrieves its own memory files and reads whatever the harness injects (S002 line 219; MHC-X01). It cannot tell you the vendor's retention or training policy for your account (S011 via the batch item). The human knows where memory lives in each tool, reads and corrects or deletes wrong entries, keeps secrets out of memory files, and checks the training and retention settings instead of assuming the model "forgets" (S011; MHC-X05; MHC-X13). For client or company data, the consumer rules above do not apply to commercial plans (MHC-X05), so the person who owns the data agreement (IT, privacy or legal) decides which product and plan may hold it.
- **Currency:** Established framework (S011, July 2026). New in 2026: implicit auto memory that learns from your behaviour, which the Stanford lecturer calls a relatively new addition after earlier attempts "weren't very good" (S002 line 219). Changing: cross-tool memory (MHC-X13) and product memory features.
- **Outdated framings to avoid:**
  - "It learns from my chats and remembers me" and the opposite, "it is stateless and remembers nothing" (S011).
  - "Memory means the model was retrained on me" (S002 line 255: memory is a block in the prompt).
  - "Keep agent context in Notion or Obsidian notes": Cursor's staff say it goes out of date fast (MHC-X13).
- **Questions it answers:**
  - "I feel like I keep re-explaining the same things between tools" (Pat2, MHC-X13).
  - "Is the memory local to each execution of Claude Code?" and "Where does retrieval happen? RAG or GraphRAG?" (Stanford students, S002 lines 253, 260).
  - "Is my conversation used to train the model?" and "Why did it forget what I told it yesterday?" (batch-reader list, S011).
- **Show it for real:** Run `/memory` to open CLAUDE.md and the auto memory file, edit one line, start a new session and show `/context` listing the memory files as loaded (MHC-X02 "Check your own session"). Open `~/.claude/projects/` and show a session's JSONL transcript, then show that a fresh session does not know its contents (MHC-X01). Open the Claude privacy settings page and the model-improvement setting (MHC-X05).
- **Priority:** must. Three items from three batches, one high; on Aaron's gap list (S004); it carries the privacy risk (S011; MHC-X05).

---

### C024 Generated is not looked up: the model's knowledge has a date

- **In one line:** Without a search tool an answer is generated from dated training data; with one, a helper may have read only a summary of the page it cites; and agents confidently write code for APIs and protocols that changed after training, so check sources, dates and versions.
- **Why it is a gap:**
  - Brachman et al. (IUI 2025), cited by Lin, found users "conflate generation with search" (S011).
  - In the Stack Overflow 2026 survey 93% rate source attribution at least somewhat important when deciding whether to trust an AI technical answer (n = 13,945) and "recent or clearly up to date" is the top trust signal (72.6%), yet only 15.9% visit Stack Overflow more to verify AI answers (S080).
  - The MCP spec changed on 2026-07-28, and most explainers and agent training data still describe the 2025 protocol (S059).
- **What to teach (specific points):**
  1. Without a search or retrieval tool, an answer comes from the weights; it is generated, not fetched (S011).
  2. A model knows best what appeared in its training data often, recently and consistently; it is weaker on anything rare, recent, niche or contested (S006). Pretrained knowledge includes misconceptions and outdated material, and none of your private data (S010 companion).
  3. Retrieval and tools are what bring in current facts: retrieval raised GPT-4's FreshQA accuracy by 32.6-49.0% relative (S011).
  4. Web search pulls what is most available, not most reliable (Ng cites a report ranking Reddit as the site AI cites most), and can surface pages decades out of date (S010 companion).
  5. A helper model searches and summarises pages for the model you talk to, so the answer can cite a page that does not say what it claims; Ng: the model has "only seen summaries of those web pages". Open the citations that matter and ask for source types (S010 companion).
  6. Agents write against retired interfaces. MCP's 2026-07-28 revision retired the initialize handshake and `Mcp-Session-Id`, deprecated HTTP+SSE, replaced server-initiated sampling and elicitation with Multi Round-Trip Requests and deprecated Dynamic Client Registration; tell the agent which spec revision to target (S059).
  7. Names expire too: OpenAI announced on 2026-09-14 that GPT-5.5 leaves ChatGPT, Work and Codex on 2026-10-14, and its notes tell you to update scripts and agents that select it (S025). A model ID an agent remembers from training may already be gone.
  8. Give the agent current documents instead of its memory: an MCP server such as Context7 pulls current third-party docs (S003 line 107), and stale docs are worse than none (S003 lines 141-145).
- **You vs the agent (as of 2026-10-12):** The agent can search, fetch documentation, cite URLs and report dates and versions when it has the tools (S080 item; S003). The human requires sources for claims that matter (versions, prices, limits, APIs), opens at least one, checks that the date and version match what is installed, and checks in the transcript that a search tool call actually happened for anything time-sensitive (S080; S011; S010). The human names the version or spec to target (S059). When you cannot judge whether a cited source is right (medical, legal, financial claims), an expert has to (S011 item).
- **Currency:** Established (training cutoffs, retrieval). What is changing now is how fast the things agents write against move: a protocol revision in July 2026 (S059), model retirements on 30 days' notice (S025).
- **Outdated framings to avoid:**
  - "The AI looked it up" for an answer with no tool call (S011).
  - "If it cites a source, it read and checked it" (S010 companion).
  - "If it sounds specific, it's current" (S080 item).
  - 2025-era MCP explainers: stateful sessions, SSE transport, server callbacks over an open stream (S059).
- **Questions it answers:** "Did the AI search the web for this or make it up?"; "How current is the model's knowledge?"; "Can I trust its links?"; "Why does this MCP tutorial not match the current SDK?" (batch-reader lists from S011, S010, S059).
- **Show it for real:** Ask a model with tools off for a library's latest version, then with web search on; show the transcript with and without the search call and compare the numbers (S011 demo). Open two citations and find one that does not support the answer (S010 demo). Switch the modelcontextprotocol.io spec selector between 2025-11-25 and 2026-07-28 (S059 demo).
- **Priority:** must. Four items from four batches; it is the root of the course rule (only what can be verified can be trusted) and it fails silently.

---

### C025 What one request contains: the whole package is resent every turn

- **In one line:** The API is stateless: every turn resends the system prompt, every tool definition, injected reminders, your instruction files, memory and the full history, so tens of thousands of tokens you never typed are in the window before your first message.
- **Why it is a gap:**
  - Beginners assume the model sees only what they typed, so they cannot explain why more connectors or a long instruction file make it worse or more expensive; the CS146S lecture's whole method is to intercept the request and look (S002 lines 97-104).
  - A Stanford student asked, looking at a captured request, "Is this all the body of one request?" (S002 line 145).
  - Aaron lists system prompts and injected instruction files, and caching, as gaps (S004).
  - Anthropic's cost page has a whole section on context you did not type (S016), and its docs have a page whose job is to show it event by event (MHC-X02).
- **What to teach (specific points):**
  1. Each turn's input is "all previous conversation history plus the current user message", and everything counts toward the window: system prompt, every message, tool definitions, tool results, images, documents, and the response with its thinking (S012).
  2. A tool's name, description, comments and full signature become prompt text, and that text is how the model decides which tool to call (S002 lines 93-95).
  3. Text you never typed sits in your own message: a system reminder carrying your CLAUDE.md with a note that it overrides default behaviour (S002 lines 277-282). Claude Code also adds your output style, a note when a file it read changes on disk, and the commit and PR attribution lines (MHC-X01).
  4. Before you type, Claude Code has loaded a system prompt (about 4,200 tokens in the docs' simulation), auto memory, environment info, MCP tool names, skill descriptions and your CLAUDE.md files: "Your prompt is tiny compared to what's already loaded" (MHC-X02). The Stanford lecturer estimates tens of thousands of tokens are used before the first request (S002 line 232).
  5. The terminal hides what enters: you see "Read auth.ts" while 2,400 tokens of file content go in, and a pass count while 1,200 tokens of test output go in (MHC-X02).
  6. MCP tool schemas are now deferred by default in Claude Code (only names and server instructions load until a tool is used), but CLI tools such as `gh` still cost less context than MCP servers (MHC-X01; S016).
  7. CLAUDE.md is loaded in full at every session start; Anthropic suggests under 200 lines and moving specialised workflows into skills, which load only when used (S016; S015). The community answer to "why skills?" is the same: AGENTS.md is read at the start of every conversation, skills are lazy-loaded (MHC-X14).
  8. Caching changes the price, not the size: cached prefix tokens still occupy the window (S012), and a one-line question in an all-day session pays to re-read the whole conversation (S016).
  9. `/context` shows the live breakdown (`/context all` per MCP tool) and the `/usage` attribution shows usage by skill, subagent, plugin and MCP server (S015; S016).
- **You vs the agent (as of 2026-10-12):** The harness assembles the request; the agent reads whatever is loaded and whatever tools return (S002; MHC-X02). The human knows what is in the package and what they added: keeps standing files short, disables unused servers with `/mcp`, and asks the agent to add hooks that filter noisy output, for example grepping a 10,000-line log for errors (S016). If you build on the API, the agent can count tokens with the `usage` field and the token counting API (S012). No expert needed; team spend governance is G06.
- **Currency:** Established mechanism (S012). Changing now: deferred MCP tool loading (MHC-X01), system prompts getting shorter (S002 lines 212, 225-229).
- **Outdated framings to avoid:**
  - "The model only sees my prompt" (S002).
  - "Only my new message is sent" / "the model remembers the conversation between messages" (S012).
  - "Caching saves context space" (S012).
  - "The agent sees what I see in the terminal" (MHC-X02).
- **Questions it answers:**
  - "Is this all the body of one request?" (Stanford student, S002 line 145).
  - "Couldn't I just have an AGENTS.md that points to folders of .md files?" (MHC-X14, answered there with lazy loading and context pollution).
  - "Why is my first message already using thousands of tokens?"; "Does the model see my CLAUDE.md every time?"; "Do MCP servers cost tokens?" (batch-reader lists from S002, S016).
- **Show it for real:** Capture one Claude Code request through a logging proxy and collapse the tools and system blocks, then find the system reminder above the typed question (S002 demo). Run `/context` in a fresh session before typing, read one file, run it again (MHC-X02). Call the API in a loop printing `usage.input_tokens` and watch it grow every turn (S012 demo). Point at this course's own agent transcripts, where attribution lines appear as injected system reminders (MHC-X01).
- **Priority:** must. Four items from three batches; it explains cost (G06), context rot (C026) and why rules in chat vanish (C027).

---

### C026 Context engineering: the window fills and degrades, so curate it

- **In one line:** A 1M-token window is not 1M useful tokens: accuracy and recall fall as it fills ("context rot") and every turn re-reads it, so choose what enters, watch `/context`, and compact or clear deliberately instead of waiting for the limit.
- **Why it is a gap:**
  - Aaron lists "models getting worse as their context fills" (S004).
  - Current Claude models default to 1M windows (S012), which invites pasting everything in.
  - Even the Stanford lecturer paraphrased the study he assigned loosely ("closer to half a million truly useful tokens", S003 line 231), while the study measured roughly 8k tokens actually used (MHC-X03).
  - Anthropic teaches `/context`, `/compact` and `/clear` in its first course (S005), and Stanford's 2026 syllabus replaced prompt engineering with context engineering (S001).
- **What to teach (specific points):**
  1. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot", so curating what is in context matters as much as the window size (S012). Attention is uneven across a long document (S006).
  2. Advertised is not usable: "Some have up to a million tokens, but not all tokens are created equal" (S003 line 51). In LangWatch's audit, as the window grew 16.6x the part judges marked as used stayed near 8k tokens, falling from 47.5% of the window below 50k to 2.5% above 600k (MHC-X03).
  3. Long context is expensive as well as noisy: every tool call re-reads the window, so each doubling of context cost about 6x more over a session (MHC-X03).
  4. When to compact, by kind of work: driving a PR 200-250k, research 250-300k, QA 250-350k, building and code understanding 300-450k; the author found no benefit near 1M (MHC-X03; S003 lines 227-231).
  5. Compaction is lossy: the median compaction turned a 574,875-token window into a 4,382-token summary, and for at least 30 steps afterwards 41.9% of the user's messages contained a correction against a 17.7% baseline, while tool errors stayed flat (MHC-X03).
  6. In Claude Code, auto-compaction runs at about 967K tokens on native-1M models; set `/autocompact 500k` to compact earlier, use `/compact focus on X` at a natural break, `/clear` between unrelated tasks, and send large reads to a subagent (S015 model-config; MHC-X02).
  7. Irrelevant material makes the agent worse: every loaded MCP tool can "blow up your context" (S002 line 154), and too many extensions add noise, so skills may not trigger or Claude may lose track of your conventions (S015).
  8. The newest models are not told how full they are: the API injects a token budget and "Token usage: X/Y; Z remaining" warnings for Sonnet 5, Sonnet 4.6, Sonnet 4.5 and Haiku 4.5, but Opus 4.7 and later, Sonnet 5.5, Haiku 5.5, Fable and Mythos 5.x get no such tags; on those, an explicit "task budget" is in beta (S012).
  9. Context engineering means choosing which tools, docs and research summary go in (S002 line 154; S003); the agent cannot use what is only in your head (S008 talk 32:03).
- **You vs the agent (as of 2026-10-12):** The agent reads files on demand, delegates to subagents and compacts at the limit by itself (S005; MHC-X01). Nothing in these sources has the agent warn you that its quality is dropping, and the newest Claude models get no budget warnings (S012). The human decides what enters (servers, files, docs), watches `/context`, compacts with a focus at natural breaks or clears, and prunes CLAUDE.md, skills and servers that don't earn their place (S015; S016). Deciding which existing docs are accurate enough to feed in needs someone with a map-level mental model of the code (S003 lines 121-123, 141-145).
- **Currency:** Established ("context rot" in Anthropic's docs, S012). New in 2026: 1M windows as the default (S012), the first measured compaction study (MHC-X03, 2026-08-02), adjustable auto-compact (S015). The two sources disagree on how much of the window is useful (S003 line 241: half to three-quarters, "more intuition"; MHC-X03: about 8k in use); both say far less than advertised.
- **Outdated framings to avoid:**
  - "A bigger context window is always better / paste the whole codebase" (S012; S003).
  - "Let the agent run until it compacts by itself" (MHC-X03).
  - "Prompt engineering is the core skill" (S001).
  - "A 1M window means it remembers everything I said" (S012).
- **Questions it answers:**
  - "If the project already has a lot of Markdown docs, should the agent just read them?" (Stanford student, S003 line 139; answer: only if well maintained).
  - "Why do skills exist instead of one big AGENTS.md?" answered in the thread with "the more things the AI has in context, the worse it performs" (MHC-X14).
  - "Why does Claude get dumber in long sessions?"; "When should I use /compact?"; "Is a 1M-context model worth it?" (batch-reader list from S002, S003).
- **Show it for real:** In a long Claude Code session run `/context`, then `/compact focus on <task>`, then `/context` again and open the summary that replaced the conversation (S005; MHC-X02). Give the same task in a session loaded with unrelated files and servers and in a clean one with a short research summary, and compare the plans (S001-S003 demo).
- **Priority:** must. Four items from three batches, two high; on Aaron's list (S004); taught on day one by the vendor (S005).

---

### C027 Sessions are disposable: clear after deciding and hand off through files

- **In one line:** Compaction keeps a summary, not the conversation, and anything said only in chat can vanish, so clear once a plan is chosen and carry research memos, plans and implementation notes in files.
- **Why it is a gap:**
  - Beginners keep one endless chat, and dead ends keep steering the agent; the Stanford lecturer admitted he skipped the clear in his own demo and would not recommend that (S003 line 233).
  - People give a rule once in chat and are surprised when it is ignored hours later; Anthropic's docs warn that "detailed instructions from early in the conversation may be lost" (MHC-X01).
  - Osmani and Shihipar, writing separately in 2026, describe the same file-based, fresh-context workflow (S036; S037).
- **What to teach (specific points):**
  1. After compaction, Claude Code re-injects from disk the system prompt, root CLAUDE.md and unscoped rules, auto memory, the plan-mode plan and a fresh git status; it re-reads up to five recently modified files (one over 5,000 tokens comes back as a path only) and re-injects invoked skills (5,000 tokens each, 25,000 total, oldest dropped) (MHC-X02).
  2. What gets summarised away: path-scoped rules and nested CLAUDE.md (they reload on demand), context hooks added earlier, and instructions given only in chat; "Put persistent rules in CLAUDE.md rather than relying on conversation history" (MHC-X02; MHC-X01).
  3. Chat apps such as claude.ai can drop the oldest turns first-in-first-out (S012).
  4. Clear after choosing: if a rejected proposal stays in the window, the agent can confuse which one it is building (S003 line 233).
  5. Past a few hundred thousand tokens, have the agent write what matters to a file and start a fresh context from it; for big work, separate sessions per phase and one agent per issue (S003 lines 235, 255).
  6. "Chat history isn't a great system of record, especially after compaction": a read-only pass writes a comprehension memo citing files, the plan is made in a clean context, "A human picks the path", and review starts fresh from the acceptance criteria (S036).
  7. Start implementation in a new session from the spec and prototype, and keep `implementation-notes.md` where the agent logs every deviation from the plan (S037).
  8. Handoff files go stale like memory: point to commands and config rather than copying them (MHC-X13), and delete or update stale docs (S003 lines 141-145).
- **You vs the agent (as of 2026-10-12):** The agent writes the memo, plan, handoff file and implementation notes, implements in a fresh session and logs deviations (S036; S037). The harness compacts by itself near the limit (MHC-X01). The human decides when a decision is final and starts clean, reviews the plan's key decisions (data model, interfaces, anything user-facing) and picks the approach (S036; S037), and puts must-persist rules in root CLAUDE.md or hooks rather than in chat (MHC-X02). In areas few people understand (auth, billing, permissions), Osmani has a human pair on every step (S036; see G04).
- **Currency:** Established practice, with 2026 specifics: the compaction survival table (MHC-X02, v2.1.198), the measured cost of compaction (MHC-X03), and 2026 practitioner workflows (S036; S037).
- **Outdated framings to avoid:**
  - "Keep everything in one conversation so the AI has full context" (S003 line 233).
  - "The chat history is the record of what was decided" (S036).
  - "Once I tell it something, it remembers for the whole session" (MHC-X01).
- **Questions it answers:** "Should I start a new chat or keep going?"; "What is the difference between /clear and /compact?"; "Why did the agent forget what we figured out yesterday?"; "What does 'Conversation compacted' mean?" (batch-reader lists from S003, S012, S015, S036); "I keep re-explaining the same things between tools" (MHC-X13).
- **Show it for real:** Have a session write `plan.md`, run `/clear`, start again with "read plan.md and implement it", and show `/context` nearly empty (S003 demo). Give a rule only in chat, run `/compact`, ask the agent to restate it; then put the rule in CLAUDE.md, `/clear`, and show it loaded in `/context` (MHC-X02).
- **Priority:** should. Three items from three batches, one high; cheap to teach and pairs naturally with C026.

---

### C028 Subagents start blind and return a summary

- **In one line:** A subagent works in its own fresh window without your conversation and hands back only its final summary: that keeps your context clean, but it knows only what its brief says, its tokens still count, and its report is a claim.
- **Why it is a gap:**
  - Users assume a subagent knows everything discussed so far, then get generic results (S015 item).
  - Multi-agent setups look like free extra intelligence (S008 item). In LangWatch's audit, 82% of one day's 2.25 billion tokens came from subagents, and two forked subagents alone used 1.14 billion (MHC-X03).
- **What to teach (specific points):**
  1. A subagent gets a fresh, separate context window; only its final text response and a small metadata trailer come back. In Anthropic's example it read 6,100 tokens of files and returned 420 (MHC-X02).
  2. It starts without your conversation history or the main session's auto memory; it loads CLAUDE.md and the same MCP and skill setup, plus the task prompt the lead agent writes (MHC-X02). The built-in Explore and Plan agents skip CLAUDE.md (S015).
  3. So a constraint you stated only in chat reaches the subagent only if the lead agent writes it into the brief (follows from points 1-2, MHC-X02).
  4. A fork is different: it inherits the parent's whole conversation. LangWatch's two forked subagents started at 523K and 304K tokens instead of the roughly 30,000 a fresh subagent gets, ran 10.7 and 8.7 hours though told to do one thing and stop, and one test run at that context cost about 568,000 tokens (MHC-X03).
  5. Subagents keep verbose output out of your context, but their requests still count toward usage; agent teams use about 7x the tokens of a standard session when teammates run in plan mode (S016). Subagents get a 5-minute cache lifetime by default (S015).
  6. Patterns that work: a read-only review loop, parallel builds with explicit file ownership, competing strategies judged on the same criteria, specialists with a bounded task; "Inspect each agent's evidence before accepting the synthesis" (S008 slide 27). A code-reviewer subagent can check what was just written (S005).
  7. Starting blind is also the point: a fresh reviewer "is more likely to notice when a test proves the implementation while missing the requirement" (S036).
  8. Beginners should not start with multi-agent schemes (S008 talk 45:01).
- **You vs the agent (as of 2026-10-12):** The agent decides much of the delegation, writes the brief, spawns the workers and merges their reports (S015; S008). The human checks that delegated work carries the constraints that matter, decides when parallel work is worth the tokens, caps rounds or gives exit criteria so a ten-minute job doesn't run for an hour (S008 talk 41:01-42:02), and treats each returned summary as a claim to check against evidence (S008 slide 27). No outside expert needed; G02 covers checking claims.
- **Currency:** Subagents are established (S002 lines 341-343; S005). New in 2026: forks, agent teams and scripted fan-out (S015; S016), and coordinators running "thousands of subagents" in Cursor Projects (S025).
- **Outdated framings to avoid:**
  - "A subagent sees the whole conversation" (MHC-X02).
  - "More agents always means better results" (S008).
  - "Delegating to subagents is free" (S016; MHC-X03).
- **Questions it answers:** "Why does Claude use natural language rather than vectors when it kicks off agents?" (Stanford student, S002 line 159: the brief is text the lead agent writes); "What is a subagent?"; "Why did the subagent ignore what we discussed?"; "Should I run several agents at once?" (batch-reader lists from S015, S008).
- **Show it for real:** Ask Claude Code to use a subagent for a codebase search, open the Agent tool call to show the brief it wrote, then run `/context` to show only the summary entered the main window (MHC-X02). Show the `/usage` attribution line for subagents (S016).
- **Priority:** should. Two items, medium severity; the LangWatch incident (MHC-X03) adds a measured cost case.

---

### C029 Thinking tokens: billed output you mostly don't see

- **In one line:** Reasoning tokens are generated before the visible answer, billed as output, counted inside the output cap (so answers come back empty when it runs out), returned only as summaries, and often cannot be switched off on current models.
- **Why it is a gap:**
  - Cost intuitions built on "tokens are the words in the answer" are wrong for reasoning models; Google and OpenAI both document billing for reasoning the user never sees (S013).
  - Builders set a small token cap to save money, then get blank answers and assume the code is broken (S013).
  - Simon Willison hit it publicly: "Opus 5.5 thought for 128,000 tokens and then gave up! It ran out of tokens before it got to the response" (S033).
- **What to teach (specific points):**
  1. Claude thinking tokens are a subset of `max_tokens`, billed as output, and count toward rate limits (S012). Gemini: pricing is based on the full thought tokens "despite only the summary being output from the API" (S013). OpenAI never returns raw reasoning (S013 companion).
  2. Thought summaries are condensed versions you opt into; thinking levels and budgets apply to the raw thoughts, not the summaries (S013).
  3. The usage fields show it: `thoughtsTokenCount` (Gemini), `output_tokens_details.reasoning_tokens` (OpenAI); OpenAI's example shows 1,024 reasoning tokens out of 1,186 output tokens (S013 and companion).
  4. The output cap includes thinking. If Gemini hits it while reasoning it stops with `finish_reason: MAX_TOKENS` "and returns truncated or empty output (while still billing for any thinking tokens generated)"; OpenAI returns `status: incomplete`, possibly before any visible output, and advises reserving at least 25,000 tokens (S013).
  5. To cut cost or latency, lower the thinking level instead of shrinking the cap (S013).
  6. Thinking often cannot be turned off: "You cannot disable thinking for Gemini 3.1 Pro", Gemini 3 Flash and Flash-Lite have no full off, and `minimal` "does not guarantee that thinking is off" (S013); GPT-6 Astra rejects effort `none` with HTTP 400 (S013 companion); in Claude Code thinking can't be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable, and `MAX_THINKING_TOKENS=0` has no effect there (S015 model-config).
  7. Budgets are hints: the model "might overflow or underflow" them (S013).
  8. On current Claude models earlier thinking blocks stay in the window by default and count as input on later turns (S012).
  9. Image models think too: Gemini's image models reason before drawing, and thinking tokens are billed by default "whether you view the process or not" (MHC-X09).
- **You vs the agent (as of 2026-10-12):** The model decides per step how much to think within the effort level it is given (S015 model-config). An agent in the loop can read a finish reason and fix a parameter. The human picks the model and level knowing the floor is not zero on many current models, watches the reasoning-token fields on usage reports, and does not mistake a summary for the actual reasoning; whoever builds an app (or the agent writing it) sets caps with reasoning in mind and checks the finish reason instead of treating an empty string as an answer (S013). No expert needed.
- **Currency:** Billing as output is established; "cannot be turned off on flagship models" is new in 2026 across three vendors (S013; S015). Defaults differ by model and change with releases (Gemini 3.1 Pro defaults to `high`, Opus 5.5 in Claude Code to `medium`) (S013; S015).
- **Outdated framings to avoid:**
  - "Tokens are the words in the answer" and "hidden thinking is free" (S013).
  - "The thinking I see is the model's full reasoning" (S013).
  - "Turn thinking off to save money" / "a thinking budget is a hard limit" (S013; S015).
  - "Say 'think hard'": in Claude Code it is ordinary text; `ultrathink` and `/effort` are the controls (S015 model-config).
  - "An empty response means the model failed" (S013).
- **Questions it answers:** "Why was my bill so high for a short answer?"; "Why does my API call return an empty answer?"; "Can I turn off thinking to make it faster?"; "Is the 'thinking' shown the real reasoning?" (batch-reader lists from S013); Willison's 128,000-token give-up is the lived version (S033).
- **Show it for real:** Send one request with high thinking and print the usage block, reasoning tokens against visible output tokens; rerun with `max_output_tokens` set to 200 and show the empty text and finish reason next to the billed thinking (S013 demo). In Claude Code on Opus 5.5, open `/config` and show the "Thinking can't be turned off" row, then the `/effort` picker (S015 model-config).
- **Priority:** should. Three items from one batch plus a practitioner report (S033); one high; mostly matters to people building on the API or watching bills.

---

### C030 Outputs vary and converge

- **In one line:** The same prompt gives a different result each run, bland output usually comes from default settings rather than "the average of the internet", and AI ideas and taste converge across users, so pin down what must not vary and bring in human taste and variance.
- **Why it is a gap:**
  - Beginners expect software-like determinism and think something broke when a rerun differs (S010 item).
  - "It's just the average of the internet" leads creators to blame the model instead of changing prompts, references or settings (S011).
  - People brainstorm with AI without noticing that everyone gets similar ideas (S068).
  - Aaron, from making course videos: if you don't specify, Opus 5.5 "almost always chooses the same few voices" from ElevenLabs, and listeners recognise them (MHC-X12).
- **What to teach (specific points):**
  1. The same detailed prompt run three times gives three different but similar apps; a vague prompt gives three very different ones; more specific prompts are more predictable, but some variation always remains (S010).
  2. Short, concrete, checkable instructions steer best (S006).
  3. Models learn a long-tailed distribution, not one average answer; samey output "usually reflects product choices": low-temperature or greedy decoding, alignment pressure and uniform assistant prompts (S011).
  4. Individually better, collectively alike: LLM-assisted stories were rated more creative one by one but more similar to each other (Doshi and Hauser 2024); across 31,076 creators the idea frontier grew through volume while creativity per piece fell (Zhou, Lee and Gu 2025) (S011).
  5. In a study Mollick cites, GPT-4's ideas were more commercially viable than 50 MBA students' but "very similar to each other"; better prompting narrows the gap without closing it, and bringing in people widens the range (S068).
  6. Models have a house taste: without a stated style Opus 5.5 falls back on its own recognisable styles, its coded music and sound effects sound like it, and it reuses the same few stock voices; Aaron had to name voices explicitly (MHC-X12).
  7. Pin what must not vary: Aaron's REMORA glitches are seeded by each line's id "so the same line always sounds the same", and every clip was normalised to the same loudness so none won by being louder (MHC-X10). Record the settings when you compare outputs (S011).
  8. The choice is the human's: nine sessions (Haiku, Sonnet, Opus at low, medium, max) given the same picture and "paint this image" produced very different paintings; those that measured against the picture copied its flaws, and Aaron's favourites were first tries painted by eye (MHC-X11). Lin cites an artist who generated over 100,000 images to keep about 20 (S011).
- **You vs the agent (as of 2026-10-12):** The agent generates many variants cheaply and measures what can be measured, such as loudness and a transcript check (MHC-X10). The human supplies the specific style, references and constraints, picks among options, and supplies the unusual angle instead of shipping the first idea (S068; MHC-X11). For work whose quality is taste (web design, camera, 3D, music, lyrics), Aaron's rule is an expert in that domain as the prompter, even though the model does the work (MHC-X12).
- **Currency:** Established (sampling, decoding, S011). New-in-2026 first-hand evidence from Aaron's own work (MHC-X10, MHC-X11, MHC-X12).
- **Outdated framings to avoid:**
  - "The same prompt always gives the same result" (S010).
  - "The average of the internet, edited for tone" / "LLMs regress to the mean" / "AI can't be original" (S011).
  - "The model made it alone in one prompt" (MHC-X12).
- **Questions it answers:** "Why did it build something different this time?"; "How do I get consistent results?"; "Why does all AI writing sound the same?"; "What does temperature do?"; "Why do all AI-generated app ideas look the same?" (batch-reader lists from S010, S011, S068).
- **Show it for real:** Run a vague app prompt three times in fresh chats and line them up, then a specific prompt three times (S010 demo). Show AO-044's grid of nine paintings from one prompt (MHC-X11). Play an ElevenLabs line with the voice the agent picks by default and with a voice chosen deliberately (MHC-X12).
- **Priority:** should. The batch items are low severity, but Aaron's own posts and Playback (MHC-X10 to X12) make it central for the media makers in the audience.

---

### C031 Local and open-weight models

- **In one line:** Laptop-sized open models are now close to the frontier for some tasks, but a local model is a file plus a runtime plus settings, the default settings decide the experience, and its behaviour (refusals included) lives in the weights, so test it on your own tasks.
- **Why it is a gap:**
  - Many builders assume useful AI only runs in a paid cloud, or treat one benchmark as proof (S033).
  - People assume running open weights locally removes the vendor's refusals and biases (S011).
- **What to teach (specific points):**
  1. On 2026-04-16 Qwen3.6-35B-A3B, a 21GB file on Willison's laptop, drew a better pelican than Claude Opus 4.7; in August Qwen 3.8 27B, a 17GB download, felt "almost competitive with what was going on on the frontier" (S033).
  2. A local model is a quantised file (17GB Q4_K_M GGUF), a runtime (LM Studio, llama-server) and settings (MHC-X06).
  3. Defaults can be badly chosen: Qwen 3.8 27B defaults to `xhigh` reasoning; one prompt took 21 minutes and 22,276 reasoning tokens for 3,223 output tokens, and 137 seconds with reasoning off. Willison: start at low or no reasoning (MHC-X06). His keynote describes the same default as "high", "a terrible default" (S033).
  4. LM Studio's default 8,192-token context was eaten by reasoning; loading the full 262,144 fixed it (MHC-X06).
  5. Speed is the catch: 15-30 tokens per second locally against 74 and 184 for two hosted OpenAI models; dense models need memory bandwidth, and multi-token-prediction speculative decoding gave about 72% more (MHC-X06).
  6. The same 17GB model handled vision (bounding boxes), tool calling and a coding-agent loop (MHC-X06).
  7. Post-training changes the same weights that hold knowledge; server-side filters are separate. DeepSeek-R1's censorship persists in its open weights run locally (Naseh et al. 2025), so local is not automatically uncensored, and a fine-tune needs re-testing for regressions (S011).
  8. Benchmarks get trained for: Google trained "for all forms of animals on all forms of transport", defeating Willison's pelican test (S033).
- **You vs the agent (as of 2026-10-12):** An agent can set up the runtime, write the config and run comparative benchmarks (Willison had GPT-5.6 in Codex benchmark two server setups, MHC-X06). The human chooses local for privacy, cost or offline use, sets the reasoning level and context length, tests on their own tasks, and accepts the speed trade-off (MHC-X06; S033). Treat fine-tuning as real training: evaluate it for regressions and value shifts (S011), which needs someone who can design that evaluation.
- **Currency:** New in 2026 (S033 calls the improvement of laptop-sized open models a key trend of the year); model releases and serving tricks change weekly (MHC-X06).
- **Outdated framings to avoid:**
  - "Local models are toys compared to the cloud" (S033; MHC-X06).
  - "Local means download and chat with the defaults" (MHC-X06).
  - "A benchmark win means it's better for your work" (S033).
  - "Local open weights are uncensored by default" (S011).
- **Questions it answers:** "Can I run a good AI model on my own computer?"; "Why is my local model so slow?"; "Is a local model uncensored?"; "Which benchmark should I trust?" (batch-reader lists from S033, S011).
- **Show it for real:** Load a 17-21GB open model in LM Studio, show the reasoning-effort and context-length settings, and time the same prompt at the default and at low reasoning with the tokens-per-second readout visible (MHC-X06 demo).
- **Priority:** could. Two items, low severity, two sources; worth a short segment because Aaron's audience runs local media models (C032).

---

### C032 Models that see, hear and make media (partly sourced; diffusion still pending)

- **In one line:** A model that reads images is not a model that makes them, media costs tokens and rides along in the resent history, generation runs through separate media models and the pipelines around them, and an agent cannot see or hear its own media output without a tool.
- **Why it is a gap:**
  - Aaron lists multimodal input and output, and diffusion, as gaps; his 00.05 rebuild planned lessons on diffusion models, multimodal APIs and voice AI (S004).
  - Stanford's software course covers none of it (S001).
  - Aaron: online "Opus 5.5 made this" media leaves out the connections, asset pipelines and human direction behind it, so people who try it bare "get a really terrible generation and you wonder why" (MHC-X12).
- **What to teach (specific points):**
  1. Understanding is not generating: "Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images" (MHC-X07). Image output comes from separate image models, such as Google's Nano Banana line; Google's Imagen models are shut down and Veo is its video model (MHC-X09).
  2. Media costs tokens. Claude: each 28x28-pixel patch is one visual token, ⌈width/28⌉ × ⌈height/28⌉; Claude 4.7 and later read up to 2576px and 4,784 tokens per image, up to about three times the standard tier (MHC-X07). Gemini: an image up to 384px is 258 tokens, larger ones are tiled at 258 per 768x768 tile, video about 263 tokens per second, audio 32 per second (MHC-X08).
  3. Images ride in the resent history: a base64 image's full bytes go out again on every turn of an agent loop, so upload once with the Files API and reference it (MHC-X07). Limits: 600 images or PDF pages per request on 1M-window Claude models, 20 per message on claude.ai (MHC-X07; S012).
  4. Vision has stated limits: Claude will not identify people, counts and coordinates are approximate, small or rotated images are unreliable, it cannot tell whether an image is AI-generated, and it does not read image metadata (MHC-X07).
  5. Image models now reason and take references: Gemini's image models think before drawing (interim "thought images" are not charged, but thinking tokens are billed by default), accept up to 14 reference images including up to 4-5 for character consistency, edit across turns, and do better with the intended scene described positively ("an empty, deserted street") than with "no cars" (MHC-X09).
  6. Every image from those models carries a SynthID watermark (MHC-X09); publishing rules are G12.
  7. The agent cannot judge media it cannot perceive. Claude rendered 223 voice clips it "had no way to listen to", checked each with a transcriber, a loudness meter and a spectrogram, and left the choice to Aaron's ears (MHC-X10); agents built 16 wallpapers none of them ever saw run (S032; see C003).
  8. "One-prompt" media hides a pipeline: people wire the model to Blender MCP, Higgsfield, asset libraries, Suno and ElevenLabs; video models need reference sheets, video references, previs and style sheets; mistakes compound, so check at each stage (style sheet, previs, camera moves). Aaron's own estimate is that generation spend can dwarf the agent's own token cost (his figures, not independently checked) (MHC-X12).
  9. Not yet sourced: how diffusion models work (denoising steps, seeds, guidance) and how they differ from language models. No source read so far teaches it.
- **You vs the agent (as of 2026-10-12):** The agent can call media models, keep seeds and loudness fixed, transcribe, draw spectrograms, grab frames and build a comparison page that makes the human's review fast (MHC-X10). It cannot hear or see its output unless given a tool for that, and a measurement is not taste (MHC-X10; S032). The human reviews at each stage and picks; for each craft (camera, 3D, music, lyrics) Aaron's rule is an expert in that domain as the prompter (MHC-X12). Consent for faces and voices and disclosure belong to G12.
- **Currency:** New in 2026 and changing weekly: the Gemini image docs were updated 2026-10-09 with Nano Banana 2.1 and an Imagen shutdown (MHC-X09); high-resolution vision arrived with Claude 4.7 (MHC-X07). Diffusion content: research still pending.
- **Outdated framings to avoid:**
  - "AI means text chat" (S004 item).
  - "A multimodal model can make images" and "attachments are free" (MHC-X07).
  - "The model did it alone in one prompt" (MHC-X12).
- **Questions it answers:** "Can the model read my screenshots?"; "How do image models work differently from chat models?" (batch-reader list, S004); "Why can't I reproduce the 'made with Opus 5.5' videos I see online?" (Aaron, MHC-X12).
- **Show it for real:** Send one screenshot to Claude through the API and print the input token count; resend it base64 in a five-turn loop and watch request size grow, then switch to a Files API reference (MHC-X07). Generate an image with a Gemini image model from a prompt alone, then with reference images (MHC-X09). Open the AO-030 listening page and show the measurements beside the clips (MHC-X10).
- **Priority:** should. Aaron's explicit gap and a large part of his audience (S004; MHC-X12); now partly sourced, but the diffusion lesson needs a source that teaches it. Lead for the next batch: Aaron's ComfyUI notes (`C:\Users\soulo\Organized\Personal\My Projects\Comfyui\references\`), where his CLAUDE.md says his measured model facts and prompting rules live, plus a current diffusion explainer found by search.
