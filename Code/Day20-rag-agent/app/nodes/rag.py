from state.agent_state import AgentState

from tools.rag_tool import search_docs

def rag(
    state:AgentState
)->AgentState:

    result=search_docs(state["user_input"])

    return {
        "answer":result
    }