from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self) :
        super().__init__()
        
        
        
    def createCar(self):
        print("Createing new car")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.setheading(180)
        
        
    def setcolor(self,clr):
        self.color(clr)
        
    def setPositon(self,position):
        self.goto(position) 
    
    def run(self,inc):
        self.forward(inc)    
        