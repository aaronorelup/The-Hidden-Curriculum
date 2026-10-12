# 01.01 "Files are just bytes" - research: the last five years of change

Lens: what this looked like about five years ago (autumn 2021), the turning points with dates, what got replaced or renamed, which old explanations now mislead, and what did not change. Compiled 2026-10-04. Status tags: **established** (settled, widely documented), **new this year** (2026), **beta/announced** (preview, Insider-only, release candidate, scheduled), **speculation** (forecast). "(secondary)" = trade press or aggregator, not the vendor; hedge on screen.

Scope reminder: 01.01 owns the mental model (a file is a numbered row of bytes; "text" is bytes read through an agreed code; the extension is a name-label the OS uses to pick a program). 01.02 owns showing extensions, renaming, "Open with" and default apps; module 15 owns secrets/security detail. Items below that belong elsewhere are marked "(name only)".

## 0. Names and spellings in the brief

- No ambiguous product names in the orchestrator notes. ".py" = Python source file; "the OS" = Windows / macOS / Linux. Aaron's own story (Python written in a `.txt` file) is in COURSE.md and fits this lesson's hook.
- "Agents read and write these files for you": the concrete current tools are coding agents (Claude Code, Codex, Cursor, Copilot agent) with Read/Write/Edit tools, and MCP servers such as the reference "filesystem" server. Sections 5 and 6.

## 1. The durable core (did NOT change in five years, or fifty)

- A file is a named sequence of bytes on storage; the OS keeps the name, size and dates separately (filesystem metadata), not "inside" the meaning of the bytes. Status: established.
- A "text file" is just bytes that a program agrees to read as characters through an encoding; a `.py` file is a text file whose content happens to be Python. Nothing in the bytes says "Python". Status: established.
- The extension is part of the name. Changing `notes.txt` to `notes.py` changes zero bytes of content; it changes which program the OS hands the file to. Status: established.
- Binary formats (PNG, PDF, ZIP, EXE) usually start with "magic bytes" that identify the real format regardless of the name; tools like `file` (Unix) have sniffed these for decades. Status: established.
- Default for both big desktop OSes is still to HIDE known extensions:
  - Windows 11: "Hide extensions for known file types" on by default; no change in 2025-2026. Source: https://pureinfotech.com/show-file-extensions-windows-11/ (2025, secondary); https://www.elevenforum.com/t/show-or-hide-file-name-extensions-for-known-file-types-in-windows-11.898/ (live tutorial, secondary). Status: established. (How to change it: 01.02.)
  - macOS Finder: "Show all filename extensions" off by default. Source: https://support.apple.com/guide/mac-help/show-or-hide-filename-extensions-on-mac-mchlp2304/mac (live Apple guide); https://macos-defaults.com/finder/appleshowallextensions.html (live). Status: established.
- Windows still uses CRLF line endings by convention and macOS/Linux LF; the bytes differ, the text looks the same. Notepad has understood LF since Windows 10 1809 (Oct 2018). Source: https://www.digitalcitizen.life/new-features-in-notepad-in-windows-10-version-1809/ (2018). Status: established.

## 2. Encoding: UTF-8 went from "usually" to "the default everywhere"

Five years ago (2021): the web was already ~97% UTF-8, but Windows programs and Python on Windows still defaulted to the local "code page" (e.g. cp1252) when no encoding was given, so the same `.py` or `.txt` could read differently on two machines.

- 2019 (Windows 10 1903): Notepad saves new files as UTF-8 without BOM by default (was ANSI). Source: https://www.bleepingcomputer.com/news/microsoft/windows-10-notepad-is-getting-better-utf-8-encoding-support/ (2018-2019); https://en.wikipedia.org/wiki/Unicode_in_Microsoft_Windows (live). Status: established.
- 2021-10 (Python 3.10): PEP 597 `EncodingWarning` added to flag `open()` calls without an explicit encoding (opt-in). Referenced in PEP 686: https://peps.python.org/pep-0686/ (PEP created 2022-03-18, status Final). Status: established.
- Precedents: Ruby 3.0 (2020) and JDK 18 (2022) made UTF-8 their default. Same PEP 686 source. Status: established.
- **Python 3.15 makes UTF-8 mode the default on every platform (PEP 686)**: text-mode `open()`, stdio and pipes use UTF-8 unless you say otherwise; opt out with `PYTHONUTF8=0` / `-X utf8=0`; Windows is the platform that changes (code page -> UTF-8). Sources: https://peps.python.org/pep-0686/ (Final); https://realpython.com/python315-utf8-default/ (2026, secondary); https://pydevtools.com/blog/python-315-utf8-default/ (2026, secondary). Status: beta/announced as of 2026-10-04 -> becomes established on release day.
  - Release timing: 3.15.0rc3 released **2026-10-02** (unplanned extra RC for lazy-import blockers); final **scheduled 2026-10-09** (originally targeted 2026-10-01). Source: https://www.python.org/downloads/release/python-3150rc3/ (2026-10-02). Wording for the lesson: "Python 3.15, due in October 2026" or "the newest Python"; do NOT say "Python 3.15 is out" before 10-09. Note: https://byteiota.com/python-3-15-is-out-what-breaks-what-to-fix/ (2026) already claims it is out - wrong as of 10-04.
