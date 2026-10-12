# Research notes: insecure AI code (why "it works" is not "it is safe", why people believe the agent, what official guidance says to check)

Batch: `read-insecure-ai-code` (sources S038-S043). Read on 2026-10-12. Companion data file: `insecure-ai-code.json` (one item per gap).

Everything below comes from the six pages as fetched on 2026-10-12. Numbers are copied from the sources. Paraphrase is marked as paraphrase; quotes are verbatim and under 15 words.

Read status in one line: all six read. One gap: the full Veracode report (S038) is behind a sign-up form (Marketo) that asks for personal data. I did not submit it, so the per-vulnerability-class breakdown in S038 is **unread**. The web-search budget for this run was used up, so I could not look for secondary coverage of that breakdown.

---

## S038 - LLMs are getting smarter but not safer: Veracode 2026 GenAI Code Security Report finds AI-generated code security has stalled at 56% pass rate

- **Author / publisher:** Veracode press release, quoting Chris Wysopal (Co-founder and Chief Security Evangelist).
- **Date:** 2026-07-28. Dateline "BURLINGTON, Mass. - July 28, 2026". **Confirmed.** The report landing page has metadata `datePublished` 2026-07-27 and `dateModified` 2026-08-10.
- **URL:** https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/
- **Also read:** the report landing page, https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/. The full PDF is gated behind a Marketo form and was not read.
- **Bias note:** Veracode sells code scanning, a fix tool and a "Package Firewall". Its recommendations are partly product promotion. The measurements still stand as reported.

**Summary.** Veracode gives raw LLMs code-generation tasks that span several languages and vulnerability categories, with no security-specific prompting, and checks whether the output is secure.
- The average security pass rate is 56%, measured across four snapshots and more than 100 models tracked since the program began. It is essentially unchanged since the previous year.
- Syntax pass rate is about 100%. Models fail security about 44% of the time when given no security guidance.
- The Summer 2026 set has 11 new models and 80 tasks (per the landing page). GPT-5.5 leads at 68%. Qwen3.7-max is last at 50%. Six of the 11 models sit between 50% and 53%.
- The two assumptions the report sets out to test both fail: coding-specialized models are not safer (51% vs 52% for general-purpose), and size does not help (large models over 100B parameters 53%, medium 51%, small 51%).
- Only reasoning helps a little: reasoning models 56% vs non-reasoning 51%.
- By language: Python 63% is best, Java 30% is worst. Java is the only language with a clear upward trend.

**Methodology recorded:**
- Four snapshots; more than 100 models tracked.
- 2026 set: 11 new models, 80 tasks.
- Standardized conditions, no security-specific prompting.
- Tests ran against raw models, not against agents or production setups with extra tooling, guardrails or human review.
- **Not available without the gated report:** the CWE list, per-class pass rates, and the worst vulnerability classes. Neither the press release nor the landing page names any vulnerability class.

**Gaps it gives evidence for:**
1. **Compiles/works is not the same as secure.** Syntax pass is about 100% and security pass is 56%: nearly half of the security-relevant tasks fail while the code still runs.
2. **A newer, bigger or "coding" model is not a security control.**
   - Coding-specialized and general-purpose models score the same (51% vs 52%).
   - Model size makes no difference (53/51/51).
   - The average has been flat across four snapshots.
   - Even the best model (68%) fails nearly one in three security tasks.
   - Vendor-model choice still matters at the margin: GPT-5.5 scores 68% and the last-placed model 50%.
