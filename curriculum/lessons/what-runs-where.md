---
key: what-runs-where
id: 03.01
title: "Browser, server, database: where your app really runs"
district: Going Live
module: 03 Putting it online
status: todo
legacy: [01-06-programs-processes-services]
minutes: [4.5, 6]
concepts: [C008, C125]
sources: [S212, S039, S041, S010, S179, S003, S075, S231]
lead: [S039, S212]
---
# Browser, server, database: where your app really runs

**Purpose (the first spoken sentence):** In this lesson you'll learn where the parts of an app you build with an agent actually run (the browser, the server, the database and the outside services it calls) and why the line between a demo and a real product runs through each of them.

**Conclusion:** An app is several places at once: whatever reaches the browser is public, secrets and permission checks belong on the server, and the database is its own service with its own rules and its own history, so a code rollback does not roll back your data, and every one of those places has to be made ready the moment real users, data or money arrive.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "What runs where." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 03 Putting it online, first lesson of three (the module's map lesson: 03.02 and 03.03 build on it).

**Lead source (audit, 2026-10-12):** S039 (Junquan Deng, Zhiyu Fan, Ruijie Meng); S212 (Lovable). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S212, S039, S041, S010); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

Length note: first lesson of a module, so about 5 minutes (500-770 spoken words). It draws the map and names each place; the keys, the deploy and the security checks are taught in the lessons listed under "Introduced here".

## What to teach (binding scope)

### C125 What runs where in your app

- **You need the map, not every line** (brief, opens the mental model). Stanford's CS146S lecturer, on agent-built code: "I don't need every detail, but I need a mental model to discern good from bad", and "I should be able to see that there's a frontend and a backend" (S003, lecture of 2026-09-29). This is the course rule applied: the agent writes every part; the viewer keeps the map that lets them judge it.
- **The browser is public** (teach). The frontend is "The part of an app users see and interact with in the browser" (S212). Everything shipped there is downloaded by every visitor and can be read in their browser. Lovable's own docs say build-time `VITE_` values "are embedded into the client bundle at build time and are safe to be public", which is only true because they are meant to be public (S212). The agent knows the browser is the wrong place for secrets: in one audited app it stored OAuth tokens in front-end `localStorage` "after applying only base64 encoding" and described that choice as "suitable for demonstration" (S039). Base64 is not hiding.
- **The server and its functions keep the secrets and the checks** (teach). The backend is "where data is stored, rules are enforced, and users are signed in"; an edge function is one of the "Small programs that run your app's behind-the-scenes logic" on the host's servers (S212). Lovable's Secrets "never reach the browser" because they are "injected into your Edge Functions automatically" (S212). The 200-app audit lists "enforcing security checks on the server side" among the security rules builders never state and agents then skip (S039). Teach the placement only; how authorisation is checked on every request is 04.02.
- **The database is its own service, with its own rules and its own history** (teach).
  - It is "Organized storage for an app's data" with its own access rules: RLS, "Rules that decide which rows of data each user can see or change" (S212).
  - It does not follow your code around: "A Git branch does not give you a separate database", and a project run on your laptop with the cloud configuration "reads and writes the same backend as your published app," so "records you create or delete locally change real data" (S212).
  - Code and data come back separately: on Replit, "By default, rollbacks do not change your database", and restoring the production database "is not performed automatically through this rollback feature" (S179). One line here; the host rollback itself is 03.03.
  - The parts also ship separately: Lovable "does not deploy a changed Edge Function or run a new migration file when your commits sync", and syncing "never publishes" (S212). So "I pushed the code" can leave the functions, the database structure and the live site each in a different state.
- **Outside services: APIs and webhooks** (brief). An API is "A way for two software systems to talk to each other"; an endpoint is "A specific URL on an API where your app sends or receives one kind of data" (S212). Your server calls outside APIs with keys (03.02). A webhook is "A notification an external service sends to your app when something happens there" (S212): outsiders calling you, which is why it must be verified before launch (04.04).
- **Some values are fixed when the app is built** (one line). Build-time values are baked into the bundle every visitor downloads (S212). Taught in 03.02.
- **Local is not a copy of live, in either direction** (one line). In Lovable apps created from 2026-05-13, "the server code runs on your machine, so connector and AI calls fail locally" (S212): something can fail on the laptop and work live, as well as the reverse. This replaces the legacy "which stop broke?" habit: ask which place a behaviour is happening in, then let the agent check that place.
- Dropped here: "rolling back code" in depth (03.03, C098); where each key may live (03.02, C069); local, preview and production as separate places (03.03, C099).

### C008 Prototype vs production: the bar changes when real users, data or physics arrive

