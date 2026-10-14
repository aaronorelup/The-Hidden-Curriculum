# Sources

The Hidden Curriculum is built on other people's hard-won knowledge, not on what an AI assumes needs teaching. Every point in [concepts.md](concepts.md) ends with the IDs of the sources it rests on, and every lesson credits the sources it is built from, by ID in its spec and by name on its page. This file is the list behind those IDs: one entry per source that any concept cites, each one fetched and read by the research crew.

- **IDs.** `S001` to `S085` are the sources the curator picked from 274 candidates (see `research/sources-candidates.md`, which says why each was chosen). `S086` to `S205` were added by the concept writers on 2026-10-12, to check a point or strengthen a concept with thin evidence; each lists the label it had in its group file under `research/concepts/`. `S206` to `S251` were added the same day by the challenge pass (`research/challenge-log.md`), each fetched and read that day, to back the concepts it reframed or added (C117-C135). `S252` to `S254` were added the same day by the audit fixes (`research/design-decision.md`, "Audit fixes"): two of Aaron's ledger posts and one of his Playback records, each read that day. IDs are permanent: lessons and the curriculum cite them.
- **Dates.** Every entry carries the date shown on the page, or the best date found behind it (byline, "last modified", changelog, archive), and says when it is inferred or when no date exists. Counting rule: each source counts once, by the first date its Date field gives for the source itself (when the field shows only an update, revision or last-modified date, that date); later revision dates and read dates never count. A date is *inferred* when the page shows none and the entry takes it from elsewhere: an archive, the URL, slide assets, the sweep notes, a relative date ("24 days ago", "Updated this week"), or the release date of the newest version the page names ("content no earlier than"); a copyright footer's year is not a date. Of the 254 sources cited, 197 (78%) are dated 2026 (177 with an explicit date, 20 inferred: S001, S005, S006, S016, S022, S081, S094, S100, S117, S121, S123, S128, S130, S131, S132, S185, S198, S218, S222, S231) and 145 (57%) are dated 2026-07 or later. 15 are older: S027, S049, S147, S186, S203, S204, S214, S219 and S224 are foundational and still current, and say so; S159 is dated background for one point; S205 is a live policy page last updated in 2025; S228, S229 and S238 are from November and December 2025, within the last 12 months; S237 is a 2025 model card whose licence is still current. 42 carry no date of their own (live documentation, policy and terms pages, the consolidated text of the EU AI Act, and a project page; some name a software version, a footer year or the date of a feature, none of which is the page's date); all were read on 2026-10-12, and most name a software version or a dated change that shows how current they are. Of the 126 sources credited in the curriculum's lesson rows (158 citations), 104 (83%) are dated 2026 and 83 (66%) are dated 2026-07 or later; 5 are older and 17 undated.
- **Kinds.** syllabus, course, docs, essay, paper, survey, report, incident, thread (a real question or discussion), framework, list, news, talk, terms, law, aaron-practice. `aaron-practice` is Aaron Orelup's own work: posts on his public ledger (many drafted by Claude from his transcripts, so the facts are first-hand and the framing is Claude's) and prompts from his recorded Claude Code history (Playback), which are not public. S243 is a notes file on his machine, also not public.
- **Suggest a source.** Open "A source the course should be built on" on the [GitHub repo](https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose) with the link, the date it was published, and what it teaches that the course is missing or has wrong. The best sources are recent, first-hand (they did the work, ran the survey or wrote the postmortem) and specific.

## Cited sources

### S001 CS146S: The Modern Software Developer (Fall 2026 syllabus, compared with Fall 2025)

- **Author:** Mihail Eric (instructor), Stanford University
- **Date:** Page undated; Fall 2026 term began 2026-09-22
- **URL:** https://themodernsoftware.dev/
- **Kind:** syllabus
- **Contributes:** What a top university now teaches agent-era builders, and what it dropped from Fall 2025 (hand-debugging, power prompting, how an LLM is made).
- **Cited by:** C001, C003, C014, C019, C021, C022, C026, C032, C033, C039, C040, C042, C044, C048, C049, C051, C052, C053, C056, C058, C062, C072, C073, C094, C122; group notes G04, G13

### S002 CS146S lecture 2026-09-24: anatomy of a state-of-the-art coding agent (transcript)

- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-24
- **URL:** https://themodernsoftware.dev/materials/9-24-26-transcript.txt
- **Kind:** course
- **Contributes:** How a coding agent is built: the 150-200-line loop, the harness around the model, what every request carries, memory as a prompt block.
- **Cited by:** C003, C021, C023, C025, C026, C028, C040, C044, C049, C051, C052, C073, C092, C124; group notes G03, G04, G05, G13

### S003 CS146S lecture 2026-09-29: advanced prompting and context engineering, RePPIT (transcript)

- **Author:** Mihail Eric, Stanford CS146S
- **Date:** 2026-09-29
- **URL:** https://themodernsoftware.dev/materials/9-29-26-transcript.txt
- **Kind:** course
- **Contributes:** Context engineering and RePPIT spec-driven work, advertised vs usable context, and agents testing their own UI in a browser.
- **Cited by:** C001, C003, C014, C016, C018, C019, C024, C026, C027, C033, C036, C039, C040, C041, C042, C048, C052, C056, C058, C094, C096, C125; group notes G03, G04, G13

### S004 AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening

- **Author:** Aaron Orelup (drafted by Claude from his feedback)
- **Date:** 2026-10-04
- **URL:** https://aaronorelup.com/ledger/lessons-sent-back/
- **Kind:** aaron-practice
- **Contributes:** The course's own rule and Aaron's gap list: why he sent back a 2021-style model lesson and a hand-debugging lesson.
- **Cited by:** C001, C010, C014, C018, C019, C021, C022, C023, C025, C026, C032, C033, C034, C035, C036, C037, C038, C040, C042, C044, C049, C051, C052, C053, C054, C055, C057, C062, C064, C065, C072, C073, C094, C103, C105; group notes G01

### S005 Claude Code 101 (Anthropic Academy)

- **Author:** Anthropic Academy
- **Date:** Page undated; slide assets dated 2026-04-09; live on 2026-10-12
- **URL:** https://anthropic.skilljar.com/claude-code-101
- **Kind:** course
- **Contributes:** Anthropic's beginner course: the agent loop, instruction files, hooks as deterministic control, permission modes.
- **Cited by:** C021, C022, C026, C028, C033, C039, C044, C045, C049, C055, C062, C077, C081, C083, C117, C122; group notes G04, G13

### S006 AI Capabilities and Limitations (Anthropic Academy)

- **Author:** Anthropic Academy
- **Date:** Page undated; live by early April 2026 (Wayback)
- **URL:** https://anthropic.skilljar.com/ai-capabilities-and-limitations
- **Kind:** course
- **Contributes:** Anthropic's course on what a model knows well and badly, uneven attention over long context, and steering with concrete instructions.
- **Cited by:** C023, C024, C026, C030, C036, C042; group notes G04

### S007 AI Fluency for Builders (Anthropic Academy with CodePath)

- **Author:** Anthropic Academy and CodePath
- **Date:** 2026-09-29 (Coursera launch; 'recently updated September 2026')
- **URL:** https://www.coursera.org/learn/ai-fluency-for-builders
- **Kind:** course
- **Contributes:** A builder course: calibrate trust on work whose answer you know, define done before delegating, own the ship, fix or stop decision.
- **Cited by:** C002, C009, C013, C016, C034, C038, C043, C055; group notes G04

### S008 Codex Bootcamp 101: Agentic coding (OpenAI Academy livestream and slide deck)

- **Author:** OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala)
- **Date:** 2026-09-23
- **URL:** https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c
- **Kind:** course
- **Contributes:** OpenAI's Codex bootcamp: the Prompt, Inspect, Act, Validate, Report loop, three questions before accepting, read diffs so you can explain them.
- **Cited by:** C003, C009, C011, C012, C014, C018, C019, C020, C021, C022, C026, C028, C033, C034, C035, C038, C039, C041, C042, C044, C045, C049, C055, C059, C062, C064, C083, C085, C091; group notes G04

### S009 Test and Debug with GitHub Copilot (GitHub Skills exercise)

- **Author:** GitHub (GitHub Skills)
- **Date:** 2026-09-29 (content committed 2026-09-30)
- **URL:** https://github.com/skills/test-and-debug-with-github-copilot
- **Kind:** course
- **Contributes:** GitHub's exercise: tie an AI explanation to evidence, write a Verification section, and a domain rule (bill-splitting rounding) the agent won't volunteer.
- **Cited by:** C005, C011, C013, C019, C034, C041, C055

### S010 Build with Andrew

- **Author:** Andrew Ng, DeepLearning.AI
- **Date:** 2026-07-17
- **URL:** https://www.deeplearning.ai/courses/build-with-andrew
- **Kind:** course
- **Contributes:** Ng's no-code course, and what its one-file demo leaves out: tests, hosting, security, keys, accounts, stored data and AI costs.
- **Cited by:** C005, C008, C016, C024, C030, C038, C055, C062, C125, C127

### S011 Six misconceptions about large language models: A minimal model and diagnostic taxonomy

- **Author:** Zhicheng Lin
- **Date:** 2026-07-08
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/
- **Kind:** paper
- **Contributes:** Lin's taxonomy of LLM misconceptions: the deployed configuration as the unit of analysis, three places information lives, tone shifting trust.
- **Cited by:** C001, C005, C021, C023, C024, C030, C031

### S012 Context windows (Claude Platform Docs)

- **Author:** Anthropic
- **Date:** Undated live docs (lists Opus 5.5 and Fable 5.1)
- **URL:** https://platform.claude.com/docs/en/build-with-claude/context-windows
- **Kind:** docs
- **Contributes:** Anthropic's docs on the context window: what each request contains, context rot, thinking blocks that must be passed back, prompt caching.
- **Cited by:** C021, C023, C025, C026, C027, C029, C032, C056, C057; group notes G03, G06

### S013 Gemini thinking (Google AI for Developers)

- **Author:** Google
- **Date:** Last updated 2026-10-09
- **URL:** https://ai.google.dev/gemini-api/docs/generate-content/thinking
- **Kind:** docs
- **Contributes:** Google's docs on thinking: reasoning tokens billed but unseen, thought signatures, and output caps that return blank answers.
- **Cited by:** C021, C029, C059; group notes G03

### S014 An update on recent Claude Code quality reports

- **Author:** Anthropic
- **Date:** 2026-04-23
- **URL:** https://www.anthropic.com/engineering/april-23-postmortem
- **Kind:** incident
- **Contributes:** Anthropic's April 2026 postmortem: three harness changes, not the model, caused the reported quality drop.
- **Cited by:** C021, C057, C059; group notes G03, G06

### S015 Extend Claude Code (features overview)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated live docs
- **URL:** https://code.claude.com/docs/en/features-overview
- **Kind:** docs
- **Contributes:** Claude Code's features overview: skills, hooks, MCP, subagents and plugins, and how each one loads into context.
- **Cited by:** C021, C023, C025, C026, C027, C028, C029, C044, C045, C046, C047, C049, C050, C051, C090, C091, C092; group notes G05

### S016 Manage costs effectively (Claude Code)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated; content no earlier than 2026-09-14 (names v2.1.271)
- **URL:** https://code.claude.com/docs/en/costs
- **Kind:** docs
- **Contributes:** Claude Code's cost page: plan usage vs API billing, context you didn't type, the token cost of agent teams, spend controls.
- **Cited by:** C021, C022, C025, C026, C028, C055, C056, C057, C058, C059, C060, C061, C095, C096; group notes G06, G10

### S017 AO-026: Sonnet 5.5 is half the price of Opus 5.5 on paper. Across three long tests it was 2% cheaper.

- **Author:** Aaron Orelup
- **Date:** 2026-09-28
- **URL:** https://aaronorelup.com/ledger/sonnet-vs-opus-gauntlet/
- **Kind:** aaron-practice
- **Contributes:** Aaron's measured Sonnet vs Opus gauntlet: cache reads were 97% of tokens, and 'half the price' came out 2% cheaper (at the pre-2026-10-07 cache price).
- **Cited by:** C055, C056, C057, C058, C059, C060, C096; group notes G06

### S018 ~$1,500 in one week running a Grok Bot fleet: expected, or a bug?

- **Author:** Stijn (dotstijn); replies by Kevin Neilson (Cursor staff), Zachariah
- **Date:** 2026-09-22
- **URL:** https://forum.cursor.com/t/172705
- **Kind:** incident
- **Contributes:** A ~$1,500 week of Cursor bot fleets: bots waking bots and re-reading 80-90k tokens per step.
- **Cited by:** C055, C056, C060; group notes G06

### S019 Zapier Agents: unexpected activity usage

- **Author:** Zapier Help Center
- **Date:** 2026-10-01 (updated)
- **URL:** https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage
- **Kind:** docs
- **Contributes:** Zapier's help article on agents draining activity quotas, including loops where an agent triggers itself.
- **Cited by:** C055, C060, C096; group notes G06

### S020 Google API Keys Weren't Secrets. But then Gemini Changed the Rules.

- **Author:** Joe Leon (Truffle Security)
- **Date:** 2026-02-25 (byline; page metadata lists 2026-10-08)
- **URL:** https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules
- **Kind:** incident
- **Contributes:** Truffle Security: Google API keys published as harmless became Gemini-billable secrets after the rules changed.
- **Cited by:** C061, C069, C071; group notes G06

### S021 The State Of AI Harness Engineering 2026

- **Author:** François Zaninotto (Marmelab)
- **Date:** 2026-09-24
- **URL:** https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html
- **Kind:** survey
- **Contributes:** A survey of harness engineering: rules vs enforcement, guards that are never tested, reviewer agents that don't help.
- **Cited by:** C014, C017, C019, C038, C044, C045, C047, C048, C051, C077, C095, C097; group notes G05

### S022 Rethinking skills and prompts for GPT-6 Astra

- **Author:** OpenAI (developers blog)
- **Date:** Undated; no earlier than 2026-09-03 (GPT-6 Astra release)
- **URL:** https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- **Kind:** docs
- **Contributes:** OpenAI's advice to prune instructions written for weaker models, and to say that running and fixing are part of the task.
- **Cited by:** C034, C038, C044, C048, C050; group notes G04, G05

### S023 Agent repeatedly ignores workspace User Rules and repo gates across multiple chats

- **Author:** Brunno Oliveira Prego; replies by Mohit (Cursor staff)
- **Date:** 2026-09-02
- **URL:** https://forum.cursor.com/t/170277
- **Kind:** incident
- **Contributes:** A Cursor agent ignored rules set in three places across four chats; staff: rules are guidance the model can deviate from.
- **Cited by:** C045, C046, C070, C071, C077, C081, C082, C084

### S024 Kiro specs (with Kiro docs index)

- **Author:** Kiro (AWS)
- **Date:** 2026-10-02
- **URL:** https://kiro.dev/docs/specs/
- **Kind:** docs
- **Contributes:** Kiro's spec docs: requirements, design and tasks, Analyze Requirements, and steering that is preferred, not enforced.
- **Cited by:** C037, C040, C045, C046

### S025 ChatGPT & Codex changelog (with Get started with ChatGPT Work)

- **Author:** OpenAI
- **Date:** Latest entry 2026-10-08
- **URL:** https://learn.chatgpt.com/docs/changelog
- **Kind:** docs
- **Contributes:** OpenAI's changelog as evidence of how fast surfaces move: Codex in the ChatGPT app, ChatGPT Work local vs cloud, new review layers.
- **Cited by:** C014, C017, C020, C022, C024, C028, C046, C052, C094, C099; group notes G05

### S026 AO-043: A cloud session pushed one post from a branch, and my whole site went back to August

- **Author:** Aaron Orelup
- **Date:** 2026-10-09 (incident 2026-10-08)
- **URL:** https://aaronorelup.com/ledger/the-branch-that-went-live/
- **Kind:** aaron-practice
- **Contributes:** Aaron's incident: a cloud session pushed from a stale branch and rolled his whole site back to August.
- **Cited by:** C011, C017, C045, C046, C047, C094, C098, C099, C101, C102, C124, C127; group notes G05, G13

### S027 Verifiability

- **Author:** Andrej Karpathy
- **Date:** 2025-11-17 (foundational and still current)
- **URL:** https://karpathy.bearblog.dev/verifiability/
- **Kind:** essay
- **Contributes:** Karpathy's thesis that AI masters what is verifiable: tasks whose environment is resettable, efficient and rewardable.
- **Cited by:** C001, C002, C003, C034; group notes G01

### S028 More than just code review

