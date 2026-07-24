from langchain_community.document_loaders import TextLoader

from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

DOCUMENT_PATH=BASE_DIR/"document"/"message.txt"

def load_document():

    loader=TextLoader(
        str(DOCUMENT_PATH),
        encoding="utf-8"
    )

    documents=loader.load()

    return documents