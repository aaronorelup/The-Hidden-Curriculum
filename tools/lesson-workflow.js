export const meta = {
  name: 'missing-map-lesson',
  description: 'Write, fact-check, narrate, animate and review one lesson of The Hidden Curriculum (optionally render + publish)',
  whenToUse: 'Producing one lesson of The Hidden Curriculum course end to end',
  phases: [
    { title: 'Research', detail: 'what is true this month, and what changed in the last five years' },
    { title: 'Plan', detail: 'content plan: must-cover list, time budget, what gets its own lesson' },
    { title: 'Script', detail: 'three angles written in parallel' },
    { title: 'Judge', detail: 'score drafts, synthesize final script + storyboard' },
    { title: 'Fact-check', detail: 'two adversarial verifiers, then fixes' },
    { title: 'Narrate', detail: 'ElevenLabs narration + ducked score' },
    { title: 'Design', detail: 'shared visuals for the lesson' },
    { title: 'Animate', detail: 'one animator per scene' },
    { title: 'Review', detail: 'two review lenses, fix rounds' },
    { title: 'Ship', detail: 'render MP4, publish, file in digiKam' },
  ],
}

const A = args || {}
const COURSE = A.course || 'C:/Users/soulo/Organized/Personal/My Projects/Courses/The-hidden-curriculum'
const SLUG = A.slug
const DIR = `${COURSE}/lessons/${SLUG}`
const CD = `cd "${COURSE}"`
// Lesson length (Aaron, 2026-10-01): orientation (module 00) and every module's first lesson ~5 min; lessons in the
// middle of a module ~10 min; never over 20. args.minutes = [lo, hi] overrides. ~140 spoken words per minute.
const [MOD, NUM] = String(A.id || '00.01').split('.')
const MIN = (A.minutes || (MOD === '00' || NUM === '01' ? [3.5, 5.5] : [8.5, 11.5])).map(m => Math.min(20, m))
const WORDS = MIN.map(m => Math.round(m * 140 / 10) * 10)
// Long lessons use longer scenes (~60 s) so the animator count stays sane; args.sections = [lo, hi] overrides.
const SECTIONS = A.sections || (MIN[1] > 12 ? [Math.round(MIN[0]), Math.round(MIN[1])] : [Math.max(6, Math.round(MIN[0] * 60 / 45)), Math.max(9, Math.round(MIN[1] * 60 / 40))])
// Today's date (pass args.today = 'YYYY-MM-DD'); lessons must be current as of this month (Aaron, 2026-10-02).
const TODAY = A.today || 'today (run `date +%F` to get it)'
// Lessons over 15 minutes get ONE guest segment (Aaron, 2026-10-01): script sections tagged [guest], spoken by the
// course's fixed third voice (voices/roster.json "guest"), at most 5 minutes; engine/music.js turns livelier under it.
const GUEST = MIN[1] > 15 ? `GUEST SEGMENT (required, this lesson runs over 15 minutes): exactly one run of 1–4 consecutive sections whose headings end in [guest] (e.g. "## 09 — Field notes [guest]"), at most 5 minutes in total (650 words at most). They are spoken by the course's guest voice, a third speaker who is never the narrator and never Aaron; run \`python tools/voice.py --guest\` to get the guest's first name. The narrator hands over by naming the guest, and the guest hands back at the end. Give the guest a real job that changes the pace: a myth-busting round, a field story told in the third person, a worked example, or a quick-fire recap. Never use the segment for padding. The score turns livelier under the guest automatically. The storyboard marks the guest's scenes on screen with a small lower-third card ("guest · <name>") and a brighter palette accent.` : 'No [guest] sections: this lesson is 15 minutes or shorter (only longer lessons have a guest).'
const LENGTH = `${MIN[0]}–${MIN[1]} minutes: ${WORDS[0]}–${WORDS[1]} spoken words in ${SECTIONS[0]}–${SECTIONS[1]} sections`
const BRIEF = `You are on the production crew for "The Hidden Curriculum" (formerly "The Missing Map"; the six-district course map, with the Lanterns (AI) strung over every district and never a district themselves, is still "the map"), Aaron Orelup's animated CONCEPTUAL course about everything nobody teaches people who build with AI (terminals, files, git, APIs, keys, hosting...). Lessons build mental models, not how-to steps.
Course folder: ${COURSE}
This lesson: ${A.id} "${A.title}" (module: ${A.module})${A.poc ? ' — this build is a PROOF OF CONCEPT of the pipeline; still make it as good as a real lesson' : ''}
Lesson folder: ${DIR}
Required reading before you do anything: ${COURSE}/COURSE.md (the lesson contract: arc, voice, visual rules, safe areas) and this lesson's row in ${COURSE}/curriculum.md.
Use absolute paths. Run tools from the course folder, e.g. \`${CD} && python tools/stills.py ${SLUG} --scene 03 --every 1\` (Git Bash syntax).
Target length: ${LENGTH} (hard rule; the course caps any lesson at 20 minutes).
Today is ${TODAY}. CURRENCY RULE (Aaron, 2026-10-02): every lesson must be true and relevant as of this month, not five years ago. Anything about AI or security must show how it changed over the last five years and where it is heading now; never present an outdated picture as the current one. The lesson's research (${DIR}/research-*.md) and content plan (${DIR}/plan.md), once they exist, are binding: the plan's must-cover list is the lesson's scope.${A.rebuild ? `\nREBUILD: this lesson was already published once in a shorter, older form (backed up outside the repo). Aaron rejected it as five years out of date; the rebuild replaces it at the same URL.` : ''}
${GUEST}
${A.notes ? 'Orchestrator notes: ' + A.notes : ''}`