- **Author:** Simon Willison
- **Date:** 2026-08-22
- **URL:** https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
- **Kind:** essay
- **Contributes:** Willison: confidently instruct, then confidently verify; reading every line was never the most effective check.
- **Cited by:** C015, C063, C072; group notes G01

### S029 The Code Nobody Reads

- **Author:** Addy Osmani
- **Date:** 2026-09-28
- **URL:** https://addyo.substack.com/p/the-code-nobody-reads
- **Kind:** essay
- **Contributes:** Osmani: stop reading every line only where something trustworthy checks; review tiers by blast radius; a person owns every merge.
- **Cited by:** C001, C002, C003, C006, C007, C009, C010, C011, C013, C014, C015, C017, C018, C020, C033, C034, C038, C040, C043, C053, C054, C062, C063, C066, C072, C118; group notes G01, G02, G04, G05

### S030 When a Coding Agent Says Done: How Do You Accept It — A 2026 Survey of the Verification Layer

- **Author:** Remy (redreamality.com)
- **Date:** 2026-10-11
- **URL:** https://redreamality.com/blog/coding-agent-done-claims-verification-survey/
- **Kind:** survey
- **Contributes:** A survey of how to accept an agent's 'done': seven shapes of false done, receipts, the AI Agreement Loop, and what verification costs.
- **Cited by:** C005, C007, C011, C012, C013, C014, C017, C034, C038, C040, C041, C042, C078, C095, C096, C100, C101; group notes G01, G02, G04

### S031 Humans are Missing from AI Coding Agent Research

- **Author:** Zora Z. Wang, John Yang, Kilian Lieret, et al. (incl. Graham Neubig, Daniel Fried, Diyi Yang)
- **Date:** 2026-07-04 (arXiv v1)
- **URL:** https://arxiv.org/abs/2608.12355
- **Kind:** paper
- **Contributes:** Wang et al.: humans are missing from agent research; agent-written tests aren't independent; ask for human-readable evidence.
- **Cited by:** C003, C013, C015, C020, C034, C035, C041, C062, C064; group notes G04

### S032 AO-027: My agents built 16 wallpapers overnight, and none of them ever saw one run

- **Author:** Aaron Orelup
- **Date:** 2026-09-29
- **URL:** https://aaronorelup.com/ledger/wallpapers-nobody-saw/
- **Kind:** aaron-practice
- **Contributes:** Aaron's 16 wallpapers built overnight that no agent saw run: 'tested' meant 'didn't crash'; give agents eyes, then check the eyes.
- **Cited by:** C001, C002, C003, C005, C007, C011, C016, C017, C032, C038, C041, C042, C096, C100; group notes G01, G10

### S033 2026 in LLMs (so far)

- **Author:** Simon Willison
- **Date:** 2026-09-27
- **URL:** https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/
- **Kind:** essay
- **Contributes:** Willison's 2026 review: the November 2025 threshold, reinforcement learning from verifiable rewards, StrongDM's no-human-review rule.
- **Cited by:** C002, C004, C015, C016, C020, C029, C031, C033, C034, C043, C052, C058, C059, C061, C063, C064, C072, C080, C087, C105; group notes G03, G04, G06

### S034 What I believe about the future of software development

- **Author:** Thorsten Ball
- **Date:** 2026-09-19
- **URL:** https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/
- **Kind:** essay
- **Contributes:** Ball: spec bugs replace code bugs; contested predictions such as 'code review is already dead' and 'unit tests might die'.
- **Cited by:** C013, C015, C033, C034, C043, C054, C058, C117, C122; group notes G04

### S035 Astra for Coding: Why Are We Doing This Again?

- **Author:** Armin Ronacher
- **Date:** 2026-09-07
- **URL:** https://lucumr.pocoo.org/2026/9/7/astra-why/
- **Kind:** essay
- **Contributes:** Ronacher's 35-hour GPT-6 Astra run (~75k lines, ~$1,200, nothing of value in his judgment): 'done' reflects what training rewards.
- **Cited by:** C004, C015, C016, C020, C041, C054, C055, C056, C058, C059, C061, C080, C096; group notes G01, G04, G06, G10

### S036 Brownfield Agentic Engineering

- **Author:** Addy Osmani
- **Date:** 2026-09-14
- **URL:** https://addyosmani.com/blog/brownfield-agentic-engineering/
- **Kind:** essay
- **Contributes:** Osmani on brownfield work: zone maps by blast radius, characterization tests, a read-only comprehension pass before changing code.
- **Cited by:** C007, C013, C015, C018, C020, C027, C028, C035, C036, C037, C038, C039, C040, C041, C042, C043, C044, C045, C047, C048, C053, C078, C080, C095, C096; group notes G01, G04, G05

### S037 A field guide to Claude Fable 5: Finding your unknowns

- **Author:** Thariq Shihipar (Anthropic)
- **Date:** 2026-07-06
- **URL:** https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
- **Kind:** essay
- **Contributes:** Shihipar's field guide to finding your unknowns: blind-spot passes, interviews, and an explainer-and-quiz gate before merging.
- **Cited by:** C018, C027, C034, C035, C036, C037, C040; group notes G04

### S038 LLMs are getting smarter but not safer: Veracode 2026 GenAI Code Security Report

- **Author:** Veracode (Chris Wysopal quoted)
- **Date:** 2026-07-28
- **URL:** https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/
- **Kind:** report
- **Contributes:** Veracode 2026: about 100% syntax pass but a 56% security pass rate, flat across four snapshots and 100+ models.
- **Cited by:** C062, C063, C087; group notes G07

### S039 Understanding the (In)Security of Vibe-Coded Applications

- **Author:** Junquan Deng, Zhiyu Fan, Ruijie Meng
- **Date:** 2026-06-22 (v1; v4 2026-09-14)
- **URL:** https://arxiv.org/abs/2606.23130
- **Kind:** paper
- **Contributes:** An audit of 200 deployed vibe-coded apps: 91% vulnerable, demo shortcuts left in, unstated security rules, 'fixes' that weaken safeguards.
- **Cited by:** C004, C008, C009, C062, C063, C064, C065, C066, C067, C075, C087; group notes G01, G07

### S040 (Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code

- **Author:** Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka
- **Date:** 2026-09-17
- **URL:** https://arxiv.org/abs/2609.21020
- **Kind:** paper
- **Contributes:** A controlled study (n = 100): developers could not pick the secure AI suggestion above chance, and experience did not help.
- **Cited by:** C006, C013, C015, C062; group notes G01

### S041 The 'vibe coding spectrum' approach to AI-assisted software development

- **Author:** Toby W, Principal Security Architect, UK NCSC
- **Date:** 2026-06-18 (PDF generated 2026-07-03)
- **URL:** https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf
- **Kind:** essay
- **Contributes:** The NCSC's vibe-coding spectrum: slide right for prototypes, left for authentication, personal data, secrets and safety.
- **Cited by:** C001, C006, C007, C008, C062, C063, C064, C066, C067, C068, C072; group notes G01

### S042 Secure Coding with AI Cheat Sheet

- **Author:** OWASP Cheat Sheet Series
- **Date:** Created 2026-05-05; last updated 2026-10-04
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html
- **Kind:** docs
- **Contributes:** OWASP's cheat sheet: human accountability for AI changes, test-gaming patterns, secrets, MCP and dependency rules.
- **Cited by:** C004, C006, C009, C012, C013, C014, C062, C063, C065, C069, C070, C073, C074, C075, C078, C081, C082, C083, C085, C086, C087, C088, C090, C092; group notes G01, G07

### S043 Claude Code: Catch security issues as Claude writes code (security-guidance plugin)

- **Author:** Anthropic (live docs)
- **Date:** Undated on page; last modified 2026-10-09
- **URL:** https://code.claude.com/docs/en/security-guidance
- **Kind:** docs
- **Contributes:** Claude Code's security-guidance plugin: a separate AI review of each turn's diff that can miss issues and blocks nothing, so it is a floor, not a gate.
- **Cited by:** C012, C014, C017, C062, C064, C065, C066, C067, C072

### S044 Hacking Moltbook: The AI Social Network Any Human Can Control

- **Author:** Gal Nagli (Wiz Research)
- **Date:** 2026-02-02
- **URL:** https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- **Kind:** incident
- **Contributes:** Wiz's Moltbook write-up: an exposed Supabase database, and the row-level security and secret-key mistakes behind it.
- **Cited by:** C065, C067, C068, C069, C082

### S045 v0 security (with External APIs / environment variables)

- **Author:** Vercel (v0 docs)
- **Date:** 2026-10-09
- **URL:** https://v0.app/docs/security
- **Kind:** docs
- **Contributes:** Vercel's v0 security docs: a NEXT_PUBLIC_ prefix publishes a key to every visitor; where environment variables belong.
- **Cited by:** C065, C066, C068, C069, C070, C071, C072, C099

### S046 Update on Security at METR

- **Author:** METR
- **Date:** 2026-08-31
- **URL:** https://metr.org/blog/2026-08-31-security-update/
- **Kind:** incident
- **Contributes:** METR's stolen API key that consumed about $600,000 of credits for three weeks before anyone noticed.
- **Cited by:** C061, C063, C066, C067, C068, C069, C070, C071, C082; group notes G06, G07

### S047 Secret scanning adds detectors for Lovable, Supabase, and more

- **Author:** GitHub Changelog
- **Date:** 2026-10-05
- **URL:** https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more
- **Kind:** docs
- **Contributes:** GitHub secret scanning: new detectors, and what push protection does and doesn't cover by default.
- **Cited by:** C071, C072

### S048 Leaked n8n API Tokens Exposed Live Instances to Credential Theft

- **Author:** Guillaume Valadon (GitGuardian), on The Hacker News
- **Date:** 2026-08-05
- **URL:** https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
- **Kind:** report
- **Contributes:** Leaked n8n API tokens: one token unlocks every stored credential; agent config files and co-authored commits as new leak paths.
- **Cited by:** C066, C069, C070, C071, C072, C082

### S049 The lethal trifecta for AI agents: private data, untrusted content, and external communication

- **Author:** Simon Willison
- **Date:** 2025-06-16 (foundational and still current)
- **URL:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **Kind:** essay
- **Contributes:** Willison's lethal trifecta: never combine private data, untrusted content and a way to send data out.
- **Cited by:** C073, C074, C076

### S050 How we contain Claude across products

- **Author:** Anthropic Engineering
- **Date:** 2026-05-25
- **URL:** https://www.anthropic.com/engineering/how-we-contain-claude
- **Kind:** report
- **Contributes:** Anthropic's containment engineering: model-layer defences are never 100%, so the boundary must sit in the environment.
- **Cited by:** C073, C075, C076, C077, C078, C079, C080, C082, C083, C085, C086, C089, C090, C092, C097, C103, C104, C117, C128; group notes G08, G13

### S051 Auto mode is now the default in Claude Code for Pro, Max, and Team plans

- **Author:** Simon Willison
- **Date:** 2026-08-08
- **URL:** https://simonwillison.net/2026/Aug/8/auto-mode/
- **Kind:** essay
- **Contributes:** Willison on auto mode becoming Claude Code's default, its approval numbers, and the working attack that followed within weeks.
- **Cited by:** C074, C076, C077, C078, C081, C086, C089, C090; group notes G08

### S052 Choose a permission mode (Claude Code)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated live docs (v2.1.283+; re-read 2026-10-12)
- **URL:** https://code.claude.com/docs/en/permission-modes
- **Kind:** docs
- **Contributes:** Claude Code's permission-mode, security and sandbox docs: what auto mode, deny rules and the sandbox actually cover (with GitHub Copilot's local sandboxing).
- **Cited by:** C045, C046, C047, C074, C075, C076, C077, C078, C079, C081, C082, C083, C086, C089, C091, C097, C123, C124; group notes G08, G09

### S053 A CISO's guide to agentic AI

- **Author:** Jason Clinton, Deputy CISO, Anthropic
- **Date:** 2026-07-17
- **URL:** https://claude.com/blog/ciso-guide-to-agentic-ai
- **Kind:** essay
- **Contributes:** Anthropic's CISO guide: start with 'what untrusted content does it ingest?'; prompts are not controls; least agency.
- **Cited by:** C074, C076, C078, C082, C083, C084, C085

### S054 One prompt let researchers take over AWS AgentCore agents (AgentCorruption)

- **Author:** Ana Maria Constantin (The Next Web), reporting Zenity Labs
- **Date:** 2026-10-08
- **URL:** https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents
- **Kind:** incident
- **Contributes:** AgentCorruption: one plain-language prompt took over AWS AgentCore agents and poisoned their memory.
- **Cited by:** C075, C076, C080, C083

### S055 OWASP Top 10 for LLM Applications 2026

- **Author:** OWASP GenAI Security Project
- **Date:** 2026-08-04
- **URL:** https://github.com/GenAI-Security-Project/GenAI-LLM-Top10
- **Kind:** framework
- **Contributes:** The OWASP Top 10 for LLM Applications 2026 (read with the Agentic Top 10): the current risk list that tutorials still miss. On 2026-10-12 the challenge pass also read four entries in full from the repository's `2026/final/` folder: LLM02 Sensitive Information Disclosure, LLM06 Unbounded Consumption, LLM07 Misinformation and LLM10 Improper Output Handling (C063, C119, C121).
- **Cited by:** C063, C069, C070, C072, C073, C075, C077, C082, C083, C084, C085, C119, C121

### S056 GitSpawn: AI coding agents run attacker code via git config

- **Author:** Francisco Rosales (Manifold Security)
- **Date:** 2026-09-01
- **URL:** https://www.manifold.security/blog/ai-coding-agents-git-hijack
- **Kind:** incident
- **Contributes:** GitSpawn: a repository's git config makes 'read-only' agent actions like git status run attacker code.
- **Cited by:** C089, C090; group notes G09

### S057 How a Malicious Repo Tricked Claude Code into Running Malware

- **Author:** Brian Cumi (Straiker STAR Labs)
- **Date:** 2026-09-22
- **URL:** https://www.straiker.ai/blog/how-a-malicious-repo-tricked-claude-code-into-running-malware
- **Kind:** incident
- **Contributes:** Straiker: a malicious repo's test file ran a live implant while the test run reported '11 passed'.
- **Cited by:** C089, C090

### S058 Agentjacking: MCP Injection Hijacks AI Coding Agents (CSA research note)

- **Author:** Cloud Security Alliance AI Safety Initiative, summarizing Tenet Security Threat Labs
- **Date:** 2026-06-12
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/
- **Kind:** incident
- **Contributes:** Agentjacking: injected Sentry errors steered coding agents through an official MCP server in 85% of tests.
- **Cited by:** C069, C071, C073, C078, C085, C086, C089; group notes G09

### S059 MCP Security Best Practices (specification revision 2026-07-28)

- **Author:** Model Context Protocol project
- **Date:** 2026-07-28
- **URL:** https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices
- **Kind:** docs
- **Contributes:** MCP's 2026-07-28 specification revision and security best practices: what 2025-era explainers now get wrong.
- **Cited by:** C024, C067, C078, C083, C091

### S060 Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks (CSA research note)

- **Author:** Cloud Security Alliance AI Safety Initiative
- **Date:** 2026-04-19 (core statistics from a 2025 study)
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/
- **Kind:** report
- **Contributes:** Slopsquatting: 19.7% of AI code samples named a nonexistent package, and the invented names repeat predictably.
- **Cited by:** C087, C088; group notes G09

### S061 ChainDrop npm Worm

- **Author:** Sai Likhith (StepSecurity)
- **Date:** 2026-08-04
- **URL:** https://stepsecurity.io/blog/chaindrop-npm-worm
- **Kind:** incident
- **Contributes:** The ChainDrop npm worm: it steals AI-tool credential files and punishes revoking a token from the infected machine.
- **Cited by:** C070, C071, C075, C078, C082, C087, C088, C089, C090, C093, C123, C129; group notes G09, G13

### S062 Playback: security moments (a malicious redirect, and verifying a download before install)

- **Author:** Aaron Orelup (typed and pasted prompts)
- **Date:** 2026-09-28 and 2026-10-10 (two sessions)
- **URL:** playback-lens session 7c75a0b6-4bcf-45ae-9869-1489cad914a6 (project C--Users-soulo-Organized-Personal-My-Projects-Sandbox-2), 2026-09-28; and session dea3f681-154f-47d6-a4f4-05cb5da99bb5 (photoshop project), 2026-10-10
- **Kind:** aaron-practice
- **Contributes:** Aaron's own near-miss with a fake 'I am not a bot' page, and checking a download before installing it.
- **Cited by:** C071, C087, C088, C093

