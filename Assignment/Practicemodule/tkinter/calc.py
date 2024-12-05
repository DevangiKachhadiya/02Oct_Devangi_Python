import tkinter

screen=tkinter.Tk()
screen.title("Calc")
screen.geometry("400x500")
screen.config(bg="black")

tkinter.Label(text="no 1",bg='black',fg='white',font='Elephant 16').grid(row=0,column=0,sticky='w')
tkinter.Label(text="no 2",bg='black',fg='white',font='Elephant 16').grid(row=1,column=0,sticky='w')
r=tkinter.Label(text="Result : ",bg='black',fg='white',font='Elephant 18')
r.place(x=115,y=365)

t1=tkinter.Entry()
t1.grid(row=0,column=1,sticky='w')
t2=tkinter.Entry()
t2.grid(row=1,column=1,sticky='w')


def add_btnclick():
    try:
        n1=int(t1.get())
        n2=int(t2.get())
        result=n1+n2
        r.config(text=f"Result: {result}")
    except ValueError:
        r.config(text=f"Result: Invalid input")
    
    print("ADD. Button Clicked")



def sub_btnclick():
    try:
        n1=int(t1.get())
        n2=int(t2.get())
        result=n1-n2
        r.config(text=f"Result: {result}")
    except ValueError:
        r.config(text=f"Result: Invalid input")
    print("SUB. Button Clicked")

def mul_btnclick():
    try:
        n1=int(t1.get())
        n2=int(t2.get())
        result=n1*n2
        r.config(text=f"Result: {result}")
    except ValueError:
        r.config(text=f"Result: Invalid input")
    print("MUL. Button Clicked")

def div_btnclick():
    try:
        n1=int(t1.get())
        n2=int(t2.get())
        result=n1/n2
        r.config(text=f"Result: {result}")
    except ValueError:
        r.config(text=f"Result: Invalid input")
    print("Div. Button Clicked")

'''def ans_btnclick():
    print("Answer is: ")'''

tkinter.Button(text="+",bg='black',fg='white',font='Elephant 18',command=add_btnclick).place(x=100,y=200)
tkinter.Button(text="-",bg='black',fg='white',font='Elephant 18',command=sub_btnclick).place(x=190,y=200)
tkinter.Button(text="*",bg='black',fg='white',font='Elephant 18',command=mul_btnclick).place(x=100,y=280)
tkinter.Button(text="/",bg='black',fg='white',font='Elephant 16',command=div_btnclick).place(x=190,y=280)

#tkinter.Button(text="Answer",bg='black',fg='white',font='Elephant 18',command=ans_btnclick).place(x=115,y=365)
screen.mainloop()