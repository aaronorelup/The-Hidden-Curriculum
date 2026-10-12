"""new_lesson.py: scaffold a lesson folder.

usage: python tools/new_lesson.py 00.02 "The map of everything" [--module Orientation] [--poc] [--bare]

Creates lessons/<id-with-dashes>-<slug>/ with index.html (from engine/lesson-template.html),
a script.md skeleton and a lesson.js skeleton. Re-running only refreshes index.html.
"""
import argparse
import datetime
import html
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import ENGINE, LESSONS  # noqa: E402

SCRIPT = """# {id} — {title}
<!-- lead=1.6 gap=0.8 tail=3 -->

> Conceptual lesson, 3-6 minutes, ~450-750 spoken words. Write for the ear:
> spell things the way they are said ("dot P Y", "V S Code"); on-screen text carries the literal form.
> Put [[cue-name]] exactly where an animation beat should land.

## 01 — The point
State the conclusion first. [[hook]]

## 02 — Where it lives on the map
...
"""

LESSON_JS = """/* {id} — {title}
   Scenes are keyed by the ## NN sections of script.md. Each scene gets (t, S):
   t = seconds since its narration section began (negative during the lead-in),
   S.cue('name', fallback) = local time of [[name]] in the script, S.dur = narration length,
   S.out = when the scene hands over. Draw everything from t alone. */
LESSON({{
  id: '{id}',
  title: '{title}',
  short: '{title}',
  module: '{module}',{poc}
  summary: '',
  keep: [
    // ['Bold lead that carries the idea alone.', 'Supporting sentence.'],
  ],
  images: {{}},
  draft: {{ '01': 10, '02': 12 }},
  noBadge: ['01'],
  scenes: {{
    '01': (t, S) => {{
      K.bg();
      K.title('{title}', K.W / 2, 560, {{ align: 'center', size: 96, alpha: K.io(t, 0, 0.8) }});
    }},
    '02': (t, S) => {{
      K.bg();
      K.map.draw(t, {{ t0: 0, pin: '{mod}' }});
    }},
  }},
}});
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('id')
    ap.add_argument('title')
    ap.add_argument('--module', default='')
    ap.add_argument('--summary', default='')
    ap.add_argument('--poc', action='store_true')
    ap.add_argument('--slug')
    ap.add_argument('--bare', action='store_true', help='for the workflow: make drafts/ and scenes/, no skeleton script or lesson.js')
    a = ap.parse_args()
    slug = a.slug or (a.id.replace('.', '-') + '-' + re.sub(r'[^a-z0-9]+', '-', a.title.lower()).strip('-'))
    if a.poc and not slug.startswith('poc-'):
        slug = 'poc-' + slug
    d = LESSONS / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / 'assets').mkdir(exist_ok=True)
    page = (ENGINE / 'lesson-template.html').read_text(encoding='utf-8')
    page = (page.replace('{{ID}}', html.escape(a.id)).replace('{{TITLE}}', html.escape(a.title))
                .replace('{{SUMMARY}}', html.escape(a.summary)).replace('{{DATE}}', datetime.date.today().isoformat())
                .replace('{{PREV}}', '').replace('{{NEXT}}', ''))
    (d / 'index.html').write_text(page, encoding='utf-8')
    if a.bare:
        (d / 'drafts').mkdir(exist_ok=True)
        (d / 'scenes').mkdir(exist_ok=True)
    if a.bare or (d / 'drafts').exists() or (d / 'scenes').exists() and any((d / 'scenes').iterdir()):
        print(d)  # lesson already in production: only the page was refreshed
        return
    if not (d / 'script.md').exists():
        (d / 'script.md').write_text(SCRIPT.format(id=a.id, title=a.title), encoding='utf-8')
    if not (d / 'lesson.js').exists():
        (d / 'lesson.js').write_text(LESSON_JS.format(id=a.id, title=a.title.replace("'", "\\'"), module=a.module,
                                                       poc="\n  poc: true," if a.poc else '', mod=a.id.split('.')[0]), encoding='utf-8')
    print(d)


if __name__ == '__main__':
    main()
