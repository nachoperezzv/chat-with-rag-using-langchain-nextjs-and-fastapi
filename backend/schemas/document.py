# Standard imports
from pydantic import BaseModel

# Third-party imports
from fastapi import UploadFile

class Document(BaseModel):
    doc: UploadFile