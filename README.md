# The Hidden Curriculum

**A free, narrated video course that fills the small gaps that stop people from building whatever they want with AI.**
Everyone can do almost anything with AI now; what trips people up is the things nobody teaches: where the agent
actually works, what "done" from an agent really means, why an app that works can still let strangers in, which key
may sit in a web page, what runs while you're away. Those gaps move every week, so the course is rebuilt as they move.

**Watch it:** https://aaronorelup.com/courses/the-hidden-curriculum/

Every lesson is a set of files in this repository: its script, its scenes (drawn in code), its narration and the real
screen recordings it shows. Change a file and re-render, and the video changes. Nothing has to be redone by hand.

## Built on other people's hard-won knowledge

The topics don't come from an AI's sense of what needs teaching. They come from 251 dated sources: university
syllabi, practitioner essays, incident reports and breach write-ups, security standards, surveys and studies, tool
documentation and the questions beginners keep asking. Each lesson is built on a few of them and credits them by name.

| file | what it is |
|---|---|
| [`curriculum.md`](curriculum.md) | the course: the map (a Start, districts that each answer one question, a Finish) and every lesson in order, with its key idea, concepts, sources and status |
| [`curriculum/lessons/`](curriculum/lessons/) | one spec per lesson: exactly what it teaches (each point with its sources), you vs the agent, the real computer actions it shows, the questions it answers |
| [`curriculum/concepts.md`](curriculum/concepts.md) | every concept the course teaches, the evidence that people miss it, and the specific points, each citing its sources |
| [`curriculum/sources.md`](curriculum/sources.md) | the sources, with authors, dates and links |
| [`curriculum/research/`](curriculum/research/) | how the curriculum was found: the source sweeps, reading notes, the challenge log, the three competing designs and the decision |

## Help fill the gaps

This is a community project. The most useful thing you can give it is evidence:

- **Something you wish you'd known** before you built with AI, and where it bit you.
- **A question** you keep running into and want a lesson to answer.
- **A source** (a post, talk, report, study or incident write-up) that names what people need to know now.
- **A correction:** a lesson that is wrong, or out of date. Out of date counts even when the facts are right: a
  lesson once taught debugging by hand, when agents now debug their own errors.

[Open an issue](https://github.com/aaronorelup/The-Hidden-Curriculum/issues/new/choose) for any of these. Pull requests
to `curriculum/lessons/*.md` (add a question, a source, a point) are welcome too. See [CONTRIBUTING.md](CONTRIBUTING.md).

## What's in the repo

```
curriculum.md              the course order and the map (tools read it; IDs are display only, keys are permanent)
curriculum/                specs, concepts, sources, research
COURSE.md                  the lesson contract: arc, voice, visual rules, what every lesson must do
lessons/<key>/             one lesson: script.md, storyboard.md, lesson.js, scenes/*.js, cues, audio/NN.mp3
                           (narration, one file per section, in Git LFS), assets/ (captures, clips), steps/, blender/
lessons/00-01-.../         the 12 legacy lessons published before the 2026-10-12 rebuild, kept as they are
engine/                    the drawing kit, the course map, the runtime and the web player
tools/                     course.py, new_lesson.py, narrate.py, mix.py, render.py, stills.py, capture.py,
                           blender_shot.py, publish.py, and lesson-workflow.js (the agents that make a lesson)
docs/                      how the course data, real-computer captures and Blender shots work
tests/legacy_freeze/       proves the legacy lessons still render pixel for pixel
```

## Re-render a lesson

You need Git LFS, Python 3 with Playwright (Chromium) and ffmpeg. Narration is already in the repo, so re-rendering
costs nothing and needs no API key; only text you change is sent to ElevenLabs (that needs a key).

```bash
git lfs install
git clone https://github.com/aaronorelup/The-Hidden-Curriculum.git
cd The-Hidden-Curriculum
pip install playwright && python -m playwright install chromium

python tools/narrate.py 00-02-the-map-of-everything   # rebuilds narration and timings from the committed MP3s
python tools/mix.py 00-02-the-map-of-everything       # the score under the voice
python tools/stills.py 00-02-the-map-of-everything --every 2   # look at frames
python tools/render.py 00-02-the-map-of-everything    # the MP4
```

(Substitute any built lesson's folder name.) To skip downloading the narration: `GIT_LFS_SKIP_SMUDGE=1 git clone ...`.

**Restructuring the course** (combining, splitting, adding, deleting or reordering lessons, renaming districts) is an
edit to `curriculum.md` plus `python tools/course.py renumber --write`, `check` and `sync`. Every lesson opens with
the course map in a generated section, so only that short section is re-narrated and every affected video re-rendered
(`python tools/course.py remap --render`). The whole recipe is in [docs/course-data.md](docs/course-data.md).

## How a lesson is made

A daily job takes the next `todo` lesson from `curriculum.md` and runs [`tools/lesson-workflow.js`](tools/lesson-workflow.js):
agents re-read the lesson's sources, check what changed this month, plan against the spec, write three competing
scripts, judge and merge them, fact-check them four ways, narrate them (ElevenLabs), record the real computer actions
the lesson shows, animate each scene, review the whole lesson twice and render it. Everything it writes lands here.

## License

None chosen yet. Until one is added, the default applies: all rights reserved.
