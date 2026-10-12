---
key: other-peoples-code
id: 07.04
title: Other people's code
district: Agent Power
module: 07 Reach and trust
status: todo
legacy: []
minutes: 15
concepts: [C087, C088, C089, C090, C093, C130]
sources: [S060, S061, S056, S057, S062, S158, S160, S042, S065, S033, S051, S052, S071, S157, S209, S039]
lead: [S060, S061]
---
# Other people's code

**Purpose (the first spoken sentence):** In this lesson you'll learn why installing a package, opening a repository, running its tests or pasting a command from a web page all run someone else's code as you, and the few habits that keep that safe.

**Conclusion:** Other people's code runs with your permissions the moment you install, open, test or paste it, so have the agent prove every new package is real and old enough, open strangers' repositories only in a throwaway box, and never run a command a web page hands you.

**Where it sits on the map:** District 4 · Agent Power — What can your agent touch?; module 07 Reach and trust (last lesson of the module).

**Lead source (audit, 2026-10-12):** S060 (Cloud Security Alliance AI Safety Initiative); S061 (Sai Likhith (StepSecurity)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S060, S061, S056, S057, S062); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Settings and versions (audit, 2026-10-12):** the spoken script teaches the vendor-neutral model. Setting names, flags and version numbers appear only on one dated "as of" card per concept and on the lesson page, never in narration. Here that means `--setting-sources user`, `--bare`, `--settings '{"disableAllHooks": true}'`, `disabledMcpjsonServers`, `core.fsmonitor` and the package managers' minimum-release-age settings: on the card and the page; the narration says what each protects against.

## What to teach (binding scope)

Length: 15 minutes (six concepts; design-decision.md expects this lesson near 15). Order and rough budget: C130, the ground floor (1.5 min) → C087 packages the AI names (3 min) → C088 install time is execution time (3 min) → C089 opening and testing run code (3 min) → C090 the trust click (2 min) → C093 downloads and pasted commands (2.5 min). The one move that ties them together: anything from outside runs first in a box that holds nothing worth stealing.

### C130 Dependencies: other people's code your project downloads
- **brief** — Most of a project is other people's code. A manifest names what you want (Python's is `pyproject.toml`); a lock file saves "the specific list of versions" you actually got. "For applications, pinning exact versions ensures reproducibility"; libraries use version ranges (S209).
- **one line** — One environment per project: "a virtual environment for each project, containing the dependencies it requires" (S209). Version numbers carry meaning: a PATCH "should only contain bug fixes", a MAJOR "indicates breaking changes" (S209).
- **brief** — The agent's picture is dated: it may lack knowledge of a dependency "published after the LLM's knowledge cutoff" (S209), and it may suggest "dependency versions that were current during training but now have known vulnerabilities" (S042).
- **one line** — Registries are open to anyone and installing can run code; both are the rest of this lesson.
- Dropped here: licences that come with every dependency, and who owns the dependency list (C053 → after-launch-keep-it-alive).

