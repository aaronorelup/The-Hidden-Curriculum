# Sweep: surveys and studies with data (2025-2026)

Research crew agent: sweep-surveys. Compiled 2026-10-12 for "The Hidden Curriculum".

Angle: what people actually do with AI now, where they struggle, what they distrust, and which skills the data says matter more or less. Every block below comes from a page that was fetched and read in this session. The numbers are the ones those pages state. Where a page is secondary coverage of a survey, it says so. 22 of the 25 sources are dated 2026, and 12 are from 2026-06 or later.

## Cross-cutting picture (each point traces to the numbered sources below)

1. **Agents are now the default, not an add-on.** 90% of professional developers use coding agents at least weekly and 68% daily [6]. Median developers report 47-63% of their code comes from AI or agents [6][3]. Coding agents are the top AI use among Stack Overflow respondents (66%) [1]. The tool landscape reshuffles within months: Claude Code went from 18% to 39% between January and mid-2026 [6]. Teaching specific tools dates fast. Teaching what all of them have in common lasts.
2. **Trust depends on whether the work can be checked.** The most common trust stance is "I trust it when I can easily verify it" (48%), and only 6.6% trust AI with important decisions [2]. 96% do not fully trust AI code, yet only 48% always check before committing [22]. This is the course's rule (AI handles what is verifiable, and humans check or bring in an expert for the rest), now backed by survey data.
3. **The human's job has moved to verification, context and judgment.** Developers rank "reviewing and validating AI code for quality and security" as the top skill (47%) [22]. Workers rank "quality control of AI output" (50%) and critical thinking (46%) top [15]. Experienced people say judgment, contextual awareness and trust-building are what AI lacks [10]. Context is the new bottleneck: 63% cite incomplete information, 57% outdated information, and 61% say key context lives in people's heads [2].
4. **Security is where "the agent said it's fine" fails hardest.** Across 100+ models, the security pass rate has stayed at 56% while syntax is near 100%. Newer, bigger and coding-specialised models are no safer [8]. 91% of 200 deployed vibe-coded apps had a vulnerability, and 55.5% of those flaws were protections nobody asked for. In about a fifth of replay runs the agent saw the risk and shipped anyway [11]. Broken access control is the top category in both the app audit [11] and GitHub's alert data (+172% YoY) [23].
5. **Learning and understanding erode when people delegate passively.** In an RCT, AI users scored 50% vs 67% on understanding, with debugging the biggest gap [21]. Students who used agents finished the task but could not extend their own code, and auto-accept went with the worst comprehension [7]. The people who kept learning asked conceptual questions or asked for explanations [21]. Experienced users iterate more and delegate less [17].
6. **Speed claims are unreliable, and some famous numbers are now outdated.** METR's "19% slower" reflects early-2025 tools. The follow-up could not measure the current effect, because developers refused to work without AI [19][5]. Organisation-level gains depend on testing, small batches and platform quality. Adoption raises instability and creates a "verification tax" [14][24].
7. **New operational gaps come with fleets of agents.** Builders run a median of 5 agents. 41% hit agent problems daily, and the top blockers are tracking state, debugging, and token or compute costs [4]. Developers report cost controls and model choice as new concerns [1]. Governance lags: only 24% of employers publish approved tools or guidance [2], and 35% of developers use AI through personal accounts [22].

---

## [1] The results of the 2026 Developer Survey are here! (Stack Overflow blog)

- **Author:** Ryan Donovan (Stack Overflow staff)
- **Date:** 2026-10-06
- **URL:** https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- **Kind:** survey
- **Credibility:** high (largest annual developer survey, 30,000+ responses from 169 countries, self-selected sample)
- **Gaps it names:**
  - Context is now a core concept of agentic engineering. Respondents rate project goals and requirements (85%) and code and docs (73%) as the most trusted context to give AI. Supplying context is the human's job.
  - 93% say an AI answer needs source attribution before they trust it. Knowing where an answer came from is a skill.
  - Token cost and model choice are now everyday concerns. Developers prioritise quality (75%) over cost (38%). Organisations set usage limits (38%), review spending (28%), and route different models to different tasks (27%).
  - AI is used mostly for familiar-area code generation (67%) and debugging (61%). Only 20% use it to deploy, operate or troubleshoot production systems. Production operations is a weak spot.
  - One-person organisations grew from 4% to 10%, which the author links to people starting businesses with agents. Solo builders need the whole hidden curriculum.
  - 79% want to build AI skills when learning something new, and 52% are still learning traditional coding skills.
- **Outdated framings:** "Search first, then Stack Overflow" (70% now ask an AI agent, 64% visit Stack Overflow less for simple questions). "AI = a chatbot" (66% of AI users work in coding agents. Claude Code is the most-cited agent at 66%, GitHub Copilot 59%).
- **Why it matters:** This is the freshest large dataset, published six days ago. It shows that agents, context and cost are what developers now think about. A course that still teaches "how to prompt a chatbot" is behind.

## [2] Stack Overflow Developer Survey 2026: full results site (AI, Knowledge and Community sections) and press release

