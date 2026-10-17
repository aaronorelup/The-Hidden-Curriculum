export const meta = {
  name: 'missing-map-lesson',
  description: 'Build one lesson of The Hidden Curriculum from its spec and sources: read sources, plan, script, fact-check, narrate, capture real-computer demos, animate, review (optionally render + publish)',
  whenToUse: 'Producing one lesson of The Hidden Curriculum course end to end',
  phases: [
    { title: 'Sources', detail: 'read every source the lesson is built on; check what changed since' },
    { title: 'Plan', detail: 'the spec is the scope: sections, time budget, demos, credits' },
    { title: 'Script', detail: 'three angles written in parallel' },
    { title: 'Judge', detail: 'score drafts, synthesize final script + storyboard' },
    { title: 'Fact-check', detail: 'four adversarial verifiers, then fixes' },
    { title: 'Narrate', detail: 'map section from the curriculum, ElevenLabs narration + score; real-computer captures in parallel' },
    { title: 'Design', detail: 'shared visuals for the lesson' },
    { title: 'Animate', detail: 'one animator per scene (section 02 is the standard map scene)' },
    { title: 'Review', detail: 'two review lenses, fix rounds' },
    { title: 'Ship', detail: 'render MP4, publish, file in R2' },
  ],
}

// args: { lesson: <JSON from `python tools/course.py next` or `course.py lesson <key>`>, today: 'YYYY-MM-DD', ship, notes?, minutes?, sections?, rebuild?, course? }
// (the old form { id, title, module, slug } still works for proofs of concept)
const A = args || {}
const L = A.lesson || {}
const COURSE = A.course || 'C:/Users/soulo/Organized/Personal/My Projects/Courses/The-hidden-curriculum'
const KEY = L.key || A.key || A.slug
const SLUG = A.slug || KEY
const ID = L.id || A.id || '00.00'
const TITLE = L.title || A.title
const MODULE = L.moduleName || A.module || ''
const DIR = `${COURSE}/lessons/${SLUG}`
const SPEC = `${COURSE}/curriculum/lessons/${KEY}.md`
const CD = `cd "${COURSE}"`
const ROWSRC = (L.rowSources && L.rowSources.length ? L.rowSources : (L.sources || []).slice(0, 5))   // the 2-5 sources the lesson is built on
const LEAD = (L.lead && L.lead.length ? L.lead : (L.specFields && L.specFields.lead) || ROWSRC.slice(0, 1))  // credited on the title card
const OTHERSRC = (L.sources || []).filter(s => !ROWSRC.includes(s))   // sources the spec cites for single points
// Length: the spec's `minutes` (a number = about that long, or [lo, hi]); otherwise the course rule (Start lessons and
// each module's first lesson ~5 min, the rest ~10). Never over 20 (Aaron, 2026-10-01). ~140 spoken words per minute.
const specMin = A.minutes || L.minutes || (L.specFields && L.specFields.minutes)
const [MOD, NUM] = String(ID).split('.')
const MIN = (Array.isArray(specMin) ? specMin.map(Number)
  : specMin ? [Math.max(3.5, Number(specMin) * 0.85), Number(specMin) * 1.15]
  : (MOD === '00' || NUM === '01' ? [3.5, 5.5] : [8.5, 11.5])).map(m => Math.min(20, Math.round(m * 10) / 10))
const WORDS = MIN.map(m => Math.round(m * 140 / 10) * 10)
const SECTIONS = A.sections || (MIN[1] > 12 ? [Math.round(MIN[0]), Math.round(MIN[1])] : [Math.max(6, Math.round(MIN[0] * 60 / 45)), Math.max(8, Math.round(MIN[1] * 60 / 40))])
const TODAY = A.today || 'today (run `date +%F` to get it)'
const GUEST = MIN[1] > 15 ? `GUEST SEGMENT (required, this lesson runs over 15 minutes): exactly one run of 1–4 consecutive sections whose headings end in [guest] (e.g. "## 09 — Field notes [guest]"), at most 5 minutes in total (650 words at most). They are spoken by the course's guest voice, a third speaker who is never the narrator and never Aaron; run \`python tools/voice.py --guest\` to get the guest's first name. The narrator hands over by naming the guest, and the guest hands back at the end. Give the guest a real job that changes the pace: a myth-busting round, a field story told in the third person, a worked example, or a quick-fire recap. Never use the segment for padding. The storyboard marks the guest's scenes with a small lower-third card ("guest · <name>").` : 'No [guest] sections: this lesson is 15 minutes or shorter (only longer lessons have a guest).'
const LENGTH = `${MIN[0]}–${MIN[1]} minutes: ${WORDS[0]}–${WORDS[1]} spoken words in ${SECTIONS[0]}–${SECTIONS[1]} sections (the map section 02 included)`

