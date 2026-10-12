---
key: own-it-sell-it-publish-it
id: 09.04
title: Own it, sell it, publish it
district: Beyond Code
module: 09 Facts, media, rights
status: todo
legacy: []
minutes: 12
concepts: [C113, C114, C115, C132, C133]
sources: [S077, S201, S203, S235, S238, S076, S078, S199, S202, S204, S236, S237, S239, S240, S243]
lead: [S203, S077]
---
# Own it, sell it, publish it

**Purpose (the first spoken sentence):** In this lesson you'll learn the three separate questions behind selling or publishing anything AI made for you: what the generator's terms and the model's licence let you do, whether you own it, and whether it takes someone else's voice, face, logo or character.

**Conclusion:** The generator's terms, the model's licence and copyright law each decide something different, so log which tool, plan and model made every asset, get written consent before you use a real person, and bring in an IP lawyer before you sell.

**Where it sits on the map:** District 6 · Beyond Code — What if it isn't software?; module 09 Facts, media, rights (lesson 4 of 4).

**Lead source (audit, 2026-10-12):** S203 (US Copyright Office); S077 (Suno, Inc.). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S077, S201, S203, S235, S238); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length note:** a mid-module lesson runs about 10 minutes; five concepts with legal detail take about 12. Stay under 15 so no guest segment is needed.

**Through-line for the script:** three gates every asset passes, in order. Gate 1, "may I use it this way?" (the generator's terms and the model's licence, both contracts). Gate 2, "do I own it?" (copyright law). Gate 3, "does it take from someone else?" (voices, faces, logos, characters). Passing one gate says nothing about the next (C133 point 6; S077, S203, S238). The asset log is the object that carries the answers through all three.

## What to teach (binding scope)

### C113 Generator terms decide what you can sell
- **Free tiers can be personal use only.** Suno Free and Basic outputs are for "your lawful, personal and non-commercial purposes" (S077); ElevenLabs free users "may only use the Services for non-commercial purposes" (S201, Section 1(c)). Depth: teach.
- **On Suno, the download is what carries commercial rights.** Pro and Premier subscribers may use commercially only outputs downloaded through an approved channel, within a monthly per-tier allowance ("The number of Downloads you are permitted per month depends on your service tier"); getting a copy any other way, stream ripping included, is prohibited (S077). Depth: teach.
- **Download before you cancel; upgrading doesn't reach back; remixes are never commercial.** Rights in downloads you already have are perpetual and survive cancellation or downgrade; nothing in the terms makes free-tier songs commercial after an upgrade; a Remix is jointly owned and personal-use only "regardless of your subscription tier" (S077). Depth: brief.
- **The contracts change under you.** Suno's terms were revised 2026-08-10, effective 2026-09-03; ElevenLabs' were last updated 2026-10-09 (S077, S201). Anything an agent remembers about a tool's terms is probably older than the live page (C024). Depth: teach.
- **Keep an asset log.** For every asset: tool, plan, date and how you obtained it. Suno may embed metadata showing the tier and whether an output was a permitted download, so the log should match what the file says (S077). Depth: teach; the log grows a column in each section below.
- **Know your recourse.** Suno's liability is capped at the greater of $100 or what you paid in the last six months, and most disputes go to individual arbitration (S077). Depth: one line.

