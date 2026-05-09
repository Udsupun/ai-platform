from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.note import Note
from app.schemas.note import NoteCreate

class NoteRepository:
    async def create_note(self, db: AsyncSession, note_data: NoteCreate, user_id: int):
        note = Note(
            title=note_data.title,
            content=note_data.content,
            user_id=user_id
        )

        db.add(note)
        await db.commit()
        await db.refresh(note)
        return note

    async def get_notes(self, db: AsyncSession):
        result = await db.execute(select(Note))
        return result.scalars().all() # Extracts ORM objects from the result