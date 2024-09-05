# from config import settings
from src.database.orm import AsyncCore
import asyncio

from src.database.validation import Validator


async def main():
    # await AsyncCore.insert_user()
    # await AsyncCore.select_users()
    await AsyncCore.update_user()

if __name__ == '__main__':
    # asyncio.run(main())
    print(f"{Validator.is_valid_email("do.wdw2g@maio")}")