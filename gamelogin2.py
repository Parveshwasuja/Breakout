from tkinter import *
# from mysql.connector import MySQLConnection
import sqlite3

from tkinter import messagebox, PhotoImage
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


class b:
    # conn = MySQLConnection(host="localhost", database="breakout", user="root", password="")
    conn = sqlite3.connect("breakout.db")
    cur = conn.cursor()
    
    def __init__(self):
        self.obj = Tk()
        self.obj.resizable(0, 0)
        self.obj.title("Breakout")
        self.obj.geometry("810x490")

        ph = PhotoImage(file="breakout.png")
        l1 = Label(self.obj, image=ph)
        l1.place(x=0, y=0, width=810, height=490)

        l3 = Label(self.obj, text="Welcome to Breakout", font=("Arial", 20, "bold"), bg="black", fg="white")
        l3.place(x=230, y=0, width=350, height=40)

        can = Canvas(self.obj, width=800, height=600, bg="black")
        can.place(x=0, y=180, width=810, height=40)

        l2 = Label(self.obj, text="Enter your Name", font=("Arial", 17, "bold"), fg="white", bg="black")
        l2.place(x=100, y=240, width=220, height=40)

        self.e1 = Entry(self.obj, font=("Arial", 18, "bold"))
        self.e1.place(x=370, y=240, width=250, height=40)

        b1 = Button(self.obj, text="Continue", font=("Arial", 18, "bold"), bg="green", fg="white",
                    command=self.continue1)
        b1.place(x=180, y=300, width=200, height=40)

        b2 = Button(self.obj, text="Quit", font=("Arial", 18, "bold"), bg="red", fg="black", command=self.exit)
        b2.place(x=420, y=300, width=200, height=40)

        b3 = Button(self.obj, text="View Score", font=("Arial", 13, "bold"), bg="blue", fg="white", command=self.view)
        b3.place(x=650, y=240, width=100, height=40)

        ob = a(can)
        ob.code()
        self.obj.mainloop()

    def getName(self):
        return self.e1.get()

    def continue1(self):
        try:
            s = "select * from users where username='{0}'".format(self.e1.get())
            cur = self.conn.cursor()
            cur.execute(s)
            s1 = cur.fetchone()
            if s1 is None:
                s2 = "insert into users(username,level1,level2) values('{0}',{1},{2})".format(self.e1.get(), "0", "0")
                cur = self.conn.cursor()
                cur.execute(s2)
                self.conn.commit()
                # os.system("python pday2.py")
                self.obj.destroy()
                import pday2
                # ob= pday2()

            else:
                messagebox.showinfo("Naming error", "Name already exists")
        except Exception as e:
            print(e)
            # messagebox.showinfo("Error", "unfortunately, Breakout is workingly stopped")

    def exit(self):
        exit()

    def view(self):
        s = "select * from users where username='{0}'".format(self.e1.get())
        cur = self.conn.cursor()
        cur.execute(s)
        s1 = cur.fetchone()
        if s1 is None:
            messagebox.showinfo("Naming error", "Name do not exists")
        else:
            level1 = Label(self.obj, text="Level 1", font=("Arial", 15, "bold"), bg="black", fg="white")
            level2 = Label(self.obj, text="Level 2", font=("Arial", 15, "bold"), bg="black", fg="white")
            level1.place(x=250, y=380, width=100, height=30)
            level2.place(x=250, y=430, width=100, height=30)
            # score = Label(self.obj,text="Score",font=("Arial",15,"bold"),bg="black",fg="white")
            # score.place(x=350,y=340,width=100,height=30)
            tx = Entry(self.obj, font=("Arial", 15, "bold"), bg="white", fg="black")
            tx.place(x=400, y=380, width=100, height=30)
            tx1 = Entry(self.obj, font=("Arial", 15, "bold"), bg="white", fg="black")
            tx1.place(x=400, y=430, width=100, height=30)
            tx.delete(0, END)
            tx.insert(0, str(s1[2]))
            tx1.delete(0, END)
            tx1.insert(0, str(s1[3]))
            tx.config(state=DISABLED)
            tx1.config(state=DISABLED)


obj2 = b()
