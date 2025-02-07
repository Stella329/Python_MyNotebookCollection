from turtle import Turtle, Screen
import random
screen = Screen()

# todo: set up the window size so I can use the coordinate
## screen.setup (width=200, height=200, startx=0, starty=0) -- sets window to 200x200 pixels, in upper left of screen
screen.setup(width=500, height =400)

# todo: the pop-up window to ask user to bet on a turtle
## turtle.textinput(title, prompt) , 返回输入的字符串
user_bet = (screen.textinput(title='Welcome to Turtle Race!', prompt='Bet on the color of a turtle who will win.')).lower()

# todo: set 6 turtles with different colors
color = ['blue', 'green', 'purple', 'orange','pink',user_bet]
turtle_bank =[] ##重要！！

num = 0
for item in color:
    turtle = Turtle(shape = 'turtle') ## shape
    turtle.color(color[num])
    # todo: set the turtle at the left-hand of screen, and line them up
    ## turtle.goto(x, y=None); current canvas size: 500x400
    turtle.penup()
    turtle.goto(x=-230, y=-150+num*60) ## 归位左边，line up
    num+=1
    turtle_bank.append(turtle) ##重要！！：can't change the instance name directly. 用于收集每个独立turtle instance


# todo: Game begin; set random forward steps for each turtle
game_on = True
while game_on:

    for turtle in turtle_bank: ##重要！！
        # todo 设置每只turtle:forward每一步的大小为random; ## turtle.forward(distance)
        distance = random.randint(0, 30)
        turtle.forward(distance)

        # todo 判断输赢,头先到x=400; turtle size = 40x40; head=(20,0)
        ## turtle.xcor() 返回海龟的 x 坐标。
        if turtle.xcor()>= 250-20:
            winning_color = turtle.pencolor() ## pencolor vs. color (fillcolor)
            game_on = False
            if winning_color == user_bet:
                print('You win!!')
            else:
                print('You lose.')
            print(f'The winning turtle is the Turtle {winning_color.capitalize()}!!')

screen.exitonclick()