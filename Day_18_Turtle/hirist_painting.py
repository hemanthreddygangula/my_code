import colorgram
colors = colorgram.extract('Day_18_Turtle\painting.jpeg',20)
rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgb_colors.append((r,g,b))


import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)

dot_count = 100
for i in range(1, dot_count+1):
    timmy.dot(25, random.choice(rgb_colors))
    timmy.fd(50)
    if i%10==0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()