### C132 The model's licence is a second contract
- **Local is not licence-free.** The licence travels with the weights you download (S235). Depth: teach.
- **The model and its outputs are licensed separately.** FLUX.1 [dev] (Non-Commercial License v1.1.1) says use "for revenue-generating activity" or "in direct interactions with or that has impact on end users" is not a non-commercial purpose, yet "You may use Output for any purpose (including for commercial purposes)" (S235). So selling images you generated can be allowed while running the same model inside a paid app or client service is not. Depth: teach.
- **Fine-tunes and LoRAs inherit the licence, and outputs may not train a rival.** "Any restrictions set forth herein regarding the FLUX.1 [dev] Model also apply to any Derivative you create"; "You may not use the Output to train, fine-tune or distill a model that is competitive with the FLUX.1 [dev] Model" (S235). LTX-2's licence covers derivatives, fine-tuned weights included (S236). Depth: brief.
- **Some licences switch on with revenue.** Under the LTX-2 Community License (2026-01-05) entities with at least $10,000,000 annual revenue need a paid commercial licence (S236). The MiniMax H3 Community License (2026-08-02) requires prior written authorisation above $20 million a year and that commercial products display "MiniMax H3" in their interface (proposed source P4). Depth: brief.
- **Each version has its own terms.** Qwen-Image (released 2025-08-04) is Apache 2.0 (S237), but Qwen-Image 2.1 (released 2026-09-20) is under the Qwen Research License Agreement: non-commercial means "for research or evaluation purposes only", commercial use needs a separate licence, and the agreement does not say whether generated images may be used commercially (proposed source P3). FLUX.2 [dev] points commercial users to separate terms its page doesn't describe (S235). Depth: teach; "same family, same licence" is the trap. Where a licence is silent, that is a question for a lawyer, not a yes.
- **A licence can depend on where you are.** The MiniMax H3 Community License excludes the European Union, the United Kingdom, South Korea and the United States, and in those places "You may not use, reproduce, modify, distribute, or display the MiniMax H3 Works or any of their Outputs" (proposed source P4). Depth: teach; it surprises people because the model downloads and runs anywhere.

### C114 Purely AI-made work has no US copyright
- **Human authorship is required.** "Copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements" (S203). The Supreme Court declined to hear Thaler v. Perlmutter on 2026-03-02, so that stands (S202). Depth: teach.
- **Prompts alone are not enough.** "Based on the functioning of current generally available technology, prompts do not alone provide sufficient control" (S203). Depth: teach.
- **What can be protected.** Your own expressive inputs that show in the output (your drawing, your lyrics), your "creative selection, coordination, or arrangement", and your creative changes to outputs; using AI "to assist rather than stand in for human creativity" does not affect protection (S203). The Office has registered "hundreds" of works that include AI, and Allen v. Perlmutter is testing how much prompting or editing is enough (S202). Depth: teach.
- **The tool's grant is not copyright, and your output may not be unique.** Suno "makes no representation or warranty to you that any copyright will vest in any Output"; both Suno and ElevenLabs say outputs may not be unique across users (S077, S201). Someone else can get the same song, and without copyright you can't stop them. Depth: teach.
- **No copyright doesn't mean free for anyone.** The tool's terms still govern what you may do with the output (S077, S201). Depth: brief.
- **Registering a work that includes AI.** Disclose the AI content, describe your contribution under "Author Created", exclude more-than-trivial AI material under "Limitation of the Claim" then "Material Excluded", never list the AI or its company as an author, and fix an older registration with a supplementary one (S204). Document as you go: prompts, when and how AI was used, a named human author (S202). Depth: brief; the asset log gains a "human contribution" column.
- **Other countries differ.** As of January 2025 the Copyright Office reported a Beijing court protecting an image made with over 150 prompts plus edits, an EU consensus that significant human input is required, and a UK statute whose reach is unclear; none of this was re-checked for 2026 (S203). Depth: one line, hedged.

### C115 Voice and likeness need consent
- **The tools require consent.** ElevenLabs bans cloning or impersonating a living person's voice or likeness "without their explicit and informed consent or other valid authorization", any voice or avatar of a real minor, and impersonating political candidates or officials without authorisation (S199); Suno allows a voice model of your own voice only (S077). Depth: teach.
- **The checkbox puts the liability on you.** On Suno you warrant you hold every right and consent and you indemnify the company (S077); on ElevenLabs you may not create output you lack the rights for (S201, Section 4(g)). Depth: brief.
- **US law already applies, and it isn't only for celebrities.** Tennessee, California, Illinois, New York, Utah, Arkansas, Montana and Washington have AI digital-replica laws that differ from one another; Tennessee's ELVIS Act gives a right of action against anyone who distributes technology whose primary purpose is producing an identifiable person's voice or likeness without consent; New York's S.8420A requires disclosing a "synthetic performer" in an ad. The federal NO FAKES Act, advanced by the Senate Judiciary Committee on 2026-06-22, is pending, not law: it would cover everyone's voice and face, with $5,000 to $25,000 per violating replica and notice-and-takedown (S078). Depth: brief; mark NO FAKES as pending on screen.
- **Uploading your own voice gives a lot away.** Suno takes a perpetual, irrevocable licence that "includes a license to your likeness, voice rights and other indicia of your persona" (S077). ElevenLabs' licence over your content, voice recordings included, is "perpetual and irrevocable", though it "will not commercialize your voice on a standalone basis without your permission", and you can opt out of training and ask to delete your voice models (S201). Depth: teach.
- **Process for anything public.** Decide whose likeness may be used, review the tool's licence clauses, get written consent and keep the signed form with the project files, and have a person review before publishing anyone identifiable (S078). Depth: brief. In the EU, a realistic clone of a real person also needs a deepfake label: consent does not replace the label (S076; taught in 09.03). Depth: one line.

