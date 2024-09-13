import asyncio

from database.orm import AsyncCore


async def main():
    return await AsyncCore.select_tasks(user_id=12)


if __name__ == '__main__':
    asyncio.run(main())
