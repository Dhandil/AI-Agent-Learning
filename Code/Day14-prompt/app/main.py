from langgraph.graph import (
    StateGraph,
    START,
    END
)

from nodes.chat import chat_node

from state.agent_state import AgentState

from llm.client import LLMClient

llm=LLMClient("deepseek")

def chat(state:AgentState)->AgentState:

    return chat_node(
        state,
        llm
    )


graph=StateGraph(AgentState)

graph.add_node(
    "chat",
    chat
)

graph.add_edge(
    START,
    "chat"
)

graph.add_edge(
    "chat",
    END
)

app=graph.compile()

result=app.invoke(
    {
        "user_input":"什么是RAG？",
        "answer":""
    }

)

print(result)