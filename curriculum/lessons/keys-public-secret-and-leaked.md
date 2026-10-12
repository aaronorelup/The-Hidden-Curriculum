---
key: keys-public-secret-and-leaked
id: 03.02
title: Keys: public, secret and leaked
district: Going Live
module: 03 Putting it online
status: todo
legacy: [01-05-environment-variables-path]
minutes: [9, 11.5]
concepts: [C069, C070, C071, C126]
sources: [S020, S048, S213, S061, S212, S045, S044, S023, S047, S046, S042, S209, S155, S153, S066, S101]
lead: [S048, S020]
---
# Keys: public, secret and leaked

**Purpose (the first spoken sentence):** In this lesson you'll learn what an API key really is, how it reaches your app as a setting, which keys may sit in the browser and which never may, where keys leak when an agent does the work, and what to do when one leaks.

**Conclusion:** A key is a permission set handed to a program as a setting: anything shipped to the browser is public, secret keys belong only on the server or in the host's secret store, agent config files and logs leak them, and a leaked key keeps working until you revoke and rotate it, because deleting the commit does nothing.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 03 Putting it online, second lesson (after what-runs-where, which drew the browser / server / database map this lesson hangs keys on).

**Lead source (audit, 2026-10-12):** S048 (Guillaume Valadon (GitGuardian), on The Hacker News); S020 (Joe Leon (Truffle Security)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S020, S048, S213, S061); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Teach in this order: how a key reaches a program (C126), what a key is and where each kind may live (C069), where keys leak in agent work (C070), what to do when one leaks (C071).

### C126 Environment variables: the settings a program receives when it starts

