from uuid import UUID

from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreateSchema, UserPartialUpdateSchema, UserResponseSchema
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
    ) -> OffsetPagination[UserResponseSchema]:
        results, total = await users_service.list_and_count(limit_offset)
        return users_service.to_schema(
            data=results,
            total=total,
            filters=[limit_offset],
            schema_type=UserResponseSchema,
        )

    @post()
    async def create_user(
        self,
        users_service: UserService,
        data: UserCreateSchema,
    ) -> UserResponseSchema:
        obj = await users_service.create(data, auto_commit=True)
        return users_service.to_schema(data=obj, schema_type=UserResponseSchema)

    @get(path="/{user_id:uuid}")
    async def get_user(
        self,
        users_service: UserService,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> UserResponseSchema:
        obj = await users_service.get(user_id)
        return users_service.to_schema(data=obj, schema_type=UserResponseSchema)

    @patch(path="/{user_id:uuid}")
    async def update_user(
        self,
        users_service: UserService,
        data: UserPartialUpdateSchema,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> UserResponseSchema:
        obj = await users_service.update(data=data, item_id=user_id, auto_commit=True)
        return users_service.to_schema(obj, schema_type=UserResponseSchema)

    @delete(path="/{user_id:uuid}")
    async def delete_user(
        self,
        users_service: UserService,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        _ = await users_service.delete(user_id, auto_commit=True)
