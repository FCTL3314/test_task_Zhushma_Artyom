from msgspec import Struct


class UserCreateSchema(Struct):
    name: str
    surname: str
    password: str


class UserUpdateSchema(Struct):
    name: str
    surname: str


class UserResponseSchema(Struct):
    id: int
    name: str
    surname: str
    created_at: str
    updated_at: str
