# Single-point source check: S129, S132, S183, S185, S186, S187

Checked 2026-10-14 against the live pages. Each point is the one the spec (curriculum/lessons/where-your-agent-works.md) takes from the source.

## S129 - Anthropic, "Use Claude Code in the cloud" (Claude Code docs, undated live docs; mentions up to v2.1.289; read 2026-10-14)
https://code.claude.com/docs/en/claude-code-on-the-web

- "Each session runs in an isolated, Anthropic-managed VM": SUPPORTED ("each session runs in an isolated, Anthropic-managed VM", Security and isolation). Caveat on the page: sessions an organization routes to a self-hosted environment run on its own infrastructure.
- Keeps running after you close your laptop: SUPPORTED ("The session keeps running after you close your laptop"; also "Cloud sessions persist even if you close your laptop"). Caveat: sessions stop after a period of inactivity and the VM is reclaimed (Environment expired).
- `claude --cloud` clones the remote: SUPPORTED verbatim ("The cloud VM clones your current directory's GitHub remote at your current branch, not your local checkout, so push first if you have local commits").
- GitHub credentials: SUPPORTED, with a qualifier the spec drops: "In Anthropic-hosted environments, your GitHub credentials stay encrypted on Anthropic's servers and never enter a session's VM."
- No-remote repo is bundled and uploaded: SUPPORTED, and broader: also happens for a github.com repo "that the Claude GitHub App isn't installed on", "even if you connected GitHub with /web-setup". Untracked files are not included.
- macOS/Linux/WSL leave out uncommitted changes to files "named like credentials or keys", including `.env`, with a `Left on this machine:` notice: SUPPORTED verbatim (also `*.tfvars`, `id_rsa`, `*.pem`, and LFS-managed files).
- Native Windows: SUPPORTED verbatim ("uncommitted changes to tracked files upload as they are, whatever the file's name. Stash or revert an edit you don't want in the cloud session before you start it.").
- Pro/Max Public sharing: SUPPORTED ("Public visibility makes the session visible to any user logged into claude.ai"; "Sessions may contain code and credentials from private GitHub repositories"). Also: repository-access verification "isn't enabled by default" on Max/Pro.
- Extra, usable: cloud sessions count toward plan usage limits; "there's no separate charge for the cloud VM".

## S132 - Anthropic (Claude Help Center), "Using Claude Code with your Pro or Max plan" ("Updated this week" as of 2026-10-14; no calendar date)
https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan

- ANTHROPIC_API_KEY: SUPPORTED ("If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key", "resulting in API usage charges rather than using your subscription's included usage").
- Shared allowance: SUPPORTED ("These limits are shared across Claude and Claude Code, meaning all activity in both tools counts against the same limits").
- Five-hour and weekly: SUPPORTED (a five-hour session limit and a weekly limit on Pro and Max). The word "rolling" is the spec's, not the source's; drop it or source it elsewhere.

## S183 - PagerDuty (survey by Wakefield Research, vendor-sponsored), 2026-06-11
https://www.pagerduty.com/newsroom/shadow-ai-workplace-survey-2026/

The spec only says to leave survey figures out unless re-checked. Re-checked: n = 1,250 office professionals in non-IT, non-technology roles at organizations with $500M+ annual revenue. 66% used AI tools at work while believing policy didn't allow it; 86% believe their organization has AI policies; 88% have shared work-related information with public AI tools such as ChatGPT, Claude or Gemini. Usable on a dated card if wanted; vendor-sponsored, so label it.

## S185 - cximenez, reply by jahala, "Ask HN: What would you include in an academic workshop on vibe coding?" (posted 2026-09-17 19:26 UTC, per the HN API)
https://news.ycombinator.com/item?id=49745403

- Poster is a university AI librarian: SUPPORTED as self-description ("I'm the resident AI librarian at a research university"); a 3-hour workshop "next month".
- One of four answers / items: SUPPORTED. jahala's reply is one comment listing four numbered items; item 4 reads "privacy - ensure using the correct settings to (at least hypothetically) avoid models being trained on your unpublished research". Spec wording "one of four answers" should be "one of four things in one reply" (the thread has 5 direct replies).
- Date: the spec's "about 2026-09-18" is a day off; the API timestamp is 2026-09-17.

## S186 - Anthropic, "Updates to Consumer Terms and Privacy Policy" (2025-08-28)
https://www.anthropic.com/news/updates-to-our-consumer-terms

- Plans covered: SUPPORTED ("Claude Free, Pro, and Max plans", "including when they use Claude Code from accounts associated with those plans").
- Excluded: SUPPORTED ("services under our Commercial Terms", Claude for Work, Claude for Government, Claude for Education, and in the FAQ the API, Amazon Bedrock, Google Cloud's Vertex API).
- "for up to 5 years" de-identified: NOT SUPPORTED as quoted. The page says "We are also extending data retention to five years, if you allow us to use your data for model training"; it does not say "up to", and does not say "de-identified" (it says tools and automated processes "filter or obfuscate sensitive data"). If "up to 5 years"/de-identified comes from S104, credit S104 for it.
- 30 days when off: SUPPORTED ("existing 30-day data retention period").
- "Your data will still be included in model training that has already started": SUPPORTED verbatim; the page adds that future training runs stop using previously stored chats once you turn it off.

## S187 - Anthropic (Claude Help Center), "Use Claude's chat search and memory to build on previous context" (page shows "Updated over 2 weeks ago" on 2026-10-14; consistent with the spec's 2026-09-30)
https://support.claude.com/en/articles/11817273-using-memory-in-claude

- On by default for Free, Pro, Max: SUPPORTED ("Memory is on by default for Free, Pro, and Max plans on the web, Claude Desktop, and Claude Mobile").
- Team/Enterprise "it's off for each member until they turn it on": SUPPORTED (Owners decide whether memory is available).
- Shared between Chat and Cowork in the cloud: SUPPORTED ("Memory is shared between Chat and Claude Cowork when Cowork runs in the cloud"); locally run Cowork sessions don't use memory.
- "When a conversation expires or is deleted, related memory entries generated from it won't be removed": SUPPORTED verbatim; delete under Settings > Memory, Topics, Delete.
- Incognito chats not saved: SUPPORTED (not saved to memory or chat history).