const BRIEF = `You are on the production crew for "The Hidden Curriculum", Aaron Orelup's free, community-maintained, code-animated course. Its idea (Aaron, 2026-10-12): everyone can do everything with AI now; what stops people is small gaps in what they know, and those gaps move every week. Lessons build conceptual mental models (what it is, where it lives, what it connects to, what will surprise you, what YOU do versus what the agent does), never click-by-click tutorials. The rule under every lesson: the agent handles what can be verified; you check what it cannot, and when you cannot, you bring in an expert (above all for security).
Course folder: ${COURSE} (a git repo; the path has spaces: quote it). This lesson: key \`${KEY}\` (permanent; folder ${DIR}), shown as ${ID} "${TITLE}", module "${MODULE}"${L.district ? `, district "${L.district}"` : ''}.${A.poc ? ' This build is a PROOF OF CONCEPT; still make it as good as a real lesson.' : ''}
BINDING SCOPE: the lesson spec ${SPEC} says what this lesson must teach (each concept's numbered points with their depth: teach / brief / one line), the sources it is built on, "You vs the agent", the real-computer demos to show, the questions it answers, what is only introduced here (and which lesson owns it), and the framings to avoid. Read it first. Also read ${COURSE}/COURSE.md (the lesson contract: arc, voice, visual rules, safe areas) and skim ${COURSE}/curriculum.md (what other lessons own, so this one points to them instead of teaching them).
BUILT ON SOURCES (Aaron's rule since 2026-10-12): the course delivers other people's hard-won knowledge clearly and credits it. Every fact, number and claim comes from the spec's sources (full entries in ${COURSE}/curriculum/sources.md) or from this run's dated research, never from memory; when the lesson uses a source's finding it names who found it ("Veracode's July 2026 report...", "Addy Osmani calls this..."), and the lesson's credits list every source it used.
Use absolute paths. Run tools from the course folder, e.g. \`${CD} && python tools/stills.py ${SLUG} --scene 03 --every 1\` (Git Bash syntax).
Target length: ${LENGTH} (hard rule; never over 20 minutes).
Today is ${TODAY}. CURRENCY RULE (Aaron, 2026-10-02 and 2026-10-12): everything must be true and relevant as of this month. Facts can be current while the TOPIC is out of date (a lesson once taught hand-debugging when agents debug their own errors): if anything in the spec now describes a job the agent does by itself, teach the human's part instead and say so in your result.
THE MAP SECTION: section 02 of script.md ("## 02 — Where this sits on the map [map]", between <!-- map:begin --> and <!-- map:end -->) and scenes/02.js are GENERATED from curriculum.md by tools/course.py sync and drawn by K.map.intro: never write or edit them. Only section 02 talks about the map. No other section may name the district, the module, any lesson number or "the next lesson" (those change when the course is restructured, and the lesson must survive a restructure with only section 02 re-narrated); refer to other lessons by what they teach ("the lesson on keys").
${GUEST}
${A.notes ? 'Orchestrator notes: ' + A.notes : ''}`

const SCRIPT_FORMAT = `script.md format (exactly):
# ${ID} — ${TITLE}
<!-- lead=1.6 gap=0.8 tail=3 -->
## 01 — <section title>
<spoken narration for this scene, with [[cue-name]] markers placed exactly before the word where an animation beat should land>
> optional production note lines start with ">" and are never spoken
## 02 — Where this sits on the map [map]
<copy section 02 EXACTLY as it is in the scaffolded ${DIR}/script.md (its map:begin/map:end block); tools/course.py sync owns it>
## 03 — <section title>
...
Rules: the narrator is one of the course's two roster voices (never Aaron): no "I/my" as Aaron (tell his true stories in the third person: "Aaron, who made this course, ..."); spell for the ear per COURSE.md's pronunciation list (".venv" = "dot V E N V"); ${SECTIONS[0]}–${SECTIONS[1]} sections; ${WORDS[0]}–${WORDS[1]} spoken words total (${MIN[0]}–${MIN[1]} min at ~140 wpm); a longer lesson spends the extra time on the mental model, the mechanism and the surprises, never on padding; about one [[cue]] per 10–15 spoken seconds with short kebab-case names; the very first spoken sentence of section 01 states the lesson's purpose (the spec's purpose line, "In this lesson you'll learn ...") before any story, hook or question (Aaron's rule), and the next sentence states the conclusion; name sources when using their findings; the last section is the "Keep this" end card with exactly three takeaways spoken plainly, followed by one short spoken credit line ("This lesson is built on work by ...", naming only the lesson's own sources ${ROWSRC.join(', ')}). The title card shows the lead source (${LEAD.join(', ')}) as "Built on <author>, <title>".`

const STORYBOARD_FORMAT = `storyboard.md format: one "## NN — title" block per script section with: **Metaphor object** (what persists), **Frame** (what is on screen, positions on the 1920x1080 canvas, drawn with the kit in ${COURSE}/engine/KIT.md: windows, terminals, editors, files, cards, pills, arrows, line icons, the painted plate, and REAL COMPUTER FOOTAGE: captures shown with K.demo / K.shot / K.termReplay, still screenshots with K.image, and at most one Blender 3D shot with K.video; see engine/KIT.md "Media exhibits" and ${COURSE}/docs/showing-real-computer-actions.md), **Capture** (if the scene shows a real capture: its name, the exact steps to record and the marks the scene times on), **Beats** (one bullet per [[cue]]: what appears/moves when that cue is spoken), **Exit** (calm last frame). Section 02 says only "standard map scene (K.map.intro)". The end card shows the three takeaways and a small "Built on" credit line with the sources' authors. Title card may use the painted plate engine/assets/teahouse-night.jpg.`

