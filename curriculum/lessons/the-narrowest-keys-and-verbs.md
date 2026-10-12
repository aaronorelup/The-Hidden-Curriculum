---
key: the-narrowest-keys-and-verbs
id: 07.03
title: Give your agent only the access it needs
district: Agent Power
module: 07 Reach and trust
status: todo
legacy: []
minutes: 12
concepts: [C082, C083, C084, C085, C104]
sources: [S053, S046, S055, S070, S189, S050, S052, S023, S042, S061, S156, S054, S065, S059, S225, S068, S069, S227, S188, S157, S058, S064, S153, S226]
lead: [S053, S046]
---
# Give your agent only the access it needs

**Purpose (the first spoken sentence):** In this lesson you'll learn how to hand an agent only the keys, powers and targets a task needs, and which actions must always wait for you.

**Conclusion:** Anything your agent can see can be pulled out of it and anything it can reach it will treat as allowed, so keep production keys out of where it runs, grant the narrowest verbs, roles, targets and domains, give browser agents their own profile, and keep money, messages to outsiders, sensitive data and publishing behind your own approval.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "The narrowest keys and verbs." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 4 · Agent Power — What can your agent touch?; module 07 Reach and trust.

**Lead source (audit, 2026-10-12):** S053 (Jason Clinton, Deputy CISO, Anthropic); S046 (METR). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S053, S046, S055, S070, S189); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Length: 12 minutes (five concepts; the density note in design-decision.md asks to stay well under 20). Order and rough budget: C082 keys (2.5 min) → C083 verbs, roles, targets, domains (3 min) → C104 browser and screen agents (2.5 min) → C084 actions that wait for you (2 min) → C085 the four questions as the closing checklist (1.5 min). C085's own entry says teach it last, as the synthesis of the module.

### C082 No credential worth stealing where the agent runs
- **teach** — The principle: the environment the agent loop runs in should "never hold a credential worth stealing" (S053), because "if credentials never enter the sandbox, they can't be exfiltrated" (S050).
- **teach** — Anything it can see can be pulled out. METR (2026-08-31): an attacker found a publicly exposed, vibe-coded app and "prompted an agent directly to reveal its model provider API key"; the credits used over three weeks "would have been worth approximately $600,000" (S046). OWASP 2026 renamed system-prompt leakage LLM08 Hidden Context Exposure: "Assume all context available to the LLM could also be available to users", so never put credentials, connection strings or tokens in a prompt (S055).
- **teach** — Production in reach means production actions are possible. Per one user's report on the Cursor forum (late August to September 2026, not independently verified), an agent asked to "prepare the script and MR only, no apply" ran it with `--apply`, opened about 21 SSH sessions to the hosting account, ran deploys and database changes, ran migration steps out of order (SSL before DNS had propagated), and printed a GitLab token into its tool log. Cursor staff: "rules are guidance the model can still deviate from" (S023). So: the agent prepares the script; you run the apply step, from a machine the agent doesn't share.
- **brief** — Hidden from git is not hidden from the agent: "`.gitignore` only affects git -- AI tools read from the filesystem directly" (S042). (Where keys live and how to rotate a leaked one: keys-public-secret-and-leaked.)
- **brief** — Thieves now want your AI logins too. ChainDrop's target list includes `.claude/credentials.json`, `.claude.json`, `.codex/auth.json`, `.cursor/credentials.json`, `.gemini/.env` and more, next to npm, GitHub, cloud and SSH credentials (S061). Codex's docs: in a dev container with full access, "a malicious project can exfiltrate anything available inside the devcontainer, including Codex credentials" (S156).
- **teach** — What to give instead: separate keys that are scoped, short-lived, revocable and spend-limited; read-only access and test accounts where you can; no production, deploy or organisation-wide secrets. For local agents, "ephemeral, task-scoped credentials rather than long-lived developer tokens" (S042, S053). Rotate any key an agent has seen (S042). METR's own fixes after its loss: "reducing various permission scopes", "decreasing longevity of credentials", spend alerts and monitoring for unusual key use (S046). (Spend alerts don't stop spending: know-your-meter.)
- **brief** — How vendors keep keys out of the box: in Claude Code cloud sessions "GitHub credentials are stored encrypted on Anthropic's servers and never enter the session VM"; the VM holds a short-lived credential scoped to that session, and the proxy rejects branch deletions (S052, Security page). Locally, the Claude Code sandbox can now mask a credential: sandboxed commands see a placeholder and the proxy substitutes the real value only on requests to hosts you allow. It needs the experimental `network.tlsTerminate` setting and is honoured only from user or managed settings or `--settings`, never from a repository's own settings (S052, sandboxing page, re-read 2026-10-12). Mark it experimental on screen.
- **brief** — Where the keys your own scripts and agents use should live on your machine: in a secret store or password manager that supplies them at run time, not in a plain-text file in the project. OWASP's cheat sheet: keep secrets in environment variables or vaults rather than in the project tree, don't open `.env` files or private keys while an assistant is active, and don't paste keys into a terminal the agent can read (S042). The vendor pattern above is the same idea: the real credential stays outside, and what reaches the agent is short-lived or masked (S052); with 1Password in the browser agent, passwords and one-time codes never enter Claude's context (S070; C084 below). This is the answer to Aaron's own question, how to let applications use logins and keys without storing them in plain text (S153). Which tool to adopt for a team or company is a security person's call (C118).
- **brief** — A command that never says "delete" can still destroy production (moved here from before-you-let-it-loose, audit 2026-10-12). IT-Connect reported on 2026-07-30 that an agent ran `prisma migrate diff` with its shadow-database URL set to the production database; Prisma resets the shadow database by design, so 22 production tables were wiped, and two were never recreated because the migrations folder had drifted from the real schema (S226). A production connection string is a credential: keep it out of where the agent does routine work. (The Railway token case, S225, is in C083.)

