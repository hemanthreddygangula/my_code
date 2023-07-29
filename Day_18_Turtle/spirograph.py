import turtle
import colors

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed(0)
timmy.pensize(1)
def spirograph(gap):
    for _ in range(int(360/gap)):
        timmy.color(colors.random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

spirograph(5)
s = turtle.Screen()
s.exitonclick()