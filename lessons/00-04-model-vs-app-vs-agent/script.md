# 00.04 — Model vs app vs agent
<!-- lead=1.6 gap=0.8 tail=3 -->
<!-- captions: G P T=GPT; A P I=API; dot T X T=.txt; dot P Y=.py; dot V E N V=.venv; C D=cd -->

## 01 — Engine, car, driver
> Final: draft B's spine (one engine / car / driver drawing for the whole lesson), with A's Notepad comparison (05), A's and C's "same engine, different door", "some apps choose for you" and the lantern line, and C's "learn the layers, not the numbers".
> Aaron's rule: sentence 1 is the purpose line, sentence 2 the conclusion. Title card shows both from frame 0.
In this lesson you'll learn the difference between an AI model, the app you use it in, and an agent. [[engine]] The model is the engine, [[car]] the app is the car built around it, and [[driver]] an agent is that same car, allowed to drive, with you in the passenger seat. [[which-layer]] Know which one you're dealing with, and most of AI's surprises start to make sense.

## 02 — Where it lives
> Map pin on 00. The Start label's question is read exactly as engine/map.js draws it. The Lanterns are AI and never a district.
On the course map, this lesson sits at the [[pin]] Start, in Orientation: what this course is, and the lantern you carry. [[lanterns]] The lanterns strung over every district are AI. This lesson [[open]] opens one up and names the parts inside.

## 03 — The engine: the model
> Facts: a model is a very large set of learned numbers (weights) stored in files, made by a lab by training on very large amounts of text. OpenAI makes GPT, Anthropic makes Claude, Google makes Gemini. Lab and family names only; no version numbers (00.03: versions move fastest in AI). "At its core" covers models that also take images.
Start with the engine. [[engine]] A model is a huge set of numbers, called weights, saved in files. A lab trains it on enormous amounts of text, and runs it on its servers. [[labs]] OpenAI makes the G P T models. Anthropic makes Claude. Google makes Gemini. [[words]] At its core: text in, more text out. [[stand]] On its own, an engine has no seats, no wheel, and no memory of the last run.

## 04 — The car: the app
> Facts: ChatGPT (OpenAI), the Claude app (Anthropic), the Gemini app (Google) and Microsoft's Copilot are apps. Many apps have a model picker (ChatGPT, GitHub Copilot, Cursor); one model is offered in many products and through the API. "ChatGPT" names only the app; "Claude" and "Gemini" name both the app and the model family. No claim about which model any app uses today.
Now build a car around it. [[car]] The app is the part you actually touch: ChatGPT, the Claude app, the Gemini app, Copilot. [[parts]] It adds the chat window, saved chats, file uploads, safety checks, and the bill. [[rules]] And hidden instructions, called a system prompt, that the model reads first. [[many-cars]] One engine can sit in many cars: the lab's own app, a code editor, a company's help desk. And one car can swap engines, with a model picker. [[names]] That's why the names blur. ChatGPT is the car. G P T, followed by a number, is the engine. With Claude and Gemini, the car and the engine share a name. The numbers change often; learn the layers instead.

## 05 — Handing over the wheel: the agent
> Facts: agent = model + tools + a loop + permissions. Coding agents such as Claude Code read files, run terminal commands and edit code; by default they ask before running commands ("by default" and "most" keep it true across products and settings).
> Aaron's story uses only the COURSE.md details, third person. It does NOT claim his code came from an AI: the chat app and the agent are a comparison with today's tools ("a plain chat window" = no access to files on your computer).
An agent is the same car, allowed to drive. [[tools]] It gets tools: it can read your files, run commands in a terminal, and edit code. [[loop]] And it works in a loop: decide the next step, do it, check what happened, and go again, until it's done or stuck. Coding agents, like Claude Code, work this way. [[notepad]] Aaron, who made this course, once wrote Python in Notepad and saved it as dot T X T. He didn't know to rename it dot P Y, to C D into the folder, or what dot V E N V was. [[agent-steps]] A plain chat window could write that code today, but the steps around it stay yours. An agent can take them. [[ask]] You stay in the passenger seat. By default, most coding agents ask before they run a command, and you can say no.

## 06 — Where the picture breaks
> The true mechanism under the metaphor: (1) a model call is stateless; chat apps resend the conversation (or the part that fits) every turn, and "memory" features are stored by the app; (2) the API is the model reached by a program with a key, no app around it; (3) tool use is the model writing a request as text, which the app (the harness) runs if its permissions allow.
Here's where the picture breaks. [[cold]] A real engine runs the whole trip. A model doesn't. With every message, it starts cold and rereads the conversation the app sends back in. So the memory lives in the car, not the engine. [[bench]] Programs can skip the car and reach the engine through an A P I, with a key. That's the engine on a test bench: no chat window, no saved chats, unless the program builds them. [[driver]] And there's no separate driver. The engine still only makes text. Some of that text says: run this command. [[app-runs]] The app is what actually runs it, and only if it's allowed.

## 07 — The surprises you'll hit
> Screen literal forms: two chat windows with different answers; a program with a key and an empty history; an "Allow this command?" prompt with Yes / No (illustrative, not a quote of one product); a model picker with generic rows and "Auto".
> Facts: differences between apps come from system prompts, settings, tools and model choice, plus sampling randomness (randomness gets its own lesson, 00.05; no teaser spoken). API calls carry only what the program sends. Some apps route to a model automatically. A model's answer about its own name or version is not reliable.
Four surprises you'll meet early. [[different]] Ask two apps the same question, and you get two different answers. Different hidden instructions, sometimes a different engine, and a little randomness every time. [[api-memory]] A program calling the A P I knows nothing about your chats in the app. Same engine, different door. [[allow]] An agent stops and asks: allow this command? That's the passenger seat working. Read it before you say yes. [[which-model]] And which model is this app using? Check its model picker; some apps choose for you. Don't ask the model: its answer about itself isn't reliable.

## 08 — Driving across the map
> What it connects to, plus "safe to ignore" in one line. Coding agents: 03 Dev environments (The Machine). Agents on git: 08 (The History). Keys for agents: 14 (Trust). "It may hold keys" keeps it true: not every agent has account keys. The recurring course line, with one honest addition.
When an agent drives, it crosses the map. [[machine]] It works in your files and your terminal: the Machine. [[history]] It can save its work with git: the History. [[trust]] It may hold keys to your accounts: Trust. AI is the lantern: [[lantern-line]] it lights every district, but it doesn't walk the streets for you. Even an agent only goes where you let it. [[later]] And which model tops this month's leaderboard? Safe to ignore for now.

## 09 — Keep this
> End card shows the same three bold leads as lesson.js keep.
Three things to keep. [[keep-1]] The model is the engine: a lab's file of numbers. Text in, text out, no memory of you. [[keep-2]] The app is the car: the chat window, your saved chats, the hidden instructions and the bill. One engine sits in many cars. [[keep-3]] An agent is the car you let drive: tools, a loop, and you in the passenger seat, deciding what it may do.
