from classes.People import *

class Student(People):
    __subject = None
    __year = None

    def input(self):
        super().input()
        self.__subject = input("Enter subject= ")
        self.__year = int(input("Enter year= "))

    def output(self):
        return super().output() + '{0:<20}'.format(self.__subject) + str(self.__year)