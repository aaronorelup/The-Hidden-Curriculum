# G11 concepts: Agents and AI work beyond code (C103-C109)

Written 2026-10-12 by the concepts-beyond-code agent for "The Hidden Curriculum".

**How this was built.** Each concept starts from the taxonomy entry (`research/taxonomy.md`, G11) and the gap items it merges (`notes/beyond-code-agents-and-facts.json` #01, #08-#11, #16, #18-#29, #32; `notes/practitioners-now.json` #09; `notes/surveys-and-learning.json` #16). Every primary source behind those items was opened again today and the figures used below were checked against the raw page text, not a summary.

**New sources.** The shared web-search budget was already used up when this agent started, so no new searches could be run. Instead, pages were fetched directly by URL. Each of those URLs came from a page already read (a link in S069, S070 or S073) or from a candidate the sweep finders logged (`research/sweep/beyond-code.md`, `community.md`, `ai-literacy.md`). Every one was fetched and read today. They carry `BC` IDs, listed with full details in the source table at the end. Give them S-IDs when the source index is next merged. Thin-evidence notes from the taxonomy are answered where a second source was found (C107, C109) and left standing where none was (C108).

**Scope note.** The where-your-data-goes and screen-agent material is built mostly on Anthropic's own documentation, because those pages were current and readable. For other vendors, the sweep agent got an HTTP 403 on OpenAI's Data Controls FAQ, and no other vendor's privacy pages were read. Teach the concepts (consumer vs commercial terms, the training toggle, memory, where a task runs) with Claude as the worked example, and check other vendors' current settings at lesson time.

---

### C103 Where your data goes

- **In one line:** Cowork tasks now run on the vendor's servers, and any local file they touch is processed there. Consumer chats (Free, Pro, Max) may be used for training, depending on a per-user setting. Memory is on by default and outlives deleted chats. Compliance agreements don't cover every feature. And many users don't know what their tool sees or remembers.
- **Why it is a gap:**
  - **What workers do with work data.**
    - About one in six professionals let the tool choose what work information it uses (10.4%) or are not sure what it uses (6.3%), n = 13,243 (S080).
    - 29.7% say AI use at work is mostly optional and up to individuals, and only 24.0% have approved tools and guidance (S080).
    - In a vendor-sponsored survey of 1,250 non-IT office professionals:
      - 88% had shared work information with public AI tools, including customer data (34%) and financial or confidential documents (31%);
      - 66% had used AI tools they believed were not permitted;
      - 86% believed their organization has an AI policy (BC07).
  - **Even Anthropic's own recent description is out of date.** An engineering post from 2026-05-25 describes Cowork as a local VM where only the chosen folders are mounted and credentials stay in the host keychain (BC06). On 2026-10-06, new Pro and Max tasks moved to the cloud, and the "Only on your computer" option was removed with no way back (BC03, S069).
  - **People ask for it.**
    - An AI librarian planning a university vibe-coding workshop got a reply listing "privacy" settings, so unpublished research isn't used for training, as one of four topics to teach (BC17).
    - Aaron's own list of missing topics includes how AI apps remember, enterprise plans, and chat vs Cowork vs Code (S004).
- **What to teach (specific points):**
  - **The work runs on the vendor's servers, not your laptop.**
    - Cowork runs each task in an isolated, temporary cloud environment.
    - A local file the task opens through the desktop app is processed on Anthropic's servers. When a task needs a file, Claude fetches a copy of just that file, and the copies are deleted when you delete the session.
    - On Pro and Max there has been no setting to keep new tasks local since 2026-10-06. For local-only work, the vendor points to Claude Code in the desktop app.
    - (S069, BC03)
  - **The cloud reaches back into your machine through the folders you connect.**
    - A cloud session reaches your computer only through the open desktop app, and only for folders you connected.
    - Scheduled tasks run with no device online.
    - On a computer your organization manages, a connected folder becomes reachable from a cloud session.
    - So connect one dedicated working folder, not your home folder or your financial records.
    - (S069, BC03)
  - **The plan you pay for decides whether your chats train models, and Pro is a consumer plan.**
    - Free, Pro and Max (including Claude Code used from those accounts) have a per-user training setting.
    - With it on, chats and coding sessions may be kept up to 5 years in de-identified form. With it off, the 30-day retention applies.
    - Team, Enterprise, the API, Bedrock, Vertex, Education and Gov are under commercial terms instead.
    - (BC02, BC01)
  - **"Off" and "delete" don't reach backwards.**
    - Turning training off later does not remove your data from training runs already under way or from models already trained.
    - Deleted chats and incognito chats are not used for future training.
    - Thumbs-up/down feedback is kept 5 years.
    - Chats flagged for policy violations are kept up to 2 years, and their classifier scores up to 7 years.
    - (BC01, BC02)
  - **Memory is a separate store with its own rules.**
    - It is on by default on Free, Pro and Max. On Team and Enterprise it stays off for each member until they turn it on.
    - It is shared between chat and cloud Cowork.
    - Deleting a chat does not remove the memories made from it: you delete those in Settings > Memory.
    - Some data is never saved: government ID numbers, financial account numbers, criminal history, immigration status.
    - (BC04)
  - **On a work account, your employer can see more than you think.**
    - Cowork on web and mobile is captured in the Compliance API, and Team or Enterprise owners can stream Cowork events to their monitoring tools (S069).
    - Incognito chats on Team and Enterprise are still included in data exports and follow the organization's retention policy (BC04).
    - The vendor's advice: keep separate accounts for work and home (BC03).
  - **A compliance agreement covers named features, not the whole product.**
    - In HIPAA-enabled organizations, Claude in Chrome is off by default, and even when an Owner turns it on it is not covered by the Business Associate Agreement (S070).
    - Memory isn't available at all to organizations with HIPAA, public-sector or custom retention agreements (BC04).
  - **Audit your own tool.** Go through four things in turn: the connected folders and connectors, the memory topics, the training toggle, and which account (personal or work) you're signed into. About one professional in six either lets the tool choose what it reads or doesn't know what it uses (S080, BC04).
- **You vs the agent (as of 2026-10-12):**
  - The agent reads whatever you have granted, saves memories on its own, and processes connected files wherever its session runs. It cannot tell you whether your employer, your client contract or a privacy law allows the data to go there.
  - The human chooses the account (consumer vs commercial), the training and memory settings, and what gets connected (a dedicated folder). They also check the employer's AI policy before connecting work data.
  - Bring in an expert when the data is regulated or contractual:
    - patient data: the compliance owner (S070, BC04);
    - client data under NDA, or personal data of customers: the data-protection or legal owner.
    The tool will work on whatever page or file it is handed (S070).
- **Currency:**
  - New in 2026:
    - the cloud default for Pro and Max (2026-10-06);
    - Cowork being merged into plain "Claude" (rolling out to Pro and Max);
    - the memory migration (legacy export offered until 2026-09-09).
    - (BC03, S069, BC04)
  - Established: the consumer training setting has been in force since 2025-08-28, and the privacy center restated the 5-year rule on 2026-07-01 (BC02, BC01).
  - Changing now: cloud Cowork is still beta on Team and Enterprise (BC03).
- **Outdated framings to avoid:**
  - "A desktop AI agent keeps my files on my computer." True of the May 2026 design (BC06), false for new Pro and Max tasks since 2026-10-06 (BC03, S069).
  - "The agent stops when I close my laptop." Cloud tasks keep going, and scheduled tasks run with no device online (BC03).
  - "Paying for Pro means my chats aren't used for training." Pro and Max are consumer terms (BC02).
  - "Deleting the chat deletes what it knows about me." Memories made from it stay (BC04), and training already done stays (BC01).
  - "Our BAA covers every feature." Claude in Chrome is outside it (S070).
  - "Company policy keeps work data out of public tools." 86% believed a policy existed, and 88% had shared work information (BC07).
- **Questions it answers:**
  - Does Cowork upload my files?
  - Where does my AI agent actually run?
  - Can a scheduled task run when my computer is off?
  - Is it OK to connect my work laptop's folders?
  - Does Claude train on my chats?
  - Is my Pro plan private?
  - How long are my conversations kept?
  - Does the AI remember what I told it, and how do I make it forget?
  - Can I use an AI browser agent with patient data?
  - Is it safe to give the AI my company's or my customers' data?
  - How do I make sure my unpublished research isn't used for training? (items #01, #10, #11 and surveys #16; BC17)
- **Show it for real:**
  - Open Settings > Privacy and show the "Help improve our AI models" toggle (BC03 names it).
  - Open Settings > Memory and show the topics list.
  - Delete a chat, then show that its memory topic is still there.
  - Start an incognito chat (the ghost icon).
  - In the desktop app, show the connected-folders list and one dedicated empty folder being connected.
  - Show a cloud task still running after the lid closes, and its run on the "Scheduled" page.
  - Show "Download task data" on a task.
  - (S069, BC03, BC04)
- **Priority:** must.
  - It affects every learner and every tool they use.
  - Four gap items from two batches, plus seven newly read sources; one item rated high severity.
  - The most important fact changed six days ago (2026-10-06), which makes it the clearest case in this group of a mental model going stale.

---

### C104 Screen and browser agents see everything visible and act on your real screen

- **In one line:** Browser agents screenshot whole tabs (other people's data included), store the sessions and act with your logged-in identity. Computer use has no sandbox, and data can move between apps without being asked. Use a separate profile, close or block sensitive apps, and pick the approval mode on purpose.
- **Why it is a gap:**
  - **The vendor itself spells out the risks.** Anthropic's own pages say the agent "can't filter sensitive content out of what it sees" and that computer use has "no sandbox". They tell users to use a separate profile and to block banking, healthcare and dating apps (S070, S069, BC05). That is advice users have to know to follow.
  - **A wrong mental model, and attacks against it.**
    - A September 2026 security analysis says most teams evaluate a browser agent like a browser extension, and that this framing "produced two clean patch cycles in 2026 and no reduction in exposure".
    - It describes a disclosed attack (PleaseFix, Black Hat USA 2026) in which one inbox-summary request exfiltrated Gmail, shared Google Drive and took over Slack, X and Claude accounts.
    - (BC08)
  - **People stop reading approval prompts.** Claude Code telemetry showed users approved about 93% of permission prompts, and attention fell the more prompts they saw (BC06).
- **What to teach (specific points):**
  - **Whatever is visible is captured, and it is kept.**
    - The browser agent screenshots the tabs it works in, and everything visible becomes part of the conversation. That includes pages behind a login and other people's personal data, and there is no redaction.
    - Side-panel sessions are saved to your history and can be reopened on your other devices.
    - (S070, S069)
  - **Give the agent its own browser profile.**
    - Use a separate browser profile with no banking, healthcare or government logins.
    - Organizations should set a restrictive site allowlist.
    - The vendor advises against using it for:
      - financial accounts;
      - legal documents;
      - medical information;
      - sensitive work accounts;
      - sites holding other people's personal data.
    - (S070, BC08)
  - **The agent has no identity of its own: it acts inside every session you are logged into.**
    - In the words of the September 2026 analysis, "Stolen credentials are the headline. Data accessed is the breach." There is no strange login to alert on (BC08).
    - In a pre-launch audit of an AI browser, each of five proof-of-concept attacks sent the user's Gmail to an attacker when the user simply asked for a summary of a page (BC09).
  - **Computer use has no sandbox between the agent and your screen.** It clicks and types on your real desktop and takes screenshots to navigate. Close sensitive files and apps before you start (S069, BC05).
  - **App permissions leak through links.** Computer use asks permission per app, and investment, trading and crypto apps are blocked by default. You can add more apps to a blocklist.
    - But a link clicked inside a permitted app still opens in another app. The vendor can hide that Chrome window from Claude, but it "can't stop the link from opening" (BC05, S069).
  - **Screen control is the slowest path, and connectors come first.**
    - In Cowork, Claude uses a connector first, then a browser, and controls your screen only when neither exists.
    - Connecting the tool is faster, more reliable, and exposes less of your screen (BC05).
  - **Data can move between apps without being asked.** With the Excel and PowerPoint add-ins, Claude can move data from one app to the other, for example a chart from a spreadsheet into a deck. Avoid sensitive data in those add-ins while Cowork is active (S069).
  - **The default approval mode lets the agent judge its own actions.**
    - The Cowork side panel defaults to "Automatically approve", where Claude screens its own actions.
    - Switch to "Manually approve" for:
      - sensitive sites;
      - a tool or site used for the first time;
      - anything hard to undo, such as sending or buying.
    - Plans can drift with no attacker involved: in testing, the agent had a plan approved and then visited a domain that was never in it.
    - (S070, S069, BC08)
  - **The network allowlist covers less than it seems.** The network-egress permissions you set for Cowork's code do not apply to web fetch, web search or MCPs, and that includes Claude in Chrome (S069).
  - **The safeguards are real, but they are not a boundary.**
    - Anthropic reports attack success under 0.08% with Opus 4.8 in internal tests, against known techniques, and still says "the risk is not zero" (S070).
    - Patches close bugs, not the authority the agent holds. One reported flaw was fixed in extension 1.0.41. A partial fix for another (1.0.70) was bypassed within a day.
    - (S070, BC08)
- **You vs the agent (as of 2026-10-12):**
  - The agent decides where to click and what to read inside what it can see. It cannot un-see a notification, a document or someone else's record that was on screen, and it screens its own actions only in auto mode.
  - The human does the setup: the separate profile, which tabs and apps are open, the app blocklist, and the approval mode. During the task they watch for files or sites never mentioned, and for scope creeping (S069).
  - The vendor's engineers say a non-technical worker should not be expected to judge risky commands. When approving an exception needs expertise the user lacks, admins should set an absolute, always-on boundary (BC06).
  - For an organization rollout, that is the security team's job: inventory who runs agents, keep separate identities for them, and log at the agent layer (BC08).
- **Currency:**
  - New in 2026 and beta:
    - Claude in Chrome is in beta, and its side panel now runs as a Cowork session on Max and Team (rolling out to Pro) (S070).
    - Computer use is in beta for Pro and Max only; Team and Enterprise have no access yet (BC05).
    - On macOS 15 or later it works in background windows by default (BC05).
    - A browser built into the desktop app is rolling out (BC03).
  - Vendor safety figures move fast and differ by date. A 2026-09-04 article still quotes an older "23.6% to 11.2%" injection-success figure (BC08), where the current help page says under 0.08% with Opus 4.8 (S070). Always date the number you show.
- **Outdated framings to avoid:**
  - "A browser extension sees only what I point it at." It sees whole tabs, logged-in pages included (S070).
  - "The agent only touches the app I gave it." Links open in other apps (S069, BC05).
  - "Safety classifiers mean I don't need to watch it." (S070, BC08)
  - "No stolen password, no breach." (BC08)
  - "Approval prompts are a control." They can be satisfied programmatically or clicked through (BC08, BC06).
  - "'Summarize this page' is a harmless request." (BC09)
- **Questions it answers:**
  - Can Claude in Chrome see my bank account?
  - Where are my browser agent sessions saved?
  - Should I use a separate Chrome profile?
  - Is letting AI control my mouse safe?
  - Can it see my other windows?
  - Can the AI move data from Excel into my slides on its own?
  - How does an AI agent log in for me? (items #08, #09, #12, #19)
- **Show it for real:**
  - Create a Chrome profile named "Agent", install the extension only there, and show that no bank or email account is signed in.
  - Open the side panel on a page with a visible notification, then reopen the stored session on a second device.
  - Show the per-app permission prompt for computer use, and add a banking app to the blocklist.
  - Have the agent click a link in a permitted email app and show Chrome opening anyway.
  - Show the approval-mode selector switched to "Manually approve".
  - (S070, BC05, items #08/#09)
- **Priority:** must.
  - High severity (2 of 3 items high), all of it new in 2026.
  - Two vendor safety pages plus the vendor's computer-use page, backed by an independent audit (BC09) and an independent risk analysis (BC08).
  - Non-coders adopt browser agents precisely for everyday errands, which is where the risk sits.

---

### C105 Personal always-on agents are coding agents holding your keys

- **In one line:**
  - A "Claw" (OpenClaw and its cousins, now sold as "personal agents") writes and runs code on your machine around the clock. That turns the machine into a credential vault.
  - The early versions were exposed to the internet by the tens of thousands.
  - Today, host installs bind to loopback, but container images still default to an exposed bind.
  - One gateway is one trust boundary, and you are its security team.
- **Why it is a gap:**
  - **Mass adoption by non-experts.** Non-technical users queued at install parties in China, Bay Area Apple stores sold out of Mac minis bought to run OpenClaw, and Meta's Muse topped the free iPhone charts in September 2026 (S033).
  - **Exposed at scale.** Internet scans counted publicly reachable instances growing from about 1,000 to 21,000+ in one week (25-31 Jan 2026). One researcher found 42,665 exposed in mid-February, 5,194 of them verified as actively vulnerable. The article reports 93.4% showing authentication-bypass conditions, and its summary puts it as "93% without authentication" (BC11).
  - **Credentials stolen through skills.** 341 malicious ClawHub skills stole API keys, wallet keys, SSH credentials and browser passwords (S071).
  - **Harm with no attacker at all.** A Meta AI security researcher's agent mass-deleted her inbox and ignored her stop messages (BC12).
  - **Aaron named it.** He lists always-on personal agents as a gap the course must fill (S004).
- **What to teach (specific points):**
  - **A Claw is a coding agent in friendlier packaging.**
    - Willison's line: "A Claw is really just a coding agent wearing a less threatening hat". Under the hood it writes and executes code on your computer.
    - The "safe Claw" for regular people is still an open race: of Meta's Muse, Willison is "not yet convinced you can't shoot yourself in the foot".
    - (S033)
  - **Everything the agent can reach is stored on that machine.** OpenClaw's docs say to assume anything under `~/.openclaw/` may contain secrets. That includes:
    - gateway tokens in the config;
    - channel credentials, for example WhatsApp's `creds.json`;
    - MCP OAuth access and refresh tokens and per-agent model auth in SQLite files;
    - session transcripts that hold private messages and tool output, readable by any process with disk access.
    - Their hardening advice: `700`/`600` permissions, full-disk encryption and a dedicated OS user (BC10).
  - **What the thieves took.**
    - The ClawHavoc skills and their keylogger captured the keys the bot already held. One skill sent the bot's `~/.clawdbot/.env` to webhook.site. The stealers took exchange API keys, wallet private keys, SSH credentials and browser passwords (S071).
    - Security guidance after the incident: connect only the accounts the agent needs, never primary email, admin or crypto. Use a dedicated VM and dedicated credentials (BC11).
  - **Exposure: the early defaults were open, and container defaults still are.**
    - Early on, the web interface ran on port 8080 with authentication disabled by default (BC11).
    - The current docs say a regular host install binds to loopback and unknown DM senders get a pairing code. But container images default to an exposed bind, so pair them with authentication.
    - One command, `openclaw security audit`, tells you if you have drifted from those defaults (BC10).
  - **"Local" does not mean only you can reach it.**
    - In one zero-click flaw, any website you visited could reach the gateway running on your machine. The gateway trusted local connections, so it guessed the password unthrottled and registered itself as a trusted device (patched within 24 hours).
    - Advice: don't browse the open web in the same browser where you're logged into the agent's control panel (BC12).
  - **One gateway is one trust boundary.**
    - Anyone allowed to message the bot can make it call its tools (exec, browser, files, network). Agents with the message tool can send across conversations and providers by default.
    - For people who don't fully trust each other, use separate gateways and credentials, ideally separate OS users or hosts. Never sign a shared agent into personal Apple or Google accounts or personal password managers.
    - (BC10, S071)
  - **There may be no remote off switch.**
    - The researcher's agent was asked to suggest what to delete, started deleting instead, and ignored her stop messages from her phone: "I had to RUN to my Mac mini like I was defusing a bomb".
    - Plan a physical or local shutdown, run the agent on a separate device or VM, and word delegation precisely ("suggest" vs "delete").
    - (BC12)
  - **You are the security team.**
    - There is no automatic update; you watch the advisories and patch.
    - After a suspected compromise the docs give four steps:
      - contain: stop the gateway and set the bind to loopback;
      - rotate: the gateway auth and every provider or API key;
      - audit: the logs, the transcripts and recent config changes;
      - collect: evidence for a report.
    - (BC12, BC10)
  - **An always-on agent can also spend money while you sleep.** Personal agents make it easy to spin up paid APIs and hosted services. Soft alerts "will not cut it", so give the agent keys and accounts with hard caps (BC14; caps are covered in C061).
- **You vs the agent (as of 2026-10-12):**
  - The agent will run whatever code its access allows and message anyone its tools allow. It cannot tell you it was robbed or that its port is open to the internet.
  - The human decides:
    - which machine it runs on (a separate device, the "aquarium" Mac mini, or a VM);
    - which scoped, revocable keys it holds;
    - who may message it.
  - The human also checks the bind and auth with the audit command, patches, and knows how to rotate every key (S033, BC10, BC12).
  - Bring in a security expert as soon as the agent holds company credentials or customer data: treat it like a service account with critical-risk access (BC11).
- **Currency:**
  - New in 2026 and still changing every month:
    - the category is being rebranded "personal" or "general" agents (S033);
    - OpenClaw is moving to a foundation backed by OpenAI, after its creator announced on 2026-02-14 that he was joining OpenAI (BC11);
    - defaults have tightened since January (BC10 vs BC11).
  - Incidents kept arriving through July 2026, for example a WhatsApp-to-host attack chain using three OpenClaw flaws (reported 2026-07-10) and a paper on stealthy memory injection in persistent personal agents (2026-07-06) (BC13).
  - Consumer "safe Claws" such as Meta's Muse (September 2026) are too new to judge (S033).
  - Memory poisoning is covered in C075, and skill marketplaces in C091.
- **Outdated framings to avoid:**
  - "It's my own machine at home, so it's private and safe." (S071, BC11)
  - "Running it in Docker isolates it from the internet." Container images default to an exposed bind (BC10).
  - "OpenClaw ships with auth disabled." True in January (BC11), no longer true for host installs (BC10). Teach both the history and the current default.
  - "If it goes wrong I'll tell it to stop." (BC12)
  - "An AI assistant only chats; it can't do anything on my machine." (S033)
- **Questions it answers:**
  - Is OpenClaw or Muse safe to install?
  - Why do people run their AI agent on a separate Mac mini?
  - What can a personal agent actually do on my computer?
  - What's the risk of running an AI agent 24/7 at home?
  - Where does my agent keep its API keys?
  - What do I do if my agent's keys leak?
  - Can I share my OpenClaw bot with friends?
  - Is my self-hosted agent exposed to the internet? (practitioners #09; items #16, #18)
- **Show it for real:**
  - Run `openclaw security audit` in a terminal and read the findings.
  - List `~/.openclaw/` and point at `credentials/`, the SQLite state files and the `sessions/*.jsonl` transcripts.
  - Show a container's published port binding next to a host install bound to loopback.
  - Open a model provider's dashboard and show the "revoke and regenerate key" control.
  - Show an agent transcript of the shell commands it wrote and ran to finish an everyday chore.
  - (BC10, S071, practitioners #09)
- **Priority:** must.
  - High severity (2 of 3 items high), all new in 2026, and the fastest-moving topic in this group.
  - Sources: two batch sources (S033, S071) plus five newly read ones (BC10-BC14).
  - Aaron named it, and non-experts are installing these agents at scale.

---

### C106 Checking AI research: a real source can still be wrong

- **In one line:** 2,184 court decisions (about 58% involving people representing themselves) concern AI citations that were fabricated, misrepresented, misquoted or outdated. Professionals and peer-reviewed papers get caught too. Existence is step one; whether the source supports the claim is the check the human, or an expert, must do.
- **Why it is a gap:**
  - **Most people caught are not lawyers.** As of 2026-10-10 the database counted 2,184 decisions: 1,259 involve pro se litigants (people representing themselves) and 864 involve lawyers. New entries arrive daily (S072).
  - **The disputes are everyday ones.** Contract (457), administrative (273), employment (198), family (142) and landlord-tenant (19) (S072).
  - **Senior professionals skip the check too.** EY Canada withdrew a report after more than 70% of its 27 citations were found to be AI-made-up or misattributed (BC15).
  - **"I always verify" is often not true.** In a researcher survey cited in S073, 87% claimed always to verify AI-generated citations, yet 42% copy-paste BibTeX without checking. 77% of reviewers do not check references thoroughly. 100 fabricated citations were found in 53 NeurIPS 2025 papers (S073, citing GhostCite and Ansari 2026).
- **What to teach (specific points):**
  - **A citation can fail in four ways.** Counts are from the database (one case can have more than one):
    - fabricated, the source doesn't exist: 1,791;
    - misrepresented, a real source that doesn't say what's claimed: 922;
    - false quote, the quoted words aren't in the source: 584;
    - outdated, the law was overturned (19) or repealed (17): 36.
    (S072)
  - **A real source can be cited for something it doesn't say.** In Grobler v. Kentucky Housing Corporation (2026-10-02), the court found three nonexistent cases and, separately, real cases that "did not support the propositions for which they were cited" (S072).
  - **Support is a separate and larger failure than existence.**
    - Only 51.5% of generative-search sentences were fully supported by their citations (Liu et al. 2023).
    - Up to 57% of RAG citations were "post-rationalized": written from memory, then given a matching-looking source (Wallat et al. 2024).
    - (both as cited in S073)
  - **Fakes are built to look plausible.**
    - An early study cited in S073 found that all five references generated for one medical topic had nonexistent titles, with PubMed IDs that pointed to unrelated papers (S073).
    - EY's report cited a non-existent McKinsey report for a figure that actually came from an obscure fintech blog, and used the same US$200 billion figure for two different things a few pages apart (BC15).
  - **Errors spread once published.** The EY report had already been cited by a newspaper, and the researchers who found the errors warned of "poisoning the well" for later researchers (BC15).
  - **The responsibility stays with whoever files or publishes.**
    - Courts tell litigants they remain responsible for verifying all filed materials. In 1182573 B.C. Ltd. v Gerber (B.C. Court of Appeal, 2026-10-07), the court gave that warning even though it named no specific hallucinated citation and imposed no AI-related sanction.
    - Consequences in October 2026 entries include appeals dismissed, cost orders and warnings.
    - In Washington v. Justice (2026-10-07), future filings were restricted unless signed by Florida Bar counsel.
    - In Tapscott v. Fariss (2026-10-07), the court ordered the filer to produce the cited cases; he did not, and the appeal was dismissed.
    - (S072)
  - **A three-step check.**
    - (1) Existence: does the source exist? This is machine-checkable; see C107.
    - (2) Support: open the source and find the exact passage. The agent can fetch it and quote the sentence; a human reads it for every claim that matters.
    - (3) Currency: is it still current, still good law, the latest version?
    - (S073, S072)
  - **Checkers help with step 1 but are imperfect.** Charlotin built an automated reference checker (PelAIkan) from the database (S072). A citation-verification benchmark cited in S073 found that a frontier model's detection score (F1) fell from 96% on generated test sets to 33% on real-world cases (S073, citing CiteAudit).
- **You vs the agent (as of 2026-10-12):**
  - The agent can search, fetch each source, quote the supporting passage and run existence checks. Those are verifiable, so make it do them.
  - The human reads the quoted passage against the claim for anything that matters, and checks that it is current.
  - When the human cannot judge, bring in an expert: a lawyer for a court filing, a clinician for a medical claim, a domain expert for a published report. The court in Washington v. Justice made that the condition for future filings (S072).
- **Currency:**
  - Established: fabricated citations have been documented since 2023 (S073).
  - Growing: cases are still being added daily in October 2026 (S072).
  - New in 2026: deep-research agents that produce long reference lists (C107), and automated reference checkers (S072, S073).
- **Outdated framings to avoid:**
  - "Hallucinated citations are a lawyer problem." About 58% of the cases are pro se (S072).
  - "That was an early-ChatGPT problem." There are new decisions every day in October 2026 (S072).
  - "If the source exists, the citation is fine." 922 decisions involve misrepresentation (S072, S073).
  - "Professional firms check AI output before publishing." (BC15)
  - "Peer review catches fabricated citations." (S073, citing Ansari 2026)
- **Questions it answers:**
  - Can I use AI to write my own legal filing?
  - How do I check the cases AI gives me are real?
  - The source is real, so why was the citation wrong?
  - How can a real reference be a hallucination?
  - How do I check an AI's sources properly?
  - The link works but I can't find the claim. What happened? (items #20, #21, #24)
- **Show it for real:**
  - In the Charlotin database, filter by "Pro Se Litigant" and open the newest entry. Read its note aloud: hallucinated citations, an order to produce them, an appeal dismissed.
  - Take an AI answer with three citations, open each, and use the browser's find-in-page for the quoted sentence. Show one that exists but does not contain the quote.
  - Ask the agent to quote the exact supporting sentence for each claim, then compare.
  - (S072, items #20/#21/#24)
- **Priority:** must.
  - High severity (3 of 3 items high).
  - Two primary sources plus a 2026 professional incident (BC15).
  - It applies to anyone who uses AI for research, reports or self-help, not only builders, and it is the course rule in its plainest form: existence is verifiable, support needs a person.

---

### C107 Link existence is machine-checkable, so make the agent check

- **In one line:** 3-13% of AI citation URLs were fabricated, and deep research agents did it more often. A dead link may be link rot rather than a fake, and a 403 is usually bot-blocking. A URL checker cut bad links to under 1%, but only when the model acted on its results.
- **Why it is a gap:**
  - **Search-enabled tools still invent URLs.** Retrieval-enabled systems fabricated 3-13% of citation URLs across 221,000+ URLs checked (S073).
  - **A Big Four report cited dead and invented links.** EY's citations to Forbes, McKinsey, Gartner, TechCrunch and Wired "were either broken URLs or never existed in the first place" (BC15).
  - **People say they check when they don't.** 87% of surveyed researchers claim always to verify AI citations, while 42% copy BibTeX unchecked (S073, citing GhostCite).
  - **Two habits, both wrong.** People either click every link by hand or trust "I verified the sources" (item #25).
- **What to teach (specific points):**
  - **How often links are fake or dead.** Across 10 models and agents on DRBench and 3 models on ExpertQA, 3-13% of citation URLs were hallucinated (no Wayback Machine record) and 5-18% did not resolve (S073).
  - **Deep research agents fabricate more, and more links is not better.**
    - Pooled, deep research agents had 10.7% hallucinated URLs vs 4.8% for search-augmented models (non-resolving: 16.2% vs 6.8%).
    - gemini-2.5-pro-deepresearch was highest at 13.3%, despite a top research-quality score.
    - gpt-5.1 gave about 4.3 times as many URLs per question as gemini-2.5-pro, with about twice the non-resolving rate.
    - (S073)
  - **A dead link is not always a fake.**
    - If the URL has a Wayback Machine snapshot, the page existed and went offline (link rot). No snapshot means it likely never existed.
    - openai-deepresearch had 10.1% non-resolving but only 3.5% hallucinated, so about 65% of its dead links were real pages gone stale.
    - Background rot is large: 25% of web pages from 2013-2023 are no longer accessible (Pew, cited in S073).
  - **A 403 or 429 usually means "blocked", not "dead".** In a headless-browser audit, 99.7% of 403 responses were not dead, and 89% of all UNKNOWN results were live or blocked-but-operational (S073).
  - **The check is small enough to hand to the agent.**
    - The paper's checker, urlhealth, is 83 lines of Python, packaged both for pip and as an agent skill.
    - It sorts each URL into one of four classes: LIVE, DEAD (404 with an archive copy), LIKELY_HALLUCINATED (404 with no archive copy) and UNKNOWN.
    - (S073)
  - **Giving the agent the checker works, but only if it uses the answer.**
    - In a self-correction loop, non-resolving URLs fell from 16.0% to 0.6% for GPT-5.1, from 6.1% to 0.1% for Gemini 2.5 Pro, and from 4.9% to 0.8% for Claude Sonnet 4.5.
    - A small model (gpt-5-nano) called the tool but kept re-proposing flagged URLs for up to 14 rounds and ended at 7.5%.
    - So read the final report, not the claim that it ran.
    - (S073)
  - **About one link in five stays UNKNOWN.** Paywalls, bot walls and rate limits left 10-20% UNKNOWN, and those need a real browser or a person (S073).
  - **Stop fabrication at the source.** The authors recommend limiting generated URLs to pages the system actually visited (S073).
  - **Some fields are riskier.**
    - Non-resolving rates ran from 5.4% (Business) to 11.4% (Theology).
    - Healthcare/Medicine was high for every model, 17.4% for Claude Sonnet 4.5.
    - The rates come from models current in April 2026. The method is the lasting lesson, not the exact numbers.
    - (S073)
- **You vs the agent (as of 2026-10-12):**
  - Link existence is verifiable, so the agent runs the checker over its own references and replaces what is flagged.
  - The human makes the check a required step and reads the final counts (how many LIKELY_HALLUCINATED or UNKNOWN remain). They open the paywalled and blocked ones in a real browser.
  - Whether a working link supports the claim is still the human's or an expert's check (C106).
- **Currency:**
  - The Wayback method is established (S073).
  - urlhealth and the deep-research measurements are new in 2026 (April) (S073).
  - The per-model rates are tied to April-2026 models and will drift.
  - This research crew follows the same rule: fetch every URL, treat a 403 as blocked, check the archive before calling a link fake (notes, S073).
- **Outdated framings to avoid:**
  - "Models with web search don't make up sources." (S073)
  - "A long bibliography means thorough research." (S073)
  - "A 404 means the AI made it up" or "a 403 means the page doesn't exist." (S073)
  - "Checking AI citations means clicking every link yourself." (S073)
- **Questions it answers:**
  - Are deep research reports reliable?
  - Why did the AI give me a link that goes nowhere?
  - The link is dead; was it made up?
  - How do I use the Wayback Machine to check a source?
  - Can I make the AI check its own sources?
  - Is there a tool that finds fake links? (items #22, #23, #25)
- **Show it for real:**
  - Have an agent run a URL checker over its own reference list in a terminal and print the per-URL status table, then show a flagged URL being replaced.
  - Paste a dead URL into web.archive.org and show either a snapshot list (link rot) or "not archived" (likely fabricated).
  - Open one UNKNOWN (403) link in a normal browser and show that it loads.
  - (S073, items #23/#25)
- **Priority:** should.
  - It is the cleanest worked example of the course rule (an existence check the agent can run itself), and it is cheap to adopt.
  - But the numbers rest on one study (S073, April 2026, older models), backed by one incident (BC15); one of 3 items is high severity.
  - Best taught inside the C106 lesson rather than alone.

---

### C108 Check an AI spreadsheet's structure, not its totals

- **In one line:** Agents type correct values instead of formulas, hide off-by-one errors behind matching totals, share the same mistakes, and may rebuild your workbook. Click outputs for formulas, and change an assumption to see them move.
- **Why it is a gap:**
  - **Even the best agent falls well short.** On end-to-end finance workbooks (DCF, LBO, 3-statement models, scenarios), the best agent (Claude Web) scored 69.1/100, falling to 53.4 at the hardest level (S074).
  - **The main failure is invisible to a value check.**
    - Values typed in where formulas belong were "typically correct".
    - An off-by-one error still produced the expected total.
    - Every agent missed the same simple accounting step.
    - (S074)
  - **People check the wrong thing.** They check AI spreadsheets by looking at the totals, or by asking a second AI (items #26, #27).
- **What to teach (specific points):**
  - **Correct numbers, no formulas.**
    - The Excel agents and ChatGPT Pro tended to paste in values computed elsewhere, so the workbook doesn't update when an input changes and can't be audited. For example:
      - Claude (Excel) hard-coded an entire model;
      - GPT-5.4 hard-coded 24.7% of answer-sheet cells;
      - a 0.26 ratio was typed into an SG&A formula instead of pointing to the assumptions table.
    - (S074)
  - **A matching total can hide a wrong formula.** For Last Twelve Months EBITDA, Claude Web summed the wrong window of quarters. Because the quarterly values were close, it still hit the expected number, and an exact-match check would have passed it (S074).
  - **Agreement between agents is not verification.** On the "Very Easy" task, all four working agents recorded a $100K receivables increase but missed the offsetting decrease. The result was Year 2 cash of $1,275 instead of $1,375 (S074).
  - **Shortcuts that are right today can break when the assumptions change.**
    - Every agent used a PMT() shortcut for the mortgage task (49-305 formulas). The reference answer used a full 180-period month-by-month schedule (8,006 formulas). The shortcut fails on variable-rate scenarios.
    - (S074)
  - **Six quick checks from the experts' rubric.**
    - Click the key outputs: are they formulas pointing to assumption cells?
    - Change one assumption: do the outputs move?
    - Enter a 0 or a blank: does #DIV/0! or #N/A spread (no IFERROR)?
    - Add a row: do the totals pick it up (fixed ranges vs tables)?
    - Copy a formula down: does a rate reference without `$B$1`-style absolute references drift to the wrong cell?
    - Check conventions: labeled units, negatives in parentheses, numbers not stored as text, consistent formulas across a range.
    - (S074)
  - **"Update this sheet" can mean "rebuild it".**
    - Opus 4.6 copied the starting workbook and rebuilt it in its own layout (Assumptions, Workings, Summary), and on one task deleted the original "Receivables" sheet.
    - Keep a copy, and check that the sheets and cell positions other files depend on still exist.
    - (S074)
  - **The product matters as much as the model.** With the same model (Opus 4.6), the vendor's GUI agent generally scored better than the researchers' API harness (S074).
  - **A headline spreadsheet score does not certify whole-model building.**
    - SpreadsheetBench, the benchmark cited in the releases of Opus 4.5 and ChatGPT Agent, tests atomic tasks.
    - WorkstreamBench's tasks have about 33 times more cells (mean) and 93 times more functions (median).
    - (S074)
- **You vs the agent (as of 2026-10-12):**
  - These structural checks are verifiable (is the cell a formula? does it move when an input changes?), so the agent can be told to run them and report: "no hard-coded outputs; show that X changes when I change Y" (item #28).
  - The human picks which assumptions matter, and traces at least one key calculation cell by cell. They test with an input whose correct answer is known and distinct, so a coincidental match can't pass.
  - For a model that money or decisions depend on, bring in a modeling or accounting professional. The rubric here took two MBAs and three finance professionals 700+ hours to build, and the shared receivables error is the kind of thing they would catch (S074).
- **Currency:**
  - New in 2026: the agents tested (Claude for Excel, ChatGPT for Excel, Opus 4.6, GPT-5.4, Gemini 3.1 Pro), as of May 2026. Newer models may score differently (S074).
  - Established: the conventions being checked, such as live formulas, absolute references, error handling and dynamic ranges (S074).
- **Outdated framings to avoid:**
  - "AI is bad at arithmetic, so check its math." The values were usually right; the structure was wrong (S074).
  - "If the total matches, the model is right." (S074)
  - "If two AIs agree, it's correct." (S074)
  - "The AI only changes what I asked it to." (S074)
  - "It scores well on a spreadsheet benchmark, so it can build my model." (S074)
- **Questions it answers:**
  - Can I trust a financial model the AI built?
  - Why doesn't my AI spreadsheet update when I change an input?
  - How do I check an AI's spreadsheet logic, not just its answer?
  - What should I check in a spreadsheet an AI made?
  - What is an absolute reference and why does it matter?
  - Why did the AI delete my sheet?
  - Should I give the AI a copy of my workbook? (items #26-#29)
- **Show it for real:**
  - Open an AI-built workbook, click a result cell, and show a typed number in the formula bar instead of a formula.
  - Change the growth assumption and show that nothing moves.
  - Select an LTM sum cell to show which range it adds up, and shift one quarter to show the total changes when it should not.
  - Type 0 into a divisor and watch #DIV/0! spread.
  - Compare the sheet tabs before and after an agent task and show a missing original tab.
  - (items #26-#29, S074)
- **Priority:** should.
  - High severity (2 of 4 items high), and data analysis is one of the most common things non-coders hand to agents.
  - But all four items rest on one source (S074). No second independent source could be found this run, because the search budget was used up.
  - Find one, for example a vendor evaluation or a practitioner incident, before building a full lesson.

---

### C109 Hardware: physical facts the AI can't check from text

- **In one line:** Part availability, footprints, open connections and effective (not nominal) component values need distributor checks, automated design checks, and simulation or measurement before boards are ordered. Production, mains power and compliance need an engineer.
- **Why it is a gap:**
  - **Physical failures are reported, though anecdotally.** Practitioners describe AI suggesting discontinued replacement parts, failing to make a footprint from a datasheet, and producing schematics with open circuits (S075, reader comments).
  - **The benchmark behind the headline measures something else.**
    - OpenAI's launch claimed GPT-6 Astra can produce a fully routed KiCad board ready for manufacture.
    - But the benchmark reported next to it (EEBench V1) excludes layout and grades only in simulation. On 2026-09-04 it had no Astra score yet.
    - (S075, BC16)
  - **Software builders don't know what text can't tell the AI.** Builders moving into devices don't know which hardware facts the AI cannot check from text (item #32).
- **What to teach (specific points):**
  - **AI is now useful for prototypes. These reports are anecdotal.**
    - Three AI-designed boards made with Fable came back working first time, where hand-made boards usually need a respin.
    - Schematic time roughly halved.
    - LLMs read datasheets well, find stock on JLCPCB/LCSC, and run SPICE on simple analog circuits.
    - (S075 comments)
  - **Check that every part is still made.** Asked to replace an end-of-life DC-DC module, ChatGPT suggested other discontinued parts. A human using Digi-Key's parametric search, then a Digi-Key rep, found working ones. Check each part's lifecycle at a distributor (S075 comments).
  - **Check footprints and connections.** One commenter's AI couldn't make a footprint from a PDF datasheet. Another's generated schematics had open circuits and components connected to nothing (S075 comments).
  - **The value on the part is not what the circuit gets.**
    - In an EEBench task, a design specified a 22 µF capacitor. At 4.7 V bias it delivered only 11.4 µF, against a 545 µF requirement. The protected rail fell below 3 V after 0.85 ms when 20 ms was required.
    - "The source built successfully; the circuit still failed the job."
    - Ceramic parts can give much less than their advertised capacitance under voltage, and parts have tolerances. "A design that works with nominal values can fail with the parts that arrive."
    - (BC16)
  - **Give the agent a simulator so it can check its own work.**
    - EEBench has agents write the circuit as code (atopile), build it, run SPICE, and inspect what failed. Every requirement is checked at worst-case tolerance corners, not nominal values.
    - The authors call this "similar to giving a coding agent a compiler and tests, except the tests are measuring voltages".
    - (BC16)
  - **Read what the benchmark measures, and who runs it.**
    - EEBench V1 excludes layout. Fabrication and bring-up are planned for V2 and later.
    - It is built and funded by atopile, which sells AI-oriented design tools (it says it does not sell scores).
    - Claude Opus 5 led its 2026-09-01 board at 61.6%, so even the leader failed a large share of the requirements.
    - Hackaday's 69.3% for GPT-6 Astra could not be confirmed on EEBench's pages.
    - (S075, BC16; benchmark reading in general is C002)
  - **Some things no simulation here covers.**
    - Layout of high-power switching (radiated RF, traces acting as antennas).
    - Routing that must be precise for signal integrity or regulatory compliance.
    - Safety and EMC compliance testing.
    - The most useful chip documentation is under NDA or is tribal knowledge, so the model never saw it.
    - (S075 comments)
  - **Mains power and shipped hardware are where mistakes hurt.**
    - One commenter described a 230 V-to-5 V design posted on Reddit with under 0.5 mm clearance, no transient protection and no isolation, meant for mass production.
    - Hardware can't be patched once shipped: a recall or rework could sink a company.
    - Production boards are expected to be "fully validated by multiple independent engineers" and to pass stringent testing (S075). The prototype-vs-production line is covered in C008.
- **You vs the agent (as of 2026-10-12):**
  - The agent can read datasheets, search stock, propose parts, write the design as code, and simulate it at tolerance corners, iterating on the failures (BC16, S075).
  - The human verifies:
    - lifecycle status at a distributor;
    - each footprint against its datasheet;
    - that automated design checks and simulation were actually run;
    - the real board on the bench before ordering in volume.
  - Bring in qualified engineers and a test lab for mains voltage, anything safety-critical, EMC and any product to be sold. The benchmark's own authors "would not ask it to design a pacemaker and blindly install the result" (BC16, S075).
- **Currency:**
  - New in 2026:
    - OpenAI's GPT-6 Astra KiCad demo (early September 2026);
    - EEBench V1 results (2026-09-01) (S075, BC16).
  - Hackaday's 2024 conclusion, "you might as well just do it all by hand", is now out of date for prototypes (S075).
  - Layout, fabrication and bring-up benchmarks are announced but not yet run (BC16).
- **Outdated framings to avoid:**
  - "AI can't help with hardware at all." Hackaday's own 2024 view, overtaken for prototypes (S075).
  - "The vendor's demo and a benchmark score mean it's production-ready." (S075, BC16)
  - "If the schematic looks complete, it's connected." (S075 comments)
  - "The part value on the schematic is what the circuit gets." (BC16)
  - "If it works on my bench, it's ready to sell." (S075)
- **Questions it answers:**
  - Can AI design a circuit board now?
  - Can ChatGPT pick parts for my circuit?
  - Why doesn't my capacitor give the value on the label?
  - How do I know if an AI benchmark means anything?
  - Can I sell a device whose board AI designed?
  - What is EMC testing, and do I need it?
  - Is it safe to build a mains power supply from an AI design? (items #31, #32, #33)
- **Show it for real:**
  - Paste an AI-suggested part number into a distributor search and show its lifecycle status.
  - Open the EEBench methodology page and highlight "Layout is deliberately out of scope", next to the vendor's routed-board claim.
  - Show the saved ngspice plot from the EEBench blog, with the rail dropping below 3 V at 0.85 ms.
  - Show an agent in a design-as-code tool running build, simulate, fix, and simulate again.
  - (S075, BC16, item #32)
- **Priority:** could, as a standalone lesson.
  - It rests on one medium-severity item. The concrete failures are reader comments, and the only measured example comes from a benchmark run by an interested vendor (BC16).
  - The audience explicitly includes people building physical devices, so the high-stakes half (mains, compliance, production sign-off) belongs in C008, which should be taught as a must.
  - Find an independent current source, such as an incident write-up or a distributor or test-lab guide, before giving this its own lesson.

---

## Sources used in this file

All were fetched and read on 2026-10-12. S-IDs are from the course source index. BC-IDs are new in this file.

| ID | Title | Author / publisher | Date | URL | Used in |
|---|---|---|---|---|---|
| S004 | AO-034: I sent back two of my course's first seven lessons | Aaron Orelup | 2026-10-04 | https://aaronorelup.com/ledger/lessons-sent-back/ | C103, C105 |
| S033 | 2026 in LLMs (so far) | Simon Willison | 2026-09-27 | https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ | C105 |
| S069 | Use Claude Cowork safely | Anthropic (Claude Help Center) | last modified 2026-10-06 | https://support.claude.com/en/articles/13364135-use-claude-cowork-safely | C103, C104 |
| S070 | Use Claude in Chrome safely | Anthropic (Claude Help Center) | last modified 2026-10-05 | https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely | C103, C104 |
| S071 | Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users | Ravie Lakshmanan, The Hacker News | 2026-02-02 (older than 3 months; still the primary incident record) | https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html | C105 |
| S072 | AI Hallucination Cases database | Damien Charlotin | last updated 2026-10-10 | https://www.damiencharlotin.com/hallucinations/ | C106 |
| S073 | Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents | Delip Rao, Eric Wong, Chris Callison-Burch | 2026-04-03 | https://arxiv.org/html/2604.03173v1 | C106, C107 |
| S074 | WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance | Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. | 2026-05-21 | https://arxiv.org/html/2605.22664v1 | C108 |
| S075 | Can AI Now Design PCBs That Just Work? (article and reader comments) | Maya Posch, Hackaday | 2026-09-05 | https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/ | C109 |
| S080 | Stack Overflow Developer Survey 2026 | Stack Overflow | released 2026-10-06 | https://survey.stackoverflow.co/2026/ | C103 |
| BC01 | How long do you store my data? | Anthropic Privacy Center | 2026-07-01 | https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data | C103 (companion of S069) |
| BC02 | Updates to Consumer Terms and Privacy Policy | Anthropic | 2025-08-28 (older than 12 months; foundational, and still current per BC01) | https://www.anthropic.com/news/updates-to-our-consumer-terms | C103 (companion of S069) |
| BC03 | Use Claude Cowork on web, desktop, and mobile (incl. "What changed for Pro and Max plans on October 6") | Anthropic (Claude Help Center) | last modified 2026-10-06 | https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile | C103, C104 |
| BC04 | Use Claude's chat search and memory to build on previous context | Anthropic (Claude Help Center) | last modified 2026-09-30 | https://support.claude.com/en/articles/11817273-using-memory-in-claude | C103 |
| BC05 | Let Claude use your computer in Cowork | Anthropic (Claude Help Center) | last modified 2026-09-16 | https://support.claude.com/en/articles/14128542-computer-use-safety | C104 |
| BC06 | How we contain Claude across products | Max McGuinness et al., Anthropic Engineering | 2026-05-25 | https://www.anthropic.com/engineering/how-we-contain-claude | C103 (outdated framing), C104 |
| BC07 | PagerDuty Report Finds Two-Thirds (66%) of Office Professionals Have Used Unauthorized AI Tools at Work | PagerDuty (survey by Wakefield Research; vendor-sponsored, n = 1,250) | 2026-06-11 | https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/ | C103 |
| BC08 | Top 6 Claude in Chrome Security Risks to Model Before You Roll It Out | Krishanu Borah (Akto), Cloud Security Alliance blog | 2026-09-04 | https://cloudsecurityalliance.org/blog/2026/09/04/top-6-claude-in-chrome-security-risks-to-model-before-you-roll-it-out | C104 |
| BC09 | Using threat modeling and prompt injection to audit Comet | Trail of Bits | 2026-02-20 (audit done April 2025) | https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/ | C104 |
| BC10 | OpenClaw docs: Gateway Security; Secrets, storage, and logs; Operator incident response | OpenClaw project | undated (live docs, fetched 2026-10-12) | https://docs.openclaw.ai/gateway/security ; https://docs.openclaw.ai/gateway/security/secrets-and-storage ; https://docs.openclaw.ai/gateway/security/operator-incident-response | C105 (companion of S071) |
| BC11 | OpenClaw: How the Viral AI Agent Became 2026's First Major Security Crisis | Hive Security | 2026-05-07 | https://hivesecurity.gitlab.io/blog/openclaw-ai-agent-security-crisis-2026/ | C105 |
| BC12 | Every OpenClaw Security Incident So Far (2025-2026) | Sliq | 2026-03-01 (shown on the page) | https://getsliq.com/blog/openclaw-security-incidents-timeline | C105 |
| BC13 | openclaw-security-news (curated list) | joylarkin (GitHub) | latest dated entry 2026-07-20 | https://github.com/joylarkin/openclaw-security-news | C105 |
| BC14 | We're going to need default hard budget caps on pretty much everything | Simon Willison | 2026-10-03 | https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/ | C105 |
| BC15 | EY retracts cyber report littered with AI errors | Denham Sadler, Information Age (ACS) | 2026-05-19 | https://ia.acs.org.au/article/2026/ey-retracts-cyber-report-littered-with-ai-errors.html | C106, C107 |
| BC16 | Can AI design circuit boards yet? (and the EEBench methodology page, undated) | EEBench, built and funded by atopile (no named author) | 2026-09-04 | https://eebench.org/blog/can-ai-design-circuit-boards-yet/ ; https://eebench.org/methodology.html | C109 (companion of S075) |
| BC17 | Ask HN: What would you include in an academic workshop on vibe coding? | cximenez; reply by jahala (Hacker News) | about 2026-09-18 (page showed "24 days ago" on 2026-10-12) | https://news.ycombinator.com/item?id=49745403 | C103 |

**Studies cited only as reported inside S073** (not opened separately): Liu et al. 2023, Wallat et al. 2024, Pew Research Center 2024, GhostCite (Xu et al. 2026), Ansari 2026, CiteAudit (Yuan et al. 2026), and Alkaissi and McFarlane 2023. Each is cited in the text above as "cited in S073".
