from os import system
import platform
import json
import uuid
from datetime import datetime
import random
import time
import pathlib 


if platform.system() == 'Windows':
    file_path = pathlib.Path("c:/Users/Пекус-Милана/Documents/GitHub/python_1/projects/cli/test1.json")

###     MODULES     ###

"""     MAIN    """

def main():
    while(1):
        clear_terminal()
        print_header()
        print(
            "Выберите желаемое действие:\n"
            "1. Посмотреть список актуальных задач;\n"
            "2. Посмотреть историю законченных задач;\n"
            "3. Добавить новую задачу;\n"
            "4. Выход из программы;\n")
        print_header()
        user_choise = get_user_choise()
        
        if user_choise == '1':
            active_task()
            
        elif user_choise == '2':
            finished_task()

        elif user_choise == '3':
            clear_terminal()
            if add_new_task() == False:
                print("Задача не была добавленна!")
            else:
                print("Задача добавленна!")
            print_header()
            sleep()

        elif user_choise == '4':
            print("Программа завершена!")
            exit()
        else:
            print("Некорректное действие")


"""     ACTIVE TASK     """

def active_task():
    """Модуль работы с активными задачами"""
    while(1):
        clear_terminal()
        print_header()
        
        data = open_read()
        unfinished = data["Задачи"]["Выполняются"]
        
        print("Список актуальных задач:")
        for task in unfinished:
            print_task(task, True)
        print_header()

        print(
            "1. Изменить статус задачи;\n"
            "2. Для изменения текущей задачи;\n"
            "3. Добавить новую задачу;\n"
            "4. Чтобы вернуться в главное меню;\n")
        user_input = get_user_choise()

        if user_input == '1':
            if not change_status():
                print("Стутус не был изменен")
            else:
                print("Статус был успешно изменен")
            sleep()

        elif user_input == '2':
        ###     FIXME    ###
            clear_terminal()
            task_to_change = use_for_change()
            if not task_to_change:
                print("Задачи не были изменены!")
            else:
                clear_terminal()
                print_header()
                print("Задача")
                print_task(task_to_change)
                print_header()

                
            sleep()

        elif user_input == '3':
            if add_new_task() == False:
                print("Задача не была добавленна!")
            else:
                print("Задача добавленна!")
            print_header()
            sleep()

        elif user_input == '4':
            break
        
        else:
            print("Некорректное действие!")


'''     CHANGE_STATUS       '''
def change_status():
    data = open_read()
    finded = 0
    while(finded == 0):
        get_task = str(input("Введите GPID задачи для изменения: "))
        if not get_task:
            return False
        unfinished = data["Задачи"]["Выполняются"]
        ended_task = None
        for index, task in enumerate(unfinished):
            if task["GPID"] == get_task:
                ended_task = unfinished.pop(index)
                finded = 1
        if finded == 0:
            print(f"Задача с GPID {get_task} не найденна!")
        
    finished = data["Задачи"]["Завершены"]
    finished.append(ended_task)

    with open ("test1.json", "w") as text:
        json.dump(data, text, ensure_ascii=False, indent=4)

    return True


'''     USE_FOR_CHANGE     '''
def use_for_change()-> dict:
    while(1):
        clear_terminal()
        print_header()
        data = open_read()
        unfinished = data["Задачи"]["Выполняются"]
        for task in unfinished:
            print_task(task)
        print_header()
        
        get_task = str(input("Введите GPID задачи для изменения: "))
        
        if not get_task:
            return False
        
        for task in unfinished:
            if task["GPID"] == get_task:
                return task
        
        print(f"Задача с GPID {get_task} не найденна!")
        sleep()


"""     FINISHED TASK       """

def finished_task():
    """Модуль по управлению законченными задачами"""
    while(1):
        clear_terminal()
        data = open_read()
        finished = data["Задачи"]["Завершены"]

        print("Список заноченных задач:")
        for task in finished:
            print_task(task, True)
        print_header()

        print(
            "1. Чтобы вернуться в главное меню;\n")
        user_choise = get_user_choise()

        if user_choise == '1':
            break
        else:
            break

"""     ADD TASK        """

def add_new_task():
    """Модуль добавления задач"""
    clear_terminal()
    #GPID = input("GPID задачи: ")
    task_name = input("Довавьте тему новой задачи: ")
    if not task_name:
        return False

    task_desc = input("Добавьте содержимое новой задачи: ")
    if not task_desc:
        task_desc = None

    new_task = {
        "GPID": get_timeID(),
        "Тема": task_name,
        "Подробное описание задачи": task_desc
    }

    with open ("test1.json", "r") as text:
        data = json.load(text)
    unfinished = data["Задачи"]["Выполняются"]
    unfinished.append(new_task)


    with open ("test1.json", "w") as text:
        json.dump(data, text, ensure_ascii=False, indent=4)
    
'''
def change_task(unfinished: 'pt'):
    "Модуль изменения задачи"
    "Отображается ИД и тема задачи"
    print_header()
    for task in unfinished:
        print_task(task)

    "Поиск по ИД или теме"
    print_header()
    selected_task = str(input("Введите тему задачи для изменения: "))

    "Задача выбрана"
    task_to_edit = None
    for task in unfinished:
        if str(task["GPID"]) == selected_task:
            task_to_edit = task
    
    if task_to_edit == None:
        print(f"Задача {selected_task} не найденна!")
    
    
    clear_terminal()
    print_task(task_to_edit, True)
    
    "Действия по задаче"
    print_header()
    print("Доступные действия:", 
            "1. Вернуться к панели управления задачами", 
            "2. Изменить статус задачи на \"Завершена\"", 
            "3. Изменить название и содержание задачи",
            "4. Добавить пометку к задаче",
            sep='\n')
    print_header()
    task_action = get_user_choise()

    "Управление задачей"
    if task_action == '1':
        return
    elif task_action == '2':
        pass
    elif task_action == '3':
        pass
    elif task_action == '4':
        pass
'''


###     FUNCTIONS       ###

"""
def get_GPID()-> int:
    "Возвращает актуальный GPID для задачи"
    "Необходимо где-то хранить актуальный"
    with open("test1.json", "r") as text:
        data = json.load(text)
    return ++data["Актульный GPID задач"]
"""

"""
def get_uuid():
    "Нечитаем изначально"
    return str(uuid.uuid4)
"""

def get_timeID()-> str:
    "Возвращает дату(ЧМГ)-рандомное число"
    "Стоит задуматься над заченой случайного числа на порядковое в течение дня"
    day = datetime.now()
    num = random.randint(1, 100)
    return f"{day:%d%m%Y}-{num}"

def clear_terminal():
    """Очистка терминала"""
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

def get_user_choise()-> any:
    """Печатает строку и возвращает число"""
    user_choise = input("Введите желаемое действие: ")
    return user_choise

def print_header():
    """Печатает 10 *"""
    print("*" * 10)
    print("\n")

def print_task(task:dict, mode:bool = False)-> None:
    """Печатает список задач по шаблону: GPID, Тема;\n
    mode(true) добавляет описание задачи """
    print(f"GPID: {task.get("GPID")}\n"
          f"Тема: {task.get("Тема")}\n")
    if mode:
        print(f"Подробное описание задачи: {task.get("Подробное описание задачи")}\n")

def open_read():
    file_path = get_filepath()
    with open (file_path, "r") as js:
        data = json.load(js)
    return data

def sleep(second:int = 2):
    time.sleep(second)

def get_filepath():
    if platform.system() == 'Windows':
        file_path = pathlib.Path("c:/Users/User/Documents/GitHub/python_1/projects/cli/test1.json")
    else:
        file_path = pathlib.Path("/home/semrom/Documents/GitHub/python_1/projects/cli/test1.json")

    return file_path

###     MAIN    ###
if __name__ == "__main__":
    main()