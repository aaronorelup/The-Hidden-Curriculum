---
key: save-points-and-the-agents-trail
id: 01.03
title: "Git without typing it: save points and the agent's trail"
district: First Build
module: 01 Your workbench
status: todo
legacy: []
minutes: 10
concepts: [C117, C124]
sources: [S026, S208, S212, S117, S209, S206, S207, S052, S129, S101, S176, S177, S227, S142, S069, S211]
lead: [S117, S212]
---

# Git without typing it: save points and the agent's trail

**Purpose (the first spoken sentence):** In this lesson you'll learn what git's save points, parallel lines and remote copies are, and how to read the trail your agent leaves so you notice what it touched.

**Conclusion:** The agent types every git command, so your part is recognition: know that a save point and a copy elsewhere exist, which branch is live, what the diff changed, and whether it touched anything you never named.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Save points and the agent's trail." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 1 · First Build — How do I build my first thing?; module 01 Your workbench (last lesson of the module: 01.01 chose the folder, 01.02 the surface and machine; this one is the record of what happened there, before 02.01 lets the agent loose).

**Lead source (audit, 2026-10-12):** S117 (Anthropic (Claude Code docs)); S212 (Lovable). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S026, S208, S212, S117); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Rough time budget: C124 5.5 min · C117 4.5 min. Order: the three git ideas, each with a one-line real case (AO-043, S026, is a callback here; it is told in full in from-your-laptop-to-a-url), then the trail and the diff, then the defaults that decide what the agent may do with git today. Recognition only: show commands to recognise in the agent's trail, never to memorise.

### C124 Git: save points, parallel lines and the copy that lives elsewhere

1. **A commit is a save point.** MIT teaches git's model rather than its commands because "While an ugly interface has to be memorized, a beautiful design can be understood": "In Git, a history is a directed acyclic graph (DAG) of snapshots", each commit pointing to its parents, and "Commits in Git are immutable" (S209, Version Control and Git, 2026-01-16). The agent makes them when asked: "commit my changes with a descriptive message" (S206). The practitioners' habit: Cursor staff's recovery toolkit includes committing often before large agent changes, and a user calls "making many Git Commits per thread" best practice (S177, 2026-08-12 to 08-16). (S209, S206, S177) — **teach**
2. **A branch is a name pointing at a commit; one of them is live.** Branches are named references to commits (S209); "create a new branch called feature/quickstart" is a sentence to the agent, not a command to learn (S206). Which branch is live is a setting somebody chose: in Aaron's AO-043 a cloud session's push to a side branch was built and put into production about forty seconds later, and his site went back to August for 8 minutes 10 seconds (S026). One line here; the incident is told in full only in from-your-laptop-to-a-url (audit, 2026-10-12). Builder platforms work the same way: Lovable "edits and syncs one branch at a time", and "Commits on other branches don't appear in Lovable until you merge them into the synced branch" (S212). (S209, S206, S026, S212) — **teach** (the idea; AO-043 as a one-line case)
3. **A remote is a copy that lives elsewhere, and git is not GitHub.** "Git is not GitHub" (S209). Git with no remote dies with the folder: in S176 the `.git` folder went with the source, and the first recovery step a reply gave was to check Git remotes (S176). Uncommitted or unpushed work doesn't travel either: a cloud session "clones your current directory's GitHub remote at your current branch, not your local checkout, so push first if you have local commits" (S129). (S209, S176, S129) — **teach**
4. **Pushing is a decision, and a public remote is publishing.** In Claude Code's auto mode (the starting mode for terminal and VS Code sessions from v2.1.283), "Pushing to any branch of the repository you're working in, including the default branch" is allowed by default; before v2.1.203 a direct push to the default branch was blocked, so older advice is wrong (S052). The remote's own branch protection still applies (S052). And a public remote is a public place: PixelLeak (Glow Labs research of 2026-09-29, reported 2026-10-02) found coding agents that, lacking a private way to attach images, put internal screenshots in public GitHub repositories; one helper's default "creates a public gitshot-images repository"; the researcher counted more than 13,000 images from developers at more than 300 organisations, 93% under employees' personal usernames (the researcher's count, not independently audited) (S227). (S052, S227) — **teach**
5. **A pull request is a proposed change you review.** "After opening a PR, Claude Code monitors CI check results and can automatically fix failures or merge the PR once all checks pass" (S208); Claude Code's auto mode blocks "Merging a pull request no human has approved, approving Claude's own pull request, or disabling CI checks" by default (S052). Who decides what merges is 04.04; what counts as evidence is 06.02. (S208, S052) — **brief**
6. **Rewriting history breaks the other copies.** Lovable: "Do not force-push, rebase, or squash commits that are already on the synced branch" (S212). Claude Code's auto mode blocks force push, `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop` and amending a commit that has already been pushed, and runs `git status` itself before any command that would discard uncommitted work (S052). (S212, S052) — **brief** (recognise the names as the dangerous ones; no syntax)
7. **Checkpoints are not git.** "Checkpoints only track changes made through Claude's file editing tools. Changes made through Bash commands or external processes are not captured. This isn't a replacement for git" (S117). "Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed" (S101). (S117, S101) — **brief**

