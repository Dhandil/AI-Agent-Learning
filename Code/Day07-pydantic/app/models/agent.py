from pydantic import BaseModel
from models.llm import LLMConfig
class AgentConfig(BaseModel):
    name : str
    role : str
    version : str
    llm : LLMConfig


