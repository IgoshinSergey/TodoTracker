from src.database.session import async_session
from sqlalchemy.exc import IntegrityError
from src.database.model import (
    User,
    Task,
)
from sqlalchemy import select, update, delete


class AsyncCore:
    @staticmethod
    async def insert_user():
        async with async_session() as session:
            user = User(
                username='Takeoff',
                email='Takeoff@gmail.com',
                hashed_password='<PASSWORD>',
            )
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                await session.rollback()

    @staticmethod
    async def insert_task():
        async with async_session() as session:
            task = Task(

            )
            session.add(task)
            session.commit()

    @staticmethod
    async def select_tasks():
        async with async_session() as session:
            query = select(Task)
            result = await session.execute(query)
            tasks = result.scalars().all()
            print(tasks)

    @staticmethod
    async def select_users():
        async with async_session() as session:
            query = select(User)
            result = await session.execute(query)
            tasks = result.scalars().all()
            for task in tasks:
                print(task)
            print(tasks)

    @staticmethod
    async def update_user(user_id: int = 1, new_username: str = 'Travis'):
        async with async_session() as session:
            user = await session.get(User, user_id)
            user.username = new_username
            await session.commit()
