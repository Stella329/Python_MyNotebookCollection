DISTANCE = 10

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # ball_position: 20x20; (x=0,y=0)
        self.color('white')
        self.shape('circle')
        self.penup()
        self.home()  # 将海龟送回起点（这适用于海龟消失在屏幕之外的情况）
        self.delta_x = DISTANCE
        self.delta_y = DISTANCE

        self.timesleep = 0.1


    def ball_move (self):
        new_x = self.xcor() + self.delta_x
        new_y = self.ycor() + self.delta_y
        self.goto(new_x,new_y)
        #不能用self.setheading() + self.forward()：a.不好控制value; b.因为forward需要iterate, setheading不需要；但本section需要放到main.py中loop

    def bounce_y(self):
        self.delta_y *= -1

    # MY METHOD没啥必要: 区分了撞击方向。但ball.heading()不起作用；x（vs.old_x)不变而y变，即为反弹
    #     head_to = self.heading()
    #     if abs(self.ycor()) >= 300 - 20: ##上下
    #         self.delta_y *= -1
    #         if 90 < head_to < 270: ##方向：会向左反弹，x变小；反之x正常变大
    #             self.delta_x *= -1

    def bounce_x(self):
        self.delta_x *= -1
        self.timesleep * 0.9
        ## todo 每次ball抨击paddle,ball_speed提高一点

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        ##todo 谁输了，下局球往对方区域move (reverse the x_coor)
        self.timesleep=0.1
        ##todo 每局结束 ball_speed: reset




