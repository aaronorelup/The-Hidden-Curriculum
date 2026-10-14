# Point check: S206, S208, S210, S241 (where-your-agent-works)

Checked 2026-10-14 against the live pages. Only the points the spec takes from each source.

## S206 — Anthropic (Claude Code docs), "Quickstart" (undated live docs; read 2026-10-14) https://code.claude.com/docs/en/quickstart

- C122.1, `&&` error: SUPPORTED, verbatim. "If you see `The token '&&' is not a valid statement separator`, you're in PowerShell, not CMD." The page also has the reverse case: "If you see `'irm' is not recognized as an internal or external command`, you're in CMD, not PowerShell." Same page: "your prompt shows `PS C:\` when you're in PowerShell and `C:\` without the `PS` when you're in CMD."
- C122.3, "not recognized" means PATH: SUPPORTED, verbatim. "When the installer finishes, open a new terminal window and run `claude --version`. ... If your shell says `claude` isn't found or isn't recognized, the install directory isn't on your PATH yet: see Fix your PATH."
- C122.4, the agent's shell on Windows: SUPPORTED, quote verbatim. "Git for Windows is recommended on native Windows so Claude Code can use the Bash tool. If Git for Windows is not installed, Claude Code uses PowerShell as the shell tool instead. WSL setups do not need Git for Windows." Wording note: the page says "the Bash tool", not "Git Bash"; the spec's paraphrase "uses Git Bash when Git for Windows is installed" is a fair reading but is not the page's words.
- Sources entry, "A terminal or command prompt open": SUPPORTED, verbatim (Before you begin).
- "You vs the agent" ("A coding agent ... fixes PATH problems (S206)"): NOT SUPPORTED by S206. The page sends the reader to a Fix your PATH page; it does not say the agent fixes PATH. Treat it as the course's own framing or source it elsewhere.

## S208 — Anthropic (Claude Code docs), "Get started with the desktop app" (undated live docs; read 2026-10-14) https://code.claude.com/docs/en/desktop-quickstart

- C022.1, three tabs: SUPPORTED. "The desktop app has three tabs: Chat: General conversation with no file access, similar to claude.ai. Cowork: An autonomous background agent that works on tasks independently while you do other work. Code: An interactive coding assistant with direct access to your local files."
- C022.3, quickstart still shows three tabs: SUPPORTED as of 2026-10-14 (no mention of the Chat/Cowork merge on this page).
- C022.5 / C128.2 / demo, Local, Cloud, SSH, WSL: SUPPORTED. "Select Local to run Claude on your machine using your files directly." "Cloud: Run sessions in the cloud that continue even if you close the app." "SSH: Connect to a remote machine over SSH, such as your own servers, cloud VMs, or dev containers. Desktop installs Claude Code on the remote machine automatically the first time you connect." "WSL (Windows): Run the session inside a WSL 2 distribution; Claude Code, tools, and git execute on the Linux side with native paths." New caveat on SSH not in the spec: a running task "can keep going while Desktop is disconnected, but with a Claude account it can stop when its sign-in expires."
- C122.5, its own terminal pane: SUPPORTED. "Drag the chat, diff, terminal, file, and browser panes into whatever layout you want. Open the terminal with Ctrl+` to run commands alongside your session."
- Sources entry, no Node.js needed: SUPPORTED. "The desktop app includes Claude Code, so you don't need to install Node.js or the CLI to use the Code tab."
- Context: the Code tab requires "a Pro, Max, Team, or Enterprise subscription."

## S210 — Aaron Orelup, "AO-029: I asked where I was supposed to learn all this..." (2026-10-01) https://aaronorelup.com/ledger/the-missing-map/

- "What is CLI?" on Aaron's list: SUPPORTED. The post says his list ran from "what is CLI" through webhooks, licences, installers, worker threads and passkeys (question asked 2026-09-30).
- Docker on Aaron's list: PARTLY SUPPORTED. Docker appears only in the post's narration (he asked where he should have learned "terminals, `.venv`, API keys, OAuth, Docker and the rest"), not in the quoted list itself. Fine to say "Docker was on Aaron's list of gaps"; do not put "What is Docker?" in quote marks as his words.

## S241 — Google, "Gemini Apps Privacy Hub" https://support.google.com/gemini/answer/13594961 (page now reads "Last updated: October 13, 2026" for the hub, the Privacy Notice and Privacy questions)

- Human reviewers: SUPPORTED. Human reviewers "review some of the data we collect for these purposes."
- Three years: SUPPORTED. "Reviewed chats are retained for up to three years." Reviewed chats "are not deleted when you delete your activity."
- 72 hours with Keep Activity off: SUPPORTED. "Temporary chats and chats you have when Keep Activity is off are retained with your account for 72 hours and used to: ..."
- Confidential warning: SUPPORTED. "Please don't enter confidential information that you wouldn't want a reviewer to see or Google to use to improve our services, including machine-learning technologies." (The spec quotes the first half only; fine.)
- Dates: CHANGED. The spec's dates (Privacy Notice 2026-06-29; hub 2026-09-24) are out of date; all three now show 2026-10-13. The four points above still read the same. Date the on-screen card "as of 2026-10-14 (page updated 2026-10-13)" and update sources.md.
