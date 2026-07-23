from state.agent_state import AgentState
from node.analyze import analyze
from node.generate import generate

state = AgentState(
    user_input = "查询天气",
    # massages = [],
    # tool_result = None,
    answer = None,
    analysis= None
)

state = analyze(state)


state = generate(state)



print(state)