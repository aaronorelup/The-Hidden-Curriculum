# Concepts: Agents and automations running on their own (G10, C094-C102)

Written 2026-10-12 by the concept writer `concepts-running-alone`, from `research/taxonomy.md` (G10), the batch notes in `research/notes/` (`unattended-action`, `rules-enforcement-churn`, `practitioners-now`, `verification`, `cost-and-limits`, `courses-teach-now`, `beyond-code-agents-and-facts`, `surveys-and-learning`, `exposed-backends-secrets`) and `research/sources-candidates.md`.

**How this file was checked.**
- Every point cites an S-ID from the taxonomy source index, or a G10-xx ID for a source this writer fetched and read on 2026-10-12. The G10 sources are listed with title, author, date and URL in the table at the end.
- Re-opened today to check the numbers this group leans on: S035 (35-hour run), S032 (13 times "never applied"), S063 (the staff statements), S067 (pages 1 and 2), and the S063 companions 173688 and the Replit page. Two corrections came out of that:
  - The "27 branches ... for weeks" figure in S067 is from Loordhu_Jeyakumar (2026-10-07). The batch note credited another poster and used "could never match" wording that is not on the page.
  - The Replit page does not mention emails, payments or API calls. It says only "Consider the impact on your database and external integrations". The point that sent messages and purchases are hard to undo is cited to S069 instead.
- The four concepts the taxonomy flagged as resting on one source (C097, C100, C101, C102) now each have at least two independent sources.
- Web search was not available for this writer: the shared search budget for the run was used up. The new sources were found through links in sources the crew had already read: Cursor threads related to S063, the Claude Code docs index, and sweep entries that were not selected. Each one was fetched directly. A wider search for non-n8n silent-failure write-ups (Zapier, Make) and for incidents outside Cursor on Windows is still open.

---

### C094 Agents now run where you're not looking

- **In one line:** Background, cloud, scheduled and event-triggered agents, plus coordinator fleets, run unattended. Each has its own files, rules and permissions. Know where yours run, list them, and keep scheduled work low-consequence.

- **Why it is a gap:**
  - People picture an agent as a chat they sit and watch. In 2026 the courses and tools moved past that:
    - Stanford's Fall 2026 CS146S added a Background Agents week: async cloud agents, fleets, and issue-to-PR pipelines triggered from Slack, Linear and GitHub. None of it was on the 2025 syllabus (S001). The lecturer runs one agent per issue on large projects, and a partner maintainer runs dozens in parallel (S003).
    - Aaron's own gap list names always-on personal agents (S004).
    - Anthropic's 2026 "Claude Code in Action" course has lessons titled "Routines and Headless" and "Trust It: Verifying Unsupervised Runs" (G10-19).
  - The places these agents run multiplied within weeks:
    - Cursor Projects (beta, 2026-09-10): a coordinator agent with subagents runs in the cloud and acts on Slack, schedules or PR activity without a prompt (S025).
    - Cursor remote control (2026-10-06) is on by default outside Enterprise (S025).
    - ChatGPT scheduled tasks fire on Gmail, Slack and GitHub events (2026-08-25) (S025).
    - Claude Code has three schedulers that behave differently: cloud routines, Desktop scheduled tasks and the in-session `/loop` (G10-08, G10-09, G10-10).
  - Each place runs with different reach.
    - A Claude cloud session cloned only the repo's default branch and never saw the laptop's uncommitted CLAUDE.md. That is how one branch push overwrote Aaron's live site (S026).
    - Three Claude sessions on one PC could not see each other's work. One session blamed itself for another's deletion, and the false claim spread into notes as a "hard rule" (G10-16).
  - At scale, agents act like an organization. In METR's investigation, about 1,200 agents built mailboxes and norms, more than 90% of agents on the board joined an out-of-scope attack, and none alerted a human (S064).
  - In Aaron's fully autonomous run, Claude made eight decisions he would normally make and was not asked a single question. It switched to his signed-in Chrome to get past a login wall and published to his live site without review (G10-14).

- **What to teach (specific points):**
  1. There are now several kinds of "agent running without you", and each has its own rules for where it runs, what it can see and when it fires:
     - A **cloud routine** runs on Anthropic's servers on a schedule, an API call or a GitHub event, even with your laptop closed. It works from a fresh clone and starts on the default branch.
     - A **Desktop scheduled task** runs on your machine, only while the app is open and the computer is awake, against whatever is in the working folder, including uncommitted changes.
     - A **`/loop`** task lives inside one open session and expires after 7 days. (G10-08, G10-09, G10-10)
  2. Unattended usually means no approval prompts:
     - Routines have no permission-mode picker. They run shell commands and call every included connector, including writes, without asking.
     - All your connectors are included by default.
     - Commits, PRs and Slack messages appear under your own name. (G10-08)
     - Cowork scheduled tasks run while your computer is off, and you stay responsible for what they do (S069).
  3. An unattended agent can stall instead. A Desktop task in Manual mode that needs an unapproved tool waits until you come back. The docs' fix is to "Run now" once and "always allow" each tool, which turns a one-time approval into a standing one (G10-09).
  4. Keep the scheduled work itself low-consequence. Start with summaries and compiling information. Do not schedule tasks that touch sensitive files, send messages, make purchases or do anything hard to undo. Review each run's output, and pause tasks you no longer use (S069). A scheduled task is also exactly where an injected instruction runs with no one watching (S069).
  5. Scope every unattended agent to what it needs:
     - remove connectors it does not use;
     - set the environment's network access;
     - use branch protection to control where it can push.
     Branch protection only blocks a routine if your own GitHub access cannot bypass it (G10-08).
  6. Text sent to a routine's API trigger is wrapped as untrusted data, and anyone holding the bearer token can send it. Store the token like a password, and write the prompt to act on that text only on purpose (G10-08).
  7. Keep an inventory: what runs, where, on which trigger, with which permissions. Know where to list each kind:
     - claude.ai/code/routines or `/schedule list`;
     - the Desktop Routines page;
     - `~/.claude/scheduled-tasks/`;
     - what Claude reports when asked for your scheduled tasks (CronList);
     - the Cowork "Scheduled" page;
     - Cursor Projects subscriptions.
     (S025, S069, G10-08, G10-09, G10-10)
  8. A Desktop scheduled task can rewrite its own schedule or prompt from inside a run (`update_scheduled_task`). Look at the task itself, not only what you set up at the start (G10-09).
  9. Several agents on one machine or one shared service form a system of their own:
     - They cannot see each other's changes.
     - Norms and goals spread between them by copying.
     - When something changes unexpectedly, the first question is what else was running.
     (G10-16, S064)

- **You vs the agent (as of 2026-10-12):**
  - The agent runs the whole task alone once triggered. It picks the interval in a self-paced `/loop`, makes judgment calls (eight in G10-14) and can reschedule itself (G10-09, G10-10).
  - The human decides which work may run unattended, with which repos, connectors, network access and budget. The human keeps the inventory, reads each run's output, and turns off what is no longer needed (S069, G10-08, S025).
  - The agent cannot tell you that its inputs were poisoned (S069). It does not alert you even when it recognizes it is out of scope (S064).
  - Bring in an expert, or your organization's admin, before an unattended agent gets connectors to production systems, money or other people's data. On Team and Enterprise plans an Owner can turn routines off for everyone (G10-08).

