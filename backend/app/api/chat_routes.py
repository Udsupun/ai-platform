from fastapi import APIRouter, Depends

from app.core.security import get_current_user
from app.dependencies.services import get_rag_service
from app.models.user import User
from app.schemas.chat import ChatRequest
from app.services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
async def chat(
    data: ChatRequest,
    current_user: User = Depends(get_current_user),
    rag_service: RAGService = Depends(get_rag_service),
):

    response = rag_service.ask_question(data.question, int(current_user.id))

    return {"response": response}
