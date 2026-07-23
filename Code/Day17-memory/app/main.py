from langgraph.graph import (
    StateGraph,
    START,
    END
)


from langgraph.checkpoint.memory import InMemorySaver


from state.agent_state import AgentState


from nodes.chat import chat_node



graph = StateGraph(
    AgentState
)



graph.add_node(
    "chat",
    chat_node
)



graph.add_edge(
    START,
    "chat"
)



graph.add_edge(
    "chat",
    END
)


# 创建保存器

memory = InMemorySaver()

app = graph.compile(
    checkpointer=memory
)



config={
    "configurable":{
        "thread_id":"user001"
    }
}

result1=app.invoke(

    {
        "messages":[
            {
                "role":"user",
                "content":"我叫小王"
            }
        ]
    },

    config=config

)

result2=app.invoke(

    {
        "messages":[
            {
                "role":"user",
                "content":"我叫什么?"
            }
        ]
    },

    config=config

)

print(result1)
print(result2)
