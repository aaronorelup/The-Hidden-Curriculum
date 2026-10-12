# Sweep: the tools people build with (October 2026)

Agent: sweep-tools. Compiled 2026-10-12 for "The Hidden Curriculum".

Angle: the official docs, onboarding and best-practice pages of the tools people build with in October 2026, read for (a) the prerequisites they quietly assume and (b) the new concepts they introduce.

Method and limits:
- Every source below was fetched and read on 2026-10-12. Nothing here comes from search snippets or memory.
- Vendor docs pages are often undated. Where a page carries no date, the block says so. Where the page's own content pins it to a release (a version number or model name), the block says how the date was inferred. Claude Code release dates come from the npm registry: v2.1.211 was published 2026-07-15, v2.1.248 on 2026-08-27, v2.1.271 on 2026-09-14 and v2.1.283 on 2026-09-25.
- The shared web-search budget ran out partway through the sweep. The later sources were found by fetching official docs indexes (llms.txt files) and pages linked from sources already read. Because of that, Bolt, Lovable and n8n are covered by their docs alone, with no outside commentary.
- Where two fetched pages cover the same tool or event, they share one block (Claude Code checkpointing, auto mode, Copilot, Gemini CLI, Kiro, Replit, Windsurf/Devin, v0, Bolt, ChatGPT Work). Each merged block lists every URL read.

---

## Cross-tool patterns (each traced to the numbered sources below)

