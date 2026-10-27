# Run backend locally:
# cd backend
# uv run uvicorn studysage.main:app --reload --reload-dir src

from fastapi import FastAPI

from studysage.api.documents import router as documents_router

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.include_router(documents_router)
