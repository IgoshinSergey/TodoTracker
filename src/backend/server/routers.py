from typing import List

from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from fastapi.responses import JSONResponse

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate

from database.model import User
from database.orm import AsyncCore

from server.cache import (
    get_total_tasks,
    get_completed_tasks,
    set_completed_tasks,
    set_total_tasks,
    increment_completed_tasks,
    increment_total_tasks,
)
from server.schemas import (
    TaskUpdate,
    TaskCreate,
    TaskBase,
    UserBase,
    TaskStatistic,
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
        user_id=user.id,
        completed=False,
    )


@api_router.post("/tasks", response_model=TaskBase, status_code=201)
async def new_task(
    data: TaskCreate,
    user: User = Depends(current_active_user),
):
    await increment_total_tasks(user.email)
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
    if new_data.completed:
        await increment_completed_tasks(user.email)
    return updated_task


@api_router.get("/tasks/statistics", response_model=TaskStatistic)
async def task_statistics(user: User = Depends(current_active_user)):
    all_tasks: list[TaskBase]
    completed_tasks: list[TaskBase]

    cached_total_tasks = await get_total_tasks(user.email)
    cached_completed_tasks = await get_completed_tasks(user.email)

    if cached_total_tasks is None or cached_completed_tasks is None:
        all_tasks = await AsyncCore.select_tasks(user_id=user.id)
        completed_tasks = await AsyncCore.select_tasks(user_id=user.id, completed=True)
        await set_total_tasks(user.email, len(all_tasks))
        await set_completed_tasks(user.email, len(completed_tasks))

        return TaskStatistic(
            total_tasks=len(all_tasks),
            completed_tasks=len(completed_tasks),
        )
    else:
        return TaskStatistic(
            total_tasks=cached_total_tasks,
            completed_tasks=cached_completed_tasks,
        )
