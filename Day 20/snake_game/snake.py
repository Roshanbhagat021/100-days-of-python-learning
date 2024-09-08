from turtle import Turtle, Screen
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) :
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]
        self.paused = False

        
    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)
     
    
    def extend(self):
        self.add_segment(self.segment[-1].position())
           
            
    def add_segment(self,position):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(position)
            self.segment.append(new_turtle)
        
           
               
    def move(self):
        if not self.paused:
            for seg in range(len(self.segment)-1, 0, -1):
                new_x_position = self.segment[seg-1].xcor()
                new_y_position = self.segment[seg-1].ycor()
                self.segment[seg].goto(new_x_position,new_y_position)          
            self.head.forward(MOVE_DISTANCE)
    
    
    def stop(self):
        self.paused = not self.paused
            
        
    def up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)  
        
               
    def down(self):
        if int(self.head.heading() ) != UP:
            self.head.setheading(DOWN) 
        
    def left(self):
        if int(self.head.heading() ) != RIGHT:
            self.head.setheading(LEFT)     
        
    def right(self):
        if int(self.head.heading() ) != LEFT:  
            self.head.setheading(RIGHT)     