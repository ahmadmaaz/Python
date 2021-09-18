import random
import smtplib
# to get the emails in db
emails=[]
f=open("universityaccountdb.txt",'r')
for line in f:
    if not '/' in line:
        continue
    indx=line.index('/')
    emails.append(line[:indx])
f.close()
uporin= input('Welcome to the university \n Press S to sign up or L to login to your account!')
if uporin.lower()=='s':
    email=input('Welcome to the Sign up Page! \n Please Enter Your email address: ')
    while not('@' in email and '.com' in email):
        email=input('Please input a valid email address: ')
    while  email in emails:
        email=input('This email is taken! Please insert another email: ') 
    password=input(' Please input your Password: ')
    while len(password)<6:
        password=input('Your password is weak \n Please input your password')
    key= str(random.randint(1,9))+str(random.randint(1,9)) +str(random.randint(1,9)) + str(random.randint(1,9)) 
    
    with smtplib.SMTP("smtp.outlook.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("ahmd_maaz05@outlook.com","DC8E6A353MMZ")

        subject = ' hey'
        msg= f'Subject: {subject} \n\n {key}'
        
        smtp.sendmail("ahmd_maaz05@outlook.com",email,msg)
    keyconfirmation= input('We have sent you a code to your email please insert it here(email verificaton!): ')
    while keyconfirmation!=key:
        keyconfirmation= input('We have sent you a code to your email please insert it here(email verificaton!): ')
    if keyconfirmation==key:
        input('You have created an account!')
    

    z= open("universityaccountdb.txt",'a+')
    z.write('\n' + email + '/'+ password)
    z.close()

if uporin.lower()=='l':
    email=input(' Welcome To the University \n |||||||||||||||||||||||||||||||||||||||||||||||||| \n Please insert your email address: ')
    while not ('@' in email and '.com' in email):
        email= input('please insert a valid format for an email!: ')
    while not email in emails:
        email=input('Email Not found! Please insert a valid email: ')
    password=input('Please insert the password: ')
    f=open("universityaccountdb.txt",'r')
    for line in f:
        if not '/' in line:
            continue
        indx=line.index('/')
    
        if email==line[:indx]:
            passcheck=line[indx+1:]
    while passcheck!=password:
        password=input('Incorrect password!: ')
    input('Login Successfully \n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ')


    



      