const SCRIPT_FORMAT = `script.md format (exactly):
# ${A.id} — ${A.title}
<!-- lead=1.6 gap=0.8 tail=3 -->
## 01 — <section title>
<spoken narration for this scene, with [[cue-name]] markers placed exactly before the word where an animation beat should land>
> optional production note lines start with ">" and are never spoken
## 02 — <section title>
...
Rules: the narrator is one of the course's two roster voices (never Aaron): no "I/my" as Aaron (tell his true stories in the third person: "Aaron, who made this course, ..."); spell for the ear per COURSE.md's pronunciation list (".venv" = "dot V E N V"); ${SECTIONS[0]}–${SECTIONS[1]} sections; ${WORDS[0]}–${WORDS[1]} spoken words total (${MIN[0]}–${MIN[1]} min at ~140 wpm); a longer lesson keeps the same arc and gives the extra time to more of the mental model, the mechanism and the surprises, never to padding; written for the ear (spell spoken forms: "dot P Y", "V S Code"); about one [[cue]] per 10–15 spoken seconds (2–5 for a short section, up to 7 for a long one) with short kebab-case names; the very first spoken sentence of section 01 states the lesson's purpose, what the viewer will learn in this lesson ("In this lesson you'll learn ..."), before any story, hook or question (Aaron's rule), and the next sentence states the conclusion; last section is the "Keep this" end card with exactly three takeaways spoken plainly.`

const STORYBOARD_FORMAT = `storyboard.md format: one "## NN — title" block per script section with: **Metaphor object** (what persists), **Frame** (what is on screen, positions on the 1920x1080 canvas, drawn only with the kit in ${COURSE}/engine/KIT.md: windows, terminals, editors, files, folders, cards, pills, arrows, line icons, the course map, the painted plate), **Beats** (one bullet per [[cue]]: what appears/moves when that cue is spoken), **Exit** (calm last frame). Put the course map (K.map.draw with a pin) in the "where it lives" scene. Title card may use the painted plate engine/assets/teahouse-night.jpg (may not exist yet; design so it still works on K.bg()).`

