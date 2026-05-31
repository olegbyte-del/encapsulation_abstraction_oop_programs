# Car Status
class Car:
    """Car class"""
    
    def __init__(self, year_model, make):
        """initialize the attributes for car class"""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        """increase 5 speed of the vehicle"""
        self.__speed += 5
        
    def brake(self):
        """decrease 5 speed of the vehicle"""
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
        
    def speed(self, new_speed):
        """Prevents the speed from becoming negative"""
        if new_speed < 0:
            print("speed cannot be negative!")
        else:
            self.__speed = new_speed

    def get_speed(self):
        """read speed"""
        return self.__speed
    
    def get_make(self):
        """read make"""
        return self.__make
    
    def get_year_model(self):
        """read year_model"""
        return self.__year_model
        
    
    

        

