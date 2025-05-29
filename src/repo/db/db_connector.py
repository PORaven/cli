import mysql.connector as conn
from typing import Dict

class DBConnector():
    def __init__(self, ENGINE:str, CONFIG: Dict):
        self.sql_engine = ENGINE
        self.sql_config = CONFIG

    def __enter__(self):
        if self.sql_engine == "MySQL":
            self.sql_connect = conn.connect(**self.sql_config)
            self.sql_cursor = self.sql_connect.cursor()
            return self.sql_cursor
        else:
            raise ValueError(f"Ritht now this sql-connector only for MySQL: {self.sql_engine}")

    def __exit__(self, exc_type, exc_value, exc_trace):
        if self.sql_engine == "MySQL":
            self.sql_connect.commit()
            self.sql_cursor.close()
            self.sql_connect.close()

    def __repr__(self):
        return f"{self.sql_engine}"

if __name__ == "__main__":
    from src.repo.db.db_config import SQL_CONFIG, SQL_ENGINE
    test = DBConnector(SQL_ENGINE, SQL_CONFIG)
    print(test)