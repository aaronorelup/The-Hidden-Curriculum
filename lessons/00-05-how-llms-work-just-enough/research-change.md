# 00.05 research: the last five years of change (Oct 2021 -> Oct 2026)

Researched 2026-10-02. Lens: what it looked like ~5 years ago, turning points with dates, what got renamed or replaced, which old explanations now mislead, and what did NOT change.
Status tags: [established] = settled, >1 year old · [new 2026] = shipped this year · [beta/announced] = preview, rolling out, or announced only · [speculation] = expectation, not announced.
Source quality note: vendor pages (anthropic.com, platform.claude.com, code.claude.com, support.claude.com, openai.com, blog.google) beat news (TechCrunch, VentureBeat, 9to5, Axios, Bleeping) beat blogs/SEO explainers. Where only a blog backs a claim it is marked "(secondary)"; the currency checker should re-verify those before they are spoken as hard numbers.

## 0. Five years ago in one paragraph (baseline, ~Oct 2021)
- GPT-3 (2020) was API-only, text in / text out, ~2,048-token context; no ChatGPT, no Claude product, no Gemini. https://arxiv.org/abs/2005.14165 (May 2020) [established]
- Image generation was a research curiosity: DDPM (the paper that made diffusion practical) June 2020; DALL-E 2 Apr 2022 and Stable Diffusion Aug 2022 came after. https://arxiv.org/abs/2006.11239 (Jun 2020) · https://stability.ai/news/stable-diffusion-public-release (Aug 22 2022) [established]
- RAG existed only as a paper (Lewis et al., Facebook AI). https://arxiv.org/abs/2005.11401 (May 2020) [established]
- No memory, no system-prompt UI, no tools, no agents, no plans/tiers, no voice. "AI" for a builder meant calling one text endpoint.

## 1. Text-only LLMs -> multimodal models (in and out)
- ChatGPT launches (text only), 30 Nov 2022. https://openai.com/index/chatgpt/ (Nov 2022) [established]
- Vision input arrives: GPT-4V in ChatGPT 25 Sep 2023; Claude 3 family with vision 4 Mar 2024; Gemini built "natively multimodal" from Dec 2023. https://openai.com/index/chatgpt-can-now-see-hear-and-speak/ (Sep 2023) · https://www.anthropic.com/news/claude-3-family (Mar 2024) [established]
- GPT-4o ("omni"), one model handling text, audio, images natively, May 2024. https://en.wikipedia.org/wiki/GPT-4o [established]
- Native image OUTPUT inside the chat model: GPT-4o image generation 25 Mar 2025, and it is autoregressive, not diffusion (unlike DALL-E). https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf (Mar 25 2025) [established]
- Gemini 3.5 Flash (I/O, 19 May 2026): text + image + audio + video in one request, 1M context. https://codersera.com/blog/gemini-3-5-complete-guide-2026/ (2026, secondary) [new 2026]
- Gemini Omni (I/O, 19 May 2026): one model taking text/image/audio/video in any mix and producing video with native audio; positioned to replace Veo 3.1; no "Veo 4" exists. https://gemini.google/overview/video-generation/ · https://aireiter.com/blog/veo-4 (Aug 2026, secondary) [new 2026]
- GPT-6 family (Astra 4 Sep 2026; Sol and Luna 22 Sep 2026). https://en.wikipedia.org/wiki/GPT-6 · https://overchat.ai/ai-hub/gpt-6-released-date (Sep 2026) [new 2026]
- Claude (Opus 5.5, Sep 2026) reads images, PDFs; does NOT generate images natively. Visual output = code (SVG/HTML artifacts, Claude Design) or a separate image model reached through a connector/MCP tool. https://godofprompt.ai/blog/can-claude-generate-images/ (2026, secondary) · https://www.anthropic.com/news/claude-design-anthropic-labs (Apr 2026) [established, verify no change before air]
- Video model as a consumer app proved fragile: OpenAI announced 24 Mar 2026 it was shutting the Sora app (closed 26 Apr 2026; Sora 2 API removal 24 Sep 2026). https://9to5google.com/2026/03/24/openai-shutting-down-sora-video-generation-app-but-without-explaining-why/ (Mar 2026) · https://techcrunch.com/2026/03/29/soras-shutdown-could-be-a-reality-check-moment-for-ai-video/ (Mar 2026) [new 2026]
- Durable idea: "multimodal" splits into (a) can SEE/HEAR (input), (b) can MAKE (output) natively, (c) makes it by calling another model as a tool. Three different things.

