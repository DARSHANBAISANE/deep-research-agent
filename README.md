<img width="957" height="937" alt="Screenshot 2026-07-27 193316" src="https://github.com/user-attachments/assets/374fc23a-f0dc-4976-9923-52b0d19e9464" />
<img width="1837" height="943" alt="Screenshot 2026-07-27 193036" src="https://github.com/user-attachments/assets/9b83d36c-7200-4e44-b279-db47f61c93ee" />


https://github.com/user-attachments/assets/09728910-544d-44da-bdc9-d521f2886664

Here is the updated, complete **`README.md`** file that matches all your project requirements (*No RAG, No citation scoring, 2-Node Graph workflow*) and includes both CLI & Streamlit execution steps:

```markdown
# 🤖 Deep Research Agent

A lightweight, stateful **2-node research pipeline** built with **LangGraph**, **LangChain**, and **Groq (Llama 3.3 70B)**. 

The agent accepts a research topic, performs real-time web searches using DuckDuckGo, and synthesizes the retrieved results into a clean executive summary in seconds.

---

## 💡 Core Design Principles

- **No RAG:** Pure live web search and LLM synthesis—no vector databases, document chunking, or embeddings required.
- **Simple 2-Node Graph:** Architected as a simple two-node graph workflow (`researcher` → `writer`) rather than a complex multi-agent orchestration.
- **No Citation / Credibility Scoring:** Focused on rapid, direct research synthesis without source-ranking overhead.
- **Fast Reasoning:** Powered by `llama-3.3-70b-versatile` via Groq and DuckDuckGo (`ddgs`).

---

## 📁 Project Structure

```text
deep-research-agent/
├── venv/           # Virtual environment (ignored)
├── .env            # API keys (ignored)
├── .gitignore      # Git exclusion rules
├── agent.py        # Core 2-node LangGraph logic & CLI entry point
├── app.py          # Streamlit Web UI implementation
└── README.md       # Project documentation

```

---

## 🛠️ Prerequisites & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/DARSHANBAISANE/deep-research-agent.git](https://github.com/DARSHANBAISANE/deep-research-agent.git)
cd deep-research-agent

```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install langgraph langchain-groq python-dotenv ddgs streamlit

```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here

```

---

## 🚀 How to Run

### Option A: Streamlit Web UI

Launch the interactive web interface:

```bash
streamlit run app.py

```

### Option B: Terminal CLI

Execute the 2-node pipeline directly in your console:

```bash
python agent.py

```

---

## ⚙️ Architecture Workflow

1. **Node 1: `researcher**` — Queries the DuckDuckGo API (`ddgs`) for live web search snippets based on the input topic.
2. **Node 2: `writer**` — Takes the raw search output and passes it to Groq (`llama-3.3-70b-versatile`) to produce a structured summary.

```

```
