from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    name: str = Field(
        min_length=1,
        description="Name of the user"
    )

    cpf: str = Field(
        min_length=1,
        description="CPF of the user"
    )

    email: EmailStr = Field(
        description="Email of the user"
    )

    cell: str = Field(
        min_length=1,
        description="Cell phone number of the user"
    )

    password: str = Field(
        min_length=8,
        description="Password must be at least 8 characters long."
    )