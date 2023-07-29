import turtle
import random
import colors

timmy = turtle.Turtle()
directions = [0,90,180,270,360]
turtle.colormode(255)


for _ in range(100):
    timmy.speed(10)
    timmy.color(colors.random_color())
    timmy.pensize(3)
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen = turtle.Screen()
screen.exitonclick()