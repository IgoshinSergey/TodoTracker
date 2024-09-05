from pydantic import (
    BaseModel,
    EmailStr,
    ValidationError,
    Field
)


class Email(BaseModel):
    email: EmailStr | None = Field(default=None)


class Validator:
    @staticmethod
    def is_valid_email(user_email: str) -> bool:
        try:
            Email(email=user_email)
            return True
        except ValidationError:
            return False
