import tkinter as tk
import random
import time
from tkinter import messagebox
root=tk.Tk()
canvas=tk.Canvas(root,height=300,width=300)
canvas.pack()
yourscore=0
cpuscore=0


def win():
    msg=messagebox.showinfo("Woaaaaah","    Nice choice ;) u won!  ")
    global yourscore
    yourscore= yourscore +1
    Score1=tk.Label(root,text=yourscore, bg='cyan',bd='10')
    Score1.place(relx=0,rely=0,relheight=0.15,relwidth=0.4)
    Score2=tk.Label(root,text=cpuscore, bg='red',bd='10')
    Score2.place(relx=0.6,rely=0,relheight=0.15,relwidth=0.4)
def lose():
    msg=messagebox.showinfo("NOOOOOOOOOOOOOOOO","Next time u will come stronger ;(")
    
    global cpuscore
    cpuscore+=  1 
    Score1=tk.Label(root,text=yourscore, bg='cyan',bd='10')
    Score1.place(relx=0,rely=0,relheight=0.15,relwidth=0.4)
    Score2=tk.Label(root,text=cpuscore, bg='red',bd='10')
    Score2.place(relx=0.6,rely=0,relheight=0.15,relwidth=0.4)
    
def draw():
    msg=messagebox.showinfo("ZZZZZZZZZZZZZZ","  Tie!!!  ")
    Score1=tk.Label(root,text=yourscore, bg='cyan',bd='10')
    Score1.place(relx=0,rely=0,relheight=0.15,relwidth=0.4)
    Score2=tk.Label(root,text=cpuscore, bg='red',bd='10')
    Score2.place(relx=0.6,rely=0,relheight=0.15,relwidth=0.4)    
    
def scissorsclick():
    yourchoice= 3
    botchoice= random.randint(1,3)
    if botchoice ==2:
        win()
    elif botchoice == 3:
        draw()
    elif botchoice==1 :
        lose() 

def paperclick():
    yourchoice= 2
    botchoice= random.randint(1,3)
    if botchoice ==2:
        draw()
    elif botchoice == 3:
        lose()
    elif botchoice==1 :
        win()

def rockclick():
    yourchoice= 1
    botchoice= random.randint(1,3)
    if botchoice ==2:
        lose()
    elif botchoice == 3:
        win()
    elif botchoice==1 :
        draw()

# pictures
rockpic = tk.PhotoImage(file = "wp55266567.png")
labelrock = tk.Label( root, image = rockpic)
labelrock.place(relx = 0, rely = 0,relwidth=0.37,relheight=0.65)

paperpic = tk.PhotoImage(file = "paper.png")
labelpaper = tk.Label( root, image = paperpic)
labelpaper.place(relx = 0.4, rely = 0,relwidth=0.2,relheight=0.65)

scissorspic = tk.PhotoImage(file = "scissors.png")
labelscissors = tk.Label( root, image = scissorspic)
labelscissors.place(relx = 0.7, rely = 0,relwidth=0.2,relheight=0.65)
#buttons
rock=tk.Button(root,text='Rock',bg='grey',bd="5",command=rockclick)
rock.place(relwidth=0.2, relheight=0.1,relx=0.1,rely=0.5)

paper=tk.Button(root,text='Paper',bg='white',bd="5",command=paperclick)
paper.place(relwidth=0.2, relheight=0.1,relx=0.4,rely=0.5)

scissors=tk.Button(root,text='Scissors',bg='yellow',bd="5",command=scissorsclick)
scissors.place(relwidth=0.2, relheight=0.1,relx=0.7,rely=0.5)

tk.mainloop()