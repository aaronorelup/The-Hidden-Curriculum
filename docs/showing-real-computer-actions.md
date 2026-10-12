# Showing real actions on a computer

Since 2026-10-12 a lesson can show how something is really done and what it really looks like: a real web page being
used, real commands with their real output, a real screenshot being pointed at, a real app on a real desktop. Aaron
asked for it so viewers see the thing they will meet, not only a drawing of it. Everything is recorded by
`tools/capture.py` and played back by the kit (`K.demo`, `K.shot`, `K.termReplay`; reference in `engine/KIT.md`,
"Captures"), so the lesson stays a pure function of time and can be re-rendered and re-recorded from the repo.

Worked example: `lessons/_demo` (never published). Five scenes: 01 a browser capture of the course's own public page
with the automatic camera and a callout on the player's captions; 02 a terminal replay of `python --version`,
`git --version`, `git init` and `git status`; 03 a screenshot from the browser capture animated with a scripted pointer,
two zooms and a click that swaps to the page it opens; 04 a 3D shot made in Blender (docs/blender-shots.md); 05 typing
and a key press on a public documentation page. No scene types in a capture time or position: they read them from the
recipes' `mark` and `shot` steps.

```
python tools/capture.py again _demo site       # re-record the browser capture (public pages only)
python tools/capture.py again _demo term       # re-run the commands
python tools/capture.py again _demo search     # re-record the typing capture
python tools/stills.py _demo --every 0.5       # look at it
python tools/render.py _demo                   # the MP4
```

## The four options

| option | what it records | engine | runs |
|---|---|---|---|
| **Browser capture** (`capture.py browser`) | Playwright drives a clean, throw-away Chromium profile through a steps file (goto, move, hover, scroll, click, type, press, wait, wait_for, mark, shot). The page is filmed with the DevTools screencast at the recipe's device pixel ratio (1024x576 at 1.875 or 1280x720 at 1.5: both a sharp 1920x1080 clip), every action goes to events.json with its time, the pointer path and the target's box, `mark` steps log a named moment with the boxes of the elements you name, and `shot` steps save real screenshots (WebP), of the page on show or, as a side shot, of the page a link leads to | `K.demo`: window chrome with the page's real URL, a smooth drawn pointer (hand over links, I-beam over text), click ripples, an automatic camera that eases toward each click or typing target and back out, a typing chip only while the typed text is too small to read, key chips beside the pointer; `callouts` box and label part of the screen | headless: anywhere Python and Playwright run, no display needed |
| **Terminal replay** (`capture.py terminal`) | real commands run one after another in a throw-away folder (cmd, PowerShell or bash) with a neutral git (no system or global config); each command, its real output line by line (stdout and stderr) and the real timings. The folder's path and your home folder are rewritten to `C:\Users\you\...`, the account name to `you`, the computer name to `DEMO-PC` | `K.termReplay` (or `K.demo` on a terminal capture): each command typed at a human pace, its real output at its real speed, real line wrapping and scrolling; `marks` box a line of output with a label | headless |
| **Screenshots, animated** (`shot` steps, or any screenshot) | a still: a `shot` step of a browser capture, a screenshot an agent took while it worked, or any image in `images: {}` | `K.shot`: the same chrome and camera as K.demo, with a scripted pointer (eased, slightly curved moves, clicks), zoom boxes, typing chips, callouts, and `swap` to the next screenshot when a click changes the page | nothing to record at render time |
| **Desktop capture** (`capture.py desktop`) | a window or a screen region filmed with ffmpeg gdigrab (the OS pointer drawn in) for N seconds while a person or a computer-use agent acts, plus a 30 Hz log of the pointer and the mouse buttons (`GetCursorPos`, `GetAsyncKeyState` for the mouse buttons only) | `K.demo`: the recording with click ripples and the automatic camera on the logged clicks (the OS pointer is already in the video; `--no-mouse` leaves it out and K.demo draws its own) | needs an interactive, unlocked Windows desktop session |

Blender: a shot script in `lessons/<slug>/blender/`, rendered by `tools/blender_shot.py` (docs/blender-shots.md);
`_demo` scene 04. It is the fifth source, for animation rather than real actions.

## When to use which in a conceptual lesson

The course is a map, not a manual (COURSE.md). A recording does not teach the steps; it lets the viewer **recognise** the
thing the first time they meet it. So a recording belongs mostly in "The surprises you'll hit" and "Where it lives"
beats, a few seconds at a time, with the narration saying what to notice and a callout boxing it.

