# 00.05 How AI models work today: content plan (binding)

Planner, 2026-10-02. Sources: research-now.md (the subject this month), research-change.md (Oct 2021 to Oct 2026),
COURSE.md, curriculum.md (all of it), 00.04's script (model vs app vs agent: engine, car, driver).
REBUILD: the old 5:30 lesson (tokens, desk, temperature, hallucination) is replaced at the same URL. Keep only its
base idea (tokens + the context window); everything else is rebuilt for October 2026.

Target: 18 to 20 minutes, **20 sections, ~2,750 spoken words** (hard rule: 2,520 to 2,800 words, 18 to 20 sections).
Narrator: RClayton (voice.json). Guest: **June** (`python tools/voice.py --guest`), sections 18 and 19 only.

---

## 1. Purpose line and conclusion

- **Purpose line (first spoken sentence, nothing before it):**
  "In this lesson you'll learn how today's AI models work, and how much that picture has changed in five years: what
  they take in and make, how they remember, what they cost, and the many places you'll meet them."
- **One-sentence conclusion (second sentence):**
  "Underneath it all is still a model that only knows what's on its desk right now; nearly everything new since then
  is about what gets put on that desk, what it hands off to other models, and where the desk sits."
- Then one line of permission: "Each topic gets a minute or two here; most get their own lesson later, and we'll
  point to where each one lives on the map." (A pointer, not a teaser: name the district, never "next time you'll...".)

## 2. As of

**As of October 2026** (researched 2026-10-02). Dated on-screen cards carry versions and prices ("Oct 2026"); the
narration names families (Claude: Haiku, Sonnet, Opus, Fable; OpenAI: G P T; Google: Gemini), never version numbers.

## 3. The change arc

**Five years ago (autumn 2021).** One model behind one text endpoint. GPT-3 was reached through an A P I only: text
in, text out, a context of about two thousand tokens (2020). No ChatGPT, no Claude app, no Gemini. No memory, no
custom instructions, no tools, no agents, no voice, no plans or tiers. Diffusion was a 2020 research paper; image
generators were a curiosity (DALL-E 2 and Stable Diffusion came in 2022). RAG was a 2020 paper.

**What changed (dated turning points to draw on a strip):**
- 2022: Stable Diffusion open weights (Aug); ChatGPT, text only (30 Nov).
- 2023: 100K-token window on Claude (May); ChatGPT custom instructions (Jul); ChatGPT can see and hear (Sep).
- 2024: 1M-token window on Gemini (Feb); Claude reads images (Mar); GPT-4o, one model for text, audio and images
  (May); prompt caching (Anthropic Aug, OpenAI Oct); thinking models (Sep); MCP (25 Nov).
- 2025: Claude Code (Feb); native image output in ChatGPT (Mar); memory spreads; "context rot" measured (Chroma, Jul);
  consumer-plan training opt-out change (Aug to Oct); Skills (16 Oct); MCP, AGENTS.md and Skills move to open
  standards (Dec).
- 2026: Cowork (Jan); OpenClaw goes viral (Jan) and Hermes Agent (Feb); free Claude gets memory (Mar); Sora app shut
  (spring); Claude Design (Apr); temperature/top-p rejected on the newest Claude models (spring); Gemini CLI becomes
  Antigravity (Jun); GPT-Live full-duplex voice and ChatGPT's Chat/Work/Codex desktop (Jul); Meta Muse (8 Sep);
  Claude chat and Cowork merge (16 Sep, rolling out); Claude Marketplace (23 Sep); OpenAI dots (29 Sep).

**Now (October 2026).** Still one next-token model at the centre, but: a desk of a million tokens that gets worse as
it fills; models that see images, documents and (Gemini) audio and video, and hand picture, sound and video work to
specialist generators, mostly diffusion; five different kinds of "memory", all of them text put back on the desk;
standing instructions and instruction files injected every turn; four meters on the bill, two of them for the cache;
knobs moved from temperature to effort; the same model reached through many rooms (chat that now also does work,
Code), many buildings (web, desktop, terminal, phone, cloud sessions), add-ons (skills, connectors, plugins) from
marketplaces, and always-on agents with their own computers.

