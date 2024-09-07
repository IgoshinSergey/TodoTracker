from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .routers import (
    api_router,
    auth_router,
    register_router,
)

app = FastAPI()

app.include_router(
    auth_router,
    prefix="/api/auth/jwt",
    tags=["Authentication"],
)
app.include_router(
    register_router,
    prefix="/api/auth",
    tags=["Registration"],
)
app.include_router(
    api_router,
    prefix="/api",
    tags=["Api routers"],
)
app.mount("/static", StaticFiles(directory="./src/web_gui/auth"), name="static")


@app.get('/')
async def auth():
    return FileResponse("./src/web_gui/auth/index.html")
