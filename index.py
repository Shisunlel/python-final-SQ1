from classes.People import *
from classes.Student import *
from classes.Staff import *
from classes.Teacher import *

def menu():
    try:
        while True:
            print("==========")
            print("1.People")
            print("2.Student")
            print("3.Staff")
            print("4.Teacher")
            print("0.Quit")
            print("==========")
            mainSelection = int(input("Choose between 0 and 4= "))
            if mainSelection.__eq__(1):
                output = 'ID{:<3}Name{:<16}Address'.format('','')
                submenu(People, people, output)
            if mainSelection.__eq__(2):
                output = 'ID{:<3}Name{:<16}Address{:<8}Subject{:<13}Year'.format('','','','')
                submenu(Student, student, output)
            if mainSelection.__eq__(3):
                output = 'ID{:<3}Name{:<16}Address{:<8}JobTitle{:<12}Salary'.format('','','','','','')
                submenu(Staff, staff, output)
            if mainSelection.__eq__(4):
                output = 'ID{:<3}Name{:<16}Address{:<8}JobTitle{:<12}Salary{:<6}RoomNumber'.format('','','','','','','')
                submenu(Teacher, teacher, output)
            if mainSelection.__eq__(0):
                raise SystemExit
    except Exception as e:
        print(e)

def submenu(CLASS, list, output):
    while True:
        print("==========")
        print("1. Add")
        print("2. Show")
        print("3. Remove By Id")
        print("0. Exit")
        print("==========")
        choice = int(input("Choose between 0 and 3= "))
        if choice.__eq__(1):
            print("1. Add")
            n = int(input("Enter n= "))
            for i in range(0,n):
                obj = CLASS()
                obj.input()
                print("==========")
                list.append(obj)
            continue
        if choice.__eq__(2):
            print("2. Show")
            if len(list).__eq__(0):
                print("List is empty")
                continue
            print(output)
            for item in list:
                print(item.output())
            continue
        if choice.__eq__(3):
            print("3. Remove By Id")
            if len(list).__eq__(0):
                print("List is empty")
                continue
            id = int(input("Enter id to remove= "))
            count = 0
            for item in list[:]:
                if(item.getID().__eq__(id)):
                    list.remove(item)
                    count = 0;
                else:
                    count = count+1;
            if(len(list) == 1 and count == 1):
                print("Remove successfully");
            elif(count.__eq__(len(list)) and count > 0):
                print("No item match with this id")
            else:
                print("Remove successfully")
            continue
        if choice.__eq__(0):
            break


people = []
student = []
staff = []
teacher = []
menu()

