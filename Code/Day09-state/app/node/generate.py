from state.agent_state import AgentState



def generate(state : AgentState)->AgentState:

    state.answer = "这是AI的回答"
    return state