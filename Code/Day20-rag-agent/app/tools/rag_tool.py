from rag.loader import load_document
from rag.vectorstore import split_documents,create_vectorstore
from rag.retriever import create_retriever

from state.agent_state import AgentState

from langchain_community.vectorstores import FAISS



def bulid_chain():

    document=load_document()

    chunks=split_documents(document)

    vetorstore=create_vectorstore(chunks)

    retriever=create_retriever(vetorstore)

    return retriever


def search_docs(user_input: str) -> str:
    retriever = bulid_chain()
    documents = retriever.invoke(user_input)

    if not documents:
        return "知识库中没有找到相关信息。"

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context
