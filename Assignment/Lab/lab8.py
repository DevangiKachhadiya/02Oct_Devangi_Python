#Write Python programs to demonstrate method overloading and method overriding.

#Method Overloading
class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
    def getdata(self,sal):
        print("Salary:",sal)

st=studinfo()
st.getdata(101,'Sanket')
st.getdata(457.34)

#Method Overriding
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