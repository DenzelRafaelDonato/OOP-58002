from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("500x400+10+20")
win.title("Welcome to Python Programming")

# Button widgets
btn = Button(win,text = "This is a button", fg = "Orange", bg = "blue", bd=15)
btn.place(x=50, y =50)

# label widget
lbl = Label(win,text = "Gender", fg = "blue", bg = "yellow")
lbl.place(x=50, y = 10)

# text field
txt = Entry(win,font= ("verdana", 12), bd = 5)
txt.place(x=50, y = 130)

# radio button

radio1 = Radiobutton(win, text = "Male", value = 1)
radio2 = Radiobutton(win, text = "Female", value = 2)
radio1.place(x=50, y = 25)
radio2.place(x=110, y = 25)

# list box

var = StringVar()
var.set("Student1")
data = "Student1","Student2","Student3"
listbx = Listbox(win,height=5,selectmode= 'multiple')
data = "Student1"
data1 = "Student2"
data2 = "Student3"

listbx.insert(END,data)
listbx.insert(END, data1)
listbx.insert(END, data2)
listbx.place(x=50, y = 200)

cb = ttk.Combobox(win,values = data)
cb.place(x=50, y=300)

win.mainloop()
