# Research notes: who uses agents and how much, trust tied to verifiability, and what heavy AI use does to understanding and skill

Agent: read-surveys-and-learning. Read on 2026-10-12. Sources S080 to S085. Machine-readable gaps are in `surveys-and-learning.json` (same folder).

## How this was read

- **All six assigned sources were fetched and read.** No source was unreadable.
- **S080 (Stack Overflow Developer Survey 2026)** was read from the results home page and from the AI, Knowledge, Community and Methodology chapters. The chapter "data" pages (`/2026/ai/data`, `/2026/knowledge/data`) give the exact question wording and every n, so the figures below come from those tables. I also read the blog summary and the press release. I found the press release through Stack Overflow's press page (https://stackoverflow.co/company/press/), because this turn's shared web-search budget was used up after my first search.
- **S082 and S085** were read as full HTML text on arXiv, not just the abstracts. S085's companion paper (A Paradox of AI Fluency) was also read in HTML.
- **S083** was read on the Anthropic research page. I also checked the arXiv record of the full paper (2601.20245) for its dates.
- **Quotes.** This file uses one direct quote (Osmani's floor/ceiling line, which the brief asks for). Everything else is close paraphrase. Coined terms appear as terms, e.g. "perception-action gap", "Confidence Trap", "code vending machine".
- **Unreadable:** none.

### Corrections to the brief

- **S080 date.** The results site itself shows no date. Release date 2026-10-06 comes from the blog post and the press release. Fieldwork ran 2026-06-23 to 2026-08-05 (methodology page). Sample: 30,903 valid responses out of 39,266 rows, from 169 countries. Recruitment came through Stack Overflow's own site, blog and opted-in email list, so the sample leans toward people already engaged with Stack Overflow.
- **S080 "93% need source attribution".** The 93% is the share rating attribution at least *somewhat* important (very important 52.1%, important 26.5%, somewhat 14.0%; n = 13,945). The press release uses the stricter 78.7% (important or very important).
- **S080 "asking an agent first (70%)".** The exact figure is 69.9% (n = 16,664). The question was multi-select ("which actions do you turn to first"), and 82.7% also search online first.
- **S080 cost and model choice.** These are real survey items, but two of them have small samples: 1,033 for "has cost or usage limits changed how you use AI" and 560 for "have you changed how you write prompts". Present them as indicative only.
- **S080 "87% trust, up from 31%".** The results page says trust rose from 31% to more than 87%. But the 87% counts the 2026 answer "I trust it when I can easily verify the output" as trust. Do not teach this as "trust in AI tripled".
- **S080 internal inconsistencies.** The blog gives 67% for "code in a familiar area" and 61% for debugging. The AI data table gives 69.3% and 63.8% (n = 12,547). The press release says 66% find AI useful for debugging; the data table gives 72.6% useful or very useful. Cite the data tables.
- **S081 date.** The page shows no date. The URL path and image uploads are 2026/08, so the date is August 2026 (inferred). Author: Mikhail Bogdanov, JetBrains Research.
- **S081 is missing two items the brief asks for.** I found no weekly-agent-use figure (the survey measures shares of last month's code, not frequency of use). I also found no explicit warning that tool rankings go stale within months. The page only says Claude Code is "increasingly becoming the mainstream" tool and that Codex is catching up. For tool churn, the evidence is the disagreement between surveys (see S081 below).
- **S082** is confirmed as 2026-07-01, v1 only. The "who it suits" and "worry about juniors" material comes from a 609-response survey of self-selected attendees of an internal Microsoft event. It is not from the PR telemetry.
- **S083** is confirmed as 2026-01-29 for the blog. The paper was arXiv v1 on 2026-01-28 and v2 on 2026-02-01. It is older than three months but within twelve, and it is foundational and still current: Osmani's August 2026 essay (S084) builds on it.
- **S085** is confirmed as 2026-05-23. The paper's groups are called "non-developers", not "non-coders". The companion "A Paradox of AI Fluency" is by Christopher Potts and Moritz Sudhof, 2026-04-28. Its data are 2023-05 to 2025-07 chat transcripts from WildChat, with OpenAI models from GPT-3.5-turbo to GPT-4.1-mini. So its failure types are current concepts, but its rates come from pre-agent chat use.

## The idea that ties these sources together

Professionals now let agents write a large share of their code and ask an agent first. But they **trust output only as far as they can check it** (S080). The ability to check comes from experience, and heavy delegation erodes it (S083, S084, S085). More output is measurable, but better software is not yet measured (S082). The people who do well with agents break work down, give context, and verify. People without that experience know AI code is risky but cannot act on that knowledge: they re-prompt instead of evaluating, and their failures stay invisible (S085 and its companion). That is the course rule, seen in surveys: delegate what is verifiable, check what the agent cannot verify, and bring in someone who can when you cannot.

---

## S080: Stack Overflow Developer Survey 2026 (results site, chapters, blog summary, press release)

- **Author:** Stack Overflow. The blog summary is by Ryan Donovan. The press release quotes CEO Prashanth Chandrasekar, and the results page also quotes CPTO Jody Bailey.
- **Date:** Released 2026-10-06 (blog and press release); the results site is undated. Fieldwork 2026-06-23 to 2026-08-05.
- **Sample:** 30,903 valid responses (39,266 rows), 169 countries, 103 questions. The n for each question is given below.
- **URLs:**
  - https://survey.stackoverflow.co/2026/ (AI chapter data: https://survey.stackoverflow.co/2026/ai/data ; Knowledge chapter data: https://survey.stackoverflow.co/2026/knowledge/data ; Community: https://survey.stackoverflow.co/2026/community ; Methodology: https://survey.stackoverflow.co/2026/methodology)
  - Blog: https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
  - Press release: https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional

**Summary.** AI use is close to universal among respondents, and sentiment is mostly favorable (62% favorable). But trust is conditional. Nearly half trust AI output only when they can easily verify it, and only 6.6% trust it for important work decisions. A new 2026 chapter on knowledge and context finds that missing, outdated and unwritten context is the main obstacle. It also finds that developers want answers they can trace to a source. Cost controls and model choice have become routine organisational decisions. The press release frames developers' skepticism as a safeguard.

**Gaps and specific points**

1. **Trust follows verifiability** (n = 14,304, question: "How much do you trust the output from AI tools or AI agents as part of your workflow?")
   - Trust it when I can easily verify the output: 48.0%
   - Trust it for many tasks, but not important decisions: 16.3%
   - Low-risk tasks only: 16.3%
   - Do not trust it for most work: 12.3%
   - Trust it for many tasks including important work decisions: 6.6%. The page says this falls to about 4% among developers with 1 to 5 years of experience.
   - Favorable attitude to AI is 53% among people with 1 to 5 years of experience and 69% among people with 16+ years. Experienced developers like AI more, and they still trust it only conditionally.

2. **What people actually do before using an AI answer** (n = 13,162, select all)
   - Run it locally: 76.5%
   - Compare against codebase context: 63.9%
   - Inspect tests or security implications: 53.0%
   - Read official docs: 38.0%
   - Search Stack Overflow: 12.2%
   - Use as-is: 9.6%
   - Ask a coworker: 6.9%
   - The most common check is "run it", which shows only that it runs. Barely half look at tests or security.

3. **Where AI is kept at arm's length** (n = 12,547)
   - Deploying or operating production: 19.9% use AI for it now, and 36.0% do not and do not plan to.
   - Security issues: 34.6% use AI for them now.
   - In the last 30 days, 18.9% delegated "changing production" to an agent (n = 13,756), against 72.9% who delegated writing code.
   - On complex tasks (n = 14,341), 16.0% say AI handles them very well, 38.8% good but not great, 16.0% bad, and 8.0% very poor.

4. **Source attribution and freshness**
   - Importance of source attribution when deciding whether to trust an AI-generated technical answer (n = 13,945): 93% rate it at least somewhat important, and 78.6% important or very important.
   - Signals that matter most when relying on work information (n = 12,996):
     - Recent or clearly up to date: 72.6%
     - From an official or trusted source: 60.0%
     - Consistent with other trusted information: 45.9%
     - Includes sources or citations: 37.6%
   - The sources people most want to be able to trace quickly are code repositories (48.1% very important) and official docs (43.7%).
   - 15.9% visit Stack Overflow more in order to verify AI answers (n = 16,985). The blog says this share is down from last year.
   - The blog notes that AI overviews and chatbots reuse community answers without always crediting the people who wrote them.

5. **Missing context**
   - Barriers to getting work context (n = 12,374):
     - Information is incomplete: 63.2%
     - Important context lives in people's heads: 60.9%
     - Information is outdated: 56.5%
     - Spread across too many tools: 53.4%
     - AI tools lack context: 20.0%
     - AI uses the wrong context: 16.8%
   - 78.6% discover important context very often, often or sometimes only after starting or finishing a task (n = 12,687).
   - 75% spend 5+ hours a week looking for information they need, and 11% spend 20+ hours (n = 12,006).
   - Context people say they most need (n = 12,678, up to 5):
     - Project goals or requirements: 85.2%
     - Code, repos or docs: 73.3%
     - Prior decisions and rationale: 44.0%
     - Related tickets: 36.9%
     - Compliance, security or policy requirements: only 19.7%
   - How people manage context (n = 12,039):
     - Keep notes or prompts in a separate doc: 53.9%
     - Start new AI chats to reset context: 45.0%
     - Manually select files for AI tools: 34.7%
   - Jody Bailey (CPTO) said, in substance, that AI is forcing organisations to write down judgment they used to get from people.

6. **Agent first, humans for the local and the unwritten**
   - Actions turned to first for a problem (n = 16,664):
     - Search online: 82.7%
     - Ask an AI agent: 69.9%
     - Search a known repository: 43.7%
     - Message someone I trust: 28.8%
   - Sources for work-specific questions (n = 14,462):
     - Coworkers or teammates: 71.9%
     - Code repositories or comments: 62.7%
     - Internal docs: 60.1%
     - Stack Overflow: 24.0%
   - 22.6% of people who don't post publicly say their questions are too specific to their company or context.
   - 64.1% visit Stack Overflow less for simple questions, and 26.5% contribute less.

7. **Cost and model choice as everyday decisions**
   - What organisations have done (n = 11,468):
     - Set limits on usage or spending: 38.1%
     - Reviewed usage or spending data: 28.3%
     - Approved different tools for different work: 27.2%
     - Limited who can use AI: 25.3%
     - Increased spending because results justified it: 20.6%
   - Individuals (n = 1,033, small sample):
     - Monitor their own use: 32.6%
     - Choose cheaper models when possible: 25.3%
     - Usage is metered: 23.8%
     - More selective about tasks: 16.6%
   - Prompt changes (n = 560, small sample): 75.4% changed prompts to improve quality, 38.4% to reduce cost.
   - Adoption factors (n = 11,462):
     - Useful, accurate results: 30.7%
     - Security or privacy requirements: 28.7%
     - Price acceptable for value: 27.0%
   - Reasons for switching tools (n = 13,144): better output quality 25.1%, organisation required it 10.6%, lower cost 6.4%.

8. **What the tool sees and remembers**
   - Control over the work information AI uses (n = 13,243):
     - I decide exactly: 44.8%
     - I pick from what's available: 19.3%
     - The tool chooses automatically: 10.4%
     - Not sure what it uses: 6.3%
   - Who should control AI memory (n = 12,825): just me 53.6%, no retained memory 14.2%, the organisation centrally 14.7%.
   - 13.0% avoid AI at work over privacy or security (n = 13,857).
   - 10.0% intentionally limit the context they share, for privacy or security.
   - Governance (n = 13,167): 29.7% say AI use is mostly optional and up to individuals; only 24.0% have approved tools and guidance.

9. **Usage scale** (calibration)
   - 65.9% use coding assistants or agents at work, and 73.0% of those use them daily (n = 17,464 and 14,478).
   - 30.9% of daily users spend 4+ hours a day with AI (n = 10,926).
   - Coding agents used in the past year (n = 12,255): Claude Code 65.5%, GitHub Copilot 58.7%, OpenAI Codex 29.5%, Cursor 25.5%.
   - No-code builders (n = 2,219): Lovable 38.3%, Replit 28.3%, v0 27.5%.
   - Reasons for avoiding AI (n = 13,857): 17.1% fear losing job skills or being replaced.
   - 79% are focusing on AI skills, and 52% learned a new coding skill this year.

**Framings it shows are outdated**
- "Developers don't trust AI" (the 2024-25 trust-gap headline). In 2026 most trust it conditionally, by verifiability.
- "Trust in AI tripled." This misreads the 87%-versus-31% comparison.
- "Stack Overflow / search is where you start." 69.9% now also ask an agent first.
- "The AI's answer is the source." Developers want attribution and freshness signals.

**Quote:** none used. The press release's key line is the CEO's: trust has to be earned through transparency, source attribution and rich technical context. It is in the paragraph after the usage figures.

---

## S081: How Much Code Do Developers Really Let Agents Write? (JetBrains Research, Developer Ecosystem Survey 2026)

- **Author:** Mikhail Bogdanov (JetBrains Research)
- **Date:** No date on the page. 2026-08, inferred from the URL path and image upload paths.
- **Sample:** 15,000+ professional developers, surveyed May to July 2026. The sample was reweighted by region, employment, language and JetBrains familiarity. About 90% are in developer, programmer or engineer roles.
- **URL:** https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/

**Summary.** Developers reported what share of last month's work code was:
- fully generated by agents,
- written with AI assistance, or
- written fully by hand.

On average, about 47% was agent-generated, 38% AI-assisted and 27% manual. The answers were given in buckets, so the averages sum to more than 100%. Pure manual coding is now a minority practice. Seniors move to agents first, and juniors stay with AI-assisted work. The shares vary a lot by language, region and tool. All figures are self-reported.

**Gaps and specific points**

- **The baseline has moved:**
  - Over half of developers write less than 20% of their code manually.
  - One in five writes no code without AI help.
  - About 22% are heavy agent users (over 80% of their code agent-generated).
- **Three clusters:**
  - Agentic coders, about 31% of developers: about 84% agent-generated, 15% assisted, 6% manual.
  - AI-assisted coders, about 47%: about 40% agent, 60% assisted, 20% manual.
  - Manual coders, about 23%: about 10% agent, 25% assisted, 75% manual.
- **Seniority:**
  - About a quarter of senior developers generate over 80% of their code with agents.
  - Juniors lean toward AI-assisted rather than fully agentic workflows. No junior figure is given.
- **Language:**
  - Go, JavaScript and TypeScript average 54-55% agent-generated.
  - Java and Python average 48-51%.
  - C and C++ are least agentic, with about 38% written by hand.
- **Region:** 32-35% of developers in China, Japan and South Korea are heavy agent users, against about 16% in Europe and the UK.
- **Tools:**
  - About 32% of Claude Code users and 42% of Codex users generate over 80% of their code with agents.
  - 37% of Codex users write no code without AI.
  - Cursor users average 58% agent-generated code.
  - Only 46-57% of heavy Claude Code and Codex users fall in the "agentic coder" cluster.
- **Caveats the author states:**
  - Self-reports may not be fully accurate.
  - Averages use bucket midpoints.
  - Category averages can exceed 100%.
  - Responses were filtered when their bounds were implausible.
- **Tool figures don't travel between surveys.** JetBrains cites 39% work adoption for Claude Code, from a prior JetBrains post. Stack Overflow (S080) reports 65.5% "used in the past year". These are different samples and different questions. Teach tool popularity as a snapshot, not a fact.

**Framings it shows are outdated**
- "AI suggests the next line; you write the program." For most respondents, agents now generate a large share of the code.
- "Real developers write their own code." The author's takeaway is that purely manual coding is quickly becoming a thing of the past.
- "Tool X is number one." Rankings depend on the survey and are moving.

**Quote:** none used.

---

## S082: Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI

- **Authors:** Emerson Murphy-Hill, Jenna Butler, Alexandra Savelieva (Microsoft)
- **Date:** 2026-07-01 (arXiv v1, the only version). Preprint.
- **URL:** https://arxiv.org/abs/2607.01418 (full text read at https://arxiv.org/html/2607.01418v1)

**Summary.** The paper uses telemetry on tens of thousands of Microsoft engineers during the rollout from 2026-01-05 to 2026-04-29:
- First use spread through social networks.
- Who kept using the tools tracked coding activity more than demographics.
- Adopters merged about 24% more pull requests per engineer per day than a synthetic control predicted, and the lift did not fade over the window.

The authors measure output, not quality. They say outright that a merged PR is not the value it delivers, and that quality is now the open question. A separate survey of 609 self-selected respondents describes who the tools suit and how people use them.

**Gaps and specific points**

- **More output, unknown quality:**
  - The lift was +24.0% PRs per engineer per day (95% CI +14.5% to +33.7%). It was +29.4% in February and +20.0% in March and April.
  - By tool, any use: Copilot CLI +24.9%, Claude Code +11.4%.
  - Lift rises with use, from +15.0% at three days a week to +50.1% at five or more. This is an association only.
  - The authors say merged PRs reward small, frequent PRs and can miss quality costs such as added complexity. The field has no agreed quality measures.
- **Cost:**
  - Token spend can run into millions of dollars a year at organisational scale.
  - Whether the output justifies the cost is a question of value, not throughput.
  - The paper reports no Microsoft spend figures.
- **Who it suits (survey):**
  - Respondents described the tools as a good fit for experienced developers who can break work into smaller chunks for the AI to implement.
  - Some were less convinced juniors could use them as effectively, and worried about how juniors would develop a sense for code.
  - Practices named: small chunks; reviewing output for correctness, completeness and sanity; steering the tool toward the best solution.
- **How work changes:**
  - Respondents describe taking on larger changes they would previously have skipped.
  - They run parallel streams of work.
  - One principal-level developer used to need many clarification prompts per task, and now prompts and switches to another task.
- **Adoption is social:**
  - Skip-level peers at 25%+ usage raised the odds of trying the tool by 216%.
  - A direct manager using it raised the odds by 82%.
  - Senior ICs were more likely to try it, and junior ICs less likely.
- **Validity caveats:**
  - One company and one window.
  - The authors work for Microsoft, which sells these tools.
  - Only Azure DevOps PRs were counted.
  - Adopters self-selected.
  - The survey sample is self-selected.

**Framings it shows are outdated**
- "AI makes you X% more productive, so more output means better results."
- "Merged means done."
- "Tool adoption follows evaluation." In practice, people try what their peers and managers use.

**Quote:** none used. The key line is the conclusion's statement that the open question is now quality: whether the added throughput yields better software.

---

## S083: How AI assistance impacts the formation of coding skills (Anthropic)

- **Authors:** Judy Hanwen Shen and Alex Tamkin
- **Date:** 2026-01-29 (blog). The paper is "How AI Impacts Skill Formation", arXiv 2601.20245, v1 2026-01-28 and v2 2026-02-01.
- **URL:** https://www.anthropic.com/research/AI-assistance-coding-skills

**Summary.** This was a randomized controlled trial with 52 mostly junior engineers. Each had used Python weekly for a year or more, and none had used the Trio async library. They built two features with Trio, with or without an AI assistant that could produce correct code, and then took a quiz.
- **Quiz:** the AI group scored 50% against 67% for hand-coders (Cohen's d = 0.738, p = 0.01). That is about two letter grades.
- **Speed:** the AI group was about two minutes faster, which was not significant.
- **Debugging:** the largest gap was on debugging questions, i.e. recognising when code is wrong and why.
- **How people used AI mattered.** Patterns that kept the participant thinking preserved learning.

**Gaps and specific points**

- **Low-scoring patterns (average quiz under 40%):**
  - **AI delegation:** AI wrote everything. This was the fastest group, with few errors.
  - **Progressive AI reliance:** a question or two at first, then handing over all the code writing.
  - **Iterative AI debugging:** using AI to debug or verify instead of to understand. This group was also slower.
- **High-scoring patterns (65% or higher):**
  - **Generation-then-comprehension:** generate code, then ask follow-up questions.
  - **Hybrid code-explanation:** ask for code together with explanations.
  - **Conceptual inquiry:** ask only conceptual questions and resolve errors yourself. This was the second-fastest pattern overall.
- **Why this matters for oversight.** The authors argue that people must keep learning in order to provide meaningful oversight of AI-generated code. Productivity from AI is not a shortcut to competence, especially in safety-critical domains.
- **Recommendations:**
  - Accept cognitive effort; getting stuck is part of mastery.
  - Managers should deploy AI deliberately, so that engineers keep learning.
  - Use learning-oriented modes: the post names Claude Code's Learning and Explanatory modes and ChatGPT Study Mode.
- **Limits:** a small sample, an immediate quiz only, one library, and the patterns are associations from qualitative analysis.
- **Fit with the course rule.** This does not say "debug by hand at work". The agent should still read and fix its own errors in production work. It says that while you are *learning* something you will have to oversee, letting the AI debug for you costs you the skill of telling when code is wrong.

**Framings it shows are outdated**
- "Learn by fixing errors by hand", as the default workflow (Aaron's correction).
- "Using AI while learning makes you learn faster automatically."
- "Never use AI while learning." Conceptual-inquiry users kept their learning and were nearly as fast as delegators.

**Quote:** none used. The key sentence on effort is in the "For individuals" recommendations.

---

## S084: Agentic Skill Decay

- **Author:** Addy Osmani (engineering leader working on Claude Code at Anthropic)
- **Date:** 2026-08-31
- **URL:** https://addyosmani.com/blog/agentic-skill-decay/

**Summary.** Osmani argues that agents skip the everyday reps that used to build engineering judgment: debugging failures, reviewing others' code, and living with abstractions that break. So mastery now has to be built deliberately. Good agent work rests on four skills, which can be practised. You can ship only what you can verify, and you can ask for only what you can imagine. He still uses agents heavily, and wants his mental model to keep pace with the code they write.

**Gaps and specific points**

- **Four skills to practise:**
  - **Deciding (decision making):** what is worth doing at all.
  - **Specifying:** making the outcome explicit.
  - **Steering:** correcting the agent mid-flight.
  - **Verifying:** deciding when the evidence is good enough.
- **Floor and ceiling.** Verification limits what you can keep. Imagination limits what you can prompt for.
  - His example: the first version of a 3D album site rendered, but used the wrong interaction pattern and performed poorly on mobile.
  - Noticing that took expertise.
- **Plausible code arrives faster than judgment.** This applies especially to someone about three years into their career. Juniors will have to be proactive about learning, and they stop being junior by shipping real things.
- **Code vending machine.** Using AI only to get outcomes can leave you good at prompting but weak at verifying. Use it as a pair that explains instead.
- **Amnesiac new hire.**
  - Each new session is like onboarding a new hire with amnesia: no knowledge of the business, product, team or users.
  - The fix is to turn corrections into durable artifacts: a lessons file, lint rules, type constraints, tests, documentation conventions.
  - Don't rely on chat memory, which compaction can erase.
  - Be selective, and don't over-invest in markdown.
- **How to stay sharp:**
  - Form a hypothesis before prompting.
  - Ask why while the agent works: what it ruled out and what it assumed.
  - Read the diff and predict what could still fail. He calls this the highest-value minute in the loop.
  - Work some problems by hand in areas you are still learning.
  - Ask for explanations, not just results.
- **Evidence over claims.** Prefer evidence you can review, such as tests and screenshots, to a summary that says the task is complete. Keep humans in the loop where correctness, safety or user impact matters.
- **Attention is the bottleneck.** Agent throughput grows faster than his attention. The more agents he runs, the more carefully he must choose where his limited time, taste and judgment go.
- **He cites:**
  - S083.
  - An Anthropic study of about 400,000 Claude Code sessions, in which intermediate task expertise raised the chance of verified success. I did not read that study; treat it as secondary.

**Framings it shows are outdated**
- "Once the agent can do it, you no longer need to understand it."
- "Prompting is the skill." Verifying is the floor.
- "The agent remembers your project." It does not, unless you write things down.

**Quote (exact):** "verification is the floor and imagination is the ceiling"

---

## S085: From Prompting to Verification: How Experience Shapes Vibe Coding Practices

- **Authors:** Ahmed Fawzy, Amjed Tahir, Kelly Blincoe
- **Date:** 2026-05-23 (arXiv v1, the only version)
- **URL:** https://arxiv.org/abs/2605.24521 (full text read at https://arxiv.org/html/2605.24521v1)
- **Companion read:** "A Paradox of AI Fluency", Christopher Potts and Moritz Sudhof, 2026-04-28. https://arxiv.org/abs/2604.25905 (full text: https://arxiv.org/html/2604.25905v1)

**Summary (S085).** A survey of 162 vibe coders: 54 non-developers, 54 novices and 54 professionals, recruited through Prolific.
- **Same awareness.** All three groups see AI code the same way: no significant differences in perceived quality ("fast but flawed", fragile, misleading confidence).
- **Different action.** Practices differ: about 45% of professionals always check code before use, novices mostly check "often", and non-developers are the only group that reports never checking.
- **Re-prompting instead of debugging.** Non-developers re-prompt instead of debugging more than professionals do, and report more QA breakdown and confusion.
- **Perception-action gap.** The authors call this a perception-action gap: awareness of risk is widespread, but the ability to evaluate, debug and verify depends on experience.

**Gaps and specific points (S085)**

- **Checking frequency differs by group** (chi-squared p = .042). The paper gives no exact share for "never".
- **What did not differ:**
  - Skipped QA, run-and-see validation, manual testing and delegating QA to the AI.
  - So all groups run the code and ask the AI to fix it. What differs is whether they can evaluate beyond that.
- **Interaction style:**
  - Non-developers rely more on AI-led generation.
  - Professionals use more interactive dialogue and give richer context.
- **Tools:**
  - Today's tools support generation, not evaluation.
  - The authors propose proactive error surfacing, explanatory support and uncertainty signals, with more scaffolding for novices.
- **Education:**
  - Teach evaluating AI code as a distinct skill: testing outputs, finding edge cases, challenging assumptions, reasoning about behaviour.
  - Teams need explicit verification practices, including human code review.
  - The paper cites prior work on security vulnerabilities and functional defects in AI code. Its own items did not measure security specifically.
- **Limits:**
  - Self-report only.
  - The gap is an interpretation that needs behavioural validation.
  - 74% of matched participants kept the same self-classification over about four weeks.
  - The authors note that re-prompting can sometimes be an efficient strategy.

**Summary (companion, A Paradox of AI Fluency).** The study covers 26,958 English WildChat transcripts from May 2023 to July 2025, annotated by Claude Sonnet 4.5 for fluency.
- **Harder tasks, more failures.** Fluent users take on harder tasks (mean complexity 3.1 against 1.5 on a 5-point scale) and fail more often overall (24% for minimal fluency, 64% for high).
- **Invisible failures.** Fluent users' failures are visible and often partly recovered. Novices' failures are mostly invisible: the conversation seems to succeed but misses what they needed. Invisible failures are 85.6% of minimal-fluency users' failures, against 22.1% for high-fluency users.

**Gaps and specific points (companion)**

- **Named failure types:**
  - **Confidence Trap:** wrong information stated with certainty and accepted.
  - **Silent Mismatch:** the AI addresses a different goal, plausibly enough that nobody flags it.
  - **Walkaway:** the conversation ends unresolved, with no failure signalled. This is most associated with the lowest-fluency users.
  - Also: Drift, Death Spiral (a repetitive loop despite corrections), Contradiction Unravel, Partial Recovery, Mystery Failure.
- **Passive acceptance** is the strongest single marker of low fluency.
  - 93% of high-fluency interactions are augmentative (working the problem with the AI), against under 1% for the lowest fluency.
  - Iterative refinement is characteristic of fluent users and nearly absent among low-fluency users.
- **Recommendations:**
  - Users should engage actively rather than accept passively.
  - Educators should reinforce that AI is not all-knowing.
  - Builders should favour engagement over frictionless experiences.
- **Caveats:**
  - Chat, not agents.
  - Older models (GPT-3.5-turbo to GPT-4.1-mini, GPT-4o and others).
  - Users were anonymous people with free access.
  - LLM-annotated, and correlational.
  - Users' domain expertise was not measured.

**Framings these show are outdated**
- "Knowing AI code can be wrong is enough to stay safe."
- "Vibe coding democratises software." Access widened; the ability to judge did not.
- "If the AI didn't report an error, it worked."
- "Fewer visible failures means you're good at AI." The reverse can be true.

**Quote:** none used, to stay inside the limit. The perception-action gap is defined in the abstract's second-to-last sentence. The Confidence Trap definition is in Appendix B of the companion paper.
