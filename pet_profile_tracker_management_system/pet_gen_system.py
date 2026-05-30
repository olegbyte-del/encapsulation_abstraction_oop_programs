# Gui Application for pet ID generator
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class PetAppGui:
    
    def __init__(self, root):
        self.root = root 
        self.root.title("Pet ID Profile Generator")
        self.root.geometry("500x500")
        self.root.configure(bg="#DBA674")
        
    def input_frame(self):
        input_frame = tk.LabelFrame(self.root,
            text = "Register Your pet",
            font = ("Cosmic Sans MS", 12, "bold"),
            padx=15,
            pady= 15,
            bg= "#000000"
        )
        input_frame.place(x=20, y=20, width=320, height=400)