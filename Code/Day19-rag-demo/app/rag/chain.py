from rag.loader import load_documents

from rag.vectorstore import (
    split_documents,
    create_vectorstore,
)

from rag.retriever import create_retriever


def build_chain():

    documents = load_documents()

    chunks = split_documents(documents)

    vectorstore = create_vectorstore(chunks)

    retriever = create_retriever(vectorstore)

    return retriever