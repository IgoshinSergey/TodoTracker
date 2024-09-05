from datetime import datetime
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    created_at: datetime


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    username: str
