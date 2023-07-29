from turtle import Turtle, Screen
timmy = Turtle()

for _ in range(20):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()