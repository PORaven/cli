import os
from src.config.system import SYSTEM
from src.models.task import Task

class UiMethods:

    @staticmethod
    def clear_terminal():
        if SYSTEM == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def print_header():
        print("-" * 20)

    @staticmethod
    def print_fouter():
        print("*" * 20)
    '''
    @staticmethod
    def get_input(input_description:str) -> str:
        return str(input(input_description))
    '''
    @staticmethod
    def show_menu(options: list):
        for i, opthion in enumerate(options, 1):
            print(f"{i}. {opthion}")
    
    @staticmethod
    def display_tasks(task: Task, need_full: bool = False):
        print(f"gpid: {task["gpid"]}")
        print(f"Тема: {task["header"]}")
        if need_full:
            print(f"Описание задачи: {task["description"]}")
            print(f"Время создания: {task["time_created"]}")
            print(f"Срочность: {task["extra_status"]}")