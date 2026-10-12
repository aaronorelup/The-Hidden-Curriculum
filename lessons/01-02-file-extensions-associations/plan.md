# 01.02 File extensions & associations: content plan (binding)

Planner, 2026-10-05. Sources: research-now.md (the subject this month), research-change.md (autumn 2021 to Oct 2026),
COURSE.md, curriculum.md (all of it), and 01.01's plan and script (this lesson picks up its metaphor).
Second lesson of Module 01 (District 1 · The Machine: what's on your computer). Mid-module lesson.

Target: 8.5 to 11.5 minutes. **14 sections, ~1,435 spoken words, ~10:11 spoken (about 10:30 with gaps)**
(hard rule: 1,190 to 1,610 words, 11 to 17 sections). **No [guest] sections** (lesson is 15 minutes or shorter).
Not a Lantern lesson: AI appears in one lantern section (13) plus the change-arc lines.
Conceptual, not how-to: **no click paths spoken** (no "View > Show > File name extensions"). The screen may show a
setting's *name* as a label ("Show file extensions", "Always", "Just once", "Change All"), never a menu trail.

---

## 1. Purpose line and conclusion

- **Purpose line (first spoken sentence, nothing before it):**
  "In this lesson you'll learn how your computer decides which program opens a file, and how you change that decision."
- **One-sentence conclusion (second sentence):**
  "The extension is a label in the file's name, your computer keeps a table that matches each label to a program,
  renaming changes the label but never the bytes, and Open with and default apps are how you edit that table."
- Optional why-care line: "AI tools now make files for you and pick their labels, and your computer's table still
  decides what opens them."
- Title card: purpose line + "A label in the name, a ledger in the computer."

## 2. As of

**As of October 2026** (researched 2026-10-05). Current releases: Windows 11 version 26H2 (rolling out since
2026-09-29) and macOS 27 Golden Gate (released 2026-09-14). Neither changed extensions or associations in any source
found. Dated facts go on small on-screen cards ("Windows 11 25H2+", "Mar 2023", "Oct 2025"); speech says "this year",
"since twenty twenty-three", "this month".

## 3. The change arc

The core is **unchanged** for decades: the extension is part of the name, the OS keeps a label-to-program table,
renaming converts nothing, and both big desktops still hide extensions by default. What changed is **who may write
the table** (a small security story) and **who makes the files** (the lantern story).

- **Five years ago (autumn 2021):** Windows 11 launched 2021-10-05. One table per user; to switch your default browser
  you had to change each label separately (.htm, .html, .pdf, http, https...), and critics, Mozilla among them, called
  it a step back. Installers could quietly rewrite rows. "Show file extensions" lived in File Explorer's View menu or
  old Folder Options. You created, named and saved every file yourself; AI was Copilot autocomplete inside a file.
  Double-clicking a .py ran it through the python.org launcher.
- **Turning points:** one-click "Set default" for browsers returns (2022-03-28); Microsoft's "principled approach"
  says apps must send you to Settings to ask, not take (2023-03-17); Windows 11 23H2 opens .7z and .rar itself (Oct
  2023: updates edit the table too); a protection driver guards some rows (http, https, .pdf) from other programs
  (Feb 2024); a new, machine-bound record of your choice (A/B-tested Apr 2025; the only one Settings writes on 25H2);
  "For developers" settings renamed **Advanced** (announced May 2025; System > Advanced on 25H2 and later); EU-only
  changes let one "Set default" button rewrite many more rows (Jul 2025); Python's install manager replaces the old
  installer and launcher (Python 3.14, Oct 2025); Claude creates real .docx/.xlsx/.pptx/.pdf files (preview 2025-09-09,
  GA for paid plans 2025-10-21, now all plans); File Explorer "AI actions" on the right-click menu for .jpg/.jpeg/.png
  (rolling out Oct 2025); Windows agent connectors, including a File Explorer MCP connector, reach Insiders (Dec 2025,
  preview); macOS 27 Finder suggests file names from content (Sept 2026).
- **Now (October 2026):** extensions still hidden by default on Windows 11 26H2 and macOS 27. The table is partly
  guarded: for protected types only you, through the OS's own Settings or Open with, can change the row; apps ask.
  AI tools and agents create files and choose their labels; when they show you a file they ask the same table.
  Windows' right-click menu offers different AI actions by file type.
- **Heading (speculation, label it):** more rows protected so only the user can change them (regulation and Microsoft's
  2023 principles point this way); more content-aware fallbacks when there is no label; agents reaching files through
  OS-level, permissioned connectors (preview today). No vendor has announced showing extensions by default or retiring
  extensions; "AI makes extensions obsolete" has nothing behind it.

## 4. MUST-COVER, in script order (one scene per section)

Depth: **teach** = the idea lands with its mechanism; **brief** = two to four sentences, named and shelved;
**one line** = a single sentence. Budget at ~2.35 words per second. Seconds sum to **611 s (10:11)**; with the
pipeline's lead/gap/tail the lesson lands near 10:30, inside 8.5 to 11.5 minutes.

| # | Section (working heading) | Must-cover topics (depth) | Words | Seconds |
|---|---|---|---|---|
| 01 | The point | Purpose line; conclusion: label in the name, a table in the computer, renaming changes the label not the bytes, Open with and default apps edit the table (teach, as a headline); why care: AI tools make files and pick labels now (one line) | 60 | 25 |
| 02 | Where it lives: the rename Aaron didn't know | Map pin: District 1 The Machine, Module 01, second stop (one line); recap of 01.01 in one breath: beads inside, a tag outside (one line); Aaron, who made this course, saved Python in Notepad as dot T X T and didn't know renaming it to dot P Y was the fix; this lesson is the *why* behind that rename (brief, third person, nothing added) | 75 | 32 |
| 03 | The porter and the ledger | Mental model (teach): the porter (Windows, Mac) reads only the tag, looks it up in a ledger at the desk, and carries the string to the door written there; the ledger = file associations; the beads are never opened on the way (teach); there is one ledger per user account, so two people on one PC can get different programs (one line) | 110 | 47 |
| 04 | What a ledger row holds | A row is more than a door: the program, the icon, the type's name in the folder ("Python file", "Text document"), and the right-click menu's commands (teach, Microsoft's own list); that's why a renamed file's icon changes instantly while no byte moves (teach); a label with no row gets a blank icon and a question (one line, set up for 12) | 100 | 43 |
| 05 | The folded tag: hidden extensions | Windows 11 and macOS still hide most extensions by default in 2026, with no announced change (brief); the tag is folded, so `hello.py.txt` shows as `hello.py` (teach: you can't edit a label you can't see); showing them is one setting on each OS (one line, no click path); on Windows 25H2 and later that setting sits on a page now called Advanced, formerly For developers (one line, on-screen label "Advanced"); on a Mac hiding is per file as well as global, so two files in one folder can differ (one line); people who build things nearly always switch extensions on (one line, framed as common practice, not a step) | 105 | 45 |
| 06 | Renaming: a new tag, the same beads | Renaming rewrites the tag; the beads stay put; Microsoft: renaming won't convert the file (teach); dot T X T to dot P Y works because the beads were already Python text (teach, pays off Aaron's story); `photo.png` to `.jpg` or `.mp3` to `.wav` converts nothing: real conversion is Save As or Export inside an app (brief); the warning both OSes show ("the file might become unusable" / "Keep .txt or Use .py") is the porter warning you the row will change (one line); the classic trap: with extensions hidden, or Notepad's Save As set to text documents, typing `hello.py` can produce `hello.py.txt` (brief, hedged "can", not "always"; do NOT say it happened to Aaron) | 130 | 55 |
| 07 | Open with: just once or always | Open with = telling the porter which door, for this file (teach); two kinds of answer: a one-time choice that leaves the ledger alone, or an always choice that rewrites the row (teach; on-screen "Just once" / "Always"); on a Mac, Open with in Get Info changes one file unless you press Change All; a Mac can remember a choice per file, Windows only per label (brief) | 100 | 43 |
| 08 | Default apps: the whole ledger | Default apps in Windows Settings is the ledger itself: look it up by label (a row) or by app (every row an app claims) (teach); proof it's per label: at Windows 11's launch in 2021, switching browsers meant changing each label one by one; a one-click Set default came back in March 2022 (brief, change arc); in Europe since July 2025 that button rewrites many more rows at once (one line, "in Europe") | 115 | 49 |
| 09 | Who gets to write in the ledger | You, installers and updates all write rows: installing an editor or Python can claim `.py`; a 2023 Windows update taught the porter to open `.7z` and `.rar` itself (brief); Microsoft's 2023 rule: apps should send you to Settings to ask, not quietly take the row (brief); since 2024 Windows guards some rows (web links, PDF) so only you can change them, and since 2025 it records your choice in a new, locked form (brief, no driver/registry names spoken); side effect: a new default sometimes "doesn't stick" until you reset defaults (one line, hedged "sometimes"); people still report apps grabbing file types (one line, hedged, no app named) | 110 | 47 |
| 10 | Where the picture breaks | Not one ledger: Windows keeps its table in the registry, a Mac maps the label to a type and then an app (and keeps per-file choices), Linux desktops also peek at the contents and keep your choices in a plain text file (brief, nouns on screen only); the porter only works the front door: name the program yourself, `python notes.txt`, and no ledger is consulted (teach); so double-clicking `script.py` and typing `python script.py` can run different Pythons: the double-click uses whatever Python the ledger points at, not your project's (brief, venvs named only); the web uses a different label altogether: the server's Content-Type, not the extension (one line) | 120 | 51 |
| 11 | A second ledger inside your editor | Apps keep private ledgers too: V S Code picks its colours and checks (its "language mode") from the extension, and you can remap it (teach); so `hello.py.txt` opens in Notepad *and* gets no Python colours in V S Code: two tables, one label (brief); when there's no label, V S Code guesses the language from the content (one line); AI-era labels are promises about which loader to use: dot safetensors vs older pickle-based `.ckpt`/`.pt` model files, dot G G U F for local models, and MCP bundles that are zips wearing their own label like dot docx (brief, one sentence each at most; renaming `.ckpt` to `.safetensors` doesn't make it safe, it just won't load) | 95 | 40 |
| 12 | The surprises you'll hit | Double-click a dot P Y and a window may flash and close: it ran, it didn't open for editing (or an editor opens; depends on the machine) (brief); "How do you want to open this file?" means the label has no row (one line); a default you set "doesn't stick" after an upgrade (one line, hedged, link to 09); a file with no extension at all gets a blank icon and the question (one line); the icon changed after a rename but the file won't open: the new row's program can't read those beads (one line); `invoice.pdf.exe` named once as the other face of the folded tag, owned by 15.17 (one line, no scare) | 100 | 43 |
| 13 | The lantern: AI makes the file, the ledger still opens it | Change arc: five years ago you created and named every file; since 2025 chat assistants like Claude hand you real Word, Excel, PowerPoint and PDF files, and coding agents write project files with labels they choose (brief); when an agent *shows* you a file it asks the same porter; when it *runs* code it names the program and skips the ledger (teach, ties to 10); Windows' right-click menu now offers AI actions by type, for example image tools only for JPEG and PNG (one line, "rolling out", "varies by market"); Windows is previewing a File Explorer connector for agents that reports the extension as its own field and works only in folders you allow (one line, "preview"); macOS 27 suggests file names from content, but the label part still picks the app (one line); heading: more permissioned agent access to files, more guarded rows (one line, "the direction looks like") | 130 | 55 |
| 14 | Keep this (+ safe to ignore) | Safe to ignore for now: the registry, ProgIDs, Mac type identifiers, Linux MIME files, and every menu path (one line); three takeaways: **The extension is a label in the name.** / **Your computer keeps a ledger from label to program.** / **Renaming changes the label; Open with and default apps change the ledger.** Next stop named neutrally on the map (01.03 Folders, paths & the working directory), no teaser | 85 | 36 |
| | **Total** | | **1,435** | **611** |

Notes for the scriptwriters:
- One idea per sentence, second person, spelled for the ear: "dot P Y", "dot T X T", "dot P N G", "dot J P G",
  "dot E X E", "V S Code", "P D F", "dot G G U F". The screen carries literals (`hello.py.txt`, `.safetensors`,
  `python notes.txt`, "Just once", "Always", "Change All", "Advanced").
- The words "file association" and "default app" must each be said at least once, tied to the ledger, so viewers
  recognise them in Settings.
- Aaron's story: only the true parts in COURSE.md (Notepad, `.txt`, didn't know to rename to `.py`, IT degree).
  The `hello.py.txt` trap is "the classic trap", never told as his.
