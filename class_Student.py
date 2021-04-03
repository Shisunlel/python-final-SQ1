from Classes.class_People import *

class Student(People):
    subject=None
    year=None
    def input(self):
        super().input()
        self.subject = str(input("Enter subject= "))
        self.year = int(input("Enter year= "))
    def output(self):
        return super().output() + '{0:<10}'.format(self.subject) + str(self.year)