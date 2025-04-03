from typing import AsyncGenerator

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository


async def provide_users_service(db_session: AsyncSession) -> AsyncGenerator[UserService, None]:
    async with UserService.new(session=db_session) as service:
        yield service
