---
key: labelling-ai-media
id: 09.03
title: Labelling AI media
district: Beyond Code
module: 09 Facts, media, rights
status: todo
legacy: []
minutes: 10
concepts: [C110, C111, C112, C116]
sources: [S076, S195, S200, S079, S077, S078, S108, S196, S197, S198, S199, S205, S239, S250]
lead: [S076, S195]
---
# Labelling AI media

**Purpose (the first spoken sentence):** In this lesson you'll learn who has to label AI-made media, where and when the label has to appear, and which platform rules apply on top, as the rules stand in October 2026.

**Conclusion:** A generator's watermark is written for machines, not for your viewers; if you publish professionally in the EU you must also tell people, where and when they first see it, and every platform you post to adds its own AI rules on top.

**Where it sits on the map:** District 6 · Beyond Code — What if it isn't software?; module 09 Facts, media, rights (lesson 3 of 4).

**Lead source (audit, 2026-10-12):** S076 (Julia Apostle, Orrick); S195 (artificialintelligenceact.eu (Future of Life Institute)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S076, S195, S200, S079); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Through-line for the script:** two marks on every piece. The invisible one the tool writes for machines (provider), and the visible one you put where people look (deployer). Then a third layer: the platform's own form and rules. Each layer is checked by someone different, and none of them does the others' job (S076, S195, S200).

**Timing note:** Article 50 has applied since 2026-08-02, and generators already on the market before that date must mark their outputs by 2026-12-02 (S195). Make this lesson before December, and re-check at production time whether any amendment has moved these dates: the consolidated text marks Article 111(4) as new without naming the amending act, and this run could not search for it (see Sources).

## What to teach (binding scope)

### C110 The tool's watermark is not your label
- **Two roles, two duties.** The provider, who makes the generating system, must mark outputs "in a machine-readable format and detectable as artificially generated or manipulated" (Art. 50(2)); the deployer, who uses a system under its own authority, must "disclose that the content has been artificially generated or manipulated" for deepfakes and certain text (Art. 50(4)) (S195, S076). Depth: teach.
- **You are a deployer when you publish in a professional capacity.** The only carve-out is use "in the course of a personal non-professional activity"; "authority" means taking responsibility for deciding to deploy and for how outputs are used, and technical control is not required, so using someone else's tool does not move the duty off you (S076). Depth: teach.
- **What the tool's marks look like.** Claude's text carries a version of Google DeepMind's SynthID-Text watermark in its word choices, adds "Nothing ... and there are no hidden characters", and is not applied where "an exact output is required" (S196). Files Claude creates, such as PNG and JPEG, carry a signed C2PA Content Credential that a free Claude Content Checker can read (S198). Gemini's images all carry SynthID (S108). Marks can be lost through heavy editing, paraphrase or stripped metadata (S198). Depth: brief.
- **What a mark can't tell anyone.** A detection hit "means Claude was probably involved"; it "can't say who wrote the text", "no hit doesn't mean a human wrote it", and only approved organisations can check Claude's text mark: "There is no public checker" (S197). The watermark "doesn't say anything about ownership or authorship" (S196). Depth: brief.
- **If you ship something that generates images, audio, video or text, you may be the provider.** Article 50(2) addresses "Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content" (S195). The Code of Practice approach layers signed metadata with an imperceptible watermark; detection must be free and human-readable, with an interoperable detection solution due by 2027-02-02; "A provider that uses a third-party solution is responsible for ensuring its compliance" (S076). Systems on the market before 2026-08-02 must comply by 2026-12-02 (S195, Art. 111(4)). Whether a thin wrapper over someone else's API makes you the provider is not settled by these sources: a lawyer scopes it (S076). Depth: brief, with the dates on screen.
- **Standard editing needs no mark.** Grammar and spelling fixes, format conversion, compression, noise reduction, minor cropping and minor colour correction are out of scope; replacing objects or faces is in (S076). Depth: one line.
- **Never strip provenance.** Suno's terms forbid you to remove or circumvent "any fingerprint, watermark or metadata" it appends (S077); ElevenLabs users "must not remove, alter, or conceal ElevenLabs watermarks, metadata or other provenance signals" (S199). Depth: brief.
- **What binds.** The Act binds; the Commission's Guidelines (dated 2026-07-20) are non-binding interpretation; the Code of Practice is voluntary, and "Adherence does not constitute conclusive evidence of compliance" (S076). Depth: one line.

