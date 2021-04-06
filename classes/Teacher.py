from classes.Staff import *


class Teacher(Staff):
    __roomnumber = None

    def input(self):
        super().input()
        self.__roomnumber = int(input("Enter Roomnumber= "))

    def output(self):
        return super().output()+'\t{0:<20}'.format(str(self.__roomnumber))






