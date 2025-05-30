import pymysql as mysql
from typing import Dict, Optional, Tuple, List

class SQLConnector():
    def __init__(self, ENGINE:str, CONFIG: Dict):
        self.sql_engine = ENGINE
        self.sql_config = CONFIG

    def __enter__(self):
        if self.sql_engine == "MySQL":
            self.sql_connect = mysql.connect(**self.sql_config)
            print("Подключение создано!🗹")
            self.sql_cursor = self.sql_connect.cursor()
            print("Курсор инициализирован!🗹")
            return self
        else:
            raise ValueError(f"Ritht now this sql-connector only for MySQL: {self.sql_engine}")

    def __exit__(self, exc_type, exc_value, exc_trace):
        if self.sql_engine == 'MySQL':
            if exc_type is None:
                self.sql_connect.commit()
            else:
                self.sql_connect.rollback()

            if self.sql_cursor:
                self.sql_cursor.close()
            self.sql_connect.close()

            self.sql_cursor = None
            self.sql_connect = None
        else:
            raise ValueError(f"Ritht now this sql-connector only for MySQL: {self.sql_engine}")
        
    def execute(self, query: str, param: Optional[Tuple] = None):
        """Выполнение запроса"""
        if not self.sql_cursor:
            raise "Ошибка в подключении к БД!"
        return self.sql_cursor.execute(query, param)
    
    def fetchall(self) -> List[Tuple]:
        """Возвращает все строки результата"""
        if not self.sql_cursor:
            raise RuntimeError("Курсор не инициализирован")
        return self.sql_cursor.fetchall()

    def fetchone(self) -> Optional[Tuple]:
        """Возвращает одну строку результата"""
        if not self.sql_cursor:
            raise RuntimeError("Курсор не инициализирован")
        return self.sql_cursor.fetchone()


if __name__ == "__main__":
    from src.repo.databases.sql_config import SQL_CONFIG, SQL_ENGINE
    test = SQLConnector(SQL_ENGINE, SQL_CONFIG)
    #print(dir(test))
    with test as cursor:
        cursor.execute("""Show tables;""")
        res = (cursor.fetchall())
    print(res)


