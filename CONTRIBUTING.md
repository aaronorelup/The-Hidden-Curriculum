# Contributing

**The course is only as good as its evidence, and you are evidence.** You don't need to know the right words: the
whole point is that nobody taught them.

## The easiest ways to help

Open an issue from the [templates](https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose):

- **Something I wish I'd known:** the gap, where it bit you, how recent it is and which tools you used.
- **A question I want answered.**
- **A source the course should be built on:** a link, its date, and what it teaches that the course lacks.
- **Something in a lesson is wrong or out of date.**

Each one is read against `curriculum/concepts.md`: it strengthens a concept, adds a point to a lesson spec, or becomes
a new concept, and the curriculum is rebuilt as the gaps move.

## Editing the curriculum directly

- **A lesson's spec** (`curriculum/lessons/<key>.md`) is plain Markdown. Add a question under "Questions this lesson
  answers", a point under a concept (with its source ID), or a source. Every point needs a source with a date.
- **A new source** goes into `curriculum/sources.md` with the next free `S` number, its author, date, URL, kind and
  what it contributes.
- **The order and the map** live in `curriculum.md`. Never type lesson IDs by hand: edit the rows, then run
  `python tools/course.py renumber --write` and `python tools/course.py check` (see `docs/course-data.md`).

## What the course will and won't teach

- **Mental models, not click-by-click tutorials.** What it is, where it lives, what it connects to, what will surprise
  you (see `COURSE.md`).
- **The human's part, not the agent's.** Agents write, run and debug code now. A lesson teaches what the agent can't
  verify for you, and when to bring in an expert, above all for security.
- **Current as of the month it's made.** Old facts and old framings are both bugs.
- **Built on sources, credited by name.** Nothing taught from memory.

## Lesson files

A lesson's folder holds its script (`script.md`, one `## NN` section per scene), its scenes (`scenes/NN.js`, pure
functions of time drawn with `engine/kit.js`), its narration (`audio/NN.mp3`, Git LFS) and its real-computer captures.
Section 02 of every new lesson is generated from `curriculum.md`: don't edit it by hand.

Real screen recordings must never show real keys, tokens, email addresses, account names or personal data. Use public
pages, throwaway folders and test values (`tools/capture.py` refuses many of these on its own).

Legacy lessons (`lessons/00-01-...` to `lessons/01-06-...`) are frozen: they render exactly as published, and
`tests/legacy_freeze/` checks that every engine change keeps them that way.
