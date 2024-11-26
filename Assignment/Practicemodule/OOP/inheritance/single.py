class father:
    car=0
    bal=0

    def get_data(self):
        self.car=input("Enter car Details: ")
        self.bal=input("Enter bank balance details: ")

class son(father):
    def print_data(self):
        print("Car: ",self.car)
        print("Bank Balance: ",self.bal)

sn=son()
sn.get_data()
sn.print_data()

'''class father:
    def get_data(self):
        print("This Is Parent Class")

class daughter(father):
    def get_child_data(self):
        print("This Is Child Class")

d=daughter()
d.get_data()
d.get_child_data()'''