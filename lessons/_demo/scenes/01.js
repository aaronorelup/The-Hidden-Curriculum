// 01  a real browser capture (public pages only): the course page, scroll to the curriculum, open 01.01, press play.
// K.demo plays assets/capture/site at capture time t - 0.8, with the pointer from events.json, click ripples and the
// automatic camera; one callout boxes the player's real captions once it is playing.
// No capture time or position is typed in: the callout hangs on the recipe's {"do": "mark", "name": "playing"} step
// (K.captureAt) and boxes the band where the player draws its captions inside the stage that mark measured
// (K.captureBox), so a re-record (`capture.py again _demo site`) moves the callout with the recording.
SCENE('01', (t, S) => {
  K.bg({ glow: 0.08 });
  DEMO.label(t, 'Browser capture', 'tools/capture.py browser · K.demo');
  const go = 0.8, play = K.captureAt('site', 'playing', 12.8);
  const st = K.captureBox('site', 'playing', 'stage', [77, 43, 1766, 994]);
  const captions = [st[0] + st[2] * 0.22, st[1] + st[3] * 0.85, st[2] * 0.56, st[3] * 0.11];
  K.demo('site', t - go, DEMO.WIN, {
    zoom: 1.75,
    alpha: K.io(t, -0.4, 0.7),
    join: 3.2,                                   // the camera pans from the play button to the captions, no dip
    callouts: [{ at: play + 2.2, until: play + 5.4, box: captions, text: 'Real captions, from the real player', zoom: 1.6 }],
  });
});
