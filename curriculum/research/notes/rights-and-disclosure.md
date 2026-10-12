# Research notes: rights and disclosure (publishing AI-made media)

Batch: read-rights-and-disclosure. Read on 2026-10-12. Theme: what creators must know before publishing AI-made media (disclosure law, ownership, likeness, platform rules).

Method note: every source below was fetched with WebFetch and read section by section (several passes with targeted questions per source). The shared web-search budget for this run was used up before I could run extra searches. As a result, the AI Act application dates were checked against the regulation text on artificialintelligenceact.eu (Articles 50, 111 and 113), fetched directly. They were not checked against a second commentary.

Supporting primary text used (not a numbered source):
- EU AI Act, Article 50, Article 111 and Article 113, consolidated text with amendments marked, Future of Life Institute site. Pages are undated, but they show "amended"/"new" markers. URLs: https://artificialintelligenceact.eu/article/50/ , https://artificialintelligenceact.eu/article/111/ , https://artificialintelligenceact.eu/article/113/ . Article 113: the Regulation "shall apply from 2 August 2026" (the general date; Chapter IV, which holds Article 50, is not among the exceptions). The Article 50 page says it applies from 2 August 2026. Article 111(4), marked "new": providers whose generative systems were placed on the market before 2 August 2026 have until 2 December 2026 to comply with Article 50(2).

---

## S076: EU AI Act, Transparency Obligations for AI-Generated Content (Article 50)

- Author: Julia Apostle (Partner, Orrick, Paris)
- Date: 2026-08-14 (confirmed: page shows "August.14.2026", 15-minute read)
- URL: https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50

Summary: This is a practitioner's map of Article 50(2), 50(4) and 50(5), read together with the Commission's non-binding Guidelines (dated 20 July 2026) and the voluntary Code of Practice. Two parties carry duties. Providers of generative systems must make outputs machine-readable and detectable as AI (the Code expects signed metadata plus an imperceptible watermark). Deployers who publish deepfakes, or AI text on matters of public interest, must disclose it visibly. The article sets out exactly where and how that disclosure must appear and what does not count. Artistic and satirical work gets a lighter duty but no exemption.

Corrections to the brief:
- The article explicitly says it does not cover "personal use exemptions". The only place it touches them is the deployer definition (Art. 3(4)): a deployer is anyone using a system under its authority, "except where the AI system is used in the course of a personal non-professional activity". "Authority" means assuming responsibility for the decision to deploy, and technical control is not required. A creator who publishes with a third-party tool in a professional capacity is therefore a deployer. The article does not use the phrase "commercial creators".
- The article does not state when the duties apply. From the regulation text, Article 50 applies from 2 August 2026. Providers whose systems were already on the market have until 2 December 2026 for the 50(2) marking duty (Art. 111(4)). The article's only forward date is 2 February 2027, the target for an interoperable detection solution.

Gaps it shows:
1. **The tool's watermark is not your disclosure.** Article 50(2) (the provider marks machine-readable) and Article 50(4) (the deployer discloses visibly) are separate duties held by different parties. A generator that embeds metadata does not discharge the publisher's duty to label.
2. **What legally counts as a deepfake.** It is AI-generated or manipulated image, audio or video that resembles existing persons, objects, places, entities or events and would falsely appear authentic or truthful. Text is not covered by the deepfake definition; it has its own rule.
3. **Where the label must sit.**
   - It must be clear and distinguishable, at the latest at first exposure, with no intervening overlay, shown long enough to read, and accessible.
   - For video, it goes at the start, after interruptions and at regular intervals.
   - End credits alone, a line in the terms and conditions, a hidden menu, or anything that needs the viewer to click or use a tool all fail.
   - The EU icons ("AI GENERATED", "AI MODIFIED") are optional, but labelling is not, and using the icon does not by itself prove compliance.
