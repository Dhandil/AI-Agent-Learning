from langgraph.graph import StateGraph,START,END

from nodes.tool import weather

from nodes.answer import answer

from state.agent_state import AgentState


graph=StateGraph(AgentState)

graph.add_node(
    "answer",
    answer
)

graph.add_node(
    "weather",
    weather
)

graph.add_edge(
    START,
    "weather"
)

graph.add_edge(
    "weather",
    "answer"
)

graph.add_edge(
    "answer",
    END
)

app=graph.compile()

result=app.invoke(
    {
        "user_input":"武汉天气怎么样",
        "tool_result":"",
        "answer":""
    }

)

print(result)