### S063 [Agent] Autonomous rd /s /q wiped the entire D: drive (Windows)

- **Author:** luck_li; reply by Colin (Cursor staff, Community Support Engineer)
- **Date:** 2026-10-09
- **URL:** https://forum.cursor.com/t/174156
- **Kind:** incident
- **Contributes:** A Cursor agent's rd /s /q wiped a whole D: drive; staff confirm Windows terminal commands are not sandboxed.
- **Cited by:** C012, C079, C081, C084, C097, C098; group notes G10

### S064 Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident

- **Author:** Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk (METR)
- **Date:** 2026-08-26
- **URL:** https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
- **Kind:** incident
- **Contributes:** METR on the OpenAI / Hugging Face incident: agents cheat impossible tasks, cross boundaries they describe, and never alert anyone.
- **Cited by:** C004, C005, C011, C012, C014, C080, C085, C094; group notes G01

### S065 GenAI and Agentic AI Exploit Roundup Q3 2026

- **Author:** OWASP Gen AI Security Project (editor)
- **Date:** 2026-10-08
- **URL:** https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026
- **Kind:** report
- **Contributes:** OWASP's Q3 2026 exploit roundup: agents treating lookalike targets as authorised; prompt-level instructions are not a boundary.
- **Cited by:** C004, C012, C045, C049, C075, C076, C080, C083, C084, C085, C087, C088, C089, C092

### S066 Webhook works in test but not in production? The test vs. production URL trap

- **Author:** Syed Farzam Saadat
- **Date:** 2026-10-04
- **URL:** https://community.n8n.io/t/318716
- **Kind:** community
- **Contributes:** n8n's test vs production webhook URL trap, and other local vs reachable mix-ups.
- **Cited by:** C099

### S067 How do you catch workflows that run fine but do nothing?

- **Author:** Richard Rodrigues; 36 posts (Romeo Apps, Nathan, Adam, Cam, Michael Stables, Enzo Software)
- **Date:** 2026-08-21 (replies to 2026-10-08)
- **URL:** https://community.n8n.io/t/308708
- **Kind:** thread
- **Contributes:** An n8n thread on workflows that run green but do nothing, and checking the destination instead of the run.
- **Cited by:** C012, C017, C099, C100, C101, C102; group notes G10

### S068 Agency and Agents

- **Author:** Ethan Mollick
- **Date:** 2026-08-31
- **URL:** https://www.oneusefulthing.org/p/agency-and-agents
- **Kind:** essay
- **Contributes:** Mollick: when an agent should bring a human in, and why keeping only the approvals automates the wrong half of the job.
- **Cited by:** C002, C004, C010, C030, C037, C042, C043, C077, C083, C084; group notes G01, G04

### S069 Use Claude Cowork safely

- **Author:** Anthropic (Claude Help Center)
- **Date:** Last modified 2026-10-06
- **URL:** https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- **Kind:** docs
- **Contributes:** Anthropic's Cowork safety page: where tasks run, what you remain responsible for, and the prompt-injection risk.
- **Cited by:** C009, C022, C073, C074, C076, C080, C081, C083, C084, C085, C086, C091, C094, C097, C098, C103, C104, C117, C123; group notes G01, G03, G10, G11, G13

### S070 Use Claude in Chrome safely (Anthropic Help Center)

- **Author:** Anthropic
- **Date:** Last modified 2026-10-05
- **URL:** https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely
- **Kind:** docs
- **Contributes:** Anthropic's Claude in Chrome safety page: everything visible in the tab is input, and you remain responsible for what it does.
- **Cited by:** C009, C073, C074, C076, C081, C084, C103, C104; group notes G11

### S071 Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users

- **Author:** Ravie Lakshmanan (The Hacker News), reporting Koi Security and OpenSourceMalware
- **Date:** 2026-02-02 (older than three months; still the primary incident record)
- **URL:** https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- **Kind:** incident
- **Contributes:** 341 malicious ClawHub skills that stole OpenClaw users' keys, mostly by getting people to paste a command.
- **Cited by:** C074, C075, C085, C091, C093, C105

### S072 AI Hallucination Cases database

- **Author:** Damien Charlotin
- **Date:** Last updated 2026-10-10
- **URL:** https://www.damiencharlotin.com/hallucinations/
- **Kind:** list
- **Contributes:** Charlotin's database of 2,184 court decisions involving AI-hallucinated material; the filer stays responsible.
- **Cited by:** C001, C009, C106; group notes G01

### S073 Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

- **Author:** Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania)
- **Date:** 2026-04-03 (models tested are older)
- **URL:** https://arxiv.org/html/2604.03173v1
- **Kind:** paper
- **Contributes:** A study of reference hallucinations: link checkers cut dead URLs, and whether a real source supports the claim is a separate check.
- **Cited by:** C003, C106, C107; group notes G11

### S074 WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

- **Author:** Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. (Columbia Business School)
- **Date:** 2026-05-21
- **URL:** https://arxiv.org/html/2605.22664v1
- **Kind:** paper
- **Contributes:** WorkstreamBench: the best finance spreadsheet agent scored 69/100, and agents typed values where formulas belong.
- **Cited by:** C002, C021, C022, C108

### S075 Can AI Now Design PCBs That Just Work?

- **Author:** Maya Posch, Hackaday
- **Date:** 2026-09-05
- **URL:** https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/
- **Kind:** essay
- **Contributes:** Hackaday on AI circuit-board design: what the benchmark skips, mains safety and EMC testing, independent review before selling.
- **Cited by:** C002, C008, C009, C109; group notes G01

### S076 EU AI Act: Transparency Obligations for AI-Generated Content (Article 50)

- **Author:** Julia Apostle, Orrick
- **Date:** 2026-08-14
- **URL:** https://www.orrick.com/en/Insights/2026/08/EU-AI-Act-Transparency-Obligations-for-AI-Generated-Content-Article-50
- **Kind:** report
- **Contributes:** Orrick on EU AI Act Article 50: providers mark outputs, deployers disclose deepfakes and AI-written public-interest text.
- **Cited by:** C110, C111, C112, C115; group notes G12

### S077 Suno Terms of Service

- **Author:** Suno, Inc.
- **Date:** Revised 2026-08-10, effective 2026-09-03
- **URL:** https://suno.com/terms
- **Kind:** docs
- **Contributes:** Suno's terms: commercial rights depend on the plan and the download; no removing watermarks or metadata.
- **Cited by:** C110, C113, C114, C115, C116; group notes G12

### S078 A Federal Shift in AI and the Right of Publicity? NO FAKES Act Advances in Congress

- **Author:** Erik Dullea, Evan Yahng (Husch Blackwell)
- **Date:** 2026-08-20
- **URL:** https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/
- **Kind:** report
- **Contributes:** Husch Blackwell on the NO FAKES Act (pending) and New York's synthetic-performer advertising law.
- **Cited by:** C111, C115; group notes G12

### S079 YouTube clarifies policies around AI slop and upsetting videos

- **Author:** Sarah Perez, TechCrunch
- **Date:** 2026-07-20 (policy rollout 2026-07-16)
- **URL:** https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- **Kind:** report
- **Contributes:** TechCrunch on YouTube's July 2026 clarifications: inauthentic and repetitive content lose monetisation, disclosure does not.
- **Cited by:** C116; group notes G12

### S080 Stack Overflow Developer Survey 2026 - full results site (AI, Knowledge, Community) and press release

- **Author:** Stack Overflow (press release quotes CEO Prashanth Chandrasekar)
- **Date:** Released 2026-10-06 (fieldwork 2026-06-23 to 2026-08-05)
- **URL:** https://survey.stackoverflow.co/2026/
- **Kind:** survey
- **Contributes:** Stack Overflow's 2026 survey: trust in AI output is conditional on being able to verify it, and what developers check before using it.
- **Cited by:** C001, C006, C010, C016, C024, C033, C035, C042, C055, C058, C061, C103; group notes G01, G04

### S081 How Much Code Do Developers Really Let Agents Write? (JetBrains Research, Developer Ecosystem Survey 2026)

- **Author:** Mikhail Bogdanov (JetBrains Research)
- **Date:** Page undated; 2026-08 from the URL
- **URL:** https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/
- **Kind:** survey
- **Contributes:** JetBrains' 2026 survey: about 47% of code fully agent-generated on average (self-reported), seniors moving first.
- **Cited by:** C033, C041; group notes G04

### S082 Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI

- **Author:** Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva
- **Date:** 2026-07-01
- **URL:** https://arxiv.org/abs/2607.01418
- **Kind:** paper
- **Contributes:** Microsoft's rollout study: about 24% more merged PRs per engineer, with no measure of quality.
- **Cited by:** C020, C033, C041, C042, C043, C058, C095; group notes G04

### S083 How AI assistance impacts the formation of coding skills (Anthropic)

- **Author:** Judy Hanwen Shen and Alex Tamkin
- **Date:** 2026-01-29 (foundational and still current)
- **URL:** https://www.anthropic.com/research/AI-assistance-coding-skills
- **Kind:** paper
- **Contributes:** Anthropic's randomized trial: full delegation while learning cut understanding most on debugging (50% vs 67%).
- **Cited by:** C010, C018, C019, C036, C042; group notes G01, G04

### S084 Agentic Skill Decay

- **Author:** Addy Osmani
- **Date:** 2026-08-31
- **URL:** https://addyosmani.com/blog/agentic-skill-decay/
- **Kind:** essay
- **Contributes:** Osmani on skill decay: verification is the floor and imagination the ceiling; habits that keep your judgment.
- **Cited by:** C010, C016, C018, C033, C035, C036, C041, C042, C043, C095; group notes G01, G04

### S085 From Prompting to Verification: How Experience Shapes Vibe Coding Practices

- **Author:** Ahmed Fawzy, Amjed Tahir, Kelly Blincoe
- **Date:** 2026-05-23
- **URL:** https://arxiv.org/abs/2605.24521
- **Kind:** paper
- **Contributes:** A survey of 162 vibe coders: all groups see AI code's flaws, but only experience lets people check it.
- **Cited by:** C006, C016, C041, C042; group notes G01, G04

### S086 My AI Workflow Builder keeps saying it fixed my workflow but it's still not working (n8n community thread)

- **Author:** Michael_Alexander and community replies
- **Date:** 2026-06-08 (replies to 2026-06-30)
- **URL:** https://community.n8n.io/t/298708
- **Kind:** thread
- **Contributes:** A newcomer asks how to verify an AI workflow builder's repeated claim that it fixed the workflow.
- **Cited by:** C001, C011, C019; group notes G01
- **Research label:** `X3` in `research/concepts/verification-line.md`; `N8N-298708` in `research/concepts/checking-work.md`

### S087 Should a Coding Agent Be Allowed to Mark Its Own Task Complete? (Cursor forum thread)

- **Author:** joinwell52 and community replies
- **Date:** 2026-08-16 (replies to 2026-10-04)
- **URL:** https://forum.cursor.com/t/168557
- **Kind:** thread
- **Contributes:** Real false 'done' reports: a narrow test run, a commit never pushed, a deploy still serving the old version.
- **Cited by:** C001, C009, C011, C012, C014, C017; group notes G01
- **Research label:** `X2` in `research/concepts/verification-line.md`; `CF-168557` in `research/concepts/checking-work.md`

### S088 Playback: Aaron's prompt rejecting lesson 00.06 (session 5c6d06f5)

- **Author:** Aaron Orelup (typed prompt)
- **Date:** 2026-10-03
- **URL:** playback-lens session 5c6d06f5-9b98-4551-8a6c-3ce7ab0b8993 (project C--Users-soulo-Organized-Personal-My-Projects-Courses-The-hidden-curriculum)
- **Kind:** aaron-practice
- **Contributes:** Aaron's own words on the course rule: check it yourself or bring in an expert, and the AI gets better at verifying every day.
- **Cited by:** C001; group notes G01
- **Read with:** S004
- **Research label:** `S004-pb` in `research/concepts/verification-line.md`

### S089 Datasette 1.0a39 and 0.65.4 security releases

- **Author:** Simon Willison
- **Date:** 2026-09-11
- **URL:** https://simonwillison.net/2026/Sep/11/datasette-security/
- **Kind:** essay
- **Contributes:** Independent verification in practice: one person wrote the test exposing each issue, another wrote the fix; AI security audits in development.
- **Cited by:** C001, C013, C014
- **Read with:** S028
- **Research label:** `S028-c3` in `research/concepts/verification-line.md`; `S028-c3` in `research/concepts/checking-work.md`

### S090 Introducing Showboat and Rodney, so agents can demo what they've built

- **Author:** Simon Willison
- **Date:** 2026-02-10
- **URL:** https://simonwillison.net/2026/Feb/10/showboat-and-rodney/
- **Kind:** essay
- **Contributes:** Tools that record real command output and screenshots, built because agents hand-edit their demo files.
- **Cited by:** C003, C012, C015
- **Read with:** S028
- **Research label:** `S028-c1` in `research/concepts/verification-line.md`; `S028-c1` in `research/concepts/checking-work.md`

### S091 Have your agent record video demos of its work with shot-scraper video

- **Author:** Simon Willison
- **Date:** 2026-06-30
- **URL:** https://simonwillison.net/2026/Jun/30/shot-scraper-video/
- **Kind:** essay
- **Contributes:** Video of a feature in use as evidence an agent can't easily fake, matched to the kind of change.
- **Cited by:** C003, C015
- **Read with:** S028
- **Research label:** `S028-c2` in `research/concepts/verification-line.md`; `S028-c2` in `research/concepts/checking-work.md`

### S092 AI Prompting for Everyone ('Sycophancy' lesson)

- **Author:** Andrew Ng, DeepLearning.AI
- **Date:** 2026-07-24
- **URL:** https://www.deeplearning.ai/courses/ai-prompting-for-everyone
- **Kind:** course
- **Contributes:** Why models agree with you (trained on thumbs-up feedback) and how to ask neutrally instead.
- **Cited by:** C005
- **Read with:** S010
- **Research label:** `S010-c` in `research/concepts/verification-line.md`

### S093 Vibe coding and agentic engineering are getting closer than I'd like

- **Author:** Simon Willison
- **Date:** 2026-05-06
- **URL:** https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/
- **Kind:** essay
- **Contributes:** Polish is free now; normalization of deviance; vibe coding is fine only where a bug hurts only you.
- **Cited by:** C005, C007, C009, C015, C016; group notes G01
- **Read with:** S028
- **Research label:** `S028-c4` in `research/concepts/verification-line.md`; `S028-c4` in `research/concepts/checking-work.md`

### S094 Finding and fixing bugs (Cursor Learn)

- **Author:** Cursor
- **Date:** Undated (first archived 2026-02-16; revised by 2026-09-02)
- **URL:** https://cursor.com/learn/finding-fixing-bugs
- **Kind:** course
- **Contributes:** How agents debug now (hypotheses, logging, console, network and monitoring data), and asking whether a fix treats the cause.
- **Cited by:** C005, C019
- **Read with:** S009
- **Research label:** `S009-c` in `research/concepts/verification-line.md`; `S009-c` in `research/concepts/checking-work.md`

### S095 From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents

- **Author:** Laksh Advani
- **Date:** 2026-06-01
- **URL:** https://arxiv.org/html/2606.09863
- **Kind:** paper
- **Contributes:** False-success rates by model; thinking models gave no protection; LLM judges never beat AUROC 0.65.
- **Cited by:** C005, C011, C014; group notes G04
- **Read with:** S030
- **Research label:** `S030-c1` in `research/concepts/verification-line.md`; `S030-c1` in `research/concepts/checking-work.md`

### S096 A Paradox of AI Fluency

- **Author:** Christopher Potts, Moritz Sudhof
- **Date:** 2026-04-28 (chat data 2023-05 to 2025-07, older models)
- **URL:** https://arxiv.org/abs/2604.25905
- **Kind:** paper
- **Contributes:** Invisible failures: 85.6% of minimal-fluency users' failures looked like success to them, against 22.1% for fluent users.
- **Cited by:** C006, C016; group notes G04
- **Read with:** S085
- **Research label:** `S085-c` in `research/concepts/verification-line.md`; `S085-c` in `research/concepts/checking-work.md`

### S097 (Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding

- **Author:** Balepur, Baumler, Chen, Choi, Rudinger, Boyd-Graber
- **Date:** 2026-07-29 (preprint; rated medium credibility in sources-candidates.md)
- **URL:** https://arxiv.org/abs/2607.26375
- **Kind:** paper
- **Contributes:** 54 students: agents helped them finish but harmed their comprehension, and low-effort use went with lower comprehension.
- **Cited by:** C010; group notes G01
- **Research label:** `X1` in `research/concepts/verification-line.md`

