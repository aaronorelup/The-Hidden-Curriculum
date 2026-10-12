---
key: checking-research-numbers-and-parts
id: 09.01
title: Checking research, numbers and parts
district: Beyond Code
module: 09 Facts, media, rights
status: todo
legacy: []
minutes: 10
concepts: [C106, C107, C108, C109]
sources: [S072, S073, S074, S075, S193, S194, S251]
lead: [S072, S073]
---
# Checking research, numbers and parts

**Purpose (the first spoken sentence):** In this lesson you'll learn which parts of AI research, spreadsheets and hardware designs the agent can check for itself, and which ones you or an expert must check before anything is filed, sent or ordered.

**Conclusion:** Whether a link exists, whether a workbook's formulas are wired up and whether a circuit survives simulation are machine checks, so make the agent run them; whether the source actually says it, whether the business logic is right and whether the part fits and is safe on a real board are yours or an expert's.

**Where it sits on the map:** District 6 · Beyond Code — What if it isn't software?; module 09 Facts, media, rights (lesson 1 of 4).

**Lead source (audit, 2026-10-12):** S072 (Damien Charlotin); S073 (Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S072, S073, S074, S075); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length (audit, 2026-10-12):** COURSE.md (Aaron, 2026-10-01) gives the first lesson of every module about 5 minutes; this one is 10. No lesson of about 5 minutes exists in this module to open it instead, and splitting would take the course past its 36-lesson cap, so the choice (retire the rule for these modules, or split and cut elsewhere) is on design-decision.md's "For Aaron to decide" list. Until he answers, keep 10.

**Length note:** a module's first lesson normally runs about 5 minutes (COURSE.md). This one carries four concepts across three kinds of work, so it is set to 10. If it must be held to 5, keep C106 and C107 whole and cut C108 and C109 to one surprise each (the typed-in number; the 22 µF capacitor).

**Through-line for the script:** one question asked three times, "could a machine have checked this?". Existence of a link, structure of a sheet and a simulated circuit: yes, so the agent does it and shows the result. Support for a claim, the business logic and the physical board: no, so a person does it (C001, owned by 00.03).

## What to teach (binding scope)

### C106 Checking AI research: a real source can still be wrong
- **A citation can fail in four ways.** Of 2,184 court decisions in Charlotin's database (last updated 2026-10-10): fabricated, the source doesn't exist (1,791); misrepresented, a real source that doesn't say what is claimed (922); false quote (584); outdated, overturned or repealed law (36). One case can have more than one (S072). Depth: teach.
- **Most of the people caught are not lawyers.** 1,259 decisions involve people representing themselves and 864 involve lawyers, in everyday disputes: contract 457, administrative 273, employment 198, family 142. New entries arrive every few days; the three newest on 2026-10-12 were dated 7 and 8 October 2026 (S072). Depth: brief. Re-read the counts on recording day.
- **A real source can be cited for something it doesn't say.** In Grobler v. Kentucky Housing Corporation (2026-10-02) the court found three nonexistent cases and, separately, real cases that "did not support the propositions for which they were cited" (S072). Depth: teach.
- **Support fails more often than existence.** As reported in Rao et al.: only 51.5% of generative-search sentences were fully supported by their citations (Liu et al. 2023), and up to 57% of retrieval citations were "post-rationalized", written from memory and then given a matching-looking source (Wallat et al. 2024) (S073). Depth: brief; say "a study reported in..." on screen, these papers were not opened.
- **Fakes look plausible, and they spread.** EY Canada withdrew a report after more than 70% of its 27 citations were found to be made up or misattributed. It cited a McKinsey report that does not exist for a figure that came from an obscure fintech blog, and used the same US$200 billion figure for two different things a few pages apart. A newspaper had already cited the report, and the researchers warned of "poisoning the well" (S193). Depth: teach; this is the lesson's professional story.
- **The person who files or publishes stays responsible.** In Washington v. Justice (2026-10-07) the appeal was dismissed and future filings were restricted unless signed by Florida Bar counsel; in Tapscott v. Fariss (2026-10-07) the court ordered the filer to produce the cited cases, he did not, and the appeal was dismissed (S072). Depth: brief.
- **The three-step check.** (1) Existence: does it exist? A machine check (C107). (2) Support: open the source and find the exact passage; the agent fetches it and quotes the sentence, a person reads it against the claim for everything that matters. (3) Currency: is it still current, still good law, the latest version? (S073, S072). Depth: teach; this is the spine of the first half.
- **"I always verify" is often not true, and checkers miss things.** As reported in Rao et al.: 87% of surveyed researchers said they always verify AI citations, yet 42% copy BibTeX unchecked (GhostCite); 100 fabricated citations were found in 53 NeurIPS 2025 papers (Ansari 2026); a citation checker's detection score fell from 96% on generated test sets to 33% on real cases (CiteAudit) (S073). Charlotin built a reference checker (PelAIkan) from the database (S072). Depth: one line.

