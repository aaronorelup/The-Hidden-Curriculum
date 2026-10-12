# 01.01 research-now: "Files are just bytes" as of October 2026

Researcher lens: the subject AS IT IS THIS MONTH (researched 2026-10-04). Not viewer prose.
Status tags: **[established]** = true for 1+ year and still true · **[new]** = new within the last 12 months (Oct 2025 to Oct 2026) · **[beta]** = beta, release candidate, announced or rolling out · **[speculation]** = expected or reported, not shipped.
"live doc" = undated or continuously updated vendor documentation, read on 2026-10-04.
Names in the brief: no ambiguous names. ".py" = Python source file. Scope note: showing extensions, renaming, "Open with" and default-app settings belong to 01.02; facts about them are here only so the planner knows what to hand off.

---

## 1. The core fact: a file is a named run of bytes; the extension is part of the name

- Content-based identification: a file's real format is announced (if at all) by its first bytes, its "magic number" or signature, not by its name; the `file` command (libmagic) reads header bytes and matches them against a database. https://en.wikipedia.org/wiki/File_(command) (live) ; https://github.com/file/file (live) **[established]**
- libmagic order: binary patterns first; if none match "and the file looks like text", it determines the text encoding and tries text patterns. That is literally the text/binary split the lesson draws. https://www.mankier.com/5/magic (live) **[established]**
- Real signatures (good on-screen material): PNG starts `89 50 4E 47` ("‰PNG"); PDF starts `25 50 44 46 2D` ("%PDF-"); ZIP starts `50 4B 03 04` ("PK"), and .docx/.xlsx are ZIP files; Windows .exe starts `4D 5A` ("MZ"); Linux executables start `7F 45 4C 46` ("ELF"). https://en.wikipedia.org/wiki/List_of_file_signatures (live) **[established]**
- A .py file has no magic number at all: it is plain text, so its first bytes are just your first line of code (`import`, `#`, or a `#!` shebang line). Python source defaults to UTF-8 since Python 3.0 (PEP 3120, 2007/2008). https://peps.python.org/pep-3120/ (2007) **[established]**
- .ipynb (Jupyter notebook) is also plain text: "simple JSON documents" with metadata, nbformat version and a cells list. Useful contrast: .py and .ipynb are both text, just different shapes of text. https://nbformat.readthedocs.io/en/latest/format_description.html (live, nbformat 5.11) **[established]**

## 2. Who reads the extension: each OS uses the name to pick the app

- Windows: picks the default app by extension through file-type associations (ProgIds, UserChoice registry). Hides extensions for known file types by default in Windows 11; showing them is View > Show > File name extensions. No announcement found (searched 2026-10-04) of Microsoft changing that default. https://lazyadmin.nl/win-11/show-file-extension-windows-11/ (live) ; https://www.elevenforum.com/t/show-or-hide-file-name-extensions-for-known-file-types-in-windows-11.898/ (live) **[established]** (how-to detail belongs to 01.02)
- Windows 11 is testing/rolling "UserChoiceLatest": a new hash on the user's default-app choice that includes a machine ID, so third-party tools can no longer set defaults silently and choices do not roam between machines. Windows 11 only. https://kolbi.cz/blog/2025/04/20/userchoicelatest-microsofts-new-protection-for-file-type-associations/ (2025-04-20) **[new-ish: first seen Apr 2025, still rolling; treat as beta]** (01.02 territory; mention at most as "Windows guards your default-app choice")
- macOS: Finder maps the extension to a Uniform Type Identifier (UTI, e.g. `.jpg` -> `public.jpeg`) in the LaunchServices database, then to the default app. A file with an unknown extension gets an ad hoc "dynamic UTI" (`dyn.…`) and macOS "won't know which app to associate it with". Content sniffing is used by Spotlight and QuickLook, not for picking the app. https://eclecticlight.co/2026/07/29/matching-files-to-apps-how-utis-work/ (2026-07-29) ; https://eclecticlight.co/2025/10/25/explainer-how-does-macos-recognise-file-types/ (2025-10-25) **[established]**
- macOS quirk worth one line: one extension can map to several UTIs and the first wins, e.g. `.ts` resolves to MPEG-2 video before TypeScript. https://eclecticlight.co/2024/04/10/how-macos-opens-a-file-in-the-correct-app/ (2024-04-10) **[established]** (good "the label is just a label" example)
- Linux: desktop file managers use MIME types guessed from extension plus content (libmagic/shared-mime-info); command-line tools mostly ignore extensions entirely. https://dev.to/andrewll/magic-numbers-in-linux-the-unsung-heroes-of-content-identification-kernel-safety-and-modern-os-56c6 (undated, 2025) **[established]** (secondary source; fine for a one-liner)
- Hedge for the script: "the extension tells the OS which program opens it" is right for double-clicking in Windows Explorer and macOS Finder; it is not how programs themselves read files. `python hello.txt` runs fine: Python reads the bytes and does not care about the name. **[established]** (standard behaviour; demonstrable)

