---
key: where-your-agent-works
id: 01.02
title: Where your agent works
district: First Build
module: 01 Your workbench
status: todo
legacy: [01-05-environment-variables-path, 01-06-programs-processes-services]
minutes: 10
concepts: [C022, C103, C122, C128]
sources: [S102, S184, S207, S209, S249, S069, S101, S208, S206, S129, S008, S025, S186, S104, S187, S241, S050, S185, S004, S210, S016, S052, S070, S074, S080, S132, S183]
lead: [S249, S209]
---

# Where your agent works

**Purpose (the first spoken sentence):** In this lesson you'll learn how chat, Cowork, desktop apps and terminal agents differ in what they can reach, which computer the work actually runs on, and where your files and chats end up.

**Conclusion:** The same model can sit behind every surface, so pick the surface by the output you need and what it must reach, and before you hand it anything private, check which machine runs the work and where your files and chats go.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; module 01 Your workbench (second lesson: 01.01 chose the folder, this one chooses the surface and the machine; 01.03 reads what the agent did there).

**Lead source (audit, 2026-10-12):** S249 (Ethan Mollick (One Useful Thing)); S209 (MIT Missing Semester (SIPB IAP 2026)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S102, S184, S207, S209, S249); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Rough time budget: C022 3 min · C103 3 min · C122 2 min · C128 2 min. Order: the surfaces and what each can reach (C022), the terminal as one of those windows (C122), the other computers the work may run on (C128), and where your data goes as a result (C103). This is a lantern lesson: every surface here is an AI product. Date every product fact on screen ("as of 2026-10-12") and say it moves monthly.

### C022 Which surface for which job

1. **Pick the surface by the output, not the logo.** OpenAI's own bootcamp slide (2026-09-23): "Use Chat when the answer is still taking shape", "Use Work when the desired output is knowledge artifacts", "Use Codex when the output is working software or applications", under the heading "Codex now lives in the new ChatGPT desktop app" (S008, slide 8). Codex moved into the ChatGPT desktop app on 2026-07-09 (S025). Anthropic's desktop app has the same split: Chat, "General conversation with no file access"; Cowork, "An autonomous background agent"; Code, "direct access to your local files" (S208). (S008, S025, S208) — **teach**
2. **A shared model, but not always, and never the same reach.** The surfaces often share models, but not always: on 2026-09-22 OpenAI shipped new models "available in Work and Codex, but not Chat" (S025). What always differs is what the session can touch. (S025) — **one line**
3. **The mode buttons are disappearing; the difference isn't.** On 2026-09-16 Anthropic announced "Claude Cowork and chat are merging into one Claude", rolling out on Pro and Max "over the next few weeks, with more plans to follow": Claude works out whether a request is a quick answer or a task, and "By default, Claude asks before taking an action" (S102). The desktop quickstart still shows three tabs (S208), so say the rollout is in progress and show whichever the viewer's app has. (S102, S208) — **teach**
4. **Where the work runs decides what it can reach.** Cowork tasks "run in the cloud: Claude's work runs in an isolated, temporary environment on Anthropic's servers"; a cloud session "reaches your computer only when the Claude Desktop app is open", and only connected folders (S069). Since 2026-10-06, new Cowork tasks on Pro and Max run in the cloud; the "Only on your computer" option was removed and the change can't be reversed; for local-only work the vendor points to Claude Code in the desktop app (S184). ChatGPT Work is the same idea at OpenAI: locally it "can also use local files, apps, and the browser"; in the cloud "your computer doesn't need to be awake" but the container "cannot access that computer's files or tools", and "Work can't switch from local to cloud execution during a turn" (S025, companion page "Get started with ChatGPT Work", undated). (S069, S184, S025) — **teach**
5. **A coding agent has one loop and many windows.** Claude Code runs the same loop in the terminal, the desktop app, IDE extensions, claude.ai/code, Remote Control, Slack and CI, in three execution environments: Local ("Full access to your files, tools, and environment"), Cloud ("Anthropic-managed VMs") and Remote Control ("Your machine, controlled from a browser") (S101). The desktop app's first step offers Local, Cloud, SSH and WSL (S208). (S101, S208) — **teach**
6. **By kind of work and by stakes.** Mollick's Summer 2026 guide (2026-07-23): for low stakes the chat apps are "all at least fine"; for high stakes use the most advanced model at a High thinking level; cloud agents (ChatGPT Work, Claude Cowork) run on the company's computers and hand back a finished result, while Codex and Claude Code "expose the work itself" (files changed, commands run, tests); keep agents asking for approval first "until you trust the system"; he reissues the guide each season (S249). Show his kind-of-work picks (research, images, video, voice, office documents) as a dated card, not narration. (S249) — **brief**

