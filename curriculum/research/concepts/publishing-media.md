# G12 Publishing AI-made media: disclosure, ownership and likeness (C110 to C116)

Concept entries for The Hidden Curriculum. Written 2026-10-12 by the concepts-publishing-media agent.

## Method and honesty notes

- **Starting point.** `taxonomy.md` (C110 to C116, which merge the 18 items in `notes/rights-and-disclosure.json`), the batch reading notes `notes/rights-and-disclosure.md`, `sweep/beyond-code.md` items 16 to 20, and `sources-candidates.md` batch 14.
- **Re-checked today.** On 2026-10-12 I re-opened all four batch sources (S076 to S079) and checked every point used here against the live page. Two corrections came out of this. First, Orrick (S076) does not define "provider" and does not say that an app built on someone else's model is a provider (see C110, point 5). Second, Suno's download quota is confirmed as monthly: "The number of Downloads you are permitted per month depends on your service tier".
- **Sources added.** The taxonomy flags C111 to C114 as thin, so I added 11 sources, each fetched and read today. They carry the local IDs SG12-01 to SG12-11 (listed at the end) so they cannot collide with S-IDs that other concept writers add.
- **How they were reached.** The shared web-search budget was already used up when this agent started, so no new searches ran. Each added page was reached in one of four ways:
  - through a URL already in the research notes (SG12-01 and SG12-02 from the batch notes; SG12-11 from `sweep/aaron.md`);
  - through a link on a page I had fetched (SG12-03 and SG12-04 from copyright.gov/ai; SG12-09 and SG12-10 from SG12-11);
  - by opening official help and terms pages directly (SG12-05 to SG12-08).

  Each page returned the content described below.
- **What is still missing:**
  - **Community questions.** No community thread (Reddit, forums, Discord, YouTube comments) was collected for media rights. The "Questions it answers" lines are the questions the batch reader derived from the sources, plus a few I derived and marked as such. None were seen in beginner posts.
  - **Measurements.** No survey or incident report measures how often creators get these rules wrong. "Why it is a gap" therefore rests on two things: how new the rules are, and the habits the sources themselves list as non-compliant.
  - **Not covered:**
    - TikTok, Meta and Spotify AI labels;
    - which amending regulation inserted AI Act Art. 111(4), i.e. the status of the "Digital Omnibus";
    - the content of the Copyright Office's Part 1 *Digital Replicas* report (I saw only its title and date, 2024-07-31).
  - **Unreadable.** https://verify.contentauthenticity.org/ (the redirect target of contentcredentials.org/verify) returned only its title, so no demo depends on it.
- **Scope.** All law here is EU or US. These entries are teaching notes, not legal advice, and every concept says when to bring in a lawyer.
- **Cross-links.** C084 covers the point that publishing is an action that is never the agent's alone. C032 covers models that make media.

---

### C110 The tool's watermark is not your label

- **In one line:** Under the EU AI Act, the tool maker (provider) marks outputs for machines, while you (deployer), when you publish professionally, must disclose to people in a way they can see. If you ship a generator, you may take on the marking duty yourself. Stripping a tool's provenance marks breaks its terms.

- **Why it is a gap:**
  - **Two duties, two parties.** Article 50(2) makes providers mark outputs "in a machine-readable format and detectable as artificially generated or manipulated". Article 50(4) makes deployers "disclose that the content has been artificially generated or manipulated" (SG12-02). A generator that embeds metadata does not discharge the publisher's duty (S076). The batch reader recorded the assumption this creates: "the tool's watermark or metadata takes care of disclosure" (rights-and-disclosure.json #01, S076).
  - **The rules are weeks old.**
    - Article 50 applies from 2 August 2026 (SG12-02).
    - The Commission's interpretive Guidelines are dated 20 July 2026 (S076).
    - Generators already on the market before 2 August 2026 have until 2 December 2026 to mark outputs. This is Art. 111(4), shown as "new" in the consolidated text (SG12-02).
  - **The marks people rely on are invisible and partial.**
    - Claude's text watermark adds "Nothing ... and there are no hidden characters".
    - It is not applied where "an exact output is required", such as factual answers and most code (SG12-09).
    - Only organisations Anthropic approves can check it: "There is no public checker" (SG12-11).
    - A viewer sees nothing unless the publisher adds a label.
  - **The vendor hands the question back to you.** Anthropic's help page tells organisations deploying Claude to "independently assess what Article 50 requires of your products and services" (SG12-10).

- **What to teach (specific points):**
  1. **Two roles with different duties.** The provider makes the generative system and must mark its outputs machine-readably. The deployer uses a system under its own authority and must visibly disclose deepfakes and certain AI-written text (S076, SG12-02).
  2. **When you are a deployer.** Publishing in a professional capacity makes you one. The only carve-out is use "in the course of a personal non-professional activity". "Authority" means taking responsibility for the decision to deploy and for how the outputs are used. "Technical control is not required", so using someone else's tool does not remove the duty (S076).
  3. **What providers' marks look like in practice:**
     - Claude text carries a version of Google DeepMind's SynthID-Text watermark, hidden in its word choices.
     - Supported files Claude creates (for example PNG and JPEG) carry a signed C2PA Content Credential in their metadata.
     - Marks can be lost through heavy editing, paraphrasing or stripped metadata.
     - Text detection is in private preview for approved organisations. A free Claude Content Checker reads the file credentials (SG12-09, SG12-10).
  4. **What a mark can and cannot tell you.** A detection hit "means Claude was probably involved". It "can't say who wrote the text, or whether Claude wrote it or only edited it", and "no hit doesn't mean a human wrote it" (SG12-11). Anthropic says the watermark "doesn't say anything about ownership or authorship" (SG12-09).
  5. **If you ship an app that generates synthetic image, audio, video or text:**
     - Article 50(2) addresses "Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content" (SG12-02).
     - The Code of Practice approach has two layers: digitally signed, time-stamped metadata plus an imperceptible watermark. Free-form text carries a watermark only, and above 200 tokens the watermark is mandatory (S076).
     - Detection must be free of charge and give human-readable results. An interoperable detection solution is targeted for 2 February 2027 (S076).
     - "A provider that uses a third-party solution is responsible for ensuring its compliance" (S076).
     - The sources do not settle whether a thin wrapper over someone else's API makes you "the provider". Orrick does not address it (S076), so have a lawyer scope it before an EU launch.
  6. **Standard editing needs no mark.** Minor cropping, standard colour and contrast changes, dust removal and red-eye correction are out of scope. Removing, replacing or inserting objects or people is in scope, and so are colour or lighting changes that alter meaning (S076).
  7. **Do not strip provenance.**
     - Suno's terms forbid you to "remove, alter, obscure or circumvent any fingerprint, watermark or metadata Suno appends", and Suno may mark the tier and download status (S077).
     - ElevenLabs' policy says users "must not remove, alter, or conceal ElevenLabs watermarks, metadata or other provenance signals" (SG12-08).
  8. **Platforms read the marks.** YouTube may automatically apply an AI label to uploads that contain C2PA metadata, and the creator cannot adjust that label (SG12-05).
  9. **What binds.** The Act is binding. The Commission Guidelines are non-binding interpretation. The Code of Practice is voluntary, and "Adherence does not constitute conclusive evidence of compliance" (S076).

