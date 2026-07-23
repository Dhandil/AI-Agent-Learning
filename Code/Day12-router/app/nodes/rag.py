from state.agent_state import AgentState


def rag(
    state:AgentState
)->AgentState:

    state["answer"]="这是RAG检索后的回答"

    return state