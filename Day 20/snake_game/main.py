from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import winsound



screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating Snake body
snake = Snake()  
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.stop, "space")

# Move snake
game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1) 
    snake.move()
    
    if snake.head.distance(food) < 15:
        winsound.PlaySound('C:\\100-days-of-python-learning\\Day 20\\snake_game\\sound\\music_food.wav', winsound.SND_ASYNC)
        food.new_food()
        snake.extend()
        scoreboard.inc_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        winsound.PlaySound('C:\\100-days-of-python-learning\\Day 20\\snake_game\\sound\\music_gameover.wav', winsound.SND_ASYNC)
        game_is_on = False    
        scoreboard.game_over()
    
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            winsound.PlaySound('C:\\100-days-of-python-learning\\Day 20\\snake_game\\sound\\music_gameover.wav', winsound.SND_ASYNC)
            game_is_on = False    
            scoreboard.game_over()
        
        

      
     
        

          




screen.exitonclick()
 