- Web share today: UTF-8 is used by **99.1%** of websites whose encoding is known (2026-09-11). Source: https://w3techs.com/technologies/details/en-utf8 (2026-09). Status: established.
- Unicode itself keeps growing: Unicode 18.0 released **2026-09-16**, +13,007 characters, 172,808 total. Sources: http://www.unicode.org/versions/Unicode18.0.0/ (2026-09-16); https://linuxiac.com/unicode-18-0-released-with-13007-new-characters/ (2026-09, secondary). Status: new this year. (Fine as a one-line aside: the code table changes; "a byte is a byte" does not.)

## 3. The plain-text editor changed under people's feet (Windows)

Five years ago: Notepad = dumb plain text; WordPad = the "rich text" one; you could tell them apart.

- 2024 (Windows 11 24H2, Oct 2024): **WordPad removed** from clean installs and upgrades; Microsoft recommends Word for .rtf/.doc and Notepad for .txt. Sources: https://www.windowslatest.com/2024/10/02/windows-11-24h2-deletes-wordpad-but-you-can-bring-it-back/ (2024-10-02); Microsoft quote via same. Status: established.
- 2025-05-30 (Insiders) / early July 2025 (general): **Notepad gains formatting** (bold, italic, headings, lists, links) stored as **Markdown in plain text**, on by default, can be turned off; you can toggle between formatted view and raw Markdown syntax. Sources: https://blogs.windows.com/windows-insider/2025/05/30/text-formatting-in-notepad-begin-rolling-out-to-windows-insiders/ (2025-05-30); https://www.windowslatest.com/2025/07/02/windows-11-notepads-rich-text-formatting-markdown-is-now-available/ (2025-07-02). Status: established. Lesson value: the bold text you SEE in Notepad is `**` characters in the bytes - a perfect "what you see is a rendering of the bytes" example.
- 2025 (Notepad 11.2508.28.0, Insiders): on-device AI Write / Rewrite / Summarize on Copilot+ PCs, no subscription; renamed from "Copilot" to "Writing tools" in Notepad 11.2512.28.0. Sources: https://www.windowscentral.com/microsoft/windows-11/windows-11-notepad-will-soon-let-you-generate-text-using-on-device-ai-models-no-subscription-required (2025); https://www.analyticsinsight.net/tech-news/microsoft-replaces-copilot-in-windows-11-notepad-with-writing-tools-update (2025-12/2026, secondary). Status: established for Insiders; general availability hedge ("on newer Windows PCs"). Name only.

## 4. Extensions as a security signal: the arms race moved

Five years ago: the classic warning was "invoice.pdf.exe" with hidden extensions, and macro-laden Office documents.

