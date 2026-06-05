from fastapi import APIRouter
from app.schemas.user.patch_user_schema import UserUpdateSchema
from app.schemas.user.user_schema import UserCreateSchema
from app.schemas.user import post_user_schema
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create",
             summary="Create a new user",
             description="Create a new user in the system, use the example below to create a user.",
             response_model=post_user_schema.PostUserSchema)
def create_user(user: UserCreateSchema):
    user_service = UserService()
    return user_service.create_user(user)

@router.patch("/update",
              summary="Update an existing user",
              description="Update an existing user in the system, use the example below to update a user.",
                response_model=post_user_schema.PostUserSchema)
def update_user(user: UserUpdateSchema):
    user_service = UserService()
    return user_service.update_user(user)