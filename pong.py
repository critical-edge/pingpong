from turtle import Turtle
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 0.5,stretch_len=0.5)
        self.penup()