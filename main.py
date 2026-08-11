from turtle import Screen

import paddle
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
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
scoreboard = Scoreboard(0,0)
scoreboard.clear()
scoreboard.draw_margin()

player_scoreboard = Scoreboard(-200,250)
computer_scoreboard = Scoreboard(200,250)



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
player_direction =""
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
        if player_direction == "down":
            pong.speed_vector[1] = -2 * (paddle.PADDLE_DEFAULT_SPEED) - pong.speed_vector[1]
        elif player_direction == "up":
            pong.speed_vector[1] = 2 * (paddle.PADDLE_DEFAULT_SPEED) - pong.speed_vector[1]
        else:
            pass


        player_scoreboard.increase_score()
        player_scoreboard.update_scoreboard()
    if round(pong.xcor())>= computer_paddle.xcor()-15 and round(pong.ycor()) in range(round(computer_paddle.ycor())-55,round(computer_paddle.ycor())+55):
        pong.speed_vector[0] = -pong.speed_vector[0]

        if round(pong.xcor()) <= player_paddle.xcor() + 15 and round(pong.ycor()) in range(
                round(player_paddle.ycor()) - 55, round(player_paddle.ycor()) + 55):
            pong.speed_vector[0] = -pong.speed_vector[0]
            if player_direction == "down":
                pong.speed_vector[1] = -2 * (paddle.PADDLE_DEFAULT_SPEED) - pong.speed_vector[1]
            elif player_direction == "up":
                pong.speed_vector[1] = 2 * (paddle.PADDLE_DEFAULT_SPEED) - pong.speed_vector[1]
            else:
                pass
        computer_scoreboard.increase_score()
        computer_scoreboard.update_scoreboard()
    pong.move()

    # PLAYER MOVEMENT LOGIC
    if KEYS["up"]:
        player_paddle.up()
        player_direction = "up"
    if KEYS["down"]:
        player_paddle.down()
        player_direction ="down"
    player_direction = ""
screen.exitonclick()