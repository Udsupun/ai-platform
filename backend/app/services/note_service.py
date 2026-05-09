from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.note_repository import NoteRepository
from app.schemas.note import NoteCreate

from app.services.vectory_service import VectorService

class NoteSevice:
    def __init__(self):
        self.repository = NoteRepository()
        self.vector_service = VectorService()

    async def create_note(self, db: AsyncSession, note_data: NoteCreate, user_id: int):
        note = await self.repository.create_note(db, note_data, user_id)
        print(note.id)
        print("Storing embeddings...")
        self.vector_service.store_note_embeddings(note.id, note.content)
        return note

    async def get_notes(self, db: AsyncSession):
        return await self.repository.get_notes(db)