# Create paddle at a position; make it move along y_coor
DISTANCE = 60

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white')

        # TODO paddle_left: width = 20, length = 100; x_pos = 350, y_pos = 0
        self.shapesize(stretch_wid=5, stretch_len=1)
            # stretch_wid 为垂直于其朝向的宽度拉伸因子，stretch_len 为平行于其朝向的长度拉伸因子
        self.penup()
        self.speed(0)  # fastest没有额外动画效果
        self.setposition(x,y) # 海龟移动到一个绝对坐标。


    def move_paddle_up(self):  ##turtle.forward（）只能沿x轴移动
        old_x = self.xcor()
        new_y = self.ycor() + DISTANCE
        self.goto(old_x,new_y)
    def move_paddle_down(self):
        old_x = self.xcor()
        new_y = self.ycor() - DISTANCE
        self.goto(old_x, new_y)


