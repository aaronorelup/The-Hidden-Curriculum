"""voice.py: give a lesson its narrator from the ElevenLabs shared Voice Library.

Aaron's rule: no stock voices (George, Rachel... everyone has heard them, and they give the AI away).
Since 2026-10-01 (from lesson 00.04 on): ONLY the narrators of 00.01 and 00.02, listed in
voices/roster.json, alternating so consecutive lessons sound different; --reroll switches to the other
roster voice. The library search below runs only if roster.json is missing (lessons 00.01-00.03 used it).
Guest speaker (lessons over 15 minutes, script sections tagged [guest], at most 5 minutes): ONE fixed third
voice, never either narrator, stored as "guest" in voices/roster.json. The first call to guest_voice() (or
`python tools/voice.py --guest`) auditions library voices the same way, preferring an accent neither narrator has.

usage:
  python tools/voice.py <lesson>            pick (or show) this lesson's voice → <lesson>/voice.json
  python tools/voice.py <lesson> --reroll   discard the current pick and choose another
  python tools/voice.py --used              list every voice the course has used
  python tools/voice.py --guest [--reroll]  show (or replace) the guest voice for lessons over 15 minutes

How a voice is chosen:
1. Candidates: English professional voice clones (trained on long recordings, so they hold up over
   minutes of narration), use case educational/narrative/conversational, cloned by 150–4,000 users
   (uncommon, but used enough to have survived), standard rate, no novelty styles (ASMR, whisper,
   character, trailer...), never used by an earlier lesson.
2. Order: a hash of lesson id + voice id, so the pick is stable for a lesson but varies between lessons;
   prefers the opposite gender to the previous lesson so consecutive lessons sound different.
3. Gate 1 (free): the voice's preview audio must be clean (no clipping, sensible loudness, low noise floor).
4. Gate 2 (~300 characters): it reads a test passage (technical words, a list, a question); ElevenLabs
   speech-to-text transcribes it. It fails on any filler (uh, um), a repeated word, a mid-phrase stall
   over 0.42 s (from the TTS timing), word error over 6%, or a pace outside 2.0-3.4 words per second.
   Voices rerolled away from, or blocked by hand (--block), land in voices/blocked.json for good.
The library listing is cached in voices/cache/library.json for 14 days.
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import ROOT, ffmpeg, ffprobe_duration, lesson_dir  # noqa: E402

CACHE = ROOT / 'voices' / 'cache' / 'library.json'
USED = ROOT / 'voices' / 'used.json'
ROSTER = ROOT / 'voices' / 'roster.json'
API = 'https://api.elevenlabs.io/v1'
# long enough (and varied enough: a list, a question, spelled letters) to expose a voice's habits;
# the first course voice passed a one-sentence test and then said "uh" all through the lesson
TEST_LINE = ('Open a terminal, change into the project folder, and run python app dot P Y. '
             'Your A P I key lives in an environment variable, not in the code. '
             'So where does the dot V E N V folder come from? Python makes it, the first time you ask for one, '
             'and every package you install for this project goes inside it.')
TEST_EXPECT = TEST_LINE
FILLERS = re.compile(r"\b(uh+|um+|erm|er|ah+|hmm+|mm+)\b", re.I)
BLOCKED = ROOT / 'voices' / 'blocked.json'
BANNED = re.compile(r'asmr|whisper|character|villain|trailer|announcer|sexy|seductive|sultry|meditat|sleep|horror|kid|child|cartoon|robot|radio|podcast host|hype|game|anime|pirate|santa|elf|monster|demon|creepy|news', re.I)
OK_DESCRIPTIVE = {'calm', 'warm', 'professional', 'confident', 'casual', 'crisp', 'mature', 'classy', 'chill', 'formal', 'upbeat', 'relaxed', 'neutral', 'soft', 'deep', 'clear', 'pleasant', 'smooth', 'friendly', 'wise', 'engaging', 'natural', 'husky', 'gentle'}


def key():
    import os
    k = os.environ.get('ELEVENLABS_API_KEY')
    if not k:
        f = pathlib.Path.home() / '.claude' / 'secrets' / 'elevenlabs.key'
        k = f.read_text(encoding='utf-8').strip() if f.exists() else None
    if not k:
        raise SystemExit('No ElevenLabs key (ELEVENLABS_API_KEY or ~/.claude/secrets/elevenlabs.key).')
    return k


def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'xi-api-key': key()}), timeout=60))


def library():
    if CACHE.exists():
        d = json.loads(CACHE.read_text(encoding='utf-8'))
        if time.time() - d.get('fetched', 0) < 14 * 86400:
            return d['voices']
    found = {}
    for uc in ['informative_educational', 'narrative_story', 'conversational']:
        page = 0
        while page <= 60:
            q = urllib.parse.urlencode({'page_size': 100, 'language': 'en', 'use_cases': uc, 'page': page})
            d = get(f'{API}/shared-voices?{q}')
            for v in d['voices']:
                found[v['voice_id']] = v
            page += 1
            if not d.get('has_more'):
                break
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps({'fetched': time.time(), 'voices': list(found.values())}), encoding='utf-8')
    return list(found.values())


def used():
    return json.loads(USED.read_text(encoding='utf-8')) if USED.exists() else {'voices': []}


def blocked():
    return json.loads(BLOCKED.read_text(encoding='utf-8')) if BLOCKED.exists() else {'voices': []}


def block(voice_id, name, reason):
    b = blocked()
    if not any(x['voice_id'] == voice_id for x in b['voices']):
        b['voices'].append({'voice_id': voice_id, 'name': name, 'reason': reason, 'date': time.strftime('%Y-%m-%d')})
        BLOCKED.parent.mkdir(parents=True, exist_ok=True)
        BLOCKED.write_text(json.dumps(b, indent=1), encoding='utf-8')


def candidates(lesson_id):
    taken = {u['voice_id'] for u in used()['voices']} | {x['voice_id'] for x in blocked()['voices']}
    out = []
    for v in library():
        n = v.get('cloned_by_count') or 0
        text = ' '.join(str(v.get(k) or '') for k in ('name', 'description', 'descriptive', 'use_case'))
        if (v.get('category') == 'professional' and v.get('language') == 'en' and 150 <= n <= 4000
                and (v.get('rate') in (None, 1, 1.0)) and v['voice_id'] not in taken
                and v.get('use_case') in ('informative_educational', 'narrative_story', 'conversational')
                and (v.get('descriptive') or 'clear') in OK_DESCRIPTIVE and not BANNED.search(text)
                and v.get('description') and v.get('preview_url')):
            out.append(v)
    last = used()['voices'][-1] if used()['voices'] else None
    def order(v):
        h = hashlib.sha1(f"{lesson_id}:{v['voice_id']}".encode()).hexdigest()
        same_gender = 1 if last and v.get('gender') == last.get('gender') else 0
        return (same_gender, h)
    return sorted(out, key=order)


def audio_stats(path):
    r = subprocess.run([ffmpeg(), '-hide_banner', '-i', str(path), '-af', 'volumedetect,astats=metadata=0', '-f', 'null', '-'],
                       capture_output=True, text=True)
    s = r.stderr
    num = lambda pat: float(re.search(pat, s).group(1)) if re.search(pat, s) else None
    return {'mean': num(r'mean_volume: ([-\d.]+) dB'), 'max': num(r'max_volume: ([-\d.]+) dB'),
            'noise': num(r'Noise floor dB: ([-\d.inf]+)'), 'dur': ffprobe_duration(path)}


def tts(voice_id, text):
    """returns (mp3 bytes, ElevenLabs character alignment)"""
    import base64
    body = {'text': text, 'model_id': 'eleven_multilingual_v2',
            'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.12, 'use_speaker_boost': True}}
    req = urllib.request.Request(f'{API}/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128', data=json.dumps(body).encode(),
                                 headers={'xi-api-key': key(), 'Content-Type': 'application/json'}, method='POST')
    r = json.load(urllib.request.urlopen(req, timeout=120))
    return base64.b64decode(r['audio_base64']), r.get('alignment') or {}


def stalls(align, limit=0.42):
    """mid-phrase silences: gaps between words longer than `limit` s where no punctuation asks for a pause"""
    ch = align.get('characters') or []
    st, en = align.get('character_start_times_seconds') or [], align.get('character_end_times_seconds') or []
    out, prev_end, prev_char = [], None, ''
    for i, c in enumerate(ch):
        if c.isspace():
            continue
        if prev_end is not None and i > 0 and ch[i - 1].isspace() and prev_char not in ',.;:?!—-' and st[i] - prev_end > limit:
            out.append(round(st[i] - prev_end, 2))
        prev_end, prev_char = en[i], c
    return out


def transcribe(mp3_bytes):
    bnd = uuid.uuid4().hex
    parts = [f'--{bnd}\r\nContent-Disposition: form-data; name="model_id"\r\n\r\nscribe_v1\r\n'.encode(),
             f'--{bnd}\r\nContent-Disposition: form-data; name="language_code"\r\n\r\neng\r\n'.encode(),
             f'--{bnd}\r\nContent-Disposition: form-data; name="tag_audio_events"\r\n\r\nfalse\r\n'.encode(),
             f'--{bnd}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode() + mp3_bytes + b'\r\n',
             f'--{bnd}--\r\n'.encode()]
    req = urllib.request.Request(f'{API}/speech-to-text', data=b''.join(parts),
                                 headers={'xi-api-key': key(), 'Content-Type': f'multipart/form-data; boundary={bnd}'}, method='POST')
    return json.load(urllib.request.urlopen(req, timeout=300))


NUMWORDS = set('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen '
               'eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million and oh'.split())


def norm_words(s):
    """lowercase words; spelled-out letters joined; any run of numbers (digits or words) becomes one '#',
    so "two thousand five" and "2005" compare equal"""
    s = s.lower().replace('’', "'").replace('‘', "'").replace('a.p.i.', 'api').replace('.py', ' py')
    s = re.sub(r'\b([a-z]) (?=[a-z]\b)', r'\1', s)          # "a p i" -> "api", "p y" -> "py"
    s = s.replace('dot py', 'py')
    out = []
    for w in re.findall(r"[a-z0-9']+", s):
        isnum = w.isdigit() or w in NUMWORDS
        if isnum and out and out[-1] == '#':
            continue
        out.append('#' if isnum else w)
    return out


def wer(ref, hyp):
    r, h = norm_words(ref), norm_words(hyp)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            cur = min(d[j] + 1, d[j - 1] + 1, prev + (r[i - 1] != h[j - 1]))
            prev, d[j] = d[j], cur
    return d[len(h)] / max(1, len(r))


def audition(v, tmp):
    """returns (ok, notes)"""
    try:
        prev = tmp / f"{v['voice_id']}-preview.mp3"
        prev.write_bytes(urllib.request.urlopen(v['preview_url'], timeout=60).read())
        st = audio_stats(prev)
    except Exception as e:  # noqa: BLE001
        return False, f'preview unavailable ({e})'
    if st['dur'] < 3 or (st['max'] is not None and st['max'] >= -0.05) or (st['mean'] is not None and not -30 <= st['mean'] <= -12):
        return False, f"preview fails: {st}"
    if st['noise'] is not None and st['noise'] > -48:
        return False, f"noisy preview: {st}"
    try:
        mp3, align = tts(v['voice_id'], TEST_LINE)
    except urllib.error.HTTPError as e:
        return False, f'tts {e.code}'
    p = tmp / f"{v['voice_id']}-test.mp3"
    p.write_bytes(mp3)
    heard = transcribe(mp3).get('text', '')
    err = wer(TEST_EXPECT, heard)
    wps = len(norm_words(TEST_EXPECT)) / max(0.1, ffprobe_duration(p))
    fill = FILLERS.findall(heard)
    hn = norm_words(heard)
    repeats = [a for a, b in zip(hn, hn[1:]) if a == b and a != '#']
    gaps = stalls(align)
    if fill or repeats:
        return False, f"hesitates ({', '.join(fill + repeats)}): {heard!r}"
    if gaps:
        return False, f'stalls mid-phrase ({gaps} s)'
    if err > 0.06:
        return False, f"word error {err:.0%}: {heard!r}"
    if not 2.0 <= wps <= 3.4:
        return False, f'pace {wps:.2f} words/s'
    return True, f"wer {err:.0%}, {wps:.2f} words/s, no fillers or stalls, preview mean {st['mean']} dB, noise floor {st['noise']} dB"


def roster():
    return json.loads(ROSTER.read_text(encoding='utf-8'))['voices'] if ROSTER.exists() else []


def save_choice(L, choice):
    (L / 'voice.json').write_text(json.dumps(choice, indent=1), encoding='utf-8')
    u = used()
    u['voices'] = [x for x in u['voices'] if x.get('lesson') != L.name] + [{k: choice[k] for k in ('voice_id', 'name', 'gender', 'accent', 'lesson', 'chosen')}]
    USED.parent.mkdir(parents=True, exist_ok=True)
    USED.write_text(json.dumps(u, indent=1), encoding='utf-8')
    return choice


def pick_roster(L, voices, reroll_from=None):
    """alternate through the roster: the voice after the one the most recent other lesson used"""
    ids = [v['voice_id'] for v in voices]
    prior = [x['voice_id'] for x in used()['voices'] if x.get('lesson') != L.name and x['voice_id'] in ids]
    i = (ids.index(prior[-1]) + 1) % len(ids) if prior else 0
    if reroll_from in ids and ids[i] == reroll_from:
        i = (i + 1) % len(ids)
    choice = dict(voices[i])
    choice.update({'lesson': L.name, 'chosen': time.strftime('%Y-%m-%d'), 'audition': f"course roster (voices/roster.json), first used on {choice.pop('first_lesson', '?')}"})
    return save_choice(L, choice)


def guest_voice(reroll=False):
    """the course's fixed third voice for guest segments; auditioned and saved to roster.json on first use"""
    r = json.loads(ROSTER.read_text(encoding='utf-8')) if ROSTER.exists() else {'voices': []}
    if r.get('guest') and reroll:
        block(r['guest']['voice_id'], r['guest'].get('name', ''), 'guest voice rerolled away from')
        r.pop('guest')
    if r.get('guest'):
        return r['guest']
    narr = {v['voice_id'] for v in r['voices']}
    accents = {(v.get('accent') or '').lower() for v in r['voices']}
    cands = [v for v in candidates('guest') if v['voice_id'] not in narr]
    cands.sort(key=lambda v: (1 if (v.get('accent') or '').lower() in accents else 0))
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='voice-guest-'))
    tried = []
    for v in cands[:14]:
        ok, notes = audition(v, tmp)
        tried.append(f"{v['name']}: {'OK' if ok else 'rejected'} ({notes})")
        print(tried[-1], flush=True)
        if ok:
            g = {k: v.get(k) for k in ('voice_id', 'public_owner_id', 'name', 'description', 'accent', 'gender', 'age', 'descriptive', 'use_case', 'cloned_by_count')}
            g.update({'chosen': time.strftime('%Y-%m-%d'), 'audition': notes, 'tried': tried})
            r['guest'] = g
            ROSTER.write_text(json.dumps(r, indent=1), encoding='utf-8')
            return g
    raise SystemExit('no guest voice passed the audition:' + chr(10) + chr(10).join(tried))


