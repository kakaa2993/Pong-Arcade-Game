from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_movement_distance = 10
        self.y_movement_distance = 10
        self.move_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.x_movement_distance
        y_position = self.ycor() + self.y_movement_distance
        self.goto(x=x_position, y=y_position)

    def y_bounce(self):
        self.y_movement_distance *= -1

    def x_bounce(self):
        self.x_movement_distance *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.move_speed = 0.1
        self.goto(x=0, y=0)
        self.move()
        self.x_bounce()


