from langchain_community.vectorstores import Chroma


def create_retriever(
    vectorstore:Chroma
):
    retriever=vectorstore.as_retriever(
        search_kwargs={
            "k":3
        }
    )

    return retriever