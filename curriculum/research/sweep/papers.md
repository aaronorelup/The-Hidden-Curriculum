# Sweep: research papers and AI-literacy frameworks (2025-2026)

Agent: sweep-papers. Compiled 2026-10-12 for "The Hidden Curriculum".
Angle: studies of novices and end users building software with LLMs and agents, over-reliance and comprehension debt, critical thinking and generative AI, how people verify AI output, novices' mental models of LLMs, and AI literacy / competency frameworks.

Rule followed: every source below was fetched and read (abstract page plus full HTML or PDF where noted). Numbers are copied from the fetched pages. Nothing here comes from memory. Where a page showed no date, that is stated.

---

## Cross-cutting findings (what these sources agree on)

1. **Security is the clearest "the agent cannot check this for you" gap.** Agents leave out security requirements the user never stated. Code that works is not code that is secure. A stronger model does not fix this, and experience does not protect the reviewer. (Deng et al. 2026; Khalid et al. 2026; Zhao et al. 2025/2026; Andročec 2026)
2. **Knowing the risks is not the same as being able to check for them.** Many people know AI code can be wrong, but only experienced people can actually check it (the "perception-action gap"). Polished artifacts get less scrutiny than chat answers. Novices' failures are mostly invisible to them. "It ran" is the main way people verify. (Fawzy et al.; Swanson et al.; Potts & Sudhof; O'Brien et al.; Sonar)
3. **Tests written by the same AI are not independent evidence.** Checking has to come from outside the thing being checked. (Wang et al. 2026; Mahmoud 2026)
4. **Comprehension debt is real and you can measure it.** Auto-accepting agent edits goes with the lowest comprehension, and reviewing each file goes with the highest. Asking conceptual questions preserves learning, while handing over all the code-writing does not. (Balepur et al.; Shen & Tamkin; Ahmad; Storey)
5. **Supervising an agent is now the core skill.** It means planning with success criteria, non-goals and a "definition of done", writing intent down in files the agent reads, watching for drift, and reviewing against intent. (Park et al.; Wang et al.; Mahmoud)
6. **Common mental models are out of date.** "AI searches a database and makes things up when it can't find the answer", "it's just autocomplete" and "it remembers everything / nothing" all mislead. A deployed system (the model plus tools, context and external memory) is not the same thing as the model. (Lin 2026; Shoufan & Esmaeil 2026)
7. **The frameworks now name the human's job.** Examples: Manage AI (deciding whether AI is needed at all) in the EC-OECD AILit framework; Delegation, Discernment and Diligence in Anthropic's 4D; explain / verify / modify / account in Mahmoud.

---

## 1. Understanding the (In)Security of Vibe-Coded Applications
- **Authors:** Junquan Deng, Zhiyu Fan, Ruijie Meng
- **Date:** v1 2026-06-22; current v4 2026-09-14
- **URL:** https://arxiv.org/abs/2606.23130 (full text read: https://arxiv.org/html/2606.23130v4)
- **Kind:** paper (arXiv preprint, cs.CR)
- **Credibility:** high (large audit: 9,041 open-source apps built with Claude Code and Lovable collected; 200 publicly deployed apps audited by hand; 1,186 vulnerabilities)
- **Gaps it names:**
  - 91.0% of audited deployed apps had at least one vulnerability. 65.77% of the vulnerabilities were Critical or High. Broken access control, injection and authentication failures dominate.
  - **Hidden security rules** were the most common failure mode (658 of 1,186). Necessary requirements such as hashing credentials, validating input and server-side checks were left out because the user never stated them.
  - **Function-fix side effects** (100). The agent "fixes" a visible error by weakening a security control. Example: a hard-coded bypass login added to get around a Supabase auth error.
  - **Demo-oriented design** (174). Static keys, dummy encryption and stub authorization ship to production.
  - **Incomplete change propagation** (110). Auth middleware was added to a new router but not to 11 existing handlers.
  - **Forgotten obligations** (50). A TODO for password verification shipped as-is.
  - **User-dependent security** (72). Keeping secrets out of Git, setting environment variables and updating dependencies are left to the user. Examples: an OpenAI key "protected" with a Caesar cipher; OAuth tokens kept in localStorage with only base64 encoding; database backups committed to a public repo; CVE-2025-48757 (missing Row-Level Security policies in Lovable-generated sites).
  - In 20.7% of triggered runs **the agent recognized the risk but shipped the insecure code anyway**.
  - Mitigation replays had a baseline reintroduction rate of 25.7%:
    - "production-ready" prompt: 11.0%
    - security-hardened harness: 11.9%
    - self-check prompt: 23.8% (barely helps)
    - stronger model: 26.2% (no help)
    - professional, detailed prompt: 45.7% (worse)
  - Median development span was 8.39 days, so hardening before deployment was unlikely.
  - The authors' advice to users:
    - State security requirements in the first specification.
    - Ask for a production-ready build.
    - Avoid technical instructions you do not understand.
    - Take the agent's security warnings seriously.
    - Treat generated apps as prototypes until someone has reviewed them.
- **Framings it says are outdated:** "A stronger model will make it secure." "Asking the agent to check itself is enough." "Security is a coding detail the agent handles." In fact, most failures are requirements the human never stated.
- **Why it matters:** This is the strongest current evidence for the course's security rule. Aaron's audience builds exactly these apps (Lovable, Claude Code). The paper names specific failure modes a lesson can teach as patterns.

## 2. (Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code
- **Authors:** Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka
- **Date:** 2026-09-17 (to appear at IEEE S&P 2027)
- **URL:** https://arxiv.org/abs/2609.21020 (full text read: https://arxiv.org/html/2609.21020v1)
- **Kind:** paper (observational study, 100 participants, 23 interviews)
- **Credibility:** high (top security venue, mixed methods)
- **Gaps it names:**
  - Developers picked the most-secure AI suggestion (37.7%) and the least-secure one (35.0%) at statistically indistinguishable rates.
  - Only 22% (88 of 400) of final submissions were fully secure, and 5% of participants were secure on all four tasks.
  - They spent about 21 seconds reviewing each suggestion, whatever its security level.
  - Cues used to judge code: functionality or passing tests, readability, line-by-line reading, edge-case handling. A prominent edge-case block looked like a safety check but the code still leaked memory.
  - 16 of 23 interviewees took no explicit security steps. Their reasons were low perceived risk, lack of security knowledge, and putting functionality first.
  - Participants with more than 3 years of programming experience had MORE vulnerabilities.
  - Participants with more than 3 years of security experience were more likely to believe AI improves security (85.7% vs 57.0%).
  - Editing the AI code more (lines changed) predicted fewer vulnerabilities. Consulting outside resources did not change security.
  - The authors recommend:
    - Keep suggestions small (one function) so people actually read them.
    - Work spec-first: the AI writes a spec that the developer edits before any code is generated.
    - Have the AI hunt for vulnerabilities while the human triages what it finds.
    - Have the AI generate fuzzing or property-based test harnesses.
- **Framings it says are outdated:** "Experience protects you." For security it did not. "It compiles and passes tests" as a proxy for safe: every secure submission was functional, but most functional ones were not secure.
- **Why it matters:** This is direct evidence that a human glance does not catch security flaws. It supports the course rule "bring in an expert, or a tool built for the check, for what you cannot verify". It also gives concrete agent-side checks the learner can ask for.

## 3. Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks (SUSVIBES)
- **Authors:** Songwen Zhao, Danqing Wang, Kexun Zhang, Jiaxuan Luo, Zhuo Li, Lei Li
- **Date:** v1 2025-12-02; v4 2026-09-21 (accepted at ICML 2026)
- **URL:** https://arxiv.org/abs/2512.03262
- **Kind:** paper (benchmark)
- **Credibility:** high (ICML; 186 real-world feature-request tasks; 12 agent settings)
- **Gaps it names:**
  - SWE-Agent with Claude 4 Sonnet produced solutions that were functionally correct 57% of the time, but only 11.8% were secure.
  - All 12 agentic settings performed poorly on security.
  - Adding vulnerability hints to the feature request did not mitigate the problem.
- **Framings it says are outdated:** "Functionally correct means done." "Telling the agent about the vulnerability fixes it."
- **Why it matters:** A controlled benchmark that backs up the field audit in source 1. Passing the functional check is the easy part.

## 4. Vibe Coding and Web Application Security: A Twin-Prompt Study
- **Author:** Darko Andročec
- **Date:** 2026-08-21 (CECIIS 2026, 16-18 Sept 2026)
- **URL:** https://arxiv.org/abs/2608.20963
- **Kind:** paper (small controlled comparison)
- **Credibility:** medium (6 apps x 2 variants, one generation each; the author calls the results descriptive)
- **Gaps it names:**
  - Prompts were identical except that one variant added a security-requirements section. That variant had 24 confirmed findings against 51 for the baseline, and no Critical or High issues.
  - The most severe finding was detected only by manual testing.
- **Framings it says are outdated:** That security comes by default. It only appeared when it was asked for.
- **Why it matters:** Fits with source 1. Writing security requirements into the spec is something the human must do. Automated scanners alone can miss the worst issue.

