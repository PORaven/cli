from sqlalchemy import Table, Column, Integer, Text, MetaData

metadata_obj = MetaData()

workers_table = Table(
    #Императивное описание таблицы
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key = True),
    Column("username", Text),
)

