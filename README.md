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
