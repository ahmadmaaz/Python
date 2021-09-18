import tkinter as tk 
import random
root= tk.Tk()
canvas= tk.Canvas(root, height=300, width=300)
canvas.pack()
root.title(("Click counter lets Go"))
number=0
x= random.randrange(2,10)
if x==2:
        y="blue"
elif x==3:
        y='black'
elif x==4:
        y='pink'
elif x==5:
        y='brown'
elif x==6:
        y='yellow'
elif x==7:
        y='light blue'
elif x==8:
        y='light green'
elif x==9:
        y='black'
elif x==10:
        y='purple'
f2=tk.Frame(root,bg=y,bd=10)
f2.place(relx=0,rely=0, relwidth=3, relheight=3)



def click():
    global number
    number+=1
    l1=tk.Label(root,text=number,font="200",bd=4)
    l1.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.25)

b1=tk.Button(root,text="click counter",bd=8,font=15, bg="red", command= click )
b1.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

    
root.mainloop()
