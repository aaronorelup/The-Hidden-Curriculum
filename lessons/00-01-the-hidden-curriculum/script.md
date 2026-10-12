# 00.01 — The hidden curriculum
<!-- lead=1.6 gap=0.8 tail=3 -->
<!-- captions: path=PATH -->

## 01 — Nobody handed you the map
> Final synthesis: spine of draft A (story-first), with grafts from C (syllabus line, verified MIT motivation, "messier than the map", keep-3) and B (AI as the voice that says "just").
> Narrated in Aaron's first person ("I", "my automations"). The stories are his and are listed in COURSE.md. If the narrator should not speak as him, swap "I" for "the person who made this course" in 01, 02 and 04.
> Title card carries the one-line conclusion from frame 0: "A gap in the syllabus, not in you."
> Degree wording (fact-check 2026-09-30): say only "Information Systems". Notion's Identity & Bio lists CSUF Business Administration, Information Systems concentration (ISDS/BAIS); the exact degree name is unresolved across sources, and "Data Science" is not on the record. Restore Aaron's fuller wording only if he confirms the diploma says it.
Building with AI runs on a second curriculum that school rarely teaches: [[topics]] terminals, files, git, keys, hosting. If you never learned it, [[not-you]] the gap is in the syllabus, not in you. This course is the [[map]] map for it: what each thing is, and where it goes. Aaron, who made this course, has a [[degree]] degree in Information Systems, and still found out the hard way.

## 02 — Python in a text file
> Only the true details from COURSE.md: Notepad, .txt, didn't know to rename to .py, didn't know to open a terminal and cd, didn't know what .venv was. Do not add "first script", times or error messages. The filename script.txt on screen is illustrative.
> Pronunciation: "dot T X T" = dot tee-ex-tee; "dot P Y" = dot pee-why; "C D" = see-dee; "dot V E N V" = dot vee-ee-en-vee for .venv (narrator pass 2026-09-30: "vee-env" was heard as ".env" in 05 and "the V and" in 07, so it is spelled letter by letter). Screen shows .txt, .py, cd, .venv.
He wrote Python in [[notepad]] Notepad and saved it as a dot T X T file. He didn't know to [[rename]] rename it to dot P Y. He didn't know to open a [[terminal]] terminal and C D into the folder first. And [[venv]] dot V E N V? He had no idea what that was. None of it is hard. Nobody had handed it to him. You probably have your own [[pile]] pile of these, too. Each one has a place.

## 03 — Why nobody taught you
> "Mostly" is load-bearing in both degree sentences: programmes vary, this is the general shape, not a rule about every school.
> "The ideas", not "theory" (fact-check 2026-09-30): CS degrees include plenty of hands-on programming and systems courses. The point, as Missing Semester puts it, is that students use these tools constantly but are rarely taught them. "Used everywhere, rarely taught" carries that mechanism.
Here's why this happens to smart people. [[cs]] Computer science mostly teaches the ideas: algorithms, data structures, how computation works. [[is]] Information systems mostly teaches how businesses run on technology: databases, processes, projects. The everyday tools fall in the [[gap]] gap between them: the terminal, the folders, the keys, the hosting. Used everywhere, rarely taught. So most people learn them the old way. [[apprentice]] Apprenticeship, where someone leans over and says, you need to C D first. Forums, where a stranger answers your exact error. And breaking things. Lots of things. [[holes]] It works, slowly. And everyone ends up with a different set of holes.

