from llm.client import DeepSeekClient


def main() -> None:
    """
    程序入口。
    """

    llm = DeepSeekClient()

    answer = llm.generate(
        "什么是AI Agent？"
    )

    print(answer)


if __name__ == "__main__":
    main()