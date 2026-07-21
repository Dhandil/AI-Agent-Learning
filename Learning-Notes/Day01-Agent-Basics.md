```markdown
# Day 1

# 今日主题

## 什么是 AI Agent —— 从大模型到智能体


---

# ① 今天学习目标


今天学习：

- 理解 AI Agent 的本质
- 理解 LLM 与 Agent 的区别
- 理解为什么企业需要 Agent
- 理解 Agent 的基本组成架构
- 建立 Agent 工程开发的整体认知


学习完成后应该能够回答：

- 什么是 Agent？
- 为什么大模型不是 Agent？
- Agent 为什么需要工具？
- 企业为什么需要 Agent 系统？


---

# ② 为什么要学习这个知识


## 1. 企业为什么需要 AI Agent？


传统软件系统：

```

用户输入

↓

固定程序逻辑

↓

输出结果

```


这种方式的问题：

- 流程固定
- 无法理解自然语言
- 难以处理复杂任务


例如：

传统客服系统：

用户：

> 我的订单什么时候到？


系统：

根据固定规则查询。


但是用户可能：

- 表达方式不同
- 问题不完整
- 需要多个系统协作


例如：

```

查询订单

↓

查询物流

↓

判断异常

↓

生成回复

```


传统程序需要大量人工编写规则。


---

## 2. 大模型带来的变化


大语言模型具有：

- 语言理解能力
- 推理能力
- 内容生成能力


但是：

LLM 本身不能执行任务。


例如：

用户：

> 帮我查询订单并通知客户。


LLM 可以理解：

"查询订单"

"通知客户"


但是不能：

- 访问订单数据库
- 发送消息


因此需要：

Agent。


---

## 3. Agent 解决什么问题？


Agent 的目标：

> 让模型不仅能够思考，还能够执行。


企业希望：

AI 不只是回答问题。

而是：

完成工作。


例如：

智能客服 Agent：

```

用户问题

↓

理解意图

↓

调用订单系统

↓

获取数据

↓

生成回复

↓

发送给用户

```


---

# ③ 原理讲解


# 1. 什么是 AI Agent？


AI Agent：

> 一个以大语言模型为核心，通过工具调用、状态管理、记忆和规划机制，自主完成任务的软件系统。


简单理解：


```

Agent

=

大脑

*

手脚

*

记忆

*

行动能力

```


对应关系：


| 人 | Agent |
|----|----|
| 大脑 | LLM |
| 手脚 | Tool |
| 记忆 | Memory |
| 思考过程 | Planning |
| 行动流程 | Workflow |


---

# 2. LLM 和 Agent 的区别


## LLM


LLM：

负责：

- 理解
- 推理
- 生成


结构：

```

用户

↓

LLM

↓

文本回答

```


---

## Agent


Agent：

负责：

- 分析任务
- 制定计划
- 调用工具
- 获取结果
- 完成目标


结构：

```

用户

↓

Agent

↓

LLM推理

↓

Tool调用

↓

外部系统

↓

结果反馈

↓

最终输出

```


---

# 3. 为什么没有工具不能叫 Agent？


因为：

智能任务不仅需要思考，还需要执行。


例如：

要求：

> 查询今天上海天气。


LLM：

知道天气相关知识。


但是：

不知道今天真实天气。


需要：

```

LLM

↓

Weather API

↓

实时天气数据

```


工具让 Agent 连接现实世界。


---

# 4. Agent 基本架构


企业 Agent 通常包含：


```

```
             用户

               |

               ↓

          Agent Controller

               |

    -----------------------

    |                     |

   LLM                 Memory


    |

    ↓

 Tool Calling

    |
```

---

|       |        |

API   数据库   文件系统

```


---

# 5. Agent 的核心循环


很多 Agent 使用：

Reason-Act-Observe


循环：

```

Reason

↓

决定下一步行动

↓

Act

↓

调用工具

↓

Observe

↓

获取结果

↓

继续推理

```


直到：

任务完成。


---

# ④ 企业实践


## 1. OpenAI 类 Agent 系统


企业通常不会直接：

```

用户

↓

GPT

```


而是：


```

用户

↓

业务系统

↓

Agent服务

↓

LLM

↓

Tools

↓

