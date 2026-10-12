---
key: making-media-with-ai
id: 09.02
title: Making media with AI
district: Beyond Code
module: 09 Facts, media, rights
status: todo
legacy: []
minutes: 10
concepts: [C030, C031, C032, C134]
sources: [S110, S111, S244, S242, S004, S010, S011, S032, S033, S068, S108, S109, S112, S113, S243]
lead: [S110, S111]
---
# Making media with AI

**Purpose (the first spoken sentence):** In this lesson you'll learn where AI images, video, music and voices actually come from, what each render costs, and which part of judging them the agent can't do for you.

**Conclusion:** The chat model you talk to reads media but doesn't make it: separate media models do, in the cloud or on your own machine, every run comes out different while everyone's defaults come out alike, the meter runs per second, per resolution and per retry, and the agent can only measure what it makes, so test cheap first and judge with your own eyes and ears.

**Where it sits on the map:** District 6 · Beyond Code — What if it isn't software?; module 09 Facts, media, rights (lesson 2 of 4).

**Lead source (audit, 2026-10-12):** S110 (Aaron Orelup); S111 (Aaron Orelup). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S110, S111, S244, S242); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Through-line for the script:** a studio next door (the legacy 00.05 image: "the clerk phones the studio next door"). The agent writes the brief, phones the studio, pays per second of film, and gets back a reel it cannot watch. Keep the metaphor; where it breaks is that the agent can be handed instruments (a transcriber, a loudness meter, frame grabs) that measure the reel, and measuring is still not watching (S110).

## What to teach (binding scope)

