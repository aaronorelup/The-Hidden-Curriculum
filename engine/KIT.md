# Kit reference (engine/kit.js, map.js, runtime.js)

Canvas is 1920×1080. Everything is a pure function of time `t`: no `Date.now()`, no `Math.random()`
(use `K.rng(seed)`), no state kept between frames. The renderer seeks frames out of order.

## A scene

```js
// lessons/<slug>/scenes/03.js
SCENE('03', (t, S) => {
  // t: seconds since this section's narration began (negative during the lead-in / crossfade)
  // S.dur: narration length   S.out: local time when the scene hands over (use for exit moves)
  // S.cue('name', fallback): local time of [[name]] in script.md
  // S.find('word' | /regex/, nth, fallback): local time a spoken word starts. A string is a literal,
  //   case-insensitive prefix ('T.' needs a real "T.", '.' is no wildcard; 'hid' also hits "hide");
  //   use a RegExp for patterns. S.find('hid', 0, fb, { whole: true }) matches whole words only
  //   (trailing punctuation on the spoken word is ignored, so "hid." still matches)
  // S.words: [[word, startAbs, endAbs], ...]
  K.bg();
  const a = S.cue('rename', 4);
  K.file(760, 520, 220, { ext: t < a ? 'txt' : 'py', name: t < a ? 'script.txt' : 'script.py' });
});
```

`lesson.js` holds metadata: `LESSON({ id, title, short, module, summary, poc, keep: [[bold, rest]],
images: { name: 'relative/path.jpg' }, draft: { '01': 10 }, noBadge: ['01'], badgeBacking: ['18'], transition: { '05': 'cut' } })`.
`transition` per section (the section being entered): `'fade'` (default, 0.6 s cross-dissolve), `'cut'`, or `'dip'`
(the outgoing scene fades to `K.bg` over the first 0.3 s, the incoming one fades in from `K.bg` over the next 0.3 s;
use it between two busy frames instead of hand-rolling an `S.out` fade). A section with no scene function yet draws
the plain background. Images load before frame 0 and appear as `K.img.name`. The painted plate:
`images: { plate: '../../engine/assets/teahouse-night.jpg' }` then `K.plate('plate', t, { zoom: true, shade: 0.35 })`.

## Timing & easing
| call | returns |
|---|---|
| `K.io(t, a, d=.6, e='io')` | 0→1 eased across [a, a+d]. e: `io` `out` `in` `sine` `back` (one overshoot max) `lin`. `a = Infinity` ("never") gives 0 and `d = 0` a clean step, never NaN (`K.seg` clamps non-finite spans; `K.layer` warns once on a NaN alpha) |
| `K.env(t, a, b=∞, d=.5)` | fades in at a, out at b |
| `K.stagger(t, a, i, step=.12, d=.6)` | i-th item of a staggered reveal |
| `K.seg(t, a, b)` `K.clamp` `K.lerp` | linear helpers |
| `K.wave(t, speed, amp, phase)` | idle sine motion |
| `K.rng(seed)` | deterministic random() |
| `K.typed(str, t, t0, cps=28)` / `K.typedDone(...)` / `K.caretOn(t)` | typewriter |
| `K.cam(t, [{at, x, y, z, d}])` + `K.withCam(cam, fn)` | eased camera over world coords |
| `K.zoomAt(x, y, z, fn)` | zoom by z about the screen point (x, y), which stays fixed (no pan at z 1); ease z yourself |

