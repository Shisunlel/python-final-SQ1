from Classes.class_Stuff import Stuff


class Teacher(Stuff):
    roomnumber=None

    def input(self):
        super().input()
        self.roomnumber = int(input("Enter Room Number= "))

    def output(self):
        return super().output() + '{0:<11}'.format(self.roomnumber)