class stud_data:
    id=int(input("Enter Student id: "))
    name=input("Enter student Name: ")

    def getdata(self):
        print("Student id:",self.id)
        print("student Name:",self.name)

st=stud_data()
st.getdata()