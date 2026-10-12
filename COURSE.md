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

- **Audience:** people who build with AI but never got the "hidden curriculum". That includes someone with
  an IT degree, like Aaron (Information Systems + Data Science), who still wrote Python in a `.txt` file and didn't know to `cd` into
  the folder first. Smart, motivated, missing context. Never talk down.
- **Title:** *The Hidden Curriculum* (renamed from the working title *The Missing Map* on 2026-10-01; "the map" stays the
  name of the course's six-district device). Do **not** use "for Dummies" anywhere: it is a Wiley trademark.
- **Format:** 5–20 minute narrated animations (see Length below), drawn entirely in code (this engine), 1920×1080, plus
  an interactive web page (transcript, chapters, takeaways) at aaronorelup.com/courses/the-hidden-curriculum/.
- **Proof-of-concept lessons** live under `lessons/poc-*` and are not part of the final course.

## The map (the shelf in your head)

Six districts, each answering one question, walked in order from Start to Finish. Every lesson pins itself on
this map. Each district is one contiguous run of modules, so the module numbers read in map order. The map is
drawn by `K.map.draw()` and must stay consistent across lessons (engine/map.js draws it; curriculum.md's
`# District` headings are the source the site reads; keep the two in step).

| Stop | Question it answers | Modules |
|---|---|---|
| Start: Orientation | what this course is, and the lantern you carry | 00 Orientation (incl. model vs app vs agent, how LLMs work) |
| 1 The Machine | what's on your computer | 01 Your computer · 02 Command line · 03 Dev environments |
| 2 The Code | what programs are made of | 04 Languages · 05 Packages · 06 Data · 07 Concurrency |
| 3 The History | how work is saved & shared | 08 Git & GitHub |
| 4 The Network | how computers talk | 09 Networking · 10 APIs/webhooks/MCP · 11 Websites · 12 Cloudflare · 13 Containers & cloud |
| 5 Trust | who may do what | 14 Identity & keys · 15 Secrets & security · 16 Running without you |
| 6 Shipping | getting it to people | 17 Applications · 18 Other platforms · 19 Payments & users · 20 Licenses |
| Finish: Capstone | one small real project, idea to running | 21 Capstone (uses every district) |

**The Lanterns are AI, and they are not a district** (Aaron, 2026-10-01). They hang over all six districts: AI shows
up everywhere, so it is taught where it shows up. Lessons whose subject is AI sit in the module they belong to (coding
agents in 03 Dev environments, agents on git in 08, MCP in 10, keys for agents in 14, scheduled agents in 16...) and
are listed on curriculum.md's `Lantern lessons:` line; the course page marks them with a lantern. Never call the
Lanterns "the seventh district", and never give AI its own module again. Shipping (district 6) is the concepts of
getting software to people; the Capstone (Finish) is one worked project that uses everything. The recurring line:
*AI is the lantern: it lights every district, but it doesn't walk the streets for you.*

## Current, not five years ago (Aaron, 2026-10-02)

Every lesson must be true and relevant **as of the month it is made**. Aaron rejected the first 00.05 (a 5-minute
"tokens, context window, temperature, hallucination" lesson) because it "would have been okay 5 years ago". So:

- **AI and security lessons always carry the change arc:** what it looked like about five years ago, what changed
  (with dates), what it is now, and where it is heading. Mark new, beta and speculative things as such.
- **Plan before writing.** The workflow researches first (`research-now.md`: the subject this month;
  `research-change.md`: the last five years, with sourced, dated facts) and a planner writes `plan.md`: purpose
  line, change arc, a must-cover list with a time budget, what is only introduced here and which lesson owns it
  (or a new lesson to add to curriculum.md), the metaphor, a cut list, and hedged wording for uncertain claims.
  The scripts, the judge and a "currency" fact-checker all hold the lesson to that plan.
- **Wide topics: brief overview here, own lesson later.** A lesson may name many things in a sentence or two
  each, as long as each one lands on its shelf. Topics that need more go into curriculum.md as their own lessons.

## The lesson arc (conceptual)

**Length (Aaron, 2026-10-01):** orientation lessons (module 00) and the first lesson of every module run about
5 minutes (~500–770 spoken words); lessons in the middle of a module about 10 minutes (~1,200–1,600 words); no lesson
over 20 minutes. A longer lesson keeps the same arc and spends the time on more mental model, mechanism and
surprises, never padding. The workflow sets the target from the lesson id (`minutes` overrides it). 00.03 is an
exception, at 8–11 minutes, because it covers how fast everything changes, and so is 00.05 (about 20 minutes,
Aaron 2026-10-02: the whole current AI landscape in brief, with a guest segment).

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
2. **Where it lives*** — the map, pin dropped on this lesson's module, one sentence on the district's question.
3. **The mental model*** — one metaphor, drawn, that carries the rest of the lesson (a kitchen, a
   post office, a key ring, a library card...). Pick one and stay with it.
4. **What's really going on** — just enough of the true mechanism under the metaphor, and **where
   the metaphor breaks** (say so plainly; that's where understanding lives).
5. **What it connects to** — neighbours on the map; how this idea hands off to others.
6. **The surprises you'll hit*** — "you'll see X, and that's this". Concrete error messages, words,
   files or screens the viewer *will* meet, shown so they're recognised later. This is the anti-confusion
   payload of the whole course.
7. **The lantern: where AI shows up here** — when it really does, one or two sentences on how AI meets this idea
   (V S Code: the chat panel and agents that edit in the editor; git: agents work on branches and open pull requests;
   keys: why an agent should get its own, scoped key). This is how AI is woven through the whole course instead of
   saved for a section of its own. Skip it when it would be forced; lantern lessons (curriculum.md) are about AI anyway.
8. **Safe to ignore for now** — what beginners worry about but can skip until later.
9. **Keep this*** — three takeaways (bold-lead sentences), on an end card. They also go in `keep:`.

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

## Pipeline (see SKILL for the daily procedure)

```
python tools/new_lesson.py 00.02 "The map of everything" --module Orientation
# write script.md (with [[cues]]) and lesson.js metadata; storyboard.md optional
python tools/narrate.py 00.02 --dry-run      # words, minutes, characters; free
python tools/narrate.py 00.02                # ElevenLabs; cached per section
python tools/mix.py 00.02                    # score ducked under voice → audio/mix.mp3
# scenes/NN.js, one per section: SCENE('NN', (t, S) => {...})
python tools/stills.py 00.02 --scene 03 --every 1   # look at every frame you care about
python tools/stills.py 00.02 --every 2 --captions   # whole-lesson contact sheet with captions
python tools/render.py 00.02                 # MP4 (4 workers)
python tools/publish.py <slug>               # lesson files + course data → blog, commit, push, verify live
```

ElevenLabs: Starter tier, 170k characters/month; a lesson is ~3–5k characters. Check before a batch.

## Narrator (Aaron's rule)

**Only the narrators of 00.01 and 00.02 from now on** (Aaron, 2026-10-01): RClayton (female, American) and
Adrian (male, Canadian), both uncommon professional clones from the ElevenLabs shared Voice Library, listed in
`voices/roster.json`. `tools/voice.py` alternates between them so consecutive lessons sound different
(`--reroll` switches to the other one). Never stock ElevenLabs voices (George, Rachel, Adam...): people hear
them everywhere and they give the AI away. (00.03 was narrated by Ember, picked before this rule.) `narrate.py` transcribes every section afterwards and
re-takes anything garbled. Each lesson page credits its narrator.
