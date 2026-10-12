---
key: before-you-ship-who-signs-off
id: 04.04
title: "Before you ship: who signs off"
district: Going Live
module: 04 Safe for strangers
status: todo
legacy: []
minutes: 13
concepts: [C009, C066, C072, C118, C120]
sources: [S043, S146, S214, S218, S221, S004, S029, S039, S042, S045, S046, S047, S055, S148, S149, S215, S220, S222, S223, S224, S228, S229, S230]
lead: [S214, S043]
---

# Before you ship: who signs off

**Purpose (the first spoken sentence):** In this lesson you'll learn what a security scan, an AI review or a checklist can and cannot tell you before launch, how to hand the rest to an expert, and why the decision to ship belongs to a person.

**Conclusion:** Scans, AI reviews and checklists are a floor, not a certificate: have the agent list every route, TODO and deploy step the build left to you and run every check a machine can, take that list to a qualified expert for what no machine can verify, and remember that you, not the agent, own the decision to ship and the patches after it.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 04 Safe for strangers (the module's closing gate, before the first stranger arrives; it collects what 04.01 to 04.03 taught into one release step).

**Lead source (audit, 2026-10-12):** S214 (UK National Cyber Security Centre); S043 (Anthropic (live docs)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S043, S146, S214, S218, S221); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Density note:** five concepts (design-decision.md flags this lesson as dense). Keep it under 15 minutes by teaching C072 and C066 as one release-gate story, giving C120 a single 2-minute segment, and C009 the close.

## What to teach (binding scope)

Rough time budget: C066 3 min · C072 3 min · C118 3 min · C120 2 min · C009 2 min. Suggested order: the inventory (what the build left behind) → the floor (what machines check, and what each misses) → the expert (how to hand over the rest) → accessibility (the same split, one more time) → who signs (the close).

### C066 Before release, inventory what was forgotten or left to you

1. **Long builds drop security work.** In S039's audit, memory defects caused 160 vulnerabilities (13.5%): a new `validateApiKey` middleware protected a new router but was not applied to 11 pre-existing handlers. Forgotten obligations caused 50 (4.2%), 90.0% of them Critical or High: one login route left password verification as a TODO. A security-hardening skill left forgotten obligations unchanged at 28.6% while other failure types fell, so the release gate has to be a step a person calls for. (S039) — **teach**
2. **Some steps were always yours.** "User-dependent security" caused 72 vulnerabilities (6.1%), most often supply-chain failures; in one app the user committed a database backup export to a public GitHub repository. Keeping secret files out of Git, setting environment variables, updating vulnerable dependencies and rotating default credentials are steps outside the code. (S039) — **teach**
3. **Ask for the inventory, then check it is complete.** S039's advice: treat generated apps as prototypes, and before public deployment request a self-check covering deferred tasks. The agent lists: every route or endpoint with the check that guards it; every TODO, FIXME and deferred security item; the authentication and authorisation paths; input handling; secrets; and surviving demo shortcuts (demo-oriented design caused 174 vulnerabilities, 14.7%, such as OAuth tokens kept in the browser's localStorage with only base64 encoding). You compare it against what you know the app does. (S039) — **teach**
4. **Add the omissions practitioners find again and again, each with a test the agent runs while you watch.** (S218, S149, S220) — **brief**, one line each:
   - Webhooks: an unverified webhook endpoint accepts forged events from anyone who guesses the URL. Test: replay one without a valid signature and expect a rejection; the fix compares an HMAC-SHA256 signature in constant time. (S218, S149, S220 item 19)
   - Rate limits on login, signup, password reset, and anything that sends email or costs money. Test: a burst against the auth routes should start returning 429. (S218, S220 item 16)
   - Uploads: check type and size, never trust the filename, don't serve uploads from your app's own origin. Test: upload a renamed executable. (S218, S220 item 23)
   - Production debug mode: debug endpoints, verbose stack traces, GraphQL introspection and source maps all off; a pentester reports that the AI never configures production error handling, and saw a demo ship with `DEBUG=True`. Test: load the live site and confirm no stack trace or source map is served. (S218, S149)
   - Logs that swallow whole requests, passwords included (taught in 04.02). Backups that exist and have been restored once (S220 item 31; 03.03).
