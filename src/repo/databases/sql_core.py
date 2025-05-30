from src.repo.databases.sql_config import SQL_CONFIG, SQL_ENGINE
from src.repo.databases.sql_connector import SQLConnector
from src.repo.base import CommonMethods

class DB_Core(CommonMethods):
    def __init__(self):
        self.connector = SQLConnector(SQL_ENGINE, SQL_CONFIG)

    def _show_tables(self):
        _SQL_ = """show tables;"""
        with self.connector as cursor:
            cursor.execute(_SQL_)
            res = cursor.fetchall()
        return res
    
    def get_unfinished(self):
        _SQL_ = """select * from unfinished"""
        with self.connector as cursor:
            cursor.execute(_SQL_)
            res = cursor.fetchall()
        return res



if __name__ == '__main__':
    test = DB_Core()
    #res = test._show_tables()
    #print(i for i in res)
    print(test.get_unfinished())