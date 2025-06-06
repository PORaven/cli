from src.ui.ui_methods import UiMethods
from src.repo.json_repo import JsonRepo
from src.utils.task_utils import generate_GPID, generate_time
from src.models.task import Task

class UiTemplates(UiMethods):
    def __init__(self):
        self.repo = JsonRepo()

    def template_main_menu(self):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        UiMethods.show_menu(
            ["Посмотреть список актальных задач",
             "Посмотреть список законченных задач",
             "Добавить новую задачу",
             "Выполнить задачу",
             "Выход"])
        UiMethods.print_fouter()
        '''
        user_input = UiMethods.get_menu_input("Ваш выбор: ")
        return user_input
        '''
    def template_main_finished_tasks(self, unfinished_list):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        for task in unfinished_list:
            UiMethods.display_tasks(task)
        UiMethods.print_header()
        UiMethods.show_menu(["Показать задачу подробнее",
                             "Изменить статус задачи на \"выполнена\"",
                             "Изменить содержимое задачи",
                             "Добавить новую задачу",
                             "Вернуться в главное меню"])
        '''
        user_input = UiMethods.get_menu_input("Ваш выбор: ")
        return user_input
        '''

    def template_main_unfinished_tasks(self):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        for task in self.repo.get_unfinished():
            UiMethods.display_tasks(task)
        UiMethods.print_header()
        '''
        user_input = UiMethods.get_menu_input("Ваш выбор: ")
        return user_input
        '''

    def template_change_status(self):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        pass

    def template_change_task(self):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        pass

    def template_add_task(self):
        UiMethods.clear_terminal()
        UiMethods.print_header()
        while True:
            header = UiMethods.get_input("Добавьте заголовок задачи: ").strip()
            if header:
                break
            else:
                print("Заголовок задачи не может быть пустым")
            
        description = UiMethods.get_input("Добавьте подробное описание задачи: ")
        if not description:
            description = None
        while True:
            extra_status = UiMethods.get_input("Задача срочная?(1-д)(0-y): ")
            match extra_status:
                case '0':
                    extra_status = False
                    break
                case '1':
                    extra_status = True
                    break
                case _:
                    print("Некорректный метод!!!")
        
        task =  {"header": header,
                 "description": description,
                 "extra_status": extra_status 
                }
        return task


if __name__ == '__main__':
    test = UiTemplates()
    #test.template_main_finished_tasks()
    #test.template_main_unfinished_tasks()
    #test.template_add_task()
        
    tt = test.template_add_task()

    from src.utils.task_utils import generate_GPID, generate_time
    def create_task(task):
        res_task = {
            'GPID' :  generate_GPID(),
            'header' : task.get("header"),
            'description' : task.get("description"),
            'remarks' : None,
            'extra_status' : task.get("extra_status"),
            'time_created' : generate_time()
        }
        return res_task
    
    print(test.repo.save_new_task(create_task(tt)))
    