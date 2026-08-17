from fastapi import APIRouter, Query, HTTPException, status
from datetime import datetime
from typing import Optional
from app.schemas.medicao.medicao_schema import MedicaoCreateSchema
from app.services.medicao_service import MedicaoService

router = APIRouter(prefix="/medicoes", tags=["Medições"])


@router.post("", status_code=status.HTTP_201_CREATED, summary="Registrar uma nova medição do ESP32")
def create_medicao(medicao: MedicaoCreateSchema):
    return MedicaoService.create_medicao(medicao)


@router.get("/latest", summary="Obter a medição mais recente")
def get_latest(deviceId: Optional[str] = Query(default=None)):
    result = MedicaoService.get_latest(deviceId)
    if not result:
        raise HTTPException(status_code=404, detail="Nenhuma medição encontrada")
    return result


@router.get("", summary="Listar medições")
def list_medicoes(
    deviceId: Optional[str] = Query(default=None),
    sensorId: Optional[str] = Query(default=None),
    inicio: Optional[datetime] = Query(default=None),
    fim: Optional[datetime] = Query(default=None),
    limit: int = Query(default=100, ge=1, le=1000),
):
    return MedicaoService.list_medicoes(deviceId, sensorId, inicio, fim, limit)