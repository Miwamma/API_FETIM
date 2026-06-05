from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    #schema para criar usuário
    nome: str = Field(min_length=1)
    cpf: str = Field(min_length=1)
    email: EmailStr = Field(min_length=1)
    celular: str = Field(min_length=1)