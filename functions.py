from main import todoList


def AddNewAction(day: int, action):
    todoList[day] = action

def GetAllActions():
    pass

def GetActionsOnDay(day: int):
    for i in range(todoList.keys()):
        print(todoList.get(day))