// ---------- Sources: read what the lesson is built on; check what changed ----------
phase('Sources')
const batches = []
for (let i = 0; i < OTHERSRC.length; i += 6) batches.push(OTHERSRC.slice(i, i + 6))
const readers = ROWSRC.map(sid => () => agent(
  `[AGENT: source-${sid}]\n${BRIEF}\n\nRe-read source ${sid} in full (its entry, with URL and date, is in ${COURSE}/curriculum/sources.md; the spec ${SPEC} says what this lesson takes from it). For a video use the youtube-transcript skill; if the page is gone, try web.archive.org. Write ${DIR}/sources/${sid}.md: the credit line (author, title, publisher, date, URL), then every fact, number, definition and example this lesson uses from it, checked against the source itself (exact figures, what was measured and on what, caveats the source states), at most two short quotes (under 15 words each), and anything in the spec that the source does NOT actually say. Then check whether it is still current as of ${TODAY}: a newer version, a correction, a newer report that supersedes it (WebSearch). Return a 5-line summary and any spec point that is wrong.`,
  { label: `source:${sid}`, phase: 'Sources' })).concat(batches.map((b, i) => () => agent(
  `[AGENT: sources-points-${i + 1}]\n${BRIEF}\n\nThe spec ${SPEC} also cites these sources for single points: ${b.join(', ')} (entries in ${COURSE}/curriculum/sources.md). For each, open it and check ONLY the specific points the spec takes from it (exact figures, wording, dates, caveats). Write ${DIR}/sources/${b[0]}-points.md: per source, the credit line and each point as the source states it, or "NOT SUPPORTED" with what it actually says. Return a short list of spec points that are wrong.`,
  { label: `sources:points-${i + 1}`, phase: 'Sources' })))
const RESEARCH = { k: 'now', how: `the spec's claims AS OF ${TODAY}: re-verify the spec's dated claims, product names, defaults, prices and limits against their cited pages and current docs, and flag every one that changed after the spec was written (2026-10-12); whether any credible, dated source now says part of the topic is something agents do by themselves (so the lesson should teach the human's role instead); for AI and security subjects, the change arc in 2-3 dated sentences (before agents, what changed, now, where it is heading). Tag every claim established / new this year / beta / speculation, with its source URL and date. NEW TOPICS the spec does not cover go to ${DIR}/proposed-additions.md (topic, why it matters, dated sources) for the curriculum to consider later, never into this lesson.` }
await parallel([...readers, () => agent(
  `[AGENT: research-now]\n${BRIEF}\n\nResearch, do not write the lesson. Lens: ${RESEARCH.how}\nUse WebSearch (mode "extended" for very recent or niche items) and WebFetch; your memory is out of date. Write ${DIR}/research-now.md: one heading per spec concept, short factual bullets each with source URL, date and status tag, then "traps" (things commonly said that are now wrong) and "framing check". Return a 5-line summary.`,
  { label: 'research:now', phase: 'Sources' })])

// ---------- Plan ----------
phase('Plan')
const PLAN_SCHEMA = { type: 'object', properties: {
  purpose: { type: 'string' }, mustCover: { type: 'array', items: { type: 'string' } },
  deferred: { type: 'array', items: { type: 'object', properties: { topic: { type: 'string' }, where: { type: 'string' } }, required: ['topic', 'where'] } },
  captures: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, mode: { type: 'string', enum: ['browser', 'terminal', 'screenshot', 'desktop'] }, what: { type: 'string' }, proves: { type: 'string' }, section: { type: 'string' } }, required: ['name', 'mode', 'what', 'section'] } },
  blender: { type: 'string', description: 'a one-paragraph brief for ONE 3D shot that genuinely clarifies an idea, or empty' },
  credits: { type: 'array', items: { type: 'string' }, description: 'S-IDs this lesson credits' },
  specChanges: { type: 'string', description: 'points of the spec this lesson changed or dropped, and why (wrong per the source, outdated, owned elsewhere)' },
  minutes: { type: 'string' } }, required: ['purpose', 'mustCover', 'deferred', 'captures', 'credits'] }
const plan = await agent(
  `[AGENT: planner]\n${BRIEF}\n\nPlan the lesson's CONTENT before anyone writes a line. Read the spec ${SPEC}, every note in ${DIR}/sources/, ${DIR}/research-now.md, ${COURSE}/COURSE.md and ALL of ${COURSE}/curriculum.md.\nWrite ${DIR}/plan.md with:\n1. Purpose line (the first spoken sentence; the spec's, tightened if needed) and the one-sentence conclusion.\n2. "As of" line.\n3. The change arc (required for AI and security subjects), 2-3 sentences: before agents (dated), what changed (dated), now, where it is heading. The pace is weeks, not years.\n4. MUST-COVER: copied from the spec's "What to teach", every point with the spec's depth (teach / brief / one line), the sources it rests on and a seconds budget; budgets sum to the target length. Add nothing the spec does not list (new topics belong in ${DIR}/proposed-additions.md). Group them into scene-sized sections in script order: 01 purpose + conclusion, 02 the standard map section (about 15 s, generated), then the rest most-useful-first, ONE scene built from the spec's "You vs the agent" (mandatory: what the agent does on its own, what the viewer must check or decide, when to bring in an expert), and the "Keep this" end card last. If a source note or research-now shows a spec point is wrong or outdated, fix or drop it and say why (specChanges).\n5. DEFERRED: topics only introduced here, each with the lesson KEY that owns it (curriculum.md), never a number.\n6. Mental model: one metaphor that carries the lesson and transforms as it goes, and where it breaks.\n7. REAL COMPUTER ACTIONS: from the spec's "Show it for real", pick the 1 to 3 that best let a viewer SEE the idea and that can be recorded safely and unattended (read ${COURSE}/docs/showing-real-computer-actions.md: browser captures of public pages or local throwaway apps, terminal captures of real commands in a temp folder, real screenshots animated with a cursor; desktop captures only when an interactive session is available). Give each a short name, mode, exact steps, which section shows it, and what it proves. Never real keys, tokens, emails or personal data.\n8. Optional 3D: one Blender shot only if 3D genuinely clarifies an idea (read ${COURSE}/docs/blender-shots.md); otherwise none.\n9. Credits: the S-IDs this lesson uses, with how each is named on screen. The title card credits the lead source(s) ${LEAD.join(', ')}; the narration names at most the lesson's own sources (${ROWSRC.join(', ')}), and the page credits every source used.\n10. Cut list and facts to handle carefully (hedged wording for new, beta or speculative claims).\nReturn the structured summary.`,
  { label: 'planner', phase: 'Plan', schema: PLAN_SCHEMA })
