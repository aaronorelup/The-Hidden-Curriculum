"""blender_shot.py: 3D shots for a lesson, built in Blender from a script kept in the lesson, so any shot can be
re-rendered from the repo (docs/blender-shots.md; engine/KIT.md "3D shots").

usage:
  python tools/blender_shot.py <lesson> <shot>                     render, encode, print the lesson.js entry
  python tools/blender_shot.py <lesson> <shot> --preview           quick look: half size, Workbench, a contact sheet
  python tools/blender_shot.py <lesson> <shot> --frames 1,60,132   just these frames, as review stills + sheet
  python tools/blender_shot.py <lesson> <shot> --dry              build only: where the anchors land (no GPU, no render)
  python tools/blender_shot.py <lesson> --list                     the lesson's shot scripts and their clips
  python tools/blender_shot.py <lesson> --stale                    which clips no longer match their script or the
                                                                   course data (exit 1 if any); render.py warns too
  options: --engine workbench|eevee  --size 1280x720  --fps 24  --samples 32  --keep (keep the PNG frames)
           --blend out.blend (also save the built scene, to open in Blender or with the Blender MCP)

A shot is lessons/<slug>/blender/<shot>.py. Blender runs it headless,
  blender.exe -b --factory-startup -P <shot>.py -- --out <tmp> ...
with this file importable as `blender_shot` (the in-Blender helpers below). The script builds its scene from nothing,
calls bs.setup() first (its declared engine, size, fps and length are what a re-render uses; command-line flags
override them for experiments only), animates with bs.bake() (values computed from the frame's time: a pure function
of time, like a canvas scene; bs.rng() for randomness) and may register bs.anchor()s. The tool renders every frame to
PNG, encodes them to the course clip spec (tools/media_util.py: H.264 High, BT.601, GOP 12, no B-frames, no audio)
at lessons/<slug>/assets/video/<shot>.mp4, writes the anchors' screen positions per frame to
lessons/<slug>/scenes/00-shot-<shot>.js (window.SHOTS + SHOT(), so a scene can put crisp canvas labels on moving 3D
objects), and prints the lesson.js entry plus the measured render time and file size.

What a clip was rendered from is recorded with its anchors (SHOTS[shot].source): the course map's hash
(COURSE.mapHash of engine/course.js) when the script read bs.course(), and the SHA-1 of the shot script and of this
tool. `--stale` (and render.py, and tools/course.py sync through stale_shots()) compare them with the files now, so
a shot built from the course data is re-rendered when the curriculum changes instead of showing the old map.

Blender uses the GPU (Workbench and EEVEE both do): reserve a slot first, e.g.
  python ~/.claude/skills/gpu-queue/gpu.py run --est 3m --kind blender-render --label "..." -- python tools/blender_shot.py ...
"""
import json
import math
import os
import pathlib
import sys

BLENDER = os.environ.get('BLENDER_EXE', r'C:/Program Files/Blender Foundation/Blender 5.2/blender.exe')
TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
DEFAULTS = {'engine': 'eevee', 'size': (1280, 720), 'fps': 24, 'seconds': 5.0, 'samples': 32}


# ===================================================================== in Blender: the helpers a shot script uses
class Shot:
    """what bs.setup() returns: the shot's clock, palette and data. Times are seconds from the clip's first frame."""

    def __init__(self, a):
        self.__dict__.update(a)

    def f(self, t):
        """the frame number shown at time t (the one K.video shows at that media time)"""
        return self.frame_start + int(math.floor(t * self.fps + 1e-6))

    def t(self, f):
        """the time of frame f (seconds; frame_start is 0.0)"""
        return (f - self.frame_start) / self.fps

    def rgb(self, c, a=1.0):
        return rgb(c, a)


_S = None            # the current Shot
_ANCHORS = {}        # name -> (point(t) -> (x, y, z), k(t) -> 0..1 or None)
_CFG = {}            # what setup() resolved, read back by _render()
_LABELS = {}         # anchor name -> label text
_USED = {}           # what the script read: {'mapHash': ...} once it called course()


def _argv():
    """the arguments after '--' on Blender's command line"""
    import argparse
    rest = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    ap = argparse.ArgumentParser(prog='blender_shot (in Blender)')
    ap.add_argument('--out')
    ap.add_argument('--engine')
    ap.add_argument('--size')
    ap.add_argument('--fps', type=float)
    ap.add_argument('--samples', type=int)
    ap.add_argument('--frames')
    ap.add_argument('--every', type=int)
    ap.add_argument('--dry', action='store_true')
    ap.add_argument('--preview', action='store_true')
    ap.add_argument('--blend')
    ap.add_argument('--lesson')
    ap.add_argument('--shot')
    return ap.parse_known_args(rest)[0]


