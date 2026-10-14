"""house_and_flat: a virtual machine and a container as two buildings, for section 10 ("The house and the flat").

Left, a detached house on its own foundation slab: a VM, which brings its own operating system. Right, a small block of
flats on ONE shared foundation with ONE service riser running up its front: containers, which share the host's kernel.
The camera pushes slowly across both; the shared foundation (and the riser that comes up out of it) glows once.
No 3D text: the scene writes the labels on the canvas at the anchors below.
Rendered by:  python tools/blender_shot.py where-your-agent-works house_and_flat   (docs/blender-shots.md)
Anchors (scenes/00-shot-house_and_flat.js):
  vm          above the house's roof ridge            label 'VM: its own operating system'
  container   above the block's roof                  label "container: shares the host's kernel"
  vm-slab     the front edge of the house's own slab  (k: 0, the house's slab never glows in the clip)
  shared      the front edge of the shared foundation (k: the glow, 0..1..0)
"""
import math

import blender_shot as bs

S = bs.setup(seconds=6.0, fps=24, size=(1280, 720), engine='eevee', samples=48)

# ---------------------------------------------------------------- materials (K.C names)
m_ground = bs.material('ground', 'page', rough=0.95)
m_lawn = bs.material('lawn', bs.mix('page', 'tile', 0.6), rough=0.92)
m_slab = bs.material('slab', bs.mix('tile', 'line2', 0.55), rough=0.8)
m_wall = bs.material('wall', bs.mix('line2', 'soft', 0.22), rough=0.75)
m_wall2 = bs.material('wall2', bs.mix('line2', 'soft', 0.12), rough=0.75)
m_roof = bs.material('roof', bs.mix('accent', 'tile', 0.55), rough=0.7)
m_ink = bs.material('ink', 'ink', rough=0.6)
m_win = bs.material('window', bs.mix('head', 'paper', 0.3), rough=0.5, emit='head', strength=1.6)
m_found = bs.material('foundation', bs.mix('tile', 'line2', 0.55), rough=0.8, emit='gold', strength=0.0)
m_riser = bs.material('riser', bs.mix('gold', 'line2', 0.55), rough=0.45, metal=0.4, emit='gold', strength=0.0)

Z0 = 0.0
bs.box('ground', (60, 60, 0.02), (0, 0, -0.02), m_ground, bevel=0)
bs.box('lawn', (12.5, 5.2, 0.03), (0.0, 0.3, 0.0), m_lawn, bevel=0.03)
Z0 = 0.03

# ---------------------------------------------------------------- left: the detached house on its own slab (the VM)
HX = -3.1
SLAB_H = 0.22
bs.box('house.slab', (2.7, 2.3, SLAB_H), (HX, 0.0, Z0), m_slab, bevel=0.04)
zf = Z0 + SLAB_H
WALL_W, WALL_D, WALL_H = 1.9, 1.55, 1.25
bs.box('house.walls', (WALL_W, WALL_D, WALL_H), (HX, 0.0, zf), m_wall, bevel=0.03)
# gable roof: two tilted planks meeting over the ridge (x runs along the ridge)
PITCH = math.radians(34)
half = WALL_D / 2 + 0.16
plank_w = half / math.cos(PITCH)
for side, sgn in (('front', -1), ('back', 1)):
    pl = bs.box(f'house.roof.{side}', (WALL_W + 0.36, plank_w, 0.08), (0, 0, 0), m_roof, bevel=0.02, base=False)
    pl.location = (HX, sgn * half / 2, zf + WALL_H + math.tan(PITCH) * half / 2 - 0.02)
    pl.rotation_euler = (-sgn * PITCH, 0.0, 0.0)
# the gable ends: a triangular prism filling the space under the roof (built from vertices, no bevel)
gable_h = math.tan(PITCH) * WALL_D / 2


def prism(name, w, d, h, loc, mat):
    import bpy
    me = bpy.data.meshes.new(name)
    v = [(-w / 2, -d / 2, 0), (-w / 2, d / 2, 0), (-w / 2, 0, h), (w / 2, -d / 2, 0), (w / 2, d / 2, 0), (w / 2, 0, h)]
    me.from_pydata(v, [], [(0, 1, 2), (3, 5, 4), (0, 3, 4, 1), (1, 4, 5, 2), (2, 5, 3, 0)])
    me.update()
    return bs._obj(name, me, loc, mat)


prism('house.gable', WALL_W - 0.02, WALL_D - 0.02, gable_h, (HX, 0.0, zf + WALL_H - 0.01), m_wall)
bs.box('house.chimney', (0.22, 0.22, 0.55), (HX + 0.55, 0.25, zf + WALL_H + 0.15), m_ink, bevel=0.02)
bs.box('house.door', (0.34, 0.04, 0.62), (HX - 0.35, -WALL_D / 2 - 0.01, zf), m_ink, bevel=0.01)
bs.box('house.win', (0.42, 0.04, 0.34), (HX + 0.4, -WALL_D / 2 - 0.01, zf + 0.55), m_win, bevel=0.01)
bs.box('house.step', (0.5, 0.25, 0.06), (HX - 0.35, -WALL_D / 2 - 0.16, zf), m_slab, bevel=0.01)