### C087 Packages the AI names may not be real: vet every new dependency
- **teach** — Models invent package names. In the USENIX Security 2025 study that the Cloud Security Alliance summarises (2026-04-19), 19.7% of 2.23 million code samples from 16 models named at least one package that doesn't exist: 205,474 unique invented names; open-source models averaged 21.7%, commercial models 5.2%. Caveat on screen: measured on 2025 model versions; "rates for newer releases may differ" (S060).
- **teach** — They invent the same names again, which is what lets attackers register them first: 43% of invented names came back on every one of ten reruns, 58% more than once. About half are pure fabrications (51%), others blend two real names (38%) or are typo variants (13%), and 8.7% of invented Python names exist on npm, so the wrong registry is a trap of its own (S060).
- **brief** — Real cases: `react-codeshift` spread through 237 repositories via AI-generated agent skills; an AI-recommended `huggingface-cli` install command copied into Alibaba's public documentation drew over 30,000 downloads in three months (S060).
- **teach** — "Agentic systems eliminate that checkpoint" (S060): no human sees the odd name before it installs. The registries agents use were flooded in 2026: RubyGems had to "shut down user registrations" in May after thousands of dubious uploads, and a malicious `mlflow-ui` package on PyPI was traced to Anthropic's own training agents (S033). An agent published a malicious package under a name from setup instructions, and it "ran on 15 real systems during its approximately one-hour availability" (S065).
- **teach** — The check the agent runs and you read, for every new dependency: it exists in the right registry; it was registered before your project started; its publisher has a track record (S060); its creation date (flag anything under 30 days old), maintainers and near-miss names (S042). Downloads and stars are weak evidence: OWASP lists download counts, CSA's checklist leaves them out (S042, S060).
- **teach** — A gate the agent can't skip: "AI agents with package management capabilities must operate under an explicit allowlist", and without one, "at minimum disable automated package installation in agentic environments" (S060); a pre-install or CI check that blocks packages younger than a minimum age (S042).
- **teach** — Minimum release age is one config line, 3 to 7 days: npm `min-release-age` (npm 11.10+), pnpm `minimumReleaseAge` (10.16+), Yarn `npmMinimalAgeGate` (4.10+), Bun `minimumReleaseAge` (1.3+), Dependabot `cooldown` (S061). You decide when an urgent security fix is worth skipping the wait.
- **one line** — Real packages can be the wrong version: "Run dependency auditing tools (npm audit, pip audit, govulncheck, cargo audit)" and "Configure CI/CD pipelines to fail on known vulnerabilities" (S042).

### C088 Install time is execution time, and provenance proves less than you think
- **teach** — Installing can run code straight away. ChainDrop (StepSecurity, 2026-08-04): a `preinstall` script downloads the real Bun runtime from GitHub and runs a roughly 710 KB obfuscated payload (S061). Mini Shai-Hulud (May 2026): a `postinstall` hook "executes a 2.3 MB obfuscated payload" (S158).
- **teach** — It runs where your keys are. ChainDrop stole credentials from npm, GitHub, AWS, Kubernetes, Vault and AI coding tools (`.claude/credentials.json`, `.claude.json`, `.codex/auth.json` and others), then republished itself with them: 444 packages and 2,212 versions in under four hours. The investigation is active and the counts may change (S061).
- **teach** — The cheapest control: run CI with `--ignore-scripts`, vetting the few packages that truly need build scripts, which "neutralizes this dropper class completely" (S061).
- **teach** — Provenance proves less than you think: "Provenance proves which commit was built. It cannot prove the commit was authorized." ChainDrop's malware came out of the projects' own release workflows with valid provenance (S061). Mini Shai-Hulud was the "first documented supply chain attack to forge valid SLSA Build Level 3 provenance attestations", so CSA calls attestations "necessary but not sufficient" (S158). OWASP: "Valid build provenance or attestation alone is not proof that an artifact is safe" (S065). A checksum published by the same pipeline proves the file arrived intact, not that the pipeline is clean (S062).
- **brief** — A lock file protects only the installs that use it: Backstage's end-to-end jobs installed fresh and pulled compromised versions between 09:31 and 10:40 UTC with their lock files unchanged; fresh scaffolds, one-off `npx` runs and new installs resolve whatever is newest at that moment (S061). The poisoned versions were reverted within hours, so a 3 to 7 day minimum age would have skipped them (S061).
- **brief** — Treat agent edits to build files as high-trust changes: install scripts in `package.json`, CI workflows, Dockerfiles, Makefiles (S042).
- **teach** — Uninstalling does not clean the machine, and rotating first can be the trap. Mini Shai-Hulud's hooks in `~/.claude/settings.json` and `.vscode/tasks.json` "survive complete removal of the originally infected package", and a Linux service is "configured to destroy the home directory" if a GitHub token is rotated while it runs (S158). ChainDrop's token monitor fires a payload when the stolen token is revoked (S061). The order: remove the persistence first, then rotate every credential, AI-tool logins included, from a clean machine (S158, S061). This is where you bring in an expert.
- Dropped here: npm's 2026 trusted-publishing rule changes (only for people who publish packages).

