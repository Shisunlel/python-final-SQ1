from Classes.People import *
from Classes.Student import *
from Classes.Stuff import *
from Classes.Teacher import *

def menu():
    try:
        list = []
        choiceRole=None
        while True:
            if(choiceRole==None):
                list= []
                print("==========")
                print("1. People")
                print("2. Student")
                print("3. Stuff")
                print("4. Teacher")
                print("0. Exit")
                choiceRole = int(input("Choose between 0 and 4= "))
            if (choiceRole == 0):
                raise SystemExit

            if(choiceRole!=None):
                print("==========")
                print("1. Add New")
                print("2. Show")
                print("3. Remove By Id")
                print("0. Back")
                choice = int(input("Choose between 0 and 3= "))
                print("==========")
                if choice.__eq__(1):
                    print("1. Add Product")
                    n = int(input("Enter n= "))
                    for temp in range(0,n):
                        if (choiceRole.__eq__(1)):
                            role = People()
                            roleOutput = "ID{:<3}Name{:<10}Address".format('', '')
                        elif (choiceRole.__eq__(2)):
                            role = Student()
                            roleOutput = "ID{:<3}Name{:<10}Address{:<3}Subject{:<3}Year".format('', '', '', '')
                        elif (choiceRole.__eq__(3)):
                            role = Stuff()
                            roleOutput = "ID{:<3}Name{:<10}Address{:<3}JobTitle{:<3}Salary".format('', '', '', '')
                        elif (choiceRole.__eq__(4)):
                            role = Teacher()
                            roleOutput = "ID{:<3}Name{:<10}Address{:<3}JobTitle{:<3}Salary{:<3}RoomNumber".format('', '', '', '', '')
                        role.input()
                        list.append(role)
                if choice.__eq__(2):
                    print("2. Show")
                    print("==========")
                    print(roleOutput)
                    for item in list:
                        print(item.output())
                    continue
                if choice.__eq__(3):
                    print("3. Remove by ID")
                    id = int(input("Enter ID= "))
                    count=0
                    for item in list[:]:
                        if(item.getID().__eq__(id)):
                            list.remove(item)
                            print("Remove successfully")
                            count = 0
                            continue
                        else:
                            count = 1
                    if(count.__eq__(1)):
                        print("No product match with this id")
                        continue

                if choice.__eq__(0):
                    choiceRole=None
                continue

    except Exception as e:
        print(e)

menu()

