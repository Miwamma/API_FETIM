from datetime import datetime
from typing import Optional
from app.repositories.medicao_repository import MedicaoRepository
from app.schemas.medicao.medicao_schema import MedicaoCreateSchema


class MedicaoService:

    @staticmethod
    def create_medicao(medicao: MedicaoCreateSchema):
        medicao_dict = medicao.model_dump()
        medicao_dict["timestamp"] = datetime.utcnow()

        medicao_id = MedicaoRepository.create(medicao_dict)

        return {"message": "Medição registrada com sucesso", "id": medicao_id}

    @staticmethod
    def _serialize(doc: dict) -> dict:
        doc["id"] = str(doc.pop("_id"))
        return doc

    @staticmethod
    def list_medicoes(
        device_id: Optional[str] = None,
        sensor_id: Optional[str] = None,
        inicio: Optional[datetime] = None,
        fim: Optional[datetime] = None,
        limit: int = 100,
    ):
        filters = {}
        if device_id:
            filters["deviceId"] = device_id
        if sensor_id:
            filters["sensorId"] = sensor_id
        if inicio or fim:
            filters["timestamp"] = {}
            if inicio:
                filters["timestamp"]["$gte"] = inicio
            if fim:
                filters["timestamp"]["$lte"] = fim

        docs = MedicaoRepository.find_all(filters, limit)
        return [MedicaoService._serialize(doc) for doc in docs]

    @staticmethod
    def get_latest(device_id: Optional[str] = None):
        doc = MedicaoRepository.find_latest(device_id)
        if not doc:
            return None
        return MedicaoService._serialize(doc)