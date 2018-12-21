from tkinter import *
from tkinter import PhotoImage

import os


class a:

    def __init__(self, can1):
        self.can = can1  # Canvas(obj, width=600, height=500, bg="#a8a8a8")
        self.tx = self.can.create_text(70, 20, text="BREAKOUT", font=("Arial", 15, "bold"), fill="yellow")
        self.x = 10
        self.dirx = 1

    def code(self):
        cd = self.can.coords(self.tx)
        self.can.move(self.tx, self.x, 0)
        if cd[0] == 60.0:
            self.x = 10
        elif cd[0] == 740:
            self.x = -10

        self.can.after(70, self.code)

    def start(self):
        obj.destroy()
        import gamelogin2

    def exit(self):
        obj.destroy()


obj = Tk()
obj.resizable(0, 0)
obj.geometry("810x490")
# obj.configure(background="black")
obj.title("Welcome to Python game")

photo = PhotoImage(file="breakout.png")
l = Label(obj, image=photo)
l.place(x=0, y=0, width=810, height=490)

can = Canvas(obj, width=800, height=600, bg="black")
can.place(x=0, y=205, width=810, height=40)

ob = a(can)
ob.code()

l2 = Label(obj, text="Breakout", font=("Arial", 20, "bold"), bg="black", fg="white")
l2.pack(fill=X, pady=250)

l1 = Label(obj, text="Welcome to Breakout", font=("Arial", 20, "bold"), bg="black", fg="white")
l1.place(x=230, y=0, width=350, height=40)

# l2.place(x=230,y=210,width=200,height=40)
b1 = Button(obj, text="Start", bg="green", fg="white", font=("Arial", 20, "bold"), command=ob.start)
b1.place(x=300, y=330, width=200, height=40)
b2 = Button(obj, text="Exit", bg="red", fg="black", font=("Arial", 20, "bold"), command=ob.exit)
b2.place(x=300, y=390, width=200, height=40)

obj.mainloop()