- 2022-02 (announced) / mid-2022: Microsoft blocks VBA macros in Office files from the internet by default. Proofpoint (Oct 2021 - Jun 2022): macro use -66%, container files (ISO/ZIP/RAR) ~+175%, LNK shortcut files +1,675% vs Oct 2021. Source: https://www.proofpoint.com/us/blog/threat-insight/how-threat-actors-are-adapting-post-macro-world (2022-07); https://www.bleepingcomputer.com/news/security/as-microsoft-blocks-office-macros-hackers-find-new-attack-vectors/ (2022-07). Status: established. Lesson value: attackers pick whichever file TYPE the OS will open with the most power - the label matters.
- 2022-11-08: Windows patches Mark-of-the-Web bypass for ISO contents (CVE-2022-41091); Dec 2022 CVE-2022-44698. Mark of the Web = a hidden tag (alternate data stream) Windows attaches to downloaded files - metadata kept beside the bytes. Sources: https://en.wikipedia.org/wiki/Mark_of_the_Web (live); https://borncity.com/win/2023/01/09/windows-and-the-mark-of-the-web-motw-security-problem/ (2023-01-09). Status: established. (name only; module 15)
- 2023-03 / Apr-May 2023: OneNote for Windows blocks ~120 dangerous embedded file extensions after attackers moved to .one files. Source: https://thehackernews.com/2023/04/microsoft-tightens-onenote-security-by.html (2023-04); https://www.ghacks.net/2023/03/31/microsoft-will-block-120-high-risk-file-extensions-in-onenote/ (2023-03-31). Status: established.
- 2023-05: Google opens **.zip and .mov top-level domains** to the public; a file name like `setup.zip` can now be auto-linked as a website; phishing domains (e.g. microsoft-office.zip) seen within days. Sources: https://www.bleepingcomputer.com/news/security/new-zip-domains-spark-debate-among-cybersecurity-experts/ (2023-05); https://www.schneier.com/blog/archives/2023/05/security-risks-of-new-zip-and-mov-domains.html (2023-05). Status: established. Lesson value: an extension-looking label is not proof of anything.
- 2024-02: Google open-sources **Magika**, a deep-learning file-type detector that reads content, not names; used to route Gmail, Drive and Safe Browsing files to scanners, "hundreds of billions" of files a week. 2025-11-06: **Magika 1.0** (Rust rewrite, 200+ types, ~1M monthly downloads). Sources: https://opensource.googleblog.com/2024/02/magika-ai-powered-fast-and-efficient-file-type-identification.html (2024-02); https://opensource.googleblog.com/2025/11/announcing-magika-10-now-faster-smarter.html (2025-11-06); https://www.infoq.com/news/2025/12/magika-rust-file-type-detector/ (2025-12). Status: established. Lesson value: even Google's own security stack does not trust the extension; it looks at the bytes.

## 5. The AI turn: agents read and write files for you

Five years ago (2021): Copilot was a technical preview doing autocomplete inside a file you had open; you created, named and saved every file yourself.

- 2024-11 (filesystem server ~2024-11-19; MCP announced 2024-11-25/26): Anthropic releases the **Model Context Protocol** with a reference **filesystem server** that lets an AI app read, write and search files in folders you allow. Sources: https://en.wikipedia.org/wiki/Model_Context_Protocol (live); https://www.pulsemcp.com/servers/modelcontextprotocol-filesystem (live, secondary). Status: established. (MCP itself: module 10.)
- 2025-02: Claude Code (research preview), then 2025 spring OpenAI Codex agent, Copilot coding agent: agents that create, edit and run files in your project (see 00.06 research-change for the dated chain). Status: established.
- Today an agent's Read tool treats files by type, not just as text: in Claude Code, images (PNG/JPG) come back "as visual content ... not as raw bytes", PDFs are read whole or by page ranges, `.ipynb` notebooks as cells with outputs. Source: https://code.claude.com/docs/en/tools-reference (live doc, fetched 2026-10-04; mentions v2.1.196 and v2.1.208 behaviour). Status: established (current doc). Lesson value: the agent, like the OS, decides HOW to read a file from what kind of file it is.
- Plain text files became the way you instruct agents:
  - **AGENTS.md** (from OpenAI Codex, Aug 2025): a Markdown file in your repo that agents read for project rules; 60,000+ projects; donated to the Linux Foundation's new **Agentic AI Foundation** on **2025-12-09** with MCP and Block's goose. Sources: https://agents.md/ (live); https://aaif.io/projects/agents-md (live); https://community.openai.com/t/openai-co-founds-the-agentic-ai-foundation-under-the-linux-foundation/1368868 (2025-12). Status: established.
  - **Agent Skills / SKILL.md**: folders with a `SKILL.md` (YAML + Markdown) that agents load; launched by Anthropic Oct 2025, published as an open standard at agentskills.io on **2025-12-18**; adopted by Microsoft, OpenAI, Cursor, GitHub and others. Sources: https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure/ (2025-12, secondary); https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/ (2025-12, secondary). Status: established.
  - Also CLAUDE.md, `.cursorrules` / Cursor rules, `.github/copilot-instructions.md`: all just text files with a conventional name. Status: established. Lesson value: "the name tells the program what to do with it" now applies to agents too - an agent looks for `AGENTS.md` by name the way Windows looks at `.py`.

