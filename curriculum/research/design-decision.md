# Design decision, 2026-10-12

Three curriculum designs were judged against the same evidence: `design-A.md` (journey first), `design-B.md` (map first) and `design-C.md` (risk first). They were read alongside `curriculum/concepts.md` (135 concepts: 85 must, 46 should, 4 could), `curriculum/sources.md` (251 sources), `COURSE.md`, `course.json` and `research/challenge-log.md`. **Design A wins.** The synthesis keeps A's spine, takes six ideas from B and C, and is written to `curriculum/curriculum-draft.md`.

No new sources were fetched for this decision. Every concept and source ID in the draft is defined in `concepts.md` or `sources.md`, and every source a lesson lists is cited in `concepts.md` by at least one of that lesson's concepts (checked by script).

## Scores

Each criterion is scored from 1 to 10.

| # | Criterion | A (journey) | B (map) | C (risk) |
|---|---|---|---|---|
| 1 | Coverage of must and should concepts | **10** | 8 | 7 |
| 2 | Lessons grounded in recent, credible sources | **9** | 8 | **9** |
| 3 | Currency (nothing framed the pre-agent way) | 8 | **9** | **9** |
| 4 | The human's role taught where it matters, security above all | **9** | 7 | **9** |
| 5 | A clear map: shelves, order, prerequisites first | **9** | 7 | 6 |
| 6 | Serves people who build anything with AI, not only web developers | **8** | 6 | **8** |
| 7 | Size: 30-36 dense lessons one month can produce | **9** | 8 | **9** |
| 8 | Legacy lessons placed sensibly | 8 | **9** | 5 |
| 9 | Titles and key ideas a beginner would want to watch | **9** | 8 | 8 |
| | **Total (out of 90)** | **79** | 70 | 70 |

What drove each score:

1. **Coverage.**
   - A: all 85 must and 45 of 46 should concepts are in core lessons, plus all 4 could. Only C029 (thinking tokens) waits.
   - B: 85 must, 43 should and 1 could. C054, C108 and C116 wait, along with C031, C109 and C112.
   - C: 85 must, but only 38 should. It parks C028 (subagents), C039 (map before you change), C129 (accounts) and five more.
2. **Sources.** All three draw only on `sources.md`, and all favour sources dated 2026-07 or later.
   - B lists S045 against 03.01, but none of that lesson's concepts (C125, C126, C130) cites it.
   - A and C have no mismatches.
   - Citations: A 151, B 160, C 165.
3. **Currency.** All three teach debugging as the agent's job. None teaches syntax, hand-debugging or the 2021 model picture.
   - B and C each give that idea its own lesson: B's 04.04 "When the agent goes in circles" and C's 08.02 "When it breaks, you supply the eyes".
   - A folds C019 into "Done is a claim" and C042 into a planning lesson, so Aaron's correction is two segments instead of one clear lesson.
