
import random 
import time
import tkinter as tk
from tkinter import messagebox




root= tk.Tk()
canvas= tk.Canvas(root, height=400, width=500)
canvas.pack()
root.title(("Number generator"))

faultnmb=0
nmb=random.randint(0,50)

    

def ext():
    messagebox.showinfo("Good Bye my lovva","Sad  ;(")
    quit()

def contnue():
    
    label1.destroy()
    label2.destroy()
    label3.destroy()
    lbl=tk.Label(root,text=" guess the number from 1-50!", bg='orange',font=8)
    lbl.place(relx=0.2,rely=0.03,relwidth=0.55,relheight=0.1)
    entry=tk.Entry(root)
    entry.place(relx=0.55, rely=0.20, relwidth=0.08, relheight=0.07)
    
    
   
    def check():
        
        
        inpt=int(entry.get())
        entry.delete(0,'end')
        global faultnmb
        if inpt!=nmb:
            fault=tk.Label(root,text='Wrong !!!', font=5, bg='pink')
            fault.place(relx=0.2, rely=0.3, relwidth=0.6,relheight=0.05)
            faultnmb+=1
            fault1=tk.Label(root,text='Failure attemps: '+ str(faultnmb), font=5, bg='pink')
            fault1.place(relx=0.65, rely=0.2, relwidth=0.3,relheight=0.07)
            print (faultnmb)
        
        if faultnmb==2:
            if nmb%2==0:
                hint=tk.Label(root,text='Hint: the number is divisible by 2', font=5, bg='yellow')
                hint.place(relx=0.1, rely=0.4, relwidth=0.8,relheight=0.2)
            if nmb%3==0:
                hint=tk.Label(root,text='Hint: the number is divisible by 3', font=10, bg='yelllow')
                hint.place(relx=0.1, rely=0.4, relwidth=0.8,relheight=0.2)
            if nmb%5==0:
                hint=tk.Label(root,text='Hint: the number is divisible by 5', font=10, bg='yellow')
                hint.place(relx=0.1, rely=0.4, relwidth=0.8,relheight=0.2)
            if nmb%7==0:
                hint=tk.Label(root,text='Hint: the number is divisible by 7', font=10, bg='yellow')
                hint.place(relx=0.1, rely=0.4, relwidth=0.8,relheight=0.2)
            else :
                hint=tk.Label(root,text='Hint: the number is not divisible by 2/3/5/7', font=10, bg='yellow')
                hint.place(relx=0.1, rely=0.4, relwidth=0.8,relheight=0.2)
        

        if faultnmb==4:
            nmb1=random.randint(5,15)
            nmb2=random.randint(5,15)
            plus= nmb+nmb2
            if plus>50:
                plus=50
            minus = nmb-nmb1
            if minus<0:
                minus=0
            finalhint= "Hint!!: the new range of the number is between "+ str(minus) +" and " + str(plus)
            fhint=tk.Label(root,text=finalhint, font=7, bg='yellow')
            
            fhint.place(relx=0, rely=0.4, relwidth=1,relheight=0.2)
        
        if faultnmb==6:
            nmb4=random.randint(1,5)
            nmb3=random.randint(1,5)
            plus1= nmb+nmb4
            if plus1>50:
                plus1=50
            minus = nmb-nmb3
            if minus<0:
                minus=0
            finalhint= "Final Hint!!: the new range of the number is between "+ str(minus) +" and " + str(plus1)
            fhint=tk.Label(root,text=finalhint, font=7, bg='yellow')
            
            fhint.place(relx=0, rely=0.4, relwidth=1,relheight=0.2)
        
        
        if faultnmb==8:
            fault=tk.Label(root,text='Maybe you will get it correct next time ;( \n \n \n \n \n      The Number was '+ str(nmb),font = ("bold",20), fg = "white" , bg='Red')
            fault.place(relx=0, rely=0, relwidth=1,relheight=0.6)
            def restartp():
                fault.destroy()
                restart.destroy()

                global faultnmb
                faultnmb=0
                hin=tk.Label(root)
                hin.place(relx=0, rely=0.4, relwidth=1,relheight=0.2)
                fault1=tk.Label(root,text='Failure attemps: '+ str(faultnmb), font=5, bg='pink')
                fault1.place(relx=0.65, rely=0.2, relwidth=0.3,relheight=0.07)
                global nmb
                nmb=random.randrange(0,50)

            restart=tk.Button(root,text="Restart!",command= restartp)
            restart.place(relx=0.4,rely=0.25,relwidth=0.3,relheight=0.1)
            
        if inpt==nmb:
            
            fault=tk.Label(root,text='WoWW correct boiii!! Good Job ;) \n \n \n \n \n', font=("bold",20),fg="white", bg='green')
            fault.place(relx=0, rely=0, relwidth=1,relheight=0.6)
            def restartp():
                fault.destroy()
                restart.destroy()
                global faultnmb
                faultnmb=0
                hin=tk.Label(root)
                hin.place(relx=0, rely=0.4, relwidth=1,relheight=0.2)
                fault1=tk.Label(root,text='Failure attemps: '+ str(faultnmb), font=5, bg='pink')
                fault1.place(relx=0.65, rely=0.2, relwidth=0.3,relheight=0.07)
                global nmb
                nmb=random.randrange(0,50)
                
            restart=tk.Button(root,text="Restart!",command= restartp)
            restart.place(relx=0.4,rely=0.25,relwidth=0.3,relheight=0.1)
    button=tk.Button(root,text='Check',bd=5,bg='pink',command=  check)
    button.place(relx=0.25, rely=0.20, relwidth=0.15,relheight=0.07)
    




# Labels in first frame    
label1=tk.Label(root,text="Lets play A game. It is a number guesser game  !!",font=9,bg='#80c1ff',bd=10)
label1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
label2=tk.Label(root,text="Rules:",font=9,bd=10)
label2.place(relx=0.1,rely=0.35,relwidth=0.2,relheight=0.1)
label3=tk.Label(root,text=" We will generate a number a number from 0 to 50 \n Your failure attempts will increase every time u get the number wrong \n  Every time u get the number wrong, a hint will pop up \n If you reach 8 attempts the game will end",bd=10)
label3.place(relx=0.3,rely=0.35,relwidth=0.7,relheight=0.2)


# Buttons 
playbutton= tk.Button(root,text="Play!!", font=5,bd=10,command= contnue)
playbutton.place(relx=0.25, rely=0.65, relwidth=0.2, relheight=0.2)
extbutton= tk.Button(root,text="Exit!!", font=5,bd=10,command= ext)
extbutton.place(relx=0.55, rely=0.65, relwidth=0.2, relheight=0.2)


root.mainloop()










