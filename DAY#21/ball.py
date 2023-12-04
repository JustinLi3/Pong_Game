from turtle import Turtle  

class Ball(Turtle): 
    def __init__(self):
        super().__init__("circle") 
        self.color("white")
        self.pu() 
        self.goto(0,0)  
        self.xmove = 10 
        self.ymove = 10 
        self.movespeed = 0.1
    def move(self, r,l):  
        self.detect(r,l)
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)  
        
     
    def detect(self, r, l): 
        if self.xcor()>=380 or self.xcor()<=-380: 
            self.goto(0,0)  
            self.xmove *=-1    
            self.movespeed = 0.1
        elif self.ycor()>=280 or self.ycor()<=-280:
            self.ymove *=-1 
        elif (self.xcor()>=330 or self.xcor()<=-330) and (self.distance(l)<=50 or self.distance(r)<=50):
            self.xmove *=-1  
            self.movespeed *=0.9
