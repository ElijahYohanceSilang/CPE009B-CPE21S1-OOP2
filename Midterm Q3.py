from tkinter import *

class MyWindow:
    def __init__(self, window):

        #LABEL
        self.lbl1 = Label(window, fg='Red', text='Enter your fullname:')
        self.lbl1.place(x=30, y=100)

        #BOX FOR TYPE
        self.Ent1 = Entry(window, bd=5)
        self.Ent1.place(x=250, y=100)

        #BUTTON
        self.Btn1 = Button(window, fg="Red", text="Click to display your Fullname", command=self.dis)
        self.Btn1.place(x=30, y=140)

        #BOX FOR OUTPUT
        self.Ent2 = Entry(window, bd=5)
        self.Ent2.place(x=250, y=140)

        #FUNCTION
    def dis (self):
        name = str(self.Ent1.get())
        result = name
        self.Ent2.insert(END, str(result))


window = Tk()
mywindow = MyWindow(window)

window.geometry("500x300+10+10")
window.title("Midterm in OOP")
window.mainloop()