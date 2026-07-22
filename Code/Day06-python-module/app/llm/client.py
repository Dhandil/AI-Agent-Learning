class LLMClient:

    def __init__(
        self,
        model_name:str

    ):
        self.model_name= model_name

    def generate(
        self,
        prompt: str
    )->str:
        return f"""
        you:{prompt}
        {self.model_name}:hello"""