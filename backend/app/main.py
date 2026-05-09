from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.note_routes import router as note_router
from app.api.auth_routes import router as auth_router
from app.db.database import Base, engine

from app.models.note import Note
from app.models.user import User

# Create the database tables
@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )
    yield

# Create the FastAPI app
app = FastAPI(
    lifespan=lifespan
)

# Include the routers
app.include_router(note_router)
app.include_router(auth_router)

# Define the root endpoint
@app.get("/")
async def root ():
    return {"message": "Fast API is Running"}