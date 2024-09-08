from database.orm import AsyncCore


if __name__ == "__main__":
    AsyncCore.create_db("todo_database")
