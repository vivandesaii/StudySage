# Run backend locally:
# cd backend
# uv run uvicorn studysage.main:app --reload --reload-dir src

from fastapi import FastAPI, HTTPException
from studysage.schemas import DocumentCreate


app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/documents", status_code=201)
async def accept_document(document: DocumentCreate):

    return document
