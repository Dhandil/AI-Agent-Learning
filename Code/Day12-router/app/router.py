from state.agent_state import AgentState


def router(
    state:AgentState
):

    return state["intent"]