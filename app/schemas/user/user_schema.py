from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreateSchema(BaseModel):
    name: str = Field(min_length=1, description="Name of the user")

    cpf: str = Field(description="CPF of the user (11 digits, numbers only)")

    email: EmailStr = Field(description="Email of the user")

    cell: str = Field(min_length=1, description="Cell phone number of the user")

    password: str = Field(min_length=8, description="Password must be at least 8 characters long.")

    @field_validator("cpf")
    @classmethod
    def validate_cpf(cls, value):
        value = str(value).strip()

        if not value.isdigit():
            raise ValueError("CPF deve conter apenas números")

        if len(value) != 11:
            raise ValueError("CPF deve ter exatamente 11 dígitos")

        return value


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"