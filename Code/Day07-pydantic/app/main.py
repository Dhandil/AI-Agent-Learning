from models.agent import AgentConfig
from models.llm import LLMConfig


llmconfig = LLMConfig(
    model = "seepseek",
    temperature= 0.4,
    max_tokens= 1000000
)
config = AgentConfig(
    name = "11111",
    role= "22222",
    version= "33333",
    llm = llmconfig
)

print(config)