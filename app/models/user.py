from datetime import datetime

from litestar.plugins.sqlalchemy import UUIDBase
from sqlalchemy import String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column


class User(UUIDBase):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), onupdate=func.now(), server_default=func.now()
    )
