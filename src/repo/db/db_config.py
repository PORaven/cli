from dotenv import load_dotenv
import os

load_dotenv()
SQL_ENGINE = os.getenv("SQL_ENGINE")

SQL_CONFIG = {
        "host": os.getenv("SQL_HOST"),
        "port": os.getenv("SQL_PORT"),
        "user": os.getenv("SQL_USER"),
        "password": os.getenv("SQL_PASS"),
        "database": os.getenv("SQL_NAME"),
}

print(SQL_ENGINE)