# 00.02 — The map of everything
<!-- lead=1.6 gap=0.8 tail=3 -->
<!-- captions: local host=localhost; four oh one=401; A P Is=APIs -->

## 01 — One road, five stops
> Final synthesis: spine of draft C (framework-first: the five stops in sentence one, map in 02, one message followed along the road, districts shelved on it). Grafts from A: "which stop" as the first useful question in 01, 401 Unauthorized as a surprise, "a service is someone else's computer" as keep-3. From B: the A P I as a service's counter for programs, where the key is checked; the router as the box every device goes through.
> Title card carries the one-line conclusion from frame 0: "One road, five stops. Ask which stop."
Everything you build with AI sits somewhere on one road: [[five-stops]] your computer, the network, the internet, services, and AI. When something breaks, the first useful question is [[which-stop]] which stop it's on. Learn that picture once, and [[land]] every later lesson has a place to land. Think of it as a road leading out of your room.

## 02 — Where it lives
> Map pin on 00. The Start label's question is read exactly as engine/map.js draws it: "what this course is, and the lantern you carry". The Lanterns are AI and never a district.
On the course map, this lesson sits at the [[pin]] Start, in Orientation: what this course is, and the lantern you carry. This is the view from the [[gate]] gate, before you walk into the six districts. One road, five stops, and [[lanterns]] lanterns strung over the whole thing.

## 03 — The road out of your room
> Aaron's story is one sentence on purpose: 00.01 told it in full. Only the true detail from COURSE.md (Python saved as .txt). Third person. "Dot T X T" letter by letter; screen shows script.txt.
> "Wi-Fi" is said "why-fye". GitHub, email and a payment page are generic examples; no prices, no popularity claims.
Stop one: [[computer]] your computer. Files, folders, programs, the terminal. Everything here is yours, and it still works with the Wi-Fi off. A lot of early confusion lives right here. Aaron, who made this course, once saved his Python as a dot T X T file. The code was fine. The problem was at stop one. Stop two: [[network]] the network. Your Wi-Fi, and the router: the box every device at home goes through on its way out. Stop three: [[internet]] the internet. Networks joined to other networks, all over the world. Nobody owns all of it. Stop four: [[services]] services. GitHub, your email, a payment page. Each one is someone else's computer, running all day, with its door open for requests. And stop five: [[ai]] AI. A model, usually running inside a service, answering in words.

## 04 — Follow one message
> Where the metaphor breaks, said plainly: it is not a line (services call services), and local models skip the road. No timings spoken on purpose: latency varies.
> The A P I as "a side counter for programs" is the plain version of: a service's defined interface for requests from code. A chat app checks your login (account and session), not an API key; keys belong to programs calling the API directly (see 10.11, subscriptions vs API billing). Both checks set up Trust (14).
Follow one message. You type a question into an AI chat. [[leave]] Your computer hands it to the Wi-Fi, and the router passes it out to the internet. The internet carries it to the right [[door]] service. The service checks it's really you, runs the model, and sends the answer [[back]] back down the road. Programs knock at a side counter, called an A P I, and show a key there. Here's where the picture breaks. [[breaks]] It isn't really a straight line. Services call other services. And some AI models run right on your own computer, with no road at all.

## 05 — Every district on the road
> Shelving per curriculum.md: Machine 01–03 and Code 04–07 on stop one; History 08 straddles stop one (git) and stop four (GitHub); Network 09–13 is the road and how things talk across it (APIs sit where the road meets the doors); Trust 14–16 at the services' doors; Shipping 17–20 puts your own thing at stop four.
> "A P Is" = "ay pee eyes".
Now the districts land on the road. [[machine]] The Machine and The Code live on your computer: files, the terminal, languages, packages. [[history]] The History starts there too. Git saves your work on your own machine; GitHub is the service where it's shared. [[network]] The Network is the road, and how things talk across it: networking, A P Is, websites, the cloud. [[trust]] Trust guards the doors of services: keys, logins, secrets. [[shipping]] And Shipping is the day you stop only visiting services, and become one.

## 06 — The surprises you'll hit
> Screen literal forms: localhost:3000 (port illustrative), "It works on my machine", 401 Unauthorized. "Local host" spoken as two words; "four oh one" spoken, captions show 401.
> Facts: localhost is this computer; a tool listening only on localhost is not reachable from other machines by default ("yet" covers that). HTTP 401 = the request lacks valid authentication credentials: missing, wrong, mistyped, expired or revoked.
Three phrases you'll meet early, and each one names a stop. [[localhost]] Local host means this computer. A tool running on local host is in your own room, and nobody else can reach it yet. [[my-machine]] It works on my machine means two computers differ: different files, different versions, different settings. That gap is a lesson, not a flaw in you. [[four-oh-one]] And four oh one, Unauthorized, means you reached the service, but the door didn't accept your key, or you brought none. Your code may be fine. That's Trust. So when something breaks, [[which-stop]] ask one question first: which stop am I at?

## 07 — The lantern: AI at every stop
> MCP is in module 10 (lantern lesson). "M C P" spelled for the ear. The recurring line closes the scene.
AI shows up at every stop. [[agent]] A coding agent edits files on your computer. It reaches its model [[across]] across the internet. With M C P, it can [[mcp]] reach other services for you. So it matters which stop it's standing at, and which keys it holds. AI is the lantern: [[light]] it lights every district, but it doesn't walk the streets for you.

## 08 — Safe to ignore for now
Some things look important and can wait. [[packets]] How routers pick a path. What's inside a packet. [[which-cloud]] Which cloud company is best. [[acronyms]] Every acronym on your network settings screen. For now, you only need to know which stop you're standing at.

## 09 — Keep this
> End card shows the same three bold leads as lesson.js keep.
Three things to keep. [[keep-1]] Everything sits on one road: your computer, the network, the internet, services, and AI lighting all of it. [[keep-2]] Ask which stop first. A problem in your room and a problem at a service's door need different fixes. [[keep-3]] A service is someone else's computer, with its door open. Most of the AI you use lives there, and answers back to yours.
