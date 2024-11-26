class Student:
    __stid=21
    __stnm='krishna'

    def __getdata(self):
        print("ID: ",self.__stid)
        print("Name: ",self.__stnm)

    def print_data(self):
        self.__getdata()

    def public_pro(self):
        print("This is global variable")

st=Student()
st.print_data()
st.public_pro()