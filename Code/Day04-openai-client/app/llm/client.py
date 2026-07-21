import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class DeepSeekClient:
    """
    DeepSeek模型客户端。

    使用OpenAI SDK兼容接口调用。
    """

    def __init__(self) -> None:
        api_key = os.getenv(
            "DEEPSEEK_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY不存在"
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )


    def generate(
        self,
        prompt: str
    ) -> str:
        """
        调用DeepSeek生成文本。
        """

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content