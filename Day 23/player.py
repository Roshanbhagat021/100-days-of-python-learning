from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
car_image_path = "C:/100-days-of-python-learning/Day 23/images/turtle.gif"

screen = Screen()
screen.register_shape(car_image_path)

class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape(car_image_path)
        self.color("yellow")
        self.penup()
        self.setheading(90)
        self.go_to_start()
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)    
       
    def is_at_finishLine(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False    
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)   
    
