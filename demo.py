import turtle 
import time
import os 
import random
import tkinter as tk


wn1= turtle.Screen()
turtle.title("Game")
wn1.bgcolor("white")
wn1.setup(width=800, height=600)
wn1.tracer(0)
time.sleep(2)
#pen1
pen1= turtle.Turtle()
pen1.speed(0)
pen1.color("black")

pen1.hideturtle()
pen1.goto(0,220)
pen1.write(" Please     Wait  ", align="center", font=("Courier", 44, "normal"))
pen1.goto(0,-50)
pen1.write(" #######  ", align="center", font=("Courier", 44, "normal"))
pen1.goto(0,-90)
pen1.write(" Loading  ", align="center", font=("Courier", 44, "normal"))
pen1.clear()
wn1.listen()
time.sleep(5)


wn= turtle.Screen()

wn= turtle.Screen()
turtle.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B 
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#ball 
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")


ball.color("white")
ball.goto(0,0)
ball.penup()

ball.dx= 1
ball.dy= 1

#pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 24, "normal"))


#score
score_a=0
score_b=0


#function
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    
#keyboard binding
wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main
while True:
        wn.update()

        print ("sheesh")
    
    
        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border checking 
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            ball.color("white")
        
        if ball.ycor() <-290:
            ball.sety(-290)
            ball.dy *= -1
            ball.color("white")
        
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            time.sleep(0.5)
            score_a +=1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1

            time.sleep(0.5)
            score_b +=1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


        # paddle and ball collisions 
        if ball.xcor() > 340 and  ball.xcor() <350   and(ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -50) :
            ball.setx(340)
            ball.dx +=1
            ball.dx *= -0.8
            ball.color("blue")

        if ball.xcor() < -340 and  ball.xcor() >-350   and(ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -50) :
            ball.setx(-340)
            ball.dx +=1
            ball.dx *= -0.8
            ball.color("red")





        #boarders for paddles
        if paddle_b.ycor()> 260:
            paddle_b.sety(260)

        if paddle_b.ycor()< -250:
            paddle_b.sety(-250)

        if paddle_a.ycor()> 260:
            paddle_a.sety(260)

        if paddle_a.ycor()< -250:
            paddle_a.sety(-250)





        #sheeshh
        
        if ball.ycor()> paddle_a.ycor() +100 and ball.xcor()<-100:
            
        
            p=paddle_a.ycor()
            
            x =ball.ycor()
            paddle_a.sety(x-30)
        
                
        
        if ball.ycor() <paddle_a.ycor() -100 and ball.xcor()<-100:
        
            k=paddle_a.ycor()

            
            x1 =ball.ycor()
            paddle_a.sety(x1+30)
        
                
        
    
        ok= random.randrange(0,1000)
        if ok==1:
            ball.shape("circle")
        if ok== 20:
            ball.shape("square")
        if ok==50:
            ball.shape("triangle")
        if ok==80:
            ball.shape("turtle")
        
        if ok==890:
            ball.shapesize(1,1,1)
        if ok==435:
            ball.shapesize()
            

    

        screeen= random.randrange(0,10000)
        if screeen==50:
            wn.bgcolor("cyan")
        if screeen==790:
            wn.bgcolor("yellow")
        if screeen==890:
            wn.bgcolor("black")
        if screeen==2890:
            wn.bgcolor("black")
        if screeen==1890:
            wn.bgcolor("black")
        if screeen==5734:
            wn.bgcolor("grey")
    
        
    

        if score_b > 1 :
            paddle_b.shapesize(4,1,2)
        if score_a > 1 :
            paddle_a.shapesize(4,1,2)

    

    
            
            
        

        #ball speed
    


    

            
            
        
    
            

            



        
















