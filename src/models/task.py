from datetime import datetime
from typing import Dict
from src.utils.task_utils import generate_GPID, generate_time
class Task:
    GPID : int
    header: str
    description: str
    reamarks: str
    extra_status: bool
    time_created: datetime

    @classmethod
    def create_task(cls, task: Dict):
        return cls(
            gpid =  generate_GPID(),
            header = task.get("header"),
            description = task.get("description"),
            reamarks = None,
            extra_status = task.get("extra_status"),
            time_created = generate_time()
        )
