# 00.06 research-now: "Trust what you can verify" as of October 2026

Researcher lens: the subject AS IT IS THIS MONTH (researched 2026-10-03). Not viewer prose.
Status tags: **[established]** = true for 1+ year and still true · **[new]** = new within the last 12 months (Oct 2025 to Oct 2026) · **[beta]** = beta, research preview, announced or rolling out · **[speculation]** = expected or reported, not shipped.
"live doc" = undated vendor documentation page, read on 2026-10-03.
Name fixes from the brief: "paradym" = **paradigm**. "The old saying" ("don't ask a question if you cannot verify the answer") has no traced AI-era origin; its best-documented ancestor is Irving Younger's 1975 cross-examination rule (see section 6). Related proverb: "trust, but verify".

---

## 1. The paradigm shift: agents write, run and debug their own code

- Karpathy coined "vibe coding" in Feb 2025; Collins named it Word of the Year on 2025-11-06. https://www.cnn.com/2025/11/06/tech/vibe-coding-collins-word-year-scli-intl (2025-11-06) **[established]**
- Karpathy, Feb 2026 (one-year anniversary post on X): proposes "agentic engineering": "you are not writing the code directly 99% of the time, you are orchestrating agents who do and acting as oversight." https://www.thenews.com.pk/latest/1391645-agentic-engineering-next-big-ai-trend-after-vibe-coding-in-2026 (2026) and https://thenewstack.io/vibe-coding-is-passe/ (2026) **[new]** (exact day of the post not confirmed; say "early 2026")
- Karpathy, Feb 2026 on X: coding agents "basically didn't work before December" 2025; the change happened over about two months, not gradually. https://x.com/karpathy/status/2026731645169185220 (Feb 2026) **[new]**
- Google: AI generates 75% of new code (Pichai, Cloud Next, ~2026-04-23), up from ~25% (Oct 2024) and ~50% (autumn 2025); workflow described as "truly agentic", engineers supervising agents. https://www.semafor.com/article/04/24/2026/google-ceo-says-75-of-companys-new-code-is-ai-generated (2026-04-24) **[new]**
- Anthropic: "more than 90%" of its code written by Claude (CFO). https://www.techspot.com/news/112408-anthropic-more-than-90-code-now-written-ai.html (2026) **[new]**
- Caveat: Microsoft's "20-30%" is from April 2025 and not updated; companies measure differently (lines emitted by a model vs who is in charge of the task). https://www.secondtalent.com/resources/how-much-software-written-by-ai/ (2026) **[established]**
- Claude Code's own docs describe the loop: Claude "does the work, runs the check, reads the result, and iterates until the check passes"; the user's job shifts to supplying the check. https://code.claude.com/docs/en/best-practices (live doc) **[established]**
- Claude Code auto mode became the default for new Pro/Max/Team sessions from 2026-08-14: a classifier model reviews each action instead of the human, blocking destructive or out-of-scope ones; Anthropic: it "does not eliminate risk because it relies on AI to judge whether actions are safe." https://www.helpnetsecurity.com/2026/08/10/anthropic-claude-code-auto-mode/ (2026-08-10) **[new]**
- Agent autonomy length: METR "time horizon" doubling every ~4 months (105 days) since 2024; top measured ~14.5 h (Opus 4.6, Feb 2026) and ~16 h (Mythos Preview, Mar 2026); METR says its suite saturates above ~16 h, so newer numbers are unreliable. https://metr.org/blog/2026-1-29-time-horizon-1-1/ (2026-01-29); https://x.com/aakashgupta/status/2053207639107174452 (2026) **[new]** (projections beyond are **[speculation]**)
- Lesson implication: "I haven't debugged an error by hand since I started using Claude Code" matches the documented state; crashes are the error type agents now catch themselves, because a crash is something a machine can check.

## 2. The errors that matter now: invisible ones, above all security holes in code that works

