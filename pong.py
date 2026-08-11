from turtle import Turtle
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 0.5,stretch_len=0.5)
        self.penup()
        self.speed_vector = [-6,8]
    def move(self):
        self.sety(self.ycor() + self.speed_vector[1])
        self.setx(self.xcor() + self.speed_vector[0])
