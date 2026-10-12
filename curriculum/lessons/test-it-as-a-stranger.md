---
key: test-it-as-a-stranger
id: 04.02
title: Test it as a stranger
district: Going Live
module: 04 Safe for strangers
status: todo
legacy: []
minutes: 11
concepts: [C067, C068, C119]
sources: [S044, S148, S152, S216, S055, S039, S041, S043, S045, S046, S059, S142, S149, S150, S151, S218, S219, S220]
lead: [S044, S148]
---

# Test it as a stranger

**Purpose (the first spoken sentence):** In this lesson you'll learn why being logged in is not the same as being allowed, how to test your app and its database the way a stranger would, and where your users' data really ends up.

**Conclusion:** Every request must be checked on the server, your database and file storage answer anyone holding the public key unless grants and row-level security say no, and your users' data also sits in logs, analytics, AI providers and backups; so have every table and bucket tested as an anonymous stranger after every schema change, collect less, and know every copy.

**Where it sits on the map:** District 2 · Going Live — How do others safely use it?; module 04 Safe for strangers (after 04.01 named the red zones; this lesson walks into two of them, permissions and personal data).

**Lead source (audit, 2026-10-12):** S044 (Gal Nagli (Wiz Research)); S148 (Supabase (inian; replies by avallete and maintainers)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S044, S148, S152, S216, S055); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Timing note (dated):** Supabase applies its new default (no automatic grants on new tables) to all existing projects on 2026-10-30 (S148). The generation plan puts this lesson around 2026-10-24. If it is made before that date, say "on 30 October"; if after, say "since 30 October". Re-open S148 before recording in case the date moves; as of 2026-10-12 the page shows no change and comments run to 2026-10-11.

## What to teach (binding scope)

Rough time budget: C067 3.5 min · C068 4.5 min · C119 3 min. The metaphor should carry "the stranger at the door who never uses your front hall" (the UI) and calls the back rooms (API, database, storage) directly.

### C067 Logged in is not allowed

1. **Authentication is who you are; authorisation is what you may do.** Broken access control is the largest category in the biggest 2026 audit: 339 of 1,186 vulnerabilities (28.58%), found in 64% of apps, and 261 of those 339 (76.99%) in backend code. Authentication failures are a separate class (176). (S039) — **teach**
2. **The screen is not the boundary.** A pentester's pattern: the AI builds a frontend with role-based UI elements, but call `GET /api/admin/users` directly and no middleware checks the role; his textbook case was a SaaS app where every access control was client-side JavaScript. Attackers skip your UI and call the backend directly. (S149, S044) — **teach**
3. **Check every request, for every object, on the server.** Changing an ID in a request to someone else's must be refused (an insecure direct object reference, IDOR). A practitioner checklist states the test: try updating another user's record by changing the ID in the request. Claude Code's end-of-turn review looks for authorisation bypass and IDOR, but it is advisory and can miss issues. (S220, S043) — **teach**
4. **Business rules live on the server.** Price, role and quota are set by server code, never trusted from the browser; the checklist's version is "no mass assignment" (a user must not be able to set `role=admin` by sending it). A real audit of a client's project, from a Hacker News thread about clients who took over development by vibe coding, found anyone having admin access, being able to set their own price during checkout, and leaking personal data. (S220, S142) — **teach**
5. **Real outcomes to show.** An app featured on Lovable's Discover page had inverted authentication logic that gave anonymous users full access while blocking signed-in ones, exposing 18,697 user records. (S150) — **brief**
6. **Auth can fail open, silently.** METR's researcher app sat behind Google login, but a fail-open bug silently disabled authentication and the app stayed reachable for several days. So test logged out, from outside, after every deploy, and require auth that denies access when anything errors. (S046) — **teach**
7. **Some designs need a redesign, not a patch.** Multi-tenant data with no tenant isolation in the database is "an architectural flaw that no amount of patching can fix". (S149) — **one line**, with the hand-off to an expert (04.04)
8. If you build an MCP server or an API others connect to, its auth rules come from the 2026-07-28 MCP spec (no token passthrough, minimal scopes). (S059) — **one line** (backlog: "Building MCP servers other people use")

### C068 Your database is directly reachable: test it as a stranger

