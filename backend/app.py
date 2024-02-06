# Third-party imports
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Internal imports
from api.routes import chat
from api.routes import documents

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(chat.router)
app.include_router(documents.router)

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000
    )