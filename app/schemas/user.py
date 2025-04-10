from datetime import datetime

from msgspec import Struct


class UserCreateSchema(Struct):
    name: str
    surname: str
    password: str


class UserPartialUpdateSchema(Struct):
    name: str | None = None
    surname: str | None = None


class UserResponseSchema(Struct):
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime
