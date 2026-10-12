# Batch 9: exposed backends and secrets (research notes)

Theme: what "the app is public" means. Open databases, keys in the browser, sites found within days, and how leaked secrets are caught.

- Read on: 2026-10-12, by the read-exposed-backends-secrets agent.
- Method: every source and companion page below was fetched and read directly. The GitHub model-detector changelog and the GitGuardian report PDF were reached through links on pages that were fetched, not through search. The shared WebSearch budget ran out partway through this batch, so no extra sources were searched for.
- Quotes: one short quote per source at most. Everything else is paraphrased.
- Machine-readable gaps: `exposed-backends-secrets.json` in this folder (one item per gap, with source IDs).

---

## S044: Hacking Moltbook: The AI Social Network Any Human Can Control

- Author: Gal Nagli (Wiz Research)
- Date: 2026-02-02 (confirmed from the byline). Disclosed to Moltbook on 2026-01-31.
- URL: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- Companion pages read:
  - Supabase Docs, Row Level Security, https://supabase.com/docs/guides/database/postgres/row-level-security (live docs, undated).
  - Supabase Docs, Securing your API, https://supabase.com/docs/guides/api/securing-your-api (live docs, undated). This page is linked from the RLS page's "Default privileges" section.

### Summary

Moltbook is a social network for AI agents, and its founder said publicly that he wrote none of its code himself. Wiz researchers used the site like ordinary visitors. In the JavaScript bundle the browser downloads (`/_next/static/chunks/<hash>.js`) they found the Supabase project URL and publishable key. They sent that key straight to Supabase's REST API and asked for the `agents` table. With row-level security (RLS) in place, that request would have returned an empty array or an authorization error. Instead it returned every agent's API key, claim token and verification code.

The researchers then mapped the rest of the schema using PostgREST error messages and GraphQL introspection, and estimated about 4.75 million exposed records. The fixes came over about three hours, in six rounds. Each round found more open tables, and after reading was locked down, the tables could still be written to.

### Gaps and specific points

1. **Anything shipped to the browser can be read, and anyone can skip your UI and call your backend directly.**
   - The connection details were hardcoded in a production JavaScript chunk that loads automatically with the page.
   - The researchers needed no special tools or intrusive testing. They read the bundle, then sent their own request to the REST endpoint.
2. **The Supabase publishable key (formerly called the anon key) is public by design. RLS is the actual lock.**
   - Wiz explains that the key acts like a project identifier and is safe to expose only when RLS policies exist.
   - Without RLS, the same key grants full database access to anyone who has it.
   - Wiz traces the root cause to one Supabase configuration setting, not to the visible key.
3. **Scale of one missing setting.**
   - 1.5 million agent API tokens, which allowed full impersonation of any agent.
   - About 35,000 email addresses: 17,000+ in the owners table, plus 29,631 early-access signups in a separate `observers` table.
   - 4,060 private DM conversations, some holding plaintext OpenAI API keys that agents had shared with each other.
4. **Locking reads is not locking writes.**
   - After the read fixes, public tables were still writable. The researchers edited a live post as a test.
   - Wiz notes that write access allows defacement and prompt-injection payloads, which can spread to other AI agents that read the content.
5. **Remediation takes rounds, and each round finds more surface.**
   - Timeline:
     - 2026-01-31 23:29 UTC: `agents`, `owners` and `site_admins` secured.
     - 2026-02-01 00:13 UTC: messages, notifications, votes and follows secured.
     - 2026-02-01 00:31 UTC: write access discovered.
     - 2026-02-01 00:44 UTC: write access blocked.
     - 2026-02-01 00:50 UTC: more tables found (`observers`, `identity_verifications`, `developer_apps`).
     - 2026-02-01 01:00 UTC: everything secured.
6. **One app's breach exposes other services' keys.**
   - Agents' DMs held OpenAI keys belonging to other people.
   - Wiz lists cascading privacy failures across AI ecosystems as one of its lessons.
7. **AI builders do not yet secure the backend for you.**
   - Wiz says today's AI tools don't yet reason about security posture or access control on the developer's behalf, so configuration needs careful human review.
   - Wiz proposes that AI assistants should enable RLS by default and that deployment platforms should scan for exposed credentials.
8. **From the Supabase docs (mechanism details the article does not give):**
   - With RLS enabled and no policies, the publishable key gets no data through the API.
   - On existing projects, a new table in `public` starts with select, insert, update and delete granted to `anon`, `authenticated` and `service_role`. The docs add that some projects do not grant these automatically.
   - The Securing-your-API page says Supabase is changing the platform default to revoke these automatic grants, so that exposure becomes opt-in. It gives no date for the change.
   - Grants and policies are separate checks. Grants decide whether a role may run an operation at all. Policies decide which rows it applies to.
   - Adding policies does not take grants back. The docs warn that a table protected only by policies still gives `anon` an insert path if the grant is never revoked.
   - A secret key (or the legacy JWT `service_role` key) runs as `service_role`, which has `bypassrls`. The docs say never to use it in the browser or expose it to customers.
   - A secret key bypasses RLS only when the request carries no user access token.
   - Views bypass RLS by default, because they are created by `postgres` as security definer. The fix is `security_invoker = true` on Postgres 15+, or revoking access, or moving the view to an unexposed schema.
   - A security-definer function in an exposed schema can be called over the Data API with its creator's privileges.
   - An event trigger can enable RLS automatically on every new table.
   - The Data API can be switched off if unused. Then none of the auto-generated endpoints respond.
9. **Unverified participation.**
   - There were about 88 agents per human owner, with no check that an "agent" was really AI and not a human running a script.
   - This is peripheral to the theme.

### Outdated framings it corrects

- "My key is visible in the page source, so I've been hacked." For Supabase's publishable key, being visible is expected. The missing policies were the bug.
- "Turn RLS on and you're done." Grants, write policies, views and security-definer functions all sit outside that switch.
- "Fixing what was reported fixes the app." Remediation found new open tables twice after the first fix.

### Quote

- "without RLS policies, this key grants full database access to anyone who has it." (Wiz, 2026-02-02)

### Corrections to the brief

- The article does not describe Supabase's defaults. Those points come from the two Supabase docs pages above.
- The automatic-grant default is changing, but the docs give no date. Teach it as "check whether your project grants automatically" and not as a fixed fact.

---

## S045: v0 security (with External APIs / environment variables)

- Author: Vercel (v0 docs)
- Date: 2026-10-09. This is the `lastUpdated` field on the Security page, confirmed. The External APIs page has the same `lastUpdated`.
- URL: https://v0.app/docs/security
- Companion pages read:
  - v0 Docs, External APIs, https://v0.app/docs/external-apis (2026-10-09).
  - Lovable Docs, Security overview, https://docs.lovable.dev/features/security (undated on the page).

### Summary

v0's security page treats every piece of generated code as possibly wrong or hostile. It analyzes code before running it, runs it in a sandbox, validates inputs and tests adversarially. It relies on Next.js's server/client split: only variables prefixed `NEXT_PUBLIC_` reach the browser. v0 warns about risky `NEXT_PUBLIC_` use and can move calls into Route Handlers or Server Actions. Its best practices are to never put sensitive tokens behind `NEXT_PUBLIC_`, to rotate keys regularly, and to use different keys for development and production.

The External APIs page explains that each variable is assigned to environments: Production (the live app), Preview (deployments from non-production branches) and Development (the v0 preview panel or local runs). The v0 preview can only see Development variables. Lovable's page describes automatic and manual scans and states plainly that they are not a guarantee.

### Gaps and specific points

1. **A naming prefix decides whether a value leaves the server.**
   - `NEXT_PUBLIC_` variables are bundled for the browser, and every visitor gets them.
   - Variables without the prefix stay server-side.
   - The fix for a key that must stay secret is to make the call from server code (a Route Handler or Server Action), not to rename the variable.
2. **Environments are separate worlds with separate keys.**
   - Each variable is assigned to Production, Preview and/or Development.
   - Name trap: the "v0 preview" panel uses the **Development** environment, while Vercel's **Preview** environment means branch deployments. Something that works in the v0 preview panel may be missing in production, and the reverse.
   - Use different keys for development and production so that a leaked development key cannot reach production data.
   - Rotate keys regularly. Variables are encrypted and stored on Vercel.
3. **The builder treats its own output as untrusted, and so should you.**
   - v0's threat model assumes generated code may be incorrect or adversarial. That is the platform protecting itself while executing code; it does not certify that the code is secure.
