from pydantic import (
    BaseModel,
    EmailStr,
    ValidationError,
    Field
)
from src.database.orm import AsyncCore, User, Task
from typing import List


class Email(BaseModel):
    email: EmailStr | None = Field(default=None)


class UserValidator:
    @staticmethod
    def is_valid_email(user_email: str) -> bool:
        try:
            Email(email=user_email)
            return True
        except ValidationError:
            return False

    @staticmethod
    async def is_unique_email(email: EmailStr) -> bool:
        duplicate: List["User"] = await AsyncCore.select_users(email=email)
        return len(duplicate) == 0

    @staticmethod
    async def is_unique_username(username: str) -> bool:
        duplicate: List["User"] = await AsyncCore.select_users(username=username)
        return len(duplicate) == 0

