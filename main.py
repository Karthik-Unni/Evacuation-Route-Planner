from src.app import FireEvacController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = FireEvacController(root, rows=15, cols=15)
    root.mainloop()
