# Animal Information
import random
class Pet:
    """Class that store pet profile data"""

    def __init__(self, name = "", animal_type= "", age=0):
        """Initialize pet instance variables and generate a random 4 digit code"""
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__id_number = f"PET-{random.randint(1000, 9999)}"
    
    # Setter
    def set_age(self, age):
        """Validates pet age if negative is input"""
        try:
            if age < 0:
                print("Age cannot be less than zero!",
                    "Setting age to N/A", sep = "\n")
                self.__age = "N/A"
            else:
                self.__age = age
        except Exception as e:
            print('Error Occured')
    
    def set_animal_type(self, animal_type):
        """Set pets animal type"""
        self.__animal_type = animal_type
    
    def set_name(self, name):
        """set pet name and automatically formatting the name"""
        self.__name = name.title()
    
    # Getter
    def get_name(self):
        """Retrieves name"""
        return self.__name 
    
    def get_animal_type(self):
        """Retrieves animal type"""
        return self.__animal_type
    
    def get_age(self):
        """Retrieves age"""
        return self.__age
    
    def get_id_number(self): 
        """Retrieves id number"""
        return self.__id_number