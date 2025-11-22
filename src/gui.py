import tkinter as tk
from tkinter import messagebox

CELL_SIZE = 35

class FireEvacGUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("🔥 Fire Evacuation Planner (A*)")

        self.mode = tk.StringVar(value="wall")

        self.canvas = tk.Canvas(
            root,
            width=controller.cols * CELL_SIZE,
            height=controller.rows * CELL_SIZE,
            bg="white"
        )
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.canvas.bind("<Button-1>", self.on_click)

        tk.Button(root, text="Wall", command=lambda: self.set_mode("wall")).grid(row=1, column=0, sticky="ew")
        tk.Button(root, text="Fire", command=lambda: self.set_mode("fire")).grid(row=1, column=1, sticky="ew")
        tk.Button(root, text="Start", command=lambda: self.set_mode("start")).grid(row=1, column=2, sticky="ew")
        tk.Button(root, text="Goal", command=lambda: self.set_mode("goal")).grid(row=1, column=3, sticky="ew")

        tk.Button(root, text="Run A*", command=self.controller.run_astar).grid(row=2, column=0, columnspan=2, sticky="ew")
        tk.Button(root, text="Clear Path", command=self.controller.clear_path).grid(row=2, column=2, sticky="ew")
        tk.Button(root, text="Clear All", command=self.controller.clear_all).grid(row=2, column=3, sticky="ew")

        self.status = tk.Label(root, text="Mode: Wall")
        self.status.grid(row=3, column=0, columnspan=4)

        self.draw()

    def set_mode(self, mode):
        self.mode.set(mode)
        self.status.config(text=f"Mode: {mode.capitalize()}")

    def on_click(self, event):
        r = event.y // CELL_SIZE
        c = event.x // CELL_SIZE

        self.controller.handle_click(r, c, self.mode.get())
        self.draw()

    def draw(self):
        self.canvas.delete("all")

        grid = self.controller.grid
        fire = self.controller.fire
        path = self.controller.path
        start = self.controller.start
        goal = self.controller.goal

        for r in range(self.controller.rows):
            for c in range(self.controller.cols):
                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "white"

                if grid[r][c] == 1: color = "black"
                if fire[r][c] == 1: color = "red"
                if (r, c) in path:  color = "blue"
                if start == (r, c): color = "green"
                if goal == (r, c):  color = "yellow"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
