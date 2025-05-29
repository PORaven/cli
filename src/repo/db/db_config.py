from dotenv import load_dotenv
import os

load_dotenv(override=True)
SQL_ENGINE = os.getenv("SQL_ENGINE")

SQL_CONFIG = {
        "host": os.getenv("SQL_HOST"),
        "port": int(os.getenv("SQL_PORT")),
        "user": os.getenv("SQL_USER"),
        "password": os.getenv("SQL_PASS"),
        "database": os.getenv("SQL_NAME"),
}

print(SQL_CONFIG)