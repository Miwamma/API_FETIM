from fastapi import APIRouter
from app.schemas.user_schema import UserCreateSchema
from app.services.user_service import UserService
from app.database.mongodb import users_collection

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserCreateSchema)
def create_user(user: UserCreateSchema):
    user_service = UserService()
    result = users_collection.insert_one(user)
    return user_service.create_user(user)
