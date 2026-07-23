from state.agent_state import AgentState

from llm.client import LLMClient

def chat_node(
    state:AgentState,
    llm:LLMClient
)->AgentState:

    response=llm.generate(
        state["user_input"]
    )

    state["answer"]=response

    return state