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
        
    @speed.setter
    def set_speed(self, new_speed): 
        if new_speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = new_speed
        
    @property
    def get_radius(self):
        return self.__radius
        
    @radius.setter
    def set_radius(self, radius): 
        self.__radius = radius
        
    @property
    def get_color(self): 
        return self.__color

    @color.setter
    def set_color(self, color): 
        self.__color = color
        
    @property
    def status_on(self):
        return self.__on
        
    @on.setter
    def set_status_on(self, on):
        self.__on = on
            