// ---------- Research: current state + five-year change, in parallel ----------
phase('Research')
const RESEARCH = [
  { k: 'now', how: 'the subject AS IT IS THIS MONTH: the current mechanisms, products, names, versions, prices and limits a learner will actually meet; what is new in the last 12 months; what is clearly heading in (announced, in beta, widely reported) and what is speculation.' },
  { k: 'change', how: 'the last FIVE YEARS of change in this subject: what it looked like five years ago, the turning points (with dates), what got replaced or renamed, and which old explanations are now misleading. Also list the ideas that did NOT change (the durable part of the mental model).' },
]
await parallel(RESEARCH.map(r => () => agent(
  `[AGENT: research-${r.k}]\n${BRIEF}\n\nResearch, do not write the lesson. Your lens: ${r.how}\nUse WebSearch and WebFetch heavily (official docs, vendor announcements and changelogs, reputable reporting); your own memory is out of date, so verify every product name, date and number against a source dated as recently as possible. Work through every topic in the orchestrator notes; if a name there is ambiguous or misspelled, find what is meant and say so.\nWrite ${DIR}/research-${r.k}.md: one heading per topic, short factual bullets each with its source URL and the source's date, a "status" tag per claim (established / new this year / beta or announced / speculation), and a closing "traps" list of things commonly said that are now wrong. No prose for the viewer. Return a 5-line summary.`,
  { label: `research:${r.k}`, phase: 'Research' })))

phase('Plan')
const PLAN_SCHEMA = { type: 'object', properties: { purpose: { type: 'string' }, mustCover: { type: 'array', items: { type: 'string' } }, deferred: { type: 'array', items: { type: 'object', properties: { topic: { type: 'string' }, where: { type: 'string' } }, required: ['topic', 'where'] } }, minutes: { type: 'string' } }, required: ['purpose', 'mustCover', 'deferred'] }
const plan = await agent(
  `[AGENT: planner]\n${BRIEF}\n\nPlan the lesson's CONTENT before anyone writes a line (Aaron, 2026-10-02: "spend more time planning what you are going to include in each lesson"). Read ${DIR}/research-now.md, ${DIR}/research-change.md, ${COURSE}/COURSE.md and ALL of ${COURSE}/curriculum.md (to know what other lessons already own, so this one introduces those topics briefly and points to where they live on the map instead of teaching them).\nWrite ${DIR}/plan.md with:\n1. Purpose line (the first spoken sentence) and the one-sentence conclusion.\n2. "As of" line: the month this lesson describes.\n3. The change arc: five years ago -> now -> where it is heading (required for AI and security subjects; otherwise one line on whether it changed).\n4. MUST-COVER list: every topic in the orchestrator notes plus anything the research shows a learner will meet this month, each with a depth (teach / brief mention / one line) and a seconds budget; the budgets sum to the target length. Group them into scene-sized sections in the order the script will use.\n5. DEFERRED: each topic only introduced here, with the curriculum lesson that owns it (ID) or "NEW: <suggested module>" when no lesson owns it yet.\n6. Mental model: one metaphor that can carry the whole lesson (and transform as it goes), plus where it breaks.\n7. Cut list: tempting things that stay out, and why.\n8. Facts to handle carefully: claims that are new, beta or speculation, with the hedged wording to use.\nReturn the structured summary.`,
  { label: 'planner', phase: 'Plan', schema: PLAN_SCHEMA })
log(`plan: ${plan.mustCover.length} must-cover topics, ${plan.deferred.length} deferred`)
const PLANNED = `The content plan is ${DIR}/plan.md (read it first; with ${DIR}/research-now.md and research-change.md for facts). Cover every MUST-COVER item at its planned depth, in its planned section, within its time budget; use the plan's purpose line, change arc and mental model; use the hedged wording for new/beta/speculative claims.`

// ---------- Script: three angles ----------
phase('Script')
const ANGLES = [
  { k: 'A', name: 'story-first', how: 'After the opening purpose sentence (required for every angle), tell one concrete, true, relatable moment (Aaron wrote Python in Notepad as a .txt file, did not know to rename it .py, or to open a terminal and cd into the folder, or what .venv was, despite an Information Systems + Data Science degree) and widen from there to the idea.' },
  { k: 'B', name: 'metaphor-first', how: 'Build the whole lesson around ONE strong visual metaphor that can be drawn and that transforms as the lesson goes on; the metaphor is the mental model.' },
  { k: 'C', name: 'framework-first', how: 'Lead with the structure: what the thing is, where it sits on the course map, then the surprises a newcomer will hit and what to ignore; crisp and skimmable.' },
]
const DRAFT_SCHEMA = { type: 'object', properties: {
  angle: { type: 'string' }, words: { type: 'number' }, metaphor: { type: 'string' },
  sections: { type: 'array', items: { type: 'object', properties: { n: { type: 'string' }, title: { type: 'string' }, beat: { type: 'string' } }, required: ['n', 'title'] } },
  pitch: { type: 'string' } }, required: ['angle', 'words', 'sections', 'pitch'] }

