from advanced_alchemy.config import AsyncSessionConfig, AlembicAsyncConfig
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from app import settings

session_config = AsyncSessionConfig(expire_on_commit=False)
alembic_config = AlembicAsyncConfig(script_location="./migrations/")
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.get_database_uri(),
    session_config=session_config,
    create_all=True,
    alembic_config=alembic_config,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
