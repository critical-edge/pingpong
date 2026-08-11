from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
#GLOBAL VARIABLES:
KEYS = {
    "up"  : False,
    "down": False,
        }
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
REFRESH_RATE = 0.02
PADDLE_UPPER_BOUND =  250
PADDLE_LOWER_BOUND = -250
PONG_UPPER_BOUND = 290
PONG_LOWER_BOUND = -290

GAME = True


#SCREEN SETUP
screen = Screen()
screen.setup(width= SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


#GAME OBJECTS SETUP:
player_paddle = Paddle(-390,0)
computer_paddle = Paddle(380,0)
pong = Pong()


#SCREEN LISTENERS:
screen.listen()
screen.onkeypress(key="Up",   fun=lambda: KEYS.update(up = True))
screen.onkeyrelease(key="Up", fun=lambda: KEYS.update(up = False))
screen.onkeypress(key="Down", fun= lambda: KEYS.update(down = True))
screen.onkeyrelease(key="Down", fun=lambda: KEYS.update(down = False))



#GAME LOOP:
computer_direction = 'up'
while GAME:
    #UPDATER
    time.sleep(REFRESH_RATE)
    screen.update()

    #COMPUTER MOVEMENT LOGIC
    if computer_paddle.ycor() >= PADDLE_UPPER_BOUND:
        computer_direction = "down"
    if computer_direction == "down":
        computer_paddle.down()
    if computer_paddle.ycor() <= PADDLE_LOWER_BOUND:
        computer_direction = "up"
    if computer_direction == "up":
        computer_paddle.up()

    #PONG LOGIC
    if pong.xcor() >= 390 or pong.xcor() <= -390:
        print("GAME OVER")
        break
    #UPPER AND LOWER boundry COLLISION
    if pong.ycor() >= PONG_UPPER_BOUND or pong.ycor() <= PONG_LOWER_BOUND:
        pong.speed_vector[1] = -pong.speed_vector[1]

    #PONG COLLIDES WITH PADDLE
    if round(pong.xcor())<= player_paddle.xcor()+15 and round(pong.ycor()) in range(round(player_paddle.ycor())-55,round(player_paddle.ycor())+55) :
        pong.speed_vector[0] = -pong.speed_vector[0]
    if computer_paddle.distance(pong) <= 52.20:
        pong.speed_vector[0] = -pong.speed_vector[0]

    pong.move()

    #PLAYER MOVEMENT LOGIC
    if KEYS["up"]:
        player_paddle.up()

    if KEYS["down"]:
        player_paddle.down()
screen.exitonclick()