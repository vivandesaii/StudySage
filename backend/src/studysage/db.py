from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

engine = create_engine(settings.database_url, echo=settings.db_echo_sql)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# Used for dependency injection with fast api, on routes that require database interaction
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
