---
key: rules-it-reads-rules-it-cant-break
id: 05.02
title: CLAUDE.md, AGENTS.md and rules that actually hold
district: Directing Well
module: 05 What the agent sees
status: todo
legacy: []
minutes: 12
concepts: [C044, C045, C046, C047, C048]
sources: [S123, S021, S023, S026, S022, S001, S002, S003, S004, S008, S015, S024, S036, S052, S065, S124, S125, S126, S127, S128, S129, S130]
lead: [S123, S021]
---
# CLAUDE.md, AGENTS.md and rules that actually hold

**Purpose (the first spoken sentence):** In this lesson you'll learn the difference between a rule your agent reads and a rule it cannot break: what an instruction file such as CLAUDE.md or AGENTS.md is for, why anything written in it is only a request, what actually makes an action impossible, and why a rule only works in the sessions that load it.

**Conclusion:** An instruction file is a short map the agent reads and may skip, so every "must never" needs a deny rule, a blocking hook, a sandbox, CI or a credential the agent never gets behind it, tested until you have seen it fire, and the file itself has to stay short, current and committed where every session can see it.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Rules it reads, rules it can't break." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; module 05 What the agent sees. Builds on 05.01 `what-the-agent-sees-each-turn` (the file rides in every request), 01.01 `the-folder-is-the-agents-world` (rules climb up from the folder you open; C046 requires C123) and 01.02 `where-your-agent-works` (the terminal; C045 requires C122).

**Lead source (audit, 2026-10-12):** S123 (Anthropic); S021 (François Zaninotto (Marmelab)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S123, S021, S023, S026, S022); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

*Length:* 12 minutes, five concepts. C044 and C045 are the spine (C045 is the security rule of the course applied to configuration). C046 is taught through Aaron's own incident. C047 is taught inside C045 as the habit that feeds it, as its concept entry recommends. C048 is a short closing segment.

## What to teach (binding scope)

### C044 Instruction files are short maps of what the code can't say
- **It is text injected next to a system prompt you can't change.** "CLAUDE.md content is delivered as a user message after the system prompt, not as part of the system prompt itself. Claude reads it and tries to follow it, but there's no guarantee of strict compliance, especially for vague or conflicting instructions" (S123). The Stanford intercept shows it above the first message as text the lecturer never typed (S002 lines 277-282; shown in 05.01, referenced here). — **brief**
- **CLAUDE.md and AGENTS.md do the same job; AGENTS.md is the cross-tool name** (S002). Claude Code reads AGENTS.md directly from v2.1.277, but by default only when there is no CLAUDE.md or CLAUDE.local.md in the working directory or above it, so adding a personal CLAUDE.local.md silently stops it reading AGENTS.md; the fix is to import AGENTS.md from a CLAUDE.md or set **Project instructions** to `claude-md-and-agents-md` (S123). — **brief** (one card: "which file wins")
- **What belongs in it:** the exact commands (test, build, start the server) and where things live (S002); "what the code can't say, and nothing else": domain and business rules, trade-offs behind the structure, external constraints, history behind odd-looking code (S036). Claude Code's `/doctor` trim check follows the same line: it cuts what Claude can derive from the code (directory layouts, dependency lists, architecture overviews) and keeps pitfalls, rationale and conventions that differ from tool defaults (S123). — **teach**
- **Write rules concrete enough to check.** "Run `npm test` before committing" instead of "Test your changes"; if two instructions contradict each other, "Claude may pick one arbitrarily" (S123). — **brief**
- **Keep it short, as an index.** Anthropic: target under 200 lines per file, with a startup warning when one is over; `@path` imports organise a file but don't reduce its cost, because imported files load at launch too (S123). OpenAI replaced one big file with about 100 lines acting as a table of contents for the rule tree (S021). A long file fails four ways (OpenAI, quoted in S021): it crowds out the task; "when everything is 'important,' nothing is"; it "rots instantly… a graveyard of stale rules"; and "a single blob doesn't lend itself to mechanical checks". Make the root file a router and move part-of-the-codebase rules into path-scoped rules that load only when matching files are touched (S022, S123). — **teach**
- **Measured (S021, September 2026):** the median root instruction file is 123 lines and 57% are over 100. ETH Zurich's study: machine-generated context files lowered success compared with no file at all and added over 20% inference cost; human-written ones gained about 4%; either way the agent spent 14-22% more reasoning tokens. In 52 of 79 repositories the harness is more AI-written than the code it governs. So: let the agent draft the file, then review it like code and give it an owner (S021; S124). — **teach**
- Layering: Claude Code concatenates every level it finds and "uses judgment" when they conflict (S015, S123). — **one line**

