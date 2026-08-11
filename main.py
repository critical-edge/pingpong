from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
KEYS = {
    "up"  : False,
    "down": False,
        }
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
REFRESH_RATE = 0.02
UPPER_BOUND =  250
LOWER_BOUND = -250
GAME = True

screen = Screen()
screen.setup(width= SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
player_paddle = Paddle(-390,0)
computer_paddle = Paddle(380,0)
pong = Pong()

screen.listen()
screen.onkeypress(key="Up",   fun=lambda: KEYS.update(up = True))
screen.onkeyrelease(key="Up", fun=lambda: KEYS.update(up = False))
screen.onkeypress(key="Down", fun= lambda: KEYS.update(down = True))
screen.onkeyrelease(key="Down", fun=lambda: KEYS.update(down = False))
computer_direction = 'up'
while GAME:
    time.sleep(REFRESH_RATE)
    screen.update()
    if computer_paddle.ycor() >= UPPER_BOUND:
        computer_direction = "down"
    if computer_direction == "down":
        computer_paddle.down()
    if computer_paddle.ycor() <= LOWER_BOUND:
        computer_direction = "up"
    if computer_direction == "up":
        computer_paddle.up()

    if KEYS["up"]:
        player_paddle.up()

    if KEYS["down"]:
        player_paddle.down()
screen.exitonclick()