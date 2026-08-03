
from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="AQUAGRID API", version="0.1.0")

app.include_router(api_router)

@app.get("/health", tags=["System"])
def health():
    return {"status":"ok","service":"aquagrid-api"}
