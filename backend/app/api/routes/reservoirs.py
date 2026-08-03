from fastapi import APIRouter
from app.models.reservoir import Reservoir

router = APIRouter(prefix="/reservoirs", tags=["Reservoirs"])

reservoirs = [
    Reservoir(
        id=1,
        name="West Reservoir",
        capacity_ml=120,
        current_ml=96
    ),
    Reservoir(
        id=2,
        name="North Tank",
        capacity_ml=25,
        current_ml=18
    ),
]

@router.get("/")
def get_reservoirs():
    return reservoirs
