from langgraph.graph import (
    StateGraph,
    START,
    END
)

from state.agent_state import AgentState

from nodes.analyze import analyze

from nodes.tool import tool

from nodes.chat import chat

from nodes.rag import rag


graph=StateGraph(AgentState)

graph.add_node(
    "analyze",
    analyze
)

graph.add_node(
    "chat",
    chat
)

graph.add_node(
    "rag",
    rag
)

graph.add_node(
    "tool",
    tool
)

graph.add_edge(
    START,
    "analyze"
)

graph.add_edge(
    "chat",
    END
)

graph.add_edge(
    "rag",
    END
)

graph.add_edge(
    "tool",
    END
)


from router import router

graph.add_conditional_edges(
    "analyze",
    router,
    {
        "chat":"chat",
        "rag":"rag",
        "tool":"tool"
    }
)

app=graph.compile()

result=app.invoke(
    {
        "user_input":"你好",
        "intent":"",
        "answer":""
    }
)

print(result)