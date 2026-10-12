# Research notes: untrusted inputs and the supply chain

Theme: opening a repo, reading a ticket or installing a package can be code execution. How malicious content reaches the agent, and how to check what you install.

Read on 2026-10-12 by the research crew (agent `read-untrusted-inputs-supply-chain`). Every point below traces to the source it is listed under. Where the brief's summary of a source did not match what the source says, the correction is marked **Correction**.

Note on method: web search budget for this run was exhausted after the fetches below, so one extra lookup (the exact day of Tenet Security's original Agentjacking post) could not be done. That date is recorded as "June 2026" from the CSA note.

---

## S056: GitSpawn

- **Title:** GitSpawn: A Single Flaw Lets Untrusted Repos Run Code in Claude Code, Codex, Cursor, and Grok
- **Author:** Francisco Rosales, Offensive Security Engineer, Manifold Security (findings also discussed on video with Ax Sharma)
- **Date:** 2026-09-01 (confirmed on the page; an update note on the same date adds Codex and Cursor)
- **URL:** https://www.manifold.security/blog/ai-coding-agents-git-hijack

**Summary.** AI coding agents run git in the background to gather project context, sometimes before you type a prompt, before the workspace-trust prompt and before login. They did so without stripping the repository's own git config, and some git settings name a program to run. `core.fsmonitor` is one: any git command that refreshes the index (`git status`, `git diff`) runs the program it names, as you, outside the agent's sandbox, with no approval prompt. Eight findings across seven agents; four were still unpatched at publication.

**Gaps it shows**

1. *Opening a folder with an agent is an execution event.*
   - Claude Code ran `git status` at startup, before the workspace-trust prompt (patched in 2.1.196). Qwen Code ran it before authentication; Grok Build on the first keystroke of a prompt; Hermes Agent on the first message; Goose when `goose review` ran `git diff` (CVE-2026-72718, patched 1.44.0). Codex and Cursor were affected and patched.
   - Still unpatched at publication (re-confirmed 2026-09-01): Qwen Code 0.22.3, Grok Build 1.0.13, Hermes Agent 0.21.0 (CVE-2026-71963, assigned by VulnCheck after no vendor triage), and a second Claude Code path (`claude ultrareview`, confirmed on 2.1.252) that uses a different, deliberately unnamed git key.
   - The command runs with your privileges: SSH keys, cloud credentials, tokens in shell config, every repo on disk.
2. *The sandbox and permission prompts do not see it.* The git subprocess runs outside the agent's sandbox, so the agent's permission model never gets a chance to ask.
3. *How the repo has to arrive.* Cloning, fetching or pulling from a hostile URL does NOT trigger it (a clone does not copy the remote's config). The `.git` folder has to arrive as files: a shared `.zip`, shared drive, sync folder, USB stick. The researchers used a zip for every proof of concept.
4. *What to check.* If you receive a repository as files, inspect `.git/config` before opening the folder with an agent. For agent builders: sanitize git config on background calls (example given: `git -c core.fsmonitor=false status`).
5. *Bug bounty reality.* Five of eight reports were duplicates of independent reports by others (one filed the same day), which shows several researchers found the same class at once; one vendor never triaged after six contacts.

**Correction.** The brief says the article advises opening untrusted repos in disposable containers. It does not: the only advice is to inspect `.git/config` (users) and sanitize git config (agent builders). Container/sandbox advice for agents comes from S058 (isolated containers with limited files, env vars and egress) and S059 (sandbox local MCP servers).

**Outdated framing it corrects.** "Reading or opening code is passive; only running it is risky." "The agent's sandbox contains whatever happens in the session." "The trust prompt comes before anything runs."

**Quotes**
- "Any setting that names a program can run it."
- "Open a folder with Claude Code and it runs `git status` before you type anything."

---

## S057: How a malicious repo tricked Claude Code into running malware

- **Title:** Fable to Haiku: How a Malicious Repo Tricked Claude Code Into Running Malware (page header also reads "Agents Gone Rogue: ...")
- **Author:** Brian Cumi, AI security researcher, Straiker STAR Labs
- **Date:** 2026-09-22 (confirmed). Discovered 2026-08-24; reported to Anthropic via HackerOne 2026-09-14; closed the same day as "Informative".
- **URL:** https://www.straiker.ai/blog/how-a-malicious-repo-tricked-claude-code-into-running-malware

**Summary.** A researcher asked Claude Code to clone a metrics-client repo, explain it, then "fix that and prepare a PR". The repo's `CONTRIBUTING.md` told reviewers to run a repo-defined subagent before pytest; `.claude/agents/first-pass.md` pinned that subagent to the small Haiku model and scoped it to `src/` and `docs/`, and said a read in the main session does not replace running the agent. Haiku returned two planted, harmless findings; the main model treated that as the audit, never opened `tests/test_compat.py`, and ran pytest. The test file downloaded and ran a Sliver C2 implant before its trivially true assertion, inside `try/except: pass`. The chat showed "11 passed". No jailbreak or prompt injection was used: only documented features.

**Gaps it shows**

1. *A repo can choose who reviews it and how.* Per-repo agent definitions (`.claude/agents/`), workflow sections of `CONTRIBUTING.md`, hooks, `.cursor/` and MCP server definitions shipped in a repo shape what your agent does. Here they downgraded the reviewer model and narrowed its scope.
2. *"Ask the agent to security-review it" is not a guarantee.* The main model accepted the subagent's scoped sweep as the whole review and did not widen it. The FAQ: neither model misbehaved; the gap was that the repo picked its reviewer and nothing re-checked the tests before they ran.
3. *Running a repo's tests executes its code.* The payload ran when pytest loaded the file, before any assertion. Swallowed errors kept the run green. `pytest`, `make`, `check.sh` and other repo-provided commands are execution surfaces.
4. *The vendor puts the boundary at your trust decision.* Anthropic's rationale: honoring the repository's configuration falls under the user's workspace-trust decision. An earlier Auto Mode finding was closed with the same "working as designed" rationale. So the human's "trust this folder" click is the control.
5. *Applies beyond one tool.* The FAQ says any agent that loads per-repo agent/workflow definitions and runs the repo's tests during PR preparation has similar exposure.
6. *What to do (article's recommendations):* do not let agents honor `.claude/agents/` (or equivalents) from an untrusted repo; require human approval before spawning a repo-defined subagent; have the main model read every test file body before the first test run; inventory every repo file that shapes agent behavior as attack surface.

**Not stated by the article:** whether a trust prompt was accepted, which permission mode was used, or whether pytest needed approval. Do not claim these.

**Outdated framing it corrects.** "Have the AI security-review the repo and you're covered." "Tests passed, so the code is fine." "Prompt injection needs a clever jailbreak."

**Quotes**
- "Tests are executable code."
- "No model jailbreak was required."

---

## S058: Agentjacking (CSA research note)

- **Title:** Agentjacking: MCP Injection Hijacks AI Coding Agents
- **Author:** Cloud Security Alliance AI Safety Initiative, summarizing Tenet Security Threat Labs (original research June 2026; exact day not given; Sentry acknowledged the disclosure on 2026-06-03, the day it was submitted)
- **Date:** 2026-06-12 (confirmed)
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-agentjacking-mcp-sentry-injection-20260612/

**Summary.** A Sentry DSN must be embedded in client-side code, and Sentry's ingest endpoint accepts events from anyone holding it. An attacker posts a fake error event whose message is markdown dressed up as Sentry's own remediation guidance. When a developer asks an agent to "look at open Sentry issues", the official Sentry MCP server returns that event with nothing marking it as attacker-written, and the agent follows it (in the PoC, running `npx` on an attacker package), stealing env vars, AWS, GitHub/GitLab, npm, Docker, Kubernetes and CI secrets. Claude Code, Cursor and Codex were tested; 85% success.

**Gaps it shows**

1. *Tool output is input.* Data an MCP server returns (errors, tickets, issues, logs, review comments) can carry instructions the agent cannot tell apart from real guidance. None of the tested agents distinguished injected events from real ones.
2. *Vetting the server's code does not vet its data.* Sentry's server was not compromised. Any server that surfaces content from outside your trust boundary (issue trackers, support queues, code review platforms, log aggregators) is an injection path.
3. *"Public by design" keys are write paths.* The DSN is "a public, write-only credential". Tenet found 71 injectable DSNs in the Tranco top million sites and at least 2,388 organizations with exposed injectable DSNs. Anyone who reads your page source can write into a queue your agent later reads.
4. *Your security stack sees nothing wrong.* The agent acts under your real identity, drops no malware binary, and its traffic looks like normal package management, so IAM, EDR, WAF and VPN passed it in testing.
5. *The vendor will not fully fix it.* Sentry added a filter for the specific payload string and called a root fix "technically not defensible" at platform level. You cannot rely on the integration vendor to close the gap.
6. *What to do (note's recommendations):* list your agent's MCP servers and flag those that surface external or user-controlled content; disable ones you do not need; require human approval before the agent runs commands or installs packages based on MCP-retrieved content; turn off autonomous modes for agents connected to such servers; beware confirmation fatigue; run agents in isolated containers or sandboxes with limited file access, restricted env-var visibility and constrained egress (block cloud metadata endpoints); use short-lived scoped credentials; rotate exposed DSNs and consider a server-side relay so the DSN never ships to browsers.
7. *Maturity:* proof-of-concept and controlled testing, not confirmed mass exploitation (say so when teaching).

Context only, not part of the attack: the note cites Elastic Security Labs finding command-injection bugs in 43% of tested MCP server implementations.

**Outdated framing it corrects.** "Prompt injection comes from shady websites." "An official MCP server from a reputable vendor is safe." "Keys that are public are harmless."

**Quotes**
- "a public, write-only credential."
- "...a legitimately operated MCP server that surfaces user-controlled content is itself an injection pathway."

---

## S059: MCP Security Best Practices (spec revision 2026-07-28) + the 2026-07-28 spec post

- **Title:** Security Best Practices (Model Context Protocol specification, revision 2026-07-28)
- **Author:** Model Context Protocol project
- **Date:** 2026-07-28 (the revision date in the URL; the page shows no separate last-modified date)
- **URL:** https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices
- **Companion skimmed:** "The 2026-07-28 Specification", David Soria Parra and Den Delimarsky (Lead Maintainers), 2026-07-28, https://blog.modelcontextprotocol.io/posts/2026-07-28/

**Summary.** The official threat list for MCP: confused deputy (proxy servers with a static client ID and consent cookies), token passthrough (forbidden), SSRF via OAuth discovery URLs, state-handle hijacking, local MCP server compromise, malicious authorization URLs (`javascript:` and shell injection), stdio proxy escalation, mix-up attacks, localhost redirect impersonation, and scope minimization. For beginners the core section is local server compromise: a local MCP server is a program that runs on your machine with the client's privileges.

**Gaps it shows**

1. *Adding a local MCP server is running a program.* Attacks: a malicious startup command in a client config, a malicious payload inside the server, or a localhost server reached via DNS rebinding. The spec's example startup command runs `npx malicious-package` and then posts `~/.ssh/id_rsa` to a remote URL.
   - One-click install clients MUST show the exact command without truncation (arguments included), flag it as dangerous, require explicit approval and allow cancel. They SHOULD highlight `sudo`, `rm -rf`, network calls and access to home/SSH paths, warn that servers run with client privileges, and sandbox servers with minimal default privileges.
   - Servers meant to run locally SHOULD use the stdio transport, or require an auth token / restricted IPC if they listen over HTTP.
2. *Token passthrough is forbidden.* An MCP server MUST NOT accept tokens not issued for it, and must not forward a user's token unvalidated to a downstream API (breaks audit trails, rate limits and trust boundaries; turns the server into an exfiltration proxy).
3. *Confused deputy.* A proxy server using one static OAuth client ID for everyone, plus a consent cookie at the third party, lets an attacker skip consent; proxies MUST implement per-client consent, exact redirect-URI matching and single-use `state`.
4. *Scope minimization.* Requesting every scope up front (`files:*`, `admin:*`) makes a stolen token catastrophic; start minimal and step up when a privileged operation is first attempted. Common mistakes: wildcard scopes, bundling privileges "to avoid future prompts".
5. *State handles are not passwords.* MCP is now stateless; a server that mints a cart/workflow ID MUST NOT treat possession of it as authentication and SHOULD bind it to the authenticated user.
6. *SSRF.* A malicious server can point a client at `169.254.169.254` (cloud metadata) or localhost services; clients deployed on servers should block private ranges and use an egress proxy.

**What 2025-era MCP explainers now get wrong (from the spec post)**
- The `initialize`/`initialized` handshake and `Mcp-Session-Id` header are retired; each request carries version, client identity and capabilities in `_meta`; optional `server/discover`. Any request can hit any instance behind a load balancer.
- The legacy HTTP+SSE transport is deprecated (one-year transition). Streamable HTTP requests carry `Mcp-Method`/`Mcp-Name` headers.
- Server-initiated `sampling/createMessage`, `elicitation/create` and `roots/list` over a held-open stream are replaced by Multi Round-Trip Requests (`resultType: "input_required"`, client retries with `inputResponses`). Roots, Sampling and Logging are deprecated but keep working at least twelve months.
- Dynamic Client Registration is deprecated in favor of Client ID Metadata Documents; clients must validate `iss`.
- Tasks moved out of the experimental core into an extension; list responses gain `ttlMs`/`cacheScope`.

**Outdated framing it corrects.** "MCP is a stateful session over SSE." "Installing an MCP server is like installing a browser extension with a permission list." (It is an arbitrary command with your privileges.)

**Quotes**
- "Warn that MCP servers run with the same privileges as the client"
- "Show the exact command that will be executed, without truncation"

---

## S060: Slopsquatting (CSA research note)

- **Title:** Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks
- **Author:** Cloud Security Alliance AI Safety Initiative
- **Date:** 2026-04-19 (confirmed). Older than three months; core statistics come from Spracklen et al., USENIX Security 2025 (foundational, with the note's own caveat about newer models).
- **URL:** https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/

**Summary.** Models invent package names, and they invent the same ones repeatedly, so attackers can register them in advance. In the cited study (2.23 million samples, 16 models, Python and JavaScript), 19.7% of samples named at least one nonexistent package (205,474 unique names); open-source models averaged 21.7%, commercial 5.2%. Re-running the same prompt ten times, 43% of hallucinated names came back every run and 58% more than once. Agents now pick and install dependencies themselves, removing the human moment where someone might have noticed.

**Gaps it shows**

1. *Hallucinated names are predictable, so they are squattable.* 38% conflations of two real names, 13% typo variants, 51% pure fabrications; 8.7% of hallucinated Python names exist on npm (cross-ecosystem confusion).
2. *Real incidents.* `react-codeshift` (a conflation of `jscodeshift` and `react-codemod`) spread through 237 repositories via AI-generated agent skills, with downloads driven by agents rather than people. `huggingface-cli` reached 30,000+ downloads in three months after an AI-recommended install command was copied into a large company's public docs. `unused-imports` on npm still had about 233 weekly downloads in Feb 2026.
3. *No human checkpoint.* Agents generate the code, choose the dependency and run the package manager; they can commit and push before monitoring fires.
4. *Install scripts run where the keys live.* Post-install scripts execute in environments holding cloud credentials, source-control tokens, model API keys and sometimes production access.
5. *How to check a new dependency (the note's list):* it exists in the target registry; it was registered before your project started (flag anything registered within the last 30 to 90 days for review); the publisher has a track record; the publisher's identity is confirmed. (The note does NOT list download counts as a check.)
6. *Controls:* treat AI-written imports and install commands as untrusted input; verify against the registry before install; commit lockfiles and verify hashes; put package-installing agents on an allowlist or turn off automated installs; scan docs and examples for install commands; SBOMs.
7. *Caveat:* the rates were measured on 2025 model versions; rates for newer models may differ, and the note claims neither better nor worse.

**Outdated framing it corrects.** "Typosquatting needs a human to mistype." "If the AI suggested it, the package must exist / be the right one." "Newer models don't hallucinate packages" (unproven either way).

**Quotes**
- "43% of hallucinated package names reappeared on every single run"
- "Agentic systems eliminate that checkpoint."

---

## S061: ChainDrop npm worm (+ GitHub changelog on npm trusted publishing)

- **Title:** ChainDrop npm Worm: Bun-loaded CI/CD credential harvester with Ethereum dead-drop C2
- **Author:** Sai Likhith, StepSecurity (a vendor that sells the hardening products it mentions; weigh product references accordingly)
- **Date:** 2026-08-04 (confirmed; updated 18:10 UTC the same day while the incident was live)
- **URL:** https://stepsecurity.io/blog/chaindrop-npm-worm
- **Companion skimmed:** "Unvalidated npm trusted publishing configurations now expire", GitHub Changelog, 2026-10-02 (page marked "Retired"), https://github.blog/changelog/2026-10-02-unvalidated-npm-trusted-publishing-configurations-now-expire

**Summary.** An attacker took over a maintainer's GitHub account (not an npm token), pushed unsigned commits to `main` that added a `preinstall` dropper, and let the projects' own release workflows publish through OIDC trusted publishing, producing valid SLSA provenance. `keyv@6.0.0`, `flat-cache`, `file-entry-cache` and others (roughly 150 million weekly downloads each for the top three) carried it; within four hours the worm had used stolen credentials to republish 444 packages / 2,212 versions across 14+ organizations, attaching self-minted Sigstore provenance. The payload harvested npm, GitHub, cloud, Kubernetes and Vault secrets, CI runner memory, wallets, and AI-tool credential files.

**Gaps it shows**

1. *Provenance proves where it was built, not that it was authorized.* In the March 2026 axios compromise, missing provenance was the warning sign; here the malicious release had valid attestations, so any gate on "has valid provenance" would have passed it.
2. *Lockfiles do not protect installs that bypass them.* Backstage's end-to-end tests scaffold a new app and install fresh, outside the repo lockfile, and resolved compromised versions transitively between 09:31 and 10:40 UTC; the payload ran and reached its C2.
3. *Install scripts are the dropper.* Running CI with `--ignore-scripts` (and vetting the few packages that need build scripts) "neutralizes this dropper class completely".
4. *Minimum release age.* A 3 to 7 day cooldown would have prevented most automatic adoption (carriers were reverted within hours). Settings named: npm `min-release-age` (npm 11.10+), pnpm `minimumReleaseAge` (10.16+), Yarn `npmMinimalAgeGate` (4.10+), Bun `minimumReleaseAge` (1.3+), Dependabot `cooldown`.
5. *Egress allowlists, not reputation lists.* The dropper downloaded the real Bun runtime from github.com and exfiltrated via GitHub; an allowlist blocks the fetch, while domain reputation sees only trusted domains.
6. *Agent config files are now persistence.* A commit added `.claude/settings.json` with a SessionStart hook (matcher `*`) and `.vscode/tasks.json` with a `runOn: folderOpen` task, so starting Claude Code in the repo or opening it in VS Code re-runs the dropper without any `npm install`. Worm commits were authored as "claude".
7. *Stealers now target AI tool credentials:* `.claude/credentials.json`, `.claude.json`, `.codex/auth.json`, `.cursor/credentials.json`, `.openai/auth.json`, `.anthropic/auth.json`, `.gemini/.env`, `.kiro/settings/mcp.json` and others, alongside `~/.npmrc`, `~/.aws/`, `~/.kube/config`, SSH keys, `~/.git-credentials`, `~/.docker/config.json`.
8. *Incident response order matters.* Assume compromise for any machine or runner that installed an affected version; remove the token monitor BEFORE rotating (revoking the stolen token triggers a payload); rotate everything including AI tool credentials, from a clean machine; reinstall with `npm ci --ignore-scripts`; pin known-good versions with `overrides`.
9. *For maintainers:* phishing-resistant MFA, short-lived fine-grained tokens, branch protection requiring review even for owners; watch release-input changes (new `files` entries, new lifecycle scripts, release tooling edits).
10. *How npm publishing is changing (GitHub changelog, 2026-10-02):* unvalidated trusted-publishing configurations now expire 48 hours after creation unless used for a successful publish; changing the repo/project identity needs a new trust relationship; npm rejects trusted-publishing tokens from GitHub Actions `issue_comment` events (in addition to `pull_request_target`). Related posts listed: staged publishing for new packages (Oct 2), opt-in dist-tag permissions (Sep 30), stage-only npm tokens (Sep 18) — titles only, not read.

**Outdated framing it corrects.** "Look for the provenance badge." "Commit your lockfile and you're safe." "Malware arrives through `npm install` only." "Only big companies' secrets are targeted" (AI tool tokens are a named target).

**Quotes**
- "Provenance proves which commit was built. It cannot prove the commit was authorized."
- "neutralizes this dropper class completely" (on `--ignore-scripts`)

---

## S062: Playback: two real security moments (topics only)

- **Title:** Playback: security moments (a malicious redirect, and verifying a download before install)
- **Author:** Aaron Orelup (his typed and pasted prompts); the checks were run by Claude in those sessions
- **Date:** two sessions: 2026-09-28 (redirect) and 2026-10-10 (download verification). The brief's single date of 2026-10-10 covers only the second.
- **Locators:** playback-lens `C--Users-soulo-Organized-Personal-My-Projects-Sandbox-2/7c75a0b6-4bcf-45ae-9869-1489cad914a6` and `C--Users-soulo-Organized-Personal-My-Projects-photoshop/dea3f681-154f-47d6-a4f4-05cb5da99bb5`
- **Credibility note:** this is practice evidence (what a real user hit and asked), not independent expertise; the explanations come from the agent's answers in those sessions.

**Summary.** (1) Following a link on a public paste site, an ad network redirected to a tracking URL and a fake "I am not a bot" page; the user clicked it and asked whether the PC was infected. The agent explained the two common fake-CAPTCHA tricks and checked the machine. (2) Before installing a newly famous free AI-built app, the user wrote explicit install conditions; the agent verified the origin, checksums, signature and lookalike domains, then installed a portable build.

**Gaps it shows**

1. *Fake CAPTCHA pages.* Two tricks: the page silently copies a harmful command to the clipboard and tells you to press Win+R, Ctrl+V, Enter (the dangerous one); or it asks you to click "Allow" notifications and then spams you. Ticking the box alone installs nothing.
2. *What to check after clicking one (Windows):* clipboard contents; Run-dialog history; recent PowerShell history; Downloads; new executables/scripts in Temp and AppData; startup programs and Run keys; scheduled tasks created recently; Defender real-time protection, definitions and detections; then remove unknown sites from browser notification permissions and run a quick scan.
3. *Ad redirects come from the host page's ads, not the content.* The paste itself was harmless; the raw-text view of the same paste avoids the ad layer.
4. *Checking a download before install:* the repo is the genuine origin with real, incremental history (not a dumped blob); releases are built by CI and published as GitHub release assets; checksums verified (and also matched the platform's own server-side digest); Windows binaries carry a valid Authenticode signature from an identity-verified publisher; Defender scan clean; no credible malware reports; VirusTotal not queried (no API key), so the file hashes were handed to the human to check.
5. *Checksums from the same pipeline prove the download is intact, not that the pipeline is clean.* No independent signatures or provenance attestations existed; an open issue flagged unpinned CI actions and an unpinned signing package next to signing secrets. (Mirrors S061's provenance point.)
6. *Lookalike sites appear within days of a free app going viral.* One lookalike domain was registered in launch week (the same day as the first press coverage, a day before the release the user had heard about) and a third-party scanner reported several vendors blacklisting it; a user's "is this site fake?" issue went unanswered. Rule: download only from the project's own repo or site.
7. *SmartScreen silence is not approval.* Files the agent downloaded with a command-line tool did not get the "downloaded from the internet" mark, so SmartScreen never prompted. Nothing was disabled; the check simply never applied.
8. *Installers have side effects.* The MSI installed machine-wide, silently, and registered "Open with" entries for .psd, .png, .jpg, .tif, .webp and about a dozen other types; a portable per-user build avoided touching file associations.
9. *Hype signals.* A 10-day-old repo with 41.8k stars, 8 releases in 9 days and claims that shrank from "parity" to "25-35%"; the user's own rule: praise with no criticism is itself a signal.
10. *The human sets the bar; the agent verifies against it.* The user separated tolerance for buggy software (his to lower) from running an unverified binary (not his to lower), and forbade disabling SmartScreen or antivirus: a block is information to report, not route around.

**Outdated framing it corrects.** "If Windows didn't warn me, the file is fine." "A matching checksum means the file is safe." "Ticking 'I'm not a robot' can't hurt."

**Quotes**
- "It does not mean run an unverified binary."
- "If something blocks it, that's information — report it, don't route around it."
