
class TaskHendler():
    def get_input(self, input_description:str = "Выберите нужный вариант: ") -> str:
        return str(input(input_description))
    