# Fan Remote

import tkinter as tk
from fan_logic import Fan

class FanRemoteGUI:
    def __init__(self, root):
        # Structure of the GUI
        self.root = root
        self.root.title("Fan Remote")
        self.root.geometry("300x500")
        self.root.configure(bg="#2A4D6F")
        
        # Icon logo for the remote
        self.logo_img = tk.PhotoImage(file=r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\fan_control_system_simulation\remote.png")
        self.root.iconphoto(False, self.logo_img)
        
        # Initialize object fan from fan_logic
        self.fan = Fan()
        
        # Screen Display
        self.screen_var = tk.StringVar(value="Fan off")
        self.screen = tk.Label(
            self.root, 
            textvariable=self.screen_var, 
            font=("Arial", 16, "bold"), 
            bg="#FDFDFD", 
            fg="#414141", 
            height=2, 
            width=20, 
            relief="sunken", 
            bd=4
        ) 
        self.screen.pack(pady=25)
        
        # Buttons for the speeds
        mode = {1: "1 Low", 2: "2 Medium", 3: "3 High"}
        
        for speed, speed_status in mode.items():
            button = tk.Button(self.root
                text = speed_status
                font=("Arial", 12, "Bold")
                width=20,
                height=3,
                action = lambda s=speed: self.set_fan_speed(s)
            ) btn.pack(pady=6)
        
        