**Where it is heading (dated signals only, hedged):** fewer modes, one agent that decides whether to answer or to work
(Anthropic 16 Sep 2026, OpenAI Jul 2026); agents that keep running on their own cloud machines; curation of the
window beats bigger windows (compaction, memory files, skills and tools loaded on demand); effort and thinking replace
sampling knobs; open standards for the plumbing (MCP, AGENTS.md, Agent Skills); diffusion for text is fast but not
frontier quality, and whether it catches up is an open question; the safety question shifts to "what did my agent
just do?".

**What did not change (say it; it is the anchor):** the model predicts the next token from what is in its window; it
keeps nothing between calls; it is paid for and limited in tokens; it can still be confidently wrong; instructions
are text, not locks.

## 4. MUST-COVER, in script order (one scene per section)

Depth key: **teach** = the idea lands with a mechanism; **brief** = two to four sentences, named and shelved;
**one line** = a single sentence. Seconds are spoken-time budgets (narrator ~2.35 words/s, June ~2.47).

| # | Section (working heading) | Must-cover topics (depth) | Words | Seconds |
|---|---|---|---|---|
| 01 | The point | Purpose line; conclusion; "brief here, own lessons later" (one line) | 60 | 26 |
| 02 | Where it lives | Map pin on Start / Orientation; the Lanterns hang over every district and are not a district; this lesson is the tour of the whole lantern, topics shelved where they live (brief) | 75 | 32 |
| 03 | The desk, five years ago and now | Mental model introduced: the model is a clerk who only knows what is on the desk right now. Builds on 00.04 in one line ("00.04 split model, app and agent; this opens the model's workspace"), no re-teaching. 2021 picture: a tiny desk, text cards only, letters through one slot (A P I only, ~2K tokens). Now: a desk the size of a hall, photos and tapes on it, rooms and phone lines around it (teach: the change arc in one picture). What did not change: next-token guessing, nothing kept between calls (one line each) | 130 | 55 |
| 04 | Tokens, and a desk that grew | Tokens as the unit (pieces of words; about four characters of English, roughly) (teach, base idea). Everything on the desk counts: hidden instructions, every message, files, images, tool results, the model's own thinking and reply (teach). Window growth 2K to 100K (2023) to 1M (2024; standard on Claude's bigger models in 2026, not Haiku) (brief). Token counts aren't comparable across model generations (newer Claude tokenizer: ~30% more tokens for the same text) (one line) | 135 | 57 |
| 05 | A fuller desk is a worse desk | Context rot: accuracy and recall fall as the window fills, well before it is full (Chroma 2025, 18 models; Anthropic's docs use the term) (teach). "Lost in the middle" (one line). Countermeasures you will see: compaction (summarise and continue; Claude Code auto-compacts), clearing old tool results, sub-agents with their own fresh desk, tools loaded only when needed (brief). Prompt engineering became "context engineering" (one line) | 135 | 57 |
| 06 | Seeing, hearing, and making | Text-only to multimodal (teach): three meanings: (a) reads many kinds of input, (b) produces many kinds natively (rare), (c) the app hands the job to a separate specialist model through an A P I or tool (most common). Claude: text, images and P D Fs in, text out only; makes visuals by writing code or by calling another model through a connector. Gemini: text, image, audio and video in one request; separate generation models. ChatGPT feels like one model but stitches several (image model, voice model). OpenAI shut down its Sora video app this spring (one line) | 160 | 68 |
| 07 | Diffusion: from static to picture | One picture: start from pure noise, remove a little per step, guided by the prompt, until the image appears; modern models do it in a compressed space (teach). Used for images, video, audio and music; most current ones use a close cousin called flow matching, fewer steps (brief). Not every image model is diffusion: OpenAI's image models are reported to build images piece by piece like text (one line). Diffusion for text exists but is uncommon: Inception's Mercury models and Google's experimental DiffusionGemma / Gemini Diffusion, very fast, smaller-model quality; every frontier chat model still writes one token after another (brief) | 165 | 70 |
| 08 | The knobs, then and now | Temperature (randomness), top-p and top-k (how many candidate words are allowed), max output tokens (hard cap) (brief, one sentence each). The change: the newest Claude models reject custom temperature/top-p/top-k; the knob that matters now is effort / thinking (how long the model works before answering); in apps the user touches model choice, effort and speed (brief). Hallucination: still there, fewer with search and tools, now also wrong actions and invented package names, not just facts (one line + one line) | 120 | 51 |
| 09 | How it "remembers" | The model keeps nothing; every memory is text something puts back on the desk (teach). Five kinds, drawn as five ways paper returns to the desk: 1) the conversation itself, re-sent each turn; 2) a memory the assistant keeps about you itself (Claude, ChatGPT, Gemini; free Claude since Mar 2026; ChatGPT rewrites its memories in the background); 3) searching old chats with a tool; 4) external stores reached by tool calls: files on your computer (Claude Code's memory files, the A P I memory tool), Notion or Drive through a connector; 5) RAG: retrieve the relevant pieces, paste them in, then answer (vector search is one way; coding agents now mostly search with plain file tools) (teach the list; each item brief). Each retrieval costs a tool call and desk space (one line) | 170 | 72 |
| 10 | Notes pinned to the desk | System prompt: the app's hidden instructions read first (Anthropic publishes claude.ai's) (brief). Your own standing instructions: preferences, styles, project instructions; re-sent every turn (brief). Injected instruction files: CLAUDE.md at a project's root (plus the user-level and company-managed ones) is loaded automatically at session start; folders below load when the agent reads there; AGENTS.md is the cross-tool open version, which Claude Code now also reads; GEMINI.md, Cursor rules are the same idea (teach). It is context, not a lock: hooks and permissions enforce; long files lower adherence; it costs tokens every turn (brief) | 135 | 57 |
| 11 | Keeping the desk warm: caching | Mechanism: the provider stores the work it already did on the start of your prompt (the prefix) and reuses it when the next request starts identically (teach). Order: tools, then system prompt, then messages; change anything early and everything after it is rebuilt (teach). Time to live: 5 minutes by default, 1 hour optional, each hit resets the timer; Claude Code on a subscription keeps it an hour, on an A P I key five minutes; after a longer break the first message rebuilds from scratch (brief). What breaks it: editing the system prompt or CLAUDE.md mid-session, changing tools or connectors, switching model, toggling thinking or top-level effort, adding or removing images, compaction (brief, on screen as a list) | 150 | 64 |
| 12 | The four meters | Normal input (full price), cache write (more than input: 1.25x for 5 minutes, 2x for an hour), cache read (a tenth of input or less), output (the expensive one, about five times input, thinking included) (teach). Why a long chat costs more every turn even when nothing new is typed: the whole desk is re-sent, cheap only if warm (brief). Cached tokens still fill the window (one line). OpenAI and Google cache automatically too (one line) | 120 | 51 |
| 13 | Rooms and buildings: modes and platforms | Mode = what kind of job; platform = where it runs and what it can touch (teach). Modes: chat, Cowork (Jan 2026, an agent for office work on your files), Code. On 16 Sep 2026 Anthropic merged chat and Cowork into one Claude that decides whether to answer or to do the work; rolling out to Pro and Max now, Team and Free later, so some viewers still see the old tabs; Claude Code stays separate (brief, hedged). Platforms: browser, desktop app, phone, terminal C L I, editor extensions, and cloud sessions that run on Anthropic's machines and keep going with the laptop shut (brief). Local vs cloud: local sees your files and stops when your laptop sleeps; cloud sees only what you give it and keeps running (teach). Equivalents: ChatGPT's Chat / Work / Codex; Google's Antigravity replaced Gemini C L I in June (one line) | 155 | 66 |
| 14 | Skills, connectors, plugins | Skill = a folder of instructions (SKILL.md, maybe scripts) whose label sits on the desk and whose pages load only when needed; open standard used by Codex, Gemini, Copilot, Cursor (brief). Connector = a phone line to another service (Gmail, Notion, GitHub), built on MCP (brief). Plugin = a boxed kit of skills, connectors, commands and hooks (brief). Where you get them: the in-app directory; the Claude Marketplace (23 Sep 2026); Claude Code plugin marketplaces, which are just git repositories anyone can host; OpenAI's apps and plugins (brief). Third-party ones are code you trust: OpenClaw's skill store had hundreds of malicious skills in Feb 2026 (one line) | 135 | 57 |
| 15 | Individual vs enterprise | Same models, different building rules (teach in one picture). Individual (Free, Pro, Max): mostly differ in usage limits; consumer chats may be used for training unless you turn it off (since autumn 2025). Team/Enterprise: single sign-on, admin control of which connectors, plugins and skills are allowed, audit logs, custom data retention, managed instruction files pushed to every machine, not trained on by default, advance notice of product changes (brief). Since Apr 2026 Claude subscriptions can't power third-party agents like OpenClaw; those need an A P I key (one line) | 105 | 45 |
| 16 | More rooms: design and voice | Claude Design (Apr 2026, research preview; describe a visual, Claude drafts it as layout and code, not with an image model; since Sep it works inside chats, beta); Claude Docs and Slides (beta, Sep 2026) (brief). Voice modes: Claude voice can now use the bigger models and connected apps (Jul 2026) and takes turns; OpenAI's GPT-Live and Gemini Live are speech-to-speech, so you can interrupt them. Pipeline (speech to text, model, text to speech) vs native speech models is the one idea (brief) | 120 | 51 |
| 17 | Desks that never close: personal agents | The category: always on, its own computer, you message it from chat apps, long memory, broad permission to act (teach in one picture). Two camps: self-hosted open source (OpenClaw: viral Jan 2026, ex-Clawdbot; Hermes Agent from Nous Research, Feb 2026, a competitor that turns solved problems into its own skills): your machine, your keys, your risk; hosted by a big company (Meta's Muse, 8 Sep; OpenAI's dots, 29 Sep, rolling out; Google's Gemini Spark for Ultra subscribers): their cloud computer, their approval rules (brief). Anthropic's nearest pieces: cloud sessions, scheduled routines, Dispatch from your phone (one line). OpenClaw's Feb 2026 security crisis: exposed instances and malicious skills (one line). Hand-over to June by name | 160 | 68 |
| 18 | Myth or still true? Part one [guest] | June, quick-fire. Each myth: what people say, verdict, the true version, and the literal thing you'll see on screen. 1) "Set temperature to zero for the same answer every time": newest Claude models return an error for it, and zero never guaranteed identical output. 2) "It remembers me": it re-reads a summary, searches old chats, or opens a file. 3) "A bigger window means it remembers everything": context rot; you'll see auto-compact. 4) "All AI art is diffusion": mostly, not all. 5) "Claude can draw that for you": it writes code or calls another model | 200 | 81 |
| 19 | Myth or still true? Part two [guest] | June continues. 6) "Cached tokens are free": writes cost more; reads are cheap but still fill the desk; a coffee break longer than the timer and the next message rebuilds. 7) "I pay for Pro, so my chats aren't trained on": consumer plans train unless you switch it off; work plans don't by default. 8) "My subscription can run any agent": not third-party ones, since April. 9) "CLAUDE.md is a rule it must obey": it's a note; hooks and permissions are the locks. 10) "Sora is where AI video lives": shut this spring. June hands back to the narrator by name | 200 | 81 |
| 20 | Where it's heading, and keep this | Heading (dated, hedged, three sentences): fewer modes, one agent; agents with their own computers; curating the desk beats a bigger desk. Safe to ignore for now: version numbers, leaderboards, and the maths inside the model. Keep this: three bold-lead takeaways (end card and `keep:`) | 120 | 51 |
| | **Total** | | **2,750** | **1,160 (19:20)** |

