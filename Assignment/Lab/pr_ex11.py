#create a class & access the properties of the class using an object.
class Student:
    id=int
    name=str

    def get_data(self):
        self.id=input("Enter an ID: ")
        self.name=input("Enter a Name: ")

    def print_data(self):
        print("ID : ",self.id)
        print("Name : ",self.name)

st=Student()
st.get_data()
st.print_data()