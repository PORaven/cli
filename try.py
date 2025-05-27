from pathlib import Path
import json

File_Path = Path("data/test.json")



def open_read():
    with open (File_Path, "r") as js:
        data = json.load(js)
    return data

data = open_read()
finished = data["Задачи"]["Завершены"]
for task in finished:
    print(type(task))