

def AddNewAction(day: int, action: str):
    todoList[day] = action

def GetAllActions():
    for i in range(todoList.keys()):
        print(todoList.get(i))
        print('\n')

def GetActionsOnDay(day: str):
    print(todoList.get(day))



todoList = dict()
AddNewAction('1', "побегать")
GetActionsOnDay('1')
GetAllActions()