- **A program gets its settings when it starts, and keeps that copy** (teach). A real case: an n8n user on 2026-07-12 set `WEBHOOK_URL` in Portainer's stack panel, yet "the test url and production url is showing local host". The reply: the panel only fills `${VAR}` placeholders in the compose file, so the value never reached the container; "a plain restart keeps the old env"; the fix is to redeploy so the container is recreated, then check inside it with `docker exec <container> printenv WEBHOOK_URL` (S213). Lesson: a changed setting needs a new terminal, a restart or a redeploy, depending on where it was set, and the only proof is reading it inside the running program.
- **Where values live** (brief). Your shell session, a `.env` file, a container's compose file (S213), and a hosting dashboard: Vercel stores them "in Vercel's built-in secure vault" (S045), Lovable keeps backend values in its Secrets manager (S212). Each place is a different copy.
- **Build-time values are public** (teach). Lovable: "Anything prefixed with `VITE_` is a build-time, browser-exposed value"; such values "are embedded into the client bundle at build time and are safe to be public" (S212). Vercel's v0: "Only variables prefixed with `NEXT_PUBLIC_` are exposed to the browser" and "Never expose sensitive tokens with `NEXT_PUBLIC_` prefix" (S045, updated 2026-10-09). Renaming a variable does not make a value secret; moving the call does: v0 says "The AI can move code to Route Handlers, Server Actions, or other server-side contexts" (S045).
- **`.env` is a naming convention, not a vault** (teach). Lovable: "Do not add `.env` to `.gitignore` in a Lovable project", because there it holds only public `VITE_` values that the build needs (S212). Elsewhere it holds secrets, and MIT's Missing Semester says secrets "must not be included in version control" (S209). Know which kind your `.env` is before anyone tells you a rule about it.
- **Configuration lives outside the code** (one line). "Software configuration should not be embedded in the code but be provided at runtime" (S209).
- **Each environment has its own values** (one line). "Use different keys for development and production environments" (S045). Local, preview and production as places is 03.03.
- Dropped here: PATH, "not recognized" and why a new terminal sees an install (where-your-agent-works, C122); Windows user vs system variables (no current source; the challenge log could not find it in Aaron's prompts).

### C069 Keys are permission sets: public vs secret, and where each may live

- **Two kinds of credential** (teach).
  - Publishable keys are meant to be in the browser. Wiz found Moltbook's Supabase key by examining "the client-side JavaScript bundles loaded automatically by the page"; Supabase's publishable key is safe to expose only "When properly configured with Row Level Security (RLS)", and Moltbook's was not, so anyone could read and write the database (S044, 2026-02-02).
  - Secret keys never are. Supabase's own docs: a secret key works through the `service_role` role, "which has the `bypassrls` attribute", and "Never use a secret key in the browser or expose it to customers" (S044, Supabase RLS docs read as its companion). RLS itself is 04.02.
- **A key's power is whatever it reaches today** (teach). Google "spent over a decade telling developers that Google API keys (like those used in Maps, Firebase, etc.) are not secrets". Then enabling the Gemini API on the same cloud project let existing keys "silently gain access" to Gemini, with no warning, and new keys defaulted to "Unrestricted". Truffle Security found 2,863 live vulnerable keys in the November 2025 Common Crawl (S020, Joe Leon, 2026-02-25). The agent cannot see which APIs are switched on in your cloud project; you can (C069).
- **An automation token reaches everything its account reaches** (brief). "An n8n API token provides access according to the permissions of the user who created it": workflow definitions (with any secrets typed into them), execution data, data tables and variables (S048, 2026-08-05). One token, many keys.
- **Where a secret may live** (brief). In the host's secret store or server-only variables: Lovable's Secrets are "encrypted, injected into your Edge Functions automatically, and never reach the browser" (S212). Not in browser code, not in a workflow node (an SSH deployment key "had been hard-coded directly into one of its nodes", S048), not in a file the agent reads (C070 below).
- **Make a stolen key worth less** (brief). Restrict each key by API and by application, and rotate any exposed key (S020); separate development and production keys and rotate regularly (S045); give keys an expiry (n8n added a 30-day default in version 1.78.0, February 2025, and many older keys never expire, S048). Spend caps are 06.03.
- Truffle's article lists Google's roadmap (scoped defaults for new AI Studio keys, blocking leaked keys used with Gemini, notifying owners) and says no root-cause fix had been seen at publication (S020). Do not say what Google ships today without a newer source; concepts.md's "required API restrictions by May 2026" is attributed to a Register report that is not in sources.md.

### C070 Where secrets leak in agent work

- **Approving a command can save the key** (teach). Claude Code can store approved shell commands in `.claude/settings.json` or `.claude/settings.local.json`. If you approve a `curl` carrying a key, the URL and key are saved with it, and "These settings files can then be committed to a repository without the same `.gitignore` safeguards" developers give `.env` (S048).
- **MCP config files leak keys** (brief). GitGuardian's State of Secrets Sprawl 2026 (S048's companion report, data for calendar 2025) found 24,008 unique secrets exposed in MCP configuration files on public GitHub, 14% of them PostgreSQL connection strings. Setup guides put keys inline in these files (S048). Keep the numbers to those two; the batch reader's "2,117 still valid" comes from the full PDF and is not on the landing page re-read on 2026-10-12.
- **Tool logs and chat** (brief). A Cursor user on 2026-09-02: "The Agent itself admitted the PAT was printed in the tool log (Data Sharing was enabled)"; Cursor staff: "Rotating the token and moving it to `GITLAB_TOKEN` was right" (S023). Treat any secret that appears in agent output as leaked.
- **Your AI tool's login is a key** (brief). The ChainDrop npm worm (2026-08-04) searched for `.claude/credentials.json`, `.claude.json`, `.codex/auth.json`, `.cursor/credentials.json`, `.gemini/.env`, `.kiro/settings/mcp.json` and others (S061).
- **`.gitignore` does not stop AI tools** (one line). OWASP: "`.gitignore` only affects git -- AI tools read from the filesystem directly"; list sensitive files in the tool's own exclusion file (`.cursorignore`, `.copilotignore` or equivalent) (S042, last updated 2026-10-04). Depth: keeping keys away from the agent is 07.03.
- **A key pasted into the chat is saved in plain text** (one line). Every message, tool use and result of a Claude Code session is written to a plaintext JSONL transcript under `~/.claude/projects/` (S101), so a key you paste into the chat stays there; treat it as leaked and rotate it. OWASP: don't paste keys into a terminal the agent can read (S042). (Aaron's own records include this leak, but research/sweep/aaron.md marks that record sensitive: tell it generically, never as his story, unless he clears it.)
- **Builders catch pasted keys** (one line). Paste a key into Lovable's chat and "Lovable saves your key as a project secret when you send the message" (S212): pasting keys into chat is common enough that builders built for it.
- **The leak rate, with its trend** (one line). GitGuardian reports Claude Code co-authored commits leaked secrets at about twice the baseline in 2025 (S048 companion). The batch notes record that the rate converged with the human baseline by December 2025; teach it as 2025 history, not as a fact about today.
- **Leaks outside the repository** (one line). About 28% of incidents originate in collaboration and productivity tools rather than code repositories (S048 companion).
- Dropped here: secrets in prompts and agents asked to reveal keys (07.03, C082); OWASP's audit-log redaction rule (04.04).

