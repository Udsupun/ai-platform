import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.chat_routes import router as chat_router
from app.api.note_routes import router as note_router
from app.core.exception_handlers import (
    app_exception_handler,
    global_exception_handler,
    validation_exception_handler,
)
from app.core.exceptions import AppException
from app.core.logging import configure_logging
from app.db.database import Base, engine
from app.services.vector_service import VectorService


# Create the database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    vector_service = VectorService()
    vector_service.create_collection()

    yield


# Configure logging
configure_logging()

# Create the FastAPI app
app = FastAPI(lifespan=lifespan)

# Configure exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

allowed_origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173",
).split(",")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
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
