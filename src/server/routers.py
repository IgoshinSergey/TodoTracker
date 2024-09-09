from typing import List

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from fastapi.responses import JSONResponse

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate

from database.model import User
from database.orm import AsyncCore

from server.schemas import (
    TaskUpdate,
    TaskCreate,
    TaskBase,
    UserBase,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


api_router = APIRouter()
auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)

current_active_user = fastapi_users.current_user(active=True)


@api_router.get("/user", response_model=UserBase)
async def get_user_data(user: User = Depends(current_active_user)):
    return UserBase(
        username=user.username,
        email=user.email,
    )


@api_router.get("/tasks", response_model=List[TaskBase])
async def get_tasks(user: User = Depends(current_active_user)):
    return await AsyncCore.select_tasks(
        user_id=user.id
    )


@api_router.post("/tasks", response_model=TaskBase, status_code=201)
async def new_task(
        data: TaskCreate,
        user: User = Depends(current_active_user),
):
    return await AsyncCore.insert_task(
        user_id=user.id,
        description=data.description,
    )


@api_router.put("/tasks/{task_id}", response_model=TaskBase)
async def update_task(
        task_id: int,
        new_data: TaskUpdate,
        user: User = Depends(current_active_user),
):
    tasks = await AsyncCore.select_tasks(id=task_id, user_id=user.id)
    if len(tasks) == 0:
        return JSONResponse(status_code=404, content={"detail": "Task not found"})

    updated_task = await AsyncCore.update_task(
        task_id=task_id,
        new_description=new_data.description,
        completed=new_data.completed,
    )
    return updated_task
