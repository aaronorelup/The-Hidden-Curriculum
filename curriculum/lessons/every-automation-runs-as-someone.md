---
key: every-automation-runs-as-someone
id: 08.03
title: Whose account is your automation using?
district: Running Alone
module: 08 Unattended work
status: todo
legacy: []
minutes: 10
concepts: [C135, C129]
sources: [S246, S245, S247, S142, S167, S168, S212, S061, S206, S210, S133]
lead: [S246, S247]
---
# Whose account is your automation using?

**Purpose (the first spoken sentence):** In this lesson you'll learn that every automation and agent acts as some account, and that everything you ship stands on a chain of accounts, so you know whose name each one runs under, what happens when that person leaves, and how to keep the chain from breaking.

**Conclusion:** An automation is only as durable as the account it runs as, so list each automation and each account your work depends on with its owner, protect every account with two factor and stored recovery codes, and move anything a business relies on to a service account with narrow access and a second owner.

**Takeaway line (the lesson's former title; retitled by the 2026-10-12 audit so a beginner can tell what it is about):** "Every automation runs as someone." Use it inside the lesson, for example as a "Keep this" bold lead, not as the title.

**Where it sits on the map:** District 5 · Running Alone — "What runs while you're away?"; module 08 Unattended work, third lesson. 08.01 asked where unattended work runs and 08.02 whether it worked; this lesson asks as whom, and what happens to it when that someone changes.

**Lead source (audit, 2026-10-12):** S246 (Microsoft); S247 (Aaron Orelup (typed prompt)). This is the hard-won work the lesson delivers: credit it by name on the title card. The narration names at most the row's sources in curriculum.md (S246, S245, S247, S142); every other source in this spec goes on a dated on-screen card and on the lesson page's source list.

**Length note:** about 10 minutes. Budget: C135 about 6 min (it carries Aaron's own story), C129 about 4 min.

## What to teach (binding scope)

### C135 Every automation runs as someone

1. **Every automation runs under an identity, usually the person who made it.**
   - Google Apps Script: "Installable triggers always run under the account of the person who created them"; a trigger you created sends email from your account even when a colleague opens the document (S245, last updated 2026-09-03).
   - Power Automate: a scheduled or automated flow runs "under the license of" its owner and uses their request limits (S246, updated 2026-09-25).
   - Claude routines: "Anything a routine does through your connected GitHub identity or connectors appears as you: commits and pull requests carry your GitHub user, and Slack messages, Linear tickets, or other connector actions use your linked accounts" (S167). A Desktop scheduled task runs on your machine with your files (S168).
   *Depth: teach (the lesson's opening model: every robot wears somebody's badge).*
2. **Nobody else can see them.** "A given account can't see triggers installed from a second account" (S245). Routines "belong to your individual claude.ai account. They are not shared with teammates" (S167). Private to you also means unknown to whoever must keep them running. *Depth: teach.*
3. **They fail where only the owner looks.** When an Apps Script trigger fails "no error message appears on your screen"; a failure summary goes by email (S245). A routine whose GitHub connection lapses skips runs for up to 72 hours, then turns itself off; while your subscription is paused, your routines don't run (S167). *Depth: brief; silent failure itself is 08.02.*
4. **They depend on the person.** In Power Automate you "can't change the owner of a non-solution cloud flow in place because the owner is part of the flow identity"; an owner change on a scheduled flow "can take up to seven (7) days to become effective"; a premium flow handed to an owner without a premium licence runs for 30 days, then "Power Automate turns off the flow" (S246). *Depth: teach.*
5. **Aaron's own case, the reason this lesson exists.** Aaron's work automations ran under his personal accounts, so they had to move to service accounts, Credential Manager, DPAPI and Entra app registrations to keep running without him (S247; COURSE.md's approved version of the story). Tell it in the third person, in those words. Do not quote his private Playback prompt: clear any direct quote from it with Aaron before scripting (audit, 2026-10-12). *Depth: teach (story).*
6. **Move what the business depends on to a non-human owner.** A service principal is "a non-human security identity"; with one as owner, "the ownership isn't tied to a user that could leave the organization"; its connections must be shared with it; it is a non-interactive user that "can't have a user license" and has its own request limits; and it can't be a co-owner (S246). When a solution-aware flow changes hands, "the original owner and the new owner become co-owners": keep a second human owner who can get in (S246). A plain user account used as a service account must be "licensed correctly to avoid multiplexing" (S246). *Depth: teach (what it is and why; no portal steps).*
7. **Keep an inventory:** each automation, the identity it runs as, the connections it uses, and its second owner (C135, C129; the places to look are the trigger and flow pages in S245, S246 and the routine list in S167). *Depth: teach (shown as a one-page table).*

### C129 Your accounts are part of your app

1. **A shipped app stands on a chain of accounts:** code host, hosting, domain registrar, database, AI provider, payments, password manager. Lose one or have it taken over, and the product breaks or turns against you. List each with its owner: you, a client, your employer, or an agent (C129; C135). Even signing in to the coding agent has four kinds of account: a Claude subscription, a Console account, a cloud provider, or a company gateway with corporate SSO (S206). *Depth: teach.*
2. **Ask the agent which account it is running as.** `claude auth status` prints an `authMethod` such as `claude.ai`, `oauth_token` or `api_key` (S133). *Depth: one line; meters are 06.03.*
3. **Account rules decide outcomes.** On Lovable, custom domains need a paid plan; "You need to be a workspace admin or owner to change nameservers"; domains bought there "belong to your workspace, not a single project"; a registrar suspends a domain "most often because you did not verify the registrant email before the deadline"; auto-renew charges the saved payment method, and an unrenewed domain stops serving traffic and is released after a roughly 30-day redemption period (S212). Watch the verification and renewal emails. *Depth: teach.*
4. **Protect each account.** Two factor is "A second verification step in addition to a password" (Lovable's glossary, S212). Keep recovery codes somewhere other than the computer they protect. Aaron's own gap list runs "through webhooks, licences, installers, worker threads and passkeys" (S210). *Depth: brief. Source gap: no source read so far explains passkeys or recovery codes; teach them at one-line depth until one is added (see Evidence notes).*
5. **Roles decide who can ship.** "Why does the client have pushing rights to the repository?" (Pooge, on an Ask HN thread where a client took over a codebase by vibe coding; S142). Whoever can push, or change nameservers or billing, can change the product (S142, S212). Give collaborators and agents the narrowest role (07.03). *Depth: brief.*
6. **A taken-over account publishes as you.** In ChainDrop (2026-08-04) "the attacker compromised the maintainer's GitHub account, pushed poisoned release commits and tags", and the projects' own release workflows shipped the malware; the worm also goes after AI tool credentials and fires a payload "when the stolen GitHub token is revoked" (S061). *Depth: brief; supply-chain details are 07.04 and rotation 03.02.*
7. **The billing account is a key too** (C055, C061). *Depth: one line; taught in 06.03.*
8. **Plan the hand-over** whenever a client, a contractor or a departing employee holds access (S142, S247; Microsoft's own related article is "How to manage orphaned flows when the owner leaves the organization", S246). *Depth: brief.*

## You vs the agent

As of 2026-10-12:

- **The agent can:** draft the account inventory from the repository's config and environment files; list the triggers, flows and routines it can see with their owners and connections; say which account it is itself signed in as (S133); and draft the move to a service identity, including which connections must be shared with it (S246).
- **The agent cannot:** see accounts that exist only in other companies' dashboards, see triggers installed by another account (S245), hold your second factor (and should not, C084), or decide who in an organisation should own something.
- **You decide and check:** which automations a business depends on; who the owner and the second owner of each are; that every account has two factor and that the recovery codes are stored away from the machine they protect; that verification and renewal emails reach someone who reads them (S212); and the hand-over before anyone leaves (S246, S247).
- **Bring in an expert** (C118): your organisation's identity or IT administrator before a personal automation becomes something the business relies on, because service principals, licences, request limits and offboarding are theirs to set (S246, S247); and someone who knows company sign-in (SSO, an identity provider) or account recovery when an account is hijacked.

## Sources this lesson is built from

- S246 — Microsoft, "Change the owner of a cloud flow in Power Automate" (Microsoft Learn; ms.date 2026-09-16, updated 2026-09-25) https://learn.microsoft.com/en-us/power-automate/change-cloud-flow-owner — the owner as part of the flow's identity and licence, the 30-day grace, service principals, co-owners.
- S245 — Google for Developers, "Installable triggers" (Apps Script docs; last updated 2026-09-03) https://developers.google.com/apps-script/guides/triggers/installable — triggers run as their creator, are invisible to other accounts, fail without an on-screen error.
- S247 — Aaron Orelup, his typed prompt on work automations tied to his personal accounts (2026-09-30; Playback session 88a586af-a275-481a-b481-23bf805cba04, line 53, not public) — the real case. Credit as Aaron's own work problem; COURSE.md lists this story (automations tied to his personal accounts moving to service accounts) among the true stories the course may tell.
- S142 — piscator, with replies including Pooge and HyprMusic, "Ask HN: Client took over development by vibe coding. What to do?" (Hacker News; 2026-04-01 per sources.md, the page shows only "6 months ago") https://news.ycombinator.com/item?id=47599303 — who can push, and the hand-over problem.
- S167 — Anthropic, "Automate work with routines" (undated live docs; cites up to v2.1.268) https://code.claude.com/docs/en/routines — routines act as you and belong to your individual account.
- S168 — Anthropic, "Schedule recurring tasks in Claude Code Desktop" (undated; cites Desktop 1.1.5368) https://code.claude.com/docs/en/desktop-scheduled-tasks — local tasks run on your machine.
- S212 — Lovable, "Glossary, Secrets, Git sync and Custom domains" (undated live docs; the custom-domain page names 2025-10-29; read 2026-10-12) https://docs.lovable.dev/features/custom-domain.md and https://docs.lovable.dev/glossary.md — roles, registrant verification, renewal, 2FA defined.
- S061 — Sai Likhith (StepSecurity), "ChainDrop npm Worm" (2026-08-04) https://stepsecurity.io/blog/chaindrop-npm-worm — a taken-over account publishing through the project's own workflow.
- S206 — Anthropic, "Quickstart" (Claude Code docs; undated, read 2026-10-12) https://code.claude.com/docs/en/quickstart — the four account types for signing in to the agent.
- S210 — Aaron Orelup, "AO-029: I asked where I was supposed to learn all this..." (2026-10-01) https://aaronorelup.com/ledger/the-missing-map/ — passkeys on the learner's own gap list.
- S133 — Anthropic, "CLI reference" (undated; cites up to v2.1.290) https://code.claude.com/docs/en/cli-reference — `claude auth status` and its `authMethod` field.

## Show it for real

- Two throwaway Google accounts, the same spreadsheet: account A installs a time-driven Apps Script trigger; account B opens the Triggers page and sees nothing: proves an automation is invisible to everyone but its creator (S245).
- Browser capture of the public Microsoft Learn page at "Change the owner of a non-solution cloud flow" and its screenshots of the Details edit panel, the plan section and the licence warning: shows where ownership and licence live without using a real tenant (S246).
- Terminal replay: `claude auth status --text` (blur the email): proves the agent itself runs as a specific account (S133).
- A pull request opened by a routine in a throwaway GitHub repo, with your own avatar as the author: proves "appears as you" (S167).
- A one-page account inventory for a small sample app, drafted by the agent from the repo's config files, then completed by hand: account, owner, second owner, two factor on?, where the recovery codes are (C129, C135).
- A throwaway GitHub repo's Settings → Collaborators page with roles: who can push is a setting someone chose (S142).
- Browser capture of Lovable's public custom-domain troubleshooting line about registrant-email suspension (S212).

## Questions this lesson answers

- How do I keep work automations running without my own login, so they don't depend on my personal account? (Aaron's question, paraphrased, S247)
- The owner of a flow left the organisation: how do we keep it working? (the title of Microsoft's related FAQ linked from S246)
- Why does the client have pushing rights to the repository? (S142)
- Why was my domain suspended? (S212's troubleshooting list)
- What is a passkey? (Aaron's list, S210; needs a source before it is answered in depth)
- Who can see my scheduled routines? (derived from S167)
<!-- add yours: open an issue or a pull request -->

## Introduced here, taught elsewhere

- Where unattended agents run, and that routines act through your connectors → agents-that-run-while-youre-away
- Automations that fail silently → green-is-not-success
- Keys as permission sets; rotating a leaked token → keys-public-secret-and-leaked
- The narrowest role for collaborators and agents; actions never the agent's alone → the-narrowest-keys-and-verbs
- The billing account and caps that stop → know-your-meter
- Account takeover as a supply-chain attack → other-peoples-code
- Domains, DNS and hosting → from-your-laptop-to-a-url
- How to bring in an expert and what to hand them → before-you-ship-who-signs-off

## Out-of-date framings to avoid

- "It does company work, so it belongs to the company." It belongs to its owner's identity and licence (S246).
- "If it breaks, someone will see an error." No error appears on screen; a summary goes to the owner's email (S245).
- "Only I can see my automations, so they are private." They are also unknown to whoever must keep them running (S245, S167).
- "Changing the owner is a quick edit." A non-solution flow can't change owner in place, and a change can take seven days (S246).
- "A strong password is enough." Taken-over accounts publish as their owner (S061); use two factor (S212).
- "Push access is just a courtesy." Whoever can push can ship (S142).

## Legacy notes

No legacy lesson covers this slot, and no published lesson teaches automation ownership or the account chain.

**Evidence notes for the writer (2026-10-12).** Passkeys and recovery codes have no source in sources.md yet. A candidate was fetched and read on 2026-10-12 but is not yet an S-ID: GitHub Docs, "Configuring two-factor authentication recovery methods" (undated) https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication-recovery-methods . It calls recovery codes "one-time codes for account recovery if you can't access your two-factor authentication method", recommends "saving them with a secure password manager", and "configuring two or more authentication methods to avoid losing access to your account". It does not mention passkeys, and it does not say to keep the codes on a different device. Add it to sources.md (and find a passkey source) before this lesson teaches either point beyond one line. concepts.md's framing "The developer's personal account can own the client's domain and repository" cites S142, but the thread does not discuss domain or repository ownership (re-read 2026-10-12), so it is replaced here by the push-rights framing. The shared web-search budget was used up during this pass, so no newer sources were searched for.
