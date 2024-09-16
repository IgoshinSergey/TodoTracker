from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from server.cache import (
    close_redis,
    clear_redis,
)
from server.routers import (
    api_router,
    auth_router,
    register_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await clear_redis()
    yield
    await close_redis()


app = FastAPI(lifespan=lifespan)

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

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)
