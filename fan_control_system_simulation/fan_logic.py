# Fan Logic

class Fan:
    """Contains information of the fan speed, radius, color, and power state"""
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=None, radius = 10.0, color="white", on=False):
        """Initialize fan attributes"""
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = color
        self.__on = on
        
    @property # getter
    def speed(self):
        """reads fan speed"""
        return self.__speed
        
    @speed.setter
    def speed(self, new_speed): 
        """condition for the attribute speed to only slow, medium, and fast"""
        if new_speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = new_speed
        
    @property
    def radius(self):
        """reads radius attribute"""
        return self.__radius
        
    @radius.setter
    def radius(self, radius):
        """condition for fan radius to fixed value"""
        self.__radius = radius
        
    @property
    def color(self):
        """reads the color attribute"""
        return self.__color

    @color.setter
    def color(self, color):
        """This means that color is only this value given"""
        self.__color = color
        
    @property
    def on(self):
        """reads the on attribute"""
        return self.__on
        
    @on.setter
    def on(self, on):
        """This means that on is only this value given"""
        self.__on = on
            