4. **Builder scans are a floor, not a certificate (Lovable).**
   - The Quick scan runs when you open the publish dialog. It checks database access rules, npm dependency vulnerabilities, and MCP servers exposed without authentication.
   - The Deep scan also reads application code: access control, unauthenticated endpoints, injection, leaked secrets, payments, authentication and sensitive-data exposure. It does not run automatically during development. You have to start it.
   - Auto-fix handles only Quick-scan findings (RLS, database access, dependencies). It does not fix Deep-scan findings.
   - Only critical dependency vulnerabilities become findings. Some are suppressed when Lovable judges they cannot affect Lovable apps or their EPSS score is low.
   - The page says the tools cannot guarantee complete security and do not replace a thorough security review. It says you are responsible for meeting the security requirements of your use case, and it recommends a professional review for apps that handle sensitive data or critical functions.
   - The "Trust center" page at `/.well-known/trust.html` is informational, not a certification.
   - Lovable says to review RLS policies regularly, especially before publishing and after changes to authentication or database structure.
   - The Security view shows "Up to date" only while scan results match the current project version, so you rerun scans after changes.
5. **Secrets pasted into chat.**
   - Lovable detects keys pasted into chat and steers them into its Secrets store.
   - It also moves API calls to server-side code, because code that runs in the browser cannot hold a secret.

### Outdated framings it corrects

- "The platform's security scan passed, so the app is secure."
- "Preview works, so production will too." These are different environments with different variables.
- "One API key for everything."

### Quote

- "We consider all code potentially incorrect or adversarial." (v0 docs, Security, 2026-10-09)

### Corrections to the brief

- "The preview sees only Development values" and the per-environment settings are on the **External APIs** page, not the Security page.
- The Security page does not tell users to review generated code. It describes v0's own threat model.
- The Lovable page does not use the phrase "a security review is not a certification". It says the tools do not replace a thorough security review and cannot guarantee complete security, and that the Trust center is not a certification.
- The Lovable page does not literally say "per table". It says to review RLS policies before publishing and after auth or schema changes. Its Quick scan flags tables without per-record access control.

---

## S046: Update on Security at METR

- Author: METR (no individual authors listed; the citation metadata gives author = METR)
- Date: 2026-08-31 (confirmed). The post says its described measures are accurate as of 2026-07-30.
- URL: https://metr.org/blog/2026-08-31-security-update/

### Summary

METR reports two 2026 near-misses.

- **March 2026.** A researcher's vibe-coded agent app ran on a personal EC2 instance that was public on purpose, behind Google login. A fail-open bug silently switched the login off, and the app sat open to the internet for several days. METR suspects the attacker found it by scanning recently registered sites, for example in certificate-transparency lists, looking for LLM and agent keywords. The attacker asked the agent to reveal its model-provider API key, added an SSH key to keep access, and over about three weeks used credits worth about $600,000. The credits were free to METR, so there was no spend ceiling, and the key type could not take a spending limit.
- **May 2026.** Financially motivated attackers probed METR. A read-only SQL query feature in the public transcript viewer had a bug that could have exposed unpublished data. An outside researcher reported it, and METR paid a bounty.

### Gaps and specific points

1. **Public means found. There is no obscurity window.**
   - The attacker most likely found the app by scanning newly registered sites (for example in certificate-transparency lists) for vibe-coded apps with LLM or agent keywords, to harvest model-provider keys.
   - The app was exposed for several days and was found within that time.
   - The May attackers ran automated scans of newly deployed services, along with credential stuffing, OAuth token-grant attempts and staff phishing.
2. **Auth that fails open.**
   - The app had login (Google authentication), but a fail-open vulnerability silently disabled it. Nothing looked broken to the owner.
   - The lesson implied: test from outside, logged out, and design auth to fail closed.
3. **An agent holding a key can be asked to hand it over.**
   - The attacker did not need to break into the server to get the key. They prompted the agent to reveal it.
   - Whatever an agent can read, anyone who can talk to the agent can try to extract.
4. **Keys without spend limits are a blank cheque.**
   - About $600,000 of credits were used over about three weeks.
   - The theft went unnoticed for three reasons. Large evaluations routinely produce rate-limit and API errors. The internal dashboard did not show rate-limited requests for all users. And because METR wasn't paying, no bill spiked.
   - METR added spend alerts to keys where possible.
5. **Persistence.**
   - Once in, the attacker added an SSH key so that access would survive a password or login fix.
   - METR's response included imaging the instance, rotating credentials, and imaging and wiping the researcher's laptop.
6. **Public apps must be isolated from private data.**
   - The public transcript viewer exposed a read-only SQL mechanism. It was scoped to public data by default, but a bug allowed more.
   - The database also held some more-sensitive data by accident.
   - METR restored the endpoint after a few days without noticing the bug.
   - METR then built an isolated public production environment, separate from internal infrastructure, so that a misconfigured public service cannot reach internal data.
