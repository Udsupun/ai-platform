from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate

class NoteRepository:
    def create_note(self, db: Session, note_data: NoteCreate):
        note = Note(
            title=note_data.title,
            content=note_data.content
        )

        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    def get_notes(self, db: Session):
        return db.query(Note).all()