### C111 How and where to disclose AI media
- **What counts as a deepfake.** Image, audio or video that resembles existing "persons, objects, places, entities or events" and would falsely appear authentic, judged as a whole with diverse audiences in mind: a photoreal fake event at a real place counts, not only a celebrity's face. Text is never a deepfake; it has its own rule (C112) (S195, S076). Depth: teach.
- **When.** "Clear and distinguishable", "at the latest at the time of the first interaction or exposure", and meeting accessibility requirements (S195, Art. 50(5)). Depth: teach.
- **Video and images.** Nothing overlays the label and it stays long enough to be recognised; for video, at the start, after interruptions and at regular intervals; live content, or content people reach at different times, needs repeated or persistent disclosure (S076). Depth: teach.
- **What fails.** Disclosure only in end credits, only in terms and conditions, in hidden menus, or anything the viewer has to act on or use a tool to see (S076). Depth: teach (this is the habit most creators have).
- **Audio.** A short, plain-language spoken disclaimer at the start; long-form or live audio repeats it at intervals and after interruptions, plus a visual label wherever there is a screen (S076). Depth: teach.
- **The EU icons are optional; labelling is not.** "AI GENERATED", "AI MODIFIED" and a basic "AI" icon are free to use; using one does not by itself prove compliance (S076). Depth: brief.
- **Art, satire and fiction get a lighter duty, not an exemption.** Only when the work is evidently artistic, satirical, fictional or analogous ("ambiguous content does not qualify"), and then disclosed "in an appropriate manner that does not hamper the display or enjoyment of the work"; end credits alone still fail, a small icon by the frame can work (S076, S195). Depth: teach.
- **YouTube is a second, separate check.** Disclose in YouTube Studio's "AI use" attribute when content is photorealistic and meaningfully altered or generated: extra AI footage of a real place, a realistic match between real tennis players, AI music that is the video's focus. Not needed for unrealistic content, beauty or colour filters, AI-written scripts, titles or thumbnails, or cloning your own voice for voice-overs. Photorealistic content may get a label on the player, other content one in the expanded description; YouTube may apply a label itself from C2PA metadata, and you can't change it; creators who keep failing to disclose risk content removal or Partner Program suspension (S200). No source here says YouTube's label satisfies Article 50: treat them as two checks (S076, S200). Depth: teach.
- **US ads.** New York's S.8420A (signed December 2025) requires conspicuous disclosure when an ad includes a "synthetic performer" (S078). Depth: one line; likeness belongs to 09.04.

### C112 AI-written public-interest text needs a responsible, fact-checking human or a label
Taught as a two-minute segment, as its concept entry recommends.
- **Scope.** AI-generated or AI-altered text "published with the purpose of informing the public on matters of public interest"; novels, poems, private correspondence and internal documents are out (S195, S076). Depth: brief.
- **The exception has two conditions.** (a) "Deliberate substantive examination by competent natural person(s)", or editorial control with authority to approve, alter or reject on substance, with fact-checking the minimum; and (b) a person or organisation holding "ultimate legal responsibility", with identity and contact details public (S076). Depth: teach.
- **What is not review.** Spell-checking, grammar correction and automated review "do not suffice", and substantive AI changes made after the review can void the exception, so review the final version (S076). Depth: brief.
- **Using it.** Publish an editorial policy and a byline naming the reviewer with contact details, or label the text (S076). Depth: brief.
- **What detection sees in Claude's text.** If Claude only proofread a text "there's almost nothing to find"; if it rewrote it, "the mark is in Claude's word choices"; asking Claude to reword gives "a new watermark" (S197). Depth: one line.

### C116 Platform rules apply on top of the tool's licence
- **Three independent layers: the law, the tool's contract and the platform's rules.** Any one can stop you; a platform refusing your content does not revoke the tool's grant, and the tool's grant does not oblige the platform to accept it (S077). Depth: teach; this is the lesson's last frame.
- **Disclosure is not demonetisation.** "Disclosing AI content won't limit a video's audience or impact its eligibility to earn money" (S200). Depth: teach (kills a common fear).
- **What does cost money on YouTube.** Since the 2026-07-16 clarifications, three kinds of "inauthentic content" can't be monetised: generic, template or mass-produced videos (tutorials that duplicate what is common included), content made to distress or manipulate (removed from the Partner Program "regardless of whether the content is AI-generated or not"), and AI depictions of real people discussing finance, legal or health topics. A channel with "too much" of any of them can't monetise, and no threshold is published (S079). The policy text says automated tools are fine but "the final product must still demonstrate your creative vision", reviewers judge the whole channel, and permission from the original creators does not exempt reused content (S205). Depth: brief.
- **Game storefronts have their own AI rules.** Steam's content survey separates content pre-generated with AI during development from content generated while the game runs, which needs a description of your guardrails (S239); itch.io: "accurately tag your project if it contains materials produced by generative AI", or risk delisting (S250). Depth: brief.
- **Other platforms are not covered by this research.** TikTok, Meta and Spotify's AI rules were not read; check each destination's own policy before uploading (concepts.md, G12 notes). Depth: one line.
- Dropped to the deep-dive backlog: creator monetisation and game storefronts in depth.

