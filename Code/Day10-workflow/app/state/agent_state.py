from pydantic import BaseModel


class AgentState(BaseModel):
    
    user_input:str | None

    intent:str | None

    answer:str | None