class grandparent:
    def getdata(self):
        print("This Is GrandParent Class")

class parent(grandparent):
    def get_data(self):
        print("This Is Parent Class")

class child(parent):
    def get_child_data(self):
        print("This Is Child Class")

c=child()
c.getdata()
c.get_data()
c.get_child_data()