Guest total: 400 words, 162 s (limit 650 words / 300 s). One run, sections 18 to 19, consecutive.

**Keep this (draft bold leads):**
1. **The model only knows what's on its desk right now.** Memory, files, chat search and instruction files are all
   text put back on the desk, and a fuller desk is a worse desk.
2. **Most "multimodal" is a hand-off.** The model reads many kinds of input; pictures, sound and video usually come
   from a separate model, most often a diffusion model that clears noise into an image.
3. **Same model, many rooms, four meters.** Modes, platforms, plugins and plans change what it can touch and what it
   costs; a warm cache makes repeats cheap, and anything changed early in the prompt rebuilds it.

**The "surprises you'll hit" beat (mandatory) is distributed:** every teach section shows at least one literal thing
the viewer will meet, and the guest round collects the rest. Screen literals to use (illustrative, not quotes of one
product unless marked): a token counter / "context left" meter (04); "auto-compact" and `/compact` (05); a paperclip
accepting image/PDF/audio (06); a noisy-to-clear strip of frames (07); an error card "temperature is not supported for
this model" (generic wording) and an effort picker `low · medium · high · xhigh · max` (08); "Searched past chats" /
a memory panel (09); a file tree with `CLAUDE.md` and `AGENTS.md` at the root (10); the usage fields
`input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens` (12); tabs "Chat · Cowork ·
Code" fading to "Claude · Claude Code" (13); `SKILL.md`, a connector card, a plugin box (14); "Research preview" /
"Beta" badges (16).

