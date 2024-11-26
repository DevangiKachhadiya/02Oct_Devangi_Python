# Write a Python program to show hierarchical inheritance. 
class Parents:
    def getdata(self):
        print("This is parents class!")

class Daughters(Parents):
    def getdata1(self):
        print("This is daughters class!!!")

class Son(Parents):
    def getdata2(self):
        print("This is son's class!!!")

obj1=Son()
obj1.getdata()
obj1.getdata2()

obj2=Daughters()
obj2.getdata()
obj2.getdata1()
