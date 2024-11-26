# Write a Python program to show method overriding.
class Parent:
    def getdata(self):
        print("Hello from parent's class")
	
class Child(Parent):
    def getdata(self):
        print("Hello from child's class")

c=Child()
c.getdata()
p=Parent()
p.getdata()