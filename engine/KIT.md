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
the plain background. Images load before frame 0 and appear as `K.img.name` (videos and sounds: see Media exhibits below). The painted plate:
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
| `K.win(x, y, w, h, {title, titleSize, kind:'notepad'/'terminal'/'explorer'/'browser'/'code', focus, stroke, alpha, url, urlLock})` | window chrome; returns content rect. `titleSize` (default 22) lets a title meet the 26 px minimum; `stroke` sets the outline colour (default gold when `focus`, else line2). `url` adds a 60 px address bar (lock + mono 26 px address, clipped) under the title bar and the content rect starts below it; `urlLock: false` drops the lock; `compact: true` (with `url`) puts the address pill in the 50 px title bar instead, like a real browser (no title text, no second row; K.demo uses it; an address too long for the pill ends in '…' before the window buttons); `icon: 'name'` draws that K.icon (30 px, `iconColor` default soft) in place of the kind's title-bar glyph, so a scene can swap the icon without redrawing the title; `buttons: false` hides the minimise / maximise / close buttons |
| `K.term(rect, t, [{at, cmd, cps, prompt} / {at, out, color}], {prompt, size, lh, pad, rows})` | terminal that types itself; keeps the newest lines in view. `lh` line height (default `size*1.5`), `pad` inner padding (default 28), `rows` fixed visible row count (default: as many as fit `rect.h`; set it so a short window does not scroll its first line away), `idle: false` hides the blinking default prompt + caret shown before the first item starts (non-shell windows) |
| `K.editor(rect, t, lines, {syntax:'py', typeAt, cps, size, gutter})` | code/text editor |
| `K.file(x, y, s, {ext, name, nameSize, alpha})` / `K.folder(x, y, s, {name, nameSize})` | file & folder icons. The name label defaults to max(18, s·0.17) px, under the 26 px minimum below s ≈ 150: pass `nameSize: 26` for small icons |
| `K.icon(name, x, y, s, {color, w, alpha})` / `K.iconTile(name, x, y, s, o)` | line icons: person key lock cloud server globe gear book cap laptop check cross question lantern bulb chat code terminal shield envelope clock puzzle tea map pin house wifi brain router phone sparkle (AI agent) warning (triangle + !) file (document outline; for a chip or tile, where `K.file` is too heavy) program / exe (a running program or executable such as python.exe: app window with a run triangle; distinct from file, code and terminal) pointer (mouse arrow cursor; its tip sits at x - s·0.22, y - s·0.38) restart (circular reload arrow: restart, retry, keep-alive) |
| `K.petals(t, {n, seed, alpha, avoid, fade})` | sparse blossom (title/end cards only). `avoid: [[x0, y0, x1, y1], ...]` keep-out rects (current transform space): a petal fades out over `fade` px (default 50) as it nears one, so petals never sit on text |
| `K.badge(id, label, {alpha, backing})` | drawn automatically on every scene except `noBadge`. `backing: true` (or an opacity, default 0.55) lays a soft dark pill behind it; set it per lesson with `LESSON({ badgeBacking: true \| ['18', '19'] })` for bright scenes (e.g. guest scenes on a `K.bg({glow})` above ~0.6) instead of hand-drawing a pill in the scene |

Colours: `K.C.page tile head strong body soft quiet line line2 accent gold blossom paper`.
`K.rgba(color, a)`, `K.mixColor(c1, c2, k)` (returns `rgb(...)`). Both accept `#rrggbb`, `#rgb` or `rgb()/rgba()` input, so they nest: `K.mixColor(K.mixColor(a, b, x), c, y)` and `K.rgba(K.mixColor(a, b, x), .5)` work (before 2026-10-03 a nested mix came out black).

## The map
The course map is laid out from data: `window.COURSE` (`engine/course.js`, written by `python tools/course.py sync` from
curriculum.md; docs/course-data.md explains the whole chain). Start, then 4 to 7 districts (one question each, up to 5 modules
each) on a U-shaped garden path (top row left to right, bottom row right to left), then the Finish, with the Lanterns (AI: one
lantern per district, never a district) strung over them. When the course changes, edit curriculum.md, run sync and re-render;
never hard-code district names, module numbers or labels in a scene. Legacy lessons (the 12 published before 2026-10-12) load
the frozen `engine/legacy/map-v1.js` instead (the same API, the hand-tuned six-district map), so their videos never change;
the template's `{{MAPJS}}` gives every other local page `engine/course.js` + `engine/map.js`. On the site a curriculum
lesson's page loads its own copy of the course data (`lessons/<key>/course.js`, written by publish.py when the lesson is
staged) instead of the shared file, so a curriculum change never redraws the map under a live page's old narration.
The Start and the Finish hold one module each (one circle, one number); `course.py check` and `audit()` enforce it.

