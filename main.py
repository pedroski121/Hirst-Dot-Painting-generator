
# paint a painting with 10 X 10 rows of spots
# each of the dots should be about 20 in size and paced by about 50 paces


from turtle import Turtle, Screen, color, xcor
import turtle
from colordata import color_data
import random


turtle.colormode(255)
screen = Screen()
tortoise = Turtle()
tortoise.hideturtle()
tortoise.shape('triangle')
tortoise.speed(5)
screen_width = screen.window_width()
screen_height = screen.window_height()
tortoise.penup()
tortoise.backward(screen_width/2 - 50)
tortoise.setheading(270)
tortoise.forward(screen_height/2 - 50)
tortoise.setheading(0)

tortoise.pendown()
xcordinate = tortoise.xcor()
ycordinate = tortoise.ycor()

divisor = 0
ycor_add = 0

for i in range(0, 100):
    divisor += 1
    tortoise.color(random.choice(color_data))
    tortoise.pensize(20)
    tortoise.forward(2)
    tortoise.penup()
    tortoise.forward(50)
    tortoise.pendown()
    if divisor % 10 == 0:
        ycor_add += 50
        tortoise.penup()

        tortoise.setposition((xcordinate, ycordinate+ycor_add))

        tortoise.pendown()


screen.exitonclick()