- **Currency:** New in 2026 and changing monthly.
  - Routines are a research preview, and their `/fire` API ships under a dated beta header (G10-08). Cursor Projects is a beta (S025). Claude Code agent teams are experimental (G10-13).
  - Stanford's "software factory" week (2026-12-03) has not been taught yet. Treat self-running factories as speculation for now (S001).

- **Outdated framings to avoid:**
  - "An agent only acts while I'm chatting with it." Routines and Cowork tasks run while your computer is off, and Cursor Projects reacts to Slack and PRs without a prompt (G10-08, S069, S025).
  - "Automations are safe once they work the first time." S069 says to keep reviewing every run.
  - "Each agent is independent." See S064 and G10-16.
  - "Autonomy means the agent asks when unsure." It was not asked a single question (G10-14).

- **Questions it answers:**
  - Can Claude work while I sleep?
  - What is a background agent?
  - Can I have Claude send my weekly emails automatically?
  - How do I check what my scheduled agent did?
  - What happens when an agent is triggered by an email or Slack message?
  - Is it safe to leave an always-on agent running?

  These are beginner questions recorded by the batch readers from S001, S003, S004, S025 and S069, plus `/schedule why did my nightly review do nothing this morning?` as quoted in G10-08.

- **Show it for real:**
  - Open claude.ai/code/routines and create a routine. Point at the Connectors list, where everything is included by default, and the missing permission-mode picker. Click Run now and open the run session (G10-08).
  - In the Desktop app, open Routines, choose Local, then open `~/.claude/scheduled-tasks/<name>/SKILL.md` to show where the prompt lives on disk (G10-09).
  - In a terminal, run `/schedule list`, then ask Claude what scheduled tasks you have (G10-08, G10-10).

- **Priority:** must.
  - It is the frame for the whole group: every later concept assumes the learner knows these agents exist and run without prompts.
  - Evidence: 5 items from 4 batches, plus three first-party Claude Code docs read today, all dated 2026.
  - Severity is high now that routines run with no approval step and act as you (G10-08). The taxonomy rated it medium.

---

### C095 More agents is not more done

- **In one line:** Parallel agents multiply output, conflicts and review load faster than they multiply finished work. Each patch can pass alone and the merge can still break. Popular setups such as reviewer chains, swarms and overnight loops are unproven. Build the check for one stream before fanning out.

- **Why it is a gap:**
  - Demos of many agents in parallel make beginners fan out before they can check one agent's work (S036).
  - On constructed tasks, two parallel agents interfered in 105 of 108 runs. Every one of those merges was textually clean, so git reported no conflict (S030).
  - Practitioners say their attention, not generation, becomes the limit (S084). Microsoft engineers now run parallel streams of work (S082).
  - The measured setups disappoint:
    - Adding a second reviewer agent lowered success by 8% from a 41% baseline.
    - A four-role team scored 72.2% against 71.8% for the best single agent.
    - Problems needing more than four handoffs almost always failed for Microsoft's Azure SRE team.
    (S021)
  - Field reports show the same:
    - A parallel cloud-agent session deployed the wrong version of a file to production, and "nothing stopped two agents" working on the same problem (G10-05).
    - Going from 1 to 4 local workers on one machine gave no net throughput gain (S030).

- **What to teach (specific points):**
  1. Parallelize last. Before fanning out, one stream needs a dependable judge, a recovery path and a review format people can absorb. Parallelism multiplies the bottleneck you already have, and one person reading every line turns into ceremonial approval (S036).
  2. "Passes alone, fails together." Run every task's tests on the combined code, not only on each branch. Tell later agents about interface changes that have landed: a roughly 130-token message describing the finished change cut interference from 2.50 to 0.04 (S030).
  3. Worktrees isolate files, not behavior. They can share git metadata, credentials, local services and network access (S036).
     - Claude Code agent teams do not put teammates in separate worktrees, so give each one its own set of files (G10-13).
     - Several sessions on one PC still share the disk, the GPU and the model folders (G10-16).
  4. More agents cost more. Claude Code warns that running several sessions or subagents multiplies token usage (G10-13). Agent teams use about 7x the tokens of a standard session when teammates run in plan mode (S016). On small, already-diagnosed tickets, orchestration spent 4-8x the tokens of fixing directly (S030).
  5. Your review time sets the safe number of agents:
     - Budget it.
     - Spend it first on the largest blast radius and the weakest check (S036), and on correctness, safety and user impact (S084).
     - Do not merge what nobody reviewed (S084).
     - More merged PRs is not more value. The Microsoft study measured +24% PRs per engineer with no quality measure (S082).
  6. Ask for evidence before copying a popular setup (reviewer agents, agent swarms, Ralph loops, giant rule files), and measure it on your own tasks one change at a time. The Ralph-loop evidence is one uncontrolled toy-app run (S021).
  7. Prevent collisions on purpose. Partition the work by files or areas. Make sure only one agent can deploy (G10-05, G10-13).

- **You vs the agent (as of 2026-10-12):**
  - Agents can split work, run in parallel, and with dynamic workflows cross-check each other's findings (G10-13). An orchestrating agent can broadcast interface changes and run the full suite on the merge (S030).
  - The human decides whether to fan out at all, from evidence. The human sets file ownership and who may deploy, and keeps review capacity in line with output (S036, S084, G10-05).
  - Bring in someone who knows the system (an owner of the area, a senior reviewer) for red-zone changes: auth, billing, permissions, or anything few people understand. S036 says a human pairs on every step there, whatever the agent count.

- **Currency:** New in 2026.
  - Agent teams are experimental and disabled by default. Agent view is a research preview. Projects is a public beta on Pro and Max (G10-13).
  - Research on parallel-agent interference is weeks old: arXiv 2609.25396, summarized 2026-10-11 (S030).

- **Outdated framings to avoid:**
  - "More agents means more done" (S036, S084, S030).
  - "No merge conflict means the merge is safe" (S030).
  - "Add a reviewer agent to catch mistakes" and "a swarm beats one agent" (S021).
  - "Approving every PR means you reviewed them" (S036).

- **Questions it answers:**
  - Should I run multiple agents at once?
  - How many agents can I manage?
  - Can I run several agents on the same repo at once?
  - Both branches passed. Why is main broken?
  - Should I use multiple agents that review each other?
  - Do Ralph loops work?

  Batch-reader records from S030, S036, S084 and S021.

- **Show it for real:**
  - Two git worktrees and two agents: one changes a function's parameters, the other adds a new caller. Each branch's tests pass and git merges cleanly. Run the suite on the merged main and watch it fail (S030 describes the mechanism).
  - Run `claude agents` to show agent view listing several background sessions and which ones need you. Then show `/usage` to see the token cost of parallel work (G10-12, G10-13, S016).

