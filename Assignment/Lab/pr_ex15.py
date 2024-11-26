#  Write a Python program to show multiple inheritance.
class Vivek:
    v_id=0
    v_std=""

    def v_getdata(self):
        self.v_id=input("Enter Vivek's ID: ")
        self.v_std=input("Enter Vivek's Study: ")

class Jeet:
    j_id=0
    j_std=""

    def j_getdata(self):
        self.j_id=input("Enter Jeet's ID: ")
        self.j_std=input("Enter Jeet's Study: ")

class Palak:
    p_id=0
    p_std=""

    def p_getdata(self):
        self.p_id=input("Enter Palak's ID: ")
        self.p_std=input("Enter Palak's Study: ")

class Kachhadiya(Vivek,Jeet,Palak):
    def printdata(self):
        print("-------------Vivek's Data------------")
        print("Vivek's ID: ",self.v_id)
        print("Vivek's Study: ",self.v_std)
        print("-------------Jeet's Data------------")
        print("Jeet's ID:",self.j_id)
        print("Jeet's Study:",self.j_std)
        print("-------------Palak's Data------------")
        print("Palak's ID: ",self.p_id)
        print("Palak's Study: ",self.p_std)

k=Kachhadiya()
k.v_getdata()
k.j_getdata()
k.p_getdata()
k.printdata()

