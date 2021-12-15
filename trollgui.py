import tkinter as tk
import random
import time
root= tk.Tk()
canvas= tk.Canvas(root, height=300, width=300)
canvas.pack()
root.title(("Troll Page"))

def clickno():
    x_new= random.randint(0,35)/100
    y_new= random.randint(50,80)/100
    print (x_new, y_new)
    Nobtn.place(relx=x_new, rely=y_new, relwidth=0.25, relheight=0.2)

def clickyes():
    txt=tk.Label(root,text="I knew it ;)",font=15,bd=10)
    txt.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.2)



txt=tk.Label(root,text="Are u stupid?!",font=15,bd=10)
txt.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.2)

Nobtn=tk.Button(canvas, text="No", bg="white", command=clickno,bd=5)
Nobtn.place(relx=0.12, rely=0.7, relwidth=0.25, relheight=0.2)


Yesbtn=tk.Button(canvas, text="Yes", bg="white" ,command=clickyes,bd=5)
Yesbtn.place(relx=0.62, rely=0.7, relwidth=0.25, relheight=0.2)
root.mainloop()