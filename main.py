import random
from turtle import Screen
import turtle as t

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("magenta")
tim.shapesize(2)
tim.speed(4)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


# colours = ["medium blue", "sienna", "lawn green", "red", "magenta", "gold", "medium turquoise", "black"]
directions = [0, 90, 180, 270]
tim.pensize(15)

# generate a random walk with named colours
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

"""
#draw a square
for _ in range(4):
     tim.forward(100)
     tim.right(90)
"""

"""
#draw a dashed line
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
"""

"""
# drawing different shapes from triangle to decagon with random colours for each shape
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
"""

screen = Screen()
screen.exitonclick()
