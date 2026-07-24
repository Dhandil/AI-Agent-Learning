from state.agent_state import AgentState


def router(
    state:AgentState
)->AgentState:

    if state["intent"]=="查询RAG":

        return "rag"
    else:
        return "chat"