- **What a web page, dashboard or settings page really looks like, and where the thing is on it**: a browser capture.
  If nothing has to move, a single shot with `K.shot` is calmer and smaller.
- **What a command prints, and how fast**: a terminal replay. It is real output, so it carries real version numbers,
  real wording and real warnings (git's `hint:` block after `git init`, a deprecation notice) that a drawing would
  smooth away. Terminal captures use a neutral git (no system or global config) so that the output is what a fresh
  install prints on any machine; on this machine the system gitconfig sets `init.defaultBranch`, which hides that hint.
  `"git_config": "machine"` in the recipe keeps this machine's config instead.
- **What an agent did**: the screenshots it took during its run, animated with `K.shot` (pointer, clicks, zoom boxes,
  `swap` to the screenshot after each click), or a desktop capture of the agent working when the motion itself matters.
- **A native app** (Explorer, VS Code, Task Manager, Windows Settings, an installer): a desktop capture, or one
  screenshot and `K.shot` when a still is enough.
- **A mechanism nobody can see** (bytes, packets, processes, tokens): keep drawing it with the kit. The usual pattern is
  the recording first ("this is what you will see"), then the drawn metaphor ("this is what is going on under it").
- Keep each recording short: 5 to 20 seconds on screen, one idea, one or two callouts. A minute of someone clicking
  around is a tutorial, which the course is not.

**Legibility.** In `DEMO.WIN` (1400 px wide) a recording is shown at 0.73 canvas pixels per video pixel, so a page
recorded at 1280x720 CSS shows its body text at about 12 to 17 px at rest, under the course's 26 px minimum. For a
page meant to be read, record a smaller viewport at a higher pixel ratio: `"size": [1024, 576], "dpr": 1.875` gives the
same sharp 1920x1080 clip with text 25 % larger at rest (the `_demo` recipes do), and the camera's zoom stays crisp
(at 1.75x a 1080p clip is upscaled about 1.28x). Even so, **the narration may only point at what the camera has zoomed
on** (or a callout has boxed): the rest of a page at rest is a picture of a page, not something to read.

## Recording them unattended (an agent producing a lesson)

Browser and terminal captures need no screen, no person and no permissions beyond the network, so a lesson workflow
agent records them the way it renders stills:

1. Write the recipe into the lesson: `lessons/<slug>/steps/<name>.json` (formats in the header of `tools/capture.py`;
   examples in `lessons/_demo/steps/`). This file is the recipe: `capture.py browser|terminal <slug> <name>` and
   `capture.py again <slug> <name>` read it (the capture folder keeps only a copy of what it was last recorded from;
   `again` says when the two differ). Browser: public pages only, real waits (`wait_for` a selector, a text or a
   condition, not long sleeps; wait until the page has settled before measuring it), one `shot` per still the scenes
   need, and a `mark` (with `boxes`) for every moment or element a scene points at. Terminal: harmless commands only
   (versions, `git init` and `git status` in the throw-away folder, `dir`, `where python`); nothing that installs,
   deletes or reaches into your real folders.
2. `python tools/capture.py browser <slug> <name>` (or `terminal`). It records into `<name>.new`, runs `check` (video
   spec, file sizes, secrets scan) and only then replaces the old capture. When a step fails it says which one
   (`step 7 of 12 (wait_for selector=#stage): Timeout 30000ms exceeded`) and the old capture stays as it was.
3. `python tools/capture.py show <slug> <name>` prints the timeline (click at 9.03 s, scroll 4.33-7.34 s, mark
   playing at 12.87 s with its boxes...). **Never type capture times or positions into a scene**: they move with every
   re-record (one re-record of the demo moved every event by 0.36 s; a slow page load moves them by seconds). Read
   them instead: `K.captureAt('site', 'playing')` is the time of a `mark` (or `shot`) step, `K.captureBox('site',
   'course-page', 'stats')` a box it measured (video pixels), `K.capture('site').clicks.find(...)` any recorded event,
   `K.termTimes('term')` a terminal replay's schedule. Scenes use the capture's own clock:
   `K.demo('site', t - S.cue('open'), ...)`.
4. `python tools/stills.py <slug> --scene NN --every 0.5` and look at every frame: what the page showed is what gets
   published.
5. When the site changes, `python tools/capture.py again <slug> <name>` re-records it from the lesson's recipe. Scenes
   that read marks and boxes follow it; look at the stills again anyway (a page can change in ways no mark sees).

**Desktop captures need an interactive session**: a logged-in, unlocked Windows desktop, because gdigrab films what is on
the screen. Two ways to drive it:

- *A person*: run `python tools/capture.py desktop <slug> <name> --seconds 15 --window "Visual Studio Code"`, which
  brings the window to the front and counts down 3 seconds, then do the action.
- *A computer-use agent*: start the same command in the background (`--countdown 2`), then perform the actions with
  the computer-use tools while it records; read the result with `show` and stills. Cheaper and safer when the motion
  does not matter: let the agent take screenshots as it works and animate them with `K.shot`.

The desktop recorder refuses to start when another window covers the target window, and throws the recording away if
one comes in front while it runs (it checks twice a second), so a notification or a chat window cannot end up in a
lesson. It logs only the pointer and the mouse buttons, never the keyboard. A `--region` recording has no such check:
everything visible in the region is filmed.

## Safety rules (hard)

- **Never record real keys, tokens, passwords, emails or personal data.** Use public pages, test accounts and
  `@example.com` addresses. The repository is public on GitHub (every capture under `lessons/`, `_demo` included, is
  published there) and lesson files are published on aaronorelup.com.
- What `capture.py` enforces: it refuses typed text, URLs, commands and terminal output that look like an API key, a
  token, a JWT, a private key, a credential assignment, a real email address, any key stored in `~/.claude/secrets`,
  your home folder's path, or this machine's account or computer name (whole words, any case: `getpass.getuser()`,
  `socket.gethostname()`, `%COMPUTERNAME%`, `%USERDOMAIN%`); in terminal output it rewrites them instead (`whoami`
  prints `DEMO-PC\you`, `hostname` prints `DEMO-PC`). It refuses commands that print the environment: a bare `set`,
  `env`, `printenv`, `export` or `declare` anywhere in the command line (`cmd /c set`, `env | sort`), PowerShell's
  `env:` drive listed (`dir env:`, `gci env:*`, `Get-Item env:*`, `Get-ChildItem -Path env:`),
  `[Environment]::GetEnvironmentVariables()`, `print(os.environ)`, `console.log(process.env)`, and any single
  variable whose name says key, token, secret or pass. Terminal commands run in a throw-away folder with a demo git
  identity (`Demo Learner <learner@example.com>`) and no system or global git config (so your real git name and email
  cannot show); browser captures use a fresh profile with no cookies, logins or extensions; desktop captures check
  that nothing covers the window and never log the keyboard.
- What it cannot catch: names, faces, private documents, someone else's data on a page, a notification, a browser's
  autofill. Look at the stills before committing. For a desktop capture turn on Do Not Disturb and close anything
  private first.
- Blur what must not show: in a browser steps file, `"redact": [{"selector": ".account-email"}]` blurs those elements
  live in the page (they stay blurred while it scrolls, side shots included), and `{"box": [x, y, w, h], "from": 0,
  "to": 4.5}` (CSS pixels, seconds) blurs a fixed area of the video and the shots (a box with no `from`/`to` applies to
  side shots too); desktop steps take the same boxes in pixels of the recorded area (`--steps desktop.json`).
- Other people's sites: prefer Aaron's own site and public documentation (the `_demo` typing scene uses the Python
  docs' search, because aaronorelup.com has no text field), show third-party pages briefly and only what the lesson
  needs, and never log in to a real account on camera.

## File sizes

Cloudflare Pages serves at most **25 MB per file**; `capture.py check` and `media_util.py check` flag anything bigger.
Measured on `_demo` (2026-10-12):

| file | size |
|---|---|
| browser capture `site`, 19.4 s, 1920x1080, CRF 23 (scrolling, a page change, a lesson playing) | 8.2 MB (about 0.42 MB a second) |
| browser capture `search`, 11.0 s (a static page, typing, a results page) | 3.1 MB |
| a static page costs almost nothing; scrolling and video inside the page cost the most | |
| terminal capture (4 commands) | 2 KB of JSON |
| a 1920x1080 shot, WebP quality 92 (the default) | 120 to 145 KB (the same shots as PNG: 0.5 to 1.4 MB). `"lossless": true` is about 30 % under the PNG; `"format": "png"` keeps a PNG |
| the rendered 73 s `_demo` lesson at 1080p (five scenes; with four it ran 58 s and 19.8 MB) | 24.2 MB, just under the limit (render.py makes a 720p copy past 24 MiB) |

**Preload budget.** Every clip, sound and shot a lesson declares is fetched before frame 0 (a streamed file could not
seek on the site), so the page waits for all of it behind "Loading lesson… n %". Keep a lesson's media under about
**15 MB** in all (about 5 s to start on a 25 Mbit/s line; `_demo` is about 13 MB: 11.2 MB of capture clips, 1.1 MB of
3D shot, 0.3 MB of shots) and leave out any shot no scene shows (a capture loads every shot its steps took).
Longer term the player could wait only for the first scenes' media and fetch the rest in the background before their
scenes start; until then, budget.

Keep a capture under about 40 seconds; split a long flow into several captures (one per scene) instead of one long
clip; raise `"crf"` to 26 for a busy page, or record at `"dpr": 1` (a smaller clip, about half the size, softer when
zoomed). Clips, shots and audio are stored in Git LFS (`.gitattributes`).

## How it works (for the next engineer)

- **Browser**: the screencast sends a frame whenever the page changes (about 50 a second while it moves, none while it
  rests). capture.py stamps every action with the same wall clock, then resamples the frames to a constant 30 fps by
  sample-and-hold, **the newest frame at or before each tick** (each output frame's centre), piped to ffmpeg, and
  encodes to the clip spec (`media_util.encode`: H.264, BT.601, GOP 12, no B-frames). Never the nearest frame: after a
  quiet stretch the next frame can be a second away, and taking it early showed the page reacting up to 0.6 s before
  the click that caused it (fixed 2026-10-12; measured on the re-recorded `_demo` clips, the page now changes 0.01 to
  0.31 s after the click or key that caused it, never before). Scrolls are animated inside the page on `requestAnimationFrame`, so each rendered frame shows the
  scroll position for its own moment (no judder); a scroll that cannot move (already at that end) takes no time and
  logs nothing. A `shot` restarts the screencast, which a screenshot can otherwise stall. A side shot reads its link
  when its step runs and opens the page in a second tab after the recording stops, so it costs the video nothing.
- **Recording safely**: every recording goes to `assets/capture/<name>.new/`, is checked, and only then replaces
  `<name>/` (the old one is renamed `.old` and deleted after the swap). A failure deletes `.new` and touches nothing else.
- **Pointer**: the browser is headless, so the video has no pointer; the engine draws one from events.json, resampled
  at 60 Hz and lightly smoothed (Gaussian, 20 ms for browser paths, 60 ms for a desktop log), with the shape the page
  really showed (`cursor: pointer` = hand, `text` = I-beam) sampled along each move.
- **Camera**: built once per capture from the clicks, typing and zoom callouts (`autoCam` in kit.js), as eased
  keyframes like `K.cam`, with the zoom eased in log scale (screen-recording tools do the same: a linear zoom grows the
  picture 1.75 times faster at the start of a 1x to 1.75x move than at its end). The time it must leave (the hold is
  over, or a scroll or page load cuts it short) is worked out first, and a zoom that could not hold still for `minHold`
  (0.6 s) is not made: a click that loads a page at once moves only the pointer. Scripted zooms that follow each other
  within a move pan straight from one to the next. The stage a zoom fills is a rounded panel under the badge band, and
  a zoom never shows past the window's edge. K.shot memoises its camera on everything autoCam reads (pointer script,
  zooms, typing, zoom callouts, `zoom`, `lead`, `hold`, `join`, `camD`, `minHold`, `follow`), so render workers seeking
  out of order always get the same camera.
- **Typing and keys**: a type step records the field's box and font size; K.demo shows the typing chip only while
  that text would be under about 24 px on screen (font size x the clip's scale x the camera's zoom), so it fades out
  as the camera zooms onto the field. Pressed keys show as key chips beside the pointer (flipped left or above near
  the frame's edge).
- **Loading**: `lesson.js` `captures: {}` are loaded by `K.loadMedia` (runtime.js already calls it with the lesson set),
  so the clip is fetched whole before frame 0 like every other video, and both the renderer (frame-exact seeks) and the
  live player (clips played in step with the narration) handle it as the video `'cap:<name>'`.
- **Desktop**: gdigrab stamps its frames with the wall clock (`start:` in its log), which lines the 30 Hz pointer log
  up with the video.
