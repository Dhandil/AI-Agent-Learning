from prompts.system import SYSTEM_PROMPT

from state.agent_state import AgentState

from llm.client import LLMClient


def chat_node(
    state:AgentState,
    llm:LLMClient
)->AgentState:
    
    prompt=f"""
    {SYSTEM_PROMPT}

    用户问题:
    {state["user_input"]}

    """

    state["answer"]=llm.generate(
        prompt
    )

    return state