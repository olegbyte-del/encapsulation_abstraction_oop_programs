# main program

# REQUIRED INSTRUCTIONS (Base Program)

# Create a Car class with private attributes: __year_model, __make, __speed (starts at 0)
# Constructor sets year_model and make, speed starts at 0
# Methods:
# accelerate() → +5 speed
# brake() → -5 speed
# get_speed() → return speed
# Test program:
# Create 1 Car object
# Call accelerate 5 times and print speed each time
# Call brake 5 times and print speed each time

# IDEA
# SORRY I WANT TO CREATE SOMETHING NA PAMPAGOODVIBES 

# Use Tkinter as a control panel
# Speed controls video output:
# High speed → fast driving car video
# Brake → stopping car meme video
# Very high speed → flying/losing control meme video
# Videos change based on current speed value

import tkinter as tk
from car_remote_gui import CarControllerGUI

def main():
    """start the Car application"""
    root = tk.Tk()
    remote = CarControllerGUI(root)
    
    root.mainloop()

if __name__ == "__main__":
    """runs the program"""
    main()
    