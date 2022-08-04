from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        new_position = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_position)

    def down(self):
        new_position = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_position)


