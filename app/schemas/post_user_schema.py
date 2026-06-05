from pydantic import BaseModel

class PostUserSchema(BaseModel):
    message: str
    user_id: str    