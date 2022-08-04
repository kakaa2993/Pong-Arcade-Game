from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

X_POSITION = 350
Y_POSITION = 0


# Set up the screen
screen = Screen()
screen.tracer(20)
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")
scoreboard = Scoreboard()
r_paddle = Paddle((X_POSITION, Y_POSITION))
l_paddle = Paddle((-X_POSITION, Y_POSITION))
ball = Ball()
screen.listen()
screen.onkey(key="Up", fun=l_paddle.up)
screen.onkey(key="Down", fun=l_paddle.down)
screen.onkey(key="s", fun=r_paddle.up)
screen.onkey(key="w", fun=r_paddle.down)

# refresh the screen
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect the collision with paddles
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320) or (ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.x_bounce()

    # Detect the ball is missed with the l paddle
    if ball.xcor() > 380:
        scoreboard.l_add_point()
        ball.restart()

    # detect the ball is missed with the r paddle
    if ball.xcor() < -380:
        scoreboard.r_add_point()
        ball.restart()


screen.exitonclick()