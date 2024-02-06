import os
import openai

from dotenv import load_dotenv, find_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma


load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
embeddings = OpenAIEmbeddings()

# loader = PyPDFLoader("C:/Users/ignac/Documents/chat-with-rag-using-langchain-nextjs-and-fastapi/backend/temp/RAG for LLM.pdf")
loader = PyPDFLoader(
    "C:/Users/ignac/Documents/chat-with-rag-using-langchain-nextjs-and-fastapi/backend/temp/MyCV_ES.pdf")
pages = loader.load_and_split(text_splitter)

# vector_db = Chroma.from_documents(
#     pages,
#     embeddings,
# )

vector_db = Chroma(
    embedding_function=embeddings
)

vector_db.add_documents(
    pages
)

query = "What did the president say about Ketanji Brown Jackson"
docs = vector_db.similarity_search(
    query=query,
    k=1
)

print(docs)