## You vs the agent
As of 2026-10-12:
- **The agent does on its own:** burns an "AI GENERATED" card in at 0:00 and after every cut; generates and inserts a spoken disclaimer at set intervals; grabs frames from the render to prove the label is there at those times; wires metadata signing and a watermark library into an app; re-encodes a file and compares its metadata before and after; fetches the current policy and terms pages and quotes the clause; lists every factual claim in a text with its source; checks a planned upload against the examples a policy page lists; drafts store survey answers from the asset log (S076, S198, S200, S239).
- **It can't:** know whether a publication is professional or personal, whether viewers would take a scene as real, whether a work is evidently satire, or whether the person, place or event shown is real; check Claude's own text watermark (only approved organisations can, S197); certify its own facts or take legal responsibility (S076); or predict how a platform reviewer will weigh a whole channel (S205).
- **You decide and check:** whether this is professional use; where the visible label goes, by watching the final render as a viewer would; that nobody, agent included, strips provenance; that public-interest text was substantively reviewed and signed, or labelled; and that store and platform forms are answered truthfully.
- **You bring in an expert:** an EU lawyer before launching a generator product in the EU, before a commercial EU release that depicts real people, for borderline political satire, or when unsure whether a topic counts as public interest; a subject expert or editor for claims you cannot check yourself; and a real, identified expert to front finance, legal or health content (S076, S079). How to brief one is taught in 04.04.

## Sources this lesson is built from
- S076 — Julia Apostle, Orrick, "EU AI Act: Transparency Obligations for AI-Generated Content (Article 50)" (2026-08-14) https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50 — provider vs deployer, placement and timing rules, art and satire, public-interest text, icons, standard editing, what binds; re-read 2026-10-12.
- S195 — artificialintelligenceact.eu (Future of Life Institute), EU AI Act Articles 50 and 111, consolidated text (undated pages; Article 50 applies from 2026-08-02) https://artificialintelligenceact.eu/article/50/ ; https://artificialintelligenceact.eu/article/111/ — the Act's own wording and the 2026-12-02 deadline; Article 111 re-read 2026-10-12.
- S200 — Google / YouTube, "Disclosing use of GenAI content" (YouTube Help; undated, page shows ©2026) https://support.google.com/youtube/answer/14328491 — when to tick "AI use", where the label shows, automatic C2PA labels, disclosure and earnings; re-read 2026-10-12.
- S079 — Sarah Perez, TechCrunch, "YouTube clarifies policies around AI slop and upsetting videos" (2026-07-20; rollout 2026-07-16) https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ — the three kinds of inauthentic content and the channel-level "too much" rule; re-read 2026-10-12.

Also cited for single points (credit on the lesson page):
- S196 — Anthropic, "Anthropic announcement on watermarking Claude's text" (2026-08-14, updated 2026-09-01) https://www.anthropic.com/news/claude-text-watermark
- S197 — Aaron Orelup (drafted by Claude Opus 5.5), "AO-040: Claude's text is watermarked now, and the mark only lives where Claude had a choice" (2026-10-06) https://aaronorelup.com/ledger/claude-text-watermark/
- S198 — Anthropic, "How Claude marks AI-generated content" (Claude Help Center; undated, "Updated this week" on 2026-10-12) https://support.claude.com/en/articles/16266773
- S108 — Google, "Image generation, 'Nano Banana'" (Gemini API docs, last updated 2026-10-09) https://ai.google.dev/gemini-api/docs/image-generation
- S077 — Suno, "Suno Terms of Service" (revised 2026-08-10, effective 2026-09-03) https://suno.com/terms
- S199 — ElevenLabs, "Prohibited Use Policy" (last updated 2026-10-09) https://elevenlabs.io/use-policy
- S078 — Erik Dullea, Evan Yahng (Husch Blackwell), "A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress" (2026-08-20) https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/
- S205 — Google / YouTube, "YouTube channel monetization policies" (latest dated update on the page 2025-07-15; live policy page) https://support.google.com/youtube/answer/1311392
- S239 — Valve, "Content Survey" (Steamworks documentation, undated live docs) https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- S250 — itch.io, "Quality guidelines" (undated live docs) https://itch.io/docs/creators/quality-guidelines

Recency and limits: S076, S079, S196, S197, S077, S199 and S078 are from the last three months; S195, S200, S198, S239 and S250 are undated live pages read on 2026-10-12. The placement details rest on one law firm's reading (S076) of non-binding Guidelines plus the Act's text; no survey or incident measures how often creators get this wrong. This run's web-search budget was used up, so the status of the amendment that inserted Article 111(4) (and any change to the Article 50 dates) could not be searched; check it before production.

