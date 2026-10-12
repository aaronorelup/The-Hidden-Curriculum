// 04  a 3D shot from Blender: the course map rising as soft blocks under the swinging lantern string, with a slow push.
// The shot is a script in the lesson (blender/course_map.py, built from the course data), rendered headless and encoded
// to the clip spec by tools/blender_shot.py (docs/blender-shots.md):
//   python tools/blender_shot.py _demo course_map      -> assets/video/course_map.mp4 + scenes/00-shot-course_map.js
// It plays here with K.video at its native 1280x720 inside a calm frame. The district names are canvas text, not
// rendered 3D text: SHOT() gives each block's place on screen in this frame (the anchors baked with the clip), so
// the words stay crisp, in the course fonts, and fade in as their block finishes rising.
SCENE('04', (t, S) => {
  K.bg({ glow: 0.1 });
  DEMO.label(t, '3D shot', 'blender/course_map.py');
  const x = 320, y = 146, w = 1280, h = 720, go = 0.4, mt = t - go;
  const k = K.io(t, -0.3, 0.7, 'out');
  K.layer(k, () => {
    K.card(x - 12, y - 12, w + 24, h + 24, { r: 28, fill: K.C.panel });
    const p = K.video('course_map', mt, x, y, w, h, { r: 18, stroke: true, bg: K.C.page });
    const shot = window.SHOTS && SHOTS.course_map;
    if (!shot) return;
    for (const name of Object.keys(shot.anchors)) {
      const a = SHOT('course_map', name, mt, p);
      if (!a || !a.label) continue;
      const end = name === 'start' || name === 'finish';
      const al = K.clamp((a.k - 0.55) / 0.45, 0, 1);
      if (end) {
        K.text(a.label, a.x, a.y + 62, { font: 'ui', weight: 600, size: 26, color: K.C.body, align: 'center', alpha: al, shadow: 12 });
      } else {
        K.text(a.label, a.x, a.y + 10, { font: 'head', weight: 700, size: 30, color: K.C.head, align: 'center', alpha: al, shadow: 14 });
      }
    }
  });
  K.text('The course map in 3D, built from the course data', 960, 922, {
    font: 'read', size: 30, color: K.C.body, align: 'center', italic: true, alpha: K.io(t, 0.6, 0.7),
  });
});
