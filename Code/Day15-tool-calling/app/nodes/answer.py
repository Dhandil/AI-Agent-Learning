from state.agent_state import AgentState

def answer_node(
    state:AgentState
):

    result=state["tool_result"]

    state["answer"]=f"查询结果：{result}"

    return state

def answer(
    state:AgentState
)->AgentState:

    return answer_node(state)