# Beyond code: desktop, browser and always-on agents; checking AI research, spreadsheets and hardware designs

Research notes for "The Hidden Curriculum". Researched 2026-10-12 by the read-beyond-code-agents-and-facts agent.
Every point below comes from a page that was fetched and read on 2026-10-12. Dates were checked against page metadata where the page itself showed none.

Method note: the web search budget for this run was already used up by other agents, so no new searching was done. Every source was opened directly by its URL (WebFetch, and curl for the raw page text). This matters for S073: every URL in these notes was fetched, so none of them is a made-up reference.

---

## S069 - Use Claude Cowork safely

- **Author / publisher:** Anthropic (Claude Help Center)
- **Date:** last modified 2026-10-06 (page metadata `dateModified` 2026-10-06T19:11:07Z; the page shows "Updated this week")
- **URL:** https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- **Also read:** Updates to Consumer Terms and Privacy Policy, Anthropic, 2025-08-28, https://www.anthropic.com/news/updates-to-our-consumer-terms. To check that it is still current I also read "How long do you store my data?", Anthropic Privacy Center, updated 2026-07-01, https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data

**Summary.** Cowork sessions now run in the cloud on Anthropic's servers. Each runs in an isolated, temporary environment that cannot reach your network and is removed when the session ends. The session reaches your computer only through the Claude Desktop app, only while the app is open, and only for folders you connected. Any local file it opens is processed on Anthropic's servers. On Pro and Max, new desktop tasks have run in the cloud since 2026-10-06. Tasks started locally before then keep running on the computer. The article organizes risk around what Claude can read (read tools) and what it can do (write tools). It says prompt injection succeeds when both are true at once. It warns that isolation limits where code runs, not what Claude reads or does. It also covers the approval modes, unattended scheduled tasks, computer use having no sandbox, plugins and MCPs, and data passing between apps, and it says the user stays responsible for every action.

**Gaps it shows**
1. **Where the agent's work and your files go.** Work runs on Anthropic's servers. Connected local folders are processed there. Scheduled tasks run while your computer is off. On a computer your organization manages, connecting a folder makes it reachable from a cloud session.
2. **Isolation is not permission.** The cloud sandbox protects your computer and network from the code Claude runs. It does nothing about what Claude can read through your connected apps and folders, or what it can do through them. Browsing, connected apps and connected folders are each a path for untrusted content to come in and for actions to go out.
3. **Read tools and write tools.** Read tools access content, such as your inbox or screenshots. Write tools act, such as creating a calendar invite, deleting a file, running a command or clicking. Write tools carry more risk, and the article recommends human oversight when the stakes are high.
4. **Prompt injection needs two conditions at once.** (a) Claude can read content from outside your trust boundary, and (b) Claude can take actions that could harm you. Remove either one and attacks get harder. The article's example: an email that says to ignore previous instructions and transfer $1000.
5. **Safeguards lower the risk but never remove it.** The safeguards are RL training, content classifiers on all untrusted input, action screening in "Automatically approve" mode, a confirmation before any permanent deletion, and a permission prompt for each app under computer use. The article still says the chance of an attack is non-zero. Warning signs that a task has been hijacked: Claude talks about unrelated topics, reaches for unexpected resources, or asks for sensitive information. If you see one, stop the task and report it.
6. **Approval modes.** There are three:
   - "Automatically approve": Claude screens each of its own actions.
   - "Skip all approvals": nothing checks the actions.
   - "Manually approve": you approve each action yourself.
   Switch to Manually approve for sensitive files, accounts or sites, for a tool, plugin or site you are using for the first time, and for actions that are hard to undo, such as sending messages or making purchases. In any mode, an injection read in the middle of a task can be acted on before you notice.
