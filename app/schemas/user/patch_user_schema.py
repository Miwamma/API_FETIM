from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    cpf: Optional[str] = None
    cell: Optional[str] = None
    password: Optional[str] = None