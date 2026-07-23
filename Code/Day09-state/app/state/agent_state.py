from pydantic import BaseModel

class AgentState(BaseModel):
    user_input : str
    # massages : list[str]
    # tool_result : str | None
    answer : str | None
    analysis : str | None