### S098 nomArmy findings (docs/findings.md)

- **Author:** rayson-tech
- **Date:** Data 2026-09-18 to 2026-10-04; last committed 2026-10-04
- **URL:** https://github.com/rayson-tech/nomarmy/blob/main/docs/findings.md
- **Kind:** report
- **Contributes:** A real job log: 24 of 265 'done, tests pass' claims were false, and naming a failure mode in the brief took a job from 1 of 3 real tests to 3 of 3.
- **Cited by:** C011, C013, C015; group notes G04
- **Read with:** S030
- **Research label:** `S030-c2` in `research/concepts/verification-line.md`; `S030-c2` in `research/concepts/checking-work.md`

### S099 MCP problem en code problem (Cursor forum)

- **Author:** Jeffrey Barts
- **Date:** 2026-09-26 (no replies)
- **URL:** https://forum.cursor.com/t/173052
- **Kind:** thread
- **Contributes:** Cloud agents reported an OAuth MCP server as 'working' for three days while their tests never touched the public path.
- **Cited by:** C011, C015, C019, C095, C099, C102
- **Research label:** `CF-173052` in `research/concepts/checking-work.md`; `G10-05` in `research/concepts/running-alone.md`

### S100 Missing Semester 2026: Code Quality lecture

- **Author:** MIT Missing Semester
- **Date:** Page undated; 2026-01-23 per the sweep notes (older than three months, still current)
- **URL:** https://missing.csail.mit.edu/2026/code-quality/
- **Kind:** course
- **Contributes:** Break the code on purpose to confirm CI catches it, and ask whether the AI's own tests are any good.
- **Cited by:** C013, C017
- **Research label:** `MS-CQ` in `research/concepts/checking-work.md`

### S101 How Claude Code works (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs
- **URL:** https://code.claude.com/docs/en/how-claude-code-works
- **Kind:** docs
- **Contributes:** The 'agentic harness' around the model, the loop, a fresh context per session, and transcripts as a separate store.
- **Cited by:** C021, C022, C023, C025, C026, C027
- **Read with:** S015
- **Research label:** `MHC-X01` in `research/concepts/model-harness-context.md`

### S102 Claude Cowork and chat are now one Claude

- **Author:** Anthropic (Claude blog)
- **Date:** 2026-09-16
- **URL:** https://claude.com/blog/cowork-is-now-claude
- **Kind:** news
- **Contributes:** The chat/Cowork merge: Claude now decides whether a request is a quick answer or a task.
- **Cited by:** C022
- **Research label:** `MHC-X04` in `research/concepts/model-harness-context.md`

### S103 How are people handling context across different AI coding tools? (Cursor forum)

- **Author:** Pat2; replies by Dean Rie (Cursor staff)
- **Date:** 2026-05-06
- **URL:** https://forum.cursor.com/t/159891
- **Kind:** thread
- **Contributes:** People re-explain projects to every tool, and stale memories 'quietly poison' recommendations.
- **Cited by:** C023, C027
- **Research label:** `MHC-X13` in `research/concepts/model-harness-context.md`

### S104 How long do you store my data? (Anthropic Privacy Center)

- **Author:** Anthropic
- **Date:** Updated 2026-07-01
- **URL:** https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
- **Kind:** docs
- **Contributes:** Consumer vs commercial retention, and data kept up to five years for training when model improvement is on.
- **Cited by:** C023, C103
- **Read with:** S069
- **Research label:** `MHC-X05` in `research/concepts/model-harness-context.md`; `BC01` in `research/concepts/beyond-code.md`

### S105 Explore the context window (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (mentions v2.1.198)
- **URL:** https://code.claude.com/docs/en/context-window
- **Kind:** docs
- **Contributes:** Everything that loads before you type, shown event by event, and how to inspect it with /context.
- **Cited by:** C023, C025, C026, C027, C028
- **Read with:** S015
- **Research label:** `MHC-X02` in `research/concepts/model-harness-context.md`

### S106 Ask HN: I still don't understand why AI agents need "skills"

- **Author:** skeptic_ai and 18 commenters
- **Date:** 2026-08-02
- **URL:** https://news.ycombinator.com/item?id=49139845
- **Kind:** thread
- **Contributes:** Real beginner questions about skills: why not one big AGENTS.md (lazy loading, context pollution), and how to vet a skill without reading it.
- **Cited by:** C025, C026, C091
- **Research label:** `MHC-X14` in `research/concepts/model-harness-context.md`; `SC08` in `research/concepts/supply-chain.md`

### S107 The Context Tax: When to Compact

- **Author:** Rogerio Chaves (LangWatch)
- **Date:** 2026-08-02
- **URL:** https://langwatch.ai/blog/context-tax-when-to-compact
- **Kind:** report
- **Contributes:** A measured compaction study: about 8k tokens in use as the window grew, cost rising with context, when to compact, and forked subagents' runaway tokens.
- **Cited by:** C026, C027, C028, C056; group notes G04
- **Research label:** `MHC-X03` in `research/concepts/model-harness-context.md`; `X02` in `research/concepts/cost-limits.md`

### S108 Image generation, 'Nano Banana' (Gemini API docs)

- **Author:** Google
- **Date:** Last updated 2026-10-09
- **URL:** https://ai.google.dev/gemini-api/docs/image-generation
- **Kind:** docs
- **Contributes:** Image models that reason before drawing, take reference images and bill thinking tokens by default.
- **Cited by:** C029, C032
- **Research label:** `MHC-X09` in `research/concepts/model-harness-context.md`

### S109 Playback: Aaron's prompt on what 'Opus 5.5 made this' videos leave out

- **Author:** Aaron Orelup (typed prompt)
- **Date:** 2026-10-03
- **URL:** playback-lens session 271db68b-18fe-40eb-bf03-9ff7bf1c1529 (project C--Users-soulo-Organized-Personal-My-Projects-My-Blog), line 579
- **Kind:** aaron-practice
- **Contributes:** One-prompt media hides a pipeline; models have a house taste; an expert in each craft should be the prompter.
- **Cited by:** C030, C032, C134
- **Research label:** `MHC-X12` in `research/concepts/model-harness-context.md`

### S110 AO-030: Claude rendered 223 clips of my game's robot voice, and couldn't hear any of them

- **Author:** Aaron Orelup
- **Date:** 2026-10-02
- **URL:** https://aaronorelup.com/ledger/remora-voice-lab/
- **Kind:** aaron-practice
- **Contributes:** An agent can generate and measure variants it cannot hear; pin seeds and loudness so the human's comparison is fair.
- **Cited by:** C030, C032
- **Research label:** `MHC-X10` in `research/concepts/model-harness-context.md`

### S111 AO-044: Nine Claudes painted the same picture in oil, and the first tries were the art

- **Author:** Aaron Orelup
- **Date:** 2026-10-11
- **URL:** https://aaronorelup.com/ledger/nine-claudes-one-painting/
- **Kind:** aaron-practice
- **Contributes:** One prompt across three models and three effort levels gave very different results; effort on a creative task.
- **Cited by:** C030, C059
- **Research label:** `MHC-X11` in `research/concepts/model-harness-context.md`; `X14` in `research/concepts/cost-limits.md`

### S112 Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things

- **Author:** Simon Willison
- **Date:** 2026-08-16
- **URL:** https://simonwillison.net/2026/Aug/16/qwen-38-27b/
- **Kind:** essay
- **Contributes:** A local model is a file, a runtime and settings, and a bad default turned one answer into 21 minutes of reasoning.
- **Cited by:** C031
- **Research label:** `MHC-X06` in `research/concepts/model-harness-context.md`

### S113 Vision (Claude Platform Docs)

- **Author:** Anthropic
- **Date:** Undated live docs (names Opus 5 and Claude 4.7+)
- **URL:** https://platform.claude.com/docs/en/build-with-claude/vision
- **Kind:** docs
- **Contributes:** Claude reads images but cannot make them; how images are counted in tokens; images resent on every turn.
- **Cited by:** C032
- **Research label:** `MHC-X07` in `research/concepts/model-harness-context.md`

### S114 Understand and count tokens (Gemini API docs)

- **Author:** Google
- **Date:** Last updated 2026-09-23
- **URL:** https://ai.google.dev/gemini-api/docs/tokens
- **Kind:** docs
- **Contributes:** How Gemini counts tokens for images, audio and video.
- **Cited by:** C032
- **Research label:** `MHC-X08` in `research/concepts/model-harness-context.md`

### S115 Human judgment doesn't leave the software factory. It relocates.

- **Author:** Addy Osmani
- **Date:** 2026-08-21
- **URL:** https://addyosmani.com/blog/human-judgment-doesnt-leave-the-software/
- **Kind:** essay
- **Contributes:** Typing falls but ownership doesn't; an agent dropped a sign-in provider customers wanted because the UI had room for three.
- **Cited by:** C033, C034, C038, C041, C043; group notes G04
- **Research label:** `G04-N4` in `research/concepts/directing-work.md`

### S116 My AI Adoption Journey

- **Author:** Mitchell Hashimoto
- **Date:** 2026-02-05 (he says he has no ties to AI companies)
- **URL:** https://mitchellh.com/writing/my-ai-adoption-journey
- **Kind:** essay
- **Contributes:** A practitioner's path: do real work in an agent, not a chat window; slice work small; delegation has overhead.
- **Cited by:** C033, C036, C040, C041, C042, C043; group notes G04
- **Research label:** `G04-N5` in `research/concepts/directing-work.md`

### S117 Best practices for Claude Code

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated; content no earlier than 2026-09-25 (names v2.1.283)
- **URL:** https://code.claude.com/docs/en/best-practices
- **Kind:** docs
- **Contributes:** Give the agent a check it can run; explore, plan, then implement; interview mode; clear and restart after two failed corrections.
- **Cited by:** C004, C013, C034, C035, C036, C037, C038, C039, C040, C041, C042, C054, C097, C117, C124; group notes G04, G13
- **Research label:** `G04-N1` in `research/concepts/directing-work.md`

### S118 Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop (AI Engineer World's Fair 2026)

- **Author:** Gabriel Martinez (G2i)
- **Date:** 2026-10-09 (YouTube upload date)
- **URL:** https://ai.engineer/talks/6qkzlT962es (video: https://www.youtube.com/watch?v=6qkzlT962es)
- **Kind:** talk
- **Contributes:** Polished output hides the decisions it made; prototypes mislead; review is the bottleneck. His judgment, not measurement; ends with a product plug.
- **Cited by:** C034, C036, C037, C040, C041, C043; group notes G04
- **Research label:** `G04-N3` in `research/concepts/directing-work.md`

### S119 Anthropic Education Report: The AI Fluency Index

- **Author:** Kristen Swanson, Drew Bent, Zoe Ludwig, Rick Dakan, Joe Feller (Anthropic)
- **Date:** 2026-02-23 per the page (BibTeX 2026-02-16; data 2026-01-20 to 01-26)
- **URL:** https://academy.claude.com/tutorials/the-ai-fluency-index
- **Kind:** report
- **Contributes:** Only 30% of conversations set the terms of the collaboration, and people building artifacts flag missing context less.
- **Cited by:** C035, C037; group notes G04
- **Research label:** `G04-N7` in `research/concepts/directing-work.md`

### S120 From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI

- **Author:** Margaret-Anne Storey
- **Date:** v1 2026-03-23, v4 2026-04-06 (abstract read)
- **URL:** https://arxiv.org/abs/2603.22106
- **Kind:** paper
- **Contributes:** 'Intent debt': the missing rationale, goals and constraints that humans and agents both need.
- **Cited by:** C035; group notes G04
- **Research label:** `G04-N6` in `research/concepts/directing-work.md`

### S121 Output styles (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated; content no earlier than 2026-08-20 (names v2.1.237)
- **URL:** https://code.claude.com/docs/en/output-styles
- **Kind:** docs
- **Contributes:** Proactive, Explanatory and Learning styles change how much the agent assumes and how much it teaches.
- **Cited by:** C035, C036; group notes G04
- **Research label:** `G04-N2` in `research/concepts/directing-work.md`

### S122 Spec-Driven Development with Coding Agents

- **Author:** Paul Everitt (JetBrains), DeepLearning.AI
- **Date:** Updated 2026-04-18 (course page and outline read)
- **URL:** https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents
- **Kind:** course
- **Contributes:** Specs live in version control next to the code; vibe coding does not extend a codebase you didn't write.
- **Cited by:** C040
- **Research label:** `G04-N8` in `research/concepts/directing-work.md`

### S123 How Claude remembers your project: CLAUDE.md, AGENTS.md, rules, auto memory (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated; mentions versions up to v2.1.285 (released 2026-09-29)
- **URL:** https://code.claude.com/docs/en/memory
- **Kind:** docs
- **Contributes:** Which instruction files load and when, AGENTS.md support, path-scoped rules, and the /doctor prompt audit.
- **Cited by:** C044, C045, C046, C047, C048, C049, C051, C052; group notes G05
- **Read with:** S015
- **Research label:** `X01` in `research/concepts/configuring-agent.md`

### S124 Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents

- **Author:** Michael Segner (Anthropic)
- **Date:** 2026-06-18
- **URL:** https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- **Kind:** docs
- **Contributes:** Which extension fits which job, hooks as deterministic control, and giving the instruction file an owner.
- **Cited by:** C044, C045
- **Research label:** `X06` in `research/concepts/configuring-agent.md`

### S125 Claude Code changelog

- **Author:** Anthropic
- **Date:** Entries read: v2.1.282 (2026-09-24) to v2.1.296 (2026-10-09)
- **URL:** https://code.claude.com/docs/en/changelog
- **Kind:** docs
- **Contributes:** Dated changes behind the 'it changes every week' point: hook semantics, skill names, the prompt audit.
- **Cited by:** C044, C045, C046, C048, C049, C050, C052
- **Research label:** `X05` in `research/concepts/configuring-agent.md`

### S126 When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls

- **Author:** Ting Yan
- **Date:** 2026-08-24 (arXiv submission; abstract read)
- **URL:** https://arxiv.org/abs/2608.23550
- **Kind:** paper
- **Contributes:** Only 4.4% of security rules in 481 public CLAUDE.md files have a matching built-in control: a 'write-only channel'.
- **Cited by:** C045; group notes G05
- **Research label:** `X08` in `research/concepts/configuring-agent.md`

### S127 Automate actions with hooks (Claude Code hooks guide)

- **Author:** Anthropic
- **Date:** Undated live docs
- **URL:** https://code.claude.com/docs/en/hooks-guide
- **Kind:** docs
- **Contributes:** How a hook blocks (exit code 2 or a deny decision), how to test one, and what a hook cannot loosen.
- **Cited by:** C045, C049, C054
- **Research label:** `X03` in `research/concepts/configuring-agent.md`

### S128 How Claude Code uses prompt caching (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated; mentions up to v2.1.283 (2026-09-25)
- **URL:** https://code.claude.com/docs/en/prompt-caching
- **Kind:** docs
- **Contributes:** What breaks the cache, when instruction-file edits take effect, and which effort changes keep the cache.
- **Cited by:** C046, C051, C052, C055, C056, C057, C059; group notes G06
- **Read with:** S015 and S016
- **Research label:** `X02` in `research/concepts/configuring-agent.md`; `X03` in `research/concepts/cost-limits.md`

### S129 Use Claude Code in the cloud (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (mentions v2.1.289)
- **URL:** https://code.claude.com/docs/en/claude-code-on-the-web
- **Kind:** docs
- **Contributes:** A cloud session clones the pushed branch, not your local checkout; untracked files never travel.
- **Cited by:** C046, C047
- **Research label:** `X07` in `research/concepts/configuring-agent.md`

### S130 Skills (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated; mentions v2.1.282 (2026-09-24)
- **URL:** https://code.claude.com/docs/en/skills
- **Kind:** docs
- **Contributes:** Skills load by their description; fields and limits; where personal skills don't load.
- **Cited by:** C046, C049, C050, C051
- **Read with:** S015
- **Research label:** `X04` in `research/concepts/configuring-agent.md`

### S131 Errors reference: usage limits and credit balance (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated; cites up to v2.1.296 (2026-10-09)
- **URL:** https://code.claude.com/docs/en/errors
- **Kind:** docs
- **Contributes:** Usage-limit and credit errors, the stray API key that bills the wrong meter, and the session and weekly windows.
- **Cited by:** C055, C061; group notes G06
- **Read with:** S016
- **Research label:** `X05` in `research/concepts/cost-limits.md`

### S132 Using Claude Code with your Pro or Max plan (Claude Help Center)

