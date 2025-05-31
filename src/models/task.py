from datetime import datetime
from typing import Dict
import json
from src.utils.task_utils import generate_GPID, generate_time

class Task:
    gpid : int
    header: str
    description: str
    #remarks_existing: bool
    #remarks_count: int
    remarks: json
    extra_status: bool
    time_created: datetime
    #updated_at: datetime
