# Main Program

import tkinter as tk
from fan_remote_gui import FanRemoteGUI

def main():
    root = tk.Tk()
    remote = FanRemoteGUI(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
    

# Program Plan

# INSTRUCTIONS (Base Program)

# Create a Fan class with constants: SLOW=1, MEDIUM=2, FAST=3
# Private attributes: speed, on (default False), radius, color
# Constructor sets default values (SLOW, 5, blue, False)
# Include getters and setters for all attributes
# Create a test program that makes 2 Fan objects

# Fan 1: FAST, radius 10, yellow, on=True
# Fan 2: MEDIUM, radius 5, blue, on=False

# Display speed, radius, color, and on/off state for both

# IDEA (make use tkinter as a remote then ones click a gif or video runs)
# inspiration : ITS SO HOT IN THE PHILIPPINES 

# Use Tkinter GUI as a remote
# Add buttons for SLOW, MEDIUM, FAST
# Button changes fan speed
# Show fan animation (GIF/video) using csv
# Animation speed matches selected fan speed