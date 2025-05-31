from sqlalchemy import text, insert
from database import engine, async_engine
from models import metadata_obj, workers_table

with engine.connect() as cursor:
    #with engine.begin() as conn - аналогичен, но оставляет неявный комит
    res = cursor.execute(text("SELECT VERSION()")) #запросы не работают без text
    #print(f"res={res.all()}") #через . указываеьт количесвто строк для перевода
    print(f"res={res.first()}") #через . указываеьт количесвто строк для перевода

with engine.connect() as cursor:
    res = cursor.execute(text("SELECT * FROM unfinished"))
    print(f"res={res.all()}")


async def async_get():
    async with async_engine.connect() as cursor:
        res = await cursor.execute(text("""SHOW TABLES;"""))
        print(f"{res.all()}")


def create_table():
    metadata_obj.drop_all(engine)   #Achtung
    metadata_obj.create_all(engine)

def insert_data():
    with engine.connect() as conn:
        '''stmt = """INSERT INTO workers (username) VALUES
        ('BOBR'),
        ('VOLK');"""
        #Потребует оборота в text при выполении'''
        stmt = insert(workers_table).values(
            [
                {"username": "Kabanchik"},
                {"username": "Baram"},
            ]
        )
        conn.execute(stmt)
        conn.commit()
