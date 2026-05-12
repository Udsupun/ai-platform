import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.note_repository import NoteRepository
from app.schemas.note import NoteCreate
from app.services.vector_service import VectorService

logger = logging.getLogger(__name__)


class NoteService:
    def __init__(self, note_repository: NoteRepository, vector_service: VectorService):
        self.repository = note_repository
        self.vector_service = vector_service

    async def create_note(self, db: AsyncSession, note_data: NoteCreate, user_id: int):
        note = await self.repository.create_note(db, note_data, user_id)
        self.vector_service.store_note_embeddings(note.id, note.content, user_id)
        return note

    async def get_notes(self, db: AsyncSession, user_id: int):
        logger.info("Fetching notes for user_id=%s", user_id)

        return await self.repository.get_notes(db=db, user_id=user_id)
