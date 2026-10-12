# 3D shots made in Blender

Since 2026-10-12 a lesson can include short 3D shots rendered in Blender (Aaron allowed Blender, through the MCP or
headless, for animation). A shot is **a Python script stored in the lesson** that builds its scene from nothing, so it
re-renders from the repo like every other part of a lesson: change the curriculum, the palette or the script, run one
command, and the clip, and the labels the scene pins on it, come out new.

```
lessons/<slug>/blender/<shot>.py          the shot: builds the scene, camera, lights, animation (committed)
lessons/<slug>/assets/video/<shot>.mp4    the rendered clip, to the course clip spec (committed, Git LFS)
lessons/<slug>/scenes/00-shot-<shot>.js   the shot's anchors (where named 3D points are on screen, every frame) and
                                          what the clip was rendered from (generated)
tools/blender_shot.py                     renders a shot headless, encodes it, writes the anchors, prints the lesson.js entry
```

Worked example: `lessons/_demo`, scene 04 (never published): `blender/course_map.py`, the six-district course map rising
as soft terraced blocks (one terrace per module, read from the course data), the garden path walked from Start to
Finish, the lantern string swinging over it with each lantern lighting as its district finishes rising, and a slow
camera push. The scene plays it with `K.video` in a calm frame and writes the district names over the blocks as canvas
text.

```
python tools/blender_shot.py _demo course_map --dry          # build only: where the anchors land on screen (no GPU)
python tools/blender_shot.py _demo course_map --preview      # Workbench, half size: a contact sheet in seconds
python tools/blender_shot.py _demo course_map --frames 1,60,132 --engine eevee   # a few final-look stills
python tools/blender_shot.py _demo course_map                # the clip, the anchors, the lesson.js entry
python tools/blender_shot.py _demo --stale                   # which clips no longer match their script or the course data
python tools/stills.py _demo --scene 04 --every 0.5          # how it sits in the lesson
```

## When 3D helps a conceptual lesson, and when it is decoration

The course is a map, not a manual (COURSE.md). The kit's flat drawings carry almost every idea; 3D earns its render
time only when depth, stacking or a physical arrangement IS the idea:

- **Layers and stacks**: the network stack, a container on an image on a kernel on hardware, a file system's folders
  inside folders, a model inside an app inside an agent. Lifting the layers apart in 3D shows "on top of" and "inside"
  literally.
- **Places and distance**: data centres, the edge, a request travelling across a globe, the course map as a place you
  walk. Perspective sells "far away" and "close to the user" better than a flat arrow.
- **One object seen from several sides**: a key and a lock, a server rack, the same file seen as bytes, as an icon and
  as a document.
- **A title or district establishing shot**: a few seconds that turn the map into a place, once per module at most.

It is decoration (skip it) when:

- the point is a word, a name or a sentence (3D text is soft and off-palette; the canvas draws words better),
- the drawing would be the same picture with perspective added,
- the motion has to follow narration timing closely: a clip is fixed once rendered, while a canvas scene moves on
  `S.cue()`; a 3D shot is a held exhibit (play it from a cue, keep it short),
- it would replace a real recording of a real screen (docs/showing-real-computer-actions.md): show the real thing.

Keep shots 3 to 8 seconds, one idea, calm first and last frames (scenes crossfade), no flashing, the camera slow
(COURSE.md motion rules apply to the clip too). The narration says what to look at.

## Writing a shot

The script runs inside Blender with `tools/blender_shot.py` importable as `blender_shot` (the helpers, `bs` below). Its
first call is `bs.setup()`; after that it only builds and animates. Rendering, encoding and the anchors are the tool's job.

```python
import math
import blender_shot as bs

S = bs.setup(seconds=5.5, fps=24, size=(1280, 720), engine='eevee', samples=48)   # these are the shot's own values
course = bs.course()                       # window.COURSE from engine/course.js: districts, modules, lessons
m = bs.material('block', bs.mix('tile', 'line2', 0.5), rough=0.7)                 # K.C names or hex, from engine/kit.js
b = bs.box('block', (2.6, 1.7, 0.4), (0, 0, 0), m, bevel=0.05)                    # origin on its base: scale z grows it
k = lambda t: bs.ease(t, 0.5, 0.6, 'out')                                         # K.io's curves: io out in sine back lin
bs.bake(b, 'scale', lambda t: (1, 1, max(0.001, k(t))))                           # keyframes from a function of time
bs.anchor('block', lambda t: (0, 0, 0.4 * k(t)), k=k, label='The Machine')        # a 3D point the scene can label
bs.light('POINT', (0, 1, 2.5), 30, color='head')
bs.camera((0, -9, 7), (0, 0, 0.3), lens=34)
```