# ---------------------------------------------------------------- right: the block of flats on one shared foundation
BX = 3.0
FOUND_W, FOUND_D, FOUND_H = 3.3, 2.3, SLAB_H
bs.box('block.foundation', (FOUND_W, FOUND_D, FOUND_H), (BX, 0.0, Z0), m_found, bevel=0.04)
zb = Z0 + FOUND_H
FLAT_W, FLAT_D, FLAT_H, GAP = 1.15, 1.5, 0.62, 0.06
RISER_W = 0.34
cols = (BX - (RISER_W / 2 + GAP + FLAT_W / 2), BX + (RISER_W / 2 + GAP + FLAT_W / 2))
FLOORS = 3
for f in range(FLOORS):
    for c, cx in enumerate(cols):
        z = zb + f * (FLAT_H + GAP)
        bs.box(f'flat.{f}{c}', (FLAT_W, FLAT_D, FLAT_H), (cx, 0.0, z), m_wall if (f + c) % 2 == 0 else m_wall2, bevel=0.03)
        bs.box(f'flat.{f}{c}.win', (0.46, 0.04, 0.26), (cx + (0.18 if c == 0 else -0.18), -FLAT_D / 2 - 0.01, z + 0.2),
               m_win if (f, c) != (1, 0) else m_ink, bevel=0.01)
top = zb + FLOORS * (FLAT_H + GAP)
bs.box('block.roof', (2 * FLAT_W + RISER_W + 2 * GAP + 0.2, FLAT_D + 0.2, 0.1), (BX, 0.0, top), m_roof, bevel=0.03)
# the service riser: one shared pipe column on the front, coming up out of the shared foundation to the roof
riser = bs.box('block.riser', (RISER_W * 0.62, 0.22, top - zb + 0.25), (BX, -FLAT_D / 2 + 0.06, zb - 0.02), m_riser, bevel=0.03)
for f in range(FLOORS):
    for c, cx in enumerate(cols):                          # a short branch from the riser into each flat
        bx = BX + (-1 if c == 0 else 1) * (RISER_W / 2 + GAP / 2)
        bs.box(f'riser.branch.{f}{c}', (GAP + 0.12, 0.08, 0.06), (bx, -FLAT_D / 2 - 0.02, zb + f * (FLAT_H + GAP) + 0.45),
               m_riser, bevel=0.01)

# ---------------------------------------------------------------- the glow: once, in the middle, calm at both ends
glow = lambda t: bs.ease(t, 2.4, 0.9, 'sine') * (1 - bs.ease(t, 3.9, 1.0, 'sine'))
bs.socket(m_found.node_tree.nodes['Principled BSDF'].inputs['Emission Strength'], lambda t: 0.9 * glow(t))
bs.socket(m_riser.node_tree.nodes['Principled BSDF'].inputs['Emission Strength'], lambda t: 0.7 * glow(t))
under = bs.light('AREA', (BX, -FOUND_D / 2 - 0.35, Z0 + 0.25), 0.0, color='gold', size=2.8, name='foundation.glow',
                 target=(BX, 0.0, Z0 + 0.1), shadow=False)
bs.bake(under.data, 'energy', lambda t: 40.0 * glow(t))

# ---------------------------------------------------------------- anchors (labels go on the canvas)
ridge = zf + WALL_H + math.tan(PITCH) * half
bs.anchor('vm', lambda t: (HX, 0.0, ridge + 0.75), label='VM: its own operating system')
bs.anchor('container', lambda t: (BX, 0.0, top + 0.55), label="container: shares the host's kernel")
bs.anchor('vm-slab', lambda t: (HX, -1.15, Z0 + SLAB_H / 2), k=lambda t: 0.0)
bs.anchor('shared', lambda t: (BX, -FOUND_D / 2, Z0 + FOUND_H / 2), k=glow)

# ---------------------------------------------------------------- light: moonlight and a soft fill, warm windows
bs.light('SUN', (0, 0, 10), 1.1, color='#A9B4E0', name='moon', target=(1.2, 1.5, 0)).data.angle = math.radians(8)
bs.light('AREA', (-1.5, -8.0, 6.5), 650.0, color='body', size=9.0, name='fill', target=(0.0, 0.0, 0.8), shadow=False)
bs.light('POINT', (HX + 0.4, -1.4, zf + 0.7), 12.0, color='head', size=0.3, name='house.porch', shadow=False)

# ---------------------------------------------------------------- camera: a slow push and truck across both, ending still
P0, P1 = (-0.9, -11.4, 4.6), (0.3, -9.9, 3.9)
A0, A1 = (-0.3, 0.0, 1.05), (0.1, 0.0, 1.1)
cam = bs.camera(P0, A0, lens=35)


def cam_at(t):
    k = bs.ease(t, 0.0, S.seconds, 'io')
    return tuple(bs.lerp(a, b, k) for a, b in zip(P0, P1)), tuple(bs.lerp(a, b, k) for a, b in zip(A0, A1))


def cam_rot(t):
    loc, aim = cam_at(t)
    cam.location = loc
    bs.look(cam, aim)
    return tuple(cam.rotation_euler)


bs.bake(cam, 'location', lambda t: cam_at(t)[0])
bs.bake(cam, 'rotation_euler', cam_rot)