log(`plan: ${plan.mustCover.length} must-cover, ${plan.deferred.length} deferred, ${plan.captures.length} captures${plan.blender ? ', 1 Blender shot' : ''}`)
const PLANNED = `The content plan is ${DIR}/plan.md (read it first; facts are in ${DIR}/sources/*.md and ${DIR}/research-now.md; scope is the spec ${SPEC}). Cover every MUST-COVER item at its planned depth, in its planned section, within its time budget; use the plan's purpose line, change arc, mental model, captures and credits; use the hedged wording for new/beta/speculative claims.`

// ---------- Script: three angles ----------
phase('Script')
const ANGLES = [
  { k: 'A', name: 'story-first', how: 'After the opening purpose sentence (required for every angle), tell one concrete, true, relatable moment from the sources (an incident, a study participant, a practitioner\'s story) or from Aaron\'s own true stories in COURSE.md, and widen from there to the idea.' },
  { k: 'B', name: 'metaphor-first', how: 'Build the whole lesson around ONE strong visual metaphor that can be drawn and that transforms as the lesson goes on; the metaphor is the mental model.' },
  { k: 'C', name: 'evidence-first', how: 'Lead with what the sources found (the numbers, the incidents, the real screens), then the mental model that explains it, then what the viewer does versus what the agent does; crisp and skimmable.' },
]
const DRAFT_SCHEMA = { type: 'object', properties: {
  angle: { type: 'string' }, words: { type: 'number' }, metaphor: { type: 'string' },
  sections: { type: 'array', items: { type: 'object', properties: { n: { type: 'string' }, title: { type: 'string' }, beat: { type: 'string' } }, required: ['n', 'title'] } },
  pitch: { type: 'string' } }, required: ['angle', 'words', 'sections', 'pitch'] }
