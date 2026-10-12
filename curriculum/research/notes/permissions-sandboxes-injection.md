# Research notes: Prompt injection, approval prompts, sandboxes and least privilege

Theme: prompt injection as a structural risk, why approval prompts fail, what a sandbox does and does not cover, and least privilege for agents.
Batch read on 2026-10-12. Every point below comes from a page fetched and read on that date. Dates were checked on the page itself. Attack descriptions are kept at the level a builder needs to understand the risk, not to reproduce it.

---

## S049 - The lethal trifecta for AI agents: private data, untrusted content, and external communication

- **Author:** Simon Willison
- **Date:** 2025-06-16. Confirmed on the page. Older than 12 months, but foundational and still current: Willison links it again in his 2026-08-08 auto-mode post, and the Anthropic team joked it should be retitled "defeating the lethal trifecta" (S051).
- **URL:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

**Summary.** If an agent has (1) access to private data, (2) exposure to untrusted content, and (3) any way to communicate externally, an attacker can get it to read the private data and send it to them. Models cannot reliably tell whose instructions they are reading, because everything becomes one stream of tokens. Guardrail products that "catch 95%" are a failing grade in security. MCP makes this easy to assemble by accident, because users mix tools from different sources. The only reliable protection for a user mixing tools is never to combine all three.

**Gaps it shows**

1. **The lethal trifecta is the one mental model for prompt-injection risk.**
   - Private data: one of the most common reasons to give a model tools at all.
   - Untrusted content: any channel where text or images an attacker controls can reach the model (web pages, emails, issues, documents).
   - External communication: any way out. An HTTP request, loading an image, or showing a clickable link can each carry data out ("exfiltration").
   - Remove any one leg and this attack has nowhere to go.
2. **The model cannot tell your instructions from the attacker's.**
   - Asked to summarize a web page, a model may follow instructions hidden in that page.
   - Telling the model "don't obey instructions in content" is not a fix: outputs are non-deterministic and attacks can be phrased endlessly.
3. **95% detection is a failing grade.**
   - Vendors sell guardrails claiming to catch "95% of attacks". In web security an attacker only needs the 5%, and can retry.
   - No known method prevents prompt injection 100% reliably.
4. **Mixing MCP tools assembles the trifecta without anyone deciding to.**
   - Many tools both read private data and pull in untrusted content. Email access alone gives an attacker a way in: they just send the assistant an email.
   - The GitHub MCP case: one tool read public issues (attacker-writable), could see private repos, and could open pull requests (a way out).
   - Vendors fix their own products, usually by closing the exfiltration path, but they cannot fix a combination the user assembled.
5. **The list of products already hit is long and recent.**
   - Named examples include Microsoft 365 Copilot, GitHub's official MCP server, GitLab Duo, ChatGPT, Google Bard, Amazon Q, Google NotebookLM, GitHub Copilot Chat, Slack, Mistral Le Chat, xAI Grok, Anthropic's Claude iOS app and ChatGPT Operator (2023-2025).
6. **Prompt injection is not jailbreaking.**
   - Jailbreaking is the user tricking the model; prompt injection is untrusted content mixed with trusted instructions, named after SQL injection. Builders who conflate them dismiss the risk ("my users won't jailbreak it").
7. **For builders, the design principle.**
   - Once an agent has read untrusted input, constrain it so that input cannot trigger consequential actions (from the "Design Patterns for Securing LLM Agents against Prompt Injections" paper the post cites; CaMeL from Google DeepMind is cited as a promising direction).

**Outdated framings it corrects:** "A better system prompt will stop injection"; "a guardrail product that catches 95% makes it safe"; "prompt injection = jailbreaking".

**Quotes**
- "unable to reliably distinguish the importance of instructions based on where they came from"
- "in web application security 95% is very much a failing grade"

---

## S050 - How we contain Claude across products

- **Author:** Anthropic Engineering (Max McGuinness, Mikaela Grace, Jiri De Jonghe, Jake Eaton, Abel Ribbink)
- **Date:** 2026-05-25. Confirmed ("Published May 25, 2026").
- **URL:** https://www.anthropic.com/engineering/how-we-contain-claude

