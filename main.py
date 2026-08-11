from turtle import Screen
from paddle import Paddle
import time
KEYS = {
    "up"  : False,
    "down": False,
        }
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
REFRESH_RATE = 0.02
GAME = True

screen = Screen()
screen.setup(width= SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
pad = Paddle(-390,0)

screen.listen()
screen.onkeypress(key="Up",   fun=lambda: KEYS.update(up = True))
screen.onkeyrelease(key="Up", fun=lambda: KEYS.update(up = False))
screen.onkeypress(key="Down", fun= lambda: KEYS.update(down = True))
screen.onkeyrelease(key="Down", fun=lambda: KEYS.update(down = False))

while GAME:
    time.sleep(REFRESH_RATE)
    screen.update()
    if KEYS["up"]:
        pad.up()

    if KEYS["down"]:
        pad.down()
screen.exitonclick()