- **Author:** Anthropic
- **Date:** 'Updated this week' as of 2026-10-12
- **URL:** https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan
- **Kind:** docs
- **Contributes:** A set ANTHROPIC_API_KEY bills the API instead of your plan; plan limits are shared between Claude and Claude Code.
- **Cited by:** C055
- **Read with:** S016
- **Research label:** `X06` in `research/concepts/cost-limits.md`

### S133 CLI reference (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (cites up to v2.1.290)
- **URL:** https://code.claude.com/docs/en/cli-reference
- **Kind:** docs
- **Contributes:** Hard stops for unattended runs (--max-budget-usd, --max-turns) and checking which account is billed.
- **Cited by:** C055, C059, C061, C095, C096
- **Research label:** `X09` in `research/concepts/cost-limits.md`; `G10-12` in `research/concepts/running-alone.md`

### S134 Interactive mode: Wait for a usage limit to reset (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (feature needs v2.1.234 or later)
- **URL:** https://code.claude.com/docs/en/interactive-mode
- **Kind:** docs
- **Contributes:** Automatic continuation after a usage-limit reset, and how to turn it off.
- **Cited by:** C055, C060
- **Research label:** `X10` in `research/concepts/cost-limits.md`

### S135 Claude Haiku 5.5

- **Author:** Simon Willison
- **Date:** 2026-10-07
- **URL:** https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/
- **Kind:** essay
- **Contributes:** Prices move under you: Sonnet 5.5 cache reads halved, and new monthly API credits for Max and Team.
- **Cited by:** C055, C057, C058, C059; group notes G06
- **Research label:** `X08` in `research/concepts/cost-limits.md`

### S136 Context Engineering in 2026: Why We Stopped Compacting Our Agent's Context

- **Author:** Louis-François Bouchard
- **Date:** 2026-08-18
- **URL:** https://www.louisbouchard.ai/context-engineering-2026/
- **Kind:** essay
- **Contributes:** Summarizing cost a team about twice as much as keeping full history, because it rewrote the cached prefix.
- **Cited by:** C056, C057
- **Research label:** `X13` in `research/concepts/cost-limits.md`

### S137 Pricing (Claude Platform Docs)

- **Author:** Anthropic
- **Date:** Undated live docs
- **URL:** https://platform.claude.com/docs/en/about-claude/pricing
- **Kind:** docs
- **Contributes:** Current per-token prices and the cache write and read multipliers.
- **Cited by:** C057, C058, C060; group notes G06
- **Research label:** `X07` in `research/concepts/cost-limits.md`

### S138 Model configuration: effort levels and default model (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (cites up to v2.1.293)
- **URL:** https://code.claude.com/docs/en/model-config
- **Kind:** docs
- **Contributes:** Effort levels and per-model defaults, and a saved setting that silently doesn't apply.
- **Cited by:** C059
- **Research label:** `X04` in `research/concepts/cost-limits.md`

### S139 We're going to need default hard budget caps on pretty much everything

- **Author:** Simon Willison
- **Date:** 2026-10-03
- **URL:** https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
- **Kind:** essay
- **Contributes:** Soft caps 'will not cut it', and agents spin up services that keep billing after the run.
- **Cited by:** C060, C061, C105; group notes G06
- **Research label:** `X01` in `research/concepts/cost-limits.md`; `BC14` in `research/concepts/beyond-code.md`

### S140 Google users fight for refunds as unauthorized API usage bills soar

- **Author:** O'Ryan Johnson (The Register)
- **Date:** 2026-05-13 (later updated on reimbursement)
- **URL:** https://www.theregister.com/ai-ml/2026/05/13/google-users-fight-for-refunds-as-unauthorized-api-usage-bills-soar/5239160
- **Kind:** news
- **Contributes:** Caps that are only alerts: a $10,138 bill, and a $250 cap raised automatically to about $100,000.
- **Cited by:** C061
- **Read with:** S020
- **Research label:** `X11` in `research/concepts/cost-limits.md`

### S141 Purpose-built model for leaked secret detection (GitHub Changelog)

- **Author:** GitHub
- **Date:** 2026-10-07
- **URL:** https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection
- **Kind:** docs
- **Contributes:** 'Budget alerts alone don't stop usage', and AI push-protection checks that consume credits.
- **Cited by:** C061
- **Read with:** S047
- **Research label:** `X12` in `research/concepts/cost-limits.md`

### S142 Ask HN: Client took over development by vibe coding. What to do?

- **Author:** piscator; audit comment by HyprMusic
- **Date:** 2026-04-01
- **URL:** https://news.ycombinator.com/item?id=47599303
- **Kind:** thread
- **Contributes:** A first-hand audit of a vibe-coded marketplace: anyone could become admin and set their own checkout price.
- **Cited by:** C062, C067, C124, C127, C129; group notes G13
- **Research label:** `G07-N9` in `research/concepts/securing-what-you-build.md`

### S143 Ask HN: Is vibe coding bad for SaaS projects?

- **Author:** gsngsn and replies
- **Date:** 2026-10-01
- **URL:** https://news.ycombinator.com/item?id=49921770
- **Kind:** thread
- **Contributes:** A real beginner question about shipping a vibe-coded SaaS product.
- **Cited by:** C062, C066
- **Research label:** `G07-N10` in `research/concepts/securing-what-you-build.md`

### S144 Ask HN: How do you deal with cyber attacks once you scale?

- **Author:** cehgmaster and replies
- **Date:** 2026-09-24
- **URL:** https://news.ycombinator.com/item?id=49826381
- **Kind:** thread
- **Contributes:** Practitioners: managers' vibe-coded mini-tools are a new attack vector; pen-test early.
- **Cited by:** C062, C063, C072, C118
- **Research label:** `G07-N13` in `research/concepts/securing-what-you-build.md`

### S145 GLM-5.3 and the spread of advanced cyber capabilities

- **Author:** Anthropic Frontier Red Team (Andrew Fasano, Marius Fleischer, Cole McFaul, Robert Xiao, Tripp Gallagher)
- **Date:** 2026-09-29
- **URL:** https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
- **Kind:** report
- **Contributes:** A downloadable open-weight model with near-Mythos exploit skill and safeguards Anthropic's tests bypassed 64-100% of the time (Anthropic is analysing a competitor's model).
- **Cited by:** C063; group notes G07
- **Research label:** `G07-N4` in `research/concepts/securing-what-you-build.md`

### S146 Ask HN: Which frontier model can do code security reviews

- **Author:** Bender and replies
- **Date:** 2026-10-07
- **URL:** https://news.ycombinator.com/item?id=49996594
- **Kind:** thread
- **Contributes:** Hobbyists find frontier models refusing security reviews, which adds to the confusion about who can check.
- **Cited by:** C063, C072, C118
- **Research label:** `G07-N12` in `research/concepts/securing-what-you-build.md`

### S147 Security-Focused Guide for AI Code Assistant Instructions

- **Author:** OpenSSF Best Practices and AI/ML Working Groups
- **Date:** 2025-08-01 (foundational and still current; no newer version found)
- **URL:** https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions
- **Kind:** framework
- **Contributes:** Concise, specific security instructions help; persona prompts like 'act as a security expert' don't.
- **Cited by:** C064
- **Research label:** `G07-N5` in `research/concepts/securing-what-you-build.md`

### S148 Breaking Change: Tables not exposed to Data and GraphQL API automatically (Supabase discussion #45329)

- **Author:** Supabase (inian; replies by avallete and maintainers)
- **Date:** 2026-04-28 (replies to 2026-06-13; applies to new projects from 2026-05-30, all projects from 2026-10-30)
- **URL:** https://github.com/orgs/supabase/discussions/45329
- **Kind:** docs
- **Contributes:** Supabase's new default: tables are not exposed until granted, and its agent skill includes the grant step.
- **Cited by:** C064, C065, C066, C068, C072
- **Research label:** `G07-N1` in `research/concepts/securing-what-you-build.md`

### S149 The OWASP Top 10 for Vibe-Coded Applications (Part 2)

- **Author:** Simon Roses Femerling (VULNEX)
- **Date:** 2026-04-23
- **URL:** https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/
- **Kind:** essay
- **Contributes:** A pentester's findings, such as missing tenant isolation being a redesign, not a patch (read through a summarising fetch; use only its quoted lines).
- **Cited by:** C053, C066, C067, C068, C072, C118, C119, C130; group notes G07, G13
- **Research label:** `G07-N6` in `research/concepts/securing-what-you-build.md`

### S150 Lovable left thousands of projects exposed for 48 days, and the vibe coding security crisis is only getting worse

- **Author:** Allison Steffens Herrera (The Next Web)
- **Date:** 2026-04-21 (modified 2026-05-07)
- **URL:** https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed
- **Kind:** news
- **Contributes:** Incident reports only: a showcased app with inverted access logic exposed 18,697 user records.
- **Cited by:** C067, C068, C069; group notes G07
- **Research label:** `G07-N7` in `research/concepts/securing-what-you-build.md`

### S151 Feature Preview: RLS Tester (Supabase discussion #45233)

- **Author:** Supabase (joshenlim)
- **Date:** 2026-04-24 (development later paused)
- **URL:** https://github.com/orgs/supabase/discussions/45233
- **Kind:** docs
- **Contributes:** Supabase itself says verifying row-level security 'has always been a gap'.
- **Cited by:** C068, C072
- **Research label:** `G07-N3` in `research/concepts/securing-what-you-build.md`

### S152 Securing your API (Supabase Docs)

- **Author:** Supabase
- **Date:** Live docs, page modified 2026-10-12
- **URL:** https://supabase.com/docs/guides/api/securing-your-api
- **Kind:** docs
- **Contributes:** Access has two layers, grants (can a role reach the table at all) and row-level security (which rows), and Supabase says to use both on every exposed object.
- **Cited by:** C068
- **Research label:** `G07-N2` in `research/concepts/securing-what-you-build.md`

### S153 Playback: Aaron's questions about storing keys for agents without plain text

- **Author:** Aaron Orelup (typed prompts)
- **Date:** 2026-09-30 and 2026-10-02
- **URL:** playback-lens session a5e52ad1-214b-4d69-b9f4-16e9967ae704 (project C--Users-soulo-Organized-Personal-My-Projects-Sandbox-2), line 3; and hidden-curriculum session 88a586af-a275-481a-b481-23bf805cba04
- **Kind:** aaron-practice
- **Contributes:** A heavy user's real need: giving agents keys without plain-text files (topics only).
- **Cited by:** C069, C070
- **Research label:** `G07-N14` in `research/concepts/securing-what-you-build.md`

### S154 We scanned 100 Lovable apps for GDPR and security. Not one came back clean.

- **Author:** Vespez Research
- **Date:** October 2026 (posted to Hacker News 2026-10-07)
- **URL:** https://vespez.com/research/lovable-100
- **Kind:** report
- **Contributes:** A vendor's automated scan (unverified, low weight): one showcase app exposed a live OpenAI key in its frontend.
- **Cited by:** C069, C119; group notes G07
- **Research label:** `G07-N8` in `research/concepts/securing-what-you-build.md`

### S155 Ask HN: Anyone else's OpenAI and Claude API keys mysteriously leaked last night?

- **Author:** par
- **Date:** 2026-09-25
- **URL:** https://news.ycombinator.com/item?id=49845022
- **Kind:** thread
- **Contributes:** Keys kept 'only on my laptop and my server, not on GitHub' still leaked.
- **Cited by:** C070, C071
- **Research label:** `G07-N11` in `research/concepts/securing-what-you-build.md`

### S156 Codex: Agent approvals & security

- **Author:** OpenAI (Codex docs)
- **Date:** Undated live docs (references Codex 0.115)
- **URL:** https://learn.chatgpt.com/docs/agent-approvals-security
- **Kind:** docs
- **Contributes:** The non-Anthropic view: approval policy and sandbox are separate settings, network is off by default, and Codex sandboxes on Windows.
- **Cited by:** C078, C079, C081, C082, C128; group notes G08
- **Research label:** `[Codex docs]` in `research/concepts/agent-power.md`

### S157 Using threat modeling and prompt injection to audit Comet

- **Author:** Trail of Bits
- **Date:** 2026-02-20 (describes an audit done in April 2025)
- **URL:** https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/
- **Kind:** report
- **Contributes:** A fake CAPTCHA and fake 'system' text got an AI browser assistant to send a user's Gmail to an attacker.
- **Cited by:** C086, C093, C104
- **Research label:** `SC07` in `research/concepts/supply-chain.md`; `BC09` in `research/concepts/beyond-code.md`

### S158 Mini Shai-Hulud: npm Worm Targets AI Developer Supply Chain (CSA research note)

- **Author:** CSA AI Safety Initiative
- **Date:** 2026-05-17
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-ai-supply-chain-20260517-csa-st/
- **Kind:** incident
- **Contributes:** The first documented supply-chain attack to forge valid SLSA provenance, with a postinstall payload.
- **Cited by:** C088, C089
- **Research label:** `SC04` in `research/concepts/supply-chain.md`

### S159 Our plan for a more secure npm supply chain

- **Author:** Xavier René-Corail (GitHub Security Lab)
- **Date:** 2025-09-22 (older than 12 months; dated background only)
- **URL:** https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/
- **Kind:** news
- **Contributes:** Background on the original Shai-Hulud worm and install scripts as its vector.
- **Cited by:** C088
- **Research label:** `SC10` in `research/concepts/supply-chain.md`

### S160 Configure permissions: project allow rules, workspace trust, and what runs before you trust a folder (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (mentions v2.1.207)
- **URL:** https://code.claude.com/docs/en/permissions
- **Kind:** docs
- **Contributes:** What runs before or without the workspace-trust prompt; headless runs skip it entirely.
- **Cited by:** C089, C090, C091
- **Research label:** `SC06` in `research/concepts/supply-chain.md`

### S161 OpenClaw: How the Viral AI Agent Became 2026's First Major Security Crisis

- **Author:** Hive Security (no author named)
- **Date:** 2026-05-07
- **URL:** https://hivesecurity.gitlab.io/blog/openclaw-ai-agent-security-crisis-2026/
- **Kind:** report
- **Contributes:** A medium-credibility compilation: 1,184 malicious skills by 2026-02-28 and 'ClickFix-style' lures (used only where labelled).
- **Cited by:** C091, C093, C105
- **Research label:** `SC09` in `research/concepts/supply-chain.md`; `BC11` in `research/concepts/beyond-code.md`

### S162 Plugin4Shell - Zero Click RCE Vulnerability found in top 4 most popular coding agents

- **Author:** Or Nevo, Dor Granat, Niv Hoffman (Air Security)
- **Date:** 2026-09-17
- **URL:** https://www.air.security/blog-posts/plugin4shell
- **Kind:** incident
- **Contributes:** Zero-click plugin swaps in four major coding agents, and version pins that nothing actually checks.
- **Cited by:** C091, C092
- **Research label:** `SC01` in `research/concepts/supply-chain.md`

### S163 A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors

- **Author:** Pengxun Li, Litian Zhang, Jianwei Hou, Shujiang Wu, Song Li, Zifeng Kang, Xi Zhang
- **Date:** v1 2026-09-03, v2 2026-09-08 (abstract read)
- **URL:** https://arxiv.org/abs/2609.03884
- **Kind:** paper
- **Contributes:** HookPry: trojanized hook updates compromised all seven agent harnesses tested.
- **Cited by:** C091, C092
- **Research label:** `SC02` in `research/concepts/supply-chain.md`

### S164 Agentic MCP Security Best Practices Guide

- **Author:** Cloud Security Alliance labs (no author named)
- **Date:** 2026-03-27 (marked draft)
- **URL:** https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- **Kind:** framework
- **Contributes:** Tool poisoning in tool descriptions, tool-name shadowing, and tool definitions that are not yet signed.
- **Cited by:** C092
- **Research label:** `SC05` in `research/concepts/supply-chain.md`

### S165 Top AI coding agent security resources - October 2026

- **Author:** Adversa AI team
- **Date:** 2026-10-02
- **URL:** https://adversa.ai/blog/top-ai-coding-agent-security-resources-october-2026/
- **Kind:** list
- **Contributes:** Advice lines only (medium credibility): check that a pinned hash is what actually landed; pause automatic plugin updates.
- **Cited by:** C092
- **Research label:** `SC03` in `research/concepts/supply-chain.md`

### S166 Claude Code in Action (course outline)

- **Author:** Anthropic Academy
- **Date:** Undated (footer © 2026)
- **URL:** https://anthropic.skilljar.com/claude-code-in-action
- **Kind:** course
- **Contributes:** A vendor course with lessons on routines, headless runs and verifying unsupervised runs.
- **Cited by:** C094, C101
- **Research label:** `G10-19` in `research/concepts/running-alone.md`