def palette():
    """K.C from engine/kit.js: {name: '#rrggbb'}. The Tea House night palette, read from the engine so a 3D shot
    and the canvas scenes around it never drift apart."""
    import re
    src = (ROOT / 'engine' / 'kit.js').read_text(encoding='utf-8')
    m = re.search(r'const C = \{(.*?)\};', src, re.S)
    return dict(re.findall(r"(\w+):\s*'(#[0-9A-Fa-f]{6})'", m.group(1) if m else ''))


def course():
    """window.COURSE from engine/course.js (written by tools/course.py sync from curriculum.md): districts, modules,
    lessons. A shot drawn from it follows the curriculum when it is re-rendered."""
    data = _course_data()
    _USED['mapHash'] = data.get('mapHash')          # the clip now depends on the course data: recorded in its source
    return data


def _course_data():
    src = (ROOT / 'engine' / 'course.js').read_text(encoding='utf-8')
    body = src[src.index('=', src.index('window.COURSE')) + 1:].strip().rstrip(';')
    return json.loads(body)


def current_map_hash():
    """COURSE.mapHash of engine/course.js now (None if it cannot be read)"""
    try:
        return _course_data().get('mapHash')
    except (OSError, ValueError):
        return None


def sha1(path):
    import hashlib
    return hashlib.sha1(pathlib.Path(path).read_bytes()).hexdigest()


def shot_data(L, shot):
    """SHOTS[shot] as recorded in lessons/<slug>/scenes/00-shot-<shot>.js, or None"""
    import re
    f = pathlib.Path(L) / 'scenes' / f'00-shot-{shot}.js'
    if not f.exists():
        return None
    m = re.search(r'^SHOTS\[(".*?")\] = (\{.*\});\s*$', f.read_text(encoding='utf-8'), re.M)
    try:
        return json.loads(m.group(2)) if m else None
    except ValueError:
        return None


def stale_shots(L, map_hash=None):
    """every shot of lesson folder L whose clip no longer matches what it would render from now:
    [{'shot', 'reasons': [...], 'notes': [...], 'course': bool (the script reads the course data), 'cmd'}].
    Reasons: no clip, no recorded source (rendered before 2026-10-12), the script changed, the course map changed
    (only for a script that called bs.course()). A changed blender_shot.py alone is not a reason (it rarely changes
    a picture); it goes in 'notes'. Used by --stale, render.py (a warning) and tools/course.py sync (a 'blender' job).
    Legacy lessons have no blender/ folder, so they never get one."""
    L = pathlib.Path(L)
    out = []
    map_hash = map_hash or current_map_hash()
    for script in sorted((L / 'blender').glob('*.py')) if (L / 'blender').is_dir() else []:
        shot, why, notes = script.stem, [], []
        clip = L / 'assets' / 'video' / f'{shot}.mp4'
        src = (shot_data(L, shot) or {}).get('source') or {}
        uses = bool(src.get('mapHash')) or (not src and 'course()' in script.read_text(encoding='utf-8'))
        if not clip.exists():
            why.append('no clip yet')
        elif not src:
            why.append('no record of what it was rendered from (rendered before blender_shot.py kept one)')
        else:
            if src.get('script') != sha1(script):
                why.append(f'blender/{shot}.py changed since the clip was rendered')
            if src.get('mapHash') and map_hash and src['mapHash'] != map_hash:
                why.append(f'the course map changed (rendered from map {src["mapHash"]}, now {map_hash})')
            if src.get('tool') and src['tool'] != sha1(__file__):
                notes.append('tools/blender_shot.py changed since (usually no visible difference)')
        if why:
            out.append({'shot': shot, 'reasons': why, 'notes': notes, 'course': uses,
                        'cmd': f'python tools/blender_shot.py {L.name} {shot}'})
    return out


def _lin(v):
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def rgb(c, a=1.0):
    """a K.C name or '#rrggbb' -> linear RGBA, which Blender materials take (the Standard view transform turns it
    back into the exact sRGB colour on a flat, unlit surface)"""
    hx = _S.C.get(c, c) if _S else c
    hx = hx.lstrip('#')
    return tuple(_lin(int(hx[i:i + 2], 16) / 255) for i in (0, 2, 4)) + (a,)


