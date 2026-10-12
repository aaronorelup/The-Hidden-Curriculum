---
key: before-you-let-it-loose
id: 02.01
title: Before your agent runs commands on your computer
district: First Build
module: 02 Your first build
status: todo
legacy: []
minutes: [5, 6]
concepts: [C077, C081, C097]
sources: [S063, S052, S051, S226, S174, S175, S176, S225, S050, S178, S117, S069, S021, S023, S068, S156, S005, S025]
lead: [S063, S051]
---
# Before your agent runs commands on your computer

**Purpose (the first spoken sentence):** In this lesson you'll learn what to set up before you let a coding agent run commands on your computer, so that one wrong command can't take your files with it.

**Conclusion:** A command the agent runs acts as you, on every drive you can reach, and a shell delete skips the Recycle Bin; clicking "yes" at the prompt will not save you, so pick the permission mode and a tool with built-in delete guards before you start, keep a copy the agent can't reach, and at a delete prompt check the paths, not the code.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Before you let it loose." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; 02 Your first build. Lesson 7 of the path and the first lesson of module 02, so about 5 minutes by the course rule; set to 5-6 because it carries three must-priority concepts about permanent data loss, and cut to them by the 2026-10-12 audit (the earlier scope ran to about 2,200 words). The E: drive wipe (S176), "open one project folder" and "a copy on the same drive is not a backup" are told once, in the-folder-is-the-agents-world; here they are one-line callbacks. Lantern lesson. Requires C122 (the terminal, 01.02) and C123 (the folder is the agent's world, 01.01), both taught earlier on the path.

**Lead source (audit, 2026-10-12):** S063 (luck_li; reply by Colin (Cursor staff, Community Support Engineer)); S051 (Simon Willison). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S063, S052, S051, S226); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Settings and versions (audit, 2026-10-12):** the spoken script teaches the vendor-neutral model. Setting names, flags and version numbers appear only on one dated "as of" card per concept and on the lesson page, never in narration.

## What to teach (binding scope)

Cut to the mental model by the 2026-10-12 audit: this slot is about 5-6 minutes, so it carries the stakes, the one habit and the one decision. Teaching order: the stakes (C097 points 1 and 3), why "it asks me first" doesn't protect you (C077 points 1-2), the mode you choose before the run (C081 points 1, 2 and 4), the tool's guard in one sentence (C097 point 6), where the agent works and the copy it can't reach (C097 point 8), and the habit at the prompt (C097 point 9). Everything else moved to another lesson or to the lesson page, as marked.

### C097 Deletes run as you: make the dangerous ones impossible, and check targets, not syntax

