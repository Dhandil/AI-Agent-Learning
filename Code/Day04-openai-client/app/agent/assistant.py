class AssistantAgent:

    def __init__(
        self,
        name:str,
        role: str,
        version: str,
        tools: list[str],
        memory: list[str]
    ):
        self.name = name
        self.role = role
        self.version = version
        self.tools = tools
        self.memory = memory

    def introduce(self)->None:
        print(self.name)

    def show_info(self)->dict:
        return {
            "name" : self.name,
            "role" : self.role,
            "version" : self.version,
            "tools" : self.tools,
            "memory" : self.memory

        }
    def add_memory(
        self,
        message: str
    )->None:
        self.memory.append(message)
    
    def show_memory(self)->list[str]:
        return self.memory
agent1=AssistantAgent(
    name="AI 学习助手",
    role="帮助学习AI Agent",
    version="1.1.1",
    tools=[],
    memory=[]
)
agent2=AssistantAgent(
    name="新闻助手",
    role="每日推送新闻",
    version="1.1.2",
    tools=[],
    memory=[]
)

print(agent1.show_info())
print(agent2.show_info())

agent1.add_memory("11111111111")
print(agent1.show_memory())