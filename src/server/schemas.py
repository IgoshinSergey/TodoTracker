from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class TaskBase(BaseModel):
    id: int
    description: str
    completed: bool