7. **The same surface can bill two ways** (added by the 2026-10-12 audit, because a heavy user meets the meter on day one). Your plan's rolling five-hour and weekly allowance, shared between Claude and Claude Code, or an API key that bills every token; if `ANTHROPIC_API_KEY` is set in your environment, Claude Code uses it instead of your subscription and the work is billed as API charges (S132). How the meter works and how to cap it is know-your-meter (06.03). (S132) — **one line**

**Dropped from C022 for this lesson:** a product's harness beating the same model elsewhere (S074) → 00.02 model-harness-and-memory (C021); the details of the usage allowance and the meter (S016) → 06.03 know-your-meter (C055; point 7 above names it in one line); image and video generators by vendor → 09.02 making-media-with-ai.

### C122 The terminal: a text window where a shell runs commands as you

1. **Terminal, shell, command.** The terminal is the window; the shell is the program reading each line. "Windows has two command-line programs: PowerShell and CMD. They look similar but use different commands": PowerShell shows `PS C:\Users\YourName>`, CMD the same without the `PS`; on macOS the default shell is Zsh (S207). The same line can work in one and fail in the other: "If you see `The token '&&' is not a valid statement separator`, you're in PowerShell, not CMD" (S206). (S207, S206) — **teach**
2. **A command runs as you.** The agent's terminal can run "Any command you could run: build tools, git, package managers, system utilities, scripts. If you can do it from the command line, Claude can too" (S101). That is the bridge to 02.01: a command it runs has your permissions on everything you can reach. (S101) — **teach**
3. **"Not recognized" usually means PATH.** "If your shell says `claude` isn't found or isn't recognized, the install directory isn't on your PATH yet"; after the fix, "open a new terminal window" (S206, S207). Recognise it; the agent fixes it. (S206, S207) — **brief**
4. **The agent's shell may not be yours.** On native Windows, Claude Code uses Git Bash when Git for Windows is installed, "If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead" (S206). A command copied from its trail can fail in your own window. (S206) — **brief**
5. **You may never open one.** "Don't want to use the terminal? The Claude Code desktop app lets you skip the terminal entirely" (S207). The effects are the same: the desktop app still runs commands, and has its own terminal pane (S208). MIT's Missing Semester still opens with the shell (2026-01-12 and 01-13) for people who will go deep (S209). (S207, S208, S209) — **one line**

**Dropped from C122:** reading a command for its verb and target → 01.03 save-points-and-the-agents-trail (C117); PATH as an environment variable and when a program picks up a change → 03.02 keys-public-secret-and-leaked (C126).

### C128 Other computers inside and beside yours

1. **VM and container.** MIT's Missing Semester (Packaging and Shipping Code, 2026-01-20): "VMs abstract the entire computer and provide a completely isolated environment with its own dedicated operating system"; containers "package an application along with its dependencies, libraries, and filesystem, but share the host's operating system kernel"; "Docker's isolation is weaker than VMs" (S209). Docker is on Aaron's own list of gaps (S210). (S209, S210) — **teach** (one picture: a house, a flat in a shared building)
2. **WSL and SSH.** WSL: "Claude Code, tools, and git execute on the Linux side with native paths". SSH: "Connect to a remote machine over SSH, such as your own servers, cloud VMs, or dev containers. Desktop installs Claude Code on the remote machine automatically the first time you connect" (S208). (S208) — **brief**
3. **A cloud session is someone else's computer working on a copy.** "Each session runs in an isolated, Anthropic-managed VM", keeps running after you close your laptop, and `claude --cloud` "clones your current directory's GitHub remote at your current branch, not your local checkout, so push first"; your GitHub credentials "stay encrypted on Anthropic's servers and never enter a session's VM" (S129). (S129) — **teach**
4. **Each box shares something by default.** A repository with no GitHub remote is bundled and uploaded to the cloud session instead; on macOS, Linux and WSL Claude Code leaves out uncommitted changes to files "named like credentials or keys", including `.env`, and names them in a `Left on this machine:` notice, but on native Windows "uncommitted changes to tracked files upload as they are, whatever the file's name" (S129). So know what crosses before you start. (S129) — **brief**
5. **Unattended agents belong in a box.** MIT on letting an agent skip approvals: "It is not secure to use this mode directly", but "it may be acceptable to run a coding agent in an isolated environment like a virtual machine or container" (S209, Agentic Coding, 2026-01-21). What a container does and doesn't isolate, and checking from inside, is 07.02. (S209) — **one line**