## 5. DEFERRED (introduced here only; owner lesson)

| Topic | Owner |
|---|---|
| Vector databases, embeddings, RAG in depth; agentic search vs vector search | 06.06 |
| How AI apps remember (memory features, chat search, memory files) in depth | NEW: 06.07 How AI apps remember (module 06 Data) |
| Tools, skills and MCP in practice | 10.10 |
| MCP itself (client, server, tools) and installing servers | 10.08, 10.09 |
| Skill/plugin marketplaces and what you're trusting when you install one | NEW: 10.12 Plugin and skill marketplaces (module 10); risk side links 05.08 supply-chain risk |
| Subscriptions vs API billing, plan limits, third-party harness rule | 10.11 |
| Prompt caching and the four token meters in depth | NEW: 10.13 Prompt caching and the token meters (module 10) |
| Sampling settings and effort as request parameters | 10.03 anatomy of one API call |
| Streaming replies token by token | 10.06 |
| Coding agents, Claude Code surfaces, local vs cloud sessions | 03.08 |
| Instruction files (CLAUDE.md, AGENTS.md), versioning prompts | 03.09 |
| Context rot and context engineering (compaction, sub-agents, what goes in the window) | NEW: 03.10 Context engineering: managing the window (module 03) |
| Sub-agents and multi-agent fan-out | 07.07 |
| Diffusion and flow models for image, video, audio; how generators work | NEW: 01.13 How image, video and sound generators work (module 01, beside 01.10) |
| Running diffusion or language models locally | 01.10 |
| Multimodal inputs/outputs through an API (sending images, audio, video; calling generator models) | NEW: 10.14 Multimodal APIs (module 10) |
| Voice AI: pipelines vs speech-to-speech | NEW: 10.15 Voice AI (module 10, after 10.06 streaming) |
| Scheduled and background agents, cloud routines | 16.11 |
| Always-on personal agents (OpenClaw, Hermes, Muse, dots) and their risks | NEW: 16.13 Always-on personal agents (module 16); keys side 14.12 |
| Individual vs enterprise plans, SSO, admin policy, retention | NEW: 15.14 AI at work: enterprise plans and admin controls (module 15); SSO concept 14.09 |
| Training on your data, retention, opt-outs | 15.13 |
| Claude Design, Docs, Slides and other AI builders | NEW: 17.10 AI design and app builders (module 17) |
| Hallucination: verifying answers | 00.06 how to learn anything technical |
| Hallucinated package names | 05.08 supply-chain risk |
| Open-weights licences (e.g. DiffusionGemma, Apache 2.0) | 20.06 |
| Model vs app vs agent | 00.04 (already taught; one-line callback only) |

