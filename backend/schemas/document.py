# Standard imports
from pydantic import BaseModel
from typing import List

# Third-party imports
from fastapi import UploadFile

class Document(BaseModel):
    doc: UploadFile
    
class Documents(BaseModel):
    docs: List[Document]