7. **Organizational controls for people who deploy side projects.**
   - METR formalized a security review for any researcher who deploys an app publicly.
   - It set rules about putting company credentials on personal infrastructure, shortened credential lifetimes, reduced permission scopes, and added logging and anomaly monitoring on API key usage.

### Outdated framings it corrects

- "Nobody will find my side project." It was found within days of exposure.
- "It has a login, so it's private."
- "Free credits mean there is no cost risk."
- "Errors and rate limits are just noise."

### Quote

- "a fail-open vulnerability that silently disabled authentication" (METR, 2026-08-31)

### Corrections to the brief

- The post does not measure how quickly new sites are found. It says certificate-transparency scanning is the *likely* discovery method, and that the app was exposed for several days. "Found within days" is a fair reading, but it is not a measured figure.

---

## S047: Secret scanning adds detectors for Lovable, Supabase, and more

- Author: GitHub Changelog
- Date: 2026-10-05 (confirmed)
- URL: https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more
- Companion pages read:
  - GitHub Changelog, Purpose-built model for leaked secret detection, 2026-10-07, https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection. This is linked from the S047 page. The brief's "model-based detector" is described here, not in S047 itself.
  - GitHub Docs, About push protection, https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection (undated on the page).

### Summary

On 2026-10-05 GitHub added detectors for AI-builder and AI-infrastructure tokens:

- Lovable `lovable_api_key`. Lovable also joined the partner program.
- Pydantic `logfire_token` and `pydantic_ai_gateway_api_key`.
- Supabase `supabase_oauth_access_token` and `supabase_scoped_personal_access_token`.

When a partner's secret appears in a public repository, GitHub reports it to the issuer so it can be revoked or rotated. "User" secrets raise alerts in public and private repositories. Two days later, GitHub described a fine-tuned model that judges whether a match is a real credential from the code around it, and that can flag passwords with no recognizable token format. AI push protection is in private preview, opt-in, off by default, and billed in AI Credits. The push-protection docs explain the defaults and how anyone with write access can bypass a block.

### Gaps and specific points

1. **Which AI-builder tokens are now recognized (as of 2026-10-05).**
   - `lovable_api_key` is a partner secret: if it is leaked in a public repo, it goes to Lovable to revoke.
   - `logfire_token` and `pydantic_ai_gateway_api_key` (Pydantic).
   - `supabase_oauth_access_token` and `supabase_scoped_personal_access_token` (Supabase).
   - Only these are listed. Do not assume every key from these vendors is covered.
2. **Partner reporting is automatic only in public repos.**
   - A partner secret found in a public repository is forwarded to the issuer to revoke or rotate.
   - User secrets produce alerts (public and private repos), and someone still has to act on them.
3. **Push protection defaults.**
   - Push protection for users is on by default, on GitHub.com only. It stops *you* pushing supported secrets to *public* repositories.
   - Bypassing user push protection creates no alert, unless repository push protection is also on.
   - Repository push protection is **off** by default. It needs GitHub Secret Protection, and an admin, organization owner or security manager has to enable it.
   - It covers command-line pushes, web UI commits, file uploads and REST API requests. For the GitHub MCP server it covers public repositories only.
4. **Anyone with write access can bypass a block.**
   - The bypass reasons are "used in tests", "false positive" and "I'll fix it later". The first two create closed alerts; "I'll fix it later" creates an open alert.
   - A bypass also writes to the audit log and emails watchers.
   - Organizations can restrict who may bypass (delegated bypass).
5. **Pattern detectors miss things.**
   - Pattern detectors need a recognizable token format. The 2026-10-07 model exists to catch passwords and other unstructured credentials that have no fixed format.
   - The GitGuardian report (read for S048) adds that keys from new AI vendors slip past push protection until detectors catch up. It cites 113,000 new DeepSeek keys leaked in 2025, and says push protection holds down density but can't stop volume.
6. **The model-based detector is mostly opt-in and costs money.**
   - Existing AI-detected password alerts moved to the new model automatically, at no extra charge with GitHub Secret Protection or GitHub Advanced Security.
   - AI push protection is in private preview, with public preview planned. It is opt-in, off by default, and an admin must enable it. It is billed as AI Credits to the organization, even for checks that don't block a push.
   - Copilot `/security-review` secret checks are announced for an upcoming private preview and will be off by default. Running `/security-review` does not enable them.
   - GitHub Enterprise Server 3.23 gets AI-detected alerts in public preview only.
   - Budget alerts do not stop spending. A hard cap needs the "Stop usage when budget limit is reached" setting.