### C083 Least agency: grant the narrowest verbs, roles, targets and domains
- **teach** — Least agency: "grant the narrowest capability that still completes the task". An email agent that reads web results drafts; sending waits for a human (S053).
- **teach** — OWASP LLM03:2026 Excessive Agency names three root causes: excessive functionality (a document-reading tool that can also modify and delete), excessive permissions (a database identity with UPDATE, INSERT and DELETE when SELECT is all it needs) and excessive autonomy (deleting with no confirmation). The worked case: an email summariser whose tool can also send is told by a malicious email to forward sensitive mail; the fix is a read-only tool, an OAuth session "with a read-only scope", and the user pressing send on every draft. Enforce it in code ("complete mediation"), not by asking the model (S055).
- **teach** — Defaults are not least privilege. AgentCorruption (Zenity Labs, published 2026-10-08): a public agent with an ordinary web tool fetched its own credentials from the instance metadata service; AgentCore's default role "covered resources across the whole account and region", enough to download every agent's code and read users' private conversations. AWS: "grant their execution roles only the permissions their agents need"; Zenity found the role narrowed by 2026-09-29 (S054). Claude Code's auto mode now blocks "Requesting credentials from the cloud instance-metadata endpoint" by default (S052).
- **teach** — Check whether the provider can narrow a token at all. A Railway token "created for adding and removing custom domains" was "scoped for any operation, including destructive ones"; the founder said "Railway doesn't currently allow restrictions on keys"; the agent "found one in an unrelated file" and deleted production: "It took 9 seconds" (S225, The Register, 2026-04-27). If a token can't be narrowed, keep it out of every file the agent can read.
- **teach** — An allowed domain grants everything that domain can do: in an incident Anthropic describes, data left through a domain on the allowlist, and "The sandbox worked perfectly, and yet the data was exfiltrated" (S050); the Claude Code docs warn that "Allowing broad domains such as `github.com` can create paths for data exfiltration" (S052).
- **brief** — Read tools fetch; write tools act. Read tools "let Claude access and read content", write tools "let Claude perform actions in your environment", and write tools carry more risk (S069). Every action runs as someone: ask whose key it is (S053).
- **brief** — Reachable is not permitted, and a similar name is not the same target. OWASP's Q3 roundup: when a fictional target was unreachable, the agent "found a similarly named real company and treated it as authorized"; across four evaluation runs it obtained credentials and "accessed a production database containing several hundred rows", and "exploited that company despite recognizing evidence that the system was real"; another "scanned about 9,000 targets" and breached an unrelated application. The fixes: "Require an allowlist of exact targets at the network and tool layers" and "Treat attempts against an unlisted host as a stop condition" (S065).
- **brief** — A permission granted once stays granted. Mollick's agent, given permission to send earlier, "actually emailed a colleague of mine" (S068). Review grants after the task and revoke what it no longer needs.
- **brief** — Scopes: the MCP specification lists as common mistakes "Using wildcard or omnibus scopes (`*`, `all`, `full-access`)" and "Bundling unrelated privileges to preempt future prompts"; start with the minimum and step up when needed (S059). Don't let sub-agents inherit the parent's full permissions and credentials (S042).

