# Single-point source check: S052, S069, S101, S129, S142, S176

Lesson: save-points-and-the-agents-trail (01.03). Checked 2026-10-23 against the live pages. Only the points the spec takes from each source were checked.

## S052: Anthropic (Claude Code docs), "Choose a permission mode"

Credit: Anthropic, Claude Code docs, "Choose a permission mode" (undated live docs, read 2026-10-23), https://code.claude.com/docs/en/permission-modes

- **Auto mode is the starting mode for terminal and VS Code from v2.1.283.** SUPPORTED: "With Claude Code v2.1.283 or later, auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions." (On earlier versions only on Pro, Max and Team plans. `claude -p` / Agent SDK start in `default`, and so does any session where `disableAutoMode` is set.)
- **Push to any branch, default included, is allowed by default.** SUPPORTED: "Pushing to any branch of the repository you're working in, including the default branch." Caveat to keep: "A non-default branch whose name marks it as a deploy or publication target, such as `production` or `gh-pages`, isn't covered." Also, `permissions.deny` rules can still block push commands in every mode.
- **"Before v2.1.203 a direct push to the default branch was blocked, so older advice is wrong."** NOT SUPPORTED. The page says nothing about default-branch pushes before v2.1.203. What it does say: "From v2.1.203 until v2.1.211, only routine default-branch pushes and pushes to the branch you started on or to branches Claude created were allowed by default." So even in that window, routine default-branch pushes were allowed; the narrower rule covered other branches. The spec's "Common mistakes" line ("direct pushes to the default branch were blocked only before v2.1.203") repeats the same error.
- **The remote's own branch protection still applies.** SUPPORTED: "The remote's own branch protection still applies."
- **Blocks "Merging a pull request no human has approved, approving Claude's own pull request, or disabling CI checks".** SUPPORTED, verbatim.
- **Blocks force push, `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`, and amending an already-pushed commit.** SUPPORTED: "Force push"; "`git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`, `git stash drop`, or `git stash clear`, which the classifier presumes would discard uncommitted changes"; "From v2.1.198, `git commit --amend` when the commit at HEAD has already been pushed" (a message-only reword of a commit Claude made this session is not blocked). The page also blocks `--amend` when HEAD was not created in this session.
- **Runs `git status` itself before any command that would discard uncommitted work.** SUPPORTED: "Claude Code also runs `git status` itself before a command that would discard uncommitted work, such as `git reset --hard` or `rm -rf`, and shows the classifier whether staged, modified, or untracked work is present."
- **Blocks "Changing where pushes go with `git remote set-url` or `git remote add`, unless you named the new remote".** SUPPORTED, verbatim.
- **Blocks pushing secrets or personal data to a known-public repository.** SUPPORTED: "Pushing secrets or personal or entrusted data to a repository known to be public..." Caveat: "When a repository's visibility isn't established, the classifier doesn't block on that alone."
- **Blocks sensitive files entering a commit or push; "the repository being private doesn't clear it".** SUPPORTED, but the rule is wider than the spec says: "Content from a sensitive local store, or from a file whose name, path, or type marks it as sensitive, entering a commit, a push, PR or issue text, a gist or paste, or a package publish, unless you named both the source and the destination. Session transcripts and conversation logs, credential and configuration dot-folders ... and user-data exports all count, and the repository being private doesn't clear it."
- **Spec metadata "mentions v2.1.292".** SUPPORTED, but v2.1.292 appears only in the filesystem / critical-path section, not in anything about git.

## S069: Anthropic (Claude Help Center), "Use Claude Cowork safely"

Credit: Anthropic, Claude Help Center, "Use Claude Cowork safely", https://support.claude.com/en/articles/13364135-use-claude-cowork-safely

- **"Is Claude accessing files or websites you didn't mention?"** SUPPORTED, verbatim. It sits under "Protect yourself from malicious attackers", item 2 "Monitor tasks, not just commands": "watch for unexpected patterns: Is Claude accessing files or websites you didn't mention?"
- **"Last modified 2026-10-06."** NOT CONFIRMED. On 2026-10-23 the page shows only "Updated today", so it has changed since 2026-10-06. The quote is unchanged. The date in the credit should be updated to 2026-10-23 (as seen).

