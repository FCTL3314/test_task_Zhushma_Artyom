from litestar.plugins.sqlalchemy import UUIDBase
from sqlalchemy import Column, String, TIMESTAMP, func


class User(UUIDBase):
    __tablename__ = "user"

    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now(), server_default=func.now())
