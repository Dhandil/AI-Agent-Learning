from state.agent_state import AgentState


def analyze(
    state:AgentState
)->AgentState:
    
    if "天气" in state.user_input:
        state.intent="weather"

    else:
        state.intent="chat"

    return state
