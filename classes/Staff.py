from classes.People import *

class Staff(People):
    jobTitle = None
    salary = None

    def input(self):
        super().input()
        self.jobTitle = str(input("Enter jobTitle= "))
        self.salary = int(input("Enter Salary= "))

    def output(self):
        return super().output() + '{0:<20}'.format(self.jobTitle) + '${0:,.2f}'.format(self.salary)