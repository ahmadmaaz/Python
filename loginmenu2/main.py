import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog,QWidget, QMainWindow,QMessageBox
from PyQt5.QtGui import QPixmap
import os
real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)
print(dir_path)
print(real_path)
 


class Loginscreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(Loginscreen, self).__init__()
        loadUi(dir_path+"/loginmenu.ui", self)
        qpixmap = QPixmap(dir_path+"/photos/nature2.jpg")
        self.picture.setPixmap(qpixmap)
        qpixmap = QPixmap(dir_path+"/photos/account.png")
        self.account_picture.setPixmap(qpixmap)
        qpixmap = QPixmap(dir_path+"/photos/password.png")
        self.password_picture.setPixmap(qpixmap)
        self.password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gotosignup.clicked.connect(self.signup)
        self.login.clicked.connect(self.Login)

    def Login(self):
        user1=self.account_login.text()
        password1= self.password_login.text()
        z=open(dir_path+"/photos/ot.txt","r+")
        for t in z:
            y=t.strip()
            if y== user1+password1:
                self.account_login.clear()
                self.password_login.clear()
                self.login_error.setText("")
                QMessageBox.about(self, "DONE", "Logged in ;)")
                widget.setCurrentIndex(widget.currentIndex()-1)
            else  :
                self.login_error.setText("             Account Not found")
        z.close()
        if len(password1)==0 and len(user1)==0:
            self.login_error.setText("Please input all fields")
        elif len(password1)==0:
            self.login_error.setText("Please insert a password")
        
        elif len(user1)==0:
            self.login_error.setText("Please insert an Username")
        
    def signup(self):
        Signup=Signupscreen()
        
        widget.addWidget(Signup)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Signupscreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(Signupscreen, self).__init__()
        loadUi(dir_path+"/signup.ui", self)
        qpixmap = QPixmap(dir_path+"/photos/nature2.jpg")
        self.picture.setPixmap(qpixmap)
        qpixmap = QPixmap(dir_path+"/photos/account.png")
        self.account_picture.setPixmap(qpixmap)
        qpixmap = QPixmap(dir_path+"/photos/password.png")
        self.password_picture.setPixmap(qpixmap)
        self.backtologin.clicked.connect(self.back)
        self.signup.clicked.connect(self.createaccount)
        self.password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    def createaccount(self):
        user= self.account_signup.text()
        password=self.password_signup.text()
        if len(password)==0 and len(user)==0:
            self.signup_error.setText("Please input all fields")
        elif len(user)==0:
            self.signup_error.setText("Please insert an Username")
        elif len(password)==0:
            self.signup_error.setText("Please insert a password")
        elif len(password)<4:
            self.password_signup.clear()
            self.signup_error.setText("This password is weak!.")
        elif len(password)>0 and len(user)>0:
            f=open(dir_path+"/photos/ot.txt",'a+')
            f.write( user+password+ "\n")
            f.close()
            self.password_signup.clear()
            self.account_signup.clear()
            self.signup_error.setText("")
            QMessageBox.about(self, "DONE", "You registered an account -back to main menu ;)")
            widget.setCurrentIndex(widget.currentIndex()-1)

app = QApplication(sys.argv)
Login = Loginscreen()
widget=QtWidgets.QStackedWidget()
widget.addWidget(Login)
widget.setFixedHeight(500)
widget.setFixedWidth(700)
widget.show()
sys.exit(app.exec_())


