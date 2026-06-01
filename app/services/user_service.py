from app.schemas.user_schema import UserCreateSchema

class UserService:

    @staticmethod
    def create_user(user: UserCreateSchema):

        return {
            "message": "Usuário criado com sucesso",
            "user": user
        }