from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from database.model import User
from config import settings


async_engine = create_async_engine(
    url=settings.get_asyncpg_dsn,
    echo=False,
)

async_session = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
