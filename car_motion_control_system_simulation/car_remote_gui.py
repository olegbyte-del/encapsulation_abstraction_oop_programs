# Car remote gui

import tkinter as tk
from car_status import Car
from video_engine import GIFPlayer

class CarControllerGUI:

    def __init__(self, root):

        # Structure of the GUI
        self.root = root
        self.root.title("Car Controller")
        self.root.geometry("380x400")
        self.root.configure(bg="#74797D")
        
        # Icon logo for the controller
        try:
            self.logo_img = tk.PhotoImage(file=r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\car_motion_control_system_simulation\controller_logo.png")
            self.root.iconphoto(False, self.logo_img)
        except:
            pass
        
        # Initialize object Car from car_status
        self.fan = Car(2026, "Toyota Hilux")
        
        # initialize video_engine
        self.gif_player = GIFPlayer(self.root)
        
        # Screen Display
        self.screen_var = tk.StringVar(value="Speed: 0 km/h [Stopped]")
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
        
        # Button for Gas and brake side by side
        button_frame = tk.Frame(self.root, bg="#2A4D6F")
        button_frame.pack(pady=20)
        
        self.gas_button = tk.Button(
            self.root, 
            text="GAS",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            bg="#1CA23B",
            fg="white",
            activebackground="#0E5A1F",
            activeforeground="white",
            command=self.accelerate_car
        )
        self.gas_button.pack(pady=15)

        brake_button = tk.Button(self.root,
            text = "Brake",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            bg="#EC1B1B",
            fg="white",
            activebackground="#840F0F",
            activeforeground="white",
            command = self.brake_car
        )
        brake_button.pack(side="left", padx=10)
        
        self.update_car_display()

    # accelerate the car
    def accelerate_car(self):
        """Accelerate the car by +5 km/h"""
        self.car.accelerate()
        print(f"Current Speed: {self.car.get_speed()} km/h")
        self.update_car_display()
        
    # Brake the car 
    def brake_car(self):
        """brake the car by -5 km/h"""
        self.car.brake()
        print(f"Current Speed: {self.car.get_speed()} km/h")
        self.update_car_display()
        
    def update_car_display(self):
        speed = self.car.get_speed()
        
        if speed == 0:
            self.screen_var.set(f"Speed: {speed} km/h\n")
            self.gif_player.play("")  
            
        elif 5 <= speed <= 25:
            self.screen_var.set(f"Speed: {speed} km/h\n")
            self.gif_player.play("")   
            
        elif 30 <= speed <= 55:
            self.screen_var.set(f"Speed: {speed} km/h\n")
            self.gif_player.play("")     
        else:
            self.screen_var.set(f"Speed: {speed} km/h\n")
            self.gif_player.play("")  