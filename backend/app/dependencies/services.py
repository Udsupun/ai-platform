# app/dependencies/services.py

from fastapi import Depends

from app.repositories.auth_repository import AuthRepository
from app.repositories.note_repository import NoteRepository
from app.services.auth_service import AuthService
from app.services.llm_service import LLMService
from app.services.note_service import NoteService
from app.services.rag_service import RAGService
from app.services.vector_service import VectorService


def get_vector_service():
    return VectorService()


def get_llm_service():
    return LLMService()


def get_note_repository():
    return NoteRepository()


def get_auth_repository():
    return AuthRepository()


def get_note_service(
    repository: NoteRepository = Depends(get_note_repository),
    vector_service: VectorService = Depends(get_vector_service),
):
    return NoteService(note_repository=repository, vector_service=vector_service)


def get_auth_service(
    repository: AuthRepository = Depends(get_auth_repository),
):
    return AuthService(
        auth_repository=repository,
    )


def get_rag_service(
    llm_service: LLMService = Depends(get_llm_service),
    vector_service: VectorService = Depends(get_vector_service),
):
    return RAGService(llm_service=llm_service, vector_service=vector_service)