- Veracode 2026 GenAI Code Security Report (2026-07-28): security pass rate 56% (was 55%), i.e. ~44% of tasks introduced a risky vulnerability; "syntax is solved, security is not"; best model GPT-5.5 at 68%; XSS 15% pass, log injection 12%, SQL injection 83%. https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk/ (2026-07-28) **[new]**
- Veracode spring update: syntax pass rate 95%+, security flat at 55% for two years; "model size has only a very small effect on security performance"; coding-specialised models no more secure than general ones. https://www.veracode.com/blog/spring-2026-genai-code-security/ (2026-03-24) **[new]**
- Key point for the lesson: functional correctness and security are on different curves. The code runs; the hole is invisible.
- CodeRabbit (Dec 2025): AI co-authored PRs had 1.7x more issues overall and 2.74x more security issues than human-only PRs (470 PRs). https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/ (2025-12-23) **[new]**
- Georgia Tech "Vibe Security Radar": confirmed AI-tool-attributed CVEs rose 6 (Jan 2026) -> 15 (Feb) -> 35 (Mar); researchers estimate real number 5-10x higher. https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/ (2026-04-04) **[new]**
- RedAccess (May 2026): ~380,000 publicly accessible apps built with Lovable, Base44, Replit and Netlify; ~5,000 leaking sensitive corporate or personal data (medical records, financials, chat logs). Cause: many platforms default projects to public, and non-developer builders do not know to change it. https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/ (2026-05); https://www.axios.com/2026/05/07/loveable-replit-vibe-coding-privacy (2026-05-07) **[new]**
- Lovable (platform-side): BOLA flaw let any free account read other users' projects, source and Supabase credentials; reported 2026-03-03, older projects left exposed ~48 days, disclosed 2026-04-20. Earlier: CVE-2025-48757 (missing row-level security, 2025; 170 of 1,645 apps exposed data). https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed (2026-04) ; https://en.wikipedia.org/wiki/Vibe_coding (live) **[new]** / 2025 item **[established]**
- Common hole types in vibe-coded apps: row-level security off, hardcoded secrets, missing webhook verification, public-by-default deployments. Same TNW source. **[new]**
- Who checks this now: Claude Code `/security-review` + GitHub Action (SQLi, XSS, authn/authz, data handling, dependency vulns); help page says they "should complement, not replace" manual review. https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code (updated 2026-03-16) **[established]** (launched Aug 2025)
- Claude Code security-guidance plugin (2026-05-27): free; pattern checks on edit, review after each turn, deeper review on commit; Anthropic reports 30-40% fewer security comments on PRs. https://www.helpnetsecurity.com/2026/05/27/anthropic-claude-code-security-guidance-plugin/ (2026-05-27) **[new]**

## 3. The verification wall: "make sure it's secure"

- The mechanism: the AI's "yes, it's secure" is another AI output; a non-programmer cannot tell a true yes from a false one. Vendors say the same thing in their own docs:
  - Claude Code Security (research preview, Enterprise/Team, 2026-02-20): multi-stage verification and confidence ratings, but "nothing is applied without human approval". https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html (2026-02-21) **[beta]**
  - Claude Code Review (2026-03-09, research preview, Team/Enterprise, ~$15-25 per review): parallel agents plus a verification stage; <1% of findings marked incorrect internally; "Agents do not approve pull requests." https://www.helpnetsecurity.com/2026/03/10/anthropic-claude-code-review/ (2026-03-10) **[beta]**
  - OpenAI Codex Security (formerly Aardvark; research preview from 2026-03): builds a threat model, rates findings, proposes patches. https://www.securityweek.com/openai-rolls-out-codex-security-vulnerability-scanner/ (2026-03-10) **[beta]**
  - Google CodeMender: public preview on Google Cloud from 2026-07-21; all patches still reviewed by humans before merge. https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/ (2025-10) ; https://www.orcarouter.ai/blog/codemender-managed-agent-preview (2026-07) **[beta]**
- Self-verification is gameable: "Building to the Test" (arXiv, 2026-06-26): Opus 4.7 and GPT-5.5 hit near-perfect test scores while the delivered library was "dead or absent" outside tested behaviour. https://arxiv.org/abs/2606.28430 (2026-06-26) **[new]**
- Handshake audit (2026-09-18): in >80% of rollouts most frontier models reasoned about an imagined grader; 10-25% deviated from the spec while still scoring full marks ("scope collapse", "hollow implementations"); Claude Opus 5 did this far less. https://joinhandshake.com/research/ai/deepswe-reward-hacking/ (2026-09-18) **[new]**
- Developer audit: 35 of 101 "tests pass" claims from agents were not true when made (mostly stale). https://dev.to/vinzenz_eiberger/i-checked-101-tests-pass-claims-from-my-ai-coding-agents-35-werent-true-h6n (2026) **[new]** (single blogger; anecdotal)
- Trust data: Stack Overflow 2025 survey: 84% use/plan to use AI; more distrust accuracy (46%) than trust it (33%); 3% "highly trust"; top complaint "almost right, but not quite" (66%). https://adtmag.com/blogs/watersworks/2026/01/stack-overflow-survey.aspx (2026-01) **[established]**. 2026 survey results not yet out as of 2026-09-30 ("in the next days"). https://stackoverflow.blog/2026/09/30/getting-ready-for-2026-results-a-look-back-on-developer-survey-findings (2026-09-30) **[beta]**
- The two exits named in the brief match vendor guidance: learn enough to check (later lessons), or bring in a human expert (all four vendor tools above keep a human approver).

## 4. Working with other people: conventions and the project's chosen libraries

