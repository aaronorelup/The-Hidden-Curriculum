# Proposed additions (not for this lesson)

Found by research-now on 2026-10-23 while checking save-points-and-the-agents-trail. For the curriculum to consider later. None of this goes into 01.03.

## 1. Boundaries you say out loud vs rules that hold
- **Topic:** In Claude Code's auto mode, a boundary stated in chat ("don't push", "wait until I review before deploying") is a classifier block signal. It is re-read from the transcript on each check and "can be lost if context compaction removes the message that stated it". For a hard guarantee the docs say to use a deny rule.
- **Why it matters:** it sits between "prose is not a control" and "prose is a rule". Beginners will over-trust it or dismiss it.
- **Owner candidate:** rules-it-reads-rules-it-cant-break.
- **Sources:** https://code.claude.com/docs/en/permission-modes#boundaries-you-state-in-conversation (read 2026-10-23); changelog v2.1.90 (2026-04-01) "Fixed auto mode not respecting explicit user boundaries".

## 2. The sanctioned path vs the agent's workaround (PixelLeak follow-up)
- **Topic:** GitHub CLI v2.99.0 added `--attach` for images and video on PRs, issues and comments (needs push access; rejects the Actions GITHUB_TOKEN). PixelLeak happened because agents found a public-repository workaround when no private path existed. The lesson: give agents an approved path, or they invent one.
- **Why it matters:** this is a general pattern (a missing capability leads the agent to a creative, public workaround), not just a screenshot fact.
- **Owner candidate:** the-narrowest-keys-and-verbs.
- **Sources:** https://github.blog/changelog/2026-09-01-github-cli-media-in-issues-pull-requests-and-comments/ (2026-09-01); https://github.com/cli/cli/releases/tag/v2.99.0; https://workos.com/blog/pixelleak-ai-coding-agents-screenshots (2026-10); https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/ (2026-10-02).

## 3. Tests that touch the real world, and a "fix" that makes it worse
- **Topic:** Karakun (2026-08-28): a "unit test" imported a script whose `main()` cloned two repositories and pushed broken YAML to `main`. The agent's revert from a shallow clone staged every file for deletion and pushed that too. It was saved only because the deploy build failed ("Pure luck"). The written CLAUDE.md/AGENTS.md rules were the weakest guard (pushed to `main` in 2 of 7 simulated-pressure runs).
- **Why it matters:** "tests pass" can itself be the destructive action, and the agent's recovery attempt is a second risk.
- **Owner candidates:** done-is-a-claim; before-you-let-it-loose; checking-what-you-cant-read.
- **Source:** https://dev.karakun.com/2026/08/28/coding-agent-pushed-deletion-to-main.html (2026-08-28).

## 4. Cloud sessions now upload repositories that have no remote
- **Topic:** `claude --cloud` bundles and uploads a local repository with no git remote, or one where the Claude GitHub App isn't installed. The bundle includes history and uncommitted tracked changes but not untracked files. On native Windows, uncommitted changes to `.env`-style files upload as they are; macOS/Linux/WSL leave them out. A never-pushed branch makes the session start somewhere else (`Branch <name> is not on GitHub`).
- **Why it matters:** this changes what "a cloud session uploads" (Windows users especially). The pointer in where-your-agent-works may need refreshing.
- **Owner candidate:** where-your-agent-works (refresh); keys-public-secret-and-leaked (the Windows `.env` detail).
- **Source:** https://code.claude.com/docs/en/claude-code-on-the-web (read 2026-10-23).

## 5. Platform-level git guardrails moving to rulesets
- **Topic:** GitHub's bulk migration of a repository's branch protections to rulesets (2026-10-20). Secondary indexes also mention a "Committer must match pusher" rule and push-rule path exceptions; those are not confirmed on GitHub's changelog in this run.
- **Why it matters:** the lesson that enforces "the agent may never push to main" will point beginners to a settings screen that is changing now.
- **Owner candidate:** rules-it-reads-rules-it-cant-break.
- **Sources:** https://github.blog/changelog/2026-10-20-bulk-migrate-branch-protections-to-rulesets-for-a-repository/ (2026-10-20); unconfirmed: https://releases.sh/github (October 2026).

## 6. Worktrees can lose unpushed commits on exit
- **Topic:** Claude Code fixes in October 2026: `claude --worktree` removed the worktree and its branch without asking when HEAD was detached, which "could lose commits" (v2.1.304, 2026-10-19); quitting removed a hook-made worktree that "may hold unpushed commits" (v2.1.301, 2026-10-15). The Desktop docs also warn that archiving a session can lose uncommitted worktree changes.
- **Why it matters:** parallel agents give each one its own copy, and those copies are disposable unless pushed.
- **Owner candidate:** agents-that-run-while-youre-away.
- **Sources:** https://code.claude.com/docs/en/changelog (v2.1.301, v2.1.304); https://code.claude.com/docs/en/desktop (read 2026-10-23).
