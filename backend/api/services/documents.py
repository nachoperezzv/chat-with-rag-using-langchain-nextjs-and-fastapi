# Third-party imports
from langchain_community.vectorstores import VectorStore

# Internal imports
from schemas.document import Documents
from api.helpers.documents import (
    save_file, 
    save_file_embedding
)


def insert_doc_service(files:Documents, vector_db:VectorStore) -> list:
    """
    Handles the inyection of new documents into the vector store
    """
    docs = []
    for file in files:
        filepath = save_file(file)
        doc_ids = save_file_embedding(filepath, vector_db)

        docs.append(doc_ids)
    
    return docs


