from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String
from config import settings
import asyncio
from typing import Annotated 
engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)

session_factory = sessionmaker(engine)
async_session_factory = sessionmaker(async_engine)

str_200 = Annotated[str, 200]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_200: String(200)
    }