**Dropped from C128:** what devcontainers share (mounted folders, forwarded credentials) and "check from inside" → 07.02 contain-it-dont-babysit-it (C078-C080).

### C103 Where your data goes

1. **"Desktop" no longer means "on your computer".** Cowork's work, "including any local files it opens through the desktop app, is processed on Anthropic's servers" (S069). "When a task needs a file in the cloud, Claude fetches a copy of just that file", and "When you delete a session, the copies Claude fetched are deleted too" (S184). "Close your laptop and Claude keeps going" (S184), and "Scheduled tasks run on their own even when your computer is off" (S069). (S069, S184) — **teach**
2. **The cloud reaches back through the folders you connect.** Only while the desktop app is open, only connected folders; on a computer your organisation manages, "connecting local folders makes them reachable from a session in the cloud"; "Consider creating a dedicated working folder for Claude rather than granting broad access" (S069). Mollick gives his agents only a non-private part of his Google Drive (S249). This is 01.01's habit applied to the cloud. (S069, S249) — **teach**
3. **Your plan decides whether your chats train models.** Free, Pro and Max, "including when they use Claude Code from accounts associated with those plans", have a training setting; with it on, data may be kept "for up to 5 years" de-identified; with it off, the 30-day retention applies; Team, Enterprise, the API (including Bedrock and Vertex), Gov and Education are under Commercial Terms instead (S186, 2025-08-28, foundational and restated by S104, updated 2026-07-01). Turning it off later doesn't reach back: "Your data will still be included in model training that has already started" (S186). The toggle is "Help improve our AI models" in Privacy (S184). Pro is a consumer plan. (S186, S104, S184) — **teach**
4. **Memory is a separate store.** On by default for Free, Pro and Max; on Team and Enterprise "it's off for each member until they turn it on"; shared between Chat and Cowork in the cloud; "When a conversation expires or is deleted, related memory entries generated from it won't be removed": delete them under Settings > Memory; incognito chats are not saved (S187). Feedback (thumbs up or down) is kept 5 years (S104). (S187, S104) — **brief**
5. **Work and home are different accounts.** Cowork on mobile and web "is captured in Compliance API" for your employer (S069); the vendor's advice is separate accounts, "Shared logins aren't supported" (S184). Sharing a Pro or Max cloud session as Public makes it visible to anyone logged into claude.ai, and "Sessions may contain code and credentials from private GitHub repositories" (S129). (S069, S184, S129) — **brief**
6. **Vendors differ; check each one.** Google's Gemini Apps (Privacy Notice 2026-06-29, hub 2026-09-24): human reviewers "review some of the data we collect"; "Reviewed chats are retained for up to three years" and "are not deleted when you delete your activity"; chats with Keep Activity off are kept 72 hours; and "Please don't enter confidential information that you wouldn't want a reviewer to see" (S241). Give viewers the four questions to ask of any tool: is there a training setting, do people review chats, how long is data kept with it off, what does deleting reach. OpenAI's data-use pages refused the research crew's fetch on 2026-10-12 (concepts.md, C103), so fill its column at recording time from a page that loads, or leave it out. (S241) — **brief**

