from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    description: str
    completed: bool
