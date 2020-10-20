#!/usr/bin/env python
# coding: utf-8

# In[106]:

from tkinter import Tk, Canvas, Frame, BOTH
import random
import time
from math import sqrt

# In[127]:

y1 = 0


class Draw(Frame):

    def __init__(self, *args):

        self.xn = []
        self.yn = []
        self.xc = []
        self.xcc = []
        self.yc = []

        super().__init__()

    def get_coord_start_line(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    def print_coord_start_line(self):
        print("self.x0, self.y0 ", self.x0, self.y0)
        print("self.xn, self.yn ", self.xn, self.yn)
        print("self.x, self.y, self.r ", self.x, self.y, self.r)

    def get_coord_line(self, args):
        if len(args) > 2:

            i = 0
            while i < len(args):
                self.xc.append(-4)
                self.xcc.append(-4)
                self.yc.append(-4)
                self.xn.append(500)
                self.yn.append(500 * args[i + 1] / args[i])
                i += 2

        else:
            # print(self.xn)
            self.xn.append(args[0])
            self.yn.append(args[1])

    def get_coord_circle(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def initUI(self):

        def move_down(event):
            global y1
            y1 += 5
            canvas.delete("all")

        def move_up(event):
            global y1
            y1 -= 5
            canvas.delete("all")

        canvas.bind_all('w', move_up)
        canvas.bind_all('s', move_down)

        for i in range(len(self.xn)):
            canvas.create_line(self.x0, self.y0, self.xn[i], self.yn[i])

        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, outline='red')
        for i in range(len(self.xcc)):
            if self.y == -4:
                print("Пересечения нет")
            elif self.xcc[i] < self.xc[i]:
                canvas.create_oval(self.xcc[i] - 2, self.yc[i] - 2, self.xcc[i] + 2, self.yc[i] + 2, outline='blue')
            elif self.xc[i] < self.xcc[i]:
                canvas.create_oval(self.xc[i] - 2, self.yc[i] - 2, self.xc[i] + 2, self.yc[i] + 2, outline='blue')
            canvas.pack(fill=BOTH, expand=1)

    def check_cross(self):
        self.xn.sort()
        self.yn.sort()
        for i in range(len(self.yn)):
            c = self.yn[i] / self.xn[i]
            print(i + 1)
            D = (self.x + self.y * c) ** 2 - (1 + c ** 2) * (self.x ** 2 + self.y ** 2 - self.r ** 2)
            if D >= 0:
                self.xc[i] = ((self.x + self.y * c) + sqrt(D)) / ((1 + c ** 2))
                self.xcc[i] = ((self.x + self.y * c) - sqrt(D)) / ((1 + c ** 2))
                if self.xc[i] < self.xcc[i]:
                    self.xc[i] = ((self.x + self.y * c) + sqrt(D)) / ((1 + c ** 2))
                    self.xcc[i] = ((self.x + self.y * c) - sqrt(D)) / ((1 + c ** 2))
                    self.yc[i] = self.xc[i] * c
                    self.xcc[i] = self.xc[i]
                else:
                    self.yc[i] = self.xcc[i] * c
                    print(self.xcc[i], self.yc[i])
            else:
                print("Нет пересечения")
        return self.xcc, self.yc

def main():
    while 1:
        reload()
        root.update_idletasks()
        root.update()
        time.sleep(0.001)


def reload():
    global pic1
    pic1 = Draw()
    pic1.get_coord_start_line(0, 0)
    global y1
    x1 = 50
    h = 30
    coords = [0] * 2 * h
    i = 0
    j = 0

    while i < 2 * h:
        coords[i] = x1
        coords[i + 1] = y1 + j
        j += 1
        i += 2

    pic1.get_coord_line(coords)
    pic1.get_coord_circle(150, 70, 60)
    pic1.check_cross()
    pic1.initUI()


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas()
    canvas.pack()
    root.update()
    root.geometry("400x250+300+300")
    main()
