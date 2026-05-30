# Animal Information

class Pet:

    def __init__(self, name = "", animal_type= "", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
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
                
            
    