The NEW rows are suggestions for curriculum.md (the orchestrator decides IDs; the lesson only names the district on
screen, e.g. "shelved in The Network, module 10").

## 6. Mental model: the clerk at the desk

**The model is a brilliant clerk who knows only what is on the desk right now.** Nothing is kept overnight; whatever
the clerk needs must be on the desk when the request arrives. One desk object persists in every scene and transforms:

- **03, 2021:** a small desk, index cards only, a single letter slot in the door (an A P I, ~2K tokens).
- **04:** the desk measured in tiles (tokens); it grows into a hall-sized desk (1M). Everything lands on it: the
  pinned note, the letters, photos, tool results, the clerk's own scratch paper.
- **05:** the hall-sized desk piles up; the clerk misses the note in the middle (context rot). Fixes: a one-page
  summary replaces the pile (compaction), old papers swept off, a second clerk at a fresh desk (sub-agent).
- **06:** photos, tapes and film reels arrive on the desk (input). The clerk only writes; for a picture it phones the
  studio next door (a specialist model through a tool or A P I).
- **07:** the studio: a different worker who starts with a page of static and wipes a little away each pass until the
  picture appears (diffusion). In one corner, a rare clerk who writes a whole page at once from a smudge (diffusion
  text).
- **08:** the dials on the desk lamp: temperature and top-p dials taped over; a new "effort" dial (how long the clerk
  works before answering).