## 2. Tokens, context window, and long-context degradation ("context rot")
- Window growth: ~2K (GPT-3, 2020) -> 100K (Claude, May 2023) -> 1M (Gemini 1.5, Feb 2024) -> 1M standard on Claude, no beta, standard price (13 Mar 2026 for Opus 4.6/Sonnet 4.6; default on Opus 4.8 28 May 2026, Opus 5 24 Jul, Opus 5.5 22 Sep, Sonnet 5.5 28 Sep 2026). https://www.anthropic.com/news/100k-context-windows (May 2023) · https://platform.claude.com/docs/en/release-notes/overview (Sep 30 2026) [established -> new 2026]
- Max OUTPUT also grew: 128k output tokens on current Claude models. same release notes [new 2026]
- "Lost in the Middle": models use info at start/end of a long context better than the middle. https://arxiv.org/abs/2307.03172 (Jul 2023) [established]
- Chroma "Context Rot" report: 18 models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3) all degrade as input grows, even on simple tasks; distractors and similar-but-wrong passages hurt more. https://www.trychroma.com/research/context-rot (Jul 2025) [established]
- Anthropic names the problem "context rot" and treats context as a finite "attention budget"; fixes: compaction (summarise and restart), structured note-taking to files, sub-agents with fresh windows, tool-result clearing. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Sep 29 2025) [established]
- Research term still active in 2026 (e.g. "Classifier Context Rot", May 2026). https://arxiv.org/pdf/2605.12366 [new 2026]
- Shift in practice: "prompt engineering" (2022-23) -> "context engineering" (2025-26): deciding what goes in the window, not just how to word the ask.

