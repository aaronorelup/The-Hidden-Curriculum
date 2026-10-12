# Legacy freeze test

The 12 lessons published before 2026-10-12 are **legacy**: whatever changes in `engine/` or `tools/`, they must
render exactly as they did then (their pages load the frozen `engine/legacy/map-v1.js`, and the rest of the engine
must not move a pixel of them either). This folder checks that, byte for byte.

```bash
# after a change to engine/ or tools/: render a new phase (any new name; an existing phase is never overwritten
# without --force), hashes only (a full phase with PNGs is about 320 MB because the paper grain defeats compression)
python tests/legacy_freeze/stills_hash.py after-my-change --no-png

# compare it with the recorded baseline; the last line is ALL IDENTICAL (exit 0) or "<n> DIFFERENCES" (exit 1)
python tests/legacy_freeze/compare.py before after-my-change
```

Both scripts work from any directory and need Python 3 with Playwright (Chromium) and, for `--diff`, Pillow. A run
takes about 30 s.

- `stills/<lesson>/before.sha256.json` is the baseline, recorded on 2026-10-12 against commit `73a7f51` (the
  course as it was before the rework) with Playwright 1.58.0 / Chromium 145.0.7632.6 (headless shell, software
  raster) on Windows 11. Every other phase you record lands next to it and is ignored by git (`.gitignore`).
- **`_sandbox` is frozen too.** Its page loads `engine/legacy/map-v1.js` like the 12 legacy lessons, so all 13
  must stay identical (its map frames `s7` and `s8` catch a change to the frozen map or to anything it draws
  with). The data-driven `engine/map.js` has its own test lesson, `lessons/_maptest`.
- **Another machine or another Chromium** can change Skia's antialiasing, and then every still differs while the
  engine did not change: `compare.py` lists what the two runs loaded (`Chromium x -> y`, font files, font faces,
  engine files), so a browser or font change is not mistaken for a regression. If that happens, record your own
  baseline at a commit where the legacy lessons are known good (`git worktree add ../hc-base <commit>`, then
  `stills_hash.py before-local --root ../hc-base`) and compare against that phase instead.
- `--diff` writes red-on-dimmed diff images for every still that differs; it needs the PNGs of both phases, so
  record both without `--no-png` (the committed baseline is hashes only).
- `times.json` fixes the times of every still (8 spread over the lesson, 2 mid-crossfade, 1 inside the "Where it
  lives" map scene, chosen by a probe on `K.map.draw`; 00-05's map still was picked by eye). Normal runs only read
  it; `stills_hash.py --plan --force` re-plans it, after which older phases are no longer comparable.

What can make a phase differ without an engine change: Google Fonts shipping a new version (the font URLs change),
a slow network (`K.fontsReady` gives up after 8 s and draws system fonts), lazily loaded font subsets, a Playwright
upgrade, or a re-planned `times.json`. `compare.py` prints each of these under the lesson whose stills differ.