5. **The agent's review cannot see the live app.** Claude Code's security reviews read the source code in your checkout, not a running site or deployed service, and the model-backed reviews skip silently outside a git repository. So the inventory also covers live configuration: which environment holds which variable (03.03), the database dashboard, and dated platform changes such as Supabase's new grant default on 2026-10-30 (04.02). (S043, S148) — **teach**
6. **Organisations now gate this.** METR requires a security review before any researcher deploys an application publicly. (S046) — **one line**

### C072 Scans, AI security reviews and checklists are a floor, not a certificate

1. **A builder's scan has stated limits.** Lovable's docs: the Quick scan runs automatically on every publish; the Deep scan (access control, unsafe input, leaked secrets, payments, authentication, sensitive data) does not run as you work, so you start it; auto-fix does not apply to Deep scan findings; only critical dependency vulnerabilities become findings; the tools "cannot guarantee complete security", and Lovable recommends an additional professional review for apps with sensitive data. Its Trust center page is "informational, not a certification". (Lovable Docs, see Sources) — **teach**
2. **The agent's own security review is advisory.** Claude Code's security-guidance plugin checks at three points: a pattern match on each edit, a separate-model review at the end of each turn, and a deeper review on each commit or push Claude makes. None of the layers blocks a write or a commit; findings go back to Claude as instructions; the review model can miss issues; commits you make from your own shell are not reviewed; `/security-review` covers only the changes on your current branch. For hard enforcement, add a blocking hook or a CI check. (S043) — **teach**
3. **Stack the layers, then cover what none of them covers.** Anthropic's own stack: the in-session plugin, `/security-review` on demand, a deeper multi-agent scan, review on pull requests, and your existing static-analysis and dependency scanners in CI. None of them tests the running app as a stranger (04.02) or judges a design (C118). (S043) — **teach**
4. **Scanners were built for other code and other secrets.** Standard static-analysis rule sets were built for human-written code (S149). GitHub's push protection for users is on by default only for public repositories on GitHub.com, repository push protection is off by default, and anyone with write access can bypass a block with a reason; model-based secret detection is in private preview and opt-in (GitHub docs and 2026-10-07 changelog, see Sources; S047). — **brief** (secret scanning is taught in 03.02)
5. **AI finds the bugs; people decide which are real.** Osmani: discovery got several times cheaper; triage did not, and confirming what is exploitable still takes a person reading code. (S029) — **brief**
6. **A refusal or a quiet review is not a sign-off.** On 2026-10-07 a hobbyist asked Hacker News which frontier models can do extensive code security reviews, ideally close to the quality of the NCC Group, for a hobby project. The replies name models anecdotally and argue about refusals; none says a model matches a security firm. No finding does not mean no vulnerability. (S146) — **brief**
7. **Checklists date fast.** The OWASP Top 10 for LLM Applications 2026 (August 2026) reordered the list: Excessive Agency is LLM03, Unbounded Consumption LLM06, and Hidden Context Exposure LLM08. A community checklist last updated the same month still labels denial of wallet with the 2025 number. Use lists to know what to ask, not as a certificate. (S055, S220) — **one line**

### C118 Bringing in an expert: who, what you hand them, what you get back

1. **Match the expert to the risk.** A security tester for apps holding other people's data or money; a privacy lawyer or data-protection officer for personal and regulated data; an accessibility auditor and disabled testers for public services, shops and banking-type services; a cloud identity specialist for credential and access design; an IP lawyer before selling media or models; a qualified engineer and test lab for mains-powered or shipped hardware. Say on screen that this mapping is the course's own, drawn from its concepts, not a source's. — **teach**
2. **Check they are qualified.** The UK NCSC: third-party penetration tests should be performed by qualified and experienced staff only; it directs UK government bodies to testers in its CHECK scheme. (S214) — **brief**
3. **Scope the job together.** Scoping should involve all relevant risk owners, technical staff who know the system, and a representative of the test team, and produce a document stating the technical boundaries of the test, the types of test expected, the effort in resource days, and the reporting you need. (S214) — **teach**
4. **Hand over a scope pack the agent assembles:** the release inventory (C066 above), the map of what runs where (03.01), the data map (04.02), test accounts for each role, a staging copy to test against, and the list of what you want checked. OWASP's Application Security Verification Standard (ASVS, 5.0.0) "provides a basis for testing web application technical security controls", so it can be that list. (S215) — **teach**
5. **What comes back:** for each issue, the tester's assessment of the level of risk it exposes and a method of resolving it. The agent fixes; the tester retests. (S214) — **teach**
6. **What a test cannot tell you.** It shows what was true at the time of the test. Vulnerability risk assessment is a business process that should not be wholly outsourced to the test team, and functional testing of security controls should still occur between tests. So the scans and stranger tests keep running, and accepting the risk that remains is your call. (S214) — **teach**
7. **Ask whether they test AI-built failure patterns.** One firm (VULNEX) says it has added them to its standard web application assessment template. (S149) — **one line**
8. **A model is an assistant to the expert, not the expert.** (S146, S029) — **one line**

