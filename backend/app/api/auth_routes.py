from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db

from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse
)

from app.services.auth_service import AuthServcie

from app.core.security import get_current_user
from app.models.user import User

service = AuthServcie()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post(
    "/register",
    response_model=TokenResponse
)
async def register (
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    token = await service.register(db, data)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post(
    "/login",
    tags=["login"]
)
async def login (
    data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    token = await service.login(db, data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }