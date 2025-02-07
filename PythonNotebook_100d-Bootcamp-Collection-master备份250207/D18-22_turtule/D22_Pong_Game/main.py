#KNOWLEDGE:
## screen.update() + time.sleep(): control the ball_move speed.


import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
from scoreboard import Scoreboard

screen = Screen()
screen.title("Have Fun in Pong!")  ##窗口标题栏文本
screen.setup(width = 800, height = 600)
    # screen.setup (width=200, height=200, startx=0, starty=0); not the turtle.screensize()
screen.bgcolor('black')
screen.tracer(0)

# TODO: paddle
paddle_1 = Paddle(350,0)
paddle_2 = Paddle(-350,0)

screen.onkey(fun=paddle_1.move_paddle_up, key='Up')
screen.onkey(fun=paddle_1.move_paddle_down, key='Down')

screen.onkey(fun=paddle_2.move_paddle_up, key='W')
screen.onkey(fun=paddle_2.move_paddle_down, key='S')
screen.listen()

# TODO: ball
ball = Ball()

# TODO: scoreboard
scoreboard = Scoreboard()
score_a = Score(x=-350/2, y=280-20)
score_b = Score(x=350/2, y=280-20)


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.timesleep)
    ## it also controls the ball_move speed; timesleep=0.1，attribute is in ball.py

    ball.ball_move()

    # TODO collide with boundary（上下）: bounce back
    # bounce logic: 只需要判定上下，因为左右为paddle判定
    # 判定逻辑：最好写在main.py中，ball.py只写动作（method）不带逻辑
    if abs(ball.ycor()) >= 300 - 20:
        ball.bounce_y()

    # TODO collide with paddle（左右）: bounce back
    #ball.distant(paddle): ONLY distance betw ball center to paddle center
    #solution同时满足：ball_y=paddle所在x时； ball.distance(paddle) <= 50 (from center to top)
    # 判定逻辑最好写在main.py，不然就得带入变量：def collide_with_paddle(self, paddle_1, paddle_2)
    if abs(ball.xcor()) >= 350-20:
        if ball.distance(paddle_1) <= 50 or ball.distance(paddle_2) <= 50: ## distance = 20*根号5
            ball.bounce_x()

    # TODO miss the ball: score
    if abs(ball.xcor()) >= 410:

        if ball.xcor() >= 410:
            score_a.add_score()
        elif ball.xcor() <= -410:
            score_b.add_score()

        ball.reset()
        ball.ball_move()
        time.sleep(1)


screen.exitonclick()