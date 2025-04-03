import os

from dotenv import load_dotenv

from app.schemas.config import Settings

load_dotenv()

settings = Settings(
    debug=os.getenv("DEBUG").lower() in ("true", "1"),
    db_name=os.getenv("DATABASE_NAME"),
    db_host=os.getenv("DATABASE_HOST"),
    db_port=os.getenv("DATABASE_PORT"),
    db_user=os.getenv("DATABASE_USER"),
    db_password=os.getenv("DATABASE_PASSWORD"),
)