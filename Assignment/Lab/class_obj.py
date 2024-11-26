#Write a Python program to create a class and access its properties using an object.
class Student:
    id=21
    name='krishna'

    def getdata(self):
        print("Id:",self.id)
        print("Name:",self.name)

st=Student()
st.getdata()