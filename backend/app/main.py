from fastapi import FastAPI

from app.db.database import engine
from app.models.notes import Note

app = FastAPI()

Note.metadata.create_all(bind=engine)

@app.get("/")
async def root ():
    return {"message": "Hello World"}