from sqlalchemy import Table, Column, Integer, Text, MetaData, ForeignKey, String, text
from database import Base, str_200
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, Annotated
import enum
import datetime
from sqlalchemy.sql import func

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
#Кастомный тип на основе БД
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

class WorkersORM(Base):
    __tablename__= "workers"

    #id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk]
    username: Mapped[str_200] 

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumesORM(Base):
    __tablename__ = 'resumes'

    #id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk]
    #title: Mapped[str] = mapped_column(String(200)) из Base
    title: Mapped[str_200]
    compensation: Mapped[Optional[int]] 
    #compensation: Mapped[int | None] Новый синтаксис 
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE")) #ссылка на имя таблицы.колонка, каскадное удаление из таблицы workers
    #created_at: Mapped[datetime.datetime] = mapped_column(server_default=Text("""SELECT now();"""))
    created_at: Mapped[created_at]
    #значение из колонки выше генерит субд, значение defaul будет генерить python