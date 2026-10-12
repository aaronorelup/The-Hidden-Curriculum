/* sandbox: exercises every kit primitive so engine changes can be eyeballed with stills.py */
LESSON({
  id: '99.99', title: 'Kit sandbox', short: 'Kit sandbox', module: 'Testing',
  summary: 'Every primitive in one place.',
  keep: [['Bold lead.', 'Rest of the sentence.']],
  draft: { '01': 6, '02': 8, '03': 8, '04': 8 },
  noBadge: ['01'],
  scenes: {
    '01': (t) => {
      K.bg({ glow: 0.14 });
      K.petals(t, { n: 6 });
      K.eyebrow('The Missing Map · lesson 99.99', K.W / 2, 440, { align: 'center', alpha: K.io(t, 0, 0.8) });
      K.title('Kit sandbox', K.W / 2, 560, { align: 'center', size: 110, alpha: K.io(t, 0.3, 0.8) });
      K.text('Everything nobody told you, drawn in code.', K.W / 2, 640, { align: 'center', font: 'read', italic: true, size: 38, color: K.C.body, alpha: K.io(t, 0.8, 0.8) });
    },
    '02': (t) => {
      K.bg();
      const r = K.win(120, 160, 820, 420, { title: 'script.txt - Notepad', kind: 'notepad' });
      K.editor(r, t, ['print("hello")', 'name = input("name? ")', '# a comment', 'print("hi", name)'], { syntax: 'py', typeAt: 0.5 });
      const r2 = K.win(1000, 160, 800, 420, { title: 'Command Prompt', kind: 'terminal', focus: true });
      K.term(r2, t, [{ at: 0.5, cmd: 'cd Desktop' }, { at: 2, cmd: 'python script.py' }, { at: 3.4, out: "can't open file 'script.py'", color: K.C.accent }]);
      K.file(300, 800, 150, { ext: 'txt', name: 'script.txt' });
      K.file(560, 800, 150, { ext: 'py', name: 'script.py', alpha: K.io(t, 2, 0.5) });
      K.folder(820, 800, 120, { name: 'Desktop' });
      K.arrow(380, 800, 480, 800, { k: K.io(t, 1, 0.8), bend: -40 });
      K.pill('.venv', 1100, 760, { alpha: K.io(t, 1, 0.5) });
      K.pill('PATH', 1260, 760, { color: K.C.head });
      K.pill('.env', 1490, 760, { font: 'mono', icon: 'lock', w: 220, color: K.C.gold });
      K.note(1000, 820, 800, 'Keep this', 'A file extension is only a label. Renaming changes the label, not the contents.', { size: 30, alpha: K.io(t, 1.5, 0.6) });
    },
    '03': (t) => {
      K.bg();
      K.icons.forEach((n, i) => {
        const x = 125 + (i % 12) * 152, y = 250 + Math.floor(i / 12) * 270;
        K.iconTile(n, x, y, 120, { alpha: K.stagger(t, 0.1, i, 0.015) });
        K.text(n, x, y + 100, { align: 'center', size: 22, color: K.C.soft });
      });
    },
    '04': (t) => {
      K.bg();
      K.map.draw(t, { t0: 0, pin: '15', focus: t > 3 ? 'trust' : null, focusK: K.io(t, 3, 0.8) });
    },
  },
});
