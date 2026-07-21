```markdown
# Day 3

# 今日主题

## 大模型 API 调用基础 —— 从聊天模型到企业 Agent


---

# ① 今天学习目标


今天学习：

- 理解什么是大模型 API
- 理解企业为什么需要 API 调用模型
- 理解 Chat Completions API 的基本思想
- 理解 Responses API 为什么更适合 Agent
- 理解 Message 结构设计
- 理解 Temperature、Token 等模型参数
- 理解企业为什么需要封装 LLM Client


学习完成后应该能够回答：

- 为什么企业不用 ChatGPT 网页版开发 Agent？
- API 在 Agent 系统中的作用是什么？
- 为什么业务代码不能直接调用模型？
- 为什么企业需要模型调用抽象层？


---

# ② 为什么要学习这个知识


# 1. 企业为什么需要大模型 API？


普通用户使用大模型：

```

用户

↓

浏览器

↓

ChatGPT

↓

回答

```


这种方式适合：

- 日常聊天
- 信息查询
- 内容生成


但是企业需要：

- 自动化处理任务
- 集成业务系统
- 控制权限
- 记录日志
- 管理成本


例如：

企业开发智能客服：


用户：

> 我的订单什么时候到？


完整流程：

```

用户

↓

客服系统

↓

Agent服务

↓

调用订单系统

↓

获取订单信息

↓

调用大模型生成回复

↓

返回用户

```


因此：

企业需要通过 API 将大模型能力嵌入自己的软件系统。


---

# 2. API 在 Agent 中的位置


完整架构：

```

用户

↓

前端应用

↓

Agent Backend

↓

LLM Client

↓

大模型 API

↓

模型

```


大模型负责：

- 理解
- 推理
- 生成


Agent系统负责：

- 流程控制
- 工具调用
- 数据管理
- 权限控制


---

# 3. 为什么不能直接使用 ChatGPT 网页版？


因为网页版本质是：

面向人的交互。


企业需要：

程序调用。


例如：

每天自动处理：

- 10000条客服消息
- 自动生成报告
- 自动分析数据


必须：

```

程序

↓

API

↓

模型

```


---

# ③ 原理讲解


# 1. 什么是 API？


API：

Application Programming Interface


中文：

应用程序接口。


简单理解：

> API 是两个软件系统之间通信的协议。


例如：

天气应用：

```

天气App

↓

天气API

↓

天气服务器

↓

返回天气数据

```


大模型 API：

也是一样：

```

程序

↓

发送请求

↓

模型服务器

↓

返回结果

```


---

# 2. 大模型 API 调用流程


一次请求：

```

用户输入

↓

Agent程序

↓

构造Request

↓

发送API请求

↓

模型推理

↓

返回Response

↓

Agent处理

↓

输出结果

````


---

# 3. Chat Completions API


传统大模型调用方式。


核心：

messages。


例如：

```json
[
    {
        "role": "system",
        "content": "你是一名助手"
    },
    {
        "role": "user",
        "content": "介绍一下RAG"
    }
]
````

模型根据：

system

和

user

生成回答。

---

# 4. 为什么 Message 使用 role？

因为模型需要区分：

不同信息来源。

例如：

System：

```
你是企业客服。

禁止泄露用户隐私。
```

User：

```
告诉我员工工资。
```

模型应该：

遵守 System。

优先级：

```
System

>

Developer

>

User
```

---

# 5. Responses API

Responses API：

是更适合 Agent 开发的新接口。

相比传统聊天接口：

更加关注：

* 工具调用
* 结构化输出
* 多步骤任务

Agent 工作流程：

```
用户

↓

Agent

↓

LLM推理

↓

调用Tool

↓

获取结果

↓

继续推理

↓

最终输出
```

因此：

Responses API 更符合 Agent 时代需求。

---

# 6. Temperature

Temperature：

控制模型输出随机性。

## 低 Temperature

例如：

```
0.1
```

特点：

输出稳定。

适合：

* 代码生成
* SQL生成
* 数据分析
* 企业流程

---

## 高 Temperature

例如：

```
0.8
```

特点：

输出更加创造性。

适合：

* 文案生成
* 创意设计
* 内容创作

---

# 7. Token 和成本

大模型 API 通常按照 Token 计费。

一次请求：

```
输入Token

+

输出Token
```

影响成本：

* Prompt长度
* 历史消息数量
* 输出长度

---

# 8. 企业如何优化 Token？

## 方法1：减少无效Prompt

避免：

大量重复规则。

---

## 方法2：使用RAG

不要：

```
把全部企业文档放入Prompt
```

应该：

```
用户问题

↓

检索相关文档

↓

发送给模型
```

---

## 方法3：Memory优化

长期对话：

不能保存所有历史。

需要：

* 摘要
* 压缩
* 长期记忆

---

# 9. 为什么需要 LLM Client？

错误设计：

```
业务代码

↓

OpenAI API
```

问题：

如果更换模型：

OpenAI

↓

Claude

↓

DeepSeek

大量代码需要修改。

---

正确设计：

```
业务层

↓

LLM Client

↓

模型供应商
```

例如：

业务代码：

```python
response = llm.generate(prompt)
```

底层：

可以切换：

```
OpenAI

Claude

Gemini

DeepSeek
```

---

# 10. LLM Client 的设计思想

本质：

软件工程中的：

适配器模式（Adapter Pattern）

作用：

屏蔽底层实现差异。

业务代码：

不关心：

* 哪个模型
* 哪个平台
* 哪种API

只关心：

输入和输出。

---

# ④ 企业实践

# 1. 企业 Agent 常见架构

```
Frontend

↓

Backend Service

↓

Agent Controller

↓

LLM Client

↓

Model API


Tool

↓

Database

↓

External System
```

---

# 2. 企业为什么需要中间层？

因为企业需要：

## 权限控制

例如：

普通员工：

只能查询。

管理员：

可以修改。

---

## 日志记录

记录：

* 用户请求
* 模型响应
* 工具调用

方便：

问题追踪。

---

## 模型切换

例如：

简单任务：

小模型。

复杂任务：

大模型。

---

# 3. 多模型策略

企业通常不会绑定一个模型。

例如：

```
简单分类

↓

小模型


复杂推理

↓

大模型


敏感任务

↓

人工审核
```

---

# ⑤ 代码实践

今天创建：

第一个企业级 LLM Client 结构。

代码位置：

```
Code/Day03-llm-api
```

目录：

```
Day03-llm-api

├── app

│   ├── main.py

│   │
│   └── llm

│       └── client.py

│

├── .env

└── requirements.txt
```

---

# 第一步：设计 LLM Client

client.py

```python
from typing import Protocol


class LLMClient(Protocol):
    """
    大模型调用接口抽象
    """

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        根据输入生成回复
        """
        ...
```

---

# 第二步：实现模型客户端

```python
class MockLLMClient:
    """
    模拟模型客户端
    """

    def generate(
        self,
        prompt: str
    ) -> str:
        """
        模拟返回结果
        """
        return (
            f"Model response for: {prompt}"
        )
```

---

# 第三步：业务调用

main.py

```python
from llm.client import MockLLMClient


def main() -> None:
    llm = MockLLMClient()

    response = llm.generate(
        "什么是RAG？"
    )

    print(response)


if __name__ == "__main__":
    main()
```

---

# 代码设计说明

为什么不直接：

```python
openai.xxx()
```

因为：

未来：

```
OpenAI

↓

DeepSeek
```

业务代码不用修改。

只替换：

LLM Client。

---

# ⑥ 今日项目

## 项目名称

企业级模型调用层设计

---

## 项目目标

实现：

一个独立的大模型调用模块。

让业务代码：

不依赖具体模型。

---

## 项目架构

```
用户

↓

Agent

↓

LLM Client

↓

Model API

↓

Response
```

---

## 今日完成内容

掌握：

* API基础
* 模型调用流程
* Responses API思想
* LLM Client设计

---

# ⑦ 思考题

## 1. 为什么企业不允许前端直接调用大模型 API？

答案：

因为：

1. API Key容易泄露。

2. 用户可能恶意调用。

3. 无法进行权限控制。

4. 难以更换模型供应商。

正确架构：

```
Frontend

↓

Backend

↓

LLM API
```

---

## 2. 一个客服 Agent 回答准确，但是速度很慢，应该如何优化？

答案：

不能直接优化，需要先定位瓶颈。

可能原因：

* Prompt过长
* 模型太大
* 请求量过高
* 缓存不足

优化：

* Prompt优化
* 模型选择
* 增加并发
* 使用缓存

---

## 3. 为什么企业需要封装 LLM Client？

答案：

因为：

* 实现系统分层
* 解耦业务和模型
* 支持多模型切换
* 降低维护成本

---

# ⑧ 面试知识

## 问题1：

为什么企业使用 API 调用大模型，而不是网页 ChatGPT？

标准答案：

网页 ChatGPT 面向人工交互，而企业需要将模型能力集成到业务系统中，实现自动化调用、权限控制、日志管理和业务流程融合。

---

## 问题2：

Temperature 有什么作用？

标准答案：

Temperature 控制模型输出随机性。

低 Temperature 提高稳定性，适合代码、SQL等任务。

高 Temperature 提高创造性，适合内容生成任务。

---

## 问题3：

为什么需要 LLM Client？

标准答案：

LLM Client 可以隔离业务代码和模型供应商，实现模型切换、统一管理和系统扩展。

---

# ⑨ 今日总结

今天必须记住：

1.

API 是程序调用大模型能力的入口。

---

2.

企业 Agent 不应该：

```
前端 → 大模型
```

应该：

```
前端

↓

Agent Backend

↓

LLM Client

↓

模型
```

---

3.

LLM Client 是企业 Agent 架构的重要抽象层。

---

4.

Agent 开发重点不是：

调用模型。

而是：

围绕模型设计可靠的软件系统。

---

# ⑩ 明天预告

Day 4：

## 第一个 AI Assistant —— 使用 OpenAI SDK 构建真实模型客户端

学习：

* OpenAI Python SDK
* API Key管理
* Responses API实战
* 第一个真实LLM调用
* 企业代码组织方式

---

# 完成状态

✅ 完成

```
```
