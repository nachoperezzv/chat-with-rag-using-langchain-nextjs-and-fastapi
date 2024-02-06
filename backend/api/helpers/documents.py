# Standard imports
import os
from dotenv import load_dotenv, find_dotenv

# Third-party imports
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import VectorStore

# Internal imports
from schemas.document import Document

load_dotenv(find_dotenv())

TEMP_PATH = os.getenv("TEMP_PATH")

def save_file(file:Document) -> str: 
    """
    Save file into memory so Langchain can read it after
    """
    filepath = f"{TEMP_PATH}/{file.filename}"
    with open(filepath, "wb+") as file_object:
        file_object.write(file.file.read())
    return filepath

def save_file_embedding(filepath: str, vector_db: VectorStore) -> list[str]:
    """
    Reads document and index it in the vector store
    """
    loader = PyPDFLoader(filepath)
    splitter = CharacterTextSplitter(chunk_size=500,)

    pages = loader.load_and_split(splitter)
    pages_ids = vector_db.add_documents(pages)

    return pages_ids