1. **Your browser talks to the database's API directly.** With Supabase-style backends, the project URL and publishable key ship in the JavaScript bundle; anyone can read them and send their own queries, skipping your UI. That is how Wiz got into Moltbook: by browsing like a normal user and reading the production bundle. (S044) — **teach**
2. **The publishable key is public by design; row-level security (RLS) is the lock.** With RLS configured, the key "acts like a project identifier"; without policies, it grants full database access. A protected table answers an anonymous request with an empty array or an authorisation error; Moltbook's answered as if the caller were an administrator. With RLS on and no policies, the publishable key gets no data. (S044; Supabase RLS docs, see Sources) — **teach**
3. **Access has two layers.** Grants decide whether a role can reach a table, view or function at all; RLS decides which rows. Supabase says to use both on every exposed object. Adding policies does not take grants back: a table protected only by policies still hands `anon` an insert path if the grant is never revoked. (S152; Supabase RLS docs) — **teach**
4. **The defaults are changing now.** On older projects, a new table in `public` gets select, insert, update and delete for `anon`, `authenticated` and `service_role`. New projects stopped doing that from 2026-05-30. On **2026-10-30** the new behaviour reaches every existing project, but only for tables created after that date: existing tables keep their grants and stay reachable, so the change closes nothing that is already open. Supabase made the change because agents, CLI scripts and AI platforms now create tables, often without a human reviewing the diff. After it, a missing grant returns error `42501` with a hint naming the exact `GRANT`; the agent can fix that by itself, but whether `anon` should have the grant is your decision. A maintainer warns that restoring the old defaults puts you back in the "everything is exposed unless you remember to revoke" posture. (S148) — **teach**
5. **Reading is not writing.** Moltbook was fixed in several rounds (four fixes in Wiz's timeline) over roughly three hours from the first report; after the first read fixes, the tables were still writable, and the researchers edited a live post with a PATCH request before writes were blocked; the last round came after they found still more open tables. Wiz's lesson: write access is a far greater risk than exposure alone. Test select, insert, update and delete, as a stranger and as a different signed-in user. (S044) — **teach**
6. **Files are data too.** Test storage buckets the same way, including storage an earlier version of the app left behind. In the Tea breach, an unsecured Firebase storage bucket in a legacy system that had not been properly secured or wiped let anyone download about 72,000 images, about 13,000 of them selfies and government ID photos. (The explainer does not say Tea was AI-built; teach it as a data case.) (S216) — **teach**
7. **Views and functions can leak around RLS.** Views bypass RLS by default because they are usually created by the `postgres` user; on Postgres 15+ `security_invoker = true` makes them obey the underlying policies. A security-definer function in an exposed schema is callable over the API with its creator's privileges; RLS does not apply to functions, so grant `EXECUTE` only to roles that need it. (Supabase RLS docs; S152) — **brief**
8. **Every schema change reopens the question.** Lovable's docs say to review RLS before publishing and after changes to authentication or database structure, and its scan shows "Up to date" only while results match the current version. Every new table an agent creates is a new door. (Lovable Docs, see Sources; S148) — **teach**
9. **The dashboard flags; it does not certify.** Supabase's Security Advisor flags affected tables and a Data API exposure badge appears in the Table Editor; Supabase itself says verifying RLS correctness "has always been a gap", and its RLS Tester preview is paused. The stranger test stays yours to run (have the agent run it). (S148, S151) — **brief**
10. **Keep public apps away from private data.** Moltbook kept agent API tokens, owner emails and private messages (some holding other people's OpenAI keys) in one exposed database. After a bug in its public viewer's read-only query feature could reach unpublished data, METR built an isolated public production environment, separate from its internal systems. (S044, S046) — **brief**

### C119 Your users' data: collect less, know every copy, delete for real

1. **Draw a data map.** Every place a user's data lands: the database, storage buckets, logs, error trackers, analytics, the AI provider you send it to, backups, and any system an earlier version left behind. OWASP's 2026 list treats logs, telemetry, traces and tool-call arguments as disclosure channels in their own right. (S216, S055) — **teach**
2. **Logs and traces are copies nobody reviews.** AI-generated error handlers dump full request objects, passwords included, into plaintext log files (S149); "never log tokens, passwords, full request bodies, or PII" (S218); LLM observability platforms log full prompts, completions and traces by default, so restrict and scrub logs and traces before they reach monitoring tools (S055, LLM02:2026). — **teach**
3. **Collect only what you can protect.** Tea told users ID images were deleted immediately after review; they were still there. For AI calls, OWASP's rule is to send only the fields the task needs to external providers. (S216, S055) — **teach**
4. **Strip location data from uploaded images.** Some leaked Tea photos kept GPS coordinates, and at least one person reportedly used them to map users' approximate locations. (S216) — **brief**
5. **The privacy policy must match the system, and deletion is a job you verify** in every copy on the map, backups and leftover systems included. The Tea lawsuits (at least ten) include claims of negligence and misrepresentation of data practices. (S216) — **brief**
6. **Sending users' data to an AI API makes that vendor a recipient.** — **one line**, owned by 04.03 (C131: ask first)
7. **A leak starts legal clocks.** Under the GDPR, a controller notifies the supervisory authority within 72 hours of becoming aware of a breach, unless it is unlikely to risk people's rights and freedoms; rules differ by country and state. (S219) — **one line** (backlog: "Your users' data and the law"; a lawyer's job)

## You vs the agent

As of 2026-10-12:

- **The agent does on its own:** writes server-side middleware, RLS policies and grants; revokes default grants; sets `security_invoker` on views; enables RLS on new tables with an event trigger; writes tests that call protected routes with no session and as a second user; runs the anonymous-key `curl` test against every table and bucket; builds the data map from code and configuration; adds log redaction, strips image metadata and writes deletion jobs it can prove with a query against every store. (S043, S044, S148, Supabase RLS docs)
- **You must:** decide who may read and change what, including business rules such as "the price comes from the server", which the agent cannot infer (S142, S149); require the stranger test against the **live** project, for all four operations, on every table, view, function and storage bucket, including storage left from earlier versions, and again after every schema change and every deploy (S044, S046, S216); confirm it yourself once with two test accounts and a logged-out private window (S046); know which Supabase default your project uses and say no to blanket grants (S148); decide what data to collect at all, own the privacy policy and check it against the data map (S216).
- **Bring in an expert** (how: 04.04, C118): a security tester for auth design in anything others depend on (logins, payments, multi-tenant data) (S041, S149); a privacy lawyer or data-protection officer for health, biometric or children's data, for EU users at scale, and as soon as a leak is suspected (S219).

## Sources this lesson is built from

- S044 — Gal Nagli (Wiz Research), "Hacking Moltbook: The AI Social Network Any Human Can Control" (2026-02-02) https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys — the publishable key in the bundle, RLS as the lock, about 4.75 million records, several rounds of fixes over roughly three hours, writes still open after reads were fixed. Older than 3 months but the largest 2026 incident on this layer. Re-read 2026-10-12.
- S148 — Supabase (inian; replies by avallete and maintainers), "Breaking Change: Tables not exposed to Data and GraphQL API automatically" (2026-04-28; comments to 2026-10-11) https://github.com/orgs/supabase/discussions/45329 — the 2026-05-30 and 2026-10-30 dates, existing tables keep their grants, the 42501 hint, agents creating tables without review. Re-read 2026-10-12.
- S152 — Supabase, "Securing your API" (live docs, modified 2026-10-12) https://supabase.com/docs/guides/api/securing-your-api — grants vs RLS, both on every exposed object, functions use `EXECUTE` grants. Re-read 2026-10-12.
- S216 — Gene Petrino and Ozzie Enriquez (Security.org), "Tea App Data Breach" (2026-07-08) https://www.security.org/identity-theft/breach/tea-app/ — the legacy storage bucket, kept ID photos, GPS metadata, lawsuits. Re-read 2026-10-12.
- S055 — OWASP GenAI Security Project, "OWASP Top 10 for LLM Applications 2026" (2026-08-04) https://github.com/GenAI-Security-Project/GenAI-LLM-Top10 — LLM02:2026 Sensitive Information Disclosure: logs and traces as disclosure surfaces, minimise what goes to providers, scrub logs before ingestion. Re-read 2026-10-12 from `2026/final/`.

Also cited for single points (credit on the lesson page):
- S039 — Deng, Fan, Meng, "Understanding the (In)Security of Vibe-Coded Applications" (v4 2026-09-14) https://arxiv.org/abs/2606.23130 — broken access control counts. Re-read 2026-10-12.
- S149 — Simon Roses Femerling (VULNEX), "The OWASP Top 10 for Vibe-Coded Applications (Part 2)" (2026-04-23) https://simonroses.com/2026/04/the-owasp-top-10-for-vibe-coded-applications-part-2/ — role-based UI with no backend check, client-side access control, tenant isolation as redesign, logs. Use only its quoted lines (read through a summarising fetch). Re-read 2026-10-12.
- S220 — boxed-dev, "vibe-coding-security" pre-launch checklist (latest commit 2026-08-09) https://github.com/boxed-dev/vibe-coding-security — the change-the-ID test and mass assignment. A small project that also sells a paid add-on; used for its concrete tests only. Re-read 2026-10-12.
- S142 — HyprMusic in "Ask HN: Client took over development by vibe coding. What to do?" (2026-04-01) https://news.ycombinator.com/item?id=47599303 — the audit findings. Correction: the comment does not say the project was a marketplace (concepts.md does); say "a client's project".
- S150 — Allison Steffens Herrera (The Next Web), "Lovable left thousands of projects exposed for 48 days..." (2026-04-21) https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed — inverted auth logic, 18,697 records. Incident report only. Re-read 2026-10-12.
- S046 — METR, "Update on Security at METR" (2026-08-31) https://metr.org/blog/2026-08-31-security-update/ — fail-open login; isolated public environment. Re-read 2026-10-12.
- S043 — Anthropic, security-guidance plugin docs (modified 2026-10-09) https://code.claude.com/docs/en/security-guidance — the end-of-turn review looks for authorisation bypass and IDOR, advisory only.
- S151 — Supabase (joshenlim), "Feature Preview: RLS Tester" (2026-04-24; paused, confirmed in a 2026-08-26 comment) https://github.com/orgs/supabase/discussions/45233 — verifying RLS "has always been a gap". Re-read 2026-10-12.
- S218 — Chizee (DEV Community), "You're Doing Vibe-Coding Wrong. Here's the 17-Point Fix." (2026-09-20, edited 2026-09-23; year inferred) https://dev.to/chizee/youre-doing-vibe-coding-wrong-heres-the-17-point-fix-e9h — what never to log. Re-read 2026-10-12.
- S219 — GDPR Article 33 via gdpr-info.eu (applies since 2018-05-25; foundational and still current) https://gdpr-info.eu/art-33-gdpr/ — the 72-hour clock.
- S059 — MCP project, "Security Best Practices" (spec revision 2026-07-28) https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices — one line only.
- Not yet in sources.md (proposed): Supabase Docs, "Row Level Security" (live docs, undated, read 2026-10-12) https://supabase.com/docs/guides/database/postgres/row-level-security — RLS on with no policies returns no data; policies do not revoke grants (the `anon` insert path); the secret key bypasses RLS; views bypass RLS by default and `security_invoker`; security-definer functions; event triggers. **Correction for concepts.md:** C068 and C065 credit these mechanism points to S044, but the Wiz post does not contain them (checked 2026-10-12); this Supabase page does.
- Not yet in sources.md (proposed): Lovable Docs, "Security" (live docs, undated on the page, read 2026-10-12) https://docs.lovable.dev/features/security — review RLS before publishing and after auth or database changes; "Up to date" only for the current version. **Correction for concepts.md:** C068 and C072 credit these points to S045, which is Vercel's v0 page and does not contain them.

## Show it for real

- In a throwaway Supabase project, create a table without RLS; `curl` `/rest/v1/<table>?select=*` with the publishable key in the `apikey` header and watch rows come back; enable RLS with no policy and rerun to get `[]`. Proves the publishable key is a project identifier and RLS is the lock (S044; Supabase RLS docs).
- Send a POST or PATCH with the same key to a table that has a read policy only. Proves reading is not writing (S044).
- Create a view over an RLS-protected table and query it with the same key; then set `security_invoker = true` and query again. Proves views can leak around RLS (Supabase RLS docs).
- In a test project on the new default, create a table, trigger the `42501` error and show the hint naming `TO anon`. Proves the agent will be handed a grant fix it can apply by itself (S148).
- Open Security Advisor and the Table Editor's Data API exposure badge. Proves the dashboard flags but the stranger test is still yours (S148, S151).
- On your own local app with two test accounts: as account A, "Copy as cURL" an API request in DevTools, change the record ID to account B's, replay it, and see whether the server refuses. Proves logged in is not allowed (S220, S039).
- In a private window, request a protected page or API route with no cookie: expect a 401 or a redirect, not data. Proves the stranger's view, and catches a fail-open login (S046).
- Request a stored file's URL from a private window, then try to list the bucket with the publishable key. Proves files are data too (S216).
- Upload a phone photo, show its GPS fields, then show them gone after the agent's fix. Proves the metadata copy (S216).
- Grep the app's logs for the test password the agent typed during testing. Proves logs are a copy (S149, S218).
- Have the agent draw the app's data map, then check one entry by hand. Proves you know every copy (S216, S055).
- Use throwaway projects, test accounts and fake data only; mask the project URL; never show a real secret key.

## Questions this lesson answers

Asked in the wild:
- "What is the corresponding setting in the config file for local dev?" and whether `auto_expose_new_tables = true` is "a permanent solution" — no: maintainers call it a temporary migration aid and it is removed on 2026-10-30 (S148, comments 2026-04-28 and 2026-06-12).
- How do I roll back after opting in, when my new tables broke? Supabase's FAQ answers with grants, and a maintainer warns what restoring the old defaults means (S148).
- Supabase cites repeated GitHub discussions asking how to verify RLS (S151).
- "What to do?" after a client vibe-coded the product: the answer was an audit with exactly these findings (S142, 2026-04-01).

Likely phrasing (proposed by the research batches, not observed being asked):
- I have a login. Why can someone see other people's data? What's the difference between authentication and authorization?
- Is it safe that my Supabase key is in my frontend code? (Yes for the publishable key, if RLS and grants are right; never for the secret key.)
- How do I know whether my database is open to the world?
- I enabled RLS, so why can anonymous users still insert rows?
- Do new tables get my security settings automatically? Does Supabase's October change fix my exposed tables?
- My table has RLS. Can a view still leak?
- Can my public site and my private data share a database?
- How do I really delete a user's data? Do I need a privacy policy? What happens if my app leaks users' data?

<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- What runs where (browser, server, database) → what-runs-where (03.01, C125)
- Publishable vs secret keys and where each may live → keys-public-secret-and-leaked (03.02, C069)
- A public URL is found and probed; apps public by default → from-your-laptop-to-a-url (03.03, C063)
- Undo and backups have limits → from-your-laptop-to-a-url (03.03, C098)
- Sending users' data to an AI provider: ask first → your-apps-ai-feature (04.03, C131)
- Webhooks, rate limits, uploads and debug mode in the release inventory; how to bring in a tester or privacy lawyer → before-you-ship-who-signs-off (04.04, C066, C118)
- Weakening fixes (key swaps, blanket grants) → working-is-not-secure (04.01, C065)
- Where your own data goes when you use AI tools → where-your-agent-works (01.02, C103)
- Backlog: "Your users' data and the law"; "Building MCP servers other people use"

## Out-of-date framings to avoid

- "The login page protects the data" / "it has a login, so it's private." (S039, S046)
- "The frontend hides the button, so users can't do it." (S149, S044)
- "My key is visible, so I've been hacked" and its opposite, "the anon key is harmless." (S044)
- "RLS on means secure." Grants, writes, views, functions and storage sit outside that switch (S044, S152, Supabase RLS docs).
- "Supabase tables are private until I share them" / "Supabase's October change fixes my exposed tables." Existing tables keep their grants (S148).
- "One fix closes the hole." Moltbook took several rounds, each finding more (S044).
- "Read-only access can't leak anything." (S046)
- "My database is locked down, so my users' data is safe." Tea's leak was a storage bucket (S216).
- "Deleting the record deletes the data" / "logs are internal, so anything can go in them." (S216, S149, S055, S218)
- "The privacy policy is boilerplate." (S216)
- Using Supabase's legacy key names ("anon key", "service_role key") as if they were current: Supabase's docs and Wiz's write-up now say publishable key and secret key (the service_role JWT key is called legacy); the database roles are still `anon` and `service_role` (Supabase RLS docs, S044). When the names changed is not in the sources read, so don't date it.

## Legacy notes

No legacy lesson covers this slot. Legacy 00.06 (`00-06-how-to-learn-anything-technical`) mentions Moltbook in one segment, correctly (public key in the page is normal; row-level security off opened everything; reads and writes), and RedAccess's public-by-default apps. It has none of: server-side authorisation and IDOR, fail-open login, grants as a second layer, the 2026-10-30 default change, writes vs reads as separate tests, storage buckets, views and functions, or the users'-data map. Its line that Moltbook "was fixed within hours" is true but should not be reused without the several rounds of fixes (writes stayed open after reads were closed), which are the lesson. Its forward pointers (06.02 / 06.04 / 14.03) refer to the retired map.
