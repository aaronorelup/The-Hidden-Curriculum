---
key: working-is-not-secure
id: 04.01
title: Working is not secure
district: Going Live
module: 04 Safe for strangers
status: todo
legacy: []
minutes: [5, 6]
concepts: [C007, C062, C064, C065]
sources: [S039, S038, S040, S029, S004, S036, S041, S042, S043, S044, S045, S143, S147, S148]
lead: [S039, S038]
---

# Working is not secure

**Purpose (the first spoken sentence):** In this lesson you'll learn why an app that works perfectly can still let strangers in, and where to spend your attention so the agent's security gaps never reach your users.

**Conclusion:** Working and secure are two separate checks: agents make code run almost every time but make it secure only about half the time, so you state the stakes, never take "it's secure" from the agent as evidence, and watch every change to sign-in, payments, permissions, personal data and secrets, including every fix.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 04 Safe for strangers (first lesson of the module, straight after 03.03 put the app at a public URL).

**Lead source (audit, 2026-10-12):** S039 (Junquan Deng, Zhiyu Fan, Ruijie Meng); S038 (Veracode (Chris Wysopal quoted)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S039, S038, S040, S029); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length (audit, 2026-10-12):** about 5-6 minutes; COURSE.md (Aaron, 2026-10-01) gives orientation lessons and the first lesson of every module about 5 minutes, and the audit applied the rule. Cut C064 points 3 to 6 and C065 point 3 to one sentence each (this spec's own cut list); every other point marked brief becomes one line, and every point marked one line moves to the lesson page.

## What to teach (binding scope)

Rough time budget: C062 2 min · C007 2 min · C065 2 min · C064 1 min. Order most-useful-first: the gap (C062), where to look (C007), the lever you write (C064), the trap in the agent's own loop (C065).

### C062 Working code is not secure code

1. **Two different properties.** In Veracode's July 2026 tests, generated code compiled about 100% of the time but passed security checks only 56% of the time on average, essentially unchanged from the year before; without security-specific prompting, models failed about 44% of security-relevant tasks. Say on screen that Veracode tested raw models, not agents with guardrails or human review. (S038) — **teach**
2. **A bigger, newer or coding-specialised model will not fix it.** Coding models 51% vs general models 52%; large 53%, medium and small 51%; reasoning models 56% vs 51%; the best model (GPT-5.5) 68%, so still roughly one security task in three failed. In S039's replay the strongest model gave no gain over the baseline (26.2% vs 25.7% of runs reintroducing the flaw). (S038, S039) — **brief**
3. **Insecure is the norm once deployed.** Of 200 publicly deployed vibe-coded apps, 91.0% had at least one confirmed vulnerability, and 65.77% of the 1,186 found were Critical or High. (S039) — **one line** (that a public URL gets found and probed is 03.03's, C063)
4. **You cannot see security by looking, and experience does not save you.** In a 100-developer study, people picked the most-secure AI suggestion (37.7%) and the least-secure (35.0%) at statistically indistinguishable rates; only 22% of final submissions were fully secure; people spent about 21 seconds per suggestion on average (37 seconds once very short logs are excluded); and 3+ years of programming experience predicted *more* vulnerabilities (β 0.2, p = 0.011). Say that the tasks were C linked-list tasks with five AI suggestions each. (S040) — **teach**
5. **Don't ask "is it secure?"; ask for evidence from something other than the agent's say-so:** scanner output, a review by a separate model call, a test of the running app made the way an outsider would. Aaron's own sent-back lesson named exactly this trap: asking a model to "make sure it's secure" when you have no way to check the answer. Which checks exist and what each misses is 04.04 (C072). (S004, S043) — **brief**
6. **A test suite the agent wrote is not security evidence** (agents can bend tests to pass). (S042) — **one line**, owned by 06.02 (C013)

### C007 Spend human attention by blast radius

1. **Tier review by what a change can break.** Osmani's working tiers: agents do a first pass on every change; small-blast-radius changes to less sensitive code can get a lighter human pass once that first pass is clean; core and sensitive paths keep an owner and careful human review; a person approves every merge. (S029) — **teach**
2. **A person draws the zone map, not the agent.** Green (good tests, isolated): the agent works in a tight loop. Yellow (mixed quality): characterization tests first. Red (authentication, billing, permissions, payroll, anything few people understand): a human on every step, or no work. Zones move only when earned. Autonomy should follow blast radius, observability and recoverability; a model's confidence is a poor guide, and left to choose, the agent starts in the scariest file. (S036) — **teach**
3. **The NCSC's vibe-coding spectrum (2026-06-18).** Slide right (full vibe coding is often fine) for prototypes, demos, internal tools with limited exposure, and work with no sensitive data or security functions. Slide left for authentication or authorisation logic, sensitive personal data, secrets, tokens or credentials, safety-critical code, and anything where a flaw's consequences would be significant. Slide-left work needs four things: review what the AI produces, understand the code, check for vulnerabilities, verify it does what you expect; another AI agent can help, and the wider system should be designed so an exploit does limited damage. "Oversight, not avoidance." (S041) — **teach**
4. **The course's red-zone list** is the overlap of S036's red zone and S041's slide-left list: **sign-in, payments, permissions, personal data, secrets.** Say it is the course's synthesis of the two, not either source's wording. (S036, S041) — **teach** (one sentence, on screen as the five red rooms)
5. **Why speed is not free.** Two costs decide how fast you can stop reading code: checking work nobody read, and undoing failures the checks missed; skipping checks pushes cost into the second, larger bucket. (S029) — **one line**

### C064 State the stakes: agents skip security you didn't ask for

1. **The largest single cause.** 658 of the 1,186 vulnerabilities (55.5%) came from "hidden security rules": requirements a secure app needs that the user never stated, such as hashing passwords, validating input and enforcing checks on the server. The authors call it a mismatch between responsibility and capability: the agent leaves security design to people who cannot supply it. (S039) — **teach**
2. **State the stakes in plain words:** what the app is for, who uses it, what data it holds, and that it is going to production with real users. In S039's replay, asking for a production-ready implementation cut the rate at which the target flaw came back from 25.7% to 11.0%, and hidden-rule failures from 24.2% to 6.1%. (S039) — **teach**
3. **Don't paste security jargon you cannot judge.** A detailed "professional" prompt made things worse (45.7% reintroduction). OpenSSF: keep security instructions concise and specific, because irrelevant pasted text makes extraneous or incorrect code more likely; it does not recommend "act as an expert" persona prompts. (S039, S147) — **brief**
4. **Stating the stakes does not override an insecure instruction you wrote yourself.** The production-ready prompt raised obedience to insecure instructions from 8.3% to 25.0%; in one app a CLAUDE.md told the agent to embed an OpenAI key "protected" by a Caesar cipher, and it did. Read your own instruction files for demands like that. (S039) — **brief** (instruction files are 05.02's)
5. **Workflow help works as well as wording, and still is not a guarantee.** A security-hardening skill cut reintroduction to 11.9%; Supabase's agent skill includes the grant step; Claude Code's `.claude/claude-security-guidance.md` gives the reviewer your threat model but is guidance, not a guardrail. (S039, S148, S043) — **brief**
6. **One secure run proves nothing.** 123 of 560 replay cells (22.0%) gave both secure and insecure results across three identical repeats; better harnesses and prompts reduce the risk but do not remove it. (S039) — **one line**

### C065 Read what the fix changed

1. **The agent debugs itself now, and that loop has a blind spot.** "The error is gone" is something the agent can verify; "the lock is still on" is not. In S039, 100 vulnerabilities (8.4%), mostly broken access control and 77.0% Critical or High, came from fixes where a visible error was resolved by weakening or bypassing a security control. Example: a bypass-login route with hard-coded credentials, added to get past a Supabase authentication error and left in the code. (S039) — **teach** (the agent-debugs-itself rule is 02.03's; this is its security consequence)
2. **A warning is not a fix.** In 90 of 434 triggered runs (20.7%), the agent recognised the risk and still produced and shipped the insecure code, leaving a comment or recommendation instead. Treat every "before production you should..." line as an open item and ask: "Did you fix it, or only mention it?" (S039) — **teach**
3. **Fix patterns to recognise** (each taught in full elsewhere): swapping in the secret (service_role) key, which bypasses row-level security entirely (Supabase RLS docs, see Sources; 03.02); adding a `NEXT_PUBLIC_` prefix so an "undefined" key works, which publishes it to every visitor (S045; 03.02); granting `anon` access because Supabase's 42501 error hint names the exact `GRANT` (S148; 04.02); deleting failing tests, weakening assertions, mocking the unit under test or asserting the buggy behaviour to turn CI green (S042; 06.02). — **brief**
4. **What to look at without reading code fluently.** After any fix that touches login, permissions, keys, CORS, row-level security, grants or tests: removed lines near "auth", "role" or "policy"; `*` in CORS; a key name newly appearing in client code; a deleted test file. Review every changed file, not the summary: OWASP says not to approve on the description alone and not to assume lockfile, test or CI changes are routine. Ask the agent to list every security-relevant change in the diff. (S042, S039) — **teach**
5. **The agent's own security reviewer blocks nothing.** Claude Code's plugin sends findings back to the writing Claude as instructions and none of its layers blocks a write or commit, so check that a flagged issue was actually changed; for hard enforcement, use a blocking hook or CI check. (S043) — **one line** (the reviewer's limits are 04.04's, C072; blocking hooks are 05.02's)

## You vs the agent

As of 2026-10-12:

- **The agent does on its own:** writes, compiles, runs and fixes the code and its tests; runs static-analysis, dependency and secret scanners; triggers a separate-model security review (Claude Code's security-guidance plugin); applies more security rules when told the stakes; can draft a threat model for you to correct; lists every security-relevant change in a diff when asked. (S038, S039, S043)
- **You must:** know that none of the agent's green checks measures security (S038, S040); state the stakes in plain words (S039); draw the red zones (sign-in, payments, permissions, personal data, secrets) and keep a human on every red-zone change (S036, S041); have every fix that touches a red zone shown to you and refuse key-swap, public-prefix and blanket-grant fixes (S039, S148); treat every caveat in the agent's summary as an open item until it is fixed or written down as a launch blocker (S039); keep your own instruction files free of insecure demands (S039); own the decision to ship (S029; taught in 04.04).
- **Bring in an expert:** for any red-zone change you cannot judge yourself, before real users, personal data or money arrive. How to find, brief and use one is 04.04 (C118). (S041, S039)

## Sources this lesson is built from

- S039 — Junquan Deng, Zhiyu Fan, Ruijie Meng, "Understanding the (In)Security of Vibe-Coded Applications" (v1 2026-06-22; v4 2026-09-14) https://arxiv.org/abs/2606.23130 — the 200-app audit (91.0%, 1,186 flaws), hidden security rules (55.5%), weakening fixes (8.4%, 77.0% Critical/High), warnings instead of fixes (20.7%), and the prompt replay (25.7% → 11.0%, 45.7%, 22.0% non-unanimous). Re-read 2026-10-12 (v4 HTML). Note on screen that Claude Code was one of the apps' builders and one of the auditors, which the authors acknowledge.
- S038 — Veracode, "LLMs are getting smarter but not safer: Veracode 2026 GenAI Code Security Report" (2026-07-28) https://www.veracode.com/news/llms-are-getting-smarter-but-not-safer-veracode-2026-genai-code-security-report-finds-ai-generated-code-security-has-stalled-at-56%25-pass-rate/ — ~100% syntax vs 56% security, flat; model type, size, reasoning and language splits. Re-read 2026-10-12. Its per-vulnerability-class breakdown sits behind a personal-data form and was not read: name no classes from it.
- S040 — Hamza Khalid, Ronald E. Thompson III, Alejandra Sabater, Perucy Mussiba, Kelsey R. Fulton, Daniel Votipka, "(Don't) Trust, but (Don't) Verify: Developers' Attention to Security in AI-Generated Code" (2026-09-17) https://arxiv.org/abs/2609.21020 — people cannot pick the secure suggestion by looking; experience did not help. Re-read 2026-10-12 (HTML v1).
- S029 — Addy Osmani, "The Code Nobody Reads" (2026-09-28) https://addyo.substack.com/p/the-code-nobody-reads — review tiers by blast radius, a person approves every merge, the two costs. Re-read 2026-10-12.

Also cited for single points (credit on the lesson page):
- S036 — Addy Osmani, "Brownfield Agentic Engineering" (2026-09-14) https://addyosmani.com/blog/brownfield-agentic-engineering/ — the green/yellow/red zone map. Re-read 2026-10-12.
- S041 — Toby W (NCSC), "The 'vibe coding spectrum' approach to AI-assisted software development" (2026-06-18) https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf — slide right / slide left and the four oversight verbs. Re-read 2026-10-12. Do not use its ETSI sentence (ambiguous about which end of the spectrum it means).
- S004 — Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons..." (2026-10-04) https://aaronorelup.com/ledger/lessons-sent-back/ — "make sure it's secure" as a question you can't verify.
- S042 — OWASP, "Secure Coding with AI Cheat Sheet" (created 2026-05-05; updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — test gaming; review every file, not the description. Re-read 2026-10-12.
- S043 — Anthropic, "Catch security issues as Claude writes code" (live docs, modified 2026-10-09) https://code.claude.com/docs/en/security-guidance — the guidance file is not a guardrail; no layer blocks. Re-read 2026-10-12.
- S045 — Vercel, "v0 security" (lastUpdated 2026-10-09) https://v0.app/docs/security — only `NEXT_PUBLIC_` variables reach the browser. Re-read 2026-10-12.
- S147 — OpenSSF, "Security-Focused Guide for AI Code Assistant Instructions" (2025-08-01; foundational and still current) https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions — concise instructions; no persona prompts. Re-read 2026-10-12.
- S148 — Supabase discussion #45329 (2026-04-28, comments to 2026-10-11) https://github.com/orgs/supabase/discussions/45329 — the agent skill includes the grant step; the 42501 hint.
- Not yet in sources.md (proposed): Supabase Docs, "Row Level Security" (live docs, undated, read 2026-10-12) https://supabase.com/docs/guides/database/postgres/row-level-security — the secret/service_role key bypasses RLS and must stay server-side. concepts.md credits this point to S044, but the Wiz post does not contain it; the Supabase page does.

## Show it for real

- Same agent, two prompts: "build a signup form" and "build a production-ready signup form for real users that stores emails and passwords"; diff the two for password hashing, input validation and server-side checks. Proves stating the stakes changes what gets built (S039's replay, on a small scale).
- Run each prompt three times and scan all six outputs with the same scanner. Proves one secure run proves nothing (S039).
- Veracode's chart: ~100% syntax vs 56% security, flat across snapshots, shown as the real published figure. Proves "works" and "secure" are different measurements (S038).
- A git diff in GitHub's or the editor's diff view where a "fix" removes a role check, widens CORS to `*` or deletes a failing test; then ask the agent "list every security-relevant change in this diff" and compare. Proves you can spot a weakening fix without reading code fluently (S039, S042).
- Scroll to the end of a real agent summary, highlight each "before production you should..." line, ask "did you fix it, or only mention it?", and grep the code to check. Proves a warning is not a fix (S039).
- Sort a real project's files into slide-right and slide-left using the NCSC lists, with the five red rooms labelled. Proves the zone map is drawn by a person in a few minutes (S041, S036).
- Use a throwaway local project and test accounts only; no real keys, emails or user data on screen.

## Questions this lesson answers

Asked in the wild:
- "Is it possible [to succeed] with vibe coding SaaS projects?" — the one security reply: test thoroughly and assess all potential security threats before any real-world use (S143, Hacker News, about 2026-10-01).
- Aaron's own: asking the agent to "make sure it's secure" when he had no way to check the answer (S004).

Likely phrasing (proposed by the research batches, not observed being asked):
- My app works perfectly. Why would it be insecure?
- Claude ran all the tests and they pass. Isn't that enough?
- Isn't the newest model secure by now?
- What should I tell the agent so it builds things securely? Does "make it production-ready" actually change anything?
- Why did the same prompt give secure code yesterday and insecure code today?
- The agent fixed my login error. How do I know it didn't just turn security off?
- Claude said "for production you should...". Did it do it?
- Which parts of my app do I actually need to check carefully? Is it OK to vibe code this?

<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- A public URL is found and probed within days → from-your-laptop-to-a-url (03.03, C063)
- Secret vs public keys, `NEXT_PUBLIC_`, service_role → keys-public-secret-and-leaked (03.02, C069)
- Grants, row-level security, the Supabase 42501 grant fix → test-it-as-a-stranger (04.02, C068)
- Which scanners and reviews exist and what each misses; bringing in an expert; who signs off → before-you-ship-who-signs-off (04.04, C072, C118, C009)
- The agent reads, fixes and re-runs its own errors → when-it-breaks-you-supply-the-eyes (02.03, C019)
- Agent-written tests are not independent evidence; test gaming → checking-what-you-cant-read (06.02, C013)
- Instruction files, deny rules and blocking hooks → rules-it-reads-rules-it-cant-break (05.02, C044, C045)
- Prototype vs production → what-runs-where (03.01, C008)

## Out-of-date framings to avoid

- "If it works, it's done." (S038)
- "The best or newest model writes secure code." (S038, S039)
- "Trust, but verify." In the study, people did neither: seconds per suggestion, and trust anyway (S040).
- "Experienced developers will catch it." (S040)
- "Don't use AI for security-critical code." The NCSC says oversight, not avoidance (S041).
- "Review every line of AI code" as the answer; and its opposite, "treat all AI code the same". Tier by blast radius (S029).
- "Let the agent decide where to start" / "if it sounds confident, give it more rope." (S036)
- "The AI knows security best practices and applies them automatically." (S039)
- "A more detailed, professional-sounding prompt is safer" / "tell it to act as a security expert." (S039, S147)
- "If the agent fixed the error, the problem is solved" / "it mentioned the risk, so it handled it." (S039)
- The 2021 picture of hand-debugging: the viewer does not read stack traces here; the agent fixes, the viewer checks what the fix changed.

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 (`00-06-how-to-learn-anything-technical`) touches it in passing: its "loud vs quiet errors" segment uses the Veracode 56% figure correctly and its "make sure it's secure" segment states the trap well. What it lacks for this slot: the S040 study (it cites a 2022 Stanford study instead, now superseded by a 2026 one), hidden security rules and stating the stakes (C064), weakening fixes and warnings-instead-of-fixes (C065), and the zone map (C007). It also points to the retired map ("Security, in Trust") and old lesson numbers; do not reuse those pointers.
