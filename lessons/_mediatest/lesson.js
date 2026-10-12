/* _mediatest: engine test for the media exhibits (K.video, K.image, K.listen, K.sound, K.cursor). NEVER publish.
   The timeline (cues.json) is synthetic, with no narration. make_assets.py rebuilds the media: audio/mix.mp3 is the
   lesson clock (a 1 kHz tick at every whole second), assets/audio/beeps.mp3 the sound exhibit (a 2 kHz burst at every
   whole second of the sound), assets/video/clip.mp4 10 s of Aaron's Lamplighter game autoplay (960x540, 24 fps, to the
   clip spec in tools/media_util.py), assets/img/screen.webp a real screenshot of a lesson page.
   tests/ checks it: exactness.py (frame-exact video), render_sync.py (MP4 picture and sound in sync), player_sync.py
   (the live page). The media times below are what those tests expect: change them together. */
LESSON({
  id: '99.98', title: 'Media test', short: 'Media test', module: 'Testing',
  summary: 'Engine test for K.video, K.image, K.listen, K.sound and K.cursor. Never published.',
  keep: [['Bold lead.', 'Rest of the sentence.']],
  noBadge: [],
  images: { still: 'assets/img/still.webp', screen: 'assets/img/screen.webp', spec_beeps: 'assets/img/spec_beeps.webp' },
  // the same file twice: scene 01 and scene 02 crossfade with the clip at two different media times
  videos: { clip: 'assets/video/clip.mp4', clip2: 'assets/video/clip.mp4' },
  sounds: { beeps: 'assets/audio/beeps.mp3' },
  scenes: {
    // moving camera, cover fit into a box of another aspect, rounded corners. Clip at (T - 1.2) - 1.5
    '01': (t) => {
      K.bg();
      const cam = K.cam(t, [{ at: 0, x: 960, y: 540, z: 1 }, { at: 2.5, x: 1060, y: 500, z: 1.3, d: 2.5 }, { at: 7.5, x: 900, y: 560, z: 1.08, d: 2.5 }]);
      K.withCam(cam, () => {
        K.video('clip', t - 1.5, 330, 190, 1260, 640, { fit: 'cover', r: 22 });
        K.text('K.video · cover · moving camera', 960, 900, { align: 'center', size: 34, color: K.C.head });
      });
    },
    // native size (960x540 at 480,270), no rounding: what tests/exactness.py compares with ffmpeg. Clip2 at (T - 13.2) + 0.25
    '02': (t) => {
      K.bg();
      K.text('K.video · native size, r 0', 960, 220, { align: 'center', size: 34, color: K.C.head });
      K.video('clip2', t + 0.25, 480, 270, 960, 540, { r: 0 });
    },
    // K.image both fits, K.listen with a sound (beeps heard at (T - 25.2) - 0.5) and without one, a missing video
    '03': (t) => {
      K.bg();
      K.image('still', 100, 150, 820, 420, { fit: 'cover', r: 20 });
      K.image('still', 1000, 150, 820, 420, { fit: 'contain', bg: K.C.code, r: 20 });
      K.text('cover', 510, 610, { align: 'center', size: 28, color: K.C.soft });
      K.text('contain + bg', 1410, 610, { align: 'center', size: 28, color: K.C.soft });
      K.listen('beeps', t - 0.5, 100, 650, 1300, 160, { label: 'beeps.mp3 · heard: a 2 kHz burst each second' });
      K.listen('nothing', t, 100, 830, 1300, 100, { dur: 12, label: 'no spectrogram, no sound: calm strip' });
      K.video('nope', t, 1460, 650, 360, 280, {});
    },
    // a small looping copy at double speed (the live player has to measure the speed and play at 2x). Clip at 2 (T - 35.6), looped
    '04': (t) => {
      K.bg();
      K.text('K.video · loop · 2x', 960, 220, { align: 'center', size: 34, color: K.C.head });
      K.video('clip', t * 2, 660, 330, 600, 338, { loop: true, r: 16, bg: K.C.code });
    },
    // a real screenshot "in use": zoom into it, a pointer that lands on a source pixel through placement.at(),
    // a click ring; and a clip with its own sound (clip2 and beeps both at (T - 46.0) - 1)
    '05': (t) => {
      K.bg();
      K.text('K.image · zoom · K.cursor', 610, 140, { align: 'center', size: 30, color: K.C.head });
      const btn = [800, 645];                                    // "Play lesson" in screen.webp (1600x900)
      const z = 1 + 1.4 * K.io(t, 2, 1.6) - 1.4 * K.io(t, 7, 1.2);
      const p = K.image('screen', 90, 190, 1040, 585, { zoom: { x: btn[0], y: btn[1], z }, r: 14, stroke: true });
      const [bx, by] = p.at(btn[0], btn[1]);
      const k = K.io(t, 1.2, 2.6, 'io');
      const cx = K.lerp(1060, bx + 6, k), cy = K.lerp(260, by + 8, k);   // the tip lands inside the button
      K.cursor(cx, cy, { click: K.seg(t, 4.2, 4.9), alpha: K.io(t, 0.6, 0.4) });
      K.text('K.video · sound: beeps', 1500, 220, { align: 'center', size: 30, color: K.C.head });
      K.video('clip2', t - 1, 1170, 260, 660, 371, { sound: 'beeps', r: 14, stroke: true });
    },
  },
});
