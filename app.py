import os
import streamlit as st
from dotenv import load_dotenv

# Import compiled LangGraph workflow from agent.py
from agent import graph

# 1. Page Configuration
st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🤖",
    layout="centered"
)

# Load environment variables
load_dotenv()

# Verify API Key presence
if not os.getenv("GROQ_API_KEY"):
    st.error("🔑 `GROQ_API_KEY` is missing from your `.env` file!")
    st.stop()

# 2. Custom CSS for UI Enhancement (Fixed unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Main container padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 800px;
    }
    
    /* Header styling */
    .stTitle {
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    /* Badge styling */
    .tech-badge {
        display: inline-block;
        background-color: #262730;
        color: #FAFAFA;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 6px;
        border: 1px solid #363945;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.title("🤖 Deep Research Agent")
st.markdown("""
<div style="margin-bottom: 20px;">
    <span class="tech-badge">LangGraph</span>
    <span class="tech-badge">Groq (Llama 3.3 70B)</span>
    <span class="tech-badge">DuckDuckGo Search</span>
    <span class="tech-badge">No RAG</span>
</div>
""", unsafe_allow_html=True)

st.write("A lightweight, stateful **2-node research pipeline** that fetches live web search results and synthesizes clean executive summaries in seconds.")

st.divider()

# 4. User Input Section
st.subheader("🔍 What would you like to research?")

topic_input = st.text_input(
    label="Topic",
    label_visibility="collapsed",
    placeholder="e.g., Latest breakthroughs in fusion energy"
)

col1, col2 = st.columns([1, 4])
with col1:
    submit_btn = st.button("Start Research", type="primary", use_container_width=True)

# 5. Execution & Output Display
if submit_btn:
    if not topic_input.strip():
        st.warning("⚠️ Please enter a research topic first.")
    else:
        st.write("")
        # Status container showing execution steps
        with st.status("Executing 2-Node Graph Workflow...", expanded=True) as status:
            st.write("1️⃣ **[Node 1: Researcher]** Querying live web results via DuckDuckGo...")
            
            # Execute the LangGraph pipeline
            results = graph.invoke({"topic": topic_input})
            
            st.write("2️⃣ **[Node 2: Writer]** Synthesizing research report with Groq (Llama 3.3 70B)...")
            status.update(label="✅ Research Complete!", state="complete", expanded=False)

        # Display Final Synthesized Report inside a tab structure
        st.subheader("📊 Research Output")
        
        tab_report, tab_raw = st.tabs(["📄 Synthesized Report", "🔍 Raw Search Data"])
        
        with tab_report:
            st.markdown(results["final_report"])
            
        with tab_raw:
            st.caption("Raw snippets retrieved by Node 1 before LLM synthesis:")
            st.code(results.get("search_results", "No search results captured."), language="markdown")

# Footer
st.divider()
st.caption("💡 *Note: Designed as a simple 2-node graph pipeline without vector DBs or multi-agent orchestration.*")
