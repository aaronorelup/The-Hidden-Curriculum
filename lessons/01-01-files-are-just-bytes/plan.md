# 01.01 Files are just bytes: content plan (binding)

Planner, 2026-10-04. Sources: research-now.md (the subject this month), research-change.md (autumn 2021 to Oct 2026),
COURSE.md, curriculum.md (all of it). First lesson of Module 01 (District 1 · The Machine: what's on your computer).

Target: 3.5 to 5.5 minutes. **8 sections, ~690 spoken words, ~4:55** (hard rule: 490 to 770 words, 6 to 9 sections).
**No [guest] sections** (lesson is under 15 minutes). Not a Lantern lesson: AI appears as one lantern section (07).
Conceptual, not how-to: no click paths, no menu names, no "here's how to turn extensions on" (that is 01.02).

---

## 1. Purpose line and conclusion

- **Purpose line (first spoken sentence, nothing before it):**
  "In this lesson you'll learn what a file really is, and what the little ending on its name, like dot P Y, actually does."
- **One-sentence conclusion (second sentence):**
  "Every file is just a row of numbers called bytes; the extension is part of the file's name, a label that tells your
  computer which program to open it with, not what is inside."
- Optional why-care line: "Agents now read and write these files for you, so knowing what a file really is keeps
  you from being surprised by what they do."
- Title card: purpose line + "Bytes inside, a label outside."

## 2. As of

**As of October 2026** (researched 2026-10-04). Dated facts go on small on-screen cards ("W3Techs, Sep 2026",
"Linux Foundation, Dec 2025"); speech says "this month", "last year", "since 2025".

## 3. The change arc

The core idea **did not change** in five years, or fifty: a file is a named run of bytes, text is bytes read through an
agreed code, and the extension is part of the name. What changed is around it, and the lantern part (agents) is new:

- **Five years ago (autumn 2021):** you created, named and saved every file yourself; AI was Copilot's autocomplete
  preview inside a file you had open. Python on Windows read text with the local code page unless told otherwise, so the
  same file could read differently on two machines. Notepad was plain; WordPad was the "rich" one.
- **Turning points:** WordPad removed from Windows 11 24H2 (Oct 2024); Notepad shows formatting stored as Markdown
  (general release Jul 2025: the bold you see is `**` in the bytes); MCP and its filesystem server let AI apps read and
  write folders you allow (Nov 2024); Claude Code and other coding agents create, edit and read files directly (2025);
  AGENTS.md (Aug 2025) handed to the Linux Foundation's Agentic AI Foundation (2025-12-09); Google's Magika 1.0, an AI
  model that identifies file types from their bytes, not their names (Nov 2025); UTF-8 on ~99% of websites (W3Techs,
  Sep 2026); Python 3.15 makes UTF-8 the default everywhere (final scheduled 2026-10-09).
- **Now (October 2026):** agents read and write your files; they read a file by its type (text as text, images as
  pictures, notebooks as cells), and plain-text files with conventional names (AGENTS.md, CLAUDE.md) are how you
  instruct them. Windows and macOS still hide known extensions by default.
- **Heading (speculation, label it):** text encoding is settling on UTF-8 everywhere; more tools (security scanners,
  editors, agents) judge a file by its bytes as well as its name, with the extension staying the computer's first,
  cheapest guess; more files whose *name* is an instruction to an AI.

## 4. MUST-COVER, in script order (one scene per section)

Depth: **teach** = the idea lands with its mechanism; **brief** = two to four sentences, named and shelved;
**one line** = a single sentence. Budget at ~2.35 words per second. Seconds sum to **294 s (4:54)**.

| # | Section (working heading) | Must-cover topics (depth) | Words | Seconds |
|---|---|---|---|---|
| 01 | The point | Purpose line; conclusion (bytes inside, label outside) (teach, as a headline); why care: agents handle files for you now (one line) | 55 | 23 |
| 02 | Where it lives | Map pin: District 1 The Machine, Module 01, first stop (one line); Aaron, who made this course, wrote Python in Notepad as a dot T X T and didn't know renaming it to dot P Y was the whole difference, despite an IT degree (brief, third person, no invented details) | 70 | 30 |
| 03 | A string of beads with a tag | The mental model: a file is a string of beads, each bead one byte, a number from 0 to 255 (teach); the paper tag is the name, and the part after the last dot is the extension (teach); the computer stores and moves beads; it never "knows" what they mean (one line) | 85 | 36 |
| 04 | Text is an agreement | Text is bytes read through a code card: UTF-8 maps numbers to letters (teach); a dot P Y file is a text file whose letters happen to be Python, and nothing in the bytes says "Python" (teach); wrong code card = garbled characters (one line); what you see is a rendering: Notepad now shows Markdown bold that is really `**` in the bytes (one line); UTF-8 on about 99% of websites, and Python 3.15, due this month, makes it the default everywhere (one line, hedged) | 105 | 45 |
| 05 | The tag only picks the program | Windows Explorer and macOS Finder read the extension to choose which program opens the file on a double-click (teach); renaming changes zero bytes (teach); programs themselves mostly ignore the tag: Python will run `notes.txt` (brief); binary files often carry a stamp in their first beads (PNG, PDF, ZIP; a .docx is a ZIP inside) that tells the real format whatever the tag says (brief); where the metaphor breaks: the tag isn't tied to the beads, the folder keeps the name separately (one line) | 110 | 47 |
| 06 | The surprises you'll hit | Hidden extensions are still the default on Windows and macOS, so "hello.py" can really be `hello.py.txt` (brief, no how-to: 01.02); renaming `photo.png` to `.jpg` doesn't convert it (one line); strange characters like `Ã©` mean the wrong code card was used (one line); double-clicking a .py file opens different things on different machines (one line, hedged); `invoice.pdf.exe`: a label can lie, which is why attackers love hidden extensions (one line, no scare) | 100 | 43 |
| 07 | The lantern: agents and your files | Agents read and write files in your project now (brief, change arc: five years ago you made every file yourself); they read by type: text as text, images as pictures, not raw bytes (one line); instruction files like AGENTS.md and CLAUDE.md are plain text whose *name* tells the agent to read them, the same trick as an extension (brief); Google uses an AI model to identify files from their bytes, not their names (one line); invisible characters can sit in a text file an agent reads (one line, points to 15.15) | 95 | 40 |
| 08 | Keep this (+ safe to ignore) | Safe to ignore for now: hex, bits, UTF-16, byte-order marks, line-ending bytes (one line); three takeaways: **A file is just bytes.** / **Text is bytes plus an agreement (UTF-8).** / **The extension is a label that picks the program, not the contents.** Next stop named neutrally on the map (01.02 owns showing and changing extensions), no teaser | 70 | 30 |
| | **Total** | | **690** | **294** |

Notes for the scriptwriters:
- One idea per sentence, second person, spelled for the ear: "dot P Y", "dot T X T", "U T F eight", "P N G", "P D F".
  The screen carries literals (`.py`, `hello.py.txt`, `89 50 4E 47`, `%PDF-`, `PK`).
- On-screen stamps: show at most two (PNG `‰PNG`, PDF `%PDF-`) and say "PNG pictures start with the same few bytes"
  rather than reading hex aloud.
- Aaron's story: only the true parts in COURSE.md (Notepad, `.txt`, didn't know to rename to `.py`, IT degree).

