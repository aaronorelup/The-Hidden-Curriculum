---
key: from-your-laptop-to-a-url
id: 03.03
title: From your laptop to a URL
district: Going Live
module: 03 Putting it online
status: todo
legacy: []
minutes: [10, 12.5]
concepts: [C063, C098, C099, C127]
sources: [S212, S026, S066, S046, S179, S039, S217, S208, S209, S099, S225, S142, S145, S045, S213, S253]
lead: [S026, S046]
---
# From your laptop to a URL

**Purpose (the first spoken sentence):** In this lesson you'll learn what actually happens between your app running on your laptop and your app answering at a web address: the build, upload and switch, the domain you rent and point, why preview and production are different places, what the host's rollback can and cannot undo, and why a public address gets found fast.

**Conclusion:** Deploying puts a built copy of your app on a host that keeps the earlier versions, under a name you rent and point with DNS; the host can switch back to an earlier version in seconds, but your database and anything already sent stay as they are, and a new public address is likely found and probed within days, so decide what it may hold before it goes up.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 03 Putting it online, third lesson (after what-runs-where and keys-public-secret-and-leaked; module 04 Safe for strangers follows).

**Lead source (audit, 2026-10-12):** S026 (Aaron Orelup); S046 (METR). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S212, S026, S066, S046, S179); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

## What to teach (binding scope)

Order: localhost is not a website (C127), deploy is build-upload-switch and preview is not production (C127, C099, told through Aaron's incident), the domain (C127), what rollback leaves behind (C098), public means found (C063). Aaron's incident (S026) is the spine: tell it in the third person, with times.

### C127 From your laptop to a URL

- **localhost is only your machine** (teach). An n8n guide puts it plainly: "`localhost:5678` works on your machine and nowhere else" (S066, 2026-10-04). Agents make localhost feel like a website: "When you run your dev server in the desktop, your app opens in the Browser pane" (S208). Nobody else can reach it, and an outside service cannot call it.
- **Deploying is build, upload, switch, and the host keeps the old versions** (teach). On 2026-10-08 Aaron's site went wrong and was switched back to an earlier version with one command (`npx wrangler rollback <version> --name blog`): 8 minutes 10 seconds of outage in all (S026). MIT's Missing Semester: "the best course of action is to have a rollback plan, where the version upgrade is reverted and a known good version is redeployed" (S209). On a builder platform the switch is a button: "Publish: The action that puts your project on a public URL", and git sync "never publishes. Your live site only changes when you publish from Lovable" (S212).
- **A domain is a name you rent and point** (teach). Bought through a registrar, renewed on a term (Lovable defaults to one year, with auto-renew on and a grace period of "around 30 days" before an unrenewed domain is released). DNS records point it at the host: an `A` record to the host's address, a `TXT` record to prove you own it; "DNS changes may take up to 72 hours to propagate, though most updates are live within a few hours". If the registrant email is not verified before the deadline, the registrar can suspend the domain (S212).
- **Certificates are automatic now, but leftovers block them** (brief). Lovable "automatically generates and installs an SSL certificate", and "You do not need to install, upload, or reissue an SSL certificate from your domain registrar"; but `CAA` records "must allow Lovable to issue the certificate", and leftover `A`, `AAAA` or `CNAME` records from an old host keep showing the old site (S212).
- **Sign-in breaks until the new domain is allowed** (brief). Lovable's FAQ, "Why does sign-in fail on my custom domain?": "Your app's auth redirect URLs don't include the new domain yet." Its own backend adds the domain automatically; your own Supabase project or Google sign-in need it added by hand (S212).
- **A static site can be published free** (one line). "GitHub Pages provides free hosting directly from a repository" (S209).

### C099 Local, preview and production are different places

- **A hosting setting decides which branch becomes production** (teach, the story). A cloud agent session started from a stale default branch and pushed one post to a side branch at 00:39:08. About 40 seconds later the host built that branch and deployed it to production, because "Builds for non-production branches" was on and the build command was `npx wrangler deploy`, which replaces the live site. The site showed four posts. The fix: build only `main`, and make any other build `npx wrangler versions upload`, which "uploads a version that goes nowhere" (S026). Lesson: read your host's build settings once (the production branch, whether preview builds run, and the command each runs).
- **Test addresses and live addresses differ** (teach). n8n's test webhook URL "only listens while you have the editor open and have clicked 'Listen for test event'"; the production URL works only when the workflow is Active; "Nine times out of ten, it's the test URL or an inactive workflow" (S066). A self-hosted tool must be told its public address (`WEBHOOK_URL`) (S066), and a free ngrok subdomain changes on every restart, which breaks every webhook registered with the old one (S213).
- **Each place has its own settings** (brief). "Use different keys for development and production environments" (S045); MIT: the same codebase deploys to "development, staging, production" with "only configuration changes, never code changes" (S209). Where those values live and why a restart is not a redeploy is 03.02.
- **Test where your users are** (brief). Cloud agents spent "three days of fix-on-fix" on a sign-in integration they called working; "No test ever went through the public URL", and the live failure was a proxy rewriting a security header (S099, 2026-09-26). At least one check goes through the public address in a real browser. Aaron's own case (AO-042, S253, 2026-10-08): for two months no video on his site could skip ahead, because the live asset server answered `200` instead of `206` to range requests while the local dev server handled ranges itself, so every check on the dev server passed; his line: "Testing in the environment you have isn't the same as testing in the one your reader has" (S253).
- **"Nothing logged" means it never arrived** (one line). n8n: if "nothing is logged at all, the request never reached n8n" (S066). Checking outcomes at the destination is 08.02.
- AO-043 (S026) is told in full only here, in the third person, with times (audit, 2026-10-12); save-points-and-the-agents-trail, rules-it-reads-rules-it-cant-break, done-is-a-claim, checking-what-you-cant-read, agents-that-run-while-youre-away and green-is-not-success call back to it in one line each. Dropped here: cloud sessions see only committed files on the default branch, and rules files that were never committed (05.02 and 08.01 make that point in one line).

### C098 Undo has limits

- **The host's rollback switches code, not data** (teach). Replit: "By default, rollbacks do not change your database", and restoring the production database "is not performed automatically through this rollback feature"; before rolling back, "Consider the impact on your database and external integrations" (S179). So rows written, emails sent and payments taken by the bad version are still there after the switch back. (The last sentence is the course's reading of "external integrations"; say it as a reading, not a quote.)
- **Rehearse the rollback before you need it** (brief). A developer advising someone whose client had taken over a codebase by vibe coding asked whether "no one attempted to deploy this to a live environment yet?" and recommended deploying "together with practicing at least one rollback" (S142, 2026-04-01). In Aaron's incident the first `wrangler deployments list` failed because the Worker's name in the repository config did not match the host's, and the history did not show which deploys came from branches (S026).
- **Make "what is live" answerable** (brief). After the incident every build writes `/version.json` with the commit, the branch the host built, the build time and the newest post, so a session can compare what is live with what it just pushed (S026). Before that, in Aaron's words, "the only alarm on this site was me happening to look at it" (S026).
- **Know where the database's backups live** (brief). In April 2026 an agent deleted a startup's production database "and all volume-level backups in a single API call", in 9 seconds, because the provider "stores volume-level backups in the same volume" (S225, The Register, 2026-04-27). Ask where your provider's backups are and test a restore once.
- Dropped here: editor checkpoints that skip shell commands and backups the agent's shell can reach (before-you-let-it-loose, C097); git with no remote (save-points-and-the-agents-trail); sent messages and purchases behind approval (the-narrowest-keys-and-verbs, C084).

