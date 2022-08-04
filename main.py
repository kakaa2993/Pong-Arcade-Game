from turtle import Turtle, Screen
from paddle import Paddle
import time
X_POSITION = 350
Y_POSITION = 0


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(20)

r_paddle = Paddle(X_POSITION, Y_POSITION)
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

# refresh the screen
game_is_on = True
while game_is_on:
    screen.update()



# time.sleep(0.1)
screen.exitonclick()