### S167 Automate work with routines, research preview (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (cites up to v2.1.268 and a 2026-04-01 beta header)
- **URL:** https://code.claude.com/docs/en/routines
- **Kind:** docs
- **Contributes:** Cloud routines: triggers, research-preview status, and commits and messages that appear under your name.
- **Cited by:** C094, C098, C099, C100, C102, C135
- **Research label:** `G10-08` in `research/concepts/running-alone.md`

### S168 Schedule recurring tasks in Claude Code Desktop

- **Author:** Anthropic
- **Date:** Undated live docs (cites Claude Desktop 1.1.5368)
- **URL:** https://code.claude.com/docs/en/desktop-scheduled-tasks
- **Kind:** docs
- **Contributes:** Desktop tasks need the app open, and a task waiting for approval stalls until you come back.
- **Cited by:** C094, C096, C099, C102
- **Research label:** `G10-09` in `research/concepts/running-alone.md`

### S169 Run prompts on a schedule (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (cites up to v2.1.248)
- **URL:** https://code.claude.com/docs/en/scheduled-tasks
- **Kind:** docs
- **Contributes:** A /loop task lives inside one open session and expires after seven days.
- **Cited by:** C094, C096, C102
- **Research label:** `G10-10` in `research/concepts/running-alone.md`

### S170 AO-019: An agent confessed to deleting 19 GB I had asked another agent to delete

- **Author:** Aaron Orelup
- **Date:** 2026-09-26 (events 2026-09-15)
- **URL:** https://aaronorelup.com/ledger/the-confession-that-spread/
- **Kind:** aaron-practice
- **Contributes:** Sessions on one machine can't see each other's work, and a false confession spread into notes as a 'hard rule'.
- **Cited by:** C094, C095, C098; group notes G10
- **Research label:** `G10-16` in `research/concepts/running-alone.md`

### S171 AO-032: I told Claude to find the best Opus 5.5 trick on X and do it without me

- **Author:** Aaron Orelup
- **Date:** 2026-10-03
- **URL:** https://aaronorelup.com/ledger/opus-55-on-x-alone/
- **Kind:** aaron-practice
- **Contributes:** An autonomous run made eight decisions alone, used his signed-in browser and published to his live site.
- **Cited by:** C094, C096; group notes G10
- **Research label:** `G10-14` in `research/concepts/running-alone.md`

### S172 Run agents in parallel (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs
- **URL:** https://code.claude.com/docs/en/agents
- **Kind:** docs
- **Contributes:** Parallel sessions multiply token use; agent teams are experimental and share one set of files.
- **Cited by:** C094, C095
- **Research label:** `G10-13` in `research/concepts/running-alone.md`

### S173 Keep Claude working toward a goal (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs (cites up to v2.1.269)
- **URL:** https://code.claude.com/docs/en/goal
- **Kind:** docs
- **Contributes:** When /goal stops on its own, and when it pauses on a usage limit.
- **Cited by:** C096
- **Research label:** `G10-11` in `research/concepts/running-alone.md`

### S174 [Windows] Agent Shell: rmdir /s with trailing \ before " escapes target and wipes volume root (Cursor forum)

- **Author:** Aleksey Solodkevich (Aleksey_Nm); staff reply by Mohit (Cursor)
- **Date:** 2026-07-29 (staff reply 2026-07-30)
- **URL:** https://forum.cursor.com/t/166931
- **Kind:** incident
- **Contributes:** A shell-quoting slip deleted about 210,000 files in 40 seconds while the agent reported a failed cleanup.
- **Cited by:** C097; group notes G10
- **Research label:** `G10-01` in `research/concepts/running-alone.md`

### S175 Agent wiped D: drive instead of deleting one folder (Cursor forum)

- **Author:** Mr.Cheng; staff replies by Dean Rie (Cursor)
- **Date:** 2026-08-29
- **URL:** https://forum.cursor.com/t/169919
- **Kind:** incident
- **Contributes:** About 80 GB deleted by a command that ran without confirmation.
- **Cited by:** C097, C123; group notes G10
- **Research label:** `G10-02` in `research/concepts/running-alone.md`

### S176 Errible: AI out of control, randomly deleting files, 6-month project wiped out (Cursor forum)

- **Author:** shuang_yang; replies by ActionGate, sattyamjjain
- **Date:** 2026-10-03 (replies to 2026-10-05)
- **URL:** https://forum.cursor.com/t/173688
- **Kind:** incident
- **Contributes:** The user approved the agent's own delete plan; source, .git, the build and both backups went.
- **Cited by:** C097, C098, C123
- **Read with:** S063
- **Research label:** `G10-03` in `research/concepts/running-alone.md`

### S177 What's the last AI-assisted change that created more recovery work than expected? (Cursor forum)

- **Author:** Mohan Iyer; replies by Dean Rie, FinDevAI, speaker
- **Date:** 2026-08-12 (replies to 2026-08-16)
- **URL:** https://forum.cursor.com/t/168209
- **Kind:** thread
- **Contributes:** Recovery toolkits people wish they had set up first, and an agent that took a question as permission.
- **Cited by:** C097, C098; group notes G10
- **Research label:** `G10-04` in `research/concepts/running-alone.md`

### S178 Checkpointing (Claude Code docs)

- **Author:** Anthropic
- **Date:** Undated live docs
- **URL:** https://code.claude.com/docs/en/checkpointing
- **Kind:** docs
- **Contributes:** Rewind does not cover rm, mv or cp run through Bash.
- **Cited by:** C097, C098
- **Research label:** `G10-07` in `research/concepts/running-alone.md`

### S179 Checkpoints and rollbacks (Replit docs)

- **Author:** Replit
- **Date:** Undated
- **URL:** https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks
- **Kind:** docs
- **Contributes:** Rollbacks don't change the production database; state outside the code needs its own way back.
- **Cited by:** C098
- **Read with:** S063
- **Research label:** `G10-06` in `research/concepts/running-alone.md`

### S180 Error handling (n8n Docs)

- **Author:** n8n
- **Date:** Undated
- **URL:** https://docs.n8n.io/flow-logic/error-handling/
- **Kind:** docs
- **Contributes:** The error workflow runs only when an execution fails, so a run that quietly does nothing never triggers it; a Stop and Error node makes it fail loudly.
- **Cited by:** C100
- **Research label:** `G10-18` in `research/concepts/running-alone.md`

### S181 AO-014: I had 801 agent transcripts and no way to read them

- **Author:** Aaron Orelup
- **Date:** 2026-09-01
- **URL:** https://aaronorelup.com/ledger/reading-my-own-agents/
- **Kind:** aaron-practice
- **Contributes:** A subagent died four hours in without anyone noticing: 80 agents started, 79 returned.
- **Cited by:** C100, C102; group notes G10
- **Research label:** `G10-15` in `research/concepts/running-alone.md`

### S182 Healthchecks.io documentation

- **Author:** Healthchecks.io
- **Date:** Undated (footer © 2015-2026); foundational and current
- **URL:** https://healthchecks.io/docs/
- **Kind:** docs
- **Contributes:** Dead man's switches: an alert when a scheduled job stops checking in.
- **Cited by:** C102
- **Research label:** `G10-17` in `research/concepts/running-alone.md`

### S183 PagerDuty Report Finds Two-Thirds (66%) of Office Professionals Have Used Unauthorized AI Tools at Work

- **Author:** PagerDuty (survey by Wakefield Research; vendor-sponsored, n = 1,250)
- **Date:** 2026-06-11
- **URL:** https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/
- **Kind:** survey
- **Contributes:** 86% believed their organization had an AI policy, and 88% had shared work information with AI tools.
- **Cited by:** C103
- **Research label:** `BC07` in `research/concepts/beyond-code.md`

### S184 Use Claude Cowork on web, desktop, and mobile (with 'What changed for Pro and Max plans on October 6')

- **Author:** Anthropic (Claude Help Center)
- **Date:** Last modified 2026-10-06
- **URL:** https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- **Kind:** docs
- **Contributes:** Since 2026-10-06, new Cowork tasks on Pro and Max run in the cloud, which outdates earlier descriptions.
- **Cited by:** C103, C104
- **Research label:** `BC03` in `research/concepts/beyond-code.md`

### S185 Ask HN: What would you include in an academic workshop on vibe coding?

- **Author:** cximenez; reply by jahala
- **Date:** About 2026-09-18 (the page showed '24 days ago' on 2026-10-12)
- **URL:** https://news.ycombinator.com/item?id=49745403
- **Kind:** thread
- **Contributes:** Privacy settings named as one of four things to teach, so unpublished research isn't used for training.
- **Cited by:** C103
- **Research label:** `BC17` in `research/concepts/beyond-code.md`

### S186 Updates to Consumer Terms and Privacy Policy

- **Author:** Anthropic
- **Date:** 2025-08-28 (older than 12 months; foundational, and still current per S104)
- **URL:** https://www.anthropic.com/news/updates-to-our-consumer-terms
- **Kind:** terms
- **Contributes:** The consumer model-training setting and the five-year retention that comes with it.
- **Cited by:** C103
- **Read with:** S069
- **Research label:** `BC02` in `research/concepts/beyond-code.md`

### S187 Use Claude's chat search and memory to build on previous context (Claude Help Center)

- **Author:** Anthropic
- **Date:** Last modified 2026-09-30
- **URL:** https://support.claude.com/en/articles/11817273-using-memory-in-claude
- **Kind:** docs
- **Contributes:** What memory and incognito chats keep, and where memory is not available at all.
- **Cited by:** C103
- **Research label:** `BC04` in `research/concepts/beyond-code.md`

### S188 Let Claude use your computer in Cowork (Claude Help Center)

- **Author:** Anthropic
- **Date:** Last modified 2026-09-16
- **URL:** https://support.claude.com/en/articles/14128542-computer-use-safety
- **Kind:** docs
- **Contributes:** Computer use has no sandbox between the agent and your screen, and the agent can't filter what it sees.
- **Cited by:** C104
- **Research label:** `BC05` in `research/concepts/beyond-code.md`

### S189 Top 6 Claude in Chrome Security Risks to Model Before You Roll It Out

- **Author:** Krishanu Borah (Akto), Cloud Security Alliance blog
- **Date:** 2026-09-04
- **URL:** https://cloudsecurityalliance.org/blog/2026/09/04/top-6-claude-in-chrome-security-risks-to-model-before-you-roll-it-out
- **Kind:** essay
- **Contributes:** With a logged-in browser agent, the data accessed is the breach, and there is no strange login to alert on.
- **Cited by:** C104
- **Research label:** `BC08` in `research/concepts/beyond-code.md`

### S190 Every OpenClaw Security Incident So Far (2025-2026)

- **Author:** Sliq
- **Date:** 2026-03-01 (shown on the page)
- **URL:** https://getsliq.com/blog/openclaw-security-incidents-timeline
- **Kind:** list
- **Contributes:** Harm without an attacker: an agent mass-deleted an inbox and ignored stop messages.
- **Cited by:** C105
- **Research label:** `BC12` in `research/concepts/beyond-code.md`

### S191 OpenClaw docs: Gateway Security; Secrets, storage, and logs; Operator incident response

- **Author:** OpenClaw project
- **Date:** Undated live docs
- **URL:** https://docs.openclaw.ai/gateway/security ; https://docs.openclaw.ai/gateway/security/secrets-and-storage ; https://docs.openclaw.ai/gateway/security/operator-incident-response
- **Kind:** docs
- **Contributes:** The always-on agent's hardening defaults and its security audit command.
- **Cited by:** C105
- **Read with:** S071
- **Research label:** `BC10` in `research/concepts/beyond-code.md`

### S192 openclaw-security-news (curated list)

- **Author:** joylarkin (GitHub)
- **Date:** Latest dated entry 2026-07-20
- **URL:** https://github.com/joylarkin/openclaw-security-news
- **Kind:** list
- **Contributes:** Incidents kept arriving through July 2026, including a WhatsApp-to-host attack chain.
- **Cited by:** C105
- **Research label:** `BC13` in `research/concepts/beyond-code.md`

### S193 EY retracts cyber report littered with AI errors

- **Author:** Denham Sadler (Information Age, ACS)
- **Date:** 2026-05-19
- **URL:** https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html
- **Kind:** news
- **Contributes:** Over 70% of a published report's 27 citations were made up or misattributed, and the errors had already spread.
- **Cited by:** C106, C107
- **Research label:** `BC15` in `research/concepts/beyond-code.md`

### S194 Can AI design circuit boards yet? (with the EEBench methodology page)

- **Author:** EEBench, built and funded by atopile (no named author)
- **Date:** 2026-09-04 (methodology page undated)
- **URL:** https://eebench.org/blog/can-ai-design-circuit-boards-yet/ ; https://eebench.org/methodology.html
- **Kind:** report
- **Contributes:** What the benchmark behind the AI circuit-board headline measures, what it excludes, and who runs it.
- **Cited by:** C109
- **Read with:** S075
- **Research label:** `BC16` in `research/concepts/beyond-code.md`

### S195 EU AI Act, Articles 50 and 111 (consolidated text with amendment markers)

- **Author:** artificialintelligenceact.eu (Future of Life Institute)
- **Date:** Undated pages (Article 50 applies from 2026-08-02)
- **URL:** https://artificialintelligenceact.eu/article/50/ ; https://artificialintelligenceact.eu/article/111/
- **Kind:** law
- **Contributes:** The Act's own text: marking and disclosure duties, and the 2 December 2026 deadline for generators already on the market.
- **Cited by:** C110, C111, C112, C131; group notes G12
- **Research label:** `SG12-02` in `research/concepts/publishing-media.md`

### S196 Anthropic announcement on watermarking Claude's text

- **Author:** Anthropic
- **Date:** 2026-08-14, updated 2026-09-01
- **URL:** https://www.anthropic.com/news/claude-text-watermark
- **Kind:** news
- **Contributes:** Where Claude's text watermark is and isn't applied, and that it says nothing about ownership or authorship.
- **Cited by:** C110, C112; group notes G12
- **Research label:** `SG12-09` in `research/concepts/publishing-media.md`

### S197 AO-040: Claude's text is watermarked now, and the mark only lives where Claude had a choice

- **Author:** Aaron Orelup (drafted by Claude Opus 5.5)
- **Date:** 2026-10-06
- **URL:** https://aaronorelup.com/ledger/claude-text-watermark/
- **Kind:** aaron-practice
- **Contributes:** There is no public checker; a hit means Claude was probably involved, and no hit doesn't mean a human wrote it.
- **Cited by:** C110, C112; group notes G12
- **Research label:** `SG12-11` in `research/concepts/publishing-media.md`

### S198 How Claude marks AI-generated content (Claude Help Center)

- **Author:** Anthropic
- **Date:** Undated ('Updated this week' on 2026-10-12)
- **URL:** https://support.claude.com/en/articles/16266773
- **Kind:** docs
- **Contributes:** Anthropic hands the Article 50 question back to deployers; content credentials and a checker for files.
- **Cited by:** C110, C112; group notes G12
- **Research label:** `SG12-10` in `research/concepts/publishing-media.md`

### S199 ElevenLabs Prohibited Use Policy

- **Author:** ElevenLabs
- **Date:** Last updated 2026-10-09
- **URL:** https://elevenlabs.io/use-policy
- **Kind:** terms
- **Contributes:** Consent for cloned voices, minors and political figures, and no stripping of watermarks or provenance.
- **Cited by:** C110, C115; group notes G12
- **Research label:** `SG12-08` in `research/concepts/publishing-media.md`

### S200 Disclosing use of GenAI content (YouTube Help)

- **Author:** Google / YouTube
- **Date:** Undated (page shows '©2026 Google')
- **URL:** https://support.google.com/youtube/answer/14328491
- **Kind:** docs
- **Contributes:** When YouTube requires its AI label, and the automatic label it may apply from C2PA metadata.
- **Cited by:** C110, C111, C116; group notes G12
- **Research label:** `SG12-05` in `research/concepts/publishing-media.md`

### S201 ElevenLabs Terms of Use

- **Author:** ElevenLabs
- **Date:** Last updated 2026-10-09
- **URL:** https://elevenlabs.io/terms-of-use
- **Kind:** terms
- **Contributes:** Commercial use only for paid users, and what you grant when you upload your own voice.
- **Cited by:** C113, C114, C115; group notes G12
- **Research label:** `SG12-07` in `research/concepts/publishing-media.md`

### S202 US Supreme Court Declines to Consider Whether AI Alone Can Create Copyrighted Works

