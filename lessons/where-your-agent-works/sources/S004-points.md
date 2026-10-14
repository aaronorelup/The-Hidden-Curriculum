# Single-point source check: S004, S008, S016, S025, S050, S052

Checked 2026-10-14 for lesson `where-your-agent-works`. Only the points the spec takes from each source were checked.

## S004
**Credit:** Aaron Orelup, "AO-034: I sent back two of my course's first seven lessons, including the one built to stop that happening" (2026-10-04), https://aaronorelup.com/ledger/lessons-sent-back/

- Spec: Aaron's gap, quoted as "chat, Cowork and Code across browser, desktop, CLI and cloud". SUPPORTED, verbatim. The page is dated Oct 04, 2026.
- Spec ("Questions it answers"): "Should I use Claude chat, Cowork or Claude Code? The desktop app or the CLI?" (Aaron's list, S004). PARAPHRASE, NOT A QUOTE. The post does not contain this question. It has only the list phrase above. Treat it as the crew's rewording of that phrase, and never put it on screen in quotation marks as Aaron's words.
- Related line in the post: "I'd said I expected chat and Cowork to merge soon". This matches S102's 2026-09-16 merge announcement.

## S008
**Credit:** OpenAI Academy (Marcus Stallworth, Tanner Wride, Aruna Chakkirala), "Codex Bootcamp 101: Agentic coding" livestream and deck "Codex Bootcamp 101 - Sept.pdf" (2026-09-23), https://academy.openai.com/public/clubs/builders-etkn1/events/codex-bootcamp-101-agentic-coding-9qeg5cpn8c

- Event date 2026-09-23 and the three presenters: SUPPORTED by the event page.
- Slide 8 heading "Codex now lives in the new ChatGPT desktop app": SUPPORTED, verbatim. The deck PDF's page 8 is numbered 8.
- "Use Chat when the answer is still taking shape": SUPPORTED, verbatim.
- "Use Work when the desired output is knowledge artifacts": SUPPORTED, verbatim.
- "Use Codex when the output is working software or applications": SUPPORTED, verbatim.
- The slide's column text, usable on screen: Chat is "Explore assumptions, pressure-test ideas, and shape the work before deciding what needs to be produced". Work is "Delegate structured knowledge tasks that turn files, data, and instructions into tangible artifacts". Codex is "Delegate software tasks that turn a goal or repository into tested, reviewable code ready for production".
- Caveat: every slide carries the footer "Confidential and proprietary.", although the deck is linked publicly from the event page. Cite the slide's words and do not show the deck itself.
- "The presenter's colleague said the difference confused him at first (talk 28:01)": NOT CHECKED. It is in the replay video (academy.openai.com/home/videos/september-23-codex-bootcamp-101-2026-09-24), which has no text transcript I could read. The only record is the research crew's log in curriculum/research/notes/vendor-academies.json. Do not use it as a quote until someone watches 28:01.
- Note: the research log also claims "the same models sit behind every surface" (talk 29:00-30:00). That conflicts with S025 (2026-09-22), and the spec rightly avoids it.

## S016
**Credit:** Anthropic (Claude Code docs), "Manage costs effectively" (undated live docs; names versions up to v2.1.271), https://code.claude.com/docs/en/costs

- The spec takes no fact from S016. It drops "the details of the usage allowance and the meter" to know-your-meter. Nothing to support.
- Relevant to point 7, which is credited to S132: S016 says the "rolling five-hour window and a weekly window" allowance "is shared with Claude chat and Cowork" only in its Claude for Teams and Enterprise section (per-seat allowance). For Pro and Max it says only "Claude Max and Pro subscribers have usage included in their subscription" and describes plan usage bars. S016 does not mention `ANTHROPIC_API_KEY` billing, so point 7 must rest on S132 alone. The page also states "Claude Code charges by API token consumption".

## S025
**Credit:** OpenAI, "ChatGPT & Codex changelog" (latest entry now 2026-10-09), https://learn.chatgpt.com/docs/changelog, with "Get started with ChatGPT Work" (undated), https://learn.chatgpt.com/codex/get-started-with-work

- Codex moved into the ChatGPT desktop app on 2026-07-09: SUPPORTED, but not on the live first-party page any more. The live changelog now reaches back only to about 2026-09-22, and the July entry has rolled off. Third-party mirrors of the changelog (gradually.ai, developertoolkit.ai, releases.sh) record the entry "Codex joins the ChatGPT desktop app" dated July 9, 2026 (v26.707): "Codex is now part of the ChatGPT desktop app on macOS and Windows". S008 slide 8 independently confirms the move. For a first-party credit, use S008 slide 8 or cite the mirror with its date.
- 2026-09-22 entry "GPT-6 Sol and Luna in Codex and ChatGPT Work": SUPPORTED, verbatim "In ChatGPT, the models are available in Work and Codex, but not Chat." The models are GPT-6 Sol and GPT-6 Luna. The same entry says "Free and Go users can access Luna in the desktop app." The later 2026-09-29 GPT-6.1 Sol entry says only "Availability depends on your plan, client, and workspace settings."
- "Latest entry 2026-10-08": OUT OF DATE. The latest entry is now 2026-10-09 (Codex CLI 0.162.1). This is minor and supports the "moves monthly" framing.
- Work page, local: "can also use local files, apps, and the browser". SUPPORTED. The full clause runs "...local files, apps, and the browser when those tools are available."
- Work page, cloud: "your computer doesn't need to be awake". SUPPORTED, given as the reason cloud mode suits scheduled research or website checks.
- Work page: the container "cannot access that computer's files or tools". SUPPORTED. The full clause runs "...or enforce its enterprise execution requirements."
- Work page: "Work can't switch from local to cloud execution during a turn": SUPPORTED. The page uses a curly apostrophe.
- Work page date: SUPPORTED that it is undated. The only dates are in its sample content.

## S050
**Credit:** Anthropic Engineering, "How we contain Claude across products" (2026-05-25), https://www.anthropic.com/engineering/how-we-contain-claude

- Date 2026-05-25: SUPPORTED.
- "The local VM": SUPPORTED. The full heading is "Pattern 3: The local VM (Claude Cowork)".
- "The user's selected workspace and .claude folder are mounted; nothing else on the host is visible.": SUPPORTED, verbatim.
- Also on the page: "Claude Cowork runs on a user's desktop with access to a workspace folder selected by the user." The post mentions no cloud execution for Cowork.
- Caveat for the "stale in four months" framing: the VM sentence describes "our first version of Claude Cowork", which "ran inside a full virtual machine". The post then says the agent loop was moved outside the VM "while keeping code execution inside of it". Even in May 2026, then, the mount sentence described the first version, although Cowork was still local and the local-VM model was current. The framing holds (local in May, cloud for new Pro and Max tasks since 2026-10-06). If the on-screen card quotes the mount sentence, label it "Cowork's first version, as described 2026-05-25".

## S052
**Credit:** Anthropic (Claude Code docs), "Configure the sandboxed Bash tool" (undated live docs), https://code.claude.com/docs/en/sandboxing. This is S052's companion page. The primary entry is https://code.claude.com/docs/en/permission-modes.

- Claude Code's sandbox covers macOS, Linux and WSL2, but not native Windows: SUPPORTED, still true on 2026-10-14. The page says "The sandbox runs on macOS, Linux, and WSL2. On native Windows, Claude Code runs commands unsandboxed. To use the sandbox on a Windows machine, run Claude Code inside a WSL2 distribution."
- Caveat: the page says the sandbox covers shell commands only (Bash, PowerShell and Monitor commands and the processes they start). "Claude's file tools, MCP servers, and hooks run outside it."
