from state.agent_state import AgentState


def analyze(state : AgentState)->AgentState:
    state.analysis = "这是一个简单问题"
    return state