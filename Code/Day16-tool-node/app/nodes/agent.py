from state.agent_state import AgentState



def agent_node(
    state:AgentState,
    llm
):

    response=llm.invoke(
        state["messages"]
    )

    state["messages"].append(response)

    return state