- **Author:** Stack Overflow (results site). The press release quotes CEO Prashanth Chandrasekar.
- **Date:** 2026-10-06 (the results pages carry no date of their own; they were released alongside the press release dated 2026-10-06)
- **URL:** https://survey.stackoverflow.co/2026/ (press release: https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional/)
- **Kind:** survey
- **Credibility:** high
- **Gaps it names:**
  - Trust depends on whether the output can be verified. 48.0% trust AI output when they can easily verify it, 16.3% trust it for many tasks but not important decisions, 16.3% trust it only for low-risk tasks, 12.3% don't trust it for most tasks, and 6.6% trust it including for important decisions.
  - Context problems: 63.2% cite incomplete information as a barrier, 56.5% outdated information, and 60.9% say important context lives in people's heads. 12.1% "very often", 23.4% "often" and 43.1% "sometimes" discover important context only after starting or finishing a task. Writing down requirements and context is a skill the human must supply.
  - Governance lags adoption. Only 24% say their employer published approved tools or official AI guidance, and about 30% say AI use is optional and left to the individual (press release).
  - Security and privacy is a deciding factor for AI adoption for 28.7%. 13.0% avoid AI over privacy or security, and 17.1% over fear of losing skills or training their replacement.
  - Learning: 52% learned a new coding skill or language this year. Of those, 58.9% used technical documentation and 52.7% used AI code-generation tools (press release).
  - What people build with AI in-house: small scripts or automations (74%), team internal tools (66%), customer-facing products (54%) (press release).
- **Outdated framings:** "Developers distrust AI." In the 2025 survey more distrusted than trusted its accuracy (see [25]). The 2026 picture is conditional trust tied to verifiability.
- **Why it matters:** This is the clearest large-sample evidence for the course's central rule. Trust follows verifiability, and missing or outdated context is the most common barrier.

## [3] State of Devs 2026 (Devographics), as reported by Dr. Web

