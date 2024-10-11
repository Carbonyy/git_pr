from main import todoList


def AddNewAction(day: int, action):
    todoList[day] = action

def GetAllActions():
    for i in range(todoList.keys()):
        print(todoList.get(i))
        print('\n')

def GetActionsOnDay(day: int):
    for i in range(todoList.keys()):
        print(todoList.get(day))





