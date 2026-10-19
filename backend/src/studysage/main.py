# Run backend locally:
# cd backend
# uv run uvicorn studysage.main:app --reload --reload-dir src

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "hello world"}

@app.get("/health")
async def health_check():
        return {"status": "ok"}

