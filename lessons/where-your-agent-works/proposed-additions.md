# Proposed additions (not for this lesson) — from research-now, 2026-10-14

For the curriculum to consider later. None of these go into where-your-agent-works.

1. **Auto mode is the new default approval.**
   Why: beginners are taught "the agent asks before acting", but current Claude Code starts in Auto, where a classifier decides. Cowork scheduled tasks that Claude creates also default to "Automatically approve". Probable owner: before-you-let-it-loose.
   Sources: https://code.claude.com/docs/en/how-claude-code-works (Auto is the built-in starting mode for v2.1.283+ in terminal and VS Code; read 2026-10-14). https://claude.com/docs/cowork/changelog (2026-09-24, new Code tab sessions start in Auto; 2026-10-01, scheduled tasks default to Automatically approve).

2. **Self-hosted cloud environments.**
   Why: an agent's "cloud" can now be the organisation's own infrastructure, where isolation and egress are the organisation's job. This changes who the expert is. Probable owner: contain-it-dont-babysit-it.
   Source: https://code.claude.com/docs/en/claude-code-on-the-web (undated, read 2026-10-14).

3. **Remote Control versus cloud.**
   Why: the two are easily confused. With Remote Control the files stay local and the session is steered from a phone or browser. Note that `--remote` is a deprecated alias for `--cloud`, while `--remote-control` is the unrelated feature. Probable owner: agents-that-run-while-youre-away.
   Sources: https://code.claude.com/docs/en/how-claude-code-works and https://code.claude.com/docs/en/claude-code-on-the-web (read 2026-10-14).

4. **OpenAI's separate Codex training toggle.**
   Why: Codex has an "Include environments" setting that the ChatGPT "Improve the model for everyone" toggle does not change. It fits the backlog item "Comparing AI vendors' privacy settings".
   Source: OpenAI Help Center "Data controls" (https://help.openai.com/en/articles/7730893-data-controls-faq). The page is undated, and the direct fetch returned 403 on 2026-10-14; this rests on search snippets and needs re-checking.

5. **Unified Claude for organisations, and the admin keys that control it.**
   Why: on November 10 the tab split ends for orgs that have not set `desktopHome`, per the third-party deployment notes. A course note may need re-recording around then. Probable owner: a currency check on this lesson plus every-automation-runs-as-someone.
   Source: https://claude.com/docs/cowork/changelog (entry 2026-10-08, beta).

6. **Network-disabled is not data-sealed.**
   Why: a cloud session with network access off can still reach the Anthropic API, "which may allow data to exit the VM". Probable owner: contain-it-dont-babysit-it.
   Source: https://code.claude.com/docs/en/claude-code-on-the-web (read 2026-10-14).

7. **On Mac and Windows, a Docker container already runs inside a Linux VM** (added by the planner, 2026-10-14).
   Why: MIT lists it as one of Docker's limits ("containers need a Linux kernel"). It changes what "container" means on a beginner's laptop, and it matters when someone asks whether a container is "inside" a VM. Probable owner: contain-it-dont-babysit-it.
   Source: MIT Missing Semester 2026, "Packaging and Shipping Code" (2026-01-20) https://missing.csail.mit.edu/2026/shipping-code/ (read 2026-10-14).
