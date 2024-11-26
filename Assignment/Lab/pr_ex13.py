# Write a Python program to show single inheritance.
class Father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter Car Details: ")
        self.bal=input("Enter Bank Balance: ")

class Son(Father):
    def print_data(self):
        print("Inherit from Father")
        print("Car: ",self.car)
        print("Bank Balance: ",self.bal)

s=Son()
s.getdata()
s.print_data()

