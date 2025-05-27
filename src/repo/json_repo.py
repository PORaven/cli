import json
from typing import Optional, List, Dict
from src.config.path_config import FILE_PATH
from src.repo.base import CommonMethods
from src.models.task import Task

class JsonRepo(CommonMethods):
    def __init__(self, file_name:str = 'test.json'):
        self.repo = FILE_PATH / file_name

    def _check_file(self) -> bool:
        return self.repo.exists()
    
    def _get_file_data_pointer(self) -> List | None:
        if not self._check_file():
            return None
        try:
            with open(self.repo, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return None
        
    
    
    def get_finished(self) -> List | None:
        data = self._get_file_data_pointer()
        if not data:
            return None
        
        tasks = data.get("Задачи", {})
        if not isinstance(tasks, dict):
            return None
        
        finished = tasks.get("Завершены", [])
        return finished if isinstance(finished, list) else None

    def get_unfinished(self) -> List[Task] | None:
        data = self._get_file_data_pointer()
        if not data:
            return None
        
        tasks = data.get("Задачи", {})
        if not isinstance(tasks, dict):
            return None
        
        finished = tasks.get("Выполняются", [])
        return finished if isinstance(finished, list) else None

    
    def save_new_task(self, task: Task) -> bool:
        try:
            data = self._get_file_data_pointer()
            if not data:
                data = {
                    "Задачи": {
                        "Завершены": [],
                        "Выполняются": []
                    }
                }
            
            # Получаем текущий список незавершенных задач
            unfinished_tasks = data["Задачи"].get("Выполняются", [])
            if not isinstance(unfinished_tasks, list):
                unfinished_tasks = []
            
            # Добавляем новую задачу
            unfinished_tasks.append(task)
            
            # Обновляем данные
            data["Задачи"]["Выполняются"] = unfinished_tasks
            
            # Сохраняем в файл
            with open(self.repo, "w", encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            
            return True
        except Exception as e:
            return False      

    def change_task_status(self, task: Task):
        pass

if __name__ == '__main__':
    test = JsonRepo("tasks.json")
    #print(test._chek_file())
    #print(test.get_file_data_pointer())
    
    #print(test.get_finished())
    #print(test.get_unfinished())
    
    test_create = {"header": "тест в ЖРепе",
                   "description": "ща узнаем",
                   "extra_status": True}

    from src.utils.task_utils import generate_GPID, generate_time
    def create_task(task):
        res_task = {
            'gpid' :  generate_GPID(),
            'header' : task.get("header"),
            'description' : task.get("description"),
            'reamarks' : None,
            'extra_status' : task.get("extra_status")
        }
        return res_task
    try_task = create_task(test_create)

    print(test.save_new_task(try_task))
