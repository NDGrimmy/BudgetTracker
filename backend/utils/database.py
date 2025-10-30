import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import DATABASE_URL


# Use DATABASE_URL from env or default to a local sqlite file for quick starts
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


def init_db():
    """Create tables. In production you'd run migrations instead."""
    Base.metadata.create_all(bind=engine)
