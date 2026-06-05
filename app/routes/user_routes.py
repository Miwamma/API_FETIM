from fastapi import APIRouter
from app.schemas.user_schema import UserCreateSchema
from app.schemas import post_user_schema
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",
             summary="Create a new user",
             description="Create a new user in the system, use the example below to create a user.",
             response_model=post_user_schema.PostUserSchema)
def create_user(user: UserCreateSchema):
    user_service = UserService()
    return user_service.create_user(user)

@router.delete("/{user_id}", 
               summary="Delete a user",
               description="Delete a user from the system")
def delete_user(user_id: str):
    user_service = UserService()
    return user_service.delete_user(user_id)