- **You vs the agent (as of 2026-10-12):**
  - **The agent** can do the verifiable parts. It can put a visible label on a render, wire metadata signing and a watermark library into an app, re-encode a file and compare its metadata before and after, and fetch the current terms (rights-and-disclosure.json #01, #07, #12).
  - **What the agent cannot know:** whether this publication is professional, where it will be seen, or whether a person, place or event it shows is real. It also cannot check Claude's text watermark, since only approved organisations can (SG12-11).
  - **The human** decides whether this is professional or personal use, puts the visible label in place, and never asks an agent to strip provenance.
  - **Bring in an expert:** an EU lawyer before launching a generator product in the EU, or before a commercial EU release that depicts real people (S076, SG12-10).

- **Currency:** New in 2026.
  - Key dates: Article 50 applies from 2026-08-02; the Guidelines are dated 2026-07-20; pre-August systems must mark by 2026-12-02; detection interoperability is due 2027-02-02 (S076, SG12-02).
  - Anthropic signed the EU Code of Practice in July 2026 and is still rolling the text watermark out to older models. Its help page lists Amazon Bedrock completion for some models "by October 17" (SG12-09, SG12-10).
  - Open question: the consolidated text does not name the amendment that inserted Art. 111(4) (SG12-02).

- **Outdated framings to avoid:**
  - "The tool's watermark or metadata takes care of disclosure." The duties are split between two parties (S076, SG12-02).
  - "EU AI rules only apply to AI companies." Professional publishers are deployers (S076).
  - "Only OpenAI and Google have to watermark." Article 50(2) addresses providers of any AI system that generates synthetic content (SG12-02).
  - "Strip the metadata so nobody knows it's AI." This breaks Suno's terms and ElevenLabs' policy (S077, SG12-08).
  - "A watermark detector tells you who wrote it." It cannot (SG12-11).

- **Questions it answers:**
  - From the batch reader (rights-and-disclosure.json #01, #07, #12):
    - "If Midjourney or Veo already watermarks my video, do I still have to label it?"
    - "Does the EU AI Act apply to me as a YouTuber or a small studio?"
    - "Is a personal post different from a client job?"
    - "My app calls an image API. Do I have to watermark?"
    - "Can I remove the Suno watermark?"
  - Derived by me from SG12-09: "Is the text Claude writes for me watermarked?"

- **Show it for real:**
  - Generate a PNG with Claude and open it in the free Claude Content Checker to show the signed credential. Then post it with no visible label and show that a viewer sees nothing (SG12-10).
  - Re-encode or strip the file's metadata and check again, to show how a pipeline silently loses the credential (SG12-10; demo idea from #12).
  - Upload a private draft containing C2PA metadata to YouTube Studio and show the automatic AI-label notice, which YouTube says it "may" apply (SG12-05).
  - Put Suno's no-stripping clause next to ElevenLabs' (S077, SG12-08).

- **Priority:** must.
  - Evidence: 3 batch items (2 high severity), now backed by 8 sources (S076, S077, SG12-02, SG12-05, SG12-08 to SG12-11), all dated 2026 or live pages.
  - Urgency: the 2 December 2026 marking deadline is seven weeks away.
  - Reach: it applies both to creators who publish (deployers) and to builders who ship generators (providers), which is the course's core audience.

---

### C111 How and where to disclose AI media

- **In one line:** In the EU, a deepfake includes realistic fake places, objects and events, not only faces. The disclosure must appear at first exposure and at intervals, never only in the end credits. Audio needs a spoken disclaimer. Art and satire get a lighter duty, not an exemption. Platform labels such as YouTube's are a separate check with different rules.

- **Why it is a gap:**
  - **Common habits fail.** A credit line or a description line is the usual practice. The guidance Orrick summarises lists these as non-compliant: disclosure "only in end credits", only in terms and conditions, in hidden menus, or anything that needs the viewer to act or use a tool (S076).
  - **"Deepfake" is broader than people think.** It covers content that "resembles existing persons, objects, places, entities or events" (S076, SG12-02), not only celebrity face swaps (rights-and-disclosure.json #02).
  - **Platform labels teach a different bar.** YouTube puts its label for non-photorealistic AI content in the expanded description, and does not require disclosure when you clone your own voice for voiceovers (SG12-05). A creator who learns placement from YouTube therefore learns rules that differ from the EU guidance for deepfakes (S076). This is my comparison of two sources. Neither source says whether a YouTube label satisfies Article 50.
  - **Thin evidence.** The placement details rest on one law-firm reading (S076) of non-binding Guidelines, plus the Act's own text (SG12-02).

- **What to teach (specific points):**
  1. **What counts as a deepfake.**
     - It is AI-generated or manipulated image, audio or video that resembles existing persons, objects, places, entities or events and "would falsely appear to a person to be authentic or truthful".
     - It is judged holistically, with diverse audiences in mind.
     - Text is never a deepfake; it has its own rule, C112 (S076, SG12-02).
  2. **When to disclose.** The label must be "clear and distinguishable" and appear "at the latest at the time of the first interaction or exposure", meeting accessibility requirements (SG12-02, Art. 50(5)).
  3. **Video and images.**
     - Nothing may overlay the label, and it must stay long enough to be recognised.
     - For video, show it at the start, after interruptions and at regular intervals.
     - For live content, or content people see at different times, disclose again later or persistently (S076).
  4. **What fails:** disclosure only in end credits, only in terms and conditions, in hidden menus, or any disclosure that requires the viewer to take an action or use a tool (S076).
  5. **The EU icons are optional.** The icons read "AI GENERATED", "AI MODIFIED" and "AI". Labelling itself is not optional, and using an icon does not by itself prove compliance (S076).
  6. **Audio.** Give a short, plain-language spoken disclaimer at the start. Long-form or live audio also needs reminders at regular intervals and after interruptions, plus a visual label wherever a screen exists (S076).
  7. **Art, satire and fiction get a lighter duty, not an exemption.**
     - It applies only when the work is evidently artistic, creative, satirical, fictional or analogous, and "ambiguous content does not qualify".
     - You must then disclose that AI content exists "in an appropriate manner that does not hamper the display or enjoyment of the work".
     - End credits alone still fail.
     - A small icon next to the frame or in the UI is acceptable. Exhibitions and cinemas can disclose at the entry point or in accompanying materials (S076, SG12-02).
  8. **YouTube is a second, separate check.**
     - During upload, find "AI use" in the Attributes section of YouTube Studio and select Yes when content is realistic and generated or meaningfully altered.
     - Examples that need it: extra AI footage of a real place, a realistic match between two real tennis players, AI music that is the focus of the video.
     - Examples that don't: unrealistic content, beauty or colour filters, AI-made scripts, thumbnails or captions, and your own cloned voice.
     - Creators who consistently fail to disclose may get a label applied manually, content removed or a suspension from the YouTube Partner Program (SG12-05).
  9. **US ads.** New York S.8420A, signed in December 2025, requires conspicuous disclosure when an advertisement includes a "synthetic performer" (S078).

- **You vs the agent (as of 2026-10-12):**
  - **The agent** can burn an "AI GENERATED" card in at 0:00 and after every cut, generate and insert a spoken disclaimer at set intervals, and check frames from the render to confirm the label is present at those times. All of this is checkable (rights-and-disclosure.json #03, #04).
  - **The human** must judge whether a viewer would take a scene as real, and whether a work is "evidently" satire or fiction. These are per-piece judgements the agent cannot verify (rights-and-disclosure.json #02, #05). The human also watches the final render as a viewer would.
  - **Bring in an expert:** a lawyer for commercial EU releases and for borderline political satire involving real people (rights-and-disclosure.json #03, #05).

- **Currency:** New in 2026.
  - Article 50 has applied since 2026-08-02. The Guidelines (2026-07-20) are non-binding and the Code is voluntary (S076, SG12-02).
  - YouTube's GenAI disclosure page is a live page with no date (SG12-05).
  - New York S.8420A was signed in December 2025. The source gives no effective date (S078).

- **Outdated framings to avoid:**
  - "Putting 'made with AI' in the description or end credits is enough." See S076.
  - "Parody and art are exempt." They get a reduced duty, and only when evidently in a listed category (S076).
  - "A deepfake is a fake video of a celebrity's face." Places, objects and events count too (S076, SG12-02).
  - "Audio can't be labelled, and show notes are enough." A spoken disclaimer is expected (S076).
  - "YouTube's AI label takes care of the law." No source here says so, and the two sets of rules differ (S076, SG12-05).

- **Questions it answers (batch reader, rights-and-disclosure.json #02 to #05):**
  - "Where exactly do I put the AI label on my video?"
  - "Is a credit at the end enough?"
  - "Do I have to use the EU icon?"
  - "How do I disclose an AI voice in a podcast? Do I need to say it more than once?"
  - "My AI short film is obviously fiction. Do I still need a label?"
  - "Is satire of a politician exempt?"
  - "Is my photoreal AI landscape a deepfake?"

- **Show it for real:**
  - In a video editor, place an "AI GENERATED" label at 0:00 and again after a mid-video cut. Next to it, show a version with only an end-credit line, marked non-compliant (#03; S076).
  - In an audio editor, insert a two-second spoken disclaimer at the start and after an ad break (#04; S076).
  - Show YouTube Studio's upload form at Attributes, then "AI use", Yes or No (SG12-05).
  - Put three generated outputs side by side (a stylised cartoon, a photoreal fake event, a photoreal real landmark) and sort them by whether the definition plausibly reaches them (#02).

- **Priority:** should.
  - Evidence: 4 batch items (1 high severity), now backed by S076, SG12-02, SG12-05 and S078, all dated 2026 or live.
  - Reasoning: the detail is EU-specific and rests on non-binding guidance, so it is best taught as the second half of the C110 lesson rather than as a lesson of its own.

---

### C112 AI-written public-interest text needs a responsible, fact-checking human or a label

- **In one line:** In the EU, AI-generated or AI-altered text published to inform the public on matters of public interest must be labelled. The exception applies only if a competent human substantively reviewed it (fact-checking at minimum) and a named person or organisation publicly takes legal responsibility. Skimming or spell-checking doesn't count.

- **Why it is a gap:**
  - Bloggers and newsletter writers who publish agent drafts assume a read-through makes the text "human-written". The bar is substantive review that includes fact-checking, plus a publicly identified responsible person (S076; rights-and-disclosure.json #06).
  - Detection now exists. Claude text has carried a watermark since the EU rules took effect, across "Claude Platform (API), Claude, Claude Code, Claude Cowork, and Claude Tag". Approved regulators, journalists and fact-checkers can check it (SG12-09, SG12-10, SG12-11).
  - Thin evidence: one law-firm reading (S076) plus the Act's text (SG12-02). There is no case, survey or incident yet.

- **What to teach (specific points):**
  1. **Scope.** The rule covers text "published with the purpose of informing the public on matters of public interest" that AI generated or manipulated (SG12-02). The deepfake rule does not cover text; this is a separate rule (S076).
  2. **Exception condition (a): human review or editorial control.** This means "Deliberate substantive examination by competent natural person(s)", or an editorial body with authority to approve, alter or reject content on substance. Fact-checking is the minimum (S076, SG12-02).
  3. **Exception condition (b): named responsibility.** A natural or legal person must hold "ultimate legal responsibility over the publication", and their identity and contact details must be public (S076).
  4. **What is not review:** "Superficial, purely formal or procedural checks" such as spell-checking, grammar correction or automated review (S076).
  5. **Order matters.** Substantial AI changes made after the human review can void the exception, so review the final version (S076).
  6. **News media.** Media service providers under Regulation (EU) 2024/1083 may rely on their existing editorial procedures (S076).
  7. **Using the exception.** Publish an editorial policy and a byline with a reviewer and contact details. Otherwise, label the text (rights-and-disclosure.json #06; S076).
  8. **What detection can see in Claude text:**
     - If Claude only proofread a text, "there's almost nothing to find".
     - If Claude rewrote it, "the mark is in Claude's word choices", and a Claude translation is marked too.
     - Asking Claude to reword produces "a new watermark" (SG12-11).
     - Text where an exact output is required is not marked (SG12-09).

- **You vs the agent (as of 2026-10-12):**
  - **The agent** drafts, can list every factual claim with its source, and can check what it can reach, such as whether a link resolves and whether a quote matches its page.
  - **What the agent cannot do:** certify its own claims. Fact-checking the claims it generated is the job the rule assigns to a competent human, and taking legal responsibility is by definition a human or organisational act (S076).
  - **The human** reviews the final text substantively, signs it and publishes contact details, or labels it.
  - **Bring in an expert:** a subject expert or editor for claims the human cannot check, and a lawyer for an EU publisher unsure whether a topic counts as "public interest" (S076).

- **Currency:** New in 2026. The rule has applied since 2026-08-02, with Guidelines dated 2026-07-20 (S076, SG12-02). Anthropic began watermarking text in August 2026 and is still rolling it out to older models (SG12-09, SG12-10).

- **Outdated framings to avoid:**
  - "If I skim it and fix typos, it's my writing." Formal checks don't count (S076).
  - "AI text never needs a label." Public-interest text does (SG12-02).
  - "Nobody can tell Claude wrote it." Approved organisations can detect the watermark (SG12-10, SG12-11).
  - "A detector hit proves the AI wrote it." It can't say who wrote it (SG12-11).

- **Questions it answers:**
  - From the batch reader (rights-and-disclosure.json #06): "Do I have to label AI-written blog posts?" and "How much editing makes it human-written?"
  - Derived by me from SG12-09 and SG12-11: "If Claude only fixes my grammar, is my post watermarked?"

- **Show it for real:**
  - Show an article page with a byline, a "reviewed and fact-checked by" line and contact details, next to an unlabelled agent draft (#06).
  - Open the Claude Help Center page's table of which models carry the text watermark on which platforms (SG12-10).

- **Priority:** could as a lesson of its own. Teach it as a two-minute segment of the C110 and C111 lesson.
  - Evidence: one item of medium severity, one interpretive source, the Act's text, and Anthropic's watermark pages (all 2026).
  - Reach: it matters to anyone in the audience who publishes AI-drafted articles that EU readers see.

---

### C113 Generator terms decide what you can sell

- **In one line:** Free tiers can be personal use only. Commercial rights can depend on a permitted download within a monthly quota, and remixes may never be commercial. Read each tool's current tier terms and log which plan made each asset.

- **Why it is a gap:**
  - **The contracts change under you.** Suno's terms were revised on 2026-08-10, effective 2026-09-03, and made the download the trigger for commercial rights. ElevenLabs' terms were last updated on 2026-10-09 (S077, SG12-07). Anything an agent remembers about a tool's licence is probably older than the live terms.
  - **Paying is assumed to cover everything.** Creators assume a subscription covers everything they generated, or that upgrading turns free-tier songs commercial. Suno's terms support neither (S077; rights-and-disclosure.json #08, #09).
  - **Tools differ.** Suno ties commercial rights to a permitted download within a monthly, per-tier quota. ElevenLabs ties them to being a paid user (S077, SG12-07). One rule learned from one tool does not carry to the next.

- **What to teach (specific points):**
  1. **Free tiers are non-commercial.** Suno Free and Basic outputs are for "your lawful, personal and non-commercial purposes" (S077). ElevenLabs free users "may only use the Services for non-commercial purposes" (SG12-07, Section 1(c)).
  2. **Suno Pro and Premier.**
     - Suno assigns its rights in outputs generated from your submissions. Commercial use is allowed only for outputs obtained through a permitted Download.
     - "The number of Downloads you are permitted per month depends on your service tier". The limits are shown on the account page and may change.
     - "You may not commercially exploit Output that has not been downloaded by you through an approved channel" (S077).
  3. **Official download channels only.** "Obtaining a copy of an Output by any means other than a download channel made available by Suno is prohibited", with recording and stream ripping given as examples (S077).
  4. **Download before you cancel.** Rights in downloads you have already obtained are perpetual and survive expiry, cancellation, downgrade or suspension (S077).
  5. **No retroactive upgrade.** Nothing in Suno's terms makes free-tier outputs commercial after you upgrade (S077).
  6. **Remixes.** A Suno Remix is jointly owned and usable only for personal, non-commercial purposes "regardless of your subscription tier". "Nothing in this paragraph permits commercial use of any Remix" (S077).
  7. **Accepting new terms.** If you don't accept revised Suno terms, you must close your account before your renewal date or within 30 days of the effective date, whichever comes first (S077).
  8. **Keep an asset log.** For each asset, record the tool, plan, date and how you obtained it. Suno may embed metadata showing the service tier and whether an output was a permitted Download, so your log should match what the file says (S077; rights-and-disclosure.json #08, #09).
  9. **Know your recourse.** Suno's liability is capped at the greater of $100 or what you paid in the last six months. Most disputes go to individual JAMS arbitration (S077).

- **You vs the agent (as of 2026-10-12):**
  - **The agent** can fetch today's terms page, quote the commercial-use clause with its date, and keep the asset log as files are generated. All of this can be checked against the page and the files.
  - **What the agent cannot see:** your plan history or download quota, unless you give it access (rights-and-disclosure.json #08, #09). Its memory of the terms is out of date after revisions like these.
  - **The human** picks the plan, downloads through the official button, and decides what to sell.
  - **Bring in an expert:** an IP lawyer for a distribution deal or a dispute over an AI track (rights-and-disclosure.json #10).

- **Currency:** New in 2026. Suno's terms took effect on 2026-09-03 and ElevenLabs' were updated on 2026-10-09 (S077, SG12-07). What is changing now: Suno's per-tier download limits "may be updated from time to time" (S077).

- **Outdated framings to avoid:**
  - "Anything I make on a free AI tool is mine to sell." See S077 and SG12-07.
  - "Upgrading later makes my old songs commercial." See S077.
  - "My subscription covers every song I generated." Only permitted downloads count (S077).
  - "I can record the stream instead of downloading it." This is prohibited (S077).
  - "Premier lets me monetise anything, including remixes." Remixes are never commercial (S077).

- **Questions it answers (batch reader, rights-and-disclosure.json #08, #09, #11):**
  - "Can I monetise a Suno song I made on the free plan?"
  - "If I upgrade, are my old songs covered?"
  - "Do I lose rights if I cancel Suno?"
  - "Why does it matter whether I download the song?"
  - "How many songs can I use commercially per month?"
  - "Can I release a remix of someone's Suno song? Who owns a remix?"

- **Show it for real:**
  - In Suno, show the download counter on the account page, download one track with the official button, and add a log line recording file, date, plan and channel (#09; S077).
  - Show Suno's remix toggle next to the Remix clause (#11).
  - Show ElevenLabs' terms, Section 1(c), next to its plan page (SG12-07).
  - Show the asset log itself as a small CSV kept beside the media folder (#08, #09).

- **Priority:** must.
  - Evidence: 3 batch items (2 high severity), now backed by two primary contracts (S077, SG12-07), both revised within the last nine weeks.
  - Stakes: money and lost rights are directly at stake, and the habit of checking the live terms carries over to every generator.

---

### C114 Purely AI-made work has no US copyright

- **In one line:** A tool may hand you its rights, but it promises no copyright, and outputs may not be unique. In the US, only human creative contribution is protected, and that contribution must exist, be documented, and be disclosed if you register.

- **Why it is a gap:**
  - **People confuse the tool's grant with copyright.**
    - Suno "makes no representation or warranty to you that any copyright will vest in any Output" (S077).
    - ElevenLabs says "you retain all rights in and to your Output", but its terms do not address whether outputs can be copyrighted (SG12-07).
  - **Outputs are not unique.** Both tools say output "may not be unique across users" (S077, SG12-07). Someone else can receive the same or a similar song or line, and you have no copyright to stop them.
  - **The question is settled for now.** The Supreme Court denied certiorari in *Thaler v. Perlmutter* on 2026-03-02, leaving the human-authorship requirement in place (SG12-01).

- **What to teach (specific points):**
  1. **Human authorship is required.** "Copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements" (SG12-03). The D.C. Circuit's holding stands after the 2026-03-02 cert denial (SG12-01).
  2. **Prompts are not enough.** "Based on the functioning of current generally available technology, prompts do not alone provide sufficient control" (SG12-03).
  3. **What can be protected.**
     - Your own expressive inputs that are perceptible in the output, such as your drawing or your lyrics.
     - Your "creative selection, coordination, or arrangement" of material.
     - Your creative modifications of outputs.
     - Using AI "to assist rather than stand in for human creativity" does not affect protection (SG12-03).
     - The Copyright Office has registered "hundreds" of works that include AI (SG12-01).
  4. **Decided case by case, and still being litigated.** *Allen v. Perlmutter* (D. Colo., filed 2024-09-26) is examining how much prompting or post-generation editing is enough (SG12-01, SG12-03).
  5. **Registering a work with AI content:**
     - Applicants "have a duty to disclose the inclusion of AI-generated content".
     - Describe the human contribution in "Author Created".
     - Explicitly exclude AI material that is more than de minimis under "Limitation of the Claim", then "Material Excluded".
     - Never list the AI tool or its company as an author.
     - If an existing registration hid AI material, fix it with a supplementary registration. Otherwise you risk cancellation, or a court disregarding the registration (SG12-04).
  6. **Document as you go.** Keep the prompts, record when and how AI was used, name a human author, and keep an attribution and ownership policy (SG12-01).
  7. **The licence still binds.** No copyright does not mean free for anyone to use. The tool's terms, such as free-tier non-commercial limits, still govern what you do with the output (S077, SG12-07; rights-and-disclosure.json #10).
  8. **Other countries differ.** As of January 2025, the Copyright Office reported:
     - a Beijing Internet Court ruling that protected an image made with over 150 prompts plus later edits;
     - an EU member-state consensus that significant human input is required;
     - a UK statute protecting "computer-generated" works whose application to AI is unclear (SG12-03).

     None of this was re-checked for 2026.

- **You vs the agent (as of 2026-10-12):**
  - **The agent** can keep a provenance log automatically: prompts, versions, the edits a human made, and timestamps (rights-and-disclosure.json #10). It can draft the "Author Created" and "Material Excluded" wording from that log (SG12-04 gives the format).
  - **What the agent cannot do:** make the creative contribution, or decide whether yours is enough. That is a case-by-case legal judgement (SG12-03).
  - **The human** makes and keeps evidence of real creative choices (lyrics, arrangement, edits).
  - **Bring in an expert:** an IP lawyer before registering a valuable work or entering a dispute (rights-and-disclosure.json #10).

- **Currency:** The core rule is established.
  - The Copyright Office Part 2 report (January 2025) and the registration guidance (2023-03-16) are foundational and still current. On 2026-10-12, copyright.gov/ai listed no update after May 2025 (SG12-03, SG12-04).
  - New in 2026: the cert denial on 2026-03-02 (SG12-01).
  - Still changing: *Allen v. Perlmutter*, and the Office's promise to issue "additional registration guidance" and update the Compendium (SG12-01, SG12-03).

- **Outdated framings to avoid:**
  - "If the tool assigns me the output, I own the copyright." See S077 and SG12-03.
  - "My AI song is unique to me." See S077 and SG12-07.
  - "AI output is automatically public domain, so licence terms don't matter." See S077.
  - "A detailed enough prompt makes me the author." See SG12-03.
  - "The Supreme Court will settle this soon." It declined (SG12-01).

- **Questions it answers (batch reader, rights-and-disclosure.json #10):**
  - "Can I copyright an AI-generated song or image?"
  - "Can someone else get the same song as me?"
  - "What should I save to prove I authored it?"

- **Show it for real:**
  - Show a project folder holding the prompt history, the raw output, the human-edited version and a provenance log, plus a diff between raw and edited (#10).
  - Walk through the Copyright Office Standard Application fields "Author Created" and "Limitation of the Claim > Material Excluded", with the guidance's sample wording "[description of content] generated by artificial intelligence" (SG12-04).

- **Priority:** must.
  - Evidence: high severity, now backed by 5 sources (S077, SG12-01, SG12-03, SG12-04, SG12-07).
  - Recency: the US position was settled in March 2026, and both tools' terms are from August to October 2026.
  - Reach: it affects every creator who wants to sell or protect AI-assisted work.

---

### C115 Voice and likeness need consent

- **In one line:** Get explicit written consent before cloning anyone's voice or face.
  - Eight US states already regulate digital replicas.
  - A pending federal bill would cover everyone's voice and face.
  - The tools themselves forbid cloning without consent.
  - Uploading your own voice can grant the tool a perpetual, irrevocable licence.

- **Why it is a gap:**
  - **"Only celebrities" and "a label fixes it" are both wrong.** People treat publicity rights as a celebrity matter. The proposed federal right "would extend broadly to all individuals", including employees, students and private citizens. The source gives no support for a label or disclaimer as a defence (S078).
  - **"There is no law yet" is wrong.** Eight states already have AI digital-replica laws (S078).
  - **Uploading your own voice gives a lot away.** Suno takes a "perpetual, irrevocable" licence that "includes a license to your likeness, voice rights and other indicia of your persona" (S077). ElevenLabs' licence is "perpetual and irrevocable" (SG12-07). The batch reader notes that creators read only the "you own your output" line (rights-and-disclosure.json #13).
  - **The tool's consent checkbox puts the liability on you.** You warrant that you hold the rights and consents, and with Suno you also indemnify the company (S077, SG12-07).

- **What to teach (specific points):**
  1. **The tools require consent.**
     - ElevenLabs bans cloning, synthesising or impersonating a living person's voice, identity or likeness "without their explicit and informed consent or other valid authorization".
     - It bans any voice or avatar using a real minor's likeness, and impersonating "political candidates or elected officials without authorization" (SG12-08).
     - Suno allows a Voice Model "resembling your own voice" only (S077).
  2. **You carry the liability.** On Suno, you warrant that you hold all rights and consents, and you indemnify Suno (S077). On ElevenLabs, you must hold all rights needed for your input and output (SG12-07, Section 4(g)).
  3. **State law already applies.** Tennessee, California, Illinois, New York, Utah, Arkansas, Montana and Washington have AI digital-replica laws, and they differ from one another (S078).
  4. **Builders face tool liability.** Tennessee's ELVIS Act (2024) creates a private right of action against anyone who distributes or makes available technology whose primary purpose is producing an identifiable person's voice or likeness without consent (S078).
  5. **Ads.** New York S.8420A (signed December 2025) requires conspicuous disclosure when an ad includes a "synthetic performer" (S078).
  6. **NO FAKES Act (pending).**
     - It was unanimously advanced by the Senate Judiciary Committee on 2026-06-22. It is not law, and "a long path remains before the bill becomes law".
     - It would create a federal right over everyone's voice and visual likeness in digital replicas, with statutory damages of $5,000 to $25,000 per violating replica.
     - It includes notice-and-takedown for online services, so a platform can remove your video on notice.
     - Named exclusions: news, documentaries, parody, satire, criticism, commentary and scholarship (S078).
  7. **What you grant when you upload your own voice.**
     - Suno takes a perpetual, irrevocable, sublicensable licence covering your likeness and voice, uses it to improve its AI models, and you waive moral rights (S077).
     - ElevenLabs takes a perpetual, irrevocable licence to your content, including voice recordings, but "will not commercialize your voice on a standalone basis without your permission".
     - On ElevenLabs you can opt out of training use at any time, and you can request deletion of your voice models (SG12-07).
  8. **Process for anything public-facing.**
     - Inventory the tools that process voices or faces.
     - Set a policy on whose likeness may be used.
     - Review vendor contracts for how likeness data is used.
     - Add human review, with consent procedures, before publishing content that shows identifiable people (S078).
     - Keep the signed consent with the project files (rights-and-disclosure.json #15).
  9. **EU disclosure still applies.** In the EU, a realistic clone of a real person is also a deepfake that needs the C111 disclosure. Consent does not replace the label (S076).

- **You vs the agent (as of 2026-10-12):**
  - **What the agent cannot verify:** consent. It is a fact about the world, and a tool's "I have permission" checkbox records your claim, not the other person's agreement (SG12-08, S077; rights-and-disclosure.json #15).
  - **The agent** can draft a consent form, file it beside the assets, and summarise a tool's licence clauses before you upload.
  - **The human** obtains written consent, decides about public figures, and reads the licence and indemnity clauses before uploading anyone's voice, including their own.
  - **Bring in an expert:** a lawyer for commercial use, public figures, political content, and any app that generates likenesses, because of ELVIS-style tool liability (S078; rights-and-disclosure.json #16).

- **Currency:**
  - State laws are established (ELVIS Act 2024; New York S.8420A signed December 2025) (S078).
  - NO FAKES is speculation: pending as of 2026-08-20 (S078).
  - Tool rules are new: ElevenLabs' policy and terms were updated on 2026-10-09 (SG12-07, SG12-08), and Suno's terms took effect on 2026-09-03 (S077).

- **Outdated framings to avoid:**
  - "Right of publicity only protects celebrities." See S078.
  - "There is no AI likeness law in the US yet." See S078.
  - "The NO FAKES Act is already law." See S078.
  - "Labelling a deepfake makes it legal." The source gives no support for this (S078).
  - "Uploading my voice to train a model is private and revocable." Both licences are perpetual and irrevocable (S077, SG12-07).

- **Questions it answers (batch reader, rights-and-disclosure.json #13, #15, #16):**
  - "Can I clone my friend's voice for a video?"
  - "Is a parody deepfake of a politician OK?"
  - "What happens if I use someone's face without asking?"
  - "What does Suno get when I upload my voice?"
  - "Can I make a voice model of a singer I like?"
  - "Do I need to label an AI actor in my ad?"
  - "Can I build an app that makes celebrity voices?"

- **Show it for real:**
  - Show a signed voice-clone consent form stored beside the project files, next to the cloning tool's own consent checkbox (#15).
  - Show ElevenLabs' "Data use" training opt-out and the voice-model deletion request (SG12-07).
  - Highlight Suno's content-licence and Voice Model clauses (#13; S077).
  - Show an ad mock-up with a conspicuous "features a synthetic performer" label (#16; S078).

- **Priority:** must.
  - Evidence: 3 batch items (1 high severity), now backed by S076, S077, S078, SG12-07 and SG12-08, all from August to October 2026.
  - Stakes: the harm falls on other people, damages would be counted per replica, and voice cloning is one click away in tools this audience uses.

---

### C116 Platform rules apply on top of the tool's licence

- **In one line:** Where you publish has its own rules. YouTube removes monetisation from whole channels with too much template-made, distressing or AI-real-person finance, legal or health content, whatever the generator's licence allows. A licence or permission does not exempt reused content.

- **Why it is a gap:**
  - **A licence is not permission to distribute everywhere.** Creators treat the generator's licence that way. Suno's own terms say third-party platform rules apply separately and that "Applicable rights holders may also have the right to collect revenue" (S077).
  - **Mass production is what YouTube names.** Faceless-channel playbooks mass-produce videos. YouTube names low-variation, template content and reviews the channel as a whole (S079, SG12-06).
  - **"AI equals demonetised" is the wrong model.** YouTube says disclosing AI use does not affect "eligibility to earn money". What costs money is inauthentic or repetitive content, distressing content, and AI depictions of real people giving advice (SG12-05, S079).

- **What to teach (specific points):**
  1. **Three independent layers:** the law, the tool's contract and the platform's rules. Any one of them can stop you. A platform refusing your content does not revoke Suno's grant, and Suno's grant does not oblige the platform to accept it (S077).
  2. **YouTube's "inauthentic content" policy** (renamed from "repetitious content"; latest dated update on the page is 2025-07-15):
     - Content that is "repetitive or mass-produced" is not monetisable.
     - So is "AI-generated content made with generic or unoriginal templates giving the impression of mass production".
     - Automated tools are fine, but "the final product must still demonstrate your creative vision" (SG12-06).
  3. **The whole channel is judged.**
     - Reviewers look at the channel's main theme, most-viewed and newest videos, and metadata.
     - Monetisation can be removed from the entire channel, with suspension from the YouTube Partner Program in some cases.
     - Penalties "may apply to all of your existing channels".
     - Creating new channels to evade restrictions "could lead to termination of all channels" (SG12-06).
  4. **July 2026 clarifications** (rolled out 2026-07-16 to all Partner Program members):
     - Template or repetitive content, including tutorials that duplicate what is already common on YouTube.
     - Distressing or manipulative content, such as an animal "rescue". Channels dedicated to it are removed from the Partner Program "regardless of whether the content is AI-generated or not".
     - AI representations of real people discussing finance, legal or health topics.
     - A channel with "too much" of any of the three cannot monetise. No threshold is published (S079).
  5. **Permission doesn't exempt reused content.** Collections of songs from different artists are not monetisable "even if you have their permission", and the reused-content policy "applies even if you have permission from the original creator" (SG12-06).
  6. **Disclosure is separate from monetisation.** YouTube's AI-use disclosure "does not limit a video's audience or affect its eligibility to earn money". Consistently failing to disclose can lead to penalties, including suspension from the Partner Program (SG12-05).
  7. **Other platforms are not covered by these sources.** Read each destination's own AI policy before uploading. TikTok, Meta and Spotify are a known gap in this research (rights-and-disclosure.md).

- **You vs the agent (as of 2026-10-12):**
  - **The agent** can mass-produce variants, and it can read a platform's policy page and check a planned upload against the examples the page lists.
  - **What the agent cannot know:** how a reviewer will weigh the channel mix. It should not be trusted to say a format is "safe" (rights-and-disclosure.json #17, #18).
  - **The human** decides the channel's format, supplies real variation and value in each video, and judges whether the channel as a whole reads as a template farm.
  - **Bring in an expert:** a real, identified human expert should front finance, legal or health content (rights-and-disclosure.json #18).

- **Currency:**
  - The "inauthentic content" rename (2025-07-15) is established within the last 12 months (SG12-06).
  - The July 2026 clarifications are new in 2026 (S079).
  - The GenAI disclosure page is a live page with no date (SG12-05).
  - What is changing: there are no numeric thresholds, and the rules on other platforms are not in these sources.

- **Outdated framings to avoid:**
  - "YouTube demonetises AI videos." The rules target repetitive, distressing or sensitive-persona content, and disclosure does not affect earning (S079, SG12-05).
  - "If I don't use AI, the repetitive rule doesn't apply to me." The template rule names CGI and templates, and the distress rule applies regardless of AI (S079, SG12-06).
  - "Each video is judged alone." The whole channel is judged (SG12-06, S079).
  - "If the AI tool says I can use it commercially, every platform will accept it." See S077.
  - "Permission from the artists makes a compilation monetisable." See SG12-06.

- **Questions it answers:**
  - From the batch reader (rights-and-disclosure.json #14, #17, #18):
    - "Can I monetise an AI faceless channel?"
    - "Will my templated shorts get demonetised?"
    - "Can I run an AI avatar finance channel?"
    - "Why would my whole channel lose monetisation for a few videos?"
    - "Can I put my Suno song on Spotify or YouTube?"
    - "Why did someone else claim revenue on my AI track?"
  - Derived by me from SG12-05: "Will ticking the AI box hurt my earnings?"

- **Show it for real:**
  - Open YouTube Studio's monetisation tab next to the channel monetisation policy page (#18; SG12-06).
  - Show a channel grid of near-identical template thumbnails and titles next to a channel whose videos visibly differ (#17).
  - Show the "AI use" attribute on the upload screen, with YouTube's note that disclosure does not affect earning (SG12-05).
  - Show Suno's third-party platform clause (#14; S077).

- **Priority:** should.
  - Evidence: 3 batch items (2 high severity), now backed by 4 sources (S077, S079, SG12-05, SG12-06) from 2025 and 2026.
  - Reasoning: the stakes are high for people earning from AI video, but the rules are specific to monetising creators, and YouTube is the only platform covered.

---

## Sources

Batch sources. Each was re-opened and re-read on 2026-10-12.

| ID | Title | Author | Date | URL |
|---|---|---|---|---|
| S076 | EU AI Act: Transparency Obligations for AI-Generated Content (Article 50) | Julia Apostle, Orrick | 2026-08-14 | https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50 |
| S077 | Suno Terms of Service | Suno, Inc. | revised 2026-08-10, effective 2026-09-03 | https://suno.com/terms |
| S078 | A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress | Erik Dullea, Evan Yahng (Husch Blackwell) | 2026-08-20 | https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/ |
| S079 | YouTube clarifies policies around AI slop and upsetting videos | Sarah Perez, TechCrunch | 2026-07-20 (rollout 2026-07-16) | https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/ |

Sources added by this agent. Each was fetched and read on 2026-10-12. The IDs are local to this group.

| ID | Title | Author | Date | URL | Note |
|---|---|---|---|---|---|
| SG12-01 | US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works | Zachary Messick, Joshua M. Dalton, Benjamin B. Anger (Morgan Lewis) | 2026-03-06 | https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works | Listed in sources-candidates.md as an "also skim" under S077 |
| SG12-02 | EU AI Act, Articles 50 and 111 (consolidated text with amendment markers) | Future of Life Institute site (artificialintelligenceact.eu) | undated pages | https://artificialintelligenceact.eu/article/50/ ; https://artificialintelligenceact.eu/article/111/ | Art. 50 page: "Comes into force 2 August 2026, according to Article 113". Art. 111(4) is marked "new" and the page does not name the amending act |
| SG12-03 | Copyright and Artificial Intelligence, Part 2: Copyrightability | US Copyright Office | January 2025 | https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf | Foundational and still current: copyright.gov/ai showed no later update (checked 2026-10-12). Executive summary (p. iii) and Conclusion (p. 41) read |
| SG12-04 | Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence (88 Fed. Reg. 16,190) | US Copyright Office | 2023-03-16 | https://www.copyright.gov/ai/ai_policy_guidance.pdf | Foundational and still the policy statement linked from copyright.gov/ai. Section IV read |
| SG12-05 | Disclosing use of GenAI content (YouTube Help) | Google / YouTube | undated (page shows "©2026 Google") | https://support.google.com/youtube/answer/14328491 | Fills the "YouTube's own label" gap flagged in rights-and-disclosure.md |
| SG12-06 | YouTube channel monetization policies (YouTube Help) | Google / YouTube | latest dated update on page 2025-07-15 | https://support.google.com/youtube/answer/1311392 | Primary text behind S079 |
| SG12-07 | ElevenLabs Terms of Use | ElevenLabs | last updated 2026-10-09 | https://elevenlabs.io/terms-of-use | Sections 1(c), 4(b), 4(c), 4(d), 4(g), 4(i), 10 |
| SG12-08 | ElevenLabs Prohibited Use Policy | ElevenLabs | last updated 2026-10-09 | https://elevenlabs.io/use-policy | Consent, minors, political figures, provenance |
| SG12-09 | Anthropic announcement on watermarking Claude's text | Anthropic | 2026-08-14, updated 2026-09-01 | https://www.anthropic.com/news/claude-text-watermark | URL taken from SG12-11's citations |
| SG12-10 | How Claude marks AI-generated content (Claude Help Center) | Anthropic | undated ("Updated this week" on 2026-10-12) | https://support.claude.com/en/articles/16266773 | URL taken from SG12-11's citations |
| SG12-11 | Claude's text is watermarked now, and the mark only lives where Claude had a choice (AO-040) | Aaron Orelup | 2026-10-06 | https://aaronorelup.com/ledger/claude-text-watermark/ | Aaron's ledger. The post says Claude Opus 5.5 drafted it, and it does not claim independent verification of Anthropic's implementation |

Fetched but not usable: https://verify.contentauthenticity.org/ returned only its title ("Content Credentials").
