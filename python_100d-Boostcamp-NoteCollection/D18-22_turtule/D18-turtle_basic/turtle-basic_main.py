#SET UP TURTLE AND SCREEN
## ted = turtle_module.Turtle() 
## ted.color('navy')
## ted.shape('turtle')

## screen = Screen() --obj
## screen.exitonclick()

import random
import turtle as turtle_module
from turtle import Turtle,Screen

# TODO 0 create turtle object
ted = turtle_module.Turtle() 
#ted.color('navy')
ted.shape('turtle')



# TODO 5 random color
## todo method 1: using 1.0 scope
def rand_color():
    r = random.random() ## float from 0-1
    g = random.random()
    b = random.random()
    ted.pencolor(r,g,b) ##it is a tuple

## todo method 2: using 255 scope -- change the module not the object
turtle.colormode(255)
def rand_color():
    R = random.randint(0,255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    ted.color(R, G, B)




# TODO 1 turtle motion
for n in range(4):
    ted.forward(200)
    ted.right(90)

# TODO 2 draw a dashed line
for n in range(10):
    ted.forward(10)
    ted.penup()
    ted.forward(10)
    ted.pendown()




# TODO 3 draw from triangle to decagon in sequence; in random color; length of side=100
##todo from triangle to decagon, using a function
def draw_shape(corner):
    rand_color()
    angle = 360/corner
    for step in range(corner): #num of corner = num of side
        ted.forward(100)
        ted.right(angle)

corner = 3
while corner < 10:
    draw_shape(corner)
    corner += 1



# TODO 4 random walk: in faster speed, and in thicker line
ted.width(2)  ## or: use ted.pendsize()
ted.speed(0) ## can use both num and str: 'fastest'(0); 'normal'(6)

# TODO method 1

for num in range(100):
    walk = random.randint(0,1)
    if walk == 0: # turn left
        rand_color()
        ted.left(90)
        ted.forward(40)
    else:
        rand_color()
        ted.right(90)
        ted.forward(40)


## TODO method 2: ted.setheading()
        
direction = [0,90,180,270]   ## for setheading
for num in range(100):
    rand_color()
    ted.setheading(random.choice(direction))
    ted.forward(40)




# TODO 5 make a spirograph: circle + many circles
def draw_circle(angle):
    '''turtle.circle(radius, extent=None, steps=None)
    Parameters:
    radius – a number
    extent – a number (or None)
    steps – an integer (or None)'''

    rand_color()
    ted.circle(100)
    ted.setheading(angle)

angle = 0
while angle < 360:
    draw_circle(angle)
    angle += 5


# TODO 0 set up the window
screen = Screen() #obj
screen.exitonclick()
