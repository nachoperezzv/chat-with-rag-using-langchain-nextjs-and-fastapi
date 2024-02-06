# Standard imports
import os
from dotenv import load_dotenv, find_dotenv

# Third-party imports
from tiktoken import get_encoding

from langchain_openai import ChatOpenAI

from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory

# Internal imports
from schemas.chat import Context
from prompts.prompts import summarize_prompt

load_dotenv(find_dotenv())

MAX_TOKENS_HISTORY = 1000
ENC_MODEL = 'cl100k_base'

enc = get_encoding(ENC_MODEL)

memory = ConversationBufferMemory()
llm = ChatOpenAI(
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-3.5-turbo"
)

def count_tokens(memory) -> int:
    """
    Returns the number of tokens in the history. Number of tokens based on gpt-4 tokenizer.
    """
    print(memory)
    print(memory.buffer)
    len(enc.encode(memory.buffer))

def retrieve_memory():
    """
    Returns conversation memory
    """    
    return memory

def retrieve_summary_memory():
    """
    Returns conversation memory summarized
    """
    return ConversationSummaryMemory(
            llm=llm,
            prompt=summarize_prompt,
            chat_memory=ChatMessageHistory().add_messages(memory)
        )

def retrieve_llm():
    "Return the llm used"
    return llm
