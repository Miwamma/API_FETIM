from app.database.mongodb import db

class UserRepository:

    collection = db["users"]

    @classmethod
    def create(cls, user_data):
        result = cls.collection.insert_one(user_data)
        return str(result.inserted_id)