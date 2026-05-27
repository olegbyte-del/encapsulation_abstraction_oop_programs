# Fan Logic

class Fan: 
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=None, radius = 10.0, color="white", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = on
        
        @property # getter
        def get_speed(self):
            return self.__speed
        
        def get_radius(self):
            return self.__radius
        
        def get_color(self): 
            return self.__color
        
        def status_on(self):
            return self.__on
        
        @speed.setter
        def set_speed(self, speed): 
            self.__speed = speed
        
        
