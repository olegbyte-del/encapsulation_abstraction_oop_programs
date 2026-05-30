# Animal Information
import random
class Pet:

    def __init__(self, name = "", animal_type= "", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        self.__id_number = f"PET-{random.randint(1000, 9999)}"
    
    # Setter
    def set_age(self, age):
        try:
            if age < 0:
                print("Age cannot be less than zero!",
                    "Setting age to N/A", sep = "\n")
        except Exception as e:
            print('Error Occured')
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_name(self, name):
        self.__name = name.title()
    
    # Getter
    def get_name(self):
        return self.__name 
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def get_id_number(self): 
        return self.__id_number