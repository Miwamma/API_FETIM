from pydantic import BaseModel

class FlowSensorSchema(BaseModel):
    id: int
    name: str
    flow_rate: float
    unit: str