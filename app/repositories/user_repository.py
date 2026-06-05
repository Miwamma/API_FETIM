from app.database.mongodb import db

class UserRepository:

    collection = db["users"]

    @classmethod
    def create(cls, user_data):
        print("Dados recebidos:", user_data)

        result = cls.collection.insert_one(user_data)

        print("ID salvo:", result.inserted_id)

        return str(result.inserted_id)
    
    @classmethod
    def delete(cls, user_id):
        result = cls.collection.delete_one({"_id": user_id})
        return str(user_id)