from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.note_repository import NoteRepository
from app.schemas.note import NoteCreate

class NoteSevice:
    def __init__(self):
        self.repository = NoteRepository()

    async def create_note(self, db: AsyncSession, note_data: NoteCreate, user_id: int):
        return await self.repository.create_note(db, note_data, user_id)

    async def get_notes(self, db: AsyncSession):
        return await self.repository.get_notes(db)