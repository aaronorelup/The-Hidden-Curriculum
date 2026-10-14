# Point checks: S069, S070, S074, S080, S101, S104 (read 2026-10-14)

Checked only the points the spec takes from each source. Quotes are copied word for word from the live page.

## S069 — Anthropic (Claude Help Center), "Use Claude Cowork safely" (last modified 2026-10-06; page shows "Updated over a week ago" on 2026-10-14) https://support.claude.com/en/articles/13364135-use-claude-cowork-safely

- Cowork's cloud run (spec What-to-teach C022.4): "Cowork tasks run in the cloud: Claude's work runs in an isolated, temporary environment on Anthropic's servers." SUPPORTED.
- "A session in the cloud reaches your computer only when the Claude Desktop app is open". SUPPORTED. The page says "the folders you've connected"; the phrase "connected folders" is the spec's paraphrase, so don't put it in quotation marks.
- "...including any local files it opens through the desktop app, is processed on Anthropic's servers" (C103.1). SUPPORTED, word for word.
- "Scheduled tasks run on their own even when your computer is off" (C103.1). SUPPORTED, word for word.
- Managed computer (C103.2): the source says "If your organization manages your computer, note that connecting local folders makes them reachable from a session in the cloud." SUPPORTED. The spec's wording "on a computer your organisation manages" is a paraphrase, so keep it outside the quotation marks.
- "Consider creating a dedicated working folder for Claude rather than granting broad access" (C103.2). SUPPORTED.
- "Cowork via mobile and web is captured in Compliance API." (C103.5). SUPPORTED. The spec's quote "is captured in Compliance API" matches.
- Approval mode ("You vs the agent"): the source says "Cowork can work through the steps of a task without pausing for your approval". It names the modes "Automatically approve", "Manually approve" and "Skip all approvals". SUPPORTED. Use those names on screen, not "permission mode".

## S070 — Anthropic (Claude Help Center), "Use Claude in Chrome safely" (last modified 2026-10-05) https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely

- The spec drops this point to the lesson on the narrowest keys and verbs. The point is SUPPORTED: "Claude in Chrome is available but not covered under your Business Associate Agreement (BAA)" ("including after an Owner turns it on"); "In organizations that have enabled HIPAA, Claude in Chrome is off by default."; "We recommend against using Claude in Chrome on pages with regulated data generally." This lesson does not use it.

## S074 — Thomson Yen, Julian Poeltl, Hongseok Namkoong et al. (Columbia Business School), "WorkstreamBench" (2026-05-21) https://arxiv.org/html/2605.22664v1

- The spec drops this point to the lesson on model, harness and memory. The point is SUPPORTED, with a caveat: "GUI agents on proprietary harnesses generally outperform API agents on our in-house agentic harness, indicating that harness quality drives a substantial portion of the gap." The authors only "suspect that Claude Web is equipped with superior agentic harness". It is an inference, not something they measured. Best agent: "Claude Web, attains only 69.1 out of 100 overall" (sources.md rounds this to 69). This lesson does not use it.

## S080 — Stack Overflow, Developer Survey 2026 (released 2026-10-06) https://survey.stackoverflow.co/2026/

- "Survey figures on shadow AI": NOT SUPPORTED. The overview page and the /2026/ai page have no figure on shadow AI, unapproved AI tools, personal AI accounts at work, or putting company data into AI tools. The nearest figures: "The tool meets security, privacy requirements" 28.7% and "meets legal or compliance requirements" 22.3% as adoption factors; "Issues with privacy or security" 13.0% as a reason to avoid AI; "my organization required or recommended a different tool" 10.6%. The spec already leaves this out. Keep it out.

## S101 — Anthropic (Claude Code docs), "How Claude Code works" (undated live docs; read 2026-10-14) https://code.claude.com/docs/en/how-claude-code-works

- Interfaces (C022.5): "You can access Claude Code through the terminal, the desktop app, IDE extensions, claude.ai/code, Remote Control, Slack, and CI/CD pipelines. ... the underlying agentic loop is identical." SUPPORTED.
- Environments: "Claude Code runs in three environments". Local: "Your machine" / "Default. Full access to your files, tools, and environment". SUPPORTED. Cloud: "Anthropic-managed VMs, or self-hosted environments your organization operates". PARTIAL: the spec cuts off the self-hosted clause, so add it or keep the quote obviously partial. Remote Control: "Your machine, controlled from a browser" / "Use the web UI while execution and your files stay local". SUPPORTED.
- "Any command you could run: build tools, git, package managers, system utilities, scripts. If you can do it from the command line, Claude can too." (C128.2). SUPPORTED, word for word.

## S104 — Anthropic Privacy Center, "How long do you store my data?" (updated 2026-07-01) https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data

- Consumer plans include Claude Code: the page's heading covers "Free, Pro, Max, and Claude Code". SUPPORTED.
- Deleted conversations: "Deleted from our back-end storage systems within 30 days." With model training on: kept de-identified "up to 5 years", and this applies only to new or resumed chats after the setting is on. SUPPORTED as a restatement of S186.
- Commercial list (Team, Enterprise, API, Bedrock, Vertex, Gov, Education): this page only refers readers to a separate commercial-retention article and gives no periods. The spec credits the list to S186, which is fine. Do not credit S104 for commercial terms.
- Feedback: "we retain data associated with that submission for 5 years." (C103.4). SUPPORTED.