### C120 Accessible is a check the agent can only half-run

1. **The web is getting less accessible, and AI coding is a suspect.** WebAIM's 2026 scan of the top million home pages: 95.9% had detected WCAG 2 failures (94.8% in 2025), 56.1 errors per page on average (51 in 2025), reversing a trend of gradual improvement. WebAIM names "automated or AI-assisted coding practices" ("vibe coding") among likely causes, without measuring it: say so. (S221) — **teach**
2. **The agent's half is machine-checkable.** The six commonest failures are the ones a checker finds: low-contrast text (83.9% of pages), missing alt text (53.1%), missing form labels (51%), empty links (46.3%), empty buttons (30.6%), missing page language (13.5%). The agent runs a checker, fixes what it reports, and re-runs it after every change. (S221) — **teach**
3. **The human's half is not.** WebAIM: not all conformance failures can be detected automatically. In the UK Government Digital Service's 2017 test of 2017 tools, 10 automated tools ran against a page with 143 planted barriers: 29% were missed by every tool, and the best single tool found 37% to 41% (put "2017 tools" on screen next to the figure, or replace it with a 2026 measurement before scripting). What no checker can judge is whether a disabled person can actually use it: bring in an accessibility auditor or disabled users for that. Do not teach keyboard-only and screen-reader passes as human-only until a source shows whether today's agents' browser tools can run them (backlog: Accessibility audits). (S221, S224) — **teach**
4. **More markup is not more access.** Pages using ARIA averaged 59.1 errors against 42 without; it is a correlation, not a measured cause. (S221) — **one line**
5. **The law is moving.** US state and local government sites and apps must meet WCAG 2.1 AA by 2027-04-26 (population 50,000 or more) or 2028-04-26 (smaller entities and special districts), dates moved by an interim final rule published 2026-04-20 (S222). The EU's Accessibility Act covers services including e-commerce, banking and e-books; the Commission's page gives no application date or small-business rule, so check the current text before stating either (S223). — **brief** (backlog: "Accessibility audits")
6. **For services others depend on, bring in people:** combine automated tools with manual checking, an accessibility audit and user testing. (S224) — **one line**

### C009 A person owns the ship decision

1. **The agent carries no accountability; a person approves.** Osmani: a person always approves the merge, and Anthropic's position is that approval is "still a human call". OWASP's Human Accountability rules: assign a human owner to every AI-generated change, require explicit developer approval before merging, keep an audit trail that records the tool and model version, never treat AI review comments as a substitute for human review, and the developer who accepts and commits the code is accountable. (S029, S042) — **teach**
2. **The "can I explain this?" test.** You need not have read every line, but you should be able to explain what the change does, what it touches and why it is safe to ship: "You can only really be accountable for what you can explain." (S029) — **teach**
3. **Say what you did not check, where people will see it.** For example, a PR description saying the change was agent-reviewed, the tests pass, and you did not read the migration logic. (S029) — **brief**
4. **Accountability needs matching authority.** The "moral crumple zone" (Elish, via Osmani): the person nearest an automated system takes the blame for failures they had little power to prevent, so whoever signs needs a say in the pace and time to understand. (S029) — **one line**
5. **Ownership continues after launch.** React2Shell (CVE-2025-55182, CVSS 10.0) was an unauthenticated remote-code-execution flaw in React Server Components; apps could be vulnerable even without Server Function endpoints, and the React team said not to depend on hosts' temporary mitigations (S228). Next.js: there is no workaround; upgrade, redeploy, and rotate secrets if the app was online and unpatched (S229). Dependabot alerts fire when a new advisory is published, with no change to your code, but an admin has to enable them and they email people with write access who watch the repository (S230). The agent runs the upgrade; a person must receive the alert and decide to rotate. — **brief** (keeping a shipped app alive is 10.02's)