## 5. DEFERRED (introduced here, taught elsewhere)

| Topic | Owner |
|---|---|
| Showing hidden extensions, renaming, "Open with", default apps; Windows' protected default-app choice (UserChoiceLatest) | 01.02 |
| Folders, paths, where a file lives | 01.03 |
| Dotfiles and hidden files (`.git`, `.env`, `.venv`) | 01.04 |
| Line endings (CR LF vs LF), OS differences, macOS type-identifier quirks (`.ts` as video) | 01.08 |
| How bytes are physically stored (disk) | 01.09 |
| PowerShell `>` writing UTF-16 vs UTF-8; redirects | 02.05 (shells: 02.02) |
| Text editor vs IDE; what Notepad now does (Markdown, AI writing tools) | 03.01 |
| Notebooks (`.ipynb` is JSON text) | 03.06 |
| Coding agents' Read / Write / Edit tools | 03.08 |
| Instruction files (AGENTS.md, CLAUDE.md, SKILL.md) | 03.09 (skill marketplaces: 10.12) |
| Data formats (JSON, Markdown, YAML...) as kinds of text | 04.06 |
| Unicode, code points, UTF-8 vs UTF-16, mojibake in depth | NEW: Module 04 ("Text encoding: Unicode, UTF-8 and garbled characters") |
| Which Python opens a double-clicked .py; the Python install manager and `py` | 05.01 |
| What running a file really means (interpreter reads your text) | 05.02 |
| MCP filesystem server | 10.08 |
| MIME types / Content-Type (how the web labels bytes) | 09.06 |
| Agents overwriting or destroying files; why git makes it undoable | 08.11 (agent permissions: 14.12) |
| Hashing vs encryption vs "encoding" (the word means something else there) | 15.05 |
| Invisible Unicode in rules files; prompt injection via files | 15.15 |
| Double-extension malware, Mark of the Web, dangerous attachment types | NEW: Module 15 ("Dangerous files: double extensions, Mark of the Web, risky attachments") |
| How executables run (`MZ`, ELF, `.app`) | 17.03 |

## 6. Mental model

**A string of beads with a paper tag.** Each bead is one byte: a number from 0 to 255. The tag is the file's name; the
word after the last dot is the extension. It persists and transforms across scenes:

1. (03) Plain beads, numbers only; the tag reads `hello.txt`.
2. (04) A **code card** (UTF-8) slides over the beads and they read as letters: `print("hi")`. Same beads, now text.
3. (05) The tag is swapped to `hello.py`: the beads don't move. A porter (the OS) reads only the tag and carries the
   string to a program's door. A second string (a picture) has a **stamped first bead** (`‰PNG`); its tag says `.jpg`:
   the tag lies, the stamp doesn't.
4. (06) The tag folds over, hiding its end (`hello.py.txt` shows as `hello.py`).
5. (07) A lantern-lit hand (the agent) picks up the string, reads the tag and the beads.
6. (08) End card: one string, one tag.

**Where it breaks (say it plainly in 05):** the tag isn't tied to the beads. The folder keeps the name, size and dates
separately, which is why renaming is instant and moves no bytes. And the tag has no power of its own: only programs
that choose to read it (Explorer, Finder, an agent looking for AGENTS.md) act on it; Python will happily run beads with
any tag. (Unspoken: on disk a file can be split into pieces; skip.)

## 7. Cut list

- **Hex dumps, bits, binary arithmetic**: one stamp is enough; reading hex aloud kills a 5-minute lesson.
- **UTF-16, byte-order marks, code pages, Unicode 17/18 character counts**: precision without a mental-model payoff; owned by the NEW encoding lesson.
- **How to show extensions / Open with / default-app settings / UserChoiceLatest**: 01.02.
- **macOS UTIs, Linux MIME databases, libmagic internals**: one-OS trivia; "Explorer and Finder read the tag" covers it.
- **Python install manager, `py` launcher, what a double-click runs on a fresh machine**: varies by machine; 05.01.
- **Notepad AI writing tools / Copilot icon removal**: news, not a mental model.
- **Malware arms race (macros to ISO to LNK to OneNote), `.zip` and `.mov` domains, Kaspersky's attachment list, Mark of the Web**: security depth belongs in Module 15; one line on `invoice.pdf.exe` only.
- **Gemini CLI and Replit file-destruction stories**: Replit was already told in 00.06; a scare story here would overshadow the idea.
- **Rules File Backdoor details, ASCII Smuggler**: one line pointing to 15.15.
- **CR LF vs LF**: invisible-byte detail for 01.08 and git.

## 8. Facts to handle carefully

| Claim | Status | Use this wording |
|---|---|---|
| Python 3.15 makes UTF-8 the default | Final not released as of 2026-10-04 (rc3 2026-10-02, final scheduled 2026-10-09) | "Python 3.15, due this month, makes UTF-8 the default everywhere." Never "is out". |
| UTF-8 share | W3Techs, Sep 2026: 99.1% of sites with a known encoding | "about 99 percent of websites" (card: "W3Techs, Sep 2026") |
| Notepad renders Markdown | Generally available since Jul 2025 on Windows 11 | "Newer Notepad on Windows 11 can show bold text that is really stars in the file." |
| Extension picks the program | True for double-click in Windows Explorer and macOS Finder; Linux desktops also sniff content; command line ignores it | "When you double-click, Windows and Mac read the extension to choose the program." Do not say "the OS always uses the extension". |
| What a double-clicked .py opens | Varies (VS Code, Notepad, Python launcher, a "how do you want to open this" prompt) | "It depends on the machine." Name no default. |
| Hidden extensions default | Still on in Windows 11 and macOS Finder; no announced change | "Windows and Mac still hide most extensions by default." |
| Agents read by type | Claude Code docs (live): images returned as visual content, not raw bytes; PDFs by page; notebooks as cells | "Coding agents like Claude Code read text as text and pictures as pictures." No version numbers. |
| AGENTS.md | From OpenAI (Aug 2025), 60,000+ projects, Linux Foundation's Agentic AI Foundation 2025-12-09 | "used in tens of thousands of projects, and now looked after by the Linux Foundation" (card: "Dec 2025") |
| Magika | Google, open source; 1.0 Nov 2025; used to scan files in Gmail, Drive, Safe Browsing | "Google uses an AI model that identifies files from their bytes, not their names." No accuracy figure spoken. |
| Magic numbers | PNG `89 50 4E 47`, PDF `%PDF-`, ZIP `PK`; .docx/.xlsx are ZIPs | "Many formats start with the same few bytes, like a stamp." Text files (.py) have no stamp. |
| Byte range | One byte = 8 bits = a number 0 to 255 | "a number from zero to two hundred fifty-five" |
| "Encoding" | In 15.05 the word means base64-style transforms | Here say "code" or "agreement" first, then "encoding, usually U T F eight"; don't call it security. |
| Heading-to claims | Speculation | "The direction looks like..." / "Expect more..." Never as fact. |
| Aaron's story | COURSE.md, true | Third person: "Aaron, who made this course, wrote Python in Notepad and saved it as dot T X T." Nothing added. |