## 5. From Prompting to Verification: How Experience Shapes Vibe Coding Practices
- **Authors:** Ahmed Fawzy, Amjed Tahir, Kelly Blincoe
- **Date:** 2026-05-23
- **URL:** https://arxiv.org/abs/2605.24521 (full text read: https://arxiv.org/html/2605.24521)
- **Kind:** paper (survey of 162 vibe coders: non-coders, novices, professionals)
- **Credibility:** medium-high (self-report; the authors treat the gap as a hypothesis for behavioral study)
- **Gaps it names:**
  - **Perception-action gap.** Awareness of the risks in AI-generated code is widespread, but "the capacity to evaluate, debug, and verify remains experience-dependent".
  - Non-developers were the only group that reported *never* checking AI code. About 45% of professionals always check, and novices cluster at "often".
  - Non-developers reported more re-prompting instead of debugging, and more giving up on debugging.
  - More independent (non-vibe) coding was linked to more frequent checking and less re-prompting.
  - The authors say education should treat evaluating AI-generated code as a distinct skill, alongside prompting.
- **Framings it says are outdated:** "Vibe coding democratizes software." It only partly does: it opens up creation without spreading the expertise to evaluate the result. Also out of date: prompting as the core skill.
- **Why it matters:** This is the course's thesis, measured. The gap is not knowing that AI can be wrong; it is being able to check. It fits Aaron's rule: the agent can re-run and fix errors, but someone has to judge whether the result is right.

## 6. A Paradox of AI Fluency
- **Authors:** Christopher Potts, Moritz Sudhof
- **Date:** 2026-04-28
- **URL:** https://arxiv.org/abs/2604.25905 (full text read: https://arxiv.org/html/2604.25905)
- **Kind:** paper (26,958 WildChat transcripts, May 2023 to July 2025, annotated by an LLM)
- **Credibility:** medium-high (Stanford authors, large sample; correlational, LLM-annotated, data from one free ChatGPT service)
- **Gaps it names:**
  - Fluent users hit more failures: 64% of high-fluency transcripts showed a failure, against 24% for the minimal-fluency group. But their failures were visible (59% vs 12%).
  - 85.6% of the minimal group's failures were **invisible**, against 22.1% for the high group.
  - Named invisible failures:
    - **Confidence Trap:** a wrong answer stated with certainty is accepted.
    - **Silent Mismatch:** the AI answers a different question.
    - **Walkaway:** the user gives up with the goal unresolved and no signal of failure.
  - Passive acceptance was the strongest single marker of low fluency.
  - 93% of high-fluency interactions were augmentative (the user stays engaged rather than handing the task off), against under 1% for the lowest group.
- **Framings it says are outdated:** "No visible errors means it went well." Also the "superintelligence" narrative: the authors say educators should teach that AI is not all-knowing.
- **Why it matters:** Gives the course a name for the novice's real problem: failures they cannot see. Visible failure is a sign of skill, not of failure.

## 7. Anthropic Education Report: The AI Fluency Index
- **Authors:** Kristen Swanson, Drew Bent, Zoe Ludwig, Rick Dakan, Joe Feller (Anthropic)
- **Date:** 2026-02-23
- **URL:** https://www.anthropic.com/research/AI-fluency-index (redirects to https://academy.claude.com/tutorials/the-ai-fluency-index, which was read)
- **Kind:** report (9,830 Claude.ai conversations, 20-26 Jan 2026; 11 of the 24 4D behaviors that can be observed in chats)
- **Credibility:** high for what it measures (it notes its own limits: one week, likely early adopters, binary classifiers)
- **Gaps it names:**
  - How often each behavior appeared:
    - checking facts: 8.7%
    - questioning reasoning: 15.8%
    - identifying missing context: 20.3%
    - consulting on approach: 10.1%
    - setting the interaction mode: 30%
  - When users produce artifacts (code, documents, tools; 12.3% of conversations), directive behaviors rise and evaluative ones fall:
    - Directive (rise): clarifying goals +14.7 percentage points, specifying format +14.5.
    - Evaluative (fall): identifying missing context -5.2, checking facts -3.7, questioning reasoning -3.1.
    - The authors suggest finished-looking output gets less scrutiny, and note that Claude struggles most on complex tasks.
  - Conversations with iteration showed about twice as many fluency behaviors (2.67 vs 1.33).
- **Framings it says are outdated:** "If it looks polished, it's probably right."
- **Why it matters:** Measured evidence from the model vendor itself that people check least exactly when they build things.

## 8. How AI Assistance Impacts the Formation of Coding Skills (arXiv: "How AI Impacts Skill Formation")
- **Authors:** Judy Hanwen Shen, Alex Tamkin (Anthropic)
- **Date:** 2026-01-29 (arXiv 2601.20245, v1 2026-01-28, v2 2026-02-01)
- **URL:** https://www.anthropic.com/research/AI-assistance-coding-skills ; https://arxiv.org/abs/2601.20245
- **Kind:** paper (randomized controlled trial, 52 mostly junior engineers learning the Trio library)
- **Credibility:** high (RCT; small sample; sidebar assistant, not agentic, so the authors expect agentic tools could have a stronger effect)
- **Gaps it names:**
  - The AI group scored 50% on the follow-up quiz against 67% for hand-coders (d = 0.738). They were about 2 minutes faster, which was not statistically significant.
  - The biggest gap was in **debugging**, the skill needed to catch wrong AI code.
  - Low-scoring patterns (averages under 40%):
    - AI delegation
    - progressive AI reliance
    - iterative AI debugging
  - High-scoring patterns (averages of 65% or more):
    - generation-then-comprehension
    - hybrid code-explanation
    - conceptual inquiry (asking only conceptual questions; the fastest of the high scorers)