## 3. Python on Windows this month (what opens a .py when you double-click it)

- Python install manager (the `py` command) is now the recommended way to install Python on Windows; 25.0 released 2025-10-08. https://www.python.org/downloads/release/pymanager-250/ (2025-10-08) **[new]**
- The traditional full installer is "deprecated since 3.14" and "will not be produced for Python 3.16 or later". https://docs.python.org/3/using/windows.html (live, 3.14.8 docs) **[new]** (deprecation announced with 3.14, Oct 2025)
- The old Python launcher was associated with `.py`, `.pyw`, `.pyc` files; the install manager docs do not clearly state its file-association behaviour. Hedge: do not say on screen which app a double-clicked .py opens on a fresh 2026 machine; it varies (VS Code, Notepad, the Python launcher, or a "How do you want to open this file?" prompt). Same source. **[established/unclear]**
- Python 3.15 makes UTF-8 the default text encoding on every platform (PEP 686, status Final): every text-mode `open()` without `encoding=` uses UTF-8 instead of the locale encoding; opt out with `PYTHONUTF8=0` or `-X utf8=0`; the change mostly affects Windows. https://peps.python.org/pep-0686/ (live; PEP Final) **[beta -> imminent]**
- Release timing: 3.15.0rc3 shipped 2026-10-02; 3.15.0 final "scheduled for 2026-10-09" (pushed back a week for lazy-import fixes). Some blogs already say "3.15 is out"; python.org says otherwise as of 2026-10-04. https://www.python.org/downloads/release/python-3150rc3/ (2026-10-02) **[beta]** -> wording: "Python 3.15, out this month, makes UTF-8 the default everywhere."

## 4. Text files are bytes too: encoding is the agreement between writer and reader

- UTF-8 is used by 99.1% of websites whose encoding is known (W3Techs, September 2026). https://w3techs.com/technologies/details/en-utf8 (2026-09) **[established]**
- Unicode 17.0 (2025-09-09): 159,801 characters, 172 scripts. Text = numbers that stand for characters; UTF-8 is the rule for turning them into bytes. https://blog.unicode.org/2025/09/unicode-170-release-announcement.html (2025-09-09) **[established]**
- Windows Notepad saves UTF-8 without BOM by default since Windows 10 1903 (2019); it reads Unix LF line endings since 2018. Notepad is no longer the place where a .py file "breaks". https://www.bleepingcomputer.com/news/microsoft/windows-10-notepad-is-getting-better-utf-8-encoding-support/ (2019) ; https://www.ghacks.net/2018/05/09/notepad-gets-extended-line-endings-support-in-windows-10/ (2018-05-09) **[established]**
- Notepad in 2026 renders Markdown (bold, tables, nested lists; Insider rollout from 2026-01-21) and has AI "writing tools"; Microsoft removed the Copilot icon/branding from Notepad from April 2026 but the AI features remain, opt-in, need a Microsoft account. https://winbuzzer.com/2026/01/22/microsoft-updates-notepad-with-markdown-and-ai-upgrades-amid-growing-feature-bloat-concerns-xcxwbn/ (2026-01-22) ; https://www.theregister.com/2026/04/13/microsoft_notepad_copilot_icon/ (2026-04-13) **[new]** (relevance: even "plain text" editors now format what they show; the bytes on disk are still plain text)
- The classic Windows encoding trap still exists: Windows PowerShell 5.1 (still the one built into Windows) writes UTF-16LE with `>`, `>>` and `Out-File`; PowerShell 7+ writes UTF-8 without BOM. Same characters, different bytes, and a tool expecting UTF-8 sees garbage or null bytes. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding (updated 2025-09-29) **[established]**
- Line endings: Windows lines end CR LF, macOS/Linux LF. Invisible difference in the bytes, visible in git diffs. https://hackaday.com/2018/05/08/windows-notepad-now-supports-unix-line-endings/ (2018-05-08) **[established]** (name only; git owns the detail)

## 5. The lantern: agents read and write these files for you

