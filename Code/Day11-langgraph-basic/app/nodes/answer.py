from state.agent_state import AgentState


def answer(
    state:AgentState
)->AgentState:

    state["answer"]=(
        "这是Agent生成的回答"
    )

    return state