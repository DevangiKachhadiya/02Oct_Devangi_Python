'''Write Python programs to demonstrate different types of inheritance 
(single, multiple, multilevel, etc.).'''
# SINGLE INHERITANCE
class Student:
    stid=int
    st_name=str
    def get_data(self):
        self.id = input("Enter an id: ")
        self.name=input("Enter a name: ")
        print("This is Main class")

class Child(Student):
    def print_data(self):
        print("Id is: ",self.id)
        print("Name is: ",self.name)
        print("This is Sub class")
    
c=Child()
c.get_data()
c.print_data()

# MULTIPLE INHERITANCE

class GrandParent:
    def getdata(self):
        print("This Is Grandparent Class")

class Parent(GrandParent):
    def getdata1(self):
        print("This Is Parent Class")

class Child(Parent):
    def getdata2(self):
        print("This Is Child Class")

c=Child()
c.getdata()
c.getdata1()
c.getdata2()

# MULTILEVEL INHERITANCE

class Vivek:
    vid=0
    vnm=""

    def getdata(self):
        self.vid=input("Enter Vivek's Id: ")
        self.vnm=input("Enter Vivek's Name: ")

class Jeet(Vivek):
    jid=0
    jnm=""

    def getdata2(self):
        self.jid=input("Enter Jeet's Id: ")
        self.jnm=input("Enter Jeet's Name: ")

class Palak(Jeet):
    pid=0
    pnm=""

    def getdata3(self):
        self.pid=input("Enter Palak's Id: ")
        self.pnm=input("Enter palak's Name: ")

class Kachhadiya(Palak):
    def printdata(self):
        print("-----------Vivek's Info--------------")
        print("Vivek's ID: ",self.vid)
        print("Vivek's Name: ",self.vnm)
        print("-------------Jeet's Info-------------")
        print("Jeet's ID: ",self.jid)
        print("Jeet's Name: ",self.jnm)
        print("-------------Palak's Info-------------")
        print("Palak's ID:",self.pid)
        print("Palak's Name: ",self.pnm)

k=Kachhadiya()
k.getdata()
k.getdata2()
k.getdata3()
k.printdata()