7. **Scheduled tasks run unattended.** Start with low-risk work such as summaries. Do not schedule tasks that touch sensitive files, send messages, make purchases or do anything hard to undo. Review the output of every run on the "Scheduled" page, and pause tasks you no longer use.
8. **Computer use has no sandbox.** Claude clicks and types on your real screen and takes screenshots of it. Block sensitive apps such as healthcare portals, banking and dating apps. A link Claude clicks in a permitted app will still open, even in an app you never permitted.
9. **Plugins and MCPs are code running with your permissions.** A plugin bundles skills, connectors and sub-agents, so one install can widen what Claude can do considerably. Local MCP servers run with the same permissions as any other program you run. Use verified extensions from the Claude Desktop directory. Enterprise plans can turn on skill scanning.
10. **Data passes between apps on its own.** With the Excel and PowerPoint add-ins, Claude may move data from one app into another without being told to.
11. **Monitor the task, not each command.** You are not expected to check every command. Watch instead for files or sites you never mentioned, and for a task growing beyond what you asked.
12. **Responsibility.** The user stays responsible for everything Claude does on their behalf: content published, messages sent, purchases, data accessed or changed, actions by scheduled tasks and computer use, and third-party terms of service.
13. **Training setting and retention on consumer plans (checked current).**
    - On Free, Pro and Max, including Claude Code used from those accounts, each user chooses whether chats are used for training.
    - With training on, chats are kept for up to 5 years in de-identified form in training pipelines. With it off, the 30-day retention applies.
    - Deleted chats are not used for training.
    - The choice covers new or resumed chats only.
    - Turning the setting off does not take your data out of training runs already under way or models already trained.
    - The policy does not apply to Team, Enterprise, the API, Bedrock, Vertex, Education or Gov, which are under commercial terms.
    - The privacy center page (updated 2026-07-01) still states the 5-year rule.

**Framings this source shows are outdated**
- "A desktop AI agent keeps your files on your computer." This is false for Cowork since 2026-10-06 on Pro and Max: files are processed on Anthropic's servers.
- "Running in a sandbox or VM makes the agent safe."
- "Cowork and Chat are separate modes." Cowork is being merged into plain "Claude", rolling out to Pro and Max.

**Quotes**
- "Isolation limits where Claude's code runs. It doesn't limit what Claude reads or does."
- "computer use has no sandbox between Claude and what's on your screen"

---

## S070 - Use Claude in Chrome safely

- **Author / publisher:** Anthropic (Claude Help Center)
- **Date:** last modified 2026-10-05 (page metadata `dateModified` 2026-10-05T15:42:32Z; the page shows "Updated this week")
- **URL:** https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely

**Summary.** Claude in Chrome is on all paid plans and is in beta in the Chrome browser. On Max and Team plans the side panel now runs as a Cowork session, and that is rolling out to Pro. Claude screenshots the tabs it works in, and anything visible in them becomes part of the conversation, because Claude cannot filter it out. The article recommends a separate browser profile with no banking, healthcare or government logins. It also warns that side-panel sessions are saved to your history and can be reopened on your other devices. The default mode is "Automatically approve". The article reports internal attack success under 0.08% with Opus 4.8, and still says the risk is not zero.

**Gaps it shows**
1. **Everything visible in the tab goes into the conversation.** That includes other people's personal data. There is no redaction. Do not open the side panel on a page showing something you do not want stored with the session.
2. **Sessions are stored and synced.** Side-panel sessions are saved to your history and can be reopened on your other devices.
3. **Use a separate browser profile.** Give Claude a profile with no banking, healthcare or government accounts signed in. Organizations can set an allowlist of sites.
4. **Approval modes in the browser.** "Automatically approve" is the default for the Cowork side panel: Claude screens its own actions and pauses only when it decides it needs you. "Manually approve" reviews every action. Confirm yourself before any sensitive or high-risk task.
5. **Prompt injection risk is never zero.**
   - Hidden text in a page, email or to-do list can tell Claude to, for example, retrieve bank statements and share them.
   - Two classifiers guard against this: one screens incoming content, the other screens each action.
   - With Opus 4.8, Anthropic reports attack success under 0.08% in its internal testing. That is a vendor figure for known techniques.
   - Novel attacks may get through and could exfiltrate data.
6. **Built-in limits.** Adult and pirated-content sites are blocked. Claude asks before opening financial sites. It is prohibited from stock trading, bypassing captchas, entering sensitive data and scraping faces. With 1Password for Claude, logins are filled without the password or one-time code entering Claude's context.
7. **Regulated data.** In HIPAA-enabled organizations Claude in Chrome is off by default. Even when turned on it is not covered by the Business Associate Agreement.
8. **What to avoid.** Financial accounts and investments, legal documents and contracts, medical information, work accounts with sensitive data, and sites holding other people's personal data.
9. **Responsibility.** You are responsible for purchases, financial transactions, posts, messages, data changes and site terms of service.

