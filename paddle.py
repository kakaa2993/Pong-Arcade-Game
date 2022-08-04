from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, posision):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto()

    def up(self):
        new_position = self.ycor() + 20
        self.goto(x=X_POSITION, y=new_position)

    def down(self):
        new_position = self.ycor() - 20
        self.goto(x=X_POSITION, y=new_position)
