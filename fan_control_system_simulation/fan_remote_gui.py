# Fan Remote

import tkinter as tk
from fan_logic import Fan

class FanRemoteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fan Remote")
        self.root.geometry("500x500")
        self.root.configure(bg="#2C5E90")
        
        self.fan = Fan()
        
        self.screen_var = tk.StringVar()