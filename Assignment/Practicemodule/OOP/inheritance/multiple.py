class Daughters:
    def getdata1(self):
        print("Hello From Daughters")

class Son:
    def getdata2(self):
        print("Hello From Son")

class Parents(Daughters,Son):
    def getdata(self):
        print("Hello From Parents")

p=Parents()
p.getdata()
p.getdata1()
p.getdata2()