### C045 Rules in prose are requests; hooks, permissions and sandboxes enforce
- **Everything written for the model is a request.** Claude Code treats CLAUDE.md "as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead" (S123). "An instruction like 'never edit `.env`' in CLAUDE.md or a skill is a request, not a guarantee. A `PreToolUse` hook that blocks the edit is enforcement" (S015). Cursor's staff, in the incident below: "rules are guidance the model can still deviate from, so the real gate is the hard controls below, not the rule text" (S023). Kiro's docs say steering is preferred, not enforced (S024). — **teach**
- **The incident (S023, Cursor forum, posted 2026-09-02).** One user had rules in three places, including `alwaysApply: true` gates and a GitLab-only user rule. Across chats from 27 August to 1 September 2026 the agent still made hosting-API calls, SSH sessions, deploys and database changes without agreement, ran a mail migration before the DNS change, opened an empty merge request, and printed a GitLab token into the tool log (the user rotated it). The post lists "'From now on' promises with no behavior change." — **teach** (the lesson's case)
- **How rare real enforcement is (S021):** across 481 public CLAUDE.md files only 4.4% of security rules are backed by a real control (citing S126, which calls CLAUDE.md "a write-only channel"); 63% of 145 large open-source projects ship an instruction file, but there are only 14 hooks across all 145; only 12 of 391 repositories commit a single deny rule and 22 declare a PreToolUse hook. — **brief**
- **What actually makes an action impossible**, one sentence each, each owned elsewhere for depth:
  - a permission **deny rule**: "Settings rules are enforced by the client regardless of what Claude decides to do" (S123);
  - a **PreToolUse hook that blocks** (exit code 2, or `permissionDecision: "deny"`): it "blocks the tool even in `bypassPermissions` mode", and a hook's "allow" can't loosen a deny rule from settings (S127);
  - the **sandbox**, which is off by default, covers shell commands only (file tools, MCP servers and hooks run outside it) and doesn't exist on native Windows (S052's sandbox page) → 07.02;
  - **CI and branch protection**, which run somewhere the agent can't edit (S021) → 06.02;
  - a **credential the agent never holds**: "A deny rule, scoped credential, or CI check doesn't have to remember" (S036) → 07.03.
  — **teach**
