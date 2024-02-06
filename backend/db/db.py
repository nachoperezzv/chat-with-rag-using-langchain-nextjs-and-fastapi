# Standard imports
import os
import openai

# Third-party imports
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings()

def get_db():
    db = Chroma(embedding_function=embeddings)
    try:
        yield db
    finally:
        del db