**The standard map section.** Section 02 of every new lesson is `## 02 — Where this sits on the map [map]`. Its narration is
generated by `course.py sync` (between `<!-- map:begin -->` and `<!-- map:end -->`, with `[[district]]` and `[[module]]` cues)
and its scene is one line, `scenes/02.js`: `SCENE('02', (t, S) => K.map.intro(t, S));`. Don't rewrite or re-animate it.
`K.map.intro(t, S, o)`: the map assembles (Start, the districts in path order, the Finish, the lanterns lighting up), the
lesson's district comes into focus at `[[district]]` (outline and glow ease in, its question is underlined; for a Start or
Finish lesson a note with the region's name and question appears by the circle, as wide as the card beside it, with the
"you are here" card under it, or beside it when both would not fit in the row), the pin drops on the module row at
`[[module]]` and only then does the row light up (wash, bright number, bold label follow `pinGlowK`), and a "you are
here" card with the lesson's title (lesson.js `title`, as on the title card; `short` is only for the badge) joins it. Where the card goes: right of the district, over its neighbour; else inside a
wide district, right of its longest label (the pin moves next to it); else left of the district, with the pin moved to
the row's left end so pin, leader and card stay together. A card over a neighbour takes that neighbour's whole column
(300 to 460 px wide, the title wraps up to three lines), and every district card it (or a Start / Finish note) covers
fades out completely before the card fades in, so the two never show through each other and no half-covered words peek out.
Then everything rests. Without cues: the district at 22% of `S.dur` (1.4 to 4 s), the module at
max(district + 1.6 s, 60%). o: `lesson` (key or id; default the lesson playing, found through `DEF.key`, or `DEF.id`
for a lesson without a key; a key the course no longer lists falls back to `DEF.module`, never to its old ID),
`title` (card text), `pin` (override), `tDistrict`, `tModule`, `t0` (assembly start, default -0.3), `card: false`,
`map: {...}` (extra draw options). `K.map.hereCard(x, y, title, o)` draws the card alone.

**Naming things.** Every `pin`, `focus` and `highlight` value goes through `K.map.resolve(x)`: a module number (`'05'` or `5`),
a module's map label or full name (`'Packages'`), a district id or name (`'code'`, `'The Code'`), `'gate'` / `'start'` /
`'end'` / `'finish'` (or the Start / Finish region's id or name), `'ai'`, a lesson key or id, or `'lesson'` (the lesson
playing). In new scenes prefer names or `'lesson'`: module numbers change when the curriculum is reordered.
`course.py check` resolves every string literal a built lesson's scenes hand the map (`pin:`, `focus:`, `highlight:`,
`K.map.chipPos('...')`, `district`, `districtOf`, `resolve`, `pinAt`, `lesson`) against the current curriculum and fails
on one the map no longer knows (a renamed district or module); a district id can be pinned in curriculum.md with
`# District 4 · The Wire — how computers talk <!-- id: network -->`.