### C063 Public means found: your app will be probed

- **Assume it is found when it goes up** (teach). METR's research app was "exposed to the public internet for several days" with authentication silently disabled. METR suspects the attacker scanned recently registered sites, for example "certificate transparency lists", for "vibe-coded sites with high-signal keywords relating to LLMs or agents", to harvest model-provider keys (S046, 2026-08-31). "Found within days" is a fair reading of METR's account, not a measured figure: say so. (The cost of that key is told in 03.02.)
- **The probing is automated** (brief). METR also saw credential stuffing, "Attempts at OAuth token grants", "Scanning of newly deployed services" and phishing of staff, with heavy use of agents (S046).
- **Insecurity is normal in deployed AI-built apps** (brief). Of 200 publicly deployed vibe-coded apps, "182 (91.00%) contain at least one vulnerability", and "65.77% are classified as Critical or High"; each finding was confirmed by a harmless live probe and two authors (S039, v4 2026-09-14). Small apps are not safer: 0.85 vulnerabilities per thousand lines in small apps against 0.22 in the largest (S039). Why, and what to do about it, is 04.01.
- **Check your platform's default visibility before the first publish** (teach). RedAccess reported about 380,000 publicly accessible apps and assets built with Lovable, Base44, Netlify and Replit, about 5,000 holding sensitive corporate data, with some tools' privacy settings making apps accessible by default and many apps indexed by search engines. The vendors dispute that public means breached; Replit's CEO: "Public apps being accessible on the internet is expected behavior" (S217, 2026-05-07). An internal tool published this way publishes its data, no hack needed.
- **Attackers have the same models** (one line). Anthropic's red team reported that an open-weight model anyone can download builds end-to-end exploits about as often as its own restricted model (50 vs 56 of 410 attempts), with safeguards bypassed "between 64% and 100% of the time" in its tests (S145, 2026-09-29). Its benchmarks target browser engines and open-source code, not web apps, and it is a competitor's analysis: say both.
- **Going public is a decision you make before you deploy** (teach). Decide what the public site may hold (no production keys, no private data until it has been checked), check it from outside, logged out, and know that organisations now gate it: METR "Formalized a security review process for any researchers publicly deploying applications" (S046).

