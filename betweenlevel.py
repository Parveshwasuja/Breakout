from tkinter import *
import  os
class c():
    def __init__(self):
        self.obj = Tk()
        self.obj.resizable(0,0)
        self.obj.title("Breakout")
        self.obj.geometry("810x490")

        photo = PhotoImage(file="breakout.png")
        l = Label(self.obj, image=photo)
        l.place(x=0, y=0, width=810, height=490)

        can = Canvas(self.obj, width=800, height=600, bg="black")
        can.place(x=0, y=205, width=810, height=40)

        l2 = Label(self.obj, text="Breakout", font=("Arial", 20, "bold"), bg="black", fg="white")
        l2.pack(fill=X, pady=250)

        l1 = Label(self.obj, text="Welcome to Breakout", font=("Arial", 20, "bold"), bg="black", fg="white")
        l1.place(x=230, y=0, width=350, height=40)

        tx = can.create_text(390, 20, text="Do you want to play level 2 ?", font=("Arial", 15, "bold"), fill="white")

        b1 = Button(self.obj, text="Continue", font=("Arial", 18, "bold"), bg="green", fg="white",command=self.continue1)
        b1.place(x=180, y=320, width=200, height=40)

        b2 = Button(self.obj, text="Exit", font=("Arial", 18, "bold"), bg="red", fg="black",command=self.exit)
        b2.place(x=430, y=320, width=200, height=40)
        self.obj.mainloop()

    def continue1(self):
        self.obj.destroy()
        import level2
        #os.system("python level2.py")

    def exit(self):
        exit()


obj1 = c()