const drafts = await parallel(ANGLES.map(g => () => agent(
  `[AGENT: script-${g.k}]\n${BRIEF}\n\nYour job: write a complete draft script + storyboard for this lesson from the "${g.name}" angle. ${PLANNED} ${g.how}\n\n${SCRIPT_FORMAT}\n\n${STORYBOARD_FORMAT}\n\nAlso load the aaron-brand skill for voice. Keep facts checkable; do not invent statistics or anecdotes beyond the true ones listed in COURSE.md.\nWrite ${DIR}/drafts/script-${g.k}.md and ${DIR}/drafts/storyboard-${g.k}.md. Count the spoken words (exclude headings, notes, cue markers) and report them. Return the structured summary.`,
  { label: `script:${g.name}`, phase: 'Script', schema: DRAFT_SCHEMA })))
const okDrafts = drafts.filter(Boolean)
log(`${okDrafts.length} drafts: ` + okDrafts.map(d => `${d.angle} ${d.words}w`).join(', '))

// ---------- Judge ----------
phase('Judge')
const JUDGE_SCHEMA = { type: 'object', properties: {
  winner: { type: 'string' }, scores: { type: 'string' }, grafts: { type: 'string' }, words: { type: 'number' },
  sections: { type: 'array', items: { type: 'object', properties: { n: { type: 'string' }, title: { type: 'string' } }, required: ['n', 'title'] } },
  metaphor: { type: 'string' } }, required: ['winner', 'scores', 'words', 'sections'] }
const judged = await agent(
  `[AGENT: judge]\n${BRIEF}\n\nThree drafts exist: ${DIR}/drafts/script-{A,B,C}.md and storyboard-{A,B,C}.md. Pitches: ${JSON.stringify(okDrafts.map(d => ({ angle: d.angle, words: d.words, metaphor: d.metaphor, pitch: d.pitch })))}\n\nScore each 1–10 on: (1) conceptual clarity for a smart beginner, (2) opens with the purpose sentence ("In this lesson you'll learn ...") as the very first words, then conclusion first / no withheld payoff (the final script.md MUST open this way; fix it if the winner doesn't), (3) strength and drawability of the mental model, (4) the "surprises you'll hit" payload, (5) voice per aaron-brand (load that skill), (6) fit to the course map, (7) animation potential with the kit (${COURSE}/engine/KIT.md), (8) factual safety. (9) coverage of ${DIR}/plan.md: list any MUST-COVER item a draft dropped or got wrong, and (10) currency: nothing presented as current that is out of date as of ${TODAY}. Pick a winner, then SYNTHESIZE the final version, which MUST cover every must-cover item in the plan: keep the winner's spine, graft the best lines/ideas from the others. Tighten ruthlessly.\n\nWrite the final ${DIR}/script.md (${SCRIPT_FORMAT})\n\nWrite the final ${DIR}/storyboard.md (${STORYBOARD_FORMAT})\n\nWrite ${DIR}/lesson.js containing ONLY metadata (scenes live in scenes/NN.js files written later):\nLESSON({ id: '${A.id}', title: '${A.title}', short: '<short badge label>', module: '${A.module}',${A.poc ? " poc: true," : ''} summary: '<one sentence, conclusion first>', keep: [['<bold lead that carries the idea alone>', '<supporting sentence>'], x3], images: { plate: '../../engine/assets/teahouse-night.jpg' }, noBadge: ['01', '<last section number>'] });\nReturn the structured result.`,
  { label: 'judge', phase: 'Judge', schema: JUDGE_SCHEMA })
log(`judge picked ${judged.winner}; ${judged.words} words; ${judged.sections.length} sections`)

