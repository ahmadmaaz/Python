
import time

name= input("input your name: ")
age= input("input your age( in yrs): ")
months= int(age)*12
days= int(months)*30
print(name+"'s"+ " age is "+ str(age) +" years or "+ str(months)+" months or "+ str(days)+ " days or "+str(days*24)+ " hours")

time.sleep(5)