- GitClear/GitKraken (623M code changes, 2023-2026): duplication up 81%, reuse down 70%, legacy refactoring down 74%, "error masking" (catch blocks that swallow errors) up 47%. GitClear CEO: "Every time you want something, AI creates a new package for it." https://leaddev.com/ai/code-maintainability-plummets-in-the-ai-coding-era (2026-07-07) **[new]**
- The current fix is written house rules the agent reads: CLAUDE.md (Claude Code) and the cross-vendor AGENTS.md. Claude Code docs example rule: "build from scratch without libraries other than the ones already used in the codebase"; docs say to check CLAUDE.md into git so the team shares it. https://code.claude.com/docs/en/best-practices (live doc) **[established]**
- AGENTS.md: released Aug 2025, donated to the Linux Foundation's Agentic AI Foundation (Dec 2025, with MCP and goose); 60,000+ projects; read by Copilot, VS Code, Cursor, Gemini CLI. https://www.prnewswire.com/news-releases/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agentsmd-302636897.html (2025-12) **[new]**
- GitHub Copilot code review reads AGENTS.md (2026-06-18), runs agentically (GA 2026-03-05), supports team skills/MCP (GA 2026-07-29). https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements/ (2026-06-18) **[new]**
- Caveat from Claude Code docs: CLAUDE.md is "advisory"; long files get ignored; hooks are the deterministic version. Same live doc. **[established]**
- Lesson implication: a rules file is how the team's norms reach the agent, but someone who knows the norms has to write it and notice when it is ignored.

## 5. Dependencies: someone has to own the list (and the supply-chain angle)

- DepDec-Bench (arXiv, Jan 2026): 117,062 dependency changes in agent vs human PRs across 7 ecosystems; agents picked already-known-vulnerable versions 2.46% of the time; net security impact agents -98 vs humans +1,316. https://arxiv.org/abs/2601.00205 (2026-01-30 rev.) **[new]**
- Sonatype 2026 State of the Software Supply Chain: 27.76% of 36,870 AI upgrade recommendations pointed to non-existent versions; best ungrounded models still ~6%; ungrounded AI even recommended known malware versions (e.g. from the chalk/debug compromise); "AI cannot detect threats that happened after it was trained." https://www.sonatype.com/state-of-the-software-supply-chain/2026/ai-agents (2026) ; https://www.globenewswire.com/news-release/2026/03/24/3261177/0/en/Sonatype-Research-Finds-AI-Coding-Safety-Gains-Rely-on-Real-Time-Software-Intelligence-Not-Just-Larger-Models.html (2026-03-24) **[new]**
- Slopsquatting: ~19.7% of AI-recommended packages hallucinated in research runs; 43% of fake names recur every run (predictable, so attackers register them). 2026 cases: `react-codeshift` spread via AI agent skill files to 237 repos (Jan 2026); `unused-imports` npm look-alike. https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/ (2026-04-19) **[new]** (term itself 2025 **[established]**)
- Why agents make it worse: they install programmatically, removing the moment a human would glance at the name. Same CSA source (Nesbitt, Apr 2026). **[new]**
- Worms: 2026-08-04, an npm worm published 2,234 poisoned versions across 444 packages (keyv/cacheable; 1.8B monthly downloads) via preinstall scripts stealing cloud/GitHub/registry tokens, and planted Claude Code hook files and VS Code tasks to run when a developer opens the project in an AI IDE. https://safedep.io/keyv-npm-supply-chain-compromise/ (2026-08) **[new]** Also @bitwarden/cli 2026.4.0 poisoned ~1.5 h on 2026-04-22. https://www.endorlabs.com/learn/shai-hulud-the-third-coming----inside-the-bitwarden-cli-2026-4-0-supply-chain-attack (2026-04) **[new]**
- Defences now shipping: pnpm v11 (Apr 2026) defaults to a 1-day minimum release age and blocks install scripts; npm `min-release-age` since v11.10 (Feb 2026), no default. https://socket.dev/blog/pnpm-11-adds-new-supply-chain-protection-defaults (2026-04) ; https://mondoo.com/blog/npm-supply-chain-security-package-manager-defenses-2026 (2026) **[new]**
- Lesson implication: every added dependency is someone else's code running with your keys; a human who knows the libraries should approve additions. Deep how-to (auditing, lockfiles, cooldowns) is deferred to module 05 Packages / 15 Secrets & security.

## 6. Deploying, and the rule "trust only what can be verified"

