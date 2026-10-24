# Point checks: S177, S206, S207, S209, S211, S227

Checked 2026-10-23 against the live pages. For each source: the credit line, then each point the spec takes from it, as the source states it.

## S177 (Cursor forum thread)

**Credit:** Mohan Iyer (thread), replies by Dean Rie (Cursor staff), FinDevAI and "speaker", "What's the last AI-assisted change that created more recovery work than expected?", Cursor forum, opened 2026-08-12, replies to 2026-08-16. https://forum.cursor.com/t/168209

- Thread question and date (spec: Questions, 2026-08-12). SUPPORTED. Mohan Iyer opened it on 2026-08-12.
- "Cursor staff's recovery toolkit includes committing often before large agent changes" (C124 point 1). SUPPORTED. Dean Rie (Cursor staff), 2026-08-13: "Git with frequent commits before big Agent changes". The same toolkit lists Agent checkpoints, IDE Local History and Plan mode, and says to review destructive commands before approving them.
- A user calls "making many Git Commits per thread" best practice (C124 point 1). SUPPORTED. FinDevAI, 2026-08-15: "...frequent Github commits, with verbose messages, leaves a very usable history, making many Git Commits per thread is best practice."
- "I see now that 'Can you change this?' is not permission" is an agent's reply quoted in S177 (C117 point 2). SUPPORTED. Posted by "speaker" on 2026-08-16, quoting the agent: "I assumed you meant it was OK to proceed. I see now that "Can you change this?" is not permission." The context: the agent kept making changes even though a rule required it to ask permission first.
- Spec date range "2026-08-12 to 08-16". SUPPORTED.

## S206 (Claude Code docs, Quickstart)

**Credit:** Anthropic, Claude Code docs, "Quickstart" (undated live docs; read 2026-10-23). https://code.claude.com/docs/en/quickstart

- "git made conversational". SUPPORTED. Step 5: "Claude Code makes Git operations conversational:"
- "commit my changes with a descriptive message". SUPPORTED, verbatim.
- "create a new branch called feature/quickstart". SUPPORTED, verbatim, listed under "more complex Git operations".
- "what files have I changed?", "show me the last 5 commits", "help me resolve merge conflicts". SUPPORTED, verbatim.
- The You-vs-agent line cites S206 for the agent committing, branching and resolving conflicts. SUPPORTED. The page has nothing on pushes, pull requests or CI; for those the spec also cites S208 and S129, which were not checked here.

## S207 (Claude Code docs, Terminal guide for new users)

**Credit:** Anthropic, Claude Code docs, "Terminal guide for new users" (undated live docs; read 2026-10-23). https://code.claude.com/docs/en/terminal-guide

- "You won't need to learn Git yourself." SUPPORTED, verbatim. Caveat on context: the sentence sits in the Windows step "Install Git for Windows (optional)": "Git for Windows provides Git Bash, which enables the Bash tool. Without it, Claude Code uses PowerShell instead. You won't need to learn Git yourself." So it is about installing Git so the agent has a shell, not a general claim about git. Using it as "you won't need to learn git" is fair. Quote the sentence as it stands and do not widen it.
- Example output shows v2.1.211 (sources entry). SUPPORTED: "prints a version number such as `2.1.211 (Claude Code)`".

## S209 (MIT Missing Semester 2026, "Version Control and Git")

**Credit:** MIT Missing Semester (supported by SIPB; videos by MIT Open Learning), "Version Control and Git", lecture of 2026-01-16 (date from the 2026 schedule page; the lecture page itself is undated). https://missing.csail.mit.edu/2026/version-control/

- "While an ugly interface has to be memorized, a beautiful design can be understood". SUPPORTED, verbatim.
- "In Git, a history is a directed acyclic graph (DAG) of snapshots". SUPPORTED, verbatim.
- Each commit points to its parents. SUPPORTED. Each commit records a set of parent commits; it is a set because a merge can have several parents.
- "Commits in Git are immutable". SUPPORTED, verbatim.
- "Branches are named references to commits". SUPPORTED as a paraphrase. The source says "References are pointers to commits", that references are mutable (they can be moved to point at a new commit), and gives names like `master` as examples. If it appears in quotation marks on screen, use "References are pointers to commits".
- "Git is not GitHub". SUPPORTED, verbatim.
- Date 2026-01-16. SUPPORTED by the schedule line "1/16: Version Control and Git" on https://missing.csail.mit.edu/2026/. The page has no organiser line saying "SIPB IAP 2026"; the acknowledgments credit SIPB and MIT Open Learning.

## S211 (Aaron Orelup, AO-007)

**Credit:** Aaron Orelup, "AO-007: No VS Code, no terminal, no idea" (aaronorelup.com ledger, 2026-08-08, describing May 2025, his first month of AI projects). https://aaronorelup.com/ledger/no-vs-code-no-terminal/

- "Git was the worst of it". SUPPORTED, verbatim.
- "doing git by hand, badly". SUPPORTED as a fragment of "I was doing git by hand, badly, and making mistakes I then had to undo."
- "May 2025, before agents typed for him". SUPPORTED. The post describes May 2025. It also says "So GitHub was a wall, not a tool" and that he "only much later found out VS Code will just do the git for you."
- The sources entry notes the post was drafted by Claude from his transcripts. Tell it in the third person, as the spec says.

## S227 (Hive Security on Glow Labs' PixelLeak)

**Credit:** Hive Security, "PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub" (2026-10-02), reporting Glow Labs research published 2026-09-29. https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/

- Glow Labs research of 2026-09-29, reported 2026-10-02, named PixelLeak. SUPPORTED.
- Agents, "lacking a private way to attach images", put internal screenshots in public GitHub repositories. PARTLY SUPPORTED; the wording overstates the source. Glow describes agents that "could not attach an image through the path they were using and chose a public repository as a workaround." The article adds that GitHub now documents `gh ... --attach` for private attachments (depending on repository access and tool version), so the failure was the path the agent had, not a missing private option. Say "unable to attach an image the way they were working, chose a public repository as a workaround."
- One helper's default "creates a public gitshot-images repository". SUPPORTED. The tool is `gitshot`; its default authenticated path "creates a public `gitshot-images` repository" and uploads images as release assets.
- More than 13,000 images from developers at more than 300 organisations. SUPPORTED: "more than 13,000 publicly accessible internal images tied to developers at more than 300 organizations."
- 93% under employees' personal usernames. SUPPORTED: "93% of the cases it found involved repositories under employees' personal usernames". The article calls this "Glow's observation, not a universal rate."
- "the researcher's count, not independently audited". SUPPORTED: the figures "are the researcher's findings, not an independently audited count."
- Controls at the token and organisation level, not only in instruction files (sources entry). SUPPORTED. The article says to give agents only the repository and token permissions the task needs, and to block or require approval for public repository creation, personal-account publishing, gists, releases and unapproved image hosts "at the token, organization, endpoint, or network boundary, not only in instruction files". It also says organisation settings do not govern personal accounts.
