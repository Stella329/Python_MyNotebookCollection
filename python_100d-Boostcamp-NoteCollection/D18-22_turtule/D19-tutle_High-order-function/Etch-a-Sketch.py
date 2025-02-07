from turtle import Turtle, Screen
ted = Turtle()

screen = Screen()
def move_forward():
    ted.forward(20)
def move_backward():
    ted.backward(20)

#Turn slowly and draw the line
def turn_left():
    new_heading = ted.heading() + 10 ##当前朝向+10
    ted.setheading(new_heading)
def turn_right():
    new_heading = ted.heading() - 10  ## 0 = East
    ted.setheading(new_heading)

#todo: clean the screen, and reset the turtle
def clear():
    ted.clear() #clean the drawings
    ted.penup()
    ted.home() #get turtle back to the origin
    ted.pendown()

#todo: screen.onkey(function=, key="Up")
#todo: screen.listen()
screen.onkey(fun=move_forward, key='W')
screen.onkey(fun=move_backward, key='S')
screen.onkey(fun=turn_right, key='D')
screen.onkey(fun=turn_left, key='A')
screen.onkey(clear, 'C')
screen.listen()

screen.exitonclick()