## 6. New risk: bytes you cannot see, read by agents that can

Not a thing five years ago. Reinforces "a file is bytes, and what you see is only a rendering".

- 2024-01: Johann Rehberger releases "ASCII Smuggler": Unicode Tag characters (U+E0000-U+E007F) mirror ASCII, render as nothing in editors and browsers, but language models read them as instructions. Used against Microsoft 365 Copilot (fixed, reported 2024-08). Sources: https://thehackernews.com/2024/08/microsoft-fixes-ascii-smuggling-flaw.html (2024-08); https://arxiv.org/pdf/2412.06090 (2024-12). Status: established.
- 2025-03-18: Pillar Security "**Rules File Backdoor**": hidden zero-width and bidirectional Unicode characters inside AI rules files for Cursor and GitHub Copilot make the agent write malicious code; invisible in the editor and in GitHub's PR view. Both vendors said users are responsible for reviewing suggestions. Sources: https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents (2025-03); https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html (2025-03). Status: established. (name only; prompt injection is a module-15 / lantern lesson topic)
- 2026: research and advisories extend the same trick to skill files and MCP tool descriptions. Sources: https://labs.cloudsecurityalliance.org/research/csa-research-note-unicode-instruction-injection-ai-skills-20/ (2026, secondary); https://arxiv.org/html/2603.00164v1 (2026-03, "Reverse CAPTCHA"). Status: new this year. Hedge.

## 7. Python on Windows: what opens a .py file (name only; 01.02 owns associations)

- Five years ago: python.org .exe installer + the `py` launcher; double-clicking a `.py` file on Windows typically RAN it in a console window (via the launcher) instead of opening it for editing - a durable beginner surprise. Status: established.
- 2025-10 (Python 3.14): new **Python Install Manager** (PEP 773) replaces the old installer and standalone launcher, which are deprecated; the full installer will not be produced for 3.16+. Sources: https://docs.python.org/3/using/windows.html (live, 3.14.8 docs); https://peps.python.org/pep-0773/ (live). Status: established. Hedge any claim about exactly what a double-click does now; leave to 01.02 / module 03.

## 8. Where it is heading

- Text encoding: effectively settled on UTF-8; the remaining holdouts (Windows code pages in old programs) shrink as runtimes flip defaults (Python 3.15). Status: speculation (well supported).
- More "content-aware" handling: security stacks (Magika), editors (Notepad rendering Markdown), and agents (reading images/PDFs natively) all decide what a file is from its bytes as well as its name. The extension remains the OS's first, cheapest guess. Status: speculation.
- More plain-text files whose NAME is an instruction to an AI (AGENTS.md, SKILL.md, rules files), now under neutral governance (Agentic AI Foundation). Status: established trend / speculation on direction.

## Traps (commonly said, now wrong or misleading)

- "The extension is what makes it a Python file / changing the extension converts the file." Wrong then and now: renaming changes the label, not the bytes. (Converting .png to .jpg by renaming does nothing.)
- "Notepad is plain text, so what you see is what is in the file." Since mid-2025, Notepad can render Markdown; bold you see is `**` in the bytes. And invisible Unicode characters can be in a file you see as empty-looking (Rules File Backdoor).
- "WordPad is the rich-text editor built into Windows." Removed in 24H2 (2024).
- "Python on Windows reads files as cp1252 / the system encoding." True through 3.14; flips to UTF-8 by default in 3.15 (final scheduled 2026-10-09). Do not state either as timeless; do not say 3.15 "is out" before 10-09.
- "Check the extension to know if a file is safe." Attackers move to whatever types open with power (macros -> ISO/LNK -> OneNote); `.zip`/`.mov` are also website names since 2023; Google's own scanners use content (Magika).
- "Only you create files; AI just suggests text." Agents now create, edit and read files directly (Claude Code, Codex, Copilot agent, MCP filesystem), including images and PDFs.
- "Hidden extensions is an old Windows quirk that was fixed." Still the default on Windows 11 AND macOS in 2026.
- "Text vs binary is about the extension." It is about the bytes: a `.txt` can hold binary junk, a `.py` can be saved in a non-UTF-8 encoding and break.