1. **A command the agent runs runs as you.** It has your permissions on every drive you can reach. On 2026-10-09 a Cursor user asked the agent to delete "a single deprecated project directory". The agent ran `cmd /c "rd /s /q ..."`, and the whole D: drive went in about 105 seconds (the timing comes from the agent's own transcript as quoted in the post): a chat-history database, several source projects and installed applications. Cursor staff replied that "Terminal commands on Windows don't run in a sandbox, so your confirmation is the main safeguard" (S063, re-opened 2026-10-12). **Depth: teach.** It is the opening case.

2. *Moved to the lesson page (audit, 2026-10-12):* the other wipe reports (S174; S176's E: drive is told once, in the-folder-is-the-agents-world). The opening case is enough for a 5-6 minute lesson.

3. **Shell deletes skip the Recycle Bin.** `rd /s /q` and `rmdir /s /q` remove files outright. All three reports say nothing came back from the bin (S063, S175, S176). **Depth: one line.** Put it on screen.

4. *Moved (audit, 2026-10-12) → contain-it-dont-babysit-it:* how one quoted path became the drive root, as the reason the guard has to be mechanical (S063, S050).

5. *Moved (audit, 2026-10-12) → the-narrowest-keys-and-verbs:* commands that never say "delete" (S226's `prisma migrate diff` against production) and S225's found token, as the case for keeping production credentials out of reach.

6. **Some tools block drive wipes mechanically; others leave it to your click.** Claude Code denies the drive-wipe patterns behind S063 and S174 in every mode (S052); Cursor on native Windows has no sandbox, and its File-Deletion Protection does not cover terminal commands (S063). **Depth: one line.** The vendor-by-vendor detail is on the lesson page (below), not in the narration.

7. *Moved (audit, 2026-10-12) → contain-it-dont-babysit-it:* each safety feature protects one path (S063, S178).

8. **Keep the agent's world small, and keep a copy it can't reach.**
   - Open the agent on one project folder, never a whole drive. Cursor staff: Cursor "limits commands to the folder it's opened in by default" (S175). The folder is not a wall (01.01), which is why points 6 and 9 still matter.
   - A backup on the same drive died with the project in S176. The advice given there: keep a backup "that the agent's shell can't reach at all" (S176).

   **Depth: one line each.** Backups, remotes and undo are taught in 01.03 and 03.03 (C098).

9. **At a delete prompt, check the targets, not the syntax.** Ask the one question a non-coder can answer: is every path in the agent's target list inside my project, and is it what I meant? Have the agent print the resolved list of paths before it deletes anything. Three sources point the same way:
   - Anthropic's safety page for Cowork asks you to watch for one pattern: "Is Claude accessing files or websites you didn't mention?" (S069).
   - Claude Code's own classifier won't pass a recursive delete whose target it can't resolve until "you name the exact path being deleted" (S052).
   - The S174 reporter asked Cursor to abort a delete when its output shows paths outside the target (S174).

   No source reports a printed target list stopping a wipe. This point is the course rule applied: the target list is the part a beginner can check. **Depth: teach.** This is the lesson's main habit.

10. *Moved to the lesson page (audit, 2026-10-12):* the first hour after a wipe. In the narration, one line inside point 9 at most: stop writing to that drive; recovery is a specialist's job (S063, S176).

### C077 Approval fatigue: people are weak per-step approvers

1. **People approve almost everything.** Users approved about 93% of permission prompts in Anthropic's May 2026 telemetry (S050) and 97% in its August 2026 post (S051, from Anthropic's primary post read with it). **Depth: teach.**

2. **The planted-command test.** In a controlled study of 1,053 paid testers, one prompt mid-session was swapped for a clearly dangerous command. Only 13.6% refused it (143 of 1,053). Human refusal fell from about 17% early in a session to about 5% after 50 or more prompts. Auto mode's classifier blocked 89% of the same commands (S051 and Anthropic's post, 2026-08-07, re-opened 2026-10-12). **Depth: teach.** This is the lesson's key number.

3-6. *Moved to the lesson page (audit, 2026-10-12):* how people widen permissions to escape prompts, rules written up front, one yes dropping a deny list, and what follows (decline-in-advance list, deny rules over ask rules, `/permissions`, urgency as a red flag). Deny rules and hooks are taught in rules-it-reads-rules-it-cant-break (05.02).

### C081 Choose the permission mode deliberately

1. **The mode is a dial from "asks before nearly everything" to "asks before nothing".** Claude Code's modes (S052, re-read 2026-10-12):

   | Mode | What runs without asking |
   |---|---|
   | Manual (`default`) | reads only |
   | `acceptEdits` | reads, file edits, common filesystem commands |
   | `plan` | reads and exploring; edits wait for a plan you approve |
   | `auto` | most actions, reviewed by a second model (the classifier) instead of you |
   | `dontAsk` | only pre-approved tools; anything else is denied (for unattended scripts) |
   | `bypassPermissions` | everything |

   **Depth: teach** the dial; show the table, and don't drill all six.

2. **You are probably in auto mode right now.** Since late September 2026 (Claude Code v2.1.283: the version goes on the dated card, not in the narration), auto is the built-in starting mode for interactive terminal and VS Code sessions on every plan and provider. Before that it was the default only on Pro, Max and Team, from 2026-08-14 (S052, S051). Organisations with the HIPAA configuration start in Manual (S052). The status bar shows the mode (`⏵⏵ auto mode on`, `⏸ manual mode on` ...), and Shift+Tab cycles through the modes (S052). **Depth: teach.** "Look at the status bar" is the habit.

4. **Bypass belongs in a disposable box, never on your own laptop.** It "offers no protection against prompt injection or unintended actions". Use it only "in isolated environments like containers, VMs, or dev containers without internet access" (S052). **Depth: teach.**

3, 5-7. *Moved to the lesson page (audit, 2026-10-12):* auto mode as a reviewer, not a guarantee; limits that hold in every mode; other tools' names for the same dial (Cursor, Codex, Cowork); checking a run you didn't watch (done-is-a-claim).

## On the lesson page, not in the narration

Kept here so the lesson page can carry it with its sources (moved out of the binding scope by the 2026-10-12 audit). Setting names and version numbers belong on a dated "as of" card or this page, never in narration. The depth marks below are from the earlier scope and no longer apply.

**The vendor detail behind C097 point 6:**

- **Claude Code** (S052, re-read 2026-10-12):
  - From v2.1.283, `rd`, `rmdir`, `del` and `erase` run through `cmd` against a system path are denied "in every mode, without asking you".
  - A PowerShell variable after literal text counts as empty, so `cmd /c rd /s /q "C:\$name"` is treated as a removal of `C:\` and denied.
  - `Remove-Item` on a system path, or on a bare `*` or `\*`, is denied outright.
  - No allow rule or hook can approve `rm` or `rmdir` on a critical path. The docs call this a circuit breaker that "guards against model error".
  - Auto mode blocks "Irreversibly destroying files that existed before the session" and "Production deploys and migrations" by default, and Claude Code runs `git status` itself before a command that would discard uncommitted work.
- **Cursor on native Windows:** no sandbox, and File-Deletion Protection "applies to the Agent's own file-delete action, not to terminal commands like `rd` or `rmdir`" (S063). Staff advice: never allowlist `rmdir`, `rd`, `del`, `Remove-Item` or `cmd`; keep destructive commands behind manual approval; hooks are "the strongest gate"; keep git and backups as the safety net. The pattern is "tracked", with "no timeline to share" (S174, staff reply 2026-07-30). The Cursor changelog for September and October 2026 shows no fix (Cursor changelog, listed in sources.md as a read-with companion of S025; read 2026-10-12).
- **Your own guard, written by the agent:** a deny rule or a hook that blocks recursive deletes outside the project. "Claude can write hooks for you" (S117). How hooks work is taught in 05.02.

**Depth: brief.** The idea to land is "mechanical guard versus your eyes". Show one docs screen, not the whole list.

**C097 point 10, the first hour after a wipe:**

- Stop writing to that drive, and don't let the agent run more commands on it.
- Run Recuva, PhotoRec or TestDisk from another drive, and restore to a different drive. On an SSD the chances drop quickly.
- Look for copies elsewhere: a git remote, CI or deploy checkouts, Cursor Local History (kept on C:), and Windows Previous Versions if System Protection was on.

(S063, S176, S174) **Depth: brief**, as one screen to recognise later.

**C097 point 2, the other wipe reports:**

- late July: a trailing backslash before a closing quote, run through `cmd /c`, deleted about 210,201 files in about 40 seconds, and the agent read its own exit code 32 as a *failed* cleanup while its error output listed paths outside the target (S174);
- 2026-10-03: the user approved the agent's own plan with "Okay, follow the recommendation and delete them". The plan said to clear only a temporary build folder. The command that ran deleted the source code, `.git`, the publish folder and both backups on the same E: drive (S176). This one shows that approving the *intent* is not approving the *command*.

**Depth: brief.**

**C077 points 3-6:**

3. **People widen permissions to escape prompts** (Anthropic's post, read with S051):
- 62% have used bypass or "don't ask again" on Bash;
- 25% of interactive sessions start in bypass mode;
- 43% have interpreter-style allow rules such as `Bash(python:*)`, which effectively allow any code;
- 5% allow any shell command outright.

   Anthropic's own docs say it plainly: "After the tenth approval you're clicking through rather than reviewing" (S117). **Depth: brief.** Put one or two of these on screen, not all four.
4. **Writing your own rules up front doesn't fix it.** In a study of 113 people without software backgrounds, 114 of their 140 rules were set to "ask", and they blocked less overreach than approving each action did (Ting Yan, arXiv 2608.27443, via S021). Marmelab's line: "A rule that ends in a prompt isn't a rule" (S021). **Depth: one line (optional).**
5. **One yes can switch off a control you built.** Cursor staff explain that an approved full-network request "drops your deny list for that command" (S023). **Depth: one line (optional).** Sandboxes and their network rules are taught in 07.02.
6. **What follows from all this:**
- Keep human approval for the few irreversible actions, and decide in advance which prompts you always decline: production, deploys, full network, moving the workspace (S023, S050).
- Make must-nevers deny rules, not ask rules. Deny rules block in every mode (S021, S052).
- Look at the allow rules you have collected (`/permissions`) (S051 primary).
- Treat urgency or pressure around an approval as a red flag. In a UK AI Security Institute stress test retold by Mollick, an agent created fake identities to pressure the human who had to approve its change; no real harm occurred (S068).

**Depth: teach** the first two; one line each for the last two.

**C081 points 3, 5, 6 and 7:**

3. **Auto mode is a reviewer, not a guarantee.** The docs say it "does not guarantee safety" and to use it "for tasks where you trust the general direction, not as a replacement for review on sensitive operations". It falls back to prompting you after 3 blocks in a row or 20 in total (S052). Anthropic: "For high-stakes changes to production infrastructure, we still recommend reviewing Claude's actions yourself" (S051 primary). **Depth: brief.** How the classifier can be fooled is 07.01's job (C076).
5. **A few limits hold in every mode.** Deny rules block even in bypass, and a critical-path `rm` is never approved by an allow rule or a hook (S052). **Depth: one line**, linking back to C097 point 6.
6. **Other tools have the same dial under other names** (S063, S156, S069):
- Cursor's run modes are Ask Every Time, Allowlist, Auto-Review and Run Everything (Settings > Agents > Approvals & Execution). After the D: wipe, staff recommended Ask Every Time, or Allowlist with an empty list.
- Codex sets approvals and the sandbox separately, and calls `--yolo` "not recommended".
- Claude Cowork has Automatically approve, Skip all approvals and Manually approve. Switch to Manually approve for sensitive files, accounts or sites; for a tool, plugin or site you're using for the first time; and when "Mistakes would be hard to undo, like sending messages or making purchases".

**Depth: brief.**
7. **The less you watched a run, the more you check it afterwards** (S005). **Depth: one line**, handing off to 02.04.

## You vs the agent

As of 2026-10-12:
- **The agent and the tool** own the syntax. The agent writes and runs the commands. It can print its resolved targets before deleting, and it can write the deny rules and hooks for you (S117). Claude Code's built-in checks deny the drive-wipe patterns from S063 and S174 mechanically (S052). The agent cannot be trusted to notice its own quoting error before the damage, may misread the result (exit code 32 reported as a failed cleanup while it was deleting a drive, S174), and may guess at what a command or token will touch (S225, S226).
- **You decide before the run:**
  - which tool and which mode, per task (check the status bar);
  - that bypass happens only in a disposable box;
  - where a tool has no mechanical delete guard (Cursor on native Windows), that deletes stay on manual approval and off the allowlist;
  - that the agent opens on one project folder;
  - that a copy exists off the machine before big changes;
  - that production credentials stay out of reach;
  - which prompts you always decline.

  (S052, S063, S174, S175, S176)
- **You check at the prompt:** the targets, not the syntax. Is every path in the agent's target list inside the project, and is it what you meant? (S069, S052)
- **Bring in an expert (C118):** if the data matters and your own recovery-tool attempt fails, bring in a professional data-recovery service. The sources list only the tools, so this step is the course rule applied: you can't verify a recovery yourself. A restore plan for a production database needs someone who has done one on that provider (03.03, C098).

## Sources this lesson is built from

- S063 — luck_li, with a reply by Colin (Cursor staff), "[Agent] Autonomous rd /s /q wiped the entire D: drive (Windows)" (2026-10-09) https://forum.cursor.com/t/174156 — the opening case, "no sandbox on Windows, your confirmation is the main safeguard", the scope of delete protection, the run modes staff recommend, the recovery steps, and the links to earlier reports. Re-opened 2026-10-12.
- S052 — Anthropic (Claude Code docs), "Choose a permission mode" (undated live docs; v2.1.283+, re-read 2026-10-12) https://code.claude.com/docs/en/permission-modes — the modes, auto mode as the starting mode, the bypass warning, deny rules in every mode, the critical-path circuit breaker, the `cmd` and `Remove-Item` delete checks, and the delete and migration actions auto mode blocks by default.
- S051 — Simon Willison, "Auto mode is now the default in Claude Code for Pro, Max, and Team plans" (2026-08-08) https://simonwillison.net/2026/Aug/8/auto-mode/ — the 1,053-tester study and the 13.6% refusal rate. Read with Anthropic's primary post of the same title (2026-08-07) https://claude.com/blog/auto-mode-default-in-claude-code, which carries the 97%, the drop from 17% to 5%, the 62/25/43/5% figures and the advice to review production changes yourself. Credit Anthropic on screen for those numbers. Both re-opened 2026-10-12.
- S226 — Florian Burnel (IT-Connect), "Claude Opus 5 wipes a production database, and it wasn't its fault" (2026-07-30) https://www.it-connect.tech/claude-opus-5-wipes-a-production-database-and-it-wasnt-its-fault/ — a command that never says "delete" (`prisma migrate diff`) resetting 22 production tables by design. Re-opened 2026-10-12.

Also cited for single points (credit on the lesson page):
- S174 — Aleksey Solodkevich, with a staff reply by Mohit (Cursor), "[Windows] Agent Shell: rmdir /s with trailing \ before " escapes target and wipes volume root" (2026-07-29) https://forum.cursor.com/t/166931 — 210,201 files in about 40 s, exit code 32, and the staff advice (no delete commands on the allowlist, hooks, "tracked", no timeline). Re-opened 2026-10-12.
- S175 — Mr.Cheng, with replies by Dean Rie (Cursor), "Agent wiped D: drive instead of deleting one folder" (2026-08-29) https://forum.cursor.com/t/169919 — about 80 GB lost, "automatically executed", and opening one project folder. Re-opened 2026-10-12.
- S176 — shuang_yang and replies, "Errible: AI out of control, randomly deleting files, 6-month project wiped out" (2026-10-03) https://forum.cursor.com/t/173688 — approving the agent's own plan, backups on the same drive, a backup the shell can't reach. Re-opened 2026-10-12.
- S225 — Thomas Claburn (The Register), "Cursor-Opus agent snuffs out startup's production database" (2026-04-27) https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442 — one line only.
- S050 — Anthropic Engineering, "How we contain Claude across products" (2026-05-25) https://www.anthropic.com/engineering/how-we-contain-claude — the 93% approval rate and "shouldn't be expected to judge bash incantations".
- S178 — Anthropic (Claude Code docs), "Checkpointing" (undated live docs, re-opened 2026-10-12) https://code.claude.com/docs/en/checkpointing — rewind doesn't cover Bash deletes.
- S117 — Anthropic (Claude Code docs), "Best practices for Claude Code" (undated; names v2.1.283; re-opened 2026-10-12) https://code.claude.com/docs/en/best-practices — "After the tenth approval..." and "Claude can write hooks for you".
- S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06; "Updated this week" on 2026-10-12) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — the "files or websites you didn't mention?" check and when to switch to Manually approve. Re-opened 2026-10-12.
- S021 — François Zaninotto (Marmelab), "The State Of AI Harness Engineering 2026" (2026-09-24) https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html — "A rule that ends in a prompt isn't a rule", and the Ting Yan study.
- S023 — Brunno Oliveira Prego, with replies by Mohit (Cursor), "Agent repeatedly ignores workspace User Rules and repo gates across multiple chats" (2026-09-02) https://forum.cursor.com/t/170277 — an approved network request drops the deny list.
- S068 — Ethan Mollick, "Agency and Agents" (2026-08-31) https://www.oneusefulthing.org/p/agency-and-agents — an agent pressuring its approver (AISI stress test).
- S156 — OpenAI, "Codex: Agent approvals & security" (undated live docs; references Codex 0.115) https://learn.chatgpt.com/docs/agent-approvals-security — approvals and the sandbox as separate settings; `--yolo` not recommended.
- S005 — Anthropic Academy, "Claude Code 101" (undated; live on 2026-10-12) https://anthropic.skilljar.com/claude-code-101 — verify unwatched runs harder.
- Cursor, changelog (read-with companion of S025, whose main entry is OpenAI's changelog; read 2026-10-12) https://cursor.com/changelog — no Windows sandbox or quoting fix listed for September or October 2026 (currency check only, not shown on screen).

## Show it for real

- In Claude Code, press Shift+Tab and watch the status bar go from `auto mode on` to `manual mode on`, `accept edits on` and `plan mode on`. Proves you can always see and change the mode, and that a fresh session likely starts in auto (S052).
- *(Lesson page only, with C077 point 6.)* Run `/permissions` in a demo profile seeded with a few typical allow rules, and point at a broad one such as `Bash(python:*)`. Proves how approvals pile up into standing permission (S051 primary; C077).
- *(Moved with C097 point 4 to contain-it-dont-babysit-it.)* In a scratch folder, take a nested-quote `cmd /c` command against a path with spaces and replace `rd` with `echo`, so it only prints the arguments it actually received. No deletion. Proves the text and the effect can differ. If the recording machine doesn't show the target widening, cut this demo rather than staging it (mechanism from S063, S174).
- Open the permission-modes page at "Critical paths" and at the `cmd` and `Remove-Item` checks. Then, in a scratch project, ask the agent for a cleanup and have it print the resolved target list first, and check each path against the project folder on screen. Proves the habit (S052, S069).
- *(Moved with C097 point 7 to contain-it-dont-babysit-it.)* In a scratch git repo, have Claude Code delete a test file through Bash, then open `/rewind` and show there's no code restore for it. Proves checkpoints don't cover shell deletes (S178).
- *(Lesson page only.)* Open Cursor's Settings > Agents > Approvals & Execution next to the File-Deletion Protection toggle. Proves the two settings guard different paths (S063).
- Run `git remote -v` in a project with no remote (empty output) and in one pushed to GitHub. Proves whether a copy exists off the machine (S176; depth in 03.03).
- Show a screenshot of the S063 thread's title and date (a public post with no personal data). Proves this happened this week, not in theory.

## Questions this lesson answers

- How did the AI delete my whole drive when I asked it to delete one folder? (the titles of S063 and S175)
- Why aren't the files in the Recycle Bin? (S063, S175, S176)
- Is the agent's terminal sandboxed? (S063)
- Can Cursor or Claude Code delete files outside my project? (S175)
- The agent deleted my files; can I get them back? (S063, S176)
- Would you still let an AI run destructive commands directly, or want an approval step first? (ActionGate's reply in S176)
- How did a migration command delete my database? (S226)
- Should I approve every command the agent runs? Is "don't ask again" safe to click? (C077)
- Which permission mode should I use, and which am I in right now? What's the difference between auto and bypass? When is bypass OK? (C081)
- Does rewind undo what the agent deleted? (S178)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- The folder as the agent's world, and why it is not a wall → the-folder-is-the-agents-world
- What a terminal and a shell are; reading what a command touches → where-your-agent-works
- Reading the agent's trail (verb and target); a git remote as the copy that lives elsewhere → save-points-and-the-agents-trail
- What each undo covers; backups, rollback and production databases (C098) → from-your-laptop-to-a-url
- Deny rules and hooks as the things that actually enforce → rules-it-reads-rules-it-cant-break
- How auto mode's classifier can be fooled by prompt injection (C076) → whose-words-is-it-reading
- Sandboxes, containers and VMs; what Claude Code's sandbox covers (C078-C080) → contain-it-dont-babysit-it
- Production tokens and narrow scopes (S225's token made for another job) (C082, C083) → the-narrowest-keys-and-verbs
- Auto-accept on untrusted or unfamiliar repos (C090) → other-peoples-code
- Unattended and scheduled runs → agents-that-run-while-youre-away
- Checking a run you didn't watch → done-is-a-claim

## Out-of-date framings to avoid

- "Read every command before you approve it and you're safe." People approve almost everything, and the syntax misled the vendor's own staff (S050, S063). This course taught it until 2026-10-12; see Retired concepts in concepts.md.
- Teaching shell quoting rules (`cmd` versus PowerShell escaping) as something the viewer must learn to spot. Explain the quoting only as the reason the guard has to be mechanical.
- "If it asks permission it can't do damage" and "approve every action and you're in control" (S051, S021).
- "The agent runs in a sandbox, so it can't hurt my machine." Not on native Windows in Cursor (S063). Claude Code's own sandbox is taught in 07.02.
- "I turned on delete protection." It covers one tool (S063).
- "Deleted files go to the Recycle Bin" (S063, S175).
- "Rewind will undo it" (S178).
- "Only a command with 'delete' in it can destroy data" (S226).
- "`--dangerously-skip-permissions` is fine on my laptop if I'm watching" (S052).
- "Auto mode is the same as bypass", or "auto mode means safe" (S052).
- "I made a backup copy in the project folder, or on the same drive" (S176).
- "Auto-run is fine because the agent is careful" (S063).

## Legacy notes

No legacy lesson covers this slot. Legacy 01.03 and 01.04 (folders, paths, dotfiles) hold the ground this lesson points back to through 01.01. Legacy 00.06, scene 07, tells a 2025 Replit production-database deletion. That case is not among this lesson's sources, and the 2026 incidents above (S063, S174, S176, S226) replace it.
