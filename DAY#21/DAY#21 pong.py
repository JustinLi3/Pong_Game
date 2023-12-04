from turtle import Turtle,Screen 
from score import Score 
from paddle import Paddle 
from ball import Ball  
import time


screen = Screen() 
screen.bgcolor("black") 
screen.setup(800,600)   
scoreboard = Score() 
screen.title("Pong")  
screen.tracer(0)

rightpaddle = Paddle(350) 
leftpaddle = Paddle(-350) 
ball = Ball()  

dashedline = Turtle()  
dashedline.color("white") 
dashedline.pu()
dashedline.goto(0,300)  
dashedline.pd()
dashedline.setheading(270) 
dashedline.forward(600) 

screen.listen() 
screen.onkey(rightpaddle.gu,"Up")  
screen.onkey(rightpaddle.gd,"Down") 
screen.onkey(leftpaddle.gu,"w") 
screen.onkey(leftpaddle.gd,"s")
on = True 
while on:  
    if ball.xcor()>=380: 
        scoreboard.updateL()
    elif ball.xcor()<=-380:  
        scoreboard.updateR()
    time.sleep(ball.movespeed) 
    
    screen.update() 
    ball.move(rightpaddle,leftpaddle)

screen.exitonclick()