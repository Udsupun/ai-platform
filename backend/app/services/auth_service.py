from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password
)

from app.models.user import User

from app.repositories.auth_repository import AuthRepository

from app.schemas.auth import (
    LoginRequest,
    RegisterRequest
)

class AuthServcie:

    def __init__(self):
        self.repository = AuthRepository()

    async def register(
        self,
        db: AsyncSession,
        data: RegisterRequest
    ):
        existing_user = (
            await self.repository.get_user_by_email(db, data.email)
        )
        if existing_user:
            raise Exception (
                "User already exists"
            )

        user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password)
        )

        await self.repository.create_user(
            db,
            user
        )

        return create_access_token({
            "sub": str(user.id)
        })

    async def login(
        self,
        db: AsyncSession,
        data: LoginRequest
    ):
        user = await self.repository.get_user_by_email(db, data.email)
        if not user:
            raise Exception (
                "Invalid email or password"
            )

        if not verify_password(data.password, user.password):
            raise Exception (
                "Invalid email or password"
            )

        return create_access_token({
            "sub": str(user.id)
        })