from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS


def split_documents(
    documents
):
    spliter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )

    chunks=spliter.split_documents(documents)

    return chunks


def create_embedding():
    embedding=HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh"
    )

    return embedding

def create_vectorstore(
    chunks
):
    embedding=create_embedding()

    vectorstore=FAISS.from_documents(
        documents=chunks,
        embedding=embedding
    )

    return vectorstore