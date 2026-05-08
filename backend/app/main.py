from fastapi import FastAPI

from app.db.database import engine
from app.models.note import Note
from app.models.user import User
from app.api.note_routes import router as note_router

app = FastAPI()

Note.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)

app.include_router(note_router)

@app.get("/")
async def root ():
    return {"message": "Hello World"}