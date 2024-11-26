class stud:
    def __init__(self, id,name):
        self.id = id
        self.name = name

    def print_data(self):
        print(f"ID:{self.id} \nName:{self.name}")

s = stud("21", "Krishna")

s.print_data()  
