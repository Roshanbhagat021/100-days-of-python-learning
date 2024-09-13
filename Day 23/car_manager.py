from turtle import Turtle, Screen
from car import Car
import random

car_image_path = "C:/100-days-of-python-learning/Day 23/images/car.gif"

screen = Screen()
screen.register_shape(car_image_path)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape(car_image_path)
            new_car.shapesize(1,1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(280,random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  
          
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT    
            
            
    
       