from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    nome: str = Field(min_length=1)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr = Field(min_length=1)
    celular: str = Field(min_length=9)