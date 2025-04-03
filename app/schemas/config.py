from msgspec import Struct


class Settings(Struct):
    debug: bool

    db_name: str
    db_host: str
    db_port: str | int
    db_user: str
    db_password: str

    def get_database_uri(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