const drafts = await parallel(ANGLES.map(g => () => agent(
  `[AGENT: script-${g.k}]\n${BRIEF}\n\nYour job: write a complete draft script + storyboard for this lesson from the "${g.name}" angle. ${PLANNED} ${g.how}\n\n${SCRIPT_FORMAT}\n\n${STORYBOARD_FORMAT}\n\nAlso load the aaron-brand skill for voice. Keep facts checkable; do not invent statistics or anecdotes.\nWrite ${DIR}/drafts/script-${g.k}.md and ${DIR}/drafts/storyboard-${g.k}.md. Count the spoken words (exclude headings, notes, cue markers; include section 02) and report them. Return the structured summary.`,
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
  `[AGENT: judge]\n${BRIEF}\n\nThree drafts exist: ${DIR}/drafts/script-{A,B,C}.md and storyboard-{A,B,C}.md. Pitches: ${JSON.stringify(okDrafts.map(d => ({ angle: d.angle, words: d.words, metaphor: d.metaphor, pitch: d.pitch })))}\n\nScore each 1–10 on: (1) conceptual clarity for a smart beginner, (2) opens with the purpose sentence as the very first words, then the conclusion, no withheld payoff, (3) strength and drawability of the mental model, (4) the "surprises you'll hit" payload, (5) voice per aaron-brand (load that skill), (6) the human's role taught where it matters (verify what can be verified; check or bring an expert for what cannot), (7) animation potential with the kit and the planned real-computer captures, (8) factual safety and sources named when used, (9) coverage of ${DIR}/plan.md's MUST-COVER list (list anything a draft dropped or got wrong), (10) currency as of ${TODAY}. Pick a winner, then SYNTHESIZE the final version, which MUST cover every must-cover item: keep the winner's spine, graft the best lines from the others. Tighten ruthlessly.\n\nWrite the final ${DIR}/script.md (${SCRIPT_FORMAT}) — read the scaffolded ${DIR}/script.md FIRST and keep its section 02 byte for byte.\n\nWrite the final ${DIR}/storyboard.md (${STORYBOARD_FORMAT})\n\nWrite ${DIR}/lesson.js containing ONLY metadata (scenes live in scenes/NN.js files written later; tools/course.py sync rewrites key/id/module):\nLESSON({ key: '${KEY}', id: '${ID}', title: '${TITLE}', short: '<short badge label>', module: '${MODULE}',${A.poc ? ' poc: true,' : ''} summary: '<one sentence, conclusion first>', keep: [['<bold lead that carries the idea alone>', '<supporting sentence>'], x3], credits: [{ id: 'S0xx', who: '<author or publisher>', title: '<title>', date: '<YYYY-MM-DD>', url: '<url>' }, ...every source the lesson uses, from ${COURSE}/curriculum/sources.md], images: { plate: '../../engine/assets/teahouse-night.jpg' }, captures: {}, noBadge: ['01', '<last section number>'] });\nReturn the structured result.`,
  { label: 'judge', phase: 'Judge', schema: JUDGE_SCHEMA })
log(`judge picked ${judged.winner}; ${judged.words} words; ${judged.sections.length} sections`)

// ---------- Fact-check ----------
phase('Fact-check')
const FC_SCHEMA = { type: 'object', properties: { issues: { type: 'array', items: { type: 'object', properties: {
  quote: { type: 'string' }, problem: { type: 'string' }, fix: { type: 'string' }, severity: { type: 'string', enum: ['wrong', 'misleading', 'nitpick'] } }, required: ['quote', 'problem', 'fix', 'severity'] } } }, required: ['issues'] }
const LENSES = [
  { k: 'sources', how: `fidelity to the sources: every number, finding and attribution in the script and storyboard must match what the source actually says (${DIR}/sources/*.md, and the source itself when in doubt), with its caveats (what was measured, on whom, when); flag findings used without naming who found it, and credits in lesson.js that are missing or wrong.` },
  { k: 'facts', how: 'every other factual claim: names, dates, what a tool is or does, who made it, numbers. Use WebSearch/WebFetch to verify anything you are not certain of.' },
  { k: 'currency', how: `the spec first, then currency, as of ${TODAY}: compare the script with the spec ${SPEC} ("What to teach" with its depths, "You vs the agent", "Out-of-date framings to avoid"), then ${DIR}/plan.md and ${DIR}/research-now.md. Flag any MUST-COVER item missing or too thin, anything described as current that is outdated, a job described as the human's that the agent now does by itself, a beta or speculative claim stated as fact, and product names, prices or limits that changed. Verify the newest claims with WebSearch.` },
  { k: 'beginner', how: 'technical accuracy of every simplification: would any sentence leave a beginner with a WRONG mental model (not just a simplified one)? Check on-screen literal text in storyboard.md (commands, file names, error messages, UI labels) is realistic, and that no section other than 02 names the district, module, a lesson number or "the next lesson".' },
]
const checks = await parallel(LENSES.map(l => () => agent(
  `[AGENT: factcheck-${l.k}]\n${BRIEF}\n\nAdversarially fact-check ${DIR}/script.md, ${DIR}/storyboard.md and ${DIR}/lesson.js. Your lens: ${l.how}\nFlag only real problems ("wrong" or "misleading"); use "nitpick" sparingly. For each, quote the exact text, explain, and give replacement wording that keeps the spoken rhythm. Do not edit files. Return the issues (empty list if clean).`,
  { label: `factcheck:${l.k}`, phase: 'Fact-check', schema: FC_SCHEMA })))
const issues = checks.filter(Boolean).flatMap(c => c.issues).filter(i => i.severity !== 'nitpick')
log(`fact-check: ${issues.length} issue(s) to fix`)
if (issues.length) {
  await agent(`[AGENT: factfix]\n${BRIEF}\n\nApply these fact-check findings to ${DIR}/script.md (and storyboard.md / lesson.js if they repeat the claim). Keep cue markers, section structure and section 02 intact. If you judge a finding itself wrong, leave the text and say why.\nFindings: ${JSON.stringify(issues)}\nReturn a short list of what you changed.`, { label: 'factfix', phase: 'Fact-check' })
}

// ---------- Narrate + capture (in parallel: narration touches script/audio/cues, capture touches assets/steps/lesson.js captures) ----------
phase('Narrate')
const NARR_SCHEMA = { type: 'object', properties: { duration: { type: 'number' }, characters: { type: 'number' }, narrator: { type: 'string' }, qa: { type: 'string' }, cueTable: { type: 'string' }, problems: { type: 'string' } }, required: ['duration', 'cueTable', 'narrator'] }
const CAP_SCHEMA = { type: 'object', properties: { captures: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, mode: { type: 'string' }, seconds: { type: 'number' }, marks: { type: 'string' }, files: { type: 'string' } }, required: ['name', 'mode'] } }, blender: { type: 'string' }, skipped: { type: 'string' } }, required: ['captures'] }
const [narr, caps] = await parallel([
  () => agent(
    `[AGENT: narrator]\n${BRIEF}\n\nProduce the narration.\n0. \`${CD} && python tools/course.py sync\` so section 02 holds the current generated map text (it only rewrites that block and lesson.js key/id/module), then check that script.md still has every other section intact.\n1. \`${CD} && python tools/narrate.py ${SLUG} --dry-run\` — confirm ${WORDS[0]}–${WORDS[1]} words (±5%), that any [guest] sections follow the GUEST rule (narrate.py prints "GUEST SEGMENT PROBLEM" when they do not; fix script.md and re-run until it does not) and that every section has cues. If a sentence has a spoken form the voice may mangle (acronyms, file extensions, symbols), fix the spelling in script.md first (never inside section 02: fix the curriculum or tools/course.py's spoken forms instead).\n2. \`${CD} && python tools/narrate.py ${SLUG}\` (ElevenLabs; the key is already stored; sections are cached). It gives this lesson its narrator (tools/voice.py: only RClayton and Adrian, voices/roster.json, alternating so consecutive lessons differ), then transcribes every section and compares it with the script (one automatic re-take above 10% word error).\n3. If a section is still flagged CHECK, read what was heard: a genuinely mispronounced word -> respell it for the ear in script.md and re-run step 2 (only changed sections re-bill); a transcript that merely differs in formatting is fine. If the voice is clearly wrong for a teacher across several sections: \`${CD} && python tools/voice.py ${SLUG} --reroll\` then step 2 with --force.\n4. \`${CD} && python tools/mix.py ${SLUG}\`\n5. Read ${DIR}/cues.json and report: total duration, characters billed, the narrator's name, the QA word error per section, and a compact cue table "NN start–end: cue@local-seconds, ...".\nIf ElevenLabs errors, report the exact error and stop.`,
    { label: 'narrator', phase: 'Narrate', schema: NARR_SCHEMA }),
  () => (plan.captures.length || plan.blender) ? agent(
    `[AGENT: capture]\n${BRIEF}\n\nRecord the real-computer footage this lesson shows. Planned captures: ${JSON.stringify(plan.captures)}.${plan.blender ? `\nPlanned 3D shot: ${plan.blender}` : ''}\nRead ${COURSE}/docs/showing-real-computer-actions.md, the "Media exhibits" section of ${COURSE}/engine/KIT.md (captures, K.demo, K.shot, K.termReplay, marks) and ${DIR}/storyboard.md (each scene's Capture block). For each capture: write the recipe ${DIR}/steps/<name>.json with \`mark\` steps for every moment a scene must time on, record it with tools/capture.py (browser and terminal modes run headless; desktop mode only if an unlocked interactive desktop is available, otherwise switch that capture to a browser capture or real screenshots and say so), run \`python tools/capture.py check ${SLUG}\`, look at the shots, and register it in ${DIR}/lesson.js \`captures: { <name>: 'assets/capture/<name>/' }\` (edit only that field). Safety rules are hard: public pages or a local throwaway app/folder only, test values only, never real keys, tokens, emails, account names or personal data (capture.py refuses many; you still look at every shot). Keep each clip small (the docs give the per-lesson budget).${plan.blender ? ` For the 3D shot: read ${COURSE}/docs/blender-shots.md, write ${DIR}/blender/<shot>.py, load the gpu-queue skill and reserve the GPU before rendering, render with tools/blender_shot.py, release the GPU, and register the clip in lesson.js videos.` : ''}\nReturn each capture's name, mode, length, its marks, and anything you had to change from the plan.`,
    { label: 'capture', phase: 'Narrate', schema: CAP_SCHEMA }) : Promise.resolve({ captures: [], skipped: 'none planned' }),
])
log(`narration ${narr.duration}s by ${narr.narrator}; captures: ${(caps && caps.captures || []).map(c => c.name).join(', ') || 'none'}`)
const CAPTURED = caps && caps.captures && caps.captures.length ? `Real-computer captures recorded for this lesson (registered in lesson.js; read engine/KIT.md "Media exhibits" and use K.captureAt / K.captureBox marks, never hard-coded times or positions): ${JSON.stringify(caps.captures)}${caps.blender ? `\n3D shot: ${caps.blender}` : ''}` : 'No captures were recorded for this lesson.'

