# Write a Python program to show hybrid inheritance. 
class Parents:
    def getdata(self):
        print("Hello from parents")
class Child1(Parents):
    def getdata1(self):
        print("Hello from Child1")
class Child2(Parents):
    def getdata2(self):
        print("Hello from Child2")
class GrandChild(Child1,Child2):
    def getdata3(self):
        print("Hello from Grandchild")
g=GrandChild()
g.getdata()
g.getdata1()
g.getdata2()
g.getdata3()
