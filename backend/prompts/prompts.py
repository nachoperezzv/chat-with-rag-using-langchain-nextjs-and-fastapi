# Third-party imports
from langchain.prompts import PromptTemplate

# Internatl imports
from prompts.strings import CHAT_PROMPT_TEMPLATE
from prompts.strings import SUMMARIZE_PROMPT_TEMPLATE

summarize_prompt = PromptTemplate(
    template=SUMMARIZE_PROMPT_TEMPLATE, 
    input_variables=["text"]
)

chat_prompt = PromptTemplate(
    template=CHAT_PROMPT_TEMPLATE,
    input_variables=["docs", "history"]
)