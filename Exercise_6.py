from tkinter import *

class MyWindow:
    def __init__(self, window):
        window.config(bg="#7b7b7b")

        #HEADING
        self.lbl1 = Label(window, fg='#9dee67', bg='#7b7b7b', text='Simple Calculator', font=("Courier New Bold", 20))
        self.lbl1.place(x=60, y=10)

        #NUMBER 1
        self.lbl2 = Label(window, fg='#9dee67', bg='#7b7b7b', text='Number 1:', font=("Courier New Bold", 10))
        self.lbl2.place(x=50, y=50)

        self.Ent1 = Entry(window, bd=5)
        self.Ent1.place(x=125, y=50)

        #NUMBER 2
        self.lbl3 = Label(window, fg='#9dee67', bg='#7b7b7b', text="Number 2:", font=("Courier New Bold", 10))
        self.lbl3.place(x=50, y=100)

        self.Ent2 = Entry(window, bd=5)
        self.Ent2.place(x=125, y=100)

        #OUTPUT
        self.lbl4 = Label(window, fg='#9dee67', bg='#7b7b7b', text="Output:", font=("Courier New Bold", 10))
        self.lbl4.place(x=50, y=150)

        self.Ent3 = Entry(window, bd=5)
        self.Ent3.place(x=125, y=150)

        #BUTTONS
        self.Btn1 = Button(window, fg="Red", text="Add", font=("Courier New Bold", 8), command=self.add)
        self.Btn1.place(x=60, y=200)
        self.Btn2 = Button(window, fg="Red", text="Subtract", font=("Courier New Bold", 8), command=self.sub)
        self.Btn2.place(x=110, y=200)
        self.Btn3 = Button(window, fg="Red", text="Multiply", font=("Courier New Bold", 8), command=self.mul)
        self.Btn3.place(x=195, y=200)
        self.Btn4 = Button(window, fg="Red", text="Divide", font=("Courier New Bold", 8), command=self.div)
        self.Btn4.place(x=273, y=200)
        self.Btn5 = Button(window, fg="Red", text="Clear", font=("Courier New Bold", 8), command=self.clear)
        self.Btn5.place(x=160, y=240)

        #CALCULATOR FUNCTIONS
    def add (self):
        self.Ent3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Ent3.insert(END, str(result))

    def sub (self):
        self.Ent3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Ent3.insert(END, str(result))

    def mul (self):
        self.Ent3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Ent3.insert(END, str(result))

    def div (self):
        self.Ent3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entxcd3.insert(END, str(result))

    def clear (self):
        self.Ent1.delete(0, 'end')
        self.Ent2.delete(0, 'end')
        self.Ent3.delete(0, 'end')


window = Tk()
mywindow = MyWindow(window)

window.geometry("400x300+10+10")
window.title("Calcu-Calculator")
window.mainloop()
