import os
from typing import TypedDict
from rag import get_context
from recommendation import generate_recommendation
from memory import memory  # Imported instance to fetch user profile data

# 1. Keep your state layout structure using standard Python types
class GraphState(TypedDict):
    question: str
    context: str
    answer: str

# 2. Keep your node logic exactly as you designed it
def retrieve_node(state: GraphState) -> GraphState:
    # Fixed typo: changed state["questions"] to state["question"]
    context = get_context(state["question"])
    state["context"] = context
    return state

def recommendation_node(state: GraphState) -> GraphState:
    # Use memory.profile and the retrieved context to build the answer
    answer = generate_recommendation(memory.profile, state["context"])
    state["answer"] = answer
    return state

# 3. Create a clean Python fallback class to mimic the graph compilation
class PythonWorkflowFallback:
    def __init__(self):
        pass

    def run(self, initial_state: dict) -> dict:
        """
        Executes your custom nodes sequentially instead of using LangGraph.
        Matches the path: Entry -> Retrieve Node -> Recommendation Node -> Finish
        """
        # Make a copy of the incoming state layout
        state = initial_state.copy()
        
        # Step 1: Run the retrieve node function
        state = retrieve_node(state)
        
        # Step 2: Run the recommendation node function
        state = recommendation_node(state)
        
        return state

# 4. Export the object as 'graph' so 'streamlit_app.py' imports it successfully
graph = PythonWorkflowFallback()
