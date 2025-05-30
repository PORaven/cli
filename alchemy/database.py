from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)
''''
with engine.connect() as cursor:
    #with engine.beggin() as conn - аналогичен, но оставляет неявный комит
    res = cursor.execute(text("SELECT VERSION()")) #запросы не работают без text
    #print(f"res={res.all()}") #через . указываеьт количесвто строк для перевода
    print(f"res={res.first()}") #через . указываеьт количесвто строк для перевода
'''
with engine.connect() as cursor:
    res = cursor.execute(text("SELECT * FROM unfinished"))
    print(f"res={res.all()}")
