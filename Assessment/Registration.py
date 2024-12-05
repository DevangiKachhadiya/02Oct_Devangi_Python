import tkinter

screen=tkinter.Tk()
screen.title("Registration Form")
screen.geometry("400x500")
screen.config(bg='light gray')

tkinter.Label(text="Name*",bg='light gray',fg='black',font=' 16').grid(row=0,column=0,sticky='w')
tkinter.Label(text="contact*",bg='light gray',fg='black',font=' 16').grid(row=1,column=0,sticky='w')
tkinter.Label(text="Email*",bg='light gray',fg='black',font=' 16').grid(row=2,column=0,sticky='w')
tkinter.Label(text="Gender*",bg='light gray',fg='black',font=' 16').grid(row=3,column=0,sticky='w')
tkinter.Label(text="City*",bg='light gray',fg='black',font=' 16').grid(row=4,column=0,sticky='w')
tkinter.Label(text="State*",bg='light gray',fg='black',font=' 16').grid(row=5,column=0,sticky='w')

t1=tkinter.Entry(font=' 16')
t1.grid(row=0,column=1,sticky='w')

t1=tkinter.Entry(font=' 16')
t1.grid(row=1,column=1,sticky='w')

t1=tkinter.Entry(font=' 16')
t1.grid(row=2,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",bg="light gray",fg="black",font=' 12').grid(row=3,column=1,sticky="w")
tkinter.Radiobutton(value=1,text="Female",bg="light gray",fg="black",font=' 12').grid(row=3,column=2,sticky='w')

t1=tkinter.Entry(font=' 16')
t1.grid(row=4,column=1,sticky='w')

t1=tkinter.Entry(font=' 16')
t1.grid(row=5,column=1,sticky='w')

def btnclick():
    print("Button clicked")

tkinter.Button(text="Register",bg='yellow',font=' 18',command=btnclick).place(x=160,y=250)

screen.mainloop()