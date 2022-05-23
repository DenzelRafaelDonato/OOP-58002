def main():
    # Find the least number among three numbers
    L = []
    num1 = eval(input("Enter the first number: "))
    L.append(num1)
    num2 = eval(input("Enter the second number: "))
    L.append(num2)
    num3 = eval(input("Enter the third number: "))
    L.append(num3)
    print("The smallest number among the three is:",str(min(L)))
main()

#The GUI Form
from tkinter import *

window = Tk()
window.title("Find the smallest number")
window.geometry("500x400+20+10")

def FindSmallest():
    L = []
    L.append(eval(ConEntry2.get()))
    L.append(eval(ConEntry3.get()))
    L.append(eval(ConEntry4.get()))
    ConSmallest.set(min(L))

#Widgets for GUI

label1 = Label(window,font = "Times 10", text = "A program that determines the smallest number")
label1.grid(row=0,column=1, columnspan=2,sticky=EW)
label2 = Label(window,text = "Insert 1st No.:")
label2.grid(row=1,column = 0,sticky=W)
ConEntry2 = StringVar()
entry2 = Entry(window,bd=3,textvariable=ConEntry2)
entry2.grid(row=1,column = 1)
label3 = Label(window,text ="Insert 2nd No.:")
label3.grid(row=2,column=0, sticky = W)
ConEntry3=StringVar()
entry3 = Entry(window,bd=3,textvariable=ConEntry3)
entry3.grid(row=2,column=1)
label4 = Label(window,text="Insert 3rd No.:")
label4.grid(row=3,column =0, sticky=W)
ConEntry4 = StringVar()
entry4 = Entry(window,bd=3,textvariable=ConEntry4)
entry4.grid(row=3,column=1)
button1 = Button(window,font = "Times 10", text="Determine the smallest number.",command=FindSmallest)
button1.grid(row=4,column = 1)
label5 = Label(window,text="The smallest number is:")
label5.grid(row=5,column=0,sticky=W)
ConSmallest = StringVar()
entry5 = Entry(window,bd=3,state="readonly",textvariable=ConSmallest)
entry5.grid(row=5,column=1)


mainloop()