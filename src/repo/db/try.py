from src.repo.db.db_connector import DBConnector
from src.repo.db.db_config import SQL_CONFIG, SQL_ENGINE

with DBConnector(SQL_ENGINE, SQL_CONFIG) as cursor:
    cursor.execute("show tables;")
    for tables in cursor.fetchall():
        print(tables)