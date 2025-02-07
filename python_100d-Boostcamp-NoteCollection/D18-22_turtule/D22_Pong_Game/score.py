from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')

        self.score = 0
        self.goto(x, y)
        self.write(arg=f'Score={self.score}', align='center', font=('Arial', 18, 'normal'))


    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score={self.score}', align='center', font=('Arial', 18, 'normal'))