// ---------- Design: shared visuals ----------
phase('Design')
const DESIGN_SCHEMA = { type: 'object', properties: { api: { type: 'string' }, notes: { type: 'string' } }, required: ['api'] }
const design = await agent(
  `[AGENT: designer]\n${BRIEF}\n\nRead ${DIR}/storyboard.md, ${DIR}/script.md, ${DIR}/cues.json and ${COURSE}/engine/KIT.md (and skim ${COURSE}/engine/kit.js for exact signatures). Load the aaron-brand skill.\n${CAPTURED}\nWrite ${DIR}/scenes/00-shared.js: the lesson's RECURRING visual objects as reusable drawing functions on a lesson namespace, e.g. \`window.M = { drawMetaphor(t, x, y, s, state) {...}, layout: {...}, palette: {...} }\`, so every scene draws the metaphor object and repeated layouts identically, plus a shared credits strip for the end card (from lesson.js credits). Only functions and constants: no SCENE() calls. Pure functions of their arguments (no Date.now/Math.random; use K.rng).\nTest it: write a TEMPORARY ${DIR}/scenes/01.js that calls your functions in a few states, run \`${CD} && python tools/stills.py ${SLUG} --scene 01 --every 2\`, Read the PNGs in ${DIR}/out/stills-01/ and check they look crafted, on-brand and legible at the sizes scenes will use. Iterate at least twice. Then DELETE the temporary scenes/01.js and the out/stills-01 folder. Never touch scenes/02.js (the standard map scene).\nReturn: "api" — a precise reference of window.M, and "notes" — visual direction every scene animator must follow.`,
  { label: 'designer', phase: 'Design', schema: DESIGN_SCHEMA })

