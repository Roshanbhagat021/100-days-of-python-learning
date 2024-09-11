from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,cordinates) :
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(cordinates)
        
        
    def paddle_position(self,x,y):
        self.goto(x,y)    

        
    def move_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)  
            # print(self.ycor())
          
    def move_down(self):
        if  self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)    
            # print("down" , self.ycor())
        
        
        
        
        
        
        
        
        
        
