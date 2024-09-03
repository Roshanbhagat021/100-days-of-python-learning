import random
from turtle import Turtle, Screen



t = Turtle()


Colors = [
    "red", "blue", "green", "purple", "orange", "pink", "brown", "black",
    "cyan", "magenta", "gold", "coral", "turquoise", "lime", "indigo", "violet", "maroon"
]
angels_to_move = [0,90,270,180]
t.shape("turtle")
t.speed(0)
t.width(6)
for move in range(200):
    random_color = random.choice(Colors)
    t.color(random_color)
    t.setheading(random.choice(angels_to_move))
    t.forward(20)




screen = Screen()
screen.exitonclick()
# 0.0
