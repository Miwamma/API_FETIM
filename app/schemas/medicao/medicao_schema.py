from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class MedicaoCreateSchema(BaseModel):
    deviceId: str = Field(min_length=1, description="Identificador do ESP32 (ex: esp32-01)")
    sensorId: str = Field(min_length=1, description="Identificador do sensor (ex: YF-S201)")
    pulses: int = Field(ge=0, description="Quantidade de pulsos contados no intervalo")
    flowRate: float = Field(ge=0, description="Vazão instantânea, em L/min")
    volume: float = Field(ge=0, description="Volume medido no intervalo, em litros")
    totalLiters: float = Field(ge=0, description="Volume total acumulado, em litros")
    intervalSeconds: Optional[int] = Field(default=None, ge=0, description="Duração do intervalo de medição, em segundos")


class MedicaoResponseSchema(BaseModel):
    id: str
    deviceId: str
    sensorId: str
    pulses: int
    flowRate: float
    volume: float
    totalLiters: float
    intervalSeconds: Optional[int] = None
    timestamp: datetime