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
        """Read fan speed"""
        return self.__speed
        
    @speed.setter
    def speed(self, new_speed): 
        """cCondition for the attribute speed to be only slow, medium, or fast"""
        if new_speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = new_speed
        
    @property
    def radius(self):
        """Read radius attribute"""
        return self.__radius
        
    @radius.setter
    def radius(self, radius):
        """Condition for fan radius to be a fixed value"""
        self.__radius = radius
        
    @property
    def color(self):
        """Read the color attribute"""
        return self.__color

    @color.setter
    def color(self, color):
        """Set the fan color attribute"""
        self.__color = color
        
    @property
    def on(self):
        """Read the power state on attribute"""
        return self.__on
        
    @on.setter
    def on(self, on):
        """Set the fan power state attribute"""
        self.__on = on
            