- **Hooks fail open unless you build them to fail closed.** In Claude Code a hook that exits with anything other than 2 and prints plain text or nothing lets the action proceed as a "non-blocking error" (S127). New on 2026-10-08 (v2.1.295): `onFailure: "block"` makes a command or HTTP hook that "can't start, times out, or exits with an unexpected code" block the action instead (S125). Cursor's equivalent `failClosed: true` hook is, in its staff's words, "the real hard block and runs regardless" (S023). Hook behaviour keeps being fixed (v2.1.294 fixed prompt and agent hooks "written as instructions" that allowed what they should block, S125), so re-test guards after updates. — **teach**
- **A hook sees only what it matches.** An `Edit|Write` matcher "fires only when Claude uses the `Edit` or `Write` tool, not when it uses `Bash`"; the `if` filter is best-effort, so "use the permission system rather than a hook to enforce a hard allow or deny" (S127). A hook that only injects a reminder is still guidance (S024). — **brief**
- **Test every guard both ways.** codex-claude-code-config files 63 cases against 12 guards: 29 that must be blocked, 19 that must be allowed, 15 that check a router's exact text; `rm -rf /tmp/scratch-dir` is allowed, `rm -rf /` is blocked, and the regex guard also refuses `rm -rf /; echo done` (S021). Aaron's build guard was tested with a fake branch build, which failed, and a fake `main` build, which passed (S026). Say it plainly: a guard you have never seen fire may be decoration. — **teach**
- **Holes to know about** (S023, S021, S127): approving a full-network request "drops your deny list for that command"; the agent moved its own workspace root, which "dropped your root rules/hooks"; and people approve what they are asked: in a study of 113 people supervising the same simulated day, those who wrote rules up front blocked 20.1 points fewer bad actions, because they set most rules to "ask me" and then approved the prompts ("93% of permission prompts get approved"): "A rule that ends in a prompt isn't a rule" (S021). New and worth one line: a mod that handles `tool.check` can approve a call your PreToolUse hook blocked, unless the hook is in managed settings (S127). — **brief**
- **The tool's own built-in instructions can beat yours.** Cursor kept suggesting `gh` despite the GitLab-only rule: "another 'no gh' rule won't reliably win" (S023). Claude Code's docs say to check whether your instruction competes with guidance it adds itself and to turn that off, for example `includeGitInstructions` (S123). The fix is a control (deny the command), not more prose. — **brief**

