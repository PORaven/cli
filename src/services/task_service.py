from src.models.task import Task
from src.repo.json_repo import JsonRepo
from src.utils.task_utils import generate_GPID, generate_time
from typing import Dict
class TaskService():

    def __init__(self):
        self.repo = JsonRepo()
    def get_input(self, input_description:str = "Выберите нужный вариант: ") -> str:
        return str(input(input_description))
    
    
    def create_and_add_task(self) -> Task | None:
        """Запрашивает данные для задачи, генерирует отсальные, проверяет на соответсвие
        Возвращает: Task - при полном успехе, либо None"""
        while True:
            header = self.get_input("Добавьте заголовок задачи: ").strip()
            if header:
                break
            else:
                print("Заголовок задачи не может быть пустым")
            
        description = self.get_input("Добавьте подробное описание задачи: ")
        if not description:
            description = None
        while True:
            extra_status = self.get_input("Задача срочная?(1-д)(0-y): ")
            match extra_status:
                case '0':
                    extra_status = False
                    break
                case '1':
                    extra_status = True
                    break
                case _:
                    print("Некорректный метод!!!")
        
        pre =  {"header": header,
                 "description": description,
                 "extra_status": extra_status 
                }
        task = self._create_task_struct(pre)
        if self._is_valid_task(task):
            return task
        else:
            return None
        
    def _create_task_struct(self, task: Dict[str, str])->Dict[str, any]:
        return {
            "gpid":  generate_GPID(),
            "header": task.get("header"),
            "description": task.get("description"),
            "remarks": None,
            "extra_status": task.get("extra_status"),
            "time_created": generate_time()
            #"updated_at":  generate_time()
        }
    
    def _is_valid_task(self, task:Task) -> bool:
        """Проверяет соответствует ли задача необходимым атрибутам
        Принимает: Task
        Возвращает: True - соответсвует, False - в обратном случае"""

        need_attribute = ["gpid", "header", "description", "remarks", "extra_status", "time_created"]
        return all(key in task for key in need_attribute)