### C032 Models that see, hear and make media
- **Understanding is not generating.** Anthropic's vision docs: "Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images." It is a question common enough to sit in that page's FAQ (S113). Images come from separate image models, such as Google's Nano Banana line, whose current workhorse is Nano Banana 2.1 (S108, S242). Depth: teach; this is the opening fact.
- **What reading media costs and what vision can't do.** Claude counts an image as 28×28-pixel patches, and Claude 4.7 and later read up to 2,576 px and 4,784 tokens per image, up to about three times the standard tier; it won't name people, can't tell whether an image is AI-generated, and does not read image metadata (S113). Depth: brief. Images being resent on every turn belongs to 05.01; one sentence at most.
- **Image models now reason and take references.** Gemini's image models think before drawing, accept up to 14 reference images including up to 4-5 for character consistency, and edit across turns (S108). Every image they make carries a SynthID watermark (S108). Depth: brief; watermarks and labels belong to 09.03.
- **The agent can't judge media it can't perceive.** Claude rendered 223 clips of a game's robot voice and said "I can't listen to audio"; it checked each one with a transcriber, a loudness meter and a spectrogram, normalised every clip to -18 LUFS so "none wins by being louder", and Aaron listened and made every choice. Measurements ruled out failures but "couldn't tell me a thing about which of the rest was good"; "That split is what made it work" (S110). Agents also built 16 wallpapers none of them ever saw run (S032). Depth: teach; this is the heart of the lesson.
- **"One prompt" media hides a pipeline.** People wire the model to Blender, Higgsfield, asset libraries, Suno and ElevenLabs; video models need reference sheets, video references and previs; mistakes compound, so check at each stage (S109, Aaron's own prompt, 2026-10-03). Aaron's controlled tests of the same five-second shot found that a start frame built from his character's canon plate and character sheet passed every check, while text alone never kept the design, and that a viral "one prompt" was 9,608 characters plus a video, a song, a repo and API keys (proposed source P2, below). Depth: teach.
- **How a diffusion model makes an image.** It starts from noise the size of the output and removes it in steps: at each step the model predicts the noise and a scheduler produces a less noisy image. Latent diffusion works on a compressed image that a decoder (the VAE) turns back into pixels; the prompt steers through a text encoder; `guidance_scale` sets how much weight the prompt gets (S244). Depth: teach, about two minutes, one drawing.
- **The seed is the starting noise, and even it doesn't guarantee a repeat.** "Diffusion is a random process that generates a different output every time." A GPU generator "can diverge from CPU results"; a generator's state is used up by each call, so reseed before each one; and reproducibility is "not *guaranteed* even with an identical seed" (S244). The page's own example model is Qwen-Image. Depth: teach (it answers "why can't I get that image back?").

### C030 Outputs vary and converge
- **Every run is different; specific prompts vary less.** The same detailed prompt run three times gives three different but similar results; a vague one gives three very different ones (S010). Depth: brief.
- **Samey output comes from product choices, not "the average of the internet".** Models learn a long-tailed distribution; bland output "usually reflects product choices" such as low-temperature decoding, alignment pressure and uniform assistant prompts (S011). Depth: brief.
- **Individually better, collectively alike.** As reported by Lin: AI-assisted stories were rated more creative one by one but more similar to each other (Doshi and Hauser 2024), and across 31,076 creators the volume of ideas grew while creativity per piece fell (Zhou, Lee and Gu 2025) (S011). In a study Mollick cites, GPT-4's product ideas were more commercially viable than MBA students' but "very similar to each other"; bringing in people widens the range (S068). Depth: brief.
- **Models have a house taste.** Without a stated style, Opus 5.5 falls back on its own recognisable styles and keeps choosing the same few stock voices, so Aaron names voices explicitly (S109). In his tests, 12 of 12 title cards with no style given were the same purple sunset, one sentence of art direction removed the purple, and 38 of 38 sessions asked to pick a narrator picked a stock voice (proposed source P2). Depth: teach.
- **Pin what must not vary, and record the settings.** In the robot-voice lab, glitches were seeded by each line's id "so the same line always sounds the same", and every clip was loudness-matched before Aaron compared them (S110); record the settings whenever you compare outputs (S011). Depth: teach.
- **The choice is yours.** Nine Claude sessions (Haiku, Sonnet and Opus at low, medium and max effort) were given one picture and "paint this image". Haiku's three looked unlike the picture; the sessions that measured colours against the picture stroke by stroke copied its flaws ("A painting that is steered toward the picture stroke by stroke copies its errors too"), and Aaron's favourite was Opus medium's first try, painted by eye: "It transformed the picture instead of copying it" (S111). Lin cites an artist who generated over 100,000 images to keep about 20 (S011). Depth: teach.

### C134 Media is metered per second, per resolution and in credits
- **Video is priced per second, by resolution.** On Google's price list (updated 2026-10-09), Veo 3.1 Standard costs $0.40 a second at 720p and 1080p and $0.60 at 4K; Veo 3.1 Fast $0.10 / $0.12 / $0.30; Veo 3.1 Lite $0.05 / $0.08, with no 4K; Veo is not on the free tier (S242). Depth: teach.
- **Images are priced by size.** Nano Banana 2.1 costs about $0.0336 an image at 1K, $0.0504 at 2K and $0.113 at 4K, and batch jobs cost half (S242). Depth: brief.
- **The model you pick can matter more than the prompt.** One 12-second fight shot with three reference images cost 144 credits on Seedance 2.5 (1080p), 24 on MiniMax H3 and 25 on Kling 3.0. Seedance held the multi-reference scene most reliably, but Aaron judged the two cheaper results better for this shot (S243). Depth: teach.
- **Credits are an allowance with limits.** Aaron's Higgsfield Plus plan gives 1,200 credits a month and a 72-second film cost about 180 of them; only 6 MiniMax H3 jobs run at once, and a seventh is refused and not charged (S243). Depth: brief.
- **Know what a failure costs.** Google: "You will only be charged if your video is successfully generated" (S242). On Higgsfield, failed and refused jobs were refunded but cost time, and a safety filter refused harmless jobs 5 times in 10 (S243). Depth: brief.
- **Iterate where it's cheap, and price the job before you send it.** "It is cheaper to re-roll a still than a video": check the start and end frames, then render (S243). Test at low resolution and short duration first; Aaron's credit figures were measured with the provider's own cost command before submitting (S243). Depth: teach; this is the lesson's habit.

### C031 Local and open-weight models
- **A local model is a file, a runtime and settings, and the defaults decide the experience.** Willison's example is a language model whose default reasoning setting turned one answer into 21 minutes (S112); the same is true of media models. Depth: brief.
- **On your own machine the meter is minutes instead of money.** On Aaron's 8 GB RTX 4070 laptop, Qwen-Image 2.1 makes a 1024×1024 image in 28.5 s warm and a native 2048×2048 one in 211.5 s; MiniMax-H3 makes a 5-second clip at 608×352 in 52-64 s and at its native 1344×768 in 293 s (proposed source P1). So "test cheap first" holds locally too. Depth: brief.
- **Laptop-sized open models are close to the frontier for some tasks, and local is not automatically uncensored.** Willison drew this as a key trend of 2026 (S033); post-training lives in the same weights, so a model's refusals travel with it (S011). Depth: one line.
- **Local is not licence-free.** The licence travels with the weights; some media models are non-commercial or exclude whole countries (taught in 09.04, C132). Depth: one line.
- Dropped from C031: reasoning-effort and context-length tuning for local language models (S112 details) → deep-dive backlog "Local and open-weight models in depth".

## You vs the agent
As of 2026-10-12:
- **The agent does on its own:** calls media models through their APIs, command-line tools and connectors; prices each job before submitting and picks the cheapest settings that meet the brief; logs spend per asset; generates many variants cheaply; keeps seeds and loudness fixed; and gives itself instruments: transcripts, loudness readings, spectrograms, frame grabs and contact sheets, plus a comparison page that makes your review fast (S110, S243).
- **You check and decide:** the budget; the style, references and constraints (one sentence of direction moves its defaults); each stage before mistakes compound (style sheet, start frame, first take); and the pick, by eye and ear, because a measurement is not taste (S110, S111, S109). Check the agent's instruments once against reality before trusting them (C003). Decide whether the pricier model is worth it for a given shot (S243).
- **You bring in an expert:** for work whose quality is taste (camera, 3D, music, lyrics), Aaron's rule is an expert in that craft as the prompter, even though the model does the work (S109); for a commercial production, a producer who has budgeted generated media before (C134). Consent for faces and voices and labelling belong to 09.03 and 09.04.

## Sources this lesson is built from
- S110 — Aaron Orelup, "AO-030: Claude rendered 223 clips of my game's robot voice, and couldn't hear any of them" (2026-10-02) https://aaronorelup.com/ledger/remora-voice-lab/ — the agent that measures but can't hear, pinned seeds and loudness, the human's ears as the decision; re-read 2026-10-12.
- S111 — Aaron Orelup, "AO-044: Nine Claudes painted the same picture in oil, and the first tries were the art" (2026-10-11) https://aaronorelup.com/ledger/nine-claudes-one-painting/ — one prompt, nine very different results, measuring copies the flaws, the first try painted by eye; re-read 2026-10-12.
- S244 — Hugging Face, Diffusers docs "Understanding pipelines, models and schedulers" and "Reproducibility" (undated live docs, foundational and current; the reproducibility page uses Qwen-Image as its example) https://huggingface.co/docs/diffusers/main/en/using-diffusers/write_own_pipeline ; https://huggingface.co/docs/diffusers/main/en/using-diffusers/reusing_seeds — how diffusion makes an image and why a seed doesn't guarantee a repeat; reproducibility page re-read 2026-10-12.
- S242 — Google AI for Developers, "Gemini Developer API pricing" (last updated 2026-10-09) https://ai.google.dev/gemini-api/docs/pricing — Veo per-second prices by resolution, Nano Banana 2.1 per-image prices, batch at half, no charge for a failed video; re-read 2026-10-12.

Also cited for single points (credit on the lesson page):
- S113 — Anthropic, "Vision" (Claude Platform Docs, undated live docs naming Claude 4.7+) https://platform.claude.com/docs/en/build-with-claude/vision — understanding only, image token counts, vision limits; re-read 2026-10-12.
- S108 — Google, "Image generation, 'Nano Banana'" (Gemini API docs, last updated 2026-10-09 per sources.md) https://ai.google.dev/gemini-api/docs/image-generation — current image models, reasoning, references, SynthID.
- S243 — Aaron Orelup, Higgsfield notes (`references/higgsfield.md`, measured 2026-09-21 to 2026-09-27; local file, not public) — measured credit costs, plan, concurrency, refunds, the re-roll-a-still rule; re-read 2026-10-12.
- S109 — Aaron Orelup, Playback prompt on what "Opus 5.5 made this" videos leave out (2026-10-03; not public) — the hidden pipeline, house taste, the craft expert as prompter.
- S032 — Aaron Orelup, "AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run" (2026-09-29) https://aaronorelup.com/ledger/wallpapers-nobody-saw/
- S010 — Andrew Ng, DeepLearning.AI, "Build with Andrew" (2026-07-17) https://www.deeplearning.ai/courses/build-with-andrew — three runs of one prompt.
- S011 — Zhicheng Lin, "Six misconceptions about large language models" (2026-07-08) https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/ — product choices, convergence studies, local censorship (studies it reports were not opened; credit them "as reported by Lin").
- S068 — Ethan Mollick, "Agency and Agents" (2026-08-31) https://www.oneusefulthing.org/p/agency-and-agents
- S112 — Simon Willison, "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things" (2026-08-16) https://simonwillison.net/2026/Aug/16/qwen-38-27b/
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/

Proposed new sources (read 2026-10-12 for this spec; not yet in sources.md, so add them before the lesson is made or drop the points that rest on them):
- P1 — Aaron Orelup, ComfyUI notes `references/settings.md` (`C:\Users\soulo\Organized\Personal\My Projects\Comfyui\references\settings.md`; measured 2026-09-21 to 2026-09-30 on his 8 GB RTX 4070 laptop; local file, not public) — local render times for Qwen-Image 2.1 and MiniMax-H3.
- P2 — Aaron Orelup (experiments run by Claude Opus 5.5 sessions), lesson plan "what 'Opus 5.5 made this' leaves out" (`C:\Users\soulo\Organized\Personal\My Projects\Courses\_planning\opus-made-this\lesson_plan.md`, 2026-10-04; local, not public) — controlled bare-vs-connected experiments: house-taste counts, references deciding likeness, the size of a viral "one prompt".

## Show it for real
- Ask Claude in the app to "make me a picture of a lighthouse at dusk": it explains it can't, or writes code that draws one; then the same brief sent to an image model: proves the studio next door.
- The agent prices the same 8-second shot at two resolutions on two models with the provider's cost command before submitting, then renders only the cheaper one (crop any account name or e-mail from the terminal): proves the meter runs per second, per resolution and per model.
- One prompt and seed rendered twice, once with a CPU generator and once on the GPU, side by side; then only the guidance scale changed (S244): proves the seed and the settings, and that a repeat isn't guaranteed.
- The same prompt run three times in fresh sessions, results in a row (S010): proves runs differ.
- The AO-044 grid of nine paintings (S111): proves one prompt, many results, and that the pick is a person's.
- The AO-030 listening page with the measurements beside the clips (S110): proves what the agent can measure and what it leaves to your ears.
- An agent's contact sheet of frames grabbed from a generated clip, with its loudness reading and transcript: proves how an agent "perceives", and that it is measurement.
- A local render on the laptop with the timing readout, at 1024 and at 2048 (P1): proves local costs time instead of credits.
- A month's credit log beside the asset log (S243): proves where the budget went.
- Before putting any generated output on screen, check its model's licence (09.04): some local media models are research-only or exclude whole countries for their outputs, so this lesson must not show them without Aaron's decision for that piece.

## Questions this lesson answers
Collected from the sources and Aaron's own prompt; no beginner forum threads were collected for media yet.
- Can Claude make images? (an FAQ on Anthropic's own vision page, S113)
- How do image models work differently from chat models? (batch-reader list, S004)
- Why can't I reproduce the "made with Opus 5.5" videos I see online? (Aaron, S109)
- Why did it make something different this time? How do I get consistent results? (S010)
- Why does all AI art and writing look the same? (S011, S068)
- Why does the same seed give a different image on another machine? (derived from S244)
- Why did one video use so many credits? Do I pay for a video that fails? How much does a minute of AI video cost? (derived from S242, S243)
- Can I run image and video models on my own computer? Is a local model uncensored? (S033, S011)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Giving the agent eyes, and checking the eyes once against reality → when-it-breaks-you-supply-the-eyes
- Running, looking finished and being good are different checks → done-is-a-claim
- Images resent on every turn and the cost of a full context → what-the-agent-sees-each-turn
- Which meter you're on, effort, and caps that stop spending → know-your-meter
- Finding what you want cheaply before building (mockups and throwaway tries) → plan-first-then-build-in-slices
- House taste comes from the harness and product choices, not the bare model → model-harness-and-memory
- Where a surface runs and where your files go → where-your-agent-works
- SynthID and Content Credentials, and labelling what you publish → labelling-ai-media
- Model licences, generator terms, and consent for voices and faces → own-it-sell-it-publish-it
- Local and open-weight models in depth → deep-dive backlog (curriculum-draft.md)

## Out-of-date framings to avoid
- "AI means text chat" and "a multimodal model can make images" (S113).
- "Attachments are free" (S113).
- "The same prompt, or the same seed, always gives the same result" (S010, S244).
- "It's just the average of the internet" and "AI can't be original" (S011).
- "The model made it alone in one prompt" (S109; P2).
- "My subscription covers it, so each render is free" and "a failed job costs nothing" (S243).
- "The best model is worth it for every shot" (S243).
- "Local models are toys" and "local means uncensored" (S033, S011).
- From the legacy lesson, unsourced in the current source list and not to be repeated without a new source: that OpenAI shut its Sora video app, that OpenAI's image models are autoregressive, that most current generators use flow matching, and the diffusion-text claims about Inception's Mercury.

## Legacy notes
Legacy 00.05 "How AI models work today" (`00-05-how-llms-work-just-enough`, published 2026-10-02, about 20 minutes) no longer stands in for this slot: the 2026-10-12 audit unlinked it, because its media segments carry facts with no entry in sources.md. For the record, the material was in its sections 06 "Seeing, hearing, and making" and 07 "Diffusion: from static to picture".
- **What it gets right:** "multimodal" hides three things (reads, makes, hands off to another model); Claude writes only text and calls another model for pictures; the studio-next-door image; diffusion as static wiped away step by step, nudged by the prompt. Its closing takeaway, "making pictures is mostly a hand-off", is this lesson's opening fact.
- **What is missing:** the meter for media (per second, per resolution, per retry, credits and refunds, C134); the agent that cannot see or hear what it makes and the split between measuring and judging (C032, S110); variance, convergence and house taste (C030); seeds, guidance, latents and the VAE (S244); local media models and their render times; and the test-cheap-first habit.
- **What is outdated or unsourced:** the claims listed above under framings; its "owner" notes point at retired lesson numbers (NEW 10.14, NEW 01.13), which this slot replaces.
- **Related unpublished draft:** `lessons/10-16-what-opus-made-this-leaves-out/` (paused 2026-10-04, not in course.json or the current curriculum) holds 75 exhibits and the controlled experiments behind P2. It is the natural feeder for this lesson's "one prompt hides a pipeline" and "house taste" segments; its own ORCHESTRATOR.md lists Aaron's decisions about what may be shown and must be read before reusing any exhibit.
