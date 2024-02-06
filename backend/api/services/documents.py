# Third-party imports
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import VectorStore

# Internal imports
from schemas.document import Document
from api.helpers.documents import (
    save_file, 
    save_file_embedding
)


def insert_doc_service(file:Document, vector_db:VectorStore) -> list[str]:
    """
    Handles the inyection of new documents into the vector store
    """
    filepath = save_file(file)
    doc_ids = save_file_embedding(filepath, vector_db)

    return doc_ids
    


