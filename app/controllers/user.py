from uuid import UUID

from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset

from app.models.user import User
from app.schemas.user import UserCreateSchema, UserUpdateSchema
from app.services.user import provide_users_service, UserService


class UserController(Controller):
    path = "/users"
    dependencies = {"users_service": Provide(provide_users_service)}
    tags = ["Users"]

    @get()
    async def list_users(
        self,
        users_service: UserService,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[User]:
        results, total = await users_service.list_and_count(limit_offset)
        return users_service.to_schema(
            data=results,
            total=total,
            filters=[limit_offset],
            schema_type=User,
        )

    @post()
    async def create_user(
        self,
        users_service: UserService,
        data: UserCreateSchema,
    ) -> User:
        obj = await users_service.create(data)
        return users_service.to_schema(data=obj, schema_type=User)

    @get(path="/{user_id_id:uuid}")
    async def get_user(
        self,
        users_service: UserService,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> User:
        obj = await users_service.get(user_id)
        return users_service.to_schema(data=obj, schema_type=User)

    @patch(path="/{user_id:uuid}")
    async def update_user(
        self,
        users_service: UserService,
        data: UserUpdateSchema,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> User:
        obj = await users_service.update(data=data, item_id=user_id)
        return users_service.to_schema(obj, schema_type=User)

    @delete(path="/{user_id:uuid}")
    async def delete_user(
        self,
        users_service: UserService,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        _ = await users_service.delete(user_id)