## Drawing
| call | notes |
|---|---|
| `K.bg({glow, glowX, glowY})` | night ground + lamp glow + vignette + grain. Start every scene with it (or `K.plate`). |
| `K.plate(name, t, {zoom, drift, shade, alpha, panX, mask})` | full-bleed painted image, darkened. `mask: [y0, y1]` shows only part of it: transparent at y0, opaque at y1 (y0 > y1 flips it), shade included, so the ground underneath shows with no seam (e.g. only the lower band of a title card: `mask: [680, 860]`) |
| `K.layer(alpha, fn)` / `K.at(x, y, s, rot, fn)` | alpha / transform wrappers |
| `K.pop(t, a, x, y, fn)` / `K.rise(t, a, fn)` | pop-in / slide-up reveals |
| `K.text(s, x, y, {size, font:'head'/'ui'/'read'/'mono', weight, color, align, alpha, upper, tracking, italic, maxW})` | returns width. `maxW` does NOT wrap: canvas squashes the glyphs horizontally to fit. To cap a width, use `K.para` / `K.wrap` |
| `K.title(s, x, y, o)` | gold Zen Maru Gothic heading (default 72 px) |
| `K.eyebrow(s, x, y, o)` | tiny uppercase gold label |
| `K.para(s, x, y, w, o)` / `K.wrap(s, w, o)` / `K.measure(s, o)` | wrapped text |
| `K.spans([{s, color, weight, font, italic, alpha}], x, y, {align, size, font, alpha})` | mixed-colour line; returns its width. Options on the second argument apply to every part, a part's own keys win (so `alpha` fades the whole line or one part) |
| `K.card(x, y, w, h, {fill, stroke, r=24, glow, alpha, shadow})` | soft card |
| `K.pill(s, x, y, {size, color, fill, stroke, glow, alpha, font, weight, tracking, upper, w, icon, iconColor})` | centred pill label; returns its width. `font: 'mono'` for code/file-name pills. `w` is a minimum width (the pill still grows to fit its text), for rows of equal pills. `icon` (a `K.icon` name) draws an icon before the text, in `iconColor` (default the text colour) |
| `K.note(x, y, w, eyebrow, body, {size, alpha})` | card with eyebrow + wrapped Georgia body; returns height |
| `K.arrow(x1, y1, x2, y2, {k, bend, cx, cy, color, w, dash, head})` | self-drawing arrow (k = progress). `cx, cy` set the quadratic control point explicitly (overrides `bend`), for curves that must route around something |
| `K.path([[x, y], ...], {k, color, w, dash, alpha, head, headSize, tension})` | self-drawing smooth arrow through every waypoint (Catmull-Rom spline; k = progress by arc length; `head: false` for a plain line; `tension` 0.5 default, 0 = straight segments). Use it instead of hand-rolling multi-bend arrows |
| `K.line(x1, y1, x2, y2, {k, color, w, dash, alpha})`, `K.mark(x, y, w, k)`, `K.ring(x, y, rx, ry, k, {color, w, rot})`, `K.glow(x, y, r, color, a)` | line (k = progress; k ≤ 0 draws nothing, no round-cap dot), underline, circle-it (`rot` tilt, default -0.08; 0 = upright for wide pills), glow |
| `K.win(x, y, w, h, {title, titleSize, kind:'notepad'/'terminal'/'explorer'/'browser'/'code', focus, stroke, alpha, url, urlLock})` | window chrome; returns content rect. `titleSize` (default 22) lets a title meet the 26 px minimum; `stroke` sets the outline colour (default gold when `focus`, else line2). `url` adds a 60 px address bar (lock + mono 26 px address, clipped) under the title bar and the content rect starts below it; `urlLock: false` drops the lock |
| `K.term(rect, t, [{at, cmd, cps, prompt} / {at, out, color}], {prompt, size, lh, pad, rows})` | terminal that types itself; keeps the newest lines in view. `lh` line height (default `size*1.5`), `pad` inner padding (default 28), `rows` fixed visible row count (default: as many as fit `rect.h`; set it so a short window does not scroll its first line away), `idle: false` hides the blinking default prompt + caret shown before the first item starts (non-shell windows) |
| `K.editor(rect, t, lines, {syntax:'py', typeAt, cps, size, gutter})` | code/text editor |
| `K.file(x, y, s, {ext, name, nameSize, alpha})` / `K.folder(x, y, s, {name, nameSize})` | file & folder icons. The name label defaults to max(18, s·0.17) px, under the 26 px minimum below s ≈ 150: pass `nameSize: 26` for small icons |
| `K.icon(name, x, y, s, {color, w, alpha})` / `K.iconTile(name, x, y, s, o)` | line icons: person key lock cloud server globe gear book cap laptop check cross question lantern bulb chat code terminal shield envelope clock puzzle tea map pin house wifi brain router phone sparkle (AI agent) warning (triangle + !) file (document outline; for a chip or tile, where `K.file` is too heavy) program / exe (a running program or executable such as python.exe: app window with a run triangle; distinct from file, code and terminal) pointer (mouse arrow cursor; its tip sits at x - s·0.22, y - s·0.38) restart (circular reload arrow: restart, retry, keep-alive) |
| `K.petals(t, {n, seed, alpha, avoid, fade})` | sparse blossom (title/end cards only). `avoid: [[x0, y0, x1, y1], ...]` keep-out rects (current transform space): a petal fades out over `fade` px (default 50) as it nears one, so petals never sit on text |
| `K.badge(id, label, {alpha, backing})` | drawn automatically on every scene except `noBadge`. `backing: true` (or an opacity, default 0.55) lays a soft dark pill behind it; set it per lesson with `LESSON({ badgeBacking: true \| ['18', '19'] })` for bright scenes (e.g. guest scenes on a `K.bg({glow})` above ~0.6) instead of hand-drawing a pill in the scene |

Colours: `K.C.page tile head strong body soft quiet line line2 accent gold blossom paper`.
`K.rgba(color, a)`, `K.mixColor(c1, c2, k)` (returns `rgb(...)`). Both accept `#rrggbb`, `#rgb` or `rgb()/rgba()` input, so they nest: `K.mixColor(K.mixColor(a, b, x), c, y)` and `K.rgba(K.mixColor(a, b, x), .5)` work (before 2026-10-03 a nested mix came out black).

## The map
`K.map.draw(t, { t0, focus: 'trust' | '15' | '00', focusK, dim, pin: '15', pinK, pinDrop, pinGlowK, path, chips })` (`chips: false` or `modules: false` hides the module rows). `questions: false | 0..1 | (districtId) => 0..1` fades the district questions (default 1), e.g. for a scaled-down map that should show only names.
`highlight: id | [ids]` (district or module ids) keeps more districts lit, with a gold outline and no glow, alongside `focus` (e.g. `focus: '00', highlight: 'machine'`). To ease it in, pass `highlight: { machine: k }` (id to 0..1) or `highlight: (districtId) => 0..1`: the outline blends from the plain line to gold and the district un-dims with k, so no overlay outline is needed. `pinSize` (default 44; the tip stays on the same spot) and `pinColor` (default `C.accent`) restyle the you-are-here pin.
`focus: '00'` / `'21'` lights the Start / Finish and dims every district (the gate itself stays lit). `pinK` fades the pin; `pinDrop` (0..1, ease it yourself, e.g. `K.io(t, a, .7, 'back')`) drops it in from 90 px above; `pinGlowK` (0..1) eases the pinned row's wash or the Start/Finish ring and glow. All default to 1.
`lanterns: 0..1 | (i) => 0..1` lights the six lanterns, one over each district (0 = bare 0.2-alpha ghost, no glow), and `lanternLabels: 0..1` fades their label row; both default to 1, so a reveal can hold the Lanterns back until they are named. The Lanterns are AI and are NOT a district (no modules; COURSE.md). `K.map.lanternAt(i)` → `{x, y}` of lantern i (`K.map.LANTERNS.n` of them).
`districtK: 0..1 | (id) => 0..1` shows each district on its own clock (ids `machine code history network trust shipping`, plus `ai` for the lantern string and `gate` / `end`); it scales the card and its opaque footprint, so at 0 the district is gone and the path shows. Default 1.
`lanternSway: n | (i) => n` multiplies each lantern's idle sway (built-in 0.06 rad; default 1). `lanternDrop: 0..1 | (i) => 0..1` drops each lantern onto the string from 90 px above, like `pinDrop` (ease it yourself; default 1 = hung).
`lanternHide: 0..1 | (i) => 0..1` lifts a lantern out of the map in place (1 = gone; the cord and labels stay; default 0). To carry it elsewhere, redraw it with `K.map.lantern(t, i, { x, y, lit, sway, alpha, glowK, s })`: the map's own glow and swaying icon (same per-index sway phase, so pass the same `i`; x/y default to `lanternAt(i)`, `glowK` 1.8 matches the map's focus-'ai' glow, `s` scales it). Lift + redraw at the same spot shows no jump.
`rowWash: { '14': { k, color }, ... }` washes any module row in a colour (k 0..1, colour hex, default gold) with the pinned row's 38 px pill, under the row's text; the pinned row's own wash wins on that row.
`K.map.chipPos('15')` → `{x, y, w}` of a module row (for arrows and camera targets).
`K.map.district('trust')` → `{x, y, w, h, name, q, mods}`. `K.map.MODULES['15']` → name. Module numbers run in map order: Start 00 · Machine 01–03 · Code 04–07 · History 08 · Network 09–13 · Trust 14–16 · Shipping 17–20 · Finish 21.
Zoom into a district: `K.withCam(K.cam(t, [{at:0, x:960, y:540, z:1}, {at:2, x:960, y:752, z:1.6}]), () => K.map.draw(t, {...}))`
(y 752 is the bottom row's middle; derive targets from `K.map.district(id)` rather than hard-coding them).
The map fits the safe area: lantern string from y 124, district rows y 258–558 and 584–920, Start (00) y 408, Finish (21) y 752.
Type on the map meets the course minimums (`K.map.TYPE`): district names 38, questions 26, module names 26 (numbers mono 22),
the Lanterns' label row 26 (eyebrow) / 30 (question) at `LANTERNS.y + 66`, Start/Finish labels 26. Module rows: baseline `d.y + 150 + 40 j` (`K.map.ROW`); a pinned row's
wash is `K.rr(c.x - 18, c.y - 19, c.w + 36, 38, 19)` around `chipPos`.

## Review stills (tools/stills.py)
`--from S --to S` limits the frames to a time window (lesson seconds); it combines with `--every` (the grid starts at `--from`), `--at` and `--scene`, and an empty window gets 9 evenly spaced frames. E.g. `python tools/stills.py <lesson> --from 41 --to 43 --every 0.25 --tag beat`.
