import pytest

from app.services.note_service import NoteService


class FakeNote:
    id = 1
    title = "Payment"
    content = "Payment failed"


class FakeNoteCreate:
    title = "Payment"
    content = "Payment failed"


class FakeNoteRepository:
    async def create_note(self, db, note_data, user_id):
        return FakeNote()


class FakeVectorService:
    def __init__(self):
        self.called = False
        self.note_id = None
        self.user_id = None
        self.content = None

    def store_note_embeddings(self, note_id, content, user_id):
        self.called = True
        self.note_id = note_id
        self.user_id = user_id
        self.content = content


@pytest.mark.asyncio
async def test_create_note_stores_vector_embeddings():
    vector_service = FakeVectorService()

    service = NoteService(
        note_repository=FakeNoteRepository(),
        vector_service=vector_service,
    )

    note = await service.create_note(
        db=None,
        note_data=FakeNoteCreate(),
        user_id=10,
    )

    assert note.id == 1
    assert vector_service.called is True
    assert vector_service.note_id == 1
    assert vector_service.user_id == 10
    assert vector_service.content == "Payment failed"