- Agent instructions are themselves plain text files: AGENTS.md (OpenAI, Aug 2025; >60,000 open-source projects; used by GitHub Copilot, Cursor and others) became a founding project of the Linux Foundation's Agentic AI Foundation on 2025-12-09, alongside MCP and goose. Claude Code uses CLAUDE.md. https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation (2025-12-09) **[new]**
- Claude Code's file tools (live doc): `Read` returns text with line numbers; images come back "as visual content ... not as raw bytes" (downscaled when large); PDFs read in page ranges (up to 20 pages at a time over 10 pages); `.ipynb` returns cells and outputs (refuses notebooks over 100 MB); `Write` creates or overwrites whole files, "It doesn't append or merge"; `Edit` makes targeted edits; `NotebookEdit` edits notebooks cell by cell. https://code.claude.com/docs/en/tools-reference (live doc) **[established/new]** (mental-model payoff: the agent treats text files and binary files differently, exactly the split this lesson teaches)
- Same doc: before Claude Code v2.1.214 (2026), on Windows PowerShell 5.1 `>` wrote UTF-16LE files, non-ASCII input arrived as `?`, and Python scripts could crash with `UnicodeEncodeError` printing non-ASCII; newer versions force UTF-8. A concrete 2026 example of agents tripping over bytes vs characters. https://code.claude.com/docs/en/tools-reference (live doc) **[new]**
- Agents misjudging files have destroyed them: Gemini CLI (2025-07-21) told to move files into a folder whose creation had failed; on Windows each `move` to a non-existent folder renamed the file instead, each overwriting the last, leaving one file. Days earlier the Replit agent deleted a production database. https://winbuzzer.com/2025/07/26/googles-gemini-cli-deletes-user-files-confesses-catastrophic-failure-xcxwbn/ (2025-07-26) ; https://incidentdatabase.ai/cite/1178/ (2025) **[established]** (useful for "knowing what a file really is so nothing surprises you"; keep to one sentence, not a scare)
- Google Magika 1.0 (Nov 2025): open-source AI model that identifies file types from content (200+ types incl. Jupyter notebooks, NumPy arrays, PyTorch models), ~99% average accuracy, rewritten in Rust; used to scan billions of files daily in Gmail, Drive, Safe Browsing and VirusTotal. AI now does the "look at the bytes, ignore the name" job at scale. https://opensource.googleblog.com/2025/11/announcing-magika-10-now-faster-smarter.html (2025-11) ; https://www.infoq.com/news/2025/12/magika-rust-file-type-detector/ (2025-12) **[new]**

## 6. Why the label matters for safety (a sentence, not a section)

- Double extensions are still a top email-malware trick in 2026: `invoice.docx.exe`, `report.pdf.exe`, `photo.jpg.exe`; they work because Windows hides known extensions by default. Kaspersky's top 15 dangerous attachment types from early-2026 email blasts: .exe, .js, .html, .dll, .bat, .vbs, .xls, .pdf, .jse, .au3, .docx, .htm, .wsf, .scr, .lnk. https://www.kaspersky.com/blog/dangerous-extensions-in-email/56238/ (2026-08-07) **[new]** (data) / **[established]** (technique: MITRE ATT&CK T1036.007, https://attack.mitre.org/techniques/T1036/007/ (live))
- Hand-off: the "turn extensions on" fix is 01.02; security depth is District 5 (module 15).

---

## Traps (things commonly said that are wrong or outdated now)

1. "Renaming a file converts it." No: renaming `photo.png` to `photo.jpg` changes only the label; the bytes still start with the PNG signature. (Section 1)
2. "The extension is what makes a file a Python file." No: the content makes it Python; the extension tells Explorer/Finder which app to launch. `python notes.txt` runs. (Sections 1, 2)
3. "Linux/macOS work the same way as Windows here." Partly: macOS Finder uses extension -> UTI; Linux shells ignore extensions; libmagic reads content. (Section 2)
4. "Notepad will mangle your code / can't handle Unix line endings." Outdated since 2018-2019 (UTF-8 default, LF support). (Section 4)
5. "Python on Windows uses your locale encoding, so always pass encoding=." Becoming outdated: 3.15 (final due 2026-10-09) defaults to UTF-8 everywhere. Still correct advice for code that must run on 3.14 or older. (Section 3)
6. "Install Python from the python.org .exe installer." Outdated direction: install manager (`py`) is the recommended route; the classic installer ends with 3.15. (Section 3)
7. "Python 3.15 is out." Not as of 2026-10-04 per python.org (rc3 2026-10-02, final scheduled 2026-10-09); some blogs jumped the gun. Hedge with "this month". (Section 3)
8. "Text files are just text, binary files are just bytes." Both are bytes; "text" means bytes that follow a character encoding (now almost always UTF-8). (Section 4)
9. "Copilot was removed from Notepad." Only the icon/branding; AI writing tools remain (opt-in). (Section 4)
10. "AI reads a file the way you see it." Agents get text files as text and images/PDFs converted (images downscaled), and can corrupt or overwrite files when they misjudge what is on disk. (Section 5)
11. "Windows will start showing extensions by default." No such announcement found as of 2026-10-04; still hidden by default. (Section 2)
