from tkinter import *

class MidtermExam:
    def __init__(self,win):
        self.label=Label(win, text = 'Enter your full name:',fg = "red")
        self.button=Button(win, text = "Click to display your Fullname", fg = "Red", command = self.print)
        self.a1=Entry(bd = 8)
        self.a2=Entry(bd = 8)
        self.label.place(x=50, y = 35)
        self.button.place(x=50, y = 100)
        self.a1.place(x=300, y = 30)
        self.a2.place(x=300, y = 100)

    def print(self):
        self.a2.insert(END, str(self.a1))

window = Tk()
myWin = MidtermExam(window)
window.title('Midterm in OOP')
window.geometry("700x300+10+10")
window.mainloop()

