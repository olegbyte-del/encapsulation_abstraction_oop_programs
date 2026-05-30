# video_engine

import tkinter as tk

class GIFPlayer:
    def __init__(self, display_screen, clock_timer):
        self.label = display_screen
        self.root = clock_timer
        self.frames = []
        self.idx = 0
        self.job = None