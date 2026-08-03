from fastapi import APIRouter
from app.api.routes import reservoirs

api_router = APIRouter()

api_router.include_router(reservoirs.router)

@api_router.get("/")
def root():
    return {
        "message": "Welcome to AQUAGRID"
    }