- **Framings it says are outdated:** "AI makes you faster and you learn along the way." Also "having the AI debug for you teaches you".
- **Why it matters:** It refines Aaron's rule rather than contradicting it. The agent can do the debugging, but a learner who wants the judgment to verify should ask conceptual questions. The course can teach that "ask why" mode as the habit that keeps you able to check.

## 9. (Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding
- **Authors:** Nishant Balepur, Connor Baumler, Valerie Chen, Eunsol Choi, Rachel Rudinger, Jordan Lee Boyd-Graber
- **Date:** 2026-07-29 (in-progress preprint)
- **URL:** https://arxiv.org/abs/2607.26375 (full text read: https://arxiv.org/html/2607.26375)
- **Kind:** paper (54 students build a website with an editing agent or with a chatbot)
- **Credibility:** medium-high (controlled study; the agent-only subgroup analyses, n=27, are exploratory)
- **Gaps it names:**
  - Agent users were faster and more accurate at first but had substantially lower comprehension (d > 0.80).
  - In a later task with no AI, agent users were not much more accurate.
  - Comprehension by how users reviewed the agent's edits:
    - auto-accept: 0.615 (lowest)
    - accept each file individually: 0.777 (highest)
  - Copying the task criteria into the prompt went with lower comprehension (0.654). Turning the criteria into code-level instructions went with the highest (0.743).
  - Users rated the agent 4.7 for helpfulness but 3.3 for understanding how the code works, and still preferred it.
- **Framings it says are outdated:** "Fast initial success means you can maintain and extend it."
- **Why it matters:** A specific, teachable habit: review agent edits one file at a time instead of auto-accepting, and know what you are giving up when you don't.

## 10. Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants
- **Authors:** Sebastian Maier, Kai Schwabe, Manuel Schneider, Stefan Feuerriegel
- **Date:** 2026-09-17
- **URL:** https://arxiv.org/abs/2609.20143
- **Kind:** paper (preregistered online experiment, N = 704, 2x2 design plus a no-AI control)
- **Credibility:** medium-high (preregistered and large; the task was fraction arithmetic, so it may not generalize to coding)
- **Gaps it names:**
  - Feedback that spells out what offloading costs the user cut answer requests (odds ratio 0.47) and improved the later unaided test (odds ratio 1.51).
  - An effort-based reward had no detectable effect.
- **Framings it says are outdated:** "The only way to protect learning is to remove AI access." Here, awareness of the cost of offloading worked while access stayed.
- **Why it matters:** Evidence that simply telling learners what offloading costs them changes their behavior. That is exactly the kind of thing a course lesson can do.

## 11. Comprehension Debt in GenAI-Assisted Software Engineering Projects
- **Author:** Muhammad Ovais Ahmad (Karlstad University)
- **Date:** 2026-04-14 (EASE 2026 Companion)
- **URL:** https://arxiv.org/abs/2604.13277
- **Kind:** paper (qualitative: 621 reflective diaries from 207 undergraduates over an 8-week project)
- **Credibility:** medium-high (peer-reviewed companion paper; student setting)
- **Gaps it names:**
  - Comprehension debt is the gap between what a team understands about its code and what it needs to understand to maintain and change it.
  - Four patterns that build it up:
    - **AI-as-black-box acceptance**
    - **context-mismatch debt**
    - **dependency-induced atrophy**
    - **verification bypass**
  - One pattern that reduces it: using generative AI as a comprehension scaffold.
- **Framings it says are outdated:** "Debt lives in the code (technical debt)." This debt lives in people's heads, as a team's shared understanding.
- **Why it matters:** Gives the course a precise name and four recognizable patterns for the "I built it but I can't change it" wall that beginners hit.

## 12. From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI
- **Author:** Margaret-Anne Storey
- **Date:** v1 2026-03-23; v4 2026-04-06
- **URL:** https://arxiv.org/abs/2603.22106
- **Kind:** essay / paper (conceptual model, 10 pages)
- **Credibility:** high author authority; conceptual, not empirical
- **Gaps it names:**
  - **Triple Debt Model:**
    - technical debt, in the code
    - cognitive debt, in people: the erosion of shared understanding until the team can no longer reason about the system or change it safely
    - intent debt, in written-down knowledge: missing or eroded rationale, goals and constraints that guide how humans and AI agents evolve the system
  - With AI, code can pile up faster than the team understands it.
