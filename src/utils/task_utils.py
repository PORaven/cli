from datetime import datetime
from random import randint

def generate_GPID() -> str:
    day = datetime.now()
    num = randint(1, 100)
    return f"{day:%d%m%Y}-{num}"

def generate_time() -> datetime:
    return datetime.now()
