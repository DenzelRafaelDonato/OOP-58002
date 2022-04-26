from tkinter import *
window = Tk()
window.geometry("400x300+20+10")
window.title('The Grid Manager')

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Entry(window,bd=3,justify="center")
        self.lbl1.grid(row=0,column=0,padx=2)
        self.lbl1.insert(0,"Standard Calculator")
        self.lbl2 = Entry(window,bd=3,justify="center")
        self.lbl2.grid(row=1,column=0,padx=2)
        self.lbl2.insert(0,"Input 1st Number :")
        self.txtfld2 = Entry(window,bd=3)
        self.txtfld2.grid(row=1,column=1)
        self.lbl3 = Entry(window,bd=3,justify="center")
        self.lbl3.grid(row=2,column=0,padx=2)
        self.lbl3.insert(0,"Input 2nd Number :")
        self.txtfld3=Entry(window,bd=3)
        self.txtfld3.grid(row=2,column=1,padx=2)
        self.lbl4 = Entry(window,bd=3,justify="center")
        self.lbl4.grid(row=3,column=0,padx=2)
        self.lbl4.insert(0,"Select Operators :")
        self.btn1=Button(window,text="Addition(+)",command=self.add)
        self.btn1.grid(row=4,column=0,padx=2)
        self.btn2 = Button(window,text="Subtraction(-)")
        self.btn2.grid(row=4,column=1,padx=2)
        self.btn2.bind('<Button-1>',self.subtract)
        self.btn3=Button(window,text="Multiply(*)", command=self.multiply)
        self.btn3.grid(row=5,column=0,padx=2)
        self.btn4=Button(window,text="Division(/)")
        self.btn4.grid(row=5,column=1,padx=2)
        self.btn4.bind('<Button-1>',self.division)
        self.lbl5=Entry(window,bd=3,justify="center")
        self.lbl5.grid(row=7,column=0,padx=2)
        self.lbl5.insert(0,"Result :")
        self.txtfld4=Entry(window,bd=4)
        self.txtfld4.grid(row=7,column=1,padx=2)

    def add(self):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1+num2
        self.txtfld4.insert(END,answer)
    def subtract(self,event):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1-num2
        self.txtfld4.insert(END,answer)
    def multiply(self):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1*num2
        self.txtfld4.insert(END,answer)

    def division(self,event):
        self.txtfld4.delete(0,'end')
        num1=int(self.txtfld2.get())
        num2=int(self.txtfld3.get())
        answer = num1/num2
        self.txtfld4.insert(END,str(answer))

mywin = MyWindow(window)

window.mainloop()