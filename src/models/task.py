from datetime import datetime
from typing import Dict
from src.utils.task_utils import generate_GPID, generate_time
class Task:
    GPID : int
    header: str
    description: str
    #remarks_existing: bool
    #remarks_count: int
    remarks: str
    extra_status: bool
    time_created: datetime

    @classmethod
    def create_task(cls, task: Dict):
        return cls(
            gpid =  generate_GPID(),
            header = task.get("header"),
            description = task.get("description"),
            remarks = None,
            extra_status = task.get("extra_status"),
            time_created = generate_time()
        )
    
    def is_valid_task(self, task) -> bool:
        """Проверяет соответствует ли задача необходимым атрибутам
        Принимает: Task
        Возвращает: True - соответсвует, False - в обратном случае"""

        need_attribute = ["gpid", "header", "description", "remarks", "extra_status", "time_created"]
        for attr in need_attribute:
            if not hasattr(task, attr):
                return False
        return True
