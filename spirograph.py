from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_list = (r, g, b)
    return timmy.color(color_list)

def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        random_color()
        timmy.circle(100)
        timmy.left(size_of_gap)

spirograph(5)

screen.exitonclick()
