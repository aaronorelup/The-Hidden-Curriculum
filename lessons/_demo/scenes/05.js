// 05  typing and a key press, recorded for real on a public documentation page (assets/capture/search: the Python
// docs' quick search, "pathlib", Enter). K.demo draws the focusing click, eases the camera onto the field, and shows
// what is typed in the field itself once the zoom makes it readable: a typing chip appears only while the field's own
// text would be under about 24 px on screen (its recorded font size times the zoom). The Enter key shows as a key
// chip beside the pointer. The results page loads; one callout boxes the first real result, at the recipe's
// {"do": "mark", "name": "results"} step (K.captureAt / K.captureBox: no capture time or position is typed in).
SCENE('05', (t, S) => {
  K.bg({ glow: 0.08 });
  DEMO.label(t, 'Typing and keys', 'capture.py type + press · K.demo');
  const go = 0.6, res = K.captureAt('search', 'results', 5.3);
  const first = K.captureBox('search', 'results', 'first', [621, 520, 1269, 68]);
  K.demo('search', t - go, DEMO.WIN, {
    alpha: K.io(t, -0.4, 0.7),
    callouts: [{ at: res + 0.5, until: res + 3.9, box: first, text: 'Real results, from the real search' }],
  });
});
