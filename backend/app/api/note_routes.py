from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.schemas.note import NoteCreate, NoteResponse
from app.services.note_service import NoteSevice

from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

service = NoteSevice()


@router.post(
    "",
    response_model=NoteResponse  # Specify the response model for the created note
)
async def create_note(
    note_data: NoteCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return await service.create_note(db, note_data, current_user.id)

@router.get(
    "",
    response_model=List[NoteResponse],
    dependencies=[Depends(get_current_user)]
)
async def get_notes(
    db: AsyncSession = Depends(get_db),
):
    return await service.get_notes(db)

@router.get(
    "/search",
    dependencies=[Depends(get_current_user)]
)
async def search_notes(
    query: str
):
    results = service.vector_service.search_notes(query)
    return [
        {
            "score": result.score,
            "content": result.payload
        }
        for result in results.points
    ]