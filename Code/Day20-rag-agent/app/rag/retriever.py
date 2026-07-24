from langchain_community.vectorstores import FAISS

def create_retriever(
    vectorstore:FAISS
):

    retriever=vectorstore.as_retriever(
        search_kwargs={
            "k":3
        }
    )

    return retriever