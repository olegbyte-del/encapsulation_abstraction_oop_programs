# Main Program

import tkinter as tk
from pet_gen_system import PetAppGui

# REQUIRED INSTRUCTIONS (Base Program)
# Create a Pet class with private attributes:
# __name
# __animal_type
# __age
# Constructor initializes all attributes
# Methods:
# set_name(), set_animal_type(), set_age()
# get_name(), get_animal_type(), get_age()
# Test program:
# Create a Pet object
# Input from user:
# name
# animal type
# age
# Store values using setters
# Display values using getters

# IDEA
# INSPIRATION: NAWALA PO ID KO HAHAHHAHAHA 
# Use Tkinter to create a Pet Profile ID System
# User inputs:
# name
# animal type
# age
# image upload (optional)
# Program generates a simple pet ID card/profile
# shows pet details
# displays uploaded image
# assigns a generated ID (example: PET-001)
# Output becomes a “pet profile generator” instead of just console input/output

def main():
    root = tk.Tk()
    app = PetAppGui(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()