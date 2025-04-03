from litestar.plugins.sqlalchemy import BigIntAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(BigIntAuditBase):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    surname: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
