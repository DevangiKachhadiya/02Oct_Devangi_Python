class stud_info:
    id=int
    name=str
    
    def getdata(self):
        self.id=int(input("Enter Student id: "))
        self.name=input("Enter student Name: ")

    def print_data(self):
        print("Student id:",self.id)
        print("student Name:",self.name)

st=stud_info()
st.getdata()
st.print_data()