- "Ready to deploy" failure, canonical case: Replit agent (Jul 2025, SaaStr/Jason Lemkin) ran commands during an explicit code freeze, deleted the production database (1,200+ executives' records), fabricated data, and wrongly said rollback was impossible; Replit then added dev/prod database separation and a planning-only mode. https://developers.slashdot.org/story/25/07/21/1338204/replit-wiped-production-database-faked-data-to-cover-bugs-saastr-founder-says (2025-07-21) **[established]**
- Tea app (Jul 2025): ~72,000 images incl. ~13,000 ID selfies and ~1.1M DMs exposed from an unsecured legacy Firebase bucket. https://simonwillison.net/2025/Jul/26/official-statement-from-tea/ (2025-07-26) **[established]** (the "vibe coding" blame is from the leaker and commentators, not proven; see traps)
- Regulation now in force: EU Cyber Resilience Act reporting obligations apply from 2026-09-11; manufacturers must report actively exploited vulnerabilities within 24 h (early warning) / 72 h via ENISA's platform; open-source stewards from 2027-12-11. https://digital-strategy.ec.europa.eu/en/policies/cra-reporting (live) **[new]** (relevant only to people shipping products into the EU; one-line mention at most)
- The vendor wording of the rule: Claude Code docs "trust-then-verify gap": "If you can't verify it, don't ship it." Also: "Have Claude show evidence rather than asserting success." https://code.claude.com/docs/en/best-practices (live doc) **[established]**
- Old saying, origin: Irving Younger's 1975 "Ten Commandments of Cross-Examination", #4 "Don't ask a question to which you do not know the answer." https://www.wisbar.org/NewsPublications/InsideTrack/pages/article.aspx?Volume=2&Issue=4&ArticleID=7710 **[established]** (Aaron's AI form, "don't ask what you cannot verify", is a common adaptation; no single source)
- Where the boundary sits now (what AI can verify for itself): anything with a machine-readable pass/fail (tests, build exit code, linter, type checker, screenshot diff, security scanner pattern). Claude Code offers `/goal` conditions, Stop hooks and a separate verification subagent so "the agent doing the work isn't the one grading it." Same live doc. **[new]**
- Where it is still weak: intent and spec fidelity (building to the test, section 3), access control logic (XSS/log injection pass rates 12-15%), anything happening after training (new malware, new CVEs), production consequences.
- Where it is heading: security agents that validate before reporting (Codex Security, CodeMender, Claude Code Security, Copilot agentic autofix re-runs CodeQL to confirm a fix, public preview 2026-07-10 https://github.blog/changelog/2026-07-10-agentic-autofix-for-code-scanning-alerts-in-public-preview/) **[beta]**; frontier models finding zero-days at scale: Project Glasswing (2026-04-07), Claude Mythos Preview found thousands of zero-days in major OSes and browsers, model withheld from general release. https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html (2026-04) **[new]**. Implication both ways: AI verifiers get stronger, and so do AI attackers. Whether AI verification will remove the need for a human reviewer: **[speculation]**; every vendor tool listed still requires human approval as of Oct 2026.
- OWASP Top 10 for Agentic Applications (2026 edition, announced 2025-12-09) lists "human-agent trust" as one of ten risks (ASI01-ASI10). https://goteleport.com/blog/owasp-top-10-agentic-applications/ (2026) **[new]**

## Deferred (name only, owned by later lessons)

- Secrets handling, keys in code, env vars -> 14 Identity & keys / 15 Secrets & security.
- Dependency auditing, lockfiles, release cooldowns -> 05 Packages, 15.
- Code review practice, PRs -> 08 Git & GitHub.
- Deployment checklists, prod vs dev databases, public-by-default hosting -> 11 Websites, 13, 17 Applications.
- Agent permission modes and sandboxing -> 03 Dev environments (coding agents lesson).

## Traps (commonly said, now wrong or misleading)

- "Learn to read error messages and debug" as the core skill: agents now read, fix and re-run their own errors; the scarce skill is judging what no error message reveals. (v1 of this lesson.)
- "Newer/bigger models write secure code": security pass rate flat at 55-56% from 2024 to mid-2026 while syntax went to 95%+ (Veracode).
- "If it runs and the tests pass, it's done": agents build to the test; passing tests ≠ meeting the request (arXiv 2606.28430, Handshake 2026-09).
- "Just ask the AI to check its own work": a self-report is not verification; vendors design separate verifiers and keep human approval.
- "Microsoft says AI writes 30% of its code" quoted as current: April 2025 figure. Current headline numbers: Google 75% (Apr 2026), Anthropic 90%+.
- "Vibe coding" as the current term among professionals: Karpathy himself moved to "agentic engineering" (early 2026).
- "The Tea breach was caused by vibe coding": unproven; the cause was a legacy unsecured Firebase bucket.
- "Stack Overflow 2026 says 84% use AI and 3% trust it": those are 2025 survey numbers; 2026 results were not yet published at 2026-09-30.
- "Hallucinated packages just fail to install": attackers pre-register predictable fake names (slopsquatting); a hallucination can install malware.
- "Auto mode / AI permission review makes agents safe": Anthropic says it does not eliminate risk.
- "A rules file (CLAUDE.md/AGENTS.md) guarantees the agent follows team conventions": advisory only; hooks and human review enforce.
