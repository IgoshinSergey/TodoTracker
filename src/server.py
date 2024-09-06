from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from auth.schemas import UserRead, UserCreate
from auth.manager import get_user_manager
from auth.auth import auth_backend

from database.model import User, Task

import uvicorn

from database.orm import AsyncCore


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)

app.mount("/static", StaticFiles(directory="./src/web_gui/auth"), name="static")
current_active_user = fastapi_users.current_user(active=True)


@app.get('/')
async def auth():
    return FileResponse("./src/web_gui/auth/index.html")


@app.get("/api/tasks")
async def get_tasks(user: User = Depends(current_active_user)):
    return await AsyncCore.select_tasks(user_id=user.id)


@app.get("/api/tasks")
async def get_tasks(user: User = Depends(current_active_user)):
    return await AsyncCore.select_tasks(user_id=user.id)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