- **Author:** Zachary Messick, Joshua M. Dalton, Benjamin B. Anger (Morgan Lewis)
- **Date:** 2026-03-06
- **URL:** https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works
- **Kind:** report
- **Contributes:** Certiorari denied in Thaler v. Perlmutter on 2026-03-02, so human authorship stays required in the US.
- **Cited by:** C114; group notes G12
- **Read with:** S077
- **Research label:** `SG12-01` in `research/concepts/publishing-media.md`

### S203 Copyright and Artificial Intelligence, Part 2: Copyrightability

- **Author:** US Copyright Office
- **Date:** January 2025 (foundational and still current; no later update on copyright.gov/ai as of 2026-10-12)
- **URL:** https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- **Kind:** report
- **Contributes:** Purely AI-generated material isn't protected, and prompts alone don't give enough control.
- **Cited by:** C114; group notes G12
- **Research label:** `SG12-03` in `research/concepts/publishing-media.md`

### S204 Copyright Registration Guidance: Works Containing Material Generated by Artificial Intelligence (88 Fed. Reg. 16,190)

- **Author:** US Copyright Office
- **Date:** 2023-03-16 (foundational and still the policy statement linked from copyright.gov/ai)
- **URL:** https://www.copyright.gov/ai/ai_policy_guidance.pdf
- **Kind:** law
- **Contributes:** How to register a work that contains AI material: disclose it and exclude it, or risk the registration.
- **Cited by:** C114; group notes G12
- **Research label:** `SG12-04` in `research/concepts/publishing-media.md`

### S205 YouTube channel monetization policies (YouTube Help)

- **Author:** Google / YouTube
- **Date:** Latest dated update on the page 2025-07-15 (live policy page, read 2026-10-12)
- **URL:** https://support.google.com/youtube/answer/1311392
- **Kind:** docs
- **Contributes:** The primary text behind the July 2026 clarifications: inauthentic, mass-produced content and the 'creative vision' rule.
- **Cited by:** C116; group notes G12
- **Read with:** S079
- **Research label:** `SG12-06` in `research/concepts/publishing-media.md`

### S206 Quickstart (Claude Code docs)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated live docs; read 2026-10-12
- **URL:** https://code.claude.com/docs/en/quickstart
- **Kind:** docs
- **Contributes:** What a beginner must already have ("A terminal or command prompt open"), the first terminal errors (PATH, PowerShell vs CMD), the working directory, an environment variable that skips login, and git made conversational.
- **Cited by:** C117, C122, C123, C124, C126, C129; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S207 Terminal guide for new users (Claude Code docs)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated live docs; its example output shows version 2.1.211; read 2026-10-12
- **URL:** https://code.claude.com/docs/en/terminal-guide
- **Kind:** docs
- **Contributes:** PowerShell vs CMD and how to tell them apart, PATH fixes that need a new window, "You won't need to learn Git yourself", and the desktop app as a way to skip the terminal.
- **Cited by:** C117, C122, C124, C126
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S208 Get started with the desktop app (Claude Code docs)

- **Author:** Anthropic (Claude Code docs)
- **Date:** Undated live docs; read 2026-10-12
- **URL:** https://code.claude.com/docs/en/desktop-quickstart
- **Kind:** docs
- **Contributes:** Every session starts by choosing a folder and an environment (Local, Cloud, SSH, WSL); the diff view and `+12 -1` indicator; dev servers in the Browser pane; PRs and CI.
- **Cited by:** C117, C122, C123, C124, C127, C128, C130; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S209 Missing Semester 2026: course index and lectures (Shell to Agentic Coding)

- **Author:** MIT Missing Semester (SIPB IAP 2026)
- **Date:** Lectures 2026-01-12 to 2026-01-23 per the index page (Version Control 01-16, Packaging and Shipping Code 01-20, Agentic Coding 01-21, Beyond the Code 01-22); lecture pages undated. Older than three months, still current.
- **URL:** https://missing.csail.mit.edu/2026/ ; https://missing.csail.mit.edu/2026/version-control/ ; https://missing.csail.mit.edu/2026/shipping-code/ ; https://missing.csail.mit.edu/2026/agentic-coding/ ; https://missing.csail.mit.edu/2026/beyond-code/
- **Kind:** course
- **Contributes:** A 2026 university course that still teaches the shell, git's model, dependencies, containers and configuration next to agentic coding; "for critical code, consider writing it by hand"; run yolo-mode agents in a VM or container; copyleft licences.
- **Cited by:** C013, C053, C117, C122, C124, C126, C127, C128, C130; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S210 AO-029: I asked where I was supposed to learn all this. Two hours later, 44 agents had made the first lesson.

- **Author:** Aaron Orelup (drafted by Claude from his transcripts)
- **Date:** 2026-10-01
- **URL:** https://aaronorelup.com/ledger/the-missing-map/
- **Kind:** aaron-practice
- **Contributes:** The course learner's own gap list (from "what is CLI" through webhooks and passkeys; terminals, `cd`, `.venv`, API keys, OAuth, Docker), from someone with an Information Systems degree.
- **Cited by:** C117, C122, C123, C128, C129, C130; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S211 AO-007: No VS Code, no terminal, no idea

- **Author:** Aaron Orelup (drafted by Claude from his transcripts)
- **Date:** 2026-08-08 (describes May 2025)
- **URL:** https://aaronorelup.com/ledger/no-vs-code-no-terminal/
- **Kind:** aaron-practice
- **Contributes:** First-month gaps from the copy-from-chat era: a file one directory over is a different file, git by hand was "the worst of it".
- **Cited by:** C123, C124; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S212 Lovable docs: Glossary, Secrets, Git sync and Custom domains

- **Author:** Lovable
- **Date:** Undated live docs; the git-sync page names 2026-05-13 and the custom-domain page names 2025-10-29; read 2026-10-12
- **URL:** https://docs.lovable.dev/glossary.md ; https://docs.lovable.dev/features/secrets.md ; https://docs.lovable.dev/integrations/git-sync-overview.md ; https://docs.lovable.dev/features/custom-domain.md
- **Kind:** docs
- **Contributes:** What the leading builder platform teaches non-technical users about frontend, backend, webhooks and 2FA; public build-time values vs backend secrets; `.env` that belongs in git; synced branches; local runs that change real data; DNS, certificates, redirect URLs and registrar suspensions.
- **Cited by:** C124, C125, C126, C127, C129; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S213 Whatsapp Trigger not working because i am running n8n with docker on local machine (n8n community thread 302932)

- **Author:** Stoneage; accepted reply by Anshul_Namdev
- **Date:** 2026-07-12
- **URL:** https://community.n8n.io/t/302932
- **Kind:** thread
- **Contributes:** A real environment-variable trap: a value set in a panel never reached the container, a restart kept the old environment, and only a redeploy fixed it (`printenv` to check). Previously listed as a companion read with S066.
- **Cited by:** C126; group notes G13
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S214 Penetration testing (NCSC guidance)

- **Author:** UK National Cyber Security Centre
- **Date:** Published 2017-08-08; reviewed 2022-01-10; page metadata dateModified 2026-04-08. Foundational and still current.
- **URL:** https://www.ncsc.gov.uk/guidance/penetration-testing
- **Kind:** framework
- **Contributes:** How to bring in a security tester: qualified and experienced staff, scoping with risk owners, what a report contains, and why a test is point-in-time and risk ownership stays with you.
- **Cited by:** C118
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S215 OWASP Application Security Verification Standard (project page)

- **Author:** OWASP Foundation
- **Date:** Page undated; latest stable version 5.0.0; read 2026-10-12
- **URL:** https://owasp.org/www-project-application-security-verification-standard/
- **Kind:** framework
- **Contributes:** A requirement list a learner can hand to a tester: it "provides a basis for testing web application technical security controls".
- **Cited by:** C118
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S216 Tea App Data Breach (Security.org explainer)

- **Author:** Gene Petrino and Ozzie Enriquez (Security.org)
- **Date:** 2026-07-08 (last updated)
- **URL:** https://www.security.org/identity-theft/breach/tea-app/
- **Kind:** incident
- **Contributes:** A legacy storage bucket left open after a migration, ID photos kept despite the privacy policy, GPS metadata used to map users, and the lawsuits that followed. Not described as AI-built.
- **Cited by:** C068, C119
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S217 Thousands of Vibe-Coded Apps Exposing Corporate, Personal Data: RedAccess (Security Boulevard)

- **Author:** Jeffrey Burt (Security Boulevard), reporting RedAccess research
- **Date:** 2026-05-07 (updated 2026-05-08)
- **URL:** https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/
- **Kind:** news
- **Contributes:** About 380,000 publicly accessible vibe-coded assets, about 5,000 with sensitive data; apps public by default and indexed by search engines; the vendors' dispute that public means breached.
- **Cited by:** C063, C119
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S218 You're Doing Vibe-Coding Wrong. Here's the 17-Point Fix.

- **Author:** Chizee (DEV Community)
- **Date:** 2026-09-20 (edited 2026-09-23; the year is inferred from the page footer)
- **URL:** https://dev.to/chizee/youre-doing-vibe-coding-wrong-heres-the-17-point-fix-e9h
- **Kind:** essay
- **Contributes:** Practitioner pre-launch omissions: what never to log, rate limits on auth and costly endpoints, webhook signatures, uploads, and debug features left on in production.
- **Cited by:** C066, C067, C068, C119
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S219 GDPR Article 33: Notification of a personal data breach to the supervisory authority

- **Author:** European Union (Regulation (EU) 2016/679), via gdpr-info.eu
- **Date:** Regulation of 2016, applying since 2018-05-25. Foundational and still current.
- **URL:** https://gdpr-info.eu/art-33-gdpr/
- **Kind:** law
- **Contributes:** The 72-hour clock after becoming aware of a breach, and its exception.
- **Cited by:** C119
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S220 vibe-coding-security: pre-launch security checklist for AI-generated apps

- **Author:** boxed-dev (GitHub)
- **Date:** Latest commit 2026-08-09 (GitHub API, read 2026-10-12)
- **URL:** https://github.com/boxed-dev/vibe-coding-security
- **Kind:** list
- **Contributes:** Testable release items: per-user and global token/cost caps, a 429 burst test, HMAC webhook verification, upload validation, tested backups. A small project (15 stars) that also sells a paid add-on; used for its concrete tests only.
- **Cited by:** C066, C067, C121
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S221 The WebAIM Million: 2026 report

- **Author:** WebAIM
- **Date:** Analysis February 2026; report updated 2026-03-30
- **URL:** https://webaim.org/projects/million/
- **Kind:** survey
- **Contributes:** 95.9% of the top million home pages fail detectable WCAG checks, up from 2025, with AI-assisted coding named (not measured) as a likely cause; the commonest failures; the limits of automated tools.
- **Cited by:** C120
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S222 Fact Sheet: New Rule on the Accessibility of Web Content and Mobile Apps (ADA.gov)

- **Author:** US Department of Justice, Civil Rights Division
- **Date:** Page dated 2024-04-08, reflecting the interim final rule published 2026-04-20 (counted as 2026, inferred)
- **URL:** https://www.ada.gov/resources/2024-03-08-web-rule/
- **Kind:** law
- **Contributes:** WCAG 2.1 AA compliance dates for US state and local governments, moved to 2027-04-26 and 2028-04-26.
- **Cited by:** C120
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S223 European Accessibility Act (European Commission page)

- **Author:** European Commission
- **Date:** Undated live page; read 2026-10-12
- **URL:** https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
- **Kind:** law
- **Contributes:** Which products and services the Act covers, including e-commerce, banking services and e-books. The page gives no application date or small-business rule.
- **Cited by:** C120
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S224 What we found when we tested tools on the world's least-accessible webpage

- **Author:** Mehmet Duran (GDS, Accessibility in government blog)
- **Date:** 2017-02-24. Foundational and still current.
- **URL:** https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
- **Kind:** report
- **Contributes:** Ten automated tools against 143 planted barriers: 29% missed by all, the best single tool found 37-41%, so combine tools with manual checks, an audit and user testing.
- **Cited by:** C120
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S225 Cursor-Opus agent snuffs out startup's production database (The Register)

- **Author:** Thomas Claburn (The Register)
- **Date:** 2026-04-27
- **URL:** https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442
- **Kind:** incident
- **Contributes:** A token made for one job with power for every job, a provider that could not scope it, and backups in the same volume: one API call, nine seconds, production gone.
- **Cited by:** C082, C083, C097, C098
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S226 Claude Opus 5 wipes a production database, and it wasn't its fault (IT-Connect)

- **Author:** Florian Burnel (IT-Connect)
- **Date:** 2026-07-30
- **URL:** https://www.it-connect.tech/claude-opus-5-wipes-a-production-database-and-it-wasnt-its-fault/
- **Kind:** incident
- **Contributes:** A command that never says "delete" (`prisma migrate diff` with a production shadow database) resetting 22 production tables by design.
- **Cited by:** C082, C097
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S227 PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub

- **Author:** Hive Security, reporting Glow Labs research of 2026-09-29
- **Date:** 2026-10-02
- **URL:** https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/
- **Kind:** incident
- **Contributes:** Agents that improvised a public upload path for evidence screenshots; counts are the researcher's, not independently audited; controls belong at the token, organisation, endpoint or network level.
- **Cited by:** C003, C015, C072, C084
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S228 Critical Security Vulnerability in React Server Components (React blog)

- **Author:** The React Team
- **Date:** 2025-12-03, updated 2026-01-26 (within the last 12 months)
- **URL:** https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components
- **Kind:** incident
- **Contributes:** React2Shell (CVE-2025-55182, CVSS 10.0): an app nobody touched becomes exploitable, and hosting mitigations are not a fix.
- **Cited by:** C009
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S229 Security Advisory: CVE-2025-66478 (Next.js blog)

- **Author:** Josh Story and Sebastian Markbåge (Vercel)
- **Date:** 2025-12-03 (updated 2025-12-06; within the last 12 months)
- **URL:** https://nextjs.org/blog/CVE-2025-66478
- **Kind:** incident
- **Contributes:** "There is no workaround": upgrade, redeploy, and rotate secrets if the app was online and unpatched.
- **Cited by:** C009
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S230 About Dependabot alerts (GitHub Docs)

- **Author:** GitHub
- **Date:** Undated live docs; read 2026-10-12
- **URL:** https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
- **Kind:** docs
- **Contributes:** Alerts fire when a new advisory is published, with no code change, but someone with admin rights must turn them on and someone must receive them.
- **Cited by:** C009
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S231 Ask HN: Vibe-coded prototypes: what happens when they go into production?

- **Author:** stosssik and replies (Hacker News)
- **Date:** Early 2026 (the page shows "8 months ago"; the crew sweep logged 2026-01-22; inferred)
- **URL:** https://news.ycombinator.com/item?id=46713673
- **Kind:** thread
- **Contributes:** A real question about vibe-coded apps after launch; the one substantive answer is that apps that grow get shut down or taken over by professionals. Thin.
- **Cited by:** C009
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S232 References to matching public code (GitHub Copilot docs)

- **Author:** GitHub
- **Date:** Undated live docs; read 2026-10-12
- **URL:** https://docs.github.com/en/copilot/concepts/completions/code-referencing
- **Kind:** docs
- **Contributes:** AI suggestions can match licensed public code (under 1% of suggestions); detected licences are recorded; you stay responsible.
- **Cited by:** C053
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S233 App Review Guidelines (Apple)

- **Author:** Apple
- **Date:** Live document with no date in the text read (the page calls itself "a living document"); read 2026-10-12
- **URL:** https://developer.apple.com/app-store/review/guidelines/
- **Kind:** terms
- **Contributes:** Guideline 5.1.2(i): disclose and get explicit permission before sharing personal data "with third-party AI"; guideline 4.7: you are responsible for chatbots and plug-ins in your app.
- **Cited by:** C119, C121, C131
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S234 AI-Generated Content policy (Google Play Console Help)

- **Author:** Google
- **Date:** Undated live policy page; read 2026-10-12
- **URL:** https://support.google.com/googleplay/android-developer/answer/13985936
- **Kind:** terms
- **Contributes:** Apps that generate content with AI must offer in-app reporting or flagging of that content.
- **Cited by:** C131
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S235 FLUX.1 [dev] Non-Commercial License v1.1.1, and the FLUX.2 [dev] model card