### C046 Which rules a session actually loads
- **What Claude Code loads, and when** (S123): at launch, CLAUDE.md and CLAUDE.local.md from the working directory and every directory above it (a one-line recap: 01.01 teaches that rules climb upward); a subfolder's CLAUDE.md only once Claude reads, writes or edits a file in that subfolder; a path-scoped rule only when a matching file is touched. Cursor behaves the same: nested rules "only load when a chat is touching `infra/` (even with `alwaysApply: true`), and pointer files only pass the path, not the rule itself" (S023). Fixed as recently as 2026-10-07 (v2.1.293): path-scoped rules and nested CLAUDE.md files did not load when Claude viewed a file with `cat`, `head` and similar instead of the Read tool (S125). — **teach**
- **An edit mid-session doesn't apply.** Root and user CLAUDE.md "are read once at session start… the edit also doesn't apply… The new content loads on the next `/clear`, `/compact`, or restart" (S128). — **teach**
- After compaction the root file is re-read from disk; nested files and path-scoped rules reload only when a matching file is touched again; chat-only instructions survive only inside the summary (S123; 05.01). Auto mode re-reads boundaries you stated in chat from the transcript, "so a boundary can be lost if context compaction removes the message that stated it. For a hard guarantee, add a deny rule instead" (S052). — **brief**
- **Where the session runs decides what it can see.** A session started on claude.ai "starts with a fresh clone of the repository, on the default branch, and nothing else" (S026). `claude --cloud` clones the GitHub remote at your current branch, "not your local checkout, so push first", and untracked files never travel (S129). Personal skills in `~/.claude/skills` don't load in Cowork or cloud sessions (S130). — **teach**
- **Aaron's case, as a one-line callback (S026).** His blog's rules lived in a CLAUDE.md one folder above the repo on his laptop, uncommitted, so the cloud session that pushed from a stale branch and took his site back to August never saw them: "The session did nothing wrong by what it could see." The incident itself is told in full only in from-your-laptop-to-a-url (audit, 2026-10-12). — **brief**
- Subagents load CLAUDE.md, except the built-in Explore and Plan agents and any agent that sets `omitClaudeMd` (S015; briefs are 05.01's subject). — **one line**
- **Check what loaded:** `/context` lists the memory files loaded at launch; a nested file prints a `Loaded` line when it loads; `/memory` lists locations; an `InstructionsLoaded` hook can log every load and why (S123). — **brief**
- **The durable fix:** commit a short CLAUDE.md inside the repo so every surface sees it, and put the must-nevers in repo-side or hosting-side controls (S026). — **teach**

### C047 Turn repeated corrections into durable checks (taught inside C045)
- A correction made in chat lasts this conversation at most; "Each Claude Code session begins with a fresh context window", and only files carry knowledge across sessions (S123). "If you quietly repair the diff, the next session can repeat it" (S036). — **brief**
- **The ladder:** a convention or command wrong twice goes into CLAUDE.md; a playbook pasted a third time becomes a skill (S015); anything a machine can check moves into "a lint rule, hook, type, test, or skill. Keep prose for constraints that cannot be enforced mechanically" (S036). OpenAI writes lint error messages that carry the fix, so the agent corrects itself next run (S021). — **teach**
- **Build rules from failures you have seen**, not someone else's CLAUDE.md copied wholesale (S021). Record why each exists and when it can go: "give every control an expiry condition, and write down the incident it exists for. One line per hook naming the failure behind it is the cheap version." Atomic CRM ships 148 harness files and zero recorded decisions, "so nothing says why any control exists, and none of them can be safely removed" (S021). — **brief**
- **Know where "remember this" goes.** Asked to remember something, Claude Code saves it to auto memory on that machine; for a project rule, say "add this to CLAUDE.md" (S123). A note on your laptop reaches neither your teammates nor a cloud session (S123, S129). — **brief**
- The payoff: "Over time the harness becomes a record of failures the team has decided not to pay for twice" (S036). — **one line**

### C048 Stale instructions and docs are worse than none
- An agent believes what is written. Stanford's lecturer: "Given a choice between ingesting bad docs and starting from scratch, I'd start from scratch… make sure those outdated docs either don't exist or are brought up to date" (S003 line 145). — **brief**
- **A model upgrade changes which instructions help** (S022, OpenAI, no earlier than 2026-09-03): "Guidance that helps Sol or Luna may overconstrain GPT-6 Astra"; "run the tests" instructions "can lead to unnecessary testing" because the new model already tests its work; replace "Before every edit, read architecture.md, database.md, and deployment.md" with "Use architecture.md for service boundaries, database.md for schema changes, and deployment.md when preparing a deployment"; reconsider strong ask-first wording. Anthropic's own harness had the same problem: "The context resets we built to compensate had become dead weight in the agent harness" (S021). — **teach**
- **Audit on every model change.** `/doctor prompt-audit` (Claude Code v2.1.283, 2026-09-25) looks for "instructions written for older models, references to files or commands that don't exist, and files that contradict each other", and changes nothing until you ask (S123, S125). OpenAI suggests asking the new model to audit your instructions (S022). — **brief**
- "Repository skills also guide other contributors' agents, which may use different models" (S022). — **one line**
- **Don't prune the safety.** Dropping prose "ask first" rules is fine only once the real must-nevers are enforced by controls (C045); this tension comes from reading S021 and S022 together. — **teach** (end the segment here)
- Dropped here: "what you know goes stale in weeks" in general (00.01, C052); half-finished migrations as contradictory precedent (10.02, C053-C054).

## You vs the agent
As of 2026-10-12:
- **The agent does on its own (when asked):** drafts the instruction file and splits a long one into an index plus topic files; runs `/doctor` trims and `/doctor prompt-audit`; writes deny rules, hooks, lint rules and CI checks and the tests for them; lists which instruction files and hooks it loaded; finds a default-branch mismatch; audits a file for rules that have no control behind them (S123, S021, S015, S026).
- **What the agent cannot verify:** that a line it drafted is true and specific to this project (S021, S036); that its own guard is complete; rules it never received ("The session did nothing wrong by what it could see", S026). Its promise that it won't happen again changes nothing (S023: "'From now on' promises with no behavior change").
- **You decide and check:** the must-never list (production deploys, SSH, production databases, payments, deleting data, sending messages, secrets); that each one has a control behind it and that you have watched it block and watched it allow (S021, S026); where each session runs and which laptop-only rules must be committed to travel; `/clear` after editing standing rules (S128); the default branch on the hosting site (S026); declining full-network and move-the-root prompts during risky work (S023); which docs are still true, and what gets cut after a model change (S022).
- **Bring in someone who can:** when a guard protects production, payments or credentials, have someone who knows that platform's permission, network and identity controls review it (S021, S065; how to bring them in: 04.04). For domain or compliance rules, the person who owns the rule writes or approves the line (C044).

## Sources this lesson is built from
- S123 — Anthropic, "How Claude remembers your project: CLAUDE.md, AGENTS.md, rules, auto memory" (Claude Code docs; undated, mentions versions up to v2.1.285 of 2026-09-29; re-read 2026-10-12) https://code.claude.com/docs/en/memory — delivered as a user message with no guarantee of compliance; context, not enforced configuration; what loads when; AGENTS.md rules; size, imports, concrete rules; `/doctor` trims and the prompt audit; where "remember this" goes; `InstructionsLoaded`.
- S021 — François Zaninotto (Marmelab), "The State Of AI Harness Engineering 2026" (2026-09-24) https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html — the measurements (4.4%, 14 hooks, 12 deny rules, 123 lines, ETH Zurich, 52 of 79); OpenAI's 100-line index and four failure modes; two-sided guard tests; "A rule that ends in a prompt isn't a rule"; expiry conditions and incident records; dead-weight resets (re-read 2026-10-12).
- S023 — Brunno Oliveira Prego, replies by Mohit (Cursor staff), "Agent repeatedly ignores workspace User Rules and repo gates across multiple chats" (2026-09-02) https://forum.cursor.com/t/170277 — the incident; "rules are guidance the model can still deviate from"; fail-closed hooks as the hard block; nested rules not loading; the root move; the full-network hole; built-in guidance beating a user rule (re-read 2026-10-12).
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09; incident 2026-10-08) https://aaronorelup.com/ledger/the-branch-that-went-live/ — rules that never reached a cloud session; the stale default branch; four separate safeguards; a guard tested both ways (re-read 2026-10-12).
- S022 — OpenAI, "Rethinking skills and prompts for GPT-6 Astra" (OpenAI developers blog; undated, no earlier than the GPT-6 Astra release on 2026-09-03) https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra — pruning instructions written for weaker models; routing instead of mandatory reading; other contributors' agents (re-read 2026-10-12).