**Dropped from C103:** browser agents and compliance agreements that exclude named features (Claude in Chrome outside a BAA, S070) → 07.03 the-narrowest-keys-and-verbs (C104); your app's users' data sent to AI providers → 04.02 and 04.03; a full per-vendor privacy comparison → backlog ("Comparing AI vendors' privacy settings"); survey figures on shadow AI (S080, S183) were not re-read for this spec, so leave them out unless re-checked.

## You vs the agent

As of 2026-10-12:

- **The agent** in the merged Claude app decides whether a request needs a task run, and asks before acting by default (S102). A coding agent writes commands for whichever shell it is in and fixes PATH problems (S206); the desktop app installs Claude Code on an SSH machine itself (S208). Asked, any agent can fetch each vendor's current privacy and retention pages and fill in the four questions with dates; it cannot tell you whether your employer, client contract or a privacy law allows the data to go there.
- **You** choose the surface by the output; choose local or cloud when files must stay on your machine (S184, S025); choose the account (consumer or commercial, work or personal) and its training and memory settings (S186, S187); connect one dedicated folder, never your home folder or financial records (S069); and set the approval mode (S069, S249).
- **Bring in an expert** (C118) before work data goes in: on a computer your organisation manages, your IT or security admin, because a connected folder becomes reachable from the cloud (S069); for regulated or contractual data (patient records, client data under NDA, customers' personal data), the compliance, legal or data-protection owner. Designing isolation for an agent that holds production credentials is 07.02's expert.

## Sources this lesson is built from

- S102 — Anthropic (Claude blog), "Claude Cowork and chat are now one Claude" (2026-09-16) https://claude.com/blog/cowork-is-now-claude — the merge; Claude decides quick answer or task; asks before acting by default; rollout to Pro and Max first.
- S184 — Anthropic (Claude Help Center), "Use Claude Cowork on web, desktop, and mobile", section "What changed for Pro and Max plans on October 6" (last modified 2026-10-06) https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile — new Pro and Max tasks run in the cloud; "Only on your computer" removed; fetched file copies; separate work and personal accounts.
- S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — where Cowork runs, local files processed on Anthropic's servers, connected folders, managed computers, scheduled tasks, Compliance API.
- S207 — Anthropic (Claude Code docs), "Terminal guide for new users" (undated live docs; example output shows v2.1.211; read 2026-10-12) https://code.claude.com/docs/en/terminal-guide — PowerShell vs CMD by their prompts; PATH and a new window; "skip the terminal entirely".
- S206 — Anthropic (Claude Code docs), "Quickstart" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/quickstart — the `&&` error; Git Bash or PowerShell as the agent's shell on Windows.
- S101 — Anthropic (Claude Code docs), "How Claude Code works" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — one loop across interfaces; Local, Cloud and Remote Control environments; "Any command you could run".
- S208 — Anthropic (Claude Code docs), "Get started with the desktop app" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/desktop-quickstart — Chat, Cowork and Code tabs; Local, Cloud, SSH and WSL; no Node.js needed for the Code tab.
- S129 — Anthropic (Claude Code docs), "Use Claude Code in the cloud" (undated live docs; mentions up to v2.1.289; read 2026-10-12) https://code.claude.com/docs/en/claude-code-on-the-web — cloud sessions in Anthropic-managed VMs; clone the pushed branch; what a local-repo upload carries on each platform; public session sharing.
- S209 — MIT Missing Semester (SIPB IAP 2026), "Missing Semester 2026": Packaging and Shipping Code (2026-01-20) and Agentic Coding (2026-01-21) https://missing.csail.mit.edu/2026/ — VMs vs containers, Docker's weaker isolation, unattended agents in a VM or container. Older than three months, still current.
- S249 — Ethan Mollick (One Useful Thing), "An opinionated guide to which AI to use to do stuff (The Summer 2026 Edition)" (2026-07-23) https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22 — choose by kind of work and stakes; cloud agents vs agents that expose the work; approvals on until you trust it.
- S008 — OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala), "Codex Bootcamp 101: Agentic coding" livestream and deck (2026-09-23) https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c — slide 8: Chat, Work or Codex by output.
- S025 — OpenAI, "ChatGPT & Codex changelog" (latest entry 2026-10-08) https://learn.chatgpt.com/docs/changelog, with "Get started with ChatGPT Work" (undated) https://learn.chatgpt.com/codex/get-started-with-work — Codex in the desktop app (2026-07-09); models in Work and Codex but not Chat (2026-09-22); local vs cloud Work.
- S186 — Anthropic, "Updates to Consumer Terms and Privacy Policy" (2025-08-28; foundational and still current) https://www.anthropic.com/news/updates-to-our-consumer-terms — which plans the training setting covers; 5 years on, 30 days off; training already started keeps your data.
- S104 — Anthropic Privacy Center, "How long do you store my data?" (updated 2026-07-01) https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data — consumer retention including Claude Code; feedback kept 5 years.
- S187 — Anthropic (Claude Help Center), "Use Claude's chat search and memory to build on previous context" (last modified 2026-09-30) https://support.claude.com/en/articles/11817273-using-memory-in-claude — memory defaults by plan; memories outlive deleted chats; incognito.
- S241 — Google, "Gemini Apps Privacy Hub" (Privacy Notice 2026-06-29; hub 2026-09-24) https://support.google.com/gemini/answer/13594961 — human reviewers, three-year retention of reviewed chats, 72 hours with activity off.
- S050 — Anthropic Engineering, "How we contain Claude across products" (2026-05-25) https://www.anthropic.com/engineering/how-we-contain-claude — Cowork described as a local VM in May 2026: the out-of-date picture this lesson corrects.
- S185 — cximenez, reply by jahala, "Ask HN: What would you include in an academic workshop on vibe coding?" (about 2026-09-18; the page showed "24 days ago" on 2026-10-12) https://news.ycombinator.com/item?id=49745403 — privacy settings named as a thing to teach beginners.
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening" (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — Aaron's own gap: "chat, Cowork and Code across browser, desktop, CLI and cloud".
- S210 — Aaron Orelup, "AO-029: I asked where I was supposed to learn all this..." (2026-10-01) https://aaronorelup.com/ledger/the-missing-map/ — "what is CLI" and Docker on Aaron's list.

