from fastapi import APIRouter
from app.schemas.user_schema import UserCreateSchema
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create")
def create_user(user: UserCreateSchema):
    return UserService.create_user(user)