**Framings this source shows are outdated**
- "A browser extension sees only what you point it at." It sees the whole tab, including pages behind a login.
- "Safety classifiers mean you do not need to watch it."

**Quotes**
- "Claude can't filter sensitive content out of what it sees"
- "The risk is not zero."

---

## S071 - Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users

- **Author / publisher:** Ravie Lakshmanan, The Hacker News, reporting Koi Security (researcher Oren Yomtov) and OpenSourceMalware (Paul McCarty, "6mile")
- **Date:** 2026-02-02 (confirmed on the page). This is older than 3 months but within 12. It is foundational for the "skill marketplace as supply chain" lesson.
- **URL:** https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- **Also skimmed:** OpenClaw docs, Gateway security, https://docs.openclaw.ai/gateway/security. Undated: the page shows no date or version. Fetched 2026-10-12. It is now a hub page that links to detailed sub-pages.

**Summary.** Koi Security audited 2,857 skills on ClawHub, the skill marketplace for the self-hosted, always-on OpenClaw assistant. It found 341 malicious skills. Of those, 335 (the "ClawHavoc" campaign) used a fake "Prerequisites" step to install malware:
- On Windows, a password-protected "openclaw-agent.zip" holding a keylogging trojan.
- On macOS, an obfuscated script from glot.io, pasted into Terminal, that fetched Atomic Stealer.

The skills used typosquatted names and polished documentation, and stole API keys, bot credentials, exchange keys, wallet private keys, SSH credentials and browser passwords. The only bar to publishing was a GitHub account at least one week old. Palo Alto Networks also warned that persistent agent memory enables time-shifted prompt injection. The OpenClaw docs now describe:
- one trust boundary per gateway;
- container images that bind to an exposed address by default;
- agents with the message tool that can send across conversations and providers by default;
- an `openclaw security audit` command that checks for drift from the defaults.

**Gaps it shows**
1. **Skill marketplaces are mostly unvetted.** ClawHub is open by default. The response was a reporting feature: up to 20 active reports per user, and a skill with more than 3 unique reports is hidden automatically. A malicious skill stays up until several people have reported it.
2. **The "Prerequisites" step is the attack.** The skill code itself may look harmless. The malware comes from a setup instruction telling you to download a zip or paste a command into Terminal, and pasting a command from a README is running a stranger's code.
3. **Lookalike names and polished docs prove nothing.**
   - Typosquats of the marketplace itself: clawhub, clawhub1, clawhubb, clawhubcli, clawwhub, cllawhub.
   - Popular-sounding utilities: youtube-summarize, polymarket-trader, auto-updater-agent, yahoo-finance-pro, Google Workspace integrations, "lost Bitcoin finders".
   - Some skills worked as advertised but hid a reverse shell inside the functional code (better-polymarket, polymarket-all-in-one).
