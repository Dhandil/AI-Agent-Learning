from state.agent_state import AgentState

from nodes.analyze import analyze

from nodes.chat import chat

from nodes.tool import weather

state=AgentState(
    user_input="hello",
    intent=None,
    answer=None
)


state=analyze(state)

if state.intent=="weather":
    state=weather(state)

else:
    state=chat(state)


print(state.answer)