### C107 Link existence is machine-checkable, so make the agent check
- **How often links are fake or dead.** Across 10 models and agents (DRBench) plus 3 on ExpertQA, 3-13% of citation URLs were hallucinated (no Wayback Machine record) and 5-18% did not resolve (S073). Depth: teach.
- **Deep research agents fabricate more, and more links is not better.** Pooled, deep research agents had 10.7% hallucinated URLs against 4.8% for search-augmented models (non-resolving 16.2% against 6.8%); gemini-2.5-pro-deepresearch was highest at 13.3% (S073). Depth: brief.
- **A dead link is not always a fake.** A Wayback snapshot means the page existed and went offline (link rot); no snapshot means it likely never existed. openai-deepresearch had 10.1% non-resolving but only 3.5% hallucinated. A Pew figure reported in the paper: 25% of web pages from 2013-2023 are no longer accessible (S073). Depth: teach.
- **A 403 usually means "blocked", not "dead".** In a headless-browser audit 99.7% of 403 responses were not dead pages (S073). Depth: teach; this is a surprise viewers will hit.
- **The check is small enough to hand over.** The paper's checker, urlhealth, is 83 lines of Python, installable with pip and as an agent skill, and sorts every URL into LIVE, DEAD (404 with an archive copy), LIKELY_HALLUCINATED (404 with no archive copy) or UNKNOWN (S073). Depth: brief.
- **It works only if the model acts on the answer.** In a self-correction loop, non-resolving URLs fell from 16.0% to 0.6% for GPT-5.1, 6.1% to 0.1% for Gemini 2.5 Pro and 4.9% to 0.8% for Claude Sonnet 4.5, while a small model (gpt-5-nano) called the tool, kept re-proposing flagged URLs for up to 14 rounds and ended at 7.5%. So read the final report, not the claim that it ran (S073). Depth: teach.
- **About one link in five stays UNKNOWN.** Paywalls, bot walls and rate limits left 10-20% unresolved; those need a real browser or a person (S073). Depth: brief.
- **Stop fabrication at the source, and know the field.** The authors' first recommendation is to let a system emit only URLs it actually visited; non-resolving rates were highest in healthcare and medicine (17.4% for Claude Sonnet 4.5). The models tested are from April 2026 and older, so teach the method, not the per-model numbers (S073). Depth: one line.

### C108 Check an AI spreadsheet's structure, not its totals
- **Even the best agent falls well short on whole models.** On end-to-end finance workbooks the best agent (Claude Web) scored 69.1/100, and 53.4 at the hardest level (S074). Depth: brief.
- **Correct numbers, no formulas.** "The hardcoded values themselves are typically correct", but typed in where formulas belong, so the sheet doesn't update and can't be audited: Claude (Excel) typed an SG&A ratio of 0.26 straight into a formula, and GPT-5.4 hard-coded 24.7% of answer-sheet cells (S074). Depth: teach.
- **A matching total can hide a wrong formula.** For last-twelve-months EBITDA, Claude Web summed the wrong window of quarters and still hit the expected number, so an exact-match check would have passed it (S074). Depth: teach.
- **Agreement between agents is not verification.** On the easiest task all four working agents recorded a $100K rise in receivables and missed the offsetting decrease: Year 2 cash $1,275 instead of $1,375 (S074). Depth: teach; this is why the known-answer test exists.
- **Shortcuts that are right today break when the assumptions change.** Every agent used a PMT() shortcut (49-305 formulas) where the reference answer built a 180-period schedule (8,006 formulas); the shortcut fails on variable-rate scenarios (S074). Depth: brief.
- **The structural audit, run by a separate checker session.** Are key outputs formulas pointing at assumption cells? Do outputs move when one assumption changes? Does a 0 or blank input spread #DIV/0! or #N/A? Do totals pick up an added row? Does a copied formula's rate reference drift without `$B$1`-style absolute references? Are units labelled and numbers not stored as text? The benchmark's LLM judge agreed with 408 expert annotations at 0.92 accuracy but missed injected absolute-reference errors, so spot-check the audit (S074). Depth: teach.
- **"Update this sheet" can mean "rebuild it".** Opus 4.6 copied the starting workbook, rebuilt it in its own layout and on one task deleted the original "Receivables" sheet; keep a copy and check that the sheets and cells other files depend on still exist (S074). Depth: teach (surprise).
- **The product matters as much as the model, and a headline score is not your model.** With the same model, the vendor's own app agent generally scored better than the researchers' API harness; SpreadsheetBench, cited in model launches, tests atomic tasks with about 33 times fewer cells (S074). Depth: one line; the harness point belongs to 00.02.