// ---------- Animate: one agent per scene (02 is the standard map scene) ----------
phase('Animate')
const SCENE_SCHEMA = { type: 'object', properties: { scene: { type: 'string' }, passes: { type: 'number' }, summary: { type: 'string' }, concerns: { type: 'string' }, engineRequests: { type: 'string', description: 'changes the shared engine/ or tools/ would need (you may not edit them yourself); empty if none' } }, required: ['scene', 'passes', 'summary'] }
const sceneKey = (x) => (String(x).match(/\d{2}/) || [String(x)])[0]
const sections = judged.sections.filter(s => sceneKey(s.n) !== '02')
const sceneBrief = (s, extra) => `[AGENT: scene-${s.n}]\n${BRIEF}\n\nYou animate scene ${s.n} ("${s.title}") and ONLY that scene: write ${DIR}/scenes/${s.n}.js as \`SCENE('${s.n}', (t, S) => { ... })\`. Other animators are writing the other scenes in parallel right now; never touch their files, ${DIR}/scenes/00-shared.js or ${DIR}/scenes/02.js, and NEVER edit anything in ${COURSE}/engine/ or ${COURSE}/tools/: if the engine needs a change, work around it and describe the change in engineRequests.\nRead: ${DIR}/storyboard.md (your block, plus the blocks before and after yours for continuity of first/last frames), ${DIR}/script.md (your section's words), ${DIR}/cues.json (your section's start/end and cue times; S.cue('name') gives local time), ${COURSE}/engine/KIT.md, and the kit source ${COURSE}/engine/kit.js when unsure of a signature.\n${CAPTURED}\nShared lesson visuals (window.M, already loaded before your file):\n${design.api}\nVisual direction: ${design.notes || ''}\nRules: start with K.bg() (or K.plate for title/end cards); everything a pure function of t; beats land ON their cues; real footage is shown inside calm window chrome and the narration only points at what the camera has zoomed onto; safe area x 80–1840, y 130–930; labels ≥ 26px; one idea per screen; calm first/last frames (scenes crossfade); at most one 'back' overshoot; the badge is drawn automatically.\nVerify like a craftsman: \`${CD} && python tools/stills.py ${SLUG} --scene ${s.n} --every 0.75\` then Read ${DIR}/out/sheet-${s.n}.jpg AND several full-size PNGs from ${DIR}/out/stills-${s.n}/ (especially just after each cue). Check: nothing overlaps unintentionally, no text clipped or off-canvas, contrast readable, motion states make sense mid-transition, the frame matches what is being SAID at that time. Fix and re-render. At least 2 full passes; 3 if anything was wrong. Also fix any page errors the tool prints.${extra ? '\n' + extra : ''}\nReturn the structured summary with honest remaining concerns.`
const animated = await parallel(sections.map(s => () => agent(sceneBrief(s), { label: `scene:${s.n}`, phase: 'Animate', schema: SCENE_SCHEMA })))
log('animated: ' + animated.filter(Boolean).map(a => `${a.scene}(${a.passes} passes)`).join(' '))

// ---------- Review: two lenses, then targeted fixes; up to two rounds ----------
phase('Review')
const REVIEW_SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, issues: { type: 'array', items: { type: 'object', properties: {
  scene: { type: 'string' }, time: { type: 'number' }, problem: { type: 'string' }, fix: { type: 'string' }, severity: { type: 'string', enum: ['major', 'minor', 'polish'] } }, required: ['scene', 'problem', 'fix', 'severity'] } } }, required: ['verdict', 'issues'] }