| helper | does |
|---|---|
| `bs.setup(seconds, fps, size, engine, samples, world='page', bloom=True, view='Standard')` | empties the factory scene, sets frame range, size, colour management (Standard view, so a flat colour comes out as its K.C hex) and a world in `K.C.page`; returns the Shot `S`: `S.fps`, `S.frames`, `S.seconds`, `S.w`, `S.h`, `S.engine`, `S.C` (the palette), `S.f(t)` / `S.t(f)` |
| `bs.palette()` · `bs.course()` | `K.C` read from engine/kit.js · `window.COURSE` read from engine/course.js |
| `bs.rgb(c)` · `bs.mix(c1, c2, k)` | a K.C name or hex as linear RGBA (what materials take) · a colour between two (sRGB, like `K.mixColor`) |
| `bs.material(name, color, rough, emit, strength, metal, spec)` | Principled material; `emit` + `strength` for things that glow (also shown flat in Workbench) |
| `bs.box` `bs.cylinder` `bs.sphere` `bs.torus` `bs.curve` `bs.empty` | soft (bevelled) primitives built with bmesh, origin on the base so `scale.z` grows them; `curve(points, depth)` is a tube (a string, a path; animate `data.bevel_factor_end` to draw it on); `parent=` for rigs |
| `bs.camera(loc, target, lens)` · `bs.look(ob, target)` · `bs.light(kind, loc, energy, color, size, target, shadow)` | the camera (becomes the scene camera) · aim anything · POINT / AREA / SUN / SPOT |
| `bs.bake(target, path, fn, index=-1)` · `bs.socket(node_input, fn)` | keyframe a property at every frame from `fn(t)` (seconds): the shot is a pure function of time, like a canvas scene. Only frames where the value changes get a key. A curve's or light's own property is baked on `ob.data`; a material input with `socket` |
| `bs.ease(t, a, d, e)` · `bs.lerp` · `bs.rng(seed)` | the kit's easing curves · deterministic random (never `random.random()` or the clock) |
| `bs.anchor(name, point, k=None, label=None)` | a named point (`point(t)` -> world xyz, or an object) whose screen position goes into `scenes/00-shot-<shot>.js` every frame, with an optional 0..1 `k(t)` and a `label` baked alongside |

Rules:

- **Build from nothing.** No `.blend` is needed; geometry is built with bmesh, materials with nodes. A `.blend` in
  `assets/` is allowed only when a script cannot express it (a sculpted or downloaded model): load it from the script
  with `bpy.ops.wm.append` / `bpy.data.libraries.load`, keep it small (Git LFS, 25 MB rule) and its licence clear.
- **Data from the course, not constants.** A shot about the map reads `bs.course()` (districts in path order, their
  modules) and bakes the labels it used with its anchors. The tool records what each clip was rendered from in
  `SHOTS[shot].source`: `mapHash` (the course map's hash from engine/course.js, only when the script called
  `bs.course()`), `script` and `tool` (SHA-1 of the shot script and of blender_shot.py), the engine, Blender's version
  and the date. When curriculum.md changes and `course.py sync` rewrites engine/course.js, the shot is stale:
  `blender_shot.py <lesson> --stale` names it (exit 1) with the command to re-render it (inside a gpu-queue lease), and
  `render.py` warns before rendering a lesson whose shot is stale, so the lesson never shows the new 2D map next to the
  old 3D one. A changed shot script is stale too; a changed blender_shot.py alone is only noted (it rarely changes a
  picture). `stale_shots(lesson_dir)` in blender_shot.py is the same check for other tools (course.py sync can report
  it as a job). A clip rendered before 2026-10-12 has no source and counts as stale. Legacy lessons have no shots, so
  their videos never change.
- **Colours from `K.C`**, by name. The Standard view transform keeps a flat surface on its hex; lit surfaces are shades
  of it. Lights may be any colour (the moonlight in the demo is a cool blue-grey).
- **No 3D text.** Words go on the canvas, pinned to the shot with anchors (below): crisp, in the course fonts, at the
  course's minimum sizes, and translatable without a re-render.
- **Deterministic.** `bs.rng(seed)` for scatter and jitter; every animated value baked from `t`.

## In the lesson

`blender_shot.py` prints the `lesson.js` entry; the clip is a video like any other (engine/KIT.md, Media exhibits):

