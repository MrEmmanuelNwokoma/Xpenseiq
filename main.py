from fastapi import FastAPI
from src.api.v1.routes.auth import auth_router


from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):        
    yield



app = FastAPI(
    title="Xpenseiq",
    description="Backend API for Xpenseiq - An expense tracker and budgeting system",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
    lifespan=lifespan
)

app.include_router(auth_router)