4. **The human's role and security.**
   - A puts machine safety before the first build (02.01: deletes, permission modes, approval fatigue). It then sets a whole module between the first public URL and inviting strangers in (04.01-04.04: insecure working code, the stranger test, the app's AI feature, the expert sign-off). It gives agent-side security a district of its own. That is 10 security lessons.
   - C puts security earliest, right after the ground floor.
   - B teaches deletes and permission modes only at lessons 22-28, and app security at lessons 30-32, after the whole Workbench.
5. **The map.**
   - A has six districts with plain journey questions, 11 modules, no module over 4 lessons, and no lesson before a concept it requires.
   - B's names are memorable, and its "Proof" district is a strong shelf. But 23 modules is too many: 13 of them hold a single lesson, and B sits at the 7-district cap.
   - C has four Requires violations:
     - C033 in 00.01 comes before C117 and C122;
     - C022 in 00.03 comes before C128;
     - C135 is taught with C129 in the backlog.
   - C's risk-first order also means the course's core habit, "done is a claim", arrives only at lesson 27.
6. **Beyond web development.**
   - A has a Beyond Code district (research, spreadsheets, hardware, making media, labelling, rights), and a district for automations.
   - C covers the same ground in two modules.
   - B sends spreadsheets, hardware and creator monetisation to the backlog.
7. **Size.**
   - A: 35 slots, 32 of them new.
   - B: 36 slots, at the cap, and fragmented into one-lesson modules.
   - C: 35 slots, only 29 of them new, because 6 slots are legacy.
   - All three are within one month at one lesson a day.
8. **Legacy.**
   - A and B make the same sound choices: 00.01 stays `todo` so the daily job rebuilds the front door first, and three slots are `legacy`.
   - B's Legacy table is the only one `tools/course.py check` parses. A's and C's `Covers` cells hold prose, such as "00.01 (partly)", which the tool reads as lesson IDs: 65 and 44 errors respectively.
   - C marks 00.01 `legacy`. That keeps the old lesson, which draws the retired six-district map, as the course's front door. C also lets the 20-minute 00.05 carry an orientation slot, and marks the environment-variables slot legacy although C126's must-know points are new.
9. **Titles.**
   - A's titles are plain and inviting: "Before you let it loose", "Contain it, don't babysit it", "Test it as a stranger", "Own it, sell it, publish it".
   - B and C have a few abstract ones: "Put the boundary in the environment", "Requests and walls", "Their tests, their review".

## Why A

A follows the order in which a builder actually meets the gaps, and it sets the course where the evidence says today's courses stop:
- Andrew Ng's no-code course (DeepLearning.AI) ends with one downloaded HTML file and never covers tests, hosting, security, keys, accounts, stored data or AI costs (S010).
- Claude Code 101 lists familiarity with a code editor and the command line as a prerequisite (S005).

A gets the learner to a URL by lesson 12. It puts the security checks, and the expert who signs off, between that URL and the first stranger, which is exactly where people otherwise believe the agent when it says the app is safe (S039: 91% of 200 deployed vibe-coded apps were exploitable). It has the best concept coverage, no prerequisite violations, a clean six-district map, and the strongest titles. Its weaknesses were specific and fixable by grafting:
- debugging as the agent's job had no lesson of its own;
- three lessons were overloaded;
- the checking shelf was invisible on the map;
- its legacy table did not parse.

## What was grafted

1. **A lesson of its own for "the agent debugs; you supply the eyes"** (from C's 08.02 and B's 04.04). The new lesson is 02.03 "When it breaks, you supply the eyes" (C003, C019, C042; S094, S009, S003, S008, S032). It is lesson 9 of the path, the moment beginners first hit errors.
   - It turns Aaron's correction (nobody debugs by hand; the agent reads, fixes and re-runs its own errors) into a shelf of its own.
   - It lightens "Done is a claim" (02.04) and the planning lesson (06.01).
   - It brings the course to 36 slots.
2. **C004 moves into "Done is a claim"** (from B's 08.01, which grouped "agents optimise for passing" with "done is a claim"). 02.04 now teaches C004, C005, C011 and C016. 06.02 "Checking what you can't read" drops from six concepts to five (C012-C015, C017).
3. **C024 moves into the rebuilt 00.01** (from B's 00.01). "The model's knowledge has a date" pairs with "what you know goes stale in weeks" (C052), and it is a must concept. In A it sat in a legacy-covered slot, so it would not have been taught fresh until a legacy rebuild. Now it is in the first new lesson the daily job makes. 00.02 keeps C021 and C023.
4. **Checking becomes visible on the map** (from C's "Delegation — how do you direct and check?", which does what B's Proof district does without adding a district). District 3's question is now "How do I direct and check it?".
5. **06.01 is retitled "Plan first, then build in slices"** (B's title and key, `plan-first-then-build-in-slices`), because unsticking a looping agent moved to 02.03.
6. **Dated deadlines in the key ideas, with a check of the generation order against them** (from C):
   - 04.02 names Supabase making grants opt-in for new tables on 2026-10-30 (C068, S148).
   - 09.03 names the EU AI Act's Article 50 duty applying from 2026-08-02 (C110, S195).
   - If the daily job resumes on 2026-10-13 at one lesson a day, 04.02 is made around 2026-10-24, before the Supabase change. 09.03 is made around 2026-11-11, three weeks before the 2026-12-02 marking deadline for generators already on the market.
7. **A Legacy table the course tool can parse, with partial cover** (from B).
   - `Covers` holds only slot IDs, or a dash.
   - Legacy 00.05 lists 05.01 and 09.02, so the course page links those `todo` slots to it until they are built. Legacy 01.05 and 01.06 list the slots they partly cover.
8. **Backlog reasons sharpened from B and C.**
   - The prompt-caching row now says that C058's cost comparison must be re-measured after the 2026-10-07 cache-price cut (from C).
   - The mobile-apps row now says that California's SB 243 must be read before it is taught (from C).
   - Creator monetisation joins the storefront row, with B's note that YouTube is the only video platform the research read.

## The result

| Region | Question | Modules | Lessons | New | Legacy-status |
|---|---|---|---|---|---|
| Start · Orientation | What this is, and your job | 1 | 3 | 1 | 2 |
| 1 · First Build | How do I build my first thing? | 2 | 7 | 6 | 1 |
| 2 · Going Live | How do others safely use it? | 2 | 7 | 7 | 0 |
| 3 · Directing Well | How do I direct and check it? | 2 | 6 | 6 | 0 |
| 4 · Agent Power | What can your agent touch? | 1 | 4 | 4 | 0 |
| 5 · Running Alone | What runs while you're away? | 1 | 3 | 3 | 0 |
| 6 · Beyond Code | What if it isn't software? | 1 | 4 | 4 | 0 |
| Finish · Capstone | Can you ship it end to end? | 1 | 2 | 2 | 0 |
| **Total** | | **11** | **36** | **33** | **3** |

**Concept coverage.**
- All 85 must, 45 of 46 should and all 4 could concepts are in core lessons.
- Each concept is taught in exactly one lesson.
- No lesson comes before a concept it requires.

**Sources.** The lessons make 158 citations of 125 distinct sources.

| Date of the source | Citations | Distinct sources |
|---|---|---|
| 2026-07 or later | 99 | 74 |
| Before 2026-07, updated since | 6 | 5 |
| Undated live documentation that names a current version | 27 | 21 |
| Undated page with no version or dated change (S179, S180, S200 and others) | 6 | 6 |
| Within the last 12 months, before 2026-07 | 18 | 17 |
| Older, foundational and still current per `sources.md` (S049, S214) | 2 | 2 |

**Lanterns.** 23 lessons have AI itself as their subject and are listed on the Lantern line (by key since the 2026-10-12 audit). District 4 ("Agent Power — What can your agent touch?") and module 05 ("What the agent sees") are named for the agent, which goes against COURSE.md's 2026-10-01 rule never to give AI its own module; the audit put that choice to Aaron ("For Aaron to decide", item 5).

**Checks run.**
- `python tools/course.py check --curriculum curriculum/curriculum-draft.md` reports only the 36 spec files that do not exist yet. The draft sits in `curriculum/`, so the tool looks for them in `curriculum/curriculum/lessons/`; at the root as `curriculum.md`, the paths resolve to `curriculum/lessons/`.
- It also gives the expected warnings that legacy 01.01 and 01.02 cover no slot.
- Its browser audit lays the map out at 3 cards per row with 0 wrapped labels. A render was checked by eye.

**Density.** These lessons carry five or six concepts and the specs should keep them under 20 minutes:
- 06.03 Know your meter and 07.04 Other people's code: six concepts each, so they will land near 15 minutes;
- 02.02, 04.04, 05.02, 05.03, 06.02, 07.01, 07.03, 08.01 and 09.04: five concepts each.

## What went to the backlog

**The one concept left out.** C029 (thinking tokens, should) is the only concept not taught in a core lesson. Its own entry says it mostly matters to API builders and bill-watchers, and 06.03 names it in a sentence.

**Deep dives on topics the core already touches.** Each waits for evidence or for a reader who needs more:
- files and file types (legacy 01.01 and 01.02: no current gap);
- processes and ports (no beginner-question evidence yet);
- hardware and the EU Cyber Resilience Act (one vendor-funded measurement);
- mobile apps, app stores and chatbot law (SB 243 unread);
- local models (two sources);
- accessibility audits (the EU dates need re-checking);
- users' data and the law (a lawyer's job; one fixed point read);
- vendor privacy settings (OpenAI's page returned HTTP 403);
- parallel-agent fleets (unproven);
- MCP servers for other people (S164 is a draft);
- prompt caching and model choice in depth (needs re-measurement after the 2026-10-07 price cut);
- game storefronts and creator monetisation (no community questions yet; one platform read);
- AI-written public-interest text, skill descriptions, spreadsheets in depth, and code licences (thin or vendor-only evidence; each is a segment in a core lesson).

## For Aaron to decide

1. **36 is the cap.** If the month runs short, the cheapest cut is 10.02 "After launch: keep it alive". Its three concepts are all should priority, and two rest on thin or disputed evidence (C053, C054). C020 would fold into 10.01, and the other two would go to the backlog.
2. **Media makers wait.** In generation order, the Beyond Code lessons arrive around days 28 to 31. None of their concepts has a Requires link to Districts 3 to 5, so District 6 could follow District 2 if the media and research audience should be served sooner.
3. **00.02's legacy status.** Neither legacy 00.04 nor 00.05 has the April 2026 harness postmortem (S014), the strongest current case for C021. If that gap matters now, set 00.02 to `todo`. *Resolved by the 2026-10-12 audit:* 00.02 and 00.03 are `todo` and come right after 00.01 in the daily job, because the legacy videos covering them teach framings their specs call out of date and pin themselves on the retired map. Aaron can reverse it by setting them back to `legacy`.
4. **Legacy 01.01 and 01.02** cover no slot. Should they stay listed on the course page as background, or be unlisted?
5. **District 4 and module 05 are named for the agent** (audit, 2026-10-12). COURSE.md (Aaron, 2026-10-01) says "never give AI its own module again". Option A: retire that rule, with the date and the reason that the whole course is now about building with agents, recorded in COURSE.md. Option B: rename District 4 "Agent Power — What can your agent touch?" to "Reach and Trust — What can it touch, and who can steer it?" and module 05 "What the agent sees" to "Setting up the work" (the map labels must then be re-checked with `course.py check`). Nothing was renamed while this is open.
6. **"What 'Opus made this' leaves out" (paused folder `lessons/10-16-what-opus-made-this-leaves-out/`).** Aaron asked for it out of sequence on 2026-10-03 and green-lit it on 2026-10-04 as a 20-minute lesson with a guest segment; its ORCHESTRATOR.md records seven of his decisions and it has 75 exhibits from controlled experiments. The draft folds its findings into 09.02 Making media with AI. Keep it as that segment, or give it its own Beyond Code slot (a 37th lesson, over the 36 cap, so one lesson would be cut; 10.02 is the cheapest, item 1). Until he answers, a backlog row names the folder so the green-lit work and his decisions are not lost.
7. **The length rule for module openers.** COURSE.md (2026-10-01): orientation lessons and each module's first lesson run about 5 minutes. The audit applied it to 00.02, 00.03, 04.01, 05.01 and 06.01 (now 5-6 minutes, cut lists in their specs) and to 02.01. It could not apply it to 07.01 (10 minutes), 08.01 (14), 09.01 (10) and 10.01 (15) without restructuring: no lesson of about 5 minutes exists in those modules to open them, and splitting goes past the 36 cap. Options: retire the rule for those modules (record it in COURSE.md with the date); for 08.01, move C105 (always-on personal agents) into its own lesson or into 07.03, which brings 08.01 to about 11 minutes; or split and cut elsewhere.
8. **COURSE.md changes that rewrite your contract** (listed in REWORK-IN-PROGRESS.md): the Lantern device when 23 of 36 lessons are on the Lantern line; beat 7 replaced by a mandatory "Your part and the agent's" beat; the five-year change arc restated for a pace measured in weeks; your 2026-10-12 rule added verbatim; your degree given as "Information Systems" (00.01's fact-check found "+ Data Science" unsupported) unless you confirm otherwise.
9. **Taking money, and shipping software that isn't a website,** are now backlog rows with no source read yet (you named both: aaron.md P01 and P08). Once two strong 2026 sources are read, payments becomes a Going Live lesson after 04.02 or a segment of 04.04, and 04.04 gains a line on testing on machines you don't own.

## Evidence limits inherited from concepts.md

- The G13 ground-floor concepts have no questions collected from beginners themselves, because the prerequisites research batch has not run (search budget used up; Reddit blocks the fetcher).
- C036, C085 and C108 rest on thin evidence.
- OpenAI's data-use page and California's SB 243 returned HTTP 403.
- All the law covered is EU or US.
- Stanford's CS146S security lecture (2026-11-03) has not happened yet.
- Design A's rationale cited Replit's "just for me / my team / the world" ladder from `research/sweep/courses.md`. That source is undated and not in `sources.md`, so it is not used anywhere in the draft. Add it to `sources.md` if it should be credited.

## Audit fixes

Applied on 2026-10-12 to `curriculum/curriculum-draft.md`, the 36 specs in `curriculum/lessons/`, `curriculum/concepts.md` and `curriculum/sources.md`, from the audit's list of 30 problems. Every new point traces to a source read that day; nothing was added from memory. Where a fix is outside those files or needs Aaron, it is recorded as a gate in `REWORK-IN-PROGRESS.md` or under "For Aaron to decide" above, and not applied.

**The draft parses again.**
- The `Lantern lessons:` line names the 23 lessons by key, not ID.
- The Legacy table's `Covers` cells name keys. Legacy 00.05 now covers only `model-harness-and-memory`: it no longer stands in for 05.01 or 09.02, because its context, caching and media segments carry facts with no entry in `sources.md` (the two specs' `legacy:` fields are now empty).
- Checking the draft where it sits still reports 36 "spec file ... is missing" errors (76 before these fixes) and skips every S- and C-ID check, because paths resolve from `curriculum/`. `REWORK-IN-PROGRESS.md` now says so. A copy at the project root returns OK with only the two expected warnings (legacy 01.01 and 01.02 cover no slot), browser map audit included (3 cards per row, 0 wrapped labels).

**Statuses and order.**
- 00.02 and 00.03 are `todo` (draft and spec), so the daily job builds them on days 2 and 3, right after 00.01. The Legacy notes for 00.04, 00.05 and 00.06 carry the course-page line "made before the 2026-10-12 map; being rebuilt"; publish.py does not publish that column, so showing it is a course-page change (gate 6 in `REWORK-IN-PROGRESS.md`).
- Rows 08.01 and 08.03 now list their concepts in the specs' teaching order (C094, C096, C105, C060, C095; C135, C129).

**Titles.** Thirteen lessons were retitled so a beginner can tell what they are about (Aaron's P11 rule). Keys are unchanged, and each spec keeps its former title as a takeaway line:
- 01.03 "Git without typing it: save points and the agent's trail"
- 02.01 "Before your agent runs commands on your computer"
- 02.03 "When it breaks: what the agent needs from you"
- 02.04 "When the agent says 'done'"
- 03.01 "Browser, server, database: where your app really runs"
- 05.02 "CLAUDE.md, AGENTS.md and rules that actually hold"
- 06.02 "Checking code you can't read"
- 06.03 "What your AI work really costs, and how to cap it"
- 07.01 "Prompt injection: when what it reads gives it orders"
- 07.02 "Sandboxes: a safe box for your agent"
- 07.03 "Give your agent only the access it needs"
- 08.02 "Automations that fail silently"
- 08.03 "Whose account is your automation using?"

The scores and examples earlier in this file keep the old titles as a record.

**Backlog.**
- Files, bytes and file types: Concepts `—`; C123 calls this material an outdated framing, and 01.01 teaches C123.
- Writing skills: 05.03 teaches C050 as one segment inside C051, not one sentence.
- Processes, ports and servers: the reason now cites first-hand evidence (new S254 and S170); 08.01 names the per-session processes in one line.
- Accessibility audits: a research note to check whether today's agents' browser tools can run keyboard-only and screen-reader passes.
- New rows: the paused "Opus made this" lesson (C030, C032, C134; S109, S110, S243); taking money; shipping desktop apps, extensions and game builds. The last two have no concept and no source yet, so they cite Aaron's requests (aaron.md P01, P08) in the reason column, and research is queued.

**Sources and evidence.**
- Spec front matter now lists every source its body cites: the 23 specs the audit named (with exactly its IDs), plus the sources the fixes below added (S252, S253, S254, S084, S101, S132, S153, S174, S178, S226).
- `sources.md`: S002's Cited by no longer lists C001, and S003's no longer lists C044, C049 or C051; all 254 Cited by lines now match the concept text. (The audit said S003 appears in the G04 and G05 notes; it appears in G04 only. Four sources' group-note lists differ from the notes; they were outside this audit and left alone.)
- `sources.md` Dates paragraph: it now states its counting rule (the first date the Date field gives for the source; an update or last-modified date only when it is the only one; revision and read dates never count; a footer year is not a date) and lists the 20 inferred IDs.
  - The recount: of 254 sources, 197 (78%) are dated 2026 (177 explicit, 20 inferred) and 145 (57%) 2026-07 or later; 15 are older and 42 undated. Of the 126 sources in lesson rows, 104 (83%) are dated 2026 and 83 (66%) 2026-07 or later.
  - These differ by one or two from the audit's 196 / 142 / 40 and 105 of 125, for two reasons. The three new sources are counted. And footer years (S166, S182, S200) and pages that only name the dates of features (S212) are treated alike, as undated.
- New sources, all read on 2026-10-12: S252 (AO-017, the BLACKWATER 2 postmortem, fetched), S253 (AO-042, the unseekable videos, fetched) and S254 (P07, Aaron's prompts on running many sessions on one PC, re-read with Playback Lens). Their facts were added to C004 point 11 and C016 (S252), C019 and C099 point 8 (S253) and C094 point 9 (S254), so their Cited by lines match.
- 02.04's row credits S252 instead of S032, because BLACKWATER 2 is now its main story and AO-027 is a callback there.

**Aaron's stories, told once each.**
- AO-043 (S026) is told in full only in 03.03. 01.03 lost it as its spine and keeps a one-line case. 05.02, 02.04, 06.02, 08.01 and 08.02 call back to it in a line.
- AO-027 (S032) is told in full only in 02.03; 00.03 and 08.01 now call back to it in one line.
- AO-017 (S252) is 02.04's main story. AO-042 (S253) is in 02.03 C019 point 5 (root cause versus a hidden symptom) and 03.03 C099 (test where your reader is).
- 08.03 C135 point 5 no longer quotes Aaron's private Playback prompt ("if I leave..."). It uses COURSE.md's approved third-person version, and any direct quote is to be cleared with him first. The same quote in concepts.md C135 was paraphrased too, because it carried the same risk.

**Scope cuts and currency.**
- 02.01 was cut from about 2,200 words of binding scope to about 1,170:
  - It keeps C097 points 1, 3, 8 and 9 (with point 6 in one sentence), C077 points 1-2 and C081 points 1, 2 and 4.
  - C097 points 4 and 7 moved to 07.02, with their demos. Point 5 (S226, plus S225's token) moved to 07.03.
  - The vendor detail, the first hour after a wipe, the other wipe reports and the rest of C077 and C081 moved to a "lesson page, not narration" section.
  - Its minutes are now [5, 6].
- 01.01 point 9 lost its D: drive quote, so each wipe is told once.
- The settings-and-versions rule (setting names, flags and version numbers only on a dated card and the lesson page, never in narration) is now in 02.01, 06.03, 07.02, 07.04 and 08.01.
- 07.02's C079 is reframed as four questions: which tools are inside the box, which secrets it can still read, whether it fails open, and whether your OS has one at all. Claude Code is the dated example.
- 06.03 keeps its mental model and moves `promptCacheTtl`, `CLAUDE_CODE_PROMPT_CACHE_TTL` and the v2.1.234, v2.1.242, v2.1.251, v2.1.260 and v2.1.280 gates to the page. 08.01 moves v2.1.217, v2.1.242 and v2.1.246 the same way.
- Length rule: 00.02, 00.03, 04.01, 05.01 and 06.01 are now [5, 6] minutes, each with a cut list built from its own brief and one-line points. 00.03's old 8-11 minute exception belonged to the legacy "How old is all this?". 07.01, 08.01, 09.01 and 10.01 are flagged in their specs and put to Aaron (item 7 above), because no shorter lesson exists in those modules and splitting breaks the 36 cap.
- Hand-work framing, 10.01:
  - C010 point 5 now says to ask conceptual questions (S083's high scorers) and have the agent quiz you on its explanation. The quiz is attributed to S037's explainer-and-quiz gate, because S083's high scorers were not quizzed by an agent.
  - Point 7 is cut to "teams have to build supervision skills on purpose (S029)".
- Hand-work framing, 02.03: C019 point 10 now tells learners to ask the agent to explain each fix and predict what could still fail (S083, S084). The agent still does the fixing.
- 04.04 C120 point 3 dates the GDS figure as 2017 tools and makes the human half "whether a disabled person can actually use it: bring in an auditor or users". It no longer teaches keyboard and screen-reader passes as human-only, pending the backlog's research note.

**Keys and the meter.**
- 03.02 C070 gains one line: a key pasted into the chat stays in the plaintext JSONL transcript under `~/.claude/projects/` (S101), so treat it as leaked. Aaron's own case (P06) is marked sensitive and told only generically.
- 07.03 C082 gains the answer to his question, so 03.02's "07.03 answers it for agents" now holds. Keep the keys your scripts and agents use in a secret store or password manager, not a plain-text project file (OWASP, S042). It is the same pattern as the vendor credential proxy and 1Password in the browser agent (S052, S070). Two sources the audit suggested were not used:
  - `apiKeyHelper`: no source read says what it does.
  - Cowork's host keychain (S050): concepts.md records that description as out of date since 2026-10-06.
- 01.02 C022 gains a one-line point 7: the same surface can bill two ways, and a set `ANTHROPIC_API_KEY` switches you to API billing (S132); 06.03 explains the meter.

**Lead sources.** Every spec has a `lead:` field naming the one or two row sources whose work it delivers, to be credited on the title card, and a note that the narration names at most the row's sources. Examples: S094 and S032 for 02.03, S017 for 06.03, S035 and S167 for 08.01, S030 and S252 for 02.04. The draft's intro mentions it. docs/course-data.md does not document the field yet (gate 4).

**Also fixed.**
- Three specs (00.01, 00.02, 00.03) ended in leaked tool-call markup (`</content>`, `</invoke>`), which was removed.
- Files this session rewrote briefly got CRLF line endings; all were restored to LF.

**Not applied (outside the four files, or Aaron's call).**
- `tools/lesson-workflow.js`: its brief already reads the spec as the binding scope (edited 13:49 the same day). The gaps that remain are gate 3 in `REWORK-IN-PROGRESS.md`.
- COURSE.md's map, Lanterns, beat 7, change arc, Aaron's rule, the degree and the settings rule are gate 4. The "Change arc" line for each AI and security spec waits for that restated arc, and must come from each spec's own dated sources.
- District 4 and module 05 names: item 5 above.
- Pushing the GitHub repo and gating publish.py on the issue chooser: gate 5. The remote was still empty on 2026-10-12, and the four templates exist locally in `.github/ISSUE_TEMPLATE/`.

**Checks run after the fixes.**
- `python tools/course.py check` on a project-root copy of the draft, with the browser audit: OK.
- A parse script over the draft, all 36 specs, concepts.md and sources.md found 0 problems:
  - 36 rows and 36 spec files, matched one to one, with the same keys, IDs, titles, statuses and concept order;
  - 134 concepts each taught in exactly one core lesson, and C029 in the backlog;
  - every row source cited by at least one of that lesson's concepts;
  - every source a spec body cites listed in its front matter;
  - every S- and C-ID defined, in the specs and in the backlog;
  - every lead within its row's sources, and every row naming 2 to 5 sources;
  - all 254 Cited by lines consistent with the concept text.
