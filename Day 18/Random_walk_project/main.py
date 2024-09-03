import random
from turtle import Turtle, Screen



t = Turtle()
t.pen(fillcolor="black", pencolor="red", pensize=10)
moves = {
    "forward":t.forward,
    "back":t.back
}
direc = {
    "right":t.right,
    "left":t.left
}
m = ["forward", "back"]
d = ["right", "left"]
Colors = [
    "red", "blue", "green", "purple", "orange", "pink", "brown", "black",
    "cyan", "magenta", "gold", "coral", "turquoise", "lime", "indigo", "violet", "maroon"
]
t.shape("turtle")
# t.width(6)
for move in range(100):
    # random_color = random.choice(Colors)
    # t.color(random_color)

    random_move = random.choice(m)
    random_dir = random.choice(d)

    moves[random_move](20)
    direc[random_dir](90)









# t.back(200)

screen = Screen()
screen.exitonclick()
# 0.0