## 04 — It isn't just you
> Checked 2026-09-30 at missing.csail.mit.edu: exact title "The Missing Semester of Your CS Education"; the front page says tool proficiency is "rarely covered" in classes and "left to students to figure out on their own"; the January 2026 (IAP) schedule lists "Agentic Coding" on 1/21/26; a 2020 offering also exists. No founding year is spoken, on purpose.
> Work story is Aaron's true one (COURSE.md): automations tied to his personal accounts had to move to service accounts, with credentials stored properly (Credential Manager, DPAPI, Entra app registrations). Keep it this general.
Even [[mit]] M I T has a course for this gap: The Missing Semester of Your C S Education. Its front page says tool skills are [[rarely]] rarely covered in class, and left to students to figure out on their own. Its January 2026 edition includes a lecture on [[agentic]] agentic coding. If M I T students need a missing semester, you're allowed to need a missing map. [[work]] It follows you to work, too. Aaron's automations there ran under his own personal accounts. They had to move to [[service]] service accounts, with their credentials stored properly. Nobody had taught him that either.

## 05 — Where it lives
> District names and questions are read exactly as engine/map.js draws them. Six districts; the Lanterns (AI) are not a district but hang over all six (COURSE.md, map restructured 2026-10-01: the earlier take said "seven districts... the seventh: the Lanterns").
> Shelving targets (curriculum.md): .txt/.py -> 01 Your computer; cd -> 02 The command line; .venv -> 05 Packages; service accounts -> 14 Identity & keys.
Here's the shelf: a [[map]] map with six districts, each answering one question. The Machine: what's on your computer. The Code: what programs are made of. The History: how work is saved and shared. The Network: how computers talk. Trust: who may do what. Shipping: getting it to people. And strung over all of them: [[lanterns]] the Lanterns. That's AI. It isn't a district of its own. It lights every district, but it doesn't walk the streets for you. This lesson sits at the [[gate]] start. And those loose questions? [[shelve]] Dot P Y and C D live in The Machine. Dot V E N V lives in The Code. Service accounts live in Trust.

## 06 — A map, not a manual
> The five questions are COURSE.md's lesson contract, in second person. "Messier than the map" is the where-the-metaphor-breaks beat: districts are tidy, real tools cross borders.
That's the promise: a map, not a [[manual]] manual. Every lesson answers [[five]] five questions: what is it, where does it live, what is it like, what does it connect to, and what will surprise you. You won't finish able to do the thing yet. You'll [[recognise]] recognise it when you meet it. Real tools are [[messy]] messier than the map. Git lives in The History, but it talks across The Network. Keys belong to Trust, and they turn up everywhere. Memorising commands is [[skip]] safe to skip. Your AI can type them. Your job is knowing what they mean.

## 07 — The surprises you'll hit
> Screen literal forms: cd, .venv, PATH. The error is Python's real message when the named file isn't in the current folder (or is still script.txt, or got saved as script.py.txt); on Windows the prefix may be the full path to python.exe, hence "something like". Python prints this before reading a single line, so it never means the code is broken (a missing file inside the code is a different error, a FileNotFoundError traceback). "Usually" belongs only on the list of causes: wrong folder, still .txt, a typo, or script.py.txt.
Two surprises you'll meet early. The first is a word: [[just]] just. Just C D into the folder. Just activate the V E N V. Just add it to your path. Tutorials say it. Coworkers say it. Your AI assistant says it too. Every just is a lesson somebody [[skipped]] skipped. It isn't a sign you're behind. It's a pin on the map. The second is an error. Run a script from the wrong place, and you'll see something like [[error]] this: can't open file, no such file or directory. That doesn't mean your code is broken. Python never even opened it. Usually, you're standing in the [[wrong-folder]] wrong folder, or the file is still called dot T X T.

## 08 — Keep this
> keep-1's bold lead returns the lesson's one-line conclusion from 01 (the narration's "the gap is in the syllabus, not in you"); its body keeps COURSE.md's voice example ("Nobody handed you this map... a missing semester"). The end card shows the same three bold leads as lesson.js keep.
Three things to keep. [[keep-1]] The gap is in the syllabus, not in you. Nobody handed you this map; it's a missing semester, not a character flaw. [[keep-2]] Every confusing thing has a shelf: six districts, with AI as the lanterns over all of them. [[keep-3]] Aim for recognition, not recipes. Once you know what a thing is and where it lives, the how-to is easy to find.