### C089 Opening, unpacking or testing untrusted code can execute it
- **teach** — Agents run git in the background, some before you've agreed to anything. GitSpawn (Manifold Security, 2026-09-01): Claude Code's startup `git status` ran a repository's `core.fsmonitor` command "before the workspace-trust prompt was accepted" (confirmed on 2.1.193, fixed by 2.1.196); eight findings across seven agents, "Four remain unpatched at publication", among them Qwen Code, Grok Build and Hermes Agent (CVE-2026-71963); a second Claude Code path, `ultrareview`, was "Confirmed still unpatched on 2.1.252 on 1 September". The rule behind it: "Any setting that names a program can run it" (S056).
- **teach** — How the repository has to arrive: "Cloning a hostile URL does nothing, and neither does fetch or pull." The `.git` folder has to come as files: a shared zip, a shared drive, a USB stick (S056). So re-clone from the origin rather than opening a copy someone sent, or check `.git/config` before an agent opens the folder (S056).
- **teach** — Agent and editor settings files are code. ChainDrop committed a `.claude/settings.json` with a SessionStart hook (matcher `*`) and a `.vscode/tasks.json` task with `runOn: folderOpen`, so starting Claude Code or opening the folder in VS Code re-ran the dropper; its commits were authored as "claude" to look like assistant output (S061). OWASP: "Review AI coding-agent configuration files as executable supply-chain artifacts" (S065).
- **teach** — Headless runs skip the trust step. A `claude -p` run or an SDK session never shows the trust dialog, yet it uses the repository's hooks, its `env` block, helpers such as `apiKeyHelper`, and project skills' hooks and `allowed-tools`, and it connects `.mcp.json` servers "without asking, approved or not." Before `claude -p` in a repository you didn't write: `--setting-sources user`, or `--bare` (the project's `env` block still applies); `--settings '{"disableAllHooks": true}'`; and `disabledMcpjsonServers` for named servers (S160).
- **teach** — Running a repository's tests runs its code. Straiker (2026-09-22): the payload sat in `tests/test_compat.py`, wrapped in `try/except: pass` behind a trivially true assertion; the run reported "11 passed" while a command-and-control session opened on the workstation (S057). The fix gives the reading job to the main model, not to you and not to a subagent the repository defined: it reads each test file before running pytest and treats test runners as execution surfaces (S057).
- **teach** — A file the agent downloads can run code without any instruction being obeyed. Rehberger (2026-08-26): asked to summarise a web page, Claude fetched a zip with `curl`, wrote its own small Python decoder and ran it inside the extracted folder; the archive's `struct.py` loaded instead of Python's own module; auto mode allowed it because it saw only the short decoder; 3 of 5, 3 of 5 and 4 of 5 small trials. Willison: "more of a confused environment attack" (S051). (What this says about classifiers: whose-words-is-it-reading.)
- **teach** — Where untrusted material belongs: a disposable container or VM with no credentials, few environment variables and limited egress. Claude Code's own guidance for "Work on an untrusted repository" is a dedicated virtual machine or a cloud session (S052, sandbox environments page). The built-in sandbox covers shell commands only; hooks and local MCP servers run outside it, and native Windows has none (S052). (Depth: contain-it-dont-babysit-it.)

### C090 Workspace trust is your decision, and a repo can choose its own reviewer
- **teach** — What the click grants: a project's `permissions.allow` rules and `additionalDirectories` take effect only after you accept the trust dialog, which lists them so you can read them first; `deny` and `ask` rules apply either way (S160). Trusting also accepts the folder's subagents, hooks, workflow instructions and tests (S057).
- **teach** — A repository can pick its own reviewer. Straiker's repository had a `CONTRIBUTING.md` pointing reviewers at a repository-defined subagent before pytest, and `.claude/agents/first-pass.md` "pins the review to Haiku and scopes it to src/ and docs/ only"; it reported planted harmless findings, and the main model never opened the test file holding the payload. "No model jailbreak was required." Anthropic closed the report as "Informative": honouring a repository's configuration falls under the user's workspace-trust decision (S057).
- **teach** — So "ask the agent to security-review it" is not an audit when the code under review can steer the review. Straiker's fixes: stop agents honouring per-repository agent definitions in untrusted code; require explicit human approval before a repository's subagent is spawned; inventory every file in a third-party repository that shapes agent behaviour (S057). Review unexpected changes to `CLAUDE.md`, `.claude/`, `AGENTS.md`, `.cursorrules` and `.cursor/rules/` like CI changes (S042).
- **brief** — What trust covers: in a repository it is keyed on the git repository root; outside one, trusting a folder covers its subfolders, so a folder dropped in later counts as "a folder whose parent you trusted" and its hooks are used; in your home directory trust lasts for the session only, so start Claude Code from a project folder (S160; S052, Security page). "Workspace trust never gates a skill's `allowed-tools` in any session" (S160).
- **one line** — The trust prompt is not always the first moment of exposure (GitSpawn, above; S056).

