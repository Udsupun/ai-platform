import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.chat_routes import router as chat_router
from app.api.note_routes import router as note_router
from app.db.database import Base, engine
from app.services.vector_service import VectorService


# Create the database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    vector_service = VectorService()
    vector_service.create_collection()

    yield


# Create the FastAPI app
app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("ALLOWED_ORIGINS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(note_router)
app.include_router(auth_router)
app.include_router(chat_router)


# Define the root endpoint
@app.get("/")
async def root():
    return {"message": "Fast API is Running"}
