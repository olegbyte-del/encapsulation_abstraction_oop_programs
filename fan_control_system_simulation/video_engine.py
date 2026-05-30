# video_engine

import tkinter as tk

class GIFPlayer:
    #initializing class for video playback
    def __init__(self, display_screen, clock_timer):
        self.label = display_screen
        self.root = clock_timer
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
        self.frames = []
        file_index = 0
        
        while True:
            Try:
                frame = tk.PhotoImage(file=self.path, format = f"gif -index {file_index}")
                self.frames.ppend(frame)
                file_index += 1
            except:
                break
            
    def loop(self):
        # loops the current gif that were selected
        self.label.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.job = self.root.after(50, self. loop)