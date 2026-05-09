from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User

class AuthRepository:

    async def get_user_by_email(
            self,
            db: AsyncSession,
            email: str
    ):
        result = await db.execute(
            select(User).where(
                User.email == email
            )
        )

        return result.scalars().first()

    async def create_user(
            self,
            db: AsyncSession,
            user: User
    ):
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user