from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from typing import List

from database.session import async_session
from database.model import (
    User,
    Task,
)


class AsyncCore:
    @staticmethod
    async def insert_task(
            description: str,
            user_id: int,
    ):
        async with async_session() as session:
            task = Task(
                description=description,
                user_id=user_id,
            )
            try:
                session.add(task)
                await session.commit()
            except IntegrityError:
                await session.rollback()

    @staticmethod
    async def select_tasks(**kwargs) -> List["Task"]:
        async with async_session() as session:
            query = select(Task)

            for key, value in kwargs.items():
                if hasattr(Task, key):
                    query = query.where(getattr(Task, key) == value)

            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update_user_username(user_id: int, new_username: str):
        async with async_session() as session:
            user = await session.get(User, user_id)
            user.username = new_username
            await session.commit()

    @staticmethod
    async def update_task_description(task_id: int, new_description: str):
        async with async_session() as session:
            task = await session.get(Task, task_id)
            task.username = new_description
            await session.commit()

    @staticmethod
    async def update_task_status(task_id: int, completed: bool):
        async with async_session() as session:
            task = await session.get(Task, task_id)
            task.completed = completed
            await session.commit()