## You vs the agent

As of 2026-10-12:
- **The agent** runs the build and the deploy, can set DNS records through a host's API, checks the certificate, reads the hosting configuration it can reach, adds a build guard, runs the rollback and checks that key pages load, and writes `/version.json` (S026). It can set `WEBHOOK_URL` and a tunnel once you decide (S066). All verifiable: ask it to show the live page, the version and the response.
- **What it cannot do:** see settings that exist only in a dashboard it cannot sign in to (in S026 the session could not read the host's dashboard, and Aaron had to sign in himself); know whether a deploy was meant to be public or what the data is worth (S046); restore production data with a code rollback (S179).
- **You** own the registrar and hosting accounts (08.03). You decide, before the first publish, what goes public and what it may hold, and you check the platform's default visibility (S046, S217). You read the build settings once (S026). You check the live site from outside, logged out, through the public address in a real browser (S099, S046). You confirm where the database's backups live and approve a production rollback (S179, S225).
- **Bring in an expert** for a production database with real users: someone who has done a point-in-time restore on that provider should check the restore plan before you need it (Replit sends you to a separate guide for that, S179). Before other people's data goes live, a penetration test and a security review (04.04; METR's gate, S046).

## Sources this lesson is built from

- S212 — Lovable, "Lovable docs: Glossary, Secrets, Git sync and Custom domains" (undated live docs; custom-domain page names 2025-10-29; read 2026-10-12) https://docs.lovable.dev/features/custom-domain.md — registrars, DNS records, 72-hour propagation, automatic certificates and what blocks them, redirect URLs, renewals and suspensions, publish as a separate step.
- S026 — Aaron Orelup, "AO-043: A cloud session pushed one post from a branch, and my whole site went back to August" (2026-10-09; incident 2026-10-08) https://aaronorelup.com/ledger/the-branch-that-went-live/ — the lesson's spine: a hosting setting that made a branch production, a rollback in one command, the friction, `/version.json`.
- S066 — Syed Farzam Saadat, "Webhook works in test but not in production? The test vs. production URL trap", n8n community (2026-10-04) https://community.n8n.io/t/318716 — localhost, test vs live addresses, Active, "nothing logged".
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — an app found while open for several days, automated probing, a security review before public deploys.
- S179 — Replit, "Checkpoints and rollbacks" (undated live docs) https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks — rollbacks leave the production database untouched; consider external integrations.
- S039 — Junquan Deng, Zhiyu Fan, Ruijie Meng, "Understanding the (In)Security of Vibe-Coded Applications" (v4 2026-09-14) https://arxiv.org/abs/2606.23130 — 91.0% of 200 deployed apps exploitable; small is not safe.
- S217 — Jeffrey Burt (Security Boulevard), reporting RedAccess, "Thousands of Vibe-Coded Apps Exposing Corporate, Personal Data" (2026-05-07) https://securityboulevard.com/2026/05/thousands-of-vibe-coded-apps-exposing-corporate-personal-data-redaccess/ — default visibility, search indexing, the vendors' dispute.
- S208 — Anthropic, "Get started with the desktop app" (Claude Code docs, undated live docs; read 2026-10-12) https://code.claude.com/docs/en/desktop-quickstart — the dev server in the Browser pane (one line).
- S209 — MIT Missing Semester, "Packaging and Shipping Code" (IAP 2026, lecture 2026-01-20; foundational and still current) https://missing.csail.mit.edu/2026/shipping-code/ — a rollback plan, environments that differ only in configuration, GitHub Pages.
- S099 — Jeffrey Barts, Cursor forum thread 173052 (2026-09-26) https://forum.cursor.com/t/173052 — no test went through the public URL (one point).
- S225 — Thomas Claburn (The Register), "Cursor-Opus agent snuffs out startup's production database" (2026-04-27) https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442 — backups in the same volume as the data (one point).
- S142 — piscator and replies (Hacker News), "Ask HN: Client took over development by vibe coding. What to do?" (2026-04-01) https://news.ycombinator.com/item?id=47599303 — deploy "together with practicing at least one rollback" (one point).
- S145 — Anthropic Frontier Red Team, "GLM-5.3 and the spread of advanced cyber capabilities" (2026-09-29) https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities — attackers can download exploit-capable models (one line).
- S045 — Vercel, "v0 security" (updated 2026-10-09) https://v0.app/docs/security — separate development and production keys (one line).
- S213 — Stoneage; reply by Anshul_Namdev, n8n community thread 302932 (2026-07-12) https://community.n8n.io/t/302932 — a free tunnel's address changes on restart (one line).

