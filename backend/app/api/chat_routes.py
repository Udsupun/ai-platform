from app.services.rag_service import (
    RAGService
)
from app.schemas.chat import ChatRequest
from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

rag_service = RAGService()


@router.post(
    "/",
    dependencies=[Depends(get_current_user)]
)
async def chat(
    data: ChatRequest
):

    response = (
        rag_service.ask_question(
            data.question
        )
    )

    return {
        "response": response
    }