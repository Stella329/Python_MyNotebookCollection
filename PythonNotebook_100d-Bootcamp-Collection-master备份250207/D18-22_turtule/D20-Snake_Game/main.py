#knowledge:
## class inheritant
## CONSTANTS
## slicing
## screen.tracer(); screen.refresh(); time.sleep(); while loop to control the screen animation

# KNOWLEDGE_snake:
##Note: here it doesn't use class inheritance to create the class
## python Constants: don't like the hard-coded piece of text inside the body of a program
## create snake class: call the method in __init__
## slice

# KNOW_food
#AIM: create food body; make it move; define the collision
## inherit Turtle() into Food: food is a turtle object
## turtle.distance(): use it to detect the collision of snake.head with food
    ## define in main game control: in main.py
## food position: random coor and refresh
    ## posistion: 不能在screen边缘

# KNOW_scoreboard
## AIM: mainly do the writings on Screen
## fun: turtle.write() + turtle.clear()

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Have Fun in My Snake Game!') ## window title

screen.tracer(0)
# turtle.tracer(n=None, delay=None)启用/禁用海龟动画并设置刷新图形的延迟时间。如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。
# 重要!!!screen.tracer(0): turn off the animation. But then you need to manually update the screen and refresh it every single time，同时结合while-loop做到每次手动刷新


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.listen()


game_on = True
while game_on:
    screen.update() #body动一次，screen刷新一次
    time.sleep(0.09) #pause the loop for a short time during each iteration

    snake.move()

    #detect collision: snake.head vs. food
    #turtle.distance(x, y=None) 返回从海龟位置到由 (x,y)，适量或另一海龟对应位置的单位距离
    ## head: 20x20; food: 10x10; distance:15=20/2+10/2
    if snake.head.distance(food) < 15.5:
        food.position_refresh()
        scoreboard.score_add()
        snake.extend_snake()

    # detect collision: snake.head vs. wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 265 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    # detect collision: snake.head vs. tail
    elif snake.tail_collision():
        game_on = False
        scoreboard.game_over()


screen.exitonclick()