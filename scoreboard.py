from turtle import Turtle
SCREEN_HEIGHT = 600

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x,y)
        self.update_scoreboard()
    def draw_margin(self):
        self.goto(0,300)
        self.pendown()
        for i in range(-300,301,5):
            if i%2 ==0:
                self.color("white")
            else:
                self.color("black")
            self.goto(0,i)
        self.penup()


    def increase_score(self):
        self.score +=1

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.score}", font=('Arial', 30, "bold"), align="center")
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", font=('Arial', 30, "bold"), align="center")
