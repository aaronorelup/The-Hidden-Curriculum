# The Hidden Curriculum — course bible

Read this before writing or animating any lesson. It is the contract every lesson follows.

## What this course is

**A map, not a manual.** Aaron's words: *"this is more for conceptual understanding rather than
how-to tutorials... so that I get a framework in my head of all these different things, so that I will
be able to store it somewhere in my head when I come to doing them, instead of being surprised and
confused the whole way."*

So every lesson answers: **what is this thing, where does it live, what is it like, what does it
connect to, and what will surprise me when I meet it.** Never step-by-step instructions. A viewer
should finish a lesson unable to *do* the thing yet, but certain they'd recognise it, know what it's
for, and know which shelf in their head it goes on.

**The core idea (Aaron, 2026-10-12):** *everyone can do everything with AI now; the biggest hindrance is small gaps in
everyone's knowledge.* The course fills those gaps so people can build and do whatever they want, and it is updated as
the gaps change, because what you need to know changes every week. It is a **community project**: people add what they
wish they had known going in and the questions they want answered (GitHub issues and pull requests on
github.com/aaronorelup/The-Hidden-Curriculum), and lessons are combined, split, added, deleted and edited as that
evidence comes in. Every lesson's files live in that repo, so any lesson can be edited and re-rendered.

**The human's role is the spine of every lesson (Aaron, 2026-10-03 and 2026-10-12):** agents write, run and debug code
now, so the course never teaches hand-coding or hand-debugging as the learner's skill. *AI can handle anything that is
verifiable. The human must check anything the AI cannot verify, and if the human cannot, they must give it to an expert
who can.* That is true and necessary above all for security: AI-written code is notorious for being vulnerable, because
people assume the agent knows how to make it safe and believe it when it says the app is safe.

- **Audience:** people who build with AI but never got the "hidden curriculum". That includes someone with
  an IT degree, like Aaron (Information Systems + Data Science), who still wrote Python in a `.txt` file and didn't know to `cd` into
  the folder first. Smart, motivated, missing context. Never talk down.
- **Title:** *The Hidden Curriculum* (renamed from the working title *The Missing Map* on 2026-10-01; "the map" stays the
  name of the course's district device). Do **not** use "for Dummies" anywhere: it is a Wiley trademark.
- **Format:** 5–20 minute narrated animations (see Length below), drawn entirely in code (this engine), 1920×1080, plus
  an interactive web page (transcript, chapters, takeaways) at aaronorelup.com/courses/the-hidden-curriculum/.
- **Proof-of-concept lessons** live under `lessons/poc-*` and are not part of the final course.

## Built on sources, not on Claude's intuition (Aaron, 2026-10-12)

Claude's own sense of what needs teaching is out of date. Research can make a lesson's facts current and still miss
that its **topic** is out of date (00.06 v1 taught hand-debugging with 2026 numbers; nobody debugs by hand any more).
The lesson Aaron liked best was built on someone else's hard work (janus's writing on Loom) and only delivered it
clearly. So:

- **The curriculum comes from sources.** `curriculum/sources.md` lists the dated sources (syllabi, practitioner
  essays, incident write-ups, standards, surveys and studies, tool docs, community questions, Aaron's own practice);
  `curriculum/concepts.md` turns them into concepts, each with specific points that cite their sources;
  `curriculum.md` distributes the concepts into lessons; `curriculum/lessons/<key>.md` (the **spec**) says exactly
  what one lesson teaches. `curriculum/research/` records how all of it was found and challenged (2026-10-12: 274
  candidates, 85 read in depth, 251 cited, 78% dated 2026). New topics enter the same way: a dated source first.
- **A lesson is built on its spec's sources and credits them by name**, on screen and on its page (`credits` in
  lesson.js). Nothing is taught from memory.
- **Check the topic, not only the facts.** Before teaching anything as the viewer's job, ask whether the agent now
  does it by itself; if it does, teach the human's part instead.
- **Heavily biased to what is new.** Prefer sources from the last three months, then the last year.

## Legacy lessons (published before 2026-10-12)

The 12 lessons published before the rebuild (00.01–00.06, 01.01–01.06) are **legacy**: kept, published and marked
(`"legacy": true` in course.json, the Legacy table in curriculum.md, "legacy" on the course page). They cover some of
the new slots for now (status `legacy`, which the daily job skips) and will be rebuilt once more new lessons exist and
Aaron's feedback has settled what the course should be. They render exactly as published: their pages load the frozen
six-district map (`engine/legacy/map-v1.js`) and `tests/legacy_freeze/` proves every engine change leaves them
pixel-identical. Never edit a legacy lesson in place; rebuild it as a new lesson under the slot's key.

## The map (the shelf in your head)

