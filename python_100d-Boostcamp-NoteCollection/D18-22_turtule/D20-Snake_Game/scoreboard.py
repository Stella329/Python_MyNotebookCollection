X = 0
Y = 270
ALIGN = 'center'
FONT = ('Arial', 18, 'normal')

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=X,y=Y)
        self.score = 0

        # turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
        self.write(arg=f'Score: {self.score}', align=ALIGN, font=FONT)


    def score_add(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGN, font=FONT)


    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg='GAME OVER', align='center', font=FONT)