4. **Audio needs a spoken disclaimer.** An audio deepfake needs a short, plain-language audible disclaimer at the beginning. Long-form or live audio also needs reminders at regular intervals and after interruptions, plus a visual disclosure where a screen exists. Content that people see at different times (live broadcasts) should be disclosed again later or persistently.
5. **The art and satire carve-out is a lighter duty, not an exemption.**
   - The work must evidently be artistic, creative, satirical, fictional or analogous. "Ambiguous content does not qualify", and the categories are read strictly.
   - The duty shrinks to disclosing that AI content exists "in an appropriate manner that does not hamper the display or enjoyment of the work". End credits alone are still not enough.
   - For digital works, an icon next to the frame or in the UI is acceptable. For physical shows, use the entry point, accompanying materials or physical carriers.
6. **AI-written text on matters of public interest.**
   - It must be disclosed unless (a) a competent human did a deliberate, substantive review, with fact-checking as the minimum, and (b) a named natural or legal person holds legal responsibility and their identity and contact details are public.
   - Spell-checking, grammar fixes or automated review do not count as review.
7. **If you build a generator, you are a provider.**
   - Outputs must be marked in a machine-readable way and be detectable. Under the Code of Practice, the current approach is two layers: digitally signed metadata plus an imperceptible watermark. Free-form text can carry only a watermark.
   - Containerised text (PDF, Word, HTML) falls under the same standard.
   - Detection tools should be free and give clear, human-readable results.
   - There is an exemption for assistive "standard editing" that does not substantially alter the input (preparing existing content without changing its meaning, style or intent).
8. **Which documents bind.** The Act binds. The Guidelines are interpretive and not binding. The Code of Practice is voluntary, and following it "does not constitute conclusive evidence of compliance".

Framings it shows are outdated:
- "Put 'made with AI' in the description or credits and you're covered." This fails Article 50(5).
- "Parody and art are exempt." They get a reduced duty, and only when the work is evidently in a listed category.
- "The platform or tool watermark handles it." That is the provider's duty, not the deployer's.

Quotes: "End credits alone do not comply with Article 50(5)." / "ambiguous content does not qualify" (Orrick, 2026-08-14).

---

## S077: Suno Terms of Service

- Author: Suno, Inc.
- Date: last revised 2026-08-10, effective 2026-09-03 (both confirmed on the page)
- URL: https://suno.com/terms

Summary: Suno's revised Terms split rights by tier. Free and Basic outputs are personal and non-commercial only. Pro and Premier subscribers receive Suno's rights in their outputs, but commercial use is allowed only for outputs they obtained through a permitted Download within their tier's monthly allocation. Downloaded rights are perpetual and survive cancellation. Suno does not promise that any copyright exists in an output, warns that outputs may not be unique, makes Remixes non-commercial for everyone, forbids stripping its fingerprints, watermarks or metadata, and takes a perpetual, irrevocable licence to user content, including the voice and likeness in a Voice Model.

Correction to the brief: 2026-09-03 is the Terms' effective date. The permitted-download rule is part of those Terms. The Terms give no download numbers: monthly limits depend on the tier, are shown on the account page, and may change.

Gaps it shows:
1. **The free tier is personal use only.** Free and Basic users may use outputs only for "lawful, personal, non-commercial purposes". The Terms do not say that free-tier outputs become commercial after an upgrade. The Pro/Premier assignment covers outputs generated from your submissions while subscribed.
2. **Commercial rights come from downloading, not from subscribing.**
   - Commercial use requires a permitted Download under your tier's allocation.
   - An output "that has not been downloaded by you through an approved channel" may not be exploited commercially.
   - Getting a copy any other way is prohibited, for example by screen-recording or ripping it.
   - Downloaded rights are perpetual and survive running out of allocation, plan or price changes, cancellation, downgrade or suspension.
3. **No copyright promise, and no uniqueness.** "Suno makes no representation or warranty to you that any copyright will vest in any Output". "Output may not be unique across users", and the service "may generate the same or similar output for a third party."
4. **Remixes are never commercial.** If you turn on remixing, a Remix is a joint work owned equally by you and the Remixer. It may be used only for "lawful, personal and non-commercial purposes, regardless of your subscription tier."
5. **Do not strip the provenance marks.** You agree not to remove, alter, obscure or circumvent any fingerprint, watermark or metadata Suno appends. Suno may use these marks to show the tier and whether an output was a permitted Download, and it may publicly identify output as made with Suno.
6. **What you give Suno.**
   - Suno takes a worldwide, perpetual, irrevocable, sublicensable, royalty-free licence to your content, including your likeness and voice rights embodied in content or a Voice Model.
   - Suno may use your content to improve its products and AI models, and you waive moral rights.
   - A Voice Model may be made only of your own voice. Uploading recordings of another person's voice for that purpose is prohibited.
   - You warrant that you hold rights to all submissions, and you indemnify Suno.