```js
LESSON({ ..., videos: { course_map: 'assets/video/course_map.mp4' } });

SCENE('04', (t, S) => {
  K.bg();
  const mt = t - S.cue('map3d', 0.4);                       // the shot's media time
  const p = K.video('course_map', mt, 320, 146, 1280, 720, { r: 18, stroke: true });
  for (const name of Object.keys(SHOTS.course_map.anchors)) {
    const a = SHOT('course_map', name, mt, p);              // {x, y, z, k, label} on the canvas, this frame
    if (a && a.label) K.text(a.label, a.x, a.y + 10, { font: 'head', size: 30, color: K.C.head, align: 'center',
                                                        alpha: K.clamp((a.k - 0.55) / 0.45), shadow: 14 });
  }
});
```

`SHOT(shot, anchor, mediaT, place)` uses the placement `K.video` returns (`place.at`), so it follows the clip through
`fit`, `crop`, `zoom` and `K.cam`; it snaps to the frame `K.video` is showing (no drift between label and picture).
Show a 1280x720 clip at 1280x720 (x 320, y 146 centres it under the badge band) for 1:1 pixels; at 1920 wide it is
upscaled 1.5x and visibly softer (render at `--size 1920x1080` if a shot must fill the screen; see the times below).

## Designing a shot with the Blender MCP

The Blender MCP (tools `mcp__Blender__*`, load them with ToolSearch) talks to a running Blender whose MCP add-on is
enabled and connected (it listens on localhost:9876; a call says "Cannot connect to Blender" otherwise). Use it to
**block out and preview** a shot interactively, never as the place the shot lives:

1. Open Blender, **File > New > General** (an empty file you do not mind losing: `bs.setup()` deletes every object in
   the scene), and start the add-on's server.
