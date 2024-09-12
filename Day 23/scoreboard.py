from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto((-270,260))
        self.update_score()
        
        
    def increase_level(self):
        self.level += 1    
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level-{self.level}",False, align="left",font=FONT)  
        
    def game_over(self):
        # self.clear()
        self.goto((0,0))
        self.write(f"Game Over",False, align="center",font=FONT)     
