# PocketMuse — Micro-Project Generator Agent  
### Freestyle Track — Agents Intensive Capstone Project  

---

## 🧩 Problem Statement  
Coming up with a well-structured project idea is one of the biggest bottlenecks for students, solo developers, and hackathon participants.  
People often have vague ideas like *“I want to build something with AI”*, but converting that into a **clear, scoped, feasible project** requires hours of research, brainstorming, evaluation, and planning.

This early stage frequently kills motivation because:
- Research is overwhelming  
- Brainstorming gets chaotic  
- Ideas aren’t evaluated for feasibility  
- There’s no clear roadmap to begin  
- People don't know which ideas are worth pursuing  

**PocketMuse** solves this by automating the “0 → 1 project creation step”.  
It turns a short prompt (like *“ai apps”*) into a structured micro-project including:
- Trend-aware research  
- Multiple brainstormed project ideas  
- Automated feasibility scoring  
- A final polished one-page pitch  
- A 7-day execution roadmap  

This allows creators to spend time **building**, not struggling with ideation.

---

## 🤖 Why Agents?  
This problem is a natural fit for agents because each step in project creation requires a *specialized thinking process*:

| Stage | What’s Needed | Best Tool |
|-------|---------------|----------|
| Research | External information + summarization | Tool-using research agent |
| Ideation | Divergent thinking, variety, creativity | Parallel LLM agents |
| Validation | Rule-based scoring, feasibility checks | Evaluation agent |
| Composition | Structured, multi-section formatting | Composer agent |
| Personalization | Carrying context across sessions | Memory bank + session service |

Instead of one monolithic LLM call, PocketMuse uses a **multi-agent system**, where each agent has a **clear responsibility**, making the pipeline:
- Modular  
- Auditable  
- Extensible  
- Deterministic  
- Easy to debug using logs  

Agents make the solution scalable, reliable, and production-friendly.

---

## 🏗️ What I Created — Architecture Overview  

PocketMuse is a **4-agent pipeline**, enhanced with tools, memory, and observability:

User Prompt
↓
Research Agent
↳ Uses web_search tool
↓
Ideation Agent (Parallel)
↳ Generates multiple ideas simultaneously
↓
Validator Agent
↳ Scores ideas on novelty, feasibility, timeline
↓
Composer Agent
↳ Produces final one-page pitch + README + roadmap
↓
Output delivered


### ✔ Features implemented (required by the Capstone instructions)
- **Multi-agent system**
  - Sequential (research → ideation → validator → composer)
  - Parallel agents (three idea generators)
- **Tools**
  - Custom `web_search` tool  
  - Optional `code_exec` tool
- **Sessions & Memory**
  - `MemoryBank` stores user preferences & prior prompts
  - `InMemorySessionService` supports stateful workflows
- **Observability**
  - Structured logging using custom `Logger`
- **Gemini Integration**
  - `google-genai` API client in `llm_client.py`
- **Runnable demo**
  - `python examples/run_demo.py`
- **Smoke test**
  - `tests/test_smoke.py` validates agent pipeline runs end-to-end

---

## 🎬 Demo  

When running:

```bash
python examples/run_demo.py


Example output:

LOG> {"event": "research.start", "topic": "ai apps"}
LOG> {"event": "ideation.start", "n": 3}
LOG> {"event": "validate.start"}
LOG> {"event": "compose.start"}

Final Composed Output:
-----------------------------------------
Micro-project pitch generated using Gemini:
• Idea Summary
• What / Why / How
• Tech Stack
• 7-Day Execution Roadmap


A detailed sample output is stored in:

submission/demo_output.txt

**The Build — Tools & Technologies Used
Languages & Frameworks**

-Python 3.10+

-Gemini via google-genai

**Architecture**

-Modular agent classes under app/agents

-Tool system under app/tools

-Memory system under app/memory

-Logger for observability

-Demo workflow under examples/

-Tests under tests/

**Key libraries**

google-genai (Gemini)

pytest (testing)

fastapi(for deployment / API exposure)

**Core Files**
File	Purpose
app/llm_client.py	Unified LLM wrapper for Gemini
research_agent.py	Trend research agent
ideation_agent.py	Parallel ideation
validator_agent.py	Feasibility evaluation
composer_agent.py	Final output generator
web_search.py	Custom search tool
logger.py	Observability
memory_bank.py	Persistent memory
run_demo.py	Demo pipeline
test_smoke.py	End-to-end test


## If I Had More Time

If the project were extended beyond the hackathon timeframe, I would evolve PocketMuse into a more complete, production-ready system. My planned improvements include:

### 1. Deployment to Cloud Run / Agent Engine
I would deploy PocketMuse as a live, publicly accessible API.  
This would allow users to generate micro-projects on demand from anywhere, and would demonstrate real cloud-based agent orchestration.

### 2. A Front-End UI
I would build a minimal web interface to make PocketMuse usable without touching code.  
The UI would allow users to:
- Enter a prompt
- View multiple ideas side-by-side
- Select the idea they want to finalize
- Download the final one-page pitch, README, or roadmap as a PDF

### 3. Adaptive Idea Ranking
PocketMuse could become smarter over time by learning from user selections.  
A lightweight reinforcement-learning style “ranking memory” could record which ideas people choose most often and adapt future ideation using:
- historical ranking data  
- user-specific preferences  
- scoring heuristics

### 4. GitHub Integration
I would add an automated GitHub workflow that:
- Creates a new repository for the chosen project
- Generates a starter folder structure
- Commits a README, roadmap, and placeholder code
- Pushes everything to the user’s GitHub automatically  
This turns PocketMuse into a true “project generator.”

### 5. Plugin Ecosystem
To make PocketMuse extensible, I would enable optional “idea packs,” such as:
- **Startup Ideas Pack** — business, SaaS, and MVP-driven concepts  
- **Research Automation Pack** — academic project ideas  
- **Academic Project Pack** — college-level project blueprints  
- **Creative Pack** — art, stories, games, and entertainment concepts  

This would allow users to customize PocketMuse based on industry or personal interests.

---

