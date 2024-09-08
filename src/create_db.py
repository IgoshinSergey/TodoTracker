from database.orm import AsyncCore
import asyncio


async def main():
    await AsyncCore.create_db("todo")

if __name__ == "__main__":
    asyncio.run(main())
