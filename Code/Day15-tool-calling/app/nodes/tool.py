from tools.weather import get_weather

from state.agent_state import AgentState

def weather_node(
    state:AgentState
):
    city="武汉"

    result=get_weather(city)

    state["tool_result"]=result

    return state


def weather(
    state:AgentState
)->AgentState:

    return weather_node(state)