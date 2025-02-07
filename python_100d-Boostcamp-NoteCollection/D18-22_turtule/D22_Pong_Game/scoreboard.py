from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,300)
        self.setheading(270)

        for num in range(600):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()



