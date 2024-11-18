class sanket:
    sid=0
    stech=""

    def s_getdata(self):
        self.sid=input("Enter sanket's ID: ")
        self.stech=input("Enter Sanket'c Tech.: ")

class ashok(sanket):
    aid=0
    atech=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID: ")
        self.atech=input("Enter Ashok's Tech.: ")

class hitesh(ashok):
    hid=0
    htech=""

    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.htech=input("Enter Hitesh's Tech.: ")

class tops()