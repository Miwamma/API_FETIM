from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.user.patch_user_schema import UserUpdateSchema
from app.schemas.user.user_schema import UserCreateSchema
class UserService:

    @staticmethod
    def create_user(user: UserCreateSchema):
        existing_user = UserRepository.find_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email informed already exists, please enter another one")

        user_dict = user.model_dump()

        user_id = UserRepository.create(user_dict)

        return {"message": "Usuário criado com sucesso"}
    
    @staticmethod
    def update_user(user: UserUpdateSchema):
        user = UserRepository.find_by_email(user.email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_dict = user.model_dump()

        user_id = UserRepository.update(user_dict)

        return {"message": "Usuário atualizado com sucesso"}