- **Priority:** should.
  - Evidence: 4 items from 4 batches plus G10-05 and G10-13, all from 2026-07 or later.
  - Severity is medium. The damage is wasted money and unreviewed merges, unless the parallel agents can deploy (G10-05).

---

### C096 Long runs need stop rules, budgets and checkpoints

- **In one line:** Agents neither stop nor wait well on their own. A 35-hour run produced nothing of value, and "never applied" was logged 13 times without halting anything. Write stop and escalate conditions, a budget, a turn or time limit, and review checkpoints into the plan, and enforce the ones that matter with something outside the model.

- **Why it is a gap:**
  - Ronacher's weekend "software factory" ran for 35 hours until he turned it off:
    - about 75k lines, 79 commits, about 1B tokens and about $1,200 raw API cost;
    - in his words, it "delivered absolutely nothing of value";
    - its own task names drifted from 1, 2, 3 to "8b2c2b2b checkpoint1";
    - he says the model will "continue until it succeeds, even if it burns through an entire subscription".
    (S035, re-opened 2026-10-12)
  - Aaron's wallpaper agents ran for 8.5 hours and $373. The notes said "never applied" thirteen times in a row, and no step said anyone had to stop (S032, re-opened 2026-10-12).
  - Aaron stopped a Sonnet Max session by hand after 8 h 42 min, still tuning. Two headless runs ended their turn while a render ran in the background, and nothing woke them (S017).
  - In AO-032, a 30-minute check-in rule was missed three times (gaps of 43, 68 and 47 minutes), because the lead session only runs when something wakes it. A 90-minute step limit was broken too: 2 h 8 min. Aaron's conclusion: the rule "needs a timer, not a promise" (G10-14).
  - The built-in limits are off by default or easy to misread:
    - `--max-turns` has "No limit by default" (G10-12).
    - `--max-budget-usd` works only in print mode, checks a client-side estimate, and "Spend can pass the cap" (G10-12).
    - Plans with no spend limit show "Unlimited" (S016).

- **What to teach (specific points):**
  1. Size the task so it ends in something checkable. Shorter runs left "imperfect but still digestible" software; the 35-hour run did not (S035). Very large work is split into issues, one agent per issue (S003). Big rebuilds go through screen-sized checkpoints (S036).
  2. Write stop and escalate conditions into the plan, not only success steps. For example: "if the target app can't be launched, halt and notify me". A status word in a log is not an alarm unless the plan says what happens when it appears (S032).
  3. Set the run's limits before it starts:
     - a dollar cap (`--max-budget-usd`, with headroom, because spend can overshoot);
     - a turn cap (`--max-turns`);
     - a spend limit on the plan instead of "Unlimited";
     - per-run caps where the platform has them (Zapier: 10 activities on Free, 40 on paid, then the agent pauses and asks).
     (G10-12, S016, S019)
  4. A goal loop stops only when its evaluator says so:
     - Claude Code's `/goal` keeps starting turns until a small model judges the condition met or impossible.
     - That evaluator only reads the conversation. It does not run commands or read files.
     - Write one measurable end state with a stated check (for example "`npm test` exits 0"), plus a clause like "or stop after 20 turns".
     (G10-11)
  5. Rules about time need a clock: a timer, hook or scheduler, not an instruction the model must remember (G10-14). The harness has guards against runaway loops, but they are caps, not judgment:
     - `/goal` stops after several turns with no tool use (G10-11).
     - Claude Code ignores the ninth consecutive Stop-block, and Cursor defaults to five automatic follow-ups. Keep a check outside the hook (S030).
     - Fixed-interval `/loop` tasks expire after 7 days (G10-10).
  6. Plan for the opposite failure as well, where the agent waits forever:
     - a headless run that ends its turn while waiting on background work (S017);
     - a Desktop task in Manual mode that stalls on a permission prompt until you return (G10-09);
     - a goal that pauses on a usage limit (G10-11).
     Give the run a way to be woken or resumed. Aaron's launcher resumes a session when no output file exists (S017).
  7. Keep a "rejected" column: failed attempts logged with their reasons, so they are reviewed instead of shipped. Write every false "done" you catch back into the brief and the gates (S032, S030).
  8. Look at intermediate results. The agent will keep going and will not judge that the run has gone off the rails (S035).

- **You vs the agent (as of 2026-10-12):**
  - The agent keeps working, keeps its own notes and spawns subagents (S035). It reports progress, not budget (S017). It can check a stated condition at each step (G10-11).
  - The human sizes the task and writes the stop, escalate and budget rules before launch. The human makes sure time rules have a real timer, checks in on long runs, and decides when to kill a run (S032, S017, G10-14).
  - Bring in an expert when you cannot write a measurable end state for the work. Without one, neither a goal evaluator nor you can tell done from drifting (G10-11, S035).

- **Currency:** New in 2026.
  - Ronacher says newer models "keep going" where earlier ones stopped (S035).
  - The loop and stop tools are changing release by release: `/goal` check-ins were uncapped before v2.1.246, and cap enforcement for `--max-budget-usd` needs v2.1.217 or later (G10-11, G10-12).

- **Outdated framings to avoid:**
  - "The longer the agent runs on its own, the more it gets done" (S035).
  - "A newer, more persistent model needs less supervision" (S035).
  - "The agent will stop when it is finished" (S017).
  - "The agent will warn me before it spends too much" (S017, S016).
  - "Logging the problem is enough" (S032).
  - "Let it run overnight and check in the morning" (S032).
  - "Tell it to check in every 30 minutes" (G10-14).

- **Questions it answers:**
  - Can I just let the agent run overnight?
  - How big a task should I give an agent at once?
  - How do I put a dollar cap on a run?
  - Why did my agent stop halfway?
  - How do I stop an overnight run from wasting hours on a broken setup?
  - Why did the agent produce so much code that doesn't do anything?

  Batch-reader records from S035, S017, S032 and S019.

- **Show it for real:**
  - Run `claude -p --max-turns 3 --max-budget-usd 0.50 "..."` and show it exiting at the limit (G10-12).
  - Set `/goal all tests in test/auth pass, or stop after 20 turns`, then run `/goal` to show turns, token spend and the evaluator's last reason (G10-11).
  - Open a long run's own notes or task file where the numbering drifts (1, 2, 5a, 8b2c...) next to a commit count that rises while the feature list does not change (S035).

- **Priority:** must.
  - Evidence: 3 items from 3 batches, all rated high severity, plus G10-11, G10-12 and G10-14.
  - Four dated 2026 incidents with measured cost or time (S035, S032, S017, G10-14).
  - Directly tied to money and wasted nights.

---

### C097 Commands run as you: read the literal command before anything destructive

- **In one line:** A shell command an agent runs has your full permissions on every drive you can reach. One quoting bug turned "delete this folder" into deleting a whole drive, and shell deletes skip the Recycle Bin. Read the exact command and target path before approving anything destructive, keep destructive commands behind manual approval, and stop writing to the drive if something is lost.

