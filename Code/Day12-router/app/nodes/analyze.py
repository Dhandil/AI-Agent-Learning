from state.agent_state import AgentState


def analyze(
    state:AgentState
)->AgentState:

    message=state["user_input"]

    if "订单" in message:

        state["intent"]="tool"

    elif "RAG" in message:

        state["intent"]="rag"

    else:

        state["intent"]="chat"

    return state
