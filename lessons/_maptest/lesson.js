/* _maptest: engine test for the data-driven course map (engine/map.js), 2026-10-12. NEVER publish.
   Four fixture courses (fixtures/old = the curriculum as of 2026-10-12, six districts; d4 / d5 / d7 = new-format
   curricula with 4, 5 and 7 districts, d7 with long module names) and a synthetic timeline with no narration:
   make.py writes cues.js (the [map] narration course.py would generate, timed at ~2.6 words/s), plan.js and the
   fixtures' course.js. Every scene switches the map's data with K.map.use(MAPTEST.<fixture>) and draws either
   K.map.draw (pins, focus) or the standard map section K.map.intro(t, S, { lesson }); scene 05 exercises the v1
   draw options old scene code relies on. A grey line under each frame says what it shows.
   Rebuild and look: python lessons/_maptest/make.py && python tools/stills.py _maptest --every 2 */
(function () {
  const C = K.C;
  const PLAN = window.MAPTEST_PLAN || [];

  function label(p) {
    const what = `${p.n} · fixture ${p.fixture} · ${p.kind}${p.lesson ? ' · ' + p.lesson : ''}${p.draw ? ' · ' + JSON.stringify(p.draw) : ''}`;
    K.text(what, 960, 1052, { font: 'mono', size: 20, color: C.quiet, align: 'center' });
  }

  // the v1 options old map scenes used: focus + focusK, an eased highlight, rowWash, a lifted and carried lantern,
  // per-district questions, chipPos / district / lanternAt / ROW / TYPE for hand-placed marks
  function compat(t) {
    const M = K.map;
    K.bg();
    M.draw(t, {
      t0: 0, focus: 'trust', focusK: K.io(t, 2, 0.8), highlight: { machine: K.io(t, 3, 0.8) },
      pin: '15', pinDrop: K.io(t, 3.4, 0.7, 'back'), pinK: K.io(t, 3.4, 0.25),
      rowWash: { 14: { k: K.io(t, 4.4, 0.6) }, '09': { k: 1, color: C.accent } },
      lanternHide: (i) => (i === 2 ? K.io(t, 5, 0.4) : 0), lanternSway: 2,
      questions: (id) => (id === 'history' ? 0 : 1),
    });
    const L2 = M.lanternAt(2), c = M.chipPos('15'), u = K.io(t, 5, 1.6);
    if (u > 0) M.lantern(t, 2, { x: K.lerp(L2.x, c.x + c.w + 70, u), y: K.lerp(L2.y, c.y - 30, u), glowK: 1.8 });
    const d = M.district('trust');
    const qk = K.io(t, 2.4, 0.8);
    if (qk > 0) K.mark(d.x + 36, d.y + M.ROW.q + 8, K.measure(d.q, { font: 'ui', size: M.TYPE.q }) + 6, qk, { alpha: 0.8, w: 3 });
    const a = K.io(t, 6.6, 0.8);
    if (a > 0) {
      const m = M.chipPos('Identity & keys');
      K.arrow(m.x - 20, m.y + 140, m.x - 4, m.y + 6, { k: a, color: C.accent, bend: -30 });
      K.text('chipPos(\'Identity & keys\')', m.x - 30, m.y + 176, { font: 'mono', size: 26, color: C.accent, alpha: a });
    }
  }

  const scenes = {};
  PLAN.forEach((p) => {
    scenes[p.n] = (t, S) => {
      K.map.use(window.MAPTEST[p.fixture]);
      try {
        if (p.kind.startsWith('intro')) K.map.intro(t, S, { lesson: p.lesson, title: p.title });
        else if (p.kind === 'draw') { K.bg(); K.map.draw(t, p.draw); }
        else compat(t, S);
      } finally { K.map.use(null); }
      label(p);
    };
  });

  LESSON({
    id: '99.97', title: 'Map test', short: 'Map test', module: 'Testing',
    summary: 'Engine test for the data-driven course map (K.map.draw, K.map.intro). Never published.',
    keep: [['Bold lead.', 'Rest of the sentence.']],
    images: {},
    scenes,
  });
})();
