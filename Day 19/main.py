# Drawing with turtle
import turtle


tim = turtle.Turtle()



turtle.colormode(255)


def move():
    tim.forward(10)


screen = turtle.Screen()

screen.onkeypress(move,"f")




screen.listen()


screen.exitonclick()