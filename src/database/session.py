from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import settings


async_engine = create_async_engine(
    url=settings.get_asyncpg_dsn,
    echo=True,
)

async_session = async_sessionmaker(async_engine)
