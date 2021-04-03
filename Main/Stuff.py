from Classes.People import People

class Stuff(People):
    jobTitle = None
    Salary = None

    def input(self):
        super().input()
        self.jobTitle = str(input("Enter jobTitle= "))
        self.Salary = int(input("Enter Salary= "))

    def output(self):
        return super().output() + '{0:<11}'.format(self.jobTitle) + '{0:<9}'.format(self.Salary)