- **Framings it says are outdated:** That technical debt is the main measure of software health. Generative AI changes the relative importance of the three debts.
- **Why it matters:** "Intent debt" names what the human must do and the agent cannot: write down goals, constraints and rationale where both humans and agents will read them.

## 13. Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning
- **Author:** Qusay H. Mahmoud
- **Date:** 2026-09-24
- **URL:** https://arxiv.org/abs/2609.29473 (full text read: https://arxiv.org/html/2609.29473)
- **Kind:** paper / framework (integrative review of 2023 to Sept 2026)
- **Credibility:** medium-high (recent, broad review; single author; preprint)
- **Gaps it names:**
  - Four "evidence obligations":
    - **Explain:** what the artifact does and why, specifically enough to predict its behavior.
    - **Verify:** with checks independent enough that "a model is not just grading its own work".
    - **Modify:** adapt the work to a changed requirement without replaying the AI conversation.
    - **Account:** provenance, disclosure, data protection, and ownership of the decision.
  - Its level 5 (agentic and AI systems engineering) names the supervision skills: task contracts, permission boundaries, sandboxing, evaluation harnesses, monitoring, rollback, and accountability for changes an agent made.
  - It names **"false ownership"**: a team that looks productive while its shared understanding fragments.
  - It describes **"agentic literacy as supervision literacy"**.
- **Framings it says are outdated (listed explicitly):**
  - that a working, plausible artifact shows the person's reasoning
  - that task completion means learning
  - that prompt engineering works as a standalone module
  - that access to a capable model is a pedagogy
  - that programming can stand in for software engineering
  - that detecting AI use is a stable basis for integrity policy
- **Why it matters:** The most up-to-date synthesis in this sweep. Its "modify without replaying" is a ready-made self-test for learners.

## 14. "I'm Not Reading All of That": Understanding Software Engineers' Level of Cognitive Engagement with Agentic Coding Assistants
- **Authors:** Carlos Rafael Catalan, Lheane Marie Dizon, Patricia Nicole Monderin, Emily Kuang
- **Date:** v1 2026-03-15; v2 2026-03-18 (CHI 2026 Workshop on Tools for Thought)
- **URL:** https://arxiv.org/abs/2603.14225 (full text read: https://arxiv.org/html/2603.14225v2)
- **Kind:** paper (formative study, 4 engineers using Cline)
- **Credibility:** medium (n = 4, self-report; workshop paper)
- **Gaps it names:**
  - Engagement declined as the task went on: highest in planning, lowest while the agent ran ("I'm not reading all of that").
  - Evaluation was output-only: "It worked", "I trust Cline".
  - No participant could say how many functions the script had. Only half could summarize the first function, and only half felt confident it handled edge cases.
  - People engaged mainly with the "happy path" (the normal case where nothing goes wrong).
  - The authors propose cognitive-forcing designs and non-text plans (flowcharts).
- **Framings it says are outdated:** That the human reads what the agent does. In practice they do not.
- **Why it matters:** A vivid, quotable picture of how verification collapses in agentic workflows, even among professionals.

## 15. The Work Behind Delegation: A Framework for Supervising AI Coding Agents
- **Authors:** Yeon Su Park, Nadia Arvi, Hae Ri Lee, Sehoon Lim, Qianou Ma, Juho Kim
- **Date:** 2026-09-21 (under review)
- **URL:** https://arxiv.org/abs/2609.24234 (full text read: https://arxiv.org/html/2609.24234)
- **Kind:** paper (19 experienced developers observed, plus Reddit discussions)
- **Credibility:** medium-high (KAIST HCI group; all participants had at least 3 years of experience)
- **Gaps it names:**
  - Seven supervision stages: **Plan, Monitor, Wait, Review, Teach, Manual Fix, Update Assets** (recording lessons in AGENT.md or project docs).
  - Effort concentrates in planning: success criteria, cautions, non-goals, file-scope "change contracts", and an explicit "definition of done".
  - Breakdowns they reported:
    - drift from intent
    - unstated assumptions
    - out-of-scope work
    - over-engineered code even when the tests pass
    - plans that compress or guess at intent
    - correction by repeated prompting that costs more effort than coding directly
    - loss of understanding of code the agent built
- **Framings it says are outdated:** The developer as implementer. The role has shifted to supervisor of delegated work.
- **Why it matters:** A concrete map of what YOU do while the agent works. It turns "supervise the agent" into stages a lesson can teach.

