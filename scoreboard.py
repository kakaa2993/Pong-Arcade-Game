from turtle import Turtle
FONT = ('Fantasy', 40, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.r_score, align='center',font=FONT)
        self.goto(100, 200)
        self.write(self.l_score, align='center',font=FONT)

    def l_add_point(self):
        self.l_score +=1
        self.update_score()

    def r_add_point(self):
        self.r_score += 1
        self.update_score()
