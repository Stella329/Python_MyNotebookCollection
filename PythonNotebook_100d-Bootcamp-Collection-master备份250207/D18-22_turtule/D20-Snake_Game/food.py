from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.shapesize(0.7,0.7)
        ## original size: 20x20; change into 10x10
        ## turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)返回或设置画笔的属性 x/y 拉伸因子和/或轮廓
        self.penup()
        self.speed('fastest')

        self.position_refresh()

    def position_refresh(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280, 260)
        ##screen size: 600x600 -> x=(-300,300); food = 10X10
        self.goto(rand_x,rand_y)