Also cited for specific points (credit on the lesson page):
- S015 — Anthropic, "Extend Claude Code" (features overview; undated live docs; re-read 2026-10-12) https://code.claude.com/docs/en/features-overview — "a request, not a guarantee"; the trigger ladder; layering.
- S127 — Anthropic, "Automate actions with hooks" (Claude Code hooks guide; undated live docs; re-read 2026-10-12) https://code.claude.com/docs/en/hooks-guide — exit 2 and deny; blocks even in bypass mode; non-blocking errors; matchers; testing a hook from the terminal; the mod caveat.
- S125 — Anthropic, "Claude Code changelog" (entries read through v2.1.296, 2026-10-09) https://code.claude.com/docs/en/changelog — `onFailure: "block"` (v2.1.295, 2026-10-08); prompt-hook fix (v2.1.294); rule-loading fix (v2.1.293); `/doctor prompt-audit` (v2.1.283).
- S128 — Anthropic, "How Claude Code uses prompt caching" (undated; mentions up to v2.1.283) https://code.claude.com/docs/en/prompt-caching — CLAUDE.md edits wait for `/clear`, `/compact` or a restart.
- S129 — Anthropic, "Use Claude Code in the cloud" (undated live docs, mentions v2.1.289) https://code.claude.com/docs/en/claude-code-on-the-web — "push first"; untracked files never travel.
- S130 — Anthropic, "Skills" (Claude Code docs; undated, mentions v2.1.295; re-read 2026-10-12) https://code.claude.com/docs/en/skills — personal skills don't load in cloud or Cowork sessions.
- S052 — Anthropic, "Choose a permission mode" with its sandbox page (Claude Code docs; undated, v2.1.283+; re-read 2026-10-12) https://code.claude.com/docs/en/permission-modes and https://code.claude.com/docs/en/sandboxing — boundaries in chat can be lost at compaction; the sandbox is off by default, shell-only, not on native Windows.
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — what the code can't say; "doesn't have to remember"; the ladder; the harness as a record of failures.
- S002 — Mihail Eric, Stanford CS146S lecture transcript (2026-09-24) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — CLAUDE.md as injected text; AGENTS.md as the shared name.
- S003 — Mihail Eric, Stanford CS146S lecture transcript (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — bad docs versus none.
- S024 — Kiro (AWS), "Kiro specs" docs (2026-10-02) https://kiro.dev/docs/specs/ — steering is preferred, not enforced. One line.
- S124 — Michael Segner (Anthropic), "Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents" (2026-06-18) https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more — give the file an owner and review changes like code (per concepts.md; not re-opened 2026-10-12).
- S126 — Ting Yan, "When 'Do Not' Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls" (arXiv, 2026-08-24; abstract) https://arxiv.org/abs/2608.23550 — the 4.4% figure, via S021.
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — "Prompt-level instructions alone do not establish a secure boundary."

**Correction found while re-checking (2026-10-12):** concepts.md (C045) cites "133 of 148 overreach actions … ran after a human approved them (S021, citing arXiv 2608.27443)". That figure is not in S021's text; S021 reports the study as 113 participants, with rule writers blocking 20.1 points fewer bad actions after approving their own "ask me" prompts. Teach S021's version, as above, and fix C045 in concepts.md.

## Show it for real
- Two panes in a demo repo whose "remote" is a local throwaway bare repository: left, CLAUDE.md says "never run git push", ask the agent to push, and it can; right, add a deny rule for `git push` in `.claude/settings.json`, ask again, and show the block. Proves prose is a request and a rule is a wall (S015, S123).
- The hooks guide's `protect-files.sh` on a dummy `.env` with fake values: ask Claude to edit it and show "Blocked: .env matches protected pattern" coming back as feedback (S127).
- The same hook tested from the terminal both ways: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | ./my-hook.sh; echo $?` prints 0, a must-block input prints 2. Two-sided tests, as S021 describes (S127, S021).
- Break the hook on purpose (rename its script): without `onFailure` the transcript shows a hook error "Failed with non-blocking status code" and the edit goes through; with `onFailure: "block"` it is blocked. New in v2.1.295 (2026-10-08): run `claude --version` on camera and re-check the behaviour on the recording machine first (S127, S125).
- `/hooks` listing what is active, and `/context` listing the memory files that loaded (S127, S123).
- Mid-session edit: add a visible rule to CLAUDE.md, ask about it (the agent doesn't know it), run `/clear`, ask again (S128).
- `/doctor prompt-audit` on a deliberately bloated CLAUDE.md, walking through two proposed edits (S123).
- A staged version of Aaron's case in a demo GitHub repo: a CLAUDE.md that sits one folder above the repo in the file explorer, a cloud session asked to print its project instructions without it, then the file committed inside the repo and the session repeated; then GitHub's Settings > Branches showing the default branch (S026, S129).
- Credited screenshots: the Cursor staff reply in S023 and S021's enforcement figures.

## Questions this lesson answers
- "I told it in CLAUDE.md never to push to main. Why did it?" and "Is it enough to tell the AI not to do something?" (gap items citing S015, S021, S023, S065)
- "What's the difference between a rule and a permission?", "What is a hook?" and "How do I stop the agent from ever touching .env?" (gap items citing S015, S021)
- "How do I actually stop the agent from deploying or touching production?" (S023)
- "What should I put in CLAUDE.md?", "How long should it be?" and "What's the difference between CLAUDE.md and AGENTS.md?" (gap items citing S001-S004, S008, S021, S036)
- "Should I let the AI write my AGENTS.md?" and "Should I use someone else's CLAUDE.md?" (S021)
- "Why does the agent ignore my rules in some chats but not others?", "Why did the cloud agent not follow my rules when my laptop agent does?" and "I updated CLAUDE.md, why is it still doing the old thing?" (gap items citing S015, S023, S026)
- "Why does the agent keep making the same mistake?" (S021, S036)
- "Should I change my CLAUDE.md or AGENTS.md when a new model comes out?", "Should I give the AI our old docs?" and "Which instructions can I delete?" (gap items citing S001, S003, S022)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Permission modes and why people approve nearly every prompt → `before-you-let-it-loose` (02.01, C077, C081)
- What the sandbox and containers actually cover → `contain-it-dont-babysit-it` (07.02, C078, C079)
- Keeping credentials out of the agent's reach; narrow verbs → `the-narrowest-keys-and-verbs` (07.03, C082, C083)
- CI as evidence the agent can't write → `checking-what-you-cant-read` (06.02, C012)
- Rules and memory files as an injection target → `whose-words-is-it-reading` (07.01, C075)
- Hooks and plugins as code that an update can swap → `skills-mcp-hooks-and-plugins` (05.03, C092)
- Skills, and how they load by description → `skills-mcp-hooks-and-plugins` (05.03, C049, C050)
- Which branch is live, and the remote copy → `save-points-and-the-agents-trail` (01.03, C124)
- A host turning a branch push into a deploy; local, preview and production → `from-your-laptop-to-a-url` (03.03, C099)
- Cloud, scheduled and background sessions and what each loads → `agents-that-run-while-youre-away` (08.01, C094)
- How fast tools and knowledge go stale in general → `the-hidden-curriculum` (00.01, C052)
- House rules and an owner for dependencies in files the agent reads → `after-launch-keep-it-alive` (10.02, C053)
- Bringing in an expert → `before-you-ship-who-signs-off` (04.04, C118)

## Out-of-date framings to avoid
- "Put it in CLAUDE.md and the agent will follow it" (S021, S023, S123).
- "Write NEVER in capitals and it becomes a hard rule" (S021 item) and "A stronger-worded rule will override the tool's default" (S023).
- "`alwaysApply: true` means always" (S023).
- "The agent promised it won't happen again" (S023).
- "A hook that injects a reminder prompt is a block" (S024).
- "Tell the agent in the system prompt what it may not do" (S065).
- "The longer and more detailed the instructions, the better" (S002, S021) and "Let the agent generate your CLAUDE.md and leave it" (S021).
- "Each tool needs its own config file" (S002, S123).
- "My CLAUDE.md protects every session", "The agent rereads CLAUDE.md every turn" and "The branch I work on locally is the one every agent gets" (S026, S128).
- "Write your CLAUDE.md once and it keeps working", "Any documentation is better than none" and "Tell the agent to always run the tests" (S021, S022, S003).
- "Just tell the agent again" and "Copy a popular CLAUDE.md template" (S036, S021).

## Legacy notes
No legacy lesson covers this slot (`legacy: []`). Legacy 00.05 touches it in one section ("Notes pinned to the desk": "a note is not a lock. Hooks and permissions enforce") and one myth ("Claude dot M D is a rule it must obey… Hooks and permissions are the locks"). Both lines are right and can be echoed, but 00.05 does not cover what belongs in the file, which sessions load it, cloud sessions, fail-open hooks, two-sided guard tests or stale instructions, so it is not a cover. When 00.05 is rebuilt, its instruction-file segment moves here.
