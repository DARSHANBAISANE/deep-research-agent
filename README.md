Here is an updated `README.md` that incorporates both the original CLI execution and your new Streamlit Web UI:

```markdown
# 🤖 Deep Research Agent

An autonomous, multi-node research agent built with **LangGraph**, **LangChain**, and **Groq (Llama 3.3 70B)**. The agent receives a topic, conducts real-time web searches using DuckDuckGo (`ddgs`), and synthesizes the findings into structured research reports. 

Includes both an **Interactive Terminal (CLI)** and a **Streamlit Web UI**.

---

## 🌟 Features

- **Multi-Node Workflow:** Constructed using a LangGraph state graph separating search retrieval and writing steps.
- **Live Web Search:** Fetches real-time web results using `ddgs`.
- **Fast Reasoning:** Powered by `llama-3.3-70b-versatile` via Groq.
- **Dual Interfaces:** Run directly in the terminal or launch a modern Streamlit web application.

---

## 🛠️ Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/DARSHANBAISANE/deep-research-agent.git](https://github.com/DARSHANBAISANE/deep-research-agent.git)
cd deep-research-agent

```

### 2. Create and Activate Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate venv (Windows Command Prompt)
venv\Scripts\activate

# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

```

### 3. Install Required Dependencies

```bash
pip install langgraph langchain-groq python-dotenv ddgs streamlit

```

---

## 🔑 Environment Configuration

1. Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here

```


2. Obtain a free API key from [GroqCloud](https://console.groq.com/keys).

---

## 🚀 How to Run

### Option A: Launch the Streamlit Web UI (Recommended)

Run the web application in your browser:

```bash
streamlit run app.py

```

### Option B: Run via Terminal (CLI)

Run the command-line interface directly in your terminal:

```bash
python agent.py

```

---

## 📂 Project Structure

```text
deep-research-agent/
│── venv/               # Virtual environment (ignored)
│── .env               # API keys (ignored)
│── .gitignore          # Files excluded from Git
│── agent.py            # CLI version of the LangGraph agent
│── app.py              # Streamlit Web UI implementation
└── README.md           # Project documentation

```

---

## 🔗 Resources

* **API Key Provider:** [GroqCloud Console](https://console.groq.com/keys)
* **Framework:** [LangGraph Documentation](https://python.langchain.com/docs/langgraph)

```

---

