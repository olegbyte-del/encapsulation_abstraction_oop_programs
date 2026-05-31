# Car Status
class Car:
    
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
        
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
        
    def speed(self, new_speed): 
        if new_speed < 0:
            print("speed cannot be negative!")
        else:
            self.__speed = new_speed

    def get_speed(self):
        return self.__speed
    
    def get_make(self):
        return self.__make
    
    def get_year_model(self):
        return self.__year_model
        
    
    

        

