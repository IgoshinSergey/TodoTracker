from typing import List

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate

from database.model import User
from database.orm import AsyncCore

from server.schemas import TaskBase

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


api_router = APIRouter()
auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)

current_active_user = fastapi_users.current_user(active=True)


@api_router.get("/tasks", response_model=List[TaskBase])
async def get_tasks(user: User = Depends(current_active_user)):
    return await AsyncCore.select_tasks(user_id=user.id)


