import asyncio

from database.orm import AsyncCore


async def main():
    tasks = await AsyncCore.update_task(
        task_id=1,
        new_description="iiiii",
        completed=True
    )
    for task in tasks:
        print(f"{task}")


if __name__ == '__main__':
    asyncio.run(main())
