# Standard imports
from pydantic import BaseModel

class Message(BaseModel):
    msg: str

class Context(BaseModel):
    user_input: str
    bot_output: str