**Dropped from C124 for this lesson:** who has push rights to a client's repository and who owns the account → 08.03 every-automation-runs-as-someone (C129); preview and production branches on a host, deploys and rollback → 03.03 from-your-laptop-to-a-url (C127, C099); a secret that was pushed → 03.02 keys-public-secret-and-leaked (C071); worktrees and parallel agents → 08.01 and the backlog.

### C117 Reading the agent's trail: enough literacy to follow what it did

1. **Recognition, not operation.** "You won't need to learn Git yourself" (S207); git is now a conversation: "what files have I changed?", "show me the last 5 commits", "help me resolve merge conflicts" (S206). Aaron in May 2025, before agents typed for him: "Git was the worst of it", "doing git by hand, badly" (S211). What stays with you is knowing what each action touched. (S207, S206, S211) — **teach**
2. **Read each step for the verb and the target.** The verb says what kind of action it was (read, write, install, delete, commit, push, send, fetch); the target says what it acted on (a path, a branch, a remote, a URL, a host). Anthropic's Cowork safety page asks one thing of you during a task: "Is Claude accessing files or websites you didn't mention?" (S069). The action on a target you never named is the one to ask about: a push to the default branch (S026, S052), a new public repository (S227), a new remote (Claude Code's auto mode blocks "Changing where pushes go with `git remote set-url` or `git remote add`, unless you named the new remote", S052). And agents read questions as orders: "I see now that 'Can you change this?' is not permission" (an agent's reply quoted in S177). (S069, S026, S052, S227, S177) — **teach**
3. **What changed: the diff and the list of changed files.** In the desktop app, "After Claude edits files, a `+12 -1` indicator appears. Click it to open the diff view, review modifications file by file, and comment on specific lines" (S208). Cloud sessions show the same, such as `+42 -18`, against the base branch, with **Compare against** to pick another (S129). The list of changed files is the one review a non-coder can always do: look for a file you never asked about. (S208, S129) — **teach**
4. **Evidence is something you read.** "Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result" (S117). AO-043's fix added a `/version.json` to every build so a session can compare the live commit with the one it just pushed (S026). (S117, S026) — **teach**
5. **The trail itself.** The agent works on "Your git state. Current branch, uncommitted changes, and recent commit history", "Claude sees your current branch's files", and every message, tool use and result is kept in a plaintext transcript (S101). (S101) — **one line** (where the folder and transcripts live is 01.01)
6. **Where it stands and where it runs** → 01.01 (working directory) and 01.02 (laptop, cloud, SSH). **Where settings and secrets live** → 03.02. **localhost versus a public URL** → 03.03. — **one line each, as pointers**

**Dropped from C117 for this lesson:** the annotated-transcript demo at full length and "the job moved to directing" → 02.02 saying-what-you-want (C033); reading a change you can't read line by line, `git diff --stat` as outside evidence → 06.02 checking-what-you-cant-read (C012).

## You vs the agent

As of 2026-10-12:

