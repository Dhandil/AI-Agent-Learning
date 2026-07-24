from state.agent_state import AgentState



def analyze(
    state:AgentState
)->AgentState:

    message=state["user_input"]

    if "报销" in message:

        state["intent"]="查询RAG"

    else:
        state["intent"]="普通聊天"

    return state