from pydantic import BaseModel

class LLMConfig(BaseModel):
    model : str
    temperature : float
    max_tokens : float