Added by the 2026-10-12 audit (credit on the lesson page):
- S132 — Anthropic (Claude Help Center), "Using Claude Code with your Pro or Max plan" ("Updated this week" as of 2026-10-12) https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan — a set `ANTHROPIC_API_KEY` bills the API instead of your plan (C022 point 7).

## Show it for real

- The Claude desktop app with its Chat, Cowork and Code tabs, or the merged message box without them, whichever the recording machine has, with the date on screen (S208, S102). Proves the surfaces are one app with different reach.
- The same small task (summarise a demo folder) in Chat, in Cowork with one connected demo folder, and in the Code tab on the same folder; show which one could read the files and which ran commands (S208, S069).
- The Code tab's environment picker: Local, Cloud, SSH, WSL (S208).
- Cowork's connected-folders list, then connecting one empty dedicated folder (S069, S184).
- Settings > Privacy with the "Help improve our AI models" toggle, and Settings > Memory with its topics list, on a demo account (S184, S187).
- PowerShell and CMD side by side: point at the `PS` prefix and run the same `&&` line in each (S206, S207).
- A cloud session at claude.ai/code still running after the laptop lid is closed (S129, S184).
- `claude --cloud` from a demo repository with no remote on macOS or WSL, showing the `Left on this machine:` notice naming a fake `.env` (S129). Do not record this on native Windows with anything real in tracked files.
- The ChatGPT desktop app's Work local or cloud choice (S025), if an account is available; otherwise a dated screenshot from OpenAI's page.

## Questions this lesson answers