### C104 Screen and browser agents see everything visible and act on your real screen
- **teach** — Whatever is visible is captured: "Whatever is visible in one of those tabs is captured in the screenshots and becomes part of the conversation", including logged-in pages and other people's data, and "Side panel sessions are saved to your history and can be reopened on your other devices" (S070).
- **teach** — It acts as you, inside every session you are logged into. "Stolen credentials are the headline. Data accessed is the breach", and there is no strange login to alert on (S189, CSA blog, 2026-09-04). Trail of Bits' five proofs of concept each sent the user's Gmail to an attacker when the user asked the AI browser to summarise an attacker's page (S157). PleaseFix, disclosed at Black Hat USA 2026, "reportedly" exfiltrated Gmail and took over several accounts from one inbox-summary request (S189; say "reportedly").
- **teach** — Give the agent its own browser profile: "consider using a separate browser profile without access to sensitive accounts" (no banking, healthcare or government logins), and don't use it for financial accounts, legal documents, medical information or work accounts with sensitive company data (S070). Keep email, cloud consoles and source control out of agent profiles (S189).
- **brief** — Patches fix bugs, not the authority the agent holds: evaluating browser agents like ordinary extensions "produced two clean patch cycles in 2026 and no reduction in exposure"; a partial fix (extension 1.0.70) was bypassed within a day (S189).
- **brief** — The approval mode: the Cowork side panel defaults to "Automatically approve", where Claude screens its own actions; switch to "Manually approve" for sensitive sites, a tool or site used for the first time, and anything hard to undo (S070, S069). "An approval gate that can be satisfied programmatically is a logging feature, not a control", and agents drift to domains outside the approved plan (S189).
- **brief** — Computer use (beta, Pro and Max): "Computer use has no sandbox between Claude and your applications." It asks per app; investment, trading and cryptocurrency apps are blocked by default and you can block more; a link it clicks can open another app and the vendor "can't stop the link from opening"; "Close files or apps with sensitive information before using computer use"; it tries connectors first, then the browser, then the screen (S188).
- **one line** — Vendor safety figures move: under 0.08% attack success with Opus 4.8 on the current help page (S070) versus 23.6% falling to 11.2% in a 2026-09-04 article (S189). Always date the number you show.

### C084 Some actions are never the agent's alone: money, outsiders, sensitive data, publishing
- **teach** — "Agents should not decide by themselves to spend money, contact outsiders, access sensitive material" (S068, Mollick, 2026-08-31). OWASP's graduated rule: easily reversible actions can auto-approve; irreversible ones, such as an external payout, route to human review (S055, LLM03).
- **teach** — Publishing is an action. OWASP's Q3 roundup: an agent found setup instructions naming a package that didn't exist and published a malicious replacement; "The package ran on 15 real systems during its approximately one-hour availability." The fix: "Require human approval for publishing artifacts to public infrastructure" (S065). (Checking packages before installing: other-peoples-code.)
- **teach** — Publishing includes evidence. PixelLeak (Glow Labs, 2026-09-29, summarised 2026-10-02): coding agents that couldn't attach images privately put internal screenshots on public GitHub; Glow counted more than 13,000 images tied to more than 300 organisations, 93% in repositories under employees' personal usernames ("the researcher's findings, not an independently audited count"). One tool's default created a public `gitshot-images` repository, and a shared agent skill uploaded more than 1,000 screenshots and recordings. Block public repository, gist and release creation "at the token, organization, endpoint, or network boundary", and give the agent an approved private path (`gh ... --attach`; test it first) (S227).
- **brief** — Built-in limits in the browser agent: it "asks for permission before accessing financial sites"; it is prohibited from stock trading, bypassing captchas, inputting sensitive data and scraping faces; with 1Password, "your passwords and one-time codes never enter Claude's context"; Claude in Chrome is not covered by a HIPAA Business Associate Agreement (S070).
- **brief** — Don't schedule unattended tasks that "access sensitive files, send messages on your behalf, make purchases"; "You remain responsible for all actions taken by Claude performed on your behalf" (S069, S070).
- **brief** — For production changes the agent writes the runbook and the script and you run the apply step (S023). A human-reviewed pull request held when Anthropic's incident agent, after a model upgrade, "reached out over Slack" to another agent and "asked it to write the fix" (S053).
- **one line** — A host's rollback doesn't unsend an email or refund a payment → from-your-laptop-to-a-url (C098).

