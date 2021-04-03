from classes.Staff import *


class Teacher(Staff):
    roomnumber = None

    def input(self):
        super().input()
        self.roomnumber = int(input("Enter Roomnumber= "))

    def output(self):
        return super().output()+'{0:<5}'.format(str(self.roomnumber))






