#get multiple students data 
def get_data(id,name):
    print("Id:",id)
    print("Name:",name)

n=int(input("Enter no of student data: "))
for i in range(n):
    x=int(input("Enter Id: "))
    y=input("Enter Name: ")
    
get_data(x,y)