from turtle import Turtle, Screen, TK
import random
from tkinter import messagebox

  

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput("Choose the winning turtle", "Which turtle will win the race? Enter the color: ")

turtuls = ["t1", "t2", "t3","t4","t5", "t6"]
colors = ["red", "yellow", "orange", "blue", "green", "purple"]



def create_turtuls():
    x_position = -220
    y_position = -100
    for turtle_index in range(6):
        turtuls[turtle_index] = Turtle("turtle")
        turtuls[turtle_index].penup()
        turtuls[turtle_index].color(colors[turtle_index])
        turtuls[turtle_index].goto(x=x_position, y=y_position)
        y_position += 40


if user_bet:
    is_race_on = True


create_turtuls()
while is_race_on:
    
    for turtle in turtuls:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle.lower() == user_bet.lower():
                TK.messagebox.showinfo(title="Race Victory!:", message=f"You Win the Race! The winning turtle is {winning_turtle}")
            else:
                messagebox.showinfo(
    title="Race Results",
    message=f"Looks like {winning_turtle.upper()} just zoomed past you! Better luck next time!",
    icon='warning'  )
            
        rand_distant = random.randint(0, 10)
        turtle.forward(rand_distant)
        
        


screen.exitonclick()