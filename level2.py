from tkinter import *
#from mysql.connector import MySQLConnection
import sqlite3
import random

class ball:

    def __init__(self, can2, slider):
        self.score2 = 0
        self.can = can2
        self.slider1 = slider
        self.l6 = Label(obj, text="Congratulations!! You have completed Level 2", font=("Arial", 25, "bold"),
                        bg="black",
                        fg="white")
        self.w = can.cget("width")
        self.h = can.cget("height")
        self.ball = self.can.create_rectangle(300, 300, 320, 318, fill="white")
        # self.blocks1 = [self.can.create_rectangle( x, y, x + 100, y+20,fill="yellow") for x in range(110, 1101, 110) for y in range(70,131,30)]
        # self.blocks2 = [self.can.create_rectangle( x, 100, x + 100, 120,fill="yellow") for x in range(110, 1101, 110)]
        # self.blocks3 = [self.can.create_rectangle( x, 130, x + 100, 150,fill="yellow") for x in range(110, 1101, 110)]
        self.x = 2
        #self.score = 0
        self.y = 2
        self.t = 1
        self.hitbottom = False

    def hitslider(self, pos):
        recpos = self.can.coords(self.slider1.rec)
        if pos[2] >= recpos[0] and pos[0] <= recpos[2]:
            if pos[3] >= recpos[1] and pos[3] <= recpos[3]:
                return True
        return False

    def collision(self, x1, y1, x2, y2, x3, y3, x4, y4):
        if (x1 > x4) or (x2 < x3) or (y1 > y4) or (y2 < y3):
            return False
        else:
            return True

    def clear(self):
        self.l6.place_forget()

    def anim(self):
        pos = self.can.coords(self.ball)

        if self.slider1.deletedblocks == 30:
            self.x = 0
            self.y = 0
            self.t = 0

            self.l6.place(x=300, y=340, width=800, height=50)
            self.score2 = self.slider1.score1
            if self.score2 > level2score:
                update1 = "update users set level2={0} where id={1}".format(self.score2, userid)
                cur1 = conn.cursor()
                cur1.execute(update1)
                conn.commit()

            #self.l6.after(2000, self.clear)

        if pos[1] <= 0:
            self.y = 6

        if pos[3] >= float(self.h):
            self.t = 0
            self.hitbottom = True
            self.slider1.lives = self.slider1.lives - 1
            self.y = 0
            self.x = 0
            self.can.after_cancel(self.tick)

            if self.hitbottom == True and self.slider1.lives > 0:
                b1.place(x=500, y=10, width=300, height=80)
                livesc.config(text=str(self.slider1.lives))
                t1 = random.randint(0, 1300)
                t2 = random.randint(300, 500)
                self.can.delete(self.ball)
                self.ball = self.can.create_rectangle(t1, t2, t1 + 20, t2 + 18, fill="white")
                self.hitbottom = False
                self.t = 1

            elif self.slider1.lives <= 0:
                livesc.config(text=str(self.slider1.lives))
                if self.slider1.deletedblocks == 30:
                    if self.score2 > level2score:
                        update1 = "update users set level2={0} where id={1}".format(self.score2, userid)
                        cur1 = conn.cursor()
                        cur1.execute(update1)
                        conn.commit()
                    self.l6.place(x=300, y=340, width=700, height=50)
                    self.l6.after(2000, self.clear)
                else:
                    self.l8 = Label(obj, text="OOps! You are failed to complete level 2",
                                    font=("Arial", 25, "bold"),
                                    bg="black",
                                    fg="white")
                    self.l8.place(x=300, y=340, width=700, height=50)
                    self.score2 = self.slider1.score1
                    self.t=0
                    if self.score2>level2score:
                        update1 = "update users set level2={0} where id={1}".format(self.score2, userid)
                        cur1 = conn.cursor()
                        cur1.execute(update1)
                        conn.commit()

                    self.l8.after(2000, self.clear)
        if self.hitslider(pos) == True:
            # self.score = self.score + 10
            # e.delete(0, END)
            # e.insert(0, str(self.score))
            self.y = -6

        if pos[0] <= 0:
            self.x = 6
        if pos[2] >= float(self.w):
            self.x = - 6

        for i in self.slider1.blocks1:
            pos1 = self.can.coords(i)
            b = self.collision(pos[0], pos[1], pos[2], pos[3], pos1[0], pos1[1], pos1[2], pos1[3])
            if b == True:
                self.slider1.score1 = self.slider1.score1 + 10
                score.config(text=str(self.slider1.score1))
                self.y = -self.y
                self.slider1.blocks1.remove(i)
                self.can.delete(i)

                self.slider1.deletedblocks += 1

        if self.t == 1:
            self.can.move(self.ball, self.x, self.y)

            if self.slider1.lives == 1:
                self.can.after_cancel(self.tick)
                self.tick= self.can.after(30, self.anim)
            if self.slider1.lives == 2:
                self.can.after_cancel(self.tick)
                self.tick = self.can.after(30, self.anim)
            if self.slider1.lives == 3:
                self.tick = self.can.after(30, self.anim)


class slider:
    def __init__(self, can1):
        self.deletedblocks = 0
        self.score1 = 0
        self.lives = 3
        self.can = can1
        self.rec = can.create_rectangle(550, 550, 700, 570, fill="red")
        self.x = 0
        self.w = can.cget("width")
        self.blocks1 = [self.can.create_rectangle(x, y, x + 100, y + 20, fill="yellow") for x in range(110, 1101, 110)
                        for y in range(70, 131, 30)]
        self.can.bind_all('<KeyPress-Left>', self.move)
        self.can.bind_all('<KeyPress-Right>', self.move1)

    def move(self, event):
        pos = self.can.coords(self.rec)
        if pos[0] <= 0:
            self.x = 0
        else:
            self.x = -35
            self.can.move(self.rec, self.x, 0)
            pos = self.can.coords(self.rec)

    def move1(self, event):
        pos = self.can.coords(self.rec)
        if pos[2] >= 1366:
            self.x = 0
        else:
            self.x = 35
            self.can.move(self.rec, self.x, 0)
            pos = self.can.coords(self.rec)


obj = Tk()
obj.geometry("1366x768")
obj.title("Breakout")
obj.configure(background="black")
can = Canvas(obj, width=1366, height=768, bg="black")

conn = sqlite3.connect("breakout.db")

name = "select * from users order by id desc limit 1"
cur = conn.cursor()
cur.execute(name)
name2 = cur.fetchone()
userid=name2[0]
level2score = name2[3]

can.place(x=0, y=70, width=1366, height=768)

ob = slider(can)

sc = Label(obj, text="Score : ", fg="white", width=200, bg="black", font=("Arial", 20, "bold"))
sc.place(x=60, y=10, width=100, height=40)

live = Label(obj, text="Lives : ", fg="white", width=200, bg="black", font=("Arial", 20, "bold"))
live.place(x=1100, y=10, width=100, height=40)

score = Label(obj, text="0", fg="white", bg="black", width=200, font=("Arial", 20, "bold"))
score.place(x=160, y=10, width=100, height=40)

livesc = Label(obj, text="3", fg="white", bg="black", width=200, font=("Arial", 20, "bold"))
livesc.place(x=1200, y=10, width=50, height=40)

def button():
    ob1.t = 1
    ob1.anim()
    b1.place_forget()
    ob1.x = 6
    ob1.y = 6


b1 = Button(obj, text="Start", bg="green", fg="white", font=("Arial", 20, "bold"), command=button)
b1.place(x=500, y=0, width=300, height=80)

ob1 = ball(can, ob)

obj.mainloop()
