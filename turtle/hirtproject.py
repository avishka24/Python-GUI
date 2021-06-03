# import colorgram
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# rgb_colors = []
# colors = colorgram.extract('haert.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
turtle.colormode(255)
tim.hideturtle()
color_list = [(254, 254, 254), (252, 201, 214), (239, 161, 182), (230, 142, 167), (250, 252, 251), (244, 244, 246)]
tim.speed("fastest")
tim.penup()
tim.setheading(200)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()