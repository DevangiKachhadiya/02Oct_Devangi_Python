class studinfo:
    #private
    __id=input("Enter Any Id: ")
    __nm=input("Enter Any Name: ")

    #private
    def __get_data(self):
        print("Id: ",self.__id)
        print("Name: ",self.__nm)

    #public
    def print_data(self):
        self.__get_data()

st=studinfo()
st.print_data()


