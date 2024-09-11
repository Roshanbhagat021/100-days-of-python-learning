from turtle import  Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong Game!!")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
ball = Ball()
scoreboard = Scoreboard()

 
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,'s')  
  
game_is_on = True
while game_is_on:
   screen.update()
   time.sleep(ball.move_speed)
   ball.move()
   if ball.check_collision_up_down_wall():
      ball.bounce_y()
      
   #Detect Collision with paddel
   if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
      ball.bounce_x()
      
   #Detect Right paddel missed the ball
   if ball.xcor() > 380:
      ball.reset_position() 
      scoreboard.l_point()
        
   #Detect left paddel missed the ball
   if ball.xcor() < -380:
      ball.reset_position()   
      scoreboard.r_point()


screen.exitonclick()
