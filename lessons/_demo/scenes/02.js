// 02  a terminal replay of real commands: python --version, git --version, git init, git status, run for real in a
// throw-away folder by tools/capture.py terminal. The commands are typed at a human pace, the output is the real
// output at its real timing. One mark boxes a line of real output once it has appeared (K.termTimes gives the times).
SCENE('02', (t, S) => {
  K.bg({ glow: 0.08 });
  DEMO.label(t, 'Terminal replay', 'tools/capture.py terminal · K.termReplay');
  const [x, y, w] = DEMO.WIN;
  const tt = K.termTimes('term'), status = tt.items[3];
  const seen = status ? status.out[0].at + 0.5 : 9;
  K.demo('term', t - 0.4, [x, y + 40, w, 720], {
    title: 'Command Prompt', alpha: K.io(t, -0.4, 0.7), size: 32,
    marks: [{ at: seen, until: seen + 3.4, match: 'On branch master', text: 'Real output, at its real speed' }],
  });
});
