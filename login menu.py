import tkinter as tk 
from tkinter import messagebox
import time
import os

y=0
def register():
    frame= tk.Frame(root,bg='light green',bd=10)
    frame.place( relx=0.5,rely=0.1,relwidth=0.85, relheight=0.7, anchor='n')
    l1=tk.Label(frame,text="User name:" ,bg="white")
    l1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.2)

    l2=tk.Label(frame, text="Password:", bg="white")
    l2.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.2)

    entry2=tk.Entry(frame, bg="white")
    entry2.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.2)

    entry3=tk.Entry(frame,show="*", bg="white")
    entry3.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.2)
    def click():
    
        x=entry2.get()
        y=entry3.get()
        ok= x+y

        if len(x)>0 and len(y)>0 :
            
            f=open("ot.txt",'a+')
            f.write( "\n"+ok)
            f.close()
            messagebox.showinfo("..","you registered an account")
            
            frame.destroy()
            
            
    
        elif x=="":
            l3=tk.Label(root, text= 'Please insert username', font=20)
            l3.place( relx= 0.2, rely= 0.85, relwidth= 0.6, relheight=0.2)
        elif y=="":
            l3=tk.Label(root, text= 'please insert a password', font=20)
            l3.place( relx= 0.2, rely= 0.85, relwidth= 0.6, relheight=0.2)
        
        
    button2=tk.Button(frame, text='Register', bd=4,font=15, bg="red", command= click)
    button2.place( relx=0.25, rely=0.75, relwidth=0.5, relheight=0.2)
    
    


#Log in page       
def login():
    
    frame= tk.Frame(root,bg='pink',bd=10)
    frame.place( relx=0.5,rely=0.1,relwidth=0.85, relheight=0.7, anchor='n')
    l1=tk.Label(frame,text="User name:" ,bg="white")
    l1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.2)

    l2=tk.Label(frame, text="Password:", bg="white")
    l2.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.2)

    entry=tk.Entry(frame, bg="white")
    entry.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.2)

    entry1=tk.Entry(frame, bg="white",show='*')
    entry1.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.2)

    def clicked():
        x=entry.get()
        y=entry1.get()
        z=open("ot.txt","r")
        for t in z:
            if t== x+y:
                
                
                
                root.destroy()
                

        z.close()
        
        
        if x=="":
            l3=tk.Label(root, text= 'Please insert username', font=20)
            l3.place( relx= 0.2, rely= 0.85, relwidth= 0.6, relheight=0.2)
        elif y=="":
            l3=tk.Label(root, text= 'please insert a password', font=20)
            l3.place( relx= 0.2, rely= 0.85, relwidth= 0.6, relheight=0.2)
        else : 
            l3=tk.Label(root, text= 'User name not found', font=20)
            l3.place( relx= 0.2, rely= 0.85, relwidth= 0.6, relheight=0.2)
    button=tk.Button(frame, text='Log-In', bd=4,font=15, bg="red", command= clicked)
    button.place( relx=0.25, rely=0.75, relwidth=0.5, relheight=0.2)
    


root= tk.Tk()
canvas= tk.Canvas(root, height=300, width=300)
canvas.pack()
root.title(("Log In page"))


frame= tk.Frame(root,bg='#80c1ff',bd=10)
frame.place( relx=0.5,rely=0.1,relwidth=0.85, relheight=0.7, anchor='n')

Loginbtn=tk.Button(frame,text="Log in" ,bg="white",command= login)
Loginbtn.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

Registerbtn=tk.Button(frame, text="Register", bg="white",command=register)
Registerbtn.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.2)
root.mainloop()