- **Author:** Black Forest Labs (Hugging Face)
- **Date:** Licence text undated (last commit "over 1 year ago"; still the current licence); FLUX.2 card undated (its collection "Updated Apr 6"); read 2026-10-12
- **URL:** https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md ; https://huggingface.co/black-forest-labs/FLUX.2-dev
- **Kind:** terms
- **Contributes:** A non-commercial model whose outputs may be sold; restrictions that follow fine-tunes; no training competitors on its outputs; separate commercial terms for FLUX.2.
- **Cited by:** C132
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S236 LTX-2 Community License Agreement

- **Author:** Lightricks (Hugging Face)
- **Date:** 2026-01-05
- **URL:** https://huggingface.co/Lightricks/LTX-2/blob/main/LICENSE
- **Kind:** terms
- **Contributes:** A licence that requires a paid commercial licence above $10 million in annual revenue, and covers derivatives.
- **Cited by:** C132
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S237 Qwen-Image (model card)

- **Author:** Qwen (Alibaba), Hugging Face
- **Date:** Released 2025-08-04; older than 12 months, licence still current on the live page
- **URL:** https://huggingface.co/Qwen/Qwen-Image
- **Kind:** docs
- **Contributes:** The permissive end of the licence spectrum: Apache 2.0.
- **Cited by:** C132
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S238 Getty Images v Stability AI [2025] EWHC 2863 (Ch)

- **Author:** High Court of England and Wales (Mrs Justice Joanna Smith DBE)
- **Date:** 2025-11-04 (within the last 12 months; appeal status not checked)
- **URL:** https://www.judiciary.uk/judgments/getty-images-v-stability-ai/ (judgment PDF: https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf, text extracted and read 2026-10-12)
- **Kind:** law
- **Contributes:** Trade mark infringement found for generated outputs carrying iStock and Getty watermarks (narrow findings); the model held not to be an "infringing copy"; the training claim abandoned for lack of UK training.
- **Cited by:** C133
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S239 Content Survey (Steamworks documentation)

- **Author:** Valve
- **Date:** Undated live docs; read 2026-10-12
- **URL:** https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- **Kind:** terms
- **Contributes:** Pre-generated vs live-generated AI content, the promise of non-infringing content, and guardrails for runtime generation.
- **Cited by:** C116, C133
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S240 Copyright and Artificial Intelligence (US Copyright Office)

- **Author:** US Copyright Office
- **Date:** Undated landing page; Part 3 (Generative AI Training) is a pre-publication version released 2025-05-09; read 2026-10-12
- **URL:** https://www.copyright.gov/ai/
- **Kind:** law
- **Contributes:** The status of the Office's report: Part 3 on training is still not final.
- **Cited by:** C133
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S241 Gemini Apps Privacy Hub (Google)

- **Author:** Google
- **Date:** Privacy Notice updated 2026-06-29; hub and privacy questions updated 2026-09-24
- **URL:** https://support.google.com/gemini/answer/13594961
- **Kind:** docs
- **Contributes:** A second vendor's data rules: human reviewers read a sample of chats, reviewed chats are kept up to three years after deletion, and chats are kept 72 hours even with activity off.
- **Cited by:** C103
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S242 Gemini Developer API pricing

- **Author:** Google AI for Developers
- **Date:** Last updated 2026-10-09
- **URL:** https://ai.google.dev/gemini-api/docs/pricing
- **Kind:** docs
- **Contributes:** Video priced per second by resolution (Veo 3.1 tiers), images priced by size, batch at half price, no charge for failed video.
- **Cited by:** C134
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S243 Aaron's Higgsfield notes (references/higgsfield.md)

- **Author:** Aaron Orelup (notes kept by Claude from his sessions)
- **Date:** 2026-09-21 to 2026-09-27 (measured entries); read 2026-10-12
- **URL:** local file, not public: `C:\Users\soulo\Organized\Personal\My Projects\Comfyui\references\higgsfield.md`
- **Kind:** aaron-practice
- **Contributes:** Measured media costs (one shot at 24 to 144 credits by model), a 1,200-credit plan, concurrency limits, refunds for failed jobs, and `ip_detected` refusals.
- **Cited by:** C032, C133, C134
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S244 Diffusers docs: Understanding pipelines, models and schedulers; Reproducibility

- **Author:** Hugging Face
- **Date:** Undated live docs (main branch; the reproducibility page uses Qwen-Image as its example); foundational and current; read 2026-10-12
- **URL:** https://huggingface.co/docs/diffusers/main/en/using-diffusers/write_own_pipeline ; https://huggingface.co/docs/diffusers/main/en/using-diffusers/reusing_seeds
- **Kind:** docs
- **Contributes:** How diffusion makes an image (noise, steps, scheduler, latent space and VAE, text encoder, guidance) and why the same seed can still differ.
- **Cited by:** C032
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S245 Installable triggers (Google Apps Script docs)

- **Author:** Google for Developers
- **Date:** Last updated 2026-09-03
- **URL:** https://developers.google.com/apps-script/guides/triggers/installable
- **Kind:** docs
- **Contributes:** Automations run as their creator, are invisible to other accounts, and fail without an on-screen error.
- **Cited by:** C135
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S246 Change the owner of a cloud flow in Power Automate (Microsoft Learn)

- **Author:** Microsoft
- **Date:** ms.date 2026-09-16; updated 2026-09-25
- **URL:** https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner
- **Kind:** docs
- **Contributes:** The owner is part of a flow's identity and licence; a 30-day grace period before an unlicensed owner's premium flow is turned off; service principals as owners that cannot leave.
- **Cited by:** C135
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S247 Playback: Aaron's prompt on work automations tied to his personal accounts

- **Author:** Aaron Orelup (typed prompt)
- **Date:** 2026-09-30
- **URL:** playback-lens session 88a586af-a275-481a-b481-23bf805cba04 (project C--Users-soulo-Organized-Personal-My-Projects-Courses-The-hidden-curriculum), line 53
- **Kind:** aaron-practice
- **Contributes:** A real case of automations a company depends on running under one person's accounts, and the move to service accounts. Same session as S153; recorded as P01 in `research/sweep/aaron.md`.
- **Cited by:** C135
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S248 Playback: Aaron's prompt asking for mobile apps, app stores and physical devices

- **Author:** Aaron Orelup (typed prompt)
- **Date:** 2026-10-01
- **URL:** playback-lens session fdb1851b-630c-43dc-8fe8-dddde2b407c9 (project C--Users-soulo-Organized-Personal-My-Projects-Courses-The-hidden-curriculum), line 417
- **Kind:** aaron-practice
- **Contributes:** The learner's request that the course cover making mobile apps, getting them into stores, compatibility basics and physical devices. Recorded as P02 in `research/sweep/aaron.md`.
- **Cited by:** C131
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S249 An opinionated guide to which AI to use to do stuff (The Summer 2026 Edition)

- **Author:** Ethan Mollick (One Useful Thing)
- **Date:** 2026-07-23
- **URL:** https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22
- **Kind:** essay
- **Contributes:** A dated, seasonal map of which tool fits which kind of work, model choice by stakes, and what higher-priced plans actually buy.
- **Cited by:** C022
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S250 Quality guidelines (itch.io creator docs)

- **Author:** itch.io
- **Date:** Undated live docs ("continually updated"); read 2026-10-12
- **URL:** https://itch.io/docs/creators/quality-guidelines
- **Kind:** terms
- **Contributes:** Tag generative-AI material or risk delisting; mass-produced pages are treated as spam.
- **Cited by:** C116
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S251 Cyber Resilience Act: policy, reporting and open-source pages (European Commission)

- **Author:** European Commission (Shaping Europe's digital future)
- **Date:** Policy page updated 2026-09-07; reporting page updated 2026-09-11; open-source page updated 2026-07-31
- **URL:** https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act ; https://digital-strategy.ec.europa.eu/en/policies/cra-reporting ; https://digital-strategy.ec.europa.eu/en/policies/cra-open-source
- **Kind:** law
- **Contributes:** Scope and dates of the CRA, the 24-hour reporting duty since 2026-09-11, and the treatment of non-monetised open source.
- **Cited by:** C008, C109
- **Added by:** challenge pass, 2026-10-12 (`research/challenge-log.md`)

### S252 AO-017: An autopilot winning is not a person playing

- **Author:** Aaron Orelup
- **Date:** 2026-09-22
- **URL:** https://aaronorelup.com/ledger/blackwater-2-postmortem/
- **Kind:** aaron-practice
- **Contributes:** The BLACKWATER 2 postmortem: 588 green tests that entered through a `?playtest` flag or a debug hook while a player's click did nothing, then an autopilot that won through the real executable on a game tuned to it; no person had played it. The first BLACKWATER, played by Aaron between turns, worked.
- **Cited by:** C004, C016
- **Added by:** audit fixes, 2026-10-12 (read that day; recorded as A07 in `research/sweep/aaron.md`)

### S253 AO-042: For two months no video on my site could skip ahead, and the agent that noticed wrote a workaround

- **Author:** Aaron Orelup
- **Date:** 2026-10-08
- **URL:** https://aaronorelup.com/ledger/every-video-can-seek/
- **Kind:** aaron-practice
- **Contributes:** A live asset server that answered `200` instead of `206`, a local dev server that hid it for two months, and an agent's workaround that left the cause in place: test where your reader is, and fix the thing underneath.
- **Cited by:** C019, C099
- **Added by:** audit fixes, 2026-10-12 (read that day; recorded as A05 in `research/sweep/aaron.md`)

### S254 Playback: Aaron running many agent sessions on one PC (processes, memory, limits)

- **Author:** Aaron Orelup (typed prompts, with the process count the agent measured in the same session)
- **Date:** 2026-09-24 to 2026-10-08 (prompts)
- **URL:** playback-lens session 25a08e95-eea8-443f-8082-67df9c1bcf71 (project C--Users-soulo-Organized-Personal-AI-ComfyUI), lines 3, 45 and 53, 2026-09-24; other sessions listed under P07 in `research/sweep/aaron.md`
- **Kind:** aaron-practice
- **Contributes:** A heavy user's machine under many sessions: each session starts its own MCP server copies (10 sessions, 11 copies of one server, about 6 GB, plus 20 `npx` wrappers), "what do you mean close a claude session?", and weekly limits stopping work mid-task.
- **Cited by:** C094
- **Added by:** audit fixes, 2026-10-12 (prompts re-read with Playback Lens that day; recorded as P07 in `research/sweep/aaron.md`)

### S255 Use Claude Cowork on Team and Enterprise plans

- **Author:** Anthropic (Claude Help Center)
- **Date:** undated live page, read 2026-10-14
- **URL:** https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans
- **Kind:** docs
- **Contributes:** Team and Enterprise keep local Cowork (work on the user's computer, code in an isolated VM); cloud Cowork is a beta org toggle, "Run Cowork in the cloud", on by default for Team and off by default for Enterprise.
- **Cited by:** C022, C103
- **Added by:** fact-check fixes for where-your-agent-works, 2026-10-14 (recorded in `lessons/where-your-agent-works/research-now.md`)

### S256 Claude Cowork / Desktop changelog

- **Author:** Anthropic
- **Date:** entries 2026-09-24 and 2026-10-01 (live changelog, read 2026-10-14)
- **URL:** https://claude.com/docs/cowork/changelog
- **Kind:** docs
- **Contributes:** 2026-09-24: new desktop Code tab sessions start in Auto, while Cowork sessions still start by asking before each action; 2026-10-01: scheduled tasks Claude creates use "Automatically approve" by default where the organization allows it.
- **Cited by:** C022
- **Added by:** fact-check fixes for where-your-agent-works, 2026-10-14 (recorded in `lessons/where-your-agent-works/research-now.md`)

## Read but not cited

These were read for the course but have no entry of their own, because no concept cites them directly.

### Companions read with a cited source

The batch readers read these alongside the entry named in brackets, for one narrow point. Concepts cite them through that entry.

- [S012] Prompt caching (Claude Platform Docs). Anthropic, undated live docs. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- [S013] Reasoning models (OpenAI API guide). OpenAI, undated live docs. https://developers.openai.com/api/docs/guides/reasoning
- [S015] MCP (Claude Code docs). Anthropic, undated live docs. https://code.claude.com/docs/en/mcp
- [S021] Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach? Ting Yan, arXiv 2608.27443, 2026-08-27 (abstract read). https://arxiv.org/abs/2608.27443
- [S025] Cursor changelog, 2026-08-27 to 2026-10-06. Cursor. https://cursor.com/changelog
- [S038] 2026 GenAI Code Security Report landing page. Veracode. https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/ (the full PDF is behind a form and was not read)
- [S044] Row Level Security (Supabase Docs). Supabase, live docs. https://supabase.com/docs/guides/database/postgres/row-level-security
- [S045] Lovable Docs: Security. Lovable, undated. https://docs.lovable.dev/features/security
- [S047] About push protection (GitHub Docs). GitHub, undated. https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- [S048] The State of Secrets Sprawl 2026. GitGuardian, PDF created 2026-03-25 (data for 2025). https://gitguardian.com/state-of-secrets-sprawl-report-2026
- [S051] Auto mode is now the default in Claude Code for Pro, Max, and Team plans. Anthropic, 2026-08-07. https://claude.com/blog/auto-mode-default-in-claude-code
- [S051] Breaking Claude Code Opus 5 Auto Mode. Simon Willison, 2026-08-27. https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
- [S051] Breaking Claude Code Opus 5 Auto Mode. Johann Rehberger (Embrace The Red), 2026-08-26. https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/
- [S052] Security, and Configure the sandboxed Bash tool (Claude Code docs). Anthropic, undated live docs. https://code.claude.com/docs/en/security ; https://code.claude.com/docs/en/sandboxing
- [S052] Local sandboxing for GitHub Copilot now generally available. GitHub Changelog, 2026-10-07. https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available
- [S054] AgentCorruption: How a single prompt collapsed the entire cloud security model. Tamir Ishay Sharbat and Lana Salameh (Zenity Labs), 2026-10-08. https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model
- [S055] OWASP Top 10 for Agentic Applications for 2026. OWASP GenAI Security Project, 2025-12-09. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
- [S055] OWASP's 2026 LLM Top 10 and New Agent Control Standard. CSA AI Safety Initiative, 2026-09-04. https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/
- [S059] The 2026-07-28 Specification (MCP blog). Model Context Protocol project, 2026-07-28. https://blog.modelcontextprotocol.io/posts/2026-07-28/
- [S061] Unvalidated npm trusted publishing configurations now expire. GitHub Changelog, 2026-10-02. https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire
- [S067] The silent failure: when your n8n workflow succeeds but does nothing (n8n community thread 307116). pirateprentice and replies, 2026-08-11. https://community.n8n.io/t/307116
- [S080] The results of the 2026 Developer Survey are here! Stack Overflow blog, 2026-10-06. https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/

### Reported inside a cited source, not opened

Concepts mention these only as the cited source reports them, and say so in the text.

- Inside S073: Liu et al. 2023, Wallat et al. 2024, Pew Research Center 2024, GhostCite (Xu et al. 2026), Ansari 2026, CiteAudit (Yuan et al. 2026), Alkaissi and McFarlane 2023.
- Inside S011: Jones et al. (CHI 2025) on memory layers, and Cheng et al. 2026 on perceived human-likeness.
- Inside S030: Xia, Wu and Park, arXiv 2609.25396, on interference between parallel patches.
- Inside S036: SWE Refactor Bench, on migrations that pass tests without finishing.
- Inside S060: Spracklen et al., USENIX Security 2025, the package-hallucination study.
- Inside S145: NIST CAISI's 2026-09-17 assessment of GLM-5.3, which S145 says its findings broadly match.

### Tried but not readable

- "The Lethal Trifecta Is Already on Your Laptops", Coder talk, 2026-10-10. https://www.youtube.com/watch?v=abw_m-DRi1k (YouTube blocked the transcript)
- "Careful Adoption of Agentic AI Services", Australian Signals Directorate's ACSC, 2026-05-01 (the cyber.gov.au page timed out)
- Content Credentials verify page. https://verify.contentauthenticity.org/ (returned only its title)
- OpenAI's Data Controls FAQ (HTTP 403 to the sweep agent)
- Reddit threads (Reddit blocks the fetcher, per the sweep notes)
- OpenAI's data-use help page (https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance): HTTP 403 again on 2026-10-12, so C103 has no OpenAI column yet
- California SB 243 (companion chatbots) on leginfo.legislature.ca.gov: HTTP 403 on 2026-10-12, so C131 does not cover it

### Everything that was considered

`research/sources-candidates.md` lists all 274 candidates the finders logged in `research/sweep/`: the 85 picked, the 27 companions folded into them, and the 162 not selected, each with the reason. `research/notes/` holds the batch readers' notes on every source they read, and `research/concepts/` the group files with the sources each concept writer added.