## Show it for real
- A PNG made by Claude opened in the free Claude Content Checker, showing the signed credential; then the same image posted with no visible label, where a viewer sees nothing (S198): proves the mark is for machines.
- The agent re-encodes that file (or strips its metadata) and the checker finds nothing (S198): proves a pipeline can lose the credential silently.
- A video timeline with an "AI GENERATED" label at 0:00 and again after a mid-video cut, beside a version with only an end-credit line marked as failing (S076): proves where and when.
- An audio editor with a two-second spoken disclaimer at the start and after an ad break (S076): proves audio labels are spoken.
- YouTube Studio's upload form on a private draft, at Attributes, then "AI use", Yes or No (S200): proves the platform's separate check. Use a test channel; hide subscriber counts and e-mail.
- Three generated stills side by side (a stylised cartoon, a photoreal fake event, a photoreal real landmark), sorted by whether the deepfake definition plausibly reaches them (S195, S076): proves "deepfake" is broader than faces.
- An article with a byline, a "reviewed and fact-checked by" line and contact details, beside an unlabelled agent draft (S076): proves the public-interest text exception.
- Steam's content survey page, pre-generated vs live-generated (S239): proves stores ask their own questions.

## Questions this lesson answers
From the research crew's batch reader (`research/notes/rights-and-disclosure.json` #01-#07, #12, #14, #17, #18) and a few derived from the sources and marked so; no beginner forum threads were collected for media rights yet.
- If Midjourney or Veo already watermarks my video, do I still have to label it?
- Does the EU AI Act apply to me as a YouTuber or a small studio? Is a personal post different from a client job?
- My app calls an image API. Do I have to watermark?
- Can I remove the Suno watermark?
- Where exactly do I put the AI label on my video? Is a credit at the end enough? Do I have to use the EU icon?
- How do I disclose an AI voice in a podcast? Do I need to say it more than once?
- My AI short film is obviously fiction. Do I still need a label? Is satire of a politician exempt?
- Is my photoreal AI landscape a deepfake?
- Do I have to label AI-written blog posts? How much editing makes it human-written?
- Is the text Claude writes for me watermarked? (derived from S196)
- Will ticking the AI box hurt my earnings? (derived from S200) Can I monetise an AI faceless channel?
- Do I have to disclose AI art in my Steam or itch.io game? (derived from S239, S250)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Publishing is an action that is never the agent's alone → the-narrowest-keys-and-verbs
- Saying it's AI when your own app's feature talks to people (chatbot disclosure) → your-apps-ai-feature
- Checking sources and claims before publishing → checking-research-numbers-and-parts
- Where SynthID and generated media come from → making-media-with-ai
- Consent for voices and faces, generator terms, ownership and infringement → own-it-sell-it-publish-it
- What to hand an expert → before-you-ship-who-signs-off
- Creator monetisation and game storefronts in depth; AI-written public-interest text in depth → deep-dive backlog (curriculum-draft.md)

## Out-of-date framings to avoid
- "The tool's watermark or metadata takes care of disclosure." The duties belong to two different parties (S076, S195).
- "EU AI rules only apply to AI companies." Professional publishers are deployers (S076).
- "Only OpenAI and Google have to watermark." Article 50(2) reaches any provider of a generating system (S195).
- "Strip the metadata so nobody knows it's AI." It breaks Suno's terms and ElevenLabs' policy (S077, S199).
- "A watermark detector tells you who wrote it" and "nobody can tell Claude wrote it" (S197, S198).
- "'Made with AI' in the description or end credits is enough" (S076).
- "Parody and art are exempt." They get a lighter duty, only when evidently in a listed category (S076).
- "A deepfake is a fake video of a celebrity's face." Places, objects and events count (S195, S076).
- "Audio can't be labelled; show notes are enough" (S076).
- "If I skim it and fix typos, it's my writing" and "AI text never needs a label" (S076, S195).
- "YouTube's AI label takes care of the law." No source says so (S076, S200).
- "YouTube demonetises AI videos" and "each video is judged alone" (S200, S079, S205).
- "If the AI tool says I can use it commercially, every platform will accept it" (S077).

## Legacy notes
No published lesson covers this slot. A proof-of-concept, `lessons/poc-synthid-text` ("How SynthID-Text works", not part of the course), animates how a text watermark lives in word choices and could supply one short visual for "what the tool's marks look like"; its mechanism details are not backed by a source in sources.md (S196 and S197 cover only what the mark can and cannot show), so source them before reuse.