def mix(c1, c2, k):
    """a colour between two K.C names / hex colours (in sRGB, like K.mixColor), as '#rrggbb'"""
    h1, h2 = (_S.C.get(c, c).lstrip('#') for c in (c1, c2))
    return '#' + ''.join(f'{round(int(h1[i:i + 2], 16) * (1 - k) + int(h2[i:i + 2], 16) * k):02x}' for i in (0, 2, 4))


def ease(t, a, d=0.6, e='io'):
    """0 -> 1 eased across [a, a + d], the same curves as K.io (io, out, in, sine, back, lin)"""
    if d <= 0:
        return 1.0 if t >= a else 0.0
    x = min(1.0, max(0.0, (t - a) / d))
    if e == 'lin':
        return x
    if e == 'in':
        return x ** 3
    if e == 'out':
        return 1 - (1 - x) ** 3
    if e == 'sine':
        return 0.5 - math.cos(math.pi * x) / 2
    if e == 'back':
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def lerp(a, b, k):
    return a + (b - a) * k


def rng(seed):
    """deterministic random() (the same numbers on every render)"""
    import random
    return random.Random(seed).random


def setup(seconds=None, fps=None, size=None, engine=None, samples=None, world='page', bloom=True, view='Standard'):
    """start from an empty scene. The script's values are the shot's own (a plain re-render reproduces the committed
    clip); command-line flags override them. Returns the Shot."""
    global _S
    import bpy
    a = _argv()
    fps = a.fps or fps or DEFAULTS['fps']
    size = tuple(int(n) for n in a.size.lower().split('x')) if a.size else tuple(size or DEFAULTS['size'])
    engine = (a.engine or engine or DEFAULTS['engine']).lower()
    if a.preview and not a.engine:
        engine = 'workbench'
    samples = a.samples or samples or DEFAULTS['samples']
    seconds = seconds or DEFAULTS['seconds']
    frames = int(round(seconds * fps))
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.curves):
        for d in list(coll):
            coll.remove(d)
    sc = bpy.context.scene
    sc.render.fps, sc.render.fps_base = int(round(fps)), int(round(fps)) / fps
    sc.frame_start, sc.frame_end = 1, frames
    sc.render.resolution_x, sc.render.resolution_y = size
    sc.render.resolution_percentage = 50 if a.preview else 100
    sc.render.image_settings.file_format = 'PNG'
    sc.render.image_settings.color_mode = 'RGB'
    sc.render.film_transparent = False
    sc.view_settings.view_transform = view
    sc.view_settings.look = 'None'
    sc.view_settings.exposure = 0.0
    sc.view_settings.gamma = 1.0
    _S = Shot({'fps': fps, 'frames': frames, 'frame_start': 1, 'seconds': frames / fps, 'w': size[0], 'h': size[1],
               'engine': engine, 'samples': samples, 'preview': a.preview, 'C': palette(), 'root': ROOT,
               'lesson': pathlib.Path(a.lesson) if a.lesson else None, 'scene': sc})
    w = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
    sc.world = w
    w.color = rgb(world)[:3]                       # Workbench draws this as the background
    if hasattr(w, 'use_nodes') and not w.node_tree:
        w.use_nodes = True
    bg = w.node_tree.nodes.get('Background') if w.node_tree else None
    if bg:
        bg.inputs['Color'].default_value = rgb(world)
        bg.inputs['Strength'].default_value = 1.0
    _CFG.update(out=a.out, frames_arg=a.frames, every=a.every, dry=a.dry, blend=a.blend, bloom=bloom, view=view)
    _ANCHORS.clear()
    _LABELS.clear()
    return _S


def material(name, color, rough=0.75, emit=None, strength=0.0, metal=0.0, spec=0.3):
    """a Principled material; `color` / `emit` are K.C names or hex. diffuse_color is what Workbench shows."""
    import bpy
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    if hasattr(m, 'use_nodes') and not m.node_tree:
        m.use_nodes = True
    m.diffuse_color = rgb(emit if (emit and strength > 0 and _S.engine == 'workbench') else color)
    m.roughness = rough
    p = m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value = rgb(color)
    p.inputs['Roughness'].default_value = rough
    p.inputs['Metallic'].default_value = metal
    if 'Specular IOR Level' in p.inputs:
        p.inputs['Specular IOR Level'].default_value = spec
    if emit:
        p.inputs['Emission Color'].default_value = rgb(emit)
        p.inputs['Emission Strength'].default_value = strength
    return m


