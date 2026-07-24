from rag.chain import build_chain


retriever = build_chain()


result = retriever.invoke(
    "住宿怎么报销？"
)


print("检索结果数量：", len(result))


for i, doc in enumerate(result, start=1):

    print(f"\n========== 第{i}条 ==========")

    print(doc.page_content)