- **The moment is the trigger, and it lands on these places** (teach). The UK NCSC: for "A proof-of-concept to demo an idea to stakeholders" the "risk profile is low", and "Full vibe coding in these contexts can often be perfectly fine"; but "authentication logic for a public facing website", "Code that processes sensitive customer data" and "Anything handling secret tokens or credentials" are "a different story" (S041, 2026-06-18). Its slide-left list (authentication or authorisation logic, sensitive personal data, secrets, tokens or credentials, safety-critical code, significant consequences) maps onto the server and the database from the C125 half of this lesson (S041, S212). The NCSC also says to "architect the wider system around your code, to minimise the impact of exploitation" (S041): knowing what runs where is what makes that possible.
- **Demo shortcuts ship** (teach). In the audit of 200 publicly deployed vibe-coded apps, "Demo-oriented design accounts for 174 vulnerabilities (14.7%)": "static demo keys, or placeholder authorization logic that remains acceptable as long as the application appears to work" (S039, v4 2026-09-14). The `localStorage` token above is one of them (S039).
- **Treat a generated app as a prototype until someone has made it otherwise** (brief). The audit's conclusion: "Generated applications should be treated as prototypes and not casually exposed to real users," because no setup it tested removed every vulnerability (S039).
- **Know what the one-file demo skipped** (brief). Andrew Ng's Build with Andrew (updated 2026-07-17) teaches building web apps by prompting "with no coding required" and ends with a lesson called "Download and open your app"; it never mentions hosting, databases, keys, accounts or security (S010). Each of those is one of the places on this lesson's map. (Re-checked 2026-10-12: the course page does not say the app is a single HTML file, so do not say so.)
- **Money and hardware raise the same bar** (one line). Production circuit boards are expected to "be fully validated by multiple independent engineers" and to "have passed stringent testing before committing to a production run" (S075, Hackaday, 2026-09-05). The mains-clearance case and the safety and EMC testing points come from reader comments on that article, not the article itself; if used, say "a commenter on Hackaday". Depth is in 09.01.
- **Real teams hit this** (one line, optional). A 2026 Ask HN asked what happens when vibe-coded internal apps become widely used; the one substantive answer: apps that grow either "crash, burn, and get shut down" or "find professionals who take over the app" (S231, date inferred as early 2026).
- Dropped here, with their owners: the 91.0% / 65.77% audit headline and "small apps are not safer" (03.03, C063); hidden security rules as a cause and the prompt-replay table ("production-ready" vs "professional" prompts) (04.01, C064); hardware safety, EMC and the EU Cyber Resilience Act 24-hour duty (09.01, C109).

## You vs the agent

As of 2026-10-12:
- **The agent** builds every part and, asked, draws the map of your app: which code runs in the browser, which on the server or in functions, which database each environment points at, and which keys live where (C125). It can do a first hardening pass and list every demo-only shortcut it took (S039). All of that is checkable, so let it do it and check two lines of the map yourself.
- **You** recognise the moment: real users, real data, a public URL, money, mains power (S041, S039). You order the production pass, and you check the map against reality: what the browser actually received (DevTools), and which database a local run writes to (S212). You confirm the demo shortcuts are gone; the agent's word that they are is a claim (02.04).
- **Bring in an expert** before real users or real data touch sign-in, personal data, secrets or payments, when you cannot judge those parts yourself: the NCSC's slide-left list is the trigger (S041). For a physical product, qualified engineers and independent review before selling (S075). How to find and brief one is 04.04.

## Sources this lesson is built from

- S212 — Lovable, "Lovable docs: Glossary, Secrets, Git sync and Custom domains" (undated live docs; git-sync page names 2026-05-13; read 2026-10-12) https://docs.lovable.dev/glossary.md ; https://docs.lovable.dev/features/secrets.md ; https://docs.lovable.dev/integrations/git-sync-overview.md — the plain definitions of frontend, backend, database, RLS, API, webhook and edge function a leading builder gives non-technical users; secrets that never reach the browser; local runs that change real data; functions and migrations that do not ship with a sync.
- S039 — Junquan Deng, Zhiyu Fan, Ruijie Meng, "Understanding the (In)Security of Vibe-Coded Applications" (v1 2026-06-22, v4 2026-09-14) https://arxiv.org/abs/2606.23130 — demo-oriented design (174 vulnerabilities, 14.7%), the base64 token in `localStorage`, server-side checks as an unstated rule, "treated as prototypes".
- S041 — Toby W, Principal Security Architect, UK NCSC, "The 'vibe coding spectrum' approach to AI-assisted software development" (2026-06-18) https://www.ncsc.gov.uk/sites/default/files/2026-07/The-vibe-coding-spectrum-approach-to-AI-assisted-software-development.pdf — when full vibe coding is fine and the slide-left list that marks the production moment; oversight, not avoidance.
- S010 — Andrew Ng, DeepLearning.AI, "Build with Andrew" (updated 2026-07-17) https://www.deeplearning.ai/courses/build-with-andrew — what the leading beginner course leaves out: hosting, data, keys, accounts, security.
- S179 — Replit, "Checkpoints and rollbacks" (undated live docs) https://docs.replit.com/core-concepts/agent/checkpoints-and-rollbacks — a rollback leaves the database alone by default and never restores production data.
- S003 — Mihail Eric, Stanford CS146S, lecture transcript "advanced prompting and context engineering" (2026-09-29) https://themodernsoftware.dev/materials/9-29-26-transcript.txt — the practitioner's case for keeping a map (frontend, backend, models) instead of reading every line.
- S075 — Maya Posch, Hackaday, "Can AI Now Design PCBs That Just Work?" (2026-09-05) https://hackaday.com/2026/09/05/can-ai-now-design-pcbs-that-just-work/ — the production bar for physical products (one line).
- S231 — stosssik and replies, "Ask HN: Vibe-coded prototypes: what happens when they go into production?" (early 2026, inferred) https://news.ycombinator.com/item?id=46713673 — a real question, and a practitioner's answer about what happens when demos grow.

