# video_engine

import tkinter as tk

class GIFPlayer:
    """Initialize animated GIF playback"""
    
    #initializing class for video playback
    def __init__(self, root):
        """Initialize constructor as well as parameters and specific directory of files"""
        
        self.window = tk.Toplevel(root)
        self.window.title("Fan Speed")
        self.window.geometry("400x400")
        
        self.label = tk.Label(self.window)
        self.label.pack()
        
        self.root = self.window
        self.frames = []
        self.idx = 0
        self.job = None
        
        # setting exact paths for gif files
        base = r"D:\PUP\First year - Second Semester\Object Oriented Programming\encapsulation_abstraction_oop_programs\fan_control_system_simulation\\"
        self.paths = {
            1: base + "low.gif",
            2: base + "medium.gif",
            3: base + "fast.gif",
            "off": base + "power off.gif"
        }
    
    def load_gif(self, path): 
        """ Extract all individual from the specified GIF file path"""
        
        self.frames = []
        file_index = 0
        
        while True:
            try:
                frame = tk.PhotoImage(file=path, format = f"gif -index {file_index}")
                self.frames.append(frame)
                file_index += 1
            except:
                break
            
    def loop(self):
        """Cycle through the GIF continously"""
        # loops the current gif that were selected
        self.label.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.job = self.root.after(50, self. loop)