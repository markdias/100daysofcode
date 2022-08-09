from turtle import Screen, Turtle
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Turtle()

def draw_net():
    net.penup()
    net.shape("square")
    net.color("red")
    net.shapesize(stretch_wid=100, stretch_len=1)
    net.goto(0,300)

def pause_game():
    global is_paused
    if is_paused:
        is_paused = False 
    else:
        is_paused = True
    return is_paused

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(pause_game, "p")

is_paused = True
game_is_on = True

draw_net()
while game_is_on:

    screen.update()
    if is_paused:
        ball.move()
    else:
        pass

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == scoreboard.WINNING_SCORE or scoreboard.r_score == scoreboard.WINNING_SCORE:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()