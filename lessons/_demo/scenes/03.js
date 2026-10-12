// 03  a real still screenshot "in use": the shot the browser capture took of the course page (site/course-page,
// 1920x1080), animated with K.shot: a scripted pointer, two zooms, a click, and the click's result: the shot crossfades
// (swap) to site/latest-lesson, the page that card really opens (a side shot: capture.py opened the card's link in a
// second tab after the recording), so the click changes the picture and the address bar like a real one. This is how
// a lesson shows an action an agent captured as screenshots.
// Every position comes from the boxes the shot steps measured (K.captureBox), none is typed in, so a re-record that
// moves the page around moves the pointer, the zooms and the callouts with it.
SCENE('03', (t, S) => {
  K.bg({ glow: 0.08 });
  DEMO.label(t, 'Screenshot in use', 'capture shot · K.shot · swap');
  const [W, H] = K.mediaSize('site/course-page') || [1920, 1080];
  const stats = K.captureBox('site', 'course-page', 'stats', [77, 698, 874, 176]);   // 214 lessons · 22 modules ...
  const card = K.captureBox('site', 'course-page', 'card', [1034, 282, 810, 456]);    // the latest-lesson card
  const play = K.captureBox('site', 'course-page', 'play', [1368, 403, 141, 141]);    // its play button
  const title = K.captureBox('site', 'latest-lesson', 'title', [77, 307, 1766, 104]); // the page it opens: its title
  const mid = (b, fx = 0.5, fy = 0.5) => ({ x: b[0] + b[2] * fx, y: b[1] + b[3] * fy });
  const clickAt = 6.2, clicked = clickAt + 0.18;            // the pointer arrives, then clicks 0.18 s later
  K.shot('site/course-page', t - 0.4, DEMO.WIN, {
    alpha: K.io(t, -0.4, 0.7),
    cursor: [
      { at: 0, x: W * 0.8, y: H * 0.92 },
      { at: 1.6, ...mid(stats, 0.5, 0.62) },
      { at: clickAt, ...mid(play), kind: 'hand', click: true },
      { at: 9.4, x: W * 0.8, y: H * 0.6 },
    ],
    zooms: [
      { at: 0.9, until: 4.3, box: stats },
      { at: 4.6, until: clicked + 0.5, box: card, z: 1.55 },  // starts within a move of 4.3: the camera pans straight on
    ],
    swap: [{ at: clicked + 0.25, name: 'site/latest-lesson', d: 0.35 }],
    callouts: [
      { at: 1.9, until: 4.1, box: stats, text: 'Real numbers, from the course data' },
      { at: clicked + 1.6, until: clicked + 5.4, box: title, text: 'Click: the latest lesson opens', side: 'top' },
    ],
  });
});