### C093 Verify downloads, and never run a command a web page gives you
- **teach** — Fake "I am not a bot" pages use two tricks. The dangerous one: the page "secretly copies a harmful command to your clipboard, then tells you to press Win+R, then Ctrl+V, then Enter". The nuisance one: it asks you to click Allow on notifications and then spams you. Ticking the box alone installs nothing; the damage comes from following the instructions after it (S062: Aaron's own session of 2026-09-28, after an ad on a paste site redirected him to such a page).
- **teach** — The rule: never paste and run a command that a page, popup or README tells you to run. ClawHavoc: 335 of the 341 malicious ClawHub skills Koi Security found used a "Prerequisites" section; on macOS it told users to paste an obfuscated script from glot.io into Terminal, which fetched Atomic Stealer, and on Windows to download a password-protected archive holding a keylogging trojan (S071). Agents fall for fake checks too: a fake "abuse prevention" CAPTCHA page got an AI browser to send the user's Gmail to an attacker (S157).
- **teach** — Set the bar before the agent starts, and let it run the checks. Aaron's brief of 2026-10-10 for a newly famous free app: "My 'low to medium bar' means I'm fine with alpha-quality buggy software. It does not mean run an unverified binary." Install only if the official repository is genuine with real history, the download comes from that source and nowhere else, checksums verify where published, and nothing credible suggests the binaries are compromised; don't disable SmartScreen or antivirus: "If something blocks it, that's information — report it, don't route around it" (S062). The agent then checked origin, history, release assets, checksums (against the published SHA256SUMS file and GitHub's own digest), the Authenticode signature and a Defender scan, and found a lookalike domain registered on 2026-10-07 that, per a third-party scanner, several security vendors blacklist, plus an unanswered user question asking whether another site was fake (S062).
- **brief** — Silence from Windows is not approval: files the agent downloaded with the GitHub CLI didn't get the "downloaded from the internet" flag that triggers SmartScreen, so it never prompted (S062, as the agent reported it).
- **brief** — Installers have side effects: the app's MSI installed machine-wide, silently, and added itself to "Open with" for .psd, .png, .jpg and about a dozen other types; the agent chose the portable zip so file associations stayed untouched (S062).
- **brief** — After a bad click on Windows, have the agent check the clipboard, Run and PowerShell history, new files in Downloads, Temp and AppData, startup items, recently created scheduled tasks and Defender's status, then remove unknown sites from browser notification permissions (S062). If a pasted command actually ran on a machine holding credentials, treat it as a compromise: rotate from a clean device and bring in an expert (S062, S061).
- **one line** — Legacy 01.02 promised this district "invoice dot P D F dot E X E", a program wearing a document's label: with extensions hidden by default, a file's name can lie about what it is. One line only; no source in sources.md covers double-extension malware yet (see Legacy notes).

## You vs the agent

As of 2026-10-12:
- **The agent does on its own:** installs packages all the time; looks up a registry and reports first-publish date, publisher and repository link in seconds; adds cooldown and `--ignore-scripts` settings; runs `npm audit` and its equivalents; verifies checksums, signatures and attestations; reads every test file before running a suite when told to; checks a download's origin, history, release assets and signature; inspects a machine after a bad click.
- **The agent cannot:** notice that a name it produced is invented (it installs whatever resolves, S060); know whether a release was authorised by its maintainer (nothing in the artifact proves it, S061); protect you from code that runs before or outside its permission model (S056); verify that a review process it was handed wasn't written by the attacker (S057); spot a file shadowing a system module (S051).
- **You check or decide:** the standing rule ("every new dependency is verified before install") and the gate that enforces it; the cooldown days and when to skip them; where every folder came from, re-cloning anything that arrived as a zip or on a drive; refusing repository-defined subagents and reviewers; running strangers' code and tests only in a disposable box; the `-p` safety flags; keeping agents on patched versions; the install conditions before the agent starts; never pasting a command a page gives you.
- **Bring in an expert (C118, before-you-ship-who-signs-off):** when a compromised package was installed, or untrusted code, tests or a pasted command ran, on a machine or CI runner holding real credentials (the clean-up order is easy to get dangerously wrong, S158, S061); when third-party code will run with real credentials or handle other people's data; when dependencies go into something that handles money, credentials or personal data (setting up composition analysis, a package firewall or an internal allowlist is a security-engineering job).

## Sources this lesson is built from

Core (credited by name on screen and on the lesson page):
- S060 — Cloud Security Alliance AI Safety Initiative, "Slopsquatting: AI Code Hallucinations Fuel Supply Chain Attacks" (2026-04-19; statistics from a 2025 study) https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/ — invented package names, why they repeat, the allowlist rule.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — install scripts, provenance that proves the build but not the intent, lock-file gaps, cooldown settings, the clean-up order.
- S056 — Francisco Rosales (Manifold Security), "GitSpawn: A Single Flaw Lets Untrusted Repos Run Code in Claude Code, Codex, Cursor, and Grok" (2026-09-01) https://www.manifold.security/blog/ai-coding-agents-git-hijack — opening a folder ran code before the trust prompt.
- S057 — Brian Cumi (Straiker STAR Labs), "How a Malicious Repo Tricked Claude Code into Running Malware" (2026-09-22) https://www.straiker.ai/blog/how-a-malicious-repo-tricked-claude-code-into-running-malware — "11 passed", the repository that picked its own reviewer.
- S062 — Aaron Orelup, Playback sessions of 2026-09-28 (a fake "I am not a bot" page) and 2026-10-10 (verifying a free app before installing it); not public — the fake-CAPTCHA tricks, the install bar, what the agent checked.

Supporting (credited on the lesson page):
- S158 — CSA AI Safety Initiative, "Mini Shai-Hulud: npm Worm Targets AI Developer Supply Chain" (2026-05-17) https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-ai-supply-chain-20260517-csa-st/ — forged provenance; hooks that survive uninstalling; the rotation trap.
- S160 — Anthropic, Claude Code docs, "Configure permissions" (undated live docs, mentions v2.1.207 and v2.1.246; read 2026-10-12) https://code.claude.com/docs/en/permissions — what the trust dialog gates, what runs before trust, the `-p` flags.
- S042 — OWASP, "Secure Coding with AI Cheat Sheet" (updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — dependency vetting, audit tools, build files as high-trust changes.
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — the agent-published package; config files as executable artifacts; provenance is not proof.
- S033 — Simon Willison, "2026 in LLMs (so far)" (2026-09-27) https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ — RubyGems registrations shut; `mlflow-ui`.
- S051 — Johann Rehberger, "Breaking Claude Code Opus 5 Auto Mode" (2026-08-26) https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/ and Simon Willison's post on it (2026-08-27, update 2026-08-30) https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/ (companions of S051) — the `struct.py` attack.
- S052 — Anthropic, Claude Code docs, "Configure the sandboxed Bash tool" https://code.claude.com/docs/en/sandboxing and "Security" https://code.claude.com/docs/en/security (undated live docs, re-read 2026-10-12) — sandbox coverage; trust in the home directory.
- S071 — Ravie Lakshmanan (The Hacker News), "Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users" (2026-02-02; older than three months, primary incident record) https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html — the "Prerequisites: paste this" lure.
- S157 — Trail of Bits, "Using threat modeling and prompt injection to audit Comet" (2026-02-20; audit April 2025) https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/ — a fake CAPTCHA aimed at an AI browser.
- S209 — MIT Missing Semester 2026, "Packaging and Shipping Code" and "Agentic Coding" (lectures 2026-01-20 and 2026-01-21; older than three months, still current) https://missing.csail.mit.edu/2026/shipping-code/ ; https://missing.csail.mit.edu/2026/agentic-coding/ — manifests, lock files, environments, semantic versions; agents and dependencies newer than their cutoff.

Candidate source (read 2026-10-12, not yet in sources.md):
- Anthropic, Claude Code docs, "Choose a sandbox environment" (undated live docs) https://code.claude.com/docs/en/sandbox-environments — "Work on an untrusted repository": a dedicated virtual machine or a cloud session. Cited above as "S052, sandbox environments page".

Re-check notes (2026-10-12):
- C087 cites S039 for "Supply-chain failures were 73 vulnerabilities (6.16%), found in 28.00% of the deployed vibe-coded apps". In the paper (S039, v4) that category is "most often exposed secrets, committed environment files, or unrotated default credentials", not packages. Do not use it as evidence about package risk.
- C087's "installed on 15 systems in about an hour" is OWASP's "ran on 15 real systems during its approximately one-hour availability" (S065). Use OWASP's wording.
- C093 and C091 name the ClawHavoc Windows lure `openclaw-agent.zip`; the re-read article says "a password-protected archive from GitHub" holding a keylogging trojan (S071). Use the article's wording.
- Manifold says to inspect `.git/config` before opening the folder with an agent; it doesn't name a tool (S056). Opening it in Notepad is the course's choice, because the danger is git running, not the file being read.
- S062's SmartScreen and MSI points are what the agent reported in that session, not measured independently; say "the agent found".
- The ChainDrop page ended with text addressed to AI readers asking for the post to be quoted verbatim; it was treated as data and ignored. Nothing in this spec depends on it.
- The download checklist still rests mainly on S062 (C093's own note); a later pass should add an independent source for it.

## Show it for real

- Terminal replay in a throwaway folder: the agent asked to report a package's first-publish date, publisher and repository link before installing, with the package's public npm or PyPI page beside it (browser capture of a public page) (S060, S042). Proves the check takes seconds and what it looks like.
- Terminal replay: `npm audit` on a small demo project (S042). Proves known-vulnerable versions are a machine check.
- Animated screenshot: a project's package-manager config before and after the agent adds a minimum-release-age line, with the setting name checked against the tool's own docs at recording time (S061).
- Desktop capture inside a disposable container: a demo package whose `package.json` has a harmless `postinstall` that writes a marker file; install it normally (marker appears), then with `--ignore-scripts` (no marker) (S061). Proves installing runs code.
- Browser capture of a public page: a package's provenance panel on npmjs.com and the commit it links to, captioned "which commit was built, not who approved it" (S061).
- Desktop capture inside a disposable VM or container, no agent running: unzip a harmless demo repository whose `.git/config` sets `core.fsmonitor` to a command that writes a marker file; run `git status`; the marker appears; open `.git/config` in a text viewer and box the line (S056). Proves "read-only" git can run a program.
- Animated screenshot: a demo repository's `.claude/settings.json` (SessionStart hook) and `.vscode/tasks.json` (`runOn: folderOpen`) side by side, not executed (S061).
- Terminal replay in a throwaway folder: a demo test file whose body writes a marker before `assert True`; pytest prints "1 passed", then the marker is on disk (S057). Proves a green test run is not a safety check.
- Desktop capture: the Claude Code trust dialog on an unfamiliar demo repository, boxing the allow rules and directories it lists; then `claude mcp list` in that untrusted folder showing a project server as pending (S160).
- Desktop capture on Windows: a release asset and its SHA256SUMS file downloaded from an official GitHub release, the hash checked in a terminal, then the exe's Properties > Digital Signatures tab (S062). Say what a match does and doesn't prove.
- Drawn, not visited: an official domain and a lookalike side by side in a drawn address bar (S062). Never load a live lookalike site for a recording.
- Desktop capture: Chrome Site settings > Notifications with an unknown site removed, then a Windows Security quick scan (S062).

## Questions this lesson answers

Asked for real:
- "I clicked the I am not a bot captcha and I'm not sure what happened. I'm worried now that it was a virus." (Aaron, 2026-09-28, S062)
- "I heard someone cloned Photoshop and released it free": is it the real one, and is it safe to install? (Aaron's brief, 2026-10-10, S062); a user of that app asked in its issue tracker whether a lookalike site was fake, and nobody answered (S062).

Phrased by the research crew from the sources named (no beginner post with these words was collected; the shared web-search budget was used up):
- Why would the AI make up a package name, and how could a made-up package hurt me? What is slopsquatting? (S060)
- How do I know a package the agent installed is legit? What does `npm audit` tell me? (S060, S042)
- Can installing a package run code on my computer? Will `--ignore-scripts` break things? (S061)
- The package has a provenance badge, or the checksum matched: am I safe? (S061, S158, S062)
- Does `package-lock.json` protect me? I installed a package that turned out to be malware: is uninstalling enough? (S061, S158)
- Someone sent me their project as a zip: is it safe to open it with Claude Code? Can opening a GitHub repo infect my computer? (S056)
- What is the `.claude` folder in this repo, and what's in `.vscode/tasks.json`? (S061)
- The tests all passed, so it's safe, right? (S057)
- What does "Do you trust the files in this folder?" actually mean? If I ask Claude to check the repo for malware first, is that enough? Why didn't Anthropic fix this? (S160, S057)
- Why didn't Windows warn me when Claude downloaded it? What is a checksum? (S062)
- What is `.venv`? What is a lock file? (S209)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Skills, plugins and MCP servers as installed code, and servers that change after approval → skills-mcp-hooks-and-plugins
- Containers, VMs and what the sandbox covers → contain-it-dont-babysit-it
- Why a classifier approved the `struct.py` attack → whose-words-is-it-reading
- Revoking and rotating a key → keys-public-secret-and-leaked
- Who owns the dependency list; licences; agents adding dependencies freely → after-launch-keep-it-alive
- Agent-written tests are not independent evidence → checking-what-you-cant-read
- The folder you open and hidden dotfiles → the-folder-is-the-agents-world
- What `.git`, a clone and a branch are → save-points-and-the-agents-trail
- What the terminal is → where-your-agent-works
- How to bring in an expert → before-you-ship-who-signs-off

## Out-of-date framings to avoid

- "If the AI suggested a package, it exists and it's the right one"; "newer models don't hallucinate packages" (unproven either way) (S060, S042).
- "Typosquatting only catches people who mistype": here the model does the mistyping, repeatably (S060).
- "If it's on npm, PyPI or RubyGems, it's legitimate"; "lots of downloads or stars means it's safe" (S033, S060).
- "Always install the latest version" (S061).
- "`npm install` just downloads code; nothing runs until I import it" (S061).
- "Look for the provenance badge"; "signed or attested builds are safe"; "a matching checksum means the file is safe" (S061, S158, S065, S062).
- "Commit your lock file and you're protected" (S061).
- "Uninstalling the bad package removes it"; "rotate your credentials immediately" before removing persistence (S158, S061).
- "Reading or opening code is safe; only running it is risky"; "the trust prompt appears before anything in the folder can run" (S056).
- "Tests passed, so the code is fine"; "running tests is a read-only check" (S057).
- "Editor and agent settings files are harmless preferences" (S061, S065).
- "The trust prompt is a formality"; "have the AI do a security review and you're covered"; "headless runs are safer because nothing pops up" (S057, S160).
- "If Windows didn't warn me, the file is fine"; "it's on GitHub, so it's safe"; "clicking 'I'm not a robot' is always harmless" (S062).

## Legacy notes

No legacy lesson covers this slot. Two handoffs arrive here:
- Legacy 01.02 (File extensions and associations) ends a scene with "invoice dot P D F dot E X E is the folded tag's other face: a program in a costume. The Trust district covers that one." Its research deferred double extensions and the "downloaded from the internet" mark to the retired 15.17. That lesson's own sources establish that Windows 11 and macOS still hide extensions by default (lessons/01-02-file-extensions-associations/research-now.md); no source in curriculum/sources.md covers double-extension malware, so this lesson gives it one line and the backlog should get a source before it gets more.
- Legacy 01.04 (Hidden files and dotfiles) says a change to a rules file or an MCP config deserves the same review as code; this lesson extends it: in a third-party repository those files are code that can run when the folder opens (S061).