Districts (4 to 7), each answering one question, walked in order from Start to Finish. Every lesson pins itself on
this map. Each district is one contiguous run of modules, so the module numbers read in map order. **The map is data
(since 2026-10-12):** curriculum.md's `# Start` / `# District N` / `# Finish` and `## Module` headings are its only
source; `python tools/course.py sync` writes them into engine/course.js, engine/map.js lays the map out from that, and
every new lesson's standard map section (section 02) is generated from it, so restructuring the course is an edit to
curriculum.md plus a few commands, never a hand-drawn change. docs/course-data.md explains the chain and how to add,
delete, split, combine, reorder and rename. The current map is in curriculum.md (`python tools/course.py map` prints
it; `--png` draws it). Never copy it into other files: it changes more than anything else in the course.

**The map opens every lesson, and it is the one section that is regenerated.** Section 02 of every new lesson
(`## 02 — Where this sits on the map [map]`) is written by `course.py sync` from the lesson's position (district,
its question, module; no numbers, no neighbouring titles) and drawn by `K.map.intro` in `scenes/02.js`. When the map
changes, `course.py remap --render` re-narrates only that short section of the lessons it affects and re-renders them.
So no other section may name the district, the module, a lesson number or "the next lesson": refer to other lessons by
what they teach.

The legacy lessons keep the six-district map of 2026-10-01 (Start · The Machine · The Code · The History · The Network ·
Trust · Shipping · Finish), frozen in `engine/legacy/map-v1.js`.

**The Lanterns are AI, and they are not a district** (Aaron, 2026-10-01). They hang over every district: AI shows
up everywhere, so it is taught where it shows up. Lessons whose subject is AI sit in the module they belong to and are
listed by key on curriculum.md's `Lantern lessons:` line; the course page marks them with a lantern. Never call the
Lanterns "the seventh district", and never give AI its own module again. The Finish is a capstone: one worked project
that uses everything. The recurring line: *AI is the lantern: it lights every district, but it doesn't walk the
streets for you.*

## Current, not five years ago (Aaron, 2026-10-02)

Every lesson must be true and relevant **as of the month it is made**. Aaron rejected the first 00.05 (a 5-minute
"tokens, context window, temperature, hallucination" lesson) because it "would have been okay 5 years ago". So:

Aaron, 2026-10-12: *"Heavily bias towards what is new because the state of AI changes every week and what you need to
know changes every week. For example, you had created a lesson about debugging code written by AI. This was a huge
mistake because no one debugs code anymore. AI does that."* A lesson can be current in its facts and out of date in its
topic; check both.

- **AI and security lessons carry the change arc in 2–3 sentences:** before agents (dated), what changed (dated), where
  it stands now, and where it is heading. The pace is weeks, not years. Mark new, beta and speculative things as such.
- **Plan before writing.** The workflow re-reads every source in the lesson's spec (`sources/<S-ID>.md`) and checks
  what changed this month (`research-now.md`, with a "framing check": is any of this now the agent's job?), then a
  planner writes `plan.md`: purpose line, change arc, a must-cover list taken from the spec with a time budget, what is
  only introduced here and which lesson (key) owns it, the metaphor, the real computer actions to record, the credits,
  a cut list, and hedged wording for uncertain claims. The scripts, the judge and four fact-checkers (sources,
  facts, currency, beginner) hold the lesson to that plan.
- **Wide topics: brief overview here, own lesson later.** A lesson may name many things in a sentence or two
  each, as long as each one lands on its shelf. Topics that need more go into curriculum.md as their own lessons.

## The lesson arc (conceptual)

**Length (Aaron, 2026-10-01):** orientation lessons and the first lesson of every module run about 5 minutes
(~500–770 spoken words); lessons in the middle of a module about 10 minutes (~1,200–1,600 words); no lesson over 20
minutes. Since 2026-10-12 a lesson's spec may set `minutes` (dense lessons that fill several small gaps run longer);
the workflow uses it, otherwise the rule above. A longer lesson keeps the same arc and spends the time on more mental
model, mechanism and surprises, never padding. The whole core path is sized for about a month of daily lessons
(30–36 lessons), and everything else waits in curriculum.md's Deep-dive backlog.

**Guest segment (Aaron, 2026-10-01):** a lesson over 15 minutes has ONE guest segment of 5 minutes at most:
consecutive script sections tagged `[guest]`, spoken by the course's fixed third voice (June, `voices/roster.json`
"guest"; never either narrator, never Aaron). The narrator hands over by name and takes back; the guest does a
pace-changing job (myth-busting, a field story, a worked example, a quick-fire recap). The score crossfades
into a livelier groove with a rising swell for the guest and back to the calm bed after (`engine/music.js`), and
the scenes carry a small "guest · June" lower-third. `narrate.py` flags a segment that is too long, broken up, or
in a lesson of 15 minutes or less.

