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
        
        