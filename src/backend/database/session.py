from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine
)

from database.model import User
from config import settings


async_engine: AsyncEngine = create_async_engine(
    url=settings.get_asyncpg_dsn_todo,
    echo=False,
)

async_session = async_sessionmaker(async_engine)


async_engine_create_db: AsyncEngine = create_async_engine(
    url=settings.get_asyncpg_dsn,
    echo=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