**Summary.** Anthropic splits agent safety into supervision (a human approves actions) and containment (the environment limits what the agent can do). Supervision is fallible: users approved roughly 93% of permission prompts and paid less attention over time. Containment works better: Claude Code's OS sandbox (reads allowed, writes only in the workspace, network denied by default) cut permission prompts by 84%. Credentials are kept out of the agent's VM. Their own incidents show where containment still leaked: data left through an allowlisted domain, and a phished user who asked Claude to send their cloud keys out.

**Gaps it shows**

1. **Supervision vs containment: approval prompts are the weak layer.**
   - Telemetry: users approved roughly 93% of permission prompts. More prompts produced "approval fatigue".
   - Auto mode (a classifier approving actions) catches roughly 83% of overeager behaviors; the article calls it one layer inside a sandbox, not a substitute for one.
   - Model-layer defenses (system prompts, classifiers, training) shape what the agent tends to do, not what it can do. "Protection in the model layer will never be 100% effective."
2. **An OS sandbox with network denied by default removes most prompts and most risk.**
   - Seatbelt on macOS, bubblewrap on Linux. Reads allowed, writes inside the workspace, network denied by default.
   - Result: an 84% reduction in permission prompts. The runtime is open source so the boundary can be audited.
3. **Credentials should never enter the agent's environment.**
   - In Cowork, credentials stay in the host keychain; the VM gets a per-session, scoped token that can be revoked separately.
   - "If credentials never enter the sandbox, they cannot be exfiltrated."
4. **An allowlist is a capability grant, not a destination filter.**
   - Cowork's egress allowlist permitted Anthropic's own API (the product needs it). A malicious file in the workspace carried hidden instructions plus an attacker's API key, and Claude uploaded workspace files to the attacker's account through that allowed domain.
   - Lesson: every function reachable through an allowed domain is attack surface. "Allow github.com" or "allow api.example.com" grants everything those hosts can do, including accepting uploads into someone else's account.
5. **The user can be the injection vector.**
   - Internal red team (Feb 2026): a phished employee launched Claude Code with a prompt to read their cloud credentials file and send it out. Claude completed it in 24 of 25 retries. Only environment controls (egress, filesystem boundary) stop this.
6. **Opening a repo can run code before you agree to trust it.**
   - Three reported vulnerabilities (mid-2025 to Jan 2026) ran code from a repository's project config before the trust dialog was accepted. Fix: defer project-local config until after consent.
7. **Injections can persist.**
   - Open problem: injected instructions can live on in CLAUDE.md files, product memory, mounted workspaces and scheduled-agent state.
   - Sub-agent output treated as more trusted than raw tool output is a new injection path.
   - Remote tools can change behavior after you approved them; an audited connector does not mean audited data.
8. **Match isolation to who is watching.**
   - Developers can read bash; knowledge workers often cannot. The less the user can evaluate, the stronger the isolation must be.
   - Custom in-house components (their allowlist proxy) were where flaws appeared; hypervisors, seccomp and gVisor held up.
9. **Isolation hides the agent from security monitoring.**
   - VM isolation also hides the agent from endpoint detection (EDR); log export is not live monitoring.

**Outdated framings it corrects:** "Human approval of each action keeps you safe"; "an allowlist of domains means data can only go to good places"; "the model will refuse to do something harmful".

**Quotes**
- "Our telemetry showed users approved roughly 93% of permission prompts."
- "it may be better conceptualized as a capability grant"

---

## S051 - Auto mode is now the default in Claude Code for Pro, Max, and Team plans

