from turtle import Turtle, Screen
import random

t = Turtle()
# tom = Turtle()
t.shape("turtle")

t.color("indianred1")


# Challange one
# t.left(90)
# def create_square():
#     for _ in range(4):
#         t.forward(100)
#         t.right(90)


# create_square()



# Challange two

# for _ in range(15):
#     t.speed(1)
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]


def draw_shapes(no_of_sides):
    angle = 360/no_of_sides
    for _ in range(no_of_sides):
        t.forward(100)
        t.right(angle)


for shape_size_n in range(3,11):
    draw_shapes(shape_size_n)


screen = Screen()
screen.exitonclick()