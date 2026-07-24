from pathlib import Path

from langchain_community.document_loaders import TextLoader


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCUMENT_PATH = (
    BASE_DIR
    / "documents"
    / "company_rule.txt"
)


def load_documents():

    loader = TextLoader(
        str(DOCUMENT_PATH),
        encoding="utf-8"
    )

    documents = loader.load()

    return documents