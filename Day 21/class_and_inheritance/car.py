class Car_basic_prototype():
    def __init__(self) :
        self.wheele = 4
        self.fuel = "petrol"
        self.self_driving = False
        
    
    def move(self):
        print("car moved 20ms ahead") 
    
    def start(self):
        print("Car started")       
        
 
class Tesla_car_model(Car_basic_prototype):
        def __init__(self):
            super().__init__()
            self.start()
            
        # def move(self):
            #    print("Moving at speed of 100kmh") 
            
            
car2 = Tesla_car_model()
car2.move()
         