const REVIEWERS = [
  { k: 'craft', how: 'visual craft and legibility: overlaps, clipping, off-canvas or tiny text, contrast, crowded frames, dead or static stretches longer than ~4 s, jarring jumps between scenes, real footage that is unreadable or shakes, brand (Tea House night palette, gold headings, pink only as decoration on title/end), anything that looks amateur.' },
  { k: 'teaching', how: 'teaching and sync: does each frame show what the narrator is saying at that moment (captions are burned in so you can compare)? Is the mental model clear and consistent from scene to scene? Does the real footage actually show what is claimed? Would a smart beginner come away with the right picture and know what is THEIR job versus the agent\'s? Does the very first spoken sentence say what the viewer will learn? Is the "Keep this" card strong, and are the sources credited?' },
]
const allFixes = []
for (let round = 1; round <= 2; round++) {
  const reviews = await parallel(REVIEWERS.map(r => () => agent(
    `[AGENT: review-${r.k}-r${round}]\n${BRIEF}\n\nReview the WHOLE lesson as a demanding creative director. Lens: ${r.how}\nRender: \`${CD} && python tools/stills.py ${SLUG} --every 1.5 --captions --tag ${r.k}\` then Read ${DIR}/out/sheet-${r.k}.jpg and open full-size PNGs from ${DIR}/out/stills-${r.k}/ wherever something might be off (look at many; zoom in on text). Also read ${DIR}/script.md and ${DIR}/cues.json. Scene 02 is the standard map scene: report problems there as engine issues (scene "02-engine"), never as scene fixes.\nReport concrete, fixable issues per scene with the timestamp and the exact fix. "major" = a viewer would notice or be misled; "minor" = noticeable on a second look; "polish" = nice to have. Do not edit files.`,
    { label: `review:${r.k}:r${round}`, phase: 'Review', schema: REVIEW_SCHEMA })))
  const found = reviews.filter(Boolean).flatMap(r => r.issues).filter(i => i.severity !== 'polish' || round === 1)
  log(`review round ${round}: ${found.length} issue(s) — ` + reviews.filter(Boolean).map(r => r.verdict).join(' | '))
  if (!found.filter(i => i.severity !== 'polish').length && round > 1) break
  if (!found.length) break
  const byScene = {}
  found.filter(i => sceneKey(i.scene) !== '02').forEach(i => { const k = sceneKey(i.scene); (byScene[k] = byScene[k] || []).push(i) })
  found.filter(i => sceneKey(i.scene) === '02').forEach(i => animated.push({ scene: '02', passes: 0, summary: 'standard map scene', engineRequests: `${i.problem} -> ${i.fix}` }))
  allFixes.push(...found)
  const fixed = await parallel(Object.entries(byScene).map(([n, list]) => () => {
    const s = sections.find(x => sceneKey(x.n) === n) || { n, title: '' }
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
    `[AGENT: engine]\n${BRIEF}\n\nScene animators and reviewers asked for these changes to the shared engine/tools (they were not allowed to make them):\n${JSON.stringify(requests)}\nApply only those that clearly help EVERY lesson and cannot break existing ones (engine/kit.js, map.js, runtime.js, player.*, tools/*.py). Skip one-lesson conveniences (say why). Legacy lessons load engine/legacy/map-v1.js and must render byte-identical: after changing anything, run \`${CD} && python tests/legacy_freeze/stills_hash.py engine-${SLUG} --no-png && python tests/legacy_freeze/compare.py before engine-${SLUG}\` (read tests/legacy_freeze/README.md first; it must print ALL IDENTICAL), \`${CD} && python tools/stills.py _sandbox --every 4 --tag engine\` and \`${CD} && python tools/stills.py ${SLUG} --every 6 --captions --tag engine\`, Read the sheets, and fix any regression. Note each change in ${COURSE}/engine/KIT.md if it changes the API. Return what you changed and what you skipped.`,
    { label: 'engine', phase: 'Review' })
}

// ---------- Final check before shipping ----------
const finalCheck = await agent(
  `[AGENT: final-check]\n${BRIEF}\n\nLast look before this lesson ships. \`${CD} && python tools/course.py check\` (must pass) and \`${CD} && python tools/stills.py ${SLUG} --every 3 --captions --tag final --cols 6\`. Read ${DIR}/out/sheet-final.jpg, then full-size PNGs for every scene start and anything suspicious. Look for regressions from the fix rounds: a scene that throws (red error text), blank or black frames mid-lesson, text overlapping text, captions covering key content, first-person "I/my" spoken as Aaron, real footage showing anything private, a section other than 02 naming the district, module or a lesson number, missing credits. Fix only clear, small problems directly in the scene file; list anything bigger. Return a one-paragraph verdict.`,
  { label: 'final-check', phase: 'Review' })

// ---------- Ship (optional) ----------
let shipped = null
if (A.ship) {
  phase('Ship')
  shipped = await agent(
    `[AGENT: shipper]\n${BRIEF}\n\n1. \`${CD} && python tools/render.py ${SLUG}\` (renders the MP4; ~5–10 min).\n2. Watch-check: extract 6 frames from ${DIR}/out/lesson.mp4 with ffmpeg at even intervals and Read them; confirm audio exists (ffprobe).\n3. \`${CD} && python tools/publish.py ${SLUG}\` and report the live URLs it verifies.\n4. Only AFTER publish succeeded: file the 1080p master in R2 (the digikam-library skill; digiKam itself is retired for filing since 2026-10-17). Move ${DIR}/out/lesson.mp4 into a new folder ${DIR}/out/library_drop/ renamed the-hidden-curriculum_${SLUG}_1080p.mp4, write a NOTES.md beside it (the lesson key and title, length, topic, narrator, "final"), then run \`python "C:/Users/soulo/Organized/Personal/My Projects/Sandbox 2/studio-infra/studio.py" push courses "<that folder>"\` and report the run id it prints. It lands in Aaron's review inbox.${A.rebuild ? ` This is a REBUILD: name the file the-hidden-curriculum_${SLUG}_1080p_v2.mp4 and say in NOTES.md which master it replaces.` : ''}\n5. In ${COURSE}/curriculum.md set this lesson's row status to \`published\` (and \`status: published\` in ${SPEC}), unless it is a proof of concept, and add a Build log line with today's date, the lesson's key and title, duration, narrator (${DIR}/voice.json), characters billed (${DIR}/audio/usage.json), captures used, and anything the plan changed from the spec. If the plan deferred a topic to a lesson that does not exist yet, add it to the Deep-dive backlog with its sources. Then \`${CD} && python tools/course.py check\` must pass.\n6. Commit the lesson's source files to the course repo (git add lessons/${SLUG} curriculum.md curriculum/lessons/${KEY}.md course.json engine/course.js; never out/, audio/*.wav or audio/mix.mp3, which .gitignore already excludes) with a message "Lesson ${ID} ${TITLE} (${KEY})", then \`git push\` (the remote is github.com/aaronorelup/The-Hidden-Curriculum; narration MP3s go through Git LFS). If the push fails, say so; do not force-push.\n7. Only after publish succeeded: free the disk. Delete ${DIR}/out/stills-*/ folders and any other review-frame folders in ${DIR}/out/. Keep the mp4 files and sheet-*.jpg.\nIf publish.py fails because the site build fails, check https://www.cloudflarestatus.com/api/v2/incidents/unresolved.json for a Workers Builds incident before debugging the code, and say so.\nReturn the URLs, file sizes, render time, the commit and anything that failed.`,
    { label: 'ship', phase: 'Ship' })
}

return { plan, drafts: okDrafts.map(d => ({ angle: d.angle, words: d.words, metaphor: d.metaphor })), judged, factIssues: issues, narration: narr, captures: caps, design: design.notes, animated: animated.filter(Boolean).map(a => ({ scene: a.scene, passes: a.passes, concerns: a.concerns })), reviewFixes: allFixes.length, engine, finalCheck, shipped }
