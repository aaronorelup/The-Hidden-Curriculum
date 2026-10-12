# 01.01 — Files are just bytes
<!-- lead=1.6 gap=0.8 tail=3 -->
<!-- captions: hello dot T X T=hello.txt; hello dot P Y=hello.py; notes dot T X T=notes.txt; photo dot P N G=photo.png; invoice dot P D F=invoice.pdf -->
## 01 — Bytes inside, a label outside
In this lesson you'll learn what a file really is, and what the little ending on its name, like dot P Y, actually does. [[headline]] Every file is just a row of numbers called bytes, and the extension is part of its name: a label that tells your computer which program to open it with, [[not-inside]] not what is inside. [[agents]] Agents read and write your files now, so this keeps them from surprising you.
> Winner: draft A (story-first), with grafts from B and C. Title card: purpose line + "Bytes inside, a label outside."

## 02 — Where it lives: a dot T X T
[[pin]] This is the first stop on the map: District One, The Machine, which asks what's on your computer. [[notepad]] Aaron, who made this course, has an I T degree. He still wrote Python in Notepad, and saved it as dot T X T. [[rename]] He didn't know that renaming it to dot P Y was the whole difference. Nothing inside had to change. Only the label. [[missing]] Nobody handed you this part. That's not a character flaw; it's a missing semester.
> True story only (COURSE.md): Notepad, .txt, didn't know to rename to .py, IT degree. Third person, nothing added.

## 03 — A string of beads with a tag
[[beads]] Picture a file as a string of beads. Each bead is one byte: a number from zero to two hundred fifty-five. [[everything]] A photo, a song, a spreadsheet, your Python script: beads, in order. [[tag]] Tied to the string is a paper tag. That's the file's name, and the part after the last dot is the extension. [[carry]] Your computer stores and moves beads. It never knows what they mean.

## 04 — Text is an agreement
[[code-card]] Numbers become words through an agreement: a code card that says which number means which letter. One hundred twelve means a small p. [[letters]] Lay the card over our beads, and they spell print, hi. A dot P Y file is just text whose letters happen to be Python. Nothing in the beads says Python. [[garbled]] Use the wrong card, and the same beads come out as garbled symbols. [[utf8]] Today's card is almost always U T F eight, used on about ninety-nine percent of websites. Python three point fifteen, due this month, makes it the default everywhere. [[rendering]] And what you see is a rendering: newer Notepad on Windows 11 can show bold text that is really stars in the file.
> Wrong card on screen is UTF-16 (reads beads in pairs), because pure-ASCII beads read the same under UTF-8, cp1252, Latin-1 and Mac Roman. Cards: "W3Techs, Sep 2026" under the 99% figure; "Python 3.15 · due Oct 2026" (never "out"). Say "code card" / "agreement", not "encoding" (15.05 uses that word for something else).

## 05 — The tag only picks the program
[[porter]] When you double-click, Windows and Mac read the extension to choose which program opens the file. [[rename-py]] Rename hello dot T X T to hello dot P Y, and not one bead moves. [[python-runs]] Programs themselves mostly ignore the tag: Python will happily run notes dot T X T. [[stamp]] Many other formats carry a stamp in their first few beads. P N G pictures all start with the same few bytes, and so do P D Fs. A modern Word file is a zip inside. The stamp is a far better clue than the tag. Plain text has no stamp. [[breaks]] Here's where the picture breaks: the tag isn't tied to the string. The folder keeps the name separately, so renaming is instant.
> Hedge kept: Explorer and Finder read the tag on a double-click; never "the OS always uses the extension". Stamps on screen only (‰PNG, %PDF-, PK); no hex read aloud.

## 06 — The surprises you'll hit
[[hidden]] Windows and Mac still hide most extensions by default, so a file that looks like hello dot P Y can really be hello dot P Y dot T X T. [[png-jpg]] Renaming photo dot P N G to dot J P G doesn't convert it. [[mojibake]] Odd symbols where an accented letter belongs mean the wrong code card was used. [[double-click]] Double-click a dot P Y file, and what opens depends on the machine. [[costume]] And a file named invoice dot P D F dot E X E is a program in a costume. A tag can lie, which is why attackers like hidden extensions.
> No how-to: showing extensions, renaming and "Open with" belong to 01.02. Name no default program for .py. Security depth lives in Module 15; no scare tone.

## 07 — The lantern: agents and your files
Five years ago, you made and named every file yourself, and AI was autocomplete inside the one you had open. [[agent-hand]] Now coding agents like Claude Code create, read and edit the files in your project directly. They read text as text and pictures as pictures. [[agents-md]] AGENTS dot M D and CLAUDE dot M D are plain text whose names say: read me first. Same trick as an extension. AGENTS dot M D is now looked after by the Linux Foundation. [[magika]] Google uses an AI model that identifies files from their bytes, not their names. The direction looks like this: the name stays the cheap first guess, and more tools check the beads too. [[invisible]] And a text file can hold invisible characters that an agent reads and you don't.
> Cards: "AGENTS.md · Linux Foundation, Dec 2025"; "Google Magika · since 2024, v1.0 Nov 2025". "The direction looks like" marks speculation. Invisible characters: pointer to 15.15, no depth.

## 08 — Keep this
[[ignore]] Safe to ignore for now: hex, bits, U T F sixteen, byte order marks and line endings. [[keep-1]] Keep this. One: a file is just bytes. [[keep-2]] Two: text is bytes plus an agreement, and the agreement is usually U T F eight. [[keep-3]] Three: the extension is a label that picks the program, not the contents. [[next]] Next on the map: file extensions and associations.
> keep: matches lesson.js. Next stop named neutrally (01.02), no teaser.