Sources were re-opened on 2026-10-12 for this spec. Correction: concepts.md gives the ngrok and `printenv` points to S066; they are in S213. S045 (re-read) does not mention v0's Development / Preview / Production mapping, so that C099 detail is not used.

Added by the 2026-10-12 audit (credit on the lesson page):
- S253 — Aaron Orelup, "AO-042: For two months no video on my site could skip ahead, and the agent that noticed wrote a workaround" (2026-10-08) https://aaronorelup.com/ledger/every-video-can-seek/ — test where your users are: the dev server that hid a broken live server (C099). Read 2026-10-12.

## Show it for real

- The same throwaway app three ways: on localhost in the desktop app's Browser pane, on a preview URL, on production; then the localhost address typed on a phone, failing: proves localhost is one machine (S208, S066).
- The hosting dashboard's build settings for a test project: production branch, the non-production builds toggle, the build commands; push a test branch and watch it appear as a preview URL, not the live site: proves a setting decides what goes live (S026).
- On a test Worker: list deployments, roll back, then open `/version.json` and compare its commit with `git log`: proves rollback is a switch and "what is live" can be checked (S026).
- Replit's rollback dialog with the "Database" option unticked: proves the code goes back and the data does not (S179).
- A registrar's DNS panel for a test domain: the `A` and `TXT` records and the propagation note: proves a domain is a rented name you point (S212).
- Deploy a test site to a fresh subdomain and search a public certificate-transparency log for it, showing the new certificate already listed: proves a new address is announced publicly (the route METR suspects, S046; say "suspects").
- n8n: the Webhook node's Test and Production URL tabs, the Active toggle, a `curl` to each, then the Executions tab: proves test and live are different addresses (S066).
- A `site:` search for a test app's domain to see whether it is already indexed (S217).

## Questions this lesson answers

- Asked in the wild: "Webhook works in test but not in production?" (S066, 2026-10-04).
- Asked in the wild: "no one attempted to deploy this to a live environment yet?" (S142, 2026-04-01).
- From the builder's own FAQ, which exists because users ask (S212): "Why does sign-in fail on my custom domain?", "My domain shows my old website instead of my Lovable app", why a domain was suspended.
- Likely phrasing (batch readers, not yet seen in a post): "Who would ever find my little app?", "Is an unlisted URL private?", "Does rollback restore my database?", "Why did pushing a branch change my live website?" (S026), "How do I put my app online so friends can use it?" (C008), "How do I know which version is live?" (S026).
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- The browser / server / database map, and code vs data → what-runs-where
- Values per environment, restart vs redeploy, keys in dashboards → keys-public-secret-and-leaked
- Why deployed AI-built apps are so often exploitable, and stating the stakes → working-is-not-secure
- Testing the live app as an anonymous stranger → test-it-as-a-stranger
- Penetration tests, the pre-ship inventory, who signs off → before-you-ship-who-signs-off
- Branches, remotes and the default branch → save-points-and-the-agents-trail
- Cloud sessions that see only committed files, and rules that never reached them → rules-it-reads-rules-it-cant-break, agents-that-run-while-youre-away
- Editor checkpoints and backups off the machine → before-you-let-it-loose
- Checking outcomes at the destination, heartbeats → green-is-not-success
- Registrar, hosting and database accounts, 2FA, renewal emails, a second owner → every-automation-runs-as-someone
- Sent messages and purchases behind a human approval → the-narrowest-keys-and-verbs

## Out-of-date framings to avoid

- "It works on localhost, so it's live." (S066)
- "Buy an SSL certificate and install it by hand." (S212)
- "DNS changes are instant." (S212)
- "Pushing to a branch never touches the live site." (S026)
- "Rolling back fixes everything" / "the host keeps backups, so I'm covered." (S179, S225)
- "Fix forward by pushing a new commit when production breaks": a rollback is seconds (S026).
- "CI is green, so it works live." (S099)
- "Nobody will find my side project" and "an unlisted URL is private." (S046)
- "The builder keeps my app private until I publish it on purpose": check the default (S217).
- "Only well-resourced attackers can build working exploits." (S145)

## Legacy notes

No legacy lesson covers this slot. Legacy 00.02 "The map of everything" (whose five-stop road is retired as the course map) names localhost as "this computer" in passing; this lesson replaces that with the full laptop-to-URL path.
