# PocketMuse — Multi-Agent Micro-Project Generator

PocketMuse is a lightweight multi-agent system that transforms a short user prompt into a complete micro-project.  
It generates research insights, multiple project ideas, feasibility scoring, and a polished one-page pitch with a  
7-day roadmap. Perfect for hackathons, ideation, personal productivity, students, and rapid prototyping.

---

## 🚀 Features

### ✅ Multi-Agent Architecture
- **ResearchAgent** → Fetches trends & reference links using custom tools  
- **IdeationAgent** → Generates multiple project ideas in parallel  
- **ValidatorAgent** → Scores feasibility, novelty & time  
- **ComposerAgent** → Produces final one-page pitch + roadmap  

### ✅ Tooling
- Custom Web Search Tool  
- System code execution tool  
- Structured logging  

### ✅ Memory & State
- In-memory session  
- Simple long-term memory JSON store  

### ✅ Observability
- Structured logs written to `/logs/pocketmuse.log`

### ✅ Gemini API Powered
Uses Google Gemini (via `google-genai`) as the main LLM.  
API key is loaded through the environment variable `GEMINI_API_KEY`.

---

## 🧠 What PocketMuse Does

Given a topic like:


PocketMuse produces:

- Research summary  
- 3+ project ideas (parallel agents)  
- Feasibility score  
- Final consolidated **one-page pitch + README + 7-day roadmap**  

---

## 📂 Project Structure

pocketmuse/
├─ app/
│ ├─ agents/
│ ├─ tools/
│ ├─ memory/
│ ├─ observability/
│ └─ llm_client.py
├─ examples/
│ └─ run_demo.py
├─ submission/
│ ├─ writeup.md
│ └─ video_script.md
├─ tests/
│ └─ test_smoke.py
├─ docs/
│ └─ architecture.png
├─ requirements.txt
└─ README.md


---

## 🔧 Installation & Setup

### 1. Create virtual environment

python -m venv venv
venv\Scripts\activate


### 2. Install dependencies
pip install -r requirements.txt
pip install google-genai


### 3. Set your Gemini API key
**Windows:**
setx GEMINI_API_KEY "YOUR_KEY_HERE"


Open a new terminal afterward.

Check:
echo %GEMINI_API_KEY%


---

## ▶️ Run Demo

python examples/run_demo.py


You will see logs and generated agent outputs.

---

## 🧪 Run Tests

pytest


Expected result:

1 passed


---

## 📦 Deployment

You can deploy using Docker or Cloud Run:

docker build -t pocketmuse .
docker run pocketmuse


For Cloud Run / Agent Engine, see `docs/deploy.md`.

---

## 📝 Submission Files for Kaggle

Located in:

submission/


Includes:
- writeup.md (project explanation)
- video_script.md (3-min video script)
- demo_output.txt (optional)

---

## 📜 License
MIT License.

---

## ⭐ Contribution
PRs welcome! This is a hackathon + capstone oriented multi-agent demo project.


