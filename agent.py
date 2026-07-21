import os
from typing import TypedDict
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS
from langgraph.graph import StateGraph, START, END

# Load API Key
load_dotenv()

# 1. Define Graph State (Holds topic, search results, and final report)
class AgentState(TypedDict):
    topic: str
    search_results: str
    final_report: str

# Initialize LLM (No RAG, no embedding models)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

# Node 1: Live Web Search (No Vector DB / RAG)
def research_node(state: AgentState):
    topic = state["topic"]
    try:
        results = DDGS().text(topic, max_results=3)
        formatted_results = "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        formatted_results = f"Search error: {e}"
    
    return {"search_results": formatted_results}

# Node 2: Synthesis (Pure LLM Summarization — No citation scoring or ranking)
def writing_node(state: AgentState):
    prompt = f"""
    Synthesize the following live web search results into a clean, well-structured research summary.

    Topic: {state['topic']}
    Search Results: {state['search_results']}
    """
    response = llm.invoke(prompt)
    return {"final_report": response.content}

# 2. Build Simple Two-Node Graph Workflow (Not a multi-agent system)
workflow = StateGraph(AgentState)

workflow.add_node("researcher", research_node)
workflow.add_node("writer", writing_node)

# Linear execution: START -> researcher -> writer -> END
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

# Compile graph
graph = workflow.compile()

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    output = graph.invoke({"topic": topic})
    print("\n--- Final Research Summary ---")
    print(output["final_report"])
