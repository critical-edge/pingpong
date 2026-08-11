from turtle import Turtle
UPPER_BOUND =  250
LOWER_BOUND = -250
PADDLE_DEFAULT_SPEED = 15
class Paddle(Turtle):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x,self.y)
    def up(self):
        if self.ycor() <= UPPER_BOUND:
            self.sety(self.ycor()+ PADDLE_DEFAULT_SPEED)
    def down(self):
        if self.ycor() >= LOWER_BOUND:
            self.sety(self.ycor() - PADDLE_DEFAULT_SPEED)