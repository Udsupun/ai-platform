from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    # Response model for a note SQLAlchemy model returns ORM attributes
    # Enable attribute-based parsing, Read from object attributes
    class Config:
        from_attributes = True
