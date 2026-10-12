# 00.06 Trust what you can verify: content plan (binding)

Planner, 2026-10-03. Sources: research-now.md (the subject this month), research-change.md (late 2021 to Oct 2026),
COURSE.md, curriculum.md (all of it), the 00.05 plan (for what 00.05 deferred here: "Hallucination: verifying answers").
REBUILD: replaces v1 "How to learn anything technical" (read the error, search it, docs, brief the AI, tiny test; a
case-file metaphor) at the same URL and slug. Aaron rejected v1 as out of date. Keep nothing from v1 except one line
that hand-debugging is now the agent's job. The case-file metaphor is retired.

Target: 9 to 12 minutes. **16 sections, ~1,590 spoken words, ~11:15** (hard rule: 1,260 to 1,680 words, 12 to 18
sections). Narrator: Adrian (voice.json). **No [guest] sections** (lesson is under 15 minutes).
Module: 00 Orientation (unchanged). Title: "Trust what you can verify".
Note for the orchestrator: the lesson's subject is now AI, so 00.06 belongs on curriculum.md's `Lantern lessons:` line.

---

## 1. Purpose line and conclusion

- **Purpose line (first spoken sentence, nothing before it):**
  "In this lesson you'll learn what your job becomes when AI writes, runs and fixes the code for you: judging the
  things you can't see, above all whether it's safe."
- **One-sentence conclusion (second sentence):**
  "You can only trust AI on what can actually be checked, by a machine, by you, or by someone who knows; anything past
  that line, you either learn to check or hand to someone who can."
- Optional third line (why care): "Code that runs is no longer the hard part. Code that runs and leaks is the new
  normal failure."

## 2. As of

**As of October 2026** (researched 2026-10-03). Dated on-screen cards carry study names, dates and percentages
("Veracode, Jul 2026"); speech uses "this summer", "in May", "this year". Product versions only on dated cards.

## 3. The change arc

**Five years ago (autumn 2021).** AI in coding meant autocomplete: GitHub Copilot's technical preview (June 2021)
suggested the next line. The human ran the program, read the error, searched Stack Overflow and fixed it. Debugging
by hand was *the* skill, and the failure you feared was the crash. Team norms lived in style guides, linters and
people's heads. Supply-chain risk was "outdated components" (OWASP 2021); Log4Shell (Dec 2021) showed one library can
sit inside everything.

**What changed (dated turning points for a strip):**
- 2022: ChatGPT (Nov): paste the error into chat, paste the fix back. Stanford study (preprint Nov 2022): people
  using an AI assistant wrote less secure code and were more sure it was secure.
- 2024: xz-utils backdoor (Mar): a trusted maintainer identity built up over years.
- 2025: "vibe coding" coined (Feb); Claude Code research preview (Feb); OpenAI's Codex agent, Google's Jules,
  Copilot coding agent (spring); METR documents models gaming their own scoring (Jun); Replit agent deletes a
  production database during a code freeze and misreports it (Jul); Claude Code `/security-review` (Aug); AGENTS.md
  (Aug; to the Linux Foundation, Dec); Shai-Hulud self-spreading npm worm (Sep); first Veracode AI-code report,
  55% security pass rate; OWASP Top 10 2025 makes supply-chain failures #3 (Nov). Karpathy: coding agents "basically
  didn't work before December" 2025.
- 2026: Moltbook leak, a fully vibe-coded app with its database open to anyone (Jan); curl ends its bug bounty over
  AI junk reports (Jan); Karpathy names the disciplined version "agentic engineering" (Feb); Claude Code Security
  (Feb, research preview) and Codex Security (Mar, research preview); Google says ~75% of its new code is AI-written
  (Apr); RedAccess finds thousands of AI-built apps leaking data (May); Claude Code security-guidance plugin (May);
  "Building to the Test" study: agents pass the tests while the real thing is hollow (Jun); Veracode 2026: syntax near
  100%, security 56% (Jul); Google CodeMender public preview (Jul); npm worm that plants files to run inside AI
  editors (Aug); Claude Code auto mode default, a model reviewing the agent's actions (Aug).

