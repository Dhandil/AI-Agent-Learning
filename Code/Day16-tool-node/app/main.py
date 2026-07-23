from langgraph.graph import (
    StateGraph,
    START,
    END
)


from state.agent_state import AgentState


from nodes.agent import agent_node

from nodes.tool import tool_node


from llm.client import FakeLLM


from tools.weather import get_weather



# 创建LLM

llm = FakeLLM(
    tools=[
        get_weather
    ]
)



# 创建Graph

graph = StateGraph(
    AgentState
)



# 添加节点


graph.add_node(
    "agent",
    lambda state:
    agent_node(
        state,
        llm
    )
)


graph.add_node(
    "tool",
    tool_node
)



# 起点

graph.add_edge(
    START,
    "agent"
)



# agent之后判断

graph.add_conditional_edges(

    "agent",

    lambda state:

        "tool"
        if "tool_calls"
        in state["messages"][-1]

        else "end",


    {

        "tool":"tool",

        "end":END

    }

)



# tool执行后回agent

graph.add_edge(
    "tool",
    "agent"
)



app = graph.compile()



result = app.invoke(

    {

        "messages":[

            {

            "role":"user",

            "content":
            "武汉天气怎么样"

            }

        ]

    }

)



print(result)
