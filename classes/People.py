class People:
    id = None
    name = None
    address = None

    def input(self):
        print("==========")
        self.id = int(input("Enter id= "))
        self.name = input("Enter name= ")
        self.address = input("Enter address= ")

    def output(self):
        return '{0:<5}'.format(str(self.id)) + '{0:<20}'.format(self.name) + '{0:<19}'.format(self.address)

    def getID(self):
        return self.id