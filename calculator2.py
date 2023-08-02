from tkinter import *

root = Tk()
root.title("Calculator")
# root.iconbitmap("favicon_io/favicon.ico")

e = Entry(root,width=35,borderwidth=5,font=('airal',10,'bold'),bg='green',fg='white')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(s):
    global equation
    equation = e.get()
    e.delete(0,END)
    e.insert(0,str(equation)+str(s))

def calculate():
    try:
        y = eval(str(e.get()))
        e.delete(0,END)
        e.insert(0,y)
    except:
        e.delete(0,END)
        e.insert(0,"Error")


button_one = Button(root,text="1",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(1))
button_two = Button(root,text="2",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(2))
button_three = Button(root,text="3",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(3))
button_four = Button(root,text="4",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(4))
button_five = Button(root,text="5",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(5))
button_six = Button(root,text="6",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(6))
button_seven = Button(root,text="7",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(7))
button_eight = Button(root,text="8",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(8))
button_nine = Button(root,text="9",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(9))
button_zero = Button(root,text="0",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('0'))
button_add = Button(root,text="+",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('+'))
button_sub = Button(root,text="-",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('-'))
button_div = Button(root,text="/",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('/'))
button_mult = Button(root,text="*",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('*'))
button_calc = Button(root,text="=",font=('airal',10,'bold'),bg='green',fg='white',padx=40,pady=20,command=calculate )
button_rbrac = Button(root,text=")",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click(')'))
button_lbrac = Button(root,text="(",font=('airal',10,'bold'),bg='blue',fg='white',padx=40,pady=20,command=lambda : button_click('('))
button_clear = Button(root,text = "C",font=('airal',10,'bold'),bg='red',fg='white',padx=40,pady=20,command=e.delete(0,END))

button_one.grid(row=1,column=0)
button_two.grid(row=1,column=1)
button_three.grid(row=1,column=2)
button_four.grid(row=2,column=0)
button_five.grid(row=2,column=1)
button_six.grid(row=2,column=2)
button_seven.grid(row=3,column=0)
button_eight.grid(row=3,column=1)
button_nine.grid(row=3,column=2)
button_zero.grid(row=4,column=1)
button_add.grid(row=4,column=0)
button_sub.grid(row=4,column=2)
button_div.grid(row=5,column=0)
button_mult.grid(row=5,column=1)
button_calc.grid(row=5,column=2)
button_rbrac.grid(row=6,column=0)
button_lbrac.grid(row=6,column=1)
button_clear.grid(row=6,column=2)

root.mainloop()