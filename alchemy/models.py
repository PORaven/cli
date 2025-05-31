from sqlalchemy import Table, Column, Integer, Text, MetaData
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

metadata_obj = MetaData()
'''
workers_table = Table(
    #Императивное описание таблицы
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key = True),
    Column("username", Text),
)

'''
class WorkersORM(Base):
    __tablename__= "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