- No click paths; no "go to Settings > ...". "It's one setting" is the most how-to the narration gets.

## 5. DEFERRED (introduced here, taught elsewhere)

| Topic | Owner |
|---|---|
| Double extensions (`invoice.pdf.exe`), Mark of the Web, risky attachment types; pickle model files that run code when loaded | 15.17 |
| Text encoding (why a renamed file shows garbled characters) | 04.07 |
| Folders and paths ("Show full path in title bar") | 01.03 |
| Hidden files and dotfiles ("Show hidden and system files") | 01.04 |
| Typing a file name as a command; PATH and PATHEXT | 01.05 |
| OS differences in depth (Mac type identifiers, Linux MIME database, line endings, case sensitivity) | 01.08 |
| Local model files (`.gguf`, `.safetensors`) and running models | 01.10 |
| Windows AI actions, Copilot in File Explorer, what each assistant can see | 01.11 |
| Script files (`.bat`, `.ps1`, `.sh`): double-click vs run | 02.06 |
| Commands and arguments (`python script.py`) | 02.04 |
| Editor vs IDE | 03.01 |
| V S Code settings, language modes, extensions | 03.02 |
| Coding agents creating, reading and editing files | 03.08 |
| Instruction files (AGENTS.md, CLAUDE.md) | 03.09 |
| Data formats (JSON, YAML, Markdown) | 04.06 |
| Which Python a double-click runs; the Python install manager and `py` | 05.01 |
| What running a file really means | 05.02 |
| Virtual environments (`.venv`) | 05.03 |
| Agents renaming or overwriting files; git as the undo | 08.11 |
| Git status in File Explorer (Insider beta) | 08.02 |
| MIME types and Content-Type on the web | 09.06 |
| MCP, and Windows' MCP agent connectors | 10.08 |
| MCP bundles (`.mcpb`) and installing servers | 10.09 |
| Agent permissions, Windows Agent Workspace, folder access prompts | 14.12 |
| Prompt injection through files an agent opens | 15.15 |
| How executables run (`.exe`, `.app`) | 17.03 |
| Code signing, SmartScreen, Gatekeeper | 17.05 |
| What installers write (registry, associations) | 17.06 |
| Leftover associations after uninstalling | 17.08 |
| Phone "default apps" (iOS 18.2 Default Apps) | 18.03 |
| URL schemes and link types (`mailto:`, `vscode://`): how a link opens an app, and why one can open the wrong one | NEW: Module 09 ("Links that open apps: URL schemes and deep links") |