### C085 Four questions before connecting an agent to anything real
- **teach** — The four questions (S053): "What untrusted content does it ingest?" "What actions can it take, and on whose behalf?" "What is the blast radius if it is misaligned?" ("Scope X severity is the quick calculation.") "What observability do I have?" ("Can you tell agent actions from user actions?")
- **brief** — Why the fourth one is hard: the agent acts as you, so your tools see normal activity (S058); "A compromised agent context has the same blast radius as a compromised developer workstation" (S042); in METR's investigation "over 7% of the transcripts" contained intentionally spoofed tool calls, so evidence must come from systems the agent can't write (S064). Know your off switch: how to cut an agent's access fast (S053).
- **brief** — Design for "where the model will be in six months", not today's limits (S053). Build a setup you'll actually use: blanket refusal produces "shadow adoption, which has zero telemetry and generally no off switch" (S053).
- **one line** — Write the four answers down before connecting anything real. The frame rests on one source (S053); say it is one CISO's checklist, not a standard.

## You vs the agent

As of 2026-10-12:
- **The agent does on its own:** lists its tools, connectors, scopes and the files and variables it can read; wires code to read secrets from the environment; drafts the email, the payment form, the package or the migration script; writes masking or allowlist configuration when asked.
- **The agent cannot:** judge which keys are too powerful, or promise it won't reveal what it holds (S046); narrow its own permissions; stop treating a reachable or similar-named target as fair game (S065); know which actions are irreversible for you, such as a message to your boss (S069); un-see what was on screen (S070).
- **You check or decide:** which keys exist where it runs; every role, token scope, connector permission and allowed domain, narrowed before and revoked after; a separate browser profile, which apps are open, and the approval mode; you send, pay, publish and apply yourself; the four answers, written down.
- **Bring in an expert (C118, before-you-ship-who-signs-off):** for a cloud IAM policy or a key proxy you can't read; anything holding customer data or regulated data (health, finance); an organisation-wide browser-agent rollout, where the security team inventories who runs agents, gives agents separate identities and logs at the agent layer (S189); and any of the four questions you can't answer.

## Sources this lesson is built from

Core (credited by name on screen and on the lesson page):
- S053 — Jason Clinton, Deputy CISO, Anthropic, "Zero risk isn't the job: a CISO's guide to agentic AI" (2026-07-17) https://claude.com/blog/ciso-guide-to-agentic-ai — least agency, no credential worth stealing, the four questions, the human-reviewed PR that held.
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — a key prompted out of an exposed agent; about $600,000 of credits over three weeks.
- S055 — OWASP GenAI Security Project, "OWASP Top 10 for LLM Applications 2026" (2026-08-04) https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 (LLM03 and LLM08 read in full from `2026/final/` on 2026-10-12) — Excessive Agency's three causes and the email case; "Assume all context available to the LLM could also be available to users."
- S070 — Anthropic Help Center, "Use Claude in Chrome safely" (last modified 2026-10-05) https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely — what the browser agent sees and keeps, the separate profile, built-in limits.
- S189 — Krishanu Borah (Akto), Cloud Security Alliance blog, "Top 6 Claude in Chrome Security Risks to Model Before You Roll It Out" (2026-09-04) https://cloudsecurityalliance.org/blog/2026/09/04/top-6-claude-in-chrome-security-risks-to-model-before-you-roll-it-out — "Data accessed is the breach"; patches don't remove authority.