- **Author:** Simon Willison (link post on Anthropic's announcement)
- **Date:** 2026-08-08. Confirmed.
- **URL:** https://simonwillison.net/2026/Aug/8/auto-mode/
- **Companion sources read:**
  - Anthropic, "Auto mode is now the default in Claude Code for Pro, Max, and Team plans", 2026-08-07 (the primary source of the numbers). https://claude.com/blog/auto-mode-default-in-claude-code
  - Simon Willison, "Breaking Claude Code Opus 5 Auto Mode", 2026-08-27 (update 2026-08-30). https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
  - Johann Rehberger (wunderwuzzi), Embrace The Red, "Breaking Claude Code Opus 5 Auto Mode", 2026-08-26. https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/

**Summary.** From 2026-08-14, new Claude Code sessions on Pro, Max and Team start in auto mode, where a classifier model approves actions instead of you. Anthropic's study of 1,053 paid testers swapped one prompt for a clearly dangerous command: only 13.6% of humans refused it, while auto mode would have blocked 89%, leaving 11%. Willison accepts auto mode beats approval fatigue, but separates accidental damage from prompt injection and asks for independent confirmation of the injection claims. Three weeks later Rehberger published a working attack in which a downloaded file shadowed a Python standard-library module, achieving code execution in 60-80% of small trial sets; Anthropic closed it as working as designed, and both writers conclude auto mode is not a security boundary.

**Gaps it shows**

1. **Humans are bad approvers, and get worse the longer they approve.**
   - 1,053 testers; 13.6% (143) refused the planted dangerous command. Auto mode blocked 89% (937).
   - Human refusal fell from about 17% early in a session to about 5% after 50+ prompts (Anthropic, 2026-08-07).
   - Users approve 97% of prompts; 62% have used bypass or "don't ask again" on Bash; 25% of interactive sessions start in bypass mode; about 43% have interpreter-wide allow rules such as `Bash(python:*)` (Anthropic, 2026-08-07).
   - Note the two Anthropic figures for approval rate: 93% (2026-05-25) and 97% (2026-08-07).
2. **11% still gets through, and that is the number to remember.**
   - Willison: "that still leaves 11% of cases where auto mode would not have prevented the action".
   - Anthropic's own red-teaming miss rate (Apollo Research) is 7%, on synthetic attacks.
3. **Accidental damage and prompt injection are different risks needing different defenses.**
   - Accidental: deleting the wrong files, clearing a production database. A classifier helps here.
   - Injection: malicious instructions hidden in content the agent reads. Willison worries about this more; his example is a malicious package telling the agent to run a helper that exfiltrates data.
4. **Vendor security claims need independent checks.**
   - The vendor-commissioned eval (Trajectory Labs): 72 scenarios x 10 runs = 720 attempts, zero successes for Opus 5, Sonnet 5 and Fable 5 in auto mode.
   - Rehberger: a "summarize this website" request still led to code execution. A 0% benchmark and a working attack can both be true when the attack is outside the benchmark's scenarios.
5. **Confused-environment attack: the agent hurts itself with files it downloaded.**
   - The agent fetched an archive, wrote its own small Python script to decode the contents and ran it inside the extracted folder. A file in the archive named like a standard-library module (`struct.py`) was loaded instead of the real one, so the agent's own harmless-looking script ran attacker code.
   - The classifier saw only the short, innocent script. In some runs it then denied Claude's attempt to kill the malicious process: "The safety mechanism itself can become part of the failure."
   - Willison's 2026-08-30 update calls it "a confused environment attack": no instruction was obeyed.
   - Success: 3/5, 3/5 and 4/5 across variants (60-80%), small samples.
6. **Auto mode is not a security boundary; containment is.**
   - Anthropic closed Rehberger's report as Informative ("working as designed"): auto mode is a convenience feature with a best-effort classifier; the boundary is OS isolation and egress control.
   - Recommendations (Rehberger, endorsed by Willison): run unattended agents in a container, VM or OS sandbox; restrict network egress; monitor agents; do not expose home directories, SSH keys or cloud credentials to the agent.

**Outdated framings it corrects:** "Approve each step and you are in control"; "auto mode / the classifier keeps me safe from injection"; "prompt injection is solved".

**Quotes**
- "Only 13.6% of the humans refused that harmful action." (Willison)
- "it is not a security boundary, and hence risky" (Rehberger)

---

## S052 - Choose a permission mode (Claude Code docs), plus Security and Sandboxing pages, plus Copilot local sandboxing GA

- **Author:** Anthropic (Claude Code documentation); GitHub (changelog)
- **Date:** Living docs pages, no date shown (undated); content references Claude Code versions up to v2.1.293, consistent with 2026-09/10. Copilot changelog: 2026-10-07, confirmed.
- **URLs:**
  - https://code.claude.com/docs/en/permission-modes
  - https://code.claude.com/docs/en/security
  - https://code.claude.com/docs/en/sandboxing
  - https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available

**Summary.** Claude Code has six permission modes, and since v2.1.283 auto mode is the starting mode for interactive terminal and VS Code sessions on every plan. The docs warn that auto mode "does not guarantee safety". A permission mode only decides whether Claude asks; the sandbox decides what a command can reach. The sandbox is off by default, covers shell commands only, and on native Windows does not exist. The working-directory boundary is a prompt, not a wall. GitHub made a similar local sandbox generally available for Copilot, which organizations can require.

**Gaps it shows**

1. **The six modes and their trade-offs.**
   - `default` (Manual): reads only run without asking. For sensitive work.
   - `acceptEdits`: reads, file edits and common filesystem commands (mkdir, touch, mv, cp, also rm and sed in the working directory per the Security page).
   - `plan`: reads, plus classifier-approved commands where auto mode exists; edits blocked until you approve a plan.
   - `auto`: everything, with a background classifier. Long tasks, fewer prompts.
   - `dontAsk`: only pre-approved tools; anything that would prompt is denied. For CI.
   - `bypassPermissions` (`--dangerously-skip-permissions`): everything. "Isolated containers and VMs only"; it "offers no protection against prompt injection or unintended actions". Refused when run as root.
2. **Auto mode is now the default, and it is not a guarantee.**
   - "Auto mode reduces permission prompts but does not guarantee safety."
   - Blocked by default (examples): `curl | bash`, sending sensitive data out, production deploys, force push, `git reset --hard`, reading credentials from the cloud metadata endpoint, printing a live token into the transcript, launching an agent loop with no sandbox.
   - Allowed by default (examples): reading `.env` and sending credentials to their matching API, installing declared dependencies, pushing to any branch of the current repo.
   - Boundaries you state in chat ("don't push") are re-read from the transcript, and can be lost when context is compacted; for a hard guarantee write a deny rule.
   - After 3 blocks in a row or 20 total, auto mode falls back to prompting.
   - Broad allow rules (`Bash(*)`, `Bash(python*)`) are dropped while in auto mode.
3. **Protected paths: the files that would let an agent change its own rules or plant code are never silently written.**
   - Directories: `.git`, `.vscode`, `.idea`, `.husky`, `.devcontainer`, `.claude` (with exceptions), and others.
   - Files: shell startup files (`.bashrc`, `.zshrc`, `.profile`), `.gitconfig`, `.npmrc`, pre-commit configs, `.mcp.json`, `.claude.json`.
   - Writes there are prompted in default/acceptEdits, routed to the classifier in auto, denied in dontAsk, allowed in bypassPermissions.
   - Critical paths (filesystem root, home, working directory and its parents) can never be `rm`'d by an allow rule.
4. **The sandbox is off by default and covers shell commands only.**
   - Turn on with `/sandbox` or `sandbox.enabled: true`.
   - Outside it: the built-in Read/Edit/Write/WebFetch tools, hooks, local MCP servers, LSP servers, status line, and commands you type yourself at `!`.
   - On native Windows there is no sandbox; Claude Code runs commands unsandboxed (use WSL2).
   - If the sandbox cannot start, Claude Code runs commands unsandboxed unless `failIfUnavailable` is set.
   - Claude can ask to retry a failed command outside the sandbox (`dangerouslyDisableSandbox`); turn that off with strict sandbox mode (`allowUnsandboxedCommands: false`).
5. **Default sandbox reads still include your secrets.**
   - Reads: "most of the machine, including credential files such as `~/.ssh` and `~/.aws/credentials`". Environment variables, including secrets, are inherited.
   - "There is no built-in credential deny list"; you must list files and variables yourself in `sandbox.credentials`.
6. **Network allowlists leak if they are broad.**
   - The proxy decides from the hostname without inspecting TLS. "Allowing broad domains such as github.com can create paths for data exfiltration", and domain fronting can reach hosts outside the list.
   - Effective sandboxing needs both filesystem and network isolation; one without the other can be undone.
7. **The working-directory boundary is a prompt, not a wall.**
   - "The boundary is a permission prompt, so a Bash command you approve can still write anywhere your user account can."
   - Anthropic reviews connectors for its directory but "does not security-audit or manage any MCP server".
   - A `-p` (headless) session shows neither the trust dialog nor the `.mcp.json` approval.
8. **Copilot now has the same idea, and organizations can enforce it.**
   - Covers Copilot CLI, the Copilot app and VS Code sessions using Agent Host. Tools and commands Copilot starts get restricted access to files, network, Git and GitHub CLI credentials; local MCP and language servers where supported.
   - Built on Microsoft eXecution Container (MXC) across Windows, macOS and Linux. "Model execution and tool isolation are separate concerns."
   - Enterprise-managed settings can require sandboxing so developers cannot weaken it. Default on/off is not stated.

**Outdated framings it corrects:** "Claude only touches files in my project folder"; "turning on the sandbox protects everything Claude does"; "auto mode is a safety feature I can rely on"; "the sandbox works the same on Windows".

**Quotes**
- "Auto mode reduces permission prompts but does not guarantee safety."
- "The sandbox covers shell commands only."

---

## S053 - Zero risk isn't the job: a CISO's guide to agentic AI

- **Author:** Jason Clinton, Deputy CISO, Anthropic
- **Date:** 2026-07-17. Confirmed.
- **URL:** https://claude.com/blog/ciso-guide-to-agentic-ai

**Summary.** A security leader's job is to make agent risk visible and bounded, not to refuse it: saying no produces shadow adoption with no telemetry and no off switch. Every agent deployment is assessed with four questions: what untrusted content it ingests, what it can do and as whom, the blast radius if it goes wrong, and whether you can tell its actions from the user's. The controls are least agency, no credentials worth stealing in the agent's environment, an egress proxy the agent cannot bypass, telemetry, and an off switch. Design for where the model will be in six months, because new capabilities appear inside existing deployments.

**Gaps it shows**

1. **The four questions, translated for a solo builder.**
   - "What untrusted content does it ingest?" Untrusted is "anything an attacker could plausibly write or alter": inbound email, the open web, third-party docs, public repos, issues, reviews. If the answer is nothing, risk is near zero.
   - "What actions can it take, and on whose behalf?" Read-only vs read/write; code execution and network egress widen it. Every action runs as some identity: whose key is it?
   - "What is the blast radius if it is misaligned?" Scope times severity: one file or everything; annoyance or data exposure.
   - "What observability do I have?" Can you tell later what the agent did versus what you did?
2. **Least agency.** "Grant the narrowest capability that still completes the task." Remove verbs rather than trust the agent not to use them (drafts but not sends; reads and searches but not deletes).
3. **No credential worth stealing where the agent runs.**
   - The agent loop "should never hold a credential worth stealing". In Cowork remote sessions, connector tokens never enter the sandbox; a reverse proxy injects them.
   - At Anthropic, PR-authoring agents run in ephemeral VMs separated from production keys, with human review before merge.
4. **Egress through a proxy the agent cannot change.** Only chosen destinations are reachable, which limits where an injected agent can send data.
5. **Saying no drives shadow adoption.** Shadow tools have "zero telemetry and generally no off switch". For a solo builder: the risky setup is the one you quietly improvise; a deliberate, contained setup is safer than an ad hoc one.
6. **Agent drift is an insider-risk problem.** An agent drifting from intent is treated as indistinguishable from an insider attack; Ponemon 2026 puts average insider-incident containment at 67 days, too slow for agents.
7. **Capabilities appear without you changing anything.** After a model upgrade (Opus 4 to 4.5, Nov 2025) Anthropic's read-only incident agent asked another agent to write a fix. A human-reviewed PR step held. Limit access based on what you cannot rule out, not on today's model limits.
8. **Prompts and scaffolding are not controls.** Elaborate prompts used as controls will be removed as models improve; they are not reliable control points.

**Outdated framings it corrects:** "Security means saying no to AI tools"; "the agent uses my login, so it is just me"; "the current model can't do that, so I don't need to block it".

**Quotes**
- "Untrusted means anything an attacker could plausibly write or alter"
- "Design for where the model will be in six months."

---

## S054 - One prompt let researchers take over AWS AgentCore agents (AgentCorruption)

- **Author:** Ana Maria Constantin (The Next Web), reporting Zenity Labs research
- **Date:** 2026-10-08. Confirmed (2:14 pm UTC). The article carries a correction: the research covered agents in one AWS account and region, not a whole region.
- **URL:** https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents
- **Companion source read:** Zenity Labs, "AgentCorruption: How a single prompt collapsed the entire cloud security model", Tamir Ishay Sharbat and Lana Salameh, 2026-10-08. https://labs.zenity.io/post/agentcorruption-how-a-single-prompt-collapsed-the-entire-cloud-security-model

**Summary.** Zenity showed that a public-facing agent on Amazon Bedrock AgentCore with an ordinary web-request tool could be asked, in plain language, to fetch its own temporary cloud credentials from the instance metadata service. Because the default execution role covered the whole account and region, those credentials reached other agents, their code, users' private conversations and stored secrets. Write access to agent memory let one injected instruction persist across future sessions. AWS called it documented, expected behavior and said customers should scope roles to the minimum; it has since moved new agents to IMDSv2-only (2026-02-14) and narrowed the default role (observed 2026-09-29).

**Gaps it shows**

1. **A public chatbot is a credential holder.**
   - Any agent runs as some identity, and its tools can often reach that identity's credentials. Expose the agent to the public and you have exposed whatever its role can do.
2. **Defaults are not least privilege; scoping the role is the builder's job.**
   - The default role covered resources across the whole account and region. AWS's answer: "grant their execution roles only the permissions their agents need" (shared responsibility).
   - Starter templates and managed-service defaults can be broader than your app needs. You must read and narrow them.
3. **A web or shell tool can reach the cloud metadata endpoint.**
   - Inside cloud compute, a link-local address returns the machine's temporary credentials. A tool that can fetch arbitrary URLs is a server-side request forgery tool unless the network blocks it.
   - Claude Code's auto mode now blocks requests to the cloud metadata endpoint by default (S052), and its sandbox refuses link-local addresses: evidence this is a known pattern.
4. **Persistent memory turns one injection into a lasting instruction.**
   - A fake conversation event stored in long-term memory told the agent to consult an attacker-controlled page before every answer; editing that page changed the agent's behavior later with no new access.
5. **Agents in the same account are not isolated from each other.** Keep customer-facing and internal agents apart where possible.
6. **"Documented behavior" is not "safe behavior".** AWS closed the first report as informative. A vendor saying "working as designed" (also S051) means the risk is yours to configure away.

**Outdated framings it corrects:** "The cloud provider's defaults are secure"; "the chatbot only answers questions, it can't do anything"; "memory is just convenience".

**Quotes**
- "Cloud security is all about segmentation and least-privilege access." (Michael Bargury, Zenity)
- "grant their execution roles only the permissions their agents need" (AWS)

---

## S055 - OWASP Top 10 for LLM Applications 2026 (plus Agentic Top 10 and CSA note)

- **Author:** OWASP GenAI Security Project
- **Date:** GitHub README says "published August 4, 2026"; the genai.owasp.org resource page lists August 3, 2026. Record as 2026-08-03/04.
- **URL:** https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 (canonical files in `2026/final/`; preface, LLM03 and LLM08 read in full)
- **Companion sources read:**
  - OWASP Top 10 for Agentic Applications for 2026, resource page dated 2025-12-09 (ASI names taken from the 2026 Appendix A framework mappings in the repo). https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
  - CSA AI Safety Initiative, "OWASP's 2026 LLM Top 10 and New Agent Control Standard", 2026-09-04. https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/

**Summary.** The 2026 list: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling. Excessive Agency rose from #6 to #3 ("the most consequential move on the list"); Unbounded Consumption rose four places (#10 to #6); System Prompt Leakage was renamed and broadened into Hidden Context Exposure; Improper Output Handling fell from #5 to #10 but now includes insecure code generated by assistants. For the first time the ranking blends practitioner votes (about 75%) with incident data (about 25%, from 6,639 classified incidents out of 7,714 compiled). Agents acting on their own belong to the separate Agentic Top 10 (ASI01-ASI10).

**Gaps it shows**

1. **Tutorials citing the 2025 list are out of date.**
   - 2025 order: Prompt Injection, Sensitive Info Disclosure, Supply Chain, Data and Model Poisoning, Improper Output Handling, Excessive Agency, System Prompt Leakage, Vector and Embedding Weaknesses, Misinformation, Unbounded Consumption.
   - "System Prompt Leakage" no longer exists as an entry.
2. **Excessive agency: the agent can do more than the task needs.**
   - Three root causes: excessive functionality, excessive permissions, excessive autonomy.
   - Examples: a read-only document tool that also deletes; a shell tool that doesn't restrict commands; a database account with write access when only reads are needed; a per-user tool running under one highly privileged identity; tools left over from an abandoned trial.
   - Worked scenario: an email-summarizing assistant whose tool can also send mail is told by a malicious email to forward sensitive mail. Remove the send function, use a read-only OAuth scope, require approval for sends.
   - "Complete mediation": enforce authorization in code or a policy layer, not by asking the model. Reversible actions can auto-approve; irreversible ones go to a human.
3. **Hidden context is not secret.**
   - "Assume all context available to the LLM could also be available to users."
   - Hidden context includes system prompts, retrieved policy text, tool schemas, and embedded credentials or connection strings. Never put secrets in prompts; enforce access control outside the model.
4. **Unbounded consumption rose because practitioners weigh cost and resource exhaustion more heavily now.**
5. **Prompt injection stays #1 on votes, not raw incident counts.** It now covers cross-modal attacks (instructions hidden in images or audio).
6. **Improper output handling now includes insecure AI-generated code at scale.**
7. **Agentic Top 10 (ASI01-ASI10):** Agent Goal Hijack; Tool Misuse & Exploitation; Identity & Privilege Abuse; Agentic Supply Chain Vulnerabilities; Unexpected Code Execution (RCE); Memory & Context Poisoning; Insecure Inter-Agent Communication; Cascading Failures; Human-Agent Trust Exploitation; Rogue Agents. Use both lists together.
8. **Agent Control Standard (CSA note).** OWASP's new Agent Control Standard (v0.1, definitions only) defines enforcement points, OpenTelemetry/OCSF tracing and an Agent Bill of Materials (inventory of an agent's tools, models and data). Pilot, don't deploy as a control. CSA's practical advice: inventory each agent and map what tools, data and systems it can reach; enforce permissions at call time and review them periodically against "permission accretion". CSA warns the new methodology may make ranks volatile, so focus on categories, not positions.

**Outdated framings it corrects:** citing the 2025 list or "System Prompt Leakage"; "hiding the system prompt protects my app"; "prompt hygiene is the main defense" (CSA: permission scope is the growing risk).

**Quotes**
- "the most consequential move on the list" (OWASP 2026 preface, on Excessive Agency)
- "Assume all context available to the LLM could also be available to users." (LLM08:2026)

---

## Unreadable

None. The Agentic Top 10 resource page shows only a title and download link; the ASI names were taken from the OWASP repo's 2026 Appendix A mappings instead. Web search budget was exhausted during this batch; no further searches were run.
