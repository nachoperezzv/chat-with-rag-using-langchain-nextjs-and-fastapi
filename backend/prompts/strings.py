SUMMARIZE_PROMPT_TEMPLATE = """
Write a concise summary of the following:
{text}
CONSCISE SUMMARY IN THE LANGUAGE OF THE TEXT:"""

CHAT_PROMPT_TEMPLATE = """
Answer this:
{}

Use this information if needed to answer the question.
{}

RESPONSE:"""