Each `## NN` section of `script.md` is one scene. Typical arc (beats marked * are mandatory):

1. **The point*** — the lesson's very first spoken sentence states its purpose: what you'll learn in this
   lesson ("In this lesson you'll learn ..." or an equally plain "This lesson is about ..."). Nothing comes
   before it: no story, no hook, no question (Aaron's rule, 2026-10-01). Then the conclusion: what it is in
   one plain sentence and why you should care. A viewer who leaves after 20 seconds leaves informed.
   The title card shows the purpose line alongside the one-line conclusion.
2. **Where it lives*** — the standard map section, generated from curriculum.md (see "The map" above): the map
   assembles, the district comes into focus, the pin drops on the module. Never written or animated by hand.
3. **The mental model*** — one metaphor, drawn, that carries the rest of the lesson (a kitchen, a
   post office, a key ring, a library card...). Pick one and stay with it.
4. **What's really going on** — just enough of the true mechanism under the metaphor, and **where
   the metaphor breaks** (say so plainly; that's where understanding lives).
5. **What it connects to** — how this idea hands off to others, naming those lessons by what they teach (never by
   number or district: those move).
6. **The surprises you'll hit*** — "you'll see X, and that's this". Concrete error messages, words,
   files or screens the viewer *will* meet, shown so they're recognised later. This is the anti-confusion
   payload of the whole course. **Show it for real** wherever it helps: a real screen recording, a real
   screenshot animated with a cursor, real terminal output (see Visual rules).
7. **You vs the agent*** — what the agent now does on its own, what the viewer must check or decide, and when to
   bring in an expert (the spec's "You vs the agent" section). Every lesson has it; for security, cost, privacy and
   "ready to ship" it is the heart of the lesson.
8. **Safe to ignore for now** — what beginners worry about but can skip until later.
9. **Keep this*** — three takeaways (bold-lead sentences), on an end card, with a small "Built on" credit line naming
   the sources. They also go in `keep:`; the sources go in `credits:`.

Order sections most-useful-first. No cliffhangers, no "but it turns out...", no withheld payoff.

## Voice (from aaron-brand; hard rules)

- Conclusion first, always. Skimmable by bold: each takeaway's bold lead carries the whole idea.
- Warm call-outs, gentle dark humour, genuinely friendly. The viewer is a guest of the tea house.
  ("Nobody handed you this map. That's not a character flaw; it's a missing semester.")
- Never: hype adjectives, "seamless / leverage / unlock / game-changer", engagement bait, "smash that",
  teasers for the next lesson, self-praise. No emoji.
- Written **for the ear**: short sentences, one idea per sentence, second person. Spell things the way
  they're said ("dot P Y", "V S Code", "sudo" as "soo-doo" only if needed). The screen carries the
  literal form (`.py`, `cd`, `C:\Users\you>`).
- **The narrator is not Aaron.** The narrator alternates between two hired voices, so the script never
  says "I" as Aaron. Tell his stories in the third person and name him: "Aaron, who made this course, wrote
  Python in Notepad..." The narrator may say "we" for the course and "you" for the viewer.
- **Spell for the ear, consistently** (these are what the voices get right):
  `.venv` → "dot V E N V" (never "vee-env": heard as ".env"), `.py` → "dot P Y", `.txt` → "dot T X T",
  `cd` → "C D", `API` → "A P I", `CLI` → "C L I", `MIT` → "M I T", `npm` → "N P M", `JSON` → "Jason",
  `SQL` → "sequel", `GUI` → "gooey", `OAuth` → "oh auth", `2FA` → "two factor". Captions and the
  transcript convert the spoken forms back to the written ones (`narrate.py` caption_words).
- Aaron's own true stories are welcome where they fit: writing Python in Notepad as `.txt`; not knowing
  to rename it `.py`; not knowing to open a terminal and `cd` to the folder; not knowing what `.venv` was;
  having an IT degree and still not knowing; at work, automations tied to his personal accounts that had to move
  to service accounts, Credential Manager, DPAPI and Entra app registrations. Don't invent new anecdotes.
- Honesty: dates and facts must be checkable. If unsure, cut the claim or phrase it as approximate.
  No invented statistics.

## Visual rules

- Tea House night palette via `K.C` (gold headings, terracotta accents, cream text on indigo). Pink
  (`K.C.blossom`) only as decoration on title/end cards, never text.
- **One idea per screen.** Labels ≤ ~8 words. The narration carries sentences; the screen carries
  nouns, literal names and the metaphor.
- Every scene moves in step with its narration: hang beats on `[[cue]]` markers (`S.cue('name')`) or
  spoken words (`S.find('word')`). Nothing important appears before it's mentioned.
- Safe area: keep text within x 80–1840, y 130–930. The badge sits top-left (y < 110). The web captions
  overlay the bottom band, so nothing essential goes below y 930.
- Minimum sizes on the 1920 canvas: 26 px for labels, 30+ px for anything to be read, 20 px only for eyebrows.
- Motion: `K.io` / `K.ease.io` for structure, 0.4–0.8 s moves, at most one overshoot (`'back'`) per scene,
  gentle camera (`K.cam`). Idle motion (bob, sway) is small. No flashing.
- The metaphor object persists and transforms across scenes rather than being redrawn from scratch
  each time; continuity makes the mental model stick.
- Title and end cards may use the painted plate `engine/assets/teahouse-night.jpg` via `K.plate()`.
- Scenes crossfade automatically (0.6 s). Design each scene so its first and last frames are calm.
- **Show real computer actions, not only drawings (Aaron, 2026-10-12).** Viewers should see how a task is really done
  and what it really looks like: browser captures (`tools/capture.py browser`, played with `K.demo`: smoothed cursor,
  click ripples, typed text, an auto-zoom that eases onto each click), real terminal sessions (`capture.py terminal`,
  `K.termReplay`), real screenshots animated as if someone were using them (`K.shot`), and desktop recordings of any
  app when an interactive session is available (`capture.py desktop`). Recipes live in `lessons/<key>/steps/` so a
  capture re-records from the repo. Never real keys, tokens, emails, account names or personal data on screen: public
  pages, throwaway folders and test values only. The narration points only at what the camera has zoomed onto.
  `docs/showing-real-computer-actions.md` has the options and rules.
- **3D shots from Blender (Aaron, 2026-10-12)** when 3D genuinely clarifies an idea (at most one per lesson): a Python
  shot script in `lessons/<key>/blender/` rendered headless by `tools/blender_shot.py` (reserve the GPU with the
  gpu-queue skill first), played with `K.video`. The Blender MCP is for designing a shot interactively; the final shot
  is always the script, so it re-renders. `docs/blender-shots.md`.

## Pipeline (see SKILL for the daily procedure)

```
python tools/course.py next                  # the first `todo` lesson: key, id, module, spec, sources (JSON)
python tools/new_lesson.py <key>             # lessons/<key>/ from curriculum.md: index.html, the standard map
                                             # section 02 (generated narration + scenes/02.js), lesson.js
# write script.md (with [[cues]]; keep section 02 as generated) and lesson.js metadata; storyboard.md optional
python tools/narrate.py <key> --dry-run      # words, minutes, characters; free
python tools/narrate.py <key>                # ElevenLabs; cached per section
python tools/mix.py <key>                    # score ducked under voice → audio/mix.mp3
# scenes/NN.js, one per section: SCENE('NN', (t, S) => {...})
python tools/stills.py <key> --scene 03 --every 1   # look at every frame you care about
python tools/stills.py <key> --every 2 --captions   # whole-lesson contact sheet with captions
python tools/render.py <key>                 # MP4 (4 workers)
python tools/publish.py <key>                # lesson files + its own course data → blog, commit, push, verify live
```

A lesson is named by its permanent **key** (its folder and URL); its ID (`03.02`) is display only and changes when the
course is restructured. After any change to curriculum.md: `python tools/course.py renumber --write`, `check`, `sync`,
`remap --render`, then `python tools/publish.py --all` (docs/course-data.md section 8). Proofs of concept still use the
old form, `python tools/new_lesson.py 99.01 "Title" --module Testing --poc`.

Real footage and 3D: `python tools/capture.py browser|terminal|desktop <key> <name>` (recipes in `lessons/<key>/steps/`),
`python tools/capture.py check <key>`, `python tools/blender_shot.py <key> <shot>`.

ElevenLabs: check the quota before a batch (the daily job does). On 2026-10-12 the plan's limit was 70,449 characters a
month, and a 10-minute lesson bills about 9,000–13,000, so the plan covers roughly six such lessons a month.
Re-rendering costs nothing: narration is cached per section and committed (Git LFS), and only changed text re-bills.

## Narrator (Aaron's rule)

**Only the narrators of 00.01 and 00.02 from now on** (Aaron, 2026-10-01): RClayton (female, American) and
Adrian (male, Canadian), both uncommon professional clones from the ElevenLabs shared Voice Library, listed in
`voices/roster.json`. `tools/voice.py` alternates between them so consecutive lessons sound different
(`--reroll` switches to the other one). Never stock ElevenLabs voices (George, Rachel, Adam...): people hear
them everywhere and they give the AI away. (00.03 was narrated by Ember, picked before this rule.) `narrate.py` transcribes every section afterwards and
re-takes anything garbled. Each lesson page credits its narrator.