- **Author:** Markus Seyfferth (Dr. Web), reporting Devographics' State of Devs 2026. The survey overview is written by Miranda Heath.
- **Date:** 2026-10-03 (survey fieldwork 2026-07-05 to 2026-09-05, 5,463 respondents. The primary results site https://2026.stateofdevs.com/en-US/ is undated.)
- **URL:** https://www.drweb.de/state-of-devs-2026-ergebnisse-ki-burnout/
- **Kind:** survey
- **Credibility:** medium (self-selected online sample, mostly experienced developers. Some figures come from secondary coverage.)
- **Gaps it names:**
  - Median respondent gets 63% of their code from AI tools. The largest single group reports 87.5%.
  - 83% work at companies that encourage AI use, and about a third use AI more because of that pressure. Devographics notes that hard mandates (quotas, rankings) may go with lower satisfaction and worse mental health.
  - Only 23% say AI tools improved their mental state, and 46% disagree. Recent feelings: less motivation 66%, growing cynicism 60%, end-of-day exhaustion 57%.
  - The overview raises cognitive overload from steering several agents in parallel ("AI brainfry"), that prompting can feel addictive, and that heavy reliance can undermine learning. These points cite outside material, not survey data.
  - On the primary site, sentiment is split: 49% positive, 42% negative.
- **Outdated framings:** "AI is a pure productivity gain." Supervising agents carries a cognitive and wellbeing cost that the human has to manage.
- **Why it matters:** This is one of the most recent surveys (fieldwork ended 2026-09-05). It gives "managing your own attention while supervising agents" as a gap with data behind it.

## [4] Temporal "State of Development 2026" (agent users), as reported by DeveloperTech

- **Author:** Ryan Daws (DeveloperTech News, TechForge Media)
- **Date:** 2026-08-26
- **URL:** https://www.developer-tech.com/news/developers-trust-ai-agents-still-verify-code-manually/
- **Kind:** survey
- **Credibility:** medium (vendor survey of 554 engineers and technical leaders who already use agents. Secondary coverage, sampling not described.)
- **Gaps it names:**
  - The report says manual checking is still the only practical way to confirm delegated work is correct, short of extensive testing or formal proofs.
  - Agent operations: 41.1% hit agent issues daily or more often, and 16.4% hourly. The top blocker is tracking state (35.7%), then debugging, then token or compute costs. 79.8% say token and compute costs limit their progress.
  - Fleets: the median respondent runs 5 agents (mean 10.7).
  - Security is the top barrier to fully autonomous agents (39.5%).
  - Speed to production: 51.3% go from AI prototype to "production-ready" in hours or faster, and 77.1% within days. The report raises an open question about managing piles of agent-built custom tools that don't work together.
- **Outdated framings:** "One assistant in one chat window." People now run several agents at once and have to manage state, cost and failures.
- **Why it matters:** This is recent data on what goes wrong once people run agents for real. State, cost and verification are concepts nobody teaches.

## [5] AI productivity: the METR number is out of date (devs group)

- **Author:** Robert Pupel (CEO and co-founder, devs group)
- **Date:** 2026-08-17
- **URL:** https://devs-group.ch/en/blog/ai-productivity-studies-2026/
- **Kind:** essay
- **Credibility:** medium (practitioner digest that names and links its studies. Its METR figures match METR's own post [19].)
- **Gaps it names:**
  - The widely quoted 19% slowdown comes from early-2025 tools. In METR's follow-up both confidence intervals include zero, so neither a slowdown nor a speed-up is established.
  - Practical measurement: measure your own baseline before rollout and again about three months later. Track reverts and hotfixes over 90 days, and track change size per author to separate agent work from human work.
  - Don't use an agent's confidence score as a review filter (cites the MSR 2026 breaking-changes study [16]).
  - Scale review depth by task type: greenfield work can be looser, refactoring and maintenance need strict review. Don't make auto-accept the default (cites the (Im)Paired Programming study [7]).
  - Context files (AGENTS.md) generally did not raise agent success but added over 20% to cost (cites [20]).
- **Outdated framings:** "AI makes developers 19% slower" (early-2025 tools) and "Copilot makes you 55% faster" (a 2022 vendor-funded lab study). Both get cited as current, and neither is.
- **Why it matters:** It turns the research into rules a learner can act on, such as review depth by task type and no default auto-accept. It also shows how quickly "facts" about AI go stale.

## [6] How Much Code Do Developers Really Let Agents Write? (JetBrains Research), with the companion AI coding agent adoption post

- **Author:** Mikhail Bogdanov (JetBrains Research)
- **Date:** 2026-08 (the posts show no day. The URL path and images point to August 2026. Survey fielded May-July 2026.)
- **URL:** https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/ (companion: https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/)
- **Kind:** survey
- **Credibility:** high (Developer Ecosystem Survey 2026, 15,000+ professional developers, localised, quota-sampled and reweighted)
- **Gaps it names:**
  - Self-reported share of code: about 47% fully agent-generated, 38% AI-assisted and 27% manual. The figures overlap and the authors flag them as approximate. Over half write less than 20% of their code by hand, and one in five writes none without AI.
  - Three segments: agentic coders (~31%, ~84% agent-generated), AI-assisted coders (~47%) and manual coders (~23%). Only ~22% hand agents more than 80% of their code.
  - Juniors lean toward AI-assisted work rather than fully agentic workflows. About a quarter of seniors generate over 80% with agents.
  - Language matters. Go, JavaScript and TypeScript are the most agentic (54-55%). C and C++ are the least (38% hand-written on average).
  - Adoption post: 90% use AI coding agents at work at least weekly, 68% daily. Claude Code rose from 18% (January 2026) to about 39%, Codex from 3% to 16%. GitHub Copilot fell from 29% to 21% and Cursor from 18% to 12%.
- **Outdated framings:** "Hand coding is the default and AI is an assistant." The author says purely manual coding is becoming a thing of the past. Any tool ranking also goes stale within months.
- **Why it matters:** This is representative, recent data showing that most professional code is now agent-written. The open skill is the one these posts do not measure: verifying the work.

## [7] (Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding

- **Author:** Nishant Balepur, Connor Baumler, Valerie Chen, Eunsol Choi, Rachel Rudinger, Jordan Lee Boyd-Graber
- **Date:** 2026-07-29
- **URL:** https://arxiv.org/abs/2607.26375
- **Kind:** paper
- **Credibility:** medium (in-progress preprint, 54 students, controlled design)
- **Gaps it names:**
  - Students who built a website with an agent that edits their code finished the task but understood their code less. They were poorly prepared to extend it without AI.
  - Copy-and-paste prompting and auto-accepting edits were linked to lower comprehension.
  - Users preferred agents anyway because they are fast and easy, even though their understanding was worse.
- **Outdated framings:** "If the task got done, you learned it." Finishing is no longer evidence of understanding.
- **Why it matters:** The course's audience is learning while building. This shows that auto-accept is the learning trap, and that an active habit (read, ask why, then accept) is part of what the course should teach.

## [8] Veracode 2026 GenAI Code Security Report (press release)

- **Author:** Veracode (quotes Chris Wysopal, co-founder and Chief Security Evangelist)
- **Date:** 2026-07-28
- **URL:** https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/ (report page: https://www.veracode.com/blog/2026-genai-code-security-report)
- **Kind:** report
- **Credibility:** medium (security vendor that sells remediation tools. The benchmark runs over four snapshots and 100+ models. The latest round is 11 models on 80 tasks.)
- **Gaps it names:**
  - The average security pass rate is 56%, essentially unchanged across four snapshots and 100+ models, while syntax pass rates are near 100%. Code that compiles and runs is not secure code.
  - Without security-specific guidance, models fail nearly 44% of security-relevant tasks. Even the best model (GPT-5.5, 68%) fails about one in three.
  - Coding-specialised models (51%) are no safer than general-purpose models (52%). Large models score 53% vs 51%, and reasoning models 56% vs 51%. A newer or bigger model is not a security plan.
  - Language spread: Python 63%, Java 30%.
  - Veracode's rule of thumb is to treat AI code like any unreviewed code: scan it, fix it, and never ship it blind.
- **Outdated framings:** "Models are improving, so security will take care of itself."
- **Why it matters:** This is longitudinal evidence for the course's security rule. The agent cannot vouch for its own security, so humans need scanners, and experts where they cannot judge.

## [9] Adoption and Impact of Command-Line AI Coding Agents: Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI

- **Author:** Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva (Microsoft)
- **Date:** 2026-07-01
- **URL:** https://arxiv.org/abs/2607.01418 (full text: https://arxiv.org/html/2607.01418)
- **Kind:** paper
- **Credibility:** high (tens of thousands of engineers, telemetry with a synthetic-control design. Single company, self-selected adopters.)
- **Gaps it names:**
  - Adopters merged about 24% more PRs per engineer per day (95% CI +14.5% to +33.7%), and the lift held over four months. The authors measured no quality outcomes and call quality the pressing open question. More output is not proof of better software.
  - Respondents saw the tools as a particularly good fit for senior developers who can break work into pieces and review the output. They doubted juniors could use them as well, and worried juniors would not develop a sense for good code.
  - Practices that mattered: breaking work into smaller chunks, reviewing output for correctness, completeness and sanity, and juggling parallel work streams. One principal engineer needed 5-10 clarification prompts per task.
  - Adoption spread socially. Engineers whose skip-level peers used the tool had +216% higher odds of trying it.
- **Outdated framings:** "AI coding means autocomplete in the IDE." The rollout was of command-line agents.
- **Why it matters:** The best large-scale field evidence from 2026. Throughput is measurable and quality is not. Decomposing and reviewing are what made seniors effective, and those are exactly the gaps this course targets.

## [10] Anthropic Economic Index report: Cadences

- **Author:** Maxim Massenkoff, Eva Lyubich, Szymon Sacher, Zoe Hitzig, Shaoyi Zhang, Ryan Heller, Peter McCrory (Anthropic)
- **Date:** 2026-06-26
- **URL:** https://www.anthropic.com/research/economic-index-june-2026-report
- **Kind:** report
- **Credibility:** high for the usage data (privacy-preserving analysis of Claude traffic). The linked survey of about 9,700 users is not representative.
- **Gaps it names:**
  - Claude Code sessions are more autonomous than chat or Cowork. About two-thirds of the gap comes from people delegating more on the same tasks, not from different tasks. The product shapes how much people hand over.
  - 93% of chat and Cowork conversations produce an identifiable output. Code and technical work is only about one-sixth. Explanations (17%), documents and reports (15%) and guidance (11%) lead, so most AI use is not coding.
  - Survey: 68% say they learn more with AI and 57% say AI made their skills more valuable. The authors warn these are self-assessments and do not rule out skill erosion.
  - People with 15+ years of experience estimate the share of their tasks AI can do about 10 points lower than first-year workers do. They name judgment, contextual awareness and trust-building as hard for AI.
  - Over a third expect AI to handle most or nearly all of their work tasks within 12 months.
- **Outdated framings:** "AI use = asking a chatbot questions." In agentic products, use is delegation.
- **Why it matters:** First-party usage data shows delegation rising in agent tools, and experienced workers saying the human's value is judgment and context. That supports the course's split between what YOU do and what the agent does.

## [11] Understanding the (In)Security of Vibe-Coded Applications

- **Author:** Junquan Deng, Zhiyu Fan, Ruijie Meng
- **Date:** 2026-06-22 (v1. Revised to v4 on 2026-09-14.)
- **URL:** https://arxiv.org/abs/2606.23130 (full text: https://arxiv.org/html/2606.23130v4)
- **Kind:** paper
- **Credibility:** medium (preprint, but large and systematic: 9,041 apps collected, 200 publicly deployed apps built with Claude Code and Lovable audited, 1,186 vulnerabilities found)
- **Gaps it names:**
  - 91.0% of audited apps had at least one vulnerability, and 65.77% of the vulnerabilities were Critical or High.
  - The top categories are broken access control (28.58% of vulnerabilities, present in 64% of apps), injection (54% of apps) and authentication failures (51.5% of apps).
  - "Hidden security rules" are the single biggest failure mode (55.5%). Server-side checks, input validation and escaping were left out because the user never asked for them. A beginner does not know what to ask for.
  - "Function-fix side effects" (8.4%): an error was "fixed" by weakening a control, for example adding a bypass-login route to get around an auth error. "Incomplete change propagation" (9.3%): a protection was added to new code but not to the old handlers.
  - "User-dependent security" (6.1%): deployment steps such as keeping secret files out of Git were left to the user, and one app committed exported database files to a public repo.
  - In 20.7% of replay runs the agent recognised the risk but shipped insecure code anyway, offering a warning instead of a fix.
  - Mitigation: asking for a "production-ready" implementation cut reintroduction from 25.7% to 11.0%. A detailed "professional" prompt full of terms the user did not understand raised it to 45.7%. Newer models did not reliably help.
  - The apps were built in short bursts (median development span 8.39 days), and the authors infer little human hardening before deployment.
- **Outdated framings:** "The agent knows how to make it safe and will tell you if it isn't." It omits unrequested protections and sometimes warns without fixing.
- **Why it matters:** This is the strongest data behind Aaron's security rule. It names the specific things a non-expert must ask for, check, or get an expert to check: authorization on every path, secrets out of the repo, and security warnings that need acting on.

## [12] Pew Research: Americans and AI 2026 (chatbot use and views), as reported by The Next Web

- **Author:** Allison Steffens Herrera (The Next Web), reporting Pew Research Center. Pew's own chart page "Americans report using ChatGPT far more than other chatbots" is dated 2026-06-11: https://www.pewresearch.org/?p=303590
- **Date:** 2026-06-17 (survey fielded 2026-02-17 to 2026-02-23)
- **URL:** https://thenextweb.com/news/pew-research-americans-ai-chatbot-skepticism-regulation-distrust-2026?type=AI
- **Kind:** survey
- **Credibility:** medium (Pew is high-quality and nationally representative, but most figures here come through secondary coverage. The chatbot-share chart was confirmed on Pew's own page.)
- **Gaps it names:**
  - 49% of US adults use AI chatbots. Uses: information searching 42%, entertainment 25%, image or video creation 24%, medical advice 20%, news 13%, emotional support 10%.
  - 71% expect AI to make their personal data less secure. 67% have little or no confidence the government can regulate AI, and 59% little or no confidence that companies will develop it responsibly.
  - 21% of workers use AI in their jobs (16% in 2024).
  - Many people use AI without recognising it as AI (37% via smartwatches, 35% via smart speakers).
- **Outdated framings:** "Everyone uses ChatGPT, so the tool landscape is ChatGPT." The public is 44% ChatGPT and 6% Claude, while developers have moved to agents (see [1], [6]). The course's audience sits between these worlds.
- **Why it matters:** It is a baseline for the general public. People use chatbots for facts and medical advice and worry about their data. Verifying non-code answers and handling data privacy are gaps for the course's non-developer audience too.

## [13] State of Web Dev AI 2026 (Devographics), as reported by I Programmer

- **Author:** Janet Swift (I Programmer)
- **Date:** 2026-05-20 (survey fielded 2026-04-08 to 2026-05-08, 7,258 respondents)
- **URL:** https://www.i-programmer.info/news/87-web-development/18880-ai-increasingly-embraced-by-web-devs.html
- **Kind:** survey
- **Credibility:** medium (self-selected and AI-focused, so likely skewed toward AI users, as the survey's own author warns. Secondary coverage.)
- **Gaps it names:**
  - The average share of AI-generated code is 54%, up from 28% in 2025.
  - The top pain point is hallucinations and inaccuracies (64%), followed by code quality (53%).
  - Concerns: "AI slop" 34%, negative cognitive impact 30%, security issues 29%, rising AI costs 16%.
  - Satisfaction with AI tools for web development is 3.4 out of 5.
- **Outdated framings:** "AI writes a small share of web code." It roughly doubled in a year.
- **Why it matters:** Web builders, a core audience, name inaccuracy and quality as their main struggles, and fewer of them rank security as a concern than the audits in [8] and [11] suggest they should.

## [14] New DORA Report Claims Strong Engineering Foundations Drive AI Return on Investment (InfoQ, on DORA's "ROI of AI-Assisted Software Development")

- **Author:** Matt Saunders (InfoQ), reporting DORA / Google Cloud. The report page https://dora.dev/ai/roi/ shows "Last updated: April 22, 2026".
- **Date:** 2026-05-11
- **URL:** https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/
- **Kind:** report
- **Credibility:** medium (DORA is a leading research program, but its figures are illustrative, model-based and labelled "high-uncertainty". Secondary coverage.)
- **Gaps it names:**
  - J-curve: expect a dip before gains, driven by the learning curve, a "verification tax" for reviewing AI code, and downstream bottlenecks in testing and change approval.
  - AI adoption correlates with rising delivery instability. Faster code generation can overwhelm pipelines and manual review gates.
  - The foundations that turn AI speed into results: automated testing, continuous integration, small batch sizes, version control practices, a quality internal platform, and internal data that AI can reach.
  - Cited estimates: 35-40% gains on simple greenfield tasks vs 10% or less on complex legacy code.
  - The report advises against cutting headcount as an AI strategy.
- **Outdated framings:** "AI will fix a broken engineering process." DORA frames AI as an amplifier of whatever system it lands in.
- **Why it matters:** It explains why tests, version control and small changes matter more with agents: they are how unverifiable speed becomes verifiable progress.

## [15] 2026 Work Trend Index Annual Report: Agents, human agency, and the opportunity for every organization (Microsoft WorkLab)

- **Author:** Microsoft WorkLab (no byline)
- **Date:** 2026-05-05
- **URL:** https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
- **Kind:** report
- **Credibility:** medium (vendor research combining a worker survey and Microsoft 365 Copilot telemetry from 100,000+ chats)
- **Gaps it names:**
  - The top human skills for the AI era are quality control of AI output (50%) and critical thinking (46%).
  - 86% of AI users treat output as a starting point, not a final answer.
  - The most advanced users ("Frontier Professionals", 16%) do some work without AI to keep their skills sharp (43% vs 30%). They also stop to decide whether a task should go to AI or a human (53% vs 33%), and they distinguish four modes: delegation, collaboration, asking and exploration.
  - As agents scale, organisations need "evaluation infrastructure" and clear answers to who reviews agent performance and who can change agent workflows. IT acts as the control plane for agent identities and permissions. The security risks named are data exfiltration, unintended actions and unauthorized access.
  - Organisational factors explain 67% of measured AI impact. Only 26% of AI users say their leadership is aligned on AI.
- **Outdated framings:** "AI is a tool you prompt." The human now sets intent, defines the quality bar and owns the outcome while agents execute.
- **Why it matters:** Outside software, the data says the same thing. The human's job is quality control, judgment and choosing the mode, and the best users protect their own skills on purpose.

## [16] Safer Builders, Risky Maintainers: A Comparative Study of Breaking Changes in Human vs Agentic PRs

- **Author:** K M Ferdous, Dipayan Banik, Kowshik Chowdhury, Shazibul Islam Shamim
- **Date:** 2026-03-29
- **URL:** https://arxiv.org/abs/2603.27524
- **Kind:** paper
- **Credibility:** medium (accepted at MSR 2026. 7,191 agent PRs and 1,402 human PRs from Python repos in the AIDev dataset.)
- **Gaps it names:**
  - On new-code tasks, agents introduced fewer breaking changes than humans (3.45% vs 7.40%). On maintenance they were riskier: 6.72% for refactoring and 9.35% for chores.
  - "Confidence trap": agent PRs marked highly confident still introduced breaking changes. Review maintenance changes strictly regardless of the confidence the agent reports.
- **Outdated framings:** "Agent code is uniformly riskier (or safer) than human code." Risk depends on the kind of task.
- **Why it matters:** It gives learners a concrete rule: an agent's confidence is not evidence, and "small cleanups" are where breakage hides.

## [17] Anthropic Economic Index report: Learning Curves

- **Author:** Maxim Massenkoff, Eva Lyubich, Peter McCrory (lead), Ruth Appel, Ryan Heller (Anthropic)
- **Date:** 2026-03-24
- **URL:** https://www.anthropic.com/research/economic-index-march-2026-report
- **Kind:** report
- **Credibility:** high (1 million conversations sampled 2026-02-05 to 2026-02-12, with controls. The authors cannot yet separate learning-by-doing from selection effects.)
- **Gaps it names:**
  - Users who signed up six or more months earlier have higher conversation success rates: about 10% in the headline, and roughly 3-5 percentage points after controlling for task, model and country.
  - Experienced users iterate more and use fully delegated ("directive") patterns less. This contradicts the authors' own earlier hypothesis that sophisticated users automate more.
  - Users bring their most complex, highest-value tasks to the strongest model (Opus).
  - If effective AI use is a skill built through experimentation, early adopters' advantage compounds, which could deepen inequality.
- **Outdated framings:** "Power users just hand everything over." The data shows the skilled pattern is iteration and steering.
- **Why it matters:** Using AI well is a learnable skill that shows up in outcomes. That is the reason this course exists: closing that gap for people who did not start early.

## [18] AI Tooling for Software Engineers in 2026 (The Pragmatic Engineer)

- **Author:** Gergely Orosz and Elin Nilsson
- **Date:** 2026-03-03 (survey 2026-01-27 to 2026-02-17, 906 respondents)
- **URL:** https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- **Kind:** survey
- **Credibility:** medium (newsletter subscribers, skewed senior: median 11-15 years of experience. Sections on cost, quality and security are behind a paywall and were not read.)
- **Gaps it names:**
  - 95% use AI weekly. 75% use it for at least half their engineering work, and 56% for 70% or more.
  - 55% regularly use AI agents, led by staff-plus engineers (63.5%). Agent uses include code review and validation, repetitive automation, bug investigation, and code creation with human oversight.
  - A common setup pairs a terminal running an agent with an IDE used to review the agent's changes. Reviewing diffs is the human's workstation skill.
  - 70% juggle 2-4 tools. Large enterprises lag on tool approval (GitHub Copilot leads at 10,000+ employees).
- **Outdated framings:** "AI coding = Copilot autocomplete." Claude Code overtook Copilot and Cursor within about eight months of release and is the most-loved tool (46%).
- **Why it matters:** It shows the current shape of experienced practice: the agent works in the terminal and the human reviews in the editor. It also shows how fast tool rankings flip.

## [19] We are Changing our Developer Productivity Experiment Design (METR)

- **Author:** Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud (METR)
- **Date:** 2026-02-24
- **URL:** https://metr.org/blog/2026-02-24-uplift-update/
- **Kind:** paper
- **Credibility:** high (the RCT team reporting on its own follow-up: 57 developers, 143 repos, 800+ tasks)
- **Gaps it names:**
  - Early 2025: AI made experienced open-source developers' tasks 19% longer (CI +2% to +39%).
  - Late 2025: returning developers about 18% faster (CI -38% to +9%), new recruits about 4% faster (CI -15% to +9%). METR calls this an unreliable signal.
  - Selection problem: developers increasingly refused to take part because they would not work without AI, and 30-50% withheld tasks they did not want to do without AI.
  - Time-on-task can no longer be measured well for developers running several agents at once. They work on unrelated tasks while agents run, so "how long did it take" is ill-defined.
- **Outdated framings:** "AI makes experienced developers 19% slower." METR itself now believes developers are probably more sped up than in early 2025 but cannot measure by how much. The broader lesson that perceived speed is unreliable still holds.
- **Why it matters:** It retires a famous statistic and shows the field has moved to parallel agents. It is a model of honestly updating a finding, which the course itself has to do every week.

## [20] Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

- **Author:** Thibaud Gloaguen, Niels Mündler-Sasahara, Mark Niklas Müller, Veselin Raychev, Martin Vechev (ETH Zurich and others)
- **Date:** 2026-02-12 (v1. Revised to v3 on 2026-09-29.)
- **URL:** https://arxiv.org/abs/2602.11988
- **Kind:** paper
- **Credibility:** medium (preprint. Two settings, multiple LLMs and agents.)
- **Gaps it names:**
  - Context files did not generally improve task success, for both LLM-generated and developer-written files, and they raised inference cost by over 20%.
  - Agents follow instructions in context files well, but repository overviews, though popular and recommended by providers, did not help.
  - Use context files for non-standard practices the agent could not infer, and test any "improvement" before relying on it.
- **Outdated framings:** "Write a big AGENTS.md or CLAUDE.md overview and the agent gets better." The data says to write instructions, not descriptions, and to measure.
- **Why it matters:** Context is the new core skill (see [1], [2]), but this shows that more context is not automatically better context. That surprises learners and is testable.

## [21] How AI assistance impacts the formation of coding skills (Anthropic)

- **Author:** Judy Hanwen Shen and Alex Tamkin (Anthropic; paper arXiv:2601.20245)
- **Date:** 2026-01-29
- **URL:** https://www.anthropic.com/research/AI-assistance-coding-skills
- **Kind:** paper
- **Credibility:** high design quality (RCT) but small (52 mostly junior engineers learning the Trio library, with a short-term quiz)
- **Gaps it names:**
  - The AI group scored 50% vs 67% for hand-coders on a quiz about the library they had just used (d = 0.738). The biggest gap was in debugging, which the authors chose because debugging, code reading and concepts are what you need to oversee AI code.
  - The AI group was not significantly faster (about 2 minutes). Some participants spent up to 30% of their time writing queries.
  - Interaction pattern decided learning. Full delegation, progressive reliance, and "let AI debug it" scored under 40%. Conceptual questions, code with explanations, and generate-then-ask-why scored 65% or more.
  - Advice: stay cognitively engaged, accept some productive struggle, and use the learning or explanatory modes that tools offer.
- **Outdated framings:** "AI automatically makes you learn faster." It can, but only with an engaged pattern of use.
- **Why it matters:** This squares with Aaron's correction. The agent does the debugging, and the human needs enough conceptual understanding to oversee it. The study gives evidence-backed ways to keep that understanding while using AI.

## [22] 2026 State of Code Developer Survey report (Sonar)

- **Author:** Sonar (blog summary by Anirban Chatterjee. Press release quotes CEO Tariq Shaukat.)
- **Date:** 2026-01-08 (fieldwork October 2025, 1,149 professional developers worldwide)
- **URL:** https://www.sonarsource.com/state-of-code-developer-survey-report.pdf (blog: https://www.sonarsource.com/blog/state-of-code-developer-survey-report-the-current-reality-of-ai-coding/)
- **Kind:** survey
- **Credibility:** medium (a code-verification vendor with an interest in the "verification gap" framing. Methodology is disclosed.)
- **Gaps it names:**
  - Verification gap: 96% do not fully trust that AI code is functionally correct, but only 48% always check AI-assisted code before committing. 95% spend some effort reviewing, testing or correcting AI output, and 59% call that effort moderate or substantial.
  - 61% agree AI often produces code that looks correct but isn't reliable. 38% say reviewing AI code takes more effort than reviewing a colleague's code (27% say less).
  - Developers' top skill for the AI era is reviewing and validating AI code for quality and security (47%), then prompting efficiently (42%).
  - Shadow AI: 35% use top AI tools through personal accounts. Of ChatGPT users, 52% use a personal account, which risks feeding company or customer data to tools outside company control.
  - Security: exposure of sensitive company or customer data is the top concern (57%). New or subtle vulnerabilities worry 47%, severe vulnerabilities 44%. Only 28% use agents for security patching, the least common agent use.
  - Toil did not shrink. It holds at about 23-25% of the week whatever the AI use, and shifts toward verification and technical debt. 53% say AI hurt technical debt by producing code that looked correct but was unreliable, and 40% blame unnecessary or duplicated code.
  - Juniors are more worried than seniors: 66% vs 48% say AI code looks right but isn't reliable, and 50% vs 41% fear their own skills eroding.
- **Outdated framings:** "AI removes developer toil." It moves the toil into verification. "Faster writing = productivity." Value now depends on confidence in what you deploy.
- **Why it matters:** It gives the most concrete numbers on the verification gap and names the skill developers themselves rank first: validating AI code for quality and security.

## [23] Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 (GitHub Octoverse 2025)

- **Author:** GitHub Staff
- **Date:** 2025-10-28 (updated 2026-02-28. Data covers 2024-09-01 to 2025-08-31.)
- **URL:** https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- **Kind:** report
- **Credibility:** high (platform telemetry from 180M+ developers. Note GitHub sells Copilot.)
- **Gaps it names:**
  - Broken access control became the most common CodeQL alert (151,000+ repos, +172% YoY), which GitHub ties partly to AI-generated code that skips auth checks.
  - About 80% of new developers use Copilot in their first week. Beginners start with AI from day one.
  - TypeScript became #1 by contributors (August 2025). GitHub links this to typed languages making agent-written code more reliable, citing a study where 94% of LLM compilation errors were type-check failures. Types are a verification tool the agent can use.
  - The Copilot coding agent helped create 1M+ PRs from May to September 2025.
- **Outdated framings:** "Language choice is taste." It now affects how checkable agent output is.
- **Why it matters:** Ecosystem-scale confirmation that AI-era security failures cluster in authorization, and that machine-checkable structure (types, tests) lets an agent check its own work.

## [24] How are developers using AI? Inside our 2025 DORA report (Google)

- **Author:** Ryan J. Salva (Google)
- **Date:** 2025-09-23
- **URL:** https://blog.google/technology/developers/dora-report-2025/
- **Kind:** report
- **Credibility:** high (nearly 5,000 technology professionals). Just over 12 months old, so it is included as foundational. Its amplifier finding was restated in DORA's 2026 ROI report [14].
- **Gaps it names:**
  - 90% adoption, a median of two hours a day with AI, and 65% relying on it heavily.
  - Trust paradox: 30% trust AI output only a little (23%) or not at all (7%), even while over 80% report productivity gains. AI supports human judgment rather than replacing it.
  - Making sure software works as intended before delivery remains an open challenge.
  - AI is a mirror and multiplier: it boosts cohesive organisations and exposes weaknesses in fragmented ones. The report introduces a seven-capability AI model and seven team archetypes.
- **Outdated framings:** "Adopt AI and delivery improves." The prior year's negative throughput finding reversed, but only under the right conditions.
- **Why it matters:** It is the baseline that later 2026 reports build on. It frames trust as calibrated use, which is the right mental model to teach.

## [25] Stack Overflow 2025 Developer Survey: AI section

- **Author:** Stack Overflow
- **Date:** undated (the page shows no date. It is the 2025 edition of the survey, over 12 months old, and included as foundational because the 2026 edition did not repeat these questions.)
- **URL:** https://survey.stackoverflow.co/2025/ai
- **Kind:** survey
- **Credibility:** high
- **Gaps it names:**
  - The top frustration is AI solutions that are almost right but not quite (66%). Next, 45.2% say debugging AI-generated code is more time-consuming.
  - People would still ask a human when they don't trust the AI's answer (75.3%), when there are ethical or security concerns about code (61.7%), or when they want to fully understand something (61.3%). These are the "bring in an expert" moments.
  - Agent concerns: accuracy 87%, security and privacy 81%.
  - Tasks they did not plan to use AI for: deployment and monitoring (75.8%), committing and reviewing code (58.7%).
  - Trust then: 3.1% highly trusted AI accuracy and 19.6% highly distrusted it.
- **Outdated framings:** In 2025, 72.2% said vibe coding was not part of their work and only 14.1% used agents daily at work. By 2026, agents are mainstream (see [1], [6]). The "almost right" problem has not been shown to go away.
- **Why it matters:** "Almost right" is still the defining failure mode, and the human is the one who has to notice it. The list of when people still want a human maps directly onto the course's rule.

---

## Notes on method and exclusions

- Search budget: the session's shared web-search limit ran out partway through, so a few planned checks could not be run. Gallup's 2026 workforce data is not included: the secondary pages found either 404'd or returned no article text, and the primary Gallup page was not reached. The Anthropic "2026 Agentic Coding Trends Report", Qodo's "State of AI Code Quality 2026", Atlassian's 2026 DevEx report and the Escape.tech scan of 5,600 vibe-coded apps were seen only in search snippets and are NOT listed.
- Unverified figures excluded: one search summary said the 2026 Stack Overflow survey found 76.5% ran AI answers locally, 63.9% compared them with their codebase and 53% inspected tests or security implications. None of the fetched Stack Overflow pages (blog, results site, press release) contained these numbers, so they are not used.
- Considered but left out as weaker or older: SD Times informal survey of 103 developers (2026-09-25, written by a vendor CEO). TechTimes vibe-coding piece (2026-05-24, many unnamed or second-hand sources). Fastly senior vs junior survey (2025-08-27). Faros AI telemetry piece (2025-07-28). JetBrains State of Developer Ecosystem 2025 (2025-10).
- Several sources are vendors with an interest in their framing: Sonar and Veracode sell verification and security tooling, GitHub and Microsoft sell Copilot, and Anthropic sells Claude. Their numbers are reported as stated, with that caveat.