### Outdated framings it corrects

- "GitHub won't let me push a secret." Only supported patterns are blocked, user protection covers public repos only, the block can be bypassed, and repository-level protection is off by default.
- "Making the repo private hides the leak." Partner auto-revocation applies only to public repos, and private repos only raise alerts.

### Quote

- "The new checks will be off by default" (GitHub Changelog, 2026-10-07)

### Corrections to the brief

- The S047 changelog itself says nothing about push protection, validity checks, the limits of pattern detection, or a model-based detector. Those points come from the 2026-10-07 changelog and the push-protection docs.

---

## S048: Leaked n8n API Tokens Exposed Live Instances to Credential Theft

- Author: Guillaume Valadon (Staff Cybersecurity Researcher, GitGuardian), a contributed article on The Hacker News
- Date: 2026-08-05 (confirmed)
- URL: https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
- Companion read: GitGuardian, The State of Secrets Sprawl 2026.
  - Landing page: https://gitguardian.com/state-of-secrets-sprawl-report-2026. It shows no date.
  - Full report: reached through https://gitguardian.com/files/the-state-of-secrets-sprawl-report-2026, which redirects to the v1.1 PDF on GitGuardian's CDN. The PDF metadata gives a creation date of 2026-03-25. The data covers calendar year 2025.

### Summary

GitGuardian found 4,576 unique n8n API tokens in 5,469 public GitHub commits since April 2025. These pointed to 1,255 hostnames, of which 896 were reachable, and 321 accepted a leaked token. The hostname was usually committed right next to the token. A newer source of leaks is Claude Code permission files (`.claude/settings.json` and `.claude/settings.local.json`), where an approved `Bash(curl ...)` rule stores both the instance URL and the `X-N8N-API-KEY` header.

With one admin token, an attacker can list users, read workflows (including hard-coded secrets), read execution payloads and data tables, pull an audit report that works as an attack map, and build workflows that either use or exfiltrate stored credentials. Older n8n keys have no expiry. The GitGuardian report adds the 2025 leak rate of Claude Code co-authored commits, the scale of MCP-config leaks, and how long leaked secrets stay valid.

### Gaps and specific points

1. **One automation-platform token reaches everything the platform reaches.**
   - REST endpoints reachable with a token: `/users` (emails, invitations), `/workflows` (full definitions, code nodes, SQL, hard-coded secrets), `/credentials` (names and types, admin only), `/executions?includeData=true` (full input and output payloads), `/data-tables`, `/variables`, and `/audit`.
   - The article describes the audit report as an attack map for whoever holds a privileged token. It shows SQL-injection exposures, filesystem nodes, unprotected webhooks, the n8n version (which can be matched to CVEs) and unused credentials.
   - An attacker can create a workflow that *uses* a stored OpenAI credential without ever seeing it. A Schedule trigger fires about 10 seconds after activation.
   - An attacker can also *exfiltrate* the raw credential by sending it in an HTTP Request node to their own listener.
   - Deleting a malicious workflow also deletes its execution records, which covers the tracks.
   - All of this was demonstrated with documented API calls only, without exploiting any vulnerability.
2. **The leak usually includes the address.**
   - The hostname was usually in the same commit, for example `N8N_URL` and `N8N_API_KEY` side by side in a committed `.env`, or variables like `N8N_MCP_URL` and `N8N_WEBHOOK_BASE_URL`. No separate discovery step was needed.
   - Many of the leaked tokens appeared to belong to owners or admins.
3. **Coding-agent permission files are a new leak path.**
   - When you approve an agent's `curl` command that carries a key, the whole command, key included, can be saved as an allow-rule in `.claude/settings.json` or `.claude/settings.local.json`.
   - These files can be committed without the `.gitignore` protection that `.env` usually gets.
4. **MCP configuration files are a major leak source (GitGuardian report, 2025 data).**
   - 24,008 unique secrets were found in MCP-related config files on public GitHub, and 2,117 of them (8.8%) were verified as working.
   - The top valid types: Google API key (19.2%), PostgreSQL connection string (14%), Firecrawl (11.9%), Perplexity (11.2%), Brave Search (11%).
   - Official MCP quickstarts often put keys inline: as CLI arguments in the server config, in an `env` block of a JSON file that gets committed, or as full `postgresql://user:password@...` strings.
   - The report's advice: keep secrets out of MCP configs, have clients own the secrets, add MCP config directories to `.gitignore`, scan before pushing, and require human approval for MCP actions that touch production.
5. **Leaked keys stay valid for years. Revoking is step one, not the end.**
   - n8n API keys are signed JWTs. Older ones often have no `exp` claim.
   - A 30-day default expiry arrived in n8n 1.78.0 (February 2025), but many tokens were created without one.
   - Revoking the key in the n8n database kills it, even though its signature is still valid.
   - In one real case, a workflow backed itself up to a public GitHub repo. An SSH deploy key that had been hard-coded in an earlier version was still sitting in the git history, and still valid.
   - GitGuardian report: 64% of the valid secrets it found in 2022 were still valid when retested in January 2026. Teams avoid rotating because it can break production, so they often leave the key alone.
   - The article's steps: revoke, work out what the token could reach, look for unauthorized changes (remembering that deleting a workflow erases its executions), and rotate every connected credential that might be exposed.
6. **Disclosure rarely produces a fix.**
   - GitGuardian contacted 7 organizations. One hosting provider and three of the four individual companies did not respond.
   - One company paid a $1,200 bounty and revoked the token immediately, which the article calls the exception.
   - n8n closed its reports. About 30% of the affected instances were on n8n.cloud or similar managed services.
   - Nobody else will clean up your leak.
7. **AI co-authored commits and leaks (GitGuardian report, 2025 data).**
   - Across 1.94 billion public commits in 2025, 1.5% contained an exposed credential. Commits co-authored by Claude Code leaked one 3.2% of the time.
   - Over the year, the Claude Code rate peaked at 31 secrets per 1,000 commits in August 2025 (about 2.4x the human baseline). It fell to 13 per 1,000 by December, which matched the human baseline. GitGuardian links the drop to the release of Claude Sonnet 4.5 in late September 2025.
   - From April onward, Claude Code commits averaged about twice as many lines. This evened out by year end.
   - GitGuardian's view: the developer remains in control of the commit, so larger AI changes should be treated as higher-impact review units.
   - How commits were classified: a Co-Authored-By trailer with a known AI tool email.
8. **Scale context (GitGuardian report).**
   - 28.65 million new hardcoded secrets in public GitHub commits in 2025, up 34%.
   - 1,275,105 leaked secrets for AI services, up 81%.
   - Internal repositories are 6x more likely than public ones to contain a hardcoded secret.
   - About 28% of incidents happen entirely outside repositories, in tools such as Slack, Jira and Confluence.

### Outdated framings it corrects

- ".env is the only file with secrets." Agent permission files and MCP configs hold them too.
- "I deleted the commit / the key, so I'm fine." The key stays in git history and stays valid until it is revoked, and every connected credential has to be rotated.
- "An automation token is just one key." It gives access to every credential and dataset the platform holds.
- "AI commits leak twice as much." That is the 2025 average. By December 2025 the rate matched the human baseline, but AI commits are still larger.

### Quote

- "without exploiting a software vulnerability" (Valadon, The Hacker News, 2026-08-05)

### Corrections to the brief

- The landing page gives only an approximate 2x figure. The 3.2% and 1.5% figures are in the full report PDF.
- The year-long trend changes how the figure should be taught. The gap closed by December 2025.
- The n8n article mentions MCP *keys* for n8n (372 found, 7 still valid, about 2%) but does not name MCP config files. The MCP config file findings come from the GitGuardian report.

---

## Cross-source headlines for the lesson

1. **Shipped code is public.** Anyone can read the bundle and call the backend directly, without using your UI (S044, S045).
2. **A visible Supabase publishable key is normal.** What matters is whether RLS, grants, write policies, views and functions hold up when called as `anon` (S044 and the Supabase docs).
3. **`NEXT_PUBLIC_`-style prefixes ship a value to every visitor.** Environments (Development, Preview, Production) hold separate keys, and the v0 preview panel is the Development environment (S045).
4. **New sites are scanned for within days.** Login code can fail open silently, so test from outside while logged out (S046).
5. **An agent will hand over a key if asked.** Keys without spend caps turned into a $600k loss that nobody noticed for three weeks (S046).
6. **Builder and GitHub scanners help, but none of them certify anything.** Deep scans and AI push protection are opt-in, user push protection covers only public repos, and anyone with write access can bypass it (S045, S047).
7. **Coding-agent permission files and MCP configs are the new `.env`.** They leak URLs and keys together into public repos (S048).
8. **A leaked secret is a durable access path.** Revoke it, find out what it could reach, check for changes, and rotate everything connected. 64% of valid secrets leaked in 2022 were still live in 2026 (S048).
