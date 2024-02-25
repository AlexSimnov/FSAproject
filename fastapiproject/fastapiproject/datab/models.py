from sqlalchemy import create_engine

from config import settings

from sqlalchemy.orm import sessionmaker

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)

session_factory = sessionmaker(bind=engine)
