from turtle import  Turtle, Screen

graphy = Turtle()
graphy.shape("turtle")
graphy.color("#75D200")

my_screen = Screen()
my_screen.title("Welcome to the turtle zoo!")
graphy.left(90)
graphy.forward(100)
graphy.right(90)
print(graphy.pos())
graphy.setposition(70, 100)
graphy.right(90)
graphy.forward(48)
graphy.right(90)
graphy.forward(65)
graphy.left(135)
graphy.setposition(70, 0)


my_screen.exitonclick()

