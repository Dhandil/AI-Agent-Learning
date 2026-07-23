from state.agent_state import AgentState


def tool(
    state:AgentState
)->AgentState:

    state["answer"]="订单状态：已发货"

    return state