- **09:** five ways paper returns to the desk: the conversation re-sent, a profile card the clerk keeps about you, a
  filing cabinet of old chats it searches, a phone line to the library or Notion across the street, an index-card
  catalogue that fetches the right pages (RAG).
- **10:** sticky notes pinned along the top edge: the vendor's note, your note, and the CLAUDE.md note that appears
  by itself when the clerk sits at that project's desk. A note, not a lock.
- **11 to 12:** the desk left laid out, in order, under a timer (cache). Swap a paper near the top and everything
  below must be laid out again. Four meters on the wall: fresh paper, laying out (write), reusing the layout (read),
  the clerk's writing (output).
- **13:** the same clerk in different rooms (chat, Cowork, Code; two rooms merging into one) and buildings (browser,
  desktop, terminal, phone, a cloud office that stays lit when you go home).
- **14:** a shelf of manuals showing only their spines until opened (skills), phone lines (connectors), boxed kits
  holding both (plugins), and the shops that sell them (marketplaces).
- **15:** home office vs company building: badge doors (sign-on), a security desk log (audit), a shredding schedule
  (retention), an approved-supplies list (connector policy).
- **16:** a design studio room; a phone line for voice (relayed through a typist, or a clerk who can actually listen).
- **17:** a desk that never closes, in its own office, that you text from your phone: in your house (self-hosted) or
  in their building (hosted).
- **20:** pull back to the whole desk, then the end card.

**Where it breaks (say so plainly, in 03/04 and again briefly where it bites):**
- There is no clerk who persists. Every request starts a fresh copy that reads the whole desk at once; "the clerk"
  exists only for the length of one reply.
- The clerk doesn't read top to bottom like a person; it weighs everything together, and that is why the middle of a
  huge pile gets missed.
- The cache is not the clerk remembering; it is stored arithmetic about the start of the desk, kept by the provider's
  servers, thrown away when the timer runs out.
