from pydantic import BaseModel

class UserUpdateSchema(BaseModel):
    name: str | None = None
    cell: str | None = None
    password: str | None = None
    cpf: str | None = None
    email: str | None = None
    cell: str | None = None