企业数据

```


原因：

需要：

- 权限控制
- 日志
- 数据隔离
- 流程管理


---

## 2. 企业 Agent 实际案例


### 智能客服 Agent


能力：

- 理解用户问题
- 查询订单
- 查询物流
- 创建工单


涉及：

Tools：

```

order_query()

create_ticket()

send_message()

```


---

### 企业知识助手


能力：

- 查询内部文档
- 总结资料
- 回答员工问题


架构：

```

Agent

↓

RAG

↓

企业知识库

```


---

### 自动化办公 Agent


能力：

- 处理邮件
- 创建会议
- 总结文档


需要：

- Tool
- Memory
- Permission


---

# ⑤ 代码实践


今天暂不编写完整 Agent。

目标：

理解 Agent 最基础代码结构。


创建：

```

Code/Day01-agent-basics

```


目录：

```

Day01-agent-basics

├── main.py

├── agent.py

└── tools.py

````


---

## 第一步：定义 Agent


agent.py


```python
class Agent:
    """
    基础 Agent 类
    """

    def __init__(self, name: str):
        self.name = name

    def run(self, task: str) -> str:
        """
        执行任务
        """
        return f"{self.name} received task: {task}"
````

---

## 第二步：创建 Agent

main.py

```python
from agent import Agent


def main() -> None:
    agent = Agent("assistant")

    result = agent.run(
        "帮助用户查询订单"
    )

    print(result)


if __name__ == "__main__":
    main()
```

---

## 代码理解

目前：

```
Agent

↓

接收任务

↓

返回结果
```

还没有：

* LLM
* Tool
* Memory

后续课程会逐步加入。

---

# ⑥ 今日项目

## 项目名称

基础 Agent 架构设计

---

## 项目目标

创建一个最简单 Agent 框架。

实现：

* Agent对象
* Task输入
* 执行入口

---

## 项目架构

```
User

↓

Agent

↓

Task Handler

↓

Result
```

---

## 今日完成内容

理解：

* Agent是什么
* Agent和LLM区别
* Agent基本组成

---

# ⑦ 思考题

## 1. 为什么 ChatGPT 不是完整 Agent？

答案：

因为 ChatGPT 主要负责文本生成。

它本身没有：

* 工具调用
* 外部系统访问
* 状态管理
* 自动执行流程

---

## 2. 如果一个 Agent 只有 LLM，没有 Tool，可以吗？

答案：

可以实现简单问答。

但是无法完成真实世界任务。

企业 Agent 通常必须具备工具能力。

---

## 3. 一个企业客服 Agent 为什么不能只依靠 Prompt？

答案：

因为 Prompt 只能影响模型行为。

不能：

* 查询数据库
* 修改订单
* 执行业务流程

需要：

Prompt + Tool + Workflow。

---

# ⑧ 面试知识

## 问题1：

什么是 AI Agent？

标准答案：

AI Agent 是一种以大语言模型为核心，通过工具调用、记忆、规划和工作流机制，实现自主完成复杂任务的软件系统。

---

## 问题2：

LLM 和 Agent 有什么区别？

标准答案：

LLM 是负责理解和生成的模型，而 Agent 是基于 LLM 构建的软件系统，通过工具、记忆和流程控制完成具体任务。

---

## 问题3：

为什么 Agent 需要 Tool？

标准答案：

因为 LLM 只能进行信息处理，无法直接影响外部世界。Tool 可以让 Agent 调用外部系统，实现查询、修改和执行操作。

---

# ⑨ 今日总结

今天必须记住：

1.

LLM ≠ Agent。

LLM 是大脑。

Agent 是完整系统。

---

2.

Agent 的核心：

```
LLM

+

Tool

+

Memory

+

Workflow
```

---

3.

企业开发 Agent：

重点不是调用模型。

而是设计可靠的软件系统。

---

4.

Agent 的价值：

让 AI 从：

"回答问题"

变成：

"完成任务"。

---

# ⑩ 明天预告

Day 2：

## Prompt Engineering —— 如何控制 Agent 的行为

学习：

* Prompt 为什么有效
* System Prompt
* User Prompt
* Context Window
* Token
* 企业 Prompt 设计方法

---

# 完成状态

✅ 完成


