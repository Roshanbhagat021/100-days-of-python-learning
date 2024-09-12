from car import Car
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_POSITIONS = [230,240,250,260,270]


class CarManager(Car):
    def __init__(self):
          super().__init__()
          
    def multiplecars(self):
        y_position = -230
        for i in range(10):
            self.createCar()
            self.setposition((random.choice(STARTING_X_POSITIONS),y_position))   
            
    
       