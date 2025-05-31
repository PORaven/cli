from models import metadata_obj, WorkersORM
from database import session_factory, async_session_factory, engine, async_engine



def create_table():
    metadata_obj.drop_all(engine)   #Achtung
    metadata_obj.create_all(engine)

def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersORM(username="Bobr")
        worker_wolk = WorkersORM(username="Wolk")
        session.add_all([worker_bobr, worker_wolk])
        session.commit()