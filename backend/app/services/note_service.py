from sqlalchemy.orm import Session

from app.repositories.note_repository import NoteRepository
from app.schemas.note import NoteCreate

class NoteSevice:
    def __init__(self):
        self.repository = NoteRepository()

    def create_note(self, db: Session, note_data: NoteCreate):
        return self.repository.create_note(db, note_data)

    def get_notes(self, db:Session):
        return self.repository.get_notes(db)