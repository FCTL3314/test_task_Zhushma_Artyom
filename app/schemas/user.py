from datetime import datetime
from uuid import UUID

from msgspec import Struct


class UserCreateSchema(Struct):
    name: str
    surname: str
    password: str


class UserUpdateSchema(Struct):
    name: str
    surname: str


class UserResponseSchema(Struct):
    id: UUID
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime
