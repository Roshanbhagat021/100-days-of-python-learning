import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import winsound
background_path = "C:/100-days-of-python-learning/Day 23/images/background_image1.gif"

screen = Screen()
screen.title("Trutle Road Crossing Game ")
screen.register_shape(background_path)
print(screen.getshapes())
screen.bgpic(background_path)
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
score = Scoreboard()

winsound.PlaySound("C:/100-days-of-python-learning/Day 23/sound/game_music.wav", winsound.SND_ASYNC)

screen.onkeypress(player.go_up, "Up") 
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            winsound.PlaySound("C:/100-days-of-python-learning/Day 23/sound/game_over.wav", winsound.SND_ASYNC)
            score.game_over()
            game_is_on = False
    
    if player.is_at_finishLine():
        player.go_to_start()
        winsound.PlaySound("C:/100-days-of-python-learning/Day 23/sound/short-success-sound-glockenspiel-treasure-video-game-6346.wav", winsound.SND_ASYNC)
        
        car_manager.level_up()
        score.increase_level()
        winsound.PlaySound("C:/100-days-of-python-learning/Day 23/sound/game_music.wav", winsound.SND_ASYNC)
        
screen.exitonclick()