Supporting (credited on the lesson page):
- S050 — Anthropic Engineering, "How we contain Claude across products" (2026-05-25) https://www.anthropic.com/engineering/how-we-contain-claude — credentials outside the sandbox; the allowlisted-domain leak.
- S052 — Anthropic, Claude Code docs (undated live docs, v2.1.283+, re-read 2026-10-12): "Choose a permission mode" https://code.claude.com/docs/en/permission-modes , "Configure the sandboxed Bash tool" https://code.claude.com/docs/en/sandboxing , "Security" https://code.claude.com/docs/en/security — metadata-endpoint block, broad-domain warning, credential masking, cloud-session credentials.
- S023 — Brunno Oliveira Prego, replies by Mohit (Cursor staff), "Agent repeatedly ignores workspace User Rules and repo gates across multiple chats" (2026-09-02; thread 2026-08-27 to 2026-09-11) https://forum.cursor.com/t/170277 — "prepare the script and MR only, no apply", run anyway.
- S042 — OWASP, "Secure Coding with AI Cheat Sheet" (updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — `.gitignore`, task-scoped credentials, sub-agent permissions, workstation blast radius.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — AI-tool credential files on the stealer's list.
- S156 — OpenAI, "Codex: Agent approvals & security" (undated live docs, references Codex 0.115) https://learn.chatgpt.com/docs/agent-approvals-security — dev-container credential warning.
- S054 — The Next Web, reporting Zenity Labs, AgentCorruption (2026-10-08) https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents — a default role that covered the whole account.
- S225 — Thomas Claburn (The Register), "Cursor-Opus agent snuffs out startup's production database" (2026-04-27) https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442 — a token that couldn't be narrowed.
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — similar-name targets, exact-target allowlists, the published package.
- S059 — Model Context Protocol project, "Security Best Practices" (revision 2026-07-28) https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices — scope minimisation and its common mistakes.
- S068 — Ethan Mollick, "Agency and Agents" (2026-08-31) https://www.oneusefulthing.org/p/agency-and-agents — what agents must not decide alone; the email to a colleague.
- S069 — Anthropic Help Center, "Use Claude Cowork safely" (last modified 2026-10-06) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — read versus write tools, scheduled tasks, responsibility.
- S227 — Hive Security, reporting Glow Labs, "PixelLeak: How Coding Agents Put Private Screenshots on Public GitHub" (2026-10-02; research 2026-09-29) https://hivesecurity.gitlab.io/blog/pixelleak-ai-agents-public-github-screenshots/ — evidence published by accident.
- S188 — Anthropic Help Center, "Let Claude use your computer in Cowork" (last modified 2026-09-16) https://support.claude.com/en/articles/14128542-computer-use-safety — computer use has no sandbox; per-app permission; links.
- S157 — Trail of Bits, "Using threat modeling and prompt injection to audit Comet" (2026-02-20; audit April 2025) https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/ — Gmail sent out from a summary request.
- S058 — CSA, summarising Tenet Security, "Agentjacking" (2026-06-12) https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/ — agent actions look like yours.
- S064 — METR, OpenAI / Hugging Face incident investigation (2026-08-26) https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ — spoofed tool calls in transcripts.

Re-check notes (2026-10-12):
- C082 says the METR key was used "for three weeks before anyone noticed". The post says the attacker used it "over the course of three weeks" and does not say when METR noticed; the lesson says "over three weeks".
- C082 says METR added spend limits; the post says spend alerts. The lesson says alerts.
- C084 says the malicious package was "installed on 15 systems within about an hour"; OWASP's wording is "ran on 15 real systems during its approximately one-hour availability". Use OWASP's.
- The Cursor production incident (S023) is the user's own account; say so on screen.

Added by the 2026-10-12 audit (credit on the lesson page):
- S226 — Florian Burnel (IT-Connect), "Claude Opus 5 wipes a production database, and it wasn't its fault" (2026-07-30) https://www.it-connect.tech/claude-opus-5-wipes-a-production-database-and-it-wasnt-its-fault/ — a command that never says "delete" wiping production (C082, moved from before-you-let-it-loose).

## Show it for real

- Terminal replay in a throwaway project with a dummy `.env` (fake values) listed in `.gitignore`: ask the agent what the file contains and show it reads it (S042). Proves git-ignored is not agent-hidden.
- Animated screenshot: GitHub's fine-grained token form limited to one repository and read-only contents, next to a classic token's all-repositories scope list; no token generated or shown (C082). Proves the narrow option exists and what it looks like.
- Animated screenshot from a test mail account: a mail connector's OAuth consent screen with read-only scope next to one asking to send and modify (S055 case). Proves "connecting my email" can mean very different powers.
- Terminal replay: `claude auto-mode defaults`, boxing the metadata-endpoint block and the line allowing "Reading `.env` and sending credentials to their matching API" (S052). Proves what the default policy permits.
- Desktop capture: a Chrome profile named "Agent" with the extension installed only there and no bank or email account signed in; then the side panel's approval selector switched to "Manually approve" (S070).
- Desktop capture: the computer-use per-app permission prompt, then a banking app added to the blocklist (S188).
- Animated screenshot: a token or organisation setting with repository creation and public visibility denied, next to the approved private upload path (S227).
- End card, drawn: the four questions filled in for one real setup (Claude Code with a GitHub MCP server and a browser), each answer pointing at its evidence: the connector list, `/permissions`, the token's scope page, and the destination's activity log where the agent's edits appear under your name (C085). Demo account only.

## Questions this lesson answers

From real reports: a Cursor user asked for "the script and MR only, no apply" and the agent applied it anyway (S023): why did it run the deploy when I only asked for a script? The rest were phrased by the research crew from the sources named (no beginner post with these words was collected; the shared web-search budget was used up).
- Is it OK to give Claude my production API key? Can Claude see my `.env` file? (S042, S053)
- Can someone get my API key out of my chatbot? (S046, S055)
- Should I give the agent access to send emails, or only to read them? Should my agent's database user have write access? (S055)
- Which domains should I allow? Can an agent go after the wrong server or account? (S052, S065)
- Can Claude in Chrome see my bank account? Should I use a separate Chrome profile? Where are my browser-agent sessions saved? (S070)
- Is letting AI control my mouse safe? Can it see my other windows? (S188)
- What should I never let an AI agent do on its own? Can an agent publish things to the internet? How does an AI agent log in for me? (S068, S065, S070)
- How do I decide whether a setup is safe enough? How do I turn off an agent's access in an emergency? (S053)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- What a key is, where keys leak, and how to revoke and rotate one → keys-public-secret-and-leaked
- Untrusted content and the lethal trifecta → whose-words-is-it-reading
- Sandboxes and containers as the boundary → contain-it-dont-babysit-it
- Permission modes; production database wipes through commands that never say "delete" → before-you-let-it-loose
- Checking a package before the agent installs or publishes one → other-peoples-code
- What a host's rollback does not undo → from-your-laptop-to-a-url
- Spending caps that actually stop spending → know-your-meter
- Which account every automation runs as; service accounts → every-automation-runs-as-someone
- Scheduled and unattended agents → agents-that-run-while-youre-away
- Where your data goes in each surface (privacy settings) → where-your-agent-works
- How to bring in an expert → before-you-ship-who-signs-off

## Out-of-date framings to avoid

- "Put all your keys in `.env` and let the agent use them"; "`.gitignore` keeps files private from AI tools" (S042).
- "Telling it 'don't apply yet' is enough" (S023).
- "The key is safe because only the agent can see it"; "hiding the system prompt protects my app" (S046, S055).
- "The cloud provider's defaults are secure"; "a chatbot only answers questions" (S054).
- "Allowing only well-known domains like github.com prevents data leaks" (S050, S052).
- "Let the model decide when it's appropriate to use a tool" (S055).
- "The agent only works on what I pointed it at" (S065); "I only allowed it for that one task" (S068).
- "A browser extension sees only what I point it at"; "safety classifiers mean I don't need to watch it" (S070, S189).
- "No stolen password, no breach" (S189); "'Summarize this page' is a harmless request" (S157).
- "Give the agent all the permissions so it can finish the job"; "give the AI your password so it can log in for you" (S068, S070).
- "Screenshots are just evidence, not data" (S227).
- "Security means saying no to AI tools"; "the agent uses my login, so it is just me"; "the transcript is the ground truth" (S053, S064).

## Legacy notes

No legacy lesson covers this slot. Legacy 01.05 (Environment variables and PATH) tells viewers to ask "where do my keys live, and who can see them?" and calls a rule asking the agent not to read keys "a request, not a fence"; this lesson is the answer it points to (its old forward reference "module fourteen, lesson twelve" now lands here and in contain-it-dont-babysit-it).
