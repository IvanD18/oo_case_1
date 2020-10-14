#!/usr/bin/env python
# coding: utf-8

# In[106]:


from tkinter import Tk, Canvas, Frame, BOTH
import random


# In[93]:


class ex(Frame):
    def __init__(self):
        pass


# In[94]:


import tkinter as tk
from math import sqrt


# In[127]:


class Draw(tk.Frame):
 
    def __init__(self, *args):#x0, y0, x1, y1, x, y, r):
        
        self.xn = []
        self.yn = []
        self.xc = []
        self.xcc = []
        self.yc = []
        
        
        super().__init__()
        #super().__init__()
        #self.initUI()
    
    def get_coord_start_line(self, x0, y0): 
        self.x0 = x0
        self.y0 = y0
        #return self.x0, self.y0#, self.x1, self.y1
    
    def print_coord_start_line(self): 
        print("self.x0, self.y0 ", self.x0, self.y0)#, self.x1, self.y1)
        print("self.xn, self.yn ", self.xn, self.yn)
        print("self.x, self.y, self.r ", self.x, self.y, self.r)
        
    def get_coord_line(self, *args): #x1, y1, 
        #self.x1 = x1
        #self.y1 = y1
        
        if len(args) > 2:        
            
            #self.xn.append(args[0:-1:2])
            #self.yn.append(args[1::2])
            
            i = 0
            while i < len(args):
                self.xc.append(-4)
                self.xcc.append(-4)
                self.yc.append(-4)
                self.xn.append(500)
                self.yn.append(500*args[i+1]/args[i])
                i += 2
            
        else:
            #print(self.xn)
            self.xn.append(args[0])
            self.yn.append(args[1])
        
    def get_coord_circle(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        #return self.x, self.y, self.r
        
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)
    
        for i in range(len(self.xn)):
            canvas.create_line(self.x0, self.y0, self.xn[i], self.yn[i])
           
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, outline='red')
        for i in range(len(self.xcc)):
            if self.y == -4:
                print("Пересечения нет")
            elif self.xcc[i]<self.xc[i]:
                canvas.create_oval(self.xcc[i]-2, self.yc[i]-2, self.xcc[i]+2, self.yc[i]+2, outline='blue')
            elif self.xc[i]<self.xcc[i]:
                canvas.create_oval(self.xc[i]-2, self.yc[i]-2, self.xc[i]+2, self.yc[i]+2, outline='blue')
            canvas.pack(fill=BOTH, expand=1)
    
    def check_cross(self):
        self.xn.sort()
        self.yn.sort()
        for i in range(len(self.yn)):
            c = self.yn[i]/self.xn[i]
            print(i+1)
            D = (self.x+self.y*c)**2-(1+c**2)*(self.x**2+self.y**2-self.r**2)
            if D>=0:
                self.xc[i] = ((self.x+self.y*c) + sqrt(D))/((1+c**2))
                self.xcc[i] = ((self.x+self.y*c) - sqrt(D))/((1+c**2))
                if self.xc[i]<self.xcc[i]:
                    self.yc[i] = self.xc[i] * c
                    self.xcc[i]=self.xc[i]
                else :
                    self.yc[i] = self.xcc[i] * c
                    print(self.xcc[i], self.yc[i])
            else:
                print("Нет пересечения")
        return self.xcc, self.yc
            
        
       

# In[128]:


def main():
    root = Tk()
    #pic1 = Draw()
    #parametrs = [0, 0, 1, 1, 2, 2, 2]
    #a = [i for i in parametrs]
    pic1 = Draw()
    pic1.get_coord_start_line(0, 0) #15, 15
    pic1.get_coord_line(random.randint(0,200), random.randint(0,200), random.randint(0,200), random.randint(0,200), random.randint(0,200), random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200),random.randint(0,200))
    pic1.get_coord_circle(150,70, 60)
    
    #pic1.print_coord_start_line()
    #print(pic1.check_cross())
    pic1.check_cross()
    pic1.initUI()
    
    
    root.geometry("400x250+300+300")
    root.mainloop()


# In[129]:


if __name__ == '__main__':
    main()
