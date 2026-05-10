from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_current_user
from app.db.dependencies import get_db
from app.dependencies.services import get_note_service
from app.models.user import User
from app.schemas.note import NoteCreate, NoteResponse
from app.services.note_service import NoteService

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post(
    "", response_model=NoteResponse  # Specify the response model for the created note
)
async def create_note(
    note_data: NoteCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    service: NoteService = Depends(get_note_service),
):

    return await service.create_note(db, note_data, int(current_user.id))


@router.get(
    "", response_model=List[NoteResponse], dependencies=[Depends(get_current_user)]
)
async def get_notes(
    db: AsyncSession = Depends(get_db), service: NoteService = Depends(get_note_service)
):
    return await service.get_notes(db)


@router.get("/search")
async def search_notes(
    query: str,
    current_user: User = Depends(get_current_user),
    service: NoteService = Depends(get_note_service),
):
    results = service.vector_service.search_notes(query, int(current_user.id))
    return [{"score": result.score, "content": result.content} for result in results]