### C109 Hardware: physical facts the AI can't check from text
- **AI is now useful for prototypes; the reports are anecdotal.** A Hackaday reader had three AI-designed boards each "come back working first time", and readers report LLMs reading datasheets well and finding stock (S075, reader comments). Depth: brief, labelled as anecdote.
- **Check that every part is still made.** Asked to replace an end-of-life DC-DC module, ChatGPT "happily recommended a selection of other discontinued parts"; a person using Digi-Key's parametric search, then a Digi-Key contact, found working ones (S075, reader comment). Depth: teach.
- **Check footprints and connections.** Readers reported an AI that "can't make a footprint from a pdf datasheet" and schematics with "open circuits, components connecting nowhere" (S075, reader comments). Depth: brief.
- **The value printed on the part is not what the circuit gets.** In EEBench, a design specified a 22 µF capacitor that delivered only 11.4 µF at 4.7 V bias against a 545 µF requirement, so the protected rail failed. "The source built successfully; the circuit still failed the job." "A design that works with nominal values can fail with the parts that arrive." (S194). Depth: teach.
- **Give the agent a simulator.** EEBench has agents write the circuit as code, build it and run SPICE at worst-case tolerance corners, which its authors compare to "giving a coding agent a compiler and tests" (S194). Depth: brief.
- **Read what a benchmark measures and who runs it.** OpenAI claimed GPT-6 Astra designs complete KiCad boards; the benchmark quoted beside it, EEBench V1, does not yet cover layout, manufacturing or bring-up, is built and funded by atopile, and its 2026-09-01 leader (Claude Opus 5) passed 61.6%. Hackaday's 69.3% for GPT-6 Astra could not be confirmed on EEBench's own pages (S075, S194). Depth: brief; benchmark reading in general belongs to 00.03.
- **What no simulation covers, and where mistakes hurt.** High-power switching layout, signal-integrity and compliance routing, EMC and safety testing, and chip documentation locked under NDA (S075, reader comments). A reader described a 230 V-to-5 V design posted for mass production with "less than 0.5mm clearance between 230v traces", no transient protection and no isolation; production boards are expected to be "fully validated by multiple independent engineers" (S075). Depth: brief; the production bar belongs to 03.01.
- **Selling a connected device in the EU now carries a dated duty.** Since 2026-09-11 manufacturers must report actively exploited vulnerabilities and severe incidents (early warning within 24 hours, notification within 72), and the Cyber Resilience Act's main obligations apply from 2027-12-11 (S251). Depth: one line; the full treatment is in the backlog.

**Evidence limits the script must respect.** C108 rests on one benchmark (S074, May 2026, models of that time). C109's failures are reader comments and its one measurement comes from a vendor-funded benchmark (S194). Rao et al.'s per-model rates are for April-2026-and-older models (S073). Hedge accordingly and say "in one benchmark" or "readers reported".