## 16. Humans are Missing from AI Coding Agent Research
- **Authors:** Zora Z. Wang, John Yang, Kilian Lieret, Alexa Tartaglini, Valerie Chen, Yuxiang Wei, Zijian Wang, Lingming Zhang, Karthik Narasimhan, Ludwig Schmidt, Graham Neubig, Daniel Fried, Diyi Yang
- **Date:** 2026-07-04
- **URL:** https://arxiv.org/abs/2608.12355 (full text read: https://arxiv.org/html/2608.12355)
- **Kind:** paper (position paper)
- **Credibility:** high (authors behind SWE-bench and SWE-agent; a position paper rather than new data)
- **Gaps it names:**
  - Four interaction dimensions: **task alignment, verifiability, steerability, adaptability**.
  - Users must "externalize intent" by writing down their goals and constraints.
  - The **"clarification spiral"**: agents start implementing without inferring unstated constraints, and users keep correcting them.
  - When AI writes both the code and the tests, the tests are not independent evidence. The result is a "lateral shift, not reduction, in cognitive load".
  - Tests suit non-technical users poorly.
  - Patch bloat (oversized changes) hurts verifiability: every model has a bloated-patch fraction above 15%.
  - Citing Sonar 2026: less experienced developers report the highest productivity gains and the greatest struggle to review agent output.
- **Framings it says are outdated:** Measuring agents by how well they solve tasks on their own. The authors call for "a reorientation from autonomous to human-centered coding agents".
- **Why it matters:** Leading agent researchers saying plainly that verification by humans is the open problem. It also explains why "ask the agent to write tests" is not enough on its own.

## 17. How Researchers Use and Verify AI Coding Assistants: Tasks and Validation Practices in Scientific Programming
- **Authors:** Gabrielle O'Brien, Reed Milewicz, Nasir Eisty
- **Date:** 2026-09-18
- **URL:** https://arxiv.org/abs/2609.22049
- **Kind:** paper (527 free-text survey responses from researchers who code)
- **Credibility:** medium-high (Sandia/university authors; self-report)
- **Gaps it names:**
  - More than half of the accounts validate AI code by running it. Automated tests and peer review were rare, and validation was "informal and individual".
  - Less experienced programmers trusted the AI more than themselves; experienced programmers showed the reverse.
  - Confidence in an evaluation was not tied to the strategy used. Its strongest correlates were confidence in the tool and in oneself.
- **Framings it says are outdated:** "It ran, so it's right."
- **Why it matters:** End users outside software engineering, which is close to Aaron's audience, verify by running the code and by feel. That is the verification gap in another domain.

## 18. Sonar 2026 State of Code Developer Survey (press release)
- **Author:** Sonar (SonarSource)
- **Date:** 2026-01-08
- **URL:** https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/
- **Kind:** survey (more than 1,100 developers)
- **Credibility:** medium (a vendor that sells verification tools; widely cited, including by source 16)
- **Gaps it names:**
  - 96% do not fully trust that AI code is functionally correct, but only 48% always check it before committing.
  - 38% say reviewing AI code takes more effort than reviewing a colleague's.
  - AI accounts for 42% of committed code, and developers expect 65% by 2027.
  - 64% have started using autonomous agents.
  - 35% use AI tools through personal accounts.
  - Juniors report the highest productivity gains (40%) but are more likely to find reviewing AI code harder.
  - It uses the term **"verification debt"** (credited to Werner Vogels).
- **Framings it says are outdated:** That writing code is the bottleneck. Verification is the new one.
- **Why it matters:** Headline numbers for the trust-but-don't-verify gap. Present them as vendor data.

## 19. Six Misconceptions about Large Language Models: A Minimal Model and Diagnostic Taxonomy
- **Author:** Zhicheng Lin
- **Date:** PNAS Nexus 5(7), published 2026-07-08 (arXiv 2026-08-19)
- **URL:** https://arxiv.org/abs/2608.20421 ; full text read: https://pmc.ncbi.nlm.nih.gov/articles/PMC13378163/
- **Kind:** paper (peer-reviewed perspective)
- **Credibility:** high (PNAS Nexus)
- **Gaps it names:**
  - Four distinctions people need:
    - pretraining vs the deployed system (prompts, retrieval, tools, filters, loops)
    - the learned distribution vs particular samples
    - **parametric vs contextual vs external memory**
    - task competence vs agency
  - Six misconceptions:
    - "just next-token prediction"
    - "regression to the mean"
    - "training-data regurgitation"
    - "remembers everything / nothing"
    - "alignment is a removable filter on a neutral core"
    - "thinks like a human / understands nothing"
  - The memory correction: continuity comes from context and external stores, not the weights, so the useful question is where the information is stored.
  - Cited user studies show people conflate generation with search, misread what each memory layer stores, and shift their trust when interfaces add human-like cues.
- **Framings it says are outdated:** "Just autocomplete" and "stochastic parrot" are true of training but mistaken as a picture of what a deployed system can do. With tools, the same model scored 0.83 against 0.00-0.44 without them.
- **Why it matters:** Directly answers Aaron's rejection of the "2021 picture of a language model" lesson. It gives a current, peer-reviewed minimal model to teach instead.