### C133 Owning it is not the same as being allowed to publish it
- **A generator can put someone else's mark in your image.** In Getty Images v Stability AI ([2025] EWHC 2863 (Ch), 2025-11-04) the High Court found trade mark infringement where generated images carried iStock and Getty Images watermarks; the findings are narrow, and the judge said it is impossible to know how many such watermarks were generated in real life (S238). Depth: teach.
- **The model is not the copy, in UK law so far, and training is unsettled.** The same judgment held that a model which does not store or reproduce the works is not an "infringing copy"; Getty dropped its training claim for lack of evidence the training happened in the UK (S238). The US Copyright Office's report on generative-AI training is still a pre-publication version (2025-05-09) (S240). Depth: one line.
- **Passing the generator's filter is not clearance.** Higgsfield hard-rejects prompts naming real brands and people with `ip_detected`, which catches some IP, not all (S243). Depth: brief.
- **Stores make the promise yours.** Steam: "you promise Valve that your game will not include illegal or infringing content", and it evaluates AI-generated content the same way as any other (S239). Depth: brief.
- **The three gates, said once more.** Does the tool's licence let me use it this way (C113, C132)? Do I own it (C114)? Does it infringe anyone (C115, C133)? Depth: teach, as the closing frame.

## You vs the agent
As of 2026-10-12:
- **The agent does on its own:** fetches today's terms page and the model's LICENSE file, quotes the commercial-use, output, territory, revenue and derivative clauses with their dates, and records model, version and licence in the asset log; keeps the log as files are made (tool, plan, date, download channel, prompts, seeds, the human's edits); drafts the "Author Created" and "Material Excluded" wording from that log; drafts a consent form and files the signed copy beside the assets; summarises a tool's licence and indemnity before you upload a voice; scans outputs for text, logos and watermarks and flags close matches to brands or characters you name (S077, S201, S204, S235).
- **It can't:** see your plan history or download allowance unless you give it access; know where you live or will sell (the territory question); decide whether your creative contribution is enough, which is a legal judgment made case by case (S203); verify consent, which is a fact about the world (a tool's checkbox records your claim, not the other person's agreement) (S199, S077); or judge whether an image evokes a franchise or a character.
- **You decide and check:** the plan, and downloading through the official button; what you sell, where, and as what product; making and keeping evidence of your real creative choices; getting written consent; judging resemblance to known characters and brands; reading the licence and indemnity before uploading anyone's voice, your own included.
- **You bring in an expert:** an IP lawyer before selling or registering a valuable work, before a distribution deal or a dispute, before building a product or client service on a model with a non-commercial, research-only, revenue-threshold or territory-restricted licence, for any commercial use of a real person's likeness or any app that generates likenesses (ELVIS-style tool liability), and before a commercial release that evokes a franchise, a character or a brand (S077, S203, S235, S078, S238). How to brief one is taught in 04.04.

## Sources this lesson is built from
- S077 — Suno, Inc., "Suno Terms of Service" (revised 2026-08-10, effective 2026-09-03) https://suno.com/terms — free vs paid tiers, the download rule, remixes, no copyright warranty, non-unique outputs, the voice-model licence, platform revenue claims; re-read 2026-10-12.
- S201 — ElevenLabs, "Terms of Use" (last updated 2026-10-09) https://elevenlabs.io/terms-of-use — non-commercial free tier, who holds outputs, the perpetual licence over your voice, training opt-out and voice-model deletion; re-read 2026-10-12.
- S203 — US Copyright Office, "Copyright and Artificial Intelligence, Part 2: Copyrightability" (January 2025; foundational and still current, no later update on copyright.gov/ai as of 2026-10-12) https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf — human authorship, prompts not enough, what can be protected.
- S235 — Black Forest Labs, "FLUX.1 [dev] Non-Commercial License v1.1.1" and the FLUX.2 [dev] model card (licence undated, unchanged for over a year and current; read 2026-10-12) https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md ; https://huggingface.co/black-forest-labs/FLUX.2-dev — model vs output licensing, derivatives, no training competitors; licence re-read 2026-10-12.
- S238 — High Court of England and Wales (Mrs Justice Joanna Smith DBE), "Getty Images v Stability AI [2025] EWHC 2863 (Ch)" (2025-11-04; appeal status not checked) https://www.judiciary.uk/judgments/getty-images-v-stability-ai/ — watermarks in outputs as trade mark infringement, the model not an infringing copy, the dropped training claim.

Also cited for single points (credit on the lesson page):
- S202 — Zachary Messick, Joshua M. Dalton, Benjamin B. Anger (Morgan Lewis), "US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works" (2026-03-06) https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works
- S204 — US Copyright Office, "Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence" (2023-03-16; foundational and still the linked policy) https://www.copyright.gov/ai/ai_policy_guidance.pdf
- S236 — Lightricks, "LTX-2 Community License Agreement" (2026-01-05) https://huggingface.co/Lightricks/LTX-2/blob/main/LICENSE
- S237 — Qwen (Alibaba), "Qwen-Image" model card (released 2025-08-04; licence still current on the page) https://huggingface.co/Qwen/Qwen-Image
- S199 — ElevenLabs, "Prohibited Use Policy" (last updated 2026-10-09) https://elevenlabs.io/use-policy
- S078 — Erik Dullea, Evan Yahng (Husch Blackwell), "A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress" (2026-08-20) https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/
- S076 — Julia Apostle, Orrick, "EU AI Act: Transparency Obligations for AI-Generated Content (Article 50)" (2026-08-14) https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50
- S239 — Valve, "Content Survey" (Steamworks documentation, undated live docs) https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- S240 — US Copyright Office, "Copyright and Artificial Intelligence" landing page (undated; Part 3 pre-publication 2025-05-09) https://www.copyright.gov/ai/
- S243 — Aaron Orelup, Higgsfield notes (`references/higgsfield.md`, 2026-09-21 to 2026-09-27; local file, not public) — `ip_detected` refusals.

Proposed new sources (fetched and read 2026-10-12 for this spec; not yet in sources.md, so add them before the lesson is made or drop the points that rest on them):
- P3 — Qwen (Alibaba), "Qwen RESEARCH LICENSE AGREEMENT" for Qwen-Image-2.1 (release date 2026-09-20) https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE ; model card https://huggingface.co/Qwen/Qwen-Image-2.1 (licence tag "qwen-research") — research-or-evaluation-only use, separate commercial licence, outputs not addressed.
- P4 — MiniMax, "MiniMax H3 COMMUNITY LICENSE AGREEMENT" (2026-08-02) https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE — excluded territories (EU, UK, South Korea, US) for the model and its outputs (Sections I.5, V.4), the $20 million authorisation threshold and "MiniMax H3" display rule (Section IV), "MiniMax claims no rights over the Outputs you generate" (Section VI.4).

Recency: S077, S201, S199, S078, S076, P3 and P4 are from the last three months; S202, S236 and S238 are within twelve months; S203 and S204 are foundational and still current; S235, S239 and S240 are live pages read on 2026-10-12. The batch readers found no beginner threads on media rights, and no study measures how often creators get these rules wrong. Disney and Universal's suit against Midjourney was not read and must not be mentioned. All law here is US, UK or EU; the lesson is teaching notes, not legal advice, and should say so once.

## Show it for real
- Suno's account page with the monthly download counter, one track downloaded with the official button, and a log line added (file, date, plan, channel) (S077): proves the download is the commercial event. Crop the account name, e-mail and billing.
- Suno's remix toggle beside the Remix clause (S077): proves a remix never sells.
- ElevenLabs' terms Section 1(c) beside its plan page, then the "Data use" training opt-out and the voice-model deletion option (S201): proves free is non-commercial and your voice licence is broad.
- FLUX.1 [dev]'s LICENSE.md with the non-commercial definition and section 2(d) highlighted side by side (S235): proves model and outputs are licensed separately.
- The Qwen-Image model card (Apache 2.0) beside the Qwen-Image-2.1 card (qwen-research) (S237, P3): proves one family can change licence between versions.
- The MiniMax H3 licence's Excluded Territories definition and Section V.4 (P4): proves a licence can depend on where you are.
- The asset log as a small CSV beside a media folder, gaining columns through the lesson: tool, plan, model, version, licence, date, channel, prompt file, human edits, consent file (S077, S202, S235): proves the habit.
- The Copyright Office Standard Application's "Author Created" and "Limitation of the Claim > Material Excluded" fields with the guidance's sample wording, filled in from the log, never submitted (S204): proves how human authorship is claimed.
- A signed voice-clone consent form for a fictional person, stored beside the project files, next to the cloning tool's own consent checkbox (S199, S077): proves the checkbox is your claim, the form is their agreement.
- A generator refusing a prompt that names a real brand (`ip_detected`), then an output the filter passed with stray logo-like text, flagged by the agent's scan (S243): proves the filter is not clearance.
- Steam's content survey promise beside the asset log (S239): proves the promise is yours.
- This lesson must practise what it teaches: before any generated output appears on screen, record its tool, plan and model licence in the lesson's own asset log, and leave out outputs from models whose licence restricts display or non-research use unless Aaron has decided that piece.

## Questions this lesson answers
From the research crew's batch reader (`research/notes/rights-and-disclosure.json` #08-#11, #13, #15, #16) and some derived from the licences and marked so; no beginner forum threads were collected for media rights yet.
- Can I monetise a Suno song I made on the free plan? If I upgrade, are my old songs covered? Do I lose rights if I cancel?
- Why does it matter whether I download the song? How many songs can I use commercially per month?
- Can I release a remix of someone's Suno song? Who owns a remix?
- Can I copyright an AI-generated song or image? Can someone else get the same song as me? What should I save to prove I authored it?
- Can I clone my friend's voice for a video? Can I make a voice model of a singer I like? What does Suno get when I upload my voice?
- Is a parody deepfake of a politician OK? Can I build an app that makes celebrity voices?
- Can I sell images I made with Flux dev? Can I use Flux dev in my paid app? Does my LoRA fall under the base model's licence? (derived from S235)
- The new version of the model I use: is it still free for commercial use? Can I use a model's output where I live? (derived from P3, P4)
- Can I sell AI art that looks like a famous character? Why did my generator refuse a brand name? Am I liable if my image has someone's logo in it? (derived from S238, S243, S239)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Labelling clones and deepfakes, and platform rules on top of the licence → labelling-ai-media
- Local media models, what they are and what they cost → making-media-with-ai
- The model's knowledge has a date (why its memory of the terms is stale) → the-hidden-curriculum
- What to hand an expert and what you get back → before-you-ship-who-signs-off
- Your users' personal data and the law → test-it-as-a-stranger
- The accounts your work depends on, and who owns them → every-automation-runs-as-someone
- Open-source licences for code, and code that matches public code → deep-dive backlog ("Code licences and matching public code"; named in after-launch-keep-it-alive)
- Game storefronts and creator monetisation in depth → deep-dive backlog (curriculum-draft.md)

## Out-of-date framings to avoid
- "Anything I make on a free AI tool is mine to sell" (S077, S201).
- "Upgrading later makes my old songs commercial" and "my subscription covers every song I generated" (S077).
- "I can record the stream instead of downloading it" (S077).
- "Premier lets me monetise anything, remixes included" (S077).
- "If the tool assigns me the output, I own the copyright" and "a detailed enough prompt makes me the author" (S077, S203).
- "My AI song is unique to me" (S077, S201).
- "AI output is public domain, so licence terms don't matter" (S077).
- "The Supreme Court will settle this soon." It declined (S202).
- "Open weights means free for anything" and "if I can download it, I can build a paid product on it" (S235, S236).
- "A LoRA I trained is mine alone" (S235, S236).
- "Same model family, same licence" (S237, P3) and "a licence applies the same everywhere" (P4).
- "Right of publicity only protects celebrities", "there is no AI likeness law in the US yet" and "the NO FAKES Act is already law" (S078).
- "Labelling a deepfake makes it legal" (S078) and "uploading my voice is private and revocable" (S077, S201).
- "If the generator let me make it, I can publish it" and "if I own the output, nobody can object to it" (S243, S239, S238).
- "The courts have settled whether AI training is legal" (S238, S240).

## Legacy notes
No published lesson covers this slot. Nothing here was taught in the legacy lessons.