1. **The agent runs the check; the human supplies it.** Claude Code's guide says that without a check the agent can run, you become the verification loop. It asks for evidence (test output, the command and its result, a screenshot) rather than a claim of success, and says: if you can't verify it, don't ship it (#1). Cursor (#12) and Codex (#9) say the same thing in their own words. Cursor adds a trap: check that the agent didn't change the tests to make them pass.
2. **Permission prompts are being replaced by an AI reviewing the AI.** Claude Code's auto mode (a classifier model) became the default on 2026-08-14 (#2, #3). Codex has an `auto_review` policy that sends approvals to a reviewer agent (#8). Antigravity has review policies where the agent decides when to ask (#15). Every vendor says this does not remove risk and that production or irreversible actions need a human (#2, #3, #7).
3. **Built-in security scans say outright that they are not enough.** Lovable says its scans do not replace a security review and that sensitive apps need a professional one (#17). Bolt says its fixes can change things you didn't want changed (#21). v0 leaves app-level auth and database access to you (#20). Copilot's validation tools can be switched off (#11). Cursor sells Security Review as a paid Teams feature (#13). Anthropic does not security-audit MCP servers (#5).
4. **Undo has edges that beginners don't see.** Claude Code checkpoints don't track Bash changes or most subagent edits, and they are not a replacement for git (#1). Replit rollbacks leave the database alone by default and never touch the production database (#18). Devin Desktop says reverts are irreversible (#19).
5. **Usage is metered in units beginners don't understand.** Examples: Claude Code resends the whole conversation on every request, and its prompt cache lasts 1 hour on a subscription but 5 minutes on usage credits (#6). Zapier bills per activity: one trigger that returns many records multiplies the cost, and loops can run without end (#23). Bolt names the habits that waste tokens (#21). Devin Desktop caps each prompt at 40 tool calls and charges a credit to continue (#19). ChatGPT Work and Codex share one pool of credits (#10).
6. **Instruction files are advice; hooks are enforcement.** Most tools now have a standing instruction file: AGENTS.md, CLAUDE.md, GEMINI.md, `.cursor/rules`, Kiro steering. Claude Code's docs say a rule in CLAUDE.md is a request, and a hook that blocks the action is enforcement (#4, #24).
7. **Products are renamed, merged or shut down within weeks.** Copilot coding agent became Copilot cloud agent (April 2026, #11). Windsurf became Devin Desktop (2026-06-02) and its Cascade agent reached end of life (#19). Gemini CLI stopped serving consumer accounts on 2026-06-18 (#14). Codex moved into the ChatGPT desktop app (2026-07-09), its docs moved to learn.chatgpt.com, and "Codex Cloud" is now labelled Legacy (#8, #10). A tutorial from a year ago can be wrong about which product to install at all.
8. **Development and production are separate worlds.** Each has its own keys, databases and environment variables (#18, #20). A `NEXT_PUBLIC_` variable is sent to the browser (#20). An API key that works in the preview may not exist in production (#20).

---

## Sources

### 1. Best practices for Claude Code (with the Checkpointing page)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** The page itself is undated. It documents Claude Code v2.1.283 (published 2026-09-25), so this version dates from late September 2026 or later. Recorded as 2026-09.
- **URL:** https://code.claude.com/docs/en/best-practices (also read: https://code.claude.com/docs/en/checkpointing)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - The context window is the scarce resource. Performance drops as it fills, and the agent starts forgetting earlier instructions. Clear it with `/clear` between unrelated tasks, and understand how auto-compaction and `/compact <instructions>` work.
  - Give the agent a check it can run: a test suite, a build exit code, a linter, a script that diffs output against a fixture, or a screenshot compared with a design. Without one, you are the verification loop.
  - There are four ways to make the agent keep working until the check passes. From weakest to strongest: say so in the prompt; set a `/goal` condition; add a Stop hook that blocks the turn from ending; or have a verification subagent or dynamic workflow try to refute the result.
  - Ask for evidence rather than a claim of success: test output, the command and what it returned, a screenshot.
  - The workflow is explore, plan, implement, commit, with plan mode (Shift+Tab, or `--permission-mode plan`). Skip the plan when you could describe the change in one sentence.
  - Spec-first for larger features: have the agent interview you, write the spec to SPEC.md, then implement it in a fresh session.
  - CLAUDE.md should hold only what the agent can't infer: commands, project quirks, required environment variables. Keep it short and prune it. If a rule keeps being ignored, the file is too long.
  - The "trust-then-verify gap": the agent produces plausible code that misses edge cases.
  - An adversarial review subagent is useful, but a reviewer asked to find gaps will always report some. Chasing every one leads to over-engineering.
  - CLI tools (`gh`, `aws`, `gcloud`) use less context than MCP servers. Unauthenticated API calls run into rate limits.
  - Unattended runs: `claude -p`, `--allowedTools`, `--permission-mode dontAsk`, and fan-out across worktrees and cloud sessions.
  - Checkpoint limits, from the Checkpointing page: Bash file changes aren't tracked, edits by most subagents aren't restored, symlinked and hard-linked files are skipped, snapshots are deleted after about 30 days, and checkpoints are no substitute for git.
- **Framings it says are outdated:**
  - "Write the code yourself and ask the AI to review it." Now you describe the outcome and the agent explores, plans and implements.
  - "The human notices every mistake." Now you give the agent a pass/fail signal and review its evidence.
  - "Manual approval of every action is the default." As of v2.1.283, auto mode is the built-in starting mode for terminal and VS Code sessions.
  - "Undo/rewind replaces version control."
- **Why it matters:** This is the vendor's own guidance, and it states Aaron's rule almost word for word: the agent does anything that has a check. It also spells out what stays with the human: supplying the check, reviewing the evidence, and refusing to ship what can't be verified.

### 2. Choose a permission mode (Claude Code)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** The page itself is undated. It cites v2.1.283 (published 2026-09-25) as the version where auto mode became the default. Recorded as 2026-09.
- **URL:** https://code.claude.com/docs/en/permission-modes
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - There are six modes, each a trade-off between convenience and oversight: Manual (config value `default`; only reads run without asking), `acceptEdits`, `plan`, `auto`, `dontAsk` (for locked-down CI) and `bypassPermissions` (for isolated containers and VMs only).
  - In auto mode, a second model (the classifier) reviews actions in your place. It does not guarantee safety. Use it when you trust the general direction of the task, not instead of reviewing sensitive operations.
  - Protected paths (such as `.git` and `.claude`) are never auto-approved, except in bypass mode.
  - Deny rules apply in every mode. Allow rules have no effect in bypass mode. Some actions no mode auto-approves (explicit ask rules, tools that need user interaction).
  - The classifier has blind spots. Example: it can't check a recursive delete aimed at a shell variable whose value came from earlier command output, because it never sees that output.
  - Classifier calls cost tokens on API and Enterprise accounts.
  - Bypass mode offers no protection against prompt injection.
  - Cloud sessions offer a different set of modes from the local CLI.
- **Framings it says are outdated:**
  - "Claude Code asks before every edit and command."
  - "Skipping permissions is the cure for prompt fatigue." Auto mode is now the recommended alternative.
- **Why it matters:** It defines the defining new concept of 2026, an AI that reviews the AI's actions, and it documents that concept's limits in the vendor's own words.

### 3. Claude Code auto mode becomes the default (Tried and Typed, with 9to5Mac)
- **Author:** Ashish Akotkar (Tried and Typed). Corroborated by Zac Hall (9to5Mac).
- **Date:** 2026-08-30 (Tried and Typed); 2026-08-14 (9to5Mac)
- **URL:** https://triedandtyped.com/2026/08/30/claude-code-auto-mode-default/ (also read: https://9to5mac.com/2026/08/14/psa-claude-code-enabling-auto-mode-as-default-next-week-anthropic-says/)
- **Kind:** essay (practitioner); news corroboration
- **Credibility:** medium (secondary sources quoting Anthropic's figures)
- **Gaps it names:**
  - On 2026-08-14, auto mode became the default for new Pro, Max and Team sessions. Modes users had already pinned were kept. Enterprise and API users were not switched that day.
  - Before the change, users approved 97% of prompts, which the author reads as reflexive clicking. 9to5Mac reports Anthropic's study of 1,053 paid testers: people caught 13.6% of dangerous commands and auto mode caught 89%. People's catch rate fell to about 5% after 50 prompts.
  - Third-party red-teaming found the classifier missed 12% of dangerous actions at first, and 7% after hardening.
  - A circuit breaker sends the session back to manual prompting after 3 consecutive blocks or 20 total.
  - Blocked by default: piping curl into bash, sending sensitive data out, production deploys and migrations, IAM changes, force pushes and hard resets, IaC destroys, DNS and TLS changes.
  - Allowed without a prompt: reading `.env` and sending the credentials in it to their matching API, and pushing to branches in the current repo, including the default branch.
  - How to tell which mode you're in (`claude --version`, the status bar). For production, pin manual mode and add `permissions.ask` rules for pushes, deploys and migrations.
- **Framings it says are outdated:**
  - "Claude asks yes/no before every edit."
  - "Pushing to main is a checkpoint." Under auto mode it is allowed without a prompt.
  - "The classifier is a rule engine." It is a separate model call.
  - "Auto mode is new." It launched as a research preview in March 2026.
- **Why it matters:** It gives concrete numbers for the course's point: a human clicking "approve" was never a good safety check. It also lists exactly what the default now does without asking, so learners know what they must gate themselves.

### 4. Extend Claude Code (features overview)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** undated
- **URL:** https://code.claude.com/docs/en/features-overview
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - How the extension features differ:
    - CLAUDE.md: loaded every session.
    - `.claude/rules/`: can be limited to certain file paths.
    - Skills: their descriptions load every session; the full content loads on demand.
    - Subagents: an isolated context that returns only a summary.
    - Dynamic workflows: scripts that run many subagents.
    - Hooks: deterministic, fired by lifecycle events.
    - MCP: connections to external systems; tool schemas are deferred until used.
    - Plugins: a way to package all of the above.
    - Also: output styles and code intelligence (LSP).
  - "Put guardrails in hooks." A "never edit .env" line in CLAUDE.md is a request. A PreToolUse hook that blocks the edit is enforcement.
  - Each feature has a context cost, and too many features add noise: skills fail to trigger and conventions get lost.
  - When to add each feature:
    - The agent gets a convention wrong twice: add it to CLAUDE.md.
    - You keep typing the same prompt: make it a skill.
    - You keep copying data from a browser tab: connect an MCP server.
    - A side task floods the conversation: send it to a subagent.
    - Something must happen every time: write a hook.
    - A second repo needs the same setup: make it a plugin.
  - How settings layer: CLAUDE.md files add together; skills, subagents and MCP servers override each other by name; hooks all run.
  - Mark skills that have side effects with `disable-model-invocation`, so they run only when you invoke them by name.
- **Framings it says are outdated:**
  - "An instruction in the prompt or rules file is a guarantee."
  - "Configure everything up front." Add each feature when its trigger shows up.
- **Why it matters:** It is the clearest single map of the 2026 extension concepts. The same concepts carry over to Cursor (rules, skills, hooks), Kiro (steering, hooks) and Codex (AGENTS.md, skills).

### 5. Security (Claude Code)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** undated
- **URL:** https://code.claude.com/docs/en/security
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - The user is responsible for reviewing proposed code and commands before approving them.
  - The working-directory boundary is only a permission prompt. A Bash command you approve can still write anywhere your user account can. Only the OS-level sandbox enforces the boundary.
  - The workspace trust dialog, and the fact that headless `-p` runs show no trust or `.mcp.json` approval prompt.
  - Anthropic reviews connectors before listing them in its directory but does not security-audit any MCP server. Reading `.mcp.json` doesn't show every server a session can load, because user scope, plugins and claude.ai connectors add more.
  - For untrusted content: don't pipe it straight to the agent; review commands; use VMs for scripts that touch external services.
  - Cloud sessions run in isolated VMs, and GitHub credentials stay behind a proxy. Your branch protection rules decide what the agent can push. Self-hosted environments are your own responsibility.
  - Windows WebDAV can bypass the permission system.
  - The page points to `/security-review` and a security-guidance plugin. Both are on-demand checks, not guarantees.
- **Framings it says are outdated:**
  - "The agent's built-in protections make it safe." The page says no system is immune to all attacks.
- **Why it matters:** It backs the course's security rule with the vendor's own words, and it names checks the agent cannot make for you: which MCP servers and repos to trust, and what your branch protections allow.

### 6. Manage costs effectively (Claude Code)
- **Author:** Anthropic (Claude Code documentation)
- **Date:** The page itself is undated. It cites v2.1.271 (published 2026-09-14). Recorded as 2026-09.
- **URL:** https://code.claude.com/docs/en/costs
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - Subscription and API billing work differently. The dollar figure in `/usage` matters only to API users.
  - Team and Enterprise seat allowances reset on a rolling five-hour window and a weekly window. The allowance is shared with Claude chat and Cowork.
  - Four different messages that beginners confuse:
    - a session or weekly limit (switching models won't help);
    - a model-specific limit (switching models will);
    - a spend limit on usage credits;
    - a context or auto-compact warning, which is not a usage limit at all.
  - Why usage climbs in a long session:
    - The whole conversation is resent with every request.
    - The prompt cache lasts 1 hour on a subscription, but 5 minutes on usage credits or an API key.
    - Scheduled tasks, goal check-ins and messages from other sessions each send the full context.
    - Subagents and agent teams make their own requests (teams use about 7 times more tokens when teammates run in plan mode).
    - Compaction is itself a large request, while `/clear` costs nothing.
  - Typical enterprise cost: about $13 per developer per active day, or $150 to $250 a month.
  - Extended thinking is billed as output tokens.
- **Framings it says are outdated:**
  - "Coding with an agent costs about the same as chatting." The page says one debugging session can use more than a day of chat.
- **Why it matters:** Usage limits surprise every beginner. This page explains the mechanism (context is resent, caching expires) instead of just listing prices.

### 7. Use Claude Cowork safely
- **Author:** Anthropic (Claude Help Center)
- **Date:** The page showed "Updated this week" when fetched on 2026-10-12. Recorded as 2026-10.
- **URL:** https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - Where Cowork runs: in an isolated, temporary cloud environment on Anthropic's servers. It reaches local files only through the Claude Desktop app, and only for folders you've connected. Local files it opens are processed in the cloud.
  - The difference between read tools and write tools. Write tools (deleting files, running commands, clicking) carry more risk.
  - Prompt injection needs two conditions: the agent reads untrusted content, and it can take a harmful action. Limiting either one reduces the risk.
  - Computer use has no sandbox. It acts directly on your screen and can open links even in apps you haven't authorized, so block sensitive apps.
  - Claude in Chrome and the built-in browser can see your logged-in pages. Don't use them for sensitive information. Network egress settings don't cover web fetch or web search.
  - Scheduled tasks run in the cloud while your computer is off, and you can't watch them live. Avoid tasks that touch sensitive data or are hard to undo.
  - Local MCP servers run with your computer's permissions. Plugins open new attack paths.
  - Switch to "Manually approve" for sensitive files, new tools and hard-to-undo actions.
  - You remain responsible for every action Claude takes on your behalf.
- **Framings it says are outdated:**
  - "It runs in an isolated environment, so it is safe." The page says isolation limits where code runs, not what Claude can read or do.
- **Why it matters:** It covers the agent that non-coders use (files, browser, schedules), and it states the prompt-injection model more precisely than any coding doc in this sweep.

### 8. Agent approvals & security (OpenAI Codex docs)
- **Author:** OpenAI (docs now hosted on learn.chatgpt.com; the old developers.openai.com URL returns a 308 redirect there)
- **Date:** undated
- **URL:** https://learn.chatgpt.com/docs/agent-approvals-security.md
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - There are two separate controls: the sandbox mode (read-only, workspace-write, danger-full-access) and the approval policy (on-request, never, granular, auto_review).
  - auto_review sends eligible approvals to a reviewer agent first. It denies critical-risk actions and fails closed when something goes wrong.
  - Network access is off by default. Web search uses a cached index by default.
  - Folders under git start in workspace-write with on-request approvals. Folders not under git start read-only. So whether a folder is under git changes what the agent may do.
  - `.git`, `.agents` and `.codex` are read-only to the agent.
  - The OS enforces the sandbox: Seatbelt on macOS, bwrap and seccomp on Linux, separate options on Windows.
  - In cloud runs, secrets are available during setup and are removed before the agent phase starts.
  - Treat web results as untrusted. Live web search and network access increase prompt-injection exposure.
  - The user's job: work on a feature branch, keep `git status` clean, and review diffs like a pull request. Use the dangerous settings only in tightly controlled environments and never on untrusted repos. A devcontainer with full access can expose its credentials to a malicious project.
  - Local and cloud execution policies are separate, and each must be tested.
- **Framings it says are outdated:**
  - The "untrusted" approval policy has been retired, and using it can stop the client from starting.
  - Codex Cloud is now labelled "(Legacy)".
- **Why it matters:** A second vendor uses the same model as Anthropic (a sandbox, approval rules, a reviewer agent) and adds concrete facts, such as cloud secrets being removed before the agent runs.

### 9. Codex best practices (OpenAI)
- **Author:** OpenAI
- **Date:** The page itself is undated. It refers to GPT-6.1 Sol, which the changelog (#10) says reached Codex on 2026-09-29. Recorded as 2026-09.
- **URL:** https://learn.chatgpt.com/guides/best-practices
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - A prompt structure: Goal, Context, Constraints, and "Done when".
  - Matching reasoning effort to the task.
  - Plan mode (`/plan` or Shift+Tab).
  - AGENTS.md at global, repo and subdirectory levels. `config.toml` holds model, sandbox, approval, profile and MCP defaults.
  - Skills as `SKILL.md` files in `$HOME/.agents/skills` or `.agents/skills`.
  - Scheduled tasks (automations), optionally run in a git worktree.
  - Subagents for bounded work, and worktrees so parallel tasks don't collide on the same files.
  - `/resume`, `/fork` and `/compact`.
  - Common mistakes:
    - giving Codex full permission to your computer before you understand the workflow;
    - running live tasks on the same files without worktrees;
    - scheduling a recurring task before it works reliably by hand;
    - skipping planning on complex work;
    - using one chat for a whole project.
  - The page assumes you already know git (worktrees, diffs, branches), tests and CI.
- **Framings it says are outdated:**
  - "Keep one long chat per project." The page says this bloats context and gives worse results over time.
- **Why it matters:** It shows that skills, AGENTS.md, plan mode and worktrees now appear in more than one vendor's tools. The course is teaching a shared vocabulary, not one company's features.

### 10. ChatGPT & Codex changelog (with "Get started with ChatGPT Work")
- **Author:** OpenAI
- **Date:** 2026-10-08 (latest entry read)
- **URL:** https://learn.chatgpt.com/docs/changelog (also read: https://learn.chatgpt.com/docs/get-started-with-work)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - Models are retired on short notice. GPT-5.5 retires from ChatGPT, ChatGPT Work and Codex on 2026-10-14 (announced 2026-09-14). GPT-5.4 left Codex for ChatGPT sign-ins on 2026-08-31. GPT-5.3-Codex-Spark was deprecated on 2026-09-14. Setups pinned to a model name break.
  - Codex joined the ChatGPT desktop app on 2026-07-09. On 2026-08-11 came a Linux desktop preview and imports from Claude Code, Claude Cowork and Cursor.
  - Tools disappear within weeks. The `codex mcp-server` command was deprecated on 2026-08-24 and removed on 2026-09-05.
  - Scheduled tasks can now be triggered by Gmail, Slack and GitHub events (2026-08-25). Other new features: site tools (WebMCP), Computer Use, Record & Replay, and Sites (preview from 2026-06-02).
  - ChatGPT Work and Codex share the same usage limits and credits. Rate-limit reset banking arrived on 2026-06-11.
  - From "Get started with ChatGPT Work":
    - Work is for delegating multi-step tasks that end in a result you review.
    - Connectors are plugins.
    - Local computer access exists only in the desktop app; a cloud container cannot reach your computer's files.
    - You approve important actions, and you review outputs before treating them as final.
    - Longer tasks use more credits.
- **Framings it says are outdated:**
  - "Codex is a separate coding product." It now lives in the ChatGPT desktop app, and ChatGPT Work handles non-coding deliverables.
  - Within the first 100,000 characters of the changelog that were read, no entry uses the term "agent mode". Delegated multi-step work is now described as ChatGPT Work. (This is an observation about the text read, not a claim about OpenAI's naming everywhere.)
- **Why it matters:** It is dated, concrete evidence for the course's premise that what you need to know changes every week.

### 11. Risks and mitigations for Copilot cloud agent (with the 2026-04-01 changelog)
- **Author:** GitHub
- **Date:** The docs page is undated. The changelog announcing the rename and the new planning features is dated 2026-04-01.
- **URL:** https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations (also read: https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent/)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - The agent checks its own output with CodeQL, secret scanning and a Copilot code review pass. New dependencies are checked against the GitHub Advisory Database for malware and High or Critical CVEs. All of these checks can be switched off.
  - Only users with write access can trigger the agent. Comments from other users are not passed to it.
  - It can push only to a `copilot/` branch or the existing PR branch, and branch protections and required checks still apply.
  - It opens draft PRs and cannot mark them ready, approve them or merge them. The person who requested the work cannot approve it, so a second person must review.
  - GitHub Actions workflows don't run on its PRs until a user with write access approves them.
  - A firewall restricts its internet access. Hidden characters, such as text in HTML comments, are filtered out before input reaches it (a prompt-injection defence).
  - Commits are authored by Copilot, credit the requester as co-author, and link to session logs.
  - Automations are attributed to the person who created them. Events from users without write access are ignored unless you opt in.
  - From the changelog: the agent can now research and draft an implementation plan for your approval before coding, and can work on a branch without opening a PR. Admins must enable it on Business and Enterprise plans.
- **Framings it says are outdated:**
  - The name "Copilot coding agent" is now "Copilot cloud agent" (April 2026).
  - "Agent work always arrives as a pull request."
- **Why it matters:** The agent's safeguards rest on repository settings that only the human can configure: branch protection, required reviewers, workflow approval. Beginners often don't know these settings exist.

### 12. Best practices for coding with agents (Cursor)
- **Author:** Lee Robinson (Cursor)
- **Date:** 2026-01-09
- **URL:** https://cursor.com/blog/agent-best-practices
- **Kind:** essay (vendor practitioner)
- **Credibility:** high
- **Gaps it names:**
  - The "agent harness" is the instructions, tools and model working together.
  - Plan mode, with plans saved to `.cursor/plans/`.
  - Rules (`.cursor/rules/`), skills (`SKILL.md`), hooks (including a stop hook that keeps the agent iterating) and commands (`.cursor/commands/`).
  - Give the agent verifiable goals: tests, linters, typecheckers. In TDD, confirm the tests fail before the code is written, and that the agent didn't modify the tests to make them pass.
  - Agent code can look right while being subtly wrong. Faster agents make review more important, not less.
  - Worktrees for parallel agents. Running the same prompt on several models and comparing the results.
  - Cloud agents clone the repo into a remote sandbox, work on their own and open PRs.
  - Debug Mode: the agent forms hypotheses, adds logging, collects runtime data and fixes based on evidence.
  - Long conversations lose focus, so start new ones. Rules go stale, so point to files instead of copying them.
  - Agents connected through MCP can reach Slack, Sentry, Datadog and databases. Decide that access deliberately.
- **Framings it says are outdated:**
  - "Debugging by hand." Debug Mode has the agent instrument the code and gather the evidence. (This matches Aaron's correction.)
- **Why it matters:** It is practical, dated guidance from a practitioner, and it names a specific verification trap: an agent that edits the tests until they pass.

### 13. Cursor changelog (2026-08-27 to 2026-10-06)
- **Author:** Cursor
- **Date:** 2026-10-06 (latest entry read)
- **URL:** https://cursor.com/changelog
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - Remote control of local agents from the iOS app (2026-10-06). The computer must stay on and online.
  - Security Review (2026-09-23, Teams and Enterprise): one review comment per PR about exploitable bugs, with severity, attack path and a proposed fix. Draft PRs are skipped.
  - Rollouts (also 2026-09-23) writes a monitoring plan for each PR and reports change health per environment. It doesn't merge or roll back on its own.
  - Cursor Projects (2026-09-10, beta): a coordinator agent plans the work and hands it to cloud and local agents. Context files are shared between agents, and work can be triggered from Slack, schedules or PRs.
  - Self-hosted machines (2026-09-02): tool execution stays on your own infrastructure. Cloud agents can run on sandbox providers such as AWS Lambda, Modal, Vercel and E2B.
  - Starting without a repo (2026-08-27): Cursor creates an "Origin" repo in the background, but publishing requires a Vercel account.
- **Framings it says are outdated:**
  - "A coding tool is an editor with an assistant." It is now a coordinator managing fleets of local and cloud agents.
  - "You need a GitHub repo first." A hidden repo is created for you, but a hosting account is still required.
- **Why it matters:** It shows prerequisites shifting under beginners: where the repo lives and who hosts the app. It also shows security review becoming a paid feature rather than a default.

### 14. Transitioning Gemini CLI to Antigravity CLI (with the Gemini CLI docs)
- **Author:** Dmitry Lyalin (gemini-cli maintainer, Google)
- **Date:** 2026-05-19 (announcement). The Gemini CLI docs home says "last updated Apr 17, 2026" and carries a banner about the 2026-06-18 move.
- **URL:** https://github.com/google-gemini/gemini-cli/discussions/27274 (also read: https://geminicli.com/docs/)
- **Kind:** community (official announcement thread, with user replies)
- **Credibility:** high for the announcement; medium for the user reports in replies
- **Gaps it names:**
  - On 2026-06-18, Gemini CLI stops serving requests for Google AI Pro and Ultra users and for free users. Enterprise licences, Google Cloud and paid API keys are unaffected. Which kind of account you sign in with now decides whether the tool works at all.
  - Antigravity CLI is built in Go, runs background workflows and shares its architecture with the Antigravity 2.0 desktop app. Skills, hooks, subagents and extensions carry over and are now called Antigravity plugins.
  - The Gemini CLI repo stays Apache 2.0. The announcement does not say whether the replacement is open source, and a commenter's direct question went unanswered in the visible replies.
  - Users report that quota runs out much faster, and that MCP servers appear in the UI but the agent doesn't detect them.
  - From the docs: GEMINI.md context files, sandboxing, checkpointing, trusted folders, plan mode, subagents, hooks, rewind, token caching, quotas, and installing with `npm install -g`.
- **Framings it says are outdated:**
  - "Gemini CLI is Google's free, open-source terminal agent for anyone with a Google account." That ended for consumer accounts on 2026-06-18.
  - Tutorials that start with `npm install -g @google/gemini-cli` and a personal Google sign-in.
- **Why it matters:** It is the clearest case of tutorial rot in this sweep: a widely taught 2025 setup simply stops working for consumer accounts.

### 15. Getting Started with Google Antigravity (codelab)
- **Author:** Google (codelab; no named author on the page)
- **Date:** undated. The codelab describes Antigravity 2.0 and its CLI, which the 2026-05-19 Gemini CLI announcement (#14) also refers to.
- **URL:** https://codelabs.developers.google.com/getting-started-google-antigravity?hl=en
- **Kind:** course (official codelab)
- **Credibility:** high
- **Gaps it names:**
  - Antigravity is a family of products: a standalone app (the agents' "central command center"), an IDE with an Agent Panel, a CLI, an SDK and extensions for other IDEs.
  - Prerequisites: Chrome as your default browser (the browser sub-agent needs it) and a personal Gmail account or a business account.
  - Choices made at install time, before the user knows what they mean:
    - a Security Preset that decides whether you review every terminal command and file access;
    - a review policy (it can be set to "Always Proceed");
    - allowed file paths and allowed or blocked URLs;
    - which MCP tools each project may use.
    - Project settings override the global ones.
  - Artifacts (task lists, implementation plans from `/plan`, walkthroughs, diffs, screenshots) exist to close the "trust gap". They are not always generated.
  - Skills (`SKILL.md`) at global or project scope.
- **Framings it says are outdated:**
  - "Editor first." The new default is an agent manager where you review artifacts.
- **Why it matters:** It shows that reviewing plans and walkthroughs, rather than reading code, is a new human skill. It also shows beginners being asked to set security policy on the install screen.

### 16. Kiro specs (with the Kiro docs index)
- **Author:** Kiro (AWS)
- **Date:** 2026-10-02 (specs page updated); 2026-10-07 (docs index updated)
- **URL:** https://kiro.dev/docs/specs/ (also read: https://kiro.dev/docs/)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - A spec is three files: requirements.md (or bugfix.md for bugs), design.md and tasks.md.
  - The workflow runs requirements, then design, then tasks. Tasks can run in dependency-based "waves" at the same time.
  - "Quick Spec" generates all three files without approval gates and suits well-understood features. "Analyze Requirements" finds gaps before design starts.
  - Steering files, hooks (on file changes, tool use or task completion), checkpoints, powers and skills, and a CLI with headless and CI modes.
  - `.kiro/` configuration is shared across the IDE, CLI, web and mobile.
  - The docs assume you know AWS IAM Identity Center, IAM, VPC endpoints, SSO, Git/GitHub, context limits and sub-agents.
- **Framings it says are outdated:**
  - "Prompt, then get code." In spec-driven work, the human reviews the requirements and design before any code exists.
- **Why it matters:** Spec-driven development is the counterweight to vibe coding. It moves the human's job to checking requirements and design, which the agent cannot verify against what you actually want.

### 17. Lovable security
- **Author:** Lovable
- **Date:** undated
- **URL:** https://docs.lovable.dev/features/security
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - The Quick scan runs automatically when you publish. It checks database access rules, npm dependency vulnerabilities and MCP servers exposed without authentication.
  - The Deep scan runs only on demand. It checks access control, unauthenticated endpoints, injection, leaked secrets, payment logic, authentication weaknesses and sensitive-data exposure.
  - Row-level security (RLS) decides which users can read or change which records. Review it before publishing and after any authentication or schema change.
  - Frontend code runs in the browser, so keys must never be hardcoded there. Lovable steers keys pasted into chat into Secrets. API calls should go through server-side code.
  - The scans don't guarantee completeness or replace a thorough security review. Apps that handle sensitive data need a professional security review.
  - The user must make sure the app meets the security requirements of its use case, and keep dependencies updated.
  - An admin option, "Block publishing with critical issues", is on by default for new Enterprise workspaces.
- **Framings it says are outdated:**
  - "The builder takes care of security."
- **Why it matters:** The vendor itself tells users to bring in an expert, which is Aaron's rule in the tool's own docs.

### 18. Replit checkpoints and rollbacks (with the Agent overview)
- **Author:** Replit
- **Date:** undated
- **URL:** https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks (also read: https://docs.replit.com/replitai/agent)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - A checkpoint captures files, packages, configuration, the AI conversation context, environment and publishing settings, the agent's memory of the project, and the database's contents and schema.
  - A rollback does not change the database unless you tick "Database", and even then it covers only the development database.
  - The production database is never restored by a rollback. It needs a separate point-in-time restore.
  - Rolling back removes every change made after that point. New work after a rollback creates an alternate branch.
  - Each checkpoint carries billing information. Agent modes (Free, Auto, Power, Max) differ in cost, and Free Mode allowances reset every five hours.
  - Plan mode produces an ordered task list for your approval before any code or data changes.
  - The docs say no coding knowledge is needed, which is why the dev/prod database split catches users off guard.
- **Framings it says are outdated:**
  - "Undo restores everything." Live user data is not restored.
- **Why it matters:** It makes the separation between development and production data concrete, and it shows exactly where the safety net stops.

### 19. Windsurf becomes Devin Desktop (AlphaSignal, with the Devin Desktop Cascade docs)
- **Author:** AlphaSignal Newsroom. Docs by Cognition.
- **Date:** 2026-06-02 (article; last modified 2026-06-16). The Cascade docs page is undated.
- **URL:** https://alphasignal.ai/news/cognition-turns-windsurf-into-devin-desktop-with-a-30-faster-local-agent (also read: https://docs.devin.ai/desktop/cascade/cascade, which docs.windsurf.com now redirects to)
- **Kind:** report (tech news); docs
- **Credibility:** medium (news); high (docs)
- **Gaps it names:**
  - Windsurf was renamed Devin Desktop through an over-the-air update. The Agent Command Center (a Kanban board of local and cloud agents grouped by status) replaced the code editor as the default view.
  - The Cascade agent was deprecated as of July 1. Its replacement, Devin Local, was rewritten in Rust, adds subagents and is reported to be up to 30% more token-efficient.
  - The Agent Client Protocol (ACP) lets Codex, Claude Agent and OpenCode run in the same workspace. It requires a Pro, Max or Teams plan.
  - From the docs: Cascade makes up to 40 tool calls per prompt. Pressing "continue" costs a new prompt credit, and auto-continue keeps spending credits. Reverts are irreversible. Named checkpoints are available.
  - The docs assume you know Restricted Mode, ACP agents, worktrees and `.gitignore`.
- **Framings it says are outdated:**
  - Tutorials that say "Windsurf" and "Cascade".
  - Editor-centred workflows.
- **Why it matters:** It is another rename that comes with a new default screen. A beginner following a 2025 guide won't find the product the guide describes.

### 20. v0 security (with External APIs and environment variables)
- **Author:** Vercel (v0 docs)
- **Date:** 2026-10-09 (`lastUpdated` in the page metadata of both pages)
- **URL:** https://v0.app/docs/security (also read: https://v0.app/docs/external-apis)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - A `NEXT_PUBLIC_` prefix sends a variable to the browser. Never use it for sensitive tokens. v0 analyzes this usage and warns about it.
  - Environment variables are set per environment: Production, Preview and Development. The v0 preview can see only Development variables. Use separate keys for development and production, and rotate them.
  - v0 treats generated code as potentially incorrect or adversarial and runs it in isolated environments. Server code deploys as Functions, each in its own container.
  - The docs give no app-level guidance on authentication or database access. That responsibility falls to the builder.
  - Hidden prerequisites in the docs index: Vercel deployments, custom domains, and database integrations (Neon, Supabase, Upstash, Blob).
- **Framings it says are outdated:**
  - "A key stored in an environment variable is private." Not if it carries the `NEXT_PUBLIC_` prefix.
- **Why it matters:** Environment variables, the split between client and server code, and separate dev and prod keys are classic hidden-curriculum gaps. Here they are stated in a current vendor doc.

### 21. Bolt: check your project's security (with "Maximize token efficiency")
- **Author:** Bolt (StackBlitz)
- **Date:** undated
- **URL:** https://support.bolt.new/building/security.md (also read: https://support.bolt.new/best-practices/maximizing-token-efficiency.md)
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - What the paid project audit checks:
    - data access: whether one user can see, change or delete another user's data;
    - public exposure: whether error messages and sign-in screens leak details, such as whether an email has an account;
    - sign-in rules;
    - business-logic misuse: changing a price, skipping a required step, reusing a single-use item;
    - input handling;
    - private keys appearing in browser-visible output;
    - which sites can connect to the app.
  - A database security check on all plans flags rules that let anyone read a table.
  - Fixes can change things you didn't want changed. Some fixes require action at outside providers (email, payments). Run the check before publishing.
  - Asking for an audit in chat costs tokens. The button does not.
  - Habits that waste tokens:
    - too much context, oversized projects, and unneeded connectors;
    - using the Max agent for simple tasks;
    - vague prompts, and prompting for actions a button already does;
    - error loops from clicking automatic fix again and again;
    - exploring ideas in Build mode instead of Plan mode.
- **Framings it says are outdated:**
  - "Keep clicking fix." Break the loop and investigate instead.
- **Why it matters:** It names business-logic abuse, a security class that both scanners and beginners miss. It also treats tokens as a currency the user has to manage.

### 22. Human-in-the-loop for AI tool calls (n8n)
- **Author:** n8n
- **Date:** undated
- **URL:** https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - You can require human approval before an AI Agent runs specific tools: ones that send messages, modify records or delete data. The workflow pauses until someone decides.
  - The reviewer sees the tool name and the parameters the AI wants to use.
  - Approvals can go to a different channel from the one users chat in (Slack, Teams, email, Telegram and others).
  - On denial, the action is cancelled and the AI is told. If the system prompt doesn't describe the review step, the agent handles denials badly.
  - Start with review on, and reduce it as your confidence grows.
  - The page assumes you can already set up credentials for each channel, create a Slack app, and use expressions (`$fromAI`, `$tool.name`, `JSON.stringify`).
- **Framings it says are outdated:**
  - "Fully autonomous agents for irreversible actions."
- **Why it matters:** It is the automation-builder's version of permission modes, and it names the specific irreversible actions to gate.

### 23. Zapier Agents: unexpected activity usage
- **Author:** Zapier Help Center
- **Date:** 2026-10-01 (updated)
- **URL:** https://help.zapier.com/hc/en-us/articles/45697420326285-Zapier-Agents-unexpected-activity-usage
- **Kind:** docs
- **Credibility:** high
- **Gaps it names:**
  - Each action is a billable activity.
  - A trigger that returns many records repeats the agent's actions for every record.
  - Each knowledge-source search and each web page visit or search costs an activity.
  - Tests count against the quota on Free plans.
  - A trigger set to process existing data reprocesses the whole source.
  - An agent can trigger a Zap that changes the data the agent watches, which creates a loop.
  - Each run is capped at 10 activities on Free plans and 40 on paid plans.
  - Fixes: keep agents to 3 to 5 related actions, process only new records, add a "processed" flag or separate input and output data to break loops, and check the Activity log regularly.
- **Framings it says are outdated:**
  - "Set it and forget it" automation without watching usage.
- **Why it matters:** It is the non-coder's version of runaway token spend, with specific, recent causes.

### 24. AGENTS.md
- **Author:** AGENTS.md project (stewarded by the Agentic AI Foundation under the Linux Foundation)
- **Date:** undated. It is foundational and still current, and is cited by the Codex docs (#9).
- **URL:** https://agents.md/
- **Kind:** framework
- **Credibility:** high
- **Gaps it names:**
  - AGENTS.md is a "README for agents". Suggested contents: a project overview, build and test commands, code style, testing instructions, security considerations, commit and PR guidelines, and deployment steps.
  - Monorepos can have one AGENTS.md per subproject. The nearest file wins, and explicit chat prompts override everything.
  - Tools that read it include Codex, Cursor, Copilot's coding agent, Windsurf, Jules, Aider, Zed, Warp, VS Code and Devin. Gemini CLI can be configured to read it.
  - Over 60,000 open-source projects use it.
  - The page doesn't mention CLAUDE.md, which Claude Code reads (see #1 and #4). A beginner has to know which file their own tool actually reads. The page suggests a symlink to keep old file names working.
- **Framings it says are outdated:**
  - "Every tool needs its own instruction file." There is now a cross-tool standard.
- **Why it matters:** It is the closest thing to a shared standard for the "standing instructions" concept that every tool in this sweep now has.

### 25. MCP Security Best Practices
- **Author:** Model Context Protocol project
- **Date:** undated. It references spec revision 2026-07-28 and points to the 2025-11-25 version for older session guidance.
- **URL:** https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- **Kind:** docs (standard)
- **Credibility:** high
- **Gaps it names:**
  - Local MCP servers are programs that run with your privileges. A malicious startup command in a config can steal SSH keys or delete files.
  - Before a one-click install, the client should show the exact command it will run and ask for explicit consent.
  - Local servers should use stdio, or HTTP with authentication, so other processes on your machine (including a DNS-rebinding web page) can't reach them.
  - Scope minimization: broad tokens (`files:*`, `admin:*`) make a stolen token far more damaging.
  - Token passthrough is forbidden (a server must not accept tokens issued for another service).
  - The confused-deputy problem with OAuth proxies.
  - SSRF: a malicious server can point a client at cloud metadata endpoints.
  - In the 2026-07-28 revision, MCP is stateless. A state handle is not authentication.
- **Framings it says are outdated:**
  - "MCP sessions." Server-assigned session IDs belong to protocol version 2025-11-25 and earlier. The current revision has no protocol-level sessions.
- **Why it matters:** MCP is the standard behind the "connectors" every tool now offers. This page lists what a user installing a server is actually trusting, and what they should check before clicking install.