### C071 A leaked secret stays live until you revoke and rotate it

- **Deleting does not un-leak** (teach). The key stays in git history and keeps working until it is revoked. GitGuardian tracked valid secrets detected in 2022: 64% were still valid four years later (S048 companion report). One n8n workflow backed itself up to a public GitHub repository, with a hard-coded SSH deployment key in it (S048).
- **The steps, in order** (teach). Revoke the token first; work out "which workflows, data, and downstream credentials the account could access"; review for unauthorised changes; rotate connected credentials "where exposure cannot be ruled out" (S048).
- **Read the usage, because nobody else is watching** (brief). METR's stolen API key was used "over the course of three weeks", consuming credits worth about $600,000, and the attacker added an SSH key to keep access (S046, 2026-08-31). The provider dashboard's usage log for that key is where you look.
- **Making the repository private does not fix it** (brief). GitHub reports partner secrets found in public repositories to the issuer so it can "revoke or rotate the credential before it can be abused"; in private repositories you get an alert someone has to act on (S047, 2026-10-05).
- **After malware, the order flips** (brief). ChainDrop installed a monitor that polled GitHub every 60 seconds for 24 hours and ran an attacker's handler when the stolen token was revoked. So: remove the persistence first, rotate from a separate clean machine (AI tool credentials included), and reinstall with install scripts disabled (`npm ci --ignore-scripts`) (S061). How such packages get in is 07.04.
- **A keys question people really ask** (one line). "My keys are only stored on my laptop and on my server, not on github", yet they leaked (S155, 2026-09-25): the places in C070 are the answer to look through.
- Dropped here: the fake-CAPTCHA clean-up checklist (07.04, C093).

## You vs the agent

As of 2026-10-12:
- **The agent** wires variables in each environment, moves secret calls to server code, searches the built bundle for key patterns (S045), reads a setting inside a running container with `printenv` (S213), adds its own tool files to the ignore lists and runs a secret scanner before a push when told to, finds every place a key is used, lists what to rotate and updates configuration after a rotation (S048). All checkable: ask for the evidence.
- **You** own the provider dashboards: you create keys and set their restrictions, expiry and caps, and you see which APIs are enabled on a cloud project, which the agent cannot (S020). You decide what is allowed to be public. You know which files your agent tools write and look at them before a repository goes public (S048). You keep keys out of commands you approve (S048). Revoking and rotating is yours because only the account owner can, and after malware you do it from a clean device (S061).
- **Bring in an expert** when production credentials or other people's data were exposed, or malware ran (S061), and for cloud access management across many projects (S020). How to brief one is 04.04.

## Sources this lesson is built from

- S020 — Joe Leon (Truffle Security), "Google API Keys Weren't Secrets. But then Gemini Changed the Rules." (2026-02-25; page metadata 2026-10-08) https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules — a key's power is what it reaches today; "Unrestricted" defaults; restrict and rotate.
- S048 — Guillaume Valadon (GitGuardian), "Leaked n8n API Tokens Exposed Live Instances to Credential Theft", The Hacker News (2026-08-05) https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html — one token reaches the whole account; approved commands saved in `.claude/settings*.json`; expiry; revoke-assess-review-rotate. With its companion, GitGuardian, "The State of Secrets Sprawl 2026" (PDF created 2026-03-25, data for 2025) https://gitguardian.com/state-of-secrets-sprawl-report-2026 — MCP config leaks, the 64% still-valid figure, the co-authored-commit rate, leaks outside repositories. Credit both on screen.
- S213 — Stoneage; reply by Anshul_Namdev, "Whatsapp Trigger not working because i am running n8n with docker on local machine", n8n community (2026-07-12) https://community.n8n.io/t/302932 — a setting that never reached the program; restart vs redeploy; check with `printenv`.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — AI tool logins as stolen keys; remove persistence before rotating, from a clean machine.
- S212 — Lovable, "Lovable docs: Glossary, Secrets, Git sync and Custom domains" (undated live docs; read 2026-10-12) https://docs.lovable.dev/features/secrets.md — `VITE_` values public by design, `.env` committed on purpose, Secrets that never reach the browser, pasted keys saved as secrets.
- S045 — Vercel, "v0 security" (last updated 2026-10-09) https://v0.app/docs/security — `NEXT_PUBLIC_` exposure, moving calls server-side, separate development and production keys.
- S044 — Gal Nagli (Wiz Research), "Hacking Moltbook: The AI Social Network Any Human Can Control" (2026-02-02) https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys, with Supabase, "Row Level Security" docs https://supabase.com/docs/guides/database/postgres/row-level-security — publishable vs secret keys (one point).
- S023 — Brunno Oliveira Prego; reply by Mohit (Cursor staff), Cursor forum thread 170277 (2026-09-02) https://forum.cursor.com/t/170277 — a token printed into an agent's tool log (one point).
- S047 — GitHub Changelog, "Secret scanning adds detectors for Lovable, Supabase, and more" (2026-10-05) https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more — public vs private repositories after a leak (one point).
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — a stolen key used for three weeks before anyone noticed (one point).
- S042 — OWASP Cheat Sheet Series, "Secure Coding with AI Cheat Sheet" (created 2026-05-05, updated 2026-10-04) https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html — `.gitignore` does not stop AI tools (one line).
- S209 — MIT Missing Semester, "Packaging and Shipping Code" (IAP 2026, lecture 2026-01-20; foundational and still current) https://missing.csail.mit.edu/2026/shipping-code/ — configuration at runtime; secrets out of version control.
- S155 — par, "Ask HN: Anyone else's OpenAI and Claude API keys mysteriously leaked last night?" (2026-09-25) https://news.ycombinator.com/item?id=49845022 — a real beginner question.
- S153 — Aaron Orelup, typed prompts in his recorded Claude Code history (2026-09-30 and 2026-10-02; Playback, not public) — the course maker's own question about keeping keys out of plain text (question only; quote the topic, not the session).

Sources were re-opened on 2026-10-12 for this spec. Corrections found: the 64%, MCP-config, co-authored-commit and outside-repository figures that concepts.md cites as S048 are in GitGuardian's companion report, not in The Hacker News article; credit the report by name when they are shown. The ngrok and `printenv` points concepts.md gives to S066 are in S213.

Added by the 2026-10-12 audit (credit on the lesson page):
- S101 — Anthropic (Claude Code docs), "How Claude Code works" (undated live docs; read 2026-10-12) https://code.claude.com/docs/en/how-claude-code-works — transcripts are plaintext JSONL under `~/.claude/projects/`, so a pasted key stays there (C070).

## Show it for real

- In a throwaway Vite or Next.js app, set a dummy `VITE_` / `NEXT_PUBLIC_` value, build, and find it in DevTools > Sources; set a dummy server-only value and show it absent: proves build-time values ship to every visitor (S212, S045).
- In a throwaway project, approve an agent's `curl` carrying a dummy key, open `.claude/settings.local.json` to show it saved in the allow list, then `git status` showing the file ready to commit: proves an approval can be a leak (S048).
- Commit a dummy key, delete it in the next commit, run `git log -p`: proves deleting does not un-leak (S048).
- Docker Compose (or Portainer) on a local test service: change a variable, restart, `printenv` shows the old value; redeploy, `printenv` shows the new one: proves restart is not redeploy (S213).
- A provider dashboard for a test key: the revoke button and the key's usage log: proves where revoking and checking happen, and that only the owner can (S048, S046).
- Google Cloud Console on a test project: the Credentials page warning on an unrestricted key, then adding an API restriction: proves a key's reach is a setting you own (S020).
- File Explorer with hidden files shown: the `.claude`, `.codex` and `.cursor` folders in the home folder, never opened on screen: proves AI logins are files a stealer can look for (S061).
- No real key on screen, ever: dummy values only, and blur any account ID.

## Questions this lesson answers

- Asked in the wild: "Anyone else's OpenAI and Claude API keys mysteriously leaked last night?... My keys are only stored on my laptop and on my server, not on github" (S155, 2026-09-25).
- Asked in the wild: "the test url and production url is showing local host even after setting ENV to ngrok url in portainer" (S213, 2026-07-12).
- Asked by the course's own maker: "how to have your applications use your log ins and keys without having to store them in plain text" (S153, Aaron's prompt, 2026-09-30); this lesson answers where keys may live, and the-narrowest-keys-and-verbs (07.03) answers it for the keys your agents and scripts use on your machine: a secret store or password manager instead of a plain-text file (S042).
- Likely phrasing (batch readers, not yet seen in a post): "Is it safe to put my Google Maps API key in my website?", "What is the difference between the publishable and the secret key?", "Why is my environment variable undefined in the browser?", "Should `.env` be in `.gitignore`?", "Is it safe to commit my `.claude` folder or my MCP config?", "The agent printed my token. What do I do?", "I pushed my API key to GitHub. Is deleting the commit enough?"
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- The browser / server / database map → what-runs-where
- Local, preview and production as separate places, each with its own dashboard values → from-your-laptop-to-a-url
- RLS and testing the database as an anonymous stranger → test-it-as-a-stranger
- Secret scanners as a floor, and the pre-ship check of what your tools will commit → before-you-ship-who-signs-off
- Keeping production keys out of where the agent runs, secrets in prompts, password managers for agents → the-narrowest-keys-and-verbs
- Spend caps, and a stray key in your environment switching your bill → know-your-meter
- Malicious packages, install scripts, fake CAPTCHA pages → other-peoples-code
- Hidden dotfiles and the home folder → the-folder-is-the-agents-world
- Git history, commits and remotes → save-points-and-the-agents-trail
- PATH and "not recognized" → where-your-agent-works
- The accounts that own each key (2FA, recovery, a second owner) → every-automation-runs-as-someone
- An AI feature's key spent by strangers → your-apps-ai-feature

## Out-of-date framings to avoid

- "Google Maps and Firebase keys aren't secrets, so paste them in your HTML." (S020)
- "A key only does what it was created for." (S020)
- "Environment variables are always secret" / "`.env` files are always secret." (S045, S212)
- "A minified bundle hides what's inside." (S044)
- "I changed the setting, so the program has it" and "restarting applies my change." (S213)
- "`.env` is the only file with secrets." (S048)
- "`.gitignore` keeps secrets away from the AI." (S042)
- "I deleted the commit, so the key is safe." (S048)
- "Making the repo private fixes it." (S047)
- "Change your passwords right away, from the same computer." (S061)
- "AI commits leak twice as much", stated as today's fact: it is 2025 data that had converged by year end (S048 companion).
- "It's just my n8n key." (S048)

## Legacy notes

Legacy lesson 01.05 "Environment variables & PATH" (`01-05-environment-variables-path`, published 2026-10-10, narrator RClayton) covers the local half of C126 for now. What it gets right: every program starts with a copy of its parent's environment (its "satchel" metaphor), changes only reach programs started afterwards, keys in the environment travel to every program and agent started from that shell, and an `ANTHROPIC_API_KEY` variable changes which account pays. Its PATH and "which python" material belongs to where-your-agent-works (C122), not here. What is missing for this slot: hosting dashboards with values per environment; build-time prefixes (`VITE_`, `NEXT_PUBLIC_`) baked into the public bundle; `.env` as a convention that one major builder commits on purpose; restart vs redeploy in a container (S213); publishable vs secret keys; the leak paths that come with agents (approved commands, MCP configs, tool logs, AI logins); and revoke-then-rotate. Its dated attack examples (s1ngularity, Shai-Hulud, npm's December 2025 token revocation) are not in sources.md; the rebuild uses ChainDrop (S061, 2026-08-04) instead. Its satchel metaphor can carry over for the C126 segment, with the break it already names: an environment cannot be sealed.
