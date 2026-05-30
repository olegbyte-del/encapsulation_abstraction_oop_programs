# video_engine

import tkinter as tk
import os
import threading

class GIFPlayer:
    """IHandles loading nad looping GIF"""
    
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
        
        base = os.path.dirname(os.path.abspath(__file__))
        
        # Icon logo for the video
        self.logo_img = tk.PhotoImage(file=os.path.join(base, "remote.png"))
        self.root.iconphoto(False, self.logo_img)
        
        # setting exact paths for gif files
        self.paths = {
            1: os.path.join(base, "low.gif"),
            2: os.path.join(base, "medium.gif"),
            3: os.path.join(base, "fast.gif"),
            "off": os.path.join(base, "power_off.gif")
        }

    def load_gif(self, path): 
        """Extract all individual from the specified GIF file path"""

        if self.job:
            self.root.after_cancel(self.job)
            self.job = None
            
        temp_frames = []
        file_index = 0
        self.idx = 0
        
        while True:
            try:
                frame = tk.PhotoImage(file=path, format = f"gif -index {file_index}")
                temp_frames.append(frame)
                file_index += 1
            except:
                break
        
        self.frames =temp_frames
        self.label.imgs = self.frames
        
    def loop(self):
        """Cycle through the GIF continously"""
        if not self.frames:
            return
        
        # loops the current gif that were selected
        self.label.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.job = self.root.after(50, self.loop)
        
    def play(self, state):
        """Play gif based on fan speed"""
        path = self.paths.get(state)
        if path:
            def load_then_play():
                self.load_gif(path)
                self.root.after(0, self.loop)
            threading.Thread(target=load_then_play, daemon=True).start()