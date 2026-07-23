from state.agent_state import AgentState

def chat_node(
    state:AgentState
)->AgentState:

    last_message=state["messages"][-1]

    answer={
        "role":"assistant",
        "content":
        f"你刚才说：{last_message['content']}"
    }

    state["messages"].append(answer)

    return state