# import colorgram
import random
import turtle
color_list = [(200, 10, 35), (247, 236, 37), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185)]
turtle.colormode(255)
t = turtle.Turtle()


# rgb_colors = []
# colors = colorgram.extract("dot_painting.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
t.penup()
t.hideturtle()

t.speed(0)
def draw_painting():
    x = -200
    for _ in range(10):
        # setting the start point of turtle
        t.goto(-200, x)
        for _ in range(10):

            t.pendown()
            t.dot(15,random.choice(color_list))
            t.penup()
            t.forward(40)
        x += 40



draw_painting()


turtle.mainloop()





