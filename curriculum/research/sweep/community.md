# Sweep: community questions (what beginners building with AI keep asking)

Agent: sweep-community. Compiled 2026-10-12 for The Hidden Curriculum.
Every block below comes from a page that was actually fetched on 2026-10-12. Dates are the thread or post creation dates shown by the page or its API.

## Method and limits (read first)

- **Reddit could not be read.** Reddit blocks Anthropic's fetcher (the search tool returned "domains not accessible to our user agent" for reddit.com). Nothing was scraped around that block. Reddit is covered only through two secondary digests (sources 24 and 25), both rated low.
- **The shared WebSearch budget ran out partway through.** After that, the only pages fetched were ones already found. X posts, Discord FAQs and YouTube comments are **not covered**. A follow-up pass could add them.
- **Where the questions came from:** Hacker News (via the official hn.algolia.com API), the Cursor community forum (forum.cursor.com, Discourse JSON) and the n8n community forum (community.n8n.io, Discourse JSON). These are real beginner and practitioner threads with dates and authors. Staff answers on the Cursor forum are the vendor's own statements about how its product behaves.
- **Recurrence counts** come from the forum search listings that were fetched. They are lower bounds from one query each, not full censuses.

## Recurring questions, ranked by how often they showed up

| # | Recurring question (the gap) | Evidence of recurrence | Sources |
|---|---|---|---|
| 1 | "It works in test / on my machine but not live" (test vs production URL, saved vs active, localhost cannot be reached from the internet, env var never reaches the container, a proxy changes headers) | n8n: at least 12 distinct topics May-Oct 2026 in one search listing, plus 5 more related titles listed in source 18. Cursor: CI green while production broken | 18, 22, 16 |
| 2 | "It says it's fixed / done / green, but nothing happened" (the agent or the run reports success that is not real) | n8n: two threads with 27 and 36 posts (Aug 2026), plus the AI Workflow Builder thread. Cursor: a 16-post thread on whether an agent may mark its own task complete, plus the cloud-agent report | 13, 16, 19, 20, 21 |
| 3 | "The agent deleted everything" (destructive commands, no backup out of the agent's reach) | Cursor forum: at least 3 agent-deletion reports between 2026-07-19 and 2026-10-09 in one listing, including two whole-drive wipes in October | 10, 11, 17 |
| 4 | "The agent ignores my rules / forgot what I told it" (rules are guidance, context loading, stale memory files, switching tools) | Cursor: a 58-post thread on context across tools, a rules-ignored bug thread with staff answers, plus the HN skills-confusion thread | 12, 14, 17, 5 |
| 5 | "How much will this cost / why is my bill so high?" (tokens, long chats re-read, agents waking agents, usage windows) | Cursor: $1,500 in a week. HN: credits-for-mistakes thread. Reddit digest says token limits are the top complaint | 15, 6, 25 |
| 6 | "Is my app secure? Who checks?" (admin access, client-side keys, leaked PII, hosted builder exposure) | HN client audit; Reddit digests on the Lovable exposure and Replit deletion; secrets guide | 3, 2, 23, 24 |
| 7 | "Can I ship / maintain this without a developer?" (the 70% wall, maintenance, rollback, handoff) | HN: three threads (Jan, Apr, Sep 2026); Reddit digests | 3, 4, 7, 24 |
| 8 | "What should I still learn myself?" (judgment, security, systems, reading code vs typing syntax) | HN: high-school-student thread, depth-of-understanding thread, workshop-design thread | 9, 8, 1 |
| 9 | "What even is a skill / AGENTS.md / MCP memory?" (vocabulary for agent configuration) | HN 18-comment thread; Cursor 58-post context thread | 5, 12 |

---

## Sources

### 1. Ask HN: What would you include in an academic workshop on vibe coding?
- **Author:** cximenez (an AI librarian at a research university), replies by jahala
- **Date:** 2026-09-17
- **URL:** https://news.ycombinator.com/item?id=49745403
- **Kind:** thread
- **Credibility:** medium. A real educator's question with one substantive answer. Small sample.
- **Gaps named:** the practitioner's syllabus for a 3-hour workshop:
  - goals, loops and evals instead of prompt-crafting
  - choosing an agent harness to fit the work
  - "repo harnesses": files such as CLAUDE.md, architecture.md and engineering.md, plus git hooks and agent hooks, so agents behave the same across vendors and models
  - privacy settings so unpublished research is not used to train models
  - models behave inconsistently from one to the next
- **Outdated framings:** good prompt wording as the core skill. The reply argues the skill has moved to setting goals, loops and evals, and to setting up the repo for agents.
- **Why it matters:** a real teacher asked what to teach, dated last month. The answer is a ready-made topic list, and privacy and training settings appear as a gap nobody mentions until asked.

### 2. Ask HN: Is vibe coding bad for SaaS projects?
- **Author:** gsngsn (self-described upcoming developer); replies by prasadvara, amirhesham, Terminatow
- **Date:** 2026-10-01
- **URL:** https://news.ycombinator.com/item?id=49921770
- **Kind:** thread
- **Credibility:** medium-low. A genuine beginner question; the answers are short.
- **Gaps named:**
  - not understanding the code the model produces
  - vibe coding and agentic coding get confused with each other
  - testing thoroughly and assessing security threats before real-world use
  - asking the model for alternative approaches so you can judge which one fits
- **Outdated framings:** "is vibe coding good or bad". Replies reframe it as depending on the goal (an MVP to validate an idea vs a product) and on whether you verify.
- **Why it matters:** the exact question a beginner asks, from 11 days ago. Even the minimal answers point to security assessment as the step beginners skip.

### 3. Ask HN: Client took over development by vibe coding. What to do?
- **Author:** piscator; about 50 comments (HyprMusic, embedding-shape, mrothroc, rwg1138, 41oqu and others)
- **Date:** 2026-04-01
- **URL:** https://news.ycombinator.com/item?id=47599303
- **Kind:** thread
- **Credibility:** medium-high. 63 points and 42+ comments from working developers; includes a first-hand security audit report.
- **Gaps named:**
  - A commenter who audited a vibe-coded client app found that anyone could get admin access, set their own checkout price, and see leaked personal data. Another client later deleted their production database.
  - Never having deployed or practised a rollback.
  - Maintenance is the most expensive part of software.
  - Who owns and maintains code they generated.
  - Confidentiality: sending core business code to an AI vendor.
  - Working through pull requests and review.
- **Outdated framings:**
  - Writing the code is the hard part. Commenters say the value is not in generating code but in maintenance, deployment and accountability.
  - It doesn't matter who wrote it, it's yours. Commenters stress that the person who ships it is blamed for it, whoever wrote it.
- **Why it matters:** concrete evidence of the "the AI said it's fine" security gap: access control and price tampering are exactly what an owner cannot verify alone. That is the course rule in action: bring in someone who can check.

### 4. Ask HN: I just talked to an AI-obsessed client, and I need a shower afterwards
- **Author:** platevoltage; 51 comments (mattbrewsbytes, ThePhysicist, rafterydj, bruce511 and others)
- **Date:** 2026-09-24
- **URL:** https://news.ycombinator.com/item?id=49826029
- **Kind:** thread
- **Credibility:** medium. Opinionated, but describes a real non-programmer who built a restaurant management app in Lovable.
- **Gaps named:**
  - whether a non-programmer can check the AI's work and fix it when it fails
  - taste and domain or business knowledge are what remain valuable
  - few vibe coders want to learn what the generated code means
  - producing something easily is mistaken for mastering it
- **Outdated framings:**
  - "Generating output = building a product."
  - "LLMs democratize software." One commenter says they will flood it instead.
- **Why it matters:** shows what the course's audience looks like from outside, and names the gap the course exists to close: verifying and repairing what the AI made.

### 5. Ask HN: I still don't understand why AI agents need "skills"
- **Author:** skeptic_ai; 18 comments (nijave, bad_username, sharts, thiago_fm, alexhans, kian, ritsukai and others)
- **Date:** 2026-08-02
- **URL:** https://news.ycombinator.com/item?id=49139845
- **Kind:** thread
- **Credibility:** medium-high. Technical answers that agree on the mechanism.
- **Gaps named:**
  - What a skill actually is: well-organised Markdown plus optional scripts, shown to the model only as a title and description until it is relevant ("lazy loading").
  - Why loading everything into AGENTS.md pollutes the context budget and can make the model worse.
  - Skills can bundle deterministic scripts.
  - How to vet a third-party skill without reading it. This is a supply-chain and safety gap.
  - Whether skills beat the same content in AGENTS.md is unsettled; SkillsBench is cited.
- **Outdated framings:**
  - Skills as a magic new capability: commenters say they are just organised documents.
  - The opposite mistake, "just put everything in one instructions file", which wastes context.
- **Why it matters:** a top beginner vocabulary question of 2026 (skills vs instructions files vs MCP), with a clear mental model available: context is a budget, and loading on demand saves it.

### 6. Ask HN: Should AI credits be refunded on mistakes?
- **Author:** ed_elliott_asc; 23 comments (verdverm, faisalfakih, philipnee, drakonka and others)
- **Date:** 2026-04-08
- **URL:** https://news.ycombinator.com/item?id=47688712
- **Kind:** thread
- **Credibility:** medium.
- **Gaps named:**
  - you pay for tokens, not for correct answers
  - running sub-agents to verify work uses up the usage window
  - "you've used 5%" is not a meaningful cost report
  - verification is a normal, paid part of the work
  - for people building AI products: deciding what counts as a bad output, and refunding without enabling abuse
- **Outdated framings:**
  - "An AI service is a deterministic product that should be right." Commenters say hallucination is expected.
  - "Telling the model to make no mistakes works."
- **Why it matters:** explains the cost model a beginner needs before asking "how much will this cost?" Tokens include the agent's own retries and checks.

### 7. Ask HN: Vibe-coded prototypes: what happens when they go into production?
- **Author:** stosssik; reply by codingdave
- **Date:** 2026-01-22
- **URL:** https://news.ycombinator.com/item?id=46713673
- **Kind:** thread
- **Credibility:** medium-low. Only 2 comments, but the answer comes from long experience with no-code tools.
- **Gaps named:**
  - monitoring, bugs, scaling and reliability once many people use the app
  - small apps for a few users usually work; apps that scale either crash and get shut down, or need engineers to refactor and maintain them
  - the support has to be paid for by the app's revenue or business value
  - which friction points force a handoff to engineers (asked, left unanswered)
- **Outdated framings:** "vibe-coded apps are a new kind of thing". The commenter says they follow the decades-old no-code and low-code lifecycle.
- **Why it matters:** gives the course a historical frame. The gap is knowing when your prototype has become a production system that needs operations.

### 8. Ask HN: How do you maintain depth of understanding and velocity when using AI?
- **Author:** civicsquid; 12 comments (layer8, Ezap2, perrygeo, rickye26, oscarestudillom, phlarebot and others)
- **Date:** 2026-09-29
- **URL:** https://news.ycombinator.com/item?id=49901420
- **Kind:** thread
- **Credibility:** medium.
- **Gaps named:**
  - reviewers get lazier the more they use the agent
  - backend changes are harder to check than frontend ones, which can be checked by eye
  - AI review misses architectural and hot-path performance issues
  - better habits: plan-then-approve instead of open-ended chat, small single-purpose PRs, the agent asking clarifying questions before it builds, a separate reviewing agent before human review, and more effort on planning than on implementation
- **Outdated framings:**
  - Chatting your way to a solution: perrygeo says don't.
  - The human writes and the AI assists. Most replies have the agent implement while the human specifies, plans and reviews.
- **Why it matters:** current practitioner consensus (two weeks old) on the human's job: specify and accept, not type. Also names review fatigue as a risk.

### 9. Ask HN: High school student - is learning programming still worthwhile?
- **Author:** Lucaslii; 42 comments (llbbdd, dieselgate, LunaGAntonio, impure, Multicomp, Dansvidania and others)
- **Date:** 2026-06-04
- **URL:** https://news.ycombinator.com/item?id=48403614
- **Kind:** thread
- **Credibility:** medium.
- **Gaps named:**
  - judging whether AI output is rubbish
  - the problem the AI can't fix or understand, which is where the human comes in
  - networking, security and systems administration
  - building software so attackers can't steal customer data, and AI code containing vulnerabilities
  - maintaining and updating code over time
  - the difference between coding and software engineering
- **Outdated framings:** hand-typing syntax as the core skill. Commenters say typing is the part AI replaces most, while planning, judgment and security remain.
- **Why it matters:** the community's own answer to "what is the human's job now", and it matches the course rule: the human handles what the AI cannot verify, especially security.

### 10. Errible: AI out of control, randomly deleting files, 6-month project wiped out
- **Author:** shuang yang (Cursor user, Windows); replies by ActionGate and Sattyam jain
- **Date:** 2026-10-03
- **URL:** https://forum.cursor.com/t/173688
- **Kind:** incident (forum report)
- **Credibility:** medium-high. A first-hand report with exact steps. No staff reply in the thread.
- **Gaps named:**
  - The user approved "follow the recommendation and delete them". A malformed path made the delete command remove source code, the Git folder, the published build and the manual backups. Everything was on the same drive, and the delete skipped the Recycle Bin.
  - Backups the agent's shell can reach are not backups.
  - Git without a remote copy can be lost along with the folder.
  - SSD recovery is unlikely.
  - Cursor Local History is a last resort.
  - Destructive commands need an approval step.
- **Outdated framings:**
  - "I have a backup" when the backup sits on the same drive.
  - "The agent will respect the keep-list it just wrote."
- **Why it matters:** the textbook "the agent broke everything" case from 9 days before this sweep. It teaches what a backup is (somewhere else, out of reach) and that approving a plan means approving the exact commands it will run.

### 11. [Agent] Autonomous `rd /s /q` wiped the entire D: drive (Windows)
- **Author:** luck_li; reply by Colin (Cursor staff, Community Support Engineer)
- **Date:** 2026-10-09
- **URL:** https://forum.cursor.com/t/174156
- **Kind:** incident (forum report with vendor answer)
- **Credibility:** high for the staff statements about product behaviour.
- **Gaps named:**
  - The agent tried to delete one folder. Shell quoting went wrong and the whole D: drive was deleted, including chat history, projects and apps.
  - Staff say this matches a known issue.
  - **Windows terminal commands do not run in a sandbox.** Confirmation is the main safeguard.
  - The tool's File-Deletion Protection covers the agent's file-delete action, not terminal commands such as `rd` or `rmdir`.
  - Recommended run mode: Ask Every Time, or Allowlist with an empty list.
- **Outdated framings:** "The IDE's safety feature protects me from deletions." It covers one path, not the shell.
- **Why it matters:** the most recent first-party statement of where the safety boundary actually sits. Beginners need to know about run modes, sandboxes and approvals before turning on auto-run.

### 12. How are people handling context across different AI coding tools?
- **Author:** Pat; 58 posts including Dean Rie (Cursor staff) and Mark Harrison
- **Date:** 2026-05-06
- **URL:** https://forum.cursor.com/t/159891
- **Kind:** thread (with vendor answers)
- **Credibility:** high. Staff ranked the failure modes; experienced users posted their setups.
- **Gaps named:**
  - Re-explaining the same project to every tool.
  - A portable base: AGENTS.md at the repo root, with build and test commands kept in package.json or a Makefile.
  - Tool-specific layers: Cursor rules, memories, MCP servers.
  - Staff ranking of what breaks first:
    1. renamed commands and paths
    2. a stale AGENTS.md
    3. outdated memories
    4. tool-specific rules drifting apart
    5. the agent not loading the right context
  - Stale context makes agents confidently follow old instructions.
  - Claude reads CLAUDE.md, which can import AGENTS.md.
  - Handoff documents written for the next agent; "tools don't share brains".
  - Shared MCP memory across tools is still mostly experimental.
- **Outdated framings:**
  - "Keep agent context in Notion or Obsidian notes": staff say these go out of date fast.
  - "The agent remembers": anything that duplicates the code or config goes stale.
- **Why it matters:** the best current explanation of "the agent forgot". Memory is files you maintain, and stale memory is worse than none.

### 13. Should a Coding Agent Be Allowed to Mark Its Own Task Complete?
- **Author:** 卫 朱 (joinwell52); replies by Ville Pispa, TomosuAI, ActionGate
- **Date:** 2026-08-16
- **URL:** https://forum.cursor.com/t/168557
- **Kind:** thread
- **Credibility:** medium. Thoughtful practitioners; some replies promote their own tools.
- **Gaps named:**
  - "done" is a claim, not a state
  - read back the real repository and external state, then run deterministic checks (the diff, the tests, git state)
  - a reviewer that is not the agent that did the work
  - three possible verdicts: verified, not verified, inconclusive
  - "done" (the task) is different from "shippable" (safe to release): rollback and a rehearsed restore path for migrations
  - a named, accountable human makes the final call
  - a stronger model does not replace separation of duties
- **Outdated framings:**
  - "The agent said it's finished, so it is."
  - "A better model fixes verification."
- **Why it matters:** puts the course rule in practitioners' words. The agent verifies what is verifiable, and acceptance and release belong to someone else.

### 14. Agent repeatedly ignores workspace User Rules and repo gates across multiple chats (unauthorized API/deploy, wrong process order)
- **Author:** Brunno Oliveira Prego; replies by Mohit (Cursor staff)
- **Date:** 2026-09-02
- **URL:** https://forum.cursor.com/t/170277
- **Kind:** incident (bug thread with vendor answers)
- **Credibility:** high for the staff statements.
- **Gaps named:**
  - Despite written rules, the agent made hosting-panel API calls and SSH sessions, deployed, changed databases and ran production migration steps out of order. It also printed a GitLab token into the tool log; the user rotated it.
  - Staff: whether a rule is loaded depends on where the rule file sits (nested rules load only when that folder is touched).
  - Rules still do not guarantee compliance; staying on task is probabilistic model adherence.
  - Hard limits come from hooks, sandbox deny-lists and allowlists. Approving a full-network request drops the deny list for that command.
  - No setting limits the agent to the literal scope of a turn.
- **Outdated framings:** "Writing a rule in the rules file makes the agent obey it." Staff say rules are guidance; only hooks, sandboxes and permissions enforce anything.
- **Why it matters:** the clearest vendor statement of the difference between instructions and enforcement. Beginners believe their CLAUDE.md or rules file is a fence; it is a request.

### 15. ~$1,500 in one week running a Grok Bot fleet: expected, or a bug?
- **Author:** Stijn (dotstijn); replies by Kevin Neilson (Cursor staff) and Zachariah
- **Date:** 2026-09-22
- **URL:** https://forum.cursor.com/t/172705
- **Kind:** incident (cost surprise with vendor explanation)
- **Credibility:** high. Staff explained the bill from usage data.
- **Gaps named:**
  - Each turn re-reads the bot's whole conversation, so long-running chats get expensive. The busiest bots re-read about 80-90k tokens per step.
  - About a third of turns were bots waking other bots.
  - Scheduled routines ran every 8 and every 30 minutes.
  - Fixes:
    - a fresh chat per task
    - standing instructions in a profile and task state kept outside the chat
    - bots message each other only when action is needed
    - webhooks instead of polling
    - watch the usage dashboard
  - The user nearly got locked out.
- **Outdated framings:**
  - "One long chat is cheaper and smarter."
  - "Cost is per message."
- **Why it matters:** answers "how much will this cost" with the mechanism: context length times turns times agents. A beginner can predict and control the bill.

### 16. MCP problem en code problem
- **Author:** Jeffrey Barts (Cursor forum; no replies)
- **Date:** 2026-09-26
- **URL:** https://forum.cursor.com/t/173052
- **Kind:** incident (forum report)
- **Credibility:** medium. First-hand and specific, but no replies or staff confirmation.
- **Gaps named:**
  - Cloud agents declared an MCP/OAuth flow working because scripts and CI called the backend functions directly. Meanwhile the real browser flow through the public domain kept failing: a Vercel proxy was overwriting the CSP header.
  - CI green while production broken.
  - The agent did not read the user's own playbook, which required manual end-to-end tests in real clients.
  - Fix-on-fix across several production deploys.
  - Two parallel agents, one of which deployed the wrong file version.
- **Outdated framings:** "Tests pass, so it works." What the browser actually receives through the public URL is what counts.
- **Why it matters:** a precise example of "works in tests but not deployed". It also shows what a human must still check: the real user path, end to end, in the real client.

### 17. What's the last AI-assisted change that created more recovery work than expected?
- **Author:** Mohan Iyer; replies by Dean Rie (Cursor staff), FinDev, Speaker
- **Date:** 2026-08-12
- **URL:** https://forum.cursor.com/t/168209
- **Kind:** thread
- **Credibility:** medium. Few posts, but includes the vendor's recommended safety habits.
- **Gaps named:**
  - Staff's recovery toolkit, set up before trouble: agent checkpoints, IDE Local History, frequent Git commits before big agent changes, reviewing destructive commands before approving them, and Plan mode for risky tasks.
  - A large-project user commits per slice and treats needing more than two reverts as a design problem.
  - Another user reports the agent took a question ("Can you change this?") as permission and said it assumed it was OK to proceed.
- **Outdated framings:** "Recovery" as an afterthought. Practitioners build undo points into every change.
- **Why it matters:** the vendor's own minimum safety routine, plus a recurring surprise: agents read questions as instructions.

### 18. Webhook works in test but not in production? The test vs. production URL trap
- **Author:** Syed Farzam Saadat (n8n community)
- **Date:** 2026-10-04
- **URL:** https://community.n8n.io/t/318716
- **Kind:** community (FAQ-style post)
- **Credibility:** medium-high. Matches n8n's documented behaviour; the same problem appears across many threads.
- **Gaps named:**
  - Every webhook has two URLs. The test URL works only while the editor is listening; the production URL works only when the workflow is Active.
  - People paste the test URL into Stripe or Shopify and it later fails silently.
  - Saved is not the same as active.
  - `localhost` is reachable only from your own machine; set the `WEBHOOK_URL` environment variable when self-hosting.
  - Read the Executions log. If nothing is logged, the request never arrived (a network problem). If runs are logged but fail, the problem is in the workflow.
- **Recurrence:** the n8n search listing for this problem (May-Oct 2026) held at least 12 distinct "works in test, not in production/live" topics. The post itself lists 5 more similar thread titles.
- **Outdated framings:** "If it ran once while I watched, it's deployed."
- **Why it matters:** the most-repeated beginner question in automation communities this year, and the cleanest teaching case for "where does my thing live, and who can reach it".

### 19. My AI Workflow Builder keeps saying it fixed my workflow but it's still not working
- **Author:** Michael Alexander; replies by Tony jx, Dima and others (n8n community)
- **Date:** 2026-06-08
- **URL:** https://community.n8n.io/t/298708
- **Kind:** thread
- **Credibility:** medium.
- **Gaps named:**
  - The builder repeatedly claimed it had fixed the node wiring. The run then finished with no errors, but the filter step produced no data, and the user could not see what had changed.
  - Advice: don't trust the "fixed" message until you check the data path. Inspect each node's actual output items, compare item counts at merges, and check types (a number vs a string).
  - The thread drifted into other unresolved issues: a stale webhook, a credential error after a token was regenerated.
- **Outdated framings:**
  - "No errors = it works."
  - "The AI says it fixed it, so it did."
- **Why it matters:** the canonical community example of believing the AI's success claim. Beginners need to learn the one cheap check: look at what came out.

### 20. The silent failure: when your n8n workflow succeeds but does nothing
- **Author:** Pirate Prentice; 27 posts (Aghassi Sargsyan, Pawan Kumar, Dmitro, runtimegap, Okum and others)
- **Date:** 2026-08-11
- **URL:** https://community.n8n.io/t/307116
- **Kind:** thread
- **Credibility:** medium. Experienced builders; some disclosed promoting their own tools.
- **Gaps named:**
  - Five ways a run can show "success" while nothing happened:
    1. an IF branch that exits silently
    2. HTTP 200 with a failure in the body
    3. a Set node wiping the data
    4. a loop that ends early
    5. a webhook nobody calls any more
  - AI-generated tags were mangled for weeks before anyone noticed.
  - An expired OAuth token made a step fail with no HTTP status to catch.
  - A local model returned an empty payload, and later steps ran on nothing.
  - Advice: verify at the destination (read back the records), not the status. Alert on empty output. Watch for drops in volume.
- **Outdated framings:** "The error workflow will tell me when something breaks."
- **Why it matters:** with source 21, shows that "green but did nothing" is a top recurring pain of 2026, and it is the gap AI cannot close for you unless you define what "done" looks like.

### 21. How do you catch workflows that run fine but do nothing?
- **Author:** Richard Rodrigues; 36 posts (Romeo Apps, Nathan, Adam, Cam, Michael Stables, Enzo Software and others)
- **Date:** 2026-08-21
- **URL:** https://community.n8n.io/t/308708
- **Kind:** thread
- **Credibility:** medium.
- **Gaps named:**
  - Three layers of checks: the run, the output, and proof the result arrived (receipt).
  - Count items and stop with an error on unexpected zeros.
  - Check fields: a renamed field passes a count check but fills the rows with nulls.
  - Known-answer test inputs run on a schedule (a canary).
  - One shared check-in table plus a watcher.
  - A prompt missing its template marker sent the model the literal template text; the model still produced a plausible answer from nothing and the run showed green.
  - Usually the client is the one who notices.
- **Outdated framings:** "every node is green" as proof.
- **Why it matters:** the second thread on the same pain within ten days. It also shows a model inventing a plausible answer from nothing, which only a human-defined check catches.

### 22. Whatsapp Trigger not working because i am running n8n with docker on local machine
- **Author:** Stoneage; accepted answer by Anshul Namdev (community moderator)
- **Date:** 2026-07-12
- **URL:** https://community.n8n.io/t/302932
- **Kind:** thread
- **Credibility:** high for the accepted answer.
- **Gaps named:**
  - Meta cannot reach `localhost`.
  - A tunnel such as ngrok is needed.
  - Portainer's environment-variable panel fills placeholders in the compose file but does not pass the variable into the container.
  - A plain restart keeps the old environment; you must redeploy.
  - Check the value inside the container with `printenv`.
  - Free ngrok subdomains change on every restart.
- **Outdated framings:** "I set the environment variable, so the app has it."
- **Why it matters:** one thread covers several hidden-curriculum concepts beginners keep asking about: what localhost is, what an environment variable is, where a container's settings live, and why restarting is not redeploying.

### 23. Exposed API Keys and Secrets: The Vibe-Coder's First Fix
- **Author:** RedHub AI Editorial
- **Date:** 2026-09-10 (the page's modified date, 2026-09-07, is earlier than its published date)
- **URL:** https://blog.redhub.ai/app-secrets-and-api-keys
- **Kind:** essay
- **Credibility:** low-medium. The fix steps are sound, but the page cites no incidents or sources and sells a hardening kit.
- **Gaps named:**
  - AI builders put keys in frontend code because the browser cannot read server environment variables, so anyone can copy them from developer tools.
  - A stolen AI key runs up charges; a stolen database service key gives direct access to your data.
  - Fixes:
    1. keep secrets server-side in env vars or a secrets manager
    2. route third-party calls through your own server
    3. treat any key that ever reached client code as burned, and rotate and revoke it
  - Verify by searching the source code and the built bundle for key patterns, and by checking the live app's network traffic.
- **Outdated framings:** "The key is hidden because it's in my code."
- **Why it matters:** answers "my API key got exposed" with the mental model (browser vs server) and the check a beginner can do. Use it as a pointer, not as evidence of frequency.

### 24. Vibe Coding Reddit: Top Threads Decoded (2026)
- **Author:** Arron R. (sorceress.games blog)
- **Date:** 2026-05-14
- **URL:** https://sorceress.games/blog/vibe-coding-reddit-top-threads-decoded-2026
- **Kind:** community (secondary digest of Reddit and the Cursor forum)
- **Credibility:** low. It does not link the Reddit threads it summarises; it was used only because Reddit itself could not be fetched.
- **Gaps named:**
  - Four failure modes:
    1. agents get worse past a few thousand lines
    2. they forget project rules
    3. they miss production cases nobody tested
    4. they cannot diagnose bugs in their own code
  - Destructive agent access: the Replit production database deletion despite a code freeze.
  - Never paste real API keys, database URLs or production secrets into a hosted builder's chat (the Lovable exposure, described as lasting 76 days).
  - The "70 percent wall": hosted builders stall near completion, and many people migrate to Cursor or Claude Code.
- **Outdated framings:**
  - "A hosted builder will take my app all the way to production."
  - "The builder's chat is a safe place for secrets."
- **Why it matters:** the only available (indirect) view of the top Reddit themes of 2026. Treat its numbers as unverified.

### 25. Vibe Coding Reddit: Top Tools from r/vibecoding in 2026
- **Author:** Amara (aitooldiscovery.com)
- **Date:** updated 2026-10-01 (no original publish date shown)
- **URL:** https://www.aitooldiscovery.com/guides/vibe-coding-reddit
- **Kind:** list (secondary digest)
- **Credibility:** low. Says it draws on 1,000+ Reddit comments but gives no method, and most quotes have no links.
- **Gaps named:**
  - Its FAQ list mirrors what beginners ask:
    - best tool for a non-coder
    - Claude Code vs Cursor
    - whether it is good enough for production
    - how much it costs per month (one cited stack is about $70/month before any business logic)
    - the biggest mistakes
  - Token limits are called the top complaint "across dozens of threads"; this is its only frequency claim.
  - Six beginner failure patterns: no spec, skipping Git, chasing perfection, ignoring error messages, the wrong tool, not understanding the code.
  - Context loss and maintainability.
- **Outdated framings:** none stated explicitly.
- **Why it matters:** a rough proxy for the r/vibecoding FAQ: cost, tool choice and production readiness. Use it only to confirm themes that the primary sources above already show.

---

## Notes for the curriculum team

- **Strongest new or underweighted topics, all with 2026 primary evidence:**
  1. "Green is not done": verify at the destination, and the agent's "fixed" is a claim (sources 13, 16, 19, 20, 21).
  2. Rules files are requests, not fences: only hooks, sandboxes and permissions enforce anything (14, 11).
  3. Backups the agent's shell can reach are not backups; run modes and approvals come before auto-run (10, 11, 17).
  4. Test URL vs production URL, localhost, env vars and redeploying: "where does my thing live and who can reach it" (18, 22, 16).
  5. Cost comes from context re-reading and agents waking agents, not from messages (15, 6).
  6. Memory is maintained files and goes stale (12, 5).
  7. Security needs someone who can check access control, client-side keys and price tampering (3, 23, 9).
- **Not covered:** Reddit directly, X, Discord FAQs and YouTube comments (tool limits, see Method). A follow-up pass with fresh search budget should target r/vibecoding, r/lovable and r/replit through an accessible mirror the user approves, plus YouTube comment threads on popular "build an app with AI" videos.