def _obj(name, data, loc=(0, 0, 0), mat=None, parent=None):
    import bpy
    ob = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    if mat is not None and hasattr(data, 'materials'):
        data.materials.append(mat)
    if parent is not None:
        ob.parent = parent
    return ob


def box(name, size, loc=(0, 0, 0), mat=None, bevel=0.05, segments=3, base=True, parent=None):
    """a soft (bevelled) box. base=True puts its origin on the bottom face, so scale.z grows it upward."""
    import bmesh
    import bpy
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x *= size[0]
        v.co.y *= size[1]
        v.co.z = v.co.z * size[2] + (size[2] / 2 if base else 0)
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, loc, mat, parent)
    if bevel:
        b = ob.modifiers.new('Bevel', 'BEVEL')
        b.width, b.segments, b.limit_method = bevel, segments, 'ANGLE'
        b.harden_normals = False
    _smooth(ob)
    return ob


def cylinder(name, r, h, loc=(0, 0, 0), mat=None, verts=48, bevel=0.0, base=True, parent=None):
    import bmesh
    import bpy
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=verts, radius1=r, radius2=r, depth=h)
    if base:
        for v in bm.verts:
            v.co.z += h / 2
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, loc, mat, parent)
    if bevel:
        b = ob.modifiers.new('Bevel', 'BEVEL')
        b.width, b.segments, b.limit_method = bevel, 3, 'ANGLE'
    _smooth(ob)
    return ob


def sphere(name, r, loc=(0, 0, 0), mat=None, scale=(1, 1, 1), segments=32, rings=16, parent=None):
    import bmesh
    import bpy
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segments, v_segments=rings, radius=r)
    for v in bm.verts:
        v.co.x *= scale[0]
        v.co.y *= scale[1]
        v.co.z *= scale[2]
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, loc, mat, parent)
    for p in me.polygons:
        p.use_smooth = True
    return ob


def torus(name, r, thick, loc=(0, 0, 0), mat=None, parent=None, segments=40):
    """a thin ring in the XY plane (a lantern rib)"""
    import bmesh
    import bpy
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    ring = []
    for i in range(segments):
        a = 2 * math.pi * i / segments
        c = (r * math.cos(a), r * math.sin(a))
        ring.append([bm.verts.new((c[0] + thick * math.cos(a) * math.cos(b), c[1] + thick * math.sin(a) * math.cos(b),
                                   thick * math.sin(b))) for b in (2 * math.pi * j / 8 for j in range(8))])
    for i in range(segments):
        r0, r1 = ring[i], ring[(i + 1) % segments]
        for j in range(8):
            bm.faces.new((r0[j], r1[j], r1[(j + 1) % 8], r0[(j + 1) % 8]))
    bm.to_mesh(me)
    bm.free()
    ob = _obj(name, me, loc, mat, parent)
    for p in me.polygons:
        p.use_smooth = True
    return ob


def _smooth(ob):
    for p in ob.data.polygons:
        p.use_smooth = True
    if hasattr(ob.data, 'set_sharp_from_angle'):
        ob.data.set_sharp_from_angle(angle=math.radians(35))


def curve(name, points, depth=0.02, mat=None, smooth=True, parent=None):
    """a tube through 3D points (a string, a path); animate data.bevel_factor_end 0..1 to draw it on"""
    import bpy
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    cu.bevel_depth, cu.bevel_resolution = depth, 3
    cu.use_fill_caps = True
    sp = cu.splines.new('NURBS' if smooth else 'POLY')
    sp.points.add(len(points) - 1)
    for p, co in zip(sp.points, points):
        p.co = (co[0], co[1], co[2], 1.0)
    if smooth:
        sp.use_endpoint_u, sp.order_u = True, min(4, len(points))
    cu.bevel_factor_mapping_end = 'SPLINE'
    return _obj(name, cu, (0, 0, 0), mat, parent)


def empty(name, loc=(0, 0, 0), parent=None):
    return _obj(name, None, loc, None, parent)


def camera(loc, target, lens=35.0, name='Camera'):
    import bpy
    cam = bpy.data.cameras.new(name)
    cam.lens = lens
    cam.sensor_width = 36
    cam.clip_start, cam.clip_end = 0.05, 200
    ob = _obj(name, cam, loc)
    bpy.context.scene.camera = ob
    look(ob, target)
    return ob


