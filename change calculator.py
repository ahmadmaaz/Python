import tkinter as tk

root= tk.Tk()
canvas= tk.Canvas(root, height=300, width=300)
canvas.pack()
root.title(("change Calculator"))

quarter=0.25
txt=""
l1=tk.Label(root,text="customer", font=40 ,bg="white", bd=6)
l1.place(relx=0.05, rely=0.1, relwidth=0.3, relheight=0.1)

l2=tk.Label(root, text="cashier",font=40, bg="white",bd=6)
l2.place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.1)

e1=tk.Entry(root)
e1.place(relx=0.45, rely=0.1, relwidth=0.3, relheight=0.1)

e2=tk.Entry(root)
e2.place(relx=0.45, rely=0.4, relwidth=0.3, relheight=0.1)
def click():
    panda= p % quarters  
    x=e1.get()
    y=e2.get()
    p=int(x)-int(y)
    if p % quarter == 0:
        l=p/0.25
        l1=tk.Label(root,text= str(l)+ " quarters"+ "  0 nickle"+ "  0 dime"+" 0 penny" ,bg="white", bd=6)
        l1.place(relx=0.0, rely=0.6, relwidth=0.8, relheight=0.1)
    
        


button=tk.Button(root, text='Change return', bd=4,font=15, bg="red",command= click)
button.place( relx=0.25, rely=0.75, relwidth=0.5, relheight=0.2)
root.mainloop()