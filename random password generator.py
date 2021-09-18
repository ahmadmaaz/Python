import string
import random

import tkinter as tk 
from tkinter import Label, messagebox
import time
import os

root= tk.Tk()
canvas= tk.Canvas(root, height=300, width=300)
canvas.pack()
root.title(("Password generator! "))

l3=tk.Label(root, text= 'insert the length of password')
l3.place( relx= 0.1, rely= 0, relwidth= 0.6, relheight=0.1)
entry=tk.Entry(root, bg="white")
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)

def click():
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    symbol= string.punctuation
    symbol1= "!@#_-?"
    digit= string.digits
    x=entry.get()
    all= lower +upper + symbol1+ digit
    woah= random.sample(all,int(x))
    password= "".join(woah)
    Label=tk.Label(frame,text=password, bg="white")
    Label.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.2)





frame= tk.Frame(root,bg='#80c1ff',bd=10)
frame.place( relx=0.5,rely=0.1,relwidth=0.85, relheight=0.7, anchor='n')

Loginbtn=tk.Button(frame,text="generate password" ,bg="white",command= click)
Loginbtn.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

Label=tk.Label(frame, bg="white")
Label.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.2)
root.mainloop()