def look(ob, target, roll=0.0):
    """point an object's -Z (a camera, a spot) at a target point"""
    from mathutils import Vector
    d = Vector(target) - Vector(ob.location)
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    ob.rotation_euler.rotate_axis('Z', roll)


def light(kind, loc, energy, color='strong', size=0.25, name=None, target=None, shadow=True):
    """POINT / AREA / SUN / SPOT; energy in Watts (W/m^2 for a sun)"""
    import bpy
    lt = bpy.data.lights.new(name or kind.title(), kind.upper())
    lt.energy = energy
    lt.color = rgb(color)[:3]
    if hasattr(lt, 'shadow_soft_size'):
        lt.shadow_soft_size = size
    if kind.upper() == 'AREA':
        lt.size = size
    if hasattr(lt, 'use_shadow'):
        lt.use_shadow = shadow
    ob = _obj(name or kind.title(), lt, loc)
    if target is not None:
        look(ob, target)
    return ob


def bake(target, path, fn, index=-1):
    """keyframe target.<path> at every frame from fn(t) (t = the frame's time in seconds), a pure function of time.
    Only the frames where the value changes get a key, so a held value stays flat. The path lives on target's own
    datablock: a curve's bevel_factor_end is bake(ob.data, 'bevel_factor_end', fn), a light's energy
    bake(ob.data, 'energy', fn), a node socket bake(node.inputs['Emission Strength'], 'default_value', fn)."""
    fr = list(range(_S.frame_start, _S.frame_start + _S.frames))
    vals = [fn(_S.t(f)) for f in fr]
    head, _, attr = path.rpartition('.')
    owner = target.path_resolve(head) if head else target
    for i, (f, v) in enumerate(zip(fr, vals)):
        if 0 < i < len(vals) - 1 and v == vals[i - 1] and v == vals[i + 1]:
            continue
        if index >= 0:
            getattr(owner, attr)[index] = v
            target.keyframe_insert(path, index=index, frame=f)
        else:
            setattr(owner, attr, v)
            target.keyframe_insert(path, frame=f)


def socket(node_input, fn):
    """keyframe a node socket's default_value from fn(t) (an emission strength, a colour)"""
    bake(node_input, 'default_value', fn)


def anchor(name, point, k=None, label=None):
    """a named 3D point whose screen position goes into scenes/00-shot-<shot>.js every frame. point(t) -> (x, y, z)
    world, or an object (its world origin); k(t) -> 0..1 (optional) travels with it, e.g. how far a block has risen,
    so a canvas label can fade in with the 3D motion; label is text the scene may draw there (baked with the clip, so
    a label and the picture always come from the same data)"""
    _ANCHORS[name] = (point, k)
    if label is not None:
        _LABELS[name] = label


def _track():
    import bpy
    from bpy_extras.object_utils import world_to_camera_view
    from mathutils import Vector
    sc, cam = bpy.context.scene, bpy.context.scene.camera
    out = {n: [] for n in _ANCHORS}
    for f in range(_S.frame_start, _S.frame_start + _S.frames):
        sc.frame_set(f)
        t = _S.t(f)
        for n, (pt, k) in _ANCHORS.items():
            co = pt.matrix_world.translation.copy() if hasattr(pt, 'matrix_world') else Vector(pt(t))
            v = world_to_camera_view(sc, cam, co)
            row = [round(v.x * _S.w, 1), round((1 - v.y) * _S.h, 1), round(v.z, 3)]
            if k is not None:
                row.append(round(float(k(t)), 3))
            out[n].append(row)
    sc.frame_set(_S.frame_start)
    return out


def _engine():
    import bpy
    sc = bpy.context.scene
    if _S.engine == 'workbench':
        sc.render.engine = 'BLENDER_WORKBENCH'
        sh = sc.display.shading
        sh.light, sh.color_type = 'STUDIO', 'MATERIAL'
        sh.show_shadows, sh.shadow_intensity = True, 0.35
        sh.show_cavity, sh.cavity_type = True, 'WORLD'
        sh.background_type = 'WORLD'
        sc.display.render_aa = '8' if not _S.preview else '5'
    elif _S.engine == 'eevee':
        sc.render.engine = 'BLENDER_EEVEE'
        ev = sc.eevee
        ev.taa_render_samples = 8 if _S.preview else _S.samples
        ev.use_shadows = True
        if hasattr(ev, 'use_raytracing'):
            ev.use_raytracing = False
        if _CFG.get('bloom'):
            _bloom(sc)
    else:
        raise SystemExit(f'unknown engine {_S.engine!r} (workbench | eevee)')


def _bloom(sc):
    """EEVEE has no bloom switch since 4.2: a compositor Glare (Bloom) node does it"""
    import bpy
    ng = bpy.data.node_groups.new('Shot compositor', 'CompositorNodeTree')
    ng.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
    rl, gl, out = ng.nodes.new('CompositorNodeRLayers'), ng.nodes.new('CompositorNodeGlare'), ng.nodes.new('NodeGroupOutput')
    gl.inputs['Type'].default_value = 'Bloom'
    gl.inputs['Highlights Threshold'].default_value = 0.9
    gl.inputs['Strength'].default_value = 0.6
    gl.inputs['Size'].default_value = 0.6
    ng.links.new(rl.outputs['Image'], gl.inputs['Image'])
    ng.links.new(gl.outputs['Image'], out.inputs[0])
    sc.compositing_node_group = ng
    sc.render.use_compositing = True


def _render():
    """runs after the shot script (the tool's last --python-expr): engine settings, anchors, frames, meta.json"""
    import time
    import bpy
    if _S is None:
        raise SystemExit('the shot script never called bs.setup()')
    out = pathlib.Path(_CFG['out'])
    out.mkdir(parents=True, exist_ok=True)
    _engine()
    sc = bpy.context.scene
    if _CFG.get('blend'):
        bpy.ops.wm.save_as_mainfile(filepath=str(pathlib.Path(_CFG['blend']).resolve()), copy=True)
    track = _track() if _ANCHORS else {}
    first, last = _S.frame_start, _S.frame_start + _S.frames - 1
    want = list(range(first, last + 1))
    if _CFG.get('frames_arg'):
        want = sorted({max(first, min(last, int(x))) for x in _CFG['frames_arg'].split(',') if x.strip()})
    elif _CFG.get('every'):
        want = sorted(set(range(first, last + 1, _CFG['every'])) | {last})
    if _CFG.get('dry'):
        want = []
    times, t_all = [], time.perf_counter()
    for f in want:
        sc.frame_set(f)
        sc.render.filepath = str(out / f'f_{f:04d}.png')
        t0 = time.perf_counter()
        bpy.ops.render.render(write_still=True)
        times.append(time.perf_counter() - t0)
        print(f'[shot] frame {f} {times[-1]:.2f}s', flush=True)
    meta = {'blender': bpy.app.version_string, 'engine': _S.engine, 'w': _S.w, 'h': _S.h, 'fps': _S.fps,
            'frames': _S.frames, 'frame_start': _S.frame_start, 'rendered': list(want), 'samples': _S.samples,
            'preview': _S.preview, 'render_s': round(time.perf_counter() - t_all, 2),
            'first_frame_s': round(times[0], 2) if times else None,
            'per_frame_s': round(sum(times[1:]) / max(1, len(times) - 1), 3) if len(times) > 1 else None,
            'track': track, 'labels': dict(_LABELS), 'mapHash': _USED.get('mapHash')}
    (out / 'meta.json').write_text(json.dumps(meta), encoding='utf-8')


# ===================================================================== outside Blender: the command line
TRACK_JS = '''// generated by tools/blender_shot.py from blender/{shot}.py; do not edit (re-run the tool)
// SHOT('{shot}', anchor, mediaT, place): where a 3D point is on the canvas this frame. place is what K.video returns,
// mediaT the same media time given to K.video. Returns {{x, y, z, k, label}} (z: distance from the camera; k: the
// anchor's own 0..1, e.g. how far a block has risen; label: the text baked with it) or null. Anchors: {names}
window.SHOTS = window.SHOTS || {{}};
SHOTS[{shot_json}] = {data};
window.SHOT = window.SHOT || function (shot, name, mediaT, place) {{
  const s = window.SHOTS[shot], a = s && s.anchors[name];
  if (!a || !place) return null;
  const i = Math.max(0, Math.min(a.length - 1, Math.floor(mediaT * s.fps + 1e-6))), r = a[i];
  const p = place.at ? place.at(r[0], r[1]) : [place.x + r[0] * place.w / s.w, place.y + r[1] * place.h / s.h];
  return {{ x: p[0], y: p[1], z: r[2], k: r.length > 3 ? r[3] : 1, label: (s.labels || {{}})[name] }};
}};
'''


