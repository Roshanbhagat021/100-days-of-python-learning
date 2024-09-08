from turtle import Turtle
import random




class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed(0)
        self.new_food() 
        
        
    def new_food(self):
        random_x_position_cod = random.randint(-280, 280)
        random_y_position_cod = random.randint(-280, 280)
        self.goto(x=random_x_position_cod, y=random_y_position_cod) 
        
          