- **The agent** types every git command: commits, branches, merges, resolves conflicts, pushes, opens pull requests, watches CI and fixes failures (S206, S208, S129). Asked, it lists the files it changed, shows whether a remote exists and whether it is public, names the default branch, and annotates its own trail with what each command read, wrote or contacted. In Claude Code's auto mode it may push to any branch of the working repository, including the default one, but is blocked by default from force push, discarding uncommitted work, changing remotes you didn't name, pushing secrets or personal data to a known-public repository, and merging a PR no human approved (S052).
- **You** check that a remote exists and is private or public as you intend, which branch is the default and which one your host deploys (S026), and what the diff changed, looking for anything you never named (S069, S208). You decide what merges and whether the agent may push to the live branch at all; a prose request is not a control, so if it must never happen, use an ask or deny rule or the remote's branch protection (S052; enforcement is 05.02). You ask for evidence rather than a claim (S117).
- **Bring in an expert** (C118) when history must be rewritten on a repository other people share, when a secret or personal data was pushed (the key must be revoked and rotated first: 03.02), or when you cannot tell what an action touched and the machine holds real credentials.

## Sources this lesson is built from

- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09; incident 2026-10-08) https://aaronorelup.com/ledger/the-branch-that-went-live/ — the stale default branch, the side branch that went live in about forty seconds, 8 minutes 10 seconds wrong, the four fixes and `/version.json`.
- S208 — Anthropic (Claude Code docs), "Get started with the desktop app" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/desktop-quickstart — the `+12 -1` indicator and diff view; "Review changes before committing"; PR monitoring that can fix and merge.
- S212 — Lovable, "Git sync" (with Glossary, Secrets and Custom domains; undated live docs, read 2026-10-12) https://docs.lovable.dev/integrations/git-sync-overview.md — one synced branch; other branches invisible until merged; no force-push, rebase or squash on it.
- S117 — Anthropic (Claude Code docs), "Best practices for Claude Code" (undated; content no earlier than 2026-09-25, names v2.1.283) https://code.claude.com/docs/en/best-practices — checkpoints are not git; show evidence rather than asserting success.
- S209 — MIT Missing Semester (SIPB IAP 2026), "Version Control and Git" (2026-01-16) https://missing.csail.mit.edu/2026/version-control/ — snapshots, a graph of commits, immutable commits, named references, "Git is not GitHub", design over interface. Older than three months, still current.
- S206 — Anthropic (Claude Code docs), "Quickstart" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/quickstart — git made conversational: commit, branch, show commits, resolve conflicts.
- S207 — Anthropic (Claude Code docs), "Terminal guide for new users" (undated live docs; example output shows v2.1.211) https://code.claude.com/docs/en/terminal-guide — "You won't need to learn Git yourself."
- S052 — Anthropic (Claude Code docs), "Choose a permission mode" (undated live docs; v2.1.283+, mentions v2.1.292; read 2026-10-12) https://code.claude.com/docs/en/permission-modes — what auto mode allows and blocks with git by default, and when that changed.
- S129 — Anthropic (Claude Code docs), "Use Claude Code in the cloud" (undated live docs; mentions up to v2.1.289) https://code.claude.com/docs/en/claude-code-on-the-web — cloud sessions clone the pushed branch, not your checkout; the cloud diff view.
- S101 — Anthropic (Claude Code docs), "How Claude Code works" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — git state as part of what the agent sees; remote actions can't be checkpointed.
- S176 — shuang_yang, replies by ActionGate and sattyamjjain, "Errible: AI out of control, randomly deleting files, 6-month project wiped out" (Cursor forum, 2026-10-03) https://forum.cursor.com/t/173688 — `.git` lost with the folder; check Git remotes first.
- S177 — Mohan Iyer, replies by Dean Rie (Cursor staff), FinDev and speaker, "What's the last AI-assisted change that created more recovery work than expected?" (Cursor forum, 2026-08-12, replies to 2026-08-16) https://forum.cursor.com/t/168209 — commit before big agent changes; an agent that took a question as permission.
- S227 — Hive Security, reporting Glow Labs research of 2026-09-29, "PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub" (2026-10-02) https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/ — agents publishing through public repositories nobody asked for; controls at the token and organisation, not only in instruction files.
- S142 — piscator, with the reply by Pooge, "Ask HN: Client took over development by vibe coding. What to do?" (2026-04-01) https://news.ycombinator.com/item?id=47599303 — "Why does the client have pushing rights to the repository?"
- S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — "Is Claude accessing files or websites you didn't mention?"
- S211 — Aaron Orelup, "AO-007: No VS Code, no terminal, no idea" (2026-08-08, describes May 2025) https://aaronorelup.com/ledger/no-vs-code-no-terminal/ — "Git was the worst of it": git by hand before agents typed it.