## You vs the agent
As of 2026-10-12:
- **The agent does on its own:** searches and fetches each source and quotes the exact sentence that supports each claim; runs a link checker such as urlhealth over its own reference list, checks the Wayback Machine for dead links and replaces what is flagged; in a separate checker session, audits a workbook's structure and reports findings with cell addresses; reads datasheets, searches distributor stock, writes a circuit as code and simulates it at tolerance corners, iterating on the failures (S073, S074, S194).
- **You check:** that the link check is a required step and its final counts (how many LIKELY_HALLUCINATED or UNKNOWN remain), not its claim that it ran; the paywalled and blocked links, in a real browser; the quoted passage against the claim, for every claim that matters, and whether it is still current (S073, S072). For a workbook: you choose the assumptions that matter, run a known-answer test whose correct answer you worked out beforehand and that a coincidence can't hit, judge the business logic (does every cash movement have its offset?), click one flagged cell to spot-check the audit, and keep a copy (S074). For hardware: each part's lifecycle status at a distributor, each footprint against its datasheet, that the design checks and simulations really ran, and the real board on the bench before ordering in volume (S075, S194).
- **You bring in an expert:** a lawyer for anything filed in court (Washington v. Justice made Florida Bar counsel the condition for future filings), a clinician for a medical claim, a domain expert for a published report (S072); a modelling or accounting professional for a model that money or decisions depend on (the benchmark's rubric took two MBAs and three finance professionals over 700 hours) (S074); qualified engineers and a test lab for mains voltage, anything safety-critical, EMC and any device you will sell, and a compliance expert before a first EU sale (S075, S194, S251). How to brief an expert is taught in 04.04.

## Sources this lesson is built from
- S072 — Damien Charlotin, "AI Hallucination Cases database" (last updated 2026-10-10) https://www.damiencharlotin.com/hallucinations/ — the four failure types and their counts, who gets caught, Grobler, Washington v. Justice, Tapscott v. Fariss; re-read 2026-10-12 (2,184 decisions; 1,259 pro se, 864 lawyers).
- S073 — Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania), "Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents" (2026-04-03; models tested are older) https://arxiv.org/html/2604.03173v1 — fake and dead link rates, link rot vs fabrication, 403s, urlhealth and the self-correction loop, plus the studies it reports (Liu 2023, Wallat 2024, Pew 2024, GhostCite, Ansari 2026, CiteAudit; not opened, credit them as "reported in Rao et al."); re-read 2026-10-12.
- S074 — Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. (Columbia Business School), "WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance" (2026-05-21) https://arxiv.org/html/2605.22664v1 — typed-in values, the matching-total error, the shared receivables mistake, the rebuild that deleted a sheet, the structural rubric; re-read 2026-10-12.
- S075 — Maya Posch, Hackaday, "Can AI Now Design PCBs That Just Work?" (2026-09-05) https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/ — the GPT-6 Astra claim, the production-validation expectation, and reader reports (discontinued parts, footprints, open circuits, the 230 V design, NDA documentation); re-read 2026-10-12.

Also cited for single points (credit on the lesson page):
- S193 — Denham Sadler, Information Age (ACS), "EY retracts cyber report littered with AI errors" (2026-05-19) https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html — the EY story; re-read 2026-10-12.
- S194 — EEBench (built and funded by atopile; no named author), "Can AI design circuit boards yet?" (2026-09-04) with the methodology page (undated) https://eebench.org/blog/can-ai-design-circuit-boards-yet/ ; https://eebench.org/methodology.html — the 22 µF capacitor, design as code with SPICE at tolerance corners, what the benchmark excludes and who runs it; re-read 2026-10-12.
- S251 — European Commission, Cyber Resilience Act policy, reporting and open-source pages (updated 2026-09-07, 2026-09-11, 2026-07-31) https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act — the reporting duty and dates.

Recency: S072, S075, S194 and S251 are from the last three months; S073, S074 and S193 are from April-May 2026, within twelve months.

