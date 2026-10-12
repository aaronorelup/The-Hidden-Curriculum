"""course_map: the course map rising as soft 3D blocks, the lantern string swinging over it, a slow camera push.

Built from the course data (engine/course.js, from curriculum.md), so a re-render follows the curriculum: one block
per district in path order (top row left to right, bottom row right to left, like K.map), one terrace per module, the
Start and Finish stones, the garden path walked from Start to Finish, one lantern per district. Colours are K.C.
Rendered by:  python tools/blender_shot.py _demo course_map   (docs/blender-shots.md)
Anchors (scenes/00-shot-course_map.js): district:<id> (the far row: the top of each block; the near row: its foot;
k = how far it has risen), start, finish (the top of each stone).
"""
import math

import blender_shot as bs

S = bs.setup(seconds=5.5, fps=24, size=(1280, 720), engine='eevee', samples=48)
C = S.C
course = bs.course()
regions = course['districts']
districts = [d for d in regions if d.get('kind', 'district') == 'district']
start = next((d for d in regions if d.get('kind') == 'start'), None)
finish = next((d for d in regions if d.get('kind') == 'finish'), None)
N = len(districts)

# ---------------------------------------------------------------- layout (Blender units; x right, y away, z up)
SPAN = 8.6                    # width of a row of district blocks
DEPTH = 1.72                  # block depth (front to back)
GX, ROW_Y = 0.34, 1.13        # gap between blocks in a row; row centre lines at +-ROW_Y (top row is the far one)
top_n = math.ceil(N / 2)
rows = [districts[:top_n], list(reversed(districts[top_n:]))]   # bottom row walks right to left
cells = {}                    # district id -> (x, y, w)
for r, row in enumerate(rows):
    n = max(1, len(rows[0]))  # both rows share the top row's column grid
    w = (SPAN - (n - 1) * GX) / n
    for c, d in enumerate(row):
        col = c if r == 0 else c + (n - len(row))      # a shorter bottom row lines up under the right-hand columns
        cells[d['id']] = (-SPAN / 2 + w / 2 + col * (w + GX), ROW_Y if r == 0 else -ROW_Y, w)
STONE_X = -SPAN / 2 - 0.95    # the Start and Finish stones, left of the rows
TURN_X = SPAN / 2 + 0.55      # where the path turns down from the top row to the bottom row

# ---------------------------------------------------------------- materials
m_ground = bs.material('ground', 'page', rough=0.95)
m_board = bs.material('board', bs.mix('page', 'tile', 0.55), rough=0.9)
m_plinth = bs.material('plinth', bs.mix('tile', 'accent', 0.32), rough=0.8)
m_slab = [bs.material('slab_a', bs.mix('tile', 'line2', 0.45), rough=0.7),
          bs.material('slab_b', bs.mix('tile', 'line2', 0.72), rough=0.7)]
m_top = bs.material('slab_top', bs.mix('line2', 'soft', 0.12), rough=0.65)      # the top terrace catches the light
m_stone = bs.material('stone', bs.mix('line2', 'quiet', 0.35), rough=0.85)
m_pedestal = bs.material('pedestal', bs.mix('tile', 'line2', 0.6), rough=0.7)
m_gold = bs.material('gold', 'gold', rough=0.35, metal=0.6)
m_ink = bs.material('ink', 'ink', rough=0.6)
m_string = bs.material('string', bs.mix('line2', 'soft', 0.4), rough=0.8)

# ---------------------------------------------------------------- ground and the map board
bs.box('ground', (60, 60, 0.02), (0, 0, -0.02), m_ground, bevel=0)
bs.box('board', (SPAN + 3.5, 2 * ROW_Y + DEPTH + 1.3, 0.06), (-0.45, 0, 0), m_board, bevel=0.05)
Z0 = 0.06                     # the board's top

# ---------------------------------------------------------------- timing (seconds): path order Start, districts, Finish
T_START = 0.15
T_D = [0.45 + i * 0.36 for i in range(N)]          # each district starts rising
T_FINISH = T_D[-1] + 0.55 if N else 1.0
T_LIT = [t + 0.55 for t in T_D]                     # its lantern lights as it finishes


def hide_when_zero(ob, k):
    bs.bake(ob, 'hide_render', lambda t: k(t) <= 0.001)
    bs.bake(ob, 'hide_viewport', lambda t: k(t) <= 0.001)


# ---------------------------------------------------------------- the districts: a plinth plus one terrace per module
PLINTH_H, SLAB_H, SLAB_GAP, INSET = 0.12, 0.19, 0.035, 0.12
tops = {}                     # district id -> top(t): the z of its top face
rise = {}                     # district id -> k(t): 0..1, how far the block has risen
for i, d in enumerate(districts):
    x, y, w = cells[d['id']]
    t0 = T_D[i]
    k_pl = (lambda t0: lambda t: bs.ease(t, t0, 0.32, 'out'))(t0)
    pl = bs.box(f"{d['id']}.plinth", (w, DEPTH, PLINTH_H), (x, y, Z0), m_plinth, bevel=0.035)
    bs.bake(pl, 'scale', (lambda k: lambda t: (1.0, 1.0, max(0.001, k(t))))(k_pl))
    hide_when_zero(pl, k_pl)
    n_mod = max(1, len(d.get('modules', [])))
    ks = [(lambda a: lambda t: bs.ease(t, a, 0.42, 'out'))(t0 + 0.16 + j * 0.09) for j in range(n_mod)]

    def base_z(t, j, k_pl=k_pl, ks=ks):
        return Z0 + PLINTH_H * k_pl(t) + sum((SLAB_H + SLAB_GAP) * ks[m](t) for m in range(j))

    for j in range(n_mod):
        sw, sd = w - 2 * INSET * (j + 1), DEPTH - 2 * INSET * (j + 1) * 0.8
        sl = bs.box(f"{d['id']}.module{j + 1}", (sw, sd, SLAB_H), (x, y, Z0), m_top if j == n_mod - 1 else m_slab[j % 2],
                    bevel=0.045)
        bs.bake(sl, 'location', (lambda j, bz: lambda t: (x, y, bz(t, j) + SLAB_GAP * ks[j](t)))(j, base_z))
        bs.bake(sl, 'scale', (lambda j: lambda t: (1.0, 1.0, max(0.001, ks[j](t))))(j))
        hide_when_zero(sl, ks[j])
    tops[d['id']] = (lambda bz, n: lambda t: bz(t, n))(base_z, n_mod)
    rise[d['id']] = ks[-1]
    # the name's place: on the top face for the far row, at the foot of the block for the near row (a far block's
    # top would sit right behind a near block's top on screen)
    far = y > 0
    bs.anchor(f"district:{d['id']}", (lambda x, y, top, far: lambda t: (x, y, top(t) + 0.02) if far else
                                      (x, y - DEPTH / 2 - 0.2, Z0))(x, y, tops[d['id']], far),
              k=ks[-1], label=d['name'])

# ---------------------------------------------------------------- Start and Finish stones (a pedestal with a gold ring)
for key, reg, row_y, t0 in (('start', start, ROW_Y, T_START), ('finish', finish, -ROW_Y, T_FINISH)):
    k = (lambda a: lambda t: bs.ease(t, a, 0.45, 'back'))(t0)
    root = bs.empty(f'{key}.root', (STONE_X, row_y, Z0))
    bs.cylinder(f'{key}.pedestal', 0.46, 0.16, (0, 0, 0), m_pedestal, bevel=0.04, parent=root)
    bs.torus(f'{key}.ring', 0.38, 0.022, (0, 0, 0.165), m_gold, parent=root)
    bs.bake(root, 'scale', (lambda k: lambda t: (max(0.001, k(t)),) * 3)(k))
    for ob in root.children:
        hide_when_zero(ob, k)
    bs.anchor(key, (lambda y: lambda t: (STONE_X, y, Z0 + 0.2))(row_y), k=k,
              label=('Start' if key == 'start' else 'Finish'))

# ---------------------------------------------------------------- the garden path: stepping stones from Start to Finish
route = [(STONE_X + 0.5, ROW_Y), (TURN_X, ROW_Y), (TURN_X, -ROW_Y), (STONE_X + 0.5, -ROW_Y)]
seglen = [math.dist(a, b) for a, b in zip(route, route[1:])]
L = sum(seglen)


def along(s):
    for (a, b), ln in zip(zip(route, route[1:]), seglen):
        if s <= ln:
            return a[0] + (b[0] - a[0]) * s / ln, a[1] + (b[1] - a[1]) * s / ln
        s -= ln
    return route[-1]


def under_block(px, py):
    return any(abs(px - x) < w / 2 + 0.08 and abs(py - y) < DEPTH / 2 + 0.08 for x, y, w in cells.values())


rand = bs.rng(7)
STEP = 0.27
walk0, walk1 = T_START + 0.2, T_FINISH        # the path is walked while the districts rise
for i in range(int(L / STEP) + 1):
    s = i * STEP
    px, py = along(s)
    if under_block(px, py):
        continue
    jitter = (rand() - 0.5) * 0.05
    a = walk0 + (walk1 - walk0) * s / L
    k = (lambda a: lambda t: bs.ease(t, a, 0.3, 'out'))(a)
    st = bs.cylinder(f'path.{i:03d}', 0.085 + jitter * 0.4, 0.025, (px + jitter, py - jitter, Z0), m_stone, verts=20, bevel=0.01)
    bs.bake(st, 'scale', (lambda k: lambda t: (max(0.001, k(t)),) * 3)(k))
    hide_when_zero(st, k)

# ---------------------------------------------------------------- the lanterns (AI): one per district, on a string, swinging
SY, SZ, SAG = ROW_Y + DEPTH / 2 + 0.75, 2.75, 0.4          # string line: behind the top row, above it
x0, x1 = -SPAN / 2 - 0.4, SPAN / 2 + 0.4
string_z = lambda x: SZ - SAG * (1 - ((x - (x0 + x1) / 2) / ((x1 - x0) / 2)) ** 2)
for side, px in (('l', x0 - 0.35), ('r', x1 + 0.35)):
    bs.cylinder(f'post.{side}', 0.035, SZ + 0.05, (px, SY, Z0), m_ink, verts=16)
pts = [(x0 - 0.35, SY, SZ)] + [(x0 + (x1 - x0) * i / 20, SY, string_z(x0 + (x1 - x0) * i / 20)) for i in range(21)] + [(x1 + 0.35, SY, SZ)]
bs.curve('string', pts, depth=0.008, mat=m_string)

for i, d in enumerate(districts):
    lx = x0 + 0.55 + (x1 - x0 - 1.1) * (i / max(1, N - 1))
    pivot = bs.empty(f'lantern{i}.pivot', (lx, SY, string_z(lx)))
    pivot.scale = (1.2, 1.2, 1.2)
    m_body = bs.material(f'lantern{i}.paper', bs.mix('head', 'paper', 0.25), rough=0.6, emit='head', strength=0.0)
    m_rib = bs.material(f'lantern{i}.rib', bs.mix('gold', 'accent', 0.35), rough=0.5)
    parts = [bs.cylinder(f'lantern{i}.cord', 0.006, 0.22, (0, 0, -0.22), m_string, verts=8, parent=pivot),
             bs.cylinder(f'lantern{i}.cap', 0.07, 0.045, (0, 0, -0.265), m_ink, verts=24, bevel=0.01, parent=pivot)]
    cz, rz, rr = -0.47, 0.22, 0.165
    parts.append(bs.sphere(f'lantern{i}.body', rr, (0, 0, cz), m_body, scale=(1, 1, rz / rr), parent=pivot))
    for dz in (-0.12, 0.0, 0.12):
        parts.append(bs.torus(f'lantern{i}.rib{dz:+.2f}', rr * math.sqrt(max(0.0, 1 - (dz / rz) ** 2)) + 0.004, 0.009,
                              (0, 0, cz + dz), m_rib, parent=pivot))
    parts.append(bs.cylinder(f'lantern{i}.foot', 0.06, 0.04, (0, 0, cz - rz - 0.03), m_ink, verts=24, bevel=0.01, parent=pivot))
    parts.append(bs.cylinder(f'lantern{i}.tassel', 0.012, 0.12, (0, 0, cz - rz - 0.15), m_rib, verts=8, parent=pivot))
    for ob in parts:
        ob.visible_shadow = False          # the light inside must reach the map
    lamp = bs.light('POINT', (0, 0, cz), 0.0, color='head', size=0.12, name=f'lantern{i}.light')
    lamp.parent = pivot
    lit = (lambda a: lambda t: bs.ease(t, a, 0.6, 'sine'))(T_LIT[i])
    bs.socket(m_body.node_tree.nodes['Principled BSDF'].inputs['Emission Strength'], (lambda k: lambda t: 2.2 * k(t))(lit))
    bs.bake(lamp.data, 'energy', (lambda k: lambda t: 70.0 * k(t))(lit))
    # the swing: a slow pendulum, each lantern a little out of step, settling a touch as the shot ends
    ph, per = i * 1.1, 2.5 + 0.18 * (i % 3)
    amp = lambda t: math.radians(7.0 - 2.0 * bs.ease(t, 0.0, S.seconds, 'sine'))
    bs.bake(pivot, 'rotation_euler', (lambda ph, per: lambda t: (
        0.45 * amp(t) * math.sin(2 * math.pi * t / (per * 1.3) + ph + 0.8),
        amp(t) * math.sin(2 * math.pi * t / per + ph), 0.0))(ph, per))

# ---------------------------------------------------------------- light: moonlight, a soft fill, the lanterns do the rest
bs.light('SUN', (0, 0, 10), 1.0, color='#A9B4E0', name='moon', target=(1.5, 1.0, 0)).data.angle = math.radians(8)
bs.light('AREA', (-1.0, -7.5, 7.0), 700.0, color='body', size=9.0, name='fill', target=(-0.4, 0.0, 0.0), shadow=False)

# ---------------------------------------------------------------- camera: a slow push in, ending still
P0, P1 = (0.3, -12.6, 10.6), (0.8, -9.6, 7.9)        # camera: from high and far to a little closer and lower
A0, A1 = (-0.3, 0.0, 0.55), (-0.2, 0.1, 0.7)         # aim: the middle of the map, a little high so the lanterns keep headroom
cam = bs.camera(P0, A0, lens=34)


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
