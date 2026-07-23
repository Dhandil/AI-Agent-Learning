from tools.weather import get_weather

from state.agent_state import AgentState

def tool_node(
    state:AgentState
):

    last_message=state["messages"][-1]

    tool_call=last_message["tool_calls"][0]

    if tool_call["name"]=="get_weather":

        result=get_weather.invoke(tool_call["args"])

        state["messages"].append(
            {
                "role":"tool",
                "content":result
            }
        )
    return state