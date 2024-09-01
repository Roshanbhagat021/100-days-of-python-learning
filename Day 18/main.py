from turtle import Turtle, Screen

t = Turtle()
tom = Turtle()
t.shape("turtle")

t.color("indianred1")

t.left(90)
def create_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)


create_square()












screen = Screen()
screen.exitonclick()