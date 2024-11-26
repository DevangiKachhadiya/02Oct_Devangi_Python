class shiv:
    sid=0
    snm=" "
    def s_getdata(self):
        self.sid=input("Enter ID: ")
        self.snm=input("Enter name: ")

class shakti(shiv):
    s_id=0
    s_nm=""
    def ss_getdata(self):
        self.s_id=input("Enter Id: ")
        self.s_nm=input("Enter name: ")

class kartik(shakti):
    k_id=0
    k_nm=""
    def k_getdata(self):
        self.k_id=input("Enter Id: ")
        self.k_nm=input("Enter name: ")

class kailash(kartik):
    def print_data(self):
        print("---------Shiv's Info--------")
        print("ID: ",self.sid)
        print("Name: ",self.snm)
        print("---------Shakti's Info--------")
        print("ID: ",self.s_id)
        print("Name: ",self.s_nm)
        print("---------Kartik's Info--------")
        print("ID: ",self.k_id)
        print("Name: ",self.k_nm)

k=kailash()
k.s_getdata()
k.ss_getdata()
k.k_getdata()
k.print_data()




        