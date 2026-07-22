from llm.client import LLMClient

class AssistantAgent:

    def __init__(
        self,
        name:str,
        role: str,
        version: str,
        tools: list[str],
        memory: list[str],
        llm: LLMClient
    ):
        self.name = name
        self.role = role
        self.version = version
        self.tools = tools
        self.memory = memory
        self.llm = llm

    def introduce(self)->None:
        print(self.name)

    def show_info(self)->dict:
        return {
            "name" : self.name,
            "role" : self.role,
            "version" : self.version,
            "tools" : self.tools,
            "memory" : self.memory,
            "llm_name" : self.llm.model_name
        }
    def add_memory(
        self,
        message: str
    )->None:
        self.memory.append(message)
    
    def show_memory(self)->list[str]:
        return self.memory


    def run(self):
        return f"{self.name} is run"

    def chat(self, prompt : str)->str:
        return self.llm.generate(prompt)