## S101: Anthropic (Claude Code docs), "How Claude Code works"

Credit: Anthropic, Claude Code docs, "How Claude Code works" (undated live docs, read 2026-10-23), https://code.claude.com/docs/en/how-claude-code-works

- **"Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed."** SUPPORTED, verbatim. The next sentence: "You control those with your permission mode and permission rules."
- **"Your git state. Current branch, uncommitted changes, and recent commit history."** SUPPORTED, verbatim (under "What Claude can access").
- **"Claude sees your current branch's files."** SUPPORTED, verbatim (under "Work across branches").
- **Every message, tool use and result is kept in a plaintext transcript.** SUPPORTED: "Each message, tool use, and result is written to a plaintext JSONL file under `~/.claude/projects/`."

## S129: Anthropic (Claude Code docs), "Use Claude Code in the cloud"

Credit: Anthropic, Claude Code docs, "Use Claude Code in the cloud" (undated live docs, read 2026-10-23), https://code.claude.com/docs/en/claude-code-on-the-web

- **A cloud session "clones your current directory's GitHub remote at your current branch, not your local checkout, so push first if you have local commits".** SUPPORTED, verbatim: "The cloud VM clones your current directory's GitHub remote at your current branch, not your local checkout, so push first if you have local commits." Caveat: with no git remote, or when the Claude GitHub App isn't installed on the repository, Claude Code bundles and uploads the local repository instead. The bundle includes history and uncommitted changes to tracked files, but not untracked files. On native Windows it uploads uncommitted changes to tracked files whatever their names.
- **The diff indicator `+42 -18` compares against the base branch, with "Compare against" to pick another branch.** SUPPORTED: "Each session shows a diff indicator with lines added and removed, like `+42 -18`. Select it to open the diff view, leave inline comments on specific lines..."; "The diff view compares the session's changes against its base branch by default. To compare against any other branch in the repository, select **Compare against** and pick one."
- **Metadata "mentions up to v2.1.289".** SUPPORTED (the v2.1.274 to v2.1.289 sign-in message).
- **That Claude watches CI and fixes failures (the "You vs the agent" section cites S129).** SUPPORTED: Auto-fix "when a check fails or a reviewer leaves a comment, Claude investigates and pushes a fix if one is clear". It requires the Claude GitHub App.

## S142: piscator, reply by Pooge, "Ask HN: Client took over development by vibe coding. What to do?"

Credit: piscator, with the reply by Pooge, "Ask HN: Client took over development by vibe coding. What to do?" (Hacker News, 2026-04-01), https://news.ycombinator.com/item?id=47599303

- **"Why does the client have pushing rights to the repository?" (Pooge).** SUPPORTED, verbatim, posted by Pooge. The date shows only as "6 months ago", which is consistent with 2026-04-01.
- Note: sources.md lists the S142 author as "piscator; audit comment by HyprMusic". For this point the spec's credit (Pooge) is the right one. HyprMusic is a different commenter.

## S176: shuang_yang, replies by ActionGate and sattyamjjain, Cursor forum

Credit: shuang_yang, replies by ActionGate and sattyamjjain, "Errible: AI out of control, randomly deleting files, 6-month project wiped out" (Cursor forum, 2026-10-03 to 2026-10-05), https://forum.cursor.com/t/173688

- **The `.git` folder went with the source.** SUPPORTED: "The source code, Git, publish, and _file_backup in E:\ERP .net were gone."
- **"The first recovery step a reply gave was to check Git remotes."** NOT SUPPORTED. sattyamjjain's reply (2026-10-04) gives a six-step list. Step 1 is "Stop writing to E: right now." Step 2 is "Check git remotes. If the repo was ever pushed anywhere (GitHub, Gitee, a company server), clone it back." ActionGate's reply (2026-10-03) suggests no recovery step; it asks whether the poster would still let an AI run destructive commands.
