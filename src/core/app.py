from src.repo.json_repo import JsonRepo
from src.models import task
from src.ui.ui_templates import UiTemplates
from src.ui.ui_methods import UiMethods
from src.services.task_service import TaskService
from time import sleep

class App():
    def __init__(self):
        self.json = JsonRepo("test4.json")
        self.ui = UiMethods()
        self.service = TaskService()

        self.actions = {
            "1": self.show_unfinished_tasks,
            "2": self.show_finished_tasks,
            "3": self.create_task,
            "4": self.finish_task,
            "5": self.exit_app,
        }

    def run(self):
        while True:
            self.ui.clear_terminal()
            self.ui.print_header()
            self.ui.show_menu(
            ["Посмотреть список актальных задач",
             "Посмотреть список законченных задач",
             "Добавить новую задачу",
             "Выполнить задачу",
             "Выход"])
            self.ui.print_header()
            choice = self.service.get_input()
            action = self.actions.get(choice)
            if action:
                action()
            else:
                print("Некорректный выбор!")

    def show_unfinished_tasks(self):

        actions = {
            "1": self.find_task,
            "2": self.create_task,
            "3": self.finish_task,
            "4": self.back_main
        }

        self.ui.clear_terminal()
        unfinished = self.json.get_unfinished()
        for i, task in enumerate(unfinished):
            self.ui.display_tasks(task)
            if i != len(unfinished) - 1:
                self.ui.print_fouter()
        self.ui.print_header()
        #self.ui.show_menu
        choice = self.service.get_input()
        action = actions.get(choice)
        if action:
            action
        else:
            print("Некорректный метод!")

        


    def show_finished_tasks(self):
        pass

    def create_task(self):
        task = self.service.create_and_add_task()
        if self.json.save_new_task(task):
            print("Задача успешно добавлена!")
        else:
            print("Проблема при добавлении задачи")
            
    def finish_task(self):
        pass
    
    def exit_app(self):
        pass    
    
    
    def _sleep(self):
        sleep(2)