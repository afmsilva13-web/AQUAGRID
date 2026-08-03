from pydantic import BaseModel

class Reservoir(BaseModel):
    id: int
    name: str
    capacity_ml: float
    current_ml: float
