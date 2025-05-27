import json
from typing import List, Dict
from src.config.path_config import FILE_PATH
from src.repo.base import CommonMethods
from src.models.task import Task

class JsonRepo(CommonMethods):
    def __init__(self, file_name:str = 'tasks.json'):
        self.repo = FILE_PATH / file_name

    def _check_file(self) -> bool:
        return self.repo.exists()
    
    def _get_file_data_pointer(self) -> List | None:
        if not self._check_file():
            return None
        try:
            with open(self.repo, "r") as file:
                json.load(file)
        except json.JSONDecodeError:
            return None
    
    def get_finished(self) -> List[Task] | None:
        data = self._get_file_data_pointer()
        if not data:
            return None
        
        tasks = data.get("Задачи", {})
        if not isinstance(tasks, dict):
            return None
        
        finished = tasks["Завершены"]
        return finished

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
    
            data["Задачи"]["Выполняются"].append(task)

            with open(self.repo, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.flush()
                return True
        except Exception as e:
            return False        

    def change_task_status(self):
        pass


if __name__ == '__main__':
    test = JsonRepo("test.json")
    #print(test._chek_file())
    #print(test.get_file_data_pointer())
    
    #print(test.get_finished())
    #print(test.get_unfinished())
    print(type(test._get_file_data_pointer()))