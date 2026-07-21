import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated, Sequence
import operator

# Load environment variables
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is missing from your .env file!")

# 1. Initialize LLM & Web Search Tool
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
search_tool = DuckDuckGoSearchRun()

# 2. Define State
class AgentState(TypedDict):
    topic: str
    search_results: str
    final_report: str

# 3. Define Node Functions
def research_node(state: AgentState):
    topic = state["topic"]
    print(f"\n[1/2] 🔍 Searching web for: '{topic}'...")
    
    # Perform live web search
    search_output = search_tool.invoke(topic)
    return {"search_results": search_output}

def writing_node(state: AgentState):
    print("[2/2] ✍️ Synthesizing research report...")
    
    prompt = f"""
    You are an expert research assistant. 
    Synthesize the following web search results into a concise 3-bullet summary with key takeaways.

    Topic: {state['topic']}
    Search Results: {state['search_results']}
    """
    
    response = llm.invoke(prompt)
    return {"final_report": response.content}

# 4. Build the LangGraph Workflow
builder = StateGraph(AgentState)

builder.add_node("researcher", research_node)
builder.add_node("writer", writing_node)

# Flow: START -> researcher -> writer -> END
builder.add_edge(START, "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", END)

graph = builder.compile()

# 5. Interactive Terminal Execution
if __name__ == "__main__":
    print("========================================")
    print("      DEEP RESEARCH AGENT (GROQ)       ")
    print("========================================")
    
    user_topic = input("\nEnter a topic to research: ")
    
    if user_topic.strip():
        results = graph.invoke({"topic": user_topic})
        print("\n========================================")
        print("          FINAL RESEARCH REPORT         ")
        print("========================================\n")
        print(results["final_report"])