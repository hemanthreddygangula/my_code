from turtle import Turtle, Screen
import random
import colors
timmy = Turtle()

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        timmy.forward(100)
        timmy.right(angle)


timmy.shape("turtle")

for i in range(3,11):
    timmy.color(random.choice(colors.colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()