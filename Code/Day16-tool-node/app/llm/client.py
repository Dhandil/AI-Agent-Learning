class FakeLLM:


    def __init__(self, tools):

        self.tools = tools



    def invoke(self, messages):


        # 第一次用户提问

        if messages[-1]["role"] == "user":


            if "天气" in messages[-1]["content"]:

                return {

                    "role":"assistant",

                    "tool_calls":[

                        {
                            "name":"get_weather",

                            "args":{
                                "city":"武汉"
                            }
                        }

                    ]

                }


        # 工具返回后

        elif messages[-1]["role"] == "tool":


            return {

                "role":"assistant",

                "content":

                f"根据查询结果：{messages[-1]['content']}"

            }



        return {

            "role":"assistant",

            "content":"普通回答"

        }