from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.models.user import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User
