from src.repo.json_repo import JsonRepo
from src.models import task
from src.ui.ui_templates import UiTemplates
from src.handler.task_handler import TaskHendler

class App():
    def __init__(self):
        self.json = JsonRepo()
        self.ui = UiTemplates()
        self.handler = TaskHendler()

    def run(self):
        while True:
            self.ui.template_main_menu()
            choise = self.handler.get_input()
            match choise:
                case "1":
                    self.ui.template_main_unfinished_tasks()
                case "2":
                    self.ui.template_main_finished_tasks()
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    break
                case "_":
                    print("Ошибка при выборе метода!")

