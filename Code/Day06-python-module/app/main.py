from agent.assistant import AssistantAgent
from llm.client import LLMClient

llm = LLMClient("deepseek")

agent = AssistantAgent(
    name= "ddddd",
    role= "sssss",
    version= "1.1.1",
    tools= [],
    memory= [],
    llm = llm
)

response = agent.chat("22222")
print(response)

