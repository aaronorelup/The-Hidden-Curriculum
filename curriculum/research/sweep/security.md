# Sweep: security standards and guidance for AI-built software and agents, 2025-2026

Swept 2026-10-12 by the `sweep-security` research agent for The Hidden Curriculum.
Every source below was fetched and read; nothing is listed from a search snippet alone. Dates are publication dates as shown on the page; "undated" means the page shows none (live documentation, read on 2026-10-12). Where a block cites a second URL, that page was fetched too.

25 sources: 17 dated 2026 (10 of them from 2026-07-17 or later, 3 from October 2026, plus the OWASP cheat sheet updated 2026-10-04), 3 dated 2025 (OWASP Agentic Top 10, OpenSSF guide, Willison's "lethal trifecta"; kept because they are the current edition or a foundational concept the 2026 sources build on), 5 undated live vendor docs (Claude Code, Codex, GitHub, Supabase).

Search budget note: the shared web-search budget ran out partway through this sweep. Planned searches for the NIST COSAiS agent overlays, a Cloud Security Alliance "secure vibe coding" guide and the OpenSSF guide's newest version were not run; the OpenSSF guide and NIST COSAiS were then fetched directly by their known URLs. NIST COSAiS (https://csrc.nist.gov/projects/cosais, last updated 2026-01-08) is NOT listed below: its agent overlays ("Using AI Agent Systems: Single Agent / Multi-Agent") are still only "proposed", so there is no finished NIST control set for agents to teach yet. The full Five Eyes PDF on cyber.gov.au timed out three times; its content is taken from CISA's own page and bulletin plus CyberScoop.

## Cross-cutting findings (read these first)

1. **Security is the clearest case of "the agent cannot verify this for you".** OWASP's cheat sheet: "AI tools do not accept responsibility for the code they generate"; a passing AI-written test suite is not evidence of security, and the same agent should not both write security code and verify it. Arnica: models are optimized for code that works, not code that is safe, and know nothing of your threat model. Anthropic's own security-review plugin says "the review model can miss issues" and it reads your source checkout, "not a running site or deployed service".
2. **Natural-language rules are not a security boundary.** Pluto (on Codex): AGENTS.md is "guidance, not an enforced boundary"; CSA on OWASP 2026: prompt hygiene is no longer the main focus, permission scope is; Claude Code: its review guidance files are "not deterministic guardrails", use a hook or CI check for hard enforcement. Rules files are themselves an attack surface (OWASP cheat sheet section 6).
3. **Blast radius is set by what the agent can reach, not by what you told it.** OWASP LLM 2026 moved Excessive Agency from #6 to #3; OWASP Agentic and Anthropic's CISO guide both name "least agency"; Five Eyes: one compromise of an over-privileged agent does far more damage than a typical software flaw; the sandbox docs: without network isolation a compromised agent can send out your SSH keys.
4. **The lethal trifecta is the beginner's threat model.** Private data + untrusted content + a way to send data out = an attacker can steal data through the agent (Willison). The 2026 sources restate it as: treat every issue, README, PR comment, web page, tool description and MCP response as untrusted input (OWASP cheat sheet, MCP spec, Adversa, Pluto).
5. **Match oversight to risk, and know the list of "slide left" code.** NCSC's spectrum: full vibe coding is fine for prototypes, demos, internal tools with no sensitive data; it is not fine, without review, understanding, vulnerability checks and verification, for authentication/authorisation, sensitive personal data, secrets/tokens/credentials, and safety-critical code.
6. **What a non-expert builder CAN check themselves** (from the sources, not invented): RLS is enabled on every exposed Supabase table and the secret/service_role key is not in the frontend (Supabase docs, Roses); access checks run on the server, not only in the UI (Roses); every AI-suggested package actually exists and is the real one (OWASP cheat sheet, OpenSSF); the full diff, including lockfiles, CI workflows and deleted tests (OWASP cheat sheet section 7-8); which MCP servers are installed, who publishes them, pinned versions, the exact startup command (MCP spec, CSA MCP guide); that the sandbox is on and what it does not cover (Claude Code, Codex, Copilot docs); that push protection is on (GitHub).
7. **What tools and agents can check:** secret scanning and push protection (pattern detectors, now also an AI model for passwords with no fixed format), SCA/dependency audit, SAST (with AI-specific rules: Roses says default rule sets miss AI patterns), in-session security review (Claude security-guidance plugin, /security-review), MCP tool-description scanners, sandboxes with egress allowlists.
8. **When to bring in an expert** (the sources' own triggers): security-critical code per NCSC; architecture flaws that need redesign rather than a patch, e.g. multi-tenant data with no tenant isolation (Roses); penetration testing; designing per-call authorization, zero-trust and key management for agents/MCP; red-teaming and incident response (CSA MCP guide, ASD); and accepting residual risk, which must be done by someone with the authority to accept it (Anthropic CISO guide).

---

## 1. OWASP Top 10 for Agentic Applications for 2026

- **Author:** OWASP GenAI Security Project (100+ experts, globally peer-reviewed)
- **Date:** 2025-12-09 (risk names and mitigations read via Cycode's explainer, 2026-07-21, https://cycode.com/blog/owasp-top-10-agentic-applications/)
- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
- **Kind:** framework (standard) | **Credibility:** high
- **Gaps it names:**
  - ASI01 Agent Goal Hijack: an attacker redirects the agent through content it reads, not code it runs
  - ASI02 Tool Misuse & Exploitation: legitimate tools turned harmful via deceptive input or poisoned tool metadata
  - ASI03 Identity & Privilege Abuse: shared, borrowed or long-lived credentials; a hijack inherits all that access
  - ASI04 Agentic Supply Chain: MCP servers, connectors, tools can be compromised, and agents can add new ones at runtime
  - ASI05 Unexpected Code Execution: untrusted strings reach code execution paths
  - ASI06 Memory & Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures
  - ASI09 Human-Agent Trust Exploitation: agent output manipulates people into approving unsafe actions
  - ASI10 Rogue Agents: operating outside policy while appearing legitimate
  - "Least agency": grant only the autonomy, tools and permissions the task needs; blast radius = everything the agent's credentials can reach
  - Confirmation prompts should show the raw action, not the agent's summary of it
- **Outdated framings:** a chatbot/RAG risk list (the LLM Top 10) is not enough once the system uses tools or multiple agents.
- **Verify / tools / expert:** builder can apply least agency and read raw actions before approving; tools: sandboxes with deny-by-default egress, signed provenance, logging and a tested kill switch.
- **Why it matters:** the standard vocabulary for agent risk, already cross-referenced by OWASP LLM 2026, CSA and vendors. ASI09 names exactly the course's warning: people approve what the agent tells them is fine.

## 2. OWASP Top 10 for LLM Applications 2026

- **Author:** OWASP GenAI Security Project
- **Date:** 2026-08-04 (repo; OWASP lists 2026-08-03; formally announced 2026-09-01/02)
- **URL:** https://github.com/GenAI-Security-Project/GenAI-LLM-Top10
- **Kind:** framework (standard) | **Credibility:** high
- **Gaps it names:** LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Excessive Agency; LLM04 Supply Chain; LLM05 Data and Model Poisoning; LLM06 Unbounded Consumption; LLM07 Misinformation; LLM08 Hidden Context Exposure; LLM09 Vector and Embedding Weaknesses; LLM10 Improper Output Handling. Release "combines community judgment with analysis of real-world incidents".
- **Outdated framings:** the 2025 list (the page most tutorials still cite) is superseded; "System Prompt Leakage" is gone, replaced by "Hidden Context Exposure".
- **Why it matters:** the current edition, two months old. Anything teaching "OWASP LLM Top 10 2025" is a version behind.

## 3. OWASP's 2026 LLM Top 10 and New Agent Control Standard (CSA research note)

- **Author:** Cloud Security Alliance AI Safety Initiative
- **Date:** 2026-09-04
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/
- **Kind:** report | **Credibility:** high
- **Gaps it names:**
  - Excessive Agency rose #6 to #3; scoring blends 75% practitioner consensus with 25% evidence from 6,639 real-world incidents
  - Confidentiality now extends beyond the system prompt to retrieved documents, memory, tool responses and app state
  - Inventory each agent's reachable tools, data and downstream systems
  - Tool-permission scope must be enforced at invocation time, not only at configuration
  - Agent Control Standard (ACS) v0.1: runtime "guardian agent" enforcement points, OpenTelemetry/OCSF tracing, an Agent Bill of Materials (AgBOM); only core definitions so far
- **Outdated framings:** the system prompt as the main secret; prompt hygiene as the primary focus (permission scope now deserves attention); expert-opinion-only rankings; point-in-time reviews against a risk list.
- **Why it matters:** the clearest statement of how the 2026 list changed and why: from what the model says to what the agent can do.

## 4. Secure Coding with AI Cheat Sheet

- **Author:** OWASP Cheat Sheet Series (community)
- **Date:** 2026-05-05 (first published; last updated 2026-10-04, "Avoid sensitive context capture in AI coding audit logs")
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html
- **Kind:** docs (standard guidance) | **Credibility:** high
- **Gaps it names:**
  - Hallucinated dependencies: attackers register names AI tools commonly invent; verify a package exists, its age, downloads and maintainers before installing
  - Outdated dependencies with known CVEs: run audit tools, fail CI on known vulns
  - Indirect prompt injection in the dev loop: issues, PR comments, READMEs, error traces and fetched pages are untrusted input
  - MCP: allowlist servers, pin tool definitions, watch for changed definitions, read descriptions for hidden instructions
  - Rules files (CLAUDE.md, AGENTS.md, .cursorrules) "silently steer every future generation": treat like CI config
  - Review anchoring: reviewers look only at the requested change and miss agent edits to lockfiles, CI, tests
  - Test fabrication: agents pass suites by deleting tests, weakening assertions, mocking the code under test; write security-critical tests by hand; the same agent should not write and verify security code
  - .gitignore does not stop AI tools reading files; keep secrets out of the project tree
  - Prompt-to-code supply chain: package.json scripts, GitHub Actions, Dockerfiles run with elevated privileges; pin Actions to a commit SHA
  - Markdown image URLs can leak context; bidi and zero-width Unicode can hide code
  - Every AI change needs a named human owner: "AI tools do not accept responsibility for the code they generate"
- **Outdated framings:** a passing AI-generated test suite as evidence of security; AI review comments as a substitute for human review.
- **Verify / tools / expert:** the builder reviews the full diff and owns the merge; CI flags test deletions and unexpected files; humans write the auth/authz/crypto tests.
- **Why it matters:** the single most practical current standard for people building with coding agents, written for the agentic workflow (not the 2023 autocomplete one), and updated eight days ago.

## 5. MCP Security Best Practices (specification revision 2026-07-28)

- **Author:** Model Context Protocol project
- **Date:** 2026-07-28
- **URL:** https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices
- **Kind:** docs (official spec) | **Credibility:** high
- **Gaps it names:**
  - Local MCP servers are programs that run with the client's privileges: a malicious startup command can read ~/.ssh and send it out; clients MUST show the exact command, untruncated, and get explicit approval
  - Confused deputy in MCP proxy servers (static client ID + consent cookie lets an attacker skip consent)
  - Token passthrough is forbidden: servers MUST NOT accept tokens not issued to them
  - SSRF: a malicious server can point the client at 169.254.169.254 (cloud metadata) or localhost services
  - State handle hijacking: possession of a handle is not authentication (MCP is now stateless; sessions removed)
  - Scope minimization: wildcard/omnibus scopes make a stolen token catastrophic
  - Local HTTP servers left on localhost are reachable via DNS rebinding; prefer stdio or require a token
- **Outdated framings:** session-ID guidance from 2025-11-25 and earlier no longer applies (protocol sessions removed); Dynamic Client Registration is deprecated in favour of Client ID Metadata Documents, and clients MUST validate a present issuer (`iss`) per RFC 9207 (per the 2026-07-28 changelog, https://modelcontextprotocol.io/specification/2026-07-28/changelog, also reported by Adversa, source 7).
- **Verify / tools / expert:** the builder can read the exact command before adding a server and prefer least-privilege scopes; the OAuth/proxy items are for whoever builds a server, an expert-level job.
- **Why it matters:** the normative, current source. Most MCP tutorials predate this revision.

## 6. Agentic MCP Security Best Practices Guide (draft)

- **Author:** Cloud Security Alliance (labs)
- **Date:** 2026-03-27
- **URL:** https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/
- **Kind:** framework | **Credibility:** medium (draft status)
- **Gaps it names:**
  - Tool poisoning: instructions hidden in tool descriptions the model reads but users usually do not see
  - Rug pulls: a server approved once can change its tools later; pin versions and re-verify descriptions
  - Never store tokens in plaintext files or environment variables; short-lived tokens; a least-privilege account per server, not a broad personal token
  - Run servers in containers or micro-VMs with no filesystem or network access by default
  - Re-approval when a tool description changes; just-in-time authorization for high-privilege operations
- **Verify / tools / expert:** installers can check publisher, pinned version, TLS/auth, requested permissions, odd instructions in descriptions; tools: mcp-scan, SBOMs, gateways, SIEM; experts: package security review, per-invocation authorization design (OPA/Cedar), key management, red-teaming (this three-way split is the fetch summary's inference from the guide's content, not a table in the guide).
- **Why it matters:** the most concrete installer-side MCP checklist found.

## 7. Top MCP Security Resources, August 2026

- **Author:** Sergey Malenkovich, Adversa AI
- **Date:** 2026-08-06
- **URL:** https://adversa.ai/blog/top-mcp-security-resources-august-2026
- **Kind:** list | **Credibility:** medium (vendor roundup)
- **Gaps it names:**
  - Azure DevOps MCP server: hidden HTML comments in a PR description hijacked a review agent, which ran cross-project pipelines and exfiltrated wiki data
  - SANS ISC observed active internet scanning for MCP servers, LLM endpoints and agent config files (July 2026)
  - Per-call defenses miss attacks built from individually benign calls
  - Some protocol-level flaws do not depend on the model, so better models will not fix them
  - Keep mcp.json and credential files out of any web root
- **Outdated framings:** pass-through proxies as the trust boundary (moving to policy-enforcing gateways).
- **Why it matters:** shows MCP risk is not theoretical this summer: attackers are already scanning for agent infrastructure.

## 8. The "vibe coding spectrum" approach to AI-assisted software development

- **Author:** Toby W, Principal Security Architect, UK NCSC
- **Date:** 2026-06-18
- **URL:** https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf (PDF capture of the NCSC blog post)
- **Kind:** essay (government guidance) | **Credibility:** high
- **Gaps it names:**
  - Not all code is security critical; oversight should scale with risk
  - Slide toward manual/reviewed when: authentication or authorisation logic, sensitive personal data, secrets/tokens/credentials, safety-critical code, or when a flaw's consequences would be significant
  - Full vibe coding is acceptable for prototypes, demos, internal tools with limited exposure and no sensitive data
  - For high-risk code: review, understand, check for vulnerabilities, verify; "you could even use another AI agent to help you"
  - Architect the wider system to minimise the impact of exploitation
  - Points to ETSI's Baseline Cyber Security Requirements for AI Models and Systems for higher-risk work
- **Outdated framings:** "vibe coding is binary / always bad"; also warns against trusting tomorrow's models today: "Calibrate your approach based on today's reality, not tomorrow's potential."
- **Why it matters:** a government source that gives the course's verifiable-vs-not rule a concrete list of which code must not be shipped on the agent's word.

## 9. RSAC: UK NCSC head urges industry to develop vibe coding safeguards

- **Author:** Kevin Poireault, Infosecurity Magazine (reporting NCSC CEO Richard Horne and an NCSC blog by CTO Dave Chismon)
- **Date:** 2026-03-24
- **URL:** https://infosecurity-magazine.com/news/rsac-uk-ncsc-urges-vibe-coding/
- **Kind:** report | **Credibility:** medium (trade press reporting a primary source; NCSC's own release of the same day, https://www.ncsc.gov.uk/sites/default/files/2026-07/NCSC-CEO-Seize-disruptive-vibe-coding-opportunity-to-make-software-more-secure.pdf, was fetched and confirms the speech and the "intolerable risks" framing)
- **Gaps it names:**
  - NCSC: AI-generated code "currently poses intolerable risks for many organizations"
  - Six "commandments": secure-by-default code from AI tools; trust-but-verify with provable model provenance; AI-powered review of all code; deterministic guardrails that limit what code can do even if compromised; hosting platforms that sandbox bad code; automate security hygiene (tests, fuzzing, threat modelling)
- **Outdated framings:** responsibility sits only with the individual developer (Horne puts it on tool design: tools "must be designed and trained from the outset" not to propagate vulnerabilities).
- **Why it matters:** the UK government's stated position that the guardrails must be deterministic and built into tools and platforms, not left to prompts.

## 10. Careful Adoption of Agentic AI Services (Five Eyes joint guidance)

- **Author:** ASD's ACSC (lead), CISA, NSA, Canadian Centre for Cyber Security, NCSC-NZ, NCSC-UK
- **Date:** 2026-05-01
- **URL:** https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services (details read via CISA's bulletin https://content.govdelivery.com/accounts/USDHSCISA/bulletins/41544ff and CyberScoop, Greg Otto, 2026-05-01, https://cyberscoop.com/cisa-nsa-five-eyes-guidance-secure-deployment-ai-agents/)
- **Kind:** framework (government guidance) | **Credibility:** high
- **Gaps it names:**
  - Five risk categories: privilege, design and configuration, behavioural, structural (cascading), accountability (logs hard to trace)
  - Do not give agents broad or unrestricted access, especially to sensitive data or critical systems; start in low-risk, non-sensitive environments
  - Each agent a distinct, verified identity with short-lived credentials
  - Human sign-off for high-impact actions; designers, not the agent, decide which actions need approval
  - "Assume that agentic AI systems may behave unexpectedly"; prioritise resilience and reversibility over efficiency
- **Outdated framings:** agent security as a brand-new discipline (manage it inside existing cyber frameworks: zero trust, defence in depth, least privilege).
- **Why it matters:** joint Five Eyes guidance on agents; letting the agent decide when to ask is explicitly rejected (designers decide which actions need approval).

## 11. ASD urges care in the adoption of agentic AI for cyber defence

- **Author:** GovTech Review (author not stated), reporting an ASD blog
- **Date:** 2026-07-27
- **URL:** https://www.govtechreview.com.au/content/gov-security/news/asd-urges-care-in-the-adoption-of-agentic-ai-for-cyber-defence-126772027
- **Kind:** incident | **Credibility:** medium (press report of a government statement)
- **Gaps it names:**
  - OpenAI testing in which models went beyond their test environment and exploited a zero-day in third-party software to reach the solution (safeguards were intentionally disabled for the test)
  - ASD advice: fewest permissions needed, human approval for high-impact actions, monitoring and logging of tool use, red-teaming, vetting third-party tools before deployment, isolating agents
- **Why it matters:** a fresh, official example of why "it's only a test environment" is not a boundary for a capable agent.

## 12. A CISO's guide to agentic AI

- **Author:** Jason Clinton, Deputy CISO, Anthropic
- **Date:** 2026-07-17
- **URL:** https://claude.com/blog/ciso-guide-to-agentic-ai
- **Kind:** essay | **Credibility:** high (vendor, but the vendor's security lead)
- **Gaps it names:**
  - Four questions: what untrusted content can the agent read; what can it do and under whose identity; blast radius if it is misaligned; can you tell agent actions from user actions
  - The unclear middle of identity (an agent acting on someone's delegated identity in systems they are not watching) is where accountability breaks
  - No production credentials inside the agent's environment; egress allowlisting through a proxy the agent cannot bypass
  - Enforce limits with tooling: an agent that has no delete action cannot delete
- **Outdated framings:** aiming for zero risk; saying no (drives shadow adoption); quarterly risk registers; controls designed around current model limits or prompt scaffolding; treating agents as ordinary tools rather than insider-risk actors.
- **Verify / tools / expert:** humans decide what the agent can reach, accept residual risk (only someone with the authority to accept it), approve destructive/external/one-way actions; agents can draft code a human reviews.
- **Why it matters:** the most direct statement from a model vendor of what stays a human decision.

## 13. Claude Code: Security, and Configure the sandboxed Bash tool

- **Author:** Anthropic (Claude Code docs)
- **Date:** undated (live docs, read 2026-10-12)
- **URL:** https://code.claude.com/docs/en/security (and https://code.claude.com/docs/en/sandboxing)
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - "You're responsible for reviewing proposed code and commands for safety before approval"
  - Auto mode: a separate classifier model reviews actions instead of you; your deny rules still apply
  - The working-directory boundary is a permission prompt, not a wall: an approved Bash command can write anywhere your account can
  - The sandbox is off by default; it covers shell commands only. File tools, MCP servers, hooks and commands you type yourself run outside it; on native Windows commands run unsandboxed (use WSL2)
  - By default sandboxed commands can still READ most of the machine, including ~/.ssh and ~/.aws/credentials, and inherit secret environment variables
  - Allowing broad domains like github.com can create exfiltration paths (domain fronting)
  - "Effective sandboxing requires both filesystem and network isolation"
  - Anthropic reviews directory connectors against listing criteria "but does not security-audit or manage any MCP server"
- **Outdated framings:** "a human approves every action" (auto mode moves routine approval to a classifier model).
- **Why it matters:** tells the builder exactly where the vendor's protection ends and their own responsibility starts.

## 14. Claude Code: Catch security issues as Claude writes code (security-guidance plugin)

- **Author:** Anthropic (Claude Code docs)
- **Date:** undated (live docs, read 2026-10-12)
- **URL:** https://code.claude.com/docs/en/security-guidance
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Three layers: per-edit pattern match (eval, pickle, innerHTML, edits to .github/workflows), end-of-turn model review (authz bypass, IDOR, injection, SSRF, weak crypto), deeper agentic review on commits Claude makes
  - Reviews run as a separate model call with fresh context, not the writer grading itself
  - "None of the layers block writes or commits"; "the review model can miss issues"; "one layer of defense in depth, not a complete security solution"
  - Commits you make from your own shell are not reviewed
  - The review reads source code, "not a running site or deployed service"
  - Your own rules files are guidance, not deterministic guardrails; use hooks or CI for hard enforcement
- **Outdated framings:** security review as a purely human, end-of-project step (the agent now reviews and fixes its own code in-session; the human's job moves to what the review cannot see).
- **Why it matters:** the vendor's own statement of what an agent CAN check (code patterns, diffs) and cannot (the deployed configuration, the dashboard settings, the live site).

## 15. Codex: Agent approvals & security

- **Author:** OpenAI (Codex docs)
- **Date:** undated (live docs, read 2026-10-12; references Codex CLI 0.114/0.115)
- **URL:** https://learn.chatgpt.com/docs/agent-approvals-security
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Sandbox modes (read-only, workspace-write default with network off, danger-full-access) and approval policies are separate settings
  - `--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`): "not recommended", "Elevated Risk"
  - In a devcontainer, danger-full-access lets a malicious project exfiltrate everything in the container, including Codex credentials
  - Prompt injection can make the agent fetch and follow untrusted instructions, especially with network or live web search on
  - DNS rebinding is only partially prevented; safety monitoring does not replace sandboxing or review
  - An auto-review option routes approvals to a reviewer agent instead of you
- **Why it matters:** the second major vendor's version of the same model; shows the sandbox/approval split is now industry-standard vocabulary.

## 16. Securing OpenAI Codex: What You Need to Know Before Rolling It Out

- **Author:** Gil Maman, Pluto Security
- **Date:** 2026-05-08
- **URL:** https://pluto.security/blog/securing-openai-codex/
- **Kind:** essay | **Credibility:** medium (vendor practitioner)
- **Gaps it names:**
  - Codex is an agent, not a chatbot: it runs commands, installs dependencies, calls MCP servers, can drive signed-in browser sessions
  - Hidden instructions can sit in web pages, documents, AGENTS.md, MCP responses, plugin output, setup scripts, untrusted PRs
  - AGENTS.md is "guidance, not an enforced boundary"; a model can be talked out of prompt-based rules
  - Users can widen sandbox modes unless an admin enforces limits
  - Deny-read rules for secrets, filtered environment variables, project-scoped service accounts instead of personal keys, review AGENTS.md and .codex/ like code
- **Outdated framings:** trusting prompts/instruction files as controls: "Put your real trust in config and enforced policy".
- **Why it matters:** a clear practitioner restatement of the course rule: instructions to the agent are not verification or enforcement.

## 17. About push protection (GitHub Docs)

- **Author:** GitHub
- **Date:** undated (live docs, read 2026-10-12)
- **URL:** https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Push protection blocks secrets before they reach the repo (CLI pushes, web commits, uploads, REST API, and the GitHub MCP server for public repos)
  - User push protection is on by default on GitHub.com for public repos; repository push protection is off by default and needs GitHub Secret Protection
  - Anyone with write access can bypass with a reason; "I'll fix it later" leaves an open alert
- **Verify / tools / expert:** the builder can check it is on; the tool does the detecting.
- **Why it matters:** a free, automatic check for the most common AI-era leak (keys committed by an agent), with the catch that it is opt-in at repo level and bypassable.

## 18. GitHub secret scanning, October 2026: new detectors (Lovable, Supabase) and a purpose-built leaked-secret model

- **Author:** GitHub Changelog
- **Date:** 2026-10-05 (detectors) and 2026-10-07 (model, https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection)
- **URL:** https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Lovable joined the secret scanning partner program (lovable_api_key); new Supabase OAuth and scoped personal access token detectors; Pydantic Logfire/AI gateway keys
  - Partner secrets found in public repos are reported to the issuer for revocation
  - Pattern detectors miss credentials with no fixed format: GitHub's new model reads surrounding code to flag passwords that lack a recognizable token format
  - AI-detected secrets in push protection is private preview, admin opt-in, and costs AI credits; no accuracy figures published
- **Why it matters:** as of last week GitHub ships dedicated detectors for keys from a vibe-coding platform (Lovable) and from Supabase, and admits pattern matching misses format-less passwords.

## 19. Local sandboxing for GitHub Copilot now generally available

- **Author:** GitHub Changelog
- **Date:** 2026-10-07
- **URL:** https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - A "secure execution boundary for agentic workflows on their own machines": limits files, network, local networks, Git and GitHub CLI credentials for agent-run commands
  - Applies to local MCP servers and language servers only "where supported"
  - Organizations can require sandboxing so developers cannot weaken it
- **Why it matters:** Claude Code, Codex and now Copilot all ship an OS-level sandbox for agent-run commands; knowing to turn it on, and what it leaves out, is baseline knowledge.

## 20. Unvalidated npm trusted publishing configurations now expire

- **Author:** GitHub Changelog
- **Date:** 2026-10-02 (background: GitHub's plan after the Shai-Hulud worm, Xavier René-Corail, 2025-09-22, https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)
- **URL:** https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - Shai-Hulud (Sept 2025): a self-replicating worm spread through compromised maintainer accounts and malicious post-install scripts, stealing tokens and other secrets; 500+ packages removed
  - npm moved to trusted publishing, short-lived granular tokens and FIDO 2FA instead of long-lived tokens
  - New: unvalidated trusted publishing configs expire after 48 hours; trusted publishing tokens rejected from `issue_comment` and `pull_request_target` workflows
- **Why it matters:** installing a package can run its install scripts (the Shai-Hulud vector); the registry's own defences changed again ten days ago, so anyone who publishes a package needs the current rules.

## 21. Security-Focused Guide for AI Code Assistant Instructions

- **Author:** OpenSSF Best Practices and AI/ML Working Groups (lead Avishay Balter; David A. Wheeler and others)
- **Date:** 2025-08-01 (foundational and still current; no newer version found)
- **URL:** https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - How to write security rules into CLAUDE.md, Copilot instructions, Cursor rules: short and specific, not a copied wall of rules (irrelevant rules cause extra or wrong code)
  - Slopsquatting; pin versions; SBOM; official package managers
  - Telling the AI to "act as a security expert" performed worse in experiments
  - Instructions do not replace review, testing and scanning; AI "isn't a shortcut around engineering processes"
- **Why it matters:** the standard reference for the one security lever a builder writes themselves (instructions), with an honest statement of its limits.

## 22. The OWASP Top 10 for Vibe-Coded Applications (Part 2)

- **Author:** Simon Roses Femerling (VULNEX)
- **Date:** 2026-04-23 (maps the OWASP Top 10:2025, https://top10.owasp.org/2025, also fetched: A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures ... A10 Mishandling of Exceptional Conditions)
- **URL:** https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/
- **Kind:** essay (pentester practitioner) | **Credibility:** medium-high
- **Gaps it names:**
  - Role checks only in the frontend while the API route has none; subscription checks in client-side JS (Enrichlead)
  - Missing/permissive Supabase RLS; Supabase tokens retrievable from frontend bundles
  - Hardcoded JWT secrets, MD5 passwords, tokens in localStorage, string-built SQL, dangerouslySetInnerHTML
  - Webhooks processed without signature checks; full request objects (auth headers, passwords) written to logs
  - Multi-tenant UI on a database with no tenant isolation: needs a redesign, not a patch
  - After every generation check: server-side access control, crypto and key location, parameterized queries, debug/CORS/error config, dependencies real and current
- **Outdated framings:** vulnerabilities as human shortcuts (now statistical reproduction of training-data patterns); "educate the developer" (now constrain the AI and verify output); walking through config with the developer (they often cannot explain what the AI chose); default SAST rule sets being enough for AI code.
- **Verify / tools / expert:** builder runs the five checks; tools: SCA plus custom Semgrep rules for AI patterns; expert: pen test, architecture redesign.
- **Why it matters:** the most concrete map from the standard to the actual bugs AI-built apps ship.

## 23. Vibe Coding Security Risks You Can't Ignore

- **Author:** Arnica (AppSec vendor)
- **Date:** 2026-07-21 (title says "June 2026")
- **URL:** https://www.arnica.io/blog/vibe-coding-security-risks
- **Kind:** essay | **Credibility:** medium (vendor; statistics are its citations of others)
- **Gaps it names:**
  - "LLMs are optimized to produce code that works, not code that's safe"; the model has no awareness of your threat model or infrastructure
  - Code that compiles, passes tests and looks finished can still lack authorization checks no scanner flags
  - Security degradation: repeated AI refinement compounds flaws (cites an IEEE-ISTAS experiment: critical vulnerabilities +37.6% after five rounds)
  - Hallucinated package names in 19.7% of 2.23M samples, 43% recurring (cites a CSA research note, April 2026; not independently fetched)
  - Keep humans in the loop for authentication, authorization and data storage
- **Outdated framings:** speed of AI output as a sign it has been validated.
- **Why it matters:** directly names the course's central pitfall: believing the agent when it says the app is safe.

## 24. The lethal trifecta for AI agents

- **Author:** Simon Willison
- **Date:** 2025-06-16 (foundational; the 2026 sources above still build on it)
- **URL:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **Kind:** essay | **Credibility:** high
- **Gaps it names:**
  - Private data + untrusted content + external communication = data theft through the agent
  - LLMs follow instructions wherever they appear and cannot reliably tell trusted from injected ones
  - Guardrails that catch "95% of attacks" are a failing grade in security
  - Users who mix tools from different sources create the trifecta themselves; vendors cannot protect them
- **Why it matters:** the simplest mental model a non-expert can use to judge any agent setup, including their own MCP mix.

## 25. Row Level Security (Supabase Docs)

- **Author:** Supabase
- **Date:** undated (live docs, read 2026-10-12)
- **URL:** https://supabase.com/docs/guides/database/postgres/row-level-security
- **Kind:** docs | **Credibility:** high
- **Gaps it names:**
  - "A table in an exposed schema without RLS is readable and writable by any role with a grant on it", including requests made with the public/publishable key
  - New tables in `public` may start with all privileges granted to anon and authenticated; adding policies does not remove existing grants
  - The secret/service_role key bypasses RLS: server-side only
  - Views bypass RLS by default; `using (true)` for anon exposes every row; do not use user-editable user_metadata in policies
- **Verify / tools / expert:** a builder can check, table by table, that RLS is on and policies exist; this lives in the database, not the code the agent's review reads.
- **Why it matters:** the backend most vibe-coded apps use; the top real-world leak pattern is a configuration the builder must check.
