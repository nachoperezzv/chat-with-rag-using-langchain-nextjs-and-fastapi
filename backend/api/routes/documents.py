# Third-party imports
from fastapi import APIRouter, Depends
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse

from langchain_community.vectorstores import VectorStore

# Internal imports
from api.services.documents import insert_doc_service

from db.db import get_db

router = APIRouter(
    prefix="/document",
)


@router.post("")
async def insert_doc(
    file: UploadFile = File(...),
    vector_db: VectorStore = Depends(get_db)
) -> JSONResponse:
    """
    Handles Endpoint for the insertion of a new PDF doc
    """
    try:
        doc_ids = insert_doc_service(file, vector_db)
        return JSONResponse(
            status_code=200,
            content={"doc_ids": doc_ids}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"message": "Error uploading document: {}".format(e)}
        )
