# Third-party imports
from langchain_community.vectorstores import VectorStore
from langchain.chains import ConversationChain

# Internal imports
from prompts.strings import CHAT_PROMPT_TEMPLATE

from api.helpers.chat import count_tokens, retrieve_memory, retrieve_summary_memory, retrieve_llm


def chat_service(msg: str, vector_db: VectorStore) -> str:
    """
    Handles chat service
    """
    retrieved_docs = vector_db.similarity_search(
        query=msg,
        k=2
    )

    service = ConversationChain(
        llm=retrieve_llm(),
        memory=retrieve_memory(),
    )

    input = CHAT_PROMPT_TEMPLATE.format(msg, '\n- '.join([doc.page_content for doc in retrieved_docs]))
    response = service(input)

    print(response)

    return response
