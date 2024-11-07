from tkinter import *

class MyWindow:
    def __init__(self, window):

        #BUTTON
        self.Btn1 = Button(window, text="Click to change Color", command=self.yel)
        self.Btn1.place(x=135, y=180)

        #FUNCTION
    def yel (self):
        self.Btn1.config (bg='Yellow')

window = Tk()
mywindow = MyWindow(window)

window.geometry("400x400+10+10")
window.title("Special Midterm Exam in OOP")
window.mainloop()