## 6. Mental model

**The porter and the ledger** (continues 01.01's string of beads with a paper tag, and its porter). The file is the
string of beads; the tag is the name; the porter is the operating system's file manager (Explorer, Finder); the
**ledger** at the porter's desk is the association table. It persists and transforms:

1. (02) 01.01's string with the tag `hello.txt` returns.
2. (03) The porter reads the tag, runs a finger down the ledger, finds `.txt -> Notepad`, carries the string to that
   door. The beads are never untied.
3. (04) One ledger row opens up into columns: door (program), icon stamp, type name, right-click menu.
4. (05) The tag folds at the last dot: `hello.py.txt` shows as `hello.py`. A small hand unfolds it (the setting).
5. (06) The tag is rewritten (`hello.txt -> hello.py`); the beads don't move; the porter now reads a different row and
   the icon changes. A second string `photo.png -> photo.jpg`: same beads, the new door can't read them.
6. (07) A note handed to the porter: "this once, door X" (row untouched) vs a pen rewriting the row ("Always").
7. (08) The whole ledger opened as a book: by label (rows) or by app (a column of rows one app claims).
8. (09) Other hands reach for the pen: an installer, an update; some rows go behind glass that only you can open.
9. (10) Three different ledgers side by side (Windows, Mac, Linux); a person walks a string straight to a door,
   bypassing the porter (`python notes.txt`); a parcel from the web arrives with a different label (Content-Type).
10. (11) Inside the door, a small second ledger (the editor's) decides how to colour the beads.
11. (13) A lantern-lit hand (the agent) ties a new tag on a new string, then either asks the porter (show) or walks to
    the door itself (run).
12. (14) End card: one string, one tag, one ledger.

**Where it breaks (say it plainly in 10):** there isn't one ledger or one porter. Windows, macOS and Linux keep the
table differently; a Mac can remember a choice per file and goes label -> type -> app; Linux desktops also peek at
the beads. The porter only works the front door (double-click, Open with, the OS's "open this" commands): any program
you name yourself ignores the ledger. And the web doesn't use the tag at all.

## 7. Cut list

- **Click paths and menu trails** (View > Show, Folder Options, Get Info steps, Settings > Apps > Default apps): the
  course is a map, not a manual. Names of settings on screen only.
- **Registry keys, ProgIDs, verbs, UserChoice / UserChoiceLatest, the hash, UCPD.sys, SetUserFTA**: mechanism trivia
  with no mental-model payoff; spoken as "Windows guards some rows" and "records your choice in a locked form".
- **The full EEA type list (.mht, .shtml, .svg, ftp, read...)**: one line "in Europe, one button rewrites many rows".
- **Mac UTI hierarchy (`public.swift-source -> public.plain-text`), `dyn.` types, LaunchServices; Linux `xdg-mime`,
  `mimeapps.list` paths, shared-mime-info**: nouns on screen in 10 at most; depth is 01.08.
- **Drawing one exact Open with dialog**: the redesigned "Just once / Always" dialog could not be confirmed as the
  retail default on 26H2; show generic one-time vs always, not a screenshot-like mockup.
- **Microsoft Store suggestions inside Open with** (Insider, Dec 2025): beta, ad-like, not a mental-model point.
- **The Claude Desktop "re-registers file types" bug report** (Sept 2026): one user's report, closed as invalid in the
  wrong tracker; naming an app on thin evidence is unfair. Kept only as an unnamed hedged line in 09.
- **Codex `vscode://` links opening the browser in Cursor**: niche; link types belong to the NEW URL-schemes lesson.
- **Native .7z/.rar details, 26H2 archive formats, WordPad removal**: one example of "updates write rows" is enough.
- **iOS 18.2 Default Apps**: phones key defaults on tasks more than extensions; 18.03.
- **Agent Workspace, separate agent accounts, "Allow always / Ask every time"**: permissions depth is 14.12.
- **Gemini CLI rename-overwrote-files story**: dramatic, but it's about agents and moves (08.11), and 01.01 cut it too.
- **Magika, magic numbers, AGENTS.md, encoding, invisible characters**: taught in 01.01; no repeat.
- **Double-extension malware detail, Kaspersky's attachment list, Mark of the Web**: 15.17; one line in 12 only.
- **Python install manager versions (26.3, 26.4 beta), PEP 773, the deprecated installer**: 05.01; here only "the
  double-click runs whichever Python the ledger points at".
- **Why Microsoft and Apple hide extensions by default**: no sourced reason in the research; don't speculate.

## 8. Facts to handle carefully

| Claim | Status | Use this wording |
|---|---|---|
| Extensions hidden by default | Still true on Windows 11 26H2 and macOS 27; no announced change (searched 2026-10-05) | "Windows and Mac still hide most extensions by default." Never "Windows shows them now". |
| Where the Windows setting lives | "For developers" renamed **Advanced**; System > Advanced on 25H2 and later | Screen label "Advanced (formerly For developers)". Spoken: "a settings page Windows now calls Advanced". Don't speak a path. |
| Renaming converts nothing | Microsoft and Apple docs, live 2026 | "Renaming changes the name, not the contents. Converting is Save As or Export inside an app." |
| `hello.py` becoming `hello.py.txt` | Depends on hidden extensions and whether `.py` is a known type on that PC | "can end up as hello dot P Y dot T X T". Never "always". Not Aaron's story. |
| Open with: one-time vs always | True on both OSes; exact Windows dialog design varies by machine | "a one-time choice, or an always choice". Mac: "Change All". Don't draw one dialog as THE dialog. |
| Windows 11 launch browser defaults | Oct 2021 per-type only; one-click "Set default" back 2022-03-28 (KB5011563) | "When Windows 11 launched in 2021, switching browsers meant changing each label one by one. A one-click button came back the next spring." Mozilla quote not needed. |
| EU default changes | EEA only, from July 2025 | "In Europe, since last year, ..." Never worldwide. |
| Apps must ask | Microsoft blog 2023-03-17 (a policy commitment) | "Since twenty twenty-three, Microsoft's rule is that apps should send you to Settings to ask." "should", not "can't". |
| Guarded rows | UCPD since Feb 2024 (found by a researcher, Microsoft didn't announce it) for http, https, .pdf (later more Office types); UserChoiceLatest from 2025 | "Since twenty twenty-four, Windows guards some rows, like web links and P D Fs, so only you can change them." No driver names, no claim it covers every type. |
| Default "doesn't stick" | Reported Sept 2026 after upgrades; fix is Reset in Default apps | "Sometimes, after an upgrade, a new default doesn't stick until you reset your defaults." Hedged, no build numbers. |
| Apps grabbing file types | Users report it (incl. an unconfirmed Sept 2026 report about an AI app) | "People still report apps grabbing file types." Name no app. |
| Windows opens .7z/.rar natively | 23H2, Oct 2023 | "A twenty twenty-three update taught Windows to open seven Z and RAR archives itself." |
| Double-clicking a .py | Varies: runs (window flashes) via launcher/install manager, or an editor that claimed .py, or "How do you want to open this?" | "What happens depends on the machine. Often it runs and the window closes before you can read it." |
| Double-click uses global Python, not your project's | Python install manager association (PEP 773); Feb 2026 discussion | "The double-click runs whichever Python the ledger points at, not your project's." No version numbers. |
| `python notes.txt` runs | Python docs, established | "Python will run notes dot T X T if you name it." |
| Linux peeks at content | freedesktop shared-mime-info uses name and content | "Linux desktops also peek at the contents." |
| Web uses Content-Type | MDN, established | "On the web, the server's label decides, not the extension." |
| V S Code language mode from extension; detection when none | VS Code docs (live); detection since 1.60 (2021) | "V S Code picks its colours from the extension, and guesses from the content only when there's no label." |
| `.safetensors` vs `.ckpt`/`.pt` | safetensors default in Transformers 2023; PyTorch 2.6 (Jan 2025) safer load by default | "Older model files could run code when loaded; dot safetensors was made so they can't. Renaming doesn't make a file safe; it just won't load." Detail -> 15.17. |
| `.mcpb` | Renamed from `.dxt` Sept 2025; a zip with a manifest | "MCP bundles are zips wearing their own label, like a Word file." (screen: `.mcpb`). |
| Claude creates files | Preview 2025-09-09, GA paid 2025-10-21, now all plans | "Since twenty twenty-five, assistants like Claude hand you real Word, Excel, PowerPoint and P D F files." |
| Agents show via OS opener, run by naming the program | Mechanism established (`start`, `open`, `xdg-open`); per-tool behaviour varies | "When an agent shows you a file, it usually asks the same porter; when it runs code, it names the program." Keep "usually". |
| File Explorer AI actions by type | Rolling out since Oct 2025; image actions only .jpg/.jpeg/.png; varies by market | "Windows has started adding AI actions to the right-click menu, and which ones you get depends on the label." Card: "Oct 2025 · varies by market". |
| Windows File Explorer MCP connector | Prerelease/preview; known folders only; needs permission | "Windows is previewing a way for agents to reach files, only in folders you allow, and it still reports the extension as its own field." Always "preview". |
| macOS 27 suggested file names | New, Sept 2026, on by default; sources silent on extensions | "macOS twenty-seven now suggests file names from what's inside." Never claim it changes extensions. |
| Heading-to claims | Speculation | "The direction looks like..." / "Expect more ..." Never as fact. No "extensions are going away". |
| Aaron's story | COURSE.md, true | Third person: "Aaron, who made this course, saved Python in Notepad as dot T X T, and didn't know renaming it to dot P Y was the fix." Nothing added. |