7. **Platforms have their own rules.** Using output on a third-party platform is subject to that platform's terms. A platform refusing your track does not revoke Suno's grant, and "applicable rights holders may also have the right to collect revenue" from distribution there.
8. **Other terms.**
   - Suno may suspend or terminate accounts and remove content at its discretion.
   - Its liability is capped at the greater of $100 or what you paid in the last six months.
   - Disputes go to individual arbitration (JAMS).
   - If you do not accept the new Terms, close your account before renewal or within 30 days of the effective date.

Supplement, Morgan Lewis, "US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works". Authors: Zachary Messick, Joshua M. Dalton, Benjamin B. Anger. Date: 2026-03-06 (confirmed). URL: https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works
- The Supreme Court denied certiorari in Thaler v. Perlmutter (No. 25-449) on 2026-03-02. This leaves in place the D.C. Circuit's 2025 holding that eligible work must be "authored in the first instance by a human being".
- The Copyright Office refuses works with no human author, but it has registered "hundreds" of works that include AI where a human exercised creative control. AI as a tool is treated differently from AI as a substitute.
- The article recommends: a human contributes creatively and is named as author; document when and how AI was used, and keep the prompts; adopt internal policies on attribution, ownership and documentation.
- Open question: how much human input is enough (prompting, editing after generation) is still being litigated. The article does not cover disclaiming AI portions in a registration.

Framings it shows are outdated:
- "I pay for Pro, so I own every song I make." Only permitted Downloads carry commercial rights, Remixes are excluded, and no copyright is promised.
- "AI output is mine or copyrighted automatically." A purely AI-made work has no US copyright.
- "AI output is public domain, so anyone can use it." The licence terms still bind you, and AI-assisted work with human creative control can be registered.

Quotes: "no representation or warranty to you that any copyright will vest in any Output" (Suno Terms, 2026-08-10). "authored in the first instance by a human being" (D.C. Circuit, quoted by Morgan Lewis, 2026-03-06).

---

## S078: A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress

- Authors: Erik Dullea, Evan Yahng (Husch Blackwell, Byte Back blog)
- Date: 2026-08-20 (confirmed)
- URL: https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/

Summary: On 2026-06-22 the Senate Judiciary Committee unanimously advanced the bipartisan NO FAKES Act. The bill would create a federal right to authorize the use of any individual's voice or visual likeness in digital replicas, with a private right of action and statutory damages. Meanwhile, eight states already have AI digital-replica laws that differ from one another. The article advises inventorying likeness-processing tools, writing policies, reviewing vendor contracts, and getting consent and human review for public-facing AI content that depicts identifiable people.

Status as of the article: committee-passed, not law. In the authors' words, "a long path remains before the bill becomes law". No House action is mentioned.

Gaps it shows:
1. **The proposed right covers everyone, not only celebrities.**
   - There would be a federal right over voice and visual likeness in digital replicas for all individuals, not just performers.
   - It reaches unauthorized replicas displayed or distributed to the public, and certain products or services that produce replicas.
   - Statutory damages would be $5,000 to $25,000 for each violative replica.
2. **Platform notice-and-takedown.** Qualifying online services keep safe-harbour protection if they comply after receiving notice of unauthorized replicas. For creators, this means a takedown can arrive even when your use was lawful.
3. **The exclusions are narrow and named.** They are news, public affairs, sports broadcasts, documentaries, parody, satire, criticism, commentary, scholarship, and certain ads for those works. The article does not say whether a label or disclaimer is a defence.
4. **State laws apply now.**
   - Tennessee, California, Illinois, New York, Utah, Arkansas, Montana and Washington have AI digital-replica laws, and they vary.
   - The Tennessee ELVIS Act (2024) gives a private right of action against anyone who distributes a tool whose primary purpose is producing an identifiable person's likeness or voice without consent.
   - New York S.8420A (signed December 2025) requires conspicuous disclosure when an ad includes a "synthetic performer", meaning a digitally created asset made, reproduced or modified by computer.
