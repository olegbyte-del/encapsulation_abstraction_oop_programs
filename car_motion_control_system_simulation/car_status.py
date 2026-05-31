# Car Status
class Car:
    
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
        
    def brake(self):
        self.speed -= 5
        
    def speed(self, new_speed): 
        if new_speed < 0:
            print("speed cannot be negative!")
        else:
            pass

    def speed(self):
        return self.__speed
    
    def make(self):
        return self.__make
    
    def year_model(self):
        return self.__year_model
        
    
    

        