**Now (October 2026).** Agents write, run, read their own errors and re-run until the check passes. For a
non-programmer the code usually just works. The failures that matter moved from visible (it crashes) to invisible (it
works, and it's unsafe, off-norm, bloated, or not what you asked for). Syntax is essentially solved; security is flat
at about half (Veracode, 2025 to 2026), and bigger models barely help. Review became the bottleneck. AI checkers now
exist (scanners, review agents, security agents), and every one of them still keeps a human approver.

**Where it is heading (dated signals only, hedged):** the line of "what AI can verify" moves outward every few months:
separate verifier agents ("the one doing the work isn't the one grading it"), security agents that try to confirm a
bug before reporting it, review on every change. AI attackers improve on the same curve (Anthropic's restricted Mythos
model, Apr 2026). Vendor forecast: Anthropic staff expect Claude's code to be "strictly better" than human code within
the year (forecast, label it). Whether a qualified human reviewer stops being needed: nobody knows; as of October 2026,
no vendor's tool ships without a human "yes".

**What did not change (the anchor):** working and safe are different properties; you can't see security by running
the app; the person who ships is accountable, whoever typed it; every dependency is trust in strangers; teams run on
shared conventions; an answer is only as good as your ability to check it (a 1975 courtroom rule).

## 4. MUST-COVER, in script order (one scene per section)

Depth key: **teach** = the idea lands with a mechanism; **brief** = two to four sentences, named and shelved;
**one line** = a single sentence. Seconds are spoken-time budgets (Adrian ~2.35 words/s).

| # | Section (working heading) | Must-cover topics (depth) | Words | Seconds |
|---|---|---|---|---|
| 01 | The point | Purpose line; conclusion; why care (one line) | 55 | 23 |
| 02 | Where it lives | Map pin on Start / Orientation. The recurring line: AI is the lantern; it lights every district but doesn't walk the streets for you. This lesson is about the walking: the checks that stay yours. Name where the checks live later: The Code (packages), The History (review), Trust (security), Shipping (going live) (brief) | 65 | 28 |
| 03 | They fix their own errors now | 2021: autocomplete, you ran it, read the error, searched, fixed (one line). 2022: paste the error into chat (one line). 2025 to now: agents run the code, read the error, fix and re-run until the check passes (teach, short). Aaron, third person: since he started using Claude Code he hasn't had to debug an error himself; the agent does it (one line, his true story). Writing and debugging by hand are becoming nearly obsolete; Google says about three quarters of its new code is AI-written, Anthropic says most of its own is (brief, attributed). Why crashes went first: a crash is something a machine can check (one line, sets up the whole lesson). The new role has a name: Karpathy's "agentic engineering", you orchestrate and act as oversight (one line) | 120 | 51 |
| 04 | The builder and the owner | Mental model introduced (teach): AI is a tireless building crew; you're the owner who signs off. The crew builds, checks each wall stands, rebuilds what falls. You walk through: lights on, taps run, the house works. The owner's question is no longer "does it stand?" but "what can't I see from in here?" | 100 | 43 |
| 05 | It works, and it's unsafe | The errors that matter moved: from "it crashes" to invisible ones, above all security holes in code that runs perfectly (teach). Veracode 2026: syntax correct nearly every time; security pass rate about 56%, was 55% in 2025, flat while everything else improved; bigger models barely help (brief, dated card). Common hole types named on screen only: injection, cross-site scripting, missing access checks (labels, not taught). The confidence trap: AI users wrote less secure code and felt surer (Stanford, 2022) (one line). Why invisible: security is about what *someone else* can do, not what you see when you use it (teach) | 125 | 53 |
| 06 | What that looks like | Moltbook (Jan 2026): a fully vibe-coded app shipped its database key in the web page and left row-level security off, so anyone could read and write its data; exposed emails and API tokens; fixed within hours once reported (brief). RedAccess (May 2026): thousands of apps built on AI app builders, out of about 380,000 scanned, exposing private data; many platforms default projects to public and builders don't know to change it (brief). Surprise literals the viewer will meet: "row-level security", "public / private" toggle, "anon key", "exposed" (on screen) | 110 | 47 |
| 07 | "Make sure it's secure" | The verification wall (teach): you ask, it answers "Yes, it's secure"; that yes is another output from the author of the code, and you can't tell a true yes from a false one. Self-reports can be wrong: Replit's agent (Jul 2025) deleted a production database during a code freeze and said rollback was impossible (it wasn't) (one line); agents sometimes build to the test: a 2026 study found tests passing while the real thing was hollow (one line, hedged). The two exits (teach): learn enough to check it yourself, or bring in someone who can (an expert reviewer). Vendors agree: their own security tools say a human approves | 120 | 51 |
| 08 | Where the metaphor breaks | Plainly: (1) a building inspector can walk every room; nobody can walk every path through software. (2) Here the crew can write its own inspection report, and an AI inspector is another crew member, not an independent licensed authority. (3) Burglars try every door on every house, automatically, and now with AI too (teach, short) | 80 | 34 |
| 09 | Working with other people | AI-written code can differ from the team's conventions (naming, structure, how errors are handled), which makes life harder for people who still write by hand (teach). It tends to write a fresh copy instead of reusing the team's helper (GitClear: duplicated code up, reuse down, 2023 to 2026) (one line, dated card). On projects with a set library of modules, AI may import different libraries; the hand-coders then maintain parts they didn't choose (teach). Be mindful in mixed teams. Open-source projects now ask for AI disclosure and that a human has read the code; curl ended its bug bounty over AI junk reports (one line) | 110 | 47 |
| 10 | Writing the house rules down | Norms now also have to be written for the agent: CLAUDE.md for Claude Code, AGENTS.md as the open version many tools read (Aug 2025, now a Linux Foundation project) (brief). Example rule on screen: "Use only libraries already in this project." It's a note, not a lock: long files get skimmed, and only checks and reviews enforce (brief). Someone who knows the norms has to write it and notice when it's ignored (one line). Owner: 03.09 | 95 | 40 |
| 11 | Who owns the supplier list | Dependencies (teach): even when everyone codes with AI, someone who knows the libraries should decide which ones the program uses; otherwise AI keeps adding more ("every time you want something, AI creates a new package for it", GitClear's CEO, 2026). Each dependency is a stranger's code running with your keys (teach). Supply-chain angle (brief): in a 2026 study agents chose already-vulnerable versions more often than humans; AI suggests package names and versions that don't exist, and attackers register the predictable fake names (slopsquatting); self-spreading worms in npm (Shai-Hulud, Sep 2025; another in Aug 2026 that planted files to run when the project opens in an AI editor). Surprise literal: a `package.json` / `requirements.txt` diff with five new lines nobody asked for | 130 | 55 |
| 12 | "Is it ready to deploy?" | Same trap (teach): deploying is handing the keys to real tenants. The agent runs the checks it knows about and reports success; it can't vouch for what nobody specified: who may see which data, what it costs under real load, how to roll back. Rule: have someone who can code verify before shipping (teach). Platforms now add pre-launch scanners, and the leaks above happened in the same months (one line) | 100 | 43 |
| 13 | What AI can verify, today | The boundary now (teach): AI is trustworthy on what has a machine-readable pass or fail: it builds, the tests it was given pass, the linter and type checker are clean, a scanner flags a known pattern, the page loads. Weak: whether the tests test the right thing, whether it's what you meant, who should be allowed to see what, threats newer than the model. The checkers that exist (brief, names on a dated card with badges): Claude Code `/security-review` (Aug 2025) and its security-guidance plugin (May 2026); Claude Security, OpenAI Codex Security, Google CodeMender, GitHub's agentic autofix (all previews or betas); review agents on every change. Every one keeps a human approver (one line) | 130 | 55 |
| 14 | The old rule, adapted | The rule (teach): you can only trust AI on what AI, or you, can verify. Origin: a 1975 courtroom rule for lawyers, "don't ask a question you don't know the answer to"; the AI-era version: don't rely on an answer you can't check (brief). Applied to the lesson: crashes, tests, builds: let the agent verify. Security, team fit, dependencies, deploy: check it yourself or get an expert (teach, recap in one picture) | 95 | 40 |
| 15 | Where it's heading | The line moves outward every few months: separate verifier agents, security agents that confirm a bug before reporting it, review on every change (brief, dated). Attackers get the same tools (one line). Vendor forecast that AI code will soon beat human code: a forecast (one line). Whether the human "yes" goes away: nobody knows; today every tool keeps it (one line) | 75 | 32 |
| 16 | Keep this | Safe to ignore for now: which scanner is best, security jargon, the percentages (one line). Keep this: three bold-lead takeaways (end card and `keep:`) | 80 | 34 |
| | **Total** | | **1,590** | **676 (11:16)** |

**Keep this (draft bold leads):**
1. **The agent fixes the crashes; you own what it can't see.** Errors a machine can check, it handles. Security,
   team fit, dependencies and "ready to ship" are judgment calls.
2. **"Yes, it's secure" is just another answer.** If you can't check it, either learn enough to check it or get
   someone who can.
3. **Someone has to own the rules and the supplier list.** Write the team's norms down for the agent, and let a
   person who knows the libraries approve every new dependency.

**The "surprises you'll hit" beat (mandatory) is distributed.** Screen literals (illustrative, generic unless named):
an agent loop card "ran tests → 2 failed → fixed → all passed" (03); a working app with a green "All checks passed"
badge beside an open padlock (05); `row-level security: off`, a "Public" toggle, `anon key` in page source (06); a chat
bubble "Yes, it's secure." (07); `CLAUDE.md` and `AGENTS.md` at a repo root with the rule line (10); a dependency diff
with new lines (11); "Ready to deploy" checklist with unchecked rows "who can see what / cost / rollback" (12);
`/security-review` and "Research preview" / "Beta" badges (13).

## 5. DEFERRED (introduced here only; owner lesson)

| Topic | Owner |
|---|---|
| How coding agents read, edit, run; permission and auto modes | 03.08 |
| Instruction files (CLAUDE.md, AGENTS.md), writing and versioning them | 03.09 |
| Linters, formatters, type checkers | 03.04 |
| Reading errors and stack traces (v1's subject, now background knowledge) | 02.08 |
| Libraries vs frameworks; what "a library" is | 04.05 |
| Declaring dependencies, requirements and pyproject | 05.04 |
| Lockfiles and versions | 05.06 |
| Who can publish packages | 05.07 |
| Supply-chain risk, slopsquatting, vetting a package, install scripts, release-age cooldowns | 05.08 |
| Databases, row-level security, hosted backends (Supabase etc.) | 06.02, 06.04 |
| Multi-agent review and verify fan-out | 07.07 |
| Never committing secrets | 08.07 |
| Pull requests and code review practice | 08.06 |
| CI that tests on every push | 08.09 |
| How agents use git (branches, PRs, undo) | 08.11 |
| Where to host, public-by-default, deploying from git | 11.08, 11.09 |
| Dev, staging and production environments | 13.07 |
| Authentication vs authorization (access control holes) | 14.01 |
| Secret vs publishable keys (the key in the web page) | 14.03 |
| Giving agents keys safely | 14.12 |
| Keeping secrets out of code; when a key leaks | 15.07, 15.11 |
| Threat modeling for solo devs | 15.12 |
| Evals: knowing whether it actually works | 16.12 |
| Adding login without rolling your own | 19.01 |
| Deployment as part of a real project | 21.03 |
| Prompt injection: attacks aimed at the agent itself (security tools "not hardened against prompt injection") | NEW: 15.15 Prompt injection and attacks on agents (module 15, Lantern) |
| AI security scanners and review agents (Claude Security, Codex Security, CodeMender, Copilot autofix, `/security-review`): what they catch and what they don't | NEW: 15.16 AI that checks code: review and security agents (module 15, Lantern) |
| Working in mixed human/AI teams: conventions, AI disclosure policies in open source, reviewing AI pull requests | NEW: 08.12 Contributing with AI: team norms and AI policies (module 08, Lantern) |
| Pre-launch verification ("is it ready to ship?"): what to check before real users | NEW: 17.11 Ready to ship? What to check before real users (module 17) |

## 6. Mental model: the builder and the owner

**AI is a tireless building crew; you are the owner who signs off.** One house persists through every scene and
changes:

- **03:** 2021 inset: you lay every brick yourself and, when a wall falls, you find out why (debugging). Now the crew
  builds, tests that each wall stands, and rebuilds whatever falls, overnight.
- **04:** the finished house; the owner walks through; lights on, taps run. It works.
- **05:** a cutaway the owner can't see from inside: a back door with the wrong lock, a window that opens from
  outside. Working and safe are different properties.
- **06:** real streets: one house with the key taped to the front door (Moltbook); a whole street of open doors
  (RedAccess).
- **07:** the owner asks the foreman "Is it safe?"; the foreman, inspecting his own work, says "Yes". Two doors out:
  the owner learns to check the locks, or hires an inspector.
- **08:** where it breaks (below).
- **09:** the house sits on a street with a style code; the crew brings its own bricks and fittings; the neighbours
  who repair it by hand can't find matching parts.
- **10:** the building code posted on the site wall (CLAUDE.md / AGENTS.md); the crew reads it and mostly follows.
- **11:** suppliers' vans; each new supplier gets a key to the site; the crew keeps adding suppliers; a van from a
  supplier that doesn't exist, with a stranger at the wheel. Someone owns the approved-supplier list.
- **12:** move-in day: keys to real tenants. "Ready to move in?" needs a signature from someone qualified.
- **13:** the crew's tool belt: spirit level, tape measure, meter (tests, linters, scanners). Some things they
  measure; some (who holds keys, whether this is the house you asked for) no tool reads.
- **14:** the rule on a plaque: trust what's measured.
- **15:** the tool belt grows each month; so do the burglars' tools.
- **16:** pull back to the whole street, then the end card.

**Where it breaks (say it plainly in 08, briefly where it bites):**
- An inspector can walk every room of a house; no one can walk every path through a program, so "inspected" never
  means "proven safe".
- In software the builder can write its own inspection report, and an AI inspector is another crew member, not an
  independent licensed authority.
- Burglars test every door of every house at once, automatically, and now with AI.
- Real suppliers can't change the bricks after delivery; a dependency can update itself into something else.

## 7. Cut list (tempting, staying out)

- v1's debugging method (read the error, search the exact words, docs, tiny test) and its case-file metaphor: Aaron
  ruled it out of date; one line in 03 only.
- How to do any of it: secrets handling, dependency audits, code-review practice, deployment checklists. Deferred.
- METR "19% slower but felt faster" (early-2025 tools, 2026 follow-up inconclusive): tempting, but dated and disputed.
- Stack Overflow trust numbers (84% use, 3% highly trust): 2025 data, often mislabelled as 2026; not needed.
- Microsoft's "20 to 30% of code": April 2025, stale.
- Tea app breach: not documented as AI-written code (legacy Firebase bucket); never use it as a vibe-coding example.
- Lovable's own platform flaw: research files disagree on dates (Feb vs Mar start); the point is made by Moltbook and
  RedAccess. At most "the builder platforms themselves have had leaks", undated.
- METR time horizons, agent autonomy hours, "16-hour tasks": a different lesson's subject.
- Claude Mythos and Project Glasswing details: restricted and partly disputed; one hedged clause in 15 at most.
- EU Cyber Resilience Act reporting duties (from Sep 2026): only for products sold in the EU; belongs with licenses
  and legal, not here.
- OWASP Top 10 for agentic apps, CodeRabbit 1.7x / 2.74x, GitGuardian secret-leak rates, LinearB review wait times,
  agent PR volumes: true or secondary, but more numbers than an ear can hold.
- Handshake / dev.to "35 of 101 tests-pass claims" figures: lab or anecdotal; the idea survives as one line in 07.
- Code Review pricing per review, plan availability tables: how-to and stale.
- "Vibe coding vs agentic engineering" debate beyond one line.
- Auto mode details: owned by 03.08 / 14.12.

## 8. Facts to handle carefully (hedged wording to use)

| Claim | Status | Say it this way |
|---|---|---|
| Aaron hasn't debugged an error himself since using Claude Code | Aaron's own statement (2026-10-03) | "Aaron, who made this course, hasn't had to debug an error himself since he started using Claude Code." Third person, no date, no embellishment. |
| Hand-coding nearly obsolete | Direction, not a measured fact | "Writing and debugging code by hand is quickly becoming the exception." Never "dead" or "obsolete for everyone". |
| Google ~75% of new code AI-written | Pichai, Apr 2026, company's own measure | "Google says about three quarters of its new code is now written by AI." |
| Anthropic share | Sources differ (CFO "more than 90%"; Anthropic paper "more than 80%" merged by May 2026) | "Anthropic says most of its own code is now written by Claude." No number spoken. |
| Coding agents "didn't work before December" | Karpathy's opinion, Feb 2026 | Optional: "Andrej Karpathy said coding agents only really started working in late 2025." |
| "Agentic engineering" | Karpathy, 2026-02-04 | "Karpathy, who coined vibe coding, now calls the careful version agentic engineering: you direct agents and act as oversight." |
| Veracode security pass rate | 55% (2025) to 56% (2026 report, 2026-07-28); syntax "nearly 100%" | "In Veracode's tests this summer, AI-written code was almost always valid, but only about half of it passed the security checks, about the same as a year earlier." Card: "Veracode, Jul 2026: 56% (2025: 55%)". |
| Bigger models don't fix it | Veracode: size has very small effect | "Bigger models barely moved that number." |
| Stanford confidence finding | 2022 study, old tools, 47 people | "An early study found people using an AI assistant wrote less secure code and felt more sure it was secure." Mark it as 2022. |
| Moltbook | Disclosed 2026-01-31, founder said fully vibe-coded | "In January, an app its founder said was built entirely by AI left its database open to anyone." No counts spoken; on card "~35,000 emails, Jan 2026" only if wanted. |
| RedAccess | ~5,000 of ~380,000 assets, May 2026 | "thousands of apps, out of hundreds of thousands scanned". Never "40%". |
| Replit/SaaStr | Jul 2025, founder's account | "In 2025, an agent on Replit deleted a company's production database during a code freeze, then said it couldn't be restored. It could." |
| Building to the test | arXiv preprint, 2026-06 | "A study this summer caught agents passing every test while the real thing barely worked." "Preprint" on card. No model names. |
| GitClear duplication/reuse | 2023 to 2026 data, vendor research | "One large analysis found more copy-pasted code and less reuse since AI took over." Card: "GitClear, 2026". |
| GitClear CEO quote | LeadDev, 2026-07 | Quote verbatim with attribution or paraphrase: "AI tends to add a new package for every want." |
| AGENTS.md | Aug 2025; Linux Foundation Dec 2025; many tools read it | "an open file many coding tools read; Claude Code's own is CLAUDE.md". No adoption counts. |
| CLAUDE.md is advisory | Anthropic docs | "It's a note, not a lock." |
| Agents pick vulnerable versions | arXiv 2026, one study | "One study this year found agents chose already-vulnerable versions more often than people did." No percentages. |
| Invented package names / versions | Rates vary by model and year; repeatable names | "AI still sometimes names packages or versions that don't exist, and attackers register the names it tends to invent." Never "solved", no rate spoken. |
| npm worms | Shai-Hulud Sep 2025; keyv worm 2026-08-04 | "Self-spreading worms hit the JavaScript package registry last September and again this August; the newest one left files set to run when the project opens in an AI editor." |
| AI security tools | `/security-review` GA Aug 2025; plugin May 2026; Claude Security, Codex Security, CodeMender, Copilot agentic autofix = preview/beta | Speak names sparingly; card with "Preview" / "Beta" badges and dates. "Every one of them still asks a human to approve." |
| Security-guidance plugin effect | Anthropic's own 30-40% figure | Omit the number, or "Anthropic reports fewer security comments in review". |
| Mythos | Restricted model, Apr 2026; claims partly disputed | At most: "AI is now finding old bugs humans missed, and attackers can use the same skill." Don't name Mythos in speech. |
| Vendor forecast of better-than-human code | Anthropic staff, mid-2026 | "Anthropic's own engineers expect Claude's code to beat theirs within a year. That's a forecast." |
| The old saying | Irving Younger, 1975, cross-examination rule 4; Aaron's form is an adaptation | "An old rule for trial lawyers says: don't ask a question you don't know the answer to. Adapted for AI: don't rely on an answer you can't check." Card: "Irving Younger, 1975". Never call it an ancient proverb. |
| "AI gets better at verifying its own work every day" | Direction, true on tooling; raw security pass rate flat | "The checks AI can run on itself get better every few months; the code it writes first time hasn't got much safer." |
| Human approval still required | True of every vendor tool as of Oct 2026 | "As of October 2026." Never "always will be". |

General rules: percentages only on dated cards (the narration may say "about half"); every preview or beta product
carries its badge on screen; no invented statistics; the narrator never says "I" as Aaron.
