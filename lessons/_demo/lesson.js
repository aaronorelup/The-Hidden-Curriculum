/* _demo: how a lesson SHOWS real actions on a computer (tools/capture.py + K.demo, K.termReplay, K.shot). NEVER publish.
   The timeline (cues.json) is synthetic, with no narration, like _mediatest. Five scenes:
     01  a real browser capture of public pages (assets/capture/site), K.demo with the automatic camera and one callout
     02  a terminal replay of real commands (assets/capture/term), K.demo -> K.termReplay
     03  a real screenshot taken during the browser capture (site/course-page), K.shot with a scripted pointer, zoom boxes
         and a click that swaps to the page it opens (site/latest-lesson, a side shot)
     04  a 3D shot made in Blender from blender/course_map.py (the course map rising, lanterns swinging), K.video in a
         calm frame, district names pinned to the blocks with SHOT() (scenes/00-shot-course_map.js)
     05  typing and a key press on a public docs page (assets/capture/search): the focusing click, the camera on the
         field, the Enter key chip beside the pointer, the results page
   Every capture time and position the scenes use comes from mark and shot steps (K.captureAt, K.captureBox).
   Re-record the captures from the repo (public pages only, nothing personal; the recipes are steps/*.json):
     python tools/capture.py again _demo site
     python tools/capture.py again _demo term
     python tools/capture.py again _demo search
   Re-render the 3D shot from its script (GPU: reserve a gpu-queue slot first; docs/blender-shots.md):
     python tools/blender_shot.py _demo course_map
   Review: python tools/stills.py _demo --every 0.5 ; python tools/render.py _demo */
LESSON({
  id: '99.97', title: 'Showing real computer actions', short: 'Showing real computer actions', module: 'Testing',
  summary: 'Demo of capture.py and K.demo, K.shot, K.termReplay. Never published.',
  keep: [['Show, then explain.', 'A real recording carries what a drawing cannot: what it really looks like.']],
  captures: { site: 'assets/capture/site/', term: 'assets/capture/term/', search: 'assets/capture/search/' },
  videos: { course_map: 'assets/video/course_map.mp4' },
  badgeBacking: true,
  transition: { '04': 'dip', '05': 'dip' },
});
