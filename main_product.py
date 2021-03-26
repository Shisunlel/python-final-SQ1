from Product import *
def menu():
    try:
        list = []
        while True:
            print("==========")
            print("1. Add Product")
            print("2. Show")
            print("3. Remove By Id")
            print("0. Exit")
            choice = int(input("Choose between 0 and 3= "))
            print("==========")
            if choice.__eq__(1):
                print("1. Add Product")
                n = int(input("Enter n= "))
                for i in range(0,n):
                    product = Product()
                    print("==========")
                    product.input()
                    list.append(product)
                continue
            if choice.__eq__(2):
                print("2. Show")
                total = 0
                if len(list).__eq__(0):
                    print("List is empty")
                    continue
                print("ID{:<3}Name{:<6}Price{:<3}Qty{:<3}Amount".format('','','',''))
                for item in list:
                    print(item.output())
                    total += item.amount()
                print("{:>22}Total: ".format('') + '$'+ str(total))
                continue
            if choice.__eq__(3):
                print("3. Remove By Id")
                if len(list).__eq__(0):
                    print("List is empty")
                    continue
                count = 0
                id = int(input("Enter id to remove= "))
                for item in list:
                    if(item.getID().__eq__(id)):
                        list.remove(item)
                        count = 0
                        print("Remove successfully")
                        continue
                    else:
                        count =1
                if count.__eq__(1):
                    print("No product match with this id")
                continue
            if choice.__eq__(0):
                raise SystemExit
    except Exception as e:
        print(e)

menu()
