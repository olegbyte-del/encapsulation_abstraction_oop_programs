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