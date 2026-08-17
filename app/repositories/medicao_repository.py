from app.database.mongodb import db


class MedicaoRepository:

    collection = db["medicoes"]

    @classmethod
    def create(cls, medicao_data: dict):
        result = cls.collection.insert_one(medicao_data)
        return str(result.inserted_id)

    @classmethod
    def find_all(cls, filters: dict, limit: int):
        cursor = cls.collection.find(filters).sort("timestamp", -1).limit(limit)
        return list(cursor)

    @classmethod
    def find_latest(cls, device_id: str = None):
        query = {"deviceId": device_id} if device_id else {}
        return cls.collection.find_one(query, sort=[("timestamp", -1)])