*Pending (audit, 2026-10-12), not yet teachable:* when a source on shipping desktop apps, extensions or game builds has been read (backlog: "Shipping a desktop app, extension or game build"), add one sourced line to the release inventory: tested on a machine and OS you don't own, or by someone who has one. Aaron asked for it (research/sweep/aaron.md P08); no source has been read yet, so it is not in this lesson's scope.

## You vs the agent

As of 2026-10-12:

- **The agent does on its own:** greps for TODOs, tabulates routes and the guard on each, applies middleware everywhere, writes `.gitignore` rules, runs the webhook, rate-limit, upload and debug-mode tests, runs scanners and separate-model reviews and fixes their findings, runs accessibility checkers and fixes what they report, assembles the scope pack (inventory, maps, test accounts, staging copy, ASVS sections), fixes a tester's findings and re-runs the agreed checks, and runs dependency upgrades when an advisory lands. (S039, S043, S218, S220, S221, S214, S229)
- **You must:** call for the inventory at the release gate and judge whether it is complete (S039); do the host, dashboard and credential steps yourself (S039, S043); turn on what is off by default (the Deep scan, repository push protection, the review plugin inside a git repo) and rerun scans after changes (Lovable Docs, GitHub docs, S043); read findings instead of clicking "fix all"; judge, or bring in an auditor or users to judge, whether a disabled person can actually use it (S224); choose, pay and scope the expert, read the risk ratings, and accept or refuse the risk that remains (S214); be able to explain what ships and write down what you did not check (S029); own the decision to ship, fix or stop, and receive the advisories afterwards (S029, S042, S230).
- **Bring in an expert:** this lesson is how (C118). The minimum: a security tester before other people's data or money touch the app; a privacy lawyer for regulated personal data; an accessibility auditor and disabled testers for public-sector, shop, banking-type and e-book services.

## Sources this lesson is built from

- S043 — Anthropic, "Catch security issues as Claude writes code" (security-guidance plugin; live docs, last modified 2026-10-09) https://code.claude.com/docs/en/security-guidance — the three layers, none blocks, reads source not the running app, skips outside git, the layered stack. Re-read 2026-10-12.
- S146 — Bender and replies, "Ask HN: Which frontier model can do code security reviews" (2026-10-07) https://news.ycombinator.com/item?id=49996594 — a real hobbyist asking whether a model can stand in for a security firm; the replies don't say one can. Re-read 2026-10-12.
- S214 — UK National Cyber Security Centre, "Penetration testing" (published 2017-08-08, reviewed 2022-01-10, page metadata modified 2026-04-08; foundational and still current) https://www.ncsc.gov.uk/guidance/penetration-testing — qualified testers, scoping, report contents, "at the time of the test", risk not outsourced. Re-read 2026-10-12.
- S218 — Chizee (DEV Community), "You're Doing Vibe-Coding Wrong. Here's the 17-Point Fix." (2026-09-20, edited 2026-09-23; the year is inferred from the page) https://dev.to/chizee/youre-doing-vibe-coding-wrong-heres-the-17-point-fix-e9h — the pre-launch omissions (webhooks, rate limits, uploads, debug mode, logging); its last point is "Run an actual security review". Re-read 2026-10-12.
- S221 — WebAIM, "The WebAIM Million: 2026 report" (analysis February 2026; updated 2026-03-30) https://webaim.org/projects/million/ — the 2026 failure rate, the six commonest failures, AI-assisted coding named as a likely cause, the limits of automated tools. Re-read 2026-10-12.

