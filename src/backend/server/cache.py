from redis import asyncio as aioredis
from config import settings

redis = aioredis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


async def set_total_tasks(email: str, total_tasks: int):
    await redis.set(f'total_tasks:{email}', total_tasks)


async def set_completed_tasks(email: str, completed_tasks: int):
    await redis.set(f'completed_tasks:{email}', completed_tasks)


async def get_total_tasks(email: str) -> int | None:
    total_tasks = await redis.get(f'total_tasks:{email}')
    return int(total_tasks) if total_tasks is not None else None


async def get_completed_tasks(email: str) -> int | None:
    completed_tasks = await redis.get(f'completed_tasks:{email}')
    return int(completed_tasks) if completed_tasks is not None else None


async def increment_total_tasks(email: str, increment: int = 1):
    await redis.incr(f'total_tasks:{email}', increment)


async def increment_completed_tasks(email: str, increment: int = 1):
    await redis.incr(f'completed_tasks:{email}', increment)


async def close_redis():
    await redis.close()


async def clear_redis():
    await redis.flushdb()
