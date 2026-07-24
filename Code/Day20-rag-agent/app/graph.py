from langgraph.graph import StateGraph,START,END

from state.agent_state import AgentState

from nodes.rag import rag
from nodes.analyze import analyze
from nodes.chat import chat

from router import router

def create_app():

    graph=StateGraph(AgentState)

    graph.add_node(
        "rag",
        rag
    )

    graph.add_node(
        "chat",
        chat
    )

    graph.add_node(
        "analyze",
        analyze
    )

    graph.add_edge(
        START,
        "analyze"
    )

    graph.add_conditional_edges(
        "analyze",
        router,
        {
            "chat":"chat",
            "rag":"rag"
        }
    )

    graph.add_edge(
        "chat",
        END
    )

    graph.add_edge(
        "rag",
        END
    )

    app=graph.compile()

    return app