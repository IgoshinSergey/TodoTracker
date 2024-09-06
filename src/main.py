# from config import settings
from database.orm import AsyncCore, User, Task
import asyncio

from typing import List


async def main():
    # await AsyncCore.insert_user()
    # users: List["User"] = await AsyncCore.select_users()
    # for user in users:
    #     print(user.id)
    # tasks: List["Task"] = await AsyncCore.select_tasks()
    # for task in tasks:
    #     print(task.id)

    # await AsyncCore.update_user()
    # await AsyncCore.insert_task("first task", 1)
    # await AsyncCore.insert_task("first task", 2)
    # await AsyncCore.insert_task("first task", 3)
    # await AsyncCore.insert_task("first task", 12)
    await AsyncCore.insert_task("second task", 12)
    await AsyncCore.insert_task("third task", 12)
    # res = await UserValidator.is_unique_email("jacck@gmail.com")
    # res = await UserValidator.is_unique_username("Travis")
    # print(f"{res=}")


if __name__ == '__main__':
    asyncio.run(main())
    # print(f"{UserValidator.is_unique_email("jack@gmail.com")}")
