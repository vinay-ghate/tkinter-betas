from tkinter import *

root = Tk()
root.title('Addition Calculator')

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current = e.get() 
    e.delete(0,END) 
    e.insert(0,str(current)+str(number))
 
def clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global sign
    sign = 'add'
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global sign
    sign = 'sub'
    f_num = int(first_number)
    e.delete(0,END)

def button_mult():
    first_number = e.get()
    global f_num
    global sign
    sign = 'mult'
    f_num = float(first_number)
    e.delete(0,END)


def button_div():
    first_number = e.get()
    global f_num
    global sign
    sign = 'div'
    f_num = float(first_number)
    e.delete(0,END)

def button_equal():
    second_num = e.get()
    if sign=='add':
        e.delete(0,END)
        e.insert(0,f_num+int(second_num))
    elif sign=='sub':
        e.delete(0,END)
        e.insert(0,f_num-int(second_num))
    elif sign=='mult':
        e.delete(0,END)
        e.insert(0,f_num*int(second_num))
    elif sign=='div':
        e.delete(0,END)
        e.insert(0,f_num/int(second_num))



myButton1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1)).grid(row=1,column=0)
myButton2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2)).grid(row=1,column=1)
myButton3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3)).grid(row=1,column=2)
myButton4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4)).grid(row=2,column=0)
myButton5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5)).grid(row=2,column=1)
myButton6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6)).grid(row=2,column=2)
myButton7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7)).grid(row=3,column=0)
myButton8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8)).grid(row=3,column=1)
myButton9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9)).grid(row=3,column=2)
myButton0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0)).grid(row=4,column=1)
myButtonadd = Button(root,text='+',padx=40,pady=20,command=button_add).grid(row=4,column=0)
myButtoncalc = Button(root,text='=',padx=40,pady=20,command=button_equal).grid(row=6,column=1)
myButtonClear = Button(root,text='C',padx=40,pady=20,command=clear).grid(row=5,column=1)
myButtonsub = Button(root,text='-',padx=40,pady=20,command=button_sub).grid(row=4,column=2)
myButtonsub = Button(root,text='x',padx=40,pady=20,command=button_mult).grid(row=5,column=0)
myButtonsub = Button(root,text='/',padx=40,pady=20,command=button_div).grid(row=5,column=2)






root.mainloop()