## 3. Memory and RAG: the many ways a model "remembers"
- Model itself has no memory between calls (unchanged since GPT-3). Everything below is the app putting text back into the window.
- RAG (retrieve then generate) paper 2020; became the default enterprise pattern 2023-24 with vector databases. https://arxiv.org/abs/2005.11401 (2020) [established]
- ChatGPT: saved memories Feb 2024 (all tiers Sep 2024); "reference chat history" 10 Apr 2025; free-tier light version Jun 2025; memory-summary rebuild called "Dreaming" Jun 2026 (summary of you loaded into every message). https://openai.com/index/memory-and-new-controls-for-chatgpt/ (2024-25) · https://help.openai.com/en/articles/8590148-memory-faq · https://x.com/mem0ai/article/2071990201531118063 (2026, secondary) [established; "Dreaming" new 2026]
- Claude: chat search as a TOOL CALL it makes on request (paid plans); auto memory (running summary of role/preferences) Team/Enterprise Aug 2025, Pro/Max late Oct 2025, Free 2 Mar 2026. https://www.digitaltrends.com/computing/claude-makes-its-ai-memory-feature-free-for-all-users-in-battle-against-chatgpt/ (Mar 2026) · https://its.syr.edu/claude-has-a-memory-heres-how-to-use-it/ [new 2026 for free tier]
- Gemini: "Past chats" personal context, rolled to free users Feb-Mar 2026; not in EEA/UK/CH; not inside Gems or Live. https://9to5google.com/2026/02/26/gemini-past-chats-free/ (Feb 2026) [new 2026]
- Claude Code "auto memory": notes Claude writes itself, per repo, loaded each session (first 200 lines / 25KB). https://code.claude.com/docs/en/memory (current) [established/new]
- API side: Anthropic agent memory public beta 23 Apr 2026 (managed agents). https://platform.claude.com/docs/en/release-notes/overview [beta]
- External memory via tools: files on disk, Notion, Drive, etc., reached through connectors/MCP (MCP launched 25 Nov 2024; donated to Linux Foundation's Agentic AI Foundation 9 Dec 2025). https://www.anthropic.com/news/model-context-protocol (Nov 2024) · https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/ (Dec 2025) [established]
- Hermes Agent (Feb 2026) markets "self-improving" memory: writes its own skill files and searches past conversations. https://www.eweek.com/news/hermes-agent-self-improving-ai-tools/ (2026) [new 2026]
- Taxonomy to teach (all = "get text back into the window"): (1) in-window history; (2) summary memory the app maintains; (3) search over old chats (tool call); (4) external store via tools (files, Notion) = RAG broadly; (5) vector-search RAG (owned by 06.06).

## 4. System prompts, custom instructions, injected instruction files
- System prompt existed in the API from early chat APIs (2023); consumer "Custom instructions" in ChatGPT Jul 2023; Claude Projects/profile preferences 2024; Gemini Gems (saved instructions + knowledge). https://openai.com/index/custom-instructions-for-chatgpt/ (Jul 2023) · https://www.cmswire.com/digital-marketing/gemini-gems-vs-chatgpt-customgpts-a-marketers-guide-to-ai-mini-agents/ [established]
- AGENTS.md: released by OpenAI Aug 2025, donated to the Agentic AI Foundation (Linux Foundation) Dec 2025; 60,000+ repos. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation (Dec 2025) · https://openai.com/index/agentic-ai-foundation/ [established]
- CLAUDE.md (Aaron wrote "claude.com"; he means CLAUDE.md): read at the start of every Claude Code session. Layers: managed policy (org, cannot be excluded) -> user (~/.claude/CLAUDE.md) -> project root (./CLAUDE.md or ./.claude/CLAUDE.md) -> CLAUDE.local.md; files in folders ABOVE the working dir load at launch; files in subfolders load on demand when Claude reads files there; .claude/rules/ for scoped rules. https://code.claude.com/docs/en/memory (current) [established]
- Claude Code now reads AGENTS.md directly when no CLAUDE.md exists (v2.1.277+); if both exist, CLAUDE.md wins unless it imports AGENTS.md. same doc [new 2026]
- Docs say: these files are context, "not enforced configuration"; to block an action use a hook. same doc [established]
- Key mental model: always-in-window text costs tokens every turn and competes for attention (ties to context rot and caching: it is the stable prefix that gets cached).

## 5. Diffusion models
- How it works (one picture): train by adding noise to real data; generate by starting from pure noise and denoising step by step, guided by the prompt. DDPM 2020. https://arxiv.org/abs/2006.11239 [established]
- Turning points: DALL-E 2 (Apr 2022), Stable Diffusion open weights (22 Aug 2022), Sora preview (Feb 2024, diffusion transformer). https://stability.ai/news/stable-diffusion-public-release · https://openai.com/index/sora/ [established]
- Now: diffusion transformers + flow matching (a straighter noise-to-data path, fewer steps) dominate image, video and audio (e.g. Flux, SD3, Stable Audio 3, joint audio-video DiTs). https://arxiv.org/pdf/2605.17991 (Stable Audio 3, May 2026) · https://arxiv.org/html/2603.16093v1 (Mar 2026) [established]
- Not every image model is diffusion: GPT-4o/GPT Image is autoregressive. https://cdn.openai.com/11998be9-5319-4302-bfbf-1167e093f1fb/Native_Image_Generation_System_Card.pdf (Mar 2025) [established]
- Diffusion for TEXT (uncommon): Inception Mercury (2025 paper), Mercury 2 = first reasoning diffusion LLM, 24 Feb 2026, ~1,000 tok/s, 128K context, OpenAI-compatible API. Google Gemini Diffusion shown May 2025, still "experimental", no news since. Inception is the only company shipping a production dLLM (per reporting). https://the-decoder.com/inception-launches-mercury-2-the-first-diffusion-based-language-reasoning-model/ (Feb 2026) · https://thenewstack.io/inception-labs-mercury-2-diffusion/ · https://arxiv.org/abs/2506.17298 (Jun 2025) [new 2026 / Gemini Diffusion: beta]
- Hybrids appearing in research (e.g. NVIDIA Nemotron-Labs-Diffusion, Jul 2026: autoregressive + diffusion modes). https://arxiv.org/pdf/2607.05722 [speculation re: mainstream adoption]
- Local tie-in: Aaron's own ComfyUI stack is diffusion/flow (owned by 01.10 running models locally).

## 6. Model settings (brief)
- Classic knobs (2020-2025): temperature, top-p, top-k, max tokens, stop sequences. [established]
- BIG CHANGE 2026: on current Claude models (Opus 4.8 May 28, Sonnet 5 Jun 30, Opus 5 Jul 24 2026, and later) setting non-default temperature/top_p/top_k returns a 400 error. The knob is effectively gone from frontier Claude APIs. https://platform.claude.com/docs/en/release-notes/overview (Sep 30 2026) [new 2026]
- Reasoning models: OpenAI o1 Sep 2024 started "thinking before answering"; Claude extended thinking Feb 2025 with budget_tokens. https://openai.com/index/learning-to-reason-with-llms/ (Sep 2024) [established]
- New knob = effort: `effort` replaced `budget_tokens` (5 Feb 2026); `xhigh` level added 16 Apr 2026 (between high and max); no beta header since 28 May 2026. Adaptive thinking (model decides how much to think) default on Sonnet 5/5.5; "always-on" on Opus 5.5 (disabling thinking errors). same release notes [new 2026]
- Max output tokens still a real setting (up to 128k on current Claude). [established]
- Consumer apps expose this as model picker + effort/"thinking" toggle, not temperature.

## 7. Prompt caching and token billing
- Pricing has four meters, not two: normal input, output, cache write, cache read. Usage fields: `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`; total input = sum of three. https://platform.claude.com/docs/en/build-with-claude/prompt-caching (current) [established]
- How it works: provider stores the computed state of a prompt PREFIX; next request with an identical prefix skips recomputing it. Order is tools -> system -> messages; a change at any level invalidates that level and everything after (also: toggling web search, thinking config, adding/removing images, tool_choice). same doc [established]
- TTL: default 5 min, refreshed free on every hit; optional 1 h. Expired = rebuilt from scratch (cache write again). same doc [established]
- Price multipliers (Anthropic): 5-min write 1.25x input; 1-h write 2x; read 0.1x (doc notes newer models such as Opus 5.5 at 0.05x; Fable/Mythos 5.1 reads $0.25/MTok). Minimum cacheable prefix 512 tokens (newest models) or 1,024. Below minimum: silently not cached. same doc + release notes [established; newer read rates new 2026, re-verify per model before quoting]
- Automatic caching (one top-level `cache_control`, breakpoint moves forward as the chat grows) 19 Feb 2026. release notes [new 2026]
- OpenAI: automatic, no markers, prompts >1,024 tokens; GPT-6 update 22 Sep 2026: up to 90% off cached input, 30-minute reuse window. https://openai.com/index/better-prompt-caching-for-gpt-6/ (Sep 2026) · https://mixed-news.com/en/openai-gpt-6-prompt-caching-30-minute-window-90-percent/ [new 2026]
- History: Anthropic prompt caching beta Aug 2024; OpenAI automatic caching Oct 2024. Before that every turn re-paid for the whole conversation. [established]
- Output tokens are the expensive meter (Opus 5.5 $4 in / $20 out per MTok; Opus 5 $5/$25; Sonnet 5 $2/$10). release notes [new 2026]
- Subscription vs API billing owned by 10.11.

## 8. Modes and platforms (Claude as worked example)
- Claude Code: research preview Feb 2025 (CLI), GA May 2025 with Claude 4; Claude Code on the web (cloud sessions + sandbox) 20 Oct 2025; desktop app with Local / Cloud / SSH / WSL targets; cloud sessions via claude.ai/code, mobile, desktop "Cloud", `claude --cloud`, persist across devices. https://en.wikipedia.org/wiki/Claude_(language_model) · https://code.claude.com/docs/en/claude-code-on-the-web · https://code.claude.com/docs/en/desktop [established]
- Cowork: research preview 12 Jan 2026 ("Claude Code for the rest of your work"): desktop agent with sandboxed shell and user-chosen folders; Max first, Pro by 16 Jan 2026; later runs in the cloud and does scheduled tasks. https://simonwillison.net/2026/jan/12/claude-cowork/ (Jan 2026) · https://aragonresearch.com/anthropic-claude-cowork/ [new 2026]
- CHAT + COWORK MERGE IS ANNOUNCED, not speculation: 16 Sep 2026 Anthropic merged chat and Cowork (plus Artifacts and Claude Design) into one interface; Claude routes each request itself (answer vs longer task). Rolling out to Pro and Max on web, desktop, mobile "over the coming weeks"; Team and Free "soon", no date. Cowork name to disappear. Claude Code stays separate. Default asks permission before acting. New betas: Claude Docs and Claude Slides. https://techcrunch.com/2026/09/16/anthropic-merges-claude-chat-and-cowork-in-one-interface/ (Sep 16 2026) · https://venturebeat.com/technology/anthropic-is-killing-off-cowork-and-folding-it-into-claude-launching-claude-docs-and-claude-slides (Sep 2026) · https://9to5mac.com/2026/09/16/anthropic-merging-claude-cowork-with-chat/ [beta/announced: rolling out now; a given viewer may still see three tabs]
- So the "three modes" picture (chat / Cowork / Code) is already becoming two (Claude / Claude Code) as of this month. Aaron's "likely getting combined soon" should be phrased as "announced 16 Sep, rolling out now".
- Platforms (surfaces): web (claude.ai), desktop app (Mac/Windows), mobile, CLI (terminal), cloud sessions (runs on Anthropic's servers, continues with laptop closed), IDE extensions, Chrome extension. Equivalents: OpenAI ChatGPT (web/desktop/mobile) + Codex (CLI, cloud; "Codex Cloud" at DevDay 2026); Google Gemini app + Gemini CLI + Antigravity. https://benchlm.ai/blog/posts/openai-devday-2026 (Sep 2026, secondary) [established]
- Durable idea: mode = what kind of job (talk / do office work / write code); platform = where it runs and what it can touch (your files vs a cloud sandbox).

## 9. Skills vs connectors vs plugins, and marketplaces
- Connectors = MCP servers (Nov 2024) that let Claude reach an outside service (Notion, Gmail, GitHub). [established]
- Skills = folder with SKILL.md (instructions + scripts) loaded on demand; launched 16 Oct 2025; made an open standard 18 Dec 2025 (agentskills.io); adopted by OpenAI Codex/ChatGPT, Gemini CLI, Copilot/VS Code, Cursor; 40+ tools by mid-2026. https://platform.claude.com/docs/en/release-notes/overview · https://www.firecrawl.dev/blog/agent-skills (2026, secondary) [established]
- Plugins = bundles of skills, commands, connectors (MCP), hooks, installable across chat, Cowork and Claude Code. https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory · https://claude.com/blog/build-plugins-for-claude [established]
- One directory: "Customize" sidebar with Skills / Connectors / Plugins tabs + Discover; Team/Enterprise get an "Your organization" tab and admin publishing policy. same support article [new 2026]
- Claude Marketplace (launched 23 Sep 2026, reported 27 Sep): 2,000+ connectors and plugins, plus paid Claude-powered agents (CrowdStrike, Harvey, Snowflake) and consulting partners. https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors/ · https://www.ghacks.net/2026/09/27/anthropic-launches-claude-marketplace-with-more-than-2000-connectors-and-plugins/ (Sep 2026) [new 2026]
- Claude Code plugin marketplaces: any git repo can be a marketplace; plus community directories (claudemarketplaces.com etc.). https://claudemarketplaces.com/ [established]
- OpenAI lineage (shows the churn): ChatGPT Plugins Mar 2023 -> shut Apr 2024; GPT Store Jan 2024; App Directory + Apps SDK (MCP-based) Dec 2025; renamed Plugin Directory 9 Jul 2026 (bundles apps + skills); custom GPTs to be retired into plugins (announced Sep 2026). https://www.taskade.com/blog/chatgpt-plugins (2026, secondary) · https://en.wikipedia.org/wiki/GPT_Store [new 2026; GPT retirement announced]
- Google: Gems + extensions/apps. [established]
- Security: OpenClaw third-party skills found exfiltrating data / doing prompt injection (Cisco, 2026) -> plugins and skills are code you trust. https://en.wikipedia.org/wiki/OpenClaw [new 2026]
- Deeper version owned by 10.10.

## 10. Individual vs enterprise
- Consumer plans (Free, Pro, Max): since 28 Aug 2025 terms update, chats/coding sessions may train models unless the user opts out; retention 5 years if opted in, 30 days if not; deadline was 8 Oct 2025. https://www.anthropic.com/news/updates-to-our-consumer-terms (Aug 2025) [established]
- Commercial terms (Team, Enterprise, Education, Government, API) are excluded from that change: no training on your data by default. same [established]
- Enterprise adds: SAML SSO, domain capture, SCIM/JIT provisioning, role-based access, audit logs + Compliance API, custom retention, admin control of which connectors/plugins/skills are allowed, org-managed CLAUDE.md for Code, org-provisioned skills. https://claude.com/solutions/enterprise · https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory · https://code.claude.com/docs/en/memory [established]
- Features often ship to individual Pro/Max first and Team/Enterprise later (Cowork merge) or the reverse (memory went Team/Enterprise first in Aug 2025). [established pattern]
- Gemini memory: personal accounts only. OpenAI Dots: Enterprise/Edu as admin-enabled beta. (see 3, 13) [new 2026]

## 11. Other surfaces: Claude Design and friends
- Claude Design (Anthropic Labs), launched 17 Apr 2026, research preview for Pro/Max/Team/Enterprise, powered by Opus 4.7: prompts -> prototypes, wireframes, decks, one-pagers; export PDF/URL/PPTX/Canva. https://www.anthropic.com/news/claude-design-anthropic-labs (Apr 2026) · https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/ [new 2026]
- 16 Sep 2026: Claude Design now works inside chat conversations rather than as a separate surface (part of the merge). https://venturebeat.com/technology/anthropic-is-killing-off-cowork-and-folding-it-into-claude-launching-claude-docs-and-claude-slides [beta/announced, rolling out]
- Claude Docs and Claude Slides: new betas 16 Sep 2026. same [beta]
- Note: Claude Design makes visuals as code/layout, not with a diffusion image model.

## 12. Voice modes
- 2021: no conversational voice in these products. ChatGPT voice (Sep 2023, speech-to-text -> LLM -> text-to-speech pipeline); Advanced Voice on GPT-4o (speech-native) 2024. https://openai.com/index/chatgpt-can-now-see-hear-and-speak/ [established]
- Claude voice mode (mobile) May 2025, on Haiku; 23 Jul 2026 upgrade: Opus and Sonnet in voice, connectors (email/calendar) mid-conversation, 11 languages. Still turn-based (listen, think, reply) on a TTS stack, not full-duplex. https://www.digitalapplied.com/blog/claude-voice-mode-opus-sonnet-connectors-2026 · https://thetechmarketer.com/claude-voice-mode-opus-sonnet-upgrade-2026/ (Jul 2026, secondary) [new 2026]
- Claude Code voice mode (/voice) Mar 2026. https://techcrunch.com/2026/03/03/claude-code-rolls-out-a-voice-mode-capability/ (Mar 3 2026) [new 2026]
- OpenAI GPT-Live (Jul 2026): full-duplex (listens while speaking, handles interruptions, backchannels), hands hard thinking to GPT-5.5 in the background; GPT-Live-1 API $0.05/min. https://openai.com/index/introducing-gpt-live/ · https://www.marktechpost.com/2026/07/08/openai-releases-gpt-live-and-gpt-live-1-mini-full-duplex-voice-models-that-delegate-deeper-reasoning-to-gpt-5-5/ (Jul 8 2026) [new 2026]
- Google: Gemini Live; Gemini 3.5 Audio (live translate). https://deepmind.google/models/model-cards/gemini-3-5-audio/ [established/new]
- Two architectures to name: pipeline (STT -> LLM -> TTS) vs speech-native / full-duplex.

## 13. Always-on personal agents (Aaron: "openclaw, hermies, muse, dots")
- Name resolution: "openclaw" = OpenClaw; "hermies" = Hermes Agent (Nous Research); "muse" = Meta Muse (Meta's agent, 8 Sep 2026; do not confuse with "Muse Spark", which reporting uses for a Meta model/agent earlier in 2026); "dots" = OpenAI Dots (29 Sep 2026). Category also includes Google Gemini Spark, xAI "Grok Bot", Manus.
- OpenClaw: open source (MIT), self-hosted, runs as a background daemon on your own machine/server, you talk to it via WhatsApp/Telegram/Slack/iMessage etc. History: released Nov 2025 as Clawdbot (named after Claude) -> Moltbot 27 Jan 2026 after Anthropic trademark complaint -> OpenClaw 30 Jan 2026; creator Peter Steinberger joined OpenAI 14 Feb 2026, project moved to OpenClaw Foundation (nonprofit); 247k GitHub stars by 2 Mar 2026; v2.0 30 Aug 2026. Security incidents: malicious third-party skills (exfiltration, prompt injection), agent created a dating profile unasked (Feb 2026); China restricted use in state bodies (Mar 2026). https://en.wikipedia.org/wiki/OpenClaw · https://alternativeto.net/news/2026/1/trending-open-source-ai-agent-clawdbot-rebrands-to-moltbot-after-pressure-from-anthropic/ [new 2026] (note: the Wikipedia summary fetched also mentioned an earlier name "Warelay"; most sources say Clawdbot; say "Clawdbot" or avoid the old names)
- Hermes Agent (Nous Research, Feb 2026): open source, Python, "self-improving" loop that writes reusable skill docs and searches past chats; 40+ bundled skills; passed OpenClaw on OpenRouter's daily app rankings ~10 May 2026 (224B vs 186B tokens/day). https://www.marktechpost.com/2026/05/10/openclaw-vs-hermes-agent-why-nous-researchs-self-improving-agent-now-leads-openrouters-global-rankings/ (May 2026) [new 2026]
- Meta Muse (8 Sep 2026): personal agent with its own cloud machine per user; reads email, browses, books, pays; keeps working after the app closes; asks before sending/buying; US, iOS/Android/web; free tier + $20/$100. https://www.axios.com/2026/09/08/meta-debuts-muse-personal-ai-agent (Sep 8 2026) · https://en.wikipedia.org/wiki/Muse_(AI_agent) [new 2026]
- OpenAI Dots (DevDay, 29 Sep 2026): "always-on agents", each with its own cloud computer + browser, GPT-6 Astra, give it a responsibility (e.g. watch bug reports) and it works 24/7; talk via ChatGPT, Slack, Teams, mobile, voice; 4,000+ app connections; approval rules; Pro and Business Premium (one Dot included), Enterprise/Edu beta via admin; Pro rollout excludes EEA/CH/UK. https://9to5google.com/2026/09/29/openai-dots-agent/ (Sep 29 2026) · https://www.business-standard.com/technology/tech-news/openai-devday-2026-dots-gpt-6-1-sol-codex-developer-tools-126093000396_1.html [new 2026, rolling out]
- Google Gemini Spark (I/O May 2026): 24/7 agent on Gemini 3.5 Flash + Antigravity harness on cloud VMs; Gmail/Calendar/Docs; confirms before consequential actions; Ultra subscribers only. https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/ · https://www.datacamp.com/blog/gemini-spark [new 2026]
- Anthropic's nearest equivalents: cloud Cowork sessions, scheduled tasks, Claude Code routines (run on Anthropic's cloud with laptop closed); Claude Managed Agents for developers. No branded "Dots-style" consumer agent announced as of 2 Oct 2026; reporting expects one from Google or Anthropic soon. https://aimultiple.com/always-on-agents · https://munderdiffl.in/blog/chatgpt-dots-alternatives/ (secondary) [speculation for a new Anthropic product]
- Category split to teach: self-hosted/open (OpenClaw, Hermes: your hardware, your model choice, your risk) vs hosted (Dots, Muse, Spark: vendor's cloud computer, vendor's approval rules). Common traits: own computer, runs without you, reachable by chat apps, memory, connectors, approval gates. Deeper: 16.11 scheduled agents.

## 14. What did NOT change (durable mental model)
- A language model still predicts the next token from the tokens in its window; it has no memory between calls. Every "memory" feature is text put back into the window.
- The context window is still the whole world for one call: if it is not in the window (or fetched by a tool into it), the model does not know it.
- Everything is paid and limited in tokens (input and output), now with cache meters on top.
- Models still hallucinate: a fluent, confident guess can be wrong; grounding (RAG, tools, citations) reduces but does not remove it.
- Instructions are text, not enforcement (CLAUDE.md docs say so explicitly); real limits come from permissions, sandboxes, hooks.
- Sampling is still probabilistic, even where the temperature knob is hidden.
- Model vs app vs agent (00.04) is still the right split; the products just stack more app and agent around the same kind of model.

## Traps: things commonly said that are now wrong or misleading (Oct 2026)
1. "LLMs only do text." Most frontier models take images/PDFs/audio, some video; some output images/audio/video natively (GPT-4o/GPT Image, Gemini Omni).
2. "Claude can make images." It cannot natively; it writes code visuals or calls an image model via a connector.
3. "All AI images come from diffusion." GPT Image is autoregressive; diffusion/flow dominates but is not universal.
4. "Diffusion is only for pictures." It also does video and audio, and (rarely) text: Mercury 2 is a shipping diffusion LLM.
5. "Bigger context window = it remembers everything." 1M tokens is standard, but quality degrades well before the limit (context rot).
6. "Set temperature to 0 for accuracy." On current Claude models non-default temperature/top_p/top_k is rejected; the live knob is effort/thinking.
7. "The model remembers you." The app re-injects summaries, searches chats, or reads files via tools; the weights do not change.
8. "Each message only costs the new words." Each turn re-sends the whole conversation; caching makes repeats cheap (0.1x or less) only if the prefix is unchanged and the cache has not expired (5 min default on Claude).
9. "Cache = free." Writes cost MORE than normal input (1.25x or 2x); it pays off only on reuse.
10. "Editing the system prompt / CLAUDE.md mid-session is harmless." Any change early in the prefix invalidates the cache from that point on.
11. "CLAUDE.md is a config file Claude must obey." It is context, not enforcement; and AGENTS.md is now read too.
12. "Claude has three modes: chat, Cowork, Code." As of 16 Sep 2026 chat and Cowork are merging (rolling out); Code stays separate.
13. "Plugins are ChatGPT's 2023 feature that died." The word is back at both companies: Claude plugins bundle skills + connectors; ChatGPT's Plugin Directory (Jul 2026) replaced the App Directory.
14. "Skills only work in Claude." Agent Skills is an open standard used by Codex, Gemini CLI, Copilot, Cursor and others.
15. "Paying for Pro means my data is not trained on." Consumer plans (incl. Pro/Max) train unless you opt out (since Oct 2025); commercial plans do not.
16. "Voice mode is the model listening." Claude voice is still a pipeline (turn-based); only some systems (GPT-Live, GPT-4o voice) are speech-native/full-duplex.
17. "Personal agents are a hobby thing." Since Sep 2026 Meta (Muse), OpenAI (Dots) and Google (Spark) ship hosted always-on agents; OpenClaw/Hermes are the self-hosted side.
18. "Sora is the video model." The Sora app closed Apr 2026 and its API in Sep 2026; video moved to models like Gemini Omni and Seedance.
19. "Prompt engineering is the skill." The 2025-26 framing is context engineering: what goes in the window.
