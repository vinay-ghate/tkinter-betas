from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Notepad Lte')
root.geometry('540x440')
root.resizable('False','False')
root.config(bg='lightblue')

def save_f():
    file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if file is None:
        return
    text = str(entry.get(1.0,END))
    file = file.write(text)
    file.close()
    
def open_file():
    file = filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content = file.read()
    Entry.insert(INSERT,content)

b1 = Button(root,width='20',height='2',bg='#fff',text='Save File',command=save_f).place(x=100,y=5)
b2 = Button(root,width='20',height='2',bg='#fff',text='Open File',command=open_file).place(x=300,y=5)

entry = Text(root,height=33,width=72,wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()