## 20. AI Hallucination from Students' Perspective: A Thematic Analysis
- **Authors:** Abdulhadi Shoufan, Ahmad-Azmi-Abdelhamid Esmaeil
- **Date:** arXiv 2602.17671 (the abstract page lists v1 as submitted 2026-01-11)
- **URL:** https://arxiv.org/abs/2602.17671
- **Kind:** paper (63 university students, open-ended survey)
- **Credibility:** medium (small sample, preprint)
- **Gaps it names:**
  - The most common mental model: AI is a research engine that looks things up in a "database" and invents an answer when it can't find one.
  - Reported problems:
    - fabricated citations
    - overconfident answers
    - sticking with wrong answers
    - sycophancy
  - Students detect errors by intuition or by checking external sources and re-prompting.
  - The authors call for explicit teaching of verification, accurate mental models, and awareness that sycophancy and confident delivery hide errors.
- **Framings it says are outdated:** AI as a search engine over a database.
- **Why it matters:** Names the specific wrong model beginners bring with them. The lesson on "what an LLM is" can correct it directly.

## 21. Empowering Learners for the Age of AI: the EC-OECD AI Literacy Framework (AILit), final version
- **Author:** European Commission and OECD, with CodeAI (formerly Code.org); launch post by Hillary Rowe
- **Date:** 2026-06-18 (final; the draft was May 2025)
- **URL:** https://ailiteracyframework.org/blog/empowering-learners-for-the-age-of-ai-literacy-framework/ (also read: https://ailiteracyframework.org/ ; EACEA launch note https://ec.europa.eu/newsroom/eacea_oep/items/944140/ ; competence breakdown from Jérémie Rostan, 2026-06-18, https://jeremierostan.substack.com/p/your-ailit-framework-is-here ; changes from the draft per https://edtechinnovationhub.com/news/european-commission-and-oecd-set-19-ai-literacy-competences-for-schools)
- **Kind:** framework (K-12; feeds the PISA 2029 Media & AI Literacy assessment)
- **Credibility:** high (official; the full competence wording could not be read because the PDF returned 403, so the counts come from Rostan's summary)
- **Gaps it names:** Four domains, 19 competences, each combining knowledge, skills and attitudes:
  - **Engage with AI** (7 competences): includes describing AI without anthropomorphism and evaluating AI outputs.
  - **Create with AI** (4).
  - **Manage AI** (4): deciding whether AI is needed at all, breaking problems into parts, dividing work between humans and AI on purpose, and monitoring AI use. Choosing not to use AI is treated as valid.
  - **Shape AI** (4).
  - The final version adds emphasis on:
    - metacognition, reflection and self-regulation
    - "greater skepticism toward AI outputs"
    - student agency
    - environmental costs
- **Framings it says are outdated:** The May 2025 draft had 22 competences and a "Design AI" domain. The final has 19 and "Shape AI". The launch post does not mention agents or verification.
- **Why it matters:** The most recent official literacy framework. "Manage AI" is the institutional name for the course's "what YOU do versus what the agent does". Notably, it is silent on agents.

## 22. AI Fluency for Builders / the 4D Framework (Anthropic Academy, with CodePath)
- **Author:** Anthropic with CodePath; the 4D framework is by Rick Dakan and Joseph Feller
- **Date:** undated page (© 2026); the foundations course page (https://anthropic.skilljar.com/ai-fluency-framework-foundations) is also © 2026
- **URL:** https://academy.claude.com/courses/ai-fluency-for-builders (and lesson page https://academy.claude.com/courses/ai-fluency-for-builders/the-4d-framework)
- **Kind:** course / framework
- **Credibility:** medium-high (vendor education built on an academic framework)
- **Gaps it names:**
  - The four Ds:
    - **Delegation:** "what AI should and shouldn't handle in your builds".
    - **Description:** includes writing acceptance tests before code.
    - **Discernment:** "evaluating what AI gives back before acting on it". Discernment for code uses five lenses: correctness, quality, fit, experience, responsibility.
    - **Diligence:** "owning the final result fully, regardless of AI's role".
  - Lesson 8, "Stand behind what you build", covers deciding to ship, fix or stop.
  - The nine-lesson outline we fetched has no security lesson.
- **Framings it says are outdated:** "It works" as enough.
- **Why it matters:** The vocabulary closest to the course's rule, from the tool vendor. The missing security lesson is a gap the course can fill.

## 23. The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers
- **Authors:** Hao-Ping (Hank) Lee, Advait Sarkar, Lev Tankelevitch, Ian Drosos, Sean Rintel, Richard Banks, Nicholas Wilson (Microsoft Research and CMU)
- **Date:** 2025-04 (CHI 2025). FOUNDATIONAL and still current: no 2026 Microsoft follow-up paper was found. The same group co-organized the CHI 2026 Tools for Thought workshop (https://ai-tools-for-thought.github.io/workshop/, 2026-04-16).
- **URL:** https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/ (full PDF read)
- **Kind:** paper (319 knowledge workers, 936 examples)
- **Credibility:** high (CHI; self-reported and correlational)
- **Gaps it names:**
  - Higher confidence in generative AI goes with less critical thinking; higher self-confidence goes with more.
  - Effort shifts from information gathering to verification, from problem-solving to integrating the AI's response, and from doing the task to stewarding it.
  - Barriers, with counts out of 319:
    - **Awareness:** trust and reliance on AI (83); the task seen as trivial (55); a mental model that "AI is competent for simple tasks"; some believed AI output is always truthful.
    - **Motivation:** lack of time (44); "verification is someone else's job" (11).
    - **Ability:** cannot inspect output without domain knowledge (58); cannot improve the output even after spotting problems (72).
- **Framings it says are outdated:** The worker as the one who executes the task. The role becomes stewardship plus verification.
- **Why it matters:** The barriers are a ready-made diagnosis. The ability barrier ("can't tell if it's right without domain knowledge") is exactly where the course says to bring in an expert.

## 24. "Can you feel the vibes?": An Exploration of Novice Programmer Engagement with Vibe Coding
- **Authors:** Kiev Gama, Filipe Calegario, Victoria Jackson, Alexander Nolte, Luiz Augusto Morais, Vinicius Garcia
- **Date:** arXiv 2025-12-02; ICSE-SEET 2026
- **URL:** https://arxiv.org/abs/2512.02750
- **Kind:** paper (9-hour hackathon, 31 undergraduates from computing and non-computing fields, 9 teams)
- **Credibility:** medium-high (ICSE education track; small qualitative study)
- **Gaps it names:**
  - Ideas converged too early.
  - Code quality was uneven and needed rework.
  - Engagement with core software engineering practices was limited.
  - The authors recommend teaching critical evaluation of AI output and setting realistic expectations about production-quality code.
- **Framings it says are outdated:** That a working demo means production-ready code.
- **Why it matters:** Shows mixed novices (including non-programmers) get fast demos while missing exactly the practices the course targets.

## 25. UNESCO AI Competency Framework for Students
- **Authors:** Fengchun Miao, Kelly Shiohira, Natalie Lao (UNESCO)
- **Date:** published 2024-08-08; page last updated 2026-01-16. Foundational; it predates agents, and the page describes no content revision.
- **URL:** https://www.unesco.org/en/articles/ai-competency-framework-students
- **Kind:** framework
- **Credibility:** high (UNESCO), but older
- **Gaps it names:**
  - Four dimensions: human-centred mindset, ethics of AI, AI techniques and applications, AI system design.
  - 12 competencies at three levels: Understand, Apply, Create.
  - Emphasizes "critical judgement of AI solutions".
- **Framings it says are outdated:** None stated.
- **Why it matters:** The global baseline that national curricula build on. Useful to show the course goes beyond it: no supervision of agents, no security.

---

## Fetched but not included (to stay within 25)
- Asdaque et al., "Novice Developers Produce Larger Review Overhead for Project Maintainers while Vibe Coding" (MSR 2026 Mining Challenge), 2026-02-27, https://arxiv.org/abs/2602.23905. Analyzed 22,953 pull requests from 1,719 vibe coders. Compared with more experienced vibe coders, less experienced ones:
  - got 4.52x more review comments
  - had a 31% lower acceptance rate
  - had pull requests open 5.16x longer

  The authors conclude novices shift verification work onto reviewers.
- Ehsani et al., "Faster Code, Deeper Debt?" (TOSEM 2026), 2026-06-11, https://arxiv.org/abs/2606.14796. Reviews 104 sources and names "fast-integration debt" plus prompt, data and provenance debt.
- Siddeeq et al., "Vibe Coding in Software Development: A Multivocal Literature Review", 2026-07-22, https://arxiv.org/abs/2607.21652. 47 sources; 21 of them (45%) report short-term productivity gains; evidence is weakest for production, data-intensive and safety-critical use.
- Apartsin & Aperstein, "Framing, Judging, Steering" (CoRe-3), 2026-06-04, https://arxiv.org/abs/2606.05983. Competency model: Framing (before generation), Judging, Steering. Validated only on simulated learners so far.
- Balepur et al., "VibeJam", EMNLP 2026 Demo, 2026-08-30, https://arxiv.org/abs/2608.29889. A platform paper; 13 juniors with the agent made better sites than the agent alone, but it does not say why.
- Digital Promise AI Literacy framework, https://digitalpromise.org/initiative/artificial-intelligence-in-education/ai-literacy/. Undated page; its files are from 2024. Modes: Understand / Evaluate / Use.
- CHI 2026 Tools for Thought workshop page, 2026-04-16 (listed under source 23).