5. **Preemption is partial.** The bill would preempt some inconsistent state laws, but not state digital-replica laws in effect as of 2025-01-02, nor laws on sexually explicit or election replicas. ELVIS likely survives. New York's law, passed after the cutoff, is a closer question.
6. **Consent and process.**
   - Get consent before generating content that depicts identifiable people.
   - Set policy on when employee, customer, executive or third-party likenesses may be used to train or generate.
   - Check vendor contracts for how likeness data is collected, kept, licensed and used.
   - Add human review before publishing.
   - Copyright, trademark, state privacy and biometric privacy law, unfair competition and employment law still apply.

Framings it shows are outdated:
- "Right of publicity is a celebrity thing." The proposed federal right covers every individual, and state laws already reach tools and ads.
- "NO FAKES is law." It is a committee-passed bill.
- "A deepfake is fine if it is labelled." The article gives no support for a label defence.

Quotes: "statutory damages ranging from $5,000 to $25,000 for each violative replica" / "a long path remains before the bill becomes law" (Dullea and Yahng, 2026-08-20).

---

## S079: YouTube clarifies policies around AI slop and upsetting videos

- Author: Sarah Perez, TechCrunch
- Date: 2026-07-20, 8:23 AM PDT (confirmed). The clarifications rolled out 2026-07-16 for all YouTube Partner Program (YPP) members.
- URL: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/

Summary: YouTube spelled out three kinds of content it will not monetize, building on its July 2025 "inauthentic content" policy:
1. Repetitive or template content with little variation between uploads, easy to mass-produce with AI, CGI or templates.
2. Distressing or manipulative content designed to upset viewers.
3. AI-made representations of real people discussing finance, legal or health topics.

Trust and safety chief Matt Halprin said a channel with "too much" of any of the three cannot monetize. The stated goal is to stop content farming, not AI itself.

Corrections to the brief:
- The article says outright that the rule applies whether or not AI was used only for the distressing category: "Channels dedicated to this content will be removed from YPP, regardless of whether the content is AI-generated or not."
- The template category's examples include CGI and templates, so in practice it is not limited to AI, but the article does not say so in those words.
- The article does not name an "originality-and-value test", gives no numeric threshold, and does not cover appeals, AI disclosure labels or likeness detection.
- The AI persona category is defined as "representations of real people made with AI". A second sentence speaks of "AI personas" in general, so the article is ambiguous about fully fictional personas.

Gaps it shows:
1. **Mass production costs a channel its monetization.** Low-variation uploads from templates, AI or CGI are demonetized. Even tutorials can fall in this category if they reproduce content already common on the platform. The penalty is at channel level ("too much" of a category), not per video.
2. **Engineered distress is out regardless of tool.** An example is an animal in distress that someone then "rescues". Channels dedicated to this are removed from YPP whether or not AI made the content.
3. **AI faces giving advice on sensitive topics.** AI representations of real people discussing finance, legal, health or medical topics are not monetizable.
4. **What is at stake is the Partner Program, not removal.** These are monetization rules. A channel can stay up but lose ad and subscription revenue if it has too much of any category.
5. **The rule targets slop, not AI.** YouTube says AI can enhance creativity and that it wants higher-quality output. The target is content farming.

Framings it shows are outdated:
- "YouTube demonetizes AI videos." The rules target repetitive, distressing or sensitive-persona content.
- "If I don't use AI I'm safe." The distressing rule applies regardless, and the template rule names CGI and templates.
- "Each video is judged alone." Enforcement is at channel level.

Quotes: Halprin, "too much of any of these three types of content" / "regardless of whether the content is AI-generated or not" (TechCrunch, 2026-07-20).

---

## Unreadable
None. All five URLs were fetched and read. The research could not be extended with new searches because the shared web-search budget ran out. Gaps that a later pass should fill from sources (not from memory):
- YouTube's own altered/synthetic content disclosure label rules.
- Other platforms' AI labels (TikTok, Meta, Spotify).
- The current Digital Omnibus status, beyond what the consolidated Act text shows.
