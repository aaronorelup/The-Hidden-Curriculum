// _demo shared bits: the scene label (top right, under the demo window so a zoom covers it)
window.DEMO = {
  label(t, eyebrow, line) {
    const k = K.io(t, -0.2, 0.6, 'out');
    K.eyebrow(eyebrow, 1840, 76, { align: 'right', alpha: k });
    K.text(line, 1840, 112, { font: 'mono', size: 26, color: K.C.soft, align: 'right', alpha: k });
  },
  // the window every capture plays in: centred, the recording's own 16:9 plus the 50 px bar
  WIN: [260, 150, 1400],
};
