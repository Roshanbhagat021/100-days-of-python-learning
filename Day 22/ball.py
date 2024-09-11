from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self) :
        self.dir = [10,-10]
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1
        self.shapesize(1,1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
        
    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def check_collision_up_down_wall(self):
        if self.ycor() > 285 or self.ycor() < -285:
            return True
            
            
    def bounce_y(self):
        self.y_move *=-1
        # self.move()  
     
    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *=0.9
        # self.move()  
     
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()
     
    
                  