`K.map.draw(t, o)` takes every v1 option: `t0` (staggered reveal), `focus`, `focusK` (0..1; also eases the focus outline),
`dim` (0.7), `pin`, `pinK`, `pinDrop`, `pinGlowK` (0..1, default 1: the pinned row's wash, bright number and bold label),
`pinSize` (44), `pinColor`, `pinSide: 'left'` / `pinX` (a module pin at the row's left end, or at an x), `highlight` (id | [ids] | `{ id: k }` |
`(districtId) => k`: gold outline, undimmed), `path` (0..1), `chips` / `modules: false`, `questions` (false | 0..1 | fn),
`lanterns`, `lanternLabels`, `lanternSway`, `lanternDrop`, `lanternHide` (each a number or `(i) => n`), `rowWash`
(`{ '14': { k, color } }`), `districtK` (0..1 or fn; ids are the district ids plus `'ai'`, `'gate'`, `'end'`).
Lookups: `chipPos(mod)` → `{x, y, w, d, lines}` (y is the middle of the row's text, also for a two-line label);
`district(id | name)` → the card `{x, y, w, h, name, q, mods, lines: {name, q}, rows: {mod: {y, lines}}, labelW}`;
`districtOf(mod)`; `lanternAt(i)`; `lantern(t, i, o)` (lift one out with `lanternHide`, redraw it anywhere);
`pinAt(x, o)` (`o.pinSide` / `o.pinX` as in draw); `lesson(keyOrId)`; `here()`; `MODULES` (number → map label); `DISTRICTS` (path order); `LANTERNS` (`n` = number of
districts, `y`, `x0`, `x1`); `GATE` / `END` (`x, y, mod, mods, name, q`); `ROW` (the rhythm in use: `name`, `q`, `first`,
`pitch`); `PATH`; `TYPE` (unchanged sizes: names 38, questions 26, labels 26, numbers mono 22, Lanterns row 26/30, Start/Finish
26); `layout()`; `audit()`; `use(courseData)` switches the data the map draws (`use(null)` = window.COURSE; tests).
Coordinates: derive them from `district()`, `chipPos()`, `GATE` / `END`, never from constants: with 4 districts the cards are
twice as wide, with 7 the top row has four.

How the layout is chosen (map.js `build`): two rows, `ceil(N/2)` on top (for an odd N, whichever split wraps fewer lines);
cards in a row share the width equally when the content fits (a two-card row fills it), else the cards that need more get it;
the frame widens from x 1670 to 1790 when that saves wrapped lines; district names, questions and module labels wrap to two
balanced lines (never ending on '&' or 'and'); the rows are packed between y 258 and 920 (gap, then padding, then a compact
rhythm) and a smaller map is centred vertically. Type never shrinks below the minimums: what cannot fit is reported by
`audit()`, and `course.py check` fails on it, naming the fix: a short label in curriculum.md,
`## Module 05 — Long Module Name <!-- map: Short name -->` (a label that wraps is a warning, with the length that fits,
measured in that label's own characters, and a suggested label). Safe area: cards x 250 to 1670 (1790), y 258 to 920;
lantern string from y 124; Start / Finish circles at x 135.
Test lesson: `lessons/_maptest` (fixture courses with 6, 4, 5 and 7 districts, every card placement; `python
lessons/_maptest/make.py`, then `python tools/stills.py _maptest --every 2`). `python tools/course.py map --png map.png
--pin <module | key>` renders one map.

## Media exhibits: video clips, screenshots, sounds
Real footage, real screenshots and real sound sit in a scene like any drawing and keep it a pure function of time: the
scene says which **media time** it wants this frame (`t - S.cue('run')`), the engine makes the picture and the sound match.
Declare the files in `lesson.js` (paths relative to the lesson folder):

```js
LESSON({ ...,
  images: { settings: 'assets/img/settings.webp', spec_song: 'assets/img/spec_song.webp' },   // stills, screenshots, spectrograms
  videos: { term: 'assets/video/terminal.mp4' },      // or { src, fps }
  sounds: { song: 'assets/audio/song.mp3' },          // or { src, gain } (linear; the live page caps it at 1)
});
```

Videos and sounds are fetched whole before frame 0 (the site answers Range requests with a plain 200, so a streamed file
could not seek); the page shows "Loading lesson… n %". A file that fails prints a console error and draws a dashed
"video missing" box (or stays silent); the lesson still plays.

| call | notes |
|---|---|
| `K.video(name, mediaT, x, y, w, h, o)` | frame of the clip at `mediaT` seconds into it, fitted into the box. Holds the first frame before 0 and the last after the end; `loop: true` wraps; `t * 2` plays at 2x. `sound: true` (or a sounds:{} name) also plays that sound at the same media time. Returns a placement (below) |
| `K.image(name, x, y, w, h, o)` | an `images:{}` picture fitted into the box; returns a placement |
| options of both | `fit: 'contain'` (default, letterboxed) or `'cover'` (fills, cropped) · `align: [ax, ay]` (0..1, default centred: where a contained picture sits / which part a cover keeps) · `crop: [sx, sy, sw, sh]` (source pixels) · `zoom: {x, y, z}` (a z-times closer look at source point x, y, kept inside the picture; ease z yourself) · `r` (corner radius, default 12) · `alpha` · `bg` (letterbox fill; the whole box is then the frame) · `stroke` (true = `C.line2`, or a colour; `lw`) · `smooth` (`'high'` default, `'medium'`, `'low'`, `false` = crisp pixels for a magnified UI) |
| placement | `{x, y, w, h, s, at(px, py)}`: the drawn picture's rect and scale, and `at` = the canvas point where source pixel (px, py) landed (current transform space), through crop and zoom: put a cursor, ring or label on a button of a screenshot |
| `K.cursor(x, y, {s, click, ringColor, alpha, kind, press, ripple, key, keyAlpha})` | a crisp OS-style mouse pointer (white, dark outline, soft shadow), hotspot at (x, y); `s` 1 = about 40 px; `click` 0..1 spreads a ring from the tip (ease it yourself); `kind`: `'arrow'` (default), `'hand'` (over a link; hotspot = fingertip), `'text'` (I-beam; hotspot = its middle); `press` 0..1 dips it to 88 % while the button is down; `ripple: true` adds a soft filled disc under the ring; `key: 'Enter'` / `'Ctrl+K'` / `['Ctrl', 'K']` shows a key chip beside it |
| `K.keycap(label, x, y, {size: 28, alpha, color, fill, stroke})` · `K.keys(combo, x, y, {size, align, alpha})` | one keyboard key chip centred at (x, y) · a key or shortcut as chips with `+` between (`'Control+Shift+P'`; Playwright names shorten to Ctrl, Win, Esc, Up...); both return their width |
| `K.listen(name, playT, x, y, w, h, {dur, label, sound, r, alpha})` | an audio exhibit as a strip: the spectrogram `images['spec_' + name]` (spanning the whole sound) with a playhead, label and clock; heard too when `sounds:{}` has `name` (`sound: false` to keep it silent). No spectrogram: a calm empty strip |
| `K.sound(name, playT)` | the sound is heard this frame at `playT` seconds into it (silent before 0 and after its end), with nothing drawn |
| `K.videoDur(name)` · `K.soundDur(name)` · `K.mediaSize(name)` | length in seconds (0 if not loaded) · `[w, h]` source pixels of an image or clip |

```js
SCENE('05', (t, S) => {   // a real screenshot "in use": zoom in, point, click, then the recording plays
  K.bg();
  const go = S.cue('click', 3), btn = [800, 645];                     // the button, in screenshot pixels
  const p = K.image('settings', 90, 190, 1040, 585, { zoom: { x: btn[0], y: btn[1], z: 1 + 1.4 * K.io(t, 1, 1.6) }, stroke: true });
  const [bx, by] = p.at(...btn), k = K.io(t, 0.8, go - 0.8);
  K.cursor(K.lerp(1060, bx, k), K.lerp(260, by, k), { click: K.seg(t, go, go + 0.7) });
  K.video('term', t - go - 0.5, 1170, 260, 660, 371, { sound: true, r: 14, stroke: true });
});
```

Rules:
- **One media time per clip per frame.** A crossfade that shows one file at two times needs it declared twice under two
  names (it is fetched once); otherwise the console says so and the second time is ignored. Same for sounds.
- **Sounds play at 1x only**, while `playT` runs with the lesson clock; a held or jumping `playT` is silent, in the MP4
  and on the page alike. Leave a pause in the narration where a sound must be heard. Clips are always muted: a clip's
  own sound is a separate `sounds:{}` file under the same name (`media_util.py audio clip.mp4 x.mp3`) plus `sound: true`.
- **How it is drawn.** Renderer (`render.py`, `stills.py`): `window.__frame` / `__png` seek every clip the frame asks for
  to that frame's centre, `(n + 0.5) / fps`, and wait (they return a promise then; Playwright awaits it), so every
  frame is the exact frame, in any seek order. `render.py` reads `window.__heard()` after each frame and mixes each 1x
  stretch of each sound over `mix.mp3`, sample-accurately. Live page (`player.js`): the clips the drawn scene wants
  play in step with the narration (typically 35 ms off; re-seeked past 0.15 s, smaller drift steered with the rate), scrubbing
  re-seeks, pausing holds the exact frame; sounds play within 0.1 s of their place; in a hidden tab the sounds keep
  in step (about once a second) and the clips wait. Tested 2026-10-12 on `lessons/_mediatest` (its `tests/`).
- **The files** (`python tools/media_util.py ...`): `encode src dst.mp4 [--from --to --fps --width --crf]` makes a clip
  to the spec, `check *.mp4` verifies it: H.264 High, yuv420p, GOP 12 (`-g 12 -keyint_min 12 -sc_threshold 0`), no
  B-frames, +faststart, constant frame rate, no audio track, under 25 MB (Cloudflare Pages), and the **BT.601**
  matrix: Chromium's canvas decodes BT.601 exactly but draws a BT.709 clip visibly off (mean error 0.3 vs 2.4 tagged,
  6.1 untagged). `audio` makes a sound exhibit (MP3 192k, -16 LUFS like the narration mix), `spectrogram` its
  `spec_<name>` strip, `still` a screenshot as WebP at display size (`--lossless` keeps UI text crisp).
  `record dst.mp4 --seconds 8 --window "part of a title"` (or `--region x,y,w,h`) records what that window shows on
  screen (it must be on top) and encodes it; a web page can also be filmed headless with Playwright's video
  recording and passed to `encode` (`tools/capture.py` does both with a pointer and click log: Captures, below). Keep clips short and at display size (960x540 half screen, 1280x720 full): a
  10 s 960x540 clip is about 2.7 MB.

### Captures: real actions on a computer (tools/capture.py, K.demo, K.shot, K.termReplay)
A lesson can SHOW how a thing is really done: a real browser session, real commands with their real output, a real
screen. `tools/capture.py` records it into `lessons/<slug>/assets/capture/<name>/` and the kit replays it, still a pure
function of time. When to use which, how an agent records them unattended, the safety rules and file sizes:
`docs/showing-real-computer-actions.md`. Worked example: `lessons/_demo` (never published).

```
python tools/capture.py browser  <lesson> <name>   Playwright, clean throw-away profile, headless (recipe: lessons/<lesson>/steps/<name>.json)
python tools/capture.py terminal <lesson> <name>   real commands in a throw-away folder, neutral git, headless
python tools/capture.py desktop  <lesson> <name> --seconds 12 --window "title"   ffmpeg gdigrab + a 30 Hz pointer log
python tools/capture.py again <lesson> <name>   re-record from the lesson's recipe · check <lesson> · show <lesson> <name>
```

The recipe is `lessons/<lesson>/steps/<name>.json` (`--steps` overrides). A recording goes to `<name>.new/` and replaces
the capture only once it finished and passed `check`; a failed step is named (`step 7 of 12 (wait_for ...): ...`) and the
old capture stays. A capture folder holds `events.json` (what happened, on the recording's own clock: `move` with its
path, `click` with the target's box, `type` with per-key times and the field's font size, `key`, `scroll`, `nav`,
`shot`, `mark` with the boxes it measured; positions in VIDEO pixels), `video.mp4` (browser / desktop, to the clip spec
above; 1024x576 CSS at device pixel ratio 1.875, or 1280x720 at 1.5, is a crisp 1920x1080 clip the camera can zoom
into; prefer the smaller viewport for a page meant to be read: its text is 25 % larger at rest), `shots/*.webp` (real
screenshots taken by `shot` steps, WebP quality 92; `"format": "png"` keeps a PNG) and `steps.json` (a copy of the
recipe it was recorded from). Declare it in `lesson.js`; it loads before frame 0 with the other media:

```js
LESSON({ ..., captures: { site: 'assets/capture/site/', term: 'assets/capture/term/' } });
```

The clip becomes the video `'cap:<name>'` (frame-exact in the MP4, played in step on the live page like any `K.video`),
each shot the image `'<name>/<shot>'` (`K.image` and `K.shot` take it), the events lookup tables. A missing or broken
capture prints a console error and draws a dashed placeholder; the lesson still plays.

| call | notes |
|---|---|
| `K.demo(name, t, rect, o)` | plays a browser or desktop capture at capture time `t` (seconds into the recording: pass `t - S.cue('go')`; it holds the first frame before 0 and the last after the end) inside window chrome at `rect` `[x, y, w, h?]` (leave `h` out: the recording's own aspect plus the 50 px bar). Draws the pointer from events.json (smoothed, the hand over links, the I-beam over text, a dip and a ripple on every click), typed text in a chip under its field **only while the field's own text is under about 24 px on screen** (its recorded font size x the clip's scale x the zoom: once the camera is on the field the real text reads, and the chip fades), pressed keys as key chips **beside the pointer**, and runs the **automatic camera**: it eases toward each click and typing target (`lead` 1.25 s before it, over `camD` 1.15 s, up to `zoom` 1.8x, in log scale), pans between targets less than `join` 2.6 s apart, holds `hold` 1.1 s and eases back out; a scroll or a page load ends a zoom, and a zoom that could not hold still for `minHold` 0.6 s before it must leave is not made (a click that loads a page at once: only the pointer moves). o: `zoom`, `follow: false` (no automatic camera), `zooms` (a scripted camera instead, as K.shot), `lead` / `hold` / `join` / `camD` / `minHold`, `callouts: [{at, until \| dur, box: [x, y, w, h] (video px) \| [[x, y, w, h], ...], text, side: 'top' \| 'bottom', dim: 0.42 \| false, zoom: true \| z}]` (a gold box drawn round part of the screen, the rest dimmed, a label pill; `zoom` also brings the camera to it; a list of boxes, e.g. a highlight that wraps over two lines, gets one outline each, one shared dim cutout, and the label and zoom on their union), `chrome: 'browser'` (default for browser captures: the address pill shows the page's real URL as it changes) \| `'window'` \| `'none'`, `url`, `title`, `frame` (the stage the zoom fills; default a rounded panel x 24-1896, y 120-1056, under the badge band), `cursor` (default on, off for a desktop capture whose video has the OS pointer), `cursorScale`, `chips: false`, `keys: false`, `fieldText` (text height / field height when no font size was recorded, 0.45), `alpha`. A terminal capture goes to `K.termReplay` inside a terminal window (o as K.termReplay, plus `title`). Returns `{cam, at(px, py), rect, content}`: `at` is the screen point of a video pixel through the camera, for your own marks |
| `K.shot(name, t, rect, o)` | a real still screenshot "in use" (an `images:{}` name or a capture's shot `'site/course-page'`), in the same chrome and camera as K.demo, with a scripted pointer: `cursor: [{at, x, y, click, kind: 'hand' \| 'text', move}]` (source px; `at` = arrival; it travels over `move` s, default by distance, along an eased, slightly curved path; `click: true` clicks 0.18 s after arriving), `zooms: [{at, until, box \| x, y, z, d, snap}]` (default: the automatic camera on the clicks; a zoom whose next one starts within a move of its `until` pans straight on, no dip; `snap: true` jumps to the framing instead of easing in, so `{at: 0, box, snap: true}` starts the shot already cropped), `typing: [{at, text, box, cps: 14}]`, `keys: [{at, key}]`, `callouts`, `swap: [{at, name, d: 0.3}]` (crossfade to the next screenshot in the same chrome and camera, the address pill taking its URL: put it about 0.25 s after the click that causes it, so a click visibly does something), `chrome`, `url` (default the shot's URL), `title`, `frame`, `alpha`. For actions an agent captured as screenshots. Its camera is memoised on everything it depends on, so scenes sharing a shot never share a camera by accident |
| `K.termReplay(rect, t, name, o)` | replays a terminal capture in a K.win content rect at capture time `t`: each real command typed at a human pace (`cps` 15, deterministic jitter), `think` 0.35 s, Enter, its real output lines at their real delays (each capped at `maxWait` 1.5 s; `speed` divides them), a fresh prompt, `gap` 1 s before the next. Keeps the newest lines in view and wraps long lines like a real terminal. o: `size` 30, `lh`, `pad` 30, `start` 0.6, `cps`, `think`, `gap`, `maxWait`, `speed`, `only: [command indexes]`, `blank` (an empty line before each new prompt; default true for cmd), `errColor`, `idle`, `alpha` (rows, caret and marks; K.demo passes its own), `marks: [{at, until \| dur, match: 'text' \| /re/, text, side: 'above' \| 'below' \| 'right', labelAt: [x, y], padX}]` (box the newest visible line that matches, with a label beside the line or under it; `side` forces the label above or below the box, e.g. above when the line fills the width and the label would cover the next output line, or `'right'` beside the line's end even when the auto rule would put it under; `labelAt` puts the label's top-left corner anywhere, e.g. in the title bar; `padX` the box's left/right padding, default 10, e.g. 4 so the box clears the `*` of `git log --graph` just before the match). Returns `K.termTimes` |
| `K.termRows(rect, t, name, o)` | the rows that same `K.termReplay(rect, t, name, o)` draws at `t`, without drawing (same wrapping, scrolling and blank lines): `{size, lh, pad, cw, cols, rows: [{i, s, x, y, top, h, endX}], find(match, {padX})}`. `y` is the baseline, `top`/`h` the row band a mark box uses, `endX` where the row's text ends. `find('text' \| /re/)` returns the newest visible matching row `{i, s, from, len, x, w, y, endX, bx, by, bw, bh}` (`x`/`w` the matched characters, `bx..bh` the mark box) or null. Use it for your own boxes, links and labels instead of copying the replay's layout |
| `K.termTimes(name, o)` | the replay's schedule for the same o: `{dur, items: [{cmd, start, typed, enter, done, out: [{at, s}]}]}`, to hang marks, callouts or narration beats on a command |
| `K.capture(name)` · `K.captureDur(name, o)` · `K.capturePointer(name, t)` | the loaded capture (events.json plus its tables: `clicks`, `types`, `presses`, `scrolls`, `navs`, `events`, `shots`), or null · its length on its own clock (the recording, or the terminal replay for o) · the recorded pointer at capture time t, `[x, y, kind]` in video pixels (map it with the `at` K.demo returns) |
| `K.captureAt(name, mark, fallback)` · `K.captureBox(name, mark, box, fallback)` | the time of a recipe's `{"do": "mark", "name": mark}` step (or of a `shot` step of that name) on the capture's clock · the box `[x, y, w, h]` (video px) that mark or shot measured for `box` (`"boxes": {"stage": "#stage"}` in its step). The fallback (and one console error) when there is none. How scenes hang callouts, zooms and pointers on a capture without typing in numbers that move with every re-record |

```js
SCENE('04', (t, S) => {                         // the browser capture, starting at [[open]]
  K.bg();
  const go = S.cue('open', 1), play = K.captureAt('site', 'playing');   // {"do": "mark", "name": "playing", ...}
  const st = K.captureBox('site', 'playing', 'stage');                    // ... "boxes": {"stage": "#stage"}}
  K.demo('site', t - go, [260, 150, 1400], {
    callouts: [{ at: play + 2.2, until: play + 5.4, box: [st[0] + st[2] * 0.22, st[1] + st[3] * 0.85, st[2] * 0.56, st[3] * 0.11],
      text: 'Real captions, from the real player', zoom: 1.6 }],
  });
});
SCENE('05', (t, S) => {                         // real commands; one line of output boxed once it has printed
  K.bg();
  const st = K.termTimes('term').items[3];
  K.demo('term', t - 0.4, [260, 190, 1400, 720], { title: 'Command Prompt', size: 32,
    marks: [{ at: st.out[0].at + 0.5, dur: 3.4, match: 'On branch master', text: 'Real output, at its real speed' }] });
});
```

Rules:
- **Times are the capture's own clock** (events.json `t`, the video's seconds); a scene maps the lesson to it with an
  offset, `t - S.cue('go')`. Callouts, marks and zooms use the same clock.
- **Never hard-code a capture time or position.** They move with every re-record (one re-record moved every event of the
  demo by 0.36 s; a slow page load moves them by seconds) and the scene would silently drift out of step. Add a `mark`
  step (with `boxes`) to the recipe at the moment a scene points at, and read it: `K.captureAt`, `K.captureBox`, a
  recorded event (`K.capture('site').clicks.find((e) => e.target === 'target=#bigplay').t`), `K.termTimes`.
  `capture.py show` is for looking, not for copying numbers into a scene. Measure a box only once the page has settled
  (`wait_for` the final text first): a box taken while a page is still filling in is wrong a second later.
- **The camera is automatic**, and calm by design (one zoom per action, never on a scroll). Turn it off with
  `follow: false`, or script it with `zooms`. Keep important callouts and labels above y 930 (the caption band): the
  camera never shows past the window's edge, so a box at the very bottom of the recording sits low on screen.
- **Never record real keys, tokens, emails or personal data** (docs/showing-real-computer-actions.md). capture.py
  refuses typed text and terminal output that look like a secret or a real email, and blurs every `redact` box; still
  look at every frame before committing, because the repo is public.
- **The narration may only point at what the camera has zoomed on** (or a callout has boxed): at rest a recording's
  body text is under the 26 px minimum, so a page at rest is a picture of a page, not something to read.
- **Sizes**: Cloudflare Pages takes at most 25 MB per file. A browser capture at 1920x1080 and CRF 23 runs about
  0.3-0.45 MB a second (the 19.4 s `_demo` site capture is 8.2 MB); keep each under a minute, or record at `"dpr": 1`.
  Everything a lesson declares loads before frame 0: keep a lesson's media under about 15 MB in all, and leave out shots
  no scene shows (docs/showing-real-computer-actions.md, File sizes).

### 3D shots (tools/blender_shot.py, SHOT)
A lesson can play short 3D shots rendered in Blender. Each shot is a Python script in the lesson,
`lessons/<slug>/blender/<shot>.py`, that builds its scene from nothing with the helpers in `tools/blender_shot.py`
(`bs.setup`, `bs.box`, `bs.material` with `K.C` names, `bs.bake` keyframes from a function of time, `bs.anchor`...)
and can read the course data (`bs.course()`), so it re-renders from the repo when the curriculum changes. When 3D
helps a conceptual lesson and when it is decoration, the helpers, the Blender MCP workflow, render times and sizes:
`docs/blender-shots.md`. Worked example: `lessons/_demo` scene 04 (`blender/course_map.py`).

```
python tools/blender_shot.py <lesson> <shot> --dry              build only, print where the anchors land (no GPU)
python tools/blender_shot.py <lesson> <shot> --preview          Workbench, half size, a contact sheet (no clip)
python tools/blender_shot.py <lesson> <shot> --frames 1,60,132  just those frames as stills (add --engine eevee)
python tools/blender_shot.py <lesson> <shot>                    the clip + anchors, prints the lesson.js entry
   options: --engine workbench|eevee  --size 1280x720  --fps 24  --samples N  --keep  --blend x.blend
```

Blender renders on the shared GPU: wrap every render in a gpu-queue lease
(`gpu.py run --est 3m --kind blender-render -- python tools/blender_shot.py ...`; the 5.5 s demo shot takes 1.5 to 2
minutes in EEVEE at 1280x720 and comes out at 1.1 MB). The tool runs
`blender.exe -b --factory-startup -P <shot>.py`, encodes the frames to the clip spec above (`media_util.encode`) at
`assets/video/<shot>.mp4`, and writes the shot's anchors to `scenes/00-shot-<shot>.js`, together with what the clip was
rendered from (`SHOTS[shot].source`: the course map's `mapHash` when the script read `bs.course()`, the SHA-1 of the
script and of the tool). `python tools/blender_shot.py <lesson> --stale` lists the shots whose clip no longer matches
their script or the course data, and render.py warns about them before it renders, so a curriculum change re-renders the
3D map too instead of showing the old one next to the new 2D map. Declare the clip like any video
(`videos: { course_map: 'assets/video/course_map.mp4' }`) and play it with `K.video`.

| call | notes |
|---|---|
| `SHOT(shot, anchor, mediaT, place)` | where a named 3D point of the shot (`bs.anchor` in its script) is on the canvas this frame: `{x, y, z, k, label}`, or null. `place` is what `K.video` returned for the same `mediaT`, so it follows `fit`, `crop`, `zoom` and `K.cam`; it snaps to the clip frame being shown. `z` is the distance from the camera, `k` the anchor's own 0..1 (e.g. how far a block has risen), `label` the text the script baked with it. `SHOTS[shot].anchors` lists the names |

```js
SCENE('04', (t, S) => {                        // the shot from [[map3d]], its district names as crisp canvas text
  K.bg();
  const mt = t - S.cue('map3d', 0.4), p = K.video('course_map', mt, 320, 146, 1280, 720, { r: 18, stroke: true });
  for (const n of Object.keys(SHOTS.course_map.anchors)) {
    const a = SHOT('course_map', n, mt, p);
    if (a && a.label) K.text(a.label, a.x, a.y + 10, { font: 'head', weight: 700, size: 30, color: K.C.head,
      align: 'center', alpha: K.clamp((a.k - 0.55) / 0.45), shadow: 14 });
  }
});
```

Rules: words never go in the 3D render (canvas text pinned with `SHOT`); a clip is fixed once rendered (re-render it when
`--stale` names it), so start it on a cue and keep it short (3 to 8 s); show a 1280x720 shot at 1280x720 for 1:1 pixels (render `--size 1920x1080`
to fill the screen); the final shot is always the script (a scene tweaked live through the Blender MCP is lost unless
its numbers go back into the script).

## Review stills (tools/stills.py)
`--from S --to S` limits the frames to a time window (lesson seconds); it combines with `--every` (the grid starts at `--from`), `--at` and `--scene`, and an empty window gets 9 evenly spaced frames. E.g. `python tools/stills.py <lesson> --from 41 --to 43 --every 0.25 --tag beat`.
