from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.app.core.config import Config

DATABASE_URL = Config.DATABASE_URL

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DbContextManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with DbContextManager() as db:
        yield db
