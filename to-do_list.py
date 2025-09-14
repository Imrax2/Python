import sys
import os
import json
tasks= []
folder=os.path.dirname(os.path.abspath(__file__))
filepath=os.path.join(folder, "Tasks.json")
if os.path.exists(filepath)==True:
    folder=os.path.dirname(os.path.abspath(__file__))
    filepath=os.path.join(folder, "Tasks.json")
    with open(filepath, "r") as file:
        try: 
            tasks= json.load(file)
        except json.decoder.JSONDecodeError:
            tasks=[]
else:
    tasks=[]
def saving():
    folder=os.path.dirname(os.path.abspath(__file__))
    filepath=os.path.join(folder, "Tasks.json")
    with open(filepath, "w") as file:
        json.dump(tasks, file)
def viewing():
    if tasks==[]:
        print("You don't have any tasks currently please add a new one!")
        menu()
    else:
        for idx,task in enumerate(tasks, start=1):
            status="[X]" if task['done'] else "[]"
            print(f"{idx}.{status} {task['name']}")
        input("\nPress enter to go back to the menu!")
def removing():
    print('Pick a task to remove!')
    for idx,task in enumerate(tasks, start=1):
        status="[X]" if task['done'] else "[]"
        print(f"{idx}.{status} {task['name']}")
    e=int(input('Please type a number of a task you want to remove!'))
    tasks.pop(e-1)
    c=input('You have successfuly removed a task! \nWould you like another one?(yes or exit)\n')
    if c.lower()=='yes':
        removing()
    elif c.lower()=='exit':
        d=input('Would you like to exit or go back to the the menu?\n Type "menu" or "exit".\n')
        if d.lower()=='menu':
            menu()
        elif d.lower()=='exit':
            saving()
            sys.exit()
        
def adding():
        b=input('Add a task to your list!\n\n')
        tasks.append({"name": b,"done" :False})
        c=input('You have successfuly added a task! \nWould you like another one?(yes or exit)\n')
        if c.lower()=='yes':
            adding()
        elif c.lower()=='exit':
            d=input('Would you like to exit or go back to the the menu?\n Type "menu" or "exit".\n')
            if d.lower()=='menu':
               menu()
            elif d.lower()=='exit':
                saving()
                sys.exit()
def marking():
    for idx,task in enumerate(tasks, start=1):
        status="[X]" if task['done'] else "[]"
        print(f"{idx}.{status} {task['name']}")
    f=int(input("Please select a task you want to mark as done!\n"))
    tasks[f-1]["done"]=True
    c=input('You have successfuly marked a task! \nWould you like another one?(yes or exit)\n')
    if c.lower()=='yes':
            marking()
    elif c.lower()=='exit':
            d=input('Would you like to exit or go back to the the menu?\n Type "menu" or "exit".\n')
            if d.lower()=='menu':
               menu()
            elif d.lower()=='exit':
                saving
                sys.exit()
def modify():
        for idx,task in enumerate(tasks, start=1):
            status="[X]" if task['done'] else "[]"
            print(f"{idx}.{status} {task['name']}")
            try:
                h=int(input("Please select which task you would like to modify\n"))
            except ValueError:
                print("Inavlid input. Please retry!\n")
                continue
            if h+1<=len(tasks):
                j=int(input("Please enter what you want to do with the task.\n1. Change name\n2. Change marking"))
            if j==1:
                i=input("Please eneter the new task name!\n")
                tasks[h-1]["name"]=i
            elif j==2:
                if tasks[h-1]["done"]==True:
                    tasks[h-1]["done"]=False
                elif tasks[h-1]["done"]==False:
                    tasks[h-1]["done"]=True
            else :
                print("Wrong input. Please retry!")
        else:
            print("You have entered invalid task please try again!")
def save_exit():
        saving()
        sys.exit()
def task_editor():
        g=int(input("Please select what would you like to do with the tasks.\n1. Add tasks\n2. Remove tasks\n3. Mark as done\n4. Modify task\n5. Clear all tasks\n6. Back\n"))
        if g==1:
            adding()
        elif g==2:
            removing()
        elif g==3:
            marking()
        elif g==4:
            modify()
        elif g==5:
            tasks.clear()
        elif g==6:
            return True
def menu():
    while True:
        print("Welcome to the to-to list menu!\n Please select a feature by writting a number!\n")
        print("1. View tasks\n2. Task editor\n3. Save and exit")
        try:
            a=int(input())
        except ValueError:
            print("Inavlid input. Please retry!\n")
            continue
        if a==1:
            viewing()
        elif a==2:
            task_editor()
        elif a==3:
            save_exit()
        else:
            print('You have entered invalid function. Please retry!')
            continue
menu()