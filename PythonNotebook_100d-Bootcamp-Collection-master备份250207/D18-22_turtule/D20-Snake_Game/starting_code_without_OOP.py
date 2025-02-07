import time
from turtle import Turtle, Screen
screen = Screen()

# TODO 1 set up the screen
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Have Fun in My Snake Game!') ## window title
screen.tracer(0)
    #todo 3-1 turtle.tracer(n=None, delay=None)启用/禁用海龟动画并设置刷新图形的延迟时间。如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。
    #todo 3-1 turtle.update()执行一次 TurtleScreen 刷新。在禁用追踪时使用 -- work like old TV CRT monitor



# TODO 2 create snake body: 3 turtles in line using Coordinate, 1 turtle=20x20 (20 pixels)
    ## 后续要用坐标移动body,因此创建时也采用Coor
start_coor = [(0, 0), (-20, 0), (-40, 0)] #body起始坐标,并排向左 Tuple

seg_list =[] #turtle item + position coordinate
for position in start_coor:
    ## create snake body (turtle item)
    new_seg = Turtle('square')
    new_seg.color('white')

    ## !!!position: can't change turtle's start position; can only move the turtle there using turtle.goto()
    new_seg.penup()
    new_seg.goto(position)  # turtle.goto(x=, y=)
    seg_list.append(new_seg)
    ##print(seg_list): <turtle.Turtle object at 0x0000019CB8492E70>

# TODO 3 move the snake body: while loop+ screen+ body movement order
game_on = True
while game_on:
    screen.update() #should-be: body动一次，screen刷新一次
    time.sleep(0.1)
        # screen.delay() slows down the animation.
        # time.sleep() sets the delay between two code instructions.

    # todo 3-2 body move order
        ## METHOD 1: (seg_list中：3-> 2 -> 1 in reverse order) 3占2的位，2占1的位，1负责主带方向
        ## using range(start, end, step) to create reverse
    for num in range(len(seg_list)-1, 0, -1): ##!!range loop doesn't include the end--head不动
        new_x = seg_list[num-1].xcor() #body_2 position
        new_y = seg_list[num-1].ycor()
            ## 返回坐标位置：turtle.xcor()
        
        seg_list[num].goto(new_x,new_y) #move body_3 (to body_2) --此时列表已变
            ## move the body segment

    # ## METHOD 2: if not in reverse order 自己想用正序
    # for num in range(0, len(seg_list)-1, 1):
    #     new_x = seg_list[num].xcor() #body 1
    #     new_y = seg_list[num].ycor()
    #     seg_list[num+1].goto(new_x,new_y) #move body2

    seg_list[0].forward(20)  ## head: 前进20


screen.exitonclick()