def _sheet(frames, dst, cols=4, label=None):
    from PIL import Image, ImageDraw
    ims = [Image.open(p).convert('RGB') for p in frames]
    if not ims:
        return None
    w, h = ims[0].size
    tw = 480
    th = round(h * tw / w)
    rows = math.ceil(len(ims) / cols)
    sheet = Image.new('RGB', (cols * tw + (cols + 1) * 8, rows * (th + 30) + 8), (16, 18, 32))
    d = ImageDraw.Draw(sheet)
    for i, (im, p) in enumerate(zip(ims, frames)):
        x, y = 8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 30)
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, y))
        d.text((x + 4, y + th + 6), (label or '') + pathlib.Path(p).stem, fill=(240, 192, 106))
    sheet.save(dst, quality=90)
    return dst


def main():
    import argparse
    import shutil
    import subprocess
    import tempfile
    import time
    sys.path.insert(0, str(TOOLS))
    from common import lesson_dir, sync_scenes  # noqa: E402
    import media_util  # noqa: E402

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('lesson')
    ap.add_argument('shot', nargs='?')
    ap.add_argument('--engine', choices=['workbench', 'eevee'])
    ap.add_argument('--size', help='WxH, e.g. 1280x720 (default: the shot script\'s own)')
    ap.add_argument('--fps', type=float)
    ap.add_argument('--samples', type=int, help='EEVEE samples per pixel (default: the script\'s, else 32)')
    ap.add_argument('--preview', action='store_true', help='half size, Workbench unless --engine, a contact sheet; no clip')
    ap.add_argument('--frames', help='comma list of frames to render as stills (no clip), e.g. 1,60,132')
    ap.add_argument('--every', type=int, default=12, help='with --preview: one frame in N (default 12)')
    ap.add_argument('--keep', action='store_true', help='keep the PNG frames (out/blender/<shot>/)')
    ap.add_argument('--blend', help='also save the built scene as this .blend (to inspect it in Blender)')
    ap.add_argument('--dry', action='store_true', help='build the scene and print the anchors on screen; render nothing (no GPU)')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--stale', action='store_true', help='list the shots whose clip no longer matches its script or the course data')
    a = ap.parse_args()
    L = lesson_dir(a.lesson)
    if a.stale:
        st = stale_shots(L)
        for x in st:
            print(f'{x["shot"]}: STALE: {"; ".join(x["reasons"])}' + (' [reads the course data]' if x['course'] else ''))
            print(f'  re-render: {x["cmd"]}  (GPU: inside a gpu-queue lease)')
        if not st:
            print('every shot matches its script and the course data')
        sys.exit(1 if st else 0)
    if a.list or not a.shot:
        for p in sorted((L / 'blender').glob('*.py')):
            clip = L / 'assets' / 'video' / f'{p.stem}.mp4'
            print(f'{p.stem:24} {"assets/video/" + clip.name + f" ({clip.stat().st_size / 1e6:.2f} MB)" if clip.exists() else "(not rendered)"}')
        return
    script = L / 'blender' / f'{a.shot}.py'
    if not script.exists():
        raise SystemExit(f'no shot script {script}')
    if not pathlib.Path(BLENDER).exists():
        raise SystemExit(f'Blender not found at {BLENDER} (set BLENDER_EXE)')
    stills = bool(a.preview or a.frames or a.dry)
    review = L / 'out' / 'blender' / (f'{a.shot}-dry' if a.dry else f'{a.shot}-preview' if a.preview else
                                      f'{a.shot}-frames' if a.frames else a.shot)
    if stills or a.keep:
        shutil.rmtree(review, ignore_errors=True)
        work = review
    else:
        work = pathlib.Path(tempfile.mkdtemp(prefix=f'shot-{a.shot}-'))
    pass_args = ['--out', str(work), '--lesson', str(L), '--shot', a.shot]
    for k in ('engine', 'size', 'fps', 'samples', 'blend'):
        if getattr(a, k):
            v = getattr(a, k)
            pass_args += [f'--{k}', str(pathlib.Path(v).resolve()) if k == 'blend' else str(v)]
    if a.preview:
        pass_args.append('--preview')
    if a.dry:
        pass_args.append('--dry')
    if a.frames:
        pass_args += ['--frames', a.frames]
    if a.preview and not a.frames:
        pass_args += ['--every', str(a.every)]
    prelude = f'import sys; sys.path.insert(0, {str(TOOLS)!r}); import blender_shot'
    cmd = [BLENDER, '-b', '--factory-startup', '--python-exit-code', '1', '--python-expr', prelude,
           '-P', str(script), '--python-expr', 'import blender_shot as bs; bs._render()', '--', *pass_args]
    print(f'blender: {script.relative_to(ROOT)} -> {work}', flush=True)
    t0 = time.perf_counter()
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    wall = time.perf_counter() - t0
    log = r.stdout + r.stderr
    if r.returncode or not (work / 'meta.json').exists():
        tail = '\n'.join(ln for ln in log.splitlines() if ln.strip())[-4000:]
        raise SystemExit(f'Blender failed (exit {r.returncode}):\n{tail}')
    meta = json.loads((work / 'meta.json').read_text(encoding='utf-8'))
    if a.dry:
        n = meta['frames']
        print(f'built in {wall:.1f} s: {n} frames at {meta["fps"]:g} fps, {meta["w"]}x{meta["h"]}; anchors (clip px x, y; k):')
        for name, rows in meta['track'].items():
            cols = '   '.join(f'f{meta["frame_start"] + i}: {r[0]:.0f}, {r[1]:.0f}' + (f'; {r[3]:.2f}' if len(r) > 3 else '')
                           for i, r in ((0, rows[0]), (n // 2, rows[n // 2]), (n - 1, rows[-1])))
            print(f'  {name:24} {cols}')
        return
    pngs = sorted(work.glob('f_*.png'))
    print(f'rendered {len(pngs)} frames with {meta["engine"]} at {meta["w"]}x{meta["h"]} '
          f'({"half size, " if meta["preview"] else ""}{meta["fps"]:g} fps): Blender {wall:.1f} s wall, '
          f'render {meta["render_s"]} s, first frame {meta["first_frame_s"]} s, then {meta["per_frame_s"]} s/frame')
    if stills:
        sheet = _sheet(pngs, review / 'sheet.jpg', label=f'{a.shot} ')
        print(f'stills: {review}\nsheet: {sheet}')
        return
    tracks = meta.pop('track', {})
    raw = work / 'frames.mkv'
    media_util.run([media_util.ffmpeg(), '-v', 'error', '-y', '-framerate', f'{meta["fps"]:g}', '-start_number',
                    str(meta['frame_start']), '-i', str(work / 'f_%04d.png'), '-c:v', 'libx264rgb', '-crf', '0',
                    '-preset', 'ultrafast', str(raw)])
    dst = L / 'assets' / 'video' / f'{a.shot}.mp4'
    problems = media_util.encode(raw, dst, fps=meta['fps'], crf=18)
    if not a.keep:
        shutil.rmtree(work, ignore_errors=True)
    trk = L / 'scenes' / f'00-shot-{a.shot}.js'
    # always written, even with no anchors: it also records what the clip was rendered from (stale_shots)
    w, h = meta['w'], meta['h']
    data = {'fps': meta['fps'], 'w': w, 'h': h, 'frames': meta['frames'], 'labels': meta.get('labels', {}),
            'anchors': tracks,
            'source': {'mapHash': meta.get('mapHash'), 'script': sha1(script), 'tool': sha1(__file__),
                       'engine': meta['engine'], 'blender': meta['blender'], 'rendered': time.strftime('%Y-%m-%d')}}
    trk.parent.mkdir(exist_ok=True)
    trk.write_text(TRACK_JS.format(shot=a.shot, shot_json=json.dumps(a.shot), names=', '.join(tracks) or '(none)',
                                   data=json.dumps(data, separators=(',', ':'))), encoding='utf-8', newline='\n')
    sync_scenes(L)
    print(f'anchors + source: {trk.relative_to(ROOT)} ({len(tracks)} anchors, {trk.stat().st_size / 1e3:.0f} KB)'
          + (f'; built from course map {meta["mapHash"]}' if meta.get('mapHash') else ''))
    mb = dst.stat().st_size / 1e6
    print(f'clip: {dst.relative_to(ROOT)} ({mb:.2f} MB, {meta["frames"] / meta["fps"]:.2f} s){" PROBLEMS: " + "; ".join(problems) if problems else ", meets the clip spec"}')
    print(f'time: {time.perf_counter() - t0:.1f} s in all (Blender {wall:.1f} s, of which rendering {meta["render_s"]} s; '
          f'encoding {time.perf_counter() - t0 - wall:.1f} s)')
    print(f'\nlesson.js:\n  videos: {{ {a.shot}: \'assets/video/{a.shot}.mp4\' }},')
    if problems:
        sys.exit(1)


if __name__ == '__main__':
    main()
