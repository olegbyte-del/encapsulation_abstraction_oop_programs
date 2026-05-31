# car video engine

import tkinter as tk
import os
import threading

class GIFPlayer:
    """IHandles loading nad looping GIF"""
    
    #initializing class for video playback
    def __init__(self, root):
        """Initialize constructor as well as parameters and specific directory of files"""
        
        self.window = tk.Toplevel(root)
        self.window.title("Car Speed")
        self.window.geometry("400x400")
        
        self.label = tk.Label(self.window)
        self.label.pack()
        
        self.root = self.window
        self.frames = []
        self.idx = 0
        self.job = None
        self._loading_path = None
        
        base = os.path.dirname(os.path.abspath(__file__))
        
        # Icon logo for the video
        self.logo_img = tk.PhotoImage(file=os.path.join(base, "controller_logo.png"))
        self.root.iconphoto(False, self.logo_img)
        
        # setting exact paths for gif files
        self.paths = {
            1: os.path.join(base, "car_not_moving.gif"),
            2: os.path.join(base, "car_moving.gif"),
            3: os.path.join(base, "car_fast.gif"),
            4: os.path.join(base, "flying.gif"),
            "brake": os.path.join(base, "car_brake.gif")
        }

    def load_gif(self, path, frame_index = 0, temp_frames = None): 
        """Extract all individual from the specified GIF file path"""

        if path != self._loading_path:
            return
        
        if temp_frames is None:
            temp_frames = []

        try:
            frame = tk.PhotoImage(file=path, format = f"gif -index {frame_index}")
            temp_frames.append(frame)
            self.root.after(0, lambda: self.load_gif(path, frame_index + 1, temp_frames))
        except:
            self.frames = temp_frames
            self.label.imgs = self.frames
            self.idx = 0
            self.loop()
        
    def loop(self):
        """Play gif based on car speed"""
        if not self.frames:
            return
        
        # loops the current gif that were selected
        self.label.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % len(self.frames)
        self.job = self.root.after(50, self.loop)
        
    def play(self, state):
        """Play gif based on car speed"""
        path = self.paths.get(state)
        if path:
            if self.job:
                self.root.after_cancel(self.job)
                self.job = None

            self.frames = []
            self._loading_path = path
            self.load_gif(path)
        