## Show it for real

- *(Moved to from-your-laptop-to-a-url, which tells AO-043 in full; audit 2026-10-12.)* AO-043 as a timeline from the post: 00:39 push, Cloudflare deploys about forty seconds later, 00:42 noticed, 00:47:58 rollback; the GitHub default-branch setting next to the host's production-branch setting (S026). Use Aaron's own screens only with his OK; otherwise a demo repository.
- In a demo repository, the agent creates a branch, commits twice and merges; animate the real `git log --graph` output as a branch graph before and after. Proves a branch is a name on a line of save points.
- The agent runs `git remote -v` in a demo project with no remote, then in one pushed to a private GitHub repository. Proves "is there a copy elsewhere" is a question with a visible answer.
- The desktop app after a small task: the `+12 -1` indicator, then the diff view file by file (S208); one changed file the prompt never mentioned, highlighted.
- An agent transcript from a demo session, each step labelled with its verb and target, and one step (a push to `main`) circled as the target nobody named.
- In a demo repository in auto mode, ask for a force push and record Claude Code's block (S052). Proves some git verbs are refused by default, and which ones.
- A checkpoint rewind that restores an edit made with the file tool but not a file deleted through a shell command (S117).
- A cloud session's `+42 -18` diff with "Compare against" (S129).

## Questions this lesson answers

- "Why does the client have pushing rights to the repository?" (Pooge on Hacker News, 2026-04-01, S142.)
- "Why did a side branch go live?" (Aaron's own incident, S026.)
- "What's the last AI-assisted change that created more recovery work than expected?" (Cursor forum, 2026-08-12, S177.)
- "Do I need to learn Git?" (derived from S207's "You won't need to learn Git yourself".)
- "Why don't my changes show up in Lovable?" (derived from S212.)
- "What does `+12 -1` mean?", "Did it touch anything outside what I asked?" (derived from S208 and S069; not yet seen in a beginner post.)
- "Why doesn't my cloud session see my latest changes?" (derived from S129.)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- The folder, the hidden `.git` folder and where transcripts live → the-folder-is-the-agents-world
- Laptop, cloud and SSH sessions, and what a cloud session uploads → where-your-agent-works
- Deletes, backups off the machine and permission modes → before-you-let-it-loose
- Treating "done, tests pass" as a claim → done-is-a-claim
- A secret in a commit: revoke and rotate; deleting the commit does nothing → keys-public-secret-and-leaked
- Preview and production branches on a host, deploys and rollback → from-your-laptop-to-a-url
- Who signs off on a merge or a release → before-you-ship-who-signs-off
- Rules that make a push impossible (deny and ask rules, hooks, branch protection) and which branch a cloud session reads its rules from → rules-it-reads-rules-it-cant-break
- Slices small enough to review, one commit per slice → plan-first-then-build-in-slices
- Accepting work you can't read line by line; CI and the diff as outside evidence → checking-what-you-cant-read
- Tokens that can't create public repositories; publishing as an action that needs a human → the-narrowest-keys-and-verbs
- Background and parallel agents, worktrees → agents-that-run-while-youre-away
- Push rights, repository owners and account hand-over → every-automation-runs-as-someone

## Out-of-date framings to avoid

- "Learn the git commands by heart before you start" (S207; S209 teaches the model, not the interface).
- "Git is my backup" when there is no remote (S176).
- "Checkpoints replace git" (S117).
- "If the agent says it's done, I don't need to look at what it ran" (S117).
- "The desktop app means I don't need any of this." It hides the terminal, not the effects (S208, S069).
- "The agent can't push to main unless I tell it to." In Claude Code's auto mode a push to any branch of the working repository, the default branch included, is allowed by default; direct pushes to the default branch were blocked only before v2.1.203 (S052).
- "Screenshots and other evidence are just files, not publishing" (S227).
- "A private repository makes it fine to commit secrets": Claude Code's auto mode blocks sensitive files entering a commit or push and says "the repository being private doesn't clear it" (S052; depth in 03.02).

## Legacy notes

No published lesson covers this slot. The old curriculum's git module was never made; legacy 01.03 pointed to "module eight, lesson eleven" for worktrees, which is retired. Aaron's own posts (S026, S211) are the first-hand material to tell in the third person.
