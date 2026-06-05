from pydantic import BaseModel

class CurrentSensorSchema(BaseModel):
    id: int
    name: str
    current_value: float
    unit: str