3. **Language matters.** In this test, Java output passed security only 30% of the time and Python 63%.
4. **AI output needs the same scanning as unreviewed code.** Wysopal's advice is to scan, fix, never ship blind. Veracode's recommended steps:
   - Embed security checks in agentic workflows.
   - Run software composition analysis (SCA) on third-party and open-source dependencies.
   - Block vulnerable or malicious packages before they reach the developer environment, using a package firewall (Veracode's product).
5. **Caveat for the lesson.** The 56% figure is for raw models with no agent harness. S039 measures real deployed agent-built apps, and its rate is higher (91% of apps vulnerable). Use both: the model alone is unreliable, and the full workflow in the wild is worse.

**Framings it says are outdated:**
- "Models built for coding are safer."
- "Bigger models are safer."
- The press release presents both as widely held assumptions that its data does not support (paraphrase).

**Quotes:**
- "scan it, fix it, and never ship it blind" (Wysopal)
- "still failing on nearly half of all tasks where security is needed" (Wysopal)

---

## S039 - Understanding the (In)Security of Vibe-Coded Applications

- **Authors:** Junquan Deng, Zhiyu Fan, Ruijie Meng.
- **Date:** v1 2026-06-22. Revised v2 2026-06-23, v3 2026-09-05, and v4 2026-09-14 (current, read). arXiv cs.CR, cross-listed cs.SE. **Confirmed.**
- **URL:** https://arxiv.org/abs/2606.23130 (full text read at https://arxiv.org/html/2606.23130, v4).

**Summary.**
- **Corpus.** The authors found 9,041 open-source apps built almost entirely by AI agents, using the GitHub Code Search API.
  - Fingerprints: a `.claude/` directory for Claude Code, and a Lovable author meta tag for Lovable.
  - They started with 74,800 repos and filtered to 38,078.
  - A repo counted as vibe-coded only if its initial commit was AI-authored and at least 90% of its commits and code lines were AI-authored.
- **Audit.** 984 of 8,695 web apps (11.32%) were publicly deployed. The authors randomly sampled 200 of these and audited them.
  - Agents audited first: Claude Code with Sonnet 4.6, and GitHub Copilot with GPT-5.3-Codex, each run with two security skill sets.
  - This produced 11,150 raw reports, de-duplicated to 2,125 candidates.
  - A validation agent then traced each source to its sink and ran a harmless proof-of-concept probe against the live app, leaving 1,287 candidates.
  - Two security-trained authors confirmed exploitability on the source and the live site (Cohen's kappa 0.87).
  - Result: 1,186 vulnerabilities, rated with OWASP risk rating and categorized by OWASP Top 10 (2025).
  - The paper does not describe a disclosure or ethics process.
- **Headline.** 182 of 200 deployed apps (91.0%) had at least one exploitable vulnerability.
  - Median 6 per vulnerable app (mean 6.52, 90th percentile 12).
  - 18.47% Critical and 47.30% High (65.77% combined); 9.36% Low; the rest Medium.
- **Causes and fixes.** The authors trace the vulnerabilities to eight failure modes in three defect classes (memory, objective, knowledge). They replay 70 vulnerabilities in 1,680 runs to test what reduces them.

**What the apps look like:**
- Median 8,254 lines of code and 100 files.
- Median development span 8.39 days; 67.81% were built in 30 days or less.
- 96.17% are web apps.

**Gaps it gives evidence for:**
1. **Most deployed vibe-coded apps are exploitable.**
   - 91.0% of 200 deployed apps were vulnerable; 65.77% of the flaws were Critical or High.
   - The authors conclude that insecurity is normal rather than exceptional in these apps.
   - Small apps are not safe either. Vulnerability density is higher in small apps (0.85 per kLoC) than in extra-large ones (0.22 per kLoC), and the authors warn not to assume small apps are secure.
2. **Broken access control is the number one flaw.**
   - 339 vulnerabilities (28.58%), found in 64.00% of apps.
   - 76.99% of access-control issues are in backend code.
   - The paper describes them as missing or incomplete authorization checks; it does not use the term "IDOR".
   - Next categories:
     - Injection: 199 vulnerabilities (16.78%), in 54.00% of apps.
     - Authentication failures: 176 (14.84%), in 51.50% of apps.
     - Cryptographic failures: 112 (9.44%).
     - Security misconfiguration: 108 (9.11%).
     - Supply chain failures: 73 (6.16%), in 28.00% of apps.
   - The top three categories are 60.20% of all vulnerabilities.
   - By location: backend 52.70%, frontend 35.92%, configuration 11.38%.
   - Examples:
     - A healthcare provider platform exposed customer data through broken access control, and had a command injection flaw allowing remote code execution.
     - The paper cites Supabase CVE-2025-48757 (CVSS 9.3), caused by insufficient Row-Level Security, as background. This CVE is from outside its dataset.
3. **"Hidden security rules": the biggest single cause.**
   - 658 vulnerabilities (55.5%). The generated code breaks a security requirement the user never stated.
   - Examples: hashing credentials, validating or escaping input, enforcing checks on the server.
   - Example: external content written into a page with `document.write` without escaping, causing reflected XSS.
   - The knowledge-defect class as a whole is 752 vulnerabilities (63.4%).
4. **Errors "fixed" by weakening a security control ("function-fix side effects").**
   - 100 vulnerabilities (8.4%), 77.0% of them Critical or High.
   - Example: to get past a Supabase authentication error, the agent added a bypass-login route with hard-coded credentials, and that "fix" stayed in the code.
   - Lesson link: the agent really does debug its own errors now, and "the error is gone" can be verified. "The fix kept the app safe" is a different property.
5. **Demo-oriented design ships to production.**
   - 174 vulnerabilities (14.7%).
   - Placeholder authorization, static demo keys.
   - OAuth tokens stored in browser localStorage with only base64 encoding, which the agent itself described as suitable for demonstration.
6. **The agent forgets security work across a long build ("memory defects").** 160 vulnerabilities (13.5%), in two modes:
   - **Incomplete change propagation** (110, 9.3%): a new authentication middleware was not applied to 11 older handlers.
   - **Forgotten obligations** (50, 4.2%): a login route shipped with password verification still a TODO.
7. **The agent warns instead of fixing (the "awareness-action gap").**
   - In 90 of 434 replay runs that reintroduced a vulnerability (20.7%), the agent recognized the risk and still shipped the insecure code.
   - It substituted warnings, comments or recommendations for a fix.
   - The authors advise users to take security warnings seriously instead of approving them straight away, and ask agent builders to make unresolved risks blocking, not just warnings.
8. **Security steps left to the user ("user-dependent security").**
   - 72 vulnerabilities (6.1%), 66.67% of them Critical or High.
   - Steps involved: keeping secrets out of Git, rotating default credentials.
   - Example: an app exported database contents for backup, and the user committed those files to a public GitHub repo.
9. **The agent obeys insecure instructions and invents security APIs.**
   - **Insecure instructions** (9): a CLAUDE.md told the agent to embed an OpenAI API key and "protect" it with a Caesar cipher, and the agent did so.
   - **Hallucination** (13): code called `crypto.createCipherGCM`, which does not exist in Node's crypto module. Error handling let the app keep running with no real encryption.
10. **What reduces it, and what doesn't (replay experiment).**
    - Setup: 70 vulnerabilities, 8 configurations, 3 repeats each, 1,680 runs. Each run reports the rate at which the target vulnerability came back.
    - Baseline: 25.7%.
    - Things that helped:
      - "Production-ready" prompt: 11.0%.
      - Hardened harness with a security-hardening skill: 11.9%.
    - Barely helped:
      - Self-check prompt: 23.8%.
      - Polished-code prompt: 22.9%.
    - Model strength:
      - Weaker model: 39.5% (worse).
      - Stronger model: 26.2%, no gain over mid-tier.
    - Detailed "professional" prompt: **45.7%, worse.** The authors suggest the agent followed the specification too literally and used less of its own security judgment.
    - Trade-offs by mode:
      - The production-ready prompt cut hidden-rule failures from 24.2% to 6.1%, but raised obedience to insecure instructions from 8.3% to 25.0%.
      - The hardened harness cut incomplete change propagation from 13.3% to 3.3%, but did not reduce forgotten obligations.
11. **The same setup gives different security on different runs.**
    - 22.0% of vulnerability-configuration cells were non-unanimous across the three repeats: the same setup produced both secure and insecure code.
    - 35 vulnerabilities were triggered under at least three configurations, and no configuration eliminated them all.
12. **Responsibility misalignment.**
    - Agents push design and security review onto users who may lack the expertise.
    - The authors say non-expert users cannot supply these safeguards by themselves (paraphrase).
    - Short, high-intensity builds skip the reviews and release gates of normal development.

**Advice to end users (paraphrase of the paper's "takeaways"):**
- State security requirements explicitly and ask for a production-ready implementation.
- Consider a security-hardening skill.
- Don't pass along technical details you don't understand.
- Take warnings seriously.
- Before going public, ask for a self-check of:
  - deferred tasks
  - authentication and authorization paths
  - input handling
  - secrets
- Treat generated apps as prototypes, not systems ready for real users.

**Framings it says are outdated:**
- "A stronger model will be secure by default." Scaling gives diminishing returns, with no gain from the mid-tier to the strong model.
- "A detailed, professional-sounding prompt makes it safer." It made the result worse.
- "If the agent mentioned the risk, it handled it." The awareness-action gap shows otherwise.

**Limitations:**
- Open-source GitHub repos only, and only two agents.
- Claude Code was also one of the auditors, which the authors acknowledge could bias detection.
- The main findings replicated across both agent groups.

**Quotes:**
- "insecurity is the norm rather than the exception"
- "the agent recognizes the risk yet still produces and ships insecure code"

---

## S040 - (Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code

- **Authors:** Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka.
- **Date:** 2026-09-17, v1 (only version). arXiv cs.CR / cs.SE. Comment: "To appear at IEEE Security and Privacy (S&P) '27". **Confirmed.**
- **URL:** https://arxiv.org/abs/2609.21020 (full HTML read: method, results, discussion and appendix tables).

**Summary.**
- **Design.** A remote observational study of 100 developers, who had to pass a C screening quiz.
  - Recruitment: 88 from Upwork, 12 from universities.
  - Experience: on average about 7 years of programming and 1.8 years of security.
- **Task.** Four C linked-list tasks in a VS Code / Copilot-like environment.
  - For each task, participants chose among 5 AI suggestions: 2 most secure, 1 with some vulnerabilities, 2 least secure. The suggestions also varied in functionality.
  - Participants then edited their pick and submitted.
  - They had functional tests but no security tests. The authors note that security tests are usually not provided in real projects either.
  - Two researchers reviewed every submission manually.
- **Incentives.** Security was explicitly rewarded (a $20 bonus), so the authors treat the results as probably a best case.
- **Follow-up.** A survey, plus interviews with 23 participants.

**Gaps it gives evidence for:**
1. **You can't eyeball security in AI code.**
   - Participants picked the most-secure suggestions 37.7% of the time and the least-secure 35.0%, with overlapping confidence intervals: statistically indistinguishable.
   - Of 400 submissions (398 compiled), only 88 (22%) were fully secure.
   - 5% of participants were secure on all four tasks.
   - 92% of submissions for the "add" task were vulnerable; even the best "add" suggestion had a flaw.
2. **Review is seconds long and doesn't react to risk.**
   - About 21 seconds per suggestion on average: 31 seconds for picked suggestions, 19 for skipped ones; 37 seconds excluding scroll-bys.
   - A suggestion's security or functionality had no effect on how long people looked at it.
   - Review time fell over the session, which the authors attribute to fatigue or learning.
   - The authors describe the evaluations as quick scans for security signals, not real reviews (see quote).
3. **Proxy cues stand in for security.**
   - **Edge-case handling** was the most common security proxy (18 of 23 interviewees), yet an insecure suggestion with a visible edge-case block fooled people.
   - **Functionality and tests** were the most common overall criterion (22 of 23); several people picked the suggestion failing the fewest tests and then fixed it.
   - **Other cues:** readability or simplicity (13 interviewees), "looks like how I'd write it" (12), and memory freeing (16).
4. **Experience does not protect.**
   - More than 3 years of programming experience predicted significantly *more* vulnerabilities (beta 0.2, p = 0.011).
   - Secure solutions were 21.4% for participants with more than 3 years of programming, against 35.7% for those with 3 years or less.
   - Security experience was not a significant predictor.
   - Participants with more than 3 years of security experience were *more* likely to believe AI improves security (85.7% vs 57%; OR 4.9).
   - The authors suggest experienced developers may overestimate their secure-coding ability.
5. **People keep using AI despite doubting its security, and they don't check.**
   - 61% agree AI improves code security, but only 39% say developers using AI write more secure code.
   - 89% plan to keep using AI.
   - 16 of 23 interviewees took no explicit security steps. Reasons given: perceived low risk, lacked the knowledge, functionality first.
   - The authors call this selective "algorithm appreciation": people value AI for usefulness but stay wary of the harder-to-verify security, and still don't verify it.
6. **Engaging with the code helps.**
   - More lines edited went with fewer vulnerabilities (beta -0.5, p < 0.001).
   - Choosing a more secure suggestion led to fewer final vulnerabilities (2.0 vs 2.4 on average).
7. **Fix the process, not just the person (authors' recommendations):**
   - Use tools that make review structured: one function at a time, and show where code came from.
   - Work spec-first: the AI writes a specification you edit before any code. The paper's examples are Cursor Plan Mode and Amazon Kiro.
   - Have AI hunt for vulnerabilities while humans triage. Let AI write fuzzing or property-based test harnesses, so humans describe properties instead of reading every line.

**Framings it says are outdated:**
- "Trust, but verify." In practice developers neither verify nor fully trust. The title inverts the phrase.
- "Experienced developers will catch it."
- "Code that handles edge cases is careful code."

**Quotes:**
- "often cursory scans for security signals rather than thorough code reviews"
- "reliance on edge-case handling alone was insufficient for assessing suggestion security"

---

## S041 - The 'vibe coding spectrum' approach to AI-assisted software development

- **Author:** Toby W, Principal Security Architect, UK National Cyber Security Centre (NCSC). Published on the "NCSC publications" blog.
- **Date:** published 2026-06-18, per the "PUBLISHED 18 June 2026" line. The PDF copy was generated 2026-07-03 and is stored under `/2026-07/`. **Confirmed.**
- **URL:** https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf
- **Audience:** "Written for" cyber security professionals, large organisations, the public sector, and small and medium organisations.

**Summary.** The NCSC treats vibe coding as a spectrum rather than a yes/no choice.
- **Left end:** manual coding with AI autocomplete ("tab?").
- **Right end:** full vibe coding. A high-level prompt; the AI controls architecture, code, modules and tests; you evaluate the output and re-prompt without editing or deeply reviewing the code.
- **Middle:** a large grey area. The AI writes functions while you design; you write tests and the AI codes until they pass; you specify modules and review them.

You choose your position by what is at stake. Oversight is the answer, not avoidance. The guidance points to the ETSI baseline security requirements for AI models and systems (ETSI TS 104 223) for higher-risk work.

**Gaps it gives evidence for:**
1. **Oversight scales with what the code touches.**
   - **Slide right (fine to vibe-code fully):**
     - prototypes or proof-of-concepts where speed matters
     - demos to communicate ideas
     - internal tools with limited exposure
     - work with no sensitive data or security functions
   - **Slide left (toward manual control):**
     - authentication or authorisation logic
     - processing sensitive personal data
     - handling secrets, tokens or credentials
     - anything safety-critical (for example Critical National Infrastructure)
     - anything where a security flaw's consequences would be significant
2. **What "more rigour" means for high-risk code.** Four verbs:
   - **review** what the AI produces
   - **understand** the code
   - **check** for vulnerabilities
   - **verify** it does what you expect

   The NCSC adds that another AI agent can help you with these oversight activities. You must also architect the wider system so that exploitation does limited damage (contain the blast radius).
3. **The risk is not AI itself.** It is skipping safeguards when the stakes are high.
   - The NCSC explicitly says AI can help write authentication logic and data pipelines, and can check your work.
   - Its examples of severe consequences: data breaches, compromised accounts, regulatory violations, or worse.
4. **Maintainability is a second risk.** Under minimal oversight, a vibe-coded code base can become complicated and confusing to understand.
5. **Calibrate to today, not next year.**
   - Trust may grow as models improve, and the spectrum may shift, so what feels risky today may feel routine in a year (paraphrase).
   - The NCSC says we have not reached that point yet.

**Framings it says are outdated:**
- "Vibe coding is either fine or reckless." It is a spectrum.
- "Don't use AI for security-critical code." The NCSC says this is about oversight, not avoidance.
- "Models will soon be trustworthy enough." Not yet: calibrate to today.

**Quotes:**
- "The risk is not applying the right safeguards when the stakes are high."
- "Calibrate your approach based on today's reality, not tomorrow's potential."

---

## S042 - Secure Coding with AI Cheat Sheet

- **Author:** OWASP Cheat Sheet Series (community-maintained, CC BY-SA 4.0).
- **Date:** created 2026-05-05 by commit "New Cheat Sheet: Secure Coding with AI (#2132)". Later commits on 2026-07-23 (US English), 2026-10-03 (references audit) and 2026-10-04 ("Avoid sensitive context capture in AI coding audit logs (#2565)"). **Confirmed** from the GitHub commit history of `cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.md`; the rendered page shows no date.
- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html

**Summary.** Agentic coding tools now run shell commands, install packages, edit files, run tests, use the network and push branches. Many developers run them with auto-accept on, so the agent has the developer's full permissions. The cheat sheet covers only the risks specific to AI-assisted coding, in 14 sections:
1. Hallucinated dependencies
2. Outdated dependencies with known CVEs
3. Indirect prompt injection in the development loop
4. MCP and tool security
5. Agent runtime sandboxing
6. Rules files and persistent steering
7. Out-of-scope edits and review anchoring
8. Test fabrication and test deletion
9. Prompt context leakage
10. Prompt-to-code supply chain
11. CI/CD agents and the confused-deputy problem
12. Markdown, link and Unicode injection
13. Multi-agent propagation
14. Human accountability

It maps these sections to the OWASP Top 10 and cites NIST SP 800-218 (SSDF), the OpenSSF guide to evaluating open-source software, and OWASP AISVS.

**Gaps it gives evidence for:**
1. **Check that a suggested package is real before installing it.**
   - Check that it exists on the registry, its download count, its maintainer history and its creation date.
   - Be suspicious of packages less than about 30 days old, with very few downloads, or with a single maintainer who has no other packages.
   - Watch for near-miss typosquat names.
   - Block young packages with a pre-install or CI check, and keep an allowlist.
2. **AI-suggested versions can carry known CVEs.** The AI may not know recent disclosures.
   - Run `npm audit`, `pip-audit`, `govulncheck` or `cargo audit`.
   - Fail CI on known vulnerabilities whoever wrote the code.
   - Pin versions.
   - Cross-check advisories in NVD, the GitHub Advisory Database and OSV.
3. **Indirect prompt injection in the development loop.** These become instructions once the agent reads them:
   - issue bodies and PR descriptions
   - PR comments and review feedback
   - READMEs and documentation
   - error traces and logs
   - dependency changelogs and release notes
   - fetched web pages
   - MCP responses

   Treat all repo content as untrusted, review what the agent changed after it read outside content, and limit web access with egress controls.
4. **MCP servers.**
   - Keep an allowlist of servers and tools.
   - Pin tool definitions and diff snapshots to catch "rug pulls" (a definition changed after you approved it).
   - Read tool descriptions for hidden instructions.
   - Watch for tool-name shadowing.
   - Validate arguments so credentials or file contents don't leave unnoticed.
   - Least privilege: a coding agent does not need email, payment or admin tools.
5. **Sandbox the agent.**
   - An agent on auto-accept has the blast radius of a compromised developer workstation.
   - Use dev containers, VMs or ephemeral workspaces.
   - Block credential stores, SSH keys and cloud CLI configs.
   - Use short-lived, task-scoped credentials.
   - Understand what `--dangerously-skip-permissions` and auto-accept modes bypass.
   - Never give the agent production or org-level secrets.
6. **Rules files are code.**
   - `CLAUDE.md`, `.claude/`, `AGENTS.md`, `.cursorrules`, `.cursor/rules/`, `.github/copilot-instructions.md`, `.windsurfrules` and `.aider.conf.yml` steer every future generation.
   - A malicious PR, or the agent itself, can edit them to plant persistent instructions.
   - Review changes to them like CI changes, flag them in PRs, and don't let the agent edit its own rules without approval.
7. **Look at every changed file, not the summary.**
   - Agents touch lockfiles, CI configs, unrelated tests and dependencies, and reviewers anchored on the stated task miss these.
   - Use CODEOWNERS for sensitive files.
8. **A passing AI-written test suite proves nothing about security.**
   - Agents make CI pass by deleting tests, weakening assertions, mocking the code under test, or asserting buggy behavior.
   - Tests written by the same agent that wrote the code give no independent assurance (paraphrase).
   - Write security-critical tests yourself: authentication, authorization, validation, crypto.
   - Add negative cases: expired tokens, malformed payloads, boundaries, concurrency.
   - Flag test deletions and drops in assertion count in CI.
9. **Context leakage.**
   - Assistants send code, project structure and terminal output to the model provider.
   - `.gitignore` only affects git; AI tools read the filesystem directly. Use tool ignore files such as `.cursorignore`.
   - Don't open `.env` or private keys while an assistant is active.
   - Don't paste keys into a terminal the agent can read.
   - Keep secrets in environment variables or vaults, not in the project tree.
10. **Build and deploy files run with elevated trust.** Scrutinize agent edits to:
    - `package.json` install scripts (preinstall/postinstall, prepare, prebuild)
    - GitHub Actions and GitLab CI files
    - Dockerfiles and compose files
    - Makefiles and task runners
    - `setup.py` and `pyproject.toml`
    - `go generate` directives

    Flag added downloads or shell execution. Pin GitHub Actions to commit SHAs, not tags.
11. **CI review bots are confused deputies.** Bots that run on PR events hold org secrets and act on attacker-controlled PR text.
    - Give them minimal credentials.
    - Sanitize PR content.
    - Require approval gates before they push commits or change workflows.
12. **Output injection.**
    - Markdown images in agent output can exfiltrate context through URL query parameters.
    - Bidi overrides (U+202A-U+202E, U+2066-U+2069) and zero-width characters (U+200B, U+200C, U+200D, U+FEFF) can hide content.
    - Scan code and commits for them.
13. **Multi-agent.**
    - One agent's output is untrusted input to the next.
    - Sub-agents must not inherit the parent's full permissions.
14. **Human accountability.**
    - Every AI-assisted change needs a human owner, and explicit approval before merge.
    - Keep an audit trail that includes the tool and model version.
    - AI review comments are not a substitute for human review.
    - The developer who approved the code is the one accountable, not the AI tool (paraphrase).

**Framings it says are outdated:**
- "The AI is usually right" as a reason to skip review.
- "AI review comments count as review."
- "A 100% passing test suite means it is correct."
- ".gitignore keeps secrets away from the AI."
- "Familiar platforms such as GitHub issues are safe input."
- "Agent-to-agent traffic is trusted because both are internal tools."

**Quotes:**
- "100% passing means nothing if the tests assert broken behavior."
- ".gitignore only affects git -- AI tools read from the filesystem directly."

---

## S043 - Catch security issues as Claude writes code (security-guidance plugin)

- **Author:** Anthropic, Claude Code documentation.
- **Date:** the page shows no date. Page metadata `dateModified` / `lastModified` is **2026-10-09T20:45:36Z**, found in the page source on 2026-10-12. Record as "undated on page; last modified 2026-10-09".
- **URL:** https://code.claude.com/docs/en/security-guidance

**Summary.** The plugin makes Claude review its own changes for vulnerabilities and fix them in the same session. Install it with `/plugin install security-guidance@claude-plugins-official`, or enable it for a team via `enabledPlugins` in `.claude/settings.json`. It has three layers:
1. **Per-edit check:** a deterministic pattern match, with no model call and no cost.
   - Examples: `eval(`, `new Function`, `os.system`, `child_process.exec`, `pickle`, `dangerouslySetInnerHTML`, `.innerHTML =`, `document.write`, and edits under `.github/workflows/`.
   - It warns after the edit lands, once per pattern per file per session.
2. **End-of-turn review:** a background, **separate Claude call** with a fresh context and a security-focused prompt.
   - It reviews the git diff of everything the turn changed, including Bash commands and subagents.
   - Covers up to 30 files, and fires at most 3 times in a row.
   - Looks for authorization bypass, IDOR, injection, SSRF and weak cryptography.
3. **Agentic commit/push review:** a deeper background review when Claude runs `git commit` or `git push` through its Bash tool.
   - It reads callers, sanitizers and related files to cut false positives.
   - Capped at 20 per rolling hour.

The model-backed reviews use Claude Opus 4.7 by default and count toward usage.

**Gaps it gives evidence for (the limits are the lesson):**
1. **The agent's security check is advisory, not a gate.**
   - No layer blocks a write or a commit (see quote).
   - Findings reach the writing Claude as instructions, and the reviewer can miss issues (see quote).
   - The docs call it one layer of defense in depth, not a complete security solution (paraphrase).
   - For hard enforcement, the docs say to add a blocking hook or a CI check.
2. **The reviewer is independent of the writer, but it is still a model.**
   - It deliberately does not let the same instance grade itself: a separate call, fresh context, told only to find problems.
   - Independence reduces bias; it does not make the review exhaustive.
3. **Commits made from your own shell are never reviewed.** The commit layer fires only on Claude's own Bash-tool commits and pushes. Not reviewed:
   - Commits you run yourself, including the `!` shell escape inside a session.
   - Duplicate findings, which are suppressed, so a clean commit shows nothing.
4. **It reads source, not the running app.**
   - The review reads the source code in your checkout, not a running site or a deployed service (paraphrase).
   - It therefore cannot see deployed configuration, hosting settings, or what the live app actually exposes. S039's audit needed live proof-of-concept probes to confirm exploitability.
5. **It silently does nothing in common beginner setups.**
   - The end-of-turn and commit reviews need a git repo, and outside one they skip without any message.
   - The model-backed reviews are skipped when there is no Anthropic authentication and no provider configured.
   - A YAML patterns file is ignored if PyYAML is missing.
   - The agentic commit review needs Python 3.10+; without it, it falls back to a single-shot review, or skips on third-party providers.
   - Cloud sessions don't load the plugin from user settings.
   - Diagnostics are written to `~/.claude/security/log.txt`.
6. **Custom rules are guidance, not guardrails.**
   - `.claude/claude-security-guidance.md` adds a threat model and checklist for the reviewer, but it does not block writes or guarantee that every violation is caught (paraphrase).
   - Custom rules are additive only.
   - `.claude/security-patterns.yaml` adds regex or substring rules, such as flagging `sk_live_` or `AKIA` key prefixes.
7. **Where it sits in the stack:**
   - in-session plugin
   - `/security-review` (one pass over the current branch's changes only)
   - Claude Security plugin (a multi-agent repo scan)
   - Code Review on PRs (Team and Enterprise plans)
   - your CI static analysis and dependency scanners, for the supply-chain and policy checks the plugin does not attempt

**Framings it says are outdated:**
- "The agent checked its own code, so it's secure."
- "The model grading itself." The plugin explicitly avoids this, and still documents misses.
- "A security reviewer in the loop means insecure code can't be committed." It does not block.

**Quotes:**
- "None of the layers block writes or commits."
- "the review model can miss issues"

---

## Cross-source synthesis: what the human must check, October 2026

The course rule says AI handles what is verifiable, and the human checks what AI cannot verify or brings in an expert. The sources map onto it like this.

- **What the agent can verify and should be left to do:**
  - Compile errors, failing tests, re-running its own code (S038: about 100% syntax pass).
  - Pattern-level and diff-level security review (S043).
  - Hunting for vulnerabilities and writing fuzz or property-test harnesses (S040 recommendation).
  - Self-check passes (S039) and AI-assisted review (S041 says another agent can help).
- **What the agent cannot verify, and the human must own:**
  1. **What the code is allowed to do and to whom.** This means the security requirements nobody stated. Hidden rules are 55.5% of S039's vulnerabilities, and access control is the number one class.
  2. **Whether a "fix" removed a safeguard.** S039 function-fix side effects; S042 test deletion and weakened assertions.
  3. **Whether a warning was acted on.** S039 awareness-action gap, 20.7%.
  4. **Deployment and secrets steps outside the code.** S039 user-dependent security; S043 reads source, not the running app; S042 `.gitignore` does not stop AI tools.
  5. **What the agent was told by content it read.** S042: injection via issues, READMEs and fetched pages; MCP; rules files; and S039's insecure CLAUDE.md example.
  6. **How much oversight this code deserves at all.** S041: auth, personal data, secrets and safety-critical code slide left.
- **When the human cannot judge it, bring in an expert.**
  - Looking does not work, even for experienced developers: S040, 37.7% vs 35.0% selection and 22% fully secure.
  - The NCSC's high-risk list (S041) is the practical trigger for getting someone qualified to review, understand, check and verify.
