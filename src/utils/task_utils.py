import json
from datetime import datetime
from typing import Dict, List
from src.config.path_config import FILE_PATH

def _get_existing_gpids(filename: str = "tasks.json") -> Dict[str, List[int]]:
    """Возвращает словарь с существующими GPID из файла, сгруппированными по датам"""
    try:
        with open(FILE_PATH / filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        gpids = {}
        tasks_block = data.get("Задачи", {})

        for status in ["Завершены", "Выполняются"]:
            for task in tasks_block.get(status, []):
                if not isinstance(task, dict):
                    continue
                gpid = task.get("gpid")
                if isinstance(gpid, str) and '-' in gpid:
                    parts = gpid.split('-')
                    date_part, num_part = parts
                    if date_part.isdigit() and len(date_part) == 8 and num_part.isdigit():
                        gpids.setdefault(date_part, []).append(int(num_part))

        return gpids
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return {}

def generate_GPID(filename: str = "tasks.json") -> str:
    """Генерирует новый GPID, учитывая существующие в файле"""
    existing = _get_existing_gpids(filename)
    today = datetime.now().strftime('%d%m%Y')
    
    # Находим максимальный номер для текущей даты
    max_num = max(existing.get(today, []), default=0)
    
    # Новый номер на 1 больше максимального
    new_num = max_num + 1
    
    return f"{today}-{new_num}"
                
def generate_time() -> datetime:
    now =  datetime.now()
    return f"{now:%H:%M:%S}"