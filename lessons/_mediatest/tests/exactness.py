"""Is every video frame the renderer draws the right frame, and the same frame every time?

usage: python lessons/_mediatest/tests/exactness.py

1. Pixels. Scene 02 draws clip2 at native size (960x540 at 480,270, no rounding) at media time (T - 13.2) + 0.25.
   For every clip frame n that scene shows alone (13..239), render lesson time T = 12.95 + (n + 0.5) / 24 through
   the renderer contract (window.__png, which seeks the clip and waits), in a shuffled order, crop the clip and
   compare it with ffmpeg's own decode of frame n and its neighbours (BT.601, as the clip is encoded; see
   tools/media_util.py). Right frame = closer to n than to n - 1 and n + 1, and the closest of all 240.
2. Determinism. The same frames again in sorted order in a fresh browser: every PNG must hash the same.
3. Seek targets everywhere else (cover + moving camera, 2x loop, the clip with sound): after window.__frame(T),
   each wanted clip's currentTime must be exactly the centre of the frame the scene formula asks for.
Writes out/tests/exactness.json.
"""
import base64
import hashlib
import io
import json
import math
import pathlib
import random
import subprocess
import sys

import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
L = HERE.parent
ROOT = L.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
from common import Server, open_lesson  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

CLIP = L / 'assets' / 'video' / 'clip.mp4'
W, H, FPS = 960, 540, 24
OUT = L / 'out' / 'tests'

SEEKS_JS = """async (T) => { await window.__frame(T, 0.5); const o = {};
  K.want.forEach((w, v) => { o[w.name] = { cur: v.currentTime, t: w.t }; }); return o; }"""


def decode(matrix='bt601', chroma='bilinear'):
    flags = {'bilinear': 'bilinear+accurate_rnd+full_chroma_int+full_chroma_inp', 'point': 'neighbor+accurate_rnd'}[chroma]
    vf = f'scale={W}:{H}:in_color_matrix={matrix}:in_range=limited:out_range=full:flags={flags},format=rgb24'
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(CLIP), '-vf', vf, '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(np.int16)


def expected_seeks(T, L_clip):
    """what lesson.js asks for at lesson time T: {clip name: frame-centre time}, scenes drawn alone only"""
    def centre(m, loop=False):
        frames = round(L_clip * FPS)
        if loop:
            m = math.fmod(math.fmod(m, L_clip) + L_clip, L_clip)
        n = min(max(math.floor(m * FPS + 1e-6), 0), frames - 1)
        return (n + 0.5) / FPS
    if 0.6 <= T < 12.8:
        return {'clip': centre(T - 2.7)}
    if 13.5 <= T < 24.8:
        return {'clip2': centre(T - 12.95)}
    if 35.9 <= T < 45.6:
        return {'clip': centre(2 * (T - 35.6), loop=True)}
    if 46.4 <= T < 57.0:
        return {'clip2': centre(T - 47.0)}
    return None


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    refs = {'601 bilinear': decode('bt601', 'bilinear'), '601 point': decode('bt601', 'point')}
    first = refs['601 bilinear']
    N = first.shape[0]
    assert N == 240, first.shape
    ns = list(range(13, N))
    order = ns[:]
    random.Random(1012).shuffle(order)
    srv = Server()
    url = srv.url(L)
    crops, hashes_a, hashes_b = {}, {}, {}
    with sync_playwright() as p:
        b, page, errs = open_lesson(p, url)
        for n in order:
            T = 12.95 + (n + 0.5) / FPS
            png = base64.b64decode(page.evaluate('t => window.__png(t)', T).split(',', 1)[1])
            hashes_a[n] = hashlib.sha256(png).hexdigest()
            crops[n] = np.asarray(Image.open(io.BytesIO(png)).convert('RGB'), np.int16)[270:270 + H, 480:480 + W]
        L_clip = page.evaluate("K.videoDur('clip')")
        # 3. seek targets in the other scenes: every 0.1 s of each scene drawn alone
        seek_rows, seek_bad = [], 0
        for k in range(0, 578):
            T = round(k * 0.1, 3)
            exp = expected_seeks(T, L_clip)
            if exp is None:
                continue
            got = page.evaluate(SEEKS_JS, T)
            ok = set(got) == set(exp) and all(abs(got[nm]['cur'] - exp[nm]) < 1e-4 for nm in exp)   # Chromium: whole microseconds
            seek_bad += not ok
            seek_rows.append({'T': T, 'expected': exp, 'got': got, 'ok': ok})
        b.close()
        b, page, errs2 = open_lesson(p, url)
        for n in ns:
            T = 12.95 + (n + 0.5) / FPS
            hashes_b[n] = hashlib.sha256(base64.b64decode(page.evaluate('t => window.__png(t)', T).split(',', 1)[1])).hexdigest()
        b.close()
    srv.close()

    rows, right = [], 0
    small = {k: v[:, ::4, ::4].astype(np.float32) for k, v in refs.items()}   # the search over all 240 frames, at 1/4 size
    for n in ns:
        c = crops[n]
        row = {'n': n}
        for name, fr in refs.items():
            mad = {k: float(np.abs(fr[k] - c).mean()) for k in (n - 1, n, n + 1) if 0 <= k < N}
            closest = int(np.abs(small[name] - c[None, ::4, ::4]).mean(axis=(1, 2, 3)).argmin())
            d = np.abs(c - fr[n]).max(axis=2)
            row[name] = {'mad_n': round(mad[n], 3), 'mad_prev': round(mad[n - 1], 3),
                         'mad_next': round(mad[n + 1], 3) if n + 1 < N else None, 'argmin': closest,
                         'pct_exact': round(float((d == 0).mean() * 100), 2), 'pct_within2': round(float((d <= 2).mean() * 100), 2),
                         'max': int(d.max())}
        best = min(refs, key=lambda k: row[k]['mad_n'])
        r = row[best]
        row['best_reference'] = best
        row['right_frame'] = r['argmin'] == n and r['mad_n'] < r['mad_prev'] and (r['mad_next'] is None or r['mad_n'] < r['mad_next'])
        right += row['right_frame']
        rows.append(row)
    same = sum(hashes_a[n] == hashes_b[n] for n in ns)
    best = {k: {'mean_mad': round(float(np.mean([r[k]['mad_n'] for r in rows])), 3),
                'mean_pct_exact': round(float(np.mean([r[k]['pct_exact'] for r in rows])), 2),
                'mean_pct_within2': round(float(np.mean([r[k]['pct_within2'] for r in rows])), 2),
                'worst_max': max(r[k]['max'] for r in rows),
                'mean_gap_to_neighbour': round(float(np.mean([min(r[k]['mad_prev'], r[k]['mad_next'] or 1e9) - r[k]['mad_n'] for r in rows])), 3)}
            for k in refs}
    summary = {'frames_checked': len(ns), 'right_frame': right, 'png_hash_same_shuffled_vs_sorted': same,
               'references': best, 'seek_checks': len(seek_rows), 'seek_wrong': seek_bad,
               'page_errors': list(dict.fromkeys(errs + errs2))}
    (OUT / 'exactness.json').write_text(json.dumps({'summary': summary, 'order_rendered': order, 'rows': rows, 'seeks': seek_rows}, indent=1), encoding='utf-8')
    print(json.dumps(summary, indent=1))
    ok = right == len(ns) and same == len(ns) and seek_bad == 0
    print('PASS' if ok else 'FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