- "What is the difference between ChatGPT, Work and Codex?" At OpenAI's own 2026-09-23 bootcamp, the presenter's colleague said the difference confused him at first (S008, talk 28:01, as logged by the research crew).
- "Should I use Claude chat, Cowork or Claude Code? The desktop app or the CLI?" (Aaron's list, S004.)
- "What is CLI?" and "What is Docker?" (Aaron's list, S210.)
- "How do I make sure my unpublished research isn't used for training?" A university AI librarian asked Hacker News what to teach in a vibe-coding workshop (about 2026-09-18), and one of four answers was to "ensure using the correct settings to (at least hypothetically) avoid models being trained on your unpublished research" (S185).
- "Does Cowork upload my files?", "Can a scheduled task run when my computer is off?", "Is my Pro plan private?", "Does deleting a chat delete what it remembers?" (C103's question list, answered by S069, S184, S186 and S187).
- "Why does it say `claude` is not recognized?", "Am I in PowerShell or CMD?" (the troubleshooting entries in S206 and S207 exist because people hit these).
- "Should I pick Local, Cloud, SSH or WSL?" (derived from S208; not yet seen in a beginner post).
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Choosing the folder; the home folder; hidden files → the-folder-is-the-agents-world
- Reading what the agent ran for its verb and target; what a cloud session's branch contains → save-points-and-the-agents-trail
- Model plus harness, and why the same model behaves differently in different products → model-harness-and-memory
- Commands run as you: deletes, permission modes, approval habits → before-you-let-it-loose
- PATH and environment variables as settings a program gets when it starts → keys-public-secret-and-leaked
- Which meter you are on, and one allowance shared across surfaces → know-your-meter
- Containers and VMs as the boundary; what a sandbox covers; checking from inside → contain-it-dont-babysit-it
- Browser and screen agents; compliance agreements that exclude features → the-narrowest-keys-and-verbs
- Cloud, background and scheduled agents running while you're away → agents-that-run-while-youre-away
- Work and personal accounts as part of what you build → every-automation-runs-as-someone
- Your users' data reaching AI providers → test-it-as-a-stranger and your-apps-ai-feature
- Which tool makes images, video and voice → making-media-with-ai

## Out-of-date framings to avoid

- "Claude is a chat website", or "Chat and Cowork are separate modes you pick" (S102).
- "Codex and ChatGPT are different AIs" (S008, S025). Also avoid the opposite: "every surface has the same models" (S025, 2026-09-22).
- "A desktop AI agent keeps my files on my computer." Anthropic's own engineering post of 2026-05-25 described Cowork as "The local VM", where "The user's selected workspace and .claude folder are mounted; nothing else on the host is visible" (S050); that is false for new Pro and Max tasks since 2026-10-06 (S184, S069). A good on-screen example of a vendor's own description going stale in four months.
- "The agent stops when I close my laptop" (S129, S184).
- "Paying for Pro means my chats aren't used for training." Pro is under consumer terms (S186).
- "Deleting the chat deletes what it knows about me" (S187, S186).
- "Learn the command line first" or "the terminal is dead." Vendors tell beginners they can skip it (S207); universities still teach it to those going deep (S209).
- "A command works the same in any terminal" (S206, S207).
- "A container is a security boundary by default" (S209: "Docker's isolation is weaker than VMs"; depth in 07.02).

## Legacy notes

No published lesson covers this slot as a whole; two give partial cover until it is made.

- **01.05 "Environment variables & PATH"** (published 2026-10-10, about 11.4 minutes). Still right: PATH as an ordered list; "not recognized" in its three wordings; open a new terminal after an install; "Claude Code reads your environment when it starts" (matches S207's new-window advice). These carry C122 point 3 for now. Its satchel metaphor and its keys-in-the-environment segment (`ANTHROPIC_API_KEY` switching billing) belong to 03.02 and 06.03, not here.
- **01.06 "Programs, processes & services"** (published 2026-10-11, about 10.8 minutes). Still right: a command starts a program that runs as you; agents start processes of their own; Claude Code's sandbox covers macOS, Linux and WSL2 but not native Windows (still true per S052). Task Manager, ports and leftover processes stay in the backlog until beginners ask; servers and ports feed 03.01.
- **What is missing from both:** the surfaces and how they differ (C022), the 2026-09-16 merge and the 2026-10-06 cloud default (S102, S184), local versus cloud versus SSH versus WSL (S208, S101, S129), VMs and containers (S209), and where data goes (C103).
- **What is outdated in both:** the retired map ("the first district, The Machine") and retired lesson numbers; one-laptop process counts and observed Python paths dated October 2026, which age quickly.