- The diffusion studio is not a clerk at all: a different kind of model that never writes word by word.
- Connectors and files are not "the clerk going somewhere": the model writes a request as text, and the app makes the
  call (00.04's point, one line).

Continuity note: 00.04's engine/car/driver stays 00.04's. Here, one line in 03 links them ("inside the engine of
00.04 there is, in effect, one desk"), then the desk carries the lesson.

## 7. Cut list (tempting, staying out)

- Transformer, attention and embedding maths; training, RLHF, fine-tuning: not needed for the mental model; owned
  elsewhere or safe to ignore.
- Version-by-version comparisons, benchmark scores, leaderboards, "which model is best": stale within weeks.
- Full price tables. Only relative multipliers in narration; one dated price card on screen at most.
- Mythos / Project Glasswing, Fable vs Mythos, Claude Science, Managed Agents, Bedrock/Vertex/Foundry channels, Batch
  API, fast mode, US-only inference: true but not what a learner meets this month in the basic picture.
- Minimum cacheable prefix sizes, cache breakpoints, pre-warming, cache diagnostics: how-to detail for 10.13.
- Token-budget "context awareness" injections, task budgets: too fine-grained.
- OpenAI's reported new $500 tier: reported, not needed.
- OpenClaw star counts and the full rename saga beyond "it started as Clawdbot": numbers vary by source.
- Hallucination rate numbers: benchmark-specific; quoting one as "the rate" would mislead.
- Hybrid autoregressive-diffusion research (e.g. NVIDIA Nemotron-Labs-Diffusion): research, not something learners meet.
- Gemini Gems, GPT Store history, ChatGPT 2023 plugins: one clause at most ("the word plugin came back").
- How to write a CLAUDE.md, how to set up memory, how to install a plugin: how-to, not this course's job here.
- Running models locally and Aaron's ComfyUI stack: 01.10 owns it; at most one line naming that his local image and
  video tools are this family.
- Anything predicting an unannounced Anthropic "dots-style" product: speculation.

## 8. Facts to handle carefully (hedged wording to use)

| Claim | Status | Say it this way |
|---|---|---|
| Chat and Cowork merged | Announced 16 Sep 2026, rolling out to Pro and Max; Team and Free "soon"; Enterprise with notice | "In mid-September Anthropic began merging chat and Cowork into one Claude. It's rolling out now, so you may still see the old tabs." Never "will be combined soon", never "done everywhere". |
| Temperature/top-p/top-k removed | Research files disagree on which model started it (Opus 4.7 vs 4.8); both agree current Claude models reject non-default values | "The newest Claude models no longer accept a custom temperature." No first-version name, no date more precise than "this year". |
| Temperature 0 = deterministic | False per Anthropic docs | "Zero never guaranteed the same answer twice." |
| 1M context | Default on current Claude models except Haiku | "a million tokens on Claude's bigger models"; card: "Oct 2026". |
| Tokenizer +30% | Anthropic pricing doc | "Newer Claude models count about a third more tokens for the same text"; or omit numbers: "token counts don't compare across models". |
| Cache read price | 0.1x on most, 0.05x Opus 5.5, 0.025x Fable 5.1 | "a tenth of the input price, or less". |
| Cache write price | 1.25x (5 min), 2x (1 h) | Exact multipliers OK on screen with "Claude A P I, Oct 2026". |
| Claude Code cache TTL | 1 h on subscription, 5 min on A P I key | Say as stated, attribute to Claude Code. |
| Claude can't make images | Established; text-only output | "Claude writes only text. For pictures it writes code, or calls another model through a connector." |
| GPT Image is autoregressive | Reported; OpenAI hasn't fully published | "OpenAI's image models are reported to build pictures piece by piece, like text." |
| Video models are diffusion | Closed-model internals not all published | "Most video generators are this family, as far as their makers have said." |
| Diffusion text models | Mercury (Inception; 2 in Feb, 2.5 in Sep 2026), DiffusionGemma (open, Jun 2026), Gemini Diffusion (experimental) | "a few diffusion text models exist, like Inception's Mercury and Google's experimental ones: very fast, not yet frontier quality". No version, no speed figures spoken. |
| Sora | App announced shut 24 Mar, closed 26 Apr 2026; API removed Sep 2026 | "OpenAI shut down its Sora video app this spring." |
| Gemini audio/video input | Live docs | Fine as stated; versions only on a dated card. |
| Memory on free plans | Claude free since 2 Mar 2026; Gemini past chats free Feb-Mar 2026 (not EEA/UK/CH) | "Memory is no longer a paid extra on Claude or Gemini" with "in most regions" for Gemini if named. |
| ChatGPT rewriting memory | "Dreaming" (Jun 2026), secondary sources | "ChatGPT now rewrites its memories of you in the background." No version name. |
| Coding agents moved from vector RAG to file search | Trend, secondary sources | "Coding agents now mostly search with plain file tools instead." |
| CLAUDE.md / AGENTS.md | Live docs; AGENTS.md reading is new | "Claude Code also reads AGENTS.md, the open version other tools use." |
| Consumer training | Since Aug-Oct 2025, opt-out | "Consumer plans, paid ones included, may be used for training unless you turn that off. Work plans aren't, by default." |
| Subscription in third-party agents | Since 4 Apr 2026 | "Since April, a Claude subscription can't power third-party agents like OpenClaw." |
| Claude Marketplace | Launched 23 Sep 2026, reported as 2,000+ items | "a marketplace launched in late September"; "more than two thousand" only with "reported". |
| Skills as open standard | Dec 2025, adopted widely (counts vary 30+/40+) | "an open format other tools now use too". No count. |
| Claude Design | Research preview since 17 Apr 2026; inside chats since 16 Sep (beta) | Always with "research preview" / "beta" badge on screen. |
| Claude voice | Opus/Sonnet + connectors since 23 Jul 2026; stack not disclosed | "Claude's voice mode takes turns; Anthropic hasn't said how it's built." Never claim Claude hears audio natively. |
| GPT-Live | Full-duplex, default ChatGPT voice since Jul 2026 | "You can interrupt it mid-sentence." |
| OpenClaw history | Clawdbot Nov 2025, Moltbot 27 Jan, OpenClaw 30 Jan 2026; creator joined OpenAI Feb 2026 | "started as Clawdbot, went viral in January". No star counts. |
| OpenClaw security | Feb 2026: hundreds of malicious skills (counts 341 to 1,184 by auditor), ~135k exposed instances | "hundreds of malicious skills and thousands of exposed installs". |
| Hermes Agent | Nous Research, Feb 2026; competitor, not successor | "a rival from Nous Research". Never "successor". Its OpenRouter ranking lead: omit. |
| Muse | Meta, 8 Sep 2026, US only | "Meta's Muse, launched in September in the US". |
| dots | OpenAI DevDay 29 Sep 2026, rolling out, Pro and Business Premium; lower-case per OpenAI | Screen "dots" lower-case; "announced this week" is wrong by air date, use "at the end of September, rolling out". |
| Gemini Spark | I/O May 2026, Ultra only | "Google's Gemini Spark, for its top plan". |
| Gemini CLI to Antigravity | Retired 18 Jun 2026 | "Google folded Gemini C L I into Antigravity in June." |
| ChatGPT Chat / Work / Codex | Desktop app 9 Jul 2026 | "OpenAI made the same move in July." |
| Anthropic "always-on" product | None announced | Only name what exists (cloud sessions, routines, Dispatch, the merged Claude that keeps working). No forecast. |
| Hallucination rates | Benchmark-specific | No numbers. "Less often than before, but not never." |
| Where it is heading | Direction claims | Frame as "what the companies are doing this year", each tied to a dated move; anything beyond that: "nobody knows yet". |

General rules: versions and prices only on dated cards; "this spring / in September / this year" in speech; any
feature tagged beta or research preview carries the badge on screen.
