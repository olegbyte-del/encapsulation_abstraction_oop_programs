# Gui Application for pet ID generator
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PetAppGui:
    
    def __init__(self, root):
        self.root = root 
        self.root.title("Pet ID Profile Generator")
        self.root.geometry("365x425")
        self.root.configure(bg="#DBA674")
        
        self.input_frame()
        
        self.image = None
        self.upload_image()
        
    def input_frame(self):
        input_frame = tk.LabelFrame(self.root,
            text = "Register Your pet".center(60),
            font = ("Cosmic Sans MS", 12, "bold"),
            padx=15,
            pady= 15,
            bg= "#D8C8C8"
        )
        input_frame.place(x=20, y=20, width=320, height=400)\
        
        tk.Label(input_frame, text = "Pet Name:", bg = "#FFFFFF").pack(anchor="w")
        self.pet_name = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.pet_name.pack(fill="x", pady=(0,10))
        
        tk.Label(input_frame, text="Animal Type:", bg="#FFFFFF").pack(anchor="w")
        self.entry_type = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.entry_type.pack(fill="x", pady=(0, 10))

        tk.Label(input_frame, text="Age (Years):", bg="#ffffff").pack(anchor="w")
        self.entry_age = tk.Entry(input_frame, font=("Cosmic Sans MS", 11))
        self.entry_age.pack(fill="x", pady=(0, 15))
        
        self.upload_button = tk.Button(
            self.input_frame, text = "🖼️ Upload Pet Photo (Optional)",
            command=self.upload_image, bg="#C5AF88", relief="flat"
        )
        self.upload_button.pack(fill="x", pady=(0, 20))