"""Compare two phases of regression stills, lesson by lesson, byte for byte (sha256 of the PNGs).

usage:
  python compare.py <phaseA> <phaseB>              e.g. python compare.py before after
  python compare.py <phaseA> <phaseB> --diff       also write stills/<lesson>/diff-<A>-<B>/<still>.png for every
                                                   still that differs (changed pixels in red over a dimmed copy
                                                   of A) and print how many pixels changed and where
  python compare.py <phaseA> <phaseB> --lessons 00-01-the-hidden-curriculum _sandbox

Last line: "ALL IDENTICAL" (exit 0) or "<n> DIFFERENCES" (exit 1). A lesson recorded in only one of the
phases counts as a difference, so a partial "after" run can never pass for a full one.
When stills differ, the inputs the two runs loaded are listed too (engine / lesson files, font files,
font subsets, Chromium version), so a font or browser change is not mistaken for an engine regression.
"""
import argparse
import json
import pathlib
import sys

OUT = pathlib.Path(__file__).resolve().parent / 'stills'   # where stills_hash.py records each phase


def load(d, phase):
    f = d / f'{phase}.sha256.json'
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else None


def input_changes(ra, rb):
    """why two runs might differ besides the engine: what each run loaded"""
    notes = []
    fa, fb = ra.get('inputs') or {}, rb.get('inputs') or {}
    changed = [k for k in sorted(set(fa) | set(fb)) if fa.get(k) != fb.get(k)]
    if changed:
        notes.append('files changed: ' + ', '.join(f'{k}{"" if k in fa else " (new)"}{"" if k in fb else " (gone)"}' for k in changed))
    if ra.get('chromium') != rb.get('chromium'):
        notes.append(f'Chromium {ra.get("chromium")} -> {rb.get("chromium")}')
    ea = [u for u in ra.get('external', []) if 'gstatic' in u]
    eb = [u for u in rb.get('external', []) if 'gstatic' in u]
    if sorted(ea) != sorted(eb):
        notes.append(f'font files differ: -{sorted(set(ea) - set(eb))} +{sorted(set(eb) - set(ea))}')
    ga = set(ra.get('faces_at_ready', [])) | set(ra.get('faces_lazy', []))
    gb = set(rb.get('faces_at_ready', [])) | set(rb.get('faces_lazy', []))
    if ga != gb:
        notes.append(f'font faces in use differ: -{sorted(ga - gb)} +{sorted(gb - ga)}')
    if ra.get('faces_lazy') or rb.get('faces_lazy'):
        notes.append('font subsets loaded lazily while drawing (first-draw fallback risk): '
                     f'{len(ra.get("faces_lazy", []))} / {len(rb.get("faces_lazy", []))}')
    if ra.get('times') != rb.get('times'):
        notes.append('TIMES DIFFER (times.json was re-planned between the phases)')
    if ra.get('driver') != rb.get('driver') or ra.get('order') != rb.get('order'):
        notes.append(f'driver/order {ra.get("driver")}/{ra.get("order")} -> {rb.get("driver")}/{rb.get("order")}')
    return notes


def pixel_diff(pa, pb, out_png):
    from PIL import Image, ImageChops
    a, b = Image.open(pa).convert('RGB'), Image.open(pb).convert('RGB')
    if a.size != b.size:
        return f'size {a.size} vs {b.size}'
    d = ImageChops.difference(a, b).convert('L')
    box = d.getbbox()
    if box is None:
        return 'pixels identical (PNG encoding differs only)'
    mask = d.point(lambda v: 255 if v else 0)
    n = sum(1 for v in mask.getdata() if v)
    peak = max(d.getdata())
    vis = Image.blend(a, Image.new('RGB', a.size, (0, 0, 0)), 0.6)
    vis.paste(Image.new('RGB', a.size, (255, 40, 40)), (0, 0), mask)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    vis.save(out_png)
    return f'{n} px changed ({100 * n / (a.size[0] * a.size[1]):.3f} %), max channel delta {peak}, bbox {box}'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('a')
    ap.add_argument('b')
    ap.add_argument('--diff', action='store_true')
    ap.add_argument('--lessons', nargs='*')
    o = ap.parse_args()
    bad = 0
    dirs = sorted(p for p in OUT.iterdir() if p.is_dir() and (load(p, o.a) or load(p, o.b)))
    if o.lessons:
        dirs = [OUT / s for s in o.lessons]
    if not dirs:
        sys.exit(f'no lesson has phase "{o.a}" or "{o.b}"')
    for d in dirs:
        ra, rb = load(d, o.a), load(d, o.b)
        if not (ra and rb):
            bad += 1
            print(f'{d.name}: MISSING phase "{o.a if not ra else o.b}"')
            continue
        ha, hb = ra['sha256'], rb['sha256']
        diff = [k for k in sorted(set(ha) | set(hb)) if ha.get(k) != hb.get(k)]
        bad += len(diff)
        same = len([k for k in ha if hb.get(k) == ha[k]])
        print(f'{d.name}: {len(ha)} vs {len(hb)} stills, {same} identical' + (f', differ: {diff}' if diff else ''))
        if diff:
            for n in input_changes(ra, rb):
                print(f'    inputs: {n}')
        for k in diff if o.diff else []:
            pa, pb = d / o.a / k, d / o.b / k
            if pa.exists() and pb.exists():
                print(f'    {k}: {pixel_diff(pa, pb, d / f"diff-{o.a}-{o.b}" / k)}')
            else:
                print(f'    {k}: only in {o.a if pa.exists() else o.b}')
    print('ALL IDENTICAL' if not bad else f'{bad} DIFFERENCES')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