2. Run the shot script in that Blender with `mcp__Blender__execute_blender_code`:
   ```python
   import sys, importlib
   sys.path.insert(0, r'C:/Users/soulo/Organized/Personal/My Projects/Courses/The-hidden-curriculum/tools')
   import blender_shot; importlib.reload(blender_shot)
   p = r'C:/Users/soulo/Organized/Personal/My Projects/Courses/The-hidden-curriculum/lessons/_demo/blender/course_map.py'
   exec(compile(open(p, encoding='utf-8').read(), p, 'exec'), {'__name__': '__main__'})
   result = {'objects': len(bpy.data.objects)}
   ```
   (`bs.setup()` reads no command line there, so the script's own values apply.)
3. Look and adjust: `get_objects_summary` / `get_object_detail_summary` to inspect, `bpy.context.scene.frame_set(60)`
   to scrub, `get_screenshot_of_area_as_image('VIEW_3D')` for the viewport (set it to the camera view and Material
   Preview or Rendered shading first), `render_viewport_to_path` for a real render of the current frame.
4. Move the camera or a light by hand in Blender if that is quicker, then read the numbers back with
   `execute_blender_code` (`result = {'cam': list(bpy.data.objects['Camera'].location)}`) and **write them into the
   script**. Anything changed only in the live Blender is lost: the final shot is always the script, rendered by
   `blender_shot.py`, because that is what re-renders from the repo.

Without the add-on, the same loop runs headless: `--preview` and `--frames` render stills you can Read, and
`--blend shot.blend` saves the built scene so it can be opened in Blender. The `mcp__Blender__*_for_cli` tools run a
background Blender on a .blend file, but only when the MCP server has `BLENDER_PATH` set to blender.exe; on 2026-10-12
it was not ("Blender executable not found at 'blender'"), and the add-on was not connected either, so the demo shot
was designed headless: `--dry` to frame it (where the anchors land, no render), `--preview` and `--frames` stills to
judge the look, then `tools/stills.py` for the scene around it.

## GPU (shared with other sessions)

Workbench and EEVEE both render on the GPU, which other sessions share (ComfyUI, other renders). Load the `gpu-queue`
skill and wrap every render in a lease with an honest estimate (measured times below, plus 20%):

```
python ~/.claude/skills/gpu-queue/gpu.py run --est 3m --kind blender-render --label "<lesson> <shot>" -- python tools/blender_shot.py <lesson> <shot>
```

Run it in the background; `run` waits its turn, renders and releases even on failure. Never run Blender while another
session holds the GPU: on the 8 GB laptop GPU a Blender render next to a ComfyUI job can run out of memory.

## Measured on this machine (RTX 4070 Laptop 8 GB, Blender 5.2.2 LTS, 2026-10-12)

The demo shot, `course_map` (117 objects, 5.5 s, 132 frames at 24 fps), every run through `blender_shot.py`. "Blender"
is the whole Blender process: start-up, building the scene, the anchors and the frames.

| run | Blender | per frame | notes |
|---|---|---|---|
| `--dry` (build + anchors, no render) | about 2 s (2.0 and 2.2 s; the first runs of the day took 4.8 to 6.0 s) | none | no GPU: run it freely while framing |
| `--preview` (Workbench, 640x360, every 12th frame (`--every`): 12 frames) | 12.3 s (a first, cold run took 27.1 s) | 0.11 s | a cold GPU start makes the first frame take up to 12 s |
| Workbench, 1280x720, all 132 frames (stills) | 24.2 s | 0.16 s | first frame 1.4 s |
| **EEVEE, 1280x720, 48 samples, all 132 frames: the clip** | **86.6 s, 99.4 s and 100.0 s** (three runs) | **0.38 to 0.73 s** | first frame 1.6 to 28 s: EEVEE compiles its shaders on the first frame, longer after a material changes; plus 1.4 to 2.2 s to encode |
| EEVEE, 1920x1080, 48 samples, 12 frames (stills) | 12.1 s | 0.70 s | so a 1080p clip of this shot is about 100 to 120 s |

So a 5-second EEVEE shot is about 1.5 to 2 minutes on this GPU: lease `--est 3m`. A 1080p one, `--est 4m`. Workbench
is about four times faster but has no light from the lanterns (flat material colours, studio light): use it for
blocking, EEVEE for the clip. The 1080p clip time is an estimate from the 12 frames, not a measured clip.

| file | size |
|---|---|
| `assets/video/course_map.mp4`, 5.5 s, 1280x720, CRF 18 (to the clip spec) | 1.10 MB (about 0.2 MB a second: dark, slow motion compresses well) |
| `scenes/00-shot-course_map.js`, 8 anchors x 132 frames | 28 KB |
| `blender/course_map.py` | 12 KB (208 lines) |
| one EEVEE PNG frame, 1280x720 / 1920x1080 (temporary, deleted after encoding unless `--keep`) | 0.8 MB / 1.7 MB |

Cloudflare Pages' 25 MB per-file limit is far away for shots this length: by extrapolation from 0.2 MB a second at
720p, a 10-second 1080p shot would be about 5 MB (busier, brighter shots compress worse; `media_util.py check` says).

## How it works (for the next engineer)

- `blender_shot.py` runs `blender.exe -b --factory-startup --python-exit-code 1 --python-expr <put tools/ on sys.path>
  -P <shot>.py --python-expr "bs._render()" -- --out <tmp> [overrides]`. The shot script builds; `_render()` then sets
  the engine (Workbench: studio light, material colours, cavity, soft shadows; EEVEE: the shot's samples, shadows, no
  ray tracing, a compositor Bloom node, because EEVEE has had no bloom switch since 4.2), computes the anchors for
  every frame (`world_to_camera_view`), renders each frame to PNG and writes `meta.json` (timings, anchors).
- The frames go to a lossless intermediate (`libx264rgb -crf 0`) and through `media_util.encode` (CRF 18), so the clip
  meets the same spec as every other clip (H.264 High, yuv420p, BT.601 tagged smpte170m, GOP 12, no B-frames,
  +faststart, no audio, under 25 MB) and `media_util.py check` passes.
- Command-line `--engine`, `--size`, `--fps`, `--samples` override the script's `bs.setup()` values for experiments;
  a plain run uses the script's, so re-rendering reproduces the committed clip. `--preview` is half size, Workbench
  (unless `--engine`), every 12th frame (`--every N`) and a contact sheet in `out/blender/<shot>-preview/`; nothing in
  `assets/` changes. `--frames` renders stills only. `--keep` keeps the PNG frames of a full render.
- The anchors file defines `window.SHOTS[<shot>]` (fps, size, labels, per-frame `[x, y, depth, k]` in clip pixels, and
  `source`: what the clip was rendered from) and `SHOT()`; it sits in `scenes/` so `scenes.js` loads it before the
  scenes (`common.sync_scenes`). It is written for every rendered shot, with no anchors too, because it carries the
  source. `bs.course()` notes the map hash it read; `_render()` puts it in meta.json and the tool writes it to `source`.
- `--dry` stops after the anchors: it prints where each anchor lands on the first, middle and last frame, so framing
  and label collisions can be fixed before any render (that is how the demo's near-row labels moved to the foot of
  their blocks: a far block's top sat right behind a near block's top on screen).
- Choices the demo makes on purpose: growing objects scale from 0.001, not 0, and are hidden (`hide_render` baked)
  until they start, so no degenerate bevel geometry is ever rendered; the lantern parts have `visible_shadow = False`
  so the point light inside each lantern reaches the map; Blender 5's compositor is a node group
  (`scene.compositing_node_group` with a Group Output node), not `scene.use_nodes`; the camera's rotation is baked
  from a look-at point every frame, so a push is two eased positions (camera and aim), never hand-keyed angles.