def pick(L: pathlib.Path, reroll=False):
    vf = L / 'voice.json'
    if vf.exists() and not reroll:
        return json.loads(vf.read_text(encoding='utf-8'))
    if roster():
        old = json.loads(vf.read_text(encoding='utf-8'))['voice_id'] if reroll and vf.exists() else None
        return pick_roster(L, roster(), old)
    lesson_id = L.name
    reject = set()
    if reroll and vf.exists():
        old = json.loads(vf.read_text(encoding='utf-8'))
        reject.add(old['voice_id'])
        # a voice rerolled away from is never offered again (a reroll means it failed a real lesson)
        block(old['voice_id'], old.get('name', ''), f'rerolled away from on {L.name}')
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='voice-'))
    tried = []
    for v in candidates(lesson_id)[:14]:
        if v['voice_id'] in reject:
            continue
        ok, notes = audition(v, tmp)
        tried.append(f"{v['name']}: {'OK' if ok else 'rejected'} ({notes})")
        print(tried[-1], flush=True)
        if ok:
            choice = {k: v.get(k) for k in ('voice_id', 'public_owner_id', 'name', 'description', 'accent', 'gender', 'age', 'descriptive', 'use_case', 'cloned_by_count', 'usage_character_count_1y')}
            choice.update({'lesson': L.name, 'chosen': time.strftime('%Y-%m-%d'), 'audition': notes, 'tried': tried})
            return save_choice(L, choice)
    raise SystemExit('no voice passed the audition:\n' + '\n'.join(tried))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lesson', nargs='?')
    ap.add_argument('--reroll', action='store_true')
    ap.add_argument('--used', action='store_true')
    ap.add_argument('--guest', action='store_true', help="show (or choose, on first use) the course's guest voice")
    ap.add_argument('--block', nargs=2, metavar=('VOICE_ID', 'REASON'), help='never offer this voice again')
    a = ap.parse_args()
    if a.block:
        block(a.block[0], '', a.block[1])
        print('blocked', a.block[0])
        return
    if a.guest:
        g = guest_voice(a.reroll)
        print(f"guest voice: {g['name']} ({g.get('gender')}, {g.get('accent')}); {g.get('audition')}")
        return
    if a.used or not a.lesson:
        for u in used()['voices']:
            print(f"{u['lesson']:<45} {u['name']} ({u.get('gender')}, {u.get('accent')})")
        return
    c = pick(lesson_dir(a.lesson), a.reroll)
    print(f"voice for {a.lesson}: {c['name']} — {c.get('gender')}, {c.get('age')}, {c.get('accent')}; cloned by {c.get('cloned_by_count')} users\n  {c.get('description')}\n  {c.get('audition')}")


if __name__ == '__main__':
    main()