## Show it for real
- Charlotin's database filtered to "Pro Se Litigant", newest entry opened and its outcome read aloud: proves the people caught this week are mostly not lawyers.
- An agent installs urlhealth with pip and runs it over its own reference list in a terminal, printing LIVE / DEAD / LIKELY_HALLUCINATED / UNKNOWN per URL, then replaces one flagged URL and prints the final counts: proves existence is a check the agent can run and report.
- A dead URL pasted into web.archive.org, once with a snapshot list (link rot) and once "not archived" (likely invented): proves dead is not the same as fake.
- One UNKNOWN (403) link opened in a normal browser, where it loads: proves a 403 usually means blocked.
- Find-in-page for a quoted sentence inside a real, public source that does not contain it: proves support is a separate check from existence.
- A fresh checker session audits a fictional AI-built workbook and reports with cell addresses; one flagged cell is clicked and the formula bar shows a typed number: proves the audit and the spot-check of the audit.
- On the same toy sheet, the growth assumption is changed and the outputs don't move; a 0 typed into a divisor spreads #DIV/0!; a known-answer input shows the model's $1,275 against the worked-out $1,375 (the benchmark's receivables case rebuilt on a toy sheet): proves why totals are the wrong check.
- The sheet tabs before and after an agent's "update", with one original tab gone: proves "update" can mean "rebuild".
- An AI-suggested part number pasted into a distributor's search, showing its lifecycle status (pick a known end-of-life part on recording day): proves the part check is a lookup, not a judgment.
- EEBench's methodology page beside the launch claim, and the blog's plot of the rail falling at 0.85 ms: proves a benchmark can measure less than the headline says.
- Safe to record: no keys are needed for urlhealth or the archive; use public sources and a fictional workbook, never personal finances.

## Questions this lesson answers
Collected by the research crew's batch readers from the sources (items #20-#33 in `research/notes/beyond-code-agents-and-facts.json`); no beginner forum threads were collected for this module yet.
- Can I use AI to write my own legal filing?
- How do I check that the cases or papers AI gives me are real?
- The source is real, so why was the citation wrong? The link works but I can't find the claim. What happened?
- Are deep research reports reliable?
- The link is dead: was it made up? How do I use the Wayback Machine to check a source?
- Can I make the AI check its own sources? Is there a tool that finds fake links?
- Can I trust a financial model the AI built? Why doesn't my AI spreadsheet update when I change an input?
- What should I check in a spreadsheet an AI made? Why did the AI delete my sheet?
- Can AI design a circuit board now? Can ChatGPT pick parts for my circuit?
- Why doesn't my capacitor give the value on the label?
- Can I sell a device whose board AI designed? Is it safe to build a mains power supply from an AI design?
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- The verification line itself (the agent checks what can be checked; you check the rest or bring in someone who can) → trust-what-you-can-verify
- Reading what a benchmark measures, and trust per kind of task → trust-what-you-can-verify
- Spot-checking the checker (verify the verifier) and evidence the agent can't write → checking-what-you-cant-read
- Why a separate checker session sees only what you hand it → what-the-agent-sees-each-turn
- The same model scoring differently in a different product → model-harness-and-memory
- The model's knowledge has a date (why the currency step matters) → the-hidden-curriculum
- Prototype vs production, the bar when real users or physics arrive → what-runs-where
- What to hand an expert and what you get back → before-you-ship-who-signs-off
- AI-written public-interest text needs a fact-checking human or a label → labelling-ai-media
- Spreadsheets with agents in depth; hardware, physical devices and the Cyber Resilience Act in depth → deep-dive backlog (curriculum-draft.md)

## Out-of-date framings to avoid
- "Hallucinated citations are a lawyer problem." Most decisions involve people representing themselves (S072).
- "That was an early-ChatGPT problem." Decisions are still being added in October 2026 (S072).
- "If the source exists, the citation is fine." 922 decisions involve real sources misrepresented (S072).
- "Models with web search don't make up sources" and "a long bibliography means thorough research" (S073).
- "A 404 means the AI made it up" or "a 403 means the page doesn't exist" (S073).
- "Checking AI citations means clicking every link yourself." The agent can run the existence check (S073).
- "Professional firms check AI output before publishing" and "peer review catches fabricated citations" (S193; Ansari 2026 as reported in S073).
- "AI is bad at arithmetic, so check its math." The values were usually right; the structure was wrong (S074).
- "If the total matches, the model is right" and "if two AIs agree, it's correct" (S074).
- "The AI only changes what I asked it to" (S074).
- "AI can't help with hardware at all." Out of date for prototypes (S075).
- "The part value on the schematic is what the circuit gets" and "if the schematic looks complete, it's connected" (S194, S075).
- "A vendor demo and a benchmark score mean it's ready to sell" (S075, S194).

## Legacy notes
No published lesson covers this slot. Nothing here was taught in the legacy lessons.