// ---------- Fact-check ----------
phase('Fact-check')
const FC_SCHEMA = { type: 'object', properties: { issues: { type: 'array', items: { type: 'object', properties: {
  quote: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' }, severity: { type: 'string', enum: ['wrong', 'misleading', 'nitpick'] } }, required: ['quote', 'problem', 'fix', 'severity'] } } }, required: ['issues'] }
const LENSES = [
  { k: 'facts', how: 'every factual claim: names, dates, what a tool is/does, who made it, numbers. Use WebSearch/WebFetch to verify anything you are not certain of.' },
  { k: 'currency', how: `currency and completeness as of ${TODAY}: compare the script with ${DIR}/plan.md and the research files. Flag any MUST-COVER item missing or too thin, anything described as current that is outdated, a speculative or beta claim stated as fact, and product names, prices or limits that changed. Verify the newest claims with WebSearch.` },
  { k: 'beginner', how: 'technical accuracy of every simplification: would any sentence leave a beginner with a WRONG mental model (not just a simplified one)? Also check on-screen literal text in storyboard.md (commands, file names, error messages) is realistic for Windows.' },
]
const checks = await parallel(LENSES.map(l => () => agent(
  `[AGENT: factcheck-${l.k}]\n${BRIEF}\n\nAdversarially fact-check ${DIR}/script.md and ${DIR}/storyboard.md (the research notes in ${DIR}/research-*.md are leads, not proof: verify). Your lens: ${l.how}\nFlag only real problems ("wrong" or "misleading"); use "nitpick" sparingly. For each, quote the exact text, explain, and give replacement wording that keeps the spoken rhythm. Do not edit files. Return the issues (empty list if clean).`,
  { label: `factcheck:${l.k}`, phase: 'Fact-check', schema: FC_SCHEMA })))
const issues = checks.filter(Boolean).flatMap(c => c.issues).filter(i => i.severity !== 'nitpick')
log(`fact-check: ${issues.length} issue(s) to fix`)
if (issues.length) {
  await agent(`[AGENT: factfix]\n${BRIEF}\n\nApply these fact-check findings to ${DIR}/script.md (and storyboard.md / lesson.js if they repeat the claim). Keep cue markers and section structure intact. If you judge a finding itself wrong, leave the text and say why.\nFindings: ${JSON.stringify(issues)}\nReturn a short list of what you changed.`, { label: 'factfix', phase: 'Fact-check' })
}

// ---------- Narrate ----------
phase('Narrate')
const NARR_SCHEMA = { type: 'object', properties: { duration: { type: 'number' }, characters: { type: 'number' }, narrator: { type: 'string' }, qa: { type: 'string' }, cueTable: { type: 'string' }, problems: { type: 'string' } }, required: ['duration', 'cueTable', 'narrator'] }
const narr = await agent(
  `[AGENT: narrator]\n${BRIEF}\n\nProduce the narration.\n1. \`${CD} && python tools/narrate.py ${SLUG} --dry-run\` — confirm ${WORDS[0]}–${WORDS[1]} words (±5%), that any [guest] sections follow the GUEST rule above (narrate.py prints "GUEST SEGMENT PROBLEM" when they do not; fix script.md and re-run until it does not) and that every section has cues. If a sentence has a spoken form the voice may mangle (acronyms, file extensions, symbols), fix the spelling in script.md first.\n2. \`${CD} && python tools/narrate.py ${SLUG}\` (ElevenLabs; the key is already stored; sections are cached). It first gives this lesson its narrator (tools/voice.py: only the narrators of 00.01 and 00.02 (RClayton and Adrian, listed in voices/roster.json), alternating so consecutive lessons differ (Aaron's rule since 2026-10-01)), then transcribes every section and compares it with the script (QA lines; one automatic re-take above 10% word error).\n3. If a section is still flagged CHECK, read what was heard: a genuinely mispronounced word -> respell it for the ear in script.md and re-run step 2 (only changed sections re-bill); a transcript that merely differs in formatting (numbers, punctuation, product names) is fine. If the voice is clearly wrong for a teacher across several sections: \`${CD} && python tools/voice.py ${SLUG} --reroll\` (switches to the other roster voice) then step 2 with --force.\n4. \`${CD} && python tools/mix.py ${SLUG}\`\n5. Read ${DIR}/cues.json and report: total duration, characters billed, the narrator's name, the QA word error per section, and a compact cue table "NN start–end: cue@local-seconds, ...".\nIf ElevenLabs errors, report the exact error and stop.`,
  { label: 'narrator', phase: 'Narrate', schema: NARR_SCHEMA })
log(`narration ${narr.duration}s by ${narr.narrator}`)

// ---------- Design: shared visuals ----------
phase('Design')
const DESIGN_SCHEMA = { type: 'object', properties: { api: { type: 'string' }, notes: { type: 'string' } }, required: ['api'] }
const design = await agent(
  `[AGENT: designer]\n${BRIEF}\n\nRead ${DIR}/storyboard.md, ${DIR}/script.md, ${DIR}/cues.json and ${COURSE}/engine/KIT.md (and skim ${COURSE}/engine/kit.js for exact signatures). Load the aaron-brand skill.\nWrite ${DIR}/scenes/00-shared.js: the lesson's RECURRING visual objects as reusable drawing functions on a lesson namespace, e.g. \`window.M = { drawMetaphor(t, x, y, s, state) {...}, layout: {...}, palette: {...} }\`, so every scene draws the metaphor object, the protagonist (if any) and repeated layouts identically. Only functions and constants: no SCENE() calls. Pure functions of their arguments (no Date.now/Math.random; use K.rng).\nTest it: write a TEMPORARY ${DIR}/scenes/01.js that calls your functions in a few states, run \`${CD} && python tools/stills.py ${SLUG} --scene 01 --every 2\`, Read the PNGs in ${DIR}/out/stills-01/ and check they look crafted, on-brand and legible at the sizes scenes will use. Iterate at least twice. Then DELETE the temporary scenes/01.js and the out/stills-01 folder.\nReturn: "api" — a precise reference of window.M (every function, its parameters, the states it supports, sizes that look good), and "notes" — visual direction every scene animator must follow (palette choices, where things sit, recurring motion).`,
  { label: 'designer', phase: 'Design', schema: DESIGN_SCHEMA })

// ---------- Animate: one agent per scene ----------
phase('Animate')
const SCENE_SCHEMA = { type: 'object', properties: { scene: { type: 'string' }, passes: { type: 'number' }, summary: { type: 'string' }, concerns: { type: 'string' }, engineRequests: { type: 'string', description: 'changes the shared engine/ or tools/ would need (you may not edit them yourself); empty if none' } }, required: ['scene', 'passes', 'summary'] }
const sceneKey = (x) => (String(x).match(/\d{2}/) || [String(x)])[0]
const sections = judged.sections
const sceneBrief = (s, extra) => `[AGENT: scene-${s.n}]\n${BRIEF}\n\nYou animate scene ${s.n} ("${s.title}") and ONLY that scene: write ${DIR}/scenes/${s.n}.js as \`SCENE('${s.n}', (t, S) => { ... })\`. Other animators are writing the other scenes in parallel right now; never touch their files or ${DIR}/scenes/00-shared.js, and NEVER edit anything in ${COURSE}/engine/ or ${COURSE}/tools/ (shared by every lesson and by the parallel animators): if the engine needs a change, work around it and describe the change in engineRequests.\nRead: ${DIR}/storyboard.md (your block, plus the blocks before and after yours for continuity of first/last frames), ${DIR}/script.md (your section's words), ${DIR}/cues.json (your section's start/end and cue times; S.cue('name') gives local time), ${COURSE}/engine/KIT.md, and the kit source ${COURSE}/engine/kit.js when unsure of a signature.\nShared lesson visuals (window.M, already loaded before your file):\n${design.api}\nVisual direction: ${design.notes || ''}\nRules: start with K.bg() (or K.plate for title/end cards; plate may be missing, then K.bg shows); everything a pure function of t; beats land ON their cues (things appear when they are said, not before); safe area x 80–1840, y 130–930; labels ≥ 26px; one idea per screen; calm first/last frames (scenes crossfade); at most one 'back' overshoot; the badge is drawn automatically.\nVerify like a craftsman: \`${CD} && python tools/stills.py ${SLUG} --scene ${s.n} --every 0.75\` then Read ${DIR}/out/sheet-${s.n}.jpg AND several full-size PNGs from ${DIR}/out/stills-${s.n}/ (especially just after each cue). Check: nothing overlaps unintentionally, no text clipped or off-canvas, contrast readable, motion states make sense mid-transition, the frame matches what is being SAID at that time (compare with cue times). Fix and re-render. At least 2 full passes; 3 if anything was wrong. Also fix any page errors the tool prints.${extra ? '\n' + extra : ''}\nReturn the structured summary with honest remaining concerns.`
const animated = await parallel(sections.map(s => () => agent(sceneBrief(s), { label: `scene:${s.n}`, phase: 'Animate', schema: SCENE_SCHEMA })))
log('animated: ' + animated.filter(Boolean).map(a => `${a.scene}(${a.passes} passes)`).join(' '))

// ---------- Review: two lenses, then targeted fixes; up to two rounds ----------
phase('Review')
const REVIEW_SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, issues: { type: 'array', items: { type: 'object', properties: {
  scene: { type: 'string' }, time: { type: 'number' }, problem: { type: 'string' }, fix: { type: 'string' }, severity: { type: 'string', enum: ['major', 'minor', 'polish'] } }, required: ['scene', 'problem', 'fix', 'severity'] } } }, required: ['verdict', 'issues'] }
const REVIEWERS = [
  { k: 'craft', how: 'visual craft and legibility: overlaps, clipping, off-canvas or tiny text, contrast, crowded frames, dead or static stretches longer than ~4 s, jarring jumps between scenes, brand (Tea House night palette, gold headings, pink only as decoration on title/end), anything that looks amateur.' },
  { k: 'teaching', how: 'teaching and sync: does each frame show what the narrator is saying at that moment (captions are burned in so you can compare)? Is the mental model clear and consistent from scene to scene? Would a smart beginner come away with the right picture? Does the very first spoken sentence say what the viewer will learn in this lesson, with the conclusion right after? Is the "Keep this" card strong?' },
]
const allFixes = []
for (let round = 1; round <= 2; round++) {
  const reviews = await parallel(REVIEWERS.map(r => () => agent(
    `[AGENT: review-${r.k}-r${round}]\n${BRIEF}\n\nReview the WHOLE lesson as a demanding creative director. Lens: ${r.how}\nRender: \`${CD} && python tools/stills.py ${SLUG} --every 1.5 --captions --tag ${r.k}\` then Read ${DIR}/out/sheet-${r.k}.jpg and open full-size PNGs from ${DIR}/out/stills-${r.k}/ wherever something might be off (look at many; zoom in on text). Also read ${DIR}/script.md and ${DIR}/cues.json.\nReport concrete, fixable issues per scene with the timestamp and the exact fix. "major" = a viewer would notice or be misled; "minor" = noticeable on a second look; "polish" = nice to have. Do not edit files.`,
    { label: `review:${r.k}:r${round}`, phase: 'Review', schema: REVIEW_SCHEMA })))
  const found = reviews.filter(Boolean).flatMap(r => r.issues).filter(i => i.severity !== 'polish' || round === 1)
  log(`review round ${round}: ${found.length} issue(s) — ` + reviews.filter(Boolean).map(r => r.verdict).join(' | '))
  if (!found.filter(i => i.severity !== 'polish').length && round > 1) break
  if (!found.length) break
  const byScene = {}
  found.forEach(i => { const k = sceneKey(i.scene); (byScene[k] = byScene[k] || []).push(i) })
  allFixes.push(...found)
  const fixed = await parallel(Object.entries(byScene).map(([n, list]) => () => {
    const s = sections.find(x => x.n === n) || { n, title: '' }
    return agent(sceneBrief(s, `THIS IS A FIX PASS. The scene already exists; improve it. Reviewers found:\n${JSON.stringify(list)}\nFix every major and minor item; polish items when cheap. If an issue lives in 00-shared.js, do not edit it — work around it in your scene and mention it.`),
      { label: `fix:${n}:r${round}`, phase: 'Review', schema: SCENE_SCHEMA })
  }))
  animated.push(...fixed.filter(Boolean))
}

// ---------- Engine requests (one agent, sequential: the engine is shared by every lesson) ----------
const requests = animated.filter(Boolean).map(a => a.engineRequests).filter(r => r && r.trim() && !/^(none|n\/a|-)\.?$/i.test(r.trim()))
let engine = null
if (requests.length) {
  engine = await agent(
    `[AGENT: engine]\n${BRIEF}\n\nScene animators asked for these changes to the shared engine/tools (they were not allowed to make them):\n${JSON.stringify(requests)}\nApply only those that clearly help EVERY lesson and cannot break existing ones (engine/kit.js, map.js, runtime.js, player.*, tools/*.py). Skip one-lesson conveniences (say why). After changing anything, prove nothing broke: \`${CD} && python tools/stills.py _sandbox --every 4 --tag engine\` and \`${CD} && python tools/stills.py ${SLUG} --every 6 --captions --tag engine\`, Read the sheets, and fix any regression. Note each change in ${COURSE}/engine/KIT.md if it changes the API. Return what you changed and what you skipped.`,
    { label: 'engine', phase: 'Review' })
}

// ---------- Final check before shipping ----------
const finalCheck = await agent(
  `[AGENT: final-check]\n${BRIEF}\n\nLast look before this lesson ships. \`${CD} && python tools/stills.py ${SLUG} --every 3 --captions --tag final --cols 6\`. Read ${DIR}/out/sheet-final.jpg, then full-size PNGs for every scene start and anything suspicious. Look for regressions from the fix rounds: a scene that throws (red error text), blank or black frames mid-lesson, text overlapping text, captions covering key content, first-person "I/my" spoken as Aaron (the narrator is a different voice; Aaron is "he"), anything a viewer would notice. Fix only clear, small problems directly in the scene file; list anything bigger. Return a one-paragraph verdict.`,
  { label: 'final-check', phase: 'Review' })

// ---------- Ship (optional) ----------
let shipped = null
if (A.ship) {
  phase('Ship')
  shipped = await agent(
    `[AGENT: shipper]\n${BRIEF}\n\n1. \`${CD} && python tools/render.py ${SLUG}\` (renders the MP4; ~5–10 min).\n2. Watch-check: extract 6 frames from ${DIR}/out/lesson.mp4 with ffmpeg at even intervals and Read them; confirm audio exists (ffprobe).\n3. \`${CD} && python tools/publish.py ${SLUG}\` and report the live URLs it verifies.\n4. Only AFTER publish succeeded: load the digikam-library skill and file the 1080p master in the Creative Library. Move ${DIR}/out/lesson.mp4 into a new folder ${DIR}/out/library_drop/ renamed the-hidden-curriculum_${SLUG}_1080p.mp4, run its \`library.py import "<that folder>" --dest missing_map\`, then annotate it (tags: Project/The Missing Map course (the library's existing tag for this course; keep it so everything stays together), Pipeline/External, Model/ElevenLabs (narration), Content/course lesson, Style/code-drawn animation, Stage/Final; a caption naming the lesson, its length, topic and narrator) and add the changelog line the skill asks for.${A.rebuild ? ` This is a REBUILD: name the file the-hidden-curriculum_${SLUG}_1080p_v2.mp4 (no clash with the old master) and re-tag the previous master of this lesson in Library/missing_map as Stage/Superseded.` : ''} The published site uses the copy publish.py already pushed (or out/lesson-720.mp4), so moving the master is safe.\n5. In ${COURSE}/curriculum.md set this lesson's status to published (unless it is a proof of concept) and add a Build log line with today's date, the lesson duration, the narrator's name (${DIR}/voice.json) and characters billed (${DIR}/audio/usage.json).${A.rebuild ? ' This is a rebuild: keep the existing Build log lines, update the row title if it changed, and add a new line saying what changed and why.' : ''}\n6. Only after publish succeeded: free the disk. Delete ${DIR}/out/stills-*/ folders and any other review-frame folders in ${DIR}/out/ (they are regenerated on demand; a lesson leaves 2 to 9 GB of them). Keep the mp4 files and sheet-*.jpg.\nIf publish.py fails because the site build fails, check https://www.cloudflarestatus.com/api/v2/incidents/unresolved.json for a Workers Builds incident before debugging the code, and say so.\nReturn the URLs, file sizes, render time and anything that failed.`,
    { label: 'ship', phase: 'Ship' })
}

return { plan, drafts: okDrafts.map(d => ({ angle: d.angle, words: d.words, metaphor: d.metaphor })), judged, factIssues: issues, narration: narr, design: design.notes, animated: animated.filter(Boolean).map(a => ({ scene: a.scene, passes: a.passes, concerns: a.concerns })), reviewFixes: allFixes.length, engine, finalCheck, shipped }
