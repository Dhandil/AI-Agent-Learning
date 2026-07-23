from langgraph.graph import StateGraph,START,END

from state.agent_state import AgentState

from nodes.answer import answer

from nodes.analyze import analyze


graph=StateGraph(AgentState)

graph.add_node(
    "analyze",
    analyze
)

graph.add_node(
    "answer",
    answer
)

graph.add_edge(
    "analyze",
    "answer"
)

graph.add_edge(
    START,
    "analyze"
)

graph.add_edge(
    "answer",
    END
)

app=graph.compile()

result=app.invoke(
    {
        "user_input":"什么是RAG",
        "answer":""
    }
)

print(result)