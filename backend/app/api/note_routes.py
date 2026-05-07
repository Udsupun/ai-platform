from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import Session

from app.db.dependencies import get_db
from app.schemas.note import NoteCreate, NoteResponse
from app.services.note_service import NoteSevice

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

service = NoteSevice()


@router.post(
    "",
    response_mode=NoteResponse
)
async def create_note(
    note_data: NoteCreate,
    db: Session = Depends(get_db)
):

    return service.create_note(db, note_data)

@router.get(
    "",
    response_model=[NoteResponse]
)
async def get_notes(
    db: Session = Depends(get_db)
):
    return service.get_notes(db)