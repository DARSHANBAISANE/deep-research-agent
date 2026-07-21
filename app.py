import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# 1. Page Configuration
st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🤖",
    layout="centered"
)

# Load environment variables
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    st.error("🔑 `GROQ_API_KEY` is missing from your `.env` file!")
    st.stop()

# 2. Initialize LLM & Search Function
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

def perform_web_search(query: str) -> str:
    try:
        results = DDGS().text(query, max_results=3)
        return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Search error: {e}"

# 3. Define LangGraph State & Nodes
class AgentState(TypedDict):
    topic: str
    search_results: str
    final_report: str

def research_node(state: AgentState):
    topic = state["topic"]
    search_output = perform_web_search(topic)
    return {"search_results": search_output}

def writing_node(state: AgentState):
    prompt = f"""
    You are an expert research assistant. 
    Synthesize the following web search results into a clean, well-structured research summary with key takeaways.

    Topic: {state['topic']}
    Search Results: {state['search_results']}
    """
    response = llm.invoke(prompt)
    return {"final_report": response.content}

# 4. Build LangGraph Workflow
@st.cache_resource
def get_graph():
    builder = StateGraph(AgentState)
    builder.add_node("researcher", research_node)
    builder.add_node("writer", writing_node)
    builder.add_edge(START, "researcher")
    builder.add_edge("researcher", "writer")
    builder.add_edge("writer", END)
    return builder.compile()

graph = get_graph()

# 5. UI Layout
st.title("🤖 Deep Research Agent")
st.caption("Powered by LangGraph, Groq (Llama 3.3 70B), and DuckDuckGo")

topic_input = st.text_input(
    "Enter a research topic:",
    placeholder="e.g., Latest breakthroughs in quantum computing"
)

if st.button("Start Research", type="primary"):
    if not topic_input.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.status("🔍 Agent is conducting research...", expanded=True) as status:
            st.write("1️⃣ Querying web search via DuckDuckGo...")
            
            # Execute graph
            results = graph.invoke({"topic": topic_input})
            
            st.write("2️⃣ Synthesizing research report with Llama 3.3...")
            status.update(label="✅ Research Complete!", state="complete", expanded=False)

        # Display Final Report
        st.markdown("### 📊 Research Report")
        st.markdown(results["final_report"])