Also cited for single points (credit on the lesson page):
- S039 — Deng, Fan, Meng, "Understanding the (In)Security of Vibe-Coded Applications" (v4 2026-09-14) https://arxiv.org/abs/2606.23130 — memory defects, forgotten obligations, user-dependent security, demo shortcuts, the self-check before deployment. Re-read 2026-10-12.
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — a person approves; "can I explain this?"; disclose what you didn't read; discovery vs triage; moral crumple zone. Re-read 2026-10-12.
- S042 — OWASP, "Secure Coding with AI Cheat Sheet" (created 2026-05-05; updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — Human Accountability (section 14). Re-read 2026-10-12.
- S149 — Simon Roses Femerling (VULNEX), "The OWASP Top 10 for Vibe-Coded Applications (Part 2)" (2026-04-23) https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/ — webhooks, `DEBUG=True`, rule sets built for human code, AI checks in a tester's template. Use only its quoted lines. Re-read 2026-10-12.
- S220 — boxed-dev, "vibe-coding-security" checklist (latest commit 2026-08-09) https://github.com/boxed-dev/vibe-coding-security — the concrete tests (items 16, 19, 23, 31). A small project that also sells a paid add-on. Re-read 2026-10-12. Correction for concepts.md: its "100 requests/minute should return 429" test is for auth routes (item 16), not AI endpoints; C121 should cite item 42 instead.
- S215 — OWASP, Application Security Verification Standard project page (latest stable 5.0.0; page undated) https://owasp.org/www-project-application-security-verification-standard/ — the requirement list to hand a tester. Re-read 2026-10-12.
- S224 — Mehmet Duran (GDS), "What we found when we tested tools on the world's least-accessible webpage" (2017-02-24; foundational and still current) https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/ — 29% missed by all tools; combine with manual checks, an audit and user testing. Re-read 2026-10-12.
- S222 — US Department of Justice, ADA.gov fact sheet on the web and mobile app rule (page dated 2024-04-08; reflects the interim final rule published 2026-04-20) https://www.ada.gov/resources/2024-03-08-web-rule/ — 2027-04-26 and 2028-04-26. Re-read 2026-10-12.
- S223 — European Commission, "European Accessibility Act" (undated live page) https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en — services covered; no application date given. Not re-read today.
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — security review before public deployment. Re-read 2026-10-12.
- S055 — OWASP GenAI Security Project, "OWASP Top 10 for LLM Applications 2026" (2026-08-04) https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 — the 2026 numbering (folder `2026/final/` lists LLM03 Excessive Agency, LLM06 Unbounded Consumption, LLM08 Hidden Context Exposure). Checked 2026-10-12.
- S148 — Supabase discussion #45329 (2026-04-28; comments to 2026-10-11) https://github.com/orgs/supabase/discussions/45329 — the 2026-10-30 deploy step.
- S047 — GitHub Changelog, "Secret scanning adds detectors for Lovable, Supabase, and more" (2026-10-05) https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more — new detectors only. Re-read 2026-10-12. Correction for concepts.md: this changelog says nothing about push-protection defaults, bypass or model-based detection; those come from the two GitHub pages below.
- S228 — The React Team, "Critical Security Vulnerability in React Server Components" (2025-12-03, updated 2026-01-26) https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components — React2Shell. Re-read 2026-10-12.
- S229 — Josh Story and Sebastian Markbåge, "Security Advisory: CVE-2025-66478" (2025-12-03, updated 2025-12-06) https://nextjs.org/blog/CVE-2025-66478 — no workaround; rotate secrets. Re-read 2026-10-12.
- S230 — GitHub Docs, "About Dependabot alerts" (undated live docs) https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts — alerts on new advisories; admins enable; who gets emailed. Re-read 2026-10-12.
- Not yet in sources.md (proposed): Lovable Docs, "Security" (live docs, undated on the page, read 2026-10-12) https://docs.lovable.dev/features/security — Quick vs Deep scan, auto-fix limits, critical-only dependency findings, "cannot guarantee complete security", Trust center "not a certification". Correction for concepts.md: C072 credits these points to S045 (Vercel's v0 page), which does not contain them.
- Not yet in sources.md (proposed): GitHub Docs, "About push protection" (undated live docs, read 2026-10-12) https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection — user push protection on by default for public repos on GitHub.com; repository push protection off by default; anyone with write access can bypass.
- Not yet in sources.md (proposed): GitHub Changelog, "Purpose-built model for leaked secret detection" (2026-10-07) https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection — AI secret detection in push protection is private preview, opt-in, billed in AI Credits.

## Show it for real

- Have the agent produce the release inventory of a small app: a table of every API route and the auth check on each, plus every TODO and FIXME; then call one unguarded route with `curl` from a logged-out terminal. Proves the inventory finds what the build forgot (S039).
- Replay a captured test webhook with its signature header removed: an unprotected handler accepts it; after the agent's fix, it is refused. Proves a forged-event hole and its test (S218, S220).
- Burst the login route of a local test app and watch 429 appear after the limit. Proves the rate limit exists (S220 item 16).
- Install the Claude Code plugin (`/plugin install security-guidance@claude-plugins-official`), ask for code using `innerHTML` and watch the per-edit warning; then commit from your own terminal and show that nothing reviews it; open `~/.claude/security/log.txt`. Proves the agent's review is a floor, not a gate (S043).
- In Lovable (or a similar builder) on a throwaway project: the Quick scan on publish, the Deep scan that must be started, and the "Up to date" marker going stale after a schema change. Proves builder scans are opt-in and point-in-time (Lovable Docs).
- Run an accessibility checker on an agent-built page and have the agent fix every finding; then tab through the page with the keyboard and listen with a screen reader to find what the checker passed. Proves that a passing checker is not the end of the check (S221, S224); do not present the keyboard and screen-reader passes as something no agent can do (see point 3).
- Have the agent turn the inventory into a one-page scope pack: boundaries, roles and test accounts, staging URL, the ASVS sections in scope; show one sample finding row (issue, risk rating, fix, retest result). Proves what you hand an expert and what comes back (S214, S215).
- On GitHub, write a PR description that says what was agent-reviewed, which checks ran (linked), and what you did not read. Proves disclosure is a few honest lines (S029).
- Use throwaway projects, a dummy webhook secret and test accounts only; nothing real on screen.

## Questions this lesson answers

Asked in the wild:
- "Which frontier models can do extensive code security reviews, security fixes?", ideally close to the quality of the NCC Group, for a hobby project (S146, Hacker News, 2026-10-07).
- Aaron's own: asking the AI to "make sure it's secure" or "ready to deploy" when he could not check the answer (S004).

Derived from the sources (not yet seen in beginner posts; replace with real questions as they arrive):
- Lovable (or Claude) says my app passed the security scan. Am I safe?
- An AI scanner found 200 issues. What now?
- When do I need a real security review? Do I need one for a side project?
- How do I find a security tester? What do I give them? What does a pen-test report contain? Do I need another test after I change the app?
- Is my AI-built site accessible? Is an automated checker enough? Do accessibility laws apply to my site?
- Who is responsible if AI-written code gets hacked? What should I write in a PR when I didn't read everything? When is it OK to launch?

<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Secret scanning and push protection in depth; leaked keys → keys-public-secret-and-leaked (03.02, C070, C071)
- Environment variables per environment; undo and backups have limits → from-your-laptop-to-a-url (03.03, C099, C098)
- The stranger test of the live app; the data map; logs → test-it-as-a-stranger (04.02, C068, C119)
- Blocking hooks and CI as enforcement → rules-it-reads-rules-it-cant-break (05.02, C045)
- AI review as triage, not acceptance; verify the verifier → checking-what-you-cant-read (06.02, C014, C017)
- "Done" is a claim → done-is-a-claim (02.04, C011)
- Keeping a shipped app patched; the dependency list's owner → after-launch-keep-it-alive (10.02, C053)
- Which accounts an app rests on → every-automation-runs-as-someone (08.03, C129)
- Backlog: "Accessibility audits"; "Your users' data and the law"

## Out-of-date framings to avoid

- "The security scan passed, so the app is safe" / "running an AI security scan means the app is secure." (Lovable Docs, S029)
- "The agent said it's secure." / "A security reviewer in the loop means insecure code can't be committed." (S043)
- "If the AI didn't flag a vulnerability, there isn't one." (S146)
- "GitHub won't let me push a secret." (GitHub push-protection docs)
- "Once auth is added, the whole app is protected." (S039)
- "The agent handled deployment, so it's configured securely." (S039, S043)
- "A pen test certifies the app is secure." It shows what was true at the time of the test (S214).
- "The expert decides whether we ship." Risk assessment is not outsourced (S214).
- "A frontier model is as good as a security firm." (S146)
- "The accessibility checker passed, so the page is accessible" / "adding ARIA makes it accessible" / "accessibility is optional polish." (S224, S221, S222)
- "The AI wrote it, so the bugs are the AI's fault" / "AI review comments count as review." (S029, S042)
- Citing the OWASP LLM Top 10 2025 as current. (S055)

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 (`00-06-how-to-learn-anything-technical`) has a "move-in day" segment with the right instinct (the agent can't vouch for what nobody specified; have someone who can verify it before you ship) and a dated card of security tools (`/security-review`, the security-guidance plugin and vendor security agents in preview) with the right conclusion that every one is meant to sit beside a human reviewer. What it lacks for this slot: the release inventory (C066), what each scanner and review misses (C072), how to bring in an expert (C118), accessibility (C120), and ownership after launch (C009). Its card's tool dates were not re-checked for this spec; re-verify against current docs before reusing any of them, and do not reuse its pointers to the retired map.
