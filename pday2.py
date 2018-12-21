from tkinter import *
#from mysql.connector import MySQLConnection
import sqlite3

import os
import random
import math
import time



# from PIL import Image, ImageTk
# from tkinter import messagebox


class ball:

    def __init__(self, can2, slider):
        self.can = can2
        self.slider1 = slider
        t1 = random.randint(0, 770)
        t2 = random.randint(0, 50)
        self.w = can.cget("width")
        self.h = can.cget("height")
        self.ball = self.can.create_oval(t1, t2, t1 + 23, t2 + 23, fill="white")
        self.x = 6
        self.score = 0
        self.y = 6
        self.hitbottom = False

    '''def clear(self):
        self.l1.place_forget()
        self.l.place_forget()
        l2.place_forget()
        #os.system("python betweenlevel.py")'''

    def hitslider(self, pos):
        recpos = self.can.coords(self.slider1.rec)
        if pos[2] >= recpos[0] and pos[0] <= recpos[2]:
            if pos[3] >= recpos[1] and pos[3] <= recpos[3]:
                return True
        # l6 = Label(obj,text="Game End",font=("Arial",50,"bold"),bg="black",fg="white")
        # l6.place(x=400,y=300,width=300,height=50)
        return False

    def anim(self):
        pos = self.can.coords(self.ball)
        if pos[1] <= 0:
            self.y = 6

        if pos[3] >= float(self.h):
            self.hitbottom = True
            self.y = 0
            self.x = 0
            if (self.score < 20):
                self.la = Label(obj, text="Your Score : ", font=("Arial", 25, "bold"), bg="black", fg="white")
                self.la.place(x=550, y=100, width=200, height=40)
                l2.config(text=str(self.score))
                l2.place(x=770, y=100, width=50, height=40)
                self.l5 = Label(obj, text="OOps!! You are failed to complete level 1", font=("Arial", 20, 'bold'),
                                bg="black", fg="white")
                self.l5.place(x=430, y=300, width=550, height=40)
                if level1score < self.score:
                    update = "update users set level1={0} where id={1}".format(self.score, userid)
                    cur = conn.cursor()
                    cur.execute(update)
                    conn.commit()

        if self.hitslider(pos) == True:
            self.score = self.score + 10
            # e.config(state=NORMAL)
            # e.delete(0, END)
            # e.insert(0, str(self.score))
            l1.config(text=str(self.score))
            self.y = -6

        if pos[0] <= 0:
            self.x = 6
        if pos[2] >= float(self.w):
            self.x = - 6
        if self.score < 20:
            self.can.move(self.ball, self.x, self.y)
            self.can.after(30, self.anim)
        if self.score == 20:
            l2.config(text=str(self.score))
            l2.place(x=770, y=100, width=50, height=40)
            update = "update users set level1={0} where id={1}".format(self.score, userid)
            cur1 = conn.cursor()
            cur1.execute(update)
            conn.commit()

            self.l = Label(obj, text="Game over", font=("Arial", 20, "bold"), bg="black", fg="white")
            self.l.place(x=520, y=150, width=300, height=40)

            self.l1 = Label(obj, text="Your Score : ", font=("Arial", 25, "bold"), bg="black", fg="white")
            self.l1.place(x=550, y=100, width=200, height=40)

            self.b5 = Button(obj, text="Next", font=("Arial", 25, "bold"), bg="red", fg="white", command=self.open)
            self.b5.place(x=600, y=250, width=150, height=40)

    def open(self):
        obj.destroy()
        import betweenlevel
        # os.system("python betweenlevel.py")


class slider:
    def __init__(self, can1):
        self.can = can1
        self.rec = self.can.create_rectangle(325, 500, 475, 520, fill="red")
        self.x = 0
        self.w = can.cget("width")
        self.can.bind_all('<KeyPress-Left>', self.move)
        self.can.bind_all('<KeyPress-Right>', self.move1)

    """def draw_rec(self):
        self.can.move(self.rec,self.x,0)
        pos = self.can.coords(self.rec)


        self.can.move(self.rec, self.x, 0)"""

    def move(self, event):
        pos = self.can.coords(self.rec)
        if pos[0] <= 0:
            self.x = 0
        else:
            self.x = -30
            self.can.move(self.rec, self.x, 0)
            # pos = self.can.coords(self.rec)
            # lb.config(text=pos)

    def move1(self, event):
        pos = self.can.coords(self.rec)
        if pos[2] >= float(self.w):
            self.x = 0
        else:
            self.x = 30
            self.can.move(self.rec, self.x, 0)
            # pos = self.can.coords(self.rec)
            # lb.config(text=pos)


obj = Tk()
conn = sqlite3.connect("breakout.db")

obj.title("Breakout")
obj.geometry("1366x768")
obj.configure(background="#A93226")
obj.update()

name = "select * from users order by id desc limit 1"
cur = conn.cursor()
cur.execute(name)
name2 = cur.fetchone()
userid = name2[0]
level1score = name2[2]

# photo = PhotoImage(file="C:\\Users\\Dell\\PycharmProjects\\parvesh\\project\\level12.png")
# l11 = Label(obj, image=photo)
# l11.place(x=0, y=0, width=1366, height=768)

l = Label(obj, text=name2[1], fg="white", font=("Arial", 24, "bold"), bg="#A93226")
l.pack(fill=X, pady=0)

can = Canvas(obj, width=800, height=600, bg="black")
can.place(x=300, y=43, width=800, height=600)

# lb = Label(obj, text="ddd", fg="blue", width=200)
# lb.place(x=10, y=10, width=200, height=30)

sc = Label(obj, text="Score : ", fg="white", width=200, bg="#A93226", font=("Arial", 20, "bold"))
sc.place(x=300, y=650, width=100, height=40)

l2 = Label(obj, text="", fg="white", bg="black", font=("Arial", 20, "bold"))

l1 = Label(obj, text="0", font=("Arial", 18, "bold"), fg="white", bg="#A93226")
l1.place(x=400, y=650, width=100, height=40)

ob = slider(can)
ob1 = ball(can, ob)


def button():
    ob1.anim()
    b1.place_forget()


b1 = Button(obj, text="Start", bg="green", fg="white", font=("Arial", 20, "bold"), command=button)
b1.place(x=600, y=300, width=200, height=60)

obj.mainloop()
