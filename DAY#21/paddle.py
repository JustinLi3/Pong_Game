from turtle import Turtle 

class Paddle(Turtle): 
    def __init__(self, place):
        super().__init__("square")  
        self.color("white")
        self.pu()
        self.goto(place,0)   
        self.shapesize(stretch_wid=5, stretch_len = 1)  
    def gu(self):  
        self.goto(self.xcor(),self.ycor()+20)
    def gd(self):  
        self.goto(self.xcor(),self.ycor()-20)