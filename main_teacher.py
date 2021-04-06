from classes.Teacher import *
def menu():
    try:
        list = []
        while True:
            print("==========")
            print("1. Add")
            print("2. Show")
            print("3. Remove By Id")
            print("0. Exit")
            choice = int(input("Choose between 0 and 3= "))
            print("==========")
            if choice.__eq__(1):
                print("1. Add Teacher")
                n = int(input("Enter N= "))
                for i in range(0,n):
                    teacher = Teacher()
                    print("==========")
                    teacher.input()
                    list.append(teacher)
                continue
            if choice.__eq__(2):
                print("2. Show")
                total = 0
                if len(list).__eq__(0):
                    print("List is empty")
                    continue
                print("ID{:<3}Name{:<16}Address{:<12}Jobtitle{:<9}Salary{:<6}Roomnumber".format('','','','',''))
                for item in list:
                    print(item.output())
                continue
            if choice.__eq__(3):
                print("3. Remove By Id")
                if len(list).__eq__(0):
                    print("List is empty")
                    continue
                count = 0
                id = int(input("Enter id to remove= "))
                for item in list[:]:
                    if(item.getID().__eq__(id)):
                        list.remove(item)
                        count = 0
                        print("Remove successfully")
                    else:
                        count =1
                if count.__eq__(1):
                    print("No Teacher match with this id")
                continue
            if choice.__eq__(0):
                raise SystemExit
    except Exception as e:
        print(e)

menu()
