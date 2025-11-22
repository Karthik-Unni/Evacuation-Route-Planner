import numpy as np
from tkinter import messagebox

from .astar import astar
from .fire import spread_fire
from .gui import FireEvacGUI


class FireEvacController:
    def __init__(self, root, rows=15, cols=15):
        self.rows = rows
        self.cols = cols

        self.grid = np.zeros((rows, cols), dtype=int)
        self.fire = np.zeros((rows, cols), dtype=int)

        self.start = None
        self.goal = None
        self.path = []

        self.gui = FireEvacGUI(root, self)

    def handle_click(self, r, c, mode):
        if mode == "wall":
            self.grid[r][c] ^= 1

        elif mode == "fire":
            self.fire[r][c] ^= 1

        elif mode == "start":
            self.start = (r, c)

        elif mode == "goal":
            self.goal = (r, c)

        self.path = []

    def run_astar(self):
        if self.start is None or self.goal is None:
            messagebox.showerror("Error", "Select Start and Goal points.")
            return

        fire_spread = spread_fire(self.fire)
        path = astar(self.grid, fire_spread, self.start, self.goal)

        if path is None:
            messagebox.showerror("No Path", "No safe evacuation path found.")
        else:
            self.path = path

        self.gui.draw()

    def clear_path(self):
        self.path = []
        self.gui.draw()

    def clear_all(self):
        self.grid[:] = 0
        self.fire[:] = 0
        self.start = None
        self.goal = None
        self.path = []
        self.gui.draw()
