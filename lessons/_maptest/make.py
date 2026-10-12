"""lessons/_maptest: the course map's test lesson. NEVER published (its folder starts with '_').

Rebuilds, with no narration and no API calls:
  fixtures/<name>/course.js   the course data of each fixture curriculum (old = a copy of curriculum.md as of
                              2026-10-12; d4 / d5 / d7 = new-format curricula with 4, 5 and 7 districts, d7 with
                              long module names), written by tools/course.py sync --course-js
  cues.js / cues.json         a synthetic timeline: one section per scene; intro sections get the [map] narration
                              tools/course.py would generate for that lesson, timed at ~2.6 words a second, so
                              S.cue('district') / S.cue('module') and S.find() behave as in a narrated lesson
  plan.js                     window.MAPTEST_PLAN: what each scene draws (lesson.js turns it into scenes)

usage: python lessons/_maptest/make.py            then: python tools/stills.py _maptest --every 2
       python tools/course.py check --curriculum lessons/_maptest/fixtures/d7/curriculum.md   (and d4, d5, old)
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import course  # noqa: E402

FIX = ['old', 'd4', 'd5', 'd7']
# n, fixture, kind, lesson key (intro) or draw options, title on the you-are-here card (None = curriculum title)
PLAN = [
    ('01', 'old', 'draw', {'t0': 0, 'pin': '01', 'focus': 'machine'}),
    ('02', 'old', 'intro', 'environment-variables-path'),
    ('03', 'old', 'intro', 'model-vs-app-vs-agent'),
    ('04', 'old', 'intro', 'ship-it'),
    ('05', 'old', 'compat', None),
    ('06', 'old', 'intro', 'lockfiles-semantic-versioning'),
    ('07', 'd4', 'draw', {'t0': 0, 'pin': 'Local AI Models', 'focus': 'Local AI Models'}),
    ('08', 'd4', 'intro', 'api-keys'),
    ('09', 'd4', 'intro', 'idea-to-plan'),
    ('10', 'd5', 'draw', {'t0': 0, 'pin': 'trust', 'focus': 'trust'}),
    ('11', 'd5', 'intro', 'what-an-api-is'),
    ('12', 'd5', 'intro', 'trust-what-you-can-verify'),
    ('13', 'd5', 'intro', 'how-online-payments-work'),
    ('14', 'd7', 'draw', {'t0': 0, 'pin': '19', 'focus': 'automation', 'highlight': {'trust': 1}}),
    ('15', 'd7', 'intro', 'local-models-and-vram'),
    ('16', 'd7', 'intro', 'what-a-container-is'),
    ('17', 'd7', 'intro', 'always-on-agents'),
    ('18', 'd7', 'intro', 'build-with-an-agent'),
    ('19', 'd7', 'intro', 'the-hidden-curriculum'),
    ('20', 'old', 'intro-long', 'folders-paths-the-working-directory'),
    # a wide district at the right end of its row: the card sits inside the district, right of its labels
    ('21', 'd4', 'intro', 'virtual-environments'),
    ('22', 'd5', 'intro', 'api-keys'),
]
WPS = 2.6
LEAD, GAP, TAIL = 1.2, 0.8, 2.0


def main():
    courses = {}
    for f in FIX:
        cur = HERE / 'fixtures' / f / 'curriculum.md'
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'course.py'), 'sync', '--curriculum', str(cur),
                        '--course-js', str(HERE / 'fixtures' / f / 'course.js'), '--lessons', str(HERE / 'fixtures' / f / 'lessons')],
                       check=True, capture_output=True)
        courses[f] = course.load(cur, lessons_dir=HERE / 'fixtures' / f / 'lessons')
    t, sections, plan = LEAD, [], []
    for n, fx, kind, arg in PLAN:
        c = courses[fx]
        entry = {'n': n, 'fixture': fx, 'kind': kind}
        if kind.startswith('intro'):
            les = c.lesson(arg)
            assert les, (fx, arg)
            text, pairs = course.map_narration(c, les)
            entry.update({'lesson': arg, 'text': text})
            if kind == 'intro-long':
                entry['title'] = 'Folders, paths and the working directory, the long way round'
            words, cues, k = [], {}, 0.0
            for tok in text.split():
                m = re.match(r'^\[\[([\w-]+)\]\](.*)$', tok)
                if m:
                    cues[m.group(1)] = round(t + k, 3)
                    tok = m.group(2)
                if not tok:
                    continue
                dw = 0.18 + 0.045 * len(tok)
                words.append([tok, round(t + k, 3), round(t + k + dw, 3)])
                k += 1 / WPS + (0.25 if tok.endswith(('.', ':')) else 0.1 if tok.endswith(',') else 0)
            dur = k + 0.4
            title = 'Where this sits on the map'
        else:
            words, cues, dur = [], {}, 9.0
            entry['draw'] = arg
            title = {'draw': 'K.map.draw', 'compat': 'v1 options'}[kind]
        sections.append({'n': n, 'title': f'{title} ({fx})', 'start': round(t, 3), 'end': round(t + dur, 3), 'audio_dur': round(dur, 3),
                         'cues': cues, 'words': words, **({'map': True} if kind.startswith('intro') else {})})
        plan.append(entry)
        t += dur + GAP
    total = round(t - GAP + TAIL, 3)
    cues = {'lesson': '_maptest', 'voice': None, 'lead': LEAD, 'gap': GAP, 'tail': TAIL, 'duration': total, 'sections': sections, 'captions': []}
    (HERE / 'cues.json').write_text(json.dumps(cues, indent=1), encoding='utf-8', newline='\n')
    (HERE / 'cues.js').write_text('window.CUES = ' + json.dumps(cues) + ';\n', encoding='utf-8', newline='\n')
    (HERE / 'plan.js').write_text('// generated by lessons/_maptest/make.py\nwindow.MAPTEST_PLAN = ' + json.dumps(plan, indent=1) + ';\n',
                                  encoding='utf-8', newline='\n')
    for s in sections:
        print(f"{s['n']} {s['start']:7.2f}-{s['end']:7.2f} {s['title']} cues {s['cues']}")
    print(f'duration {total} s')


if __name__ == '__main__':
    main()
