from sqlalchemy import select, text
from typing import List

from server.schemas import TaskBase
from database.session import (
    async_session,
    async_engine_create_db,
)
from database.model import (
    User,
    Task,
)


class AsyncCore:
    @staticmethod
    async def create_db(db_name: str) -> None:
        async with async_engine_create_db.begin() as conn:  # Use async with to manage the connection context
            await conn.execute(text("commit"))
            await conn.execute(text(f"CREATE DATABASE {db_name}"))

        # conn = async_engine_create_db.connect()
        # await conn.execute("COMMIT")
        # await conn.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        # await conn.close()

    @staticmethod
    async def insert_task(description: str, user_id: int) -> TaskBase:
        async with async_session() as session:
            task: Task = Task(
                description=description,
                user_id=user_id,
            )
            session.add(task)
            await session.flush()
            result: TaskBase = TaskBase(
                id=task.id,
                description=task.description,
                completed=task.completed
            )
            await session.commit()
            return result

    @staticmethod
    async def select_tasks(**kwargs) -> List[TaskBase]:
        async with async_session() as session:
            query = select(Task)

            for key, value in kwargs.items():
                if hasattr(Task, key):
                    query = query.where(getattr(Task, key) == value)

            result = await session.execute(query)
            result = result.scalars().all()
            tasks = [
                TaskBase(
                    id=task.id,
                    description=task.description,
                    completed=task.completed
                ) for task in result
            ]
            return tasks

    @staticmethod
    async def update_username(user_id: int, new_username: str):
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
