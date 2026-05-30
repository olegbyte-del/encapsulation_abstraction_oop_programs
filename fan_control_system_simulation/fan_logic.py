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
    def speed(self):
        return self.__speed
        
    @speed.setter
    def speed(self, new_speed): 
        if new_speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = new_speed
        
    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, radius): 
        self.__radius = radius
        
    @property
    def color(self): 
        return self.__color

    @color.setter
    def color(self, color): 
        self.__color = color
        
    @property
    def on(self):
        return self.__on
        
    @on.setter
    def on(self, on):
        self.__on = on
            
