from app.repositories.user_repository import UserRepository
class UserService:

    @staticmethod
    def create_user(user):

        user_dict = user.model_dump()

        user_id = UserRepository.create(user_dict)

        return {"message": "Usuário criado com sucesso", "user_id": user_id}
    

    @staticmethod
    def delete_user(user_id):
        # Lógica para deletar um usuário
        user_id = UserRepository.delete(user_id)
        return {"message": "Usuário deletado com sucesso", "user_id": user_id}