from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.display_score()
        
    def inc_score(self):
        self.clear()
        self.score += 1 
        self.display_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)     
        
    def display_score(self):
         self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)   
         
         
        
        