from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Age Teller")
root.geometry('400x180')
root.resizable('false','false')

Label(root,text="Age Teller",font=('arial',12)).place(x=150,y=0)

Label(root,text="Enter Your Name : ").place(x=0,y=30)
name = Entry(root)
name.place(x=120,y=30)

Label(root,text="Date Of Birth DD MM YYYY: ").place(x=0,y=50)

day = ttk.Combobox(root,width=5)
day['values'] = [i for i in range(1,31)]
day.place(x=0,y=70)

month = ttk.Combobox(root,width=5)
month['values'] = [i for i in range(1,12)]
month.place(x=60,y=70)

year = ttk.Combobox(root,width=10)
year['values'] = [i for i in range(1949,2023)]
year.place(x=120,y=70)

def magics():
    y1.configure(text="Hello "+name.get())
    y2.configure(text=f"Your age is {2023-int(year.get())} Years")

magic = Button(root,text="Magic!!",command=magics)
magic.place(x=10,y=100)

y1 = Label(root,text = "")
y1.place(x=10,y=120)

y2 = Label(root,text = "")
y2.place(x=10,y=140)

root.mainloop()