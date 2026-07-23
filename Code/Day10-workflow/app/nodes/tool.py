from state.agent_state import AgentState


def weather(
    state:AgentState
)->AgentState:
    
    state.answer="今天晴天，30度"

    return state