from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from server.routers import (
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
app.mount("/auth", StaticFiles(directory="./web_gui/auth"), name="auth")
app.mount("/tracker", StaticFiles(directory="./web_gui/tracker"), name="tracker")


@app.get('/')
async def auth():
    return FileResponse("./web_gui/auth/index.html")


@app.get('/welcome')
async def auth():
    return FileResponse("./web_gui/tracker/index.html")