## Show it for real

- The agent draws the map of a small test app (browser, functions, database, an outside API, a webhook), then the viewer checks two of its lines: proves the map is checkable and the agent's map is a claim until checked (S212).
- DevTools on a throwaway app: search the loaded JavaScript for a dummy `VITE_` value (found) and for the name of a backend secret (not found): proves "the browser is public" with a real screen and no real key (S212).
- A local run of a throwaway project creates a test record, which then appears in the published app's data: proves local is not a sandbox (S212).
- Replit's checkpoint rollback dialog, pointing at the unticked "Database" option under additional rollback options: proves code and data come back separately (S179).
- Search a demo project for "demo", "placeholder", "TODO" and "localStorage", then ask the agent to list every demo-only shortcut it took: proves demo choices are findable and that listing them is the agent's job (S039).
- The NCSC article's spectrum and its slide-left list, shown as the page itself and credited: proves where the production line is drawn by a national security agency, not by the course (S041).

## Questions this lesson answers

- Asked in the wild: "Vibe-coded prototypes: what happens when they go into production?" (S231, early 2026).
- Derived from the sources, not yet seen in a beginner post (G13 notes): "What is the difference between frontend and backend?" and "What is a webhook?" (S212); "Why did testing on my laptop change real data?" (S212); "Does rollback restore my database?" (S179); "My prototype works. What changes before I let real people use it?" (S041, S039); "Is it OK that the demo has a hard-coded admin password?" (S039).
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Where each key may live, build-time values, `.env` → keys-public-secret-and-leaked
- Deploying, preview vs production, what the host's rollback does → from-your-laptop-to-a-url
- How often deployed AI-built apps are exploitable, and how fast public apps are found → from-your-laptop-to-a-url
- Why "it works" is not "it is secure", and stating the stakes → working-is-not-secure
- Authorisation checked on the server for every request, RLS, testing as an anonymous stranger → test-it-as-a-stranger
- Webhook verification, the pre-ship inventory, bringing in an expert → before-you-ship-who-signs-off
- The accounts behind each place (host, database, domain, AI provider) → every-automation-runs-as-someone
- Which machine the agent itself runs on (laptop, VM, cloud) → where-your-agent-works
- Hardware: safety, EMC and the EU Cyber Resilience Act → checking-research-numbers-and-parts
- "Done" and "secure" from the agent are claims → done-is-a-claim

## Out-of-date framings to avoid

- "My app is one program on one computer." (C125; S212)
- "Rolling back the code rolls back the data." (S179)
- "Running it locally is a safe sandbox." (S212)
- "Encoding a token (base64) hides it in the browser." (S039)
- "Ship the prototype and harden it later." (S039)
- "Building an app means getting one thing to open in the browser." (S010)
- The opposite error, "Don't use AI for anything real": the NCSC says "this isn't about saying 'don't use AI for security-critical code'"; it is about oversight (S041).
- Teaching the frontend/backend split as if the viewer will write it by hand: the agent writes every part; the viewer keeps the map (S003).

## Legacy notes

Legacy lesson 01.06 "Programs, processes & services" (`01-06-programs-processes-services`, published 2026-10-11, narrator Adrian) covers this slot only in part. What it gets right and can feed the rebuild: a server is a long-running process that waits for requests; "localhost means your own machine"; an agent's commands and the servers it starts are processes running as you. What is missing: it is entirely about one computer. It never draws the app as several places (browser, host's servers, database service, outside APIs), never says the browser is public or that secrets and checks belong on the server, never separates code from data, and never names the production moment. Its Task Manager, port-in-use and "zombie" material goes to the backlog (curriculum.md: "Processes, ports and servers on your machine"), and its dated product claims (sandbox coverage, Microsoft Execution Containers, Ollama defaults) are not in sources.md, so none of them carries over without a fresh source. The retired 00.02 "The map of everything" habit ("which stop broke?") returns here as "which place is this running in?" (curriculum.md legacy table), framed for agents: the viewer names the place, the agent checks it.