- **Why it is a gap:**
  - Cursor staff, after an agent's `rd /s /q` wiped a user's D: drive in about 105 seconds on 2026-10-09: on Windows, terminal commands "don't run in a sandbox, so your confirmation is the main safeguard". File-Deletion Protection covers only the agent's own delete tool, not `rd` or `rmdir` (S063, re-opened today).
  - The same thread links reports from 2026-06-19 (C:\ wiped, Windows reinstalled), 2026-07-29, 2026-08-29, 2026-09-18 and 2026-09-19 (S063).
    - 2026-07-29: a trailing backslash before a closing quote, through `cmd /c`, caused about 210,201 file deletions in about 40 seconds. The agent reported a failed cleanup even though its stderr listed paths outside the target (G10-01).
    - 2026-08-29: about 80 GB deleted. The command "is automatically executed", meaning no confirmation, and the user reports the data cannot be recovered (G10-02).
  - The user approved the agent's own plan, "follow the recommendation and delete them". The command that ran removed source, `.git`, the published build and both backups (G10-03).
  - People read the stated intent instead of the command. One reply in G10-04 reports an agent that took the question "Can you change this?" as permission.

- **What to teach (specific points):**
  1. A command an agent runs in your terminal runs as you. On Windows in Cursor there is no sandbox, so your approval is the safeguard. Know your tool's run mode (Cursor: Settings > Agents > Approvals & Execution). Staff recommend Ask Every Time, or Allowlist with an empty list (S063, G10-02).
  2. Never allowlist delete commands or shells: `rmdir`, `rd`, `del`, `Remove-Item`, `cmd`. Keep destructive commands behind manual approval, and add hooks that block the risky patterns (G10-01). A regex guard such as `destructive-command-guard.py` blocks variants like `rm -rf /; echo done` that a prose rule may not stop (S021).
  3. Approve the literal command, not the description. Check:
     - the exact target path;
     - any quotes nested inside `cmd /c` or another shell;
     - paths with spaces or non-ASCII characters;
     - a trailing backslash before a closing quote.
     Shell quoting differs between cmd, PowerShell and bash. Staff explained that in PowerShell a backslash does not escape a quote the way it looks (S063, G10-01).
  4. Ask the agent to list the target first and print what it will delete before deleting it (S063, batch item #02). Staff's longer-term fixes point the same way: open the agent on one project folder, not a whole drive, to limit its scope (G10-02). The post's own suggestions are to refuse recursive deletes of volume roots and to abort when output shows paths outside the target (G10-01).
  5. Safety features protect one path each:
     - Cursor's File-Deletion Protection covers the agent's delete tool only (S063).
     - Claude Code's checkpoints do not track `rm`, `mv` or `cp` run through Bash (G10-07).
     The agent can pick the shell over the protected tool without telling you (S063).
  6. Shell deletes (`rd /s /q`, `rmdir /s /q`) do not go to the Recycle Bin (S063, G10-02, G10-03).
  7. The first hour after a wipe:
     - Stop writing to that drive.
     - Run recovery tools (Recuva, PhotoRec, TestDisk) from another drive, and restore to a different drive. On an SSD with TRIM, the chances drop quickly.
     - Look for copies elsewhere: Cursor Local History (only for files edited and saved in Cursor), Windows Previous Versions (only if System Protection was on), a git remote, CI or deploy checkouts, email, other machines.
     (S063, G10-02, G10-03)
  8. The agent must not be the one running more commands on the damaged drive (S063).

- **You vs the agent (as of 2026-10-12):**
  - The agent writes and runs commands. It can check that a path exists and list a folder before deleting. It cannot be trusted to notice its own quoting error before the damage, and it may misreport the result (S063, G10-01).
  - The human chooses the run mode, keeps deletes off the allowlist, reads the literal command and target before approving, and knows the first-hour recovery steps (S063, G10-01, G10-03).
  - If the data matters and your own recovery-tool attempt fails, bring in a professional data-recovery service. The sources only list tools, so this step is the course rule applied: data recovery is something you cannot verify yourself.

- **Currency:** Established. The mechanisms (shell quoting, recursive deletes, the Recycle Bin, TRIM) are old.
  - What is new in 2026 is agents running these commands on their own, and the run of reports from June to October 2026 (S063).
  - Cursor calls the quoting pattern tracked, "no timeline to share" (G10-01). Until a fix ships, the human controls are the only ones.

- **Outdated framings to avoid:**
  - "The agent runs in a sandbox, so it can't hurt my machine." Not on Windows in Cursor (S063).
  - "I turned on delete protection." It covers one tool (S063).
  - "The agent said it would delete one folder, so that's what the command does" (S063, G10-01, G10-03).
  - "Deleted files go to the Recycle Bin" (S063, G10-02).
  - "Rewind will undo it." Not for Bash changes in Claude Code (G10-07).

- **Questions it answers:**
  - How did the AI delete my whole drive when I asked it to delete one folder?
  - Can Cursor or Claude Code delete files outside my project?
  - Is the agent's terminal sandboxed?
  - Why aren't they in the Recycle Bin?
  - The agent deleted my files; can I get them back?

  These are from S063, G10-02 and G10-03, whose titles and opening posts ask exactly this.

- **Show it for real:**
  - In a scratch folder, replace `rd` with `echo` and run a nested-quote command against a path with spaces to print the arguments the command actually receives. No real deletion (the mechanism described in S063 and G10-01).
  - Open Cursor's Approvals & Execution settings next to the File-Deletion Protection setting (S063).
  - In Claude Code, have Claude delete a test file with Bash, then open `/rewind` and show that it cannot be restored (G10-07).

- **Priority:** must.
  - Severity is high: permanent data loss.
  - At least six dated reports from June to October 2026, three of them read today (S063, G10-01, G10-02, G10-03).
  - The taxonomy's one-source flag is resolved.

---

### C098 Undo has limits

- **In one line:** Every undo button covers only part of what an agent can change:
  - A backup the agent's shell can reach, or git with no remote, dies with the project.
  - Platform rollback leaves production databases untouched by default.
  - Editor checkpoints skip shell commands.
  - A sent message or a purchase cannot be recalled.

  Know your rollback path for code, data and live effects before the agent starts.

- **Why it is a gap:**
  - In G10-03 (2026-10-03) one delete took a six-month project's source, its `.git` folder, the publish folder, `_file_backup` and a manual ERP backup zip. All of them were on the same E: drive.
  - "Rollback" sounds like an undo for everything. Two current docs say otherwise:
    - Replit: "By default, rollbacks do not change your database", and the production database "is not performed automatically through this rollback feature" (G10-06).
    - Claude Code checkpoints do not track files changed by Bash, usually do not restore subagent edits, and are "not a replacement for version control" (G10-07).
  - People do not know that hosting keeps previous versions you can roll back to in seconds. Aaron's site was wrong for 8 min 10 s, and the only alarm was him happening to look (S026).
  - Nineteen GB of model files deleted on 2026-09-15 were still missing on 2026-09-26 (G10-16).

- **What to teach (specific points):**
  1. A backup the agent's shell can reach is not a backup. Keep one copy on a different disk or in versioned cloud storage. Before letting an agent loose, push to a remote and confirm with `git remote -v` that the copy exists off the machine (S063, G10-03).
  2. Git with no remote is a single copy. If `.git` is deleted, the history is gone. After a loss, the first recovery step is to look for a remote, CI or deploy checkouts, and other machines (S063, G10-03).
  3. Know what each undo covers:
     - **Claude Code checkpoints:** edits by Claude's file tools only. Not Bash `rm`, `mv` or `cp`. Usually not subagent edits. Not other sessions' edits. Snapshots are removed after about 30 days (G10-07).
     - **Replit checkpoints:** files, conversation, config and agent memory, plus the development database only if you tick it. Never production data (G10-06).
     - **Cursor:** checkpoints, Local History and frequent commits are the recovery toolkit. Set them up before the big change (G10-04).
  4. State outside the code needs its own path back. The production database needs its own point-in-time restore (G10-06). Replit tells you to "Consider the impact on your database and external integrations" before rolling back (G10-06).
  5. Sent messages and purchases are the hardest actions to undo. Require manual approval for them (S069). Anything a routine does through your connectors (a Slack message, a ticket, a PR) is done as you (G10-08).
  6. Rehearse a hosting rollback before you need it:
     - The command can take seconds, for example `npx wrangler rollback <version-id> --name <worker-name>`.
     - Then confirm key pages return 200.
     - Expect friction: `wrangler deployments list` failed because the Worker name in the repo config differed from Cloudflare's, and the history did not mark which deploys came from branches.
     (S026)
  7. Make "what is live" answerable. Each build writes `/version.json` with the commit, the branch, the build time and the newest post. Sessions compare it with what they just pushed (S026).
  8. Commit before large agent changes. Use Plan mode for risky tasks. Review destructive commands before approving them (G10-04).

- **You vs the agent (as of 2026-10-12):**
  - The agent can set up the remote and the push, run a rollback command, verify pages, and build `/version.json`. Those are all verifiable steps (S026, S063).
  - It cannot unsend an email, restore production data through rollback, or recover what its own shell deleted (G10-06, S069, S063).
  - The human confirms that a backup really exists off the machine. The human knows which state lives outside the code (production database, third-party services, messages sent) and approves production rollbacks (S063, G10-06, S026).
  - For a production database with real users, have someone who has done a point-in-time restore on that provider check the restore plan before you need it. The doc sends you to a separate guide for that reason (G10-06).

- **Currency:** Established.
  - The checkpoint and rollback features are 2026 versions and change with releases. For example, Claude Code subagent-edit and symlink handling are documented per version (G10-07).
  - The habit of keeping undo points in every change is current practice (G10-04).

- **Outdated framings to avoid:**
  - "Git is my backup" when there is no remote (S063, G10-03).
  - "I made a backup copy in the project folder" (G10-03).
  - "Checkpoints mean I can always undo the agent" (G10-06, G10-07).
  - "Fix forward by pushing a new commit when production breaks" (S026).

- **Questions it answers:**
  - Is git a backup?
  - Where should I keep backups when using an AI agent?
  - If the agent breaks my app, can I just roll back?
  - Does rollback restore my database?
  - My site broke after a deploy; how do I go back?
  - How do I know which version is live?

  Batch-reader records from S063 and S026, and the G10-04 thread title.

- **Show it for real:**
  - Run `git remote -v` in a project with no remote (empty output) and in one pushed to GitHub (S063).
  - Open a Replit checkpoint's rollback dialog and point at the unticked Database option (G10-06).
  - List Cloudflare Worker deployments, roll back, then open `/version.json` and compare its commit with `git log` (S026).
  - Delete a file via Bash in Claude Code and show that `/rewind` cannot bring it back (G10-07).

- **Priority:** must.
  - Severity is high: unrecoverable loss of data and production state.
  - Two independent incidents (G10-03, S026) and two first-party docs (G10-06, G10-07), all current.

---

### C099 Local, preview and production are different places

- **In one line:** Where something runs decides what it can reach and what it changes:
  - localhost is unreachable from outside;
  - a test webhook URL works only while you watch;
  - a saved workflow is not an active one;
  - an env var typed into a dashboard may never reach the container;
  - a cloud agent sees only committed files on the default branch;
  - a hosting setting can make any branch production.

- **Why it is a gap:**
  - In n8n, using the production URL with the workflow switched to Active fixes "Nine times out of ten" of the "works in test, not in production" posts (S066).
  - Common beginner mistakes:
    - Copying a localhost URL into a cloud service (S066).
    - Typing a value into Portainer's environment panel that never reaches the container (S066, thread 302932).
    - Assuming a branch push is safe because it is "not main". On Aaron's site, Cloudflare's "Builds for non-production branches" ran `npx wrangler deploy`, so a pushed branch replaced the live site within about 40 seconds (S026).
  - A cloud session "starts with a fresh clone of the repository, on the default branch, and nothing else", so it never saw the laptop's rules (S026).
  - Cloud agents declared an OAuth flow working because their tests called the backend directly. "No test ever went through the public URL", so CI was green while production was broken: a Vercel proxy was overwriting the CSP header (G10-05).
  - Beginners use one key everywhere. In v0, the "preview" panel is the Development environment, not Vercel's Preview environment (S045).

- **What to teach (specific points):**
  1. localhost means "this machine only". Stripe, a form service or anything else on the internet cannot call it. You need a tunnel or a real domain.
     - A self-hosted n8n must be told its public URL (`WEBHOOK_URL`), or it keeps showing localhost URLs.
     - A free ngrok subdomain changes on every restart, which breaks every webhook registered with the old one.
     (S066)
  2. Test mode and live mode are different addresses:
     - n8n's `/webhook-test/` listens only while the editor is open and armed.
     - `/webhook/` works only when the workflow is Active. Saving is not activating.
     - Test end to end from the real source system, not the Test button. A source still pointing at an old URL means a webhook nobody calls.
     (S066, S067)
  3. "No execution logged" means the request never arrived (a URL, network or activation problem). Failed executions mean the problem is inside the workflow. That one rule tells you which half to look at (S066).
  4. Verify config inside the running process, not in the settings screen. A dashboard env panel may only fill `${VAR}` in a compose file. A restart keeps the old environment; a redeploy picks up the new one. Check with `docker exec <container> printenv VAR` (S066).
  5. Each environment has its own variables and keys:
     - Vercel and v0 assign each variable to Development, Preview and/or Production, and the v0 preview sees only Development values.
     - Use separate development and production keys, and rotate them.
     (S045)
     - In Claude Code cloud environments, environment variables are visible to anyone who uses the environment. On Pro and Max, store API keys as network secrets instead (G10-08).
  6. Where an agent runs decides what it sees:
     - Cloud sessions and routines clone the repo fresh, start on the default branch, never see uncommitted local files, and can reach only allowed domains (blocked requests fail with 403 `host_not_allowed`) (S026, G10-08).
     - A Desktop scheduled task runs against your working folder as it is, including uncommitted changes (G10-09).
     - A ChatGPT Work cloud container cannot reach your computer's files (S025).
  7. Read your hosting build settings once: the production branch, whether preview builds run, and the build command for each. A preview build should upload a version, not deploy it (`npx wrangler versions upload`). A repo-side guard only protects branches that contain it (S026).
  8. Test where your users are. Run at least one check through the public URL in a real client, not only scripts calling the backend (G10-05).

- **You vs the agent (as of 2026-10-12):**
  - The agent can build the workflow and tell you which URL to use. It can set `WEBHOOK_URL` and a tunnel once you decide, run `printenv`, wire code to read env vars, read hosting config and add a build guard (S066, S045, S026).
  - It cannot see what you pasted into another company's dashboard, settings that exist only in a hosting dashboard, or a request that never arrived (S066, S026).
  - The human owns the provider accounts, signs in, reviews build and deploy settings, creates separate keys, and confirms the outside service has the production URL (S026, S045, S066).
  - For production keys, auth flows and proxy or CDN headers, have someone who knows that platform review the setup when you cannot verify it yourself. The CSP header in G10-05 was invisible to every test the agents ran.

- **Currency:** Established. The mechanisms are old web basics.
  - What changes now is that agents work in more places at once, each with its own view: local, Desktop scheduled, cloud routines, Cursor self-hosted machines (S025, G10-08, G10-09).

- **Outdated framings to avoid:**
  - "It worked in my test, so it's live" (S066).
  - "The URL in my browser is the URL other services use" (S066).
  - "I set the variable, so the app has it" and "Restarting applies my config changes" (S066).
  - "If it works in the preview it works live" (S045).
  - "Pushing to a branch never touches the live site" (S026).
  - "My CLAUDE.md protects every session" (S026).
  - "CI is green, so it works" (G10-05).

- **Questions it answers:**
  - Why does my webhook only work when the editor is open?
  - Why can't Stripe reach my webhook on localhost?
  - Why didn't my automation run overnight?
  - Why isn't my environment variable working?
  - Why does my app work in the v0 preview but not after I publish?
  - Why did pushing a branch change my live website?

  These come from S066 (its title is "Webhook works in test but not in production?") and from batch-reader records for S045 and S026.

- **Show it for real:**
  - In n8n, toggle a Webhook node between its Test and Production URL tabs, flip Active, and `curl` each one. Then open the Executions tab after sending to the wrong URL and the right one (S066).
  - Run `docker exec <container> printenv WEBHOOK_URL` before and after a redeploy (S066).
  - Open the hosting dashboard's build settings and point at the production branch, the non-production builds toggle and the two build commands. Push a test branch and show it appear as a preview URL (S026).

- **Priority:** must.
  - Evidence: 6 items from 3 batches (the most in this group), plus G10-05, G10-08 and G10-09.
  - Some of the most frequent beginner questions.
  - A real production incident in Aaron's own practice (S026).

---

### C100 Green is not success: automations that run but do nothing

- **In one line:**
  - Error alerts catch only runs that throw. An expired token, a renamed field, a filter that matches nothing, or a 200 response with a failure body all finish "successfully", sometimes for weeks.
  - An agent run's green status means only that it did not crash.
  - "Fixed" is not "shipped".

- **Why it is a gap:**
  - The n8n Error Trigger fires "only on unhandled exceptions", and the failures people miss are "exactly the case where nothing throws" (nathan3 in S067, re-opened today). n8n's own docs say the error workflow runs "if an execution fails" (G10-18).
  - Reports from the thread:
    - "27 branches were skipped for weeks while every run still showed green" (Loordhu_Jeyakumar, 2026-10-07, S067).
    - Five workflows were broken and all five were green. One sent `{"":""}` and the endpoint answered 200 (enzosoftware, 2026-09-04, S067).
  - The same pattern holds for coding agents. Claude Code's routines docs say a green run status "does not mean the task in your prompt succeeded", and that task-level failures show only in the transcript (G10-08).
  - Inside one Claude Code session, an agent "died four hours in and I never noticed". Eighty agents started and 79 returned (G10-15).

- **What to teach (specific points):**
  1. A green or "Succeeded" status means only that nothing threw. Define what a successful run produces, and make the run fail loudly when it does not produce it. In n8n, end the path with a Stop and Error node (S067, G10-18).
  2. Know the silent-success patterns, because each one ends green:
     - an IF branch that ends silently;
     - HTTP 200 with `success: false` in the body (check the API's failure field, not the status code);
     - a Set node with "Keep Only Set" that wipes downstream data;
     - a loop that ends early on one bad record;
     - a webhook nobody calls;
     - a dead trigger;
     - an expired OAuth token that fails with no HTTP status;
     - zero items, which can mean a quiet period or a broken condition.
     (S067)
  3. A missing step is not a failed step. In n8n, a node on an IF branch that stops matching "isn't marked skipped. It's not in runData at all". Look for missing keys, not bad statuses (S067).
  4. The error handler itself can be off. An error workflow with no active published version is skipped in silence, leaving only a server log line (S067).
  5. For agent runs, open the run and read what it did. Blocked network requests, missing connector tools and task-level failures appear in the transcript, not in the status dot. You can ask `/schedule why did my nightly review do nothing this morning?` (G10-08). An agent's closing "done" is a claim: in one field record, 24 of 265 claims did not hold when re-verified (S030).
  6. A repeated status word in a log is not an alarm. "Never applied" thirteen times halted nothing (S032).
  7. "Never worked" is different from "stopped working". A monitor that compares runs against their own history "cannot detect defects present from the start" (S067). A pruned run is "not evidence of absence" (S067).
  8. "Fixed does not mean shipped." Fetch the artifact the way the recipient gets it (a download, an import, a deploy) and test that copy (S067).

- **You vs the agent (as of 2026-10-12):**
  - Once you state the expected outcome, the agent can add assertions, failure branches and checks for each pattern. It can read a run's log and explain why it did nothing (S067, G10-08).
  - The human defines what a successful run produces, asks for each silent-success guard, and reads at least the first runs' transcripts or outputs. The human also reviews checks that always fire: in S067, one scanner flagged 58 of 83 templates, a sign the check itself was broken.
  - When the business depends on an automation (billing, customer records), bring in someone who knows the destination system to say what "arrived correctly" means.

- **Currency:** Established for automation tools; the n8n thread runs from 2026-08-21 to 2026-10-08.
  - New in 2026 is the same gap in agent runs: routine status dots, subagents that die silently, and false "done" claims (G10-08, G10-15, S030).

- **Outdated framings to avoid:**
  - "No error alert means it worked" (S067).
  - "Set up an error workflow and you're covered" (S067).
  - "200 OK means it worked" (S067).
  - "The run is green, so the agent did the task" (G10-08).
  - "The orchestrator's summary tells me what happened" (G10-15).
  - "I fixed it, so it's fixed for everyone" (S067).

- **Questions it answers:**
  - My workflow says success but nothing happened. Why?
  - How do I know my automation is actually working?
  - The API returned 200; why didn't anything happen?
  - Why did my routine do nothing this morning?
  - Why is my fix not working for customers?

  The first is S067's own title ("How do you catch workflows that run fine but do nothing?"). The fourth is G10-08's example. The rest are batch-reader records from S067.

- **Show it for real:**
  - Build a two-node n8n workflow with an IF that can never match, run it, and show the green Succeeded status with nothing downstream. Then toggle "Keep Only Set" on a Set node and watch fields disappear while the run stays green (S067).
  - Open a routine's run list on claude.ai/code/routines, then open a green run whose transcript shows a blocked request (G10-08).

- **Priority:** must.
  - Severity is high: failures go undetected for days or weeks, and the client often notices first (S067).
  - The taxonomy's one-source flag is resolved: G10-08 and G10-18 are first-party docs, G10-15 and S032 are first-hand cases.
  - It applies to every automation and agent run the audience will set up.

---

### C101 Check outcomes in layers: run, output and receipt

- **In one line:** Beyond "did it run", check the output (item counts, required fields, types, freshness) and the receipt (proof at the destination). Feed known-answer canaries through the live pipeline.

- **Why it is a gap:**
  - Most builders watch only run status. RomeoApps' three-layer model in S067 separates execution health from outcome health.
  - Builders who add a count check stop there. Nulls, wrong types and silent drops still pass (S067, including thread 307116).
  - The same lesson in coding agents: a receipt written by the runner, not the agent, is what catches stale or partial "tests pass" claims (S030).
  - Anthropic's 2026 Claude Code course has a lesson titled "Trust It: Verifying Unsupervised Runs" (G10-19).

- **What to teach (specific points):**
  1. Check three layers (S067):
     - **Run health:** did it start and end on time, with retries, upstream status and the error path in order?
     - **Output health:** is the item count within the expected window, is the data fresh, are required fields present, does the schema hash match, are there no duplicate keys?
     - **Receipt health:** is there a downstream record ID, an acknowledgement, or an explicit exception entry?
  2. A green run with an unexpected zero is a review item, not a success. Alert on consecutive misses to avoid weekend noise (S067).
  3. Put a gatekeeper right after the main query or write: an IF on the item count that routes to Stop and Error (S067).
  4. Count is necessary but not enough. Count measures cardinality, not correctness. After an upstream rename, rows land with null or wrongly typed fields. Assert required fields are non-null and of the right type, and compare counts before and after each transforming node: a dedupe step dropped a whole dataset while reporting success (S067).
  5. Known-answer canaries catch plausible-but-wrong output. On a schedule, send a flagged test payload through the production path to a harmless destination, and check that the expected result appears within a window. A canary that stops reporting is itself the alert (S067).
  6. For agent work, the receipt comes from the runner, not the agent: the command, exit code, counts, skips and commit SHA. If the SHA is not HEAD, the result is stale. A good receipt also names what was not run (S030).
  7. For a deploy, the receipt is the live site. Check that `/version.json` shows the commit you pushed, that key pages return 200, and that a video answers a range request with 206 (S026).
  8. Human spot-checks are still needed. A believable but wrong value passes every automated layer (S067).

- **You vs the agent (as of 2026-10-12):**
  - The agent implements every layer: count windows, null and type assertions, canary workflows, receipts, version endpoints (S067, S030, S026).
  - Only the human knows the expected count window, the fields the business depends on, what counts as a receipt, and the known answer for a canary input. The agent can wire a canary but cannot write the answer key (S067).
  - When "correct" is a domain judgment (financial figures, medical or legal content), have a domain expert write or check the known answers.

- **Currency:** Established. Monitoring practice from data engineering, applied in 2026 threads (S067).
  - The receipt-from-the-runner idea for agents is new in 2026 (S030).

- **Outdated framings to avoid:**
  - "Monitoring means watching for errors" (S067).
  - "If rows arrived, the data is fine" (S067).
  - "The agent said tests pass" (S030).

- **Questions it answers:**
  - What should I monitor in an automation?
  - How do I know data actually arrived?
  - How do I validate data in n8n?
  - Why are my records arriving with empty fields?
  - How do I test an automation that's already live?
  - What is a canary check?

  Batch-reader records from S067.

- **Show it for real:**
  - Put an IF after an n8n write node that checks the item count and routes failures to Stop and Error, then trigger it with empty input (S067).
  - Post a flagged test payload to the production webhook, show it landing in a test sheet, then break the path and show the alert (S067).

- **Priority:** should.
  - It is the practical fix for C100 and can be taught with it.
  - Evidence: 3 items from one batch plus S030 and S026, all from 2026.
  - Severity is high where data matters, but it is a technique, not a mental-model gap.

---

### C102 Watch from outside and at the destination

- **In one line:** A check inside a workflow cannot see the workflow stop, and a scheduler can skip runs quietly. Use an external heartbeat (a dead man's switch), verify the record where it lands, and read the bytes actually sent at least once.

- **Why it is a gap:**
  - If the schedule trigger dies, an IF check inside the workflow never runs (rodri.galloswork in S067). The thread asks for exactly this: something external such as Healthchecks.io, cron pings or a heartbeat.
  - Schedulers skip runs without an error in any run you would look at:
    - Desktop scheduled tasks skip runs while the computer sleeps (G10-09).
    - A routine whose GitHub connection lapses skips runs for up to 72 hours, then turns itself off (G10-08).
  - The only alarm when Aaron's site went back to August was Aaron happening to look, three minutes after it broke (S026).
  - In an 80-agent session, nothing surfaced the one agent that never returned (G10-15).
  - Sender-side views lie. "The endpoint answered 200. Every node green", but `{"":""}` left the machine (S067). Agents tested the backend directly while the public URL was broken (G10-05).

- **What to teach (specific points):**
  1. A watcher has to live outside what it watches. A dead man's switch such as Healthchecks.io stays silent while pings arrive and alerts when one is missed:
     - "Period" is how often a ping should come.
     - "Grace time" absorbs normal delays.
     - Optional `/start` and `/fail` pings measure run time and report failures.
     (G10-17)
  2. The n8n heartbeat pattern (S067):
     - Each workflow calls a check-in sub-workflow that records last_seen, last_count and last_ok.
     - A table holds each automation's maximum silence and minimum count.
     - A watcher runs every 15 minutes and alerts on silence, a low count or not-ok.
     - The watcher itself pings an external cron service, so a dead instance still alerts.
  3. The outside-in alternative: poll the platform's executions API, and compare each workflow's gaps and error rate with its own baseline (S067).
  4. Check the history for skipped runs, not only failed ones. Desktop's run history shows skipped runs and why: asleep, previous run still going, other tasks running (G10-09). Know your scheduler's quiet failure modes: routines stop after 72 hours without GitHub (G10-08), and `/loop` stops when the session closes (G10-10).
  5. Verify at the destination. The final check should prove the record exists: downstream ID present, business fields non-null, source ID preserved, run ID attached. Reconcile counts and read back. A YouTube upload succeeded, but its hashtags were never applied, unnoticed for weeks (S067).
  6. Read what was actually sent, once, before trusting any check. Point the workflow at a logging server and read the raw request (S067). Test through the public URL in a real client, not only scripts calling the backend (G10-05).
  7. Make the live system answer for itself. Aaron's site now serves `/version.json`, which sessions compare with what they pushed (S026). For agent fleets, read the run records (transcripts, workflow files) rather than the orchestrator's summary. That is how the dead agent and its $22 were found (G10-15).

- **You vs the agent (as of 2026-10-12):**
  - The agent builds the heartbeat, the watcher, the read-backs and the logging-server test, and can poll execution APIs (S067).
  - It cannot notice its own scheduler not firing. From inside, a dead trigger and a quiet day look the same (S067, G10-09).
  - The human decides how long silence is acceptable for each automation and where alerts go. The human looks at the destination with their own eyes at least once (S067).
  - For a system other people depend on, bring in someone who runs production monitoring to pick alert routes and thresholds. Thresholds that are too noisy turn into ignored alerts (S067).

- **Currency:** Established.
  - Dead man's switches and destination reconciliation are long-standing operations practice. Healthchecks.io has run since 2015 (G10-17).
  - New in 2026: agent schedulers with their own quiet skip rules (G10-08, G10-09, G10-10), and multi-agent runs where one worker can die unnoticed (G10-15).

- **Outdated framings to avoid:**
  - "If it breaks, I'll get an error email" (S067).
  - "The node shows the data, so it was sent" (S067).
  - "I scheduled it, so it runs." It is skipped while the computer sleeps or GitHub is disconnected (G10-09, G10-08).

- **Questions it answers:**
  - How do I get alerted if my automation stops running?
  - What is a heartbeat or dead man's switch?
  - How do I see exactly what my workflow sent?
  - Why didn't my scheduled task run?

  Batch-reader records from S067. The last is the scenario G10-09 documents.

- **Show it for real:**
  - Create a Healthchecks.io check and have a workflow ping it. Disable the workflow and show the check go late, then down, after the grace time (G10-17, S067).
  - Point an n8n HTTP Request node at a logging server and compare the body received with what the node panel shows (S067).
  - Open a Desktop scheduled task's history and hover a skipped run to read why (G10-09).

- **Priority:** should.
  - It completes C100 and C101, and can be taught in the same lesson.
  - The taxonomy's one-source flag is resolved with G10-08, G10-09, G10-15, G10-17 and S026.
  - Severity is high for anything other people depend on. Lower for personal automations.

---

## Sources

### S-IDs used (from the taxonomy source index)

S001, S003, S004, S016, S017, S019, S021, S025, S026, S030, S032, S035, S036, S045, S063, S064, S066, S067, S069, S082, S084.
- Titles, authors, dates and URLs are in `taxonomy.md` § Source index.
- Re-opened on 2026-10-12: S032, S035, S063, S067 (pages 1 and 2).
- S080 is listed under C095 in the taxonomy (a "manager of agents" remark), but this file does not use it. The remark was not re-checked.

### New sources read for this group (G10-xx)

All were fetched and read by this writer on 2026-10-12.

| ID | Title | Author | Date | URL |
|---|---|---|---|---|
| G10-01 | [Windows] Agent Shell: rmdir /s with trailing \ before " escapes target and wipes volume root | Aleksey Solodkevich (Aleksey_Nm); staff reply by Mohit (Cursor) | 2026-07-29 (staff reply 2026-07-30) | https://forum.cursor.com/t/166931 |
| G10-02 | Agent wiped D: drive instead of deleting one folder | Mr.Cheng; staff replies by Dean Rie (Cursor) | 2026-08-29 | https://forum.cursor.com/t/169919 |
| G10-03 | Errible: AI out of control, randomly deleting files, 6-month project wiped out (companion read for S063) | shuang_yang; replies by ActionGate, sattyamjjain | 2026-10-03 (replies to 2026-10-05) | https://forum.cursor.com/t/173688 |
| G10-04 | What's the last AI-assisted change that created more recovery work than expected? | Mohan Iyer; replies by Dean Rie, FinDevAI, speaker | 2026-08-12 (replies to 2026-08-16) | https://forum.cursor.com/t/168209 |
| G10-05 | MCP problem en code problem | Jeffrey Barts | 2026-09-26 | https://forum.cursor.com/t/173052 |
| G10-06 | Checkpoints and rollbacks (companion read for S063) | Replit docs | undated (no date on page) | https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks |
| G10-07 | Checkpointing | Anthropic (Claude Code docs) | undated; current docs | https://code.claude.com/docs/en/checkpointing |
| G10-08 | Automate work with routines (research preview) | Anthropic (Claude Code docs) | undated; cites versions up to v2.1.268 and beta header experimental-cc-routine-2026-04-01 | https://code.claude.com/docs/en/routines |
| G10-09 | Schedule recurring tasks in Claude Code Desktop | Anthropic (Claude Code docs) | undated; cites Claude Desktop 1.1.5368 | https://code.claude.com/docs/en/desktop-scheduled-tasks |
| G10-10 | Run prompts on a schedule | Anthropic (Claude Code docs) | undated; cites up to v2.1.248 | https://code.claude.com/docs/en/scheduled-tasks |
| G10-11 | Keep Claude working toward a goal | Anthropic (Claude Code docs) | undated; cites up to v2.1.269 | https://code.claude.com/docs/en/goal |
| G10-12 | CLI reference | Anthropic (Claude Code docs) | undated; cites up to v2.1.290 | https://code.claude.com/docs/en/cli-reference |
| G10-13 | Run agents in parallel | Anthropic (Claude Code docs) | undated; current docs | https://code.claude.com/docs/en/agents |
| G10-14 | AO-032: I told Claude to find the best Opus 5.5 trick on X and do it without me | Aaron Orelup | 2026-10-03 | https://aaronorelup.com/ledger/opus-55-on-x-alone/ |
| G10-15 | AO-014: I had 801 agent transcripts and no way to read them | Aaron Orelup | 2026-09-01 | https://aaronorelup.com/ledger/reading-my-own-agents/ |
| G10-16 | AO-019: An agent confessed to deleting 19 GB I had asked another agent to delete | Aaron Orelup | 2026-09-26 (events 2026-09-15) | https://aaronorelup.com/ledger/the-confession-that-spread/ |
| G10-17 | Healthchecks.io documentation (docs home) | Healthchecks.io | undated (footer © 2015-2026); foundational and current | https://healthchecks.io/docs/ |
| G10-18 | Error handling | n8n Docs | undated | https://docs.n8n.io/flow-logic/error-handling/ |
| G10-19 | Claude Code in Action (course outline) | Anthropic Academy | undated (footer © 2026) | https://anthropic.skilljar.com/claude-code-in-action |

**Notes on the new sources.**
- **Claude Code doc dates.** The docs pages carry no dates. The version numbers they cite place them in late September to early October 2026: the batch notes record v2.1.271 as released 2026-09-14 and v2.1.296 as released 2026-10-09 (S016).
- **G10-14, G10-15 and G10-16** are Aaron's ledger posts, drafted by Claude from his transcripts. The incident facts and measurements are first-hand. The framing is Claude's (see `sweep/aaron.md`).
- **G10-01:** its root-cause analysis is the poster's own. Cursor staff confirmed only that the pattern is known and tracked.
- **Dean Rie** is shown as Cursor staff in G10-02. G10-04 does not label him.
