#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Calculator. Square, Cube and n root

from tkinter import Tk, Label, Entry, StringVar
import math as m
import tkinter as tk

root = tk.Tk()

#############################################################

#STEP 1: Create the canvas
canvas1 = tk.Canvas(root, width=300, height = 150)
canvas1.pack()

#STEP 2: Add the entry boxes
entry1 = tk.Entry(root)
canvas1.create_window(150, 20, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(150,40,window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(150,60,window=entry3)

# Create respective labels for entry 1,2,3
field1 = tk.Label(text=('Enter Number'))           
canvas1.create_window(40,20, window=field1)
field2 = tk.Label(text=('Decimal Places'))           
canvas1.create_window(40,40, window=field2)
field3 = tk.Label( text=('nth root?'))           
canvas1.create_window(40,60, window=field3)


# STEP 3: 
# Include a function, the square root function: text=float(x1)**0.5
def getSquareRoot():
    x1 = entry1.get()
    x3 = entry2.get()
    label1 = tk.Label(root, text=(round(float(x1)**(1/2),int(x3)))           )
    canvas1.create_window(75,90, window=label1)
    
# Cube root function
def getCubeRoot():
    x2 = entry1.get()
    x3 = entry2.get()
    label2 = tk.Label(root, text=(round(float(x2)**(1/3),int(x3))))
    canvas1.create_window(150,90,window=label2)
    
# n root function
def get_n_root():
    x1 = entry1.get()
    x3 = entry2.get()
    x4 = entry3.get()
    label3 = tk.Label(root, text=(round(float(x1)**(1/(float(x4))),int(x3))))
    canvas1.create_window(220,90,window=label3)
    
    
#STEP 4: Add the function buttons
button1 = tk.Button(text='Square Root', command=getSquareRoot)
canvas1.create_window(60, 120, window=button1)
button2 = tk.Button(text='Cube Root', command=getCubeRoot)
canvas1.create_window(150,120,window=button2)
button3 = tk.Button(text= 'nth Root', command=get_n_root)
canvas1.create_window(220,120,window=button3)

#######################################################################
root.mainloop()


# In[ ]:




