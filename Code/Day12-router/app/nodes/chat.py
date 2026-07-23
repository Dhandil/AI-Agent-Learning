from state.agent_state import AgentState


def chat(
    state:AgentState
)->AgentState:

    state["answer"]="普通聊天回答"

    return state