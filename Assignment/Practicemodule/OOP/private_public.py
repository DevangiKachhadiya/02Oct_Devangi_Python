class public:
    sid=21
    snm='krishna'

    def getdata(self):
        print("This is public")

p=public()
print(p.sid)
print(p.snm)
p.getdata()
