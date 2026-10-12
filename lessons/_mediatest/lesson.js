/* _mediatest: engine test for video and image exhibits (K.video, K.image, K.listen), 2026-10-04.
   NEVER publish. The timeline (cues.json) is synthetic, with no narration: the "narration" clock is audio/mix.mp3,
   which is the Lamplighter game's own capture.wav (experiments/game/cpp-bare). The clip is 10 s of that game's
   autoplay.mp4 re-encoded to 960x540, 24 fps, H.264 yuv420p, GOP 12 (BT.709 limited range). */
LESSON({
  id: '99.98', title: 'Media test', short: 'Media test', module: 'Testing',
  summary: 'Engine test for K.video, K.image and K.listen. Never published.',
  keep: [['Bold lead.', 'Rest of the sentence.']],
  noBadge: [],
  images: { still: 'assets/img/still.webp', spec_song: 'assets/img/spec_song.webp' },
  // the same file twice: scene 01 and scene 02 crossfade with the clip at two different media times
  videos: { clip: 'assets/video/clip.mp4', clip2: 'assets/video/clip.mp4' },
  scenes: {
    // moving camera, cover fit into a box of another aspect, rounded corners
    '01': (t) => {
      K.bg();
      const cam = K.cam(t, [{ at: 0, x: 960, y: 540, z: 1 }, { at: 2.5, x: 1060, y: 500, z: 1.3, d: 2.5 }, { at: 7.5, x: 900, y: 560, z: 1.08, d: 2.5 }]);
      K.withCam(cam, () => {
        K.video('clip', t - 1.5, 330, 190, 1260, 640, { fit: 'cover', r: 22 });
        K.text('K.video · cover · moving camera', 960, 900, { align: 'center', size: 34, color: K.C.head });
      });
    },
    // native size (960x540 at 480,270), no rounding: what the frame-exactness test compares with ffmpeg
    '02': (t) => {
      K.bg();
      K.text('K.video · native size, r 0', 960, 220, { align: 'center', size: 34, color: K.C.head });
      K.video('clip2', t + 0.25, 480, 270, 960, 540, { r: 0 });
    },
    // K.image both fits, K.listen with and without a spectrogram, and a missing video's placeholder
    '03': (t) => {
      K.bg();
      K.image('still', 100, 150, 820, 420, { fit: 'cover', r: 20 });
      K.image('still', 1000, 150, 820, 420, { fit: 'contain', bg: K.C.code, r: 20 });
      K.text('cover', 510, 610, { align: 'center', size: 28, color: K.C.soft });
      K.text('contain + bg', 1410, 610, { align: 'center', size: 28, color: K.C.soft });
      K.listen('song', t, 100, 650, 1300, 160, { dur: 12, label: 'capture.wav · the game\u2019s own music' });
      K.listen('nothing', t, 100, 830, 1300, 100, { dur: 12, label: 'no spectrogram: calm strip' });
      K.video('nope', t, 1460, 650, 360, 280, {});
    },
    // a small looping copy at double speed (the live player has to measure the speed and play at 2x)
    '04': (t) => {
      K.bg();
      K.text('K.video · loop · 2x', 960, 220, { align: 'center', size: 34, color: K.C.head });
      K.video('clip', t * 2, 660, 330, 600, 338, { loop: true, r: 16, bg: K.C.code });
    },
  },
});