4. **An always-on agent machine is a credential vault.** The keylogger captured API keys and credentials, including those the bot already held. One skill (rankaj) sent the bot's credentials from `~/.clawdbot/.env` to webhook.site. The stealers took exchange API keys, wallet private keys, SSH credentials and browser passwords. The macOS targeting followed reports of people buying Mac Minis to run the assistant around the clock.
5. **The lethal trifecta.** Private data, untrusted content and the ability to communicate externally together make an agent vulnerable by design (Simon Willison's term, cited by Palo Alto Networks).
6. **Persistent memory turns prompt injection into delayed attacks.** Fragments that look harmless can be written into long-term memory and combine later. Palo Alto calls these "time-shifted prompt injection, memory poisoning, and logic bomb-style activation".
7. **Self-hosted gateway hygiene (OpenClaw docs).**
   - A gateway is one trust boundary: for people who do not trust each other, split gateways, credentials, and ideally OS users or hosts.
   - Container images default to an exposed bind, so always pair them with authentication.
   - Agents with the message tool can send across conversations and channel providers unless you restrict it.
   - Run `openclaw security audit` to catch drift from the defaults.
   - Incident response: contain, rotate (assume compromise if secrets leaked), audit, collect.

**Framings this source shows are outdated**
- "Skills are just prompts or markdown, so they are harmless."
- "A popular marketplace has vetted what it lists."
- "A self-hosted agent is private, so it is safe."

**Quotes**
- "The skill's documentation looks professional." (Oren Yomtov, Koi Security)
- "Skills with more than 3 unique reports are auto-hidden by default." (ClawHub docs, quoted by THN)

---

## S072 - AI Hallucination Cases database

- **Author / publisher:** Damien Charlotin
- **Date:** last updated 2026-10-10 (stated on the page). Licensed CC BY 4.0.
- **URL:** https://www.damiencharlotin.com/hallucinations/

**Summary.** The database tracks court and tribunal decisions that found, or implied, that a party relied on AI-hallucinated material. It stood at **2,184 cases** on 2026-10-10. Pro se litigants, meaning people representing themselves, account for **1,259 (about 58%)** and lawyers for 864. The rest are judges (32), experts (15), prosecutors (5), government lawyers (3), paralegals (2), an arbitrator and a federal defender. By type, a case can carry more than one:

| Type | Cases |
|---|---|
| Fabricated | 1,791 |
| Misrepresented | 922 |
| False quotes | 584 |
| Outdated advice | 36 (overturned case law 19, repealed law 17) |

The decisions come from 45 jurisdictions or forums. The largest are the USA (1,492), Canada (233), Australia (112), the UK (76) and Israel (57). Consequences in the latest entries include appeals dismissed, future pro se filings restricted, adverse costs orders, warnings and admonishments.

**Gaps it shows**
1. **Checking AI research is a problem for non-coders too.** Most of the people caught were not lawyers. They were ordinary people using AI for their own court filings. Their AI-written briefs cited cases that do not exist, and courts dismissed appeals over it. In one recent example (Tapscott v. Fariss, Iowa Court of Appeals, 2026-10-07), the court ordered the filer to produce the cited cases. He did not respond, and the appeal was dismissed.
2. **A citation can fail in four ways.**
   - Fabricated: the source does not exist.
   - Misrepresented: a real source that does not say what is claimed.
   - False quote: a quotation that is not in the source.
   - Outdated: law that was overturned or repealed.
   Grobler v. Kentucky Housing Corporation (Kentucky Court of Appeals, 2026-10-02) had three nonexistent cases, plus real cases that did not support the propositions they were cited for.
3. **Courts put verification on the filer.** In 1182573 B.C. Ltd. v Gerber (B.C. Court of Appeal, 2026-10-07), the court warned that litigants remain responsible for verifying all filed materials. Saying you used AI is not a defense.
4. **The way out is to bring in someone who can check.** One case ordered that future filings be signed by Florida Bar counsel (Washington v. Justice, 2026-10-07): for a high-stakes document you cannot verify yourself, you need an expert who can.
5. **Tools now exist to check references.** The author built an automated reference checker (PelAIkan) from this database. That makes "do these citations exist?" a check you can verify mechanically.

**Framings this source shows are outdated**
- "Hallucinated citations are a lawyer problem."
- "Hallucination is an old-model problem." Cases are still being added daily in October 2026.

**Quotes**
- "Fake cites, wrong cites, real consequences." (site tagline)

---

## S073 - Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

- **Authors:** Delip Rao, Eric Wong, Chris Callison-Burch (University of Pennsylvania)
- **Date:** 2026-04-03 (arXiv v1 stamp). Models tested include gpt-4.1, gpt-5.1, claude-3-5-sonnet, claude-sonnet-4-5, gemini-2.5-pro and the two deep-research agents. The rates for October 2026 models may differ. The method is still current.
- **URL:** https://arxiv.org/html/2604.03173v1

**Summary.** The authors checked 221,000+ citation URLs: 53,090 on DRBench from 10 models and agents, and 168,021 on ExpertQA from 3 models across 32 fields.
- **3-13%** of URLs were hallucinated: non-resolving, with no Wayback Machine record.
- **5-18%** did not resolve at all.
- **Deep research agents fabricated more (10.7%)** than search-augmented models (4.8%). Non-resolving rates were 16.2% vs 6.8%.
- More citations did not mean better ones.
- They release urlhealth, an 83-line checker. With it, models cut non-resolving URLs by 6-79x, to under 1%, but only when the model actually acted on the results.
- The paper checks only whether a source exists, not whether it supports the claim. The authors call support a separate question.

**Gaps it shows**
1. **Fabricated links are common, and deep research is worse.**
   - gemini-2.5-pro-deepresearch had the highest hallucination rate, 13.3%, despite a top DRBench quality score.
   - Four OpenAI search-augmented models had no stale URLs, so every one of their dead links was fabricated.
   - gpt-5.1 produced about 4.3 times as many URLs per question as gemini-2.5-pro, with about twice the non-resolving rate.
2. **A dead link is not the same as a fake link.** If the URL has a Wayback Machine snapshot, it existed once and went stale (link rot). If there is no snapshot, it likely never existed. openai-deepresearch had 10.1% non-resolving but only 3.5% hallucinated, so about 65% of its failures were link rot. A 403 error is usually bot-blocking, not a dead page: a headless-browser audit found 99.7% of them live. In the audit of UNKNOWN results, 89% were live or blocked-but-accessible.
3. **A live link does not mean the source supports the claim.** A citation can be nonexistent, real but unsupportive, or both. Earlier work cited in the paper puts the gap in numbers:
   - Liu et al. 2023: only 51.5% of generative-search sentences were fully supported by their citations.
   - Wallat et al. 2024: up to 57% of RAG citations were "post-rationalized", meaning the model wrote from memory and then attached a matching-looking source.
   Fabricated citations also pair real journal names with nonexistent titles, or give PubMed IDs that point to unrelated papers.
4. **Give the agent a checker, and make sure it uses the answer.**
   - With urlhealth, GPT-5.1 dropped from 16.0% to 0.6%, Gemini 2.5 Pro from 6.1% to 0.1%, and Claude Sonnet 4.5 from 4.9% to 0.8%.
   - gpt-5-nano called the tool but kept re-proposing flagged URLs for up to 14 rounds.
   - 10-20% of URLs stay UNKNOWN (paywalls, bot-blocking) and need a human or a real browser.
   - The authors recommend limiting generated URLs to pages the system actually visited.
5. **Some fields are riskier.** Non-resolving rates ran from 5.4% in Business to 11.4% in Theology. Healthcare and medicine was high for every model (17.4% for Claude). Within medicine, subfields ranged from 14.8% to 21.4%.
6. **Saying you verified is not verifying.** The paper cites surveys in which researchers claim they always verify citations, yet many copy BibTeX without checking.

**Framings this source shows are outdated**
- "Models with web search don't hallucinate sources." Retrieval-enabled systems still fabricated 3-13% of URLs.
- "A dead link means the AI made it up." It may be link rot.
- "A working link means the citation is good."

**Quotes**
- "Tool-based mitigation thus requires not just tool access but competent tool use."
- "does the source exist?" (the paper's framing of the question that comes before "does it support the claim?")

**Bearing on this crew's own method:** this research crew should fetch every URL it cites. It should treat a 403 as "blocked", not "fake". It should check archive.org before calling a dead link fabricated, and it should confirm that the page actually says what we attribute to it.

---

## S074 - WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance

- **Authors:** Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen, Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, Hongseok Namkoong (Columbia Business School; Poeltl at ESB Business School, Reutlingen University)
- **Date:** 2026-05-21 (arXiv v1 stamp). Agents tested include Claude Web, Claude (Excel), ChatGPT (Excel), ChatGPT Pro, Opus 4.6, GPT-5.4, Gemini 3.1 Pro, Grok, Kimi K2, Qwen3 and OLMo 3.
- **URL:** https://arxiv.org/html/2605.22664v1

**Summary.** Agents had to build complete multi-sheet Excel workbooks for finance tasks from the Financial Modeling World Cup, ModelOff and Wall Street Prep: DCF, LBO, 3-statement models and scenario analysis. Each workbook was graded on accuracy, formulas and format by an LLM judge. The judge reached 0.92 accuracy against 408 expert annotations, and experts spent more than 700 hours designing the rubric. **The best agent, Claude Web, scored 69.1/100**, falling to 53.4 at difficulty level 4. The main failures:
- Values typed in where formulas should be. The values were usually correct, but the sheet was unauditable.
- An off-by-one window error hidden by a total that still matched.
- A simple accounting step that every agent missed.
- Missing units and conventions, missing error handling, and shortcuts that break when assumptions change.

**Gaps it shows**
1. **The numbers are right but there are no formulas.**
   - The Excel agents and ChatGPT Pro tend to type in values computed elsewhere, so the workbook does not update when an input changes.
   - Claude (Excel) hard-coded an entire model.
   - GPT-5.4 hard-coded 24.7% of answer-sheet cells.
   - A ratio of 0.26 was typed into an SG&A formula instead of pointing to the assumptions table.
   - In a 1,000+ row trading simulation, Claude Web pasted externally computed results instead of formulas. The judge called it unauditable.
   Checking only the values would never catch any of this.
2. **A matching total can hide a wrong formula.** In a Last Twelve Months EBITDA calculation, Claude Web summed the wrong window of quarters. Because the quarterly values were close, the total still matched. The judge failed it as "coincidentally unaffected", and an exact-match check would have passed it.
3. **Every agent can make the same mistake.** On the "Very Easy" task, all four functioning agents recorded a $100K receivables increase but missed the offsetting decrease. That gave Year 2 cash of $1,275 instead of $1,375. Three agents agreeing does not make the answer right.
4. **A shortcut can break when assumptions change.**
   - Every agent used a PMT() shortcut for the mortgage task, and it fails on variable-rate scenarios.
   - A rate cell without $ (absolute) references breaks when the formula is copied down.
   - Fixed ranges miss new rows unless you use tables.
   - Without IFERROR, one erroneous "0" input breaks the whole workbook.
5. **Missing units and conventions.**
   - Labels are missing, where a unit column in square brackets is expected.
   - Negatives show with a minus sign instead of parentheses.
   - Numbers are stored as text.
   - Formulas are inconsistent across a range that should be uniform.
   - "Mega-formulas" no one can read.
6. **Agents may rebuild your workbook instead of editing it.** Opus 4.6 copied the workbook and rebuilt it in its own layout (Assumptions, Workings, Summary). It deleted the original "Receivables" sheet. Check that what you handed over still exists.
7. **The harness matters as much as the model.** The same model (Opus 4.6) generally scored better inside the vendor's GUI agent than in the researchers' API harness. "Which product" matters as much as "which model".

**Checks a human should run on an AI-built spreadsheet (from the rubric and appendices)**
- Click the key outputs: are they formulas that point to assumption cells?
- Change one assumption: do the outputs move?
- Enter a zero or a blank: does anything turn into #DIV/0! or #N/A?
- Add a row: do the totals pick it up?
- Copy a formula down: do the references hold?
- Are units labeled, signs shown as conventions require, and numbers stored as numbers?
- Can you follow the logic step by step?

**Framings this source shows are outdated**
- "AI is bad at arithmetic, so check the math." The arithmetic was usually right. The structure, auditability and edge cases were wrong.
- "If the total matches, the model is right."

**Quotes**
- "Even the strongest agent, Claude Web, attains only 69.1 out of 100 overall"
- "The hardcoded values themselves are typically correct"

---

## S075 - Can AI Now Design PCBs That Just Work?

- **Author / publisher:** Maya Posch, Hackaday
- **Date:** 2026-09-05 (confirmed on the page, 7:00 pm). The article had 64 comments when read.
- **URL:** https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/
- **Also read:**
  - EEBench blog, "Can AI design circuit boards yet?", EEBench by atopile, 2026-09-04, no named author: https://eebench.org/blog/can-ai-design-circuit-boards-yet/
  - EEBench methodology page, undated: https://eebench.org/methodology.html

**Summary.** OpenAI's GPT-6 Astra launch claimed the model could turn a schematic into a fully routed KiCad PCB ready for manufacturing. Hackaday asked whether that is "a nifty party trick" that only works under controlled conditions, like most autorouters. The article reports GPT-6 Astra at 69.3% (±10%) on EEBench, near Claude Opus 5 but cheaper and faster. It notes that EEBench is run by the developers of atopile, a code-first PCB tool built for AI agents. Its conclusion: vibe-coded prototypes are a useful shortcut, but production boards must handle edge cases, be validated by multiple independent engineers, and pass stringent testing. The concrete failures come from the reader comments, not the article body:
- discontinued parts suggested as replacements;
- no footprint from a PDF datasheet;
- schematics with open circuits;
- unsafe mains supplies;
- EMC compliance.

**Discrepancy found (flag for lesson writers).** EEBench V1 explicitly **does not test PCB layout**. The methodology page says layout is deferred, and fabrication and bring-up are planned for V2 and later. Scores are graded in simulation in atopile, not KiCad. The EEBench post dated 2026-09-04 says EEBench had **no GPT-6 Astra score yet**, and the leaderboard on the 2026-09-04 post lists Claude Opus 5 at 61.6%. So the 69.3% figure Hackaday reports could not be confirmed from EEBench pages read on 2026-10-12: the leaderboard page renders empty without JavaScript. Even if the figure is real, it measures circuit design in simulation, not the layout claim. That is itself the teachable point.

**Gaps it shows**
1. **Check what a benchmark measures before trusting a claim built on it.**
   - The vendor's claim (routed PCB, ready to manufacture) and the benchmark cited next to it (circuit design in simulation, layout excluded) measure different things.
   - The benchmark is run and funded by a company with a commercial interest. It says it does not sell scores and pays for the runs.
   - A score of about 60-70% still means about a third of the requirements failed.
2. **Where AI hardware design fails (practitioner reports, anecdotal).**
   - Nick: asked for a replacement for an end-of-life DC-DC module, ChatGPT suggested other discontinued parts. A human using Digi-Key's parametric search, then a Digi-Key rep, found one that worked.
   - shinsukke: the AI could not make a footprint from a PDF datasheet.
   - Gabi: generated schematics had open circuits and parts connected to nothing.
   - Mac: high-power switching layouts bring radiated RF and traces that act as antennas.
   - Nik: some routing must be precise for signal integrity or regulatory compliance.
3. **Nominal is not effective, a trap a simulator catches and a chat answer misses (EEBench example).** A submission specified a 22 µF capacitor, but it was only 11.4 µF effective at 4.7 V bias, against a 545 µF requirement. The protected rail fell below 3 V after 0.85 ms when 20 ms was required. Part values on a schematic are not what the part delivers in the circuit.
4. **Successes are real but anecdotal.**
   - Em: three AI-designed boards made with Claude worked first time, where hand-made designs usually need a respin. Routing was messy.
   - Em, separately: LLMs are good at reading datasheets, finding stock on JLCPCB/LCSC, and running SPICE on simple analog circuits.
   - Iman: Claude roughly halved schematic time.
   AI is a strong research and prototyping aid, and that is different from production sign-off.
5. **A prototype is not a production design: bring in an expert.**
   - Production boards need validation by multiple independent engineers and stringent testing (article).
   - Safety and EMC compliance testing are still required (Christoph).
   - A Reddit design for a 230V-to-5V supply had under 0.5 mm clearance, no transient protection and no isolation, intended for mass production (Fredriknk).
   - Hardware cannot be patched after shipping, and a fault a year in means replacements, legal disputes and recalls (olaf, jrbloom).
   - The most useful chip documentation is under NDA or tribal knowledge, so the AI never saw it (extralongdivision).
6. **Accountability.** Commenters ask who is responsible when a fully automated board fails. The company, not the tool, carries the customer fallout (Nik, olaf).

**Framings this source shows are outdated**
- "AI can't do hardware at all." It is now useful for prototypes, datasheet reading and simple analog simulation.
- "The vendor's demo and benchmark mean it is production-ready."

**Quotes**
- "a nifty party trick that works under strictly controlled conditions" (Hackaday, posing the question)
- "be fully validated by multiple independent engineers" (Hackaday, on production boards)

---

## Unreadable / limits
- None of the seven assigned sources was unreadable.
- The EEBench leaderboard (https://eebench.org/) renders its table with JavaScript. Fetched without it, the table was empty, so the GPT-6 Astra 69.3% score could not be confirmed there.
- No new web searches could be run (the shared search budget was exhausted). All facts come from directly fetched pages.
