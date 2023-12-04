from turtle import Turtle, Screen
screen = Screen() 
screen.tracer(0) 
class Score(Turtle):
    def __init__(self): 
        super().__init__() 
        self.ls = 0 
        self.rs = 0 
        self.color("white") 
        self.pu() 
        self.print()  
    def updateL(self): 
        self.ls+=1  
        self.print()
    def updateR(self):
        self.rs+=1 
        self.print()
    def print(self):  
        self.clear() 
        self.goto(-100,200) 
        self.write(self.ls, move = False,align = "center" ,font = ("Courier",80,"normal"))  
        self.goto(100,200) 
        self.write(self.